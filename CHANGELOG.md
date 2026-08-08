# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-08-08

### Changed
- **BREAKING: License changed from Apache 2.0 to PolyForm Noncommercial 1.0.0.** Commercial use of this software is no longer permitted without written permission. Academic, NHS, charitable, and personal use remain fully permitted. See [NOTICE](NOTICE) for transition details.

### Added
- Level 3 Agent Architecture: stateful learner memory (`practice-loop-memory/`), context curation engine (`index.json`), cohort governance aggregator (`scripts/aggregate_governance.py`).
- Lifecycle events (`on_intake`, `on_gate1`, `on_verify`, `on_gate2`, `on_commit`) documented across all 12 skills.
- Step 10: Memory Update (opt-in) added to all loop skills.
- `TRADEMARK.md` — "Practice Loops" trademark policy established.
- Updated README infographic for Level 3 architecture.
- 21 new eval test cases for Level 3 architecture features.

## [0.1.0] - 2026-08-07

### Added
- Initial release of 12 NMC-anchored Practice Loops for Nursing as a Claude Code plugin.
- Standard 6-pillar framework: Trigger → Task → Standard → Verification → Iteration → Human Sign-Off.
- Governance and safety framework with mandatory human sign-off and disk audit trails.
- Added comprehensive `SECURITY.md` detailing clinical safety principles and vulnerability disclosure policy.
- GitHub Actions workflow (`validate.yml`) for continuous integration.
