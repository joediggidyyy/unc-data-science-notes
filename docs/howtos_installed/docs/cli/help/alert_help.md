# ALERT Command Help

## Metadata

| Field | Value |
| --- | --- |
| Document Title | alert help |
| Domain / Scope | CLI |
| Artifact Type | Guide |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/cli/alert_help.md |

---


```
usage: python.exe C:\Users\joedi\AppData\Local\Programs\Python\Python314\Scripts\codesentinel alert
       [-h] [--title TITLE] [--severity {info,warning,error,critical}]
       [--channels CHANNELS [CHANNELS ...]]
       message

positional arguments:
  message               Alert message

options:
  -h, --help            show this help message and exit
  --title TITLE         Alert title
  --severity {info,warning,error,critical}
                        Alert severity
  --channels CHANNELS [CHANNELS ...]
                        Channels to send alert to

```
