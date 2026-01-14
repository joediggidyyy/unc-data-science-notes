# Search Command (`search`)

The `search` command provides a governed text search utility, replacing raw shell commands like `grep` or `findstr`. It ensures consistent behavior across platforms and supports SEAM-compliant filtering.

## Usage

```bash
codesentinel search <pattern> [path] [options]
```

## Arguments

- `pattern`: The regex pattern to search for.
- `path`: The directory or file to search (default: current directory).

## Options

- `--recursive`, `-r`: Search recursively through directories.
- `--include`, `-i <pattern>`: Include only files matching the glob pattern (e.g., `*.py`).
- `--exclude`, `-e <pattern>`: Exclude files matching the glob pattern (e.g., `*.pyc`).
- `--context`, `-C <lines>`: Show `<lines>` of context before and after each match.
- `--line-number`, `-n`: Display line numbers for matches.
- `--case-insensitive`, `-c`: Perform case-insensitive search.
- `--json`: Output results in JSON format for tooling integration.

## Examples

**Search for "TODO" in all Python files:**
```bash
codesentinel search "TODO" --recursive --include "*.py"
```

**Search for "SEAM" with context:**
```bash
codesentinel search "SEAM" docs/ --recursive --context 2
```

**Case-insensitive search for "error":**
```bash
codesentinel search "error" logs/ --case-insensitive
```
