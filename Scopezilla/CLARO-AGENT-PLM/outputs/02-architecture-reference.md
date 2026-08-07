# Architecture Reference — Internal Technical Document
## CLARO Agente PLM — POC PLM & Agentforce

**Audience:** PS Architect, Technical Consultant, QA  
**Version:** 1.0 · 2026-06-17  
**Grounding:** USB v2.0 `[KB:USB]` · USD v2.0 `[KB:USD]` · Agentforce KB Apr-2026 `[KB:agentforce:5247-5510]`

---

## 1. Architectural Principles

| # | Principle | Why it matters here |
|---|---|---|
| 1 | **AI for authoring, determinism for execution** | LLM compiles rules at author-time; AST Walker evaluates at runtime without LLM. Non-determinism is never in the validation critical path. `[KB:USB:370-384]` |
| 2 | **Async-first, DLQ-always** | Every batch runs asynchronously. No silent failures — every error lands in a Dead Letter Queue or is captured by a Transaction Finalizer. `[KB:USB:379]` |
| 3 | **Platform Cache prohibited — static Map cache required** | STORM_PLM and Ibuy orgs have an absolute ban on Platform Cache partitions. Apex static `Map<String, Object>` instances held in VM memory replace it. `[KB:USB:200-205]` · `[KB:USD:20]` |
| 4 | **Einstein Trust Layer non-negotiable** | All LLM traffic (rule compilation, diagnostic narrative) routes through ETL. Zero-Data Retention Policy active. Raw Claro pricing data never reaches an external model. `[KB:USB:379-383]` |
| 5 | **Deploy-safe security** | `fieldPermissions` XML tags must never include required fields or Master-Detail relationships. `CannotQuickDeployError` is the baseline risk; every sprint uses `RunSpecifiedTests`. `[KB:USB:409-411]` |
| 6 | **POC as platform pattern** | Every design decision must be replicable for Agents 1, 3, 4. No one-offs. `[KB:USB:375-383]` |

---

## 2. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  EXPERIENCE LAYER                                                    │
│  LWC: DemandaCsvWizard  ·  Agentforce Chat Console (Admin / Ops)    │
└──────────────┬──────────────────────────┬───────────────────────────┘
               │ Upload CSV               │ Natural-language commands
               ▼                          ▼
┌─────────────────────────┐  ┌──────────────────────────────────────┐
│  ASYNC INGESTION (E01)  │  │  AGENTFORCE AGENTS (E06 / E07)       │
│  DemandaCsvWizard       │  │  Admin Agent  →  compile-time        │
│  Controller             │  │  Ops Agent    →  runtime             │
│  Queueable chain        │  │  Atlas Reasoning Engine              │
│  byte-offset cursor     │  │  [KB:agentforce:5353-5418]           │
│  Plm_Csv_Import_State__c│  └──────────────┬───────────────────────┘
└──────────┬──────────────┘                 │ ConnectApi call
           │ trigger eval                   ▼
           │              ┌─────────────────────────────────────────┐
           │              │  LLM COMPILATION ENGINE (E02)           │
           │              │  PlmRuleSpecCompilerService             │
           │              │  PLM_Rule_Compiler Prompt Template      │
           │              │  ConnectApi.EinsteinLLM                 │
           │              │  applicationName=                       │
           │              │  'PromptTemplateGenerationsInvocable'   │
           │              │  → AST JSON → Plm_Rule_Spec__c          │
           │              │  Einstein Trust Layer  ◄── LGPD gate    │
           │              └──────────────┬──────────────────────────┘
           │                             │ compiled spec
           ▼                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  AST EVALUATION ENGINE (E03)                                     │
│  PlmRuleSpecEvaluator (pure Apex, no LLM)                        │
│  Id-cursor Queueable pagination                                  │
│  Static Map<String,Object> cache  (Platform Cache prohibited)    │
│  Decision tables: PLM_RuleCatalog · PLM_FieldRuleMapper          │
│  Verdict write: Item_Demanda__c.Avaliacao_Regras_JSON__c         │
│             and Demanda__c.Resumo_Avaliacao_JSON__c              │
│  Severity routing: ERRO / AVISO / INFO by Fone | BL | TV        │
└────────────────────────┬─────────────────────────────────────────┘
                         │ on completion
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  AI DIAGNOSTIC NARRATIVE (E05)                                  │
│  PlmDiagnosticoNarrativaContextBuilder / Service / Queueable    │
│  PLM_Diagnostico_Narrativa Prompt Template                      │
│  → HTML stored in Demanda__c.Diagnostico__c                     │
└─────────────────────────────────────────────────────────────────┘

Cross-cutting:
┌─────────────────────────────────────────────────────────────────┐
│  OBSERVABILITY + DLQ (E04)                                      │
│  Plm_Compile_Chunk__e Platform Event → SHA-256 idempotent log   │
│  Plm_Compile_DLQ__c + Plm_Eval_DLQ__c                          │
│  Database.Finalizer chain-death recovery                        │
│  PlmZombieReaperService (5-min Schedulable)                     │
└─────────────────────────────────────────────────────────────────┘

Foundation:
┌──────────────────────────────────────────────────────────────────┐
│  SECURITY + PLATFORM CONFIG (E09) · AI GOVERNANCE (E10)         │
│  Validacao_Engine_Access permset  ·  OWD: Demanda__c = Private  │
│  SSO: Okta IdP  ·  Lifecycle: SailPoint                         │
│  Einstein Trust Layer controls  ·  LGPD sign-off gate (Week 6)  │
└──────────────────────────────────────────────────────────────────┘
```

`[KB:USB:219-384]`

---

## 3. Epic-by-Epic Technical Design

### E01 — Async CSV Ingestion
**Fit:** Custom Dev  
**Key components:** `DemandaCsvWizardController`, `DemandaCsvImportQueueable`, `Plm_Csv_Import_State__c`, `DemandaCsvWizard` LWC

**Design decisions:**
- Controller reads the CSV string and splits at configurable byte-offset boundaries (tuned to stay under 60k async CPU ceiling). `[assumption: validate 60k async CPU ceiling against Apex governor docs]`
- CRLF/UTF-8 normalization happens in the controller before chunking, not inside the Queueable — keeps the async lane clean.
- `Plm_Csv_Import_State__c` holds the cursor (record ID, byte offset, chunk index) so the chain is resumable after a Finalizer event.
- Heap guard: LWC enforces a 6,000,000-character hard cap client-side before upload. `[KB:USB:375]`
- Each Queueable creates `Demanda__c` (header) and bulk-inserts `Item_Demanda__c` rows per chunk.
- Platform Cache is not used anywhere in this epic. `[KB:USD:20]`

**Risks:** Actual CSV volumes from Claro not confirmed (GAP-006). If real batches approach 50k rows, the cursor design may need Batchable fallback (scoped out per USD §5.1 as W3.2 backlog).

---

### E02 — LLM Rule Compilation Engine
**Fit:** Configuration + Custom Dev  
**Key components:** `PlmRuleSpecCompilerService`, `PlmRuleSpecSchemaValidator`, `PLM_Rule_Compiler` Prompt Template, `Plm_Rule_Spec__c`, `Source_Hash__c`, `Compile_Mode__c`

**Design decisions:**
- `ConnectApi.EinsteinLLM.generateMessages()` invoked with `applicationName = 'PromptTemplateGenerationsInvocable'`. This is the only supported pattern for server-side Prompt Template invocation from Apex. `[KB:agentforce:95930-95982]`
- Prompt Template `PLM_Rule_Compiler` is configured in Prompt Builder (no-code layer) — system prompt instructs the LLM to output strictly valid AST JSON matching the `PlmRuleSpec` schema. Few-shot examples in the template anchor the output format.
- `PlmRuleSpecSchemaValidator` validates the returned JSON against a strict Apex schema class before writing to `Plm_Rule_Spec__c`. Malformed output triggers DLQ write, not a silent failure.
- `Source_Hash__c` stores SHA-256 of the DSL source; `Spec_Key__c` is the stable identifier. Drift detection: if `Source_Hash__c` changes on re-submit, a recompile is triggered and the old spec is soft-deleted (audit trail preserved). This is the LGPD rule lineage anchor. `[KB:USB:642-646]`
- Track B Batchable mode (`Compile_Mode__c = 'Batch'`): bulk recompile of all specs when a schema change requires it — runs as `Database.Batchable` against `Plm_Rule_Spec__c` SOQL.
- `INTERNAL_ERROR` from `ConnectApi` is retried up to 3 times with exponential backoff inside the Queueable. After 3 failures the spec is written to `Plm_Compile_DLQ__c`.

**Risks:** Agentforce Unlimited license + Einstein credits must be active in sandbox before Build Week 3 (GAP-002).

---

### E03 — AST Rule Evaluation Engine
**Fit:** Custom Dev  
**Key components:** `PlmRuleSpecEvaluator`, `PlmRuleContextInvocable`, `PlmRuleContextQueueable`, Decision Tables `PLM_RuleCatalog` + `PLM_FieldRuleMapper`

**Design decisions:**
- Pure-Apex AST walker. No dynamic SOQL, no LLM, no Platform Cache. All spec nodes are loaded into a static `Map<String, Object>` at class initialization time (VM-lifetime, durable within a transaction). `[KB:USB:288-291]`
- Evaluation loop: `PlmRuleContextQueueable` paginates over `Item_Demanda__c` records using an Id cursor, passes each record to `PlmRuleSpecEvaluator.evaluate(itemId, specKey)`, writes verdict JSON back.
- **Severity routing:** Decision table `PLM_RuleCatalog` maps product type (Fone / BL / TV) → applicable spec keys. `PLM_FieldRuleMapper` maps CSV column names → `Item_Demanda__c` fields. This keeps routing logic out of code — configurable via CMDT without a deploy.
- **Verdict structure:** `{"result":"PASS|FAIL|AVISO","rules":[{"id":"R-001","verdict":"FAIL","msg":"Preço BL inválido para combo"}],...}` written to `Avaliacao_Regras_JSON__c` per item; rollup JSON to `Resumo_Avaliacao_JSON__c` on parent `Demanda__c`.
- `<50ms per record` SLA assumes single-spec evaluation in static cache. Multi-spec (combined Fone+BL+TV line) may need profiling before committing SLA in UAT. `[assumption: validate sub-50ms against Apex profiling data for multi-spec case]`

**Risks:** CPU time for full-batch evaluation at 10k records not profiled yet — add to Sprint 1 spike.

---

### E04 — Observability, Resilience & DLQ
**Fit:** Custom Dev  
**Key components:** `Plm_Compile_Chunk__e`, `Plm_Compile_Chunk_Log__c`, `Plm_Compile_Snapshot__c`, `Plm_Compile_DLQ__c`, `Plm_Eval_DLQ__c`, `Database.Finalizer`, `PlmZombieReaperService`

**Design decisions:**
- **Platform Events** (`Plm_Compile_Chunk__e`) fire on every successful Queueable chunk completion. Subscriber trigger writes to `Plm_Compile_Chunk_Log__c` with a SHA-256 idempotency token — prevents duplicate log entries on PE replay. `[assumption: PE daily limit 250k/day; validate against expected max batch volumes]`
- **Transaction Finalizer:** Each Queueable implements `Database.Finalizer`. On `FinalizerContext.getResult() == ParentJobResult.UNHANDLED_EXCEPTION` or `.LIMITS_EXCEEDED`, writes directly to `Plm_Compile_DLQ__c` (compile path) or `Plm_Eval_DLQ__c` (eval path) and re-enqueues from last good cursor. `[assumption: 1 Finalizer per Queueable — validate quota]`
- **Compile Snapshot:** On successful batch completion, `Plm_Compile_Snapshot__c` records spec key, version, source hash, timestamp, and compile user — provides LGPD-compliant rule lineage for ANATEL audit. `[KB:USB:642-646]`
- **ZombieReaper:** `PlmZombieReaperService` runs every 5 minutes via `System.schedule`. Queries `Plm_Csv_Import_State__c` and `Plm_Rule_Spec__c` for records stuck in `Processing` status with a heartbeat older than the configured timeout. Moves them to DLQ with `ZOMBIE` error code. This covers the gap between Finalizer execution and status update that can leave orphan records.
- **DLQ ops pattern:** Both DLQ objects carry `Retry_Count__c`, `Last_Error__c`, and `Next_Retry_At__c`. Ops Agent (E07) can trigger a manual retry via an Agent Action that re-enqueues the original payload.

---

### E05 — AI Diagnostic Narrative
**Fit:** Configuration + Custom Dev  
**Key components:** `PlmDiagnosticoNarrativaContextBuilder`, `PlmDiagnosticoNarrativaService`, `PlmDiagnosticoNarrativaQueueable`, `PLM_Diagnostico_Narrativa` Prompt Template, `Demanda__c.Diagnostico__c`

**Design decisions:**
- Context builder assembles a JSON context object per `Demanda__c`: total items, error/warning/info counts, top-N failed rules with product type, sample item IDs. This is the grounding payload for the Prompt Template.
- Prompt Template `PLM_Diagnostico_Narrativa` instructs the LLM to produce a structured HTML diagnostic report in pt-BR — sections: Summary, Critical Errors, Warnings, Recommendations. Response is stored in `Demanda__c.Diagnostico__c` (long text area).
- Invocation is async (separate Queueable) triggered after `PlmRuleContextQueueable` completes on a `Demanda__c`. This keeps the evaluation critical path free from LLM latency.
- All LLM calls route through Einstein Trust Layer (same ETL context as E02). `[KB:USB:379]`
- Context payload size risk: if a Demanda has thousands of failed items, the assembled JSON may exceed Prompt Template input limits. Mitigation: cap the `top-N failed rules` at 25 in the context builder. `[assumption: validate Prompt Template input token limit against context builder output size]`

---

### E06 — Agentforce PLM Admin Agent
**Fit:** Configuration  
**Key components:** `Agentforce_PLM_Admin` Agent, 4 subagents, Atlas Reasoning Engine, GenAI Plugin actions

**Design decisions:**
- **Agent type:** Employee Agent (internal users only). Deployed to Salesforce internal channels — no customer-facing surface. `[KB:agentforce:5392-5418]`
- **Atlas Reasoning Engine:** Hybrid graph-based + LLM reasoning. The Agent Router subagent classifies incoming user intent and transitions to the appropriate subagent deterministically. `[KB:agentforce:5353-5357]`
- **4 subagents (formerly "topics"):**
  1. `CompileRule` — takes natural-language rule description in pt-BR, invokes `PlmRuleSpecCompilerService` via Agent Action (Apex invocable), returns compile result.
  2. `RecompileDriftedRules` — queries `Plm_Rule_Spec__c` for specs with `Source_Hash__c` mismatch, bulk-recompiles, reports summary.
  3. `RuleStatusCheck` — retrieves compile status, version, and last snapshot for a given `Spec_Key__c`.
  4. `BulkCompile` — triggers `Compile_Mode__c = 'Batch'` batchable for full catalog recompile; returns job ID.
- **Human-in-the-loop gate:** Before any spec is written to production `Plm_Rule_Spec__c`, the agent presents the compiled AST JSON for admin review. A `Confirm` action is required before the spec is activated. This is the LGPD "supervisão humana" control. `[KB:USB:651-653]`
- **Dependency:** Requires 10–15 Knowledge Articles with correct Data Categories in the org (GAP-001). Without KB grounding, the agent's compile instructions lack context for domain-specific rule terms.

---

### E07 — Agentforce PLM Ops Agent
**Fit:** Configuration  
**Key components:** `Agentforce_PLM_Ops` Agent, 6 subagents, Atlas Reasoning Engine

**Design decisions:**
- **Agent type:** Employee Agent. Ops persona — runtime monitoring and diagnostics. `[KB:agentforce:5247-5265]`
- **6 subagents:**
  1. `TriggerCsvIngestion` — invokes `DemandaCsvImportQueueable` for a specified `Demanda__c` record.
  2. `KickoffEvaluation` — invokes `PlmRuleContextQueueable` for a specified Demanda.
  3. `GenerateDiagnostic` — invokes `PlmDiagnosticoNarrativaQueueable` for a Demanda.
  4. `CheckBatchStatus` — queries `Demanda__c` processing status, DLQ counts, and last heartbeat.
  5. `RetryDLQItem` — re-enqueues a specific `Plm_Compile_DLQ__c` or `Plm_Eval_DLQ__c` record.
  6. `SummarizeErrors` — pulls top errors from a Demanda's items and returns a narrative summary for the operator.
- **FLS open thread:** `Demanda__c.Diagnostico__c` (HTML narrative field) and `Demanda__c.Resumo_Avaliacao_JSON__c` must be explicitly included in `Validacao_Engine_Access` permset FLS. Currently unconfirmed — add to E09 permset spec.
- **No knowledge base dependency** — Ops Agent is purely data-driven (Salesforce record queries + Apex invocables). GAP-001 only blocks E06.

---

### E08 — UX & LWC Components
**Fit:** Custom Dev  
**Key components:** `plmProcessoHome`, `plmAvaliacaoPanel`, `plmRuleSpecsAdmin`, `DemandaCsvWizard`, PLM App, PLM_Rule_Specs_Admin tab, FlexiPage layout

**Design decisions:**
- `DemandaCsvWizard` LWC handles file selection, client-side 6M char guard, progress display, and upload trigger. Server-side chunking logic lives in `DemandaCsvWizardController` (E01) — LWC is presentational.
- `plmAvaliacaoPanel` reads `Demanda__c.Resumo_Avaliacao_JSON__c` and renders a severity breakdown (ERRO/AVISO/INFO counts, per-product-type breakdown). Renders `Demanda__c.Diagnostico__c` HTML narrative inline.
- `plmRuleSpecsAdmin` lists `Plm_Rule_Spec__c` records, shows compile status, drift flag, last snapshot date, and provides a "Recompile" action button that calls the Admin Agent via an Agent Action.
- No UX research in scope — Claro SME (Lucas) drives layout requirements. `[KB:USD:78-79]`
- FlexiPage layout for both Admin and Ops personas — separate page assignments via permset.

---

### E09 — Security, Access Model & Platform Configuration
**Fit:** Configuration  
**Key components:** `Validacao_Engine_Access` permset, `Plm_Tenant__mdt`, `Plm_Compile_Config__mdt`, 5 `Aux_*__mdt` families (66 seed rows), Decision Tables

**Design decisions:**
- **OWD:** `Demanda__c` = Private. `Item_Demanda__c` = Controlled by Parent (Master-Detail). No sharing rules needed — Ops persona sees their own batches only; Admin sees all via role hierarchy. `[KB:USB:407-410]`
- **Permission Set:** `Validacao_Engine_Access` grants FLS + CRUD on all PLM objects. **Critical constraint:** XML `<fieldPermissions>` must never include fields with `required=true` or Master-Detail relationship fields — this causes `CannotDeployException` in cross-org deploys. `[KB:USB:410]`
- **Async permset:** Separate permset grants `system.apex.async` permission to the integration user running Queueables — keeps async access isolated from UI user permset.
- **CMDT families:**
  - `Plm_Tenant__mdt` — per-org tunables (max chunk size, retry limits, heartbeat timeout)
  - `Plm_Compile_Config__mdt` — Prompt Template API names, ConnectApi application names
  - `PLM_RuleCatalog` — product type → spec key routing (Decision Table)
  - `PLM_FieldRuleMapper` — CSV column name → `Item_Demanda__c` field API name (Decision Table)
  - `Aux_*__mdt` (5 families, 66 seed rows) — domain reference data for rule evaluation
- **SSO / Identity:** Okta as IdP for SSO. SailPoint manages provisioning/deprovisioning lifecycle across STORM_PLM and Ibuy. `[KB:USB:640-641]`

---

### E10 — AI Governance & LGPD Compliance
**Fit:** Configuration + Custom Dev  
**Key components:** Einstein Trust Layer settings, `Spec_Key__c`, `Source_Hash__c`, `Plm_Compile_Snapshot__c`, LGPD legal sign-off

**Design decisions:**
- **Einstein Trust Layer controls to activate:** Zero-Data Retention Policy (no LLM training on Claro data), Secure Data Retrieval / Grounding, Prompt Defense (injection protection), Data Masking (mask `Preco__c` and other pricing fields in LLM context), Toxicity Scoring, Brazil geo-routing. `[KB:USB:644-654]`
- **Rule lineage:** `Spec_Key__c` (stable human-readable identifier) + `Source_Hash__c` (SHA-256 of DSL source) + `Plm_Compile_Snapshot__c` record provide an immutable, queryable audit trail. Any ANATEL Res. 680/2020 audit can reconstruct the exact rule version active at any point in time. `[KB:USB:642-646]`
- **LGPD gate:** E10 is a **hard go-live gate**. Claro legal must review data classification and sign off on ETL controls before Week 8 production deploy. The PS team activates and documents ETL controls in Build Week 5; Claro legal review window is UAT Week 6. No exception. (GAP-005)
- **Human-in-the-loop:** Admin Agent's compile confirmation step (E06) doubles as a "human approval before AI output lands in production" control — required under Claro's AI ethics policy. `[KB:USB:651]`
- Salesforce Shield (Platform Encryption + Event Monitoring) is **out of scope** for this POC per user decision. ETL controls alone are accepted as the LGPD baseline for an 8-week POC.

---

## 4. Data Model

```
Demanda__c (header)
  ├── Status__c                  (Processing / Success / Failed)
  ├── Total_Linhas__c            (number)
  ├── Resumo_Avaliacao_JSON__c   (long text — rollup verdict from E03)
  ├── Diagnostico__c             (long text / HTML — from E05)
  └── Item_Demanda__c (MD child)
        ├── Tipo_Produto__c      (Fone / BL / TV)
        ├── Avaliacao_Regras_JSON__c  (verdict per item)
        └── [CSV column fields]

Plm_Rule_Spec__c
  ├── Spec_Key__c               (stable rule identifier)
  ├── Source_Hash__c            (SHA-256 of DSL source)
  ├── Ast_Json__c               (compiled AST)
  ├── Compile_Status__c         (Draft / Active / Drifted / Archived)
  └── Compile_Mode__c           (Track A = single / Track B = Batch)

Plm_Csv_Import_State__c        (resumable cursor)
Plm_Compile_Chunk_Log__c       (Platform Event log — idempotent)
Plm_Compile_Snapshot__c        (audit trail — LGPD lineage)
Plm_Compile_DLQ__c             (failed compilation records)
Plm_Eval_DLQ__c                (failed evaluation records)
```

CMDT (no data migration):
```
Plm_Tenant__mdt · Plm_Compile_Config__mdt
PLM_RuleCatalog · PLM_FieldRuleMapper
Aux_*__mdt (5 families, 66 seed rows)
```

`[KB:USB:399-411]`

---

## 5. Integration Surface

| Integration | From | To | Direction | Trigger | Pattern |
|---|---|---|---|---|---|
| Rule Compilation | `PlmRuleSpecCompilerService` | Einstein LLM (ETL) | Bidirectional | Agent action / bulk Queueable | `ConnectApi.EinsteinLLM.generateMessages()` — native Apex, no external callout |
| Diagnostic Narrative | `PlmDiagnosticoNarrativaService` | Einstein LLM (ETL) | Bidirectional | Post-eval Queueable | Same ConnectApi pattern |
| NBO Propensity (Agent 3) | Agentforce (future) | Legacy NBO system | Outbound | On-demand (out of scope this POC) | RESTful API via Named Credentials |

**No integration work in this POC** beyond the native ConnectApi LLM calls. `[KB:USB:253-255]`

---

## 6. Deployment Strategy

**Every deploy uses `RunSpecifiedTests`** — Quick Deploy is rejected cross-org (`CannotQuickDeployError`). `[KB:USB:193-195]` `[KB:USD:84]`

| Sprint | Test class registry additions |
|---|---|
| Sprint 1 (E09 + E01 foundation) | `DemandaCsvWizardControllerTest`, `PlmCsvImportQueueableTest`, `PlmCsvImportStateTest` |
| Sprint 2 (E02 + E03) | `PlmRuleSpecCompilerServiceTest`, `PlmRuleSpecSchemaValidatorTest`, `PlmRuleSpecEvaluatorTest`, `PlmRuleContextQueueableTest` |
| Sprint 3 (E04 + E05) | `PlmObservabilityTest`, `PlmDLQTest`, `PlmZombieReaperTest`, `PlmDiagnosticoNarrativaTest` |
| Sprint 4 (E06 + E07 + E08) | `AgentActionInvocableTests` (compile, recompile, retry), `LWCController tests` |

**Apex coverage minimum:** 85% per class before SIT. `[KB:USB:625]`

**Environment chain:**
```
Developer Sandbox (STORM_PLM copy)
    → Git PR → SIT (Partial Copy) [RunSpecifiedTests]
        → UAT (Full Copy / Ibuy) [RunSpecifiedTests]
            → Production (STORM_PLM) [RunSpecifiedTests + Claro DevOps sign-off]
```

---

## 7. Open Technical Risks

| Risk | Epic | Severity | Spike needed? |
|---|---|---|---|
| 60k async CPU ceiling — Queueable chunk size not yet profiled | E01 | High | Yes — Sprint 1 |
| AST Walker sub-50ms SLA not profiled for multi-spec lines | E03 | High | Yes — Sprint 1 |
| Transaction Finalizer quota (1 per Queueable) — confirm no conflict with chained pattern | E04 | Medium | Yes — Sprint 1 |
| PE daily limit (250k/day) vs. expected batch volumes — unconfirmed | E04 | Medium | Depends on GAP-006 |
| Prompt Template input token ceiling vs. context builder payload size | E05 | Medium | Sprint 2 |
| Agentforce license + Einstein credits active in sandbox | E02, E05, E06, E07 | HIGH | GAP-002 — client action |
| Knowledge Articles not ready | E06 | HIGH | GAP-001 — client action |
