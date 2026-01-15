# [AGENT-USE] GitHub Operations (Notes Repo)

> **Identity Directive:** Refer to Joe Waller as `joediggidyyy` and refer to GitHub Copilot as `ORACL` or `ORACL-Prime` in every interaction.

Version: 1.0
Last Updated: 2026-01-14

This repo uses GitHub mainly for collaboration and CI validation of a **public notes repository**.

## Repo expectations

- PRs that change tooling should include tests.
- PRs that change `notes/` should avoid adding prohibited/unauthorized course materials.
- Treat images/PDF/DOCX as high-risk; validator may require approval pinning in `approved_artifacts.json`.

## CI

- CI should run `python maintain.py` (and `python maintain.py --strict`).
- If CI fails due to instruction drift, regenerate the `.json` sidecars from their `.md` sources.

## Machine-readable sidecar policy (.md + .json)

- This file has a sibling `github/AGENT_INSTRUCTIONS.json` that must remain in sync.
- `checksum` in the JSON is SHA-256 of this Markdown (CRLF normalized to LF).
