# Design Spec — `practice-loops` Claude Code Plugin

- **Date:** 2026-06-29
- **Status:** Draft for review
- **Author:** Lincoln Gombedza · Nursing Citizen Development / Clinical Quality Artificial Intelligence (CQAI)
- **Topic:** Turn the "Practice Loops for Nursing" framework into runnable Claude Code skills, distributed as a plugin.

## 1. Summary

Build a Claude Code **plugin** named `practice-loops` that ships one **skill per Practice Loop**. Each skill turns the framework's six pillars (Trigger → Task → Standard → Verification → Iteration → Human Sign-Off) into an enforced, repeatable protocol that Claude follows, including a **visible 10-point verification score**, a **self-correction loop with an 8/10 threshold**, **stop/escalation conditions**, a mandatory **human sign-off** gate, and a **structured audit log written to disk** on every run.

We build **flagship-first**: a shared `practice-loop-method` skill plus the **Placement Support** loop, fully working and tested, then replicate the pattern to the remaining five loops.

## 2. Goals / Non-goals

**Goals**
- A nurse adds one marketplace and installs every Practice Loop as a skill.
- Each loop is *governable*: visible scoring, red lines, escalation, and an audit trail — not "AI agreeing with itself."
- Loops are short to invoke (`/practice-loops:placement-support`) and model-invokable from natural language ("run a placement support loop on these notes").
- Reuses the NMC standards and language already established in the framework docs.

**Non-goals (YAGNI)**
- No web app / Hugging Face Space in this iteration (may wrap the same skills later).
- No programmatic enforcement engine in code (chosen model is skills; enforcement is via the SKILL.md protocol + audit log).
- No processing of identifiable patient data — the loops are designed for anonymised inputs only.
- No automated triggers/automation — manual invocation only (per the framework's "start manual" rule).

## 3. Context

- Framework + content: `Practice-Loops-for-Nursing-MASTER-GUIDE.md`, `Practice-Loops-for-Nursing-Playbook.md`, `Practice-Loop-Templates.md`, and the three source documents in this folder.
- Org: `github.com/Clinical-Quality-Artifical-Intelligence` (CQAI) — UK open-source, "Nurse as Citizen Developer," sibling repos include `open-nursing-core-ig`, `nursing-council-agent`, `nhs-preceptorship-transparency`.
- Research basis: loop engineering (Boris Cherny / Anthropic; Addy Osmani); separate verifier; state on disk; stop conditions.

## 4. Locked decisions

1. **Run target:** Claude Code skills.
2. **Packaging:** Claude Code plugin + marketplace.
3. **Scope/sequence:** flagship-first — shared method skill + Placement Support, then replicate the other five.
4. **License:** Apache-2.0. **Repo location:** inside the existing `/Volumes/Backup/practice loops/` folder.

## 5. Architecture

```
Marketplace (.claude-plugin/marketplace.json)
   └── Plugin: practice-loops (.claude-plugin/plugin.json)
         └── skills/
               ├── practice-loop-method/      ← shared protocol, audit format, red lines, "teach the method"
               ├── placement-support/          ← FLAGSHIP (built fully)
               ├── preceptorship/              ← replicated
               ├── clinical-supervision/       ← replicated
               ├── edi-intelligence/           ← replicated
               ├── teaching/                   ← replicated
               └── action-tracking/            ← replicated
```

- **Skills are model-invoked** via their `description` frontmatter, and also directly callable as `/practice-loops:<loop>`.
- Each loop skill is **self-contained** (restates the critical guardrails) but points to `practice-loop-method` for the full method, so the loops stay consistent and short.
- **State/audit lives on disk** in the user's working directory: `./practice-loop-audit/`.

## 6. Repository structure

The repo root is the existing folder. New plugin files are added without disturbing the existing docs (which move under `docs/` for tidiness during implementation).

```
practice loops/                      (git repo root → GitHub: practice-loops)
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── practice-loops/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           ├── practice-loop-method/SKILL.md
│           └── placement-support/
│               ├── SKILL.md
│               └── references/
│                   ├── verifier.md
│                   ├── nmc-standard.md
│                   └── audit-template.md
├── examples/
│   ├── placement-support.input.md        (anonymised sample)
│   └── placement-support.audit.sample.md (resulting audit log)
├── docs/                                  (existing master guide, playbook, templates, decks, infographic)
├── README.md
├── CONTRIBUTING.md
├── LICENSE                                (Apache-2.0)
└── .gitignore                            (ignores practice-loop-audit/, OS cruft; PDFs handled per §16)
```

## 7. Manifest files

**`.claude-plugin/marketplace.json`**
```json
{
  "name": "cqai-practice-loops",
  "owner": { "name": "Clinical Quality Artificial Intelligence" },
  "metadata": { "description": "Safe, governed AI practice loops for nursing." },
  "plugins": [
    {
      "name": "practice-loops",
      "source": "./plugins/practice-loops",
      "description": "One skill per nursing Practice Loop: trigger, task, NMC standard, verification, iteration, human sign-off, and an audit trail."
    }
  ]
}
```

**`plugins/practice-loops/.claude-plugin/plugin.json`**
```json
{
  "name": "practice-loops",
  "description": "Safe, governed AI practice loops for nursing (placement support, preceptorship, clinical supervision, EDI, teaching, action tracking).",
  "version": "0.1.0",
  "author": { "name": "Clinical Quality Artificial Intelligence" },
  "homepage": "https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops",
  "repository": "https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops",
  "license": "Apache-2.0"
}
```

## 8. The shared `practice-loop-method` skill

Frontmatter `description`: *"Explains and enforces the Practice Loop method for nursing — the six pillars, the 10-point verifier, the 8/10 scoring rule, stop conditions, human sign-off, and the audit log. Use when asked about practice loops, or as the method behind any specific loop."*

Body contents:
- The six pillars and the nursing-process mapping.
- The **universal loop protocol** (the 9 steps in §9) that every loop skill must follow.
- The **clinical red lines** (never-automate list) and the **identifiable-data halt rule**.
- The **audit log format** (§11) and where it is written.
- The 8/10 scoring rule and the four stop/escalation triggers.

## 9. Loop skill anatomy — the enforced protocol

Each loop's `SKILL.md` instructs Claude to execute these steps **in order**, and to refuse to skip the sign-off:

1. **Intake / Trigger.** Confirm manual start. Ask for the input (notes/transcript). **Halt** if the content appears to contain identifiable patient/staff data unless the user confirms it is anonymised / IG-approved.
2. **Task.** State the bounded task and the explicit "you must NOT decide" boundaries for this loop.
3. **Standard.** Load `references/nmc-standard.md` for this loop.
4. **Draft.** Produce the output.
5. **Verify.** Score the draft against the 10 points in `references/verifier.md`, **printing each score /10** and naming what is weak.
6. **Iterate.** If any point < 8/10, revise the weakest part, explain the change, re-score. Max **3 rounds**.
7. **Stop / escalate.** Halt and flag immediately on: conflict or biased/discriminatory content; messy/insufficient input; safeguarding or urgent clinical risk; or anything needing nuanced ethical judgement.
8. **Human sign-off.** Present the result clearly marked **DRAFT — pending human sign-off**, name the accountable role, and never present it as final.
9. **Audit log.** Append a structured entry to `./practice-loop-audit/YYYY-MM-DD-<loop>.md` (template in §11).

Frontmatter per loop (example, Placement Support):
```yaml
---
name: placement-support
description: >
  Run a Practice Loop that turns placement meeting notes into a DRAFT SMART action
  plan, separating learning needs from conduct concerns, scored against NMC standards,
  with escalation flags and an audit trail. Use for student placement support / action plans.
---
```

## 10. Reference files (per loop)

- **`verifier.md`** — the 10-point check (concern clear; evidence vs opinion; conduct vs capability; SMART; review date; named responsibilities; supportive/non-punitive; reasonable adjustments; escalation; no unauthorised decisions), each with a one-line "what good looks like."
- **`nmc-standard.md`** — the specific NMC Code / Standards of Proficiency / SSSA / PAD / Equality Act anchors relevant to that loop.
- **`audit-template.md`** — the structured audit-log entry the skill fills in.

## 11. Audit log format

Written to `./practice-loop-audit/2026-06-29-placement-support.md`:
```
# Practice Loop run — placement-support
- Timestamp: 2026-06-29T14:03Z
- Operator: <name/role>
- Loop & version: placement-support v0.1.0
- Input provenance: anonymised? [yes/no] · IG reference: <if any>
- Boundaries declared: <what AI must not decide>

## Verification scores
| Round | Concern | Evid/Opin | Conduct/Cap | SMART | Review date | Owners | Tone | Adjustments | Escalation | No unauth. | Min |
|-------|---------|-----------|-------------|-------|-------------|--------|------|-------------|-----------|-----------|-----|
| 1 | 7 | 6 | 8 | 6 | 5 | 7 | 9 | 8 | 9 | 10 | 5 |
| 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 10 | 9 |

## Escalations / flags
- <none | description + recommended human action>

## Status
DRAFT — pending human sign-off by: ____________________   Date: __________
```

## 12. Red lines & data-safety gate (enforced in every skill)

- Never decide: pass/fail or fitness to practise; diagnosis or clinical treatment; mental capacity; final safeguarding or disciplinary outcomes; HR/employment outcomes.
- Never process identifiable patient/staff data without IG approval — **halt and ask** if detected.
- Always output a DRAFT for human sign-off; never finalise.

## 13. Flagship — Placement Support loop

- **Task:** From anonymised placement meeting notes, draft a SMART action plan separating **learning needs** from **conduct concerns**; include student voice; map to PAD requirements and NMC professional values.
- **Boundaries:** must not decide progression/pass-fail, fitness to practise, capability, or employment.
- **Standard (`nmc-standard.md`):** NMC Standards of Proficiency; SSSA; PAD; Equality Act reasonable adjustments; supportive/non-punitive language.
- **Output:** action-plan table (Concern | Type | SMART action | Owner | Review date) + Reviewer notes + DRAFT sign-off block + audit log.
- **Examples:** `examples/placement-support.input.md` (anonymised) and the resulting `examples/placement-support.audit.sample.md`.

## 14. The other five loops (to replicate)

Same protocol; differences are Task, Boundaries, Standard, and the verifier emphasis:
- **Preceptorship** — 3-month review prep; confidence map + evidence gaps; strengths-based.
- **Clinical supervision** — themes + reflective prompts + agreed actions; restorative tone; wellbeing/risk flags.
- **EDI intelligence** — representation/progression gaps from aggregate metrics; rate-based fair comparison; no individual attribution; small-number disclosure check.
- **Teaching** — session plan + knowledge checks + inclusive adjustments; mapped to NMC proficiencies; "verify clinical content locally" flag.
- **Action tracking** — decisions/owners/deadlines/risks from a transcript; risks flagged for human grading, not graded by AI.

## 15. Testing & validation

- `claude plugin validate` passes on the plugin.
- Manual load via `claude --plugin-dir ./plugins/practice-loops`; invoke `/practice-loops:placement-support` on `examples/placement-support.input.md`.
- Confirm: scores printed; sub-8 triggers a revision; an injected safeguarding cue triggers escalation; an injected identifiable-data line triggers the halt; an audit file is written; output is labelled DRAFT.
- `/reload-plugins` workflow documented in README for contributors.

## 16. Licensing & governance

- **Apache-2.0** `LICENSE`; copyright held by the CIC (per the NCD/CQAI entity structure). NOTICE attribution to CQAI / Lincoln Gombedza.
- README carries a **clinical-safety note**: anonymised inputs only; outputs are drafts pending professional sign-off; not a medical device; not for the red-line decisions.
- Large source PDFs: keep the repo lean — either move the two source decks out of the published repo or store under `docs/` and exclude from release; decide before first push.

## 17. Rollout / milestones

1. Scaffold repo: manifests, LICENSE, README, .gitignore, git init.
2. Build `practice-loop-method` skill.
3. Build `placement-support` skill + references + examples.
4. Validate + manual test (the §15 checks).
5. Replicate the five remaining loops.
6. Final validate, polish README, then (on user's go-ahead) push to the CQAI org and optionally submit to the community marketplace.

## 18. Open questions / risks

- **Audit integrity:** the audit log is model-written, so it records what Claude did, not an independent check. Acceptable for v0.1 given the skills decision; a future engine could enforce it. Documented as a known limitation.
- **Publishing the source PDFs/decks** in a public repo (size + whether they should be public). Default: exclude from the published repo.
- **Marketplace name** (`cqai-practice-loops`) and whether to also list it in `nhs-preceptorship-transparency` or a central CQAI marketplace repo.

## 19. References

- Master guide, playbook, templates (this folder).
- Claude Code plugins: code.claude.com/docs/en/plugins ; plugin-marketplaces ; skills.
- Loop engineering: addyosmani.com/blog/loop-engineering.
