---
name: revalidation
description: >
  Run a Practice Loop that checks ANONYMISED revalidation evidence (practice hours, CPD,
  feedback, reflective accounts) against the NMC revalidation requirements and drafts a
  portfolio readiness summary with gaps, escalation flags, and an audit trail. Use for
  preparing or reviewing an NMC revalidation portfolio.
---

# Revalidation loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for the revalidation evidence. **HALT and ask** if it contains
identifiable patient/colleague data (feedback must be anonymised) unless the user confirms it is
anonymised / IG-approved.

## 2. Task & boundaries
Draft a DRAFT portfolio readiness summary that checks the evidence against the NMC requirements (mapped to NMC proficiency platforms 1–7)
and lists gaps and next steps.
You MUST NOT: act as the confirmer or sign the registrant off; fabricate or assume hours, CPD, or
reflective content; make a fitness-to-practise judgement.

## 2.5 Proficiency platform & evidence mapping
Cross-reference the revalidation evidence (CPD hours, feedback, reflective accounts) against the NMC proficiencies database (`placement-support/references/proficiencies/`):
- Map practice hours and CPD topics across the 7 NMC Platforms (1: Professionalism, 2: Health promotion, 3: Assessment/care planning, 4: Care delivery, 5: Leadership/teamwork, 6: Safety/quality, 7: Care coordination).
- Ensure reflective accounts explicitly reference NMC proficiencies (`P1`–`P29`) and Code themes.

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce: a requirements checklist (met / partial / gap, with evidence pointer and NMC Platform mapping) and a prioritised
list of actions to be revalidation-ready.

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and escalate to a human if the evidence suggests a health, conduct, or fitness-to-practise concern, or if confidential third-party data is present.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the registrant (and, separately, the confirmer); never present as a completed or confirmed portfolio.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-revalidation.md`, including per-round scores and any flags.

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.

