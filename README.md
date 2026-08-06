<div align="center">

# 🩺 Practice Loops for Nursing

### Safe, governed AI workflows for nurses — as a Claude Code plugin

*From the [Clinical Quality Artificial Intelligence (CQAI)](https://github.com/Clinical-Quality-Artifical-Intelligence) "Nurse as Citizen Developer" movement.*

[![validate](https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops/actions/workflows/validate.yml/badge.svg)](https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-1d9e75.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-da7756.svg)](https://code.claude.com/docs/en/plugins)
![Loops](https://img.shields.io/badge/loops-12-026a76.svg)
![Status](https://img.shields.io/badge/version-0.1.0-534ab7.svg)
![Human sign‑off](https://img.shields.io/badge/human%20sign--off-required-d85a30.svg)
[![Security Policy](https://img.shields.io/badge/security-policy-red.svg)](SECURITY.md)

<br/>

<img src="docs/framework/Nursing-LOOPS-infographic.png" alt="Practice Loops for Nursing — the prompt, the six-stage practice loop (trigger, task, standard, verification, iteration), human sign-off, and the components a loop needs" width="820">

</div>

---

## What is a Practice Loop?

A **Practice Loop** is a repeatable, AI-supported nursing workflow with a *job, a standard, and a stopping rule*. Instead of one-off prompting, each loop drives Claude through six pillars —

> **Trigger → Task → Standard → Verification → Iteration → Human Sign-Off**

— printing a 10-point verification score, self-correcting anything below 8/10, halting on risk, and writing an **audit trail** to disk.

> **AI supports the workflow; the registered professional owns the judgement.**

It maps directly onto the nursing process you already use: **Assess → Plan → Intervene → Evaluate → Adjust.**

---

## 🔁 The Loops

| Skill | Turns this… | …into a DRAFT |
|---|---|---|
| ✅ `action-tracking` | a meeting transcript | governance-ready action log; risks flagged for human grading |
| 💬 `clinical-supervision` | supervision notes | restorative follow-up record: themes, actions, prompts |
| ⚖️ `edi-intelligence` | aggregate workforce metrics | equity briefing using rate-based fair comparison |
| 🔍 `incident-reflection` | incident or near-miss notes | structured reflection: what happened, learning, actions |
| 🎓 `placement-support` | placement meeting notes | SMART action plan separating learning needs from conduct concerns |
| 📋 `policy-to-practice` | a policy or guideline | plain-English implementation guide mapped to ward context |
| 🔄 `practice-loop-method` | any clinical topic | a fully structured practice loop definition ready to run |
| 🌱 `preceptorship` | preceptee progress logs | 3-month review: confidence map + evidence gaps + reflective prompts |
| ♿ `reasonable-adjustments-passport` | an employee's adjustment needs | a completed Reasonable Adjustments Passport draft |
| 🪞 `reflective-practice` | a clinical experience or event | a structured reflection using Gibbs or ERA cycle |
| 📝 `revalidation` | practice hours + CPD log | a revalidation submission draft mapped to NMC requirements |
| 📚 `teaching` | a topic + audience level | session resource mapped to NMC proficiencies, with inclusive adjustments |

---

## 🚀 Quick Start

### 1. Install the plugin

In Claude Code, run:

```
/plugin install https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops
```

### 2. Run a loop

```
/placement-support
```

Claude will prompt you for your notes, run the six-pillar loop, and produce a draft for your review.

### 3. Sign off

Every loop ends with a **human sign-off step**. Claude cannot complete a loop without your explicit confirmation. The output and your sign-off are written to an audit trail file.

---

## 🏗️ How It Works

```
Trigger          ← you provide raw notes / context
   ↓
Task             ← Claude identifies the job to be done
   ↓
Standard         ← loop anchors to NMC standards / policy
   ↓
Verification     ← Claude scores itself /10; retries if < 8
   ↓
Iteration        ← Claude self-corrects up to 3 times
   ↓
Human Sign-Off   ← YOU review and approve the draft
   ↓
Audit Trail      ← full record written to disk
```

---

## 📁 Repository Structure

```
.claude-plugin/          Claude Code marketplace manifest
.github/workflows/       CI — validates loop definitions on every push
docs/
  framework/             Infographic and conceptual framework
  safety/                Safety and risk documentation
  superpowers/           What each loop can do
evals/                   Evaluation harnesses and test cases
examples/                Example inputs and expected outputs
plugins/
  practice-loops/
    skills/              One folder per loop (12 loops)
    hooks/               Pre/post loop hooks
scripts/                 Developer utilities
```

---

## 🛡️ Safety Principles

1. **No patient-identifiable data** — loops process de-identified professional notes only
2. **Human sign-off is mandatory** — every loop halts until a registered professional approves
3. **Audit trail by default** — every run is logged with timestamp, loop version, and sign-off record
4. **Risk escalation built-in** — loops halt and surface concerns rather than proceeding past risk thresholds
5. **NMC-anchored** — every output is mapped to the relevant NMC standard or Code clause

See [SECURITY.md](SECURITY.md) for the full security and disclosure policy.

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new loop, report a bug, or improve an existing skill.

All contributions must:
- Pass the `validate.yml` CI check
- Include an eval test case in `evals/`
- Include an example in `examples/`
- Maintain the human sign-off requirement — this is non-negotiable

---

## 📜 Licence

[Apache 2.0](LICENSE) — see [NOTICE](NOTICE) for attribution details.

---

## 🔒 Privacy

See [PRIVACY.md](PRIVACY.md) for data handling principles.

---

*Built with ❤️ for nursing by the [CQAI](https://github.com/Clinical-Quality-Artifical-Intelligence) "Nurse as Citizen Developer" movement.*
