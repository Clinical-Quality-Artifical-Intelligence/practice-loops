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

## Why Pandoc

This replaced two hand-written OOXML generators that stored the article text as string
arrays inside the code. They had drifted apart, both wrote to the same output path so
whichever ran last won, and neither could render a table. Pandoc handles tables,
footnotes, real Word heading styles, and a proper title block from the YAML front
matter — none of which was worth reimplementing.
