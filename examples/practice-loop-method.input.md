# Sample Practice Loop Method Proposal (Synthetic)

## Loop Name
- `handover-summary`

## Proposed Purpose
- Transform raw, unstructured shift handover notes into a standardized SBAR (Situation, Background, Assessment, Recommendation) draft summary for oncoming nurses.

## Proposed 6-Pillar Loop Definition
1. **Trigger**: Raw shift notes pasted by registrant.
2. **Task**: Extract patient safety priorities, pending lab results, and outstanding care tasks.
3. **Standard**: SBAR structure; NMC Code *Preserve Safety* & *Practise Effectively*.
4. **Verification**: 10-point scoring against completeness, accuracy, and de-identification.
5. **Iteration**: Self-correct if score < 8/10.
6. **Human Sign-Off**: Registrant reviews and approves before pasting into electronic health record.
