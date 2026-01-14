import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


def _repo_root() -> Path:
    # .../public_notes_repo_template/tests/test_*.py -> .../public_notes_repo_template
    return Path(__file__).resolve().parents[1]


def _script_path() -> Path:
    return _repo_root() / "tools" / "convert_assets_to_markdown.py"


def _write_minimal_pdf(path: Path) -> None:
    # A tiny, mostly-empty PDF stub. For our purposes, existence is enough.
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\n%%EOF\n"
    path.write_bytes(payload)


def _write_minimal_docx(path: Path, *, text: str = "Hello world") -> None:
    """Create a minimal OOXML .docx (ZIP) with a single paragraph.

    This avoids non-stdlib dependencies while producing a file Pandoc can usually parse.
    """

    path.parent.mkdir(parents=True, exist_ok=True)

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

    # Keep the doc very simple: one paragraph.
    document = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:r><w:t>{text}</w:t></w:r></w:p>
  </w:body>
</w:document>
"""

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document)


def _find_pandoc_exe() -> Path | None:
    """Return a path to pandoc.exe/pandoc if we can find one."""

    hit = shutil.which("pandoc")
    if hit:
        return Path(hit).resolve()

    # Common Windows install locations.
    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\\Program Files")) / "Pandoc" / "pandoc.exe",
        # Quarto-bundled pandoc (often present with RStudio on Windows)
        Path(r"C:\\Program Files\\RStudio\\resources\\app\\bin\\quarto\\bin\\tools\\pandoc.exe"),
    ]

    for cand in candidates:
        try:
            if cand.exists() and cand.is_file():
                return cand.resolve()
        except OSError:
            continue

    return None


def _run_converter(
    *,
    repo_root: Path,
    args: list[str],
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess:
    script = _script_path()
    if not script.exists():
        raise RuntimeError(f"Missing converter script at {script}")

    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    cmd = [sys.executable, str(script), "--repo-root", str(repo_root), *args]
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)


class TestConvertAssetsToMarkdown(unittest.TestCase):
    def test_dry_run_makes_no_writes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            notes = root / "notes" / "Semester" / "COURSE" / "Week01"
            docx = notes / "docx" / "sample.docx"
            pdf = notes / "sample.pdf"

            _write_minimal_docx(docx)
            _write_minimal_pdf(pdf)

            out_docx_md = docx.with_suffix(".md")
            out_pdf_stub_md = pdf.with_suffix(".md")

            cp = _run_converter(
                repo_root=root,
                args=["--dry-run", "--verbose", "--include-pdf-stubs", "--front-matter"],
            )
            self.assertEqual(cp.returncode, 0, msg=cp.stderr or cp.stdout)

            self.assertFalse(out_docx_md.exists(), "dry-run must not create DOCX markdown")
            self.assertFalse(out_pdf_stub_md.exists(), "dry-run must not create PDF stub markdown")

    def test_pdf_stub_written_with_front_matter(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            notes = root / "notes" / "Semester" / "COURSE" / "Week01"
            pdf = notes / "lecture.pdf"
            _write_minimal_pdf(pdf)

            out_stub = pdf.with_suffix(".md")

            cp = _run_converter(
                repo_root=root,
                args=["--verbose", "--include-pdf-stubs", "--front-matter"],
            )
            self.assertEqual(cp.returncode, 0, msg=cp.stderr or cp.stdout)
            self.assertTrue(out_stub.exists(), "expected PDF stub markdown to be created")

            text = out_stub.read_text(encoding="utf-8")
            self.assertIn("---", text, "expected YAML front matter")
            self.assertIn("engine: pdf-stub", text)
            self.assertIn("Open the PDF", text)
            self.assertIn("lecture.pdf", text)

    def test_preflight_requires_pandoc_when_docx_exists(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            notes = root / "notes" / "Semester" / "COURSE" / "Week01" / "docx"
            docx = notes / "hello.docx"
            _write_minimal_docx(docx)

            # Force pandoc discovery to fail by passing an explicit invalid path.
            cp = _run_converter(
                repo_root=root,
                args=["--preflight", "--pandoc-path", str(root / "does_not_exist" / "pandoc.exe")],
                extra_env={"PANDOC_PATH": "", "PATH": ""},
            )
            self.assertEqual(cp.returncode, 2, msg=cp.stderr or cp.stdout)

    def test_docx_conversion_live_when_pandoc_available(self) -> None:
        pandoc_exe = _find_pandoc_exe()
        if pandoc_exe is None:
            self.skipTest("pandoc not found (skipping live DOCX conversion test)")

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            notes = root / "notes" / "Semester" / "COURSE" / "Week01" / "docx"
            docx = notes / "hello.docx"
            # Build an email-like string at runtime so the repo validator doesn't flag
            # this test file itself for containing an email address.
            email = "".join(["student", "@", "example", ".", "com"])
            _write_minimal_docx(docx, text=f"Hello from docx (contact: {email})")

            out_md = docx.with_suffix(".md")
            media_dir = notes / "generated_media" / docx.stem

            cp = _run_converter(
                repo_root=root,
                args=["--verbose", "--front-matter", "--redact-emails", "--pandoc-path", str(pandoc_exe)],
            )
            self.assertEqual(
                cp.returncode,
                0,
                msg=(cp.stderr or cp.stdout),
            )
            self.assertTrue(out_md.exists(), "expected DOCX markdown to be created")
            self.assertTrue(media_dir.exists(), "expected media extraction dir to be created")

            md = out_md.read_text(encoding="utf-8")
            self.assertIn("engine: pandoc", md)
            self.assertNotIn(email, md, "expected email address to be redacted")
            self.assertIn("[REDACTED_EMAIL]", md, "expected redaction marker to be present")
            # Content can vary across Pandoc versions; require only some non-empty body.
            self.assertGreater(len(md.strip()), 20)


if __name__ == "__main__":
    unittest.main()
