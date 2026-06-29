#!/usr/bin/env python3
"""UserPromptSubmit hook: warn (non-blocking) when a prompt looks like it contains
identifiable patient/staff data, reminding the user to anonymise. Defence-in-depth for
the practice-loops plugin — it never blocks, it injects a cautionary system reminder."""
import sys, json, re

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # never disrupt the session
    prompt = data.get("user_prompt", "") or ""

    patterns = {
        "NHS number (10 digits)": r"\b\d{3}[ -]?\d{3}[ -]?\d{4}\b",
        "date of birth": r"\b(0?[1-9]|[12]\d|3[01])[/\-.](0?[1-9]|1[0-2])[/\-.](19|20)\d\d\b",
        "email address": r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b",
        "UK postcode": r"\b[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}\b",
    }
    hits = [name for name, pat in patterns.items() if re.search(pat, prompt, re.I)]
    if not hits:
        sys.exit(0)

    msg = (
        "POSSIBLE IDENTIFIABLE DATA detected in this prompt (" + ", ".join(hits) + "). "
        "Practice Loops are for ANONYMISED inputs only. Before proceeding, confirm the data is "
        "anonymised or has Information Governance (IG) approval. Do not record identifiable "
        "patient/staff data; if a loop is running, follow its identifiable-data HALT step."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": msg
        }
    }))
    sys.exit(0)

if __name__ == "__main__":
    main()
