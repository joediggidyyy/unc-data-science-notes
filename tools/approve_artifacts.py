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
    python tools/approve_artifacts.py --category image --under notes --all-images --note "Reviewed"
  python tools/approve_artifacts.py --remove --path notes/.../image.png
  python tools/approve_artifacts.py --list

Standard-library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


DEFAULT_MANIFEST = "approved_artifacts.json"


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


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
