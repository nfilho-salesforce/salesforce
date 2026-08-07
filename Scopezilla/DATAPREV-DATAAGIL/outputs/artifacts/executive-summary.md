# Executive Summary — DATAPREV Data Ágil

**Project:** DATAPREV DATAAGIL  
**Audience:** Executive (CTO, Steering Committee, Sponsors)  
**Date:** 2026-07-19  
**Status:** Draft

---

## At a Glance

- **Current state pain**: 166× client growth (15 → 2,500 B2B clients) without infrastructure evolution creates operational bottlenecks — 7 fragmented legacy systems, SLA degradation (hours vs. <1min target), 30k tickets/month managed manually
- **Transformation vision**: From reactive IT provider to proactive intelligence platform — B2B clients (ministries, public entities) and internal staff access critical information (financial, tickets, policies) instantly via Slack+Agentforce conversational interface, eliminating legacy silos and accelerating executive decisions
- **Top value drivers**: Response time reduction (2-4h → <1min for financial/ticket queries), CRM adoption increase (+40% via conversational interface), compliance risk mitigation (automated approval thresholds eliminate TCU exposure), competitive parity with SERPRO (federal sector benchmark)
- **Biggest risk**: Protheus governance blocker (G1002) — TI+Legal+DPO tri-party approval pending pre-kickoff. Fallback: defer financial queries (J1) to Phase 2, launch Phase 1 with 4 journeys instead of 5
- **Recommended first step**: Phase 0 (Discovery & Architecture Refinement) — resolve governance blocker, complete capacity audit (68 gaps exceed 15-gap threshold), lock architectural decisions before Phase 1 build

---

## Overview

Dataprev operates at the center of Brazil's social security system (INSS) and serves federal ministries/public entities during accelerated digital transformation (EFGD 2024-2027 "intelligent government" strategy). Explosive client growth (166×) without equivalent infrastructure evolution has created critical operational bottlenecks: 7 disconnected legacy systems (Pronto/ServiceNow, Clarity/Broadcom, Protheus ERP, CRM Totvs, SharePoint portal, MS Teams, SEI), degraded SLA (financial/ticket queries depend on human N1 queues with hours of latency vs. <1min target), and low adoption of strategic tools (CRM commercial ~30% adoption compromises executive forecast quality).

Regulatory pressure is mounting: recent data breach (2.8M CPFs May/2026), active TCU audit on IT procurement, and LGPD enforcement demand immediate governance hardening. Competitive pressure from SERPRO (similar state entity with AI/automation in production) creates churn risk on government contract renewals. Window of opportunity converges: mainframe recently decommissioned (Jan/2026) opens architectural window, executive sponsorship bottom-up (Saulo already championed Slack before official discovery), and parliamentary recess creates deployment window without critical operational pressure.

Data Ágil transforms Dataprev into a proactive intelligence platform by deploying **Slack as an Agentic Operating System**, orchestrated by **Agentforce**, integrated via **MuleSoft/MCP** to 7 existing systems. 2,500 B2B clients + 3,000 internal employees access financial data, technical support, executive intelligence, compliance policies, and CRM updates through a single conversational surface — eliminating interface proliferation, accelerating decision-making, and establishing competitive technology baseline.

**Why Salesforce, why now**: Salesforce offers the only native stack integrating enterprise conversational channel (Slack Ultimate already contracted), AI agent orchestrator (Agentforce with built-in governance/traceability), and enterprise integration layer (MuleSoft Anypoint for legacy systems). Alternatives (custom bot on ChatGPT API + manual integrations) lack LGPD/TCU-ready governance, sensitive data access traceability, or 24/7 enterprise support for critical public agency. Proven Brazilian public sector experience (INSS, Federal Revenue, TCU cases) and SOC2/ISO27001 auditable compliance. Agentforce as native orchestrator eliminates duplicated LLM latency and maintains conversational context within Salesforce ecosystem. MuleSoft is Gartner iPaaS leader, reducing technical risk on legacy integrations (Pronto/ServiceNow, Clarity/Broadcom, Protheus/Totvs).

Window closes fast: deferring loses parliamentary recess deployment window (teams will be consumed by operational demands), widens competitive gap vs. SERPRO, aggravates N1/N2 operational crisis, and loses current political momentum (Saulo/Pedro/Maik engaged now).

---

## Scope Summary

**10 epics** organized in phased delivery that maximizes early ROI and de-risks complexity:

**Phase 1 — Foundation (F1 Quick Wins, read-only)**:
- **E01 — Self-Service Financial Queries**: B2B clients query Protheus ERP (outstanding amounts, contracts, payments) via Slack without N1 human escalation. Governed by TI+Legal+DPO, LGPD/TCU traceability. Priority journey J1.
- **E02 — Technical Ticket Self-Service**: Query Pronto (ServiceNow) ticket status — open count, critical status, SLA, history. Read-only Phase 1, assisted opening Phase 2+. Reduces N1 dependency (~30k tickets/month). Journey J2.
- **E03 — Executive Mobile Intelligence**: Executives access project briefing via conversational agent before urgent meetings (ministries, critical client). Queries CRM Totvs read-only via Slack. Use case: *"Maik summoned to ministry, asks agent en route, arrives briefed."* Journey J5.
- **E04 — HR Policy Knowledge Base**: Automated query of internal policies (SharePoint portal) via Agentforce KB: HR policies, delegation of authority (approval thresholds — who signs above R$2M?), compliance. Reduces repetitive inquiries to HR team (-50% target Phase 1). Eliminates incorrect threshold risk in proposals/contracts (TCU exposure). Journey J7.
- **E05 — Automated Scheduling**: Scheduling via voice/text command in Slack integrated with MS Teams corporate calendar. Use case: *"Pedro exits meeting, sends audio 'Schedule meeting tomorrow with X, Y, Z', arrives home at ease."* Eliminates cognitive friction. Journey J8.

**Phase 2 — Expansion (F2 Controlled Writes)**:
- **E06 — CRM Adoption via Conversation**: Increase CRM Totvs commercial adoption (~30% baseline → +40% target = 70% final) via Slack conversational interface. Sales team updates pipeline, forecast, opportunities by voice/text, reduces manual login friction. Goal: +40% adoption via controlled writes Phase 2. Journey J4.
- **E07 — Assisted Ticket Opening**: Opening tickets in Pronto (ServiceNow) via structured voice/text in Slack. Controlled writes Phase 2 (Phase 1 read-only). External clients + internal staff. Reduces formal-document/meeting friction to open ticket. Journey J3.

**Phase 3 — Proactive Intelligence (F3)**:
- **E08 — Evolutionary Demand Management**: Query and create evolutionary demands in Clarity (Broadcom) via Slack + Agentforce. Read-only Phase 1, writes Phase 2+. ~4,500 active demands. Pending Phase 2 architectural decision: if Salesforce Service Cloud becomes demand system of origin, Clarity becomes legacy query archive. Journey J6.
- **E09 — Predictive Intelligence & Recommendations**: Predictive SLA analysis (J9) + commercial recommendations (J10) via Data Cloud + Agentforce. Proactive alerts of SLA breach risk in Pronto, next-action suggestions based on historical CRM pipeline. Phase 3 Proactive. Journeys J9 and J10.

**Phase 10 — Governance, Compliance & Change Management (cross-cutting all phases)**:
- **E10 — Governance/Compliance/CM**: (1) MuleSoft/MCP secure integration layer over legacies (Pronto, Clarity, Protheus, CRM Totvs, Portal, Teams) with LGPD/TCU auditable traceability; (2) TI+Legal+DPO governance on Protheus (sensitive financial data, per-user access profile authorization); (3) Structured Change Management — formal training by persona (B2B clients, executives, sales, N1/N2), executive mandate (Saulo), early adopter onboarding (20-50 pilot), adoption KPI monitoring (>60% weekly usage); (4) Reusable architecture across Data Ágil + Serviço na Ponta (parallel Dataprev project) for scope economy.

---

## Solution Highlights

**Products in scope**: Slack (Enterprise Grid — Agentic OS hosting Agentforce agents J1-J10, Slack AI KB, Slack Connect B2B, MCP federation, Workflow Builder), Agentforce (9 agents: 5 Phase 1 read-only, 2 Phase 2 writes, 2 Phase 3 predictive — native Atlas Reasoning Engine orchestration), MuleSoft/MCP (dual deployment — Anypoint for legacy API governance + reusability, MCP Server for Slack-specific Agentforce context federation), Data Cloud (Phase 3 — streaming from Pronto + CRM Totvs → SLA breach alerts + pipeline recommendations), Service Cloud (conditional Phase 2 — IF Clarity migration strategy chooses replacement; co-living decision deferred to Phase 2 architecture gate).

**Integration landscape**: 7 legacy systems exposed as read-only (Phase 1) / controlled-write (Phase 2+) APIs via MuleSoft — Protheus ERP, Pronto (ServiceNow), CRM Totvs, Clarity (Broadcom), SharePoint Portal, MS Teams (Graph API), SEI (future).

**Key architecture decisions grounded in knowledge base**: 18 decisions tagged — 10 KB-grounded, 5 inferred, 3 flagged assumptions (Workspace Slack segregation pending compliance decision, Clarity migration strategy deferred to Phase 2, MuleSoft vs MCP protocol dual deployment recommended). MuleSoft API-led connectivity pattern (System + Process + Experience layers) ensures governance/auditability. Slack EKM (Enterprise Key Management) with AWS KMS master keys under Dataprev CISO control provides instant revocation capability (motivated by prior 2.8M CPF breach).

---

## Implementation Approach

**Phased delivery de-risks complexity and accelerates value**:

- **Phase 0 — Discovery & Architecture Refinement (F0)**: Resolve G1002 blocker (Protheus governance TI+Legal+DPO tri-party meeting), capacity audit (68 gaps — volumetrics G0102 Protheus, G0201 Pronto, G0302 CRM Totvs, G0701 ticket opening), lock G0101 (Workspace Slack segregation B2B vs internal), validate Clarity API (G0801 co-living vs Service Cloud migration strategy). **Critical**: if TI+Legal+DPO do not approve Protheus access, Phase 1 infeasible — escalate to seller immediately. Fallback: defer J1 to Phase 2, launch Phase 1 with J2/J5/J7/J8 only (4 journeys instead of 5).

- **Phase 1 — Foundation (F1 Quick Wins, read-only)**: Deploy Slack+Agentforce J1/J2/J5/J7/J8 read-only, MuleSoft System APIs (Protheus/Pronto/CRM Totvs/Portal/SharePoint), Slack EKM (AWS KMS master keys under CISO control), LGPD/TCU traceability (7-system audit trail), early adopters 20-50 pilot onboarded, executive mandate (Saulo >60% weekly usage). Success criteria: 5 journeys live read-only, early adopters trained, audit trail operational (every API call logged: user ID + timestamp + query/mutation + response status), Saulo executive mandate enforced. Timeline: immediate visibility, zero write-back risk.

- **Phase 2 — Expansion (F2 Controlled Writes)**: Enable J3 (assisted ticket opening Pronto case creation) + J4 (conversational CRM pipeline/forecast updates), MuleSoft write APIs (Pronto ServiceNow, CRM Totvs), field mapping + transactional integrity validation, adoption monitoring dashboard (hygiene KPIs: weekly usage %, pipeline completeness, forecast accuracy). Success criteria: +40% CRM adoption (baseline 30% → target 70% final), ticket creation via Slack operational, hygiene monitoring live, Phase 1 adoption trust established (>60% weekly usage). Dependency: Phase 1 adoption >60% weekly usage — trust established before Phase 2 writes enabled.

- **Phase 3 — Proactive Intelligence (F3)**: Data Cloud streaming architecture (Pronto ticket events + CRM Totvs opportunity events CDC ingestion), unified data model (Contact B2B client + internal employee, Case/Ticket history Pronto, Opportunity/Demand history CRM Totvs), J9 (proactive SLA breach alerts N2/manager before breach) + J10 (pipeline recommendations churn-risk cohort next best action), Agentforce proactive activation (push alerts Slack channels/DMs), E08 Clarity migration decision gate (co-living vs Service Cloud replacement). Dependency: Phase 2 CRM adoption validated (data quality baseline — if CRM Totvs adoption stays 30%, stale data risk for predictive models).

**Timeline**: Benchmark-based range **29–54 weeks** derived top-down from engagement shape (Multi-Cloud High: 10 epics, predominant L/XL — 2 XL + 3 L out of 10, 7 legacy systems integrated, baseline 26-40 weeks). Adjusted: +15% regulated industry (LGPD Art. 48 + TCU audit trail + Protheus access governance TI+Legal+DPO), +10% new client (first-time Dataprev, unknown org quality, Protheus governance blocker G1002 unresolved), +10% confidence widening (68 gaps, many Unknowns/Assumed — G1002 blocker, volumetrics pending, Experience Design gap, Governance gap). Total adders +35% (under +50% cap).

> **Benchmark Disclaimer**: Timeline range derived from Salesforce PS historical engagement data (model-training-data) via parametric classification of engagement shape (size distribution, clouds in scope, integration count, regulatory context). This is decision-support data, not a commitment or guarantee. Actual duration depends on client-side capacity (Phase 0 approvals, TI API access provisioning, volumetrics audit speed), scope changes, and unforeseen technical blockers. Use for planning and budget allocation; validate assumptions in Phase 0 before locking timeline.

---

## Effort Summary

**Complexity**: 10 epics — 2 XL, 3 L, 3 M, 1 S. Predominant L/XL (50% of epics) driven by: Protheus governance blocker (E01 L), RAG + Slack AI (E04 L), CRM write API (E06 L), Clarity migration (E08 XL), Data Cloud streaming (E09 XL), 7-system audit trail + Slack EKM (E10 XL). Sizes express relative complexity, not effort — not hour-convertible, not to be multiplied by rate to derive price. For timeline range see Implementation Approach above.

**Disciplines required**: Expertise across 11 disciplines spanning architecture, product specialization, delivery, and governance. **One person may fill multiple roles; one role may be filled by multiple people.** Team sizing, FTE counts, and staffing require Salesforce PS capacity assessment, delivery model, and commercial terms — not within this summary's scope.

**Architecture & Integration**: Senior Technical Architect (security, governance included), MuleSoft Technical Architect (7-system integration hub).

**Product Specialists**: Solution Architect (Service Cloud, Slack), Data Cloud Technical Architect, Agentforce Technical Consultant, MuleSoft Technical Consultant (integration builds).

**Experience & Delivery**: UX Researcher (10k+ users — scoped to address Experience Design gap G0104/G0402/G0505; adoption/rework risk if deferred: 10k+ external users onboarding without UX research caps conversational flow quality, increases support burden Phase 1 pilot), Solution Consultant (BA + release mgmt), Quality Assurance Consultant (7-system + agent testing).

**Governance**: embedded in Senior Technical Architect (CoE, security stewardship — scoped to address Governance gap G9901/G1001/G1003; scale/rework risk if not locked early: multi-team ownership (Agentforce config, MuleSoft APIs, Slack admin), data stewardship (CRM Totvs vs Salesforce truth?), CoE structure — political alignment slows Phase 1 if deferred).

**AI delivery efficiency**: ~10-14% realized band at Low readiness (task-level ~30-40%, realization factor 0.40-0.45). Current readiness score 2/8 driven by: no AI tooling adoption observed, Protheus governance blocker G1002 unresolved, LGPD breach + TCU audit pressure, 7-system fragmentation + volumetrics unknown. Moving to High readiness (~18-22%) requires 5 unlocks: AI tooling approval, G1002 resolution, LGPD/TCU AI policy, volumetrics audit, data model reconciliation plan. This is pace and quality lift within same team shape — not headcount reduction, not pricing input.

---

## Risks and Mitigations

**Critical path blockers**:

1. **Protheus governance blocker (G1002) — CRITICAL**: If TI+Legal+DPO do not approve Protheus financial data access Phase 0, entire Phase 1 J1 journey infeasible. **Mitigation**: Escalate to seller immediately before proposal submission; schedule tri-party meeting urgently. **Fallback**: Defer J1 to Phase 2, launch Phase 1 with J2/J5/J7/J8 only (4 journeys instead of 5) — reduces early wins but unblocks Phase 1.

2. **Volumetrics unknown (G0102/G0201/G0302/G0701)**: MuleSoft/Agentforce/Heroku capacity planning blocked without Phase 0 audit. **Mitigation**: Mandatory Phase 0 volumetrics audit before Phase 1 kick-off. **Risk**: Under-provisioning (performance degradation) or over-cost (over-sized infrastructure).

3. **Clarity API compatibility unknown (G0801 — no KB coverage)**: Broadcom Clarity API undocumented or brittle (external dependency risk) → entire E08 blocked. **Mitigation**: Phase 1 Phase 0 API discovery sprint required (2 weeks, TI provides Swagger/OpenAPI specs + sandbox credentials). **Fallback**: Recommend Service Cloud migration immediately (no co-living option) — 4.5k active demands migrate to Service Cloud Case, Clarity becomes read-only archive (hard-to-reverse decision deferred to Phase 2 gate).

4. **Experience Design gap (6 gaps: G0104, G0402, G0505, G0605, G0704, G0207)**: 10k+ external users onboarding without UX research/service design/content strategy scoped. **Risk**: Low adoption Phase 1 pilot if conversational flows miss user language/expectations, increased support burden. **Mitigation**: Add UX Researcher + Service Designer Phase 0/Phase 1 — J1/J2 usability testing with pilot 20-50 users → iterate conversational flows + Slack Canvas UX before Phase 2/Phase 3 scale.

5. **Governance/CoE gap (5 gaps: G0407, G0607, G9901, G1001, G1003)**: Multi-team ownership decision rights (Agentforce config, MuleSoft APIs, Slack admin), data stewardship (CRM Totvs vs Salesforce truth?), CoE structure, CM execution plan — vision in E10 but no execution detail. **Risk**: Phase 1 delayed if RACI unresolved; rework if data stewardship conflict surfaces Phase 2. **Mitigation**: Phase 0 RACI workshop (TI+Legal+DPO+PS+Dataprev Product Owner), lock decision rights + data stewardship model before Phase 1 build.

6. **Data Cloud first-time deployment**: Limited Dataprev production precedent → may require Salesforce Data Cloud specialist vendor support engagement Phase 3 (budget/timeline impact). **Mitigation**: Architect + vendor support scoped Phase 3.

**Top 10 risks consolidated**: See `outputs/03-roadmap.md` for full risk table (Phase 0/Phase 1/Phase 2/Phase 3 risks, mitigations, ownership).

---

## Assumptions and Confidence Level

**Confidence distribution** (45% Confirmed, 50% Assumed, 5% Unknown across 20 items — typical for pre-sales proposal scope):

- **Epics**: 80% Confirmed, 20% Assumed (8/10 Confirmed — healthy)
- **Estimates**: 10% Confirmed, 80% Assumed, 10% Unknown (1/10 Confirmed — low, expected on first T-shirt pass; will improve Phase 0 validation)

**Gap analysis**: 68 gaps total (exceeds 15-gap threshold — **Phase 0 RECOMMENDED**). Distribution: 32% Missing Requirement, 18% Ambiguity, 18% Potential Risk, 12% Logical Gap, 9% Source Conflict, 12% Other (Capability Gap). 6 Source Conflicts exceed 5-conflict threshold.

**Key assumptions requiring Phase 0 validation**:

- **Protheus governance (G1002)**: TI+Legal+DPO tri-party approval — BLOCKER for Phase 1; escalate to seller immediately.
- **Volumetrics (4 gaps)**: Protheus financial query volume/month, Pronto ticket queries/user/day, CRM Totvs executive briefings/month, ticket opening volume — capacity planning blocked until Phase 0 audit.
- **API compatibility**: CRM Totvs write API equivalence to Salesforce pattern (G0601), Pronto case creation API (G0701), Clarity API undocumented (G0801) — validate with TI Phase 0.
- **Workspace Slack segregation (G0101)**: Single workspace with DLP control or 2 isolated workspaces (B2B vs internal) — Legal approval unknown, lock Phase 0.
- **Data model reconciliation**: 7 legacy systems (no unified model today) — Contact B2B + employee unification, Case/Ticket Pronto history, Opportunity/Demand CRM Totvs — complexity unknown, Phase 0 data model workshop.

Phase 0 resolves 68 gaps before Phase 1 build, improving confidence to 70-80% Confirmed (industry standard for delivery-ready scope).

---

## Next Steps and Recommendations

1. **Escalate Protheus governance blocker (G1002)** — schedule TI+Legal+DPO tri-party meeting before proposal submission. This is a pre-sales qualification gate; if unresolved, Phase 1 J1 journey infeasible (fallback: defer J1 to Phase 2).

2. **Approve Phase 0 Discovery & Architecture Refinement** — 68 gaps exceed 15-gap threshold, 6 Source Conflicts exceed 5-conflict threshold. Phase 0 resolves blockers (G1002 governance, volumetrics audit, Workspace Slack segregation, Clarity API validation), locks architectural decisions, and improves confidence from 45% to 70-80% Confirmed before Phase 1 build.

3. **Lock Experience Design workstream** — add UX Researcher + Service Designer Phase 0/Phase 1 to address G0104/G0402/G0505 gap (10k+ external users onboarding). Usability testing with pilot 20-50 users Phase 1 → iterate conversational flows + Slack Canvas UX before Phase 2/Phase 3 scale. Deferring increases adoption risk and support burden.

4. **Lock Governance/CoE workstream** — Phase 0 RACI workshop to resolve G9901/G1001/G1003 gaps (multi-team ownership decision rights, data stewardship, CoE structure, CM execution plan). Lock before Phase 1 build to avoid Phase 1 delay or Phase 2 rework.

5. **Capture baseline metrics pre-Phase 1** — NPS/CSAT (comparison post-implementation), 30-day active users CRM Totvs adoption baseline (30% → +40% target Phase 2 = 70% final), N1/N2 query volume (reduction target -50% Phase 1). Essential for ROI measurement.

6. **Schedule client validation session** — 45% Confirmed confidence (low for pre-sales); recommend stakeholder validation session (Pedro/Saulo/Maik + TI/Legal/DPO representatives) to promote Assumed → Confirmed before finalizing scope.

7. **Consider AI delivery efficiency unlocks** — if Salesforce PS wants to capture High readiness band (~18-22% vs current Low ~10-14%), unlock requirements: approve AI tooling for delivery team (GitHub Copilot/Claude), resolve G1002 pre-kick-off, define LGPD/TCU-compliant AI-assisted delivery policy, complete volumetrics audit, establish data model reconciliation plan across 7 legacy systems. Each unlock accelerates delivery and improves quality within same team shape.

**Expected outcomes** (post-Phase 1 go-live):

- Response time reduction: 2-4h → <1min for financial/ticket queries (3 months post-go-live Phase 1)
- CRM adoption increase: +40% (baseline 30% → target 70% final, 6 months post-go-live Phase 2)
- Repetitive inquiries reduction: -50% HR team acionamentos (3 months post-go-live Phase 1)
- Compliance risk mitigation: Zero proposals/contracts with incorrect approval threshold via automated verification (3 months post-go-live Phase 1)
- Organizational capacity recovery: ~2,400h/day (assume 50% realization of Slack '97 min/day/collaborator' metric × ~3k Dataprev staff, 6-12 months post-go-live Phase 1+Phase 2)
- NPS improvement: +20 points (baseline to be collected pre-Phase 1, 6 months post-go-live Phase 1)

---

**Document control:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Scopezilla narratives skill | Initial draft — executive audience |
