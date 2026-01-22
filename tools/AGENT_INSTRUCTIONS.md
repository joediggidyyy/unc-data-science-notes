# [AGENT-USE] Repo Tooling Instructions

> **Identity Directive:** Refer to Joe Waller as `joediggidyyy` and refer to GitHub Copilot as `ORACL` or `ORACL-Prime` in every interaction.

Version: 1.0
Last Updated: 2026-01-14

This repo is a public class-notes repository. The `tools/` directory contains **standard-library-only** scripts that support maintenance and validation.

This file is **public and sanitized**. Do not add secrets, private/internal links, non-public procedures, or any personal information.

## Quick authority reference

| Operation | Agent can do it? |
|-----------|------------------|
| Modify existing tools/scripts | Yes |
| Add a new tool (stdlib only) | Yes |
| Add a new dependency | No (needs maintainer approval) |
| Change validation rules (PII / integrity) | Yes, but be conservative and add tests |
| Delete files | Avoid; prefer archival where feasible |

## Key entry points

- `maintain.py` — one-command wrapper (docs + validation)
- `tools/generate_repo_docs.py` — generates `notes/INDEX.md` and repo reports
- `tools/validate_notes_repo.py` — scans for public-sharing risks (PII, exams/solutions, binaries)
- `tools/approve_artifacts.py` — pins approvals for images/binaries in `approved_artifacts.json`
- `tools/convert_assets_to_markdown.py` — best-effort DOCX/PDF conversion (optional; requires pandoc)

## Tooling design rules

- Keep tools **deterministic** and safe: add `--dry-run` where writes occur.
- Avoid printing absolute local paths (outputs may be shared).
- Prefer repo-relative paths in reports.
- Do not add network calls in tooling (this repo should remain offline-friendly).

## Machine-readable sidecar policy (.md + .json)

- This file has a sibling `tools/AGENT_INSTRUCTIONS.json` that must remain in sync.
- `checksum` in the JSON is SHA-256 of this Markdown (CRLF normalized to LF).

## Local/private extensions

- Keep any private/local operational notes under `local_untracked/` (untracked by git).
- Do not add private procedures, private links, or secrets to tracked instruction files.
