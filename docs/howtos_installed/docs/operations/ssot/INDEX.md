# SSOT Canonicals (Operations)

This directory contains **stable-path canonical SSOT entry points** for operational domains.

## Rules

- These files are **names-only** (placeholders only; no secrets, identifiers, hostnames, or tokens).
- Each canonical declares an **SSOT boundary**:
  - **Authoritative**: source configuration / policy / registries
  - **Derived**: dashboards, reports, generated artifacts, logs (unless explicitly declared authoritative)
- Status SSOT remains `operations/tasks.json`.
- **Search hygiene**: the keyword `SSOT` is reserved for stable-path canonicals (this directory, and Brain-native SSOT indices under `brain/docs/operations/ssot/`). Other documents should prefer wording like "canonical", "authoritative", "derived", or "design proposal" and avoid `SSOT` in titles.

## Pointer-layer convention (recommended)

When updating existing docs (runbooks/guides/dashboards) without rewriting them, add a minimal pointer block near the top:

> Canonical entry point: `docs/operations/ssot/<DOMAIN>_SSOT.md`
> 
> Status registry: `operations/tasks.json`
> 
> Note: this document is supporting/derived; if it conflicts with the canonical entry point, treat the canonical as authoritative.

## Evidence surfaces (common)

Canonicals should prefer linking to evidence *surfaces* (paths), not pasting outputs.

- Status SSOT (authoritative): `operations/tasks.json`
- Gate events registry (authoritative evidence): `logs/behavioral/gates/gate_events.jsonl`
- QuestStack evidence trails (append-only evidence): `logs/queststack/*_evidence.jsonl`
- Dashboards (derived views, refreshed from SSOT/evidence): `docs/dashboards/room/*.md`

## Brain-native SSOT canonicals

The `SSOT` keyword is also used under Brain-native SSOT indices:

- Brain SSOT index: `brain/docs/operations/ssot/README.md`

## Canonical entry points

- Security + telemetry integrations: `docs/operations/ssot/SECURITY_AND_TELEMETRY_INTEGRATIONS_SSOT.md`
- CIDS ecosystem operations: `docs/operations/ssot/CIDS_ECOSYSTEM_SSOT.md`
- ORACode operations: `docs/operations/ssot/ORACODE_OPERATIONS_SSOT.md`
- ORACL Greek designations: `docs/operations/ssot/ORACL_GREEK_DESIGNATION_SCHEMA_SSOT.md`
- Deployment + fleet: `docs/operations/ssot/DEPLOYMENT_AND_FLEET_SSOT.md`
- Jobs + execution: `docs/operations/ssot/JOBS_AND_EXECUTION_SSOT.md`

## Related planning

- Remediation plan: `docs/operations/plans/SSOT_DOMAIN_CANONICAL_REMEDIATION_PLAN_20251230.{md,json}`
- Filesystem audit: `docs/reports/maintenance/ssot/SSOT_DOMAIN_CANONICAL_FILESYSTEM_AUDIT_20251230.{md,json}`
