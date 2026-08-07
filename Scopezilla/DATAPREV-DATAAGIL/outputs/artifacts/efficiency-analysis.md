# AI Delivery Efficiency Analysis — DATAPREV DATAAGIL

**Project:** DATAPREV DATAAGIL  
**Document:** AI Delivery Efficiency Analysis  
**Date:** 2026-07-19  
**Status:** Draft

---

## So What

**~10-14% realized delivery efficiency at Low readiness.** A pace and quality lift within the same team shape — not headcount reduction, not a pricing input.

Where the gains show up on this project:
- **Technical Engineering & QA** (~10-16%): MuleSoft API connector generation (E01/E02/E03/E06/E07) + Agentforce agent scaffolding (E06/E07) + 7-system integration test data synthesis (E10) — capped by legacy API discovery/validation + regulated context (LGPD/TCU audit trail human review)
- **Analysis & Design** (~14-20%): Agentforce conversational intent design (E06/E07) + Data Cloud unified data model (E09 — Contact B2B/employee reconciliation, 7-system fragmentation) + RAG corpus indexing (E04 normativas) — capped by 68 gaps (many Unknowns/Assumed) + Experience Design gap (G0104/G0402/G0505)
- **Documentation & Knowledge Management** (~14-23%): RAG corpus curation (E04 normativas + Slack AI) + training materials by persona (E10 — B2B/executivos/comercial/N1-N2/Pessoas) + LGPD/TCU audit trail docs — capped by compliance-sensitive content (alçadas, perfil de acesso) requiring Jurídico/DPO human review every iteration

**Roles that capture the most**: Agentforce Technical Consultant (conversational intent design + agent scaffolding), Data Cloud Technical Architect (unified data model + predictive segmentation), Solution Consultant (BA + training materials by persona).

**Where AI does not help**: Protheus governance blocker resolution (G1002 — TI+Jurídico+DPO tri-party negotiation), Workspace Slack segregation decision (G0101 — Jurídico approval unknown), Clarity migration strategy (G0801 — hard-to-reverse decision), Experience Design for 10k+ users (G0104/G0402/G0505 — user research + service design), RACI + CoE charter facilitation (G9901/G1001/G1003 — political alignment), executive mandate enforcement (Saulo >60% adoption KPIs) — plus highest-AI-tax work is 7-system integration orchestration (Pronto, Clarity, Protheus, CRM Totvs, Conexão, Teams, SEI) + regulated compliance review (LGPD/TCU manual audit trail for every AI output).

**To move up to High readiness (~18-22%)**: Approve GitHub Copilot/Claude for PS delivery team (currently no AI tooling in use), resolve Protheus governance blocker G1002 pre-kick-off (TI+Jurídico+DPO tri-party meeting), define LGPD/TCU-compliant AI-assisted delivery policy (what level of human review required), complete volumetrias audit (G0102/G0201/G0302/G0701 — data hygiene baseline), establish data model reconciliation plan across 7 legacy systems.

---

## Headline

**Realized: ~10-14%** (Low readiness) · **Task-level blend: ~30-40%** · **Realization factor: 0.40-0.45** — Multi-cloud mixed config + custom dev (7 legacy integrations + Agentforce + Data Cloud) at established enterprise client with regulated context (LGPD/TCU) · **Confidence: Assumed**

---

## Client-Readiness Scenarios

| Scenario | Realized Band | Notes |
|---|---|---|
| **Low readiness (current: ✓)** | ~10-14% | Current state per discovery signals. Gains stay modest until AI tooling approved for delivery team, Protheus governance blocker resolved (G1002), and compliance review process streamlined (LGPD/TCU manual audit trail for every AI output suppresses velocity). |
| Mid readiness | ~12-18% | Tooling unlocked, governance blocker resolved, compliance policy defined. Delivery team captures standard multi-cloud gains — config/doc acceleration + API connector generation + test data synthesis. |
| High readiness | ~18-22% | Conditions favor upper end: tooling + governance unblocked + data hygiene baseline + unified data model plan. Faster client with clean data captures more of the AI upside. |

**Current scenario**: Low readiness (score 2/8)

### Signals behind the score

- **AI tooling posture**: 0/2 — No AI tooling adoption signals in discovery (no mention of GitHub Copilot, Claude, Cursor, or similar developer tools). Huawei partnership (fev/2026) is pilot-phase research, not delivery tooling for implementation team.
- **Delivery velocity / speed bias**: 1/2 — Competing pressures: mainframe sunset (jan/2026) + data breach (mai/2026) motivate urgency, BUT 68 gaps (many Unknowns) + Protheus governance blocker (G1002) unresolved + conservative federal-gov bureaucracy slow decision cycles. Mid velocity assumed.
- **Data & environment hygiene**: 1/2 — Mixed signals: 7 legacy systems fragmented (Pronto, Clarity, Protheus, CRM Totvs, Conexão, Teams, SEI) with no unified data model today (hygiene risk), BUT volumetrias unknown (G0102/G0201/G0302/G0701) — capacity planning blocked. Mid hygiene assumed.
- **Legal / security / compliance posture**: 0/2 — Active blockers: Protheus governance blocker G1002 (TI+Jurídico+DPO tri-party approval pending), LGPD breach incident (2.8M CPFs mai/2026), TCU audit scrutiny. Compliance-heavy slows AI adoption (every model output needs human review for audit trail).

### What it takes to move up

- **Low → Mid**:
  - Approve GitHub Copilot/Claude for PS delivery team (currently no AI tooling in use)
  - Resolve Protheus governance blocker G1002 pre-kick-off (TI+Jurídico+DPO tri-party meeting)
  - Define LGPD/TCU-compliant AI-assisted delivery policy (what level of human review required for model-generated code/config/docs)

- **Mid → High**:
  - Volumetrias audit complete (G0102/G0201/G0302/G0701) — data hygiene baseline established before F1
  - Data model reconciliation plan across 7 legacy systems (Contact B2B + employee unification, Case/Ticket Pronto history, Opportunity/Demand CRM Totvs) — reduces integration rework

---

## By Category

### Technical Engineering & QA — realized ~10-16% (task-level ~25-35%)

- **Driving epics**: E01 (L — Consultas Financeiras Self-Service), E02 (M — Autoatendimento Chamados Técnicos), E03 (M — Intelligence Executiva Mobile), E06 (L — Adoção CRM via Conversação), E07 (M — Abertura de Chamados Assistida), E08 (XL — Gestão de Demandas Evolutivas)
- **How it shows up here**: MuleSoft API connector generation (7 System APIs E01/E02/E03/E06/E07 + E08 Clarity unknown API) + Agentforce agent scaffolding (E06/E07 F2 writes) + test data synthesis (7-system integration testing E10). AI accelerates API mapping + boilerplate connectors [3], but legacy system API discovery/validation + Clarity API unknown (G0801) remain human-only. Multi-system integration testing (Pronto + CRM Totvs + Protheus + Clarity + Conexão + Teams + SEI) stays complex — AI generates synthetic test data but orchestration + regression testing review is human-led [5]. Cap: regulated context (LGPD/TCU audit trail) requires human review every API call logging implementation + Protheus perfil de acesso enforcement logic.

### Analysis & Design — realized ~14-20% (task-level ~35-45%)

- **Driving epics**: E04 (L — Knowledge Base Normativas RH), E06 (L — Adoção CRM via Conversação), E08 (XL — Gestão de Demandas Evolutivas), E09 (XL — Intelligence Preditiva e Recomendações), E10 (XL — Governança, Compliance e Change Management)
- **How it shows up here**: Agentforce conversational intent design (E06/E07 J4/J3 — field mapping from voice/text to API required fields) + Data Cloud unified data model (E09 — Contact B2B/employee reconciliation, Case/Ticket Pronto 4+ related objects, Opportunity/Demand CRM Totvs) + RAG corpus indexing strategy (E04 Portal Conexão normativas + Slack AI channel recaps). AI drafts intent skeletons + data model mappings [2], but 68 gaps (many Unknowns/Assumed) + 7-system fragmentation force iteration. Experience Design gap (G0104/G0402/G0505 — 10k+ external users onboarding, no UX research scoped) caps conversational flow design quality without pilot feedback. Governance gap (G9901/G1001/G1003 — multi-team ownership RACI, data stewardship, Agentforce prompt governance) remains human-negotiation-heavy [6].

### Documentation & Knowledge Management — realized ~14-23% (task-level ~35-50%)

- **Driving epics**: E04 (L — Knowledge Base Normativas RH), E10 (XL — Governança, Compliance e Change Management)
- **How it shows up here**: RAG corpus curation (E04 — Portal Conexão normativas indexing + Slack AI channel recaps federation) + training materials by persona (E10 — B2B clients J1, executivos J5, comercial J4/J6, N1/N2 J2/J3, Pessoas J7) + compliance audit trail docs (LGPD/TCU rastreabilidade every API call + Protheus perfil de acesso governance). AI drafts training modules + normativa summaries + audit trail templates [2][7], but compliance-sensitive content (alçadas 2 milhões de reais, perfil de acesso governance model) requires Jurídico/DPO human review every iteration — regulatory conservatism caps velocity. TCU audit trail design (every API call logged with user ID + timestamp + query/mutation) benefits from AI-generated templates but final approval human-gated.

### Project Management & Operations — realized ~6-11% (task-level ~15-25%)

- **Driving epics**: E10 (XL — Governança, Compliance e Change Management)
- **How it shows up here**: Change management execution (E10 — early adopters program 20-50 pilot users F1, executive mandate Saulo adoption KPIs >60% uso semanal F2, adoption monitoring dashboard CRM Analytics). AI drafts status summaries + adoption dashboards [2], but stakeholder alignment (Saulo executive sponsor + TI+Jurídico+DPO tri-party Protheus governance blocker G1002) + conflict resolution (multi-team ownership RACI G9901/G1001) stay human-only. Phase sequencing (F0 blocker resolution → F1 → F2 adoption gate → F3) benefits modestly from AI risk flagging but dependency tracking (G1002 Protheus governance blocker mandatory before F1) is human-driven.

---

## By Role Type

### Senior Technical Architect — realized ~12-18% (task-level ~30-40%)

- **Amplified**: API design (MuleSoft 7-system System APIs + Agentforce MCP federation), Security architecture (LGPD Art. 48 + TCU audit trail + Slack EKM), Integration patterns (API-led connectivity System + Process + Experience)
- **Still human-only**: Protheus governance blocker resolution (G1002 — TI+Jurídico+DPO tri-party negotiation), Org strategy decision (single org vs multi-org — no regulatory isolation signal in discovery)
- **How the day changes**: API design gains: AI drafts MuleSoft System API skeletons + Swagger/OpenAPI specs from legacy system discovery [3], but Clarity API unknown (G0801 — no KB coverage) + Protheus governance blocker (G1002 — perfil de acesso model TI+Jurídico+DPO approval) require human validation. Security architecture (LGPD/TCU audit trail every API call + Slack EKM AWS KMS instant revocation) AI-drafts baseline but compliance review human-gated. CoE governance (multi-team ownership RACI G9901/G1001/G1003) stays negotiation-heavy — AI summarizes options, people decide.

### Agentforce Technical Consultant — realized ~12-18% (task-level ~30-40%)

- **Amplified**: Conversational intent design (10 jornadas J1-J10 — voice/text field mapping), Agent scaffolding (Agentforce Atlas Reasoning Engine orchestration), Confidence tuning (F1 early adopters feedback iteration)
- **Still human-only**: Experience Design gap (G0104/G0402/G0505 — 10k+ users onboarding, no UX research scoped), Agentforce prompt governance (G1001 — who owns prompt iteration? multi-team RACI)
- **How the day changes**: Intent design acceleration: AI drafts conversational field mappings from API specs (Protheus financials, Pronto ticket creation, CRM Totvs pipeline updates) [2][4], but Experience Design gap (no usability testing with pilot users F1 J1/J2) caps flow quality without iteration feedback. Agentforce proactive activation (J9 SLA breach alerts + J10 pipeline recommendations F3) benefits from AI-generated segmentation logic drafts, but Data Cloud ingestion architecture (Pronto + CRM Totvs CDC validation) human-validated. 10 jornadas (5 read-only F1, 2 writes F2, 2 proactive F3 + 1 scheduling F1) — AI scaffolds agents faster but governance model (who approves prompt changes? G1001) unresolved slows iteration.

### MuleSoft Technical Architect — realized ~10-16% (task-level ~25-35%)

- **Amplified**: API-led connectivity pattern design (System + Process + Experience layers), Capacity planning (volumetrias audit + rate limiting design), Rastreabilidade LGPD/TCU (every API call logging architecture)
- **Still human-only**: Volumetrias unknown (G0102/G0201/G0302/G0701 — capacity planning blocked until Phase 0 audit), Clarity API compatibility validation (G0801 — external dependency risk, no KB coverage)
- **How the day changes**: API architecture gains: AI drafts System API layer specs + rastreabilidade logging patterns [1][3], but volumetrias unknown (4 gaps G0102/G0201/G0302/G0701) blocks capacity planning until Phase 0 audit — AI can't invent load profiles. Clarity API unknown (G0801 — Broadcom API undocumented or brittle) requires TI-provided Swagger/OpenAPI specs + sandbox credentials Phase 0 discovery sprint (2 weeks) before AI-assisted connector build viable. MuleSoft/MCP dual deployment (Anypoint for legacy APIs, MCP Server for Slack federation G9902) — AI drafts architecture decision doc but protocol choice human-validated per Salesforce best practices.

### Data Cloud Technical Architect — realized ~12-18% (task-level ~30-40%)

- **Amplified**: Unified data model design (Contact B2B/employee reconciliation, Case/Ticket/Opportunity history), Streaming architecture (Pronto ServiceNow + CRM Totvs CDC ingestion), Predictive segmentation (SLA breach cohort, churn-risk cohort)
- **Still human-only**: Historical data load sizing decision (if >500k records, performance/cost implications — volumetrias unknown G0701), Einstein Discovery ML-based vs rule-based decisioning (business rule complexity unknown)
- **How the day changes**: Data model gains: AI drafts Contact B2B + employee unification schema + Case/Ticket Pronto 4+ related objects reconciliation [2], but 7-system fragmentation (no unified model today) + volumetrias unknown (G0701) makes historical load sizing guesswork without Phase 0 audit. Data Cloud streaming architecture (Pronto + CRM Totvs CDC ingestion G0901) AI-drafts event-driven pattern but validation blocked until TI provides API specs + data model mappings. Predictive segmentation (J9 SLA breach alerts + J10 pipeline recommendations F3) — AI scaffolds Einstein Discovery models but business rule complexity (what defines churn-risk cohort?) human-defined. First-time Dataprev production Data Cloud deployment may require Salesforce vendor support F3 (limited precedent).

### Solution Architect — realized ~10-16% (task-level ~25-35%)

- **Amplified**: Service Cloud configuration + implementation, Slack Workspace architecture decision (G0101 — single vs dual workspace), Cross-cloud orchestration (Service Cloud + Agentforce + MuleSoft + Data Cloud)
- **Still human-only**: Workspace Slack segregation decision (G0101 — B2B vs internos, Jurídico approval unknown), Clarity migration strategy (G0801 — co-living vs Service Cloud replacement, hard-to-reverse decision deferred F2)
- **How the day changes**: Config gains: AI drafts Service Cloud Flow orchestration + Slack Canvas UX mockups (J1/J2/J5/J7/J8) [2], but Workspace Slack segregation (G0101 — single recommended, dual if Jurídico requires) unresolved blocks Slack admin setup. Clarity migration strategy (G0801 — co-living API writes vs. Service Cloud full replacement, 4.5k active demands migrate) hard-to-reverse decision deferred F2 architecture gate after F1 adoption validated — AI drafts both paths but choice human-gated. Slack Canvas UX design (conversational flow + help content) benefits from AI-generated mockups but Experience Design gap (G0104/G0402/G0505 — no usability testing scoped) caps quality without pilot feedback F1.

### Solution Consultant — realized ~12-18% (task-level ~30-40%)

- **Amplified**: Business analysis (20-phase-0-gap resolution, user stories per persona), Training materials by persona (B2B/executivos/N1-N2/Pessoas), Adoption monitoring dashboard setup (CRM Analytics uso semanal %)
- **Still human-only**: RACI + CoE charter facilitation (G9901/G1001 — multi-team ownership decision rights, data stewardship), Executive mandate enforcement (Saulo adoption KPIs >60% uso semanal F2 — dashboard monitored weekly, non-adopters escalated)
- **How the day changes**: BA gains: AI drafts user stories per persona + training module outlines [2][7], but 68 gaps (many Unknowns/Assumed) + governance gap (G9901/G1001/G1003 — multi-team ownership RACI unresolved) force iteration. Training materials (Trailhead modules + video library + Slack Canvas help content) AI-generated but persona-specific content (B2B clients J1, executivos J5, comercial J4/J6, N1/N2 J2/J3, Pessoas J7) requires CM Lead human validation per client culture. Adoption monitoring dashboard (CRM Analytics: uso semanal %, agent adoption by persona, API call volume/error rate, audit log compliance metrics) AI-drafts baseline but executive mandate (Saulo enforces >60% target F2) + non-adopter escalation workflow human-driven.

### Quality Assurance Consultant — realized ~12-20% (task-level ~30-45%)

- **Amplified**: Test data synthesis (7-system integration testing), Test case generation (unit testing MuleSoft API connectors + Agentforce intent parsing), Performance testing (F1 MuleSoft API rate limits + F3 Data Cloud streaming throughput)
- **Still human-only**: Security testing (LGPD/TCU audit trail verification — every API call logged correctly), UAT per phase F1/F2/F3 scale validation (pilot users → early adopters → full scale)
- **How the day changes**: Test generation gains: AI synthesizes test data for 7-system integration (Pronto, Clarity, Protheus, CRM Totvs, Conexão, Teams, SEI) + generates unit test cases for MuleSoft API connectors [3][5], but multi-system regression testing (F2/F3 scale — ensure F1 read-only jornadas remain operational when F2 writes enabled) stays human-orchestrated. Security testing (LGPD/TCU audit trail verification + Slack EKM instant revocation tested) human-led — compliance context requires Jurídico/DPO review every audit log validation. Performance testing (F1 MuleSoft API rate limits validated against volumetrias + F3 Data Cloud streaming throughput) blocked until volumetrias audit complete (G0102/G0201/G0302/G0701 Phase 0) — AI generates load test scripts but capacity targets human-defined post-audit.

### UX Researcher — realized ~8-14% (task-level ~20-30%)

- **Amplified**: Conversational flow iteration (Agentforce voice/text + Slack Canvas UX), Usability testing synthesis (J1/J2 pilot feedback 20-50 early adopters F1)
- **Still human-only**: Service design for 10k+ external users onboarding (Experience Design gap G0104/G0402/G0505 — no UX research scoped initially), Accessibility compliance validation (LGPD + federal gov standards)
- **How the day changes**: Flow iteration gains: AI drafts conversational flow variants + Slack Canvas UX mockups from pilot feedback [2], but Experience Design gap (G0104/G0402/G0505 — 10k+ external users onboarding, no UX research scoped) means no usability testing baseline F1 unless added. Service design for J3 (Abertura Chamados Assistida) + J4 (Adoção CRM Conversacional) human-led — AI generates flow options but user research (what questions do 10k+ B2B clients ask? what language do they use?) not automatable. Accessibility compliance (LGPD + federal gov standards) human-validated — AI flags WCAG gaps but Jurídico approval required.

### Change Management Lead — realized ~6-11% (task-level ~15-25%)

- **Amplified**: Training delivery materials by persona, Adoption monitoring dashboard (CRM Analytics uso semanal %)
- **Still human-only**: Early adopters program facilitation (20-50 pilot users F1 — champions identified, trained first), Executive mandate support (Saulo enforces adoption KPIs >60% uso semanal F2 — non-adopters escalated)
- **How the day changes**: CM gains: AI drafts training materials + adoption dashboard templates [2], but early adopters program (20-50 pilot users F1 — who are the champions? how to incentivize?) human-facilitated. Executive mandate (Saulo enforces >60% uso semanal target F2) + non-adopter escalation workflow human-driven — AI flags low-adoption cohorts but executive relationship management not automatable. Training by persona (B2B clients J1, executivos J5, comercial J4/J6, N1/N2 J2/J3, Pessoas J7) AI-generated but persona-specific delivery (what resonates with federal gov B2B clients vs. internal comercial?) requires CM Lead human judgment per client culture.

---

## Human-Only Work

- **Protheus Governance Blocker Resolution (G1002)** — TI+Jurídico+DPO tri-party meeting negotiation (perfil de acesso model approval) — legal/political alignment across three internal stakeholders. AI can draft governance models but cannot negotiate tri-party sign-off.
- **Workspace Slack Segregation Decision (G0101)** — Jurídico approval unknown (B2B vs internos workspace segregation) — legal interpretation of data isolation requirements. AI can draft both options but Jurídico approval human-gated.
- **Clarity Migration Strategy (G0801)** — Hard-to-reverse decision (co-living vs Service Cloud replacement, 4.5k active demands migrate) deferred F2 architecture gate — business risk assessment + vendor relationship implications (Broadcom Clarity co-living governance). AI drafts both paths but choice human-gated.
- **Experience Design for 10k+ Users (G0104/G0402/G0505)** — User research (what questions do 10k+ B2B clients ask? what language?) + service design (onboarding flow for federal gov users) — human empathy + domain context. AI generates flow variants but pilot feedback interpretation not automatable.
- **RACI + CoE Charter Facilitation (G9901/G1001/G1003)** — Multi-team ownership decision rights (Agentforce config, MuleSoft APIs, Slack admin), data stewardship (CRM Totvs vs Salesforce truth?), CoE structure — political alignment across internal stakeholders. AI drafts RACI templates but stakeholder negotiation human-driven.
- **Executive Mandate Enforcement (Saulo >60% Adoption KPIs)** — Executive relationship management (Saulo enforces adoption, non-adopters escalated) — trust-building + influence. AI flags low-adoption cohorts but executive persuasion not automatable.
- **Project Pulse Reports** — Trust-building work that AI can summarize but not facilitate — stakeholder pulse (Saulo satisfied? TI/Jurídico/DPO aligned?) requires human judgment.
- **Stakeholder Alignment** — Human-to-human negotiation across TI+Jurídico+DPO tri-party + executive sponsor Saulo — AI drafts positions, people decide.
- **Conflict Resolution** — Human judgment — multi-team ownership RACI conflicts (who owns Agentforce prompt changes? G1001) require negotiation.

---

## Assumptions & Caveats

- Task-level gains come from published 2022–2026 studies; realization factor (0.40–0.45) accounts for Amdahl's law, review/AI-tax overhead, and unmoved human-barrier work.
- **Honest range for coding**: RCT evidence spans −19% (METR 2025 [1], mature OSS) to +21% (Paradis/Google 2024 [4], complex enterprise) to +55% (Peng/GitHub 2022 [3], greenfield lab). The realistic-enterprise row (~25-35% task-level) is the defensible starting point for Salesforce integration and custom work (7 legacy API connectors + Agentforce + Data Cloud).
- Individual gains ≠ team gains: DORA 2024 [5] measured individual productivity rising while delivery stability and throughput fell. Ground claims in project-level outcomes, not developer self-report.
- Model capability is racing ahead of realized workflow gains (Stanford HAI 2026 [9]); that gap is why project-level bands stay in ~10-25% even as task-level benchmarks improve. Amdahl's law + review overhead + human-barrier work (governance, stakeholder alignment, compliance) cap realized gains below task-level blend.
- Bands are qualitative and project-specific — no hours, FTE, or cost implications are computed or implied. This analysis is a pace and quality lift within the same team shape, not a headcount reduction signal or pricing input.
- Realization factor assumes AI tooling is approved for delivery team (currently Low readiness per discovery — no AI tooling signals observed, Protheus governance blocker G1002 unresolved, compliance-heavy LGPD/TCU context). Moving to Mid/High readiness requires unlocks listed in scenarios.
- Regulated context (LGPD Art. 48 + TCU audit trail) modestly reduces realized gains — every API call logging implementation + compliance docs require human review (Jurídico/DPO approval). Conservative federal-gov bureaucracy slows decision cycles.
- 7-system integration (Pronto, Clarity, Protheus, CRM Totvs, Conexão, Teams, SEI) + 68 gaps (many Unknowns/Assumed) + volumetrias unknown (G0102/G0201/G0302/G0701) increase iteration overhead — AI accelerates but validation blocked until Phase 0 audit complete.
- Experience Design gap (G0104/G0402/G0505 — 10k+ external users onboarding, no UX research scoped) caps conversational flow quality without pilot usability testing F1. If UX researcher added, realized band shifts modestly upward (+2-3 percentage points) in Analysis & Design category.
- Client readiness score (2/8 — Low readiness scenario) derived from discovery signals: no AI tooling adoption observed, Protheus governance blocker unresolved (G1002), LGPD breach incident (mai/2026) + TCU audit pressure active, 7-system fragmentation + volumetrias unknown. Score increases if unlocks executed (see scenarios).
- Regulated context (LGPD/TCU) + 68 gaps (many Unknowns/Assumed) + Protheus governance blocker (G1002) + volumetrias unknown (4 gaps) create higher-than-average iteration overhead vs. typical multi-cloud engagement. Realized band may shift upward (+2-4 percentage points) if Phase 0 gap resolution successful + AI tooling approved.

---

## Sources

1. **METR (July 2025)** — RCT of experienced OSS developers; measured ~19% slowdown despite perceived ~20% speedup.
2. **BCG × Harvard (2023, 2025 pilots)** — 12.2–40% time savings on in-scope tasks; "jagged frontier" degrades on out-of-scope tasks.
3. **Peng et al., GitHub (2022)** — lab RCT, 95 devs on a greenfield HTTP-server task; ~55% faster, 95% CI [21%, 89%].
4. **Paradis et al., Google (arXiv 2410.12944, 2024)** — RCT of 96 Google engineers on a complex enterprise task; ~21% time reduction with wide CI. Counterweight to [1].
5. **DORA 2024 State of DevOps** — first rigorous team-level measurement that individual AI productivity gains coexist with decreased delivery stability and throughput.
6. **DORA 2025** — "AI is an amplifier" of existing sociotechnical systems; qualitative, supplement to [5].
7. **McKinsey (2025)** — 30-45% doc drafting savings in enterprise consulting context.
8. **GitClear (2025)** — measured code churn increase (more reverts, more context switches) in production AI-assisted development.
9. **Stanford HAI AI Index 2026** — capability benchmarks outrunning realized workflow gains by 18-24 months; deployment lag.

---

**Document control:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Scopezilla efficiency skill | Initial draft |
