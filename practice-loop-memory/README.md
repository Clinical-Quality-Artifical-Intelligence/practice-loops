# Practice Loop Memory (`practice-loop-memory/`)

Persistent, cross-session memory for Practice Loop runs — implementing **Level 3 Agent Memory Architecture** (stateless LLM reasoning + persistent state harness).

## Purpose

Each Practice Loop run is normally isolated. This memory layer allows loops to recall a learner's development trajectory across sessions — for example, a Month 3 placement review can reference Month 1 learning gaps without the nurse re-pasting old notes.

## How It Works

- Memory is **opt-in**: a memory record is only created/updated when the nurse provides a **learner pseudonym** (never a real name).
- Each learner gets a single JSON file: `<pseudonym>.json` (e.g. `student-alpha.json`).
- The file follows the schema defined in [`schema.json`](schema.json).
- At the `on_commit` lifecycle phase, the loop appends a trajectory entry recording proficiency scores, flags, learning gaps, and strengths from the session.

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
