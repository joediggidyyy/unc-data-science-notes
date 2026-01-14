<!-- Agent Quick Reference: Document Formatting Templates -->
# Agent Quick Reference — Document Formatting

## Metadata

| Field | Value |
| --- | --- |
| Document Title | AGENT QUICK REFERENCE |
| Domain / Scope | DOC |
| Artifact Type | Document |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/guides/AGENT_QUICK_REFERENCE.md |

---


Purpose: provide a compact set of reference templates and rules that automated agents (and contributors) should follow when creating or normalizing repository documentation. These are minimal, deterministic patterns used by CodeSentinel's documentation tooling.

1) Header template (legacy README style)

```md
# {PROJECT_NAME}

*A Polymath Project*

{PROJECT_DESCRIPTION}
 
- Notes: Keep exactly one blank line between title, subtitle and description. Do not include a version line or a '---' separator in the standard README header.

2) Standard footer template

```md
---

SEAM Protected™ by CodeSentinel
 
- Notes: Footer should be a short policy/footer block. Place at the end of the file and ensure there is exactly one trailing newline after the footer.

3) Spacing rules

- Collapse runs of 2+ consecutive blank lines to a single blank line.
- Ensure a single blank line between headings and lists/paragraphs.
- Trim trailing whitespace on every line.
- Ensure final file ends with a single newline.

4) README: "Project Structure" section

- Use a fenced code block with a simple tree listing. Keep items sorted alphabetically and include short parenthetical notes when helpful. Example:

## Project Structure

```text
CodeSentinel/
  README.md
  CHANGELOG.md
  CONTRIBUTING.md
  codesentinel/
    __init__.py
    cli/
```
```

5) Changelog template (Keep a Changelog)

- Top-level heading: `# Changelog`
- Release sections: `## [X.Y.Z] - YYYY-MM-DD` or `## [Unreleased]`
- Bullet groups: `### Added`, `### Changed`, `### Fixed`, `### Deprecated` when applicable.

6) Metadata rules

- If adding a `Last Updated` metadata line, insert it directly after the H1 title (or the first '---' front-matter block if present) using the format:

```

Last Updated: YYYY-MM-DD

```

- Only a single `Last Updated:` line must exist in a document. The rebuild process will update the single canonical line.

7) Enforcement checklist for agents

- Read the file before making edits (mandatory).
- Validate header and footer templates match the patterns above.
- Run whitespace normalization (collapse multiple blanks, trim trailing spaces).
- Ensure `Project Structure` code fence is rebuilt from the current workspace when requested.
- Make a non-destructive backup before writing (archive or timestamped copy).

8) Quick usage examples (agent-friendly)

- Validate a file: use the repository helper logic `verify_documentation_headers_footers(path)` and `verify_documentation_branding(path)` in `codesentinel/cli/__init__.py`.
- Rebuild README structure: `codesentinel update readme --rebuild` (supports `--dry-run`).

9) Notes and rationale

- These templates mirror the legacy `main` branch formatting and are intentionally minimal to reduce churn from automated updates. When in doubt prefer fewer lines and preserve human-written content unless explicit policy violation is detected.

## SessionMemory Inactivity Checklist

- The SessionMemory inactivity listener automatically marks a session as `pending` after 25 minutes of silence and fully pauses caches at 40 minutes.
- Eligible assets: `.agent_session/task_state.md`, `context_cache.json`, QuestStack snapshots, and behavioral cache exports. Virtual environments remain governed by `codesentinel venv ...` policies.
- Status & controls (CLI-first):

```text
codesentinel memory inactivity-status      # Show idle timer, pause history, refractory window
codesentinel memory inactivity-freeze      # Force a pause (add --force and --note "reason")
codesentinel memory inactivity-thaw        # Resume immediately (add --force to ignore snapshot mismatches)
codesentinel memory inactivity-cancel      # Clear a pending pause before it activates
```

- Always inspect status before forcing a freeze/thaw and log the action in your session todo list.
- Resume before running `codesentinel clean --root` so root policy checks see an accurate `.agent_session/` snapshot.
- Audit artifacts live in `logs/session_memory/events.jsonl` and the behavioral dashboard scorecard; do not tamper with them.

-- End of quick reference

## Agent Instructions Snapshot Checklist

- `docs/guides/AGENT_INSTRUCTIONS.md` is mirrored to `quarantine_legacy_archive/backups/` on every CLI invocation (4-hour freshness window) and whenever `codesentinel docs backup-agent` runs.
- Discover backups instantly, even after a memory wipe:

```text
codesentinel docs backup-agent --list          # Show the most recent snapshots (limit defaults to 10)
codesentinel docs backup-agent --latest        # Print the single most recent snapshot path
codesentinel docs backup-agent --json --list   # Machine-readable listing for automation
codesentinel docs backup-agent --reason edit   # Force a fresh snapshot with a reason tag
```

- Metadata + latest pointer live under `logs/doc_backups/`:
  - `agent_instructions.jsonl` keeps the append-only audit trail.
  - `latest_agent_instructions.txt` contains the freshest path, timestamp, checksum, and trigger; open it if the CLI is unavailable.
- The CLI auto-backup prints `[INFO] Agent instructions safety backup created: CodeSentinel/...` when it refreshes the snapshot. Lack of that line means the prior snapshot is still within the freshness SLA.
