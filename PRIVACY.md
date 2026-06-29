# Privacy Policy — Practice Loops plugin

**Last updated:** 2026-06-29 · **Publisher:** Clinical Quality Artificial Intelligence (CQAI)

## Summary

The `practice-loops` Claude Code plugin **collects no data, contains no analytics or telemetry, and transmits nothing to CQAI or any third party.** It runs entirely within your own Claude Code environment.

## What the plugin is

The plugin is a set of skills (Markdown instructions), one local hook, and helper scripts. It has **no backend and makes no network requests of its own.**

## Data handling

- **Your inputs** (the notes/transcripts you provide to a loop) are processed by **your own Claude session**, under the terms of your Claude/Anthropic agreement. The plugin does not send your inputs anywhere else.
- **Audit logs** are written **locally** to `./practice-loop-audit/` on your machine. They are never uploaded or shared by the plugin.
- **The PII-guard hook** runs locally on your device; it inspects your prompt only to display a warning and sends nothing externally.
- **No cookies, accounts, identifiers, or usage tracking** are used by the plugin.

## Your responsibility

The plugin is designed for **anonymised inputs only**. Do not enter identifiable patient or staff data without your organisation's Information Governance approval. Outputs are drafts for review by a registered professional. See the [clinical-safety note](README.md) and [DCB0129 safety case](docs/safety/).

## Contact

Questions: info@nursingcitizendevelopment.com · https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops
