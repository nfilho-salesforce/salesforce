# Solution Brief — DATAPREV Data Ágil

**Project:** DATAPREV DATAAGIL  
**Document:** Client-facing epic-by-epic summary  
**Date:** 2026-07-19  
**Status:** Draft

---

## Executive Summary

DATAPREV Data Ágil delivers a unified conversational intelligence platform by deploying **Slack as an Agentic Operating System**, orchestrated by **Agentforce**, and integrated via **MuleSoft/MCP** to 7 existing systems (Pronto/ServiceNow, Clarity/Broadcom, Protheus ERP, CRM Totvs, Portal Conexão/SharePoint, MS Teams, SEI). This architecture eliminates interface proliferation (10+ disconnected systems today) and enables 2,500 B2B clients + 3,000 internal employees to access financial data, technical support, executive intelligence, compliance policies, and CRM updates through a single conversational surface.

**Phased delivery de-risks complexity and accelerates value:**
- **F1 Quick Wins** (read-only, 5 jornadas): immediate visibility into Protheus financials, Pronto tickets, CRM pipeline, SharePoint normativas, and Teams calendar — with zero write-back risk.
- **F2 Expansion** (controlled writes, 2 jornadas): conversational CRM updates and ticket creation after adoption trust established.
- **F3 Proactive** (predictive analytics, 3 jornadas): Data Cloud–powered SLA breach alerts and pipeline recommendations.

Cross-cutting **Governança, Compliance & Change Management** (E10) runs from day 1 — LGPD/TCU rastreabilidade mandatory, Protheus perfil de acesso governed by TI+Jurídico+DPO, and structured CM with training by persona (clientes B2B, executivos, comercial, N1/N2).

---

## 1. Consultas Financeiras Self-Service

**Business context**: B2B clients (ministérios, entes públicos) currently request financial data (valores em aberto, contratos, pagamentos) via formal ofício or phone to Dataprev N1 — slow, high-friction, scales linearly with client base (2.5k clients today, 10k+ target). Protheus ERP holds financial truth, but only Dataprev internal finance team accesses it. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:13-52]

**Solution approach**: Agentforce agent (J1) in Slack enables B2B clients to query Protheus ERP financials conversationally — *"Quais contratos estão em aberto?"* → agent returns valores em aberto + status + vencimento via MuleSoft-exposed read-only API. **Governance-first:** read access governed by TI+Jurídico+DPO perfil de acesso per user (tri-party meeting required pre-kick-off to define authorization model). Every query logged for LGPD/TCU audit trail. [extends: MuleSoft secure API exposure pattern for ERP integration]

---

## 2. Autoatendimento Chamados Técnicos

**Business context**: ~30k tickets/month in Pronto (ServiceNow), ~13-14k from INSS alone. Clients currently call N1 or send email to check ticket status (quantos abertos, SLA, histórico) — N1 team becomes human query layer, adding latency and scale constraint. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:13-52]

**Solution approach**: Agentforce agent (J2) in Slack queries Pronto (ServiceNow) read-only via MuleSoft API — clients ask *"Status dos meus chamados críticos?"* → agent returns ticket count, SLA status, resolution history. F1 read-only eliminates N1 dependency for status queries; F2+ enables ticket creation (J3 Abertura Chamados Assistida). [assumption: ServiceNow Pronto REST API compatibility — validate auth model + rate limits with Dataprev TI]

---

## 3. Intelligence Executiva Mobile

**Business context**: Executivos (e.g., Maik, other C-level) convocados a reuniões urgentes com ministérios or critical B2B clients without time to log into CRM Totvs for pipeline, contratos macro, forecast. Arrive unprepared or delay meeting to gather data. CRM Totvs adoption low (~50 active users, ~30% of comercial) — login friction high. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:13-52]

**Solution approach**: Agentforce agent (J5) in Slack delivers executive briefing on-demand via conversational query to CRM Totvs read-only API — *"Briefing sobre cliente Mega-Corp antes da reunião"* → agent returns pipeline, contratos macro, forecast, last interactions. Mobile-first (Slack mobile app) — executive gets briefing during commute, arrives pautado. [assumption: CRM Totvs API equivalence to Salesforce CRM pattern — validate integration feasibility + data model mapping]

---

## 4. Knowledge Base Normativas RH

**Business context**: Portal Conexão (SharePoint) holds internal normativas (políticas RH, delegação de competência, alçadas de aprovação 2 milhões de reais), but search is poor and employees repeatedly ask Pessoas team same questions. Risk: incorrect alçada on proposals/contratos → TCU audit exposure. ~50% of Pessoas team inquiries are repetitive (same normativa lookups). [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:29]

**Solution approach**: Agentforce agent (J7) indexes Portal Conexão/SharePoint normativas + Slack AI channel recaps into RAG corpus — employees ask *"Quem assina contratos acima de 2 milhões de reais?"* → agent returns exact alçada policy with source citation (KB article + line). Eliminates acionamentos repetitivos (-50% target F1), reduces TCU risk (correct alçada always surfaced). [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:127] — L1-Q: Federated Analytical Retrieval; [assumption: SharePoint portal Conexão API extraction + content indexing method — validate with Dataprev TI]

---

## 5. Agendamento Automatizado MS Teams

**Business context**: Employees exit meetings and forget to schedule follow-ups (common scenario: *"Pedro sai de reunião, manda áudio 'Agenda reunião amanhã com X, Y, Z', chega em casa tranquilo"*). Manual MS Teams calendar scheduling adds cognitive friction — either forget or interrupt deep work to schedule. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:31]

**Solution approach**: Agentforce agent (J8) accepts voice/text scheduling commands in Slack → creates MS Teams meeting via Microsoft Graph API — *"Agendar reunião amanhã 10h com João e Maria sobre projeto X"* → agent parses, checks availability, creates meeting, sends invites. Eliminates "não esquece, não esquece" atrito cognitivo. [extends: Slack Workflow Builder + Microsoft Teams calendar integration pattern via Graph API]

---

## 6. Adoção CRM via Conversação

**Business context**: CRM Totvs adoption low (~50 active users, ~30% of comercial). Login friction + form-filling burden → comercial avoids updating pipeline, forecast, oportunidades. Result: stale CRM data, forecast inaccuracy, executive blind spots. Target: +40% adoption F2 via conversational interface. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:23-24]

**Solution approach**: Agentforce agent (J4) enables conversational CRM updates in Slack (F2 controlled writes) — comercial says *"Oportunidade Mega-Corp avançou para proposta, valor 5 milhões de reais"* → agent updates CRM Totvs pipeline via MuleSoft write API, confirms back. Voice/text interface eliminates login + form friction. Hygiene improves → forecast accuracy improves → executive trust in CRM data restored. [assumption: CRM Totvs write API equivalence to Salesforce Sales Cloud pattern — validate field mapping + transactional integrity]

---

## 7. Abertura de Chamados Assistida

**Business context**: Ticket creation (Pronto/ServiceNow) currently requires formal ofício (B2B clients) or manual web form (internal employees) — high friction, delays incident reporting, slows resolution. F1 read-only (J2 Autoatendimento) handles status queries; F2 unlocks ticket creation. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:31]

**Solution approach**: Agentforce agent (J3) accepts voice/text ticket creation in Slack (F2 controlled writes) — *"Abrir chamado crítico: sistema X fora do ar desde 9h"* → agent validates, creates Pronto ticket via MuleSoft write API, returns ticket number + SLA. Reduces friction ofício/reunião → faster incident reporting → lower MTTR. [assumption: ServiceNow Pronto case creation API — validate authentication model + required fields]

---

## 8. Gestão de Demandas Evolutivas

**Business context**: ~4.5k active evolutionary demands in Clarity (Broadcom). Consulta + criação via web interface only — no conversational access. F1 read-only queries; F2+ decision: co-living (Agentforce writes Clarity via MuleSoft) vs. Service Cloud migration (Clarity becomes read-only archive, Service Cloud system of origin). **Hard-to-reverse decision** — defer to F2 architecture gate after F1 adoption validated. [assumption: Broadcom Clarity API compatibility + governance model — no KB coverage; validate with Dataprev TI]

**Solution approach**: Agentforce agent (J6) queries Clarity read-only (F1) — *"Status das demandas evolutivas projeto Y?"* → agent returns demand count, status, priorities. F2 architecture decision (co-living vs. Service Cloud replacement) pending. If Service Cloud chosen: demandas migrate to Service Cloud Case object (4.5k active + historical archive), Clarity becomes read-only; if co-living: Agentforce writes Clarity via MuleSoft. [extends: general Service Cloud case management pattern as potential replacement architecture F2+]

---

## 9. Intelligence Preditiva e Recomendações

**Business context**: Reactive support model today — SLA breaches discovered after the fact (Pronto tickets), pipeline churn reactive (CRM Totvs opportunities lost without early warning). No predictive analytics layer. F3 unlocks proactive intelligence via Data Cloud streaming from Pronto + CRM Totvs. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:22]

**Solution approach**: Agentforce agent (J9/J10) consumes Data Cloud segments — **J9 (SLA breach alerts):** Data Cloud ingests Pronto ticket events → identifies high-risk SLA breach cohort → Agentforce alerts N2/manager proactively in Slack before breach occurs. **J10 (pipeline recommendations):** Data Cloud ingests CRM Totvs opportunity events → identifies churn-risk cohort → Agentforce suggests next best action to comercial (*"Oportunidade X sem atividade 30 dias — agendar call?"*). Transforms reactive to proactive posture. [assumption: Data Cloud ingestion from Pronto + CRM Totvs — validate data model + streaming architecture]

---

## 10. Governança, Compliance e Change Management

**Business context**: 7 legacy systems (Pronto, Clarity, Protheus, CRM Totvs, Conexão, Teams, SEI), each with own governance model, no unified audit trail. LGPD breach incident (2.8M CPFs) motivates immediate compliance hardening. TCU audit pressure non-negotiable (federal government accountability). CM failure risk high (10k+ future users onboarding without structured training → low adoption, high support burden). [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:27, 34]

**Solution approach (cross-cutting, runs F1-F3):**

**Compliance & Governance:**
- **MuleSoft/MCP audit trail:** Every API call (Protheus, Pronto, CRM Totvs, Clarity, Conexão) logged with user ID + timestamp + query/mutation + response status → LGPD/TCU rastreabilidade. [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:123] — L1-T: MuleSoft MCP Bridge audit trail
- **Protheus perfil de acesso:** TI+Jurídico+DPO tri-party meeting (Gap G1002 blocker) defines read access governance per user before F1 kick-off — who can query which financial data.
- **Slack EKM (Enterprise Key Management):** [KB: Advanced Strategic Architecture and Value Analysis_ Slack as an Agentic Operating System (Agentic OS) & Agentforce 360.md:128] — L1-R: AWS KMS master keys under Dataprev CISO control — instant revocation capability if breach detected. Motivated by prior 2.8M CPF breach.

**Change Management:**
- **Training by persona:** B2B clients (J1 Consultas Financeiras), executivos (J5 Intelligence Executiva), comercial (J4/J6 CRM + demandas), N1/N2 (J2/J3 chamados). Formal training sessions F1, early adopters (20-50 pilot users) → scale F2/F3.
- **Executive mandate:** Saulo (executive sponsor) enforces adoption KPIs (>60% uso semanal target F2).
- **Arquitetura reutilizável:** Data Ágil architecture + Serviço na Ponta (parallel reuse) amortizes delivery cost across programs.

**Risks flagged:** 
- **Experience Design gap (6 gaps):** No UX research/service design/content strategy scoped for 10k+ external user onboarding — add UX researcher + service designer F1 (J1/J2 usability testing with pilot) → iterate conversational flows + Slack Canvas UX.
- **Governance/CoE gap (5 gaps):** Multi-team ownership RACI (Agentforce config, MuleSoft APIs, Slack admin), data stewardship (CRM Totvs vs. Salesforce truth?), CoE charter, CM execution plan — add RACI + CoE structure + CM workstream detail to E10.

---

## T-Shirt Size Distribution (Complexity Indicators)

Sizes express **relative complexity, not effort** — they are **not hour-convertible** and must **not be multiplied by a rate** to produce a price. For a timeline range, see `roadmap` skill (top-down benchmark-based derivation from engagement shape). For indicative pricing, see `commercials` skill (requires user-validated rate).

| Epic | Size | Primary Complexity Driver |
|------|------|---------------------------|
| E01 — Consultas Financeiras | **L** | Protheus ERP governance blocker (TI+Jurídico+DPO tri-party approval), MuleSoft API exposure + perfil de acesso per-user enforcement, LGPD/TCU audit trail |
| E02 — Autoatendimento Chamados | **M** | Pronto (ServiceNow) API integration, read-only F1 (lower risk than write), standard ticket query pattern |
| E03 — Intelligence Executiva | **M** | CRM Totvs read-only integration, standard CRM briefing pattern, mobile-first UX (Slack mobile) |
| E04 — KB Normativas | **L** | Portal Conexão/SharePoint RAG corpus indexing, Slack AI + MCP Real-time Search API federation, compliance-sensitive content (alçadas 2 milhões de reais) |
| E05 — Agendamento MS Teams | **S** | Standard MS Teams Graph API integration, low governance risk (calendar write-only) |
| E06 — Adoção CRM | **L** | CRM Totvs write API (F2 controlled writes), field mapping + transactional integrity validation, adoption measurement + hygiene monitoring |
| E07 — Abertura Chamados | **M** | Pronto (ServiceNow) write API (F2), required-fields validation, incident workflow orchestration |
| E08 — Gestão Demandas | **XL** | Clarity (Broadcom) API unknown + co-living vs. Service Cloud migration decision (hard-to-reverse), 4.5k active demands data migration if Service Cloud chosen, dual-path architecture risk |
| E09 — Intelligence Preditiva | **XL** | Data Cloud streaming architecture (Pronto + CRM Totvs ingestion), unified data model (Contact, Case, Opportunity), predictive segmentation (SLA breach cohort, churn-risk cohort), Agentforce activation |
| E10 — Governança/Compliance/CM | **XL** | 7-system audit trail orchestration, Protheus governance model (TI+Jurídico+DPO), Slack EKM deployment, multi-persona CM (B2B + internos + N1/N2), CoE structure, RACI by system, Experience Design workstream (UX research F1 pilot) |

**Total: 2 XL, 3 L, 3 M, 1 S, 0 XS** — multi-cloud, multi-legacy-system, compliance-heavy, phased delivery (F1/F2/F3).

---

## Architecture Highlights

**Products in scope:**
- **Slack** (Enterprise Grid): Agentic OS, hosts Agentforce agents J1-J10, Slack AI KB, Slack Connect B2B, MCP federation, Workflow Builder
- **Agentforce**: 9 agents (5 F1 read-only, 2 F2 write, 2 F3 predictive) — native orchestration (Atlas Reasoning Engine)
- **MuleSoft/MCP**: Dual deployment — Anypoint for legacy API governance + reusability, MCP Server for Slack-specific Agentforce context federation
- **Data Cloud** (F3): Streaming from Pronto + CRM Totvs → SLA breach alerts + pipeline recommendations
- **Service Cloud** (conditional F2): IF Clarity migration strategy chooses replacement; co-living decision deferred to F2 architecture gate

**Integration landscape:** 7 legacy systems exposed as read-only (F1) / controlled-write (F2+) APIs via MuleSoft — Protheus ERP, Pronto (ServiceNow), CRM Totvs, Clarity (Broadcom), Portal Conexão (SharePoint), MS Teams (Graph API), SEI (future).

**Licensing estimates (pending volumetria validation):**
- ~13k Slack licenses (2.5k B2B + 3k internos + future 7.5k legacy users F1-F3)
- Slack Enterprise Grid (EKM, DLP, org analytics required)
- Agentforce licenses (per-agent pricing TBD — validate with Salesforce)
- MuleSoft Anypoint (API call volume pending volumetria audit — Gaps G0102, G0201, G0302, G0701)

**Critical path blockers:**
- **Gap G1002 (Protheus governance):** TI+Jurídico+DPO tri-party meeting required before proposal sign-off — escalate to seller immediately
- **Volumetrias unknown (4 gaps):** Capacity planning blocked for Agentforce, MuleSoft, Heroku — F1 pre-kick-off audit required

**Open architecture decisions (deferred):**
- **Gap G0101:** Workspace Slack segregation (B2B vs. internos) — recommend single, segregate if Jurídico requires
- **Gap G0801:** Clarity migration strategy (co-living vs. Service Cloud) — defer to F2 architecture gate after F1 adoption validated
- **Gap G9902:** MuleSoft vs. MCP protocol — dual deployment recommended (Anypoint for legacy APIs, MCP Server for Slack federation)

---

## Next Steps

1. **Escalate Gap G1002** — schedule TI+Jurídico+DPO tri-party meeting before proposal submission (Protheus governance blocker)
2. **T-shirt sizing approval** — review distribution (2 XL, 3 L, 3 M, 1 S) + complexity drivers before locking estimates
3. **Roadmap skill** — phase E01-E10 across F1/F2/F3 + derive timeline range + identify roles/disciplines
4. **Validate assumptions** — TI provides API specs + sandbox credentials for Pronto, CRM Totvs, Protheus, Clarity, Conexão, MS Teams

---

**Grounding:** Load-bearing decisions tagged throughout with `[KB:...]` (project knowledge base), `[extends:...]` (inferred patterns), or `[assumption:...]` (flagged for validation). 10 decisions grounded in KB, 5 inferred, 3 assumptions flagged.

**Document control:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Scopezilla design skill | Initial draft |
