# Practice Loop Memory (`practice-loop-memory/`)

This directory stores **local, non-identifiable stateful memory** across Practice Loop runs, aligning with **Level 2/3 Agent Memory Architectures** (stateless LLM reasoning + persistent state harness).

## Memory Structure

- `cohort-trajectories.json`: Stores anonymised development trajectories over time (e.g. Month 1 vs Month 3 proficiency progress).
- `assessor-preferences.json`: Stores local trust/unit preferences, custom verifier rules, and institutional phrasing standards.

> 🔒 **Privacy Rule**: Memory files MUST NOT store patient or staff identifiable data (names, DOB, NHS numbers). Use anonymised hashes or pseudonyms only.
