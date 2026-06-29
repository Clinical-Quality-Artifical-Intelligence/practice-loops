# Practice Loops for Nursing — The Playbook

**Moving from prompting to practice architecture: how nurses can build safe, structured, governed AI workflows.**

*A framework by Lincoln Gombedza · Nursing Citizen Development (NCD)*
*Synthesised from the "Loop Engineering" movement (Boris Cherny / Anthropic, Addy Osmani) and the NCD "Practice Loops" decks.*

---

## 0. The one-sentence version

> Stop writing better prompts. Start designing **loops** — repeatable, AI-supported workflows built around a professional standard, a verification gate, a stop condition, and a human sign-off.

In software, the people who built the tools stopped prompting. As Boris Cherny (Head of Claude Code, Anthropic) put it: *"I don't prompt Claude anymore. I have loops running that prompt Claude... my job is to write loops."* Addy Osmani calls this **loop engineering**: *"You design the system that does it, instead of doing it yourself."*

This playbook translates that idea into nursing **without** pretending AI understands clinical accountability. The professional always owns the judgement. The AI only ever supports the workflow.

---

## 1. The problem with prompting

Most nurses use AI in the slowest way possible — **you are the engine, the AI is just the tool**:

```
Type request → Wait for answer → Read output → Fix it → Ask again → Repeat
```

This *ceiling of inefficiency* is fine for one-off questions. It **breaks down** when the work is:

- **Repeated** (every student, every month, every handover)
- **Structured** (it always follows the same shape)
- **Quality-dependent** (it must meet a standard — NMC Code, SMART actions, safeguarding cues)

Examples where it breaks: student placement concerns, supervision notes, preceptorship reviews, teaching materials, EDI briefings.

---

## 2. The paradigm shift: prompt vs. practice loop

| | **The Prompt** | **The Practice Loop** |
|---|---|---|
| **What it is** | A single instruction: *"Do this."* | A repeated workflow: *"Work toward this goal, check it against the standard, improve it, and stop."* |
| **Example** | "Write a student action plan from these notes." | "Write a student action plan. Check it against: clear concern, SMART actions, NMC values, escalation route. Score it /10. If below 8, revise. Stop after 3 rounds and flag for human review." |
| **Outcome** | AI guesses the required standard and stops after one attempt. | AI knows *what* to produce, *how* to check it, *when* to improve it, and *when* to escalate. |

### Loops are not alien to nursing
You already run loops every day. The generic AI loop maps directly onto the nursing process:

| AI loop | Nursing equivalent |
|---|---|
| Discover | **Assess** |
| Plan | **Plan** |
| Execute | **Intervene** |
| Verify | **Evaluate** |
| Iterate | **Adjust** |

Care planning, clinical audit, quality improvement (PDSA), and governance are *already* loops. AI can now help run parts of that cycle — under your sign-off.

---

## 3. The three levels of AI maturity in nursing

| Level | Input | Action | Human role |
|---|---|---|---|
| **1 — AI as Assistant** | A single question ("Summarise this policy") | One-off answer | Reads and manually edits |
| **2 — Structured Helper** | A task *with criteria* ("Summarise policy, flag governance actions") | Follows instructions with better constraints | Checks against local standards |
| **3 — Practice Loop** | A defined goal, trigger, standard, and stopping rule | Runs (semi-)autonomously until output meets the threshold or needs escalation | **Reviews the final output and holds professional accountability** |

The breakthrough is moving from a one-off assistant to a **structured workflow partner** — without ever surrendering the decision.

---

## 4. The anatomy of a Practice Loop

A Practice Loop has **six stages**, grouped into Setup → Engine → Shield:

```
THE SETUP            THE ENGINE                          THE SHIELD
1. Trigger  →  2. Task  →  3. Standard ⇄ 4. Verification ⇄ 5. Iteration  →  6. Human Sign-Off
```

### Stage 1 — Trigger (what starts the workflow)
**Rule: start manual. Keep the nurse in control. Automated triggers come later.**
Examples: pasting meeting notes, uploading a transcript, a calendar event, a monthly metrics drop.

### Stage 2 — Task (what specific work needs doing)
Eliminate assumptions. A weak task lets AI fill gaps with guesses.

- ❌ **Weak:** "Help with this student."
- ✅ **Strong:** "Review the placement notes. Draft a SMART action plan separating *learning needs* from *conduct concerns*. **Do not make employment or capability decisions.**"

**Task checklist:** ✓ output required & intended audience · ✓ boundaries · ✓ what AI **must not** decide.

### Stage 3 — Standard (what "good" looks like)
**Without a standard, AI simply agrees with itself. "Sounds professional" is not a standard.**
Check output against concrete references:

- NMC **Code** and NMC **Standards of Proficiency**
- Clinical supervision principles
- Safeguarding thresholds
- Equality Act 2010 considerations
- Trauma-informed, supportive, non-punitive language
- SMART criteria and "reasonable adjustments"

The standard is what turns AI from a *writing* tool into a *structured support* tool.

### Stage 4 — Verification (the gate that checks the output)
> Without verification, a loop is just **repetition**. With verification, a loop becomes **improvement**.

Best practice from loop engineering: the **verifier should be separate from the maker** — don't let the AI grade its own homework. Score the draft against this **10-point verifier**:

| Verification question | Why it matters |
|---|---|
| Is the concern clearly described? | Prevents vague or unfair documentation |
| Is evidence separated from opinion? | Supports fairness and auditability |
| Are actions SMART? | Makes support measurable and actionable |
| Is risk explicitly addressed? | Protects patient and staff safety |
| Is the review date clear? | Prevents "drift" in support/clinical plans |
| Are responsibilities named? | Improves accountability — who does what |
| Is language supportive and non-punitive? | Maintains psychologically safe learning |
| Are reasonable adjustments considered? | Equality Act / EDI compliance |
| Is escalation required? | Stops risks being hidden in summaries |
| Does it avoid unauthorised decisions? | Protects the accountability boundary |

**The quick five-question check for everyday use** — the two nursing-specific ones nobody else thinks to add:

- **Evidence vs. opinion** — is fact clearly separated from interpretation?
- **Conduct vs. capability** — are behavioural issues distinguished from performance issues?
- **Equity and bias** — non-punitive language and reasonable adjustments included?
- **SMART actions** — Specific, Measurable, Achievable, Relevant, Timely?
- **Escalation flags** — specific safeguarding / clinical-safety risks surfaced for a human?

**Fails the filter →** loop back to iteration. **Passes →** safe for human review.

**The scoring rule:** the AI scores each criterion out of 10. **If anything scores below 8/10 it must self-correct the weak section before you ever see it** — so your attention is spent only on pre-verified material.

### Stage 5 — Iteration (self-correction)
The loop scores the output, exposes its reasoning, and fixes the weakest part **before** showing it to you.

> "The action plan scores 6/10 because two actions are vague. I will revise them into SMART actions with named responsibilities and review dates." → 8/10

This is fundamentally different from a human typing "make it better." The loop identifies *what* is weak and *why*, and makes the reasoning visible.

### Stage 6 — Human Sign-Off (the anchor of accountability)
**AI can draft, summarise, check, flag, organise, and prepare. It must NEVER hold professional accountability.**

| What **AI CAN** do (the Engine) | What **humans MUST** do (the Decider) |
|---|---|
| Draft · Summarise · Check · Flag · Organise · Prepare | **Review · Sign-off · Decide** |

**Mandatory human sign-off triggers** — failure to obtain sign-off here is a critical breach of professional responsibility:

- Patient care, clinical treatment, and risk decisions
- Safeguarding thresholds
- Fitness to practise / student progression
- Conduct, capability, and HR processes
- Occupational health, health & disability, reasonable adjustments
- **Any decision that materially affects a person**

---

## 5. The diagnostic matrix: build vs. avoid

> Not everything needs a loop. Knowing what **not** to automate is professional discipline, not anti-AI.

### ✅ BUILD (manageable risk) — when *all* are true:
- The task happens repeatedly **and** follows a recognisable structure
- A clear standard exists and the output **can be checked**
- It saves time, reduces missed actions, improves auditability
- It **does NOT remove necessary human judgement**

### ⛔ AVOID — the clinical red lines. Do **not** use loops to:
- Decide whether a student **passes or fails**, or their fitness to practise
- Diagnose a patient or decide **clinical treatment**
- Determine **capacity**
- Make final **safeguarding** or **disciplinary** decisions
- Process **identifiable patient data** without governance (DPIA / IG approval)

> The safest developers are the ones who know exactly what should **not** be automated.

### Stop conditions — when the loop must halt and escalate
Every loop needs an explicit stop condition. Beyond "passed verification" or "hit the retry limit," the AI must **stop and hand to a human immediately** when it detects:

- **Conflict or bias** — discriminatory language or conflicting data points
- **Messy input** — insufficient or garbled information that prevents a safe output
- **Risk flags** — safeguarding concerns or urgent clinical risks
- **Complex judgement** — professional uncertainty or nuanced ethical weighing

---

## 6. The hidden risks: quiet failures

Obvious failures are easy to spot. **Quiet failures look polished but are dangerous:**

- Confident but inaccurate summaries
- Missing safeguarding cues
- Vague risk statements
- Action plans that *sound* supportive but aren't measurable

**The goal is not AI activity — it is accountable improvement.** Value is not "outputs generated"; it is:

- Outputs **accepted after human review**
- **Safer handovers** and audit readiness
- A measurable **reduction in missed actions**

### The real cost
Loops consume tokens, compute, time, attention, review effort, and maintenance. **A loop that produces poor outputs creates hidden work.** Track real success indicators: reduction in missed actions · better audit readiness · improved SMART action completion · clearer escalation · safer handover.

---

## 7. The Practice Loop Canvas

Your blueprint for translating AI use into safe design thinking. Fill this in *before* you build:

| Field | Question |
|---|---|
| **Problem** | What repeated friction or administrative burden does this solve? |
| **Users** | Which professional roles are responsible for the loop? |
| **Trigger** | What starts the loop (manual or automated)? |
| **Input** | What specific data (transcripts, notes, reports) does it need? |
| **Task** | What specific output must the AI produce? |
| **Standard** | What professional benchmark (NMC Code, Trust policy) does it check against? |
| **Verification** | What 10-point scoring questions judge quality (8/10 threshold)? |
| **Stop condition** | What criteria force immediate escalation to a human? |
| **Escalation** | What is the designated route for human review when risks are flagged? |
| **Human sign-off** | Which named role is accountable for the final output? |
| **Risk & equity** | Bias risks? Data-protection requirements? |
| **Success measure** | What metric proves value (time saved, SMART completion, missed actions reduced)? |

> **Build order rule:** always start with one **manual** example before automating. A weak manual process becomes a dangerous automated process.

---

## 8. Where Practice Loops shine

| Use case | Input → Loop → Output |
|---|---|
| **Placement support** | Meeting notes → extracts SMART actions, maps to NMC values → draft action plan for educator review |
| **Preceptorship** | Progress logs → maps clinical confidence, identifies evidence gaps → 3-month review prep |
| **Clinical supervision** | Rough notes → extracts themes, generates reflective prompts → structured follow-up record |
| **EDI intelligence** | Monthly workforce metrics → identifies representation/progression gaps → equity-focused briefing |
| **Teaching** | Topic → drafts session plan, knowledge checks, inclusive adjustments → educator-adapted resource |
| **Action tracking** | Meeting transcript → extracts decisions, owners, deadlines, risks → governance-ready checklist |
| **Policy translation** | National report → summarises and flags local governance actions → action list for sign-off |

---

## 9. The mindset shift: from prompter to architect

| The Prompter | The Architect (Nursing Citizen Developer) |
|---|---|
| Focuses on the **tool** | Focuses on the **workflow** |
| Asks "How do I write a better prompt?" | Sees the pain point, understands the standard, maps escalation routes |
| Goal: generate a quick answer | Asks "What workflow am I improving? Where does professional judgement sit?" |
| | Goal: design **safer, fairer** digital practice systems |

This is **not** about nurses becoming software engineers. It is about nurses becoming **designers of intelligent practice systems** — finding the repeated task, defining the NMC standard, and locating exactly where human review must happen.

---

## 10. The safe build order: how to start

Develop every loop in this governed 7-step sequence — never jump straight to automation:

```
1. Manual testing       → Run it manually with ONE real, anonymised example. Does it help?
2. Reusable prompt      → Formalise the instructions into a repeatable structure.
3. Verification checklist→ Bake the standards (NMC, trust policy) in as checking rules.
4. Define stop conditions→ Explicitly list when the AI must escalate to a human.
5. Stress testing       → Test with messy data, high-risk scenarios, and conflict.
6. MDT review           → Socialise with PEFs, EDI leads, and IG colleagues.
7. Governed automation  → Add automated triggers ONLY after the manual loop is proven safe.
```

> Technology teams build platforms, but nurses understand practice. Practice Loops give nurses a way to **translate their expertise into AI-supported workflows** — without pretending AI understands healthcare accountability on its own.

---

## Appendix A — Glossary (loop engineering → nursing)

| Loop-engineering term | What it means in a Practice Loop |
|---|---|
| **Goal / `/goal`** | The defined outcome that "done" looks like (e.g. a sign-off-ready action plan). |
| **Memory / State** | Durable record kept **on disk** (a markdown log, a tracked spreadsheet, a case record) — the model forgets between runs, so progress must live outside it. |
| **Verifier / sub-agent** | A *separate* checking step that scores the output against the standard — never the same step that wrote it. |
| **Stop condition** | The exit rule: success (passes verification), failure (too many retries / unrecoverable), or budget (time/effort cap). Always set at least one of each. |
| **Cost** | Tokens, time, attention, and review effort. A polished-but-wrong loop creates hidden cost. |
| **Skill** | Reusable project knowledge (your NMC standards, trust policy, templates) so the loop doesn't start from zero each time. |
| **Worktree / isolation** | Keep drafts separate from the record of truth until a human signs off. |

## Appendix B — Governance checklist before you go live

- [ ] No identifiable patient/staff data enters the loop without DPIA / IG approval
- [ ] The standard is written down and references current NMC / trust documents
- [ ] Verification questions are explicit and check safety, SMART, equity, and boundaries
- [ ] A stop condition and an escalation route are defined
- [ ] A named human reviews and signs off every output that affects a person
- [ ] An equity check has been done (could this amplify bias?)
- [ ] The input, output, and decision can be traced (audit)
- [ ] You started with a manual example before automating

**Three final governance questions to document before any institutional rollout:**

1. **Data sovereignty** — is the tool approved for the level of data being used (anonymised vs. identifiable)?
2. **Equity** — does the loop account for reasonable adjustments and avoid amplifying bias?
3. **Auditability** — is there a clear trace of input, verification steps, and human sign-off?

---

*Sources: zodchiii "LOOPS — Everything you need to know" (Claude/ChatGPT/Mira); Addy Osmani, "Loop Engineering" (addyosmani.com/blog/loop-engineering); Claude Code agent-loop documentation; NCD decks "Practice Loops for Nursing Citizen Developers" and "Designing Safe AI Workflows in Nursing." Framework adaptation: Lincoln Gombedza, Nursing Citizen Development.*
