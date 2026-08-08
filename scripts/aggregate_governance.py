#!/usr/bin/env python3
"""
Practice Loops — Cohort Governance Aggregator
==============================================
Parses ./practice-loop-audit/ logs and generates a Level 3 Reflective Memory report:
  - Audit compliance & human sign-off completion rate
  - Average 10-point verification scores
  - Frequency of safety/wellbeing flags
  - Top mapped NMC proficiencies across runs

Usage:
    python scripts/aggregate_governance.py
    python scripts/aggregate_governance.py --output governance-summary.md
"""

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
AUDIT_DIR = ROOT / "practice-loop-audit"


FLAG_PATTERNS = [
    (r"(?i)patient.?safety", "Patient Safety"),
    (r"(?i)safeguarding", "Safeguarding"),
    (r"(?i)escalat(?:ion|ed|e)", "Escalation"),
    (r"(?i)wellbeing|well-being", "Wellbeing"),
    (r"(?i)fitness.?to.?practise", "Fitness to Practise"),
]

# A bullet that records the ABSENCE of a concern, e.g.
#   "- **No fitness-to-practise indicator identified.**"
NEGATED_BULLET = re.compile(r"^\s*[-*+]?\s*\*{0,2}(?:no|none|not|nil)\b", re.I)


def extract_section(content, heading_pattern):
    """Return the body of the first `## <heading>` matching heading_pattern."""
    lines = content.splitlines()
    out, capturing = [], False
    for line in lines:
        if line.startswith("#"):
            if capturing:
                break
            if re.search(heading_pattern, line, re.I):
                capturing = True
            continue
        if capturing:
            out.append(line)
    return "\n".join(out)


def parse_scores(content):
    """Extract the ten verifier scores from each round row of the score table.

    Rows look like:
        | Round | 1 | 2 | ... | 10 | Min |
        |-------|---|---|-----|----|-----|
        | 1     | 9 | 7 | ... | 10 | 7   |

    A naive `\\|\\s*(\\d{1,2})\\s*\\|` over the whole file is wrong three ways: it
    captures the Round number as a score (reporting a "lowest score" of 1 for a run
    whose true minimum was 7), it captures the Min column a second time, and because
    regex matches cannot overlap it silently skips alternate cells. Parse the table
    structurally instead.
    """
    scores = []
    in_table = False
    for raw in content.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0].lower().startswith("round"):
            in_table = True
            continue
        if set("".join(cells)) <= set("-: "):  # header separator row
            continue
        if not in_table or len(cells) < 3:
            continue
        # First cell is the round number, last is the pre-computed Min.
        for cell in cells[1:-1]:
            m = re.fullmatch(r"(\d{1,2})(?:/10)?", cell)
            if m and 0 <= int(m.group(1)) <= 10:
                scores.append(int(m.group(1)))
    return scores


def parse_flags(content):
    """Count flags raised in the Escalations / flags section.

    Scoped to that section, and bullets recording the absence of a concern are
    skipped. A whole-file keyword search counts "No fitness-to-practise indicator
    identified" as a fitness-to-practise flag — reporting the opposite of what the
    registrant actually wrote, in the direction that most alarms a reader.
    """
    section = extract_section(content, r"escalation|flags")
    if not section.strip():
        section = content  # fall back rather than silently reporting zero

    found = []
    for raw in section.splitlines():
        line = raw.strip()
        if not line or NEGATED_BULLET.match(line):
            continue
        for pattern, label in FLAG_PATTERNS:
            if re.search(pattern, line) and label not in found:
                found.append(label)
    return found


def parse_audit_file(filepath):
    """Parse a single audit log markdown file and extract structured data."""
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    result = {
        "file": filepath.name,
        "signed_off": True,
        "scores": parse_scores(content),
        "safety_flags": parse_flags(content),
        "proficiencies": [],
    }

    # Sign-off status
    if "DRAFT" in content and "pending human sign-off" in content:
        result["signed_off"] = False

    # Extract proficiency references (P1 through P29, with optional *)
    profs = re.findall(r"\bP(\d{1,2})\*?\b", content)
    result["proficiencies"] = [f"P{p}" for p in profs if 1 <= int(p) <= 29]

    return result


def aggregate(results):
    """Aggregate parsed results into a summary report."""
    total = len(results)
    signed_off = sum(1 for r in results if r["signed_off"])
    pending = total - signed_off

    all_scores = []
    for r in results:
        all_scores.extend(r["scores"])

    flag_counts = {}
    for r in results:
        for f in r["safety_flags"]:
            flag_counts[f] = flag_counts.get(f, 0) + 1

    prof_counts = {}
    for r in results:
        for p in r["proficiencies"]:
            prof_counts[p] = prof_counts.get(p, 0) + 1

    return {
        "total_runs": total,
        "signed_off": signed_off,
        "pending": pending,
        "compliance_rate": (signed_off / total * 100) if total > 0 else 0,
        "scores": all_scores,
        "avg_score": (sum(all_scores) / len(all_scores)) if all_scores else None,
        "min_score": min(all_scores) if all_scores else None,
        "max_score": max(all_scores) if all_scores else None,
        "flag_counts": flag_counts,
        "total_flags": sum(flag_counts.values()),
        "prof_counts": prof_counts,
    }


def format_report(summary):
    """Format the summary as a readable report string."""
    lines = []
    lines.append("=" * 65)
    lines.append(" 🩺 PRACTICE LOOPS — COHORT GOVERNANCE SUMMARY")
    lines.append("=" * 65)
    lines.append("")
    lines.append(f"  Total Practice Loop Runs        : {summary['total_runs']}")
    lines.append(f"  Completed Human Sign-Offs (G2)   : {summary['signed_off']}")
    lines.append(f"  Pending Sign-Offs (DRAFT)        : {summary['pending']}")
    lines.append(f"  Gate 2 Compliance Rate            : {summary['compliance_rate']:.0f}%")
    lines.append("")

    if summary["avg_score"] is not None:
        lines.append("  --- Verification Scores ---")
        lines.append(f"  Average Score                    : {summary['avg_score']:.1f}/10  (target: ≥8)")
        lines.append(f"  Lowest Score                     : {summary['min_score']}/10")
        lines.append(f"  Highest Score                    : {summary['max_score']}/10")
        lines.append("")

    if summary["flag_counts"]:
        lines.append("  --- Safety & Escalation Flags ---")
        for flag, count in sorted(summary["flag_counts"].items(), key=lambda x: x[1], reverse=True):
            lines.append(f"  {flag:<35}: {count}")
        lines.append(f"  Total flags across all runs      : {summary['total_flags']}")
        lines.append("")

    if summary["prof_counts"]:
        lines.append("  --- Top Mapped NMC Proficiencies ---")
        sorted_profs = sorted(summary["prof_counts"].items(), key=lambda x: x[1], reverse=True)
        for p, count in sorted_profs[:10]:
            lines.append(f"  {p:<8}: {count} occurrences")
        lines.append("")

    lines.append("=" * 65)
    return "\n".join(lines)


def format_markdown(summary):
    """Format the summary as a markdown document."""
    lines = []
    lines.append("# Practice Loops — Cohort Governance Summary\n")
    lines.append(f"*Generated from `./practice-loop-audit/` — {summary['total_runs']} run(s) analysed.*\n")

    lines.append("## Audit Compliance\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Total Runs | {summary['total_runs']} |")
    lines.append(f"| Human Sign-Offs Complete (Gate 2) | {summary['signed_off']} |")
    lines.append(f"| Pending (DRAFT) | {summary['pending']} |")
    lines.append(f"| Compliance Rate | {summary['compliance_rate']:.0f}% |")
    lines.append("")

    if summary["avg_score"] is not None:
        lines.append("## Verification Scores\n")
        lines.append("| Metric | Value |")
        lines.append("|---|---|")
        lines.append(f"| Average Score | {summary['avg_score']:.1f}/10 |")
        lines.append(f"| Lowest Score | {summary['min_score']}/10 |")
        lines.append(f"| Highest Score | {summary['max_score']}/10 |")
        lines.append("")

    if summary["flag_counts"]:
        lines.append("## Safety & Escalation Flags\n")
        lines.append("| Flag Type | Count |")
        lines.append("|---|---|")
        for flag, count in sorted(summary["flag_counts"].items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| {flag} | {count} |")
        lines.append("")

    if summary["prof_counts"]:
        lines.append("## Top Mapped NMC Proficiencies\n")
        lines.append("*Most frequently mapped proficiencies indicate common learning themes across the cohort.*\n")
        lines.append("| Proficiency | Occurrences |")
        lines.append("|---|---|")
        sorted_profs = sorted(summary["prof_counts"].items(), key=lambda x: x[1], reverse=True)
        for p, count in sorted_profs[:10]:
            lines.append(f"| {p} | {count} |")
        lines.append("")

    lines.append("---\n")
    lines.append("*This report is auto-generated by `scripts/aggregate_governance.py`. It summarises trends — it does not make clinical decisions.*")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate Practice Loop audit logs into a governance summary."
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Write a markdown summary to the specified file path (relative to repo root).",
    )
    args = parser.parse_args()

    if not AUDIT_DIR.exists():
        print(f"No practice-loop-audit/ directory found at {AUDIT_DIR}")
        return 1

    audit_files = sorted(AUDIT_DIR.glob("*.md"))
    # Exclude governance summary files from analysis
    audit_files = [f for f in audit_files if "governance-summary" not in f.name]

    if not audit_files:
        print("No audit log files found under ./practice-loop-audit/")
        return 1

    results = [parse_audit_file(f) for f in audit_files]
    summary = aggregate(results)

    # Print terminal report
    print(format_report(summary))

    # Optionally write markdown
    if args.output:
        output_path = ROOT / args.output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(format_markdown(summary), encoding="utf-8")
        print(f"\nMarkdown summary written to: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
