# DPIA — Cross-Session Learner Memory (`practice-loop-memory/`)

**Status:** TEMPLATE — requires completion and sign-off by the deploying organisation
**Feature assessed:** opt-in cross-session learner memory (loop steps 1.5 and 10)
**Framework:** UK GDPR Article 35, following the ICO's seven-step DPIA process
**Version assessed:** `practice-loops` at the merge of PR #7
**Template prepared:** 8 August 2026

---

## How to use this document

Practice Loops is software, not a service. Memory files are written to the operator's own
disk and **never transmitted to Clinical Quality Artificial Intelligence (CQAI)**. CQAI is
therefore neither controller nor processor for this data.

**The data controller is the NHS trust, university, or other organisation that deploys the
plugin** (or, for a self-directed registrant using it on their own CPD, that individual).
That organisation must complete and sign off this DPIA before enabling memory for real
learners.

Sections marked 🔹 are pre-populated from the software's actual behaviour and should be
verified, not assumed. Sections marked ⬜ **must be completed by the deploying organisation** —
they depend on facts about your estate that the software cannot know.

> A DPIA that glosses over risk is worse than no DPIA: it manufactures a false assurance.
> Risks below are stated at full strength deliberately.

---

## Step 1 — Screening: is a DPIA required?

Assessed against the ICO's nine high-risk criteria.

| # | ICO criterion | Met? | Basis |
|---|---|:---:|---|
| 1 | Evaluation or scoring | **Yes** | Each session records 10-point verifier scores, `learning_gaps` and `strengths` about an identified-by-pseudonym individual |
| 2 | Automated decision-making with legal or significant effects | **No** | Two human gates (§3.5, §7–8); loops are explicitly forbidden from progression, pass/fail, fitness-to-practise, capability and employment decisions. **But** outputs inform human assessment decisions — see Risk R7 |
| 3 | Systematic monitoring | **Yes** | The feature exists to track a learner's development trajectory longitudinally across sessions |
| 4 | Sensitive or highly personal data | **Yes** | Not by design, but reachable in practice — see Risk R1. Schema `flags` examples include `"wellbeing: sleep disruption"` |
| 5 | Large scale | ⬜ | Depends on deployment. Cohort-wide use across a placement provider would meet this |
| 6 | Matching or combining datasets | ⬜ | Met if memory content is reconciled against PAD records, attendance, or student records |
| 7 | Data concerning vulnerable individuals | **Yes** | Students in a marked power imbalance: the assessors operating the loop control their progression |
| 8 | Innovative use of technology | **Yes** | Large language model applied to educational assessment support |
| 9 | Processing that could prevent someone exercising a right or using a service | **Yes (potential)** | Recalled gaps and flags may influence placement progression and support decisions |

**Determination: a DPIA is REQUIRED.** Six criteria are met on the software's behaviour alone,
against an ICO threshold of two.

---

## Step 2 — Describe the processing

### 2.1 Nature 🔹

Memory is a read/write pair around a Practice Loop run:

- **Step 1 (`on_intake`)** — the loop offers cross-session memory and asks for a pseudonym. Real names, initials and staff numbers are to be refused. No pseudonym means the loop runs statelessly and steps 1.5 and 10 are skipped.
- **Step 1.5 (`on_intake`)** — before any reasoning, the loop reads `./practice-loop-memory/<pseudonym>.json` and surfaces open learning gaps with first-recorded dates, prior flags, the verifier score trend, and `assessor_preferences`.
- **Step 10 (`on_commit`)** — the loop appends a trajectory entry for this session.

Reads and writes are programmatic, not model-discretionary: the assistant cannot elect to skip
consulting or updating the record.

### 2.2 Scope 🔹

Per `practice-loop-memory/schema.json`, each record holds:

| Field | Content |
|---|---|
| `learner_pseudonym` | Operator-supplied pseudonym (also the filename) |
| `programme_year` | NMC programme year 1, 2 or 3 |
| `trajectory[].date` | ISO date of each run |
| `trajectory[].loop` | Which loop was executed |
| `trajectory[].proficiencies_mapped` | NMC proficiency codes, e.g. `P7`, `P10*` |
| `trajectory[].scores` | `round1_min`, `final_min` (0–10) |
| `trajectory[].flags` | Escalation/safety flags, free text |
| `trajectory[].learning_gaps` | Free text |
| `trajectory[].strengths` | Free text |
| `assessor_preferences` | `trust_name`, `custom_verifier_notes`, `preferred_phrasing` |

Volume, number of data subjects, and frequency: ⬜ **to be completed.**

### 2.3 Context 🔹

Pre-registration nursing students, nursing associates, preceptees and supervisees on NHS
placement, and registrants using reflective or revalidation loops on their own practice. The
relationship is one of assessment: the operator is typically the practice assessor, practice
supervisor, academic assessor or PEF. Data subjects are unlikely to expect a persistent
cross-session record to exist unless told, which makes Step 3 material rather than a formality.

### 2.4 Data flow 🔹

```
Nurse pastes anonymised notes  ──►  Step 1: HALT if identifiable
                                    Step 1: pseudonym requested (opt-in)
                                              │
                              ┌───────────────┴───────────────┐
                       no pseudonym                     pseudonym given
                              │                               │
                     stateless run                Step 1.5: READ
                     (no memory I/O)              ./practice-loop-memory/<pseudonym>.json
                              │                               │
                              └───────────────┬───────────────┘
                                              ▼
                                   Gate 1 (§3.5) — nurse validates
                                              ▼
                                   Draft → verify → iterate
                                              ▼
                                   Gate 2 (§7–8) — registrant sign-off
                                              ▼
                          Step 9: audit entry → ./practice-loop-audit/
                          Step 10: WRITE trajectory entry → memory file
```

Storage is plaintext JSON on the operator's filesystem. **No transmission to CQAI at any point.**
Whether the model provider processes the *contents* of a recalled record is a separate question —
see Risk R5.

### 2.5 Purpose 🔹

To let a later session reference earlier learning gaps without the nurse re-pasting historical
notes, and to distinguish a *recurring* gap (escalate as a pattern) from a first occurrence
(address as a learning need).

---

## Step 3 — Consultation

| Party | Position |
|---|---|
| Data subjects (students/preceptees) | ⬜ **Must be consulted.** They are identifiable to the operator via the pseudonym and are the subject of an evaluative record. Transparency cannot be satisfied by the pseudonym alone |
| Practice education / university partners | ⬜ To be completed |
| Trust DPO | ⬜ Sign-off required at Step 7 |
| Student union / student representatives | ⬜ Recommended given the power imbalance (criterion 7) |
| Model provider terms | ⬜ Review the applicable enterprise terms for training/retention — see R5 |

---

## Step 4 — Necessity and proportionality

| Principle | Assessment |
|---|---|
| Lawful basis (Art. 6) | ⬜ To be determined by the controller. Public task (Art. 6(1)(e)) is the likely basis for an NHS/HEI assessment function; consent is a poor fit given the power imbalance — a student cannot freely refuse their assessor |
| Special category basis (Art. 9) | ⬜ **Required if R1 is not eliminated.** No Art. 9 condition is currently identified, and none is implied by the software |
| Purpose limitation | 🔹 Schema is purpose-specific. Risk is free-text drift in `flags` / `learning_gaps` / `custom_verifier_notes` |
| Data minimisation | 🔹 Fields are proportionate. `assessor_preferences.trust_name` is organisational and shrinks the anonymity set — see R2 |
| Accuracy | 🔹 Partly mitigated by design: recalled content is presented as *prior context to be confirmed, not established fact*, and Gate 1 puts it before a registrant. No mechanism exists to correct or delete a superseded entry — see R4 |
| Storage limitation | ⬜ **No retention period is implemented.** `trajectory[]` grows without bound and nothing expires. See R6 |
| Security | ⬜ Plaintext, unencrypted, inheriting only filesystem permissions. See R3 |

**Could the purpose be achieved less intrusively?** Partly. A per-placement record deleted at
placement end would serve the stated purpose (Month 1 → Month 3) without an indefinite
longitudinal file. The controller should consider scoping memory to a single placement.

---

## Step 5 — Risk assessment

| ID | Risk | Likelihood | Severity | Overall | 
|---|---|:---:|:---:|:---:|
| **R1** | **Special category data enters memory.** `reasonable-adjustments-passport` concerns disability and states at §17 that "Health information is special-category data" — then writes `learning_gaps` and `flags` to the same schema, which has no Art. 9 handling. Caring responsibilities, fatigue and wellbeing flags are similarly reachable from placement loops | High | High | **HIGH** |
| **R2** | **Re-identification of the pseudonym.** Pseudonym + `programme_year` + `trust_name` + dated placement trajectory is highly identifying in a cohort of a few students on one ward. The pseudonym is a **key, not anonymisation** — the file is personal data | High | Medium | **HIGH** |
| **R3** | **Unprotected storage / unintended cloud sync.** Files are plaintext JSON in the working directory, protected only by `.gitignore`, which governs git and nothing else. **Verified on the development machine: the repository sits inside OneDrive, so `practice-loop-memory/` syncs to a personal cloud account.** `practice-loop-memory/README.md`'s claim that files "exist locally only" does not hold wherever the working directory is inside OneDrive, Dropbox, or a redirected Documents folder — the common case on NHS Windows estates | High | High | **HIGH** |
| **R4** | **No rectification or erasure path.** Nothing implements Art. 16 (rectification) or Art. 17 (erasure). A student disputing a recorded gap has no route to amend it, and a wrong entry is recalled into every future session | Medium | High | **HIGH** |
| **R5** | **Recalled content is sent to the model provider.** Step 1.5 injects the record into the prompt, so history that never left disk at rest does leave it in use. Under consumer terms this may be retained or used for training | Medium | High | **HIGH** |
| **R6** | **Unbounded retention.** No expiry, no maximum trajectory length, no deletion at placement or programme end. Breaches storage limitation by default | High | Medium | **HIGH** |
| **R7** | **Function creep into assessment decisions.** Loops must not decide progression, but a longitudinal record of scores and recurring flags is exactly what a capability or FtP process would seek. Absent policy, memory becomes de facto evidence | Medium | High | **HIGH** |
| **R8** | **Data subjects unaware.** Memory is opt-in *for the nurse*, not the student. Nothing requires the student be told a record exists | High | Medium | **HIGH** |
| **R9** | **Pseudonym collision or merge.** Two people under one pseudonym, or reused pseudonyms across cohorts, contaminate records. Mitigated in instruction ("never merge two pseudonyms") but not enforced technically | Low | High | **MEDIUM** |
| **R10** | **Model misreads recalled context.** A gap recorded loosely is amplified across sessions | Medium | Medium | **MEDIUM** |

---

## Step 6 — Mitigating measures

| Risk | Measure | Status | Owner |
|---|---|:---:|---|
| R1 | Loops correctly identify health data as special category at intake and HALT | ✅ In place | Software |
| R1 | Exclude `reasonable-adjustments-passport` from memory, **or** define an Art. 9 condition and separate handling before enabling it | ⬜ To implement | Controller + CQAI |
| R1 | Constrain `flags` to a controlled vocabulary rather than free text | ⬜ To implement | CQAI |
| R2 | Pseudonym mandated; real names to be refused at intake | ✅ In place | Software |
| R2 | Treat memory files as personal data in all policies. Do not describe them as anonymised | ⬜ To implement | Controller |
| R2 | Consider dropping `trust_name` where the cohort is small | ⬜ To implement | Controller |
| R3 | `.gitignore` prevents accidental commit and publication | ✅ In place | Software |
| R3 | **Site memory outside any cloud-synced folder**, on encrypted storage (BitLocker or equivalent) | ⬜ To implement | Controller |
| R3 | Correct `practice-loop-memory/README.md`, which currently overstates locality | ⬜ To implement | CQAI |
| R4 | Recall presented as "to be confirmed"; Gate 1 puts it before a registrant | ✅ In place | Software |
| R4 | Documented rectification and erasure procedure, and a student-facing route to invoke it | ⬜ To implement | Controller |
| R5 | Enterprise/business model terms with training disabled | ⬜ To implement | Controller |
| R6 | Retention schedule — recommend scoping to a single placement and deleting at placement end | ⬜ To implement | Controller |
| R7 | Loops explicitly forbidden from progression/FtP/capability/employment decisions | ✅ In place | Software |
| R7 | Written policy that memory must not be used as evidence in capability or FtP proceedings | ⬜ To implement | Controller |
| R8 | Privacy notice to students, issued at placement induction, stating what is recorded and for how long | ⬜ To implement | Controller |
| R9 | "Never merge two pseudonyms" instruction | ✅ In place | Software |
| R9 | Documented pseudonym allocation scheme preventing reuse across cohorts | ⬜ To implement | Controller |
| R10 | Two human gates plus 10-point verifier with sub-8 iteration | ✅ In place | Software |

---

## Step 7 — Conclusion and sign-off

**Residual risk with the software as shipped and no organisational controls: HIGH.**

Seven risks are HIGH, and four of them (R1, R3, R4, R6) cannot be mitigated by the software
alone — they require organisational decisions about lawful basis, storage location, retention,
and data subject rights.

**Recommendation: do not enable cross-session memory for real learners until at least R1, R3,
R4, R6 and R8 carry completed mitigations.** Practice Loops runs fully without memory: if no
pseudonym is given, steps 1.5 and 10 are skipped and every other governance property is
retained. Statelessly is the correct default until this DPIA is completed.

**ICO prior consultation** (Art. 36) is required only if residual risk remains HIGH after all
mitigations. With the measures above implemented, residual risk is expected to fall to
LOW–MEDIUM and prior consultation should not be needed. ⬜ *Controller to confirm.*

| Role | Name | Signature | Date |
|---|---|---|---|
| Data Protection Officer | | | |
| Caldicott Guardian / Clinical Safety Officer | | | |
| Head of Practice Education | | | |
| Senior Information Risk Owner (SIRO) | | | |

**Review:** annually, or on any change to the memory schema, the set of loops that write to it,
or the storage location.

---

## Caveat

This template was generated with AI assistance against the software's actual behaviour at the
merge of PR #7. It is **not legal advice**. It identifies risks and pre-populates what is
determinable from the code; it does not substitute for review by your DPO, and the
organisational sections cannot be completed by anyone outside your organisation.
