# Jobs + Execution — Canonical SSOT

## Metadata

- Owner: ORACL-Prime
- Stakeholder: joediggidyyy
- Status: active (stable-path canonical)
- Classification: internal

## Purpose

Single canonical SSOT entry point for jobs/execution governance:

- what "status" is and where it is authoritative
- how evidence is recorded
- how dashboards relate to the SSOT

## SSOT boundary (authoritative vs derived)

| Surface | Role | Path(s) |
|---|---|---|
| Task/status registry | Authoritative | `operations/tasks.json` |
| Gate evidence | Authoritative evidence | `logs/behavioral/gates/gate_events.jsonl` |
| QuestFrames | Planning spec | `docs/planning/questframes/**.json` |
| QuestStack (SessionMemory) | Authoritative | `.agent_session/task_stack.json`, `.agent_session/queststack_journal.jsonl` |
| QuestStack views (repo paperwork) | Derived view | `docs/operations/queststacks/**.md`, `logs/queststack/*` |
| Jobs dashboard | Derived view | `docs/dashboards/room/JOBS_DASHBOARD.md` |

## Operating rule

- Do not duplicate status tables into multiple docs.
- Status lives in `operations/tasks.json`.
- Dashboards are derived, refreshed from SSOT.
- Treat repo QuestStack paperwork (`docs/operations/queststacks/*`, `logs/queststack/*`) as derived/generated views; do not infer authoritative state from them.

## Entry points

- Jobs dashboard (derived): `docs/dashboards/room/JOBS_DASHBOARD.md`

## Change log

- 2025-12-30: Created as stable-path canonical SSOT entry point (pointer-layer only).
