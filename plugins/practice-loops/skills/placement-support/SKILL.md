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

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.

