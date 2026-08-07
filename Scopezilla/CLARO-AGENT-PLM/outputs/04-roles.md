# Roles & Skills — Disciplines Required
## CLARO Agente PLM — POC PLM & Agentforce

**Version:** 1.0 · 2026-06-17

---

## Salesforce PS Team

### Technical Architect
**Allocation:** Full — 8 weeks · All phases

**Skills required:**
- Salesforce Agentforce Employee Agents — Atlas Reasoning Engine, subagent design, Agent Action wiring
- Einstein Platform — Prompt Templates, ConnectApi.EinsteinLLM invocation, Einstein Trust Layer configuration
- Apex architecture — Queueable chains, Transaction Finalizers, Database.Finalizer, Platform Events
- LGPD compliance architecture — data classification, rule lineage design, ETL controls
- DevOps — Salesforce CLI, RunSpecifiedTests, cross-org deploy patterns (CannotQuickDeployError mitigation)
- Custom Metadata architecture — CMDT families, Decision Tables, runtime tunables

**Phases active:** P0 (architecture lock) → P1 (Sprint 1–3 oversight + spikes) → P2 (LGPD controls, UAT support) → P3 (hypercare, KT lead)

---

### Technical Consultant
**Allocation:** Full — 8 weeks · All phases

**Skills required:**
- Apex development — Queueable chaining, byte-offset cursor, static Map cache patterns, AST walker algorithm
- Apex unit testing — ≥85% coverage, async test patterns, mock callout frameworks
- Lightning Web Components — file upload, data visualization panels, Salesforce UI framework
- Platform Events — publisher/subscriber trigger patterns, SHA-256 idempotency
- Salesforce CLI + SFDX — source-format deployment, `RunSpecifiedTests` execution
- Custom Metadata — seed data management, Decision Table configuration

**Phases active:** P0 (CMDT baseline) → P1 (primary build, all epics) → P2 (defect resolution, parallel run) → P3 (production deploy)

---

### QA Specialist
**Allocation:** 1.5 — 8 weeks · All phases

**Skills required:**
- Apex test strategy — unit coverage, integration test design for async Queueable chains
- Concurrency and stress testing — large-volume CSV simulation (up to 6M chars / 10k rows)
- Agentforce agent testing — conversation-based acceptance scenarios, precision measurement
- Defect management — Jira lifecycle, severity classification
- UAT facilitation — scripted acceptance testing with business users
- Parallel run coordination — comparing system outputs against legacy BRE

**Phases active:** P0 (test strategy, RunSpecifiedTests co-authorship) → P1 (Sprint 1–3 test execution) → P2 (UAT lead, concurrency tests, LGPD test evidence) → P3 (production smoke test)

---

### Project Manager
**Allocation:** Dedicated — 8 weeks · All phases  
**Billing:** Billable Salesforce PS resource, paid by Claro (not shared with Luciano/SWE)

**Skills required:**
- Agile / Scrum delivery governance
- Risk register management and escalation
- Client dependency tracking and escalation
- Stakeholder communication (PS ↔ Claro leadership)
- Formal project documentation (milestones, acceptance, close)

**Phases active:** All — continuous throughout engagement

---

## Claro Team Required

| Role | Person | Critical Window | Commitment |
|---|---|---|---|
| SME / Technical Discovery Lead | Lucas | Week 1 (CSV samples, schema) + UAT Weeks 6–7 | Weekly availability |
| SWE Lead / Infrastructure | Luciano | Weeks 1–2 (sandboxes, DevOps) + Week 8 (production deploy) | Active Weeks 1–2 and 8 |
| Operational Sponsor | Fabrício | Weeks 6–7 (UAT sign-off), Week 8 (steering) | Sign-off authority |
| Claro Legal | TBD | Week 6 (LGPD review — **hard gate**) | Scheduled review session |
| Operational Analysts (2–3) | TBD | Weeks 1–2 (KB Articles), Weeks 6–7 (UAT) | Half-days during UAT |

---

## Disciplines Matrix — Who Covers What

| Domain | PS TA | PS TC | PS QA | PS PM | Claro |
|---|---|---|---|---|---|
| Agentforce agent design | **Lead** | Support | — | — | Lucas (SME) |
| Apex engine development | Design | **Lead** | Test | — | — |
| LWC components | Design | **Lead** | Test | — | Lucas (layout) |
| Einstein Trust Layer / LGPD | **Lead** | Support | Evidence | — | Legal (sign-off) |
| DevOps / deploy pipeline | **Lead** | **Lead** | Registry | — | Luciano (infra) |
| Test strategy + execution | Design | Support | **Lead** | — | Analysts (UAT) |
| Delivery governance | — | — | — | **Lead** | Fabrício (sponsor) |
| Knowledge Articles / KB | — | — | — | Track | **Claro owns** |

---

*Note: One person may cover multiple roles. A 3.5-person PS team (TA + TC + 1.5 QA + PM) is consistent with the 8-week SC-complexity POC scope. Team sizing is benchmark-based — not a staffing commitment.*

`[KB:USB:96]` `[KB:USD:82]`
