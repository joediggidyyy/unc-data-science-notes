# Contributing

Thanks for helping improve these notes.

## Ways to contribute

- Report a typo or broken link
- Ask for clarification
- Suggest a better example
- Submit a pull request with an improvement

## Before you open a PR

- Check the relevant `notes/<term>/<course>/<week>/` index.
- Follow `ACCESSIBILITY.md` and `STYLE_GUIDE.md`.
- Keep changes focused and easy to review.

## Images and other flagged files

If your change adds images (or other flagged binaries):

- Expect the validator to warn until CodeSentinel review approves the file.
- After approval, add the artifact to `approved_artifacts.json`.

Approve a specific file:

```text
python tools/approve_artifacts.py --category image --path notes/.../image.png --note "Reviewed by CodeSentinel"
```

Interactive review menu (new/unapproved images):

```text
python tools/approve_artifacts.py --interactive
```

## Content rules

- Do not add copyrighted course materials (slides, handouts) unless explicitly permitted.
- Do not add prohibited assignment solutions.
- Prefer linking to official sources instead of copying large excerpts.

## Maintenance and validation

Before requesting review, please run:

```text
python maintain.py
```

For publish-readiness checks (may fail until approvals are recorded):

```text
python maintain.py --strict
```

Note: `reports/` is generated locally and is not committed.

## Suggested PR format

- What changed?
- Why is it better?
- Where should reviewers look first?
