# UPDATE Command Help

## Metadata

| Field | Value |
| --- | --- |
| Document Title | update help |
| Domain / Scope | CLI |
| Artifact Type | Guide |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/cli/update_help.md |

---


```text
usage: codesentinel update [-h]
                           {docs,changelog,readme-rebuild,version,help-files}
                           ...

positional arguments:
  {docs,changelog,readme-rebuild,version,help-files}
                        Update actions
    docs                Bulk documentation refresh workflow
    changelog           Append detected releases to CHANGELOG.md
    readme-rebuild      Reconstruct README.md from templates and metrics
    version             Bump version numbers across the repo
    help-files          Export CLI help (mode-aware banner + docs bundle)

options:
  -h, --help            show this help message and exit
  --set-version SET_VERSION
                        Set project version across key manifests
  --dry-run             Show planned changes without writing files
  --export EXPORT       Target directory for help-files export (default:
                        docs/cli)
  --format {md,txt,both}
                        Output format for help-files export
  --commands COMMANDS [COMMANDS ...]
                        Limit help-files export to a subset of commands

```

## Mode-Aware Help Files

`codesentinel update help-files` now renders every CLI command in three modes:

| View | Mode Variable | Description |
|------|---------------|-------------|
| Non-Agent | `ORACL_MODE=manual` | Pure manual guidance with agent automation disabled. |
| Agent | `ORACL_MODE=agent` | Forces automation hints and agent-ready switches. |
| Hybrid | `ORACL_MODE=auto` | Follows SEAM policy (manual-first, escalates when cleared). |

Each exported file contains:

1. A view banner describing the mode and automation policy.
2. Agent-integration status for the command (Ready, Experimental, Planned, etc.).
3. Raw `--help` output captured from the CLI, allowing doc teams to embed identical help text in the handbook.

Use `--commands status scan` to limit output to specific commands, and `--format md` if you only need Markdown for publication.

## Inline Help Banner

Running `codesentinel <command> --help` now prints a banner before the standard argparse content. The banner mirrors the exported metadata so operators get the same context without leaving the terminal. Example:

```text
============================================================
[Help View: NON-AGENT] :: Non-Agent View (mode: manual)
Automation disabled. Commands emit manual guidance only.
Agent Integration: NOT-APPLICABLE
Mode source: manual. Set ORACL_MODE=manual to force manual execution.
============================================================
usage: codesentinel status [-h]

```

Set `ORACL_MODE=agent` (or run `codesentinel agents mode set --value agent` once that command ships) to view the agent-focused banner. This makes it easy to validate which commands are cleared for automation directly from the CLI.
