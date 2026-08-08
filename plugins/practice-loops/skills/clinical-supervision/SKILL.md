---
name: clinical-supervision
description: >
  Run a Practice Loop that turns ANONYMISED clinical supervision notes into a DRAFT
  structured follow-up record — themes, agreed actions, and reflective prompts — in a
  restorative tone, scored against supervision principles, with wellbeing/risk flags and
  an audit trail. Use for restorative clinical supervision follow-up records.
---

# Clinical Supervision loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for the supervision notes. **HALT and ask** if they contain
identifiable data unless the user confirms they are anonymised / IG-approved.

## 2. Task & boundaries
Produce a DRAFT structured follow-up record: key themes, agreed actions (with owners and
timeframes, mapped to NMC Platform 1 & supervision principles), and open reflective prompts for next session.
You MUST NOT: make any clinical, conduct, or performance decision; add interpretation beyond
what the notes support; record something as "agreed" unless the notes show agreement.

## 2.5 Restorative supervision & proficiency mapping
Cross-reference supervision themes against the NMC proficiencies database (`placement-support/references/proficiencies/`):
- Map professional reflection and wellbeing themes to NMC Platform 1 (Accountability & Ethics; `P1`, `P5`, `P8`).
- Align agreed actions with Restorative Clinical Supervision principles (A-OS Model: Action, Outcome, Support).

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce: Themes | Agreed actions (+ NMC Platform/Proficiency + owner + timeframe) | Reflective prompts for next time.

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and flag for a human on any risk to a patient, the supervisee's wellbeing, a safeguarding
concern, or a professional-boundary issue.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the supervisor; never present as final.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-clinical-supervision.md`, including per-round scores and any flags.

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.

