Command formatting guideline
============================

Preferred style when showing shell commands in documentation:

- Always use fenced code blocks for commands (triple-backtick fenced blocks).
- Use an explicit language hint when helpful, e.g. ```bash or ```pwsh for PowerShell on Windows.
- Keep the command alone on a single line, with a short one-line description above (if needed).
- Avoid inline or indented command lines inside bullet lists when possible — code blocks are clearer and easier to scan.

Example (good):

```bash
# Dry-run a full ORACode rebuild
python tools/oracode/rebuild_graph.py --dry-run
```

Reasoning:

- Code blocks are dyslexia-friendly and easier to visually parse and copy.
- They make it obvious what the exact command is, reducing copy errors.

When to deviate:

- When commands are being discussed in-line as part of a paragraph (very short, single word), inline may be acceptable.

Enforcement:

- We intend to prefer this format in new docs and when editing existing docs.
- A lightweight checker will flag frequent violations — use it to triage documents for follow-up updates.

CI enforcement
--------------
We run a CI step that executes `tools/scripts/check_command_blocks.py` on pull requests and pushes.
If the checker finds plaintext command lines outside of fenced code blocks the CI job will fail and print the locations so authors can fix them before merge.

This helps future agents and humans maintain the code-block convention with low overhead.

Thank you for preferring the code-block format — I'll follow it in future replies and help apply it across docs when requested.
