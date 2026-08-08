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

Then ask whether the nurse wants **cross-session memory** for this loop. If yes, ask for a
**pseudonym** for the subject of the loop — the student, preceptee or supervisee, or the
registrant themselves for reflective and revalidation loops (e.g. `student-alpha`, `self-2026`).
Never a real name, initials, staff number, or any other identifier. If no pseudonym is given,
run the loop statelessly and skip steps 1.5 and 10.

## 1.5 Recall — prior trajectory (opt-in)
If a pseudonym was given in step 1, read `./practice-loop-memory/<pseudonym>.json` **before**
you reason about this session. If the file does not exist, say so and continue — this is the
first recorded session for that pseudonym.

From the most recent entries, surface to the nurse in no more than five lines:
- open **learning gaps** carried forward, with the date each was first recorded,
- previous **flags**, and whether anything in this session repeats them,
- the **score trend** (`scores.round1_min` / `scores.final_min`) across entries, and
- `assessor_preferences` (trust name, custom verifier notes, preferred phrasing) if present.

Treat recalled content as **prior context to be confirmed, not established fact** — the nurse
may know it is out of date, superseded, or wrong. A gap or flag that reappears across sessions
is a signal to escalate a **pattern** rather than repeat the same action; say so explicitly if
you see one. Never infer a person's identity from memory content, and never merge two
pseudonyms into one record.

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

## 3.5 Gate 1 — nurse validates the reasoning (STOP)
Before drafting anything, present your **problem identification and diagnostic reasoning** and
stop for the nurse to confirm, correct, or reject it. Present briefly:
- what you assess the core concern(s) or signal(s) to be, and how you have categorised each,
- the NMC proficiencies you mapped in step 2.5, and why,
- what you are treating as **fact** versus **inference**, and
- anything recalled in step 1.5 that you are carrying into this session.

**Do not proceed to step 4 until the nurse has responded.** This is a stop condition, not a
rhetorical question. Categorising and framing the input is a registrant's judgement and it
changes the entire output, so this is the boundary of your authority. Where this loop
distinguishes a **learning need** from a **conduct concern**, that categorisation must be
confirmed here — never assumed. If the nurse corrects you, restate the corrected reasoning
before you draft.

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

