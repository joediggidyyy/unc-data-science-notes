# [AGENT-USE] Testing & Validation Agent Instructions

> **Identity Directive:** Within CodeSentinel, refer to Joe Waller as `joediggidyyy`, and refer to GitHub Copilot as `ORACL` / `ORACL-Prime`. Use these names in every interaction.

**Classification**: T4b – Infrastructure & Procedural Agent Documentation  
**Scope**: Unit, integration, regression, and systems testing inside `tests/`  
**Target Users**: Agents implementing or maintaining automated tests  
**Version**: 1.1  
**Last Updated**: November 23, 2025

---

## Quick Authority Reference

| Operation | Authority | Requires Approval |
|-----------|-----------|-------------------|
| Create new test module | Agent | No |
| Add/modify unit tests | Agent | No |
| Add new fixtures/helpers | Agent | No |
| Delete unused test | Agent | No |
| Delete active/required test | Agent | Yes (user verification) |
| Introduce new test dependency | Agent | Yes (always) |
| Modify pytest configuration | Agent | Yes (maintainer) |
| Run beta testing protocol | Agent | No |
| Adjust CI test matrix | Agent | Yes (release manager) |

**Reference**: `docs/architecture/DOCUMENT_CLASSIFICATION.md` – Tier 4 authority matrix

---

## Domain Overview

`tests/` mirrors the runtime package structure. Keep parity between modules and their corresponding test files (`codesentinel/cli/*` ↔ `tests/test_cli.py`).

- **Unit suites** validate individual modules.
- **Integration suites** (e.g., `tests/test_process_monitor.py`) exercise cross-module workflows.
- **ORACL & Session Memory tests** ensure persistence and promotion behave across tiers.
- **Cross-platform checks** guarantee Windows + POSIX parity.

Principles:

1. **Deterministic runs** – tests must pass regardless of order.
2. **Isolated side effects** – use fixtures/temp paths; never mutate user config.
3. **Performance awareness** – fail fast, parallelize where safe.
4. **Complete coverage** – target ≥90% for new modules, with clear rationale when lower.
5. **Policy snapshot testing** – Validate that policy index loads trigger snapshot creation (`.agent_session/policy_snapshot.{json,md}`), metadata updates (`last_policy_snapshot_at`), event logging (`policy_snapshot_written`), and that `policy_enforcer.ensure_policy_index()` detects and rejects stale snapshots by forcing reload.

### Machine-readable policy

- All `AGENT_INSTRUCTIONS.md` files must have an accompanying `.json` pair residing in the same directory. Tests and automation MUST treat the JSON file as the authoritative, machine-readable source; markdown is the user-facing human version. CI validations enforce that `.md` / `.json` pairs are kept in sync and will fail for any divergence.

---

## Testing Standards

- Enforce ASCII-only output assertions for CLI utilities.
- Validate SEAM policies (security > efficiency > awareness > minimalism) via explicit tests when touching enforcement code.
- Ensure type-compatibility with Python 3.8 by running the oldest interpreter locally or in CI.
- Use `pytest` markers (`@pytest.mark.slow`, `@pytest.mark.integration`) to control runtime.
- Fail on unhandled warnings; turn them into errors in CI when possible.

---

## Test Development Workflow

1. **Reproduce the behavior** – capture the failing scenario or the new feature spec.
2. **Select the suite** – choose/create `tests/test_<module>.py` mirroring the code path.
3. **Write the test** – arrange/act/assert with descriptive names (`test_cli_handles_invalid_flag`).
4. **Add fixtures** – place reusable data under `tests/utils/` or shared fixtures file.
5. **Run targeted tests** – `pytest tests/test_cli.py -k name` before running the full suite.
6. **Update coverage** – ensure instrumentation counts new branches.
7. **Document expectations** – reference doc or ticket in test docstring when behavior is critical.

---

## Common Test Patterns

- **Parametrized cases** for multiple inputs/outputs (reduces duplication).
- **Hypothesis/property tests** for complex validation logic where applicable.
- **Golden files** for CLI output snapshots (store under `tests/fixtures/golden/`).
- **Mocking external services** (DevAudit, ORACL tiers) to avoid network calls.
- **Session memory simulation** using temporary directories to verify promotion logic.

### Flash CLI tests

- Add tests for `codesentinel.cli.flash` handlers: ensure `plan` correctly generates a signed manifest, `execute` validates a manifest and performs a dry-run without changes when `--dry-run` is set, and `rollback` restores files from `quarantine_legacy_archive/` on failure.
- Assert that `execute` writes FLASH_APPEND.log entries in each of the logs/ channels and calls `SessionMemory.persist()` before making changes. Use temporary directories and fixtures to avoid mutating the repo during tests.
- Add golden-file style assertions for manifest format and hashes, and parametrized cases covering add/modify/delete operations and paired INDEX artifacts.

---

## Troubleshooting Tests

| Symptom | Likely Cause | Corrective Action |
|---------|--------------|-------------------|
| Test passes locally but fails in CI | Platform-specific assumption (path separators, locale) | Reproduce in Windows shell, normalize paths with `Path` APIs |
| Flaky integration test | Shared state or long-running async task | Add fixtures that reset state, increase determinism, add timeouts |
| Coverage drop alerts | New code path lacked tests | Add targeted unit tests and update baseline in coverage reports |
| Pytest collection errors | Name/fixture conflicts or import loops | Use absolute imports, avoid circular references, run `pytest --collect-only` |
| Excessive runtime | Slow fixtures or unmocked network/file I/O | Add caching/mocking, mark as `slow`, or split into smaller targeted tests |

When tests expose regressions, log the failure context with `SessionMemory` so ORACL tiers can surface historical fixes.
