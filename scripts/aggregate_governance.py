#!/usr/bin/env python3
"""
Practice Loops Governance Aggregator
Parses `./practice-loop-audit/` logs and generates a Level 3 Reflective Memory report:
- Audit compliance & human sign-off completion rate
- Average 10-point verification scores
- Frequency of safety/wellbeing flags
- Top mapped NMC proficiencies across runs
"""

import pathlib, re, json, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
AUDIT_DIR = ROOT / "practice-loop-audit"

def analyze_audits():
    if not AUDIT_DIR.exists():
        print("No practice-loop-audit directory found.")
        return

    audit_files = sorted(AUDIT_DIR.glob("*.md"))
    if not audit_files:
        print("No audit log files found under ./practice-loop-audit/")
        return

    total_runs = len(audit_files)
    signed_off = 0
    pending_signoff = 0
    scores = []
    safety_flags = 0
    proficiency_counts = {}

    for f in audit_files:
        content = f.read_text(encoding="utf-8", errors="ignore")
        
        # Sign-off status check
        if "DRAFT — pending human sign-off" in content or "pending human sign-off" in content:
            pending_signoff += 1
        else:
            signed_off += 1

        # Min score extraction
        score_matches = re.findall(r"\|\s*(\d{1,2})/10\s*\|", content)
        for s in score_matches:
            val = int(s)
            if val <= 10:
                scores.append(val)

        # Safety flags check
        if "Patient Safety Flag" in content or "escalat" in content.lower():
            safety_flags += 1

        # Proficiency extraction (P1 - P29, P1* - P29*)
        profs = re.findall(r"\b(P\d{1,2}\*?)\b", content)
        for p in profs:
            proficiency_counts[p] = proficiency_counts.get(p, 0) + 1

    print("=" * 60)
    print(" 🩺 PRACTICE LOOPS — COHORT GOVERNANCE & REFLECTIVE MEMORY SUMMARY")
    print("=" * 60)
    print(f"Total Practice Loop Runs Evaluated : {total_runs}")
    print(f"Completed Human Sign-Offs (Gate 2) : {signed_off}")
    print(f"Pending Human Sign-Offs (DRAFT)    : {pending_signoff}")
    
    if scores:
        avg_score = sum(scores) / len(scores)
        print(f"Average Verification Score         : {avg_score:.1f}/10 (Target: >=8/10)")
        print(f"Lowest Score Encountered           : {min(scores)}/10")

    print(f"Safety/Escalation Flags Surfaced   : {safety_flags}")
    
    if proficiency_counts:
        print("\nTop Mapped NMC Proficiencies Across Runs:")
        sorted_profs = sorted(proficiency_counts.items(), key=lambda x: x[1], reverse=True)
        for p, count in sorted_profs[:5]:
            print(f"  - {p}: {count} occurrences")
    print("=" * 60)

if __name__ == "__main__":
    analyze_audits()
