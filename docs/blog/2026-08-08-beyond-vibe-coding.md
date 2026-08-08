---
title: "Beyond Vibe Coding"
subtitle: "Building clinical AI that knows when to stop — six pillars, two human gates, and what happened when we audited our own claims"
author: "Lincoln Gombedza · Clinical Quality Artificial Intelligence (CQAI)"
date: "8 August 2026"
lang: en-GB
---

Walk into a nursing lab, a placement study room, or a ward breakroom and you will find something that no digital strategy document has caught up with yet. Students are using AI to untangle placement feedback. Preceptors are using it to structure three-month reviews. Newly qualified nurses are using it to decode trust policies and draft SMART action plans at eleven at night.

This is not a pilot. It is not waiting for approval. It is happening now, on personal phones, in personal accounts, with no audit trail and no one to ask.

The question is no longer whether nurses will use AI. It is whether the way they use it can survive contact with professional accountability.

## First, some credit where it is due

"Vibe coding" — building by conversation, iterating by feel, shipping without a computer science degree — did something the NHS digital programme never managed. It put the means of building software into the hands of the people who actually understand the work.

I am a nurse. I build tools. I could not have done that ten years ago. The barrier was never clinical insight; it was the cost of turning insight into working software. Vibe coding collapsed that cost, and the profession should be honest about how much it gained.

So this is not an argument that exploratory prompting is bad. It is an argument that it is **the wrong instrument for one specific class of work** — and that class happens to include most of what nursing documentation actually is.

## The failure mode that matters

In software, a bad vibe-coded output usually announces itself. The build breaks. The test goes red. Something obviously does not work.

Clinical documentation has no build step. A bad output looks exactly like a good one.

We call this **quiet failure**: fluent, confident, professional-sounding text that is factually wrong, or subtly unfair, or silently missing the thing that mattered most. A placement action plan that reads beautifully and never mentions the escalation concern. A supervision summary that captures the themes and loses the safeguarding flag. A support plan written in deficit language that will follow a student through their programme.

Nobody notices. That is the entire problem. A crash is loud; quiet failure is a plausible paragraph.

You cannot prompt your way out of this. Better wording produces better-sounding output, which is the same failure with more polish. What you need is something structurally different: a workflow that checks itself against a standard you defined in advance, and that stops.

## From prompting to practising

A **Practice Loop** is a repeatable, AI-supported workflow with a job, a standard, a stopping rule, and a memory. It runs six pillars in order and never skips one:

**Trigger → Task → Standard → Verification → Iteration → Human sign-off**

The pillars matter less than what they force you to do. Naming the **task** means naming what the AI must *not* decide. Naming the **standard** means committing to a benchmark — the NMC Code, a proficiency, the Equality Act — before you see the output and start rationalising. **Verification** means the draft is scored against that standard, out of ten, with each score printed. **Iteration** means anything below eight gets rewritten *before a human ever reads it*.

This maps onto something nurses already know cold: assess, diagnose, plan, implement, evaluate. Practice Loops did not invent a workflow. It borrowed the one the profession has used since Orlando formalised it in 1961, and pointed it at a language model.

## The two places a loop must stop

Most "human-in-the-loop" design is a signature box at the end. That is not oversight; it is a receipt.

The reason it fails is well documented in clinical informatics: show a clinician a finished, confident output and ask them to approve it, and automation bias does the rest. Reviewing a polished plan is a fundamentally easier cognitive task than forming a judgement — so the brain takes the easier one.

The research on clinical reasoning points to where the intervention actually belongs. The critical cognitive step is not producing the plan; it is the move from raw assessment data to identifying the problem. Get the problem wrong and everything downstream is coherent, well-structured, and wrong. Errors at diagnosis cascade.

So a Practice Loop stops **twice**.

**Gate 1** comes before anything is drafted. The loop presents its reasoning: what it thinks the concerns are, how it has categorised each one, which proficiencies it mapped and why, and — critically — what it is treating as fact versus inference. Then it stops and waits. Not rhetorically. It does not proceed.

For a placement loop, the sharpest example is the split between a **learning need** and a **conduct concern**. That single categorisation changes the entire plan, the tone, the route, and what it means for the student. It is a registrant's judgement. A language model must not make it quietly on the way to producing something that looks finished.

**Gate 2** is the familiar one: the output is marked DRAFT, the accountable role is named, assumptions and gaps are listed explicitly, and a registrant signs. Nothing leaves the loop as final.

## What happened when we audited our own claims

Here is the part that is uncomfortable to publish, and the reason I am publishing it.

Practice Loops is open source. The README described the dual-gate architecture. The framework documents specified it as a normative requirement — the skill *"MUST present candidate nursing diagnoses to the user and prompt for confirmation before proceeding to action planning."* The eval suite asserted it: *"on_gate1 pauses for nurse validation."*

Then we audited the code against the documentation.

**Gate 1 did not exist.** The word "Gate" appeared in none of the eleven loop definitions. Every loop went from loading the standard straight to drafting. Gate 2 — the signature at the end — was real. The gate that actually protects against automation bias was documentation only.

It was not the only gap. The cross-session memory feature, advertised as letting a Month 3 review recall Month 1 learning gaps, was **write-only**: every loop appended to the record and nothing ever read it back. And the write itself was unreachable, because it was conditioned on a pseudonym that no step ever asked the user for.

Three capabilities, all documented, none working. Nobody had lied. The docs described an intention, the intention was real, and nothing in the pipeline ever compared the two.

That is the actual lesson, and it generalises well beyond us: **a governance framework that cannot detect its own drift is a governance document, not a governance system.**

So the fix was not only to implement the three things. It was to make the build fail without them. The static checker now verifies each safety clause *inside the section that must carry it*, requires the Gate 1 section to contain an actual stop instruction rather than a description of one, and enforces read/write symmetry on memory so a loop cannot write a record it never reads.

We tested that enforcement the only way that means anything: by running it against the old code. It rejects all eleven loops, naming each defect separately. A check that only ever passes tells you nothing.

## Being precise about what this is

There is a useful three-level framing for agent loops, set out in Oracle's *The Agent Loop Decoded*. Level 1 is a model with tools and no memory beyond the context window. Level 2 reads memory before it reasons and writes after it acts. Level 3 adds a deliberate boundary between what the harness does automatically and what the model gets to decide, plus context compaction and offloading.

We had been describing Practice Loops as Level 3. Measured honestly, it is **Level 2 implemented in full, with parts of Level 3** — the programmatic/agent-triggered boundary and context curation are there; compaction and tool-output offloading are not, because these are short single-purpose runs that do not yet need them.

That correction matters more than it sounds. The boundary between automatic and discretionary operations is a **safety** property in clinical work, not an efficiency one. A loop that could choose to skip reading its own escalation history is not a governed loop. So those operations run whether the model judges them necessary or not, and only genuinely discretionary steps — expanding a recalled entry, escalating a concern — are left to it.

One deliberate omission: no vector database, no embeddings, no memory engine. Keyword-matched JSON on local disk, zero dependencies. That is not technical modesty. It is what makes the whole thing reviewable by a clinical governance team and deployable inside a trust, which is the only deployment that counts.

## What is still open

Cross-session memory is opt-in, and it should stay off until a Data Protection Impact Assessment is signed. A pseudonym plus a dated placement trajectory is re-identifying in a cohort of four students on one ward — the pseudonym is a key, not anonymisation. We have published the DPIA template with the risks stated at full strength, including two we only found by reading the code: adjustments data reaching a schema with no special-category handling, and memory files syncing to a personal cloud account because `.gitignore` governs git and nothing else.

Every loop runs fully without memory. Statelessly is the correct default until that assessment is done.

## The point

Nurses are the largest workforce in health care, and they are already using these tools. The choice is not adoption or abstinence. It is whether what they use has a standard, a stopping rule, and an audit trail — or whether it just sounds right.

Vibe coding got nurses through the door as builders. It should be celebrated for that and then, for this class of work, set down. What replaces it is not more sophisticated prompting. It is loops that verify themselves against standards you committed to in advance, stop at the two points where a registrant's judgement is genuinely required, and leave a trail you would be content to hand a regulator.

**AI supports the workflow. The registered professional owns the judgement.**

---

Practice Loops is open source and free for non-commercial use by NHS trusts, universities, educators and students under the PolyForm Noncommercial 1.0.0 licence.

**Repository:** <https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops>

Practice Loops™ is a trademark of Lincoln Gombedza / Clinical Quality Artificial Intelligence (CQAI). The framework draws on the ADPIE nursing process (Orlando, 1961; Yura & Walsh, 1967), work on clinical reasoning and automation bias (Benner, 2001; Pesut & Herman, 1999; Sittig & Hardiker, 2020), and the agent-loop levels described in Oracle's *The Agent Loop Decoded* (Alake, 2026).
