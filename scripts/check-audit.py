#!/usr/bin/env python3
"""Lint practice-loop audit logs for governance completeness.

Usage: python3 scripts/check-audit.py [AUDIT_DIR]
Default AUDIT_DIR is ./practice-loop-audit. Exits non-zero if any audit file is
missing required governance fields. Intended for periodic CSO / governance review."""
import sys, pathlib, re

REQUIRED = [
    ("timestamp", r"(?im)^- *Timestamp:"),
    ("operator", r"(?im)^- *Operator:"),
    ("loop & version", r"(?im)^- *Loop & version:"),
    ("input provenance", r"(?im)^- *Input provenance:"),
    ("verification scores", r"(?im)^##+ *Verification scores"),
    ("escalations section", r"(?im)^##+ *Escalations"),
    ("DRAFT sign-off status", r"(?i)DRAFT.*sign[- ]?off"),
]

def main():
    audit_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "practice-loop-audit")
    if not audit_dir.exists():
        print(f"No audit directory at '{audit_dir}'. Nothing to check.")
        return 0
    files = sorted(audit_dir.glob("*.md"))
    if not files:
        print(f"No audit logs in '{audit_dir}'.")
        return 0
    failed = 0
    for f in files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        missing = [name for name, pat in REQUIRED if not re.search(pat, text)]
        if missing:
            failed += 1
            print(f"FAIL {f.name}: missing {missing}")
        else:
            print(f"ok   {f.name}")
    if failed:
        print(f"\n{failed} audit file(s) incomplete.")
        return 1
    print(f"\nAll {len(files)} audit log(s) complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
