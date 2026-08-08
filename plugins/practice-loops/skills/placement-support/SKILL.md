---
name: placement-support
description: >
  Run a Practice Loop that turns ANONYMISED placement meeting notes into a DRAFT SMART
  action plan, separating learning needs from conduct concerns, scored against NMC
  standards, with escalation flags and an audit trail. Use for student placement
  support, action plans, or placement concern reviews.
---

# Placement Support loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute the steps in
order. Never skip verification or sign-off.

## 1. Intake
Confirm this is a manual start. Ask the user to paste the placement meeting notes.
**HALT and ask** if the notes contain identifiable data (student or patient name, DOB, NHS
number, location) unless the user confirms they are anonymised or IG-approved.

## 2. Task & boundaries
Draft a SMART action plan that:
- separates **learning needs** from **conduct concerns** into two clearly labelled sections,
- maps each learning need to specific NMC **proficiencies** and valid assessment methods (from `references/proficiencies/`),
- includes the **student voice**, and
- maps to PAD requirements and NMC professional values.

You MUST NOT: decide progression or pass/fail; make any fitness-to-practise, capability,
employment, or disciplinary decision; invent facts (mark gaps "to confirm with student/assessor").

## 2.5 Proficiency mapping (context curation)
First, read `references/proficiencies/index.json` and scan the input notes for matching keyword clusters.
Load **only** the matched proficiency rows from `references/proficiencies/year-<N>-proficiencies.md` (based on the student's programme year, defaulting to Year 1 if unspecified) and the relevant assessment methods from `references/proficiencies/assessment-methods.md`. Do **not** load all proficiencies into context — pull only what the input keywords match.

For each concern or learning need:
- Map it to the specific NMC proficiency number(s) (e.g. `P7`, `P18`, `P21`) using the index.
- Note the valid assessment method(s) (e.g. Direct Observation, Simulation, Discussion).
- Flag any proficiencies marked with `*` as requiring perpetual direct supervision.
- Include any `guidance` notes from the index entry.

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce the action plan as a table — Concern | Type (learning/conduct) | Mapped Proficiency | SMART action | Assessment Method | Owner | Review date — followed by a short **student voice** section.

## 5. Verify
Score the draft against all 10 points in `references/verifier.md`. **Print each score out of 10**
and name what is weak.

## 6. Iterate
If any point scores below 8, revise the weakest part, explain the change, and re-score.
Maximum 3 rounds.

## 7. Stop / escalate
Halt and flag for a human if you detect a safeguarding or patient-safety concern, biased or
punitive framing, conflicting accounts, or notes too thin to support a safe plan.

## 8. Human sign-off
Present the plan clearly marked **DRAFT — pending human sign-off**, name the accountable role
(practice assessor / academic assessor), and add a **Reviewer notes** section listing
assumptions made and gaps to confirm. Never present it as final.

## 9. Audit log
Append a completed entry (using `references/audit-template.md`) to
`./practice-loop-audit/<today>-placement-support.md`, including the per-round scores and any flags.
