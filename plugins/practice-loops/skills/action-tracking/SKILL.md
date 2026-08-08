---
name: action-tracking
description: >
  Run a Practice Loop that turns ANONYMISED meeting notes or a transcript into a DRAFT
  governance-ready action log — decisions, actions, owners, deadlines, and risks — faithful to
  the source, with risks flagged for human grading and an audit trail. Use for meeting action
  tracking and governance follow-up.
---

# Action Tracking loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order. Never skip verification or sign-off.

## 1. Intake
Confirm a manual start and ask for the meeting notes/transcript. **HALT and ask** if they contain
identifiable data unless the user confirms they are anonymised / IG-approved.

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
Produce a DRAFT governance-ready action log: decisions, actions, owners, deadlines, and risks (mapped to NMC Platforms 6 & 7).
You MUST NOT: invent owners or deadlines not stated (mark "owner/deadline TBC"); record a decision
the notes do not clearly support; assign final risk severity (flag risks for human grading instead).

## 2.5 Proficiency & governance mapping
Cross-reference governance actions against the NMC proficiencies database (`placement-support/references/proficiencies/`):
- Map safety/quality actions to NMC Platform 6 (Safety & Quality Improvement; `P6`, `P18`, `P19`, `P25`).
- Map care coordination actions to NMC Platform 7 (Care Coordination & Transition; `P26`, `P28`, `P29`).

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
Produce: an action log table (Decision/Action | NMC Platform/Proficiency | Owner | Deadline | Linked risk) and a separate
"Risks for human grading" list. Distinguish decisions from discussion.

## 5. Verify
Score against all 10 points in `references/verifier.md`. **Print each score out of 10** and name weaknesses.

## 6. Iterate
If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and flag any patient-safety or safeguarding item for immediate human attention.

## 8. Human sign-off
Present clearly marked **DRAFT — pending human sign-off** by the chair/governance lead; never present as final.

## 9. Audit log
Append a completed entry (audit format in the `practice-loop-method` skill) to
`./practice-loop-audit/<today>-action-tracking.md`, including per-round scores and any flags.

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.

