# Deployment + Fleet — Canonical SSOT

## Metadata

- Owner: ORACL-Prime
- Stakeholder: joediggidyyy
- Status: active (stable-path canonical)
- Classification: internal

## Purpose

Single canonical SSOT entry point for deployment/fleet governance:

- what is authoritative vs derived
- how inventory and deployment tooling are expected to behave
- names-only and env-var-first constraints

## SSOT boundary (authoritative vs derived)

| Surface | Role | Path(s) |
|---|---|---|
| Inventory template | Authoritative template | `deployment/inventory.example.json` |
| Operator inventory | Local-only (gitignored) | `deployment/inventory.json` |
| Deployment tooling | Authoritative | `deployment/deploy_fleet.py`, `deployment/deploy_physical.ps1` |
| Gates | Authoritative evidence | `logs/behavioral/gates/gate_events.jsonl` |
| Staging payloads | Derived / environment-specific | `deployment/staging/**` |

## Non-negotiables

- Inventory must be env-var references only (no plaintext hostnames/usernames/key paths).
- Credentials are env-var-only.

## Entry points

- Deployment guide: `deployment/README.md`

## Change log

- 2025-12-30: Created as stable-path canonical SSOT entry point (pointer-layer only).
