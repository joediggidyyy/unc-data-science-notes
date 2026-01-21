# Public Notes Compliance Checklist (Repository Policy)

This file is a **repo-specific interpretation** intended to help keep a public notes repository safe for public sharing.

It is not legal advice and not an official policy document.

## Academic integrity rules for this repo

### Do

- Write explanations in your own words.
- Cite sources for definitions, non-trivial claims, and adapted ideas.
- Use your own examples (or examples clearly permitted for reuse).

### Do NOT

- Post exam/test questions, answer keys, or “recently given test” details.
- Post prohibited assignment solutions (or step-by-step instructions that function as a solution) unless explicitly allowed.
- Copy/paste from instructor slides/handouts or textbooks unless you have explicit permission and redistribution rights.

## Respect, safety, and community standards

- No harassment, bullying/cyberbullying, threats, or targeted abuse.
- Keep discussions in issues/PRs constructive and professional.

## Privacy / confidentiality

Do not include:

- Student names + grades
- Student ID numbers
- Private emails/phone numbers
- Screenshots showing private rosters, grades, or private communications

## CodeSentinel approvals for flagged artifacts

Some file types (especially **images**) are hard to automatically review for privacy.
This repo uses an approval manifest so CodeSentinel-reviewed items don't keep
triggering warnings.

- Manifest: `approved_artifacts.json` (tracked)
- Approval is **pinned by SHA256**.

If the file changes, the SHA changes, and it must be re-approved.

Validator behavior (summary):

- Unapproved images: `WARN` (manual privacy review required)
- Approved images (path + SHA256 match): `INFO` (no further scrutiny required)

### Approving an artifact

After CodeSentinel review approves an image (or other high-risk binary), add it
to the manifest:

```text
python tools/approve_artifacts.py --category image --path notes/.../image.png --note "Reviewed by CodeSentinel"
```

Interactive review menu (new/unapproved images):

```text
python tools/approve_artifacts.py --interactive
```

Remove an approval:

```text
python tools/approve_artifacts.py --remove --path notes/.../image.png
```

List approved entries:

```text
python tools/approve_artifacts.py --list
```

## Additional disclaimers

- These are unofficial student-authored notes.
- Do not use this repo to violate course/instructor policies.
- If you are unsure whether sharing something is allowed, do not publish it.

## How we enforce this

- The repository includes `tools/validate_notes_repo.py` to flag likely violations.
- The validator is conservative: it reports *risk signals*, not guilt.

## Reports (local-only)

The validator and maintenance tooling write reports to `reports/` for reviewers,
but **reports are not published**. The `reports/` folder is ignored by git.
