# Security + Telemetry Integrations — Canonical SSOT

## Metadata

- Owner: ORACL-Prime
- Stakeholder: joediggidyyy
- Status: active (stable-path canonical)
- Classification: internal

## Purpose

Single canonical SSOT entry point for:

- security + redaction doctrine (names-only)
- telemetry evidence surfaces (what exists, where it lives)
- integration boundaries (what is allowed, what must fail-closed)

## Scope

In scope:
- credential handling doctrine (env-var-only)
- evidence discipline (append-only JSONL, gate events)
- telemetry and dashboard surfaces as derived views

Out of scope:
- vendor-specific setup guides (those remain in their domain docs, referenced below)

## SSOT boundary (authoritative vs derived)

| Surface | Role | Path(s) |
|---|---|---|
| Env-var standards | Authoritative | `.github/copilot-instructions.md` (names-only policy), `tools/config/env/expected_env_vars.json` |
| Task/status registry | Authoritative | `operations/tasks.json` |
| Gate evidence log | Authoritative evidence | `logs/behavioral/gates/gate_events.jsonl` |
| Security dashboards | Derived view | `docs/dashboards/room/SECURITY_DASHBOARD.md` |
| Health dashboards | Derived view | `docs/dashboards/room/HEALTH_DASHBOARD.md` |
| Reports & audits | Derived artifacts | `docs/reports/**` |
| Runtime logs | Evidence (append-only) | `logs/**` (treat as evidence; not configuration) |

## Non-negotiables

- No secrets committed. No hostnames committed. No device identifiers committed by default.
- Never log credential values.
- Prefer env-var references; do not rely on plaintext inventory fields.

## Evidence surfaces (pointers)

- Gates:
  - Preflight / BOD / EOD emit evidence to: `logs/behavioral/gates/gate_events.jsonl`
- SessionMemory health:
  - `codesentinel memory health --json` (names-only output)

## Entry points (supporting docs)

- Security policy docs: `docs/policies/**`
- Security dashboards (derived): `docs/dashboards/room/SECURITY_DASHBOARD.md`
- Vault operations: `docs/guides/VAULT_*` (names-only)

## Change log

- 2025-12-30: Created as stable-path canonical SSOT entry point (pointer-layer only).
