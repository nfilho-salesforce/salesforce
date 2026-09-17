# LATAM Agentic Governance Services
Source: Salesforce PS LATAM — Agentic Governance Services (Internal, July 2026)
Relevance: DER-SP is a regulated public-sector agency deploying an Agentforce agent that triages emergency calls (pane/sinistro) and, per the Riscos sheet, already carries an unaddressed governance gap ("Qualidade do Agente Conversacional" — no QA/monitoring owner identified) plus an LGPD gap (no DPO/consent flow named). Use this to scope a lightweight governance conversation alongside the MVP, not as a separate sold engagement unless the DER asks for one.

## Why This Applies Here (6 Risks, mapped to DER-SP gaps)
- Hallucinated Execution: Agentforce misclassifying pane vs. sinistro drives an incorrect dispatch — this is the exact "Qualidade do Agente Conversacional" risk already logged in the project's own Riscos matrix.
- Lack of Auditability: C2C manual overrides of automatic dispatch have no required audit trail today (Riscos: "Governança de Despacho").
- Compliance Failures: LGPD — geolocation + phone number + accident/victim data with no confirmed legal basis or DPIA (Riscos: "Dados Sensíveis / LGPD").
- Organizational Disruption: unclear human-agent handoff rules between the WhatsApp AI agent and C2C are still open (Adaptive Interview area).

## 5 Core Service Lines (for reference if DER wants a formal governance track)
1. Governance Assessment — Risk analysis, maturity assessment, governance roadmap. 4-8 weeks.
2. Framework Design — Policies, standards, compliance frameworks. 6-10 weeks.
3. Architecture Design — Security architecture, observability, integration patterns. 8-12 weeks.
4. Governance Implementation — Deploy tech stack, policy automation, training. 12-20 weeks.
5. Continuous Optimization — Monitoring, compliance, performance optimization. $250K-$1M/year.

## Sizing Guide
- 1-5 agents, single department → Governance Foundations → 12-16 weeks. **DER-SP fits here today** (one WhatsApp triage agent + one pending Coworker/Service Agent decision — well under the 10-agent threshold for Enterprise Governance).
- 10-50 agents, multi-department → Enterprise Governance → 6-9 months.
- 100+ agents, enterprise-wide → Strategic Transformation → 9-18 months.

## Top 5 Discovery Questions (useful as governance-specific prompts, distinct from the MVP Adaptive Interview)
1. Agent Inventory: how many autonomous agents are planned across the emergency MVP and the general Service Cloud attendance combined?
2. Data & Compliance: how is agent access to sensitive data (geolocation, phone, accident/victim details) restricted and logged?
3. Auditability: can every agent classification decision and every C2C manual override be traced after the fact?
4. Ownership: who owns agent quality/QA once the emergency MVP goes live — a named role, not just "C2C"?
5. Cost of Inaction: what is the operational/legal cost of a misclassified emergency dispatch, given this is a life-safety service?

## Positioning Note
Given this account is at "02 - Scoping" for a Field Service greenfield SOW (not a governance-specific sale), the right move is to fold the governance discovery questions above into the existing Adaptive Interview rather than pitch a separate governance engagement — unless the DER's own risk/compliance stakeholders raise it first.
