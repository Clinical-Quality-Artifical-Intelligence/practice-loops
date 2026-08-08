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
# 10 (memory update) is intentionally absent: it is opt-in per loop, and is instead
# enforced for read/write symmetry by check_memory_symmetry() below.
# 3.5 (Gate 1) IS required: human validation of the reasoning before drafting is a
# governance property of every loop, not an optional extra.
REQUIRED_SECTIONS = ["1", "2", "3", "3.5", "4", "5", "6", "7", "8", "9"]

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
    # Gate 1 must actually halt. A section that merely describes the reasoning without
    # pausing for the registrant is the failure this check exists to catch.
    ("3.5", "Gate 1 stop condition",   r"(?i)\bstop\b|wait for the nurse|do not proceed"),
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


def check_memory_symmetry(sections):
    """Memory read (1.5) and memory write (10) are two halves of one mechanism.

    A loop that writes a trajectory but never reads it accumulates a record nobody
    benefits from, and silently fails the cross-session promise it advertises. Rather
    than force every loop to carry memory, require that whichever half exists brings
    the other with it.
    """
    has_read = "1.5" in sections and re.search(r"practice-loop-memory", sections["1.5"])
    has_write = "10" in sections and re.search(r"practice-loop-memory", sections["10"])
    problems = []
    if has_write and not has_read:
        problems.append(
            "writes memory in section 10 but never reads it: section 1.5 must read "
            "./practice-loop-memory/<pseudonym>.json before reasoning")
    if has_read and not has_write:
        problems.append(
            "reads memory in section 1.5 but never writes it: section 10 must append a "
            "trajectory entry")
    if (has_read or has_write) and not re.search(r"(?i)pseudonym", sections.get("1", "")):
        problems.append(
            "uses memory but section 1 never asks for a pseudonym, so the memory "
            "condition can never be satisfied")
    return problems


def check_loop(name, text):
    """Return a list of human-readable problems for one loop skill.

    Reports every class of problem in one pass rather than returning at the first.
    A missing section and a broken memory contract are independently useful to know
    about, and stopping early hides the second behind the first.
    """
    sections = split_sections(text)
    problems = [
        f"missing required section: {s}" for s in REQUIRED_SECTIONS if s not in sections
    ]
    problems += [
        f"section {sec} missing {label}"
        for sec, label, pattern in REQUIRED
        # sections absent entirely are already reported above; don't double-report
        if sec in sections and not re.search(pattern, sections[sec])
    ]
    return problems + check_memory_symmetry(sections)


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
