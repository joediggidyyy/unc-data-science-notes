# DEV-AUDIT Command Help

## Metadata

| Field | Value |
| --- | --- |
| Document Title | dev audit help |
| Domain / Scope | CLI |
| Artifact Type | Report |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/cli/dev_audit_help.md |

---


```
usage: python.exe C:\Users\joedi\AppData\Local\Programs\Python\Python314\Scripts\codesentinel dev-audit
       [-h] [--silent] [--agent] [--export EXPORT] [--focus AREA] [--tools]
       [--configure]

options:
  -h, --help       show this help message and exit
  --silent         Run brief audit suitable for CI/alerts
  --agent          Export audit context for AI agent remediation (requires
                   GitHub Copilot)
  --export EXPORT  Export audit results to JSON file
  --focus AREA     Focus audit analysis on specific area (e.g., "scheduler",
                   "new feature", "duplication detection"). Only available
                   with Copilot integration.
  --tools          Run tool and environment configuration audit (checks VS
                   Code MCP server setup)
  --configure      Interactively configure workspace tool settings (use with
                   --tools)

```
