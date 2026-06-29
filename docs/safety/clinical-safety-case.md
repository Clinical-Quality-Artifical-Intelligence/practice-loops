# Clinical Safety Case Report — Practice Loops plugin

**Standard:** DCB0129 — Clinical Risk Management: its Application in the Manufacture of Health IT Systems
**Manufacturer:** Clinical Quality Artificial Intelligence (CQAI)
**Product:** `practice-loops` Claude Code plugin, v0.1.0
**Status:** ⚠️ **DRAFT — requires review and sign-off by a named Clinical Safety Officer (CSO).** This document is populated by the manufacturer as a starting point; it is not a completed safety case until a suitably qualified CSO has reviewed it, agreed the hazard log, and signed the declaration. Extend it with the `dcb0129`, `hazard-log`, and `crm-plan` skills.

---

## 1. Scope and purpose

The product is a set of AI-supported **Practice Loops** delivered as a Claude Code plugin for nursing education, supervision, and governance tasks (placement support, preceptorship, clinical supervision, EDI workforce intelligence, teaching, action tracking). Each loop produces a **draft** document for a registered professional to review and sign off.

**Intended use:** assist registered nurses, educators, PEFs, supervisors, and EDI/governance leads with repeated, structured, reviewable documentation tasks using **anonymised** inputs.

**Out of scope / not intended for:** direct patient care, clinical decision-making, or any of the clinical red lines (see §4). The product is **not a medical device**; it does not diagnose, treat, or make decisions about individuals.

## 2. Clinical risk management system

CQAI applies a clinical risk management process aligned with DCB0129. Roles: a named **Clinical Safety Officer** (a registered clinician) owns clinical risk; the development team implements controls. Evidence is maintained in this repository (`docs/safety/`), with the hazard log in [`hazard-log.md`](hazard-log.md).

## 3. Clinical risk analysis (summary)

Hazards were identified by considering how the product could contribute to patient or staff harm through its outputs and use. The full analysis is in the hazard log. Principal hazards:

| ID | Hazard | Principal controls |
|----|--------|--------------------|
| H1 | "Quiet failure": plausible-but-inaccurate output accepted | Visible 10-point verification; 8/10 self-correction; mandatory DRAFT + human sign-off; audit log |
| H2 | Identifiable patient/staff data entered into the tool | Anonymised-only design; PII-guard hook; in-loop identifiable-data HALT; README/NOTICE warnings |
| H3 | Automation bias — DRAFT treated as final, sign-off skipped | DRAFT labelling on every output; mandatory sign-off step; named accountable role; training note |
| H4 | Loop used for a clinical red-line decision | Explicit red lines in the method skill and per-loop boundaries; escalation step |
| H5 | Missed escalation of a safeguarding / clinical-risk cue | Stop/escalate step; verifier point 9; behavioural eval fixtures exercise the cue |
| H6 | Bias amplification / deficit or discriminatory framing | Verifier tone + equity points; EDI rate-based method; Equality Act anchor in standards |
| H7 | Audit-log integrity (model-written, not independently enforced) | Audit template; `check-audit.py` linter; documented limitation; CSO periodic review |
| H8 | Outdated/incorrect clinical content taught (teaching loop) | "Verify against current local/national guidance before teaching" flag; teaching verifier |
| H9 | Tampering / weakened guardrails after modification | `check_guardrails.py` static eval in CI; Apache-2.0 provenance; version pinning |

## 4. Clinical red lines (hazard controls of last resort)

The product must never be used to make a final decision on: pass/fail or fitness to practise; clinical diagnosis or treatment; mental capacity; safeguarding outcomes; disciplinary outcomes; HR/employment outcomes. No identifiable data without Information Governance approval. These are encoded in the `practice-loop-method` skill and each loop's boundaries.

## 5. Risk evaluation and acceptability

Using the NHS clinical risk matrix (severity × likelihood; see hazard log legend), all identified hazards reduce to an **acceptable** or **ALARP** residual rating after the controls above, **on the condition that** the mandatory human sign-off and anonymisation controls are honoured in use. Residual risk depends on deploying organisations enforcing local IG and sign-off — see deployment assumptions (§7).

## 6. Residual risk and limitations

- The audit log is **model-generated** and records what the assistant did; it is **not an independent assurance mechanism** (H7). A future enforced-engine implementation would strengthen this.
- Verification is **prompted** within the skill plus a **static guardrail eval** in CI; it is not a runtime hard gate. Human sign-off remains the primary safety control.
- The PII-guard hook is a **non-blocking** warning safety net, not a guarantee.

## 7. Deployment assumptions (for the deploying organisation — DCB0160)

A deploying NHS/education organisation should: confirm IG approval and anonymisation practice; require named human sign-off on every output; brief users on the red lines and automation bias; and review audit logs periodically. A DCB0160 deployment safety case should be produced locally.

## 8. Conclusion

Subject to CSO review and the deployment assumptions, the residual clinical risk of the `practice-loops` plugin is considered acceptable for its intended use (anonymised, draft-only, human-signed-off nursing documentation support).

## 9. Clinical Safety Officer declaration

> I confirm I have reviewed this clinical safety case and the associated hazard log, that the clinical risks have been managed to an acceptable level for the intended use, and that residual risks and deployment assumptions are clearly stated.

- CSO name / registration: ____________________
- Signature: ____________________  Date: __________
