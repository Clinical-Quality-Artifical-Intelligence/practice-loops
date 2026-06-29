# Contributing

Thanks for helping build safe, governed practice loops for nursing.

## Add a new loop

1. Copy the flagship as a template:
   ```bash
   cp -r plugins/practice-loops/skills/placement-support plugins/practice-loops/skills/<your-loop>
   ```
2. Edit the four files:
   - `SKILL.md` — frontmatter `name`/`description`, and the Task, Boundaries, and step details.
   - `references/verifier.md` — the 10-point check tuned to this loop.
   - `references/nmc-standard.md` — the relevant NMC / policy / Equality Act anchors.
   - (optional) `references/audit-template.md` — or reuse the audit format in the `practice-loop-method` skill.
3. Add the loop name to `EXPECTED` in `scripts/validate.py`.
4. Validate:
   ```bash
   python3 scripts/validate.py
   claude plugin validate ./plugins/practice-loops
   ```
5. Commit with a `feat: add <loop> loop skill` message.

## Non-negotiables

Every loop **must**:
- Halt on apparently identifiable data (no identifiable data without IG approval).
- Print verification scores and self-correct anything below 8/10.
- Mark its output **DRAFT — pending human sign-off** and never finalise.
- Write an audit entry to `./practice-loop-audit/`.
- Keep the clinical red lines intact (no pass/fail, diagnosis/treatment, capacity, final safeguarding/disciplinary/HR decisions).

## Style

Keep skills tight and imperative. Mirror the framework wording in `docs/framework/`. Use anonymised examples only.
