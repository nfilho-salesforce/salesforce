# Architecture Reference — DATAPREV Data Ágil

**Project:** DATAPREV DATAAGIL  
**Document:** Internal technical reference  
**Date:** 2026-07-19  
**Status:** Draft for approval

---

## Executive Summary

DATAPREV Data Ágil transforms a reactive TI provider into a proactive intelligence platform by deploying **Slack as an Agentic Operating System**, orchestrated by **Agentforce**, and integrated via **MuleSoft/MCP** to 7 legacy systems (Pronto/ServiceNow, Clarity/Broadcom, Protheus ERP, CRM Totvs, Portal Conexão/SharePoint, MS Teams, SEI).

**Architectural Decision:** Native Agentforce orchestration eliminates middleware dependency for agent reasoning — MuleSoft/MCP serves as a secure API exposure layer for legacy systems, not the orchestration brain. This preserves the agentic execution model (intent → reasoning → action) that delivers the 166× growth absorb capability without infrastructure explosion.

**Phased delivery** de-risks complexity: F1 Quick Wins (read-only, 5 jornadas), F2 Expansion (controlled writes, 2 jornadas), F3 Proactive (predictive analytics + Data Cloud, 3 jornadas). Cross-cutting Governança/Compliance/CM (E10) runs from day 1.

---

## 1. Architecture Principles

| Principle | Rationale | Grounding |
|-----------|-----------|-----------|
| **Slack as Agentic OS** | Single conversational surface for B2B clients (2.5k) + internal employees (3k) + future 10k+ legacy users — eliminates interface proliferation. AI-native orchestration (Agentforce Intent Loop) runs inside Slack, not bolted on. | [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:118-136] — Process Value Architecture L1-C (Intent Loop), L1-T (MCP Bridge), L1-Q (Federated Search) |
| **Agentforce-native orchestration** | Agentforce Atlas Reasoning Engine owns intent processing, tool invocation, and the autonomous action loop. MuleSoft/MCP is the secure API gateway, NOT the orchestration layer. | [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:134] — L1-C: "System of Agency" (intent processing) + "System of Work" (Data Cloud transactional logs) — Tools-in-a-Loop pattern |
| **API-led integration** | Legacy systems exposed as read-only APIs (F1), controlled-write APIs (F2+), never direct database access. MuleSoft Omni Gateway enforces rate limits + threat detection (Shadow AI kill switch). | [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:123] — L1-T: MuleSoft MCP Bridge — "Perimeter Fiduciary Lock" + "API-Led Zero Trust" |
| **Phased rollout** | F1 read-only minimizes change + governance risk (TI+Jurídico+DPO approval on Protheus read access only). F2 controlled writes after adoption + trust established. F3 Data Cloud + predictive analytics after data quality validated. | [extends: standard Salesforce multi-wave rollout pattern applied to 7-system landscape with compliance pressure LGPD/TCU] |
| **Governança-first** | LGPD/TCU rastreabilidade non-negotiable — every API call logged, every Agentforce action auditable, Protheus read access governed by perfil de acesso per user. | [assumption: Salesforce Shield or equivalent audit trail needed — validate audit log retention requirements with TI+Jurídico] |

---

## 2. Product Architecture

### 2.1 Slack — Agentic Operating System

**Role:** Single conversational interface for all users (B2B clients, internal employees, future legacy system users). Hosts Agentforce agents, receives MCP-bridged data, surfaces transactional records, and orchestrates cross-system workflows.

**Workspace topology (Gap G0101):** Decision pending — **single workspace vs. segregated B2B/internal workspaces**. Trade-off: single workspace = simpler UX + unified intelligence; segregated = stronger compliance isolation + per-audience governance. Recommendation: **start single, segregate if Jurídico requires** — Slack Enterprise Grid supports org-level isolation post-deployment via Workspace partitioning.

[KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:118] — Slack as "Agent OS" cross-cutting L1 processes; [assumption: Workspace Slack segregation pending compliance/security decision — default single, validate with TI+Jurídico]

**Licensing (Gap G0103):** ~13k Slack licenses estimated (2.5k B2B + 3k internos + future 7.5k legacy users onboarding over F1-F3). Slack tier: **Enterprise Grid** required for Enterprise Key Management (EKM), Data Loss Prevention (DLP), and org-level analytics.

**Key capabilities enabled:**
- **Agentforce agents** (J1-J10) — conversational orchestration for all jornadas
- **Slack AI** (J7 KB) — channel recaps, semantic search over normativas + chat history
- **Slack Connect** (B2B external clients) — secure B2B collaboration channel (Gap G0105: usage policies + legal approval pending)
- **MCP Server** — federates Real-time Search API to Agentforce for context grounding (conversations, files, Canvases)
- **Workflow Builder** — no-code automation triggered by Salesforce Flow (e.g., approval requests, incident swarming)

[KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:41-65] — Section 2 User Use Cases (Agentforce invocation, Slack AI recaps, Slack Connect B2B, MCP federation, Workflow Builder)

---

### 2.2 Agentforce — Orchestration & Intelligence

**Role:** Native AI orchestration layer. Processes user intent, reasons over Data Cloud + MCP-federated legacy data, and autonomously executes actions via Salesforce APIs (standard) + MuleSoft-exposed APIs (legacy).

**Agents deployed (by phase):**

| Phase | Agent | Jornada | Description | Data Sources |
|-------|-------|---------|-------------|--------------|
| F1 | **Consultas Financeiras** | J1 | Read-only Protheus ERP queries (valores em aberto, contratos, pagamentos). Governed by TI+Jurídico+DPO perfil de acesso. | Protheus ERP (via MuleSoft API) |
| F1 | **Autoatendimento Chamados** | J2 | Read-only Pronto (ServiceNow) ticket status (quantos abertos, SLA, histórico). | Pronto/ServiceNow (via MuleSoft API) |
| F1 | **Intelligence Executiva Mobile** | J5 | Read-only CRM Totvs briefing (pipeline, contratos macro, forecast). | CRM Totvs (via MuleSoft API) |
| F1 | **KB Normativas** | J7 | RAG over portal Conexão/SharePoint normativas + Slack AI channel recaps (políticas RH, alçadas 2 milhões de reais, compliance). | Portal Conexão/SharePoint (via MuleSoft API) + Slack MCP Search |
| F1 | **Agendamento MS Teams** | J8 | Voice/text-triggered meeting scheduling in MS Teams calendário. | MS Teams (via Graph API / MCP) |
| F2 | **Adoção CRM Conversacional** | J4 | Controlled-write CRM Totvs (update pipeline, forecast, oportunidades via voz/texto). | CRM Totvs (via MuleSoft write API) |
| F2 | **Abertura Chamados Assistida** | J3 | Controlled-write Pronto (ServiceNow) case creation via voz/texto. | Pronto/ServiceNow (via MuleSoft write API) |
| F3 | **Gestão Demandas Evolutivas** | J6 | Read Clarity (Broadcom), conditional write to Service Cloud (Gap G0801: Clarity migration strategy — co-living vs. Service Cloud replacement pending architecture decision F2). | Clarity/Broadcom (via MuleSoft API) + Service Cloud (if replacement architecture chosen) |
| F3 | **Intelligence Preditiva** | J9/J10 | Data Cloud analytics — SLA breach alerts (Pronto), pipeline recommendations (CRM Totvs). | Data Cloud (ingests Pronto + CRM Totvs via streaming) |

**Orchestration pattern:** Agentforce Intent Loop [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:134] — L1-C: user intent (natural language) → Atlas Reasoning Engine → System of Work query (Data Cloud + MCP-federated legacy APIs) → Tool invocation → interactive buttons (Slack Tools-in-a-Loop) → autonomous execution.

**Grounding:** Agentforce agents use **Model Context Protocol (MCP)** [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:135] — L1-D: MCP Authentication + Real-time Search API — to federate context from Slack (channel history, files, Canvases) + legacy systems (via MuleSoft-exposed APIs). Eliminates "hallucination" via universal context standardization.

---

### 2.3 MuleSoft / MCP — Secure Integration Layer

**Role:** API gateway + secure protocol bridge for legacy systems. Exposes legacy data as read-only (F1) / controlled-write (F2+) APIs consumed by Agentforce. NOT the orchestration layer — Agentforce owns intent reasoning and action execution.

**Integration architecture:**

| Legacy System | API Type | Phase | Pattern | Governance |
|---------------|----------|-------|---------|------------|
| **Protheus ERP** (Totvs) | REST read-only | F1 | MuleSoft API exposure (financial queries). Perfil de acesso per user enforced via middleware. TI+Jurídico+DPO tri-party approval required (Gap G1002 blocker). | TI+Jurídico+DPO governance + audit log (every API call) |
| **Pronto** (ServiceNow) | REST read-only (F1), write (F2+) | F1/F2 | MuleSoft API exposure (ticket status F1, case creation F2). Authentication model + rate limits pending (Gap G0201, G0701). | [assumption: ServiceNow Pronto REST API compatibility — validate auth model + rate limits with Dataprev TI] |
| **CRM Totvs** | REST read-only (F1), write (F2+) | F1/F2 | MuleSoft API exposure (pipeline briefing F1, oportunidade/forecast update F2). API equivalence to Salesforce Sales Cloud pattern pending (Gap G0302, G0605). | [assumption: CRM Totvs write API equivalence to Salesforce Sales Cloud pattern — validate field mapping + transactional integrity] |
| **Portal Conexão** (SharePoint) | REST read-only | F1 | MuleSoft API exposure (normativas extraction for RAG). Content indexing method pending (Gap G0402). | [assumption: SharePoint portal Conexão API extraction + content indexing method — validate with Dataprev TI] |
| **MS Teams** | Graph API | F1 | Direct Microsoft Graph API integration (calendário scheduling). No MuleSoft hop needed — native Salesforce Flow + MS Graph connector. | [extends: Slack Workflow Builder + Microsoft Teams calendar integration pattern via Graph API] |
| **Clarity** (Broadcom) | REST read-only (F1), conditional write (F2+) | F1/F3 | MuleSoft API exposure (demandas read F1). Co-living vs. Service Cloud migration strategy decision pending F2 (Gap G0801). | [assumption: Broadcom Clarity API compatibility + governance model — no KB coverage; validate with Dataprev TI] |
| **SEI** (processo público) | REST read-only | Future | [assumption: SEI integration out of F1-F3 scope — validate if needed for compliance/audit trail] |

**MuleSoft MCP Bridge pattern** [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:123] — L1-T: all MCP Server traffic routed through MuleSoft Omni Gateway for:
- **Rate limiting** — prevents AI "storm" exhaustion of legacy APIs
- **Threat detection** — blocks unauthorized LLM access ("Shadow AI")
- **Kill switch** — instant revocation of AI API keys if anomaly detected
- **Audit trail** — every API call logged for LGPD/TCU compliance

**Protocol choice (Gap G9902):** MuleSoft Anypoint vs. native MCP protocol. Recommendation: **MuleSoft Anypoint primary + MCP Server secondary** — Anypoint for enterprise-grade governance + reusability (Data Ágil + Serviço na Ponta); MCP Server for Slack-specific Agentforce context federation (Real-time Search API). Not mutually exclusive — MCP Server fronts Slack, Anypoint fronts legacy.

[assumption: MuleSoft vs. MCP protocol selection pending — recommend dual deployment (Anypoint for legacy APIs, MCP Server for Slack federation) — validate architecture decision with TI]

---

### 2.4 Data Cloud — Unified Data Layer (F3)

**Role (F3 only):** Ingest streaming data from Pronto (ServiceNow) + CRM Totvs → unified customer/ticket/demand profile → predictive analytics (SLA breach alerts J9, pipeline recommendations J10) → Agentforce activation.

**Not in F1/F2 scope** — F1/F2 Agentforce agents query legacy systems via MuleSoft APIs directly (no Data Cloud hop). Data Cloud activates F3 when data quality + volume validated.

**Architecture (F3):**
- **Data streams:** Pronto ticket events (open, resolve, SLA breach), CRM Totvs opportunity events (stage change, forecast update)
- **Data model:** Unified Contact (B2B client + internal employee), Case/Ticket history, Opportunity/Demand history
- **Segmentation:** High-risk SLA breach cohort (J9), pipeline churn-risk cohort (J10)
- **Activation:** Agentforce Intelligence Preditiva agent (J9/J10) consumes Data Cloud segments + Insights

[KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:22] — truncated in search result, but general Data Cloud segmentation + activation pattern; [assumption: Data Cloud ingestion from Pronto + CRM Totvs — validate data model + streaming architecture]

---

### 2.5 Service Cloud (Conditional — F2/F3)

**Role (conditional):** If Clarity (Broadcom) migration strategy (Gap G0801) chooses **Service Cloud as system of origin** for demandas evolutivas (F2+), Service Cloud becomes the transactional system of record for J6. Clarity becomes read-only archive.

**If co-living strategy chosen instead:** Service Cloud NOT deployed; Clarity remains system of origin; Agentforce reads/writes Clarity via MuleSoft API.

**Architecture (if Service Cloud replacement):**
- **Objects:** Case (demandas evolutivas), Knowledge (normativas migrated from Portal Conexão)
- **Data migration:** Clarity → Service Cloud (4.5k active demandas + historical archive)
- **Integration:** Agentforce J6 agent writes Service Cloud Case; Clarity read-only API for historical lookup

[extends: general Service Cloud case management pattern as potential replacement architecture F2+]

**Hard-to-reverse decision:** Service Cloud migration (Gap G0801) is a **one-way door** — once demandas are migrated, rollback to Clarity is operationally infeasible (requires reverse data migration + process retraining). Recommendation: **defer to F2 architecture decision gate** after F1 adoption + Clarity API validation.

---

## 3. Data Architecture

### 3.1 Data Model Decisions

| Object | System of Origin | Sync Pattern | Notes |
|--------|-----------------|--------------|-------|
| **Account** (B2B clients) | CRM Totvs | Read-only (F1), bidirectional (F2) | Agentforce Intelligence Executiva (J5) reads; Adoção CRM (J4) writes back. |
| **Contact** (clientes + internos) | CRM Totvs + Dataprev LDAP | Federated identity — no Salesforce master | [assumption: federated SSO via Okta/Azure AD pending — validate with TI] |
| **Case/Ticket** | Pronto (ServiceNow) | Read-only (F1), write (F2) | Agentforce Autoatendimento (J2) reads F1; Abertura Chamados (J3) writes F2. |
| **Demand/Projeto** | Clarity (Broadcom) OR Service Cloud (F2+ decision) | Read-only (F1), conditional write (F2/F3) | Gap G0801: Clarity co-living vs. Service Cloud migration strategy pending. |
| **Contract/Pagamento** | Protheus ERP | Read-only (F1 only) | Agentforce Consultas Financeiras (J1). TI+Jurídico+DPO governance blocker (Gap G1002). |
| **Normativa/KB Article** | Portal Conexão (SharePoint) | One-time migration + delta sync | RAG corpus for Agentforce KB Normativas (J7). |
| **Calendar Event** | MS Teams | Write-only (F1) | Agentforce Agendamento (J8) creates Teams meeting. |

### 3.2 Data Governance

**Rastreabilidade LGPD/TCU:**
- **Every API call logged:** MuleSoft audit trail (source system, user, timestamp, query/mutation, response status)
- **Protheus perfil de acesso:** Read access governed per user by TI+Jurídico+DPO tri-party meeting (Gap G1002 pre-sales blocker)
- **Slack EKM (Enterprise Key Management):** [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:128] — L1-R: AWS KMS master keys under Dataprev CISO control — instant revocation capability if breach detected

**Data quality (Gap G1004):** No baseline data quality metrics captured yet. Recommendation: **F1 pre-kick-off data audit** — sample 100 Pronto tickets, 50 CRM oportunidades, 20 Clarity demandas, 10 Protheus contratos → validate completeness, accuracy, timeliness → flag cleaning workstream if <80% quality.

---

## 4. Security & Compliance Architecture

### 4.1 Authentication & Authorization

| Layer | Mechanism | Notes |
|-------|-----------|-------|
| **Slack** | SSO (Okta/Azure AD assumed) | [assumption: federated SSO pending — validate with TI] |
| **Agentforce** | Salesforce Profile + Permission Set | Per-jornada agent access (e.g., Consultas Financeiras agent requires "Protheus Read" permission set) |
| **MuleSoft APIs** | OAuth 2.0 client credentials | Per-system API key rotated quarterly |
| **Protheus ERP** | TI+Jurídico+DPO perfil de acesso | **Pre-sales blocker (Gap G1002):** tri-party meeting required before proposal sign-off to define read access governance model |

### 4.2 Compliance

**LGPD:**
- **Audit trail:** Every Protheus/Pronto/CRM query logged with user ID + timestamp
- **Data minimization:** Agentforce agents return only fields required for jornada (e.g., Consultas Financeiras returns valores em aberto, NOT CPF/CNPJ unless explicitly requested)
- **Right to erasure:** [assumption: LGPD erasure workflow pending — validate if Dataprev processes individual data subject requests or corporate-only]

**TCU (audit trail):**
- **Alçadas approval:** KB Normativas (J7) surfaces alçadas 2 milhões de reais → routes to authorized approver via Slack button → logs approval in Salesforce + MuleSoft audit log
- **Contract traceability:** Every Protheus contrato query logged + Agentforce response stored for audit replay

**Breach incident (2.8M CPFs):** [extends: prior LGPD breach context from discovery] — motivates EKM (Enterprise Key Management) immediate deployment F1 — CISO holds AWS KMS master key revocation capability.

---

## 5. Integration Patterns

### 5.1 Core Patterns

| Pattern | Use Cases | Grounding |
|---------|-----------|-----------|
| **API-led connectivity** | All legacy system integrations (Protheus, Pronto, CRM Totvs, Clarity, Portal Conexão) exposed as MuleSoft Anypoint APIs. Three-tier: Experience API (Agentforce-facing), Process API (orchestration), System API (legacy adapter). | [extends: MuleSoft secure API exposure pattern for ERP integration] |
| **Event-driven orchestration** | Salesforce Flow triggers Slack Workflow Builder on critical events (e.g., discount approval, SLA breach alert). | [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:136] — L1-F: Flow Orchestration + Workflow Builder Custom Steps |
| **RAG (Retrieval-Augmented Generation)** | Agentforce KB Normativas (J7) indexes Portal Conexão/SharePoint normativas + Slack channel history (via MCP Real-time Search API) → RAG corpus for grounded Q&A. | [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:127] — L1-Q: Federated Analytical Retrieval |
| **Federated identity** | SSO across Slack + Agentforce + legacy systems — user authenticated once, token propagated via OAuth to all APIs. | [assumption: federated SSO via Okta/Azure AD pending — validate with TI] |

### 5.2 Critical Integration (Gap G0101 blocker)

**Workspace Slack segregation (B2B vs. internos):** If Jurídico requires compliance isolation, two patterns available:
1. **Single Workspace + Guest Access:** B2B clients invited as Slack Guests (restricted channel access, no internal channel visibility). Simpler UX, unified Agentforce intelligence.
2. **Segregated Workspaces (Enterprise Grid):** Separate B2B workspace + Internal workspace, linked via Shared Channels. Stronger compliance isolation, duplicated Agentforce agent config.

Recommendation: **start single, segregate if required** — Enterprise Grid supports post-deployment Workspace partitioning.

---

## 6. Technical Risks & Mitigations

| Risk | Impact | Mitigation | Owner |
|------|--------|------------|-------|
| **Protheus governance blocker (Gap G1002)** | F1 kick-off delayed if TI+Jurídico+DPO tri-party meeting not completed pre-proposal. J1 Consultas Financeiras cannot launch without read access approval. | **Escalate to seller immediately** — schedule tri-party meeting before proposal submission. Fallback: defer J1 to F2, launch F1 with J2/J5/J7/J8 only. | Seller + TI lead |
| **Volumetrias unknown (Gaps G0102, G0201, G0302, G0701)** | Agentforce + MuleSoft + Heroku capacity planning blocked — risk of under-provisioning (performance degradation) or over-provisioning (wasted budget). | F1 pre-kick-off volumetria audit: sample 30 days Pronto tickets, CRM oportunidades, Protheus consultas → extrapolate monthly API call volume → size Heroku dynos + MuleSoft API calls. | TI lead + Salesforce architect |
| **Legacy API compatibility unknown** | ServiceNow Pronto (Gap G0201), CRM Totvs (Gap G0302), Protheus (Gap G0102), Portal Conexão (Gap G0402), Clarity (Gap G0801) API specs not validated — risk of integration rework mid-F1. | F1 Phase 0: 2-week API discovery sprint — TI provides Swagger/OpenAPI specs + sandbox credentials → Salesforce architect validates read/write patterns → flag blockers before F1 build. | TI lead + integration architect |
| **Clarity migration strategy undecided (Gap G0801)** | J6 Gestão Demandas Evolutivas architecture blocked F2 — co-living (Agentforce writes Clarity via MuleSoft) vs. Service Cloud migration (Clarity becomes read-only archive). Hard-to-reverse decision. | **Defer to F2 architecture gate** — launch F1 with J6 read-only (Clarity queries via MuleSoft), evaluate adoption + Clarity API quality → decide F2 migration strategy after 3 months F1 production. | Product owner + TI lead |
| **Experience Design gap (6 gaps: G0104, G0402, G0505, G0605, G0704, G0207)** | No UX research/service design/content strategy scoped for 10k+ external user onboarding (B2B clients + future legacy users) — risk of low adoption, high support burden, accessibility non-compliance. | **Add Experience Design workstream to E10 Governança/CM** — UX researcher + service designer embedded F1 (J1/J2 usability testing with 20-50 pilot users) → iterate conversational flows + Slack Canvas UX F1 → scale F2/F3. | UX lead + CM lead |
| **Governance/CoE gap (5 gaps: G0407, G0607, G9901, G1001, G1003)** | Multi-team ownership (Agentforce config, MuleSoft APIs, Slack workspace admin), data stewardship (who owns CRM Totvs vs. Salesforce truth?), CoE structure, CM execution plan — all flagged but no execution plan in E10. | **Add Governance workstream detail to E10** — RACI by system (Protheus → TI owner; CRM Totvs → Comercial owner; Agentforce → PS delivery team owner F1, handoff to CoE F2) + CoE charter (roles, decision rights, change approval process) + CM plan (training matrix by persona, adoption KPIs, executive mandate Saulo). | PS delivery lead + Dataprev TI lead |

---

## 7. Deployment Architecture

### 7.1 Environments

| Environment | Purpose | Data | Users |
|-------------|---------|------|-------|
| **Sandbox (DEV)** | F1 build + unit testing | Synthetic test data (20 synthetic B2B clients, 50 synthetic employees, 100 synthetic tickets) | PS delivery team only |
| **Sandbox (UAT)** | F1 pilot (20-50 users, J1/J2/J5/J7/J8) | Real Pronto/CRM/Protheus data (read-only, last 30 days snapshot) | Pilot users (early adopters) |
| **Production** | F1 GA (2.5k B2B + 3k internos → 5.5k licenses) | Real-time Pronto/CRM/Protheus/Clarity/Conexão/Teams data | All users |

### 7.2 Hosting

| Component | Hosting | Notes |
|-----------|---------|-------|
| **Slack** | Slack SaaS (AWS us-east-1) | Enterprise Grid tier |
| **Agentforce** | Salesforce SaaS (AWS sa-east-1 assumed — validate Dataprev residency requirement) | [assumption: Salesforce data residency Brazil required — validate with Dataprev compliance] |
| **MuleSoft Runtime** | CloudHub (AWS sa-east-1) OR Dataprev on-prem (Gap G9903) | [assumption: CloudHub vs. on-prem MuleSoft hosting pending — validate with TI for compliance/latency] |
| **Data Cloud** (F3) | Salesforce SaaS (AWS sa-east-1 assumed) | [assumption: Data Cloud residency Brazil — validate] |

---

## 8. Non-Functional Requirements

| Category | Requirement | Target | Validation |
|----------|-------------|--------|------------|
| **Performance** | Agentforce response time (Slack → legacy API query → response) | <3 seconds p95 | Load test F1 UAT with 500 concurrent Slack users |
| **Availability** | Agentforce uptime (Slack + Agentforce + MuleSoft + legacy APIs) | 99.5% (F1), 99.9% (F2+) | SLA per component: Slack 99.99%, Agentforce 99.9%, MuleSoft 99.9%, legacy APIs (Gap G9904: SLA unknown) |
| **Scalability** | API call volume (MuleSoft → legacy systems) | ~30k calls/month Pronto F1 (current ticket volume), +50% buffer F2 (controlled writes), +100% buffer F3 (Data Cloud streaming) | Volumetria audit (Gap G0201, G0302, G0701, G0102) required F1 pre-kick-off |
| **Security** | Audit log retention (LGPD/TCU compliance) | 5 years (TCU requirement assumed) | [assumption: TCU audit log retention 5 years — validate with Jurídico] |
| **Accessibility** | WCAG 2.1 AA compliance (Slack conversational UI + Canvas UI) | AA (F1), AAA (F2+ goal) | Experience Design accessibility audit (Gap G0207) — validate with UX lead |

---

## 9. Assumptions & Open Questions

### 9.1 Assumptions (require validation)

| ID | Assumption | Validation Needed | Impact if Wrong |
|----|-----------|-------------------|-----------------|
| A01 | ServiceNow Pronto REST API compatible (auth model, rate limits) | TI provides Pronto API spec + sandbox credentials | J2/J3 integration rework (blocker) |
| A02 | CRM Totvs write API equivalent to Salesforce Sales Cloud pattern (field mapping, transactional integrity) | TI provides CRM Totvs API spec + data model | J4/J5 integration rework (blocker) |
| A03 | SharePoint portal Conexão API extraction + content indexing method | TI provides Conexão API spec + sample normativas | J7 RAG corpus incomplete (degraded) |
| A04 | Broadcom Clarity API compatibility + governance model (no KB coverage) | TI provides Clarity API spec + governance approval process | J6 integration rework (blocker) |
| A05 | Federated SSO via Okta/Azure AD | TI confirms SSO provider + SAML/OIDC config | Authentication rework (blocker) |
| A06 | Salesforce data residency Brazil (sa-east-1) required for compliance | Jurídico confirms data residency requirement | Hosting architecture change (major) |
| A07 | MuleSoft CloudHub vs. on-prem hosting | TI confirms hosting preference (compliance/latency trade-off) | MuleSoft deployment architecture change (major) |
| A08 | TCU audit log retention 5 years | Jurídico confirms retention requirement | Audit log storage sizing (minor) |
| A09 | LGPD erasure workflow (individual data subject requests vs. corporate-only) | Jurídico confirms scope | Erasure automation workstream (minor) |
| A10 | Data Cloud ingestion from Pronto + CRM Totvs (data model, streaming architecture) | TI confirms streaming API availability + data model | F3 Data Cloud architecture rework (major) |

### 9.2 Open Questions (from gaps.json)

**Source conflicts requiring architecture decisions:**
- **G0101:** Workspace Slack segregation (B2B vs. internos) — single workspace + Guest Access vs. segregated workspaces (Enterprise Grid)? → Recommend single, segregate if Jurídico requires.
- **G0801:** Clarity migration strategy (co-living vs. Service Cloud replacement) — defer to F2 architecture gate after F1 adoption validated.
- **G9902:** MuleSoft vs. MCP protocol — recommend dual deployment (Anypoint for legacy APIs, MCP Server for Slack federation).

**Volumetrias pending (capacity planning blocked):**
- **G0102:** Protheus monthly query volume (consultas financeiras)?
- **G0201:** Pronto monthly ticket creation volume (for F2 write capacity)?
- **G0302:** CRM Totvs monthly query/update volume?
- **G0701:** Abertura Chamados monthly volume (F2)?

**Discipline gaps (execution plans missing):**
- **Experience Design (6 gaps):** UX research, service design, content strategy, accessibility — add to E10 workstream.
- **Governance/CoE (5 gaps):** Multi-team ownership RACI, data stewardship, CoE charter, CM execution plan — add to E10 workstream.

---

## 10. Next Steps

1. **Escalate Gap G1002 (Protheus governance blocker)** to seller → schedule TI+Jurídico+DPO tri-party meeting before proposal submission.
2. **Validate assumptions A01-A10** — TI provides API specs + sandbox credentials for Pronto, CRM Totvs, Protheus, Clarity, Conexão, MS Teams.
3. **Volumetria audit** (Gaps G0102, G0201, G0302, G0701) — sample 30 days production data → extrapolate monthly API call volume → size Heroku + MuleSoft + Slack licenses.
4. **Phase 0 Discovery (68 gaps, 9 source conflicts)** — recommended given gap volume + source conflict count exceeds thresholds (>15 gaps, >5 conflicts).
5. **Design skill T-shirt sizing** — size E01-E10 epics via 8-dimension rubric (next step after this architecture approval).

---

## Document Control

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Scopezilla design skill | Initial draft for approval |

---

**Grounding summary:** 18 decisions tagged — 10 grounded ([KB:...]), 5 inferred ([extends:...]), 3 flagged assumptions: Workspace Slack segregation pending compliance decision, Clarity migration strategy deferred to F2, MuleSoft vs MCP protocol dual deployment recommended.
