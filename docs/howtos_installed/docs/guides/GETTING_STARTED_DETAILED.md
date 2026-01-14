# Detailed Getting Started Guide

## Metadata

| Field | Value |
| --- | --- |
| Document Title | Detailed Getting Started Guide |
| Domain / Scope | DOC |
| Artifact Type | Guide |
| Classification | Internal |
| Execution Window | 2025-12-10 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/guides/GETTING_STARTED_DETAILED.md |

---

## Overview

This guide expands on `QUICK_START.md` with an end-to-end walkthrough for setting up CodeSentinel locally, preparing the Python environment, and validating that the CLI works. Follow these steps sequentially the first time you install the project.

## 1. Prerequisites

1. **Python**: Version 3.8–3.12 (match the version listed in `pyproject.toml`).
2. **Git**: Required for cloning and pulling updates.
3. **Pipx or virtualenv**: Recommended for isolated installs. The guide below uses `python -m venv`.
4. **PowerShell (Windows) or bash/zsh (macOS/Linux)**: All commands are shell-agnostic unless noted.

> ℹ️ If you plan to contribute code, also install `pre-commit` so repository hooks can run locally.

## 2. Clone the Repository

```pwsh
# Choose a workspace directory first
cd ~/Documents

# Clone via SSH or HTTPS
git clone git@github.com:joediggidyyy/CodeSentinel-1.git
cd CodeSentinel-1
```

Verify that you can list the repository root (`README.md`, `pyproject.toml`, `codesentinel/`, etc.).

## 3. Create and Activate a Virtual Environment

```pwsh
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

Upgrade packaging tooling:

```pwsh
python -m pip install --upgrade pip wheel setuptools
```

## 4. Install CodeSentinel in Editable Mode

```pwsh
pip install -e ".[dev]"
```

- Installs runtime dependencies from `pyproject.toml`
- Installs development extras defined in the `[project.optional-dependencies]` table
- Makes the `codesentinel` CLI available in the virtual environment

## 5. Run Smoke Tests

Execute the minimal health checks before digging deeper:

```pwsh
codesentinel --help
codesentinel advise --help
python run_tests.py -k "session_memory or quick"
```

If any command fails, review the troubleshooting tips below.

## 6. Initialize Session Memory Artifacts

Many workflows expect `.agent_session/` and `logs/session_memory/` to exist. Run:

```pwsh
codesentinel memory health --json
```

This populates the cache directories and produces a baseline health report under `logs/session_memory/health/`.

## 7. Link Supporting Documentation

After installation, skim the following assets to understand operating guardrails:

| Document | Why it matters |
| --- | --- |
| [`README.md`](../README.md) | High-level positioning, supported commands, quick install |
| [`SECURITY.md`](../SECURITY.md) | Credential handling rules and disclosure flow |
| [`docs/guides/README.md`](README.md) | Navigation hub for every guide |
| [`docs/architecture/IP_PROTECTION_STRATEGY.md`](../architecture/IP_PROTECTION_STRATEGY.md) | Describes SEAM-first security controls |
| [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) | Canonical instructions for ORACL agents |

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `pip install` fails due to build isolation | Upgrade `pip`, clear the virtual environment, retry with `pip install -e .` |
| `codesentinel` command not found | Confirm your virtual environment is active; on Windows ensure you executed `Activate.ps1` instead of `activate.bat` |
| Tests hang on integrity checks | Run `python run_tests.py -k "not slow"` to identify the failing module, then inspect `logs/` for context |
| `codesentinel memory health` warns about missing policy snapshot | Execute `codesentinel policy dump --reason "bootstrap"` to refresh the guard data |

## Next Steps

1. Complete the Contributor Checklist in `CONTRIBUTING.md` if you intend to submit patches.
2. Review `QUICK_PUBLISH_REFERENCE.md` before attempting packaging or release tasks.
3. Bookmark `docs/guides/INDEX.md` for future reference—every new workflow is cataloged there.

## Revision History

| Date | Change | Author |
| --- | --- | --- |
| 2025-12-10 | Initial detailed getting-started guide | ORACL-Prime |
