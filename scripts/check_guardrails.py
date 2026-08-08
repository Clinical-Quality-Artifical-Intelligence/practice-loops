#!/usr/bin/env python3
"""Static guardrail eval: assert every loop skill encodes the non-negotiable safety
clauses. This is the CI-runnable part of the eval suite (no model needed). Behavioural
fixtures that DO need a model live in evals/cases.md.

Guardrails are checked *per section*, not against the whole file. A bare
whole-file keyword search passes as long as the word appears anywhere, so a loop
could have its entire HALT clause deleted and still go green on one incidental
use of "halt" in prose. Anchoring each requirement to the section that must
carry it means deleting or gutting that section fails the build.

Exit non-zero if any loop skill is missing a required guardrail."""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "practice-loops" / "skills"
METHOD = "practice-loop-method"

# Section numbers every loop SKILL.md must define, as `## <n>. <title>`.
# 2.5 (proficiency mapping) is intentionally absent: its title varies per loop.
# 10 (memory update) is intentionally absent: it is opt-in per loop.
REQUIRED_SECTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# (section number, label, regex) — the regex must match within THAT section's body.
REQUIRED = [
    ("1", "identifiable-data HALT",    r"(?i)\bhalt\b"),
    # Loops phrase the identifiability gate in domain-appropriate terms: placement
    # loops say "identifiable data / anonymised", edi-intelligence says "could
    # identify an individual / disclosure-safe". Accept any of them, but only
    # within the intake section.
    ("1", "identifiability gate",      r"(?i)anonymis|pseudonymis|IG[- ]approv|identifiab|identif(?:y|ies)|disclosure[- ]safe"),
    ("2", "bounded task / must-not",   r"(?i)must not"),
    ("5", "verification scoring",      r"(?i)out of 10|10[- ]point"),
    ("6", "8/10 iteration rule",       r"(?i)below 8|at least 8|≥\s*8|<\s*8"),
    ("7", "stop / escalate",           r"(?i)escalat|halt"),
    ("8", "DRAFT output",              r"DRAFT"),
    ("8", "human sign-off",            r"(?i)sign[- ]?off"),
    ("9", "audit log path",            r"practice-loop-audit"),
]

HEADING = re.compile(r"^##\s+(.*?)\s*$", re.M)
# "1. Intake" -> "1"; "2.5 Proficiency mapping" -> "2.5"; "10. Memory update" -> "10"
NUMBERED = re.compile(r"^(\d+(?:\.\d+)?)\.?\s+")


def split_sections(text):
    """Return {section-number: body} for `## <n>. <title>` headings."""
    sections, matches = {}, list(HEADING.finditer(text))
    for i, m in enumerate(matches):
        num = NUMBERED.match(m.group(1))
        if not num:
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[num.group(1)] = text[m.end():end]
    return sections


def check_loop(name, text):
    """Return a list of human-readable problems for one loop skill."""
    sections = split_sections(text)
    missing_sections = [s for s in REQUIRED_SECTIONS if s not in sections]
    if missing_sections:
        return [f"missing required section(s): {missing_sections}"]
    return [
        f"section {sec} missing {label}"
        for sec, label, pattern in REQUIRED
        if not re.search(pattern, sections[sec])
    ]


def main():
    if not SKILLS.exists():
        print(f"FAIL: no skills dir at {SKILLS}")
        return 1

    loops = sorted(p for p in SKILLS.iterdir() if p.is_dir() and p.name != METHOD)
    if not loops:
        # Without this guard an empty glob reports "All 0 loop skills pass" and
        # exits 0 — a vacuous pass that would hide a build/checkout failure.
        print(f"FAIL: no loop skills found under {SKILLS}")
        return 1

    failed = 0
    for loop in loops:
        md = loop / "SKILL.md"
        if not md.exists():
            print(f"FAIL {loop.name}: no SKILL.md")
            failed += 1
            continue
        problems = check_loop(loop.name, md.read_text(encoding="utf-8", errors="ignore"))
        if problems:
            print(f"FAIL {loop.name}:")
            for p in problems:
                print(f"       - {p}")
            failed += 1
        else:
            print(f"ok   {loop.name}: all {len(REQUIRED)} guardrails present, in-section")

    # The method skill must document the red lines, under its own heading.
    method = SKILLS / METHOD / "SKILL.md"
    if not method.exists():
        print(f"FAIL {METHOD}: no SKILL.md")
        failed += 1
    else:
        t = method.read_text(encoding="utf-8", errors="ignore")
        if not any(re.search(r"(?i)red line", h) for h in HEADING.findall(t)):
            print(f"FAIL {METHOD}: no section heading documents the clinical red lines")
            failed += 1
        else:
            print(f"ok   {METHOD}: red lines documented")

    if failed:
        print(f"\n{failed} guardrail failure(s).")
        return 1
    print(f"\nAll {len(loops)} loop skills pass the guardrail check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
