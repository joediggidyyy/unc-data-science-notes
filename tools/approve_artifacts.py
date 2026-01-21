"""Approve high-risk artifacts for this repo by pinning them in a manifest.

Purpose
- Images (and other flagged binaries) are WARNed by the validator because they
  require manual privacy review.
- Once CodeSentinel review approves an artifact, we record it in a whitelist
  pinned by SHA256 so it won't warn again unless the file changes.

Default manifest: approved_artifacts.json (repo root)

Usage
  python tools/approve_artifacts.py --path notes/.../image.png
  python tools/approve_artifacts.py --category image --path notes/.../image.png --note "Reviewed"
    python tools/approve_artifacts.py --category image --all-images --under notes --note "Reviewed"
  python tools/approve_artifacts.py --remove --path notes/.../image.png
  python tools/approve_artifacts.py --list

Interactive (new/unapproved images)
    python tools/approve_artifacts.py --interactive
    python tools/approve_artifacts.py --list-new-images
    python tools/approve_artifacts.py --approve-all-new-images --note "Reviewed"

Standard-library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


DEFAULT_MANIFEST = "approved_artifacts.json"


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


def _load_unapproved_images_from_compliance_report(*, repo_root: Path, report_path: Path) -> List[str]:
    """Return repo-relative paths for images requiring manual review.

    Matches the validator finding used across this repo:
      severity=WARNING and message="Image file present; manual privacy review required."
    """

    if not report_path.exists() or not report_path.is_file():
        return []

    try:
        data = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return []

    findings = data.get("findings")
    if not isinstance(findings, list):
        return []

    hits: List[str] = []
    for f in findings:
        if not isinstance(f, dict):
            continue
        if f.get("severity") != "WARN":
            continue
        if f.get("message") != "Image file present; manual privacy review required.":
            continue

        path = f.get("path")
        if not isinstance(path, str) or not path:
            continue

        if not path.lower().endswith(tuple(IMAGE_EXTENSIONS)):
            continue

        try:
            if not (repo_root / path).exists():
                continue
        except OSError:
            continue

        hits.append(path)

    out: List[str] = []
    seen: set[str] = set()
    for p in hits:
        if p in seen:
            continue
        seen.add(p)
        out.append(p)
    return out


def _confirm_bulk_approval() -> bool:
    print("\n[approve] WARNING: Bulk-approving images can publish private content.")
    print("[approve] Only proceed if you have already manually reviewed ALL images.")
    phrase = input("Type APPROVE_ALL to continue: ").strip()
    return phrase == "APPROVE_ALL"


def _prompt_action(*, count: int) -> str:
    print("\n[approve] Unapproved images detected.")
    print(f"[approve] Count: {count}")
    print("\nChoose an action:")
    print("  1) Approve ALL new images (requires confirmation; unsafe)")
    print("  2) List new images")
    print("  3) Review one-by-one")
    print("  4) Quit")
    while True:
        choice = input("Selection [1-4]: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256_file(path: Path, *, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _safe_relpath(repo_root: Path, path: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except Exception:
        # Fall back to best-effort normalization
        return path.as_posix().replace("\\", "/")


def _load_manifest(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"version": 1, "approved": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"version": 1, "approved": {}}

    if not isinstance(data, dict):
        return {"version": 1, "approved": {}}

    approved = data.get("approved")
    if not isinstance(approved, dict):
        approved = {}

    return {"version": int(data.get("version", 1) or 1), "approved": approved}


def _write_manifest(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _iter_files_under(repo_root: Path, under: Path) -> List[Path]:
    base = (repo_root / under).resolve() if not under.is_absolute() else under.resolve()
    if not base.exists() or not base.is_dir():
        raise SystemExit(f"Not a directory: {under}")
    return [p for p in base.rglob("*") if p.is_file()]


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Approve high-risk artifacts by pinning them in approved_artifacts.json")
    ap.add_argument("--repo-root", default=None, help="Repo root (default: parent of this tools/ directory)")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST, help="Manifest filename (relative to repo root)")
    ap.add_argument(
        "--category",
        default="image",
        choices=["image", "document", "presentation", "other"],
        help="Approval category for entries",
    )
    ap.add_argument("--note", default=None, help="Optional note to store with the approval")
    ap.add_argument("--path", action="append", default=[], help="Repo-relative path to approve (repeatable)")
    ap.add_argument(
        "--under",
        default=None,
        help="Approve/remove files under this directory (repo-relative) (used with --all-images)",
    )
    ap.add_argument(
        "--all-images",
        action="store_true",
        help="Approve/remove all image files under --under (defaults to notes/ if omitted)",
    )
    ap.add_argument("--remove", action="store_true", help="Remove approval entries for the given paths")
    ap.add_argument("--list", action="store_true", help="List approved entries (paths only)")

    ap.add_argument(
        "--compliance-report",
        default="reports/compliance_report.json",
        help="Path (repo-relative) to the compliance report JSON used to detect unapproved images",
    )
    ap.add_argument(
        "--list-new-images",
        action="store_true",
        help="List NEW (currently unapproved) images found in the latest compliance report.",
    )
    ap.add_argument(
        "--approve-all-new-images",
        action="store_true",
        help="Approve all NEW (currently unapproved) images found in the latest compliance report (unsafe; requires confirmation).",
    )
    ap.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive review menu for NEW (currently unapproved) images found in the latest compliance report.",
    )
    args = ap.parse_args(argv)

    repo_root = (
        Path(args.repo_root).expanduser().resolve()
        if args.repo_root
        else Path(__file__).resolve().parents[1]
    )

    manifest_path = repo_root / args.manifest
    manifest = _load_manifest(manifest_path)
    approved: Dict[str, Any] = dict(manifest.get("approved") or {})

    if args.list:
        for k in sorted(approved.keys()):
            print(k)
        return 0

    # New/unapproved image workflow (driven by latest compliance report)
    if args.list_new_images or args.approve_all_new_images or args.interactive:
        report_path = (repo_root / str(args.compliance_report)).resolve()
        unapproved_images = _load_unapproved_images_from_compliance_report(
            repo_root=repo_root,
            report_path=report_path,
        )

        if args.list_new_images:
            if not unapproved_images:
                return 0
            for p in unapproved_images:
                print(p)
            return 0

        to_approve: List[str] = []
        if args.approve_all_new_images:
            if not unapproved_images:
                return 0
            if not (sys.stdin.isatty() and sys.stdout.isatty()):
                raise SystemExit("Refusing bulk approval in a non-interactive session")
            if not _confirm_bulk_approval():
                return 0
            to_approve = list(unapproved_images)
        elif args.interactive:
            if not (sys.stdin.isatty() and sys.stdout.isatty()):
                raise SystemExit("Interactive mode requires a TTY")
            if not unapproved_images:
                print("[approve] No new (unapproved) images found.")
                return 0

            choice = _prompt_action(count=len(unapproved_images))
            if choice == "4":
                return 0
            if choice == "2":
                for p in unapproved_images:
                    print(p)
                return 0
            if choice == "1":
                if _confirm_bulk_approval():
                    to_approve = list(unapproved_images)
                else:
                    return 0
            else:
                approved_now: List[str] = []
                for i, p in enumerate(unapproved_images, start=1):
                    print(f"\n[approve] ({i}/{len(unapproved_images)}) Review: {p}")
                    ans = input("Approve this image? [y]es/[n]o/[q]uit: ").strip().lower()
                    if ans == "q":
                        break
                    if ans in {"y", "yes"}:
                        approved_now.append(p)
                to_approve = approved_now

        # Fall through to the normal approval logic with explicit paths.
        args.category = "image"
        if not to_approve:
            return 0
        args.path = list(args.path) + to_approve

    # Expand bulk selection into explicit paths.
    explicit_paths: List[str] = list(args.path)
    if args.all_images:
        under = Path(args.under) if args.under else Path("notes")
        files = _iter_files_under(repo_root, under)
        for p in files:
            if p.suffix.lower() in IMAGE_EXTENSIONS:
                explicit_paths.append(_safe_relpath(repo_root, p))

    if not explicit_paths:
        ap.error("--path is required unless --list is used (or use --all-images)")

    changed = False

    for raw in explicit_paths:
        p = (repo_root / raw).resolve()
        if not p.exists() or not p.is_file():
            raise SystemExit(f"Not a file: {raw}")

        rel = _safe_relpath(repo_root, p)

        if args.remove:
            if rel in approved:
                approved.pop(rel, None)
                changed = True
            continue

        sha = _sha256_file(p)
        entry: Dict[str, Any] = {
            "sha256": sha,
            "category": args.category,
            "approved_utc": _utc_now(),
        }
        if args.note:
            entry["notes"] = args.note

        approved[rel] = entry
        changed = True

    if changed:
        out = dict(manifest)
        out["approved"] = approved
        _write_manifest(manifest_path, out)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
