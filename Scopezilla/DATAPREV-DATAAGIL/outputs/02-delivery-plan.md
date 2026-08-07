# Roadmap — DATAPREV Data Ágil

**Project:** DATAPREV DATAAGIL  
**Document:** Phased Implementation Roadmap  
**Date:** 2026-07-19  
**Status:** Draft

---

## Timeline

**Benchmark-based program duration: 29–54 weeks** (top-down from engagement shape; Multi-Cloud High parametric row: 10 epics, predominant L/XL — 2 XL + 3 L out of 10, 7 legacy systems integrated, baseline 26-40 weeks. Adjusted: +15% regulated industry LGPD Art. 48 + TCU audit trail + perfil de acesso governance TI+Jurídico+DPO, +10% new client first-time Dataprev unknown org quality Protheus governance blocker G1002 unresolved, +10% confidence widening 68 gaps many Unknowns/Assumed. Total adders +35% under +50% cap). **Benchmark-based, not a commitment.**

**Benchmark Disclaimer** (source: model-training-data):

*The benchmark-based duration range above is derived from historical Salesforce Professional Services engagements of comparable size and complexity captured in the model's training data. It is provided as decision-support only and does not constitute a commitment, warranty, or guarantee of actual project duration. Actual timelines depend on client readiness, resource availability, scope changes, and execution quality. This range should be validated against your organization's delivery benchmarks and adjusted for deal-specific factors before use in client-facing commitments.*

---

## Phase Summary

| Phase | Objectives | Epics | Dependencies |
|-------|-----------|-------|--------------|
| **Phase 0 — Discovery & Architecture Refinement (F0)** | Resolver G1002 blocker (Protheus governance TI+Jurídico+DPO tri-party meeting), volumetrias audit (Protheus/Pronto/CRM Totvs/Abertura Chamados capacity planning), decidir Workspace Slack segregation (B2B vs internos), validar Clarity API (co-living vs Service Cloud migration) | None (gap resolution pre-kick-off) | None — blocker for F1 start |
| **Phase 1 — Foundation (F1 Quick Wins)** | Deploy Slack+Agentforce J1/J2/J5/J7/J8 read-only, MuleSoft System APIs (7 systems), Slack EKM, rastreabilidade LGPD/TCU, early adopters 20-50 piloto | E01, E02, E03, E04, E05, E10 (continuous) | Phase 0 approved (G1002 Protheus governance) |
| **Phase 2 — Expansion (F2 Controlled Writes)** | Enable J3 (Abertura Chamados) + J4 (Adoção CRM), MuleSoft write APIs (Pronto/CRM Totvs), field mapping + transactional integrity, adoption monitoring | E06, E07, E10 (continuous) | Phase 1 adoption >60% uso semanal (trust established) |
| **Phase 3 — Proactive Intelligence (F3)** | Data Cloud streaming (Pronto+CRM Totvs), unified Contact/Case/Opportunity model, J9 (SLA breach alerts) + J10 (pipeline recommendations), E08 Clarity migration decision gate | E08, E09, E10 (continuous) | Phase 2 CRM adoption validated, E08 architecture decision (co-living vs Service Cloud) |

---

## Phase 0 — Discovery & Architecture Refinement (F0)

**Objectives**: Resolve pre-kick-off blockers before F1 build starts — G1002 Protheus governance blocker (TI+Jurídico+DPO tri-party meeting approval for financial data access), volumetrias capacity planning audit (G0102 Protheus quantas consultas financeiras/mês, G0201 Pronto quantos usuários finais consultam status via Slack, G0302 CRM Totvs quem são os executivos target headcount, G0701 Abertura Chamados volume metrics), decidir G0101 Workspace Slack segregation (single workspace c/ DLP control or 2 workspaces isolated B2B vs internos — security/governance decision with TI+Jurídico+DPO), validar Clarity API compatibility (G0801 blocker — no KB coverage Broadcom Clarity; TI provides Swagger/OpenAPI specs + sandbox credentials for API discovery spike).

**Epics included**: None (gap resolution only)

**Success criteria**: 
- G1002 approved — Protheus acesso TI+Jurídico+DPO signed off (perfil de acesso per user authorization model defined)
- Volumetrias collected — capacity planning MuleSoft API calls/month, Agentforce Conversations usage, Heroku dynos sizing unblocked
- Workspace Slack decision locked — single or dual workspace architecture finalized
- Clarity API validated — REST API compatibility + authentication model confirmed; co-living vs Service Cloud migration strategy options documented for F2 gate

**Dependencies**: None — this phase is the blocker gate for F1 start

**Risks**: 
- **Critical blocker**: Se TI+Jurídico+DPO não aprovar Protheus acesso, F1 inviável — escalate to seller immediately before proposal submission. Fallback: defer J1 (Consultas Financeiras) to F2, launch F1 with J2/J5/J7/J8 only (4 jornadas instead of 5).
- **Volumetrias audit delay**: If TI cannot provide capacity metrics within Phase 0 window, MuleSoft/Agentforce/Heroku sizing will be Assumed (not Confirmed) → risk of under-provisioning or over-cost.
- **Clarity API unavailable**: If Broadcom Clarity API is undocumented or brittle (external dependency risk), entire E08 epic blocked → recommend Service Cloud migration path immediately (no co-living option).

---

## Phase 1 — Foundation (F1 Quick Wins)

**Objectives**: Deploy Slack+Agentforce J1/J2/J5/J7/J8 read-only (5 jornadas), MuleSoft System APIs expose 7 legacy systems (Protheus ERP, Pronto ServiceNow, CRM Totvs, Portal Conexão SharePoint, MS Teams Graph API, Clarity Broadcom, SEI future) with rastreabilidade LGPD/TCU (every API call logged: user ID + timestamp + query/mutation + response status), Slack EKM deployment (AWS KMS master keys under Dataprev CISO control — motivated by prior 2.8M CPF breach instant revocation capability), early adopters 20-50 piloto onboarded (training by persona: B2B clientes J1, executivos J5, N1/N2 J2, Pessoas J7, all J8), executive mandate (Saulo enforces adoption KPIs >60% uso semanal target).

**Epics included**: E01 (Consultas Financeiras Self-Service), E02 (Autoatendimento Chamados Técnicos), E03 (Intelligence Executiva Mobile), E04 (Knowledge Base Normativas RH), E05 (Agendamento Automatizado), E10 (Governança, Compliance e Change Management — continuous)

**Success criteria**:
- 5 jornadas live read-only: J1 (Protheus financial queries), J2 (Pronto ticket status), J5 (CRM Totvs executive briefing), J7 (KB Normativas políticas RH alçadas 2 milhões de reais), J8 (MS Teams calendar scheduling via voice/text)
- Early adopters trained: 20-50 pilot users across 4 personas (B2B clientes, executivos, N1/N2, Pessoas) — formal training sessions completed, usage validated
- Audit trail operational: LGPD/TCU rastreabilidade — 7-system MuleSoft API call logging to Salesforce custom object, 5-year retention configured
- Saulo executive mandate enforced: adoption KPIs dashboard live (uso semanal %, agent adoption by persona, API call volume/error rate)

**Dependencies**: Phase 0 approved — G1002 Protheus governance blocker resolved (TI+Jurídico+DPO tri-party meeting signed off)

**Risks**:
- **Experience Design gap (G0104/G0402/G0505)**: 10k+ external users onboarding sem UX research/service design/content strategy scoped → low adoption risk. Mitigation: add UX researcher + service designer F1 (J1/J2 usability testing with 20-50 pilot) → iterate conversational flows + Slack Canvas UX before scale.
- **Governance/CoE gap (G9901/G1001/G1003)**: Multi-team ownership (Agentforce config, MuleSoft APIs, Slack admin, CRM Totvs vs Salesforce truth) undefined — decision rights, data stewardship, CoE structure, CM workstream execution plan missing. Mitigation: RACI by system + CoE charter finalized Phase 0 or early F1.
- **Volumetrias unknown (G0102/G0201/G0302)**: Capacity planning MuleSoft API rate limiting, Agentforce Conversations usage, Heroku dynos blocked without Phase 0 audit. Mitigation: Phase 0 volumetrias audit mandatory before F1 kick-off.

---

## Phase 2 — Expansion (F2 Controlled Writes)

**Objectives**: Enable J3 (Abertura Chamados Assistida — Pronto ServiceNow case creation via Slack voice/text) + J4 (Adoção CRM Conversacional — CRM Totvs pipeline/forecast/oportunidades updates via Slack voice/text), MuleSoft write APIs (Pronto case creation + required-fields validation subject/priority/description/category, CRM Totvs pipeline updates + field mapping + transactional integrity validation), adoption monitoring dashboard (hygiene KPIs: uso semanal %, pipeline completeness staleness, forecast accuracy — derived from CRM Totvs activity logs), +40% CRM adoption target (baseline 30% → 70% final adoption).

**Epics included**: E06 (Adoção CRM via Conversação), E07 (Abertura de Chamados Assistida), E10 (Governança, Compliance e Change Management — continuous)

**Success criteria**:
- J3 operational: Ticket creation via Slack validated (Pronto ServiceNow case creation API working, ticket number + SLA returned to user, incident workflow orchestration Pronto internal routing/assignment rules triggered)
- J4 operational: CRM updates via Slack validated (CRM Totvs write API field mapping correct, transactional integrity confirmed, comercial confirms pipeline/forecast updates reflected in CRM UI)
- +40% CRM adoption: Baseline 30% (50 active users ~30% of 170 total comercial) → target 70% final adoption = 119 users. Adoption monitoring dashboard live (uso semanal %, pipeline hygiene metrics).
- F1 adoption trust established: >60% uso semanal Phase 1 (early adopters validated, executive mandate Saulo enforced) — trust baseline before F2 writes enabled

**Dependencies**: Phase 1 adoption >60% uso semanal — trust established before F2 writes enabled (read-only F1 validates Agentforce conversational UX before controlled writes F2 risk)

**Risks**:
- **CRM Totvs write API compatibility unknown (G0601 blocker)**: Validate field mapping + transactional integrity mechanism with TI before F2 build. If CRM Totvs write API is batch-only (not real-time), comercial sees stale pipeline during the day → defeats real-time adoption goal. Mitigation: Phase 0 or F1 technical discovery spike — CRM Totvs API response time, throughput limits, retry logic validated.
- **Pronto write API authentication model (G0701)**: ServiceNow case creation API — validate authentication model + required fields + category taxonomy with TI before F2 build. Volumetria unknown (ticket creation volume/day) — needed for MuleSoft capacity planning. Mitigation: Phase 0 volumetrias audit includes J3 ticket creation projection.
- **F2 controlled writes risk**: Incorrect field mapping (Agentforce conversational input → CRM Totvs/Pronto required fields) or failed transaction → stale data (CRM forecast inaccuracy, ticket creation fails → user frustration). Mitigation: robust validation + retry logic + QA testing F2 (field mapping correctness, transactional integrity, error handling).

---

## Phase 3 — Proactive Intelligence (F3)

**Objectives**: Data Cloud streaming architecture (Pronto ServiceNow ticket events + CRM Totvs opportunity events CDC ingestion — event-driven Change Data Capture pattern), unified data model (Contact B2B client + internal employee, Case/Ticket history from Pronto with 4+ related objects, Opportunity/Demand history from CRM Totvs — complex multi-source unified model), J9 (SLA breach alerts proativos — Data Cloud identifies high-risk SLA breach cohort → Agentforce alerts N2/manager before breach occurs), J10 (pipeline recommendations — Data Cloud identifies churn-risk cohort → Agentforce suggests next best action to comercial "Oportunidade X sem atividade 30 dias — agendar call?"), Agentforce proactive activation (push alerts to Slack channels/DMs), E08 Clarity migration decision gate (co-living: Agentforce writes Clarity via MuleSoft; OR Service Cloud migration: 4.5k active demands migrate to Service Cloud Case, Clarity becomes read-only archive — hard-to-reverse decision deferred to F2 gate after F1 adoption validated 3 months production).

**Epics included**: E08 (Gestão de Demandas Evolutivas), E09 (Intelligence Preditiva e Recomendações), E10 (Governança, Compliance e Change Management — continuous)

**Success criteria**:
- J9 operational: SLA breach alerts proativos — Data Cloud high-risk cohort identified (Pronto ticket lifecycle ingested, SLA breach prediction model trained), Agentforce pushes alerts to N2/manager Slack channels/DMs before breach ("Alerta: Ticket X risco SLA breach em 2h")
- J10 operational: Pipeline recommendations — Data Cloud churn-risk cohort identified (CRM Totvs opportunity lifecycle ingested, historical pipeline patterns analyzed), Agentforce suggests next best action to comercial Slack ("Oportunidade Y sem atividade 30 dias — agendar call?")
- Clarity decision locked: Co-living (Agentforce writes Clarity via MuleSoft write API, Clarity remains system of origin) OR Service Cloud migration (4.5k active + historical demands migrate to Service Cloud Case object, Clarity becomes read-only archive, Agentforce writes Service Cloud). Recommendation: defer to F2 gate after F1 adoption + Clarity API validation (3 months F1 production).
- Data Cloud streaming validated: Pronto ticket events + CRM Totvs opportunity events ingested (CDC streaming APIs working), unified Contact/Case/Opportunity profiles operational (multi-source data model reconciled)

**Dependencies**: 
- Phase 2 CRM adoption validated — data quality baseline (if CRM Totvs adoption stays 30%, stale data risk for predictive models — GIGO: garbage in, garbage out)
- E08 architecture decision — co-living vs Service Cloud (hard-to-reverse, one-way door; if wrong choice, rollback to Clarity operationally infeasible reverse data migration + process retraining)

**Risks**:
- **Data Cloud streaming architecture unknown (G0901 assumption)**: Validate Pronto ServiceNow + CRM Totvs streaming API availability + CDC pattern compatibility with TI before F3 build. If batch-only (not streaming), predictive alerts delayed (nightly batch → stale alerts next day). Mitigation: Phase 0 or F1 technical discovery — streaming API feasibility validated.
- **Clarity API compatibility unknown (G0801 blocker — no KB coverage)**: Broadcom Clarity API undocumented or brittle (external dependency risk). F1 Phase 0 API discovery sprint required (2 weeks, TI provides Swagger/OpenAPI specs + sandbox credentials). Mitigation: early API validation Phase 0 + fallback to Service Cloud migration if Clarity API infeasible.
- **Data quality dependency**: If Pronto tickets or CRM Totvs opportunities incomplete/stale (CRM Totvs low adoption 30% baseline → pipeline not maintained), predictive models degrade (GIGO). Mitigation: F2 CRM adoption validated (>70% target) before F3 Data Cloud ingestion starts — ensures data quality baseline.
- **Historical data load size unknown**: If >500k records (Pronto tickets 6-12 months + CRM Totvs opportunities), performance/cost implications Data Cloud ingestion. Mitigation: Phase 0 volumetrias audit includes historical data volume projection.
- **Einstein Discovery model accuracy unknown**: Requires F3 pilot tuning (model training + eval loops). If ML-based (not rule-based), AI/ML workstream needed (data scientist + training dataset preparation + model validation + retraining cadence) — not scoped in epic brief. Mitigation: clarify ML vs rule-based approach before F3 sizing.
- **Data Cloud first-time deployment**: Limited Dataprev production precedent — may require vendor support engagement (Salesforce Data Cloud specialist). Mitigation: architect + vendor support scoped F3.

---

## Standard Processes (Consolidated Across Phases)

### Testing Strategy
- **Unit testing**: Per-epic (MuleSoft API connectors, Agentforce intent parsing, Salesforce Flow orchestration)
- **Integration testing**: Cross-system (Protheus/Pronto/CRM Totvs/Clarity/Conexão/Teams 7 systems, MuleSoft → Salesforce → Slack → Agentforce end-to-end)
- **UAT**: Per phase (F1 early adopters 20-50 piloto, F2/F3 scale validation)
- **Performance testing**: F1 (MuleSoft API rate limits validated against volumetrias), F3 (Data Cloud streaming throughput validated)
- **Security testing**: LGPD/TCU audit trail verification (every API call logged correctly), Slack EKM instant revocation tested

### Deployment Strategy
- **Phased rollout**: F1 (early adopters 20-50 piloto → validate adoption >60% uso semanal before F2), F2 (scale to full comercial 170 users + N1/N2 support team), F3 (scale to all 3k internal employees + 2.5k B2B external orgs)
- **Rollback plan**: Per phase (F1 read-only low risk — disable Agentforce agents + MuleSoft APIs; F2 controlled writes moderate risk — revert to F1 read-only if writes fail; F3 Data Cloud high risk — pause streaming ingestion if predictive models degrade)
- **Hypercare**: 2 weeks post-go-live per phase (F1/F2/F3 — architect + admin + QA on-call for production issues)

### Training & Change Management
- **Training by persona**: B2B clientes (J1 Consultas Financeiras), executivos (J5 Intelligence Executiva), comercial (J4/J6 CRM + demandas), N1/N2 (J2/J3 chamados) — formal training sessions F1, Trailhead modules + video library + Slack Canvas help content
- **Early adopters program**: 20-50 pilot users F1 (multi-persona) — champions identified, trained first, usage validated before scale F2/F3
- **Executive mandate**: Saulo (executive sponsor) enforces adoption KPIs (>60% uso semanal target F2) — dashboard monitored weekly, non-adopters escalated
- **Adoption monitoring**: Salesforce CRM Analytics dashboard (uso semanal %, agent adoption by persona, API call volume/error rate, audit log compliance metrics) — updated daily, reviewed weekly by CM Lead + Saulo

---

## Consolidated Risk Table

| Risk | Impact | Mitigation | Phase |
|------|--------|------------|-------|
| **Protheus governance blocker (G1002)** | Critical — if TI+Jurídico+DPO não aprovar Protheus acesso, F1 inviável | Escalate to seller immediately before proposal submission. Tri-party meeting (TI + Jurídico + DPO + Salesforce Architect) Phase 0. Fallback: defer J1 to F2, launch F1 with J2/J5/J7/J8 only (4 jornadas). | 0 |
| **Experience Design gap (G0104/G0402/G0505)** | High — 10k+ external users onboarding sem UX research → low adoption F1 | Add UX researcher + service designer F1 (J1/J2 usability testing with 20-50 pilot) → iterate conversational flows + Slack Canvas UX before scale F2/F3 | 0, 1 |
| **Governance/CoE gap (G9901/G1001/G1003)** | High — multi-team ownership undefined → sprawl/shadow IT post-F1 | RACI by system + CoE charter finalized Phase 0 or early F1 (decision rights, data stewardship, Agentforce prompt governance, MuleSoft API governance) | 0, 1 |
| **Volumetrias unknown (G0102/G0201/G0302/G0701)** | Medium — capacity planning MuleSoft/Agentforce/Heroku blocked → risk under-provisioning or over-cost | Phase 0 volumetrias audit mandatory (TI provides projections: Protheus queries/mês, Pronto status queries/day, CRM Totvs executive headcount, Abertura Chamados volume/day) | 0 |
| **Clarity API compatibility unknown (G0801)** | High — no KB coverage Broadcom Clarity; if API undocumented/brittle, E08 blocked | F1 Phase 0 API discovery sprint (2 weeks, TI provides Swagger/OpenAPI specs + sandbox credentials). Fallback: recommend Service Cloud migration immediately (no co-living option) | 0, 3 |
| **CRM Totvs/Pronto write API compatibility (G0601/G0701)** | Medium — if batch-only (not real-time), comercial sees stale pipeline → defeats adoption goal | Phase 0 or F1 technical discovery spike (CRM Totvs + Pronto API response time, throughput limits, retry logic validated) | 0, 1, 2 |
| **F2 controlled writes risk** | Medium — incorrect field mapping → stale CRM data/ticket creation fails | Robust validation + retry logic + QA testing F2 (field mapping correctness, transactional integrity validated, error handling tested) | 2 |
| **Data Cloud streaming architecture unknown (G0901)** | Medium — if batch-only (not streaming), predictive alerts delayed (nightly → stale alerts) | Phase 0 or F1 technical discovery (Pronto + CRM Totvs streaming API availability + CDC pattern compatibility validated with TI) | 0, 1, 3 |
| **Data quality dependency F3** | High — if CRM Totvs adoption stays 30%, stale data → predictive models degrade (GIGO) | F2 CRM adoption validated (>70% target) before F3 Data Cloud ingestion starts — ensures data quality baseline | 2, 3 |
| **Einstein Discovery model accuracy unknown** | Medium — if ML-based, requires data scientist + training dataset + model validation (AI/ML workstream not scoped) | Clarify ML vs rule-based approach before F3 sizing. If ML, scope data scientist + training cadence F3. | 3 |
| **Data Cloud first-time deployment** | Low — limited Dataprev production precedent → may require vendor support | Architect + Salesforce Data Cloud specialist vendor support scoped F3 | 3 |

---

**Document control:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Scopezilla roadmap skill | Initial draft |
