---
name: policy-to-practice
description: >
  Run a Practice Loop that turns a national report, guideline, or policy into a DRAFT plain-English
  summary plus a local governance action list, faithful to the source, with actions flagged for
  human decision and an audit trail. Use to translate national policy into local actions.
---

# Policy to Practice loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for the policy/report (or a link/extract). **HALT and ask** if any
accompanying material contains identifiable data unless the user confirms it is anonymised / IG-approved.

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
Draft a DRAFT plain-English summary and a candidate local governance action list (what may need to
change locally, who might own it, mapped to NMC Platforms 3 & 6).
You MUST NOT: decide or commit the organisation to governance/clinical actions; assert local
applicability as fact; invent owners/deadlines (mark "TBC"); misrepresent the source.

## 2.5 Proficiency & policy mapping
Cross-reference policy clauses against the NMC proficiencies database (`placement-support/references/proficiencies/`):
- Map care delivery rules to NMC Platform 3 (Assessing Needs & Care Planning; `P3`, `P7`, `P24`).
- Map safety/quality mandates to NMC Platform 6 (Safety & Quality Improvement; `P6`, `P18`, `P19`, `P25`).

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
Produce: a faithful summary (key points + what changed) and a candidate action list
(Action | Possible owner | NMC Platform/Proficiency | Source reference | For human decision).

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and escalate to a human where the policy implies a patient-safety, regulatory, or significant resource change requiring formal governance.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the relevant governance lead; actions are candidates for human decision, never commitments.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-policy-to-practice.md`, including per-round scores and any flags.

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.
