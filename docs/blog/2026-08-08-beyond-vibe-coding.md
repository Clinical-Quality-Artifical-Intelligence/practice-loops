---
title: "Beyond Vibe Coding"
subtitle: "Building clinical AI that knows when to stop — six pillars, two human gates, and an audit trail you could hand a regulator"
author: "Lincoln Gombedza · Clinical Quality Artificial Intelligence (CQAI)"
date: "8 August 2026"
lang: en-GB
---

Walk into a nursing lab, a placement study room, or a ward breakroom and you will find something no digital strategy document has caught up with yet. Students are using AI to untangle placement feedback. Preceptors are using it to structure three-month reviews. Newly qualified nurses are using it to decode trust policies and draft SMART action plans at eleven at night.

This is not a pilot. It is not waiting for approval. It is happening now, on personal phones, in personal accounts, with no audit trail and no one to ask.

The question is no longer whether nurses will use AI. It is whether the way they use it can survive contact with professional accountability.

## First, some credit where it is due

"Vibe coding" — building by conversation, iterating by feel, shipping without a computer science degree — did something the NHS digital programme never managed. It put the means of building software into the hands of the people who actually understand the work.

I am a nurse. I build tools. I could not have done that ten years ago. The barrier was never clinical insight; it was the cost of turning insight into working software. Vibe coding collapsed that cost, and the profession should be honest about how much it gained.

So this is not an argument that exploratory prompting is bad. It is an argument that it is **the wrong instrument for one specific class of work** — and that class happens to include most of what nursing documentation actually is.

## The failure mode that matters

In software, a bad vibe-coded output usually announces itself. The build breaks. The test goes red. Something visibly does not work.

Clinical documentation has no build step. A bad output looks exactly like a good one.

Call this **quiet failure**: fluent, confident, professional-sounding text that is factually wrong, or subtly unfair, or silently missing the thing that mattered most. A placement action plan that reads beautifully and never mentions the escalation concern. A supervision summary that captures the themes and loses the safeguarding flag. A support plan written in deficit language that will follow a student through their programme.

Nobody notices. That is the entire problem. A crash is loud; quiet failure is a plausible paragraph.

You cannot prompt your way out of this. Better wording produces better-sounding output, which is the same failure with more polish. What is needed is something structurally different: a workflow that checks itself against a standard you defined in advance, and that stops.

## From prompting to practising

A **Practice Loop** is a repeatable, AI-supported workflow with a job, a standard, a stopping rule, and a memory. It runs six pillars in order and never skips one:

**Trigger → Task → Standard → Verification → Iteration → Human sign-off**

The pillars matter less than what they force you to do. Naming the **task** means naming what the AI must *not* decide. Naming the **standard** means committing to a benchmark — the NMC Code, a specific proficiency, the Equality Act — *before* you see the output and start rationalising. **Verification** means the draft is scored against that standard, out of ten, with every score printed and the weaknesses named. **Iteration** means anything scoring below eight is rewritten before a human ever reads it.

That last point is the one people underestimate. The professional's attention is the scarcest resource in the system. Spending it on a first draft that a checklist could have caught is a waste of the only thing in the loop that holds registration.

This maps onto something nurses already know cold: assess, diagnose, plan, implement, evaluate. Practice Loops did not invent a workflow. It borrowed the one the profession has used since Orlando formalised it in 1961 and pointed it at a language model.

## The two places a loop must stop

Most "human-in-the-loop" design is a signature box at the end. That is not oversight. That is a receipt.

The reason it fails is well described in clinical informatics: show a clinician a finished, confident output and ask them to approve it, and automation bias does the rest. Reviewing a polished plan is a fundamentally easier cognitive task than forming a judgement, so the brain takes the easier one. The signature gets given. The reasoning never gets examined.

The literature on clinical reasoning tells you where the intervention actually belongs. The critical cognitive step is not producing the plan — it is the move from raw assessment data to identifying the problem. Get the problem wrong and everything downstream is coherent, well-structured, and wrong. Errors at diagnosis cascade; they do not announce themselves either.

So a Practice Loop stops **twice**.

**Gate 1** comes before anything is drafted. The loop presents its reasoning: what it takes the concerns to be, how it has categorised each one, which proficiencies it mapped and why, and — critically — what it is treating as fact versus inference. Then it stops and waits. Not rhetorically. It does not proceed.

Here is why that gate is placed there and not somewhere more convenient. In a placement loop, the sharpest decision in the whole workflow is whether something is a **learning need** or a **conduct concern**. A student who recorded abnormal observations and did not escalate them verbally might have a knowledge gap about escalation thresholds — or might have known and chosen not to. Those are different findings. They produce different plans, different tone, different routes, and mean profoundly different things for that student's progression.

That categorisation is a registrant's judgement. It is exactly the kind of call a language model will make fluently, confidently, and invisibly on its way to producing something that looks finished. So the loop is not permitted to make it. It offers a reading, shows its working, and waits to be corrected.

**Gate 2** is the familiar one, done properly: the output is marked DRAFT, the accountable role is named, and a **Reviewer notes** section lists every assumption made and every gap still to confirm. The registrant signs. Nothing leaves the loop as final.

Both gates are written into the audit entry — not just the signature at the end. An audit trail that records only the final approval cannot evidence that anyone validated the reasoning *before* the plan existed, which is the entire purpose of stopping in the middle.

## Governance has to be enforced, not documented

This is the part that separates a framework from a folder of intentions.

It is easy to write down that a loop must halt on identifiable data, must score itself, must stop for a registrant before drafting. It is much harder to guarantee that the loop still does all of that six months and forty commits later, when someone has restructured it in a hurry.

So the standards are machine-checked, and the build fails without them. Every loop is verified to carry each safety clause **inside the section that must carry it** — a keyword appearing somewhere in the file is not evidence of anything. The Gate 1 section must contain an actual stop instruction, not a description of one. Memory must be symmetrical: a loop that writes a learner's trajectory but never reads it back is caught and rejected, because it accumulates a record nobody benefits from while advertising a benefit it does not deliver.

And the checks are tested by trying to break them. A verifier that only ever passes tells you nothing at all — it is indistinguishable from a verifier that always passes. So each one is run against deliberately broken input to confirm it fails, and fails for the right reason.

The principle generalises well beyond nursing: **a governance framework that cannot detect its own drift is a governance document, not a governance system.** If your safety property is not enforced by something that can say no, it is a preference.

## Being precise about what this is

There is a useful three-level framing for agent loops, set out in Oracle's *The Agent Loop Decoded*. Level 1 is a model with tools and no memory beyond the context window. Level 2 reads memory before it reasons and writes after it acts. Level 3 adds a deliberate boundary between what the harness does automatically and what the model is allowed to decide, plus context compaction and offloading.

Measured against that, Practice Loops is **Level 2 implemented in full, with parts of Level 3**. The programmatic boundary and dynamic context curation are there. Compaction and tool-output offloading are not, because these are short single-purpose runs that do not yet need them.

The boundary is worth dwelling on, because in clinical work it is a **safety** property rather than an efficiency one. Recalling prior history, loading the standard, presenting Gate 1, scoring against the verifier, writing the audit entry — all of these run whether or not the model judges them necessary. Only genuinely discretionary steps are left to it. A loop that could choose to skip reading its own escalation history is not a governed loop.

One deliberate omission: no vector database, no embeddings, no memory engine. Keyword-matched JSON on local disk, zero dependencies. That is not technical modesty. It is what makes the whole thing reviewable by a clinical governance team and deployable inside a trust, which is the only deployment that counts.

## What is still open

Cross-session memory is opt-in, and it should stay switched off until a Data Protection Impact Assessment is signed off locally. A pseudonym plus a dated placement trajectory is re-identifying in a cohort of four students on one ward — the pseudonym is a key, not anonymisation.

So the DPIA template ships with the code, with the risks stated at full strength rather than smoothed over. It records seven high risks, four of which cannot be closed by software at all, because lawful basis, storage location, retention and data subject rights are organisational decisions. Two of those risks are easy to miss: adjustments data, which is special category, reaching the same store as everything else; and memory files quietly syncing to a personal cloud account, because `.gitignore` governs git and nothing else.

Every loop runs fully without memory. Statelessly is the correct default until that assessment is done, and saying so in the documentation is part of the job.

## The point

Nurses are the largest workforce in health care, and they are already using these tools. The choice is not adoption or abstinence. It is whether what they use has a standard, a stopping rule, and an audit trail — or whether it merely sounds right.

Vibe coding got nurses through the door as builders, and it deserves credit for that. For this class of work, it should then be set down. What replaces it is not more sophisticated prompting. It is loops that verify themselves against standards committed to in advance, stop at the two points where a registrant's judgement is genuinely required, and leave a trail you would be content to hand a regulator.

**AI supports the workflow. The registered professional owns the judgement.**

---

Practice Loops is open source and free for non-commercial use by NHS trusts, universities, educators and students under the PolyForm Noncommercial 1.0.0 licence.

**Repository:** <https://github.com/Clinical-Quality-Artifical-Intelligence/practice-loops>

Practice Loops™ is a trademark of Lincoln Gombedza / Clinical Quality Artificial Intelligence (CQAI). The framework draws on the ADPIE nursing process (Orlando, 1961; Yura & Walsh, 1967), work on clinical reasoning and automation bias (Benner, 2001; Pesut & Herman, 1999; Sittig & Hardiker, 2020), and the agent-loop levels described in Oracle's *The Agent Loop Decoded* (Alake, 2026).
