#!/usr/bin/env python3
"""Validate the practice-loops plugin structure. Exit non-zero on any problem."""
import json, sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "practice-loops"
errors = []

def check(cond, msg):
    if not cond:
        errors.append(msg)

# marketplace.json
mk = ROOT / ".claude-plugin" / "marketplace.json"
check(mk.exists(), "missing .claude-plugin/marketplace.json")
if mk.exists():
    d = json.loads(mk.read_text())
    check("name" in d, "marketplace.json: missing 'name'")
    check(isinstance(d.get("plugins"), list) and d["plugins"], "marketplace.json: 'plugins' must be a non-empty list")

# plugin.json
pj = PLUGIN / ".claude-plugin" / "plugin.json"
check(pj.exists(), "missing plugin.json")
if pj.exists():
    d = json.loads(pj.read_text())
    for f in ("name", "description", "version"):
        check(f in d, f"plugin.json: missing '{f}'")
    check(d.get("name") == "practice-loops", "plugin.json: name must be 'practice-loops'")

# skills: each skills/<x>/SKILL.md must have YAML frontmatter with a description
skills_dir = PLUGIN / "skills"
if skills_dir.exists():
    for sk in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        md = sk / "SKILL.md"
        check(md.exists(), f"{sk.name}: missing SKILL.md")
        if md.exists():
            text = md.read_text()
            m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            check(bool(m), f"{sk.name}: SKILL.md missing YAML frontmatter")
            if m:
                check("description:" in m.group(1), f"{sk.name}: frontmatter missing 'description'")
            # loop skills (not the method skill) must enforce the audit log + DRAFT sign-off
            if sk.name != "practice-loop-method":
                check("practice-loop-audit" in text, f"{sk.name}: SKILL.md must write to ./practice-loop-audit/")
                check("DRAFT" in text, f"{sk.name}: SKILL.md must mark output as DRAFT")

EXPECTED = {"practice-loop-method", "placement-support"}
present = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.exists() else set()
missing = EXPECTED - present
check(not missing, f"missing required skills: {sorted(missing)}")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"OK — {len(present)} skills validated: {sorted(present)}")
