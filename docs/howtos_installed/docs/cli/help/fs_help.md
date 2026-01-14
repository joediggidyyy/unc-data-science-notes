# FileSystem Command (`fs`)

The `fs` command group provides governed filesystem operations that comply with SEAM policies. It replaces raw shell commands like `ls`, `cp`, `mv`, and `rm` to ensure safety, auditability, and consistency across platforms.

## Usage

```bash
codesentinel fs <action> [arguments]
```

## Actions

### `list` (ls)
List files and directories.

**Syntax:**
```bash
codesentinel fs list [path] [--recursive] [--long] [--json]
```

**Options:**
- `path`: Directory or file to list (default: current directory).
- `--recursive`, `-r`: List recursively.
- `--long`, `-l`: Show detailed information (size, modification time).
- `--json`: Output results in JSON format.

### `copy` (cp)
Copy files or directories.

**Syntax:**
```bash
codesentinel fs copy <source> <destination> [--recursive] [--force]
```

**Options:**
- `source`: Source path.
- `destination`: Destination path.
- `--recursive`, `-r`: Recursive copy (required for directories).
- `--force`, `-f`: Overwrite existing files.

### `move` (mv)
Move or rename files or directories.

**Syntax:**
```bash
codesentinel fs move <source> <destination> [--force]
```

**Options:**
- `source`: Source path.
- `destination`: Destination path.
- `--force`, `-f`: Overwrite existing files.

### `archive` (rm)
Safely archive files instead of deleting them. This command moves files to the `quarantine_legacy_archive/` vault and generates a manifest for auditability.

**Syntax:**
```bash
codesentinel fs archive <paths...> --reason <reason> [--force]
```

**Options:**
- `paths`: One or more paths to archive.
- `--reason`, `-m`: **Required.** Reason for archival (e.g., "obsolete", "refactoring").
- `--force`, `-f`: Skip confirmation prompt.

**Policy Note:**
Direct deletion (`rm`) is discouraged. Always use `fs archive` to ensure recoverable history and SEAM compliance.
