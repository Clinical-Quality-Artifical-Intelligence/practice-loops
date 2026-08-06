## Summary of Changes

Brief description of what this PR introduces or fixes.

## Type of Change

- [ ] 🩺 New Practice Loop / Skill
- [ ] 🐛 Bug fix in existing loop definition
- [ ] 🛡️ Security / Governance enhancement
- [ ] 📚 Documentation update
- [ ] 🧪 Evals / Test fixture update

## Practice Loop Quality & Safety Checklist

- [ ] **No Identifiable Data**: Verification script confirms no patient or staff identifiable details are included in examples or skills.
- [ ] **Six Pillars Encoded**: If adding/updating a loop, it includes Trigger, Task, Standard, Verification (/10), Iteration (<8), and Human Sign-Off.
- [ ] **DRAFT Output**: All generated outputs are explicitly marked `DRAFT`.
- [ ] **Audit Trail**: Output is configured to write to `./practice-loop-audit/`.
- [ ] **NMC Standards**: Loop is mapped to relevant NMC standards or Code clauses.
- [ ] **CI Validation**: Passed local validation via `python3 scripts/validate.py` and `python3 scripts/check_guardrails.py`.

## Related Issues

Closes #
