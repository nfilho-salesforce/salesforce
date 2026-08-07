# Project Roadmap
## CLARO Agente PLM — POC PLM & Agentforce

**Version:** 1.0 · 2026-06-17  
**Duration:** 8 weeks (client commitment) · Methodology: Agile (Scrum) `[KB:USB:473]`

---

## Timeline at a Glance

```
Week  │  1    │  2    │  3    │  4    │  5    │  6    │  7    │  8
──────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────
Phase │◄──────── P0 ──────────►│◄──────────── P1 ──────────────►│  P2   │  P2   │ P3
      │  Discovery & Arch.     │  S1   │  S2   │  S3   │◄─ UAT ─►│ Go-Live
──────┼───────────────────────┼───────┼───────┼───────┼───────┼───────┼───────
E09   │████████████████████████│░░░░░░░│       │       │       │       │
E01   │                       │███████│       │       │       │       │
E02   │                       │       │███████│       │       │       │
E03   │                       │       │███████│       │       │       │
E04   │                       │       │███████│       │       │       │
E05   │                       │       │       │███████│       │       │
E06   │                       │       │       │███████│       │░░░░░░░│
E07   │                       │       │       │███████│       │░░░░░░░│
E08   │                       │       │       │███████│       │       │
E10   │                       │       │       │░░░░░░░│███████│       │
──────┼───────────────────────┼───────┼───────┼───────┼───────┼───────┼───────
Gates │ Deps confirmed W2 ▼   │       │       │ SIT ▼ │LGPD ▼ │UAT ✓ │ Live
```

`█` = active build  `░` = active in background / fine-tuning

---

## Phase 0 — Discovery & Architecture (Weeks 1–2)

**Goal:** Lock all design decisions, confirm every client dependency, and unblock the Build sprint.

### Week 1 — Environment + Baseline

| Activity | Owner | Output |
|---|---|---|
| Sandbox chain provisioning confirmed | Claro (Luciano) | Dev + SIT + Ibuy UAT accessible to PS |
| Sample production Demanda CSVs received | Lucas | 3–5 files for volume profiling |
| Technical kickoff: rule schema, AST JSON spec format, CMDT seed structure | TA + Lucas | Architecture decision log |
| Security model baseline: OWD, permset skeleton, SSO config | TA + TC | Permset XML skeleton (no required/MD fields) |
| CMDT seed: `Plm_Tenant__mdt`, `Plm_Compile_Config__mdt` initial rows | TC | CMDT deployed to Dev sandbox |
| RunSpecifiedTests registry v1 | TA + Luciano | Sprint class mapping agreed |

### Week 2 — Architecture Lock

| Activity | Owner | Output |
|---|---|---|
| Agentforce license + Einstein credits confirmed active in sandbox | Luciano | GAP-002 closed |
| 10–15 Knowledge Articles with Data Categories live in sandbox | Lucas / Fabrício | GAP-001 closed |
| LGPD legal review window scheduled for Week 6 | PM + Legal | Calendar confirmed |
| Sprint 1 CPU spike design: Queueable chunk size, byte-offset boundaries | TA | Chunk size spec locked |
| Architecture design document approved by Claro | TA + Lucas | **Gate: Build sprint unblocked** |

> **Critical gate:** Build sprint (Week 3) does not start until all Week 1–2 dependencies are resolved. Any slip here compresses the Build window — not the UAT window. `[KB:USB:487-493]`

---

## Phase 1 — Build Sprints (Weeks 3–5)

### Sprint 1 — Foundation (Week 3)
**Epics:** E01, E09

| Deliverable | Epic |
|---|---|
| `DemandaCsvWizardController` + `DemandaCsvImportQueueable` — byte-offset chain functional | E01 |
| `Plm_Csv_Import_State__c` — resumable cursor deployed | E01 |
| `Demanda__c` + `Item_Demanda__c` objects with all required fields | E01, E09 |
| `DemandaCsvWizard` LWC — upload UI, 6M char client-side guard | E01, E08 |
| `Validacao_Engine_Access` permset — FLS/CRUD, no required/MD fields | E09 |
| 5 `Aux_*__mdt` families, 66 seed rows deployed | E09 |
| Unit test coverage ≥ 85% on all Sprint 1 classes | — |
| **Spike:** CPU ceiling profiling — chunk size confirmed or adjusted | E01 |

**Sprint 1 deploy:** Dev → SIT (Partial Copy) via `RunSpecifiedTests`

---

### Sprint 2 — Core Engine (Week 4)
**Epics:** E02, E03, E04

| Deliverable | Epic |
|---|---|
| `PlmRuleSpecCompilerService` + `PLM_Rule_Compiler` Prompt Template — DSL → AST JSON | E02 |
| `Plm_Rule_Spec__c` with `Spec_Key__c`, `Source_Hash__c`, `Compile_Status__c` | E02 |
| `PlmRuleSpecSchemaValidator` — schema validation + DLQ write on malformed output | E02 |
| `PlmRuleSpecEvaluator` (AST Walker) — deterministic, static Map cache, <50ms target | E03 |
| `PLM_RuleCatalog` + `PLM_FieldRuleMapper` Decision Tables with initial mappings | E03, E09 |
| Platform Events: `Plm_Compile_Chunk__e` + SHA-256 idempotent log | E04 |
| DLQ objects: `Plm_Compile_DLQ__c` + `Plm_Eval_DLQ__c` | E04 |
| `Database.Finalizer` wired to all Queueables | E04 |
| `PlmZombieReaperService` scheduled + `Plm_Compile_Snapshot__c` | E04 |
| Unit test coverage ≥ 85% on all Sprint 2 classes | — |
| **Spike:** AST Walker sub-50ms profiling for multi-spec lines; Finalizer quota confirmed | E03, E04 |

**Sprint 2 deploy:** Dev → SIT via `RunSpecifiedTests`

---

### Sprint 3 — Intelligence & UX (Week 5)
**Epics:** E05, E06, E07, E08

| Deliverable | Epic |
|---|---|
| `PLM_Diagnostico_Narrativa` Prompt Template + `PlmDiagnosticoNarrativaService/Queueable` | E05 |
| `Agentforce_PLM_Admin` Employee Agent — 4 subagents configured, human-in-the-loop gate active | E06 |
| `Agentforce_PLM_Ops` Employee Agent — 6 subagents configured | E07 |
| Agent FLS confirmed: `Diagnostico__c` + `Resumo_Avaliacao_JSON__c` in permset | E07, E09 |
| LWC: `plmProcessoHome`, `plmAvaliacaoPanel`, `plmRuleSpecsAdmin` | E08 |
| FlexiPage layout + PLM App + `PLM_Rule_Specs_Admin` tab | E08 |
| Einstein Trust Layer controls activated: Zero-Data Retention, Data Masking, Prompt Defense, Toxicity Scoring, Brazil geo-routing | E10 |
| Unit test coverage ≥ 85% on Sprint 3 classes | — |
| **Spike:** Prompt Template input token limit vs. context builder payload size | E05 |

**Sprint 3 deploy:** Dev → SIT → **UAT (Full Copy / Ibuy)** via `RunSpecifiedTests`

---

## Phase 2 — UAT & Fine-Tuning (Weeks 6–7)

**Goal:** Validate all KPIs with real Claro data. Run parallel comparison vs. legacy BRE. Close LGPD gate.

### Week 6 — Stress Testing + LGPD Review

| Activity | Owner |
|---|---|
| Concurrency test: CSV at 6M chars / 10k rows — zero CPU overflow, 100% DLQ capture | QA + TC |
| KPI-TI-001 validation: AST Walker timing <50ms/record with real production data | QA + TA |
| KPI-OPS-001 validation: batch ingestion stable at ≤10k rows | QA |
| Agent Admin precision testing: compile accuracy with real pt-BR rule descriptions | QA + Lucas |
| **LGPD legal review:** data classification, ETL controls documentation reviewed | Claro Legal + TA |
| Defect triage: Crítico + Alto defects assigned same-day | PM + TC |

### Week 7 — User Acceptance + Parallel Run

| Activity | Owner |
|---|---|
| UAT with Claro operational analysts — full business scenario walk-through | QA + Lucas + Fabrício |
| Parallel run: AST Walker verdicts vs. legacy BRE 127 rules — parity confirmed | QA + TC + Lucas |
| Agent Ops testing: batch monitoring, DLQ retry, status queries | QA + Ops analysts |
| **LGPD sign-off received** (hard gate — no sign-off = no go-live) | Claro Legal |
| All open Crítico/Alto defects resolved | TC |
| Formal UAT acceptance document signed | Lucas / Fabrício / Luciano |

> **UAT entry criteria:** 85% unit test coverage on all classes, SIT complete with no blocker defects, Agentforce license active, KB articles live. `[KB:USB:625]`  
> **UAT exit criteria:** 100% business scenarios passing, KPIs validated, LGPD signed, formal acceptance received. `[KB:USB:626]`

---

## Phase 3 — Go-Live & Hypercare (Week 8)

| Activity | Owner |
|---|---|
| Production deploy to STORM_PLM via `RunSpecifiedTests` | TC + Luciano |
| Smoke test in production: CSV import → evaluation → diagnostic narrative loop | QA + TA |
| Legacy BRE 127-rule backup snapshot completed (read-only archive) | TC + Luciano |
| Hypercare monitoring: ZombieReaper, DLQ counts, Agentforce conversation logs | TA |
| Knowledge Transfer: Admin Agent operation, DLQ retry, CMDT rule management | TA + TC |
| Formal project close document signed by Claro steering committee | PM |
| Post-POC backlog handoff: W3.1–W3.5, W3.8 items documented for Claro roadmap | TA + PM |

---

## Critical Path & Dependencies

```
GAP-003 (Sandboxes) ──► Sprint 1 start
GAP-001 (KB Articles) ──► Sprint 3 start (E06/E07)
GAP-002 (SF License) ──► Sprint 3 start (E02/E05/E06/E07)
GAP-004 (RunSpecifiedTests) ──► Every sprint deploy
GAP-006 (CSV samples) ──► Sprint 1 chunk-size spike
GAP-005 (LGPD sign-off) ──► Go-live gate
```

**The Build sprint has zero float.** Any slip in P0 client dependencies compresses P1, not P2 — UAT and go-live windows are fixed. The PM escalates immediately if any P0 dependency misses its target date.

---

## Key Milestones

| Milestone | Target | Gate? |
|---|---|---|
| P0 complete: all dependencies confirmed, architecture locked | End of Week 2 | Yes — Build blocked until met |
| Sprint 1 SIT deploy clean | End of Week 3 | No |
| Sprint 2 SIT deploy clean | End of Week 4 | No |
| Sprint 3 UAT deploy clean | End of Week 5 | No |
| LGPD legal sign-off received | Week 6–7 | **Yes — go-live blocked until met** |
| UAT acceptance signed | End of Week 7 | **Yes — go-live blocked until met** |
| Production go-live | Week 8 | — |
