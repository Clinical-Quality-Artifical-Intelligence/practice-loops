#!/usr/bin/env python3
"""Static guardrail eval: assert every loop skill encodes the non-negotiable safety
clauses. This is the CI-runnable part of the eval suite (no model needed). Behavioural
fixtures that DO need a model live in evals/cases.md.

Exit non-zero if any loop skill is missing a required guardrail."""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "practice-loops" / "skills"
METHOD = "practice-loop-method"

# (label, regex) — each loop SKILL.md must match all of these
REQUIRED = [
    ("identifiable-data HALT", r"(?i)HALT"),
    ("anonymised/IG check",    r"(?i)anonymis|IG[- ]approv|identifiable"),
    ("bounded task / must-not", r"(?i)must not|MUST NOT"),
    ("verification scoring",   r"(?i)score.*out of 10|out of 10|/10"),
    ("8/10 iteration rule",    r"(?i)below 8|< *8|8/10|≥ *8|at least 8"),
    ("stop / escalate",        r"(?i)escalat"),
    ("DRAFT output",           r"DRAFT"),
    ("human sign-off",         r"(?i)sign[- ]?off"),
    ("audit log path",         r"practice-loop-audit"),
]

def main():
    if not SKILLS.exists():
        print("no skills dir"); return 1
    loops = sorted(p for p in SKILLS.iterdir() if p.is_dir() and p.name != METHOD)
    failed = 0
    for loop in loops:
        md = loop / "SKILL.md"
        if not md.exists():
            print(f"FAIL {loop.name}: no SKILL.md"); failed += 1; continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        missing = [label for label, pat in REQUIRED if not re.search(pat, text)]
        if missing:
            print(f"FAIL {loop.name}: missing guardrails -> {missing}"); failed += 1
        else:
            print(f"ok   {loop.name}: all {len(REQUIRED)} guardrails present")
    # method skill must document the red lines
    method = (SKILLS / METHOD / "SKILL.md")
    if method.exists():
        t = method.read_text(encoding="utf-8", errors="ignore")
        if not re.search(r"(?i)red line", t):
            print(f"FAIL {METHOD}: missing the clinical red lines"); failed += 1
        else:
            print(f"ok   {METHOD}: red lines documented")
    if failed:
        print(f"\n{failed} guardrail failure(s)."); return 1
    print(f"\nAll {len(loops)} loop skills pass the guardrail check."); return 0

if __name__ == "__main__":
    sys.exit(main())
