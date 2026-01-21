"""Single-command maintenance wrapper for this notes repository.

This wrapper is intended to be the one simple command you run before publishing
(or before opening/merging PRs):

- Regenerate supporting documentation (indexes + change reports)
- Run conservative public-sharing content/compliance validation

Standard-library only.

Usage (from repo root):
  python maintain.py
  python maintain.py --dry-run --verbose
  python maintain.py --strict

Exit codes:
- 0: OK
- 1: validation WARN treated as failure (--strict)
- 2: validation ERROR
- 3: maintenance wrapper failure (unexpected)
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _write_text(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def _write_json(path: Path, payload: Dict[str, Any], dry_run: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", dry_run=dry_run)


def _safe_relpath(path: Path, repo_root: Path) -> str:
    """Render a repo-relative path for logs/reports (avoid absolute local paths)."""

    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except Exception:
        return path.name


def _missing_paths(paths: List[Path]) -> List[Path]:
    missing: List[Path] = []
    for p in paths:
        try:
            if not p.exists():
                missing.append(p)
        except OSError:
            missing.append(p)
    return missing


@dataclass(frozen=True)
class _ImageApprovalSelection:
    mode: str  # off | list | prompt | approve-all
    note: str


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Maintain the notes repo (docs + validation) in one command.")
    p.add_argument("--repo-root", default=None, help="Repo root path (default: directory containing this file)")
    p.add_argument("--dry-run", action="store_true", help="Compute changes but do not write any files")
    p.add_argument("--strict", action="store_true", help="Treat validator WARN findings as failures")
    p.add_argument("--verbose", action="store_true", help="Print verbose output")
    p.add_argument(
        "--scaffold-week-readmes",
        action="store_true",
        help="Create missing notes/<Term>/<Course>/<WeekXX>/README.md files (additive; never overwrites)",
    )
    p.add_argument(
        "--convert-assets",
        action="store_true",
        help="Run DOCX -> Markdown conversion under notes/ (best-effort; PDFs are kept as-is)",
    )
    p.add_argument(
        "--convert-force",
        action="store_true",
        help="When converting assets, overwrite existing generated Markdown outputs",
    )
    p.add_argument(
        "--pandoc-path",
        default=None,
        help="Optional explicit path to pandoc for --convert-assets (or set PANDOC_PATH)",
    )
    p.add_argument(
        "--front-matter",
        action="store_true",
        help="When converting assets, prepend YAML front-matter to generated Markdown",
    )
    p.add_argument("--skip-docs", action="store_true", help="Skip documentation generation")
    p.add_argument("--skip-validate", action="store_true", help="Skip compliance validation")

    p.add_argument(
        "--image-approval",
        choices=["off", "list", "prompt", "approve-all"],
        default="prompt",
        help=(
            "What to do when unapproved images are detected by the validator. "
            "'prompt' shows an interactive menu when a TTY is available; in CI/non-interactive sessions it behaves like 'list'."
        ),
    )
    p.add_argument(
        "--approve-all-new-images",
        action="store_true",
        help="Approve all NEW (currently unapproved) images found in the latest compliance report (unsafe; requires confirmation).",
    )
    p.add_argument(
        "--list-new-images",
        action="store_true",
        help="List NEW (currently unapproved) images found in the latest compliance report.",
    )
    p.add_argument(
        "--image-approval-note",
        default="Reviewed (maintain.py)",
        help="Note to store in approved_artifacts.json when approving images",
    )
    return p.parse_args(argv)


def _is_ci() -> bool:
    # Conservative detection: if a CI env var is present, never prompt.
    return bool(
        ("CI" in __import__("os").environ)
        or ("GITHUB_ACTIONS" in __import__("os").environ)
        or ("TF_BUILD" in __import__("os").environ)
    )


def _load_unapproved_images_from_compliance_report(*, repo_root: Path, report_path: Path) -> List[str]:
    """Return repo-relative paths for images requiring manual review.

    We define "new" images as those that the validator flagged as:
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

        # Ensure it's actually an image path.
        if not path.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            continue

        # Ensure it still exists.
        try:
            if not (repo_root / path).exists():
                continue
        except OSError:
            continue

        hits.append(path)

    # De-dup while preserving order.
    out: List[str] = []
    seen: set[str] = set()
    for p in hits:
        if p in seen:
            continue
        seen.add(p)
        out.append(p)
    return out


def _effective_image_approval(ns: argparse.Namespace) -> _ImageApprovalSelection:
    if bool(getattr(ns, "approve_all_new_images", False)):
        return _ImageApprovalSelection(mode="approve-all", note=str(ns.image_approval_note))
    if bool(getattr(ns, "list_new_images", False)):
        return _ImageApprovalSelection(mode="list", note=str(ns.image_approval_note))
    return _ImageApprovalSelection(mode=str(ns.image_approval), note=str(ns.image_approval_note))


def _prompt_image_approval_action(*, count: int) -> str:
    print("\n[maintain] Unapproved images detected.")
    print(f"[maintain] Count: {count}")
    print("\nChoose an action:")
    print("  1) Approve ALL new images (requires confirmation; unsafe)")
    print("  2) List new images")
    print("  3) Review one-by-one")
    print("  4) Skip")
    while True:
        choice = input("Selection [1-4]: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice


def _confirm_bulk_approval() -> bool:
    print("\n[maintain] WARNING: Bulk-approving images can publish private content.")
    print("[maintain] Only proceed if you have already manually reviewed ALL images.")
    phrase = input("Type APPROVE_ALL to continue: ").strip()
    return phrase == "APPROVE_ALL"


def _approve_images(
    *,
    repo_root: Path,
    image_paths: List[str],
    note: str,
    dry_run: bool,
    verbose: bool,
) -> Dict[str, Any]:
    details: Dict[str, Any] = {
        "count": len(image_paths),
        "note": note,
        "dry_run": bool(dry_run),
    }
    if not image_paths:
        return details

    if dry_run:
        if verbose:
            for p in image_paths:
                print(f"[maintain] would approve image: {p}")
        return details

    import tools.approve_artifacts as approve_artifacts

    args: List[str] = ["--repo-root", repo_root.as_posix(), "--category", "image", "--note", note]
    for p in image_paths:
        args.extend(["--path", p])

    rc = approve_artifacts.main(args)
    details["exit_code"] = rc
    return details


def _iter_docx_missing_md(notes_root: Path) -> List[Path]:
    """Find DOCX files under notes/ that are missing a sibling .md output.

    - Ignores Word lock/temp files (prefix '~$').
    - Output convention matches tools/convert_assets_to_markdown.py default (sibling .md).
    """

    missing: List[Path] = []
    try:
        candidates = notes_root.rglob("*.docx")
    except Exception:
        return missing

    for docx in candidates:
        try:
            if not docx.is_file():
                continue
        except OSError:
            continue

        # Word lock/temp file
        if docx.name.startswith("~$"):
            continue

        md = docx.with_suffix(".md")
        try:
            if not md.exists():
                missing.append(docx)
        except OSError:
            missing.append(docx)

    return missing


def main(argv: Optional[List[str]] = None) -> int:
    ns = _parse_args(argv)

    repo_root = Path(ns.repo_root).expanduser().resolve() if ns.repo_root else Path(__file__).resolve().parent
    reports_dir = repo_root / "reports"

    run_payload: Dict[str, Any] = {
        "generated_utc": _utc_now_iso(),
        "repo_root": None,
        "python": {
            "version": sys.version.split()[0],
            "executable": None,
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "options": {
            "dry_run": bool(ns.dry_run),
            "strict": bool(ns.strict),
            "scaffold_week_readmes": bool(ns.scaffold_week_readmes),
            "convert_assets": bool(ns.convert_assets),
            "convert_force": bool(ns.convert_force),
            "skip_docs": bool(ns.skip_docs),
            "skip_validate": bool(ns.skip_validate),
            "verbose": bool(ns.verbose),
        },
        "steps": [],
        "status": "UNKNOWN",
        "exit_code": None,
    }

    def step(name: str, status: str, details: Dict[str, Any]) -> None:
        run_payload["steps"].append({"name": name, "status": status, "details": details})

    try:
        if not repo_root.exists():
            raise FileNotFoundError(f"Repo root does not exist: {repo_root}")

        if ns.verbose:
            # Avoid printing absolute local paths (helps prevent accidental leaks
            # if terminal output is shared/screenshotted).
            print("[maintain] repo_root=(omitted)")
            print(f"[maintain] dry_run={ns.dry_run} strict={ns.strict}")

        # 1) Optional/auto asset conversion (dry-run -> preflight -> execution)
        notes_root = repo_root / "notes"
        docx_missing_md = _iter_docx_missing_md(notes_root)
        auto_convert = bool(docx_missing_md) and (not ns.convert_assets)
        should_convert = bool(ns.convert_assets) or auto_convert

        if not should_convert:
            step("convert", "SKIPPED", {})
        else:
            import tools.convert_assets_to_markdown as convert_assets_to_markdown

            base_args: List[str] = ["--repo-root", repo_root.as_posix()]
            if ns.verbose:
                base_args.append("--verbose")
            if ns.pandoc_path:
                base_args.extend(["--pandoc-path", str(ns.pandoc_path)])
            if ns.front_matter:
                base_args.append("--front-matter")
            # Safety default for public notes: generated Markdown should not contain emails.
            base_args.append("--redact-emails")
            if ns.convert_force:
                base_args.append("--force")

            convert_details: Dict[str, Any] = {
                "mode": "explicit" if ns.convert_assets else "auto_missing_docx_md",
                "missing_docx_md": len(docx_missing_md),
            }

            # 1a) Dry-run plan (always safe/no-write)
            rc_plan = convert_assets_to_markdown.main([*base_args, "--dry-run"])
            step("convert_plan", "OK" if rc_plan == 0 else "ERROR", {**convert_details, "exit_code": rc_plan})
            if rc_plan != 0:
                run_payload["status"] = "FAIL"
                run_payload["exit_code"] = 3 if rc_plan == 3 else rc_plan
                _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                return run_payload["exit_code"]

            # 1b) Preflight validation (tooling prerequisites)
            rc_pre = convert_assets_to_markdown.main([*base_args, "--preflight"])
            if rc_pre != 0 and auto_convert:
                # If auto-triggered, do not fail the whole wrapper just because pandoc isn't installed.
                # Record it and continue with docs/validation.
                step(
                    "convert_preflight",
                    "SKIPPED",
                    {**convert_details, "exit_code": rc_pre, "reason": "preflight failed (likely pandoc missing)"},
                )
                step("convert_execute", "SKIPPED", {**convert_details, "reason": "preflight failed"})
            else:
                step("convert_preflight", "OK" if rc_pre == 0 else "ERROR", {**convert_details, "exit_code": rc_pre})
                if rc_pre != 0:
                    run_payload["status"] = "FAIL"
                    run_payload["exit_code"] = 3 if rc_pre == 3 else rc_pre
                    _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                    _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                    return run_payload["exit_code"]

                # 1c) Execution (skipped if wrapper is in dry-run mode)
                if ns.dry_run:
                    step("convert_execute", "SKIPPED", {**convert_details, "reason": "wrapper dry-run"})
                else:
                    rc_exec = convert_assets_to_markdown.main(base_args)
                    step("convert_execute", "OK" if rc_exec == 0 else "ERROR", {**convert_details, "exit_code": rc_exec})
                    if rc_exec != 0:
                        run_payload["status"] = "FAIL"
                        run_payload["exit_code"] = 3 if rc_exec == 3 else rc_exec
                        _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                        _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                        return run_payload["exit_code"]

                    # If conversion was requested/auto-triggered due to missing outputs, verify the expected .md files exist.
                    if docx_missing_md:
                        still_missing: List[str] = []
                        for docx in docx_missing_md:
                            md = docx.with_suffix(".md")
                            try:
                                if not md.exists():
                                    still_missing.append(_safe_relpath(md, repo_root))
                            except OSError:
                                still_missing.append(_safe_relpath(md, repo_root))

                        if still_missing:
                            run_payload["status"] = "FAIL"
                            run_payload["exit_code"] = 3
                            step(
                                "convert_outputs",
                                "ERROR",
                                {**convert_details, "missing_outputs": still_missing},
                            )
                            _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                            _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                            return 3

        # 2) Docs generation (after conversion so indexes can include generated Markdown)
        if ns.skip_docs:
            step("docs", "SKIPPED", {})
        else:
            import tools.generate_repo_docs as generate_repo_docs

            rc_docs = generate_repo_docs.run(
                repo_root,
                dry_run=ns.dry_run,
                verbose=ns.verbose,
                scaffold_week_readmes=ns.scaffold_week_readmes,
            )

            docs_details: Dict[str, Any] = {"exit_code": rc_docs}
            if rc_docs == 0 and not ns.dry_run:
                expected_docs_outputs = [
                    repo_root / "notes" / "INDEX.md",
                    reports_dir / "repo_health_report.md",
                    reports_dir / "repo_inventory.json",
                    reports_dir / "repo_change_report.md",
                    reports_dir / "_repo_docs_state.json",
                ]
                missing = _missing_paths(expected_docs_outputs)
                if missing:
                    docs_details["missing_outputs"] = [_safe_relpath(p, repo_root) for p in missing]
                    rc_docs = 3
                    docs_details["effective_exit_code"] = 3

            step("docs", "OK" if rc_docs == 0 else "ERROR", docs_details)
            if rc_docs != 0:
                run_payload["status"] = "FAIL"
                run_payload["exit_code"] = 3
                _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                return 3

        # 3) Validation
        if ns.skip_validate:
            rc_val = 0
            step("validate", "SKIPPED", {})
        else:
            import tools.validate_notes_repo as validate_notes_repo

            val_args: List[str] = ["--path", repo_root.as_posix(), "--report-dir", "reports"]
            if ns.strict:
                val_args.append("--strict")
            rc_val = validate_notes_repo.main(val_args)

            validate_details: Dict[str, Any] = {"exit_code": rc_val}
            if rc_val in (0, 1) and not ns.dry_run:
                expected_validate_outputs = [
                    reports_dir / "compliance_report.md",
                    reports_dir / "compliance_report.json",
                ]
                missing = _missing_paths(expected_validate_outputs)
                if missing:
                    validate_details["missing_outputs"] = [_safe_relpath(p, repo_root) for p in missing]
                    # Treat missing outputs as wrapper failure even if validator returned OK/WARN.
                    run_payload["status"] = "FAIL"
                    run_payload["exit_code"] = 3
                    step(
                        "validate_outputs",
                        "ERROR",
                        {"missing_outputs": validate_details["missing_outputs"]},
                    )
                    _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                    _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                    return 3

            step("validate", "OK" if rc_val == 0 else ("WARN" if rc_val == 1 else "ERROR"), validate_details)

        # 4) Optional image approval workflow (based on latest compliance report)
        image_sel = _effective_image_approval(ns)
        if ns.dry_run or ns.skip_validate:
            step("image_approval", "SKIPPED", {"reason": "dry-run or validation skipped"})
        else:
            report_json = reports_dir / "compliance_report.json"
            unapproved_images = _load_unapproved_images_from_compliance_report(
                repo_root=repo_root,
                report_path=report_json,
            )

            if not unapproved_images:
                step("image_approval", "SKIPPED", {"reason": "no new images"})
            else:
                # Never prompt in CI / non-interactive sessions.
                can_prompt = (sys.stdin.isatty() and sys.stdout.isatty() and (not _is_ci()))

                mode = image_sel.mode
                if mode == "prompt" and not can_prompt:
                    mode = "list"

                if mode == "off":
                    step("image_approval", "SKIPPED", {"reason": "disabled", "new_images": len(unapproved_images)})
                elif mode == "list":
                    print("\n[maintain] New (unapproved) images:")
                    for p in unapproved_images:
                        print(f"- {p}")
                    step("image_approval", "OK", {"mode": "list", "new_images": len(unapproved_images)})
                else:
                    # Interactive or explicit bulk approval.
                    to_approve: List[str] = []
                    if mode == "approve-all":
                        if not _confirm_bulk_approval():
                            step("image_approval", "SKIPPED", {"reason": "bulk approval not confirmed"})
                        else:
                            to_approve = list(unapproved_images)
                    elif mode == "prompt":
                        choice = _prompt_image_approval_action(count=len(unapproved_images))
                        if choice == "4":
                            step("image_approval", "SKIPPED", {"reason": "user skipped"})
                        elif choice == "2":
                            print("\n[maintain] New (unapproved) images:")
                            for p in unapproved_images:
                                print(f"- {p}")
                            step("image_approval", "OK", {"mode": "list", "new_images": len(unapproved_images)})
                        elif choice == "1":
                            if _confirm_bulk_approval():
                                to_approve = list(unapproved_images)
                            else:
                                step("image_approval", "SKIPPED", {"reason": "bulk approval not confirmed"})
                        else:
                            # one-by-one
                            approved_now: List[str] = []
                            for i, p in enumerate(unapproved_images, start=1):
                                print(f"\n[maintain] ({i}/{len(unapproved_images)}) Review: {p}")
                                ans = input("Approve this image? [y]es/[n]o/[q]uit: ").strip().lower()
                                if ans == "q":
                                    break
                                if ans in {"y", "yes"}:
                                    approved_now.append(p)
                            to_approve = approved_now

                    if to_approve:
                        details = _approve_images(
                            repo_root=repo_root,
                            image_paths=to_approve,
                            note=image_sel.note,
                            dry_run=False,
                            verbose=bool(ns.verbose),
                        )
                        step("image_approval", "OK" if details.get("exit_code", 0) == 0 else "ERROR", {"mode": mode, **details})
                        if details.get("exit_code", 0) != 0:
                            run_payload["status"] = "FAIL"
                            run_payload["exit_code"] = 3
                            _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                            _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                            return 3

                        # Re-run validator so the repo is "whole" after approvals.
                        if not ns.skip_validate:
                            import tools.validate_notes_repo as validate_notes_repo

                            val_args2: List[str] = ["--path", repo_root.as_posix(), "--report-dir", "reports"]
                            if ns.strict:
                                val_args2.append("--strict")
                            rc_val2 = validate_notes_repo.main(val_args2)
                            step("validate_after_approval", "OK" if rc_val2 == 0 else ("WARN" if rc_val2 == 1 else "ERROR"), {"exit_code": rc_val2})
                            rc_val = rc_val2
                    else:
                        # No approvals performed.
                        if mode == "approve-all":
                            # Already handled by confirmation path
                            pass
                        else:
                            step("image_approval", "SKIPPED", {"reason": "no images approved"})

        run_payload["status"] = "OK" if rc_val == 0 else ("WARN" if rc_val == 1 else "FAIL")
        run_payload["exit_code"] = rc_val

        _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
        _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)

        return rc_val

    except SystemExit as e:
        # If one of the underlying scripts calls SystemExit, normalize it.
        code = int(e.code) if e.code is not None else 3
        run_payload["status"] = "FAIL"
        run_payload["exit_code"] = code
        step("wrapper", "ERROR", {"system_exit": code})
        _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
        _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
        return code
    except Exception as e:
        run_payload["status"] = "FAIL"
        run_payload["exit_code"] = 3
        step("wrapper", "ERROR", {"type": type(e).__name__, "message": str(e)})
        _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
        _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
        if ns.verbose:
            raise
        print(f"[maintain] ERROR: {type(e).__name__}: {e}")
        return 3


def _render_run_md(payload: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Maintenance Run Report")
    lines.append("")
    lines.append(f"- Generated (UTC): `{payload.get('generated_utc')}`")
    lines.append("- Repo root: (omitted)")

    status = payload.get("status")
    exit_code = payload.get("exit_code")
    lines.append(f"- Status: **{status}**")
    lines.append(f"- Exit code: `{exit_code}`")
    lines.append("")

    py = payload.get("python", {})
    lines.append("## Environment")
    lines.append("")
    lines.append(f"- Python: `{py.get('version')}`")
    lines.append("- Executable: (omitted)")

    plat = payload.get("platform", {})
    lines.append(f"- Platform: `{plat.get('system')} {plat.get('release')} ({plat.get('machine')})`")
    lines.append("")

    lines.append("## Steps")
    lines.append("")
    for s in payload.get("steps", []):
        lines.append(f"- **{s.get('name')}**: {s.get('status')} ({s.get('details')})")

    lines.append("")
    lines.append("## Outputs")
    lines.append("")
    lines.append("- `notes/INDEX.md` (if docs step ran)")
    lines.append("- `reports/repo_health_report.md` (if docs step ran)")
    lines.append("- `reports/repo_inventory.json` (if docs step ran)")
    lines.append("- `reports/repo_change_report.md` (if docs step ran)")
    lines.append("- `reports/compliance_report.md` (if validate step ran)")
    lines.append("- `reports/compliance_report.json` (if validate step ran)")
    lines.append("")

    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    raise SystemExit(main())
