# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Step 1.5 Recall** in all 11 loop skills: if a pseudonym is given at intake, the loop reads `./practice-loop-memory/<pseudonym>.json` **before reasoning** and surfaces open learning gaps, prior flags, the score trend, and `assessor_preferences`. Recalled content is treated as prior context to be confirmed, and a recurring gap is escalated as a pattern rather than repeated as an action.
- **Step 1 now offers cross-session memory and asks for a pseudonym.** Previously step 10 was conditioned on "if a learner pseudonym was provided during intake", but no step ever asked for one — so the memory feature was unreachable unless the nurse volunteered a pseudonym unprompted.
- **Step 3.5 Gate 1** in all 11 loop skills: the loop presents its problem identification and diagnostic reasoning and **stops** for the nurse to confirm or correct it before drafting. The dual-gate architecture was documented in the README and asserted in `evals/cases.md`, but no loop implemented the Gate 1 pause; only Gate 2 (sign-off) existed.
- **Programmatic vs agent-triggered boundary table** in the `practice-loop-method` skill: safety-relevant operations run regardless of what the assistant judges necessary; only genuinely discretionary steps are left to the model.
- Eval cases for memory intake/recall, memory update, and Gate 1 (`evals/cases.md`).

### Changed
- `scripts/check_guardrails.py` now requires section 3.5 in every loop and enforces **memory read/write symmetry**: a loop that writes a trajectory without reading it — or that uses memory without asking for a pseudonym — fails the build. Verified by negative test: all 11 pre-change loops are rejected, each reporting all three defects.
- Guardrail failures are now reported in full rather than stopping at the first class of problem.
- Documentation claims reconciled with the implementation. The "Level 3 Agent Architecture" label is replaced with a precise statement: Level 2 implemented in full, Level 3 partial (programmatic/agent-triggered boundary and context curation present; compaction, tool-output offloading and context-window monitoring absent). Note that "Level 3" in `docs/framework/` refers to this project's *own* maturity ladder and is a different scale.
- `edi-intelligence` memory is keyed to a cohort or dataset pseudonym, not a learner, and explicitly forbids per-individual records — the loop accepts aggregate, non-identifiable data only.
- `practice-loop-memory/README.md` documents the read half of the mechanism and notes that cross-session tracking of an individual is a distinct data-protection proposition from single-session drafting, even pseudonymised.

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
