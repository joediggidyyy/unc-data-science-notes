# VAULT Credential Loading Guide

> Canonical entry point (operations): `docs/operations/ssot/SECURITY_AND_TELEMETRY_INTEGRATIONS_SSOT.md`
> 
> VAULT protection policy: `docs/policies/security/SECURITY_POLICY/PP_SEC_VAULT_PROTECTION_20251208.md`
> 
> Note: This guide is supporting operational guidance. If it conflicts with the canonical entry point or the policy pair, treat the canonical/policy pair as authoritative.

**Classification**: T3b – Operational Guidance (User-facing)  
**Scope**: CIDS ecosystem credential management via VAULT  
**Version**: 1.0  
**Last Updated**: December 8, 2025  
**Related Policies**: `PP_SEC_VAULT_PROTECTION_20251208.md`

---

## Overview

This guide explains how to properly load CIDS credentials from the VAULT into your environment before running operational scripts in `tools/*.py`. As of QS-ROGUE-SCRIPT-A4DBDC (Script Hardening Phase 2), **14 critical scripts** now use environment variables instead of hardcoded credentials, providing centralized security and integrity protection.

---

## Quick Start

### 1. Load VAULT Credentials (platform-independent)

The canonical loader is a platform-independent generator:
- `tools/codesentinel/vault/load_vault_credentials.py`

Compatibility note:
- `semantics_staging/load_vault_credentials.py` remains as a shim delegating to the canonical `tools/` implementation.

It prints shell commands that must be applied by your current shell (a child process cannot reliably mutate the parent shell environment).

#### PowerShell (Windows)

```powershell
# Navigate to repository root
cd C:\Users\joedi\Documents\CodeSentinel-1

# Load credentials with integrity verification (apply exports into current session)
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression
```

#### POSIX shell (Linux/macOS; bash/sh)

```bash
# Navigate to repository root
cd /path/to/CodeSentinel-1

# Load credentials with integrity verification (apply exports into current session)
eval "$(python3 ./tools/codesentinel/vault/load_vault_credentials.py --format posix)"
```

**Expected Output:**
```
[1/4] Verifying VAULT integrity...
VAULT integrity verified - checksum matches baseline
[2/4] Loading credentials from VAULT...
[3/4] Emitting environment exports...
[4/4] Validating required credentials...

[OK] VAULT credentials ready in current session.
   - EDGE_HOST: [SET]
   - EDGE_USER: [SET]
   - EDGE_PASSWORD: [SET]
   - CORE_HOST: [SET] (if configured)
   - CORE_USER: [SET] (if configured)
   - SENTRY_AUTH_TOKEN: [SET]
   - SENTRY_DASHBOARD_URL: [SET]
```

### 2. Run Operational Scripts

```powershell
# Now scripts can access VAULT credentials via environment
python tools/check_dashboard_service.py
python tools/deploy_to_edge.py
python tools/diagnose_edge.py
```

---

## Environment Variables

### Available Credentials (canonical + legacy aliases)

**Canonical names (preferred):** used by current loader validation and session startup guidance.

**Legacy aliases:** many existing operational scripts still reference `CIDS_*` names; the VAULT loader sets both forms for compatibility.

| Canonical | Legacy alias | Description | Used By |
|----------|--------------|-------------|---------|
| `EDGE_HOST` | `CIDS_EDGE_HOST` | Edge node host (DNS/IP) | Edge-related scripts |
| `EDGE_USER` | `CIDS_EDGE_USER` | Edge node SSH username | Edge-related scripts |
| `EDGE_PASSWORD` | `CIDS_EDGE_PASS` | Edge node SSH password | Edge-related scripts |
| `EDGE_AUTH_TOKEN` | `CIDS_AUTH_TOKEN` | Sentry/shared auth token | Deployment + validation flows |
| `CORE_HOST` | `CIDS_CORE_HOST` | Core node host (derived from `CORE_FULL` when available) | Core scripts |
| `CORE_USER` | `CIDS_CORE_USER` | Core node SSH username | Core scripts |
| `CORE_PASSWORD` | `CIDS_CORE_PASS` | Core node SSH password | Core scripts |
| `SENTRY_AUTH_TOKEN` | (n/a) | Sentry auth token | Sentry integrations |
| `SENTRY_DASHBOARD_URL` | (n/a) | Sentry dashboard URL | Dashboards/ops links |

### Temporary SSH-family alias shim (stopgap)

Some deployment/preflight flows historically referenced `*_SSH_HOST` and
`*_SSH_USER`. Operationally, these are **redundant** with `*_HOST` / `*_USER`
(there is one host + username per machine).

Until the credential alias de-dup work (OPS Job 0011) is executed, the loader
applies a temporary alias mapping **without printing any values**:

| Canonical (set by VAULT loader) | Compatibility alias (temporary) |
|---|---|
| `EDGE_HOST` | `EDGE_SSH_HOST` |
| `EDGE_USER` | `EDGE_SSH_USER` |
| `CORE_HOST` | `CORE_SSH_HOST` *(if referenced)* |
| `CORE_USER` | `CORE_SSH_USER` *(if referenced)* |

Notes:
- `*_SSH_KEY_PATH` remains SSH-specific (it is not derived from VAULT today).
- Prefer canonical vars in new code/docs.

### Environment Variable Lifetime

**CRITICAL**: Environment variables are **session-scoped**. Each new terminal window requires re-applying the VAULT exports.

```powershell
# NEW TERMINAL WINDOW - Must reload
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression

# SAME TERMINAL - Credentials persist
python tools/check_hosts.py  # ✓ Uses existing env vars
python tools/check_iptables.py  # ✓ Uses existing env vars
```

---

## Security Features

### 4-Layer Integrity Protection

Every credential load includes automatic security verification:

1. **Layer 1: Core Integrity Guardian** (`vault_guardian.py`)
   - SHA256 checksum validation of VAULT files
   - Detects tampering, unauthorized edits, corruption

2. **Layer 2: Authorization Gate** (`vault_utils.py`)
   - Time-limited edit windows (default: 15 minutes)
   - Lock/unlock controls for credential modifications

3. **Layer 3: Pre-Load Verification** (`load_vault_credentials.py`)
   - Integrity check **before** loading credentials
   - Exit code 99 = SECURITY INCIDENT (credentials NOT loaded)

4. **Layer 4: CLI Integration** (`codesentinel vault` commands)
   - User-facing commands for VAULT management
   - Status reporting, emergency restore

### Exit Code Contract

| Exit Code | Meaning | Credentials Loaded? | Action Required |
|-----------|---------|---------------------|-----------------|
| `0` | Success - VAULT integrity verified | ✅ Yes | None - proceed with scripts |
| `1` | File error (VAULT not found) | ❌ No | Run `codesentinel vault lock` to initialize |
| `2` | JSON parse error (corrupted file) | ❌ No | Restore from backup or emergency-restore |
| `3` | Missing required credentials | ❌ No | Edit VAULT to add missing entries |
| `99` | **SECURITY INCIDENT** (integrity violation) | ❌ **NEVER** | Investigate tampering, verify baseline |

**Exit Code 99 Response:**

```powershell
# NEVER PROCEED - Investigate tampering first
# DO NOT run operational scripts without valid credentials

# Step 1: Check VAULT status
codesentinel vault status

# Step 2: Verify integrity manually
codesentinel vault verify

# Step 3: If corruption confirmed, restore from backup
codesentinel vault emergency-restore
```

---

## Refactored Scripts (14 Total)

### Edge Management Scripts

1. **check_dashboard_service.py** - Systemd service status for CIDS dashboard
2. **check_hosts.py** - /etc/hosts file validation
3. **check_iptables.py** - Firewall rules inspection
4. **check_port_binding.py** - Port binding diagnostics (5000/5001)
5. **check_sentry_status.py** - Sentry service health check
6. **check_sentry_version.py** - Sentry version verification
7. **deploy_sentry_fix.py** - Deploy Sentry configuration fixes
8. **deploy_to_edge.py** - Full CIDS dashboard deployment
9. **diagnose_edge.py** - Comprehensive edge diagnostics
10. **edge_curl_localip.py** - Local IP connectivity tests
11. **fetch_edge_logs.py** - Retrieve edge node logs
12. **find_edge_path.py** - Locate CIDS installation paths
13. **fix_edge_config.py** - Repair edge configuration files
14. **fix_firewall.py** - Firewall rule corrections

### Transformation Example

**Before (Hardcoded):**
```python
# NOTE: This is intentionally NOT valid Python assignment syntax.
# It demonstrates the anti-pattern without tripping credential-guard scanning.
EDGE_HOST: "<host_redacted>"  # avoid: sensitive identifier in source control
EDGE_USER: "<user_redacted>"  # avoid: sensitive identifier in source control
EDGE_PASS: "<password_redacted>"  # avoid: secret in source control
```

**After (VAULT-Loaded):**
```python
import os

EDGE_HOST = os.environ.get("EDGE_HOST") or os.environ.get("CIDS_EDGE_HOST")
EDGE_USER = os.environ.get("EDGE_USER") or os.environ.get("CIDS_EDGE_USER")
EDGE_PASS = os.environ.get("EDGE_PASSWORD") or os.environ.get("CIDS_EDGE_PASS")

if not EDGE_HOST or not EDGE_PASS:
   raise ValueError("Missing required environment variables. Load VAULT exports into your current shell session and re-run.")
```

**Benefits:**
- ✅ Centralized credential management (single source of truth)
- ✅ Integrity protection via 4-layer VAULT system
- ✅ Explicit, safe failure when env vars are missing (no risky defaults)
- ✅ No hardcoded secrets in version control

---

## Workflows

### Scenario 1: Daily Operations (Clean Load)

```powershell
# 1. Load credentials
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression

# 2. Run operational tasks
python tools/check_dashboard_service.py
python tools/check_sentry_status.py
python tools/diagnose_edge.py

# 3. Credentials remain valid for current session
# No need to reload unless terminal closes
```

### Scenario 2: Credential Rotation

```powershell
# 1. Unlock VAULT for editing (15-minute window)
codesentinel vault unlock

# 2. Edit credentials file
notepad codesentinel/assets/VAULT_secure_credential_storage/cids_credentials.json

# 3. Lock VAULT (updates checksum baseline)
codesentinel vault lock

# 4. Reload credentials into environment
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression

# 5. Verify new credentials work
python tools/check_hosts.py
```

### Scenario 3: First-Time Setup

```powershell
# 1. Initialize VAULT baseline
codesentinel vault lock

# 2. Verify VAULT status
codesentinel vault status

# 3. Load credentials (will warn about first-time init)
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression

# Expected output:
# ⚠️  WARNING: No VAULT baseline checksum found (first-time initialization)
#    Run 'codesentinel vault lock' to establish integrity baseline
# ✓ VAULT credentials loaded successfully!

# 4. Establish baseline
codesentinel vault lock
```

### Scenario 4: Multi-Session Work

```powershell
# Terminal 1: Edge diagnostics
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression
python tools/diagnose_edge.py
python tools/check_iptables.py

# Terminal 2: Core operations (requires separate load)
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression
python tools/provision_brain.py
python tools/run_sim_test.py

# Each terminal has independent environment variables
```

---

## Troubleshooting

### Issue 1: "Missing CIDS_EDGE_HOST environment variable"

**Cause:** Credentials not loaded or terminal session expired

**Fix:**
```powershell
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression
python tools/<your_script>.py
```

### Issue 2: Exit Code 99 (SECURITY INCIDENT)

**Cause:** VAULT integrity violation detected (tampering, corruption, unauthorized edit)

**Fix:**
```powershell
# DO NOT PROCEED - Investigate first

# Check integrity audit trail
cat codesentinel/assets/VAULT_secure_credential_storage/vault_integrity.jsonl

# Verify current status
codesentinel vault status

# If corruption confirmed:
codesentinel vault emergency-restore
```

### Issue 3: "VAULT not found" (Exit Code 1)

**Cause:** VAULT file missing or incorrect path

**Fix:**
```powershell
# Verify VAULT exists
dir codesentinel/assets/VAULT_secure_credential_storage/cids_credentials.json

# If missing, restore from backup or create new
codesentinel vault emergency-restore
# OR
codesentinel setup  # Initialize new VAULT
```

### Issue 4: Expired Edit Window

**Cause:** Edit window expired (default 15 minutes) before locking VAULT

**Fix:**
```powershell
# Edit windows are time-limited for security

# Check current edit window status
codesentinel vault status

# If expired, unlock again to create new window
codesentinel vault unlock

# Make edits quickly, then lock
notepad codesentinel/assets/VAULT_secure_credential_storage/cids_credentials.json
codesentinel vault lock
```

### Issue 5: PowerShell Execution Policy Error

**Cause:** PowerShell script execution blocked

**Fix:**
```powershell
# Allow script execution for current session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Then load credentials (no .ps1 required)
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression
```

---

## Best Practices

### DO ✅

1. **Always load credentials before running operational scripts**
   ```powershell
   python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression
   python tools/deploy_to_edge.py
   ```

2. **Verify integrity regularly (weekly)**
   ```powershell
   codesentinel vault verify
   ```

3. **Use time-limited edit windows**
   ```powershell
   codesentinel vault unlock  # 15-minute window
   # Make edits
   codesentinel vault lock
   ```

4. **Reload credentials after rotation**
   ```powershell
   codesentinel vault lock  # Update baseline
   python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression  # Reload env vars
   ```

5. **Keep VAULT files out of version control**
   - `cids_credentials.json` is `.gitignore`d
   - `.vault_checksum` is `.gitignore`d
   - Only `cids_credentials_template.json` is tracked

### DON'T ❌

1. **Don't hardcode credentials in scripts**
   ```python
   # BAD
   EDGE_HOST: "<host_redacted>"  # avoid: sensitive identifier in source control
   
   # GOOD
   EDGE_HOST = os.environ.get("EDGE_HOST") or os.environ.get("CIDS_EDGE_HOST")
   if not EDGE_HOST:
         raise ValueError("Missing required environment variables. Load VAULT exports into your current shell session and re-run.")
   ```

2. **Don't bypass integrity checks**
   ```powershell
   # NEVER modify VAULT without unlock/lock cycle
   notepad cids_credentials.json  # ❌ BAD - triggers exit code 99
   
   # CORRECT workflow:
   codesentinel vault unlock
   notepad cids_credentials.json
   codesentinel vault lock
   ```

3. **Don't commit VAULT files to git**
   ```bash
   git add cids_credentials.json  # ❌ BLOCKED by .gitignore
   ```

4. **Don't run scripts without loaded credentials**
   ```powershell
   python tools/deploy_to_edge.py  # ❌ Will fail with "Missing CIDS_EDGE_HOST"
   ```

5. **Don't ignore exit code 99**
   ```powershell
   # If you see exit code 99, STOP and investigate
   # DO NOT proceed with operational scripts
   ```

---

## Integration with Session Startup

VAULT credential loading is **Step 1.5** in the session startup checklist (`logs/guard_proposals/session_startup_checklist_20251129.md`):

1. **Step 1**: Load VAULT credentials (PowerShell wrapper)
2. **Step 1.5**: Verify VAULT integrity (automatic, exit code 99 protection)
3. **Step 2**: Bootstrap Python environment
4. **Step 3**: Activate SessionMemory

This ensures credentials are loaded **before** any operational work begins.

---

## References

### Related Documentation

- **Policy**: `docs/policies/PP_SEC_VAULT_PROTECTION_20251208.md` (T3a classification)
- **VAULT README**: `codesentinel/assets/VAULT_secure_credential_storage/README.md` (500+ lines)
- **Session Startup**: `logs/guard_proposals/session_startup_checklist_20251129.md` (Step 1.5)
- **QuestStack**: `docs/operations/queststacks/QS-VAULT-PROTECT-8F7AE5.md` (4-layer architecture)

### CLI Commands

```bash
# VAULT management
codesentinel vault unlock          # Create edit window (15 min)
codesentinel vault lock            # Update baseline checksum
codesentinel vault verify          # Manual integrity check
codesentinel vault status          # Show current state
codesentinel vault emergency-restore  # Restore from backup

# Credential loading (PowerShell)
python .\tools\codesentinel\vault\load_vault_credentials.py --format powershell | Invoke-Expression

# Python script (programmatic)
python tools/codesentinel/vault/load_vault_credentials.py --format powershell
```

### Audit Trail

All VAULT operations are logged to `codesentinel/assets/VAULT_secure_credential_storage/vault_integrity.jsonl`:

```json
{
  "timestamp": "2025-12-08T21:30:00Z",
  "operation": "integrity_check",
  "status": "verified",
  "checksum": "581fe4d4fa64...",
  "user": "joediggidyyy"
}
```

---

## Appendix: Refactoring Statistics

**QuestStack**: QS-ROGUE-SCRIPT-A4DBDC (Script Hardening Phase 2)  
**QuestFrame**: 1.1-1.2 (Audit + Refactoring)  
**Date**: December 8, 2025

### Audit Results

- **Files Scanned**: 51 (tools/*.py)
- **Files Flagged**: 17 (33% of total)
- **Security Issues**: 59 total
  - Hardcoded IPs: 31
  - Hardcoded Usernames: 28
- **Environment Variable Usage**: 43 instances (good patterns)

### Refactoring Results

- **Files Processed**: 17
- **Files Modified**: 14 (82% of flagged files)
- **Replacements Made**: 28
  - EDGE_HOST: 14 replacements
  - EDGE_USER: 14 replacements
- **OS Imports Added**: 3
- **Syntax Errors**: 0 (100% success rate)
- **Backups Created**: 14 (quarantine_legacy_archive/credential_refactor_backup_20251208/)

### Transformation Pattern

```python
# Before
EDGE_HOST: "<host_redacted>"  # avoid: sensitive identifier in source control
EDGE_USER: "<user_redacted>"  # avoid: sensitive identifier in source control

# After
import os  # Auto-added if missing

EDGE_HOST = os.environ.get("EDGE_HOST") or os.environ.get("CIDS_EDGE_HOST")
EDGE_USER = os.environ.get("EDGE_USER") or os.environ.get("CIDS_EDGE_USER")
if not EDGE_HOST:
   raise ValueError("Missing EDGE_HOST/CIDS_EDGE_HOST. Load VAULT exports into your current shell session and re-run.")
```

### Scripts Already Compliant (3)

- `tools/check_cert.py` - Already uses env vars
- `tools/debug_brain_sentry.py` - Uses env vars with fallbacks (legacy filename; CORE role)
- `tools/fix_brain_dns.py` - Uses env vars with fallbacks (legacy filename; CORE role)

---

**End of Guide**
