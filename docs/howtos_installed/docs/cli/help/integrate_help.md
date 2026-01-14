# INTEGRATE Command Help

## Metadata

| Field | Value |
| --- | --- |
| Document Title | integrate help |
| Domain / Scope | CLI |
| Artifact Type | Guide |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/cli/integrate_help.md |

---


```
usage: python.exe C:\Users\joedi\AppData\Local\Programs\Python\Python314\Scripts\codesentinel integrate
       [-h] [--new] [--all] [--workflow {scheduler,ci-cd,all}] [--dry-run]
       [--force] [--backup]

options:
  -h, --help            show this help message and exit
  --new                 Integrate newly added commands into workflows
                        (default)
  --all                 Integrate all available commands into workflows
  --workflow {scheduler,ci-cd,all}
                        Target workflow for integration (default: scheduler)
  --dry-run             Show integration opportunities without making changes
  --force               Force integration even if conflicts detected
  --backup              Create backup before integration

```
