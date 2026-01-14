# CodeSentinel Shipping Document Classification

## Metadata

| Field | Value |
| --- | --- |
| Document Title | SHIP DOCUMENT CLASSIFICATION |
| Domain / Scope | ARCH |
| Artifact Type | Document |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/schemas/SHIP_DOCUMENT_CLASSIFICATION.md |

---


This matrix captures which documents must ship with the production release based on the rule:

> **Ship only assets that dictate system operations or define ORACL behavior (matching the current ORACL learning entity).**

All other documents—reports, audits, analytics, historical logs—remain internal-only foundations for R&D teams.

---

## Shipping set (must accompany production build)

| Document | Rationale |
| --- | --- |
| `docs/AI_AGENT_RULES.md` | Canonical operating rules for CodeSentinel agents; required so downstream operators enforce the same guardrails. |
| `docs/ORACL_MEMORY_ARCHITECTURE.md` | Describes the three-tier Session/Context/Intelligence memory construct that must be replicated to match this environment. |
| `docs/ORACL_MEMORY_ECOSYSTEM_PROPOSAL.md` | Supplements the architecture doc with lifecycle, replication, and governance details so ORACL behaves identically at launch. |
| `docs/ROOT_CLEANUP_AUTOMATION.md` | Defines the repository root-policy engine; shipping teams need it to keep SEAM protections engaged. |
| `docs/SCAN_CLEAN_WORKFLOW.md` | Prescribes the monitoring/scan cadence and triggers; production automations depend on the documented workflow. |
| `docs/TOOL_MANAGEMENT_POLICY.md` | Explains how ORACL onboards or revokes tools—critical for maintaining parity with this environment’s capabilities. |
| `docs/ENTERPRISE_INTEGRATION_GUIDE.md` | Shows how to embed CodeSentinel into enterprise pipelines; necessary for operators to stand up the service. |
| `docs/AGENT_INTEGRATION_STATUS_SYSTEM.md` | Defines the status telemetry contract ORACL consumes to reason about agent readiness. |
| `docs/AGENT_INSTRUCTIONS.md` | Provides the official operational instructions referenced by codes and automation. |
| `docs/AGENT_QUICK_REFERENCE.md` | Compact version of the above for on-call engineers; still part of the required operating surface. |
| `docs/SESSION_IMPLEMENTATION_ANALYSIS_20251107.md` | Captures how ORACL sessions are recorded/promoted; required for state continuity. |
| `docs/SESSION_COMPLETION_SUMMARY.md` | Defines completion/handoff semantics between tiers, ensuring Learning Tier parity. |

> **Note:** If any of the above evolve, this file must be updated so the shipping manifest always matches the contract engineers rely on.

---

## Internal-only reference set (do not ship by default)

These documents stay within engineering because they are analytical artifacts, retrospectives, or generated reports. They can be provided on request but are not required for the baseline production rollout.

- `docs/ADVANCED_ANALYTICS_FRAMEWORK.md`
- `docs/AUTOMATED_TASKS_AUDIT_20251107.md`
- `docs/CLI_AGENT_INTEGRATION_ANALYSIS.md`
- `docs/DOCUMENT_FORMATTING_AUTOMATION.md`
- `docs/FEATURE_*` analysis reports (e.g., `FEATURE_DISTRIBUTED_AGENT_INSTRUCTION_STRATEGY.md`)
- `docs/FINAL_COMPLETION_SUMMARY_20251107.md`
- `docs/FORMATTING_IMPLEMENTATION_SUMMARY.md`
- `docs/GOVERNANCE_T0-5_ESTABLISHMENT.md`
- `docs/HELP_EXAMPLES_OPTIMIZATION.md`
- `docs/INFRASTRUCTURE_HARDENING_REPORT.md`
- `docs/NOVEL_DATA_FEDERATION_*` planning/progress artifacts
- `docs/UPDATE_COMMAND_IMPLEMENTATION_SUMMARY.md`
- `docs/metrics/**` (including `METRICS_DATA_RETENTION.md` and `legacy_reports/`)
- `docs/reports/**` (all generated dashboards)
- Any other ad-hoc audits or historical records stored under `docs/audit/`, `docs/reports/`, or `docs/metrics/`

---

## Review notes & next steps

1. **Validation review** – Walk through the shipping list together and confirm no missing system-operation or ORACL-behavior doc.
2. **Process enforcement** – Tie CI or release tooling to this classification so only the “shipping set” is bundled automatically.
3. **Change tracking** – Whenever a document changes categories, update this matrix and the corresponding release manifest.

This document is intentionally lightweight so we can iterate on the mix during review sessions without digging through historical chat logs.
