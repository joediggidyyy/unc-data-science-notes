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
        help="Run DOCX/PDF -> Markdown conversion under notes/ (best-effort; OFF by default)",
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
        "--include-pdf-stubs",
        action="store_true",
        help="When converting assets, generate PDF stub Markdown pages (link-only)",
    )
    p.add_argument(
        "--front-matter",
        action="store_true",
        help="When converting assets, prepend YAML front-matter to generated Markdown",
    )
    p.add_argument("--skip-docs", action="store_true", help="Skip documentation generation")
    p.add_argument("--skip-validate", action="store_true", help="Skip compliance validation")
    return p.parse_args(argv)


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

        # 1) Optional asset conversion (dry-run -> preflight -> execution)
        if not ns.convert_assets:
            step("convert", "SKIPPED", {})
        else:
            import tools.convert_assets_to_markdown as convert_assets_to_markdown

            base_args: List[str] = ["--repo-root", repo_root.as_posix()]
            if ns.verbose:
                base_args.append("--verbose")
            if ns.pandoc_path:
                base_args.extend(["--pandoc-path", str(ns.pandoc_path)])
            if ns.include_pdf_stubs:
                base_args.append("--include-pdf-stubs")
            if ns.front_matter:
                base_args.append("--front-matter")
            # Safety default for public notes: generated Markdown should not contain emails.
            base_args.append("--redact-emails")
            if ns.convert_force:
                base_args.append("--force")

            # 1a) Dry-run plan (always safe/no-write)
            rc_plan = convert_assets_to_markdown.main([*base_args, "--dry-run"])
            step("convert_plan", "OK" if rc_plan == 0 else "ERROR", {"exit_code": rc_plan})
            if rc_plan != 0:
                run_payload["status"] = "FAIL"
                run_payload["exit_code"] = 3 if rc_plan == 3 else rc_plan
                _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                return run_payload["exit_code"]

            # 1b) Preflight validation (tooling prerequisites)
            rc_pre = convert_assets_to_markdown.main([*base_args, "--preflight"])
            step("convert_preflight", "OK" if rc_pre == 0 else "ERROR", {"exit_code": rc_pre})
            if rc_pre != 0:
                run_payload["status"] = "FAIL"
                run_payload["exit_code"] = 3 if rc_pre == 3 else rc_pre
                _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                return run_payload["exit_code"]

            # 1c) Execution (skipped if wrapper is in dry-run mode)
            if ns.dry_run:
                step("convert_execute", "SKIPPED", {"reason": "wrapper dry-run"})
            else:
                rc_exec = convert_assets_to_markdown.main(base_args)
                step("convert_execute", "OK" if rc_exec == 0 else "ERROR", {"exit_code": rc_exec})
                if rc_exec != 0:
                    run_payload["status"] = "FAIL"
                    run_payload["exit_code"] = 3 if rc_exec == 3 else rc_exec
                    _write_json(reports_dir / "maintenance_run.json", run_payload, dry_run=ns.dry_run)
                    _write_text(reports_dir / "maintenance_run.md", _render_run_md(run_payload), dry_run=ns.dry_run)
                    return run_payload["exit_code"]

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
            step("docs", "OK" if rc_docs == 0 else "ERROR", {"exit_code": rc_docs})
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
            step("validate", "OK" if rc_val == 0 else ("WARN" if rc_val == 1 else "ERROR"), {"exit_code": rc_val})

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
