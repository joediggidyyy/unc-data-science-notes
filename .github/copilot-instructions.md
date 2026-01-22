CANONICAL_PROJECT_VERSION: "1.1.5"

# UNC Data Science Notes — Copilot Instructions

> **Identity Directive:** Refer to Joe Waller as `joediggidyyy` and refer to GitHub Copilot as `ORACL` or `ORACL-Prime` in every interaction.

Version: 1.0
Last Updated: 2026-01-14

This repository is a **public, dyslexia-friendly class notes repo**. The primary goals are:

- keep `notes/` readable and navigable
- avoid accidental leakage of private information
- avoid sharing prohibited/unauthorized course materials

## Non-negotiables for public sharing

- **No personal info (PII)** in tracked content: emails, phone numbers, student IDs, gradebook screenshots, rosters.
- **No solutions/answer keys** or assessment content unless explicitly permitted for public distribution.
- **Treat binaries as high-risk**: images, slides, PDFs, and DOCX must be reviewed before committing.

If you are unsure whether something is allowed to be public, default to: **do not publish it**.

## Primary workflow (the one command)

Run the maintenance wrapper from the repo root:

- `python maintain.py`
- `python maintain.py --strict` (treat WARN findings as failures)

This will:

1. regenerate navigation docs (e.g., `notes/INDEX.md`)
2. run the conservative repo validator and write `reports/compliance_report.{md,json}`

## Approving images and other flagged artifacts

The validator flags images for manual review. After review, pin approvals by SHA256 in `approved_artifacts.json`:

- Approve one file: `python tools/approve_artifacts.py --path notes/.../image.png --note "Reviewed"`
- Approve all images under notes/: `python tools/approve_artifacts.py --all-images --note "Reviewed"`

If an approved file changes, it must be re-approved.

## Editing guidance

- Prefer **small diffs** and keep changes focused.
- Avoid adding new dependencies unless a maintainer explicitly requests it.
- Avoid printing or storing absolute local paths in generated reports (use repo-relative paths).

## Instruction file pairing (Markdown + JSON)

- This file has a sibling `.github/copilot-instructions.json` that must remain in sync.
- `checksum` in the JSON is SHA-256 of this Markdown (CRLF normalized to LF).
- `sections` in the JSON are derived from headings (`#`, `##`, `###`) and the text between them.