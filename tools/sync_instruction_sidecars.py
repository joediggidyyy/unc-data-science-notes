"""sync_instruction_sidecars.py

Keep instruction Markdown/JSON pairs in sync.

This repo uses a lightweight convention:

- For each `AGENT_INSTRUCTIONS.md`, there must be a sibling `AGENT_INSTRUCTIONS.json`.
- For `.github/copilot-instructions.md`, there must be a sibling `.github/copilot-instructions.json`.
- `checksum` in the JSON is SHA-256 of the Markdown content after normalizing CRLF -> LF.
- `sections` are derived from headings (`#`, `##`, `###`, ...) and the text between them.

Standard-library only.

Usage (from repo root):
  python tools/sync_instruction_sidecars.py --all
  python tools/sync_instruction_sidecars.py --paths .github/copilot-instructions.md tools/AGENT_INSTRUCTIONS.md

Exit codes:
- 0: success
- 2: invalid inputs
- 3: unexpected error
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+#+\s*)?$", re.MULTILINE)


def _normalize_md_text(text: str) -> str:
    # Normalize CRLF/CR -> LF for hashing + section extraction.
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _split_sections(md_text: str) -> Tuple[Optional[str], List[Dict[str, str]]]:
    """Return (title, sections).

    Title is the first H1 (`# ...`) if present.
    Sections are produced for every heading level encountered.

    Each section record is:
      {"name": <heading text>, "content": <text until next heading>}
    """

    matches = list(_HEADING_RE.finditer(md_text))
    if not matches:
        return None, [{"name": "(no headings)", "content": md_text}]

    sections: List[Dict[str, str]] = []
    title: Optional[str] = None

    for i, m in enumerate(matches):
        level = len(m.group(1))
        name = (m.group(2) or "").strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)

        content = md_text[start:end]
        # Trim a single leading newline to match existing sidecars.
        if content.startswith("\n"):
            content = content[1:]

        sections.append({"name": name, "content": content})

        if title is None and level == 1:
            title = name

    return title, sections


def _json_sidecar_path(md_path: Path) -> Path:
    if md_path.name == "copilot-instructions.md":
        return md_path.with_suffix(".json")
    if md_path.name == "AGENT_INSTRUCTIONS.md":
        return md_path.with_suffix(".json")
    # Generic behavior: sibling .json.
    return md_path.with_suffix(".json")


def _build_sidecar(md_path: Path) -> Dict[str, Any]:
    raw = md_path.read_text(encoding="utf-8")
    md = _normalize_md_text(raw)

    title, sections = _split_sections(md)

    payload: Dict[str, Any] = {
        "checksum": _sha256_hex(md),
        "metadata": {},
        "sections": sections,
        "title": title or md_path.stem,
    }
    return payload


def _write_json(path: Path, payload: Dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def _discover_all(repo_root: Path) -> List[Path]:
    paths: List[Path] = []

    copilot_md = repo_root / ".github" / "copilot-instructions.md"
    if copilot_md.exists():
        paths.append(copilot_md)

    paths.extend(sorted(repo_root.rglob("AGENT_INSTRUCTIONS.md")))

    # Keep only unique paths.
    uniq: List[Path] = []
    seen = set()
    for p in paths:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        uniq.append(p)
    return uniq


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Sync instruction Markdown/JSON sidecars")
    p.add_argument("--repo-root", default=None, help="Repo root (default: auto-detect)")
    p.add_argument("--all", action="store_true", help="Sync all instruction pairs in the repo")
    p.add_argument("--paths", nargs="*", default=None, help="Specific Markdown files to sync")
    p.add_argument("--dry-run", action="store_true", help="Compute but do not write")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    ns = _parse_args(argv)

    repo_root = Path(ns.repo_root).expanduser().resolve() if ns.repo_root else Path(__file__).resolve().parents[1]

    if not repo_root.exists():
        print("[sync] ERROR: repo root does not exist")
        return 2

    if bool(ns.all) == bool(ns.paths):
        print("[sync] ERROR: specify exactly one of --all or --paths")
        return 2

    if ns.all:
        md_paths = _discover_all(repo_root)
    else:
        assert ns.paths is not None
        md_paths = [Path(p).expanduser().resolve() if not Path(p).is_absolute() else Path(p) for p in ns.paths]
        md_paths = [p if p.is_absolute() else (repo_root / p).resolve() for p in md_paths]

    # Filter to existing files.
    missing = [p for p in md_paths if not p.exists()]
    if missing:
        print("[sync] ERROR: missing Markdown file(s):")
        for p in missing:
            try:
                rel = p.relative_to(repo_root)
                print(f"  - {rel.as_posix()}")
            except Exception:
                print(f"  - {p}")
        return 2

    for md_path in md_paths:
        payload = _build_sidecar(md_path)
        json_path = _json_sidecar_path(md_path)
        _write_json(json_path, payload, dry_run=ns.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
