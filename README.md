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

Week folders are intentionally kept simple:

- `notes/<Term>/<Course>/<WeekXX>/` contains **PDFs** (and other viewable artifacts).
- `notes/<Term>/<Course>/<WeekXX>/docx/` contains Word source files and any generated Markdown/media.

We do **not** generate PDF-to-Markdown "stub" pages. GitHub renders PDFs well enough, and keeping
Week roots free of extra `.md` files makes the tree easier to scan.

## Public-sharing expectations

- These notes are original and written in my own words.
- Before committing, personal information (emails, phone numbers, IDs) should be removed.

### CodeSentinel approvals (images and other flagged files)

Images are intentionally flagged by the validator for manual privacy review.
After CodeSentinel review approves an image, it should be added to
`approved_artifacts.json` (pinned by SHA256) so it will not warn again unless the
file changes.

## Maintenance

The maintenance wrapper refreshes navigation files and runs a conservative privacy/integrity check.

It can also auto-generate missing Markdown siblings for `.docx` files under `notes/`
(Pandoc required).

### Run maintenance

```text
python maintain.py
```

### Publish-readiness (strict)

Strict mode treats validator warnings as failures.

```text
python maintain.py --strict
```

### Image approvals

Images are treated as **high-risk** for public sharing.

If unapproved images are detected, `maintain.py` can show a review menu in an
interactive terminal.

No images are approved automatically.
Approvals only happen when you choose an approve action.

Approvals are pinned (by SHA256) in `approved_artifacts.json`.
If a file changes, it must be re-approved.

#### During maintenance

- Interactive terminal: show a menu (approve all / list / review one-by-one / skip).
- CI or non-interactive sessions: print a list (no prompting).

#### Maintenance flags

```text
python maintain.py --image-approval off
python maintain.py --list-new-images
python maintain.py --approve-all-new-images
```

#### Standalone approvals (without running maintenance)

```text
python tools/approve_artifacts.py --interactive
python tools/approve_artifacts.py --path notes/.../image.png --note "Reviewed"
python tools/approve_artifacts.py --all-images --under notes --note "Reviewed"   # unsafe
python tools/approve_artifacts.py --list
```

### Reports (local-only)

Generated reports are written to `reports/` and are **not published**.
The `reports/` folder is ignored by git.

<!-- AUTO-GENERATED:START (repo-docs) -->
## Notes navigation

- [Notes Index](notes/INDEX.md)

(Navigation links are maintained automatically.)
<!-- AUTO-GENERATED:END (repo-docs) -->

## Alpha/Beta testing (volunteers)

We’re seeking volunteers to test early changes for CodeSentinel, ORACL, and CIDS.

- Start a GitHub Discussion titled `Alpha/Beta Testing Interest`.
- Do not post PII, secrets, private logs, private network data, or prohibited materials.
- Early-stage; no funding/compensation at this time.
