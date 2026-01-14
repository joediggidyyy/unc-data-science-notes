# CIDS Ecosystem Operations — Canonical SSOT

## Metadata

- Owner: ORACL-Prime
- Stakeholder: joediggidyyy
- Status: active (stable-path canonical)
- Classification: internal

## Purpose

Single canonical SSOT entry point for the CIDS ecosystem’s operational meaning:

- what is authoritative vs derived
- where evidence lives
- how endpoint semantics are described (without leaking identifiers)

## Scope

In scope:
- operator-facing entry points and evidence surfaces
- endpoint meaning taxonomy (UI vs heartbeat ingress)

Out of scope:
- full UI/IA design (kept in planning docs)

## SSOT boundary (authoritative vs derived)

| Surface | Role | Path(s) |
|---|---|---|
| Job status registry | Authoritative | `operations/tasks.json` |
| As-built operational architecture | Authoritative narrative | `docs/reports/CIDS_ECOSYSTEM_OPERATIONAL_ARCHITECTURE.md` |
| Gate evidence | Authoritative evidence | `logs/behavioral/gates/gate_events.jsonl` |
| Dashboards | Derived view | `docs/dashboards/room/CIDS_DASHBOARD.md`, `docs/dashboards/room/MASTER_DASHBOARD.md` |
| UI wireframes | Planning artifact | `docs/reports/ui/DASHBOARD_MULTI_PAGE_REFACTOR_WIREFRAMES_20251229.md` |

## Endpoint semantics (names-only)

- "Dashboard UI" and "Sentry heartbeat ingress" may share host/port; they are **not the same signal**.
- Rule: do **not** treat a heartbeat ingress endpoint as proof that the UI is healthy.

Example mapping (placeholders only):

- Dashboard UI: `https://<DASHBOARD_HOST>:5000/`
- Heartbeat ingress: `https://<DASHBOARD_HOST>:5000/api/heartbeat`
- Diagnostic health (not proof of UI health): `https://<DASHBOARD_HOST>:5000/api/health`

## Evidence surfaces (pointers)

- Gates: `logs/behavioral/gates/gate_events.jsonl`
- Dashboards refreshed from SSOT:
  - `docs/dashboards/room/JOBS_DASHBOARD.md`
  - `docs/dashboards/room/MASTER_DASHBOARD.md`

## Entry points (supporting docs)

- CIDS parent tracker (navigator): `docs/operations/plans/CIDS_PARENT_TRACKER_20251229.md`
- CIDS dashboards (derived): `docs/dashboards/room/CIDS_DASHBOARD.md`

## Change log

- 2025-12-30: Created as stable-path canonical SSOT entry point (pointer-layer only).
