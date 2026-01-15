# [AGENT-USE] Legacy Template Folder (infrastructure/)

> **Identity Directive:** Refer to Joe Waller as `joediggidyyy` and refer to GitHub Copilot as `ORACL` or `ORACL-Prime` in every interaction.

Version: 1.0
Last Updated: 2026-01-14

This repository does **not** manage infrastructure-as-code. The `infrastructure/` folder is a legacy/template artifact.

Treat it as **out of scope** for normal repo maintenance.

## Where the real work is

- `notes/` for content
- `tools/` + `maintain.py` for repo automation and validation
- `approved_artifacts.json` for pinned approvals of images/binaries

## Machine-readable sidecar policy (.md + .json)

- This file has a sibling `infrastructure/AGENT_INSTRUCTIONS.json` that must remain in sync.
- `checksum` in the JSON is SHA-256 of this Markdown (CRLF normalized to LF).
