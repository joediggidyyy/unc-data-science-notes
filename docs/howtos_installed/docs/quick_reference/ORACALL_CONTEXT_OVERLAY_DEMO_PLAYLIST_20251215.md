# ORACall Demo Playlist (Context Overlay Showcase) — 2025-12-15

Owner: ORACL-Prime  
Audience: mixed (technical + non-technical)  
Purpose: Provide a short, reliable set of natural-language searches that highlight the **new context overlay** capability (session ↔ document linkage) in the ORACode knowledge graph.

> **How to run**: copy/paste each query into ORACall search.
>
> Example:
> - `codesentinel oracall search "<query>"`
>
> Optional: after any query that returns a specific file path you can run a trace to show connections:
> - `codesentinel oracall trace "<that path>" --direction both --depth 1 --json`

---

## The 10-query playlist (copy/paste)

1. "What did we work on in the most recent session?"

2. "Show me documents connected to the session timeline."

3. "Which sessions are connected to the session implementation analysis?"

4. "Find anything connected to the session recovery report."

5. "What is related to our finetuning policy?"

6. "Which sessions are linked to the finetuning sessions policy?"

7. "Show me the 'next session issues' document and what connects to it."

8. "What sessions connect to 'next session issues'?"

9. "What sessions are related to each other?"

10. "Summarize the docs that cluster around recent sessions."

---

## Quick stage directions (what to say out loud)

- **Query 1**: "This is the fast 'what happened last time' question — it pulls linked work artifacts without scanning logs."
- **Queries 2–6**: "Now we do reverse lookups: pick a doc topic, and ask which sessions connect to it."
- **Queries 7–8**: "This shows planning continuity — how 'next session issues' becomes a hub across sessions."
- **Query 9**: "This is the 'graph moment' — sessions can be linked to other sessions through curated references."
- **Query 10**: "High-level rollup — helps a non-technical audience see that the system can summarize a cluster of related work."

---

## Notes (why these work in this repository)

These queries are designed to reliably hit curated linkage topics that exist in the repository’s curated link index and documentation manifests, including:
- session timeline
- session implementation analysis
- session recovery report
- finetuning policy / finetuning sessions policy
- next session issues

The new context overlay injects learned edges (relation: `context_links`) into the ORACode weighted graph. These edges are generated from curated artifacts (no Tier-2 log ingestion) and published to:
- `semantics_vault/oracl_index/learned_edges.json`

Telemetry for overlay generation is appended to:
- `logs/behavioral/context_overlay.jsonl`

---

## Safety

- No plaintext sensitive identifiers (hosts, IPs, usernames, tokens, keys, passwords).
- Credentials are environment variables only (names-only in docs/logs).
- Overlay inputs are curated artifacts under `docs/` (no `logs/` ingestion).
