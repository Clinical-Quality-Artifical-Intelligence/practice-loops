#!/usr/bin/env python3
"""Assert the plugin manifests are valid JSON. Exit non-zero on any problem.

Kept as a file rather than an inline `python -c` in CI: inline double-quoted Python
is quoted differently by bash and pwsh, so the same step would not be portable
across the ubuntu/windows matrix legs.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

MANIFESTS = (
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "plugins" / "practice-loops" / ".claude-plugin" / "plugin.json",
)

def main():
    failed = 0
    for m in MANIFESTS:
        rel = m.relative_to(ROOT).as_posix()
        if not m.exists():
            print(f"FAIL {rel}: missing"); failed += 1; continue
        try:
            # encoding is explicit: without it Windows falls back to cp1252 and any
            # non-ASCII character (e.g. the ™ used throughout this project) breaks CI.
            json.loads(m.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"FAIL {rel}: invalid JSON -> {e}"); failed += 1
        else:
            print(f"ok   {rel}")
    if failed:
        print(f"\n{failed} manifest failure(s)."); return 1
    print("\nmanifests OK"); return 0

if __name__ == "__main__":
    sys.exit(main())
