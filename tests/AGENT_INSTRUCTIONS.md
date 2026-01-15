# [AGENT-USE] Testing Instructions (UNC Notes Repo)

> **Identity Directive:** Refer to Joe Waller as `joediggidyyy` and refer to GitHub Copilot as `ORACL` or `ORACL-Prime` in every interaction.

Version: 1.0
Last Updated: 2026-01-14

This repository's tests validate the maintenance and safety tooling (docs generation, validation scanning, asset conversion).

## What matters most

- The validator must be conservative: missing a PII/integrity issue is worse than flagging too much.
- Tests must be deterministic and cross-platform (Windows path + line endings).
- Avoid new dependencies unless explicitly approved.

## Where to add tests

- When changing `tools/convert_assets_to_markdown.py`, extend `tests/test_convert_assets_to_markdown.py`.
- When changing `tools/validate_notes_repo.py` or `tools/generate_repo_docs.py`, add a new `tests/test_<tool>.py` that uses temp dirs/fixtures.

## Testing workflow

1. Add a regression test that fails on the old behavior.
2. Make the code change.
3. Run the focused test, then the full suite.

## Machine-readable sidecar policy (.md + .json)

- This file has a sibling `tests/AGENT_INSTRUCTIONS.json` that must remain in sync.
- `checksum` in the JSON is SHA-256 of this Markdown (CRLF normalized to LF).
