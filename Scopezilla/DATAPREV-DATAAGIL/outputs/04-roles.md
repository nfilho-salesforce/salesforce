# Roles & Skills — Disciplines Required

**Project:** DATAPREV DATAAGIL  
**Document:** Required Disciplines & Phase Coverage  
**Date:** 2026-07-19  
**Status:** Draft

---

## Framing

This document identifies the disciplines this engagement requires. **One person may fill multiple roles; one role may be filled by multiple people.** Team sizing, FTE counts, and staffing are not within this artifact's scope — those require human judgment based on Salesforce PS's capacity, delivery model, and commercial terms.

---

## Executive Summary

The engagement demands **expertise across 11 disciplines** spanning architecture, product specialization, delivery, and governance:

**Architecture & Integration:** Senior Technical Architect (security, governance included), MuleSoft Technical Architect (7-system integration hub)

**Product Specialists:** Solution Architect (Service Cloud, Slack), Data Cloud Technical Architect, Agentforce Technical Consultant, MuleSoft Technical Consultant (integration builds)

**Experience & Delivery:** UX Researcher (10k+ users), Solution Consultant (BA + release mgmt), Quality Assurance Consultant (7-system + agent testing)

**Governance:** embedded in Senior Technical Architect (CoE, security stewardship)

All disciplines active across Phase 0 → Phase 3 with ramp patterns matching the phase sequence. Architects stay through go-live + hypercare; specialists ramp in/out by phase scope.

---

## Disciplines by Phase

| Discipline | Phases Active | Rationale |
|-----------|--------------|-----------|
| **Senior Technical Architect** | 0,1,2,3 | Architecture decisions (org strategy, integration patterns, API design), security architecture (LGPD Art. 48 + TCU audit trail + Slack EKM AWS KMS instant revocation), governance/CoE leadership (multi-team decision rights, data stewardship, Agentforce prompt governance, MuleSoft API governance per G9901/G1001/G1003) |
| **MuleSoft Technical Architect** | 0,1,2,3 | MuleSoft Anypoint Platform architecture (7-system System APIs: Protheus ERP, Pronto ServiceNow, CRM Totvs, Portal Conexão SharePoint, MS Teams Graph API, Clarity Broadcom, SEI future), API-led connectivity pattern (System + Process + Experience), rastreabilidade LGPD/TCU (every API call logging design), capacity planning (volumetrias from Phase 0 audit + rate limiting + Heroku dynos sizing) |
| **Solution Architect** | 0,1,2,3 | Service Cloud configuration + implementation, Slack administration (Workspace decision G0101 — single or dual workspace architecture + DLP control + Slack Canvas UX for J1/J2/J5/J7/J8), cross-cloud orchestration (Service Cloud + Agentforce + MuleSoft + Data Cloud unified model) |
| **Data Cloud Technical Architect** | 2,3 | Data Cloud streaming architecture (G0901 — Pronto ServiceNow + CRM Totvs CDC ingestion validation + event-driven pattern), unified data model (Contact B2B client + internal employee, Case/Ticket history Pronto 4+ related objects, Opportunity/Demand history CRM Totvs — complex multi-source reconciliation), Einstein Discovery ML-based vs rule-based decisioning, historical data load sizing (if >500k records, performance/cost implications) |
| **UX Researcher** | 0,1,2 | Experience Design gap resolution (G0104/G0402/G0505 — 10k+ external users onboarding sem UX research scoped), J1/J2 usability testing with 20-50 early adopters F1, conversational flow iteration (Agentforce voice/text + Slack Canvas UX before F2/F3 scale), service design for J3 (Abertura Chamados Assistida) + J4 (Adoção CRM Conversacional) |
| **Agentforce Technical Consultant** | 1,2,3 | Agentforce agent build (10 jornadas J1-J10 — 5 read-only F1, 2 controlled writes F2, 2 proactive F3 + 1 scheduling F1), conversational intent design + testing (voice + text input validation, field mapping from conversational input to API required fields), Agentforce proactive activation (push alerts Slack channels/DMs for J9 SLA breach + J10 pipeline recommendations), confidence tuning (F1 early adopters feedback → agent iteration) |
| **MuleSoft Technical Consultant** | 1,2,3 | MuleSoft connector build (7 System APIs F1 read-only, 2 write APIs F2 — Pronto case creation + CRM Totvs pipeline updates), field mapping + transactional integrity validation (G0601/G0701 — CRM Totvs/Pronto write API compatibility), retry logic + error handling (robust validation for F2 controlled writes), volumetrias-driven capacity planning implementation (MuleSoft API rate limiting actual configuration post-Phase 0 audit) |
| **Solution Consultant** | 0,1,2,3 | Business analysis (20-phase-0-gap resolution, user stories per persona B2B/executivos/N1-N2/Pessoas), release management (4-phase deliveries F0→F1→F2→F3), training + change management coordination (formal training sessions by persona F1, Trailhead modules + video library + Slack Canvas help content, adoption monitoring dashboard setup), RACI + CoE charter facilitation (G9901/G1001 — multi-team ownership decision rights/data stewardship) |
| **Quality Assurance Consultant** | 1,2,3 | Testing strategy execution (unit testing per-epic MuleSoft API connectors + Agentforce intent parsing + Salesforce Flow orchestration, integration testing cross-system 7 systems + Agentforce end-to-end, UAT per phase F1/F2/F3 scale validation), performance testing (F1 MuleSoft API rate limits validated against volumetrias + F3 Data Cloud streaming throughput), security testing (LGPD/TCU audit trail verification — every API call logged correctly + Slack EKM instant revocation tested), regression testing (F2/F3 scale — ensure F1 read-only jornadas remain operational when F2 writes enabled) |
| **Technical Project Manager** | 0,1,2,3 | Phase sequencing (F0 blocker resolution → F1 → F2 adoption gate → F3), dependency tracking (Phase 0 G1002 Protheus governance blocker resolution mandatory before F1 start + F1 >60% uso semanal adoption before F2 writes + F2 CRM adoption validated before F3 Data Cloud ingestion), risk mitigation execution (top 10 risk table — escalate Protheus governance blocker to seller immediately if TI+Jurídico+DPO não aprovar), hypercare coordination (2 weeks post-go-live per phase F1/F2/F3 — architect + admin + QA on-call) |
| **Change Management Lead** | 1,2,3 | Training delivery (by persona: B2B clientes J1, executivos J5, comercial J4/J6, N1/N2 J2/J3, Pessoas J7, all J8), early adopters program (20-50 pilot users F1 — champions identified, trained first, usage validated before F2/F3 scale), executive mandate support (Saulo enforces adoption KPIs >60% uso semanal F2 — dashboard monitored weekly, non-adopters escalated), adoption monitoring dashboard (CRM Analytics: uso semanal %, agent adoption by persona, API call volume/error rate, audit log compliance metrics — updated daily, reviewed weekly by CM Lead + Saulo) |

---

## Assumptions

- **Multi-disciplinary staffing:** Headcount typically < role count (e.g., senior dev covering Apex + integration, BA covering release management on small teams)
- **Client-side roles:** assumes client provides Product Owner + executive sponsor (Saulo) + TI/Jurídico/DPO tri-party meeting attendees Phase 0 for Protheus governance G1002 blocker resolution
- **Governance resolution:** assumes Phase 0 or early F1 RACI finalized (G9901/G1001/G1003 — multi-team ownership decision rights, data stewardship, Agentforce prompt governance, MuleSoft API governance)
- **Experience Design opt-in:** UX Researcher active F0/F1/F2 to resolve G0104/G0402/G0505 gap (10k+ external users onboarding); if client handles UX internally, this discipline drops
- **Data Cloud specialist:** Data Cloud Technical Architect active F2/F3 only (not F0/F1) — F3 proactive intelligence phase; may require Salesforce vendor support engagement (first-time Dataprev production Data Cloud deployment)
- **Change Management resourcing:** CM Lead assumes dedicated role F1→F3 given 10k+ users + executive mandate adoption KPIs enforcement; smaller engagements often fold CM into BA/PM

---

## Risks

- **Protheus governance blocker (G1002) — CRITICAL:** If TI+Jurídico+DPO não aprovar Protheus financial data access Phase 0, entire F1 J1 jornada inviável → escalate to seller immediately before proposal submission. Fallback: defer J1 to F2, launch F1 with J2/J5/J7/J8 only (4 jornadas instead of 5) — reduces early wins but unblocks F1.
- **Volumetrias unknown (G0102/G0201/G0302/G0701):** MuleSoft/Agentforce/Heroku capacity planning blocked without Phase 0 audit → risk under-provisioning (performance degradation) or over-cost (over-sized infrastructure). Mandatory Phase 0 volumetrias audit before F1 kick-off.
- **Clarity API compatibility unknown (G0801 — no KB coverage):** Broadcom Clarity API undocumented or brittle (external dependency risk) → entire E08 blocked. F1 Phase 0 API discovery sprint required (2 weeks, TI provides Swagger/OpenAPI specs + sandbox credentials). Fallback: recommend Service Cloud migration immediately (no co-living option) — 4.5k active demands migrate to Service Cloud Case, Clarity becomes read-only archive (hard-to-reverse decision deferred to F2 gate).
- **Data Cloud first-time deployment:** Limited Dataprev production precedent → may require Salesforce Data Cloud specialist vendor support engagement F3 (budget/timeline impact). Mitigate: architect + vendor support scoped F3.
- **Multi-disciplinary resource pool:** If Salesforce PS capacity constrained (single architects covering multiple products), phase ramp may serialize (slower) vs parallel (faster). Mitigate: resource plan early visibility + escalate to delivery lead if bottleneck.

---

**Document control:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | 2026-07-19 | Scopezilla roadmap skill | Initial draft |
