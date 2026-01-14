# ORACode Operations — Canonical SSOT

## Metadata

- Owner: ORACL-Prime
- Stakeholder: joediggidyyy
- Status: active (stable-path canonical)
- Classification: internal

## Purpose

Single canonical SSOT entry point for ORACode operational rules, especially the "source vs artifact" boundary and recursion prohibitions.

## SSOT boundary (authoritative vs derived)

| Surface | Role | Path(s) |
|---|---|---|
| Graph integrity policy | Authoritative | `docs/architecture/oracode/GRAPH_INTEGRITY_POLICY.md` |
| ORACode source code | Authoritative | `codesentinel/**`, `tools/oracode/**` |
| Weighted graph index | Derived output | `semantics_vault/oracl_index/weighted_graph_index.json` |
| Runtime telemetry | Evidence (derived) | `logs/**` |
| Archives | Opaque nodes | `archive/**`, `quarantine_legacy_archive/**` |

## Non-negotiables

- Do not treat derived artifacts (graph indices, dashboards, logs) as configuration.
- Do not scan `semantics_vault/` or `logs/` for edges.

## Execution entry points

- Post-job gate (graph rebuild lane): `tools/codesentinel/gates/gate_post_job.py`
- Graph rebuild tooling: `tools/oracode/**`

## Change log

- 2025-12-30: Created as stable-path canonical SSOT entry point (pointer-layer only).
