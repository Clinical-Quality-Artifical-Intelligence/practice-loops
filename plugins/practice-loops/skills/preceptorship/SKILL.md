---
name: preceptorship
description: >
  Run a Practice Loop that turns ANONYMISED preceptee progress logs into DRAFT 3-month
  review materials — a confidence map by clinical area and an evidence-gaps list with
  reflective prompts — scored against the preceptorship framework, with escalation flags
  and an audit trail. Use for preceptorship reviews of newly qualified nurses.
---

# Preceptorship loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for the preceptee's progress logs. **HALT and ask** if they
contain identifiable data unless the user confirms they are anonymised / IG-approved.

## 2. Task & boundaries
Prepare DRAFT 3-month review materials: (a) a confidence map by clinical area mapped to NMC proficiencies, (b) an
evidence-gaps list, (c) strengths-based reflective prompts.
You MUST NOT: declare preceptorship complete or signed off; make a competence or capability
judgement; assume confidence the logs do not evidence.

## 2.5 Proficiency & preceptorship mapping
Cross-reference the preceptee's progress logs against the NMC proficiencies reference database (see `placement-support/references/proficiencies/`):
- Map observed confidence signals and practice areas to specific NMC proficiencies (e.g. `P7`, `P18`, `P21`).
- For evidence gaps, identify which specific proficiencies require further consolidation or observation.
- Flag any safety-critical proficiencies (marked `*`) requiring ongoing direct supervision.

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce: confidence map (Clinical Area | NMC Mapped Proficiency | Evidence from Logs | Confidence Signal), evidence-gaps
list (mapped to proficiencies), and 5–8 open reflective prompts.

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and flag for a human on any patient-safety, wellbeing, or practice concern, or logs too thin to support a fair review.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the preceptor; add Reviewer notes
(assumptions, gaps to confirm with the preceptee). Never present as final or as a completion decision.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-preceptorship.md`, including per-round scores and any flags.
