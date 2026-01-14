"""Validate a public notes repository for common public-sharing risk areas.

This is a *best-effort*, conservative scanner. It cannot prove compliance.

Focus areas:
- Academic integrity risks: plagiarism signals, "answer key" / "solution" leakage,
  exam/test content, unauthorized collaboration cues
- Privacy risks: personal contact info (emails, phone numbers)
- Potentially sensitive binaries: images and presentations (manual review required)

This validator supports an approval manifest (default: approved_artifacts.json)
to record CodeSentinel-reviewed artifacts (especially images). Approved items are
pinned by SHA256; if the file changes, it must be re-approved.

Reference guidance:
- Consult your institution's academic integrity / conduct policies.
- If you're unsure whether sharing something is allowed, do not publish it.

Usage:
    python tools/validate_notes_repo.py --path <repo_root>
    python tools/validate_notes_repo.py --path <repo_root> --strict

Exit codes:
- 0: PASS (no ERROR findings; WARN findings allowed unless --strict)
- 1: WARN treated as failure (--strict)
- 2: ERROR findings
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Dict, Iterable, List, Optional, Pattern, Set, Tuple


@dataclass(frozen=True)
class Finding:
    severity: str  # ERROR | WARN | INFO
    path: str
    message: str
    hint: Optional[str] = None


def _mask_email(value: str) -> str:
    # Keep domain shape, hide most of the local-part.
    if "@" not in value:
        return value
    local, domain = value.split("@", 1)
    if not local:
        return f"***@{domain}"
    keep = local[:1]
    return f"{keep}***@{domain}"


def _mask_phone(value: str) -> str:
    digits = re.sub(r"\D+", "", value)
    if len(digits) < 4:
        return "***"
    return f"***-***-{digits[-4:]}"


TEXT_EXTENSIONS: Set[str] = {".md", ".txt", ".rst"}
BROAD_TEXT_EXTENSIONS: Set[str] = {".md", ".txt", ".rst", ".ipynb", ".jl", ".py"}
PRESENTATION_RISK_EXTENSIONS: Set[str] = {".ppt", ".pptx", ".key"}
DOCUMENT_BINARY_EXTENSIONS: Set[str] = {".pdf", ".doc", ".docx"}

# Heuristic patterns (keep intentionally small and explainable)
PATTERNS: List[Tuple[str, Pattern[str], str, str]] = [
    (
        "ERROR",
        re.compile(r"\b(answer\s*key|official\s*solutions?|solutions?\s*manual)\b", re.I),
        "Possible answer key / solutions content.",
        "Remove it unless explicitly permitted for public sharing.",
    ),
    (
        "WARN",
        re.compile(r"\b(midterm|final\s*exam|exam\s*questions?|test\s*questions?)\b", re.I),
        "Possible exam/test content reference.",
        "Avoid posting assessment questions/answers or details from recent assessments.",
    ),
    (
        "WARN",
        re.compile(r"\b(canvas\s*grade|gradebook|student\s*id|pid\b)\b", re.I),
        "Possible grade/identifier reference.",
        "Ensure no student records or identifiers are included.",
    ),
]

EMAIL_RE: Pattern[str] = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE_RE: Pattern[str] = re.compile(r"\b(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b")

# Images are allowed only when they are not screenshots of private content.
# We cannot OCR, so we flag images for manual review and apply stricter checks
# on filenames that suggest email/grades.
IMAGE_EXTENSIONS: Set[str] = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
SUSPICIOUS_IMAGE_NAME_RE: Pattern[str] = re.compile(r"(email|inbox|gmail|outlook|canvas|grade|roster|student|pid|id)", re.I)

DEFAULT_EXCLUDES: Set[str] = {
    ".git",
    ".agent_session",
    ".venv",
    ".venv_313",
    ".venv_314",
    ".venv-core",
    "local_untracked",
    "node_modules",
    "__pycache__",
    ".ruff_cache",
    "logs",
    "quarantine_legacy_archive",
    "archive",
    "temp",
    "reports",
}


APPROVAL_MANIFEST_DEFAULT = "approved_artifacts.json"

CONTENT_ROOTS: Set[str] = {
    # Primary publishable content
    "notes",
    # Optional content areas
    "assets",
    "glossary",
    "index",
}

EXPORT_ROOTS: Set[str] = {
    # Generated artifacts (optional to commit; often published as release assets)
    "exports",
}


def is_under_roots(root: Path, path: Path, roots: Set[str]) -> bool:
    try:
        rel = path.relative_to(root)
    except Exception:
        return False
    return bool(rel.parts) and rel.parts[0] in roots


def should_apply_integrity_patterns(root: Path, path: Path) -> bool:
    """Return True when academic-integrity keyword heuristics should be applied.

    Rationale: repo policy/docs necessarily *mention* prohibited concepts (exam, answer key,
    student id). We only want to run those heuristics on publishable content areas.
    """

    return is_under_roots(root, path, CONTENT_ROOTS)


def iter_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        # In-place prune
        dirnames[:] = [d for d in dirnames if d not in DEFAULT_EXCLUDES]
        for fn in filenames:
            yield Path(dirpath) / fn


def read_text_safely(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Try a permissive decode; if it still looks binary, skip
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return None
    except Exception:
        return None


def add_finding(
    root: Path,
    findings: List[Finding],
    severity: str,
    path: Path,
    message: str,
    hint: Optional[str] = None,
) -> None:
    try:
        rel_path = path.relative_to(root).as_posix()
    except Exception:
        rel_path = path.as_posix()
    findings.append(
        Finding(
            severity=severity,
            path=str(rel_path),
            message=message,
            hint=hint,
        )
    )


def _sha256_file(path: Path, *, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _safe_relpath(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except Exception:
        return path.as_posix().replace("\\", "/")


def _load_approval_manifest(root: Path, *, manifest_path: Optional[Path] = None) -> Dict[str, Any]:
    """Load the approval manifest.

    Format:
      {
        "version": 1,
        "approved": {
          "notes/.../image.png": {
            "sha256": "...",
            "category": "image",
            "approved_utc": "...",
            "notes": "..." (optional)
          }
        }
      }
    """

    mp = manifest_path or (root / APPROVAL_MANIFEST_DEFAULT)
    if not mp.exists():
        return {"version": 1, "approved": {}}
    try:
        data = json.loads(mp.read_text(encoding="utf-8"))
    except Exception:
        return {"version": 1, "approved": {}}

    if not isinstance(data, dict):
        return {"version": 1, "approved": {}}

    approved = data.get("approved")
    if not isinstance(approved, dict):
        approved = {}
    return {"version": int(data.get("version", 1) or 1), "approved": approved}


def _is_approved(
    *,
    root: Path,
    path: Path,
    sha256: str,
    approvals: Dict[str, Any],
) -> Tuple[bool, Optional[str]]:
    """Return (is_approved, reason_if_not).

    Approvals are keyed by repo-relative POSIX paths and pinned by SHA256.
    """

    rel = _safe_relpath(root, path)
    entry = approvals.get(rel)
    if entry is None:
        return False, "not listed"
    if not isinstance(entry, dict):
        return False, "invalid entry"
    expected = entry.get("sha256")
    if not expected or not isinstance(expected, str):
        return False, "missing sha256"
    if expected.lower() != sha256.lower():
        return False, "sha256 mismatch"
    return True, None


def validate_required_files(root: Path, findings: List[Finding]) -> None:
    required = [
        "README.md",
        "COMPLIANCE.md",
        "LICENSE.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
    ]
    for rel in required:
        p = root / rel
        if not p.exists():
            add_finding(
                root,
                findings,
                "WARN",
                p,
                f"Missing recommended file: {rel}",
                "Add it to make expectations explicit for public readers.",
            )
        else:
            # Basic sanity check
            try:
                if p.is_file() and p.stat().st_size == 0:
                    add_finding(root, findings, "WARN", p, f"File is empty: {rel}")
            except Exception:
                pass


def validate_text_file(
    root: Path,
    path: Path,
    text: str,
    findings: List[Finding],
    *,
    apply_integrity_patterns: bool,
) -> None:
    # PII heuristics: emails and phone-like strings are disallowed for this repo.
    m = EMAIL_RE.search(text)
    if m:
        add_finding(
            root,
            findings,
            "ERROR",
            path,
            f"Found an email address: {_mask_email(m.group(0))}",
            "Remove email addresses from tracked content.",
        )

    m = PHONE_RE.search(text)
    if m:
        add_finding(
            root,
            findings,
            "ERROR",
            path,
            f"Found a phone-number-like string: {_mask_phone(m.group(0))}",
            "Remove phone numbers from tracked content.",
        )

    if apply_integrity_patterns:
        for severity, pattern, msg, hint in PATTERNS:
            if pattern.search(text):
                add_finding(root, findings, severity, path, msg, hint)


def validate_repo(root: Path, *, approvals: Optional[Dict[str, Any]] = None) -> List[Finding]:
    findings: List[Finding] = []

    if not root.exists() or not root.is_dir():
        return [Finding("ERROR", ".", "Path does not exist or is not a directory.")]

    validate_required_files(root, findings)

    manifest = _load_approval_manifest(root)
    approved_map: Dict[str, Any] = dict(manifest.get("approved") or {})
    if approvals is not None:
        # Allow callers/tests to inject/override approvals.
        approved_map = approvals

    for path in iter_files(root):
        # Do not scan the validator itself for integrity keywords.
        if path.name == Path(__file__).name:
            continue

        suffix = path.suffix.lower()

        # Flag images for manual review unless explicitly approved in the manifest.
        # NOTE: If an image is approved, it should not fail in strict mode.
        if suffix in IMAGE_EXTENSIONS:
            try:
                sha = _sha256_file(path)
            except Exception:
                sha = ""

            is_ok, reason = _is_approved(root=root, path=path, sha256=sha, approvals=approved_map)
            if is_ok:
                add_finding(
                    root,
                    findings,
                    "INFO",
                    path,
                    "Image present and approved (pinned by SHA256).",
                    "No further scrutiny required unless the file changes.",
                )
            else:
                if SUSPICIOUS_IMAGE_NAME_RE.search(path.name):
                    add_finding(
                        root,
                        findings,
                        "ERROR",
                        path,
                        "Image filename suggests it may contain private info (email/grades/roster).",
                        "Do not store screenshots of email/Canvas/grades in the repository unless reviewed and approved.",
                    )
                else:
                    add_finding(
                        root,
                        findings,
                        "WARN",
                        path,
                        "Image file present; manual privacy review required.",
                        "If approved by CodeSentinel, add it to approved_artifacts.json so it won't warn again.",
                    )
            continue

        # Binary formats:
        # - Presentations are higher risk for redistribution (often instructor decks).
        # - PDF/DOCX are allowed for a notes repo, but should be reviewed for privacy.
        if suffix in PRESENTATION_RISK_EXTENSIONS:
            sev = "INFO" if is_under_roots(root, path, EXPORT_ROOTS) else "WARN"
            # If explicitly approved, suppress WARN.
            try:
                sha = _sha256_file(path)
            except Exception:
                sha = ""
            is_ok, _reason = _is_approved(root=root, path=path, sha256=sha, approvals=approved_map)
            if is_ok:
                sev = "INFO"
            add_finding(
                root,
                findings,
                sev,
                path,
                f"Presentation file present: {suffix}",
                "If public, ensure this is your own work or you have permission to share it.",
            )
            continue

        if suffix in DOCUMENT_BINARY_EXTENSIONS:
            sev = "INFO" if is_under_roots(root, path, EXPORT_ROOTS) else "INFO"
            add_finding(
                root,
                findings,
                sev,
                path,
                f"Document file present: {suffix}",
                "If public, review for personal information before committing.",
            )
            continue

        if suffix in BROAD_TEXT_EXTENSIONS:
            text = read_text_safely(path)
            if text is None:
                add_finding(root, findings, "WARN", path, "Could not read text file reliably.")
                continue
            validate_text_file(
                root,
                path,
                text,
                findings,
                apply_integrity_patterns=should_apply_integrity_patterns(root, path),
            )

    return findings


def write_reports(root: Path, findings: List[Finding], report_dir: Path) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    errors = [f for f in findings if f.severity == "ERROR"]
    warns = [f for f in findings if f.severity == "WARN"]

    status = "PASS" if not errors and not warns else ("FAIL" if errors else "WARN")

    md_path = report_dir / "compliance_report.md"
    json_path = report_dir / "compliance_report.json"

    md_lines: List[str] = []
    md_lines.append("# Repository Compliance Report")
    md_lines.append("")
    md_lines.append(f"- Generated (UTC): `{now}`")
    md_lines.append("- Repository root: (omitted)")
    md_lines.append(f"- Status: **{status}**")
    md_lines.append(f"- Findings: {len(findings)} (ERROR={len(errors)}, WARN={len(warns)})")
    md_lines.append("")
    md_lines.append("## Scope")
    md_lines.append("")
    md_lines.append("This is an automated, best-effort scan for public-sharing risk indicators:")
    md_lines.append("- academic integrity leakage (solutions, exam content)")
    md_lines.append("- privacy/PII (emails, phone numbers)")
    md_lines.append("- potentially sensitive binaries (presentations, images)")
    md_lines.append("")
    md_lines.append("## Findings")
    md_lines.append("")

    if not findings:
        md_lines.append("No findings. [OK]")
    else:
        for f in findings:
            md_lines.append(f"- [{f.severity}] `{f.path}` — {f.message}")
            if f.hint:
                md_lines.append(f"  - hint: {f.hint}")

    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    json_payload = {
        "generated_utc": now,
        "root": None,
        "status": status,
        "counts": {"total": len(findings), "error": len(errors), "warn": len(warns)},
        "findings": [
            {"severity": f.severity, "path": f.path, "message": f.message, "hint": f.hint}
            for f in findings
        ],
        "notes": "Automated scan; indicates risk signals only.",
    }
    json_path.write_text(json.dumps(json_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(description="Validate a notes repo for common public-sharing risks.")
    ap.add_argument("--path", default=".", help="Repository root path")
    ap.add_argument("--strict", action="store_true", help="Fail on WARN findings as well as ERROR")
    ap.add_argument("--report-dir", default="reports", help="Directory (relative to root) to write compliance reports")
    args = ap.parse_args(argv)

    root = Path(args.path).resolve()
    findings = validate_repo(root)

    # Always write a sanitized compliance report.
    report_dir = root / args.report_dir
    write_reports(root, findings, report_dir)

    # Print a simple report (sanitized)
    errors = [f for f in findings if f.severity == "ERROR"]
    warns = [f for f in findings if f.severity == "WARN"]

    print("Notes Repo Validator")
    print("Root: (omitted)")
    print(f"Findings: {len(findings)} (ERROR={len(errors)}, WARN={len(warns)})")
    print("")

    for f in findings:
        print(f"[{f.severity}] {f.path}: {f.message}")
        if f.hint:
            print(f"        hint: {f.hint}")

    if errors:
        return 2
    if args.strict and warns:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
