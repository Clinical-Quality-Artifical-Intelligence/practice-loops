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
- [ ] **Both Gates Present**: Gate 1 (§3.5 — reasoning presented and the loop **stops** for the nurse before drafting) and Gate 2 (§7–8 — stop/escalate and DRAFT sign-off).
- [ ] **Memory Symmetry**: If the loop writes memory (§10) it also reads it (§1.5), and §1 asks for a pseudonym. Never a real name.
- [ ] **DRAFT Output**: All generated outputs are explicitly marked `DRAFT`.
- [ ] **Audit Trail**: Output is configured to write to `./practice-loop-audit/`.
- [ ] **NMC Standards**: Loop is mapped to relevant NMC standards or Code clauses.
- [ ] **CI Validation**: Passed local validation via `npm test` (or `python scripts/validate.py`, `python scripts/check_guardrails.py`, `python scripts/check_manifests.py`). Note `python`, not `python3` — the latter does not resolve on Windows.

## Related Issues

Closes #
