# Public Class Notes (Dyslexia-Friendly)

This repository contains student-authored course notes, organized by term/course/week, with accessibility-first formatting.

## Quick navigation

- Notes index: [`notes/INDEX.md`](notes/INDEX.md)

## What you will find here

- Markdown notes for easy reading in the browser.
- Original note artifacts when available (for example, PDF/DOCX) for downloading.

## Folder structure

Notes live under:

`notes/<Term>/<Course>/<WeekXX>/...`

Example:

`notes/Spring_2026/DATA780/Week02/`

## Public-sharing expectations

- These notes are original and written in my own words.
- Before committing, personal information (emails, phone numbers, IDs) should be removed.

### CodeSentinel approvals (images and other flagged files)

Images are intentionally flagged by the validator for manual privacy review.
After CodeSentinel review approves an image, it should be added to
`approved_artifacts.json` (pinned by SHA256) so it will not warn again unless the
file changes.

## Maintenance

This repository includes a small maintenance script that refreshes navigation files and runs a conservative privacy/integrity check:

- `python maintain.py`

Before publishing major updates, strict mode is recommended:

- `python maintain.py --strict`

Generated reports are written to `reports/` and are **not published** (the folder
is ignored by git).

<!-- AUTO-GENERATED:START (repo-docs) -->
## Notes navigation

- [Notes Index](notes/INDEX.md)

(Navigation links are maintained automatically.)
<!-- AUTO-GENERATED:END (repo-docs) -->
