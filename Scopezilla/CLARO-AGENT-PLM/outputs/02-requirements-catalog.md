# Requirements Catalog & Gap Register
## CLARO Agente PLM — POC PLM & Agentforce

**Version:** 1.0  
**Date:** 2026-06-17  
**Grounding:** USD v2.0, USB v2.0 (see `knowledge/`)

---

## 1. Requirements Catalog

| ID | Category | Description | Fit | Salesforce Capability | Confidence |
|---|---|---|---|---|---|
| REQ-TEC-001 | TEC | Async CSV ingestion — byte-offset Queueable chain, CPU guard, up to 6M chars / 10k rows | Custom Dev | Apex Queueable + DemandaCsvWizardController | Confirmed |
| REQ-PRO-001 | TEC | Deterministic AST Walker evaluation, <50ms/record, no LLM at runtime | Custom Dev | PlmRuleSpecEvaluator (pure Apex) | Confirmed |
| REQ-TEC-002 | TEC | LLM compilation: pt-BR DSL → AST JSON via ConnectApi + Einstein Prompt Templates | Config + Custom Dev | PLM_Rule_Compiler Prompt Template + PlmRuleSpecCompilerService | Confirmed |
| REQ-TEC-003 | TEC | Observability + DLQ: Platform Events, Transaction Finalizers, ZombieReaper, Compile Snapshots | Custom Dev | Platform Events (native config) + custom DLQ objects + Finalizer wiring | Confirmed |
| REQ-BIZ-001 | BIZ | Two Agentforce Employee Agents: Admin (compile-time governance) + Ops (runtime operations) | Configuration | Agentforce Builder — Topics, Actions, Atlas Reasoning Engine | Confirmed |
| REQ-DAT-001 | DAT | 3-channel severity routing (ERRO/AVISO/INFO) keyed by product type (Fone/BL/TV) | Custom Dev | Decision Tables (PLM_RuleCatalog, PLM_FieldRuleMapper) + AST verdict write | Confirmed |
| REQ-GOV-001 | GOV | Knowledge Articles: 10–15 FAQs + Data Categories — **client dependency, Week 1** | Capability Gap | Native Service Cloud Knowledge (structure PS; content Claro's) | Confirmed |
| REQ-CON-001 | CON | No Platform Cache on STORM_PLM/Ibuy — Apex static Map cache workaround | Custom Dev | Static Map instances (in-memory, transaction-durable) | Confirmed |
| REQ-SEC-001 | SEC | Validacao_Engine_Access permset, OWD Private on Demanda__c, SSO (Okta/SailPoint) | Configuration | Permission Sets + Sharing Model + SSO IdP configuration | Confirmed |
| REQ-AI-001 | AI | Einstein Trust Layer: Zero-Data Retention, Data Masking, Toxicity Scoring, Prompt Defense | Configuration | Einstein Trust Layer (org-level controls) | Confirmed |
| REQ-LGPD-001 | GOV | LGPD: rule lineage (Spec_Key__c + Source_Hash__c), audit trail, Brazil geo-routing — legal sign-off gate | Config + Custom Dev | Platform Events log (config) + lineage fields (custom) | Confirmed |

**Fit profile summary:** 5 Custom Dev · 3 Configuration · 2 Config+Custom Dev · 1 Capability Gap  
→ Confirms **Super Custom (SC)** overall classification. `[KB:USD:232-246]`

---

## 2. Requirements → Epic Mapping

| Epic | Epic Name | Fit | Requirements Covered | Key Risk |
|---|---|---|---|---|
| E01 | Async CSV Ingestion | Custom Dev | REQ-TEC-001, REQ-CON-001 | Heap overflow >6M chars; no native fallback |
| E02 | LLM Rule Compilation Engine | Config + Custom Dev | REQ-TEC-002 | ConnectApi INTERNAL_ERROR handling; Agentforce license dep |
| E03 | AST Rule Evaluation Engine | Custom Dev | REQ-PRO-001, REQ-DAT-001, REQ-CON-001 | 50ms SLA unvalidated — `[assumption]` |
| E04 | Observability, Resilience & DLQ | Custom Dev | REQ-TEC-003 | Transaction Finalizer quota (1/Queueable); PE daily cap — `[assumption]` |
| E05 | AI Diagnostic Narrative | Config + Custom Dev | REQ-BIZ-001 | Context builder size vs. Prompt Template input limits |
| E06 | Agentforce PLM Admin Agent | Configuration | REQ-BIZ-001, REQ-TEC-002, REQ-GOV-001 | KB readiness is Week-1 hard gate (GAP-001) |
| E07 | Agentforce PLM Ops Agent | Configuration | REQ-BIZ-001 | FLS scope for diagnostic narrative fields — open thread |
| E08 | UX & LWC Components | Custom Dev | REQ-TEC-001, REQ-BIZ-001 | No UX research in scope; Claro SME drives layout |
| E09 | Security, Access Model & Platform Config | Configuration | REQ-SEC-001, REQ-CON-001 | XML tag injection prohibition on permsets — deploy risk `[KB:USB:410]` |
| E10 | AI Governance & LGPD Compliance | Config + Custom Dev | REQ-AI-001, REQ-LGPD-001 | Legal sign-off is a non-negotiable go-live gate (GAP-005) |

---

## 3. Process Hierarchy (To-Be)

```
L1: Product Lifecycle Management
├── L2: Catalog Governance
│   └── L3: Rule Creation & Maintenance
│       ├── L4: Self-Service Rule Authoring       → E06 (Admin Agent)
│       └── L4: LLM Automated Compilation         → E02 (LLM Engine)
│           └── L5: Schema Validation vs. AST JSON
└── L2: Catalog Management
    └── L3: Lifecycle Operations
        └── L4: Validação de Lotes Assíncronos    → E01 (CSV Ingest)
            ├── L4: AST Walker Evaluation         → E03 (Eval Engine)
            ├── L4: DLQ + Resilience              → E04 (Observability)
            ├── L4: HTML Diagnostic Narrative     → E05 (Diagnostic)
            └── L4: Runtime Ops Interface         → E07 (Ops Agent)
```

---

## 4. KPI Register

| KPI ID | Name | Baseline | Target | Epic | Confidence |
|---|---|---|---|---|---|
| KPI-TI-001 | Rule Evaluation Execution Time | Not measured (minutes) | <50ms/record | E03 | High |
| KPI-TI-002 | Rule Authoring & Update Time | Days (requires deploy) | 0 minutes (no redeploy) | E02, E06 | High |
| KPI-OPS-001 | Batch Ingestion Capacity | Not measured | ≤10,000 rows/batch | E01 | Medium |

---

## 5. Gap Register

| ID | Priority | Title | Affected Epics | Resolution Path |
|---|---|---|---|---|
| GAP-001 | 🔴 HIGH | Knowledge Articles not ready — client Week-1 dependency | E06, E07 | Hard gate: Build doesn't start until 10–15 FAQs are live in sandbox |
| GAP-002 | 🔴 HIGH | Agentforce Unlimited + Einstein credits not confirmed active Day 1 | E02, E05, E06, E07 | Claro confirms by end of Week 2; PS validates via ConnectApi test call |
| GAP-003 | 🔴 HIGH | Sandbox chain (Dev + SIT + UAT/Ibuy) not confirmed | All | Claro DevOps confirms + grants access by end of Week 1 |
| GAP-004 | 🔴 HIGH | RunSpecifiedTests class mapping for STORM_PLM/Ibuy not documented | All | PS + Claro DevOps produce registry in Weeks 1–2; update each sprint |
| GAP-005 | 🔴 HIGH | LGPD data classification sign-off — Claro legal review pending | E10 | PS activates ETL controls Week 5; legal review Week 6; sign-off before go-live |
| GAP-006 | 🟡 MEDIUM | CSV avg/max rows not formally confirmed — assumes 10k rows / 6M chars | E01, E03 | Lucas provides 3–5 production sample CSVs by end of Week 1 |

---

## 6. Open Threads (from Discovery + Strategy)

- STORM_PLM / Ibuy concurrency windows — confirm before Build (relates to GAP-003, GAP-004)
- Agentforce Ops FLS scope — field visibility for HTML diagnostic narrative reports (relates to E07)
- Budget / investment ceiling — not discussed
- LGPD controls — Claro legal sign-off (GAP-005)

---

*Sources: `[KB:USD]` = USD v2.0 (knowledge/USD...md) · `[KB:USB]` = USB v2.0 (knowledge/USB...md)*
