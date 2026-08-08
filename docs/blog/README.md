# Blog & articles

Long-form articles as Markdown. The Markdown is the artefact of record — prose is
reviewable in a diff, and any claim it makes can be checked against the code in the
same pull request.

| Article | Date |
|---|---|
| [Beyond Vibe Coding](2026-08-08-beyond-vibe-coding.md) | 8 August 2026 |

## Building a .docx

```bash
npm run build:article
```

Output goes to `dist/articles/` (gitignored). To build a specific file:

```bash
python scripts/build_article.py docs/blog/some-article.md
```

Requires Pandoc:

```bash
winget install --id JohnMacFarlane.Pandoc --scope user
```

**House styles.** Drop a `reference.docx` in this directory and the build applies it
automatically — fonts, heading colours, spacing. Create a starting point with
`pandoc --print-default-data-file reference.docx > docs/blog/reference.docx`, restyle it
in Word, and save.

## Figures

**Figures are generated from real command output, never drawn.** This is not a style
preference. A mocked-up screenshot of a clinical governance tool can show a safety
feature the code does not have, and no reader can tell the difference — which is exactly
what happened to the two demo images this workflow replaced.

To capture a new one, pipe the real command through the renderer:

```bash
python scripts/check_guardrails.py | python scripts/render_terminal_svg.py --title "practice-loops $ python scripts/check_guardrails.py" --output docs/framework/demo-guardrail-check.svg
```

SVG is the source format: labels stay diffable, so a wrong claim can be caught in review
rather than being baked into pixels. GitHub renders SVG inline, and Word 2016+ handles
the SVG that Pandoc embeds.

Some publishing targets — LinkedIn among them — will not accept SVG upload. For those:

```bash
npm run build:figures
```

That rasterises every SVG in `docs/framework/` to `dist/figures/*.png` at 2× using
headless Edge or Chrome, so it needs nothing installed. Pandoc's own SVG conversion
would need `rsvg-convert`, which is not available via winget.

## Why Pandoc

This replaced two hand-written OOXML generators that stored the article text as string
arrays inside the code. They had drifted apart, both wrote to the same output path so
whichever ran last won, and neither could render a table. Pandoc handles tables,
footnotes, real Word heading styles, and a proper title block from the YAML front
matter — none of which was worth reimplementing.
