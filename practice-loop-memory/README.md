# Practice Loop Memory (`practice-loop-memory/`)

Persistent, cross-session memory for Practice Loop runs: stateless model reasoning over a
persistent state layer held on the nurse's own disk.

## Purpose

Each Practice Loop run is otherwise isolated. This memory layer lets a loop recall a learner's development trajectory across sessions — for example, a Month 3 placement review can reference Month 1 learning gaps without the nurse re-pasting old notes.

## How It Works

Memory is a **read/write pair**, and both halves are required. A loop that wrote a trajectory
without ever reading it back would accumulate a record nobody benefits from — so
`scripts/check_guardrails.py` fails the build if a loop implements one half without the other.

- Memory is **opt-in**: a record is only created or read when the nurse supplies a **pseudonym** at intake (never a real name, initials, or staff number). No pseudonym means the loop runs statelessly.
- Each subject gets one JSON file: `<pseudonym>.json` (e.g. `student-alpha.json`), following the schema in [`schema.json`](schema.json).
- **Read — step 1.5, `on_intake`:** before any reasoning, the loop reads the file and surfaces open learning gaps (with first-recorded dates), prior flags, the score trend, and any `assessor_preferences`. Recalled content is treated as **prior context to be confirmed, not established fact** — the nurse may know it is out of date. A gap that recurs across sessions is flagged as a *pattern to escalate*, not an action to repeat.
- **Write — step 10, `on_commit`:** the loop appends a trajectory entry recording proficiencies mapped, verifier scores, flags, learning gaps, and strengths from the session.
- Reads and writes are **programmatic, never agent-triggered**: a loop must not decide for itself whether to consult its own history. See the boundary table in the `practice-loop-method` skill.

## Where this sits in the agent-loop levels

Using the three-level framing from Oracle's [The Agent Loop Decoded](https://blogs.oracle.com/developers/the-agent-loop-decoded-three-levels-every-agent-engineer-must-know), which these loops draw on:

- **Level 2 — implemented.** Memory is read before the model reasons and written after it acts, and the loop actively manages that state rather than having memory happen to it.
- **Level 3 — partially implemented.** The deliberate programmatic vs agent-triggered boundary and dynamic context curation are in place. Conversation compaction, tool-output offloading, and context-window monitoring are **not** — Practice Loops are short, single-purpose runs where those pressures do not yet arise.

Deliberately **not** adopted: vector stores, embeddings, and a database-backed memory engine. Loops are Markdown skills over stdlib-only Python with no dependencies, which is what makes them reviewable by a clinical governance team and deployable inside an NHS trust. Keyword-matched JSON on local disk is sufficient.

## Cross-session records carry a data-protection duty

Single-session drafting and longitudinal tracking of a named individual are different propositions under UK GDPR, even pseudonymised. Before enabling memory for real learners, a trust or university should assess it as processing of personal data: a pseudonym plus a placement trajectory can be re-identifying in a small cohort. Treat the pseudonym as a key, not as anonymisation.

## Privacy Rules

> 🔒 **Non-Negotiable**: Memory files MUST NOT store patient or staff identifiable data.
>
> - No real names, DOB, NHS numbers, or addresses.
> - Use only the pseudonym provided by the nurse (e.g. "student-alpha", "preceptee-B").
> - Memory JSON files are excluded from GitHub via `.gitignore` — they exist locally only, like audit logs.

## File Convention

```
practice-loop-memory/
├── README.md          ← This file (committed to Git)
├── schema.json        ← JSON Schema definition (committed to Git)
├── .gitkeep           ← Ensures directory is tracked (committed to Git)
├── student-alpha.json ← Learner memory record (LOCAL ONLY, .gitignored)
└── preceptee-B.json   ← Learner memory record (LOCAL ONLY, .gitignored)
```

## Schema Overview

Each memory file contains:

| Field | Description |
|---|---|
| `learner_pseudonym` | The pseudonym hash (matches the filename) |
| `programme_year` | 1, 2, or 3 (NMC programme year) |
| `trajectory[]` | Array of session entries, each recording date, loop type, proficiencies mapped, scores, flags, learning gaps, and strengths |
| `assessor_preferences` | Optional trust-specific preferences (trust name, custom verifier notes, preferred phrasing) |

See [`schema.json`](schema.json) for the full JSON Schema definition.
