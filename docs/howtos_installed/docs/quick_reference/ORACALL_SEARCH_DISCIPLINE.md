# ORACall Search Discipline (Canonical)

This card makes the repository-wide search workflow painfully explicit.

## Canonical search order

1) **ORACall first** (canonical)
   - `codesentinel oracall search ...`
   - `codesentinel oracall trace ...`

2) Meaning-based workspace search (when ORACall is unfit)

3) File-glob search (when you know the filename/pattern)

4) Exact string search (when you know the literal)

5) **Regex / grep is last resort only**

## Regex last-resort rule

Use regex only when:

- ORACall is unavailable/unfit for the question, **and**
- meaning-based search does not disambiguate, **and**
- the target is a structural pattern not expressible as an exact string.

When regex is used, record a one-sentence justification in the session log.

## Checklist suite (SSOT)

Canonical workflow templates live at:

- `operations/checklists/OPENING_CHECKLIST.{md,json}`
- `operations/checklists/CLOSING_CHECKLIST.{md,json}`

Security rule: never place plaintext sensitive identifiers in checklists, logs, or reports.
