---
name: edi-intelligence
description: >
  Run a Practice Loop that turns AGGREGATE, non-identifiable workforce metrics into a DRAFT
  equity-focused briefing — representation and progression signals using rate-based fair
  comparison, plus leadership questions — scored for fairness and disclosure safety, with an
  audit trail. Use for EDI / workforce equity briefings.
---

# EDI Intelligence loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for AGGREGATE workforce metrics. **HALT and ask** if the data
could identify an individual (small cells, free-text, names) unless the user confirms it is
aggregate and disclosure-safe.

## 2. Task & boundaries
Produce a DRAFT equity briefing: representation gaps and progression/disproportionality signals
using **rate-based** comparison (e.g. rate per 100, not raw counts), plus exploratory leadership
questions (mapped to NMC Platform 1 and Equality Act 2010).
You MUST NOT: draw conclusions about individuals; assert causation from correlation; make HR,
disciplinary, or employment recommendations about any person.

## 2.5 Proficiency & equity mapping
Cross-reference workforce signals against the NMC proficiencies database (`placement-support/references/proficiencies/`):
- Map equity findings to NMC Platform 1 (Being an Accountable Professional) and Equality Act 2010 protected characteristics.
- Frame leadership questions around inclusive practice, reasonable adjustments, and fair progression.

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce: Headline signals | Representation/progression gaps (with rates & NMC Platform 1 alignment) | Leadership questions | Data caveats.

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and flag on any data-quality problem, possible disclosure risk (small numbers), or signal that could identify an individual.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the EDI/workforce lead; never present as final.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-edi-intelligence.md`, including per-round scores and any flags.
