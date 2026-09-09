# Style Guide

This guide keeps the repository consistent and easy to scan.

## File naming

- Use `Week01`, `Week02`, … (zero-padded)
- Use consistent file paths and naming conventions for note pages:
  - `notes/<Term>/<Course>/<WeekXX>/...`
  - `notes/<Term>/<Course>/<WeekXX>/docx/`
  - Use descriptive names for files, beginning with the course code and avoiding spaces and special characters.

## Page template

Recommended top-of-page structure:

0. Header with course code, week number, title, and date (if relevant)
1. Week #: Title 
2. Why this page exists (1-2 sentences)
3. Key terms (bullets + short definitions)
4. Main content (sections)
5. Worked examples (if relevant)
6. Quick check / summary (optional)

## Voice

- Write in plain language.
- Prefer active voice.
- Define terms before using them heavily.

## Code blocks (when unavoidable)

- Keep code short.
- Add commentary *above* the code block in bullets.
- Avoid long unbroken code dumps.
- Keep in-line comments to a minimum; use the commentary bullets instead.

## Citations

- If you rely on a source, add a short “References” section at the bottom or use captioned links.
- Prefer links rather than copying large excerpts.

## Reference guides (QuickReferences)

Guides under `notes/QuickReferences/` may be **Markdown-native**: the guide is
`README.md` at the guide folder root, so `notes/INDEX.md` links straight to it.

These guides follow the rules above, with a few additions:

- **One H1** — the guide title. Major sections are H2, sub-sections H3.
- **Front matter** — a short YAML block at the top with `title`, `slug`,
  `summary`, `audience`, `tags`, and a version and review date where relevant.
- **Difficulty labels** — see `ACCESSIBILITY.md`.
- **Code blocks** — a code-heavy reference guide (for example, a pytest or SQL
  guide) may use more code than a week's notes. Keep each block short and to one
  idea, put the explanation in bullets *above* the block, and show expected
  output in its own short block. The "keep code short" rule still applies per
  block.
- **Links** — relative within the guide folder; no absolute or site-root paths,
  so the guide can be copied elsewhere unchanged.
