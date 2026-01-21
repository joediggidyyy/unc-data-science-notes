"""convert_assets_to_markdown.py

Experimental conversion helper for this notes repository.

Goal
- Convert in-repo source documents (primarily .docx) into readable Markdown that
    renders well on GitHub, while preserving formatting *as much as Markdown can*.

Reality check (important)
- Markdown cannot represent every Word layout feature (precise spacing,
  textboxes, complex multi-column layouts, page headers/footers, etc.).
- The best practical approach is typically:
  - DOCX -> Markdown via Pandoc (best-effort formatting)
  - Keep PDF for offline viewing / "print-like" fidelity

This script uses only the Python standard library, but it can optionally invoke
external tools if installed.

Preferred engine
- Pandoc: https://pandoc.org/

Safety
- Does NOT delete sources.
- Skips existing outputs by default.

Typical usage (from repo root)
- Plan what would be converted:
    python tools/convert_assets_to_markdown.py --dry-run --verbose

- Convert all DOCX under notes/ (requires pandoc installed):
    python tools/convert_assets_to_markdown.py --verbose

Exit codes
- 0: success (including "nothing to do")
- 2: missing required external tool for requested conversion
- 3: unexpected failure
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


DEFAULT_NOTES_DIR_NAME = "notes"
DEFAULT_MEDIA_DIR_NAME = "generated_media"


def _utc_now_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).isoformat(timespec="seconds")


def _iter_files(root: Path, *, suffixes: Sequence[str]) -> Iterable[Path]:
    sufset = {s.lower() for s in suffixes}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        # Skip Word lock/temp files (e.g., "~$lecture.docx"). These are not real documents.
        if p.name.startswith("~$"):
            continue
        if p.suffix.lower() in sufset:
            yield p


def _safe_relpath(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except Exception:
        return path.as_posix()


def _detect_pandoc(explicit: Optional[str] = None) -> Optional[str]:
    """Best-effort Pandoc discovery.

    Resolution order:
    1) explicit path passed by caller
    2) environment variable PANDOC_PATH
    3) PATH lookup (shutil.which)
    4) common Windows install locations
    """

    def _as_exe(candidate: str) -> Optional[str]:
        if not candidate:
            return None
        try:
            p = Path(candidate).expanduser()
        except Exception:
            return None

        # If a directory is provided, try typical executable names.
        try:
            if p.exists() and p.is_dir():
                for name in ("pandoc.exe", "pandoc"):
                    exe = (p / name)
                    if exe.exists() and exe.is_file():
                        return str(exe.resolve())
        except OSError:
            return None

        try:
            if p.exists() and p.is_file():
                return str(p.resolve())
        except OSError:
            return None

        # If it's not a file path, allow command-style lookup.
        hit = shutil.which(candidate)
        return str(Path(hit).resolve()) if hit else None

    # 1) explicit (treat as strict override)
    if explicit is not None:
        hit = _as_exe(explicit)
        return hit

    # 2) env
    env_hit = _as_exe(os.environ.get("PANDOC_PATH", ""))
    if env_hit:
        return env_hit

    # 3) PATH
    hit = shutil.which("pandoc")
    if hit:
        return str(Path(hit).resolve())

    # 4) common Windows locations (keep this short and conservative)
    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\\Program Files")) / "Pandoc" / "pandoc.exe",
        Path(r"C:\\Program Files\\RStudio\\resources\\app\\bin\\quarto\\bin\\tools\\pandoc.exe"),
    ]
    for cand in candidates:
        try:
            if cand.exists() and cand.is_file():
                return str(cand.resolve())
        except OSError:
            continue

    return None


def _render_front_matter(src_rel: str, engine: str) -> str:
    # Keep it minimal and YAML-safe.
    lines = [
        "---",
        f"generated_at_utc: { _utc_now_iso() }",
        f"generated_from: {src_rel}",
        f"generator: tools/convert_assets_to_markdown.py",
        f"engine: {engine}",
        "---",
        "",
    ]
    return "\n".join(lines)


def _normalize_md(md_text: str) -> str:
    # Best-effort cleanup without changing meaning.
    # - Normalize newlines
    # - Trim trailing whitespace
    md_text = md_text.replace("\r\n", "\n").replace("\r", "\n")
    md_text = "\n".join(line.rstrip() for line in md_text.split("\n"))

    # Ensure file ends with single newline.
    return md_text.rstrip() + "\n"


_IMG_SRC_RE = re.compile(r'(<img\s+[^>]*?\bsrc=")([^"]+)(")', re.IGNORECASE)


def _rewrite_absolute_img_src(md_text: str, *, dst: Path, repo_root: Path) -> str:
    """Rewrite absolute img src paths into paths relative to the generated .md file.

    Pandoc sometimes emits HTML <img> tags with Windows-absolute paths (e.g.
    C:\\Users\\...\\generated_media\\...\\image1.png). Those paths both leak local
    machine details and break rendering on GitHub.
    """

    repo_root_resolved = repo_root.resolve()

    def _to_rel(src: str) -> str:
        src_norm = src.replace("\\", "/")

        # Handle common absolute forms:
        # - C:/...
        # - file:///C:/...
        if src_norm.lower().startswith("file:///"):
            src_norm = src_norm[len("file:///") :]

        if not re.match(r"^[A-Za-z]:/", src_norm):
            return src

        abs_path = Path(src_norm)
        try:
            abs_resolved = abs_path.resolve()
        except Exception:
            abs_resolved = abs_path

        try:
            rel_to_repo = abs_resolved.relative_to(repo_root_resolved)
            target = repo_root_resolved / rel_to_repo
            return os.path.relpath(str(target), start=str(dst.parent)).replace("\\\\", "/")
        except Exception:
            # Fall back to a basename-only link if we cannot safely relativize.
            return abs_path.name

    def _repl(m: re.Match[str]) -> str:
        prefix, src, suffix = m.group(1), m.group(2), m.group(3)
        return prefix + _to_rel(src) + suffix

    return _IMG_SRC_RE.sub(_repl, md_text)


_EMAIL_RE = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def _redact_emails(md_text: str) -> str:
    """Redact email addresses from generated Markdown.

    This is a safety/compliance measure for a public notes repo template.
    The goal is to prevent accidental publication of personal contact info
    embedded in source documents.
    """

    return _EMAIL_RE.sub("[REDACTED_EMAIL]", md_text)


def _run(cmd: List[str], *, cwd: Optional[Path], verbose: bool) -> Tuple[int, str, str]:
    if verbose:
        print("[convert] run:", " ".join(cmd))

    p = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return int(p.returncode), p.stdout, p.stderr


def _convert_docx_to_md_with_pandoc(
    *,
    src: Path,
    dst: Path,
    extract_media_dir: Path,
    wrap_none: bool,
    gfm: bool,
    pandoc_path: Optional[str],
    verbose: bool,
) -> Tuple[bool, str]:
    pandoc = _detect_pandoc(pandoc_path)
    if not pandoc:
        return False, "Pandoc not found. Provide --pandoc-path (or set PANDOC_PATH) to convert DOCX -> Markdown."

    dst.parent.mkdir(parents=True, exist_ok=True)
    extract_media_dir.mkdir(parents=True, exist_ok=True)

    cmd: List[str] = [
        pandoc,
        str(src),
        "-o",
        str(dst),
        "--extract-media",
        str(extract_media_dir),
    ]
    if gfm:
        cmd.extend(["-t", "gfm"])
    if wrap_none:
        cmd.extend(["--wrap=none"])

    rc, _out, err = _run(cmd, cwd=None, verbose=verbose)
    if rc != 0:
        return False, f"pandoc failed (exit {rc}): {err.strip()}"

    return True, "ok"


def _write_text(path: Path, content: str, *, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def _default_dst_for_src(src: Path, *, mode: str) -> Path:
    """Determine output location.

    mode:
    - sibling: /path/file.docx -> /path/file.md
    - md_dir:  /path/file.docx -> /path/md/file.md
    """

    if mode == "sibling":
        return src.with_suffix(".md")
    if mode == "md_dir":
        return src.parent / "md" / (src.stem + ".md")
    raise ValueError(f"Unknown output mode: {mode}")


def _default_media_dir_for_src(src: Path, *, media_dir_name: str) -> Path:
    # Keep extracted assets close to the source doc for relative linking.
    return src.parent / media_dir_name / src.stem


def _find_related_asset(
    *,
    src: Path,
    notes_root: Path,
    target_suffix: str,
) -> Optional[Path]:
    """Find a best-effort related file (same stem) near src.

    This is intentionally conservative and local:
    - Prefer same directory
    - Then walk up toward notes_root, checking:
      - <dir>/<stem><suffix>
      - <dir>/docx/<stem><suffix>
    """

    stem = src.stem
    suffix = target_suffix.lower()

    def _try_dir(d: Path) -> Optional[Path]:
        candidates = [
            d / f"{stem}{suffix}",
            d / "docx" / f"{stem}{suffix}",
        ]
        for c in candidates:
            try:
                if c.exists() and c.is_file():
                    return c
            except OSError:
                continue
        return None

    cur = src.parent
    while True:
        hit = _try_dir(cur)
        if hit:
            return hit

        if cur == notes_root:
            break
        if cur.parent == cur:
            break
        cur = cur.parent

    return None


def _rel_link(dst: Path, target: Path) -> str:
    try:
        return os.path.relpath(str(target), start=str(dst.parent)).replace("\\", "/")
    except Exception:
        return target.name


def _render_reference_header(*, dst: Path, pdf: Optional[Path], docx: Optional[Path]) -> str:
    lines: List[str] = []
    lines.append("> Markdown version for convenient browsing. Original files:")
    if pdf is not None:
        lines.append(f"> - PDF: [{pdf.name}]({_rel_link(dst, pdf)})")
    if docx is not None:
        lines.append(f"> - DOCX: [{docx.name}]({_rel_link(dst, docx)})")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines) + "\n"


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Convert DOCX assets under notes/ into Markdown for GitHub rendering (best-effort)."
    )
    p.add_argument(
        "--repo-root",
        default=None,
        help="Repo root path (default: parent of tools/)",
    )
    p.add_argument(
        "--notes-root",
        default=None,
        help="Notes root path (default: <repo-root>/notes)",
    )
    p.add_argument(
        "--output-mode",
        choices=["sibling", "md_dir"],
        default="sibling",
        help="Where to write .md files relative to sources",
    )
    p.add_argument(
        "--media-dir-name",
        default=DEFAULT_MEDIA_DIR_NAME,
        help="Directory name for extracted images/media (pandoc --extract-media)",
    )
    p.add_argument(
        "--pandoc-path",
        default=None,
        help=(
            "Explicit path to pandoc executable (or directory containing it). "
            "Overrides PATH lookup. You can also set PANDOC_PATH env var."
        ),
    )
    p.add_argument("--front-matter", action="store_true", help="Prepend minimal YAML front-matter to generated Markdown")
    p.add_argument("--redact-emails", action="store_true", help="Redact email addresses from generated Markdown")
    p.add_argument("--force", action="store_true", help="Overwrite existing output .md files")
    p.add_argument(
        "--preflight",
        action="store_true",
        help=(
            "Validate prerequisites (e.g., pandoc availability when DOCX files exist) and exit. "
            "Does not write files."
        ),
    )
    p.add_argument("--dry-run", action="store_true", help="Print actions but do not write files")
    p.add_argument("--verbose", action="store_true", help="Verbose logging")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    ns = _parse_args(argv)

    script_path = Path(__file__).resolve()
    repo_root = Path(ns.repo_root).expanduser().resolve() if ns.repo_root else script_path.parent.parent
    notes_root = Path(ns.notes_root).expanduser().resolve() if ns.notes_root else (repo_root / DEFAULT_NOTES_DIR_NAME)

    if not notes_root.exists():
        print(f"[convert] notes root not found: {notes_root}")
        return 0

    docx_files = sorted(_iter_files(notes_root, suffixes=[".docx"]))

    if ns.preflight:
        # Preflight should be safe/no-write and focused on actionable prerequisites.
        if ns.verbose:
            print(f"[convert] preflight: docx_count={len(docx_files)}")

        if docx_files:
            pandoc = _detect_pandoc(ns.pandoc_path)
            if not pandoc:
                print("[convert] ERROR: Pandoc not found (required for DOCX -> Markdown). Provide --pandoc-path or set PANDOC_PATH.")
                return 2
            if ns.verbose:
                print(f"[convert] preflight OK: pandoc={pandoc}")

        return 0

    if ns.verbose:
        print(f"[convert] repo_root={repo_root}")
        print(f"[convert] notes_root={notes_root}")
        print(f"[convert] docx_count={len(docx_files)}")
        print(f"[convert] output_mode={ns.output_mode} dry_run={ns.dry_run} force={ns.force}")

    # DOCX -> MD
    conversions_attempted = 0
    conversions_ok = 0

    for src in docx_files:
        dst = _default_dst_for_src(src, mode=ns.output_mode)
        if dst.exists() and not ns.force:
            if ns.verbose:
                print(f"[convert] skip existing: {_safe_relpath(dst, repo_root)}")
            continue

        media_dir = _default_media_dir_for_src(src, media_dir_name=ns.media_dir_name)

        conversions_attempted += 1
        if ns.dry_run:
            print(f"[convert] would convert DOCX -> MD: {_safe_relpath(src, repo_root)} -> {_safe_relpath(dst, repo_root)}")
            continue

        ok, msg = _convert_docx_to_md_with_pandoc(
            src=src,
            dst=dst,
            extract_media_dir=media_dir,
            wrap_none=True,
            gfm=True,
            pandoc_path=ns.pandoc_path,
            verbose=ns.verbose,
        )
        if not ok:
            print(f"[convert] ERROR: {_safe_relpath(src, repo_root)}: {msg}")
            # Missing pandoc is an actionable configuration issue.
            if "Pandoc not found" in msg:
                return 2
            continue

        # Optional: normalize + front matter.
        try:
            md = dst.read_text(encoding="utf-8")
            md = _normalize_md(md)

            # Pandoc sometimes emits Windows-absolute image src paths; rewrite them.
            md = _rewrite_absolute_img_src(md, dst=dst, repo_root=repo_root)

            if ns.redact_emails:
                md = _redact_emails(md)

            # Add a small human header linking to the source artifacts.
            related_pdf = _find_related_asset(src=src, notes_root=notes_root, target_suffix=".pdf")
            header = _render_reference_header(dst=dst, pdf=related_pdf, docx=src)
            md = header + md

            if ns.front_matter:
                src_rel = _safe_relpath(src, repo_root)
                md = _render_front_matter(src_rel, engine="pandoc") + md
            _write_text(dst, md, dry_run=False)
        except Exception as e:
            print(f"[convert] WARN: post-process failed for {_safe_relpath(dst, repo_root)}: {type(e).__name__}: {e}")

        conversions_ok += 1
        if ns.verbose:
            print(f"[convert] OK: {_safe_relpath(src, repo_root)} -> {_safe_relpath(dst, repo_root)}")

    if ns.verbose:
        print(f"[convert] attempted={conversions_attempted} ok={conversions_ok}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
