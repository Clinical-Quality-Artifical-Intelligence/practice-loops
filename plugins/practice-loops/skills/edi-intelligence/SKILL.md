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

Then ask whether the nurse wants **cross-session memory** for this dataset. If yes, ask for a
**cohort or dataset pseudonym** (e.g. `ward-3-2026q2`, `trust-directorate-A`) — never an
individual, and never a real name or identifier. This loop handles aggregate data only: do
**not** create or update a memory record about any single person. If no pseudonym is given,
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

## 10. Memory update (opt-in)
If a learner pseudonym was provided during intake, append a trajectory entry to
`./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped,
verification scores (round 1 min and final min), any flags, learning gaps identified, and
strengths observed. Follow the schema in `./practice-loop-memory/schema.json`.
Never store real names or identifiable data in the memory file.

