# Shipping Manifest Automation – User Help

**Audience**: Engineers preparing CodeSentinel releases

## Metadata

| Field | Value |
| --- | --- |
| Document Title | SHIP MANIFEST AUTOMATION HELP |
| Domain / Scope | DOC |
| Artifact Type | Guide |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/guides/SHIP_MANIFEST_AUTOMATION_HELP.md |

---


This guide explains how to work with the shipping manifest guard, including the new `.shipinclude` override file and the CLI toggles that control each automation mode.

---

## 1. Overview

CodeSentinel enforces a canonical list of documents (`docs/SHIP_MANIFEST.json`) before anything ships. Two complementary automation modes are available:

| Mode | Purpose | Default |
| --- | --- | --- |
| **Autodiscovery (Option A)** | Walks the repo and auto-registers common documentation anchors (README, SECURITY, QUICK_START, etc.). | Enabled |
| **`.shipinclude` overrides (Option B)** | Lets a team declare extra include/exclude glob patterns for edge cases or partner deliverables. | Disabled |

Use the CLI to confirm manifest health and to flip these options on or off per project.

---

## 2. Using the `.shipinclude` File (Option B)

1. **Create the file** at the repository root: `.shipinclude` (JSON or YAML accepted; start with JSON for simplicity).
2. **Define the structure**:

    ```json
    {
      "include": [
        "docs/partners/**",
        "docs/reports/evergreen/templates/*.md"
      ],
      "exclude": [
        "docs/legacy/**"
      ],
      "notes": "Sample partner override"
    }
    ```

3. **Commit the file** so automated hooks can pick it up.
4. **Enable Option B via CLI** (see Section 4) so the guard knows to read the overrides.

> The `.shipinclude` file augments Option A—it never replaces the baseline manifest. When enabled, the guard merges autodiscovered entries with everything matched by the include patterns and then removes anything under `exclude`.

---

## 3. Verifying the Manifest

Run the verification command before each push:

```cmd
codesentinel ship verify --require-tracked --require-unignored
```

Add `--json` for machine-readable output or point `--manifest` at a non-default location if your repo uses a different filename.

---

## 4. Enabling or Disabling Automation Options

All option management flows through the CLI to keep audit trails consistent. The new `options` subcommand edits `codesentinel.json` safely.

### List Current State

```cmd
codesentinel ship options --list
```

### Enable an Option

```cmd
codesentinel ship options --enable shipinclude
```

### Disable an Option

```cmd
codesentinel ship options --disable autodiscovery
```

Optional flags:

- `--config <path>` – point at an alternate config relative to the repo root (default: `codesentinel.json`).

Once Option B is enabled, the guard treats `.shipinclude` as authoritative for extra inclusions/exclusions. When disabled, the file is ignored even if present.

---

## 5. Operational Checklist

1. Run `codesentinel ship track` whenever you add a manual document (coming in Sprint Q4).
2. Keep `docs/SHIP_DOCUMENT_CLASSIFICATION.md` aligned with any `.shipinclude` additions for reviewer clarity.
3. Capture partner-specific overrides inside `.shipinclude` and document the rationale in PR descriptions.
4. Use `codesentinel ship verify --json` inside CI to gate releases.

---

## Support References

- Planning context: `docs/planning/SHIP_MANIFEST_AUTOMATION_PLAN.md`
- Classification matrix: `docs/SHIP_DOCUMENT_CLASSIFICATION.md`
- Placeholder tracking: `docs/planning/PLACEHOLDER_REGISTRY.md`
