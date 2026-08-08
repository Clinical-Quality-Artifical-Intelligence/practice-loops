---
name: incident-reflection
description: >
  Run a Practice Loop that turns an ANONYMISED incident or near-miss into a DRAFT learning-focused
  reflective summary in a just-culture tone — contributing factors and learning, NOT root-cause or
  blame — with safety escalation flags and an audit trail. Use for learning from incidents/near-misses.
---

# Incident Reflection loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for the anonymised incident/near-miss account. **HALT and ask** if
it contains identifiable patient/staff data unless the user confirms it is anonymised / IG-approved.

## 2. Task & boundaries
Draft a DRAFT learning-focused summary: what happened (factually), contributing factors (systems
lens), and learning/actions (mapped to NMC safety & quality proficiencies) — in a just-culture, non-blaming tone.
You MUST NOT: determine root cause as a finding; apportion blame or judge individual conduct;
make a Duty of Candour, disciplinary, or patient-safety incident-grading decision.

## 2.5 Proficiency & safety mapping
Cross-reference the incident learning points against the NMC proficiencies database (`placement-support/references/proficiencies/`):
- Map system/human/environmental learning points to specific NMC proficiencies (e.g. `P6` quality/safety improvement, `P7` deterioration, `P19` IPC, `P25` hazard response).
- Highlight valid assessment/remediation methods for preventing recurrence.

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce: factual summary | contributing factors (system/human/environment) | learning points mapped to NMC proficiencies (`P6`, `P7`, `P19`, `P25`) |
suggested actions for human consideration.

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and escalate immediately if the incident indicates ongoing patient-safety risk, a safeguarding concern, or a possible Duty of Candour trigger — for human decision, not the loop's.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the appropriate lead; never present as a root-cause analysis, incident grade, or candour decision.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-incident-reflection.md`, including per-round scores and any flags.

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.

