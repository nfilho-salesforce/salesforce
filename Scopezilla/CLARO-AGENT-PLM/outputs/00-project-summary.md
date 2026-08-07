# Project Summary — CLARO Agente PLM

**Date:** 2026-06-17  
**Status:** Design · Roadmap · Efficiency complete — ready for validate/export  
**Engagement model:** T&M · Sizing: SC (Super Custom) · 8 weeks

---

## Executive Summary

Claro Brasil is implementing a native Salesforce PLM catalog validation POC to replace a legacy BRE engine with 127 hard-coded rules. The engagement deploys two Agentforce Employee Agents (PLM Admin and PLM Ops) backed by an AST Walker Apex engine and Einstein Prompt Templates, enabling self-service rule authoring without redeployment, resilient async CSV ingestion up to 10,000 lines, and autonomous batch diagnostics. The 8-week delivery runs across two Salesforce orgs (STORM_PLM and Ibuy) under a T&M model, with Claro funding a dedicated PM provided by Salesforce PS.

---

## Company & Industry Context

- **Client:** Claro Brasil — Telecomunicações (subsidiary of América Móvil)
- **Industry:** Telecom / Communications (no Scopezilla vertical pack available; Telecom-specific context sourced from client docs)
- **Region:** Brazil (LATAM)
- **Regulatory note:** LGPD (Lei Geral de Proteção de Dados) **applies** to this engagement — data handling controls must be confirmed before go-live, even if the Demanda/Item pipeline operates primarily on product catalog data

---

## Current vs. Target Salesforce Landscape

| Dimension | Current State | Target State |
|-----------|--------------|-------------|
| Catalog engine | Legacy BRE — 127 hard-coded rules, redeploy required for any change | AST Walker Apex engine — JSON spec-driven, <50ms/record |
| Rule authoring | Manual code changes + deployment pipeline | Self-service via Agentforce PLM Admin (natural language → compiled JSON spec, no redeploy) |
| CSV ingest | Synchronous, prone to CPU/heap overflow on large volumes | Async-first Queueable chain with byte-offset cursor, up to 10k lines / 6M chars |
| Batch diagnostics | Manual | Agentforce PLM Ops: import → evaluate → HTML narrative diagnostic |
| Failure handling | Silent failures / zombie transactions | DLQ-first: Transaction Finalizers + Dead Letter Queues + ZombieReaper (100% coverage) |
| Orgs | STORM_PLM + Ibuy (no Platform Cache partitions available) | Same orgs; cache via static Maps + durable CMDTs |

---

## Project Scope

### In Scope
- **Agent 2 (PLM) only** — Agents 1 (KB), 3 (NBO), and 4 (Lead Qual) are explicitly out of scope for this engagement
- 3 product types: Fone, BL, TV
- 3 severity channels: ERRO (blocks Pre_Aprovado), AVISO, INFO
- Agentforce PLM Admin (4 topics, compile-time): compile, recompile, status
- Agentforce PLM Ops (6 topics, runtime): import CSV, evaluate, diagnose
- AST Walker engine (PlmRuleSpecEvaluator) — deterministic, no LLM at runtime
- LLM rule compilation via Einstein Prompt Template (PLM_Rule_Compiler, ConnectApi)
- HTML diagnostic narrative via Prompt Template (PLM_Diagnostico_Narrativa)
- LWC DemandaCsvWizard + plmProcessoHome + plmAvaliacaoPanel + plmRuleSpecsAdmin
- Async Queueable chain with byte-offset cursor (Plm_Csv_Import_State__c)
- Observability: Platform Events, Compile Snapshots, DLQ, Transaction Finalizers, ZombieReaper
- Permset Validacao_Engine_Access
- Decision Tables (PLM_RuleCatalog, PLM_FieldRuleMapper) + 5 Aux CMDT families (66 seed rows)

### Out of Scope
- Agents 1, 3, 4 (KB / NBO / Lead Qualification)
- Bulk API 2.0 ingest for CSVs > 6MB (backlog W3.1)
- Batchable evaluator for demands > 50k items (backlog W3.2)
- Custom Apex roll-ups for Demanda__c summary fields (backlog W3.3)
- Import-state CSV heartbeat sweep (backlog W3.5)
- Production hardening: permset split (Operator vs Admin), regex complexity caps (backlog W3.4/W3.8)
- Platform Cache (prohibited in STORM_PLM and Ibuy)
- Multi-org / managed packaging / namespace
- Cross-system integration (MuleSoft, external APIs, CDC)
- Non-Salesforce data platforms (Data Cloud, Snowflake, dbt)
- Net-new Knowledge Article creation (client responsibility)

---

## Delivery Team

| Role | Source | Notes |
|------|--------|-------|
| Project Manager | Salesforce PS — dedicated, billable (paid by Claro) | Delivery governance, client interface, gap tracking |
| Technical Architect | Salesforce PS | AST Walker, Queueables, DLQ, cross-org devops |
| Technical Consultant | Salesforce PS | Agentforce build, Prompt Templates, LWC |
| QA Consultant (1.5) | Salesforce PS | Test strategy, Parallel Run, UAT, RunSpecifiedTests |
| **Project Manager** | **Salesforce PS — billable, paid by Claro** | Delivery governance, milestone tracking |
| Lucas | Claro (SME técnico) | Key technical subject matter expert |
| Luciano | Claro (SWE lead) | SWE leadership (PM role relieved by dedicated PS PM) |
| Fabricio | Claro (Ops lead / sponsor) | Operational sponsor |

---

## Timeline

| Phase | Duration | Key Activities |
|-------|----------|---------------|
| P0 — Discovery & Architecture | Weeks 1–2 | DSL rule alignment, schema JSON definition, architecture locked, all 6 client dependencies confirmed |
| P1 — Build Sprints (S1/S2/S3) | Weeks 3–5 | S1: E01+E09 foundation · S2: E02+E03+E04 engine · S3: E05+E06+E07+E08 intelligence+UX |
| P2 — UAT & Fine-tuning | Weeks 6–7 | Stress tests (CSV 6M chars), Parallel Run vs. legacy BRE, LGPD legal sign-off, UAT acceptance |
| P3 — Deploy & Hypercare | Week 8 | Deploy via RunSpecifiedTests, Go-Live, Knowledge Transfer, formal project close |

---

## Key Technical Constraints

- **No Platform Cache** in STORM_PLM or Ibuy — cache strategy: static Maps → durable Plm_Rule_Spec__c → SOQL on Spec_Key__c
- **Quick-deploy rejected** cross-org (CannotQuickDeployError) — all deploys via `--test-level RunSpecifiedTests`
- **Required/MD fields must not appear in permset fieldPermissions** — auto-granted via objectPermissions
- **Governor envelopes by lane:** sync 10k CPU, async 60k CPU, PE 250k/day
- Einstein Prompt Templates require `applicationName='PromptTemplateGenerationsInvocable'` in all `generateMessagesForPromptTemplate` calls

---

## Risks & Open Questions

| Priority | Risk | Status |
|----------|------|--------|
| High | NBO external system API docs not confirmed (Agent 3 — conditional) | **Out of scope** for this POC; de-risked |
| High | CSV volumetry: heap overflow risk for batches >50k items | Mitigated by async Queueable chain; >50k Batchable in backlog (W3.2) |
| High | STORM_PLM / Ibuy concurrency windows — maintenance and batch lock policies unknown | **Open** — client must confirm before build starts |
| Medium | PM role | **Resolved** — dedicated Salesforce PS PM, billable, paid by Claro |
| Medium | Knowledge Article readiness (10–15 FAQs + Data Categories) | **Open** — client prerequisite for Week 1 |
| Medium | FLS / permset security model for Agentforce Ops reports | Open — confirm field-level visibility restrictions with Claro security team |
| Medium | **LGPD compliance** | **Open — CONFIRMED APPLIES.** Data handling controls required before go-live; Claro legal/compliance must clarify scope of personal data in the pipeline |
| Low | Budget / investment ceiling | Not discussed — flag for commercial review |

---

## Data & Compliance

- **LGPD applies** — confirmed. Even if the Demanda/Item pipeline processes product catalog data (Fone/BL/TV types, not subscriber PII), Claro's broader platform context triggers LGPD obligations. Pre-go-live data handling review required.
- No HIPAA, PCI, or SOX signals in discovery material.
- Security hardening (permset split, regex caps) explicitly deferred to post-POC backlog.
- Einstein Trust Layer active — all LLM traffic (compile + diagnostic) routes through Salesforce Trust Layer; no raw data exposed to external LLM providers.

---

## Open Threads

1. **LGPD controls** — Claro legal must confirm data classification and handling obligations before go-live
2. **STORM_PLM / Ibuy concurrency windows** — batch lock and maintenance schedule needed before F1 build starts
3. **Knowledge Article readiness** — 10–15 FAQs with Data Categories required by Week 1 (client dependency)
4. **Budget / investment ceiling** — not yet discussed; needed for commercial positioning
5. **Agentforce Ops FLS scope** — field-level visibility restrictions for narrative diagnostic reports

---

## Next Steps

1. Drop USB and USD documents into `knowledge/` for downstream skill grounding *(already present)*
2. Run `strategy` to frame the business case narrative
3. Or jump to `requirements` to define the epic skeleton
