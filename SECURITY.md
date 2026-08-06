# Security Policy

> **Healthcare context**: Practice Loops processes clinical-adjacent text (nursing notes, supervision records, workforce metrics). No file contains patient-identifiable data by design, but contributors and users must treat all loop inputs with the same care as clinical information.

---

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x (current) | ✅ Active |
| < 0.1.0 | ❌ Not supported |

---

## Reporting a Vulnerability

**Please do NOT open a public GitHub Issue for security vulnerabilities.**

### How to Report

1. **GitHub Security Advisory**: Open a [GitHub Security Advisory](https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops/security/advisories/new) (private, GitHub-managed disclosure).
2. Include as much detail as possible:
   - Affected file(s) or loop(s)
   - Steps to reproduce
   - Potential impact (especially any clinical safety risk)
   - Suggested fix if known

### Response Timeline

| Stage | Target |
|-------|--------|
| Acknowledgement | Within **48 hours** |
| Initial triage | Within **5 business days** |
| Fix or mitigation | Within **30 days** (critical: 7 days) |
| Public disclosure | After fix is released |

We follow a **coordinated disclosure** model. Reporters are credited in the release notes unless they request anonymity.

---

## Scope

### In Scope

- Prompt injection vulnerabilities in any loop definition
- Logic flaws that could cause a loop to **skip the human sign-off step**
- Audit trail tampering or bypass
- Data leakage between loop sessions
- Verification score manipulation (e.g. always returning ≥ 8/10)
- CI/CD pipeline compromise (`.github/workflows/`)
- Malicious dependency injection in `plugins/` or `scripts/`

### Out of Scope

- Bugs in Claude itself (report to Anthropic)
- Theoretical attacks with no practical exploit path
- Social engineering of maintainers
- Issues in forks not maintained by this organisation

---

## Clinical Safety Principles

This project is built on the principle that **AI supports the workflow; the registered professional owns the judgement.**

Any vulnerability that could:
- Remove or weaken the **human sign-off requirement**
- Suppress a **risk escalation**
- Fabricate or alter an **audit trail**
- Cause a loop to output clinical advice without appropriate caveats

...is treated as **Critical severity** regardless of CVSS score, and will be fast-tracked for immediate remediation.

---

## NMC & Regulatory Alignment

Loops are designed against NMC (Nursing and Midwifery Council) standards. Security issues that could expose registrants to regulatory risk (e.g. audit trail gaps during an NMC fitness-to-practise investigation) are treated with the same urgency as patient safety issues.

---

## Acknowledgements

We thank the security research community for helping keep clinical AI tools safe and trustworthy.

---

*Maintained by the [Clinical Quality Artificial Intelligence (CQAI)](https://github.com/Clinical-Quality-Artifical-Intelligence) organisation.*
