# Canonical Virtual Environment Policy

## Metadata

| Field | Value |
| --- | --- |
| Document Title | PRIMARY VENV POLICY |
| Domain / Scope | DOC |
| Artifact Type | Policy |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/guides/PRIMARY_VENV_POLICY.md |

---


> **Relocation Notice:** Canonical edits live at `CodeSentinel/docs/policies/operations/OPERATIONS_POLICY/PP_OPS_PROTOCOL_POL_PRIMARY_VENV_20251115.md` with the JSON mirror under the same `pp/` directory. This guide copy is frozen post-pooling.

CodeSentinel now enforces a **dual-environment workflow**: a hardened `.venv-core/` environment for every security-sensitive operation, plus disposable sandboxes for everything else. Documentation is the source of truth, so the CLI, automation hooks, and human operators must follow the policy exactly as written here.

## 1. Core Environment (`.venv-core/`)

| Property | Requirement |
| --- | --- |
| Location | `CodeSentinel/.venv-core/` |
| Python Version | **3.14.x** (CLI prints a warning if mismatched) |
| TTL | **None** – never pruned, archived, or repurposed |
| Purpose | Run every privileged command: `codesentinel !!!!`, `codesentinel status`, doc/GUI workflows, release automation, and any action that mutates the repo state |
| Provisioning | `codesentinel venv ensure --primary --requirements requirements.txt` |
| Activation | Windows: `\.venv-core\Scripts\activate`; macOS/Linux: `source .venv-core/bin/activate` |

Additional guardrails:

- `.venv-core/` is recorded in `docs/index/venv_manifest.json` with `metadata.primary = true` and `ttl_exempt = true`. Automation refuses to prune it.
- GUI dependencies (Plotly, Kaleido, tkinter bindings) must stay installed inside `.venv-core/`; re-run `pip install -r requirements.txt` there after audits or rebuilds.
- Rebuild `.venv-core/` only when upgrading to a new Python 3.14 patch release or when security review demands a fresh virtual environment.

## 2. Sandboxed Environments (`.venv-*`)

| Property | Requirement |
| --- | --- |
| Naming | `.venv-<purpose>` (e.g., `.venv-tests`, `.venv-ops`) |
| TTL | Controlled via registry metadata / TTL markers. Safe to prune via `codesentinel venv prune`. |
| Provisioning | `codesentinel venv ensure --name tests --requirements requirements-dev.txt` |
| Usage | Beta testing, automation hooks, PoCs, or any workflow that should not contaminate `.venv-core/` |

Automation still archives these sandboxes before removal and logs lifecycle events to `docs/reports/maintenance/venv/*.json`.

## 3. Dual-Environment Workflow

1. **Always** activate `.venv-core/` before invoking CodeSentinel CLI commands.
2. When a sandbox is required (e.g., `.venv-tests`), create it **from inside** `.venv-core/` so dependency locks and audit logs capture the correct provenance.
3. Run experiments inside the sandbox, but return to `.venv-core/` to commit results, update documentation, or execute release tooling.
4. Document every sandbox in `venv_manifest.json` (or via `codesentinel venv inventory --json`) to keep ORACL tiers synchronized.

## 4. Operational Checklist

1. After cloning:

   ```cmd
   python -m codesentinel.cli venv ensure --primary --requirements requirements.txt
   .\.venv-core\Scripts\activate
   ```

2. For automation/test sandboxes:

   ```cmd
   python -m codesentinel.cli venv ensure --name tests --requirements requirements-dev.txt
   ```

3. **Never delete `.venv-core/`.** Use `codesentinel venv prune` only for `.venv-*` sandboxes.
4. If the GUI complains about missing Plotly/Kaleido, confirm you are inside `.venv-core/` and rerun:

   ```cmd
   pip install -r requirements.txt
   ```

This split keeps the security-first workflow intact while still allowing disposable experimentation under SEAM Protection™.
