# CodeSentinel Git Command (`codesentinel git`)

The `git` command provides a governed interface for version control operations, enforcing SEAM policies on branch protection and workflow safety.

## Usage

```bash
codesentinel git <action> [arguments]
```

## Actions

### `status`
Show the working tree status.
```bash
codesentinel git status
```

### `add`
Add file contents to the index.
```bash
codesentinel git add <pathspec>...
```

### `commit`
Record changes to the repository.
```bash
codesentinel git commit -m "Commit message"
codesentinel git commit -a -m "Commit message"
```

### `push`
Update remote refs along with associated objects.
**Policy Enforcement**: Pushing directly to protected branches (`main`, `master`, `production`) requires explicit confirmation or the `--force` flag.
```bash
codesentinel git push [remote] [branch]
codesentinel git push origin feature/my-feature
```

### `pull`
Fetch from and integrate with another repository or a local branch.
```bash
codesentinel git pull [remote] [branch]
```

## SEAM Policy Integration

- **Branch Protection**: Prevents accidental pushes to production branches.
- **Traceability**: All operations are executed through the standard git binary but wrapped with policy checks.
