# Detailed Contributing Guide

## Metadata

| Field | Value |
| --- | --- |
| Document Title | Detailed Contributing Guide |
| Domain / Scope | DOC |
| Artifact Type | Guide |
| Classification | Internal |
| Execution Window | 2025-12-10 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/guides/CONTRIBUTING_DETAILED.md |

---

## Purpose

This document expands on `CONTRIBUTING.md` with concrete steps for setting up branches, running validation tools, and preparing pull requests that satisfy SEAM guardrails. Reference it whenever you prepare a change set.

## 1. Ground Rules

1. **Security First** – Never commit secrets, credentials, or `.env` files. Use environment variables exclusively.
2. **Archive-First** – Instead of deleting files, move them into `quarantine_legacy_archive/` or another designated archive path.
3. **Single Source of Truth** – Reuse helpers inside `codesentinel/utils/` or `tools/codesentinel/` rather than duplicating logic.
4. **Cross-Platform** – All scripts must run on Windows PowerShell and macOS/Linux shells.

## 2. Branch Workflow

```pwsh
# Ensure main is current
git checkout main
git pull origin main

# Create a feature branch
git checkout -b feature/<short-description>
```

Use short, kebab-cased descriptions (e.g., `feature/fix-session-health`).

## 3. Run the Required Checks

| Command | When to run | Purpose |
| --- | --- | --- |
| `python run_tests.py` | Before every push | Executes the entire pytest suite with repository defaults |
| `codesentinel memory health --json` | After touching SessionMemory | Confirms cache freshness and guard status |
| `codesentinel scan` | When editing security or policy files | Runs security linting and dependency checks |
| `python tools/oracode/graph_builder.py --index semantics_vault/oracl_index/index.jsonl` | After updating docs with cross-links | Ensures unresolved references stay below policy thresholds |

Log command output in the PR description so reviewers can verify evidence quickly.

## 4. Formatting & Style

- **Python**: Follow `black` formatting (`pyproject.toml` contains the authoritative configuration).
- **Markdown**: Apply `codesentinel format file <path>` to normalize headers and metadata tables.
- **Imports**: Keep absolute imports for packages and prefer relative imports inside `codesentinel/` packages for clarity.
- **Doc Headers**: Include metadata tables for all documents placed under `docs/` unless the schema specifies otherwise.

## 5. Writing Tests

1. Place new tests inside `tests/` mirroring the module path (e.g., `codesentinel/utils/foo.py` → `tests/test_utils.py`).
2. Use fixtures for filesystem or environment manipulation so tests stay hermetic.
3. Prefer `pytest.mark.parametrize` when validating multiple inputs.
4. Always run `pytest <new-test-file>` locally before invoking `run_tests.py` to save time.

## 6. Submitting a Pull Request

1. Push your branch and create a PR targeting `main`.
2. Fill in the template, including:
   - Description of the change and motivation
   - Testing evidence (commands + pass/fail summary)
   - Any policy updates or documentation changes
3. Tag reviewers and label the PR appropriately (`security`, `docs`, `cli`, etc.).
4. Keep the diff focused. Large refactors require prior approval from the maintainers.

## 7. After Merge

- Pull `main` and delete your branch locally and remotely.
- Re-run `codesentinel memory health` to refresh caches for the next task.
- If the change impacts documentation or the ORACL knowledge graph, schedule a `rebuild_graph.py` run per `.github/copilot-instructions.md`.

## Reference Documents

| Artifact | Description |
| --- | --- |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Canonical contributor policy |
| [`README.md`](../README.md) | Project overview and support channels |
| [`SECURITY.md`](../SECURITY.md) | Vulnerability disclosure and credential rules |
| [`docs/architecture/IP_PROTECTION_STRATEGY.md`](../architecture/IP_PROTECTION_STRATEGY.md) | IP protection mandates |
| [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) | Agent operating directives |

## Revision History

| Date | Change | Author |
| --- | --- | --- |
| 2025-12-10 | Initial detailed contributing workflow | ORACL-Prime |
