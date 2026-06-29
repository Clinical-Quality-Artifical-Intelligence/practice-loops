# Practice Loops — evaluation suite

Two layers of evaluation:

## 1. Static guardrail eval (automated, runs in CI)

`python3 scripts/check_guardrails.py` asserts every loop skill encodes the
non-negotiable safety clauses (identifiable-data HALT, anonymisation/IG check, bounded
task, verification scoring, the 8/10 iteration rule, escalation, DRAFT output, human
sign-off, audit log) and that the method skill documents the clinical red lines. No model
required — this is the regression guard for safety wording.

## 2. Behavioural fixtures (model-in-the-loop)

`cases.md` lists, per loop, an input and the behaviour a correct run must exhibit. These
need a Claude session to execute (the loop is a skill, not a function), so they are run
manually or in a model-backed CI job. The anonymised inputs in [`../examples/`](../examples/)
double as fixtures, each with a matching `*.audit.sample.md` showing the expected shape.

### How to run a behavioural case
```text
claude --plugin-dir ./plugins/practice-loops
/practice-loops:<loop>        # paste the fixture input
```
Then confirm the "Expect" checks in `cases.md` for that loop.
