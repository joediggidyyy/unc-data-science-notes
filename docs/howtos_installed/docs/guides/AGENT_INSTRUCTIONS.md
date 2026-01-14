# [AGENT-USE] Documentation Operations Agent Instructions

> **Identity Directive:** Within CodeSentinel, refer to Joe Waller as `joediggidyyy`, and refer to GitHub Copilot as `ORACL` / `ORACL-Prime`. Use these names in every interaction.

**Classification**: T4b – Infrastructure & Procedural Agent Documentation  
**Scope**: Creation, maintenance, and archival of content under `docs/` (architecture, guides, reports, quick references)  
**Target Users**: Agents publishing or refactoring CodeSentinel documentation  
**Version**: 1.1  
**Last Updated**: November 23, 2025

---

## Quick Authority Reference

| Operation | Authority | Requires Approval |
|-----------|-----------|-------------------|
| Create Tier 2 doc (guides, quick refs) | Agent | No |
| Create Tier 1 doc (architecture, policy) | Agent | Yes (user verification) |
| Modify Tier 2 doc | Agent | No (minor), Yes (major structural changes) |
| Modify Tier 1 doc | Agent | Yes (explicit approval) |
| Delete Tier 2 doc | Agent | Yes (user approval + archive) |
| Delete Tier 1 doc | Agent | Yes (explicit instruction + archive proof) |
| Archive document | Agent | Yes (verification + metadata) |
| Update README summaries | Agent | No |
| Publish release notes | Agent | No |

**Reference**: `docs/architecture/DOCUMENT_CLASSIFICATION.md` – classification tiers & authority matrices

---

## Domain Overview

The documentation tree communicates policy, procedures, and operational state.

- **Architecture** – Permanent policies, classification rules, SEAM foundations.
- **Guides** – How-to content, onboarding playbooks, integration walk-throughs.
- **Reports & Logs** – Audit history, automation output, ORACL summaries.
- **Planning & Operations** – Tactical plans, OKRs, and ongoing programs.

Guiding principles:

1. **Truthfulness** – Every doc must reflect the current codebase and workflows.
2. **Traceability** – Include metadata (version, classification, last updated).
3. **ASCII compatibility** – UI can use UTF-8, but console snippets stay ASCII-safe.
4. **Non-destructive changes** – Archive prior versions rather than deleting.
5. **Single source of truth** – Link to canonical documents instead of duplicating policy text.

### Machine-readable policy

- All AGENT_INSTRUCTIONS.md files must publish a matching `.json` file. The `.json` is the official machine-readable representation used by agents and automation; markdown is a human-facing view. CI will enforce md/json synchronization; mismatches cause the validation gate to fail.

---

## Documentation Workflow

1. **Scope & classification** – Determine tier (0–4) and record it in the header.
2. **Authority check** – Confirm approvals required per tier before editing.
3. **Drafting** – Use consistent Markdown headings, callouts, and tables; add repository-relative links.
4. **Validation** – Run markdown lints (MD001/MD025/MD009) and ensure examples execute.
5. **Archival** – Move superseded docs into `archive/` with metadata JSON.
6. **Publishing** – Update backlinks/indexes (`docs/index/docs_manifest.json`) so discovery tools stay accurate.
7. **Session memory** – Log major documentation decisions with `SessionMemory.log_decision()` for ORACL recall.

---

## Classification Guidelines

- Tier 4 (Procedural): Satellite instructions, quick checklists. Editable with agent approval.
- Tier 3 (Operational): Planning docs, sprint notes. Archive quarterly.
- Tier 2 (Informational): Guides/tutorials. Maintain changelog sections for high-traffic pages.
- Tier 1 (Foundational): Architecture, policy, security doctrine. Require explicit owner approval and dual-review.
- Always embed the tier, version, owner, and review date in the metadata block.

Decision helpers:

- **Does the doc govern system-wide behavior?** → Tier 1.
- **Is it a “how-to” for a narrow audience?** → Tier 2/3.
- **Is it machine-facing or a quick reference inside another doc?** → Tier 4.

---

## Common Documentation Patterns

- **Structure**: Title → Metadata → Executive summary → Procedures → Validation → References.
- **Callouts**: Use block quotes for directives, fenced blocks for commands, numbered steps for procedures.
- **Tables**: Prefer Markdown tables for authority matrices and decision trees.
- **Cross-linking**: Reference related docs using relative paths with the repo prefix (e.g., `CodeSentinel/docs/guides/...`).
- **Change tracking**: Append a "Revision History" list for Tier 1–2 documents.

---

## Archival Procedures

1. **Eligibility** – Determine whether the document is superseded, deprecated, or moved.
2. **Archive path** – Mirror the source tree inside `archive/{active|inactive}/[tier]/...`.
3. **Metadata** – Create or update `metadata.json` capturing: tier, author, archived_date (UTC), rationale, replacements.
4. **Cross-references** – Update backlinks to point to the new canonical location.
5. **Validation** – Ensure archived files open cleanly (UTF-8) and are listed in manifests.
6. **Git history** – Record archival in commit message (`archive: move <doc>`), noting ticket/issue.

---

## Troubleshooting Guide

| Symptom | Likely Cause | Corrective Action |
|---------|--------------|-------------------|
| Markdown lint failures (MD025, MD009) | Duplicate H1 or trailing spaces | Normalize heading hierarchy, trim whitespace |
| Broken internal links | Path moved without updating references | Run link checker (`tools/docs/link_audit.py`) and fix relative paths |
| Out-of-date metadata | Document edited without updating header | Refresh version/date/owner block and log decision |
| Missing archive metadata | File moved manually | Create metadata JSON and backfill manifest entries |
| Unicode rendering issues | Used fancy bullets or symbols in console snippets | Replace with ASCII equivalents and rerun lint |

Keep documentation changes synchronized with SEAM routing plans (see `.github/copilot-instructions.md`) so agents always operate under the latest guardrails.
