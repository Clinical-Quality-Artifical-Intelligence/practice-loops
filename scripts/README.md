# Developer Scripts

Utility scripts for validating, linting, auditing, and analysing Practice Loops.

## Scripts Overview

| Script | Purpose |
|---|---|
| `validate.py` | Validates plugin manifests, skill structure, proficiency database, and memory layer. Run on every push via CI. |
| `check_guardrails.py` | Static guardrail eval — asserts every loop skill encodes the 9 non-negotiable safety clauses (HALT, DRAFT, sign-off, etc.). |
| `check-audit.py` | Validates audit log file format and completeness. |
| `aggregate_governance.py` | **Cohort Governance Aggregator** — parses `./practice-loop-audit/` logs to generate ward/trust quality signals. |

## Usage

```bash
# Validate plugin structure
python scripts/validate.py

# Check safety guardrails
python scripts/check_guardrails.py

# Generate cohort governance summary (terminal output)
python scripts/aggregate_governance.py

# Generate cohort governance summary (markdown file)
python scripts/aggregate_governance.py --output practice-loop-audit/governance-summary.md
```
