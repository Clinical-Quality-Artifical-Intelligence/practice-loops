# Practice Loops Plugin — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `practice-loops` Claude Code plugin — one skill per nursing Practice Loop — flagship-first (shared method skill + Placement Support), then replicate the other five loops.

**Architecture:** A Claude Code plugin + marketplace. Each loop is a `skills/<loop>/SKILL.md` that enforces the 6-pillar protocol (intake with identifiable-data halt → task+boundaries → NMC standard → draft → visible 10-point verification → iterate to ≥8/10 → stop/escalate → DRAFT human sign-off → audit log to `./practice-loop-audit/`). A `scripts/validate.py` harness is the automated test that all manifests parse and every skill is well-formed.

**Tech Stack:** Markdown (SKILL.md), JSON manifests, Python 3 (validator only). No runtime dependencies. Reference spec: `docs/superpowers/specs/2026-06-29-practice-loops-plugin-design.md`.

**Working dir:** repo root is `/Volumes/Backup/practice loops/` (git already initialised, `main`, spec committed). Do NOT push to GitHub until the user approves.

---

## Conventions

- Commit after each task with the message shown. Add the trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` to every commit.
- "Run validator" = `python3 scripts/validate.py` from repo root; expected output shown per task.
- Skill namespace is `practice-loops`, so loops invoke as `/practice-loops:<loop>`.
- Plugin lives at `plugins/practice-loops/`.

---

## Task 1: Validation harness (the test) + repo scaffolding

**Files:**
- Create: `scripts/validate.py`
- Create: `plugins/practice-loops/.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`

- [ ] **Step 1: Write the validator (failing test first)**

Create `scripts/validate.py`:

```python
#!/usr/bin/env python3
"""Validate the practice-loops plugin structure. Exit non-zero on any problem."""
import json, sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "practice-loops"
errors = []

def check(cond, msg):
    if not cond: errors.append(msg)

# marketplace.json
mk = ROOT / ".claude-plugin" / "marketplace.json"
check(mk.exists(), "missing .claude-plugin/marketplace.json")
if mk.exists():
    d = json.loads(mk.read_text())
    check("name" in d, "marketplace.json: missing 'name'")
    check(isinstance(d.get("plugins"), list) and d["plugins"], "marketplace.json: 'plugins' must be a non-empty list")

# plugin.json
pj = PLUGIN / ".claude-plugin" / "plugin.json"
check(pj.exists(), "missing plugin.json")
if pj.exists():
    d = json.loads(pj.read_text())
    for f in ("name", "description", "version"):
        check(f in d, f"plugin.json: missing '{f}'")
    check(d.get("name") == "practice-loops", "plugin.json: name must be 'practice-loops'")

# skills: each skills/<x>/SKILL.md must have YAML frontmatter with a description
skills_dir = PLUGIN / "skills"
if skills_dir.exists():
    for sk in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        md = sk / "SKILL.md"
        check(md.exists(), f"{sk.name}: missing SKILL.md")
        if md.exists():
            text = md.read_text()
            m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            check(bool(m), f"{sk.name}: SKILL.md missing YAML frontmatter")
            if m:
                check("description:" in m.group(1), f"{sk.name}: frontmatter missing 'description'")
            # loop skills (not the method skill) must reference the audit log path
            if sk.name != "practice-loop-method":
                check("practice-loop-audit" in text, f"{sk.name}: SKILL.md must write to ./practice-loop-audit/")
                check("DRAFT" in text, f"{sk.name}: SKILL.md must mark output as DRAFT")

EXPECTED = {"practice-loop-method", "placement-support"}
present = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.exists() else set()
missing = EXPECTED - present
check(not missing, f"missing required skills: {sorted(missing)}")

if errors:
    print("VALIDATION FAILED:")
    for e in errors: print("  -", e)
    sys.exit(1)
print(f"OK — {len(present)} skills validated: {sorted(present)}")
```

- [ ] **Step 2: Run validator to confirm it fails**

Run: `python3 scripts/validate.py`
Expected: FAIL — lists missing marketplace.json / plugin.json / required skills.

- [ ] **Step 3: Create `plugins/practice-loops/.claude-plugin/plugin.json`**

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

- [ ] **Step 4: Create `.claude-plugin/marketplace.json`**

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

- [ ] **Step 5: Run validator (still fails on missing skills — expected)**

Run: `python3 scripts/validate.py`
Expected: FAIL — only `missing required skills: ['placement-support', 'practice-loop-method']` remains (manifests now pass).

- [ ] **Step 6: Commit**

```bash
git add scripts/validate.py .claude-plugin/marketplace.json plugins/practice-loops/.claude-plugin/plugin.json
git commit -m "feat: scaffold practice-loops plugin manifests + validator"
```

---

## Task 2: The `practice-loop-method` skill

**Files:**
- Create: `plugins/practice-loops/skills/practice-loop-method/SKILL.md`

- [ ] **Step 1: Create the method skill**

Full content for `SKILL.md` (frontmatter + body). The body is the canonical protocol every loop references.

```markdown
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
3. **Standard** — the NMC Code / Standards of Proficiency / Trust policy / Equality Act anchor.
4. **Verification** — score the draft against the 10-point verifier.
5. **Iteration** — fix anything scoring < 8/10 before a human sees it.
6. **Human sign-off** — a registrant reviews and is accountable; output is always a DRAFT.

Maps to the nursing process: Assess → Plan → Intervene → Evaluate → Adjust.

## The universal loop protocol (every loop skill follows this in order)
1. **Intake / Trigger.** Confirm manual start and ask for the input. **HALT** if the content
   looks like identifiable patient/staff data (names, DOB, NHS number, addresses) unless the
   user confirms it is anonymised / IG-approved.
2. **Task.** Restate the bounded task and the "must NOT decide" boundaries.
3. **Standard.** Load the loop's `references/nmc-standard.md`.
4. **Draft.** Produce the output.
5. **Verify.** Score against the 10 points below, **printing each score /10** and naming weaknesses.
6. **Iterate.** If any point < 8, revise the weakest part, explain the change, re-score. Max 3 rounds.
7. **Stop / escalate.** Halt and flag on: conflict/biased language · messy or insufficient input ·
   safeguarding or urgent clinical risk · anything needing nuanced ethical judgement.
8. **Human sign-off.** Present clearly marked **DRAFT — pending human sign-off**; name the
   accountable role; never present as final.
9. **Audit log.** Append an entry to `./practice-loop-audit/YYYY-MM-DD-<loop>.md` (format below).

## The 10-point verifier
1. Concern clearly described 2. Evidence separated from opinion 3. Conduct distinguished from
capability 4. Actions are SMART 5. Review date clear 6. Responsibilities named 7. Language
supportive & non-punitive 8. Reasonable adjustments considered 9. Escalation surfaced 10. No
unauthorised decisions made.

## The clinical red lines — never use a loop to:
- Decide pass/fail or fitness to practise
- Diagnose a patient or decide clinical treatment
- Determine mental capacity
- Make final safeguarding or disciplinary decisions
- Make HR / employment outcomes
- Process identifiable patient data without IG approval

## Audit log format
Append to `./practice-loop-audit/YYYY-MM-DD-<loop>.md`:

​```
# Practice Loop run — <loop>
- Timestamp: <ISO8601>
- Operator: <name/role>
- Loop & version: <loop> v<plugin version>
- Input provenance: anonymised? [yes/no] · IG reference: <if any>
- Boundaries declared: <what AI must not decide>

## Verification scores
| Round | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Min |
|-------|---|---|---|---|---|---|---|---|---|----|-----|
| 1 | … |

## Escalations / flags
- <none | description + recommended human action>

## Status
DRAFT — pending human sign-off by: ____________________   Date: __________
​```
```

- [ ] **Step 2: Run validator**

Run: `python3 scripts/validate.py`
Expected: FAIL — only `missing required skills: ['placement-support']` remains.

- [ ] **Step 3: Commit**

```bash
git add plugins/practice-loops/skills/practice-loop-method/SKILL.md
git commit -m "feat: add shared practice-loop-method skill"
```

---

## Task 3: Placement Support — reference files

**Files:**
- Create: `plugins/practice-loops/skills/placement-support/references/verifier.md`
- Create: `plugins/practice-loops/skills/placement-support/references/nmc-standard.md`
- Create: `plugins/practice-loops/skills/placement-support/references/audit-template.md`

- [ ] **Step 1: Create `verifier.md`** — the 10 points, each with a one-line "what good looks like" tuned to a student action plan (e.g. "4. SMART — every action has a measure and a deadline; no vague verbs like 'improve'."). Cover: concern clear; evidence vs opinion; conduct vs capability; SMART; review date; named owners; supportive/non-punitive tone; reasonable adjustments; escalation surfaced; no progression/FtP decision.

- [ ] **Step 2: Create `nmc-standard.md`** — the anchors for placement support: NMC Standards of Proficiency for Registered Nurses; NMC SSSA; the student's PAD requirements; student voice; Equality Act 2010 reasonable adjustments; supportive, developmental language.

- [ ] **Step 3: Create `audit-template.md`** — the fillable audit entry from the method skill, with the placement-support column legend.

- [ ] **Step 4: Run validator**

Run: `python3 scripts/validate.py`
Expected: still FAIL on `missing required skills: ['placement-support']` (SKILL.md not yet created) — references alone don't satisfy it.

- [ ] **Step 5: Commit**

```bash
git add plugins/practice-loops/skills/placement-support/references/
git commit -m "feat: add placement-support reference files (verifier, NMC standard, audit template)"
```

---

## Task 4: Placement Support — the loop skill

**Files:**
- Create: `plugins/practice-loops/skills/placement-support/SKILL.md`

- [ ] **Step 1: Create the skill** following the universal protocol, specialised for placement support.

```markdown
---
name: placement-support
description: >
  Run a Practice Loop that turns ANONYMISED placement meeting notes into a DRAFT SMART
  action plan, separating learning needs from conduct concerns, scored against NMC
  standards, with escalation flags and an audit trail. Use for student placement
  support, action plans, or placement concern reviews.
---

# Placement Support loop

Follow the Practice Loop method (see the `practice-loop-method` skill). Execute in order; never skip sign-off.

## 1. Intake
Confirm this is a manual start. Ask the user to paste the placement meeting notes.
**HALT and ask** if the notes contain identifiable data (student/patient name, DOB, NHS
number, location) unless the user confirms they are anonymised / IG-approved.

## 2. Task & boundaries
Draft a SMART action plan that separates **learning needs** from **conduct concerns** in two
labelled sections, includes the student voice, and maps to PAD requirements and NMC values.
You MUST NOT: decide progression or pass/fail; make any fitness-to-practise, capability,
employment, or disciplinary decision; invent facts (mark gaps "to confirm with student/assessor").

## 3. Standard
Read and apply `references/nmc-standard.md`.

## 4. Draft
Produce the action plan: a table (Concern | Type [learning/conduct] | SMART action | Owner |
Review date) + a short student-voice section.

## 5. Verify
Score the draft against all 10 points in `references/verifier.md`. **Print each score /10** and
name what is weak.

## 6. Iterate
If any point scores < 8, revise the weakest part, explain the change, and re-score. Max 3 rounds.

## 7. Stop / escalate
Halt and flag for a human if you detect a safeguarding or patient-safety concern, biased or
punitive framing, conflicting accounts, or notes too thin to support a safe plan.

## 8. Human sign-off
Present the plan clearly marked **DRAFT — pending human sign-off**, name the accountable role
(practice assessor / academic assessor), and add a Reviewer notes section (assumptions, gaps to
confirm). Never present it as final.

## 9. Audit log
Append a completed entry (per `references/audit-template.md`) to
`./practice-loop-audit/<today>-placement-support.md`, including per-round scores and any flags.
```

- [ ] **Step 2: Run validator**

Run: `python3 scripts/validate.py`
Expected: PASS — `OK — 2 skills validated: ['placement-support', 'practice-loop-method']`.

- [ ] **Step 3: Commit**

```bash
git add plugins/practice-loops/skills/placement-support/SKILL.md
git commit -m "feat: add placement-support loop skill (flagship)"
```

---

## Task 5: Example input + sample audit output

**Files:**
- Create: `examples/placement-support.input.md`
- Create: `examples/placement-support.audit.sample.md`

- [ ] **Step 1:** Create `examples/placement-support.input.md` — a realistic, fully **anonymised** set of placement meeting notes (use "the student", "Practice Assessor", no real identifiers) that includes one learning need, one conduct concern, and one subtle wellbeing cue (to exercise escalation).

- [ ] **Step 2:** Create `examples/placement-support.audit.sample.md` — the audit log that a correct run produces from that input (two rounds of scores, an escalation flag for the wellbeing cue, DRAFT status).

- [ ] **Step 3: Commit**

```bash
git add examples/
git commit -m "docs: add anonymised placement-support example + sample audit"
```

---

## Task 6: Manual functional test of the flagship

No code; this is the acceptance test for the skills behaviour. Record results in the PR/commit message.

- [ ] **Step 1: Load the plugin locally**

Run: `claude --plugin-dir "./plugins/practice-loops"` (separate terminal). If `claude` CLI is unavailable in this environment, note it and rely on the validator + manual content review instead.

- [ ] **Step 2: Invoke** `/practice-loops:placement-support` and paste `examples/placement-support.input.md`.

- [ ] **Step 3: Confirm acceptance criteria:**
  - [ ] Verification scores are printed for round 1.
  - [ ] A sub-8 score triggers at least one revision round.
  - [ ] The wellbeing cue triggers an escalation flag.
  - [ ] Adding a line with a fake name triggers the identifiable-data HALT.
  - [ ] Output is labelled DRAFT and names the accountable role.
  - [ ] An audit file appears under `./practice-loop-audit/`.

- [ ] **Step 4: Commit** any wording fixes discovered, message `fix: refine placement-support after manual test`.

---

## Task 7: README, docs tidy, clinical-safety note

**Files:**
- Create: `README.md`, `CONTRIBUTING.md`
- Move: existing `*.md`, `*.docx`, `*.pdf`, infographic, deck into `docs/`
- Modify: `.gitignore` (exclude source PDFs from the published repo per spec §16)

- [ ] **Step 1:** Move the existing framework docs/decks/infographic into `docs/` (keep the spec + plan where they are under `docs/superpowers/`).

- [ ] **Step 2:** Add the two large source PDFs to `.gitignore` (keep them locally under `docs/` but out of the published repo); leave the master guide, playbook, templates, infographic tracked.

- [ ] **Step 3:** Write `README.md`: what a Practice Loop is (1 paragraph), install (`/plugin marketplace add Clinical-Quality-Artifical-Intelligence/practice-loops` then `/plugin install practice-loops`), the loop list, a **clinical-safety note** (anonymised inputs only; outputs are drafts pending professional sign-off; not a medical device; never for the red-line decisions), local dev (`--plugin-dir`, `/reload-plugins`), and the Apache-2.0 + CQAI attribution.

- [ ] **Step 4:** Write `CONTRIBUTING.md`: how to add a new loop (copy `placement-support/`, edit the 3 references + SKILL.md, run `python3 scripts/validate.py`).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "docs: add README, CONTRIBUTING, clinical-safety note; tidy docs/"
```

---

## Task 8: Replicate the remaining five loops

For EACH loop below, repeat Tasks 3–4 (references + SKILL.md) using `placement-support` as the template, then run `python3 scripts/validate.py` (update `EXPECTED` in the validator to include the new skill) and commit `feat: add <loop> loop skill`.

- [ ] **8a. preceptorship** — Task: 3-month review prep; confidence map + evidence gaps; strengths-based. Boundaries: don't sign off preceptorship/competence. Standard: national preceptorship framework + NMC Code. Verifier emphasis: each confidence claim evidenced; gaps actionable; non-leading reflective prompts.
- [ ] **8b. clinical-supervision** — Task: themes + reflective prompts + agreed actions from supervision notes. Boundaries: no performance/conduct/clinical decisions. Standard: restorative supervision principles + NMC professionalism. Verifier emphasis: themes drawn only from notes; restorative tone; wellbeing/risk flagged.
- [ ] **8c. edi-intelligence** — Task: representation/progression gaps from AGGREGATE metrics. Boundaries: no individual attribution; no HR recommendations. Standard: Equality Act + WRES/WDES; rate-based fair comparison. Verifier emphasis: rate-based not raw counts; signals-to-investigate not proven causes; small-number disclosure check.
- [ ] **8d. teaching** — Task: session plan + knowledge checks + inclusive adjustments for a stated level. Boundaries: flag clinical content for local verification. Standard: NMC Standards of Proficiency mapping + UDL. Verifier emphasis: outcomes mapped to proficiency statements; checks aligned; "verify before teaching" flag.
- [ ] **8e. action-tracking** — Task: decisions/owners/deadlines/risks from a transcript. Boundaries: don't invent owners/deadlines; don't grade risk severity. Standard: auditable action-log format. Verifier emphasis: every action traceable; risks separated and flagged for human grading.

- [ ] **Final step:** run `python3 scripts/validate.py` (expects all 7 skills) and commit `feat: complete six practice loops`.

---

## Task 9: Release prep (no push)

- [ ] **Step 1:** Run `python3 scripts/validate.py` → PASS with 7 skills. If `claude plugin validate` is available, run it too.
- [ ] **Step 2:** Confirm `version` in `plugin.json` is `0.1.0`; update README loop list to all six.
- [ ] **Step 3:** Commit `chore: prepare v0.1.0`.
- [ ] **Step 4:** STOP. Surface to the user for approval before any `git remote add` / push to the CQAI org or marketplace submission.

---

## Notes for the implementer
- The deliverables ARE the markdown skills — keep them tight, imperative, and consistent with the framework docs already in `docs/`.
- Do not weaken the red lines or the DRAFT/sign-off requirement in any loop.
- The validator is the regression guard; keep `EXPECTED` in sync as loops are added.
- Reference skills with @ where useful, e.g. the shared method skill.
```
