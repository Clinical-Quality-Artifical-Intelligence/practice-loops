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
    d = json.loads(mk.read_text(encoding="utf-8"))
    check("name" in d, "marketplace.json: missing 'name'")
    check(isinstance(d.get("plugins"), list) and d["plugins"], "marketplace.json: 'plugins' must be a non-empty list")

# plugin.json
pj = PLUGIN / ".claude-plugin" / "plugin.json"
check(pj.exists(), "missing plugin.json")
if pj.exists():
    d = json.loads(pj.read_text(encoding="utf-8"))
    for f in ("name", "description", "version"):
        check(f in d, f"plugin.json: missing '{f}'")
    check(d.get("name") == "practice-loops", "plugin.json: name must be 'practice-loops'")

# package.json
pkg = ROOT / "package.json"
check(pkg.exists(), "missing package.json")
if pkg.exists():
    d = json.loads(pkg.read_text(encoding="utf-8"))
    check("name" in d, "package.json: missing 'name'")
    check(d.get("name") == "@clinical-quality-artifical-intelligence/practice-loops", "package.json: name must be '@clinical-quality-artifical-intelligence/practice-loops'")

# skills: each skills/<x>/SKILL.md must have YAML frontmatter with a description
skills_dir = PLUGIN / "skills"
if skills_dir.exists():
    for sk in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        md = sk / "SKILL.md"
        check(md.exists(), f"{sk.name}: missing SKILL.md")
        if md.exists():
            text = md.read_text(encoding="utf-8")
            m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            check(bool(m), f"{sk.name}: SKILL.md missing YAML frontmatter")
            if m:
                check("description:" in m.group(1), f"{sk.name}: frontmatter missing 'description'")
            # loop skills (not the method skill) must enforce the audit log + DRAFT sign-off
            if sk.name != "practice-loop-method":
                check("practice-loop-audit" in text, f"{sk.name}: SKILL.md must write to ./practice-loop-audit/")
                check("DRAFT" in text, f"{sk.name}: SKILL.md must mark output as DRAFT")

EXPECTED = {
    "practice-loop-method",
    "placement-support",
    "preceptorship",
    "clinical-supervision",
    "edi-intelligence",
    "teaching",
    "action-tracking",
    "revalidation",
    "reflective-practice",
    "incident-reflection",
    "reasonable-adjustments-passport",
    "policy-to-practice",
}
present = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.exists() else set()
missing = EXPECTED - present
check(not missing, f"missing required skills: {sorted(missing)}")

# proficiencies database
prof_dir = skills_dir / "placement-support" / "references" / "proficiencies"
check(prof_dir.exists(), "missing placement-support/references/proficiencies/ directory")
if prof_dir.exists():
    for db_file in ("assessment-methods.md", "year-1-proficiencies.md", "year-2-proficiencies.md", "year-3-proficiencies.md"):
        check((prof_dir / db_file).exists(), f"missing proficiency database file: {db_file}")

# practice-loop-memory directory
mem_dir = ROOT / "practice-loop-memory"
check(mem_dir.exists(), "missing practice-loop-memory/ directory")
if mem_dir.exists():
    check((mem_dir / "README.md").exists(), "missing practice-loop-memory/README.md")
    check((mem_dir / "schema.json").exists(), "missing practice-loop-memory/schema.json")
    if (mem_dir / "schema.json").exists():
        schema = json.loads((mem_dir / "schema.json").read_text(encoding="utf-8"))
        check("properties" in schema, "schema.json: missing 'properties' key")
        check("learner_pseudonym" in schema.get("properties", {}), "schema.json: missing 'learner_pseudonym' property")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"OK — {len(present)} skills validated: {sorted(present)}")
