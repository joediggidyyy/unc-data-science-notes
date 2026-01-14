# CodeSentinel Command Manual

**Classification:** Public | **Domain:** CLI | **Last Updated:** 2025-12-01

---

## Overview

This manual provides a high-density reference for the `codesentinel` CLI. Commands are grouped by operational domain.

## Domain Index

- [**Core Operations**](#core-operations) (Scan, Clean, Dashboard, Update)
- [**CIBI (Phase 2)**](#cibi-phase-2) (FS, Search, Git)
- [**Memory & Policy**](#memory--policy) (Session, Integrity, Alerts)
- [**Agent & Automation**](#agent--automation) (Workbench, Ops, Jobs)
- [**Deployment**](#deployment) (Flash, Venv, Ship)
- [**Utilities**](#utilities) (Format, Docs, DevAudit)

---

## Core Operations

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`status`** | | Show CodeSentinel system status. |
| **`scan`** | `--security`, `--bloat-audit`, `--all` | Run specific or all scan types. |
| | `--output <file>`, `--json` | Output results to file or JSON. |
| | `--agent`, `--export <file>` | Export context for agent remediation. |
| **`clean`** | `--cache`, `--temp`, `--logs` | Clean specific artifact types. |
| | `--build`, `--test`, `--root` | Clean build/test artifacts or root dir. |
| | `--emojis`, `--git` | Remove emojis; run git gc. |
| | `--all`, `--full` | Clean everything; full root validation. |
| | `--older-than <days>` | Only remove items older than N days. |
| | `--dry-run`, `--force` | Simulate or force without prompt. |
| **`dashboard`** | `update --targets <list>` | Update panels (e.g., `security`, `jobs`). |
| | `master` | Rebuild the full master dashboard. |
| | `watch` | Continuous watch mode for updates. |
| **`update`** | `docs`, `changelog`, `version` | Update documentation or project version. |
| | `readme-rebuild` | Rebuild README from fragments. |
| | `--set-version <ver>` | Set specific version string. |
| **`setup`** | `--gui`, `--non-interactive` | Run setup wizard (GUI or headless). |

---

## CIBI (Phase 2)

*CodeSentinel Integrated Bash Interface - Governed Shell Operations*

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`fs`** | `list <path>` | List directory contents (governed `ls`). |
| | `read <path>` | Read file contents (governed `cat`). |
| | `write <path>` | Write file contents (governed `echo`). |
| | `delete <path>` | **Archival delete** (governed `rm`). |
| | `move`, `copy` | Move or copy files. |
| **`search`** | `text <pattern>` | Search text in files (governed `grep`). |
| | `files <pattern>` | Find files by name (governed `find`). |
| **`git`** | `status` | Show git status. |
| | `commit`, `push`, `pull` | Standard git operations with policy checks. |
| | `branch`, `checkout` | Branch management. |

---

## Memory & Policy

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`memory`** | `show`, `stats`, `tasks` | Display session state and statistics. |
| | `clear --force` | Clear session cache. |
| | `health --json` | Run SessionMemory Health Monitor (SMHM). |
| | `cycle-reset` | Reset "Cycle" cache efficiency counter. |
| | `restore` | Restore artifacts from disk. |
| | `process <subcmd>` | Manage orphan processes (`kill`, `watch`, `tree`). |
| | `inactivity-<action>` | `status`, `freeze`, `thaw`, `cancel`. |
| **`policy`** | `verify --fix` | Verify and fix policy violations. |
| | `dump --reason <txt>` | Create a policy snapshot. |
| **`integrity`** | `status --detailed` | Show integrity monitoring state. |
| | `start --baseline <file>` | Start monitoring against baseline. |
| | `stop --save-state` | Stop monitoring. |
| | `verify --report <file>` | Verify files against baseline. |
| | `config <subcmd>` | Manage `baseline`, `whitelist`, `critical`. |
| **`alert`** | `send <msg>` | Send manual alert. |
| | `--severity <level>` | `info`, `warning`, `error`, `critical`. |
| | `--channels <list>` | `console`, `file`, `email`, `slack`. |
| | `config <options>` | Configure channels and filters. |

---

## Agent & Automation

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`agents`** | `instructions` | Manage agent instruction sets. |
| **`workbench`** | `catalog`, `audit`, `enforce` | Agent Workbench tools. |
| | `--orphans`, `--json` | Show orphans; JSON output. |
| **`ops`** | `list`, `run` | List or run Operations Surface tasks. |
| | `--task-id <id>` | Run specific task. |
| | `--sandbox <env>` | Specify sandbox environment. |
| **`jobs`** | `report`, `classify` | Job reporting and classification. |
| **`schedule`** | `start`, `stop`, `status` | Manage maintenance scheduler. |
| **`integrate`** | `--new`, `--all` | Integrate commands into workflows. |
| | `--workflow <target>` | Target `scheduler`, `ci-cd`, or `all`. |
| **`learn`** | `<args>` | Behavioral learning module. |
| **`insight`** | `<args>` | Insight Atlas visualization. |
| **`plan`** | `<args>` | Planning module utilities. |

---

## Deployment

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`flash`** | `plan` | Generate a delta update plan. |
| | `execute` | Execute the pending flash plan. |
| | `rollback` | Revert the last flash deployment. |
| **`venv`** | `create`, `reuse`, `ensure` | Manage virtual environments. |
| | `inventory`, `prune`, `audit` | List, clean, and check venvs. |
| **`ship`** | `<args>` | Ship manifest utilities. |

---

## Utilities

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`format`** | `file <path>`, `dir <path>` | Format files or directories. |
| | `check`, `check-dir` | Check style without modifying. |
| | `schemes`, `rules` | List available schemes/rules. |
| | `gui` | Open formatter configuration GUI. |
| **`docs`** | `find <terms>` | Intelligent documentation search. |
| | `validate-name` | Validate doc filenames/headers. |
| | `backup-agent` | Snapshot agent instructions. |
| **`!!!!`** | `--agent`, `--silent` | **DevAudit** (Rapid Diagnostics). |
| *(or `dev-audit`)* | `--focus <area>` | Focus on `security`, `scheduler`, etc. |
| | `--tools`, `--configure` | Audit/config workspace tools. |
| | `--review` | Interactive review mode. |
| **`metrics`** | `export` | Export daily policy lookup metrics. |
| **`pdf`** | `<args>` | PDF conversion utilities. |
| **`tags`** | `<args>` | Tag management. |
| **`advise`** | `<args>` | Advisory module. |
| **`feedback`** | `<args>` | Feedback collection. |
| **`edit`** | `<args>` | Edit utilities. |
| **`gui`** | | Launch the main GUI. |
| **`wagonwheel`** | `<args>` | WagonWheel guardrail utilities. |

---

## ORACode Tools

| Command | Subcommand / Options | Description |
| :--- | :--- | :--- |
| **`benchmark`** | `python tools/oracode/benchmark_simulator.py` | Run performance benchmark suite. |
| | *Output* | P95 latency, throughput (req/s). |
| **`graph`** | `python tools/oracode/weighted_graph_builder.py` | Rebuild `weighted_graph_index.json`. |
| | *Use Case* | Run after significant refactoring. |
| **`defrag`** | `python tools/codesentinel/defrag_instructions.py` | Sync Markdown/JSON instructions. |
| | `--all` | Process all instruction pairs. |

---
*Generated by ORACL-Prime for CodeSentinel v1.1.3.b1*
