# DOCX authoring workflow (DOCX -> Markdown + PDF)

This repository supports authoring notes in Microsoft Word `.docx`.

This repo intentionally allows storing original artifacts (PDF/DOCX) alongside the
Markdown for convenient download and cross-checking.

Structure (example):

- `notes/<Term>/<Course>/<WeekXX>/...` (Markdown + original artifacts)
- `notes/<Term>/<Course>/<WeekXX>/docx/` (optional: source `.docx` files)

## If you commit DOCX

- `.docx` is a binary bundle, so PR diffs are limited.
- It can contain metadata (author, comments, tracked changes).

Before committing:

- Remove tracked changes and comments.
- Use a neutral author name if Word embeds identity.
- Export to PDF if you want a layout-preserving version.

## Authoring rules (to improve conversion quality)

In Word:

- Use **Styles** for headings (Heading 1/2/3), lists, and emphasis.
- Avoid manual spacing hacks; prefer paragraph spacing settings.
- Keep line length reasonable; use whitespace.
- Remove tracked changes and comments before exporting.

## Converting DOCX -> Markdown

Recommended tool: Pandoc.

- Convert `.docx` to GitHub-flavored Markdown.
- Inspect output for:
  - heading levels
  - bullet list indentation
  - math formatting (if any)
  - any embedded links

## Converting DOCX -> PDF

PDF is best used as a layout-preserving artifact.

- Use Word export to PDF with accessibility in mind (real text, correct reading order).
- Avoid screenshot-based PDFs.

## Validation

Run the validator before publishing:

- `python tools/validate_notes_repo.py --path . --strict`

Notes:

- Images are flagged for manual privacy review until approved.

Approve a specific image:

```text
python tools/approve_artifacts.py --category image --path notes/.../image.png --note "Reviewed"
```

Interactive review menu (new/unapproved images):

```text
python tools/approve_artifacts.py --interactive
```

- Reports are written to `reports/` but are local-only (ignored by git).

## One-command workflow (optional conversion)

If you want conversion to be part of your routine pre-publish workflow, the maintenance wrapper supports an opt-in conversion step:

- `python maintain.py --convert-assets --front-matter`

This remains **OFF by default** so you can control when generated Markdown gets written.

## Testing the conversion tool

The repo includes a stdlib-only test suite that performs:

- a no-write dry-run check
- a live DOCX -> MD conversion test (auto-skips if Pandoc cannot be found)

Run from the repo root:

- `python -m unittest -v`

If the live DOCX test is skipped due to Pandoc not being on PATH, prepend the Pandoc directory to PATH for the session.
