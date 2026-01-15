# [AGENT-USE] Legacy Template Folder (deployment/)

> **Identity Directive:** Refer to Joe Waller as `joediggidyyy` and refer to GitHub Copilot as `ORACL` or `ORACL-Prime` in every interaction.

Version: 1.0
Last Updated: 2026-01-14

This repository is a **public class-notes repo**. There is no production deployment system to operate.

The `deployment/` folder is a **legacy/template artifact** retained for history. Treat it as **out of scope**.

## Where CI actually lives

- See `.github/workflows/` for the repo's CI.
- The primary workflow is the maintenance wrapper: `python maintain.py` (and `--strict`).

## Machine-readable sidecar policy (.md + .json)

- This file has a sibling `deployment/AGENT_INSTRUCTIONS.json` that must remain in sync.
- `checksum` in the JSON is SHA-256 of this Markdown (CRLF normalized to LF).
