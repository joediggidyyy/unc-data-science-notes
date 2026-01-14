# Gate Evidence Locations (Quick Reference)

Purpose: help operators and agents locate hard-gate evidence without relying on file-search behavior that may hide gitignored paths.

## Canonical evidence sinks

- Shared gate event stream:
  - `logs/behavioral/gates/gate_events.jsonl`

- QuestStack-local evidence (when a gate is run as part of a QuestFrame):
  - `logs/queststack/<QUESTSTACK_ID>_evidence.jsonl`

## Why search may say "no matches"

In many environments, file search defaults to respecting ignore rules (for example `.gitignore`). Since `logs/` is commonly ignored, searching for `**/gate_events.jsonl` may return no matches even though the file exists.

This is expected.

If you need to confirm the file exists, navigate directly to the path above or list the directory:

- `logs/behavioral/gates/`

## Safety

- Gate evidence is **names-only** and must never contain secret values.
- Evidence may include file paths; do not add plaintext sensitive identifiers (hosts, IPs, usernames, tokens, keys, passwords).
