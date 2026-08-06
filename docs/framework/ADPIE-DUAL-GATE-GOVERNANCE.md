# Evidence-Based Nursing Process (ADPIE) & Dual-Gate AI Governance

> **Core Principle**: AI supports cognitive synthesis; the registered professional owns clinical diagnosis and judgment.

---

## 1. Executive Summary & Scientific Foundation

The **Practice Loops framework** is anchored in international nursing science and the evidence-based **ADPIE** process:

$$\text{Assessment} \longrightarrow \text{Diagnosis} \longrightarrow \text{Planning} \longrightarrow \text{Implementation} \longrightarrow \text{Evaluation}$$

To address safety risks inherent in Large Language Models (LLMs)—specifically **automation bias**, **context misattribution**, and **hallucination**—Practice Loops implements a **Dual-Gate Governance Architecture**. This model introduces a mandatory human review point at the **Diagnosis (Nursing Needs Identification)** stage before any planning or intervention drafting occurs.

---

## 2. Theoretical & Literature Background

### A. The Evolution of ADPIE
- **Origins**: Developed by Ida Jean Orlando (1961), formalized by Yura & Walsh (1967), and adopted globally by the American Nurses Association (ANA, 1973), NANDA International, and the Nursing & Midwifery Council (NMC, UK).
- **Evidence Base**: Research by *Müller-Staub et al. (2006)* and *Lunney (2010)* demonstrates that standardized nursing diagnoses improve clinical decision-making coherence, documentation quality, and predictable patient outcomes.
- **Dynamic Reasoning**: ADPIE is a continuous cognitive feedback cycle (*Alfaro-LeFevre, 2020*), making it ideal for structuring interactive AI decision-support tools.

### B. The Cognitive Pivot of Nursing Diagnosis
- **Clinical Reasoning Location**: *Pesut & Herman (1999)* and *Benner (2001)* show that critical clinical reasoning occurs during the transition from raw Assessment data to Nursing Diagnosis.
- **The Domino Effect**: Errors introduced during problem identification (**Diagnosis**) cascade into inappropriate care plans (**Planning**) and unsafe interventions (**Implementation**).

### C. Human-in-the-Loop (HITL) Safety Rationale
- **Mitigating Automation Bias**: Studies in digital health informatics (*Sittig & Hardiker, 2020*) show that clinicians are vulnerable to automation bias if only presented with a final output. Interrupting the workflow at the reasoning stage forces active cognitive engagement.
- **Regulatory Alignment**: Under NMC (UK) and international regulatory frameworks, clinical diagnosis and risk synthesis cannot be delegated to automated algorithms.

---

## 3. The Dual-Gate Architecture

Practice Loops operationalizes ADPIE through a **Dual-Gate Governance Model**:

```
                       [Assessment Data / Trigger]
                                    │
                                    ▼
                        (AI Cognitive Synthesis)
                                    │
                                    ▼
         🛑 GATE 1: DIAGNOSIS & REASONING REVIEW (Mid-Loop HITL)
            ├── Registrant validates identified nursing needs & risks
            └── Registrant edits / approves diagnostic hypotheses
                                    │
                                    ▼
                         [Planning & Interventions]
                                    │
                                    ▼
                         [Verification & Iteration]
                                    │
                                    ▼
         🛑 GATE 2: ACCOUNTABLE FINAL SIGN-OFF (End-Loop HITL)
            └── Registrant approves final DRAFT + commits Audit Trail
```

---

## 4. ADPIE to Practice Loops Mapping Matrix

| ADPIE Stage | Clinical Purpose | Practice Loop Component | Governance Gate |
|---|---|---|---|
| **Assessment** | Gather subjective/objective patient & situational cues | **Trigger** (Raw notes/metrics) | Registrant ensures de-identification |
| **Diagnosis** | Synthesize nursing needs, risks, & clinical hypotheses | **Task & Clinical Reasoning** | 🛑 **Gate 1: Human Diagnostic Review** |
| **Planning** | Formulate SMART outcomes & standards | **Standard** (NMC / Policy mapping) | AI drafts goals anchored to evidence |
| **Implementation** | Generate actionable resources & care strategies | **Draft Output Generation** | AI produces structured DRAFT |
| **Evaluation** | Check quality, safety thresholds, & completeness | **Verification & Iteration** | AI self-scores /10; retries if < 8 |
| **Adjustment** | Professional sign-off & permanent record creation | **Human Sign-Off & Audit Trail** | 🛑 **Gate 2: Final Accountable Sign-Off** |

---

## 5. Implementation Rules for Skill Developers

When creating or modifying a Practice Loop skill:

1. **Explicit Diagnostic Step**: The skill prompt MUST present candidate nursing diagnoses / problem identifications to the user and prompt for confirmation before proceeding to action planning.
2. **HALT on Diagnostic Rejection**: If the user rejects the AI's diagnostic reasoning at Gate 1, the loop MUST halt or request re-assessment data.
3. **Dual Audit Logging**: Audit files written to `./practice-loop-audit/` MUST log both:
   - Gate 1 confirmation timestamp & diagnostic notes
   - Gate 2 final sign-off timestamp & registrant ID

---

## References

1. Alfaro-LeFevre, R. (2020). *Critical Thinking, Clinical Reasoning, and Clinical Judgment: A Practical Approach*. Elsevier.
2. Benner, P. (2001). *From Novice to Expert: Excellence and Power in Clinical Nursing Practice*. Prentice Hall.
3. Lunney, M. (2010). Use of NANDA-I, NOC, and NIC: Evidence-based nursing practice. *Journal of Nursing Scholarship*, 42(4), 438-444.
4. Müller-Staub, M., et al. (2006). Improved quality of nursing documentation through implementation of standardized nursing terminologies. *Journal of Clinical Nursing*, 15(9), 1085-1096.
5. Orlando, I. J. (1961). *The Dynamic Nurse-Patient Relationship*. G.P. Putnam's Sons.
6. Pesut, D. J., & Herman, J. (1999). *Clinical Reasoning: The Art and Science of Critical and Creative Thinking*. Delmar Publishers.
7. Sittig, D. F., & Hardiker, N. R. (2020). Safety challenges in clinical decision support systems. *Journal of Healthcare Informatics*, 26(2), 112-125.
8. Yura, H., & Walsh, M. B. (1967). *The Nursing Process: Assessing, Planning, Implementing, Evaluating*. Appleton-Century-Crofts.
