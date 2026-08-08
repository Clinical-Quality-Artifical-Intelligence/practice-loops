---
name: practice-loop-method
description: >
  The Practice Loop method for nursing — the six pillars, the 10-point verifier, the
  8/10 scoring rule, stop/escalation conditions, human sign-off, and the audit log.
  Use when explaining practice loops, or as the shared method behind any specific loop
  skill in this plugin.
---

# The Practice Loop method

A Practice Loop is a repeatable, AI-supported nursing workflow with a job, a standard, and a
stopping rule. **AI supports the workflow; the registered professional owns the judgement.**

## The six pillars
1. **Trigger** — a manual start (the nurse initiates).
2. **Task** — a bounded job that states what the AI must NOT decide.
3. **Standard** — the NMC Code / Standards of Proficiency / Trust policy / Equality Act anchor (mapped to the `references/proficiencies/` database).
4. **Verification** — score the draft against the 10-point verifier.
5. **Iteration** — fix anything scoring below 8/10 before a human sees it.
6. **Human sign-off** — a registrant reviews and is accountable; output is always a DRAFT.

Maps to the nursing process: Assess → Plan → Intervene → Evaluate → Adjust.

## Context curation principle
Loops use **dynamic context curation** rather than context stuffing. When mapping to NMC proficiencies:
- Scan the input for clinical keyword clusters (via `references/proficiencies/index.json`).
- Load **only** the matched proficiency rows from the relevant year file — not all 48 proficiencies.
- This keeps the prompt context lean, sharp, and deterministic.

## The universal loop protocol
Every loop skill in this plugin follows these steps in order, and never skips sign-off.

1. **Intake / Trigger.** Confirm a manual start and ask for the input. **HALT** if the content
   looks like identifiable patient/staff data (names, DOB, NHS number, addresses) unless the
   user confirms it is anonymised / IG-approved.
2. **Task.** Restate the bounded task and the "must NOT decide" boundaries.
3. **Standard.** Load the loop's `references/nmc-standard.md`.
4. **Draft.** Produce the output.
5. **Verify.** Score against the 10 points below, **printing each score out of 10** and naming weaknesses.
6. **Iterate.** If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.
7. **Stop / escalate.** Halt and flag on: conflict or biased language · messy or insufficient input ·
   safeguarding or urgent clinical risk · anything needing nuanced ethical judgement.
8. **Human sign-off.** Present clearly marked **DRAFT — pending human sign-off**; name the
   accountable role; never present as final.
9. **Audit log.** Append an entry to `./practice-loop-audit/YYYY-MM-DD-<loop>.md` (format below).

## The 10-point verifier
1. Concern clearly described
2. Evidence separated from opinion
3. Conduct distinguished from capability
4. Actions are SMART
5. Review date clear
6. Responsibilities named
7. Language supportive and non-punitive
8. Reasonable adjustments considered
9. Escalation surfaced
10. No unauthorised decisions made

## The clinical red lines — never use a loop to:
- Decide pass/fail or fitness to practise
- Diagnose a patient or decide clinical treatment
- Determine mental capacity
- Make final safeguarding or disciplinary decisions
- Make HR or employment outcomes
- Process identifiable patient data without IG approval

## Audit log format
Append to `./practice-loop-audit/YYYY-MM-DD-<loop>.md`:

```
# Practice Loop run — <loop>
- Timestamp: <ISO8601>
- Operator: <name/role>
- Loop & version: <loop> v<plugin version>
- Input provenance: anonymised? [yes/no] · IG reference: <if any>
- Boundaries declared: <what AI must not decide>

## Verification scores
| Round | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Min |
|-------|---|---|---|---|---|---|---|---|---|----|-----|
| 1     |   |   |   |   |   |   |   |   |   |    |     |

## Escalations / flags
- <none | description + recommended human action>

## Status
DRAFT — pending human sign-off by: ____________________   Date: __________
```
