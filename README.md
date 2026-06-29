# Practice Loops for Nursing

> A Claude Code plugin from **Clinical Quality Artificial Intelligence (CQAI)** — the "Nurse as Citizen Developer" movement.

A **Practice Loop** is a repeatable, AI-supported nursing workflow with a job, a standard, and a stopping rule. Instead of one-off prompting, each loop drives Claude through six pillars — **Trigger → Task → Standard → Verification → Iteration → Human Sign-Off** — printing a 10-point verification score, self-correcting anything below 8/10, halting on risk, and writing an audit trail to disk. **AI supports the workflow; the registered professional owns the judgement.**

## The loops

| Skill | What it does |
|---|---|
| `/practice-loops:placement-support` | Anonymised placement notes → DRAFT SMART action plan separating learning needs from conduct concerns |
| `/practice-loops:preceptorship` | Progress logs → DRAFT 3-month review: confidence map + evidence gaps + reflective prompts |
| `/practice-loops:clinical-supervision` | Supervision notes → DRAFT restorative follow-up record: themes, actions, prompts |
| `/practice-loops:edi-intelligence` | Aggregate workforce metrics → DRAFT equity briefing using rate-based fair comparison |
| `/practice-loops:teaching` | Topic + level → DRAFT session resource mapped to NMC proficiencies, with inclusive adjustments |
| `/practice-loops:action-tracking` | Meeting transcript → DRAFT governance-ready action log; risks flagged for human grading |
| `/practice-loops:practice-loop-method` | The shared method (explains/anchors all of the above) |

## Install

In Claude Code:

```
/plugin marketplace add Clinical-Quality-Artifical-Intelligence/practice-loops
/plugin install practice-loops
```

Then invoke a loop by name (e.g. `/practice-loops:placement-support`) or in natural language ("run a placement support loop on these notes"). See `examples/` for an anonymised sample input and the audit log it produces.

## ⚠️ Clinical-safety note

- **Anonymised inputs only.** Never paste identifiable patient or staff data; the loops will halt and ask if they detect it. Do not use any AI tool on identifiable data without your organisation's Information Governance approval.
- **Every output is a DRAFT** pending sign-off by a named registered professional. The loop never finalises.
- **Never** use a loop to decide pass/fail or fitness to practise, diagnose or treat, determine mental capacity, or make final safeguarding, disciplinary, or employment decisions.
- This is **not a medical device** and does not replace professional judgement. The audit log records what the assistant did; it is not an independent assurance check.

## Local development

```bash
claude --plugin-dir ./plugins/practice-loops   # load without installing
# then /reload-plugins after edits
python3 scripts/validate.py                     # structural check
claude plugin validate ./plugins/practice-loops # official check
```

## Background & framework

The full framework — playbook, templates, the master guide, and the source decks — lives in [`docs/framework/`](docs/framework/). Design spec and implementation plan are under [`docs/superpowers/`](docs/superpowers/).

## Licence & attribution

Apache-2.0 (see `LICENSE`). © Clinical Quality Artificial Intelligence. Practice Loops framework by Lincoln Gombedza.
