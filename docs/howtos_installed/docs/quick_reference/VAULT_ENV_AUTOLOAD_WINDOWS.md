# Windows Auto-Load for VAULT Environment Variables

**Audience:** Operator workstation / CORE node (Windows)

## Goal
After logon (or boot), the system should be **BOD-ready** with no manual prerequisite steps.

“BOD-ready” here means:
- VAULT integrity is enforced (no unauthorized edits)
- the operator shell has the SSOT-required env vars set (names-only validation)
- CORE credentials are present (CORE_* is mandatory)

This is achieved by running the existing VAULT loader non-interactively at logon and (optionally) persisting variables to the current user's environment so *new shells* inherit them automatically.

## Components
- Loader (applies to current PowerShell session; validates SSOT):
  - `tools/codesentinel/vault/Load-VaultCredentials.ps1`
  - Supports `-Profile operator_shell` and `-PersistUser`
- Scheduled task helper (registers an AtLogOn task):
  - `tools/windows/Register-CodesentinelVaultEnvLoaderTask.ps1`

## Non-interactive model (recommended)

### Option A (strictly no manual steps for new shells): Scheduled Task + PersistUser

1. Register a Scheduled Task (AtLogOn) to run the loader.
2. Enable `-PersistUser` so required variables are persisted to the current user's environment *after* SSOT validation passes.

This makes new PowerShell sessions inherit the variables without requiring the operator to run the loader manually.

### Option B (lower exposure, session-only): Scheduled Task without PersistUser

- The task runs at logon and prepares the environment for that task process.
- New shells may still require a loader run unless your terminal/profile is configured to run the loader at session start.

This reduces the “secrets stored in user env” exposure, but it is not the strongest interpretation of “no prerequisite steps” for every new shell.

## Recommended setup
- Register a Scheduled Task that runs at user logon:
  - Target: `tools/codesentinel/vault/Load-VaultCredentials.ps1`
  - Profile: `operator_shell` (CORE_* is mandatory in this profile)
  - Optional (recommended for “no manual steps”): `-PersistUser`

## Notes (security tradeoff)
- Persisting secrets into the user environment means the values are stored in the user profile environment.
- This may be required for the "no manual steps" operational model, but it increases exposure compared to session-only loading.
- Names-only discipline is maintained in logs and console output; values are never printed.

## Notes (scope / limitations)
- The BOD gate validates env state but does not mutate the *parent shell* environment. This is by design.
- If you require the operator shell to be ready without running the loader manually, you must use an OS-level autoload mechanism (e.g., Scheduled Task + PersistUser) or an equivalent profile-based hook.

## Validation
- BOD gate validates required env vars via SSOT (fail closed):
  - `tools/codesentinel/gates/gate_bod.py`
  - Exit code 40 indicates missing required env vars
