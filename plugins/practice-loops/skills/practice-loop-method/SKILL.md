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

## Lifecycle events
Every loop execution maps to five named lifecycle phases:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  on_intake   │───►│  on_gate1    │───►│  on_verify   │───►│  on_gate2    │───►│  on_commit   │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
  PII HALT, recall    Diagnostic         10-Point Score      Final Sign-Off      Audit File &
  & provenance        validation (STOP)  & Iteration         Approval            Memory Update
```

1. **on_intake** (Steps 1–1.5): PII detection, provenance check, and — if a pseudonym was given
   — recall of the prior trajectory before any reasoning begins.
2. **on_gate1** (Steps 2–3.5): Bounded task and boundaries declared, standard and matched
   proficiencies loaded, then diagnostic reasoning presented to the nurse. **The loop stops
   here until the nurse confirms or corrects it** — nothing is drafted before that.
3. **on_verify** (Steps 4–6): Draft production, 10-point scoring, and sub-8 iteration.
4. **on_gate2** (Steps 7–8): Stop/escalate check and human sign-off — output is always DRAFT.
5. **on_commit** (Steps 9–10): Audit log written to disk and memory updated (if a pseudonym was
   provided at intake).

## The universal loop protocol
Every loop skill in this plugin follows these steps in order, and never skips sign-off.

1. **Intake / Trigger.** Confirm a manual start and ask for the input. **HALT** if the content
   looks like identifiable patient/staff data (names, DOB, NHS number, addresses) unless the
   user confirms it is anonymised / IG-approved. Then offer cross-session memory and, if the
   nurse wants it, take a **pseudonym** — never a real name or identifier.
1.5. **Recall (opt-in).** If a pseudonym was given, read
   `./practice-loop-memory/<pseudonym>.json` **before reasoning** and surface open learning
   gaps, prior flags, the score trend, and any `assessor_preferences`. Recalled content is
   prior context **to be confirmed, not established fact**. A gap that recurs across sessions
   is a pattern to escalate, not an action to repeat.
2. **Task.** Restate the bounded task and the "must NOT decide" boundaries.
3. **Standard.** Load the loop's `references/nmc-standard.md`.
3.5. **Gate 1 — nurse validates the reasoning (STOP).** Present problem identification and
   diagnostic reasoning — how each concern is categorised, the mapped proficiencies, fact
   versus inference, and anything carried in from recall — then **wait for the nurse to confirm
   or correct it before drafting**. This is a stop condition: categorisation is a registrant's
   judgement and it changes the entire output.
4. **Draft.** Produce the output.
5. **Verify.** Score against the 10 points below, **printing each score out of 10** and naming weaknesses.
6. **Iterate.** If any point is below 8, revise the weakest part, explain the change, re-score. Max 3 rounds.
7. **Stop / escalate.** Halt and flag on: conflict or biased language · messy or insufficient input ·
   safeguarding or urgent clinical risk · anything needing nuanced ethical judgement.
8. **Human sign-off.** Present clearly marked **DRAFT — pending human sign-off**; name the
   accountable role; never present as final.
9. **Audit log.** Append an entry to `./practice-loop-audit/YYYY-MM-DD-<loop>.md` (format below).
10. **Memory update (opt-in).** If a pseudonym was provided at intake, append a trajectory entry to `./practice-loop-memory/<pseudonym>.json` recording: date, loop name, proficiencies mapped, verification scores (round 1 min and final min), any flags, learning gaps, and strengths. Follow the schema in `./practice-loop-memory/schema.json`. Never store real names or identifiable data.

Steps 1.5 and 10 are the two halves of one mechanism. A loop that writes memory but never reads
it accumulates a record nobody benefits from; a loop that reads without writing cannot improve.
If a loop implements one, it must implement the other.

## Programmatic vs agent-triggered operations
Not every operation should be the assistant's choice, and the boundary is deliberate. Two
failure modes sit either side of it: load too much automatically and the context bloats; leave
too much to the assistant's discretion and safety-relevant context goes missing.

| Operation | Programmatic | Agent-triggered | Why |
|---|:---:|:---:|---|
| Recall prior trajectory (1.5) | Yes | No | A loop must never decide whether to look at its own history |
| Load matched proficiencies (2.5) | Yes | No | The standard is not optional |
| Load the loop's `nmc-standard.md` (3) | Yes | No | As above |
| Present Gate 1 reasoning (3.5) | Yes | No | The nurse's judgement is not an optimisation to trade away |
| Score against the verifier (5) | Yes | No | Verification cannot be skipped |
| Write the audit entry (9) | Yes | No | Governance evidence, not a convenience |
| Write the memory entry (10) | Yes | No | Automatic once a pseudonym exists |
| Expand a recalled entry in full | No | Yes | Only when the recalled summary is insufficient |
| Load an additional proficiency cluster | No | Yes | Only when the input reveals a theme the keywords missed |
| Escalate under step 7 | No | Yes | Requires judgement about what was actually observed |

Everything in the first group runs whether or not the assistant judges it necessary. That is a
**safety** property rather than an efficiency one: a loop that could choose to skip its own
escalation history is not a governed loop.

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
- Memory (step 1.5): pseudonym [none | <pseudonym>] · prior entries recalled: <n> · gaps carried forward: <list | none>

## Gate 1 — diagnostic reasoning review (step 3.5)
- Presented at: <ISO8601>
- Reasoning presented: <categorisation · proficiencies mapped · fact vs inference>
- Registrant response: [confirmed | corrected | rejected]
- Correction made: <none | what the registrant changed>
- Confirmed by: ____________________   Date: __________

## Verification scores
| Round | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Min |
|-------|---|---|---|---|---|---|---|---|---|----|-----|
| 1     |   |   |   |   |   |   |   |   |   |    |     |

## Escalations / flags
- <none | description + recommended human action>

## Gate 2 — accountable final sign-off
DRAFT — pending human sign-off by: ____________________   Date: __________
```

Both gates are logged, not just the final one. `ADPIE-DUAL-GATE-GOVERNANCE.md` requires the audit
file to record the Gate 1 confirmation alongside the Gate 2 sign-off: an audit trail that shows
only the final signature cannot evidence that a registrant validated the reasoning *before* the
plan was drafted, which is the whole point of the mid-loop gate.
