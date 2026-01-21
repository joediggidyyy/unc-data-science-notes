"""generate_repo_docs.py

Repository documentation generator for a public class-notes repo.

Goals
- Scan the repository for changes (no git required).
- Generate/refresh supporting documentation (indexes + reports).
- Be safe and idempotent: only edit within AUTO-GENERATED blocks, otherwise write
  to dedicated generated files.

Designed for the notes mini-repo root:
  unc-data-science-notes/

This script uses only the Python standard library.

Typical usage (from repo root):
  python tools/generate_repo_docs.py

Exit codes
- 0: success
- 2: invalid repo structure
- 3: unexpected error
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


AUTO_START = "<!-- AUTO-GENERATED:START (repo-docs) -->"
AUTO_END = "<!-- AUTO-GENERATED:END (repo-docs) -->"

DEFAULT_EXCLUDE_DIRS: Set[str] = {
    ".git",
    ".github",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    # Local-only / archival areas (never publish; never drive change detection).
    "local_untracked",
    "quarantine_legacy_archive",
    "archive",
    "temp",
    # Generated artifacts should not drive change detection.
    "reports",
}


def _utc_now_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).isoformat(timespec="seconds")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def _safe_relpath(path: Path, repo_root: Path) -> str:
    rel = path.relative_to(repo_root).as_posix()
    # Guard against weird paths (shouldn't happen for relative_to).
    return rel.replace("\\", "/")


def _iter_files(repo_root: Path, exclude_dirs: Set[str], exclude_files: Set[str]) -> Iterable[Path]:
    for p in repo_root.rglob("*"):
        if p.is_dir():
            continue
        rel_parts = p.relative_to(repo_root).parts
        if any(part in exclude_dirs for part in rel_parts):
            continue
        rel = "/".join(rel_parts).replace("\\", "/")
        if p.name in exclude_files or rel in exclude_files:
            continue
        yield p


def _hash_file(path: Path, *, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _file_fingerprint(path: Path, *, full_hash_threshold_bytes: int = 5 * 1024 * 1024) -> Dict[str, Any]:
    """Fingerprint a file.

    For files <= threshold, compute sha256.
    For larger files, store size + mtime_ns to avoid huge CPU cost.
    """

    st = path.stat()
    size = int(st.st_size)
    mtime_ns = int(st.st_mtime_ns)

    fp: Dict[str, Any] = {"size": size, "mtime_ns": mtime_ns}
    if size <= full_hash_threshold_bytes:
        fp["sha256"] = _hash_file(path)
    else:
        fp["sha256"] = None
    return fp


def _load_state(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"version": 1, "generated_at": None, "files": {}}
    try:
        return json.loads(_read_text(path))
    except Exception:
        # Corrupt state should never block; start fresh.
        return {"version": 1, "generated_at": None, "files": {}}


def _save_state(path: Path, state: Dict[str, Any], dry_run: bool) -> None:
    state_out = dict(state)
    state_out["generated_at"] = _utc_now_iso()
    _write_text(path, json.dumps(state_out, indent=2, sort_keys=True) + "\n", dry_run=dry_run)


def _compute_manifest(repo_root: Path, *, exclude_dirs: Set[str], exclude_files: Set[str]) -> Dict[str, Any]:
    files: Dict[str, Any] = {}
    for p in _iter_files(repo_root, exclude_dirs=exclude_dirs, exclude_files=exclude_files):
        rel = _safe_relpath(p, repo_root)
        files[rel] = _file_fingerprint(p)
    return {"version": 1, "generated_at": _utc_now_iso(), "files": files}


def _diff_manifests(prev: Dict[str, Any], curr: Dict[str, Any]) -> Dict[str, List[str]]:
    prev_files = prev.get("files", {}) or {}
    curr_files = curr.get("files", {}) or {}

    prev_keys = set(prev_files.keys())
    curr_keys = set(curr_files.keys())

    added = sorted(curr_keys - prev_keys)
    removed = sorted(prev_keys - curr_keys)

    modified: List[str] = []
    for k in sorted(prev_keys & curr_keys):
        if prev_files.get(k) != curr_files.get(k):
            modified.append(k)

    return {"added": added, "removed": removed, "modified": modified}


def _discover_notes_tree(notes_root: Path) -> Dict[str, Any]:
    """Discover notes under notes/<Term>/<Course>/<WeekXX>/..."""

    tree: Dict[str, Any] = {"terms": {}}
    if not notes_root.exists():
        return tree

    repo_root = notes_root.parent

    for term_dir in sorted([p for p in notes_root.iterdir() if p.is_dir()]):
        term = term_dir.name
        term_entry = tree["terms"].setdefault(term, {"courses": {}})

        for course_dir in sorted([p for p in term_dir.iterdir() if p.is_dir()]):
            course = course_dir.name
            course_entry = term_entry["courses"].setdefault(course, {"weeks": {}})

            for week_dir in sorted([p for p in course_dir.iterdir() if p.is_dir()]):
                week = week_dir.name
                md_files = sorted([f for f in week_dir.rglob("*.md") if f.is_file()])

                # Prefer week README if present.
                readme = week_dir / "README.md"
                readme_rel = _safe_relpath(readme, repo_root) if readme.exists() else None

                course_entry["weeks"][week] = {
                    "path": _safe_relpath(week_dir, repo_root),
                    "readme": readme_rel,
                    "md_count": len(md_files),
                }

    return tree


def _iter_week_dirs(notes_root: Path) -> Iterable[Tuple[str, str, str, Path]]:
    """Yield (term, course, week, week_dir) for notes/<Term>/<Course>/<WeekXX>/..."""

    if not notes_root.exists():
        return

    for term_dir in sorted([p for p in notes_root.iterdir() if p.is_dir()]):
        term = term_dir.name
        for course_dir in sorted([p for p in term_dir.iterdir() if p.is_dir()]):
            course = course_dir.name
            for week_dir in sorted([p for p in course_dir.iterdir() if p.is_dir()]):
                week = week_dir.name
                yield term, course, week, week_dir


def _render_week_readme_md(term: str, course: str, week: str) -> str:
    lines: List[str] = []
    lines.append(f"# {course} - {week} ({term})")
    lines.append("")
    lines.append("> Notes and materials for this week.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("(Coming soon.)")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("(Coming soon.)")
    lines.append("")
    lines.append("## References")
    lines.append("")
    lines.append("(Coming soon.)")
    lines.append("")
    return "\n".join(lines) + "\n"


def _scaffold_missing_week_readmes(repo_root: Path, notes_root: Path, *, dry_run: bool) -> Dict[str, Any]:
    created: List[str] = []
    skipped: List[str] = []

    for term, course, week, week_dir in _iter_week_dirs(notes_root):
        readme = week_dir / "README.md"
        if readme.exists():
            skipped.append(_safe_relpath(readme, repo_root))
            continue
        _write_text(readme, _render_week_readme_md(term, course, week), dry_run=dry_run)
        created.append(_safe_relpath(readme, repo_root))

    return {"created": created, "skipped": skipped}


def _collect_notes_health(repo_root: Path, notes_root: Path, notes_tree: Dict[str, Any]) -> Dict[str, Any]:
    terms = notes_tree.get("terms", {}) or {}
    term_count = len(terms)
    course_count = 0
    week_count = 0
    weeks_missing_readme: List[str] = []
    weeks_empty_md: List[str] = []

    for term, term_entry in terms.items():
        courses = (term_entry or {}).get("courses", {}) or {}
        course_count += len(courses)
        for course, course_entry in courses.items():
            weeks = (course_entry or {}).get("weeks", {}) or {}
            week_count += len(weeks)
            for week, w in weeks.items():
                week_path = w.get("path")
                if not w.get("readme") and week_path:
                    weeks_missing_readme.append(week_path)
                if int(w.get("md_count") or 0) == 0 and week_path:
                    weeks_empty_md.append(week_path)

    # Asset counts inside notes/ (helps strict-mode readiness).
    suffix_counts: Dict[str, int] = {}
    if notes_root.exists():
        for p in notes_root.rglob("*"):
            if not p.is_file():
                continue
            suf = p.suffix.lower()
            if not suf:
                continue
            if suf in {".pdf", ".docx", ".pptx", ".ppt", ".xlsx", ".xls", ".png", ".jpg", ".jpeg", ".gif", ".svg"}:
                suffix_counts[suf] = suffix_counts.get(suf, 0) + 1

    return {
        "term_count": term_count,
        "course_count": course_count,
        "week_count": week_count,
        "weeks_missing_readme_count": len(weeks_missing_readme),
        "weeks_missing_readme_sample": weeks_missing_readme[:25],
        "weeks_empty_md_count": len(weeks_empty_md),
        "weeks_empty_md_sample": weeks_empty_md[:25],
        "notes_asset_suffix_counts": dict(sorted(suffix_counts.items())),
    }


def _render_health_report_md(health: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Repo Health Report")
    lines.append("")
    lines.append(f"Generated (UTC): {_utc_now_iso()}")
    lines.append("")
    lines.append("## Notes structure")
    lines.append("")
    lines.append(f"- Terms: `{health.get('term_count')}`")
    lines.append(f"- Courses: `{health.get('course_count')}`")
    lines.append(f"- Weeks: `{health.get('week_count')}`")
    lines.append("")
    lines.append("## Content completeness")
    lines.append("")
    lines.append(f"- Weeks missing `README.md`: `{health.get('weeks_missing_readme_count')}`")
    lines.append(f"- Weeks with 0 markdown files: `{health.get('weeks_empty_md_count')}`")
    lines.append("")

    def _sample_section(title: str, items: List[str]) -> None:
        lines.append(f"### {title}")
        lines.append("")
        if not items:
            lines.append("(none)")
            lines.append("")
            return
        for it in items:
            lines.append(f"- `{it}`")
        lines.append("")

    _sample_section("Weeks missing README (sample)", health.get("weeks_missing_readme_sample", []) or [])
    _sample_section("Weeks empty of markdown (sample)", health.get("weeks_empty_md_sample", []) or [])

    lines.append("## Notes assets (counts by type)")
    lines.append("")
    counts = health.get("notes_asset_suffix_counts", {}) or {}
    if not counts:
        lines.append("(none)")
        lines.append("")
    else:
        for k, v in counts.items():
            lines.append(f"- `{k}`: `{v}`")
        lines.append("")

    lines.append("## Tip")
    lines.append("")
    lines.append(
        "If this repository is public, review PDFs/DOCX/images for personal information before committing them."
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def _md_link(text: str, rel_path: str) -> str:
    return f"[{text}]({rel_path})"


def _strip_notes_prefix(repo_rel_path: str) -> str:
    """Convert a repo-relative path like 'notes/Term/Course/Week01/...' into a path
    relative to the notes root (suitable for links inside notes/INDEX.md).
    """

    p = Path(repo_rel_path.replace("\\", "/"))
    parts = p.parts
    if parts and parts[0] == "notes":
        p = Path(*parts[1:])
    return p.as_posix()


def _render_notes_index_md(repo_root: Path, notes_tree: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Notes Index")
    lines.append("")
    lines.append("Index of `notes/` organized by term/course/week.")
    lines.append("")
    lines.append(f"Last updated (UTC): {_utc_now_iso()}")
    lines.append("")

    terms = notes_tree.get("terms", {})
    if not terms:
        lines.append("No notes found under `notes/`.")
        lines.append("")
        return "\n".join(lines) + "\n"

    for term, term_entry in terms.items():
        lines.append(f"## {term}")
        lines.append("")
        courses = (term_entry or {}).get("courses", {})
        if not courses:
            lines.append("(No courses found)")
            lines.append("")
            continue

        for course, course_entry in courses.items():
            lines.append(f"### {course}")
            weeks = (course_entry or {}).get("weeks", {})
            if not weeks:
                lines.append("")
                lines.append("(No weeks found)")
                lines.append("")
                continue

            lines.append("")
            for week, w_entry in weeks.items():
                week_repo_rel = w_entry.get("path")
                readme_repo_rel = w_entry.get("readme")

                week_rel = _strip_notes_prefix(week_repo_rel) if week_repo_rel else None
                readme_rel = _strip_notes_prefix(readme_repo_rel) if readme_repo_rel else None

                label = week
                if readme_rel:
                    lines.append(f"- {_md_link(label, readme_rel)}")
                elif week_rel:
                    lines.append(f"- {_md_link(label, week_rel + '/')}")
                else:
                    lines.append(f"- {label}")
            lines.append("")

    return "\n".join(lines) + "\n"


def _replace_or_append_autoblock(existing: str, new_block: str) -> str:
    """Replace content inside AUTO markers; if not found, append a new section."""

    if AUTO_START in existing and AUTO_END in existing:
        before, rest = existing.split(AUTO_START, 1)
        _old, after = rest.split(AUTO_END, 1)
        return before.rstrip() + "\n\n" + AUTO_START + "\n" + new_block.rstrip() + "\n" + AUTO_END + after

    # No markers: append a new section at the end.
    existing = existing.rstrip() + "\n\n"
    return existing + AUTO_START + "\n" + new_block.rstrip() + "\n" + AUTO_END + "\n"


def _render_root_readme_block() -> str:
    lines: List[str] = []
    lines.append("## Notes navigation")
    lines.append("")
    lines.append(f"- {_md_link('Notes Index', 'notes/INDEX.md')}")
    lines.append("")
    lines.append("(Navigation links are maintained automatically.)")
    return "\n".join(lines)


def _render_change_report_md(diff: Dict[str, List[str]], prev_generated_at: Optional[str]) -> str:
    lines: List[str] = []
    lines.append("# Repository Change Report")
    lines.append("")
    lines.append(f"Generated (UTC): {_utc_now_iso()}")
    if prev_generated_at:
        lines.append(f"Previous run: {prev_generated_at}")
    lines.append("")

    def section(title: str, items: List[str]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("(none)")
            lines.append("")
            return
        for it in items:
            lines.append(f"- `{it}`")
        lines.append("")

    section("Added", diff.get("added", []))
    section("Modified", diff.get("modified", []))
    section("Removed", diff.get("removed", []))

    return "\n".join(lines) + "\n"


def _validate_repo_layout(repo_root: Path) -> Tuple[bool, str]:
    required = [repo_root / "README.md", repo_root / "notes"]
    for p in required:
        if not p.exists():
            return False, f"Missing required path: {p.name}"
    return True, "ok"


def run(repo_root: Path, *, dry_run: bool, verbose: bool, scaffold_week_readmes: bool = False) -> int:
    ok, msg = _validate_repo_layout(repo_root)
    if not ok:
        print(f"[repo-docs] ERROR: {msg}")
        return 2

    reports_dir = repo_root / "reports"
    state_path = reports_dir / "_repo_docs_state.json"

    # Exclude generated artifacts from the manifest itself.
    exclude_dirs = set(DEFAULT_EXCLUDE_DIRS)
    exclude_files = {
        state_path.name,
        # Generated index should not drive change detection.
        "notes/INDEX.md",
    }

    prev_state = _load_state(state_path)
    prev_generated_at = prev_state.get("generated_at")

    # Optional scaffolding may create new files; decide based on current layout.
    notes_root = repo_root / "notes"

    curr_state_pre = _compute_manifest(repo_root, exclude_dirs=exclude_dirs, exclude_files=exclude_files)
    diff_pre = _diff_manifests(prev_state, curr_state_pre)

    any_changes = bool(diff_pre["added"] or diff_pre["removed"] or diff_pre["modified"]) or (prev_generated_at is None)

    if verbose:
        # Avoid printing absolute local paths (helps prevent accidental leaks if
        # output is shared/screenshotted).
        print("[repo-docs] repo_root=(omitted)")
        print(f"[repo-docs] dry_run={dry_run}")
        prev_state_display = _safe_relpath(state_path, repo_root) if state_path.exists() else "(none)"
        print(f"[repo-docs] previous_state={prev_state_display}")
        print(f"[repo-docs] changes: +{len(diff_pre['added'])} ~{len(diff_pre['modified'])} -{len(diff_pre['removed'])}")

    if not any_changes and not scaffold_week_readmes:
        if verbose:
            print("[repo-docs] No changes detected; nothing to do.")
        return 0

    scaffold_result: Dict[str, Any] = {"created": [], "skipped": []}
    if scaffold_week_readmes:
        scaffold_result = _scaffold_missing_week_readmes(repo_root, notes_root, dry_run=dry_run)
        if verbose and scaffold_result.get("created"):
            print(f"[repo-docs] scaffolded week READMEs: {len(scaffold_result['created'])}")

    # Generate docs.
    notes_tree = _discover_notes_tree(notes_root)

    notes_index_path = notes_root / "INDEX.md"
    notes_index_md = _render_notes_index_md(repo_root, notes_tree)
    _write_text(notes_index_path, notes_index_md, dry_run=dry_run)

    # Root README: update/append autoblock
    root_readme_path = repo_root / "README.md"
    root_readme = _read_text(root_readme_path)
    root_block = _render_root_readme_block()
    updated_root_readme = _replace_or_append_autoblock(root_readme, root_block)
    if updated_root_readme != root_readme:
        _write_text(root_readme_path, updated_root_readme, dry_run=dry_run)

    # Health report (useful for auditing completeness and strict-mode readiness).
    health = _collect_notes_health(repo_root, notes_root, notes_tree)
    _write_text(reports_dir / "repo_health_report.md", _render_health_report_md(health), dry_run=dry_run)

    # Persist state last so a partial run doesn't hide failures.
    curr_state_post = _compute_manifest(repo_root, exclude_dirs=exclude_dirs, exclude_files=exclude_files)
    diff_post = _diff_manifests(prev_state, curr_state_post)
    _save_state(state_path, curr_state_post, dry_run=dry_run)

    # Reports: inventory + change report
    inventory = {
        "generated_at": _utc_now_iso(),
        "notes_tree": notes_tree,
        "notes_health": health,
        "scaffold": scaffold_result,
        "change_summary": {k: len(v) for k, v in diff_post.items()},
        "changes": diff_post,
    }
    _write_text(reports_dir / "repo_inventory.json", json.dumps(inventory, indent=2, sort_keys=True) + "\n", dry_run=dry_run)

    change_report_md = _render_change_report_md(diff_post, prev_generated_at=prev_generated_at)
    _write_text(reports_dir / "repo_change_report.md", change_report_md, dry_run=dry_run)

    if verbose:
        print("[repo-docs] Generated/updated:")
        print(f"  - {_safe_relpath(notes_index_path, repo_root)}")
        print(f"  - {_safe_relpath(root_readme_path, repo_root)}")
        print(f"  - reports/repo_health_report.md")
        print(f"  - reports/repo_inventory.json")
        print(f"  - reports/repo_change_report.md")
        print(f"  - reports/{state_path.name}")

    return 0


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Scan repo changes and generate supporting documentation.")
    p.add_argument(
        "--repo-root",
        default=None,
        help="Path to repository root (default: parent of this script's parent directory).",
    )
    p.add_argument("--dry-run", action="store_true", help="Compute changes but do not write any files.")
    p.add_argument("--verbose", action="store_true", help="Print details about detected changes and outputs.")
    p.add_argument(
        "--scaffold-week-readmes",
        action="store_true",
        help="Create missing notes/<Term>/<Course>/<WeekXX>/README.md files (additive; never overwrites).",
    )
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    ns = _parse_args(argv)
    script_path = Path(__file__).resolve()

    if ns.repo_root:
        repo_root = Path(ns.repo_root).expanduser().resolve()
    else:
        # tools/generate_repo_docs.py -> repo root is parent of tools/
        repo_root = script_path.parent.parent

    try:
        return run(repo_root, dry_run=ns.dry_run, verbose=ns.verbose, scaffold_week_readmes=ns.scaffold_week_readmes)
    except Exception as e:
        print(f"[repo-docs] ERROR: {type(e).__name__}: {e}")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
