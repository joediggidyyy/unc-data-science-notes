# ORACL Greek Designation Schema (SSOT)

This document defines the canonical meaning of **ORACL Greek designations** used to label agents, runs, dashboards, simulations, and incident modes.

## Rules

- **Designations encode purpose and authority**, not “rank”.
- **Production-impacting actions must never be initiated from simulation-only designations.**
- Designations should be assigned per *run/session* and recorded in logs (e.g., gate events / QuestStack evidence) when available.
- If an environment has additional local labels, they must map back to one of the canonical designations below.

## Canonical designation set

These are the primary, expected designations for CodeSentinel operations.

### $\Alpha$ (ALPHA) — Primary execution (real-world intent)

**Purpose:** Execute changes intended to affect real systems (repo state, deployments, policy enforcement).

**Typical contexts:**
- normal operations on a real workspace
- approved remediation work

**Constraints:**
- Must honor SEAM ordering (Security > Efficiency > Awareness > Minimalism).
- Must use archive-first procedures for destructive filesystem operations.

### $\Beta$ (BETA) — Verification / validation

**Purpose:** Validate results, reproduce, test, and confirm behavior.

**Typical contexts:**
- running gates/tests
- verifying dashboards and SSOT pointers

**Constraints:**
- Should prefer read-only actions where possible.
- Can propose fixes; execution belongs to $\Alpha$ or a delegated executor.

### $\Gamma$ (GAMMA) — Simulation / what-if (non-production)

**Purpose:** Explore scenarios safely without impacting production state.

**Typical contexts:**
- Calamum-style “what if X fails?” rehearsal
- sandboxed design exercises

**Constraints:**
- Must not perform real network or deployment actions.
- Must clearly mark outputs as simulation/estimates.

### $\Delta$ (DELTA) — Incident response / recovery

**Purpose:** Stabilize and recover from outages, corruption, or “system unreachable” incidents.

**Typical contexts:**
- emergency restore / rebuild procedures
- recovery after accidental moves/archives (e.g., UNC prune fallout)

**Constraints:**
- Prefer reversible operations.
- Must document the recovery rationale and evidence paths.

### $\Epsilon$ (EPSILON) — Audit / observation

**Purpose:** Observe and report, generate inventories, and surface discrepancies.

**Typical contexts:**
- filesystem surveys
- compliance snapshots

**Constraints:**
- Read-only by default.

### $\Pi$ (PI) — Policy / guardrail enforcement

**Purpose:** Enforce policy invariants (secrets handling, md/json pairing rules, guardrails).

**Typical contexts:**
- policy verification runs
- instruction pair synchronization checks

**Constraints:**
- Changes are allowed only when explicitly in “fix” mode and must be minimal.

## Calamum mapping

When operating under the **Calamum framework** (calamity planning / simulation / response), use these mappings:

- **Calamum-Sim**: $\Gamma$ (scenario rehearsal, no production impact)
- **Calamum-IR**: $\Delta$ (real recovery actions)
- **Calamum-Audit**: $\Epsilon$ (evidence gathering and after-action reports)

## Logging / labeling convention

Recommended label format (names-only, ASCII-safe):

- `ORACL:<DESIGNATION>:<CONTEXT>:<SHORT_LABEL>`

Examples:

- `ORACL:ALPHA:ops:dashboard-refresh`
- `ORACL:GAMMA:sim:router-outage-rehearsal`
- `ORACL:DELTA:recovery:unc-prune-rollback`

## Machine-readable schema

Canonical JSON source:

- `docs/schemas/oracl_greek_designations.schema.json`
