# UNC Prune Recovery Guide (archive-first)

This guide describes how to recover if a UNC prune/cleanup run made a CodeSentinel workspace “unreachable” (missing critical files, broken imports, or missing repo roots).

## What “unreachable” usually means

Common symptoms:

- `codesentinel status` fails because the workspace is missing core directories.
- The repo root no longer contains expected roots (e.g., `codesentinel/`, `tools/`, `docs/`).
- VS Code workspace opens, but commands fail because paths were moved.

## Where the prune tool records evidence

The prune script writes a run record JSON (default):

- `report_tmp/unc_prune_run.json`

The run record includes:

- `archive_root` (where items were moved)
- `moves[]` with `src`, `dst`, and `executed` fields

## Recovery steps

1. **Locate the most recent run record** on the affected workspace.
2. Identify the `archive_root` value.
3. For each `moves[]` entry with `executed=true`, **move the item back** from `dst` to `src`.

Notes:

- This workflow is fully reversible because the prune tool **moves** into `quarantine_legacy_archive/` and does not delete.
- If a destination collision occurred, the tool may have used a `__dupN` suffix; check the run record.

## After restoring files

Run these checks in the recovered workspace:

- `codesentinel status`
- `codesentinel memory health --json`
- `codesentinel oracode graph rebuild` (if ORACode artifacts are missing)
- `codesentinel dashboard update` (to refresh `docs/dashboards/room/`)

## Preventing repeats

Before running a prune execute on a UNC mirror:

- Always run `--dry-run` and `--validate` first.
- Confirm the plan does not propose moving any core roots.
- Confirm the plan repo name matches the current repo name.

If you must prune in a non-standard tree, edit the plan to mark questionable candidates as `REVIEW` and do not use `--include-review` unless you are intentionally moving them.
