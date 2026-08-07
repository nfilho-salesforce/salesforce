# Dual-Track Estimate Comparison — DATAPREV DATAAGIL

**Project:** DATAPREV DATAAGIL  
**Date:** 2026-07-19  
**Status:** SSSL-approved starting point  
**Currency:** BRL (Reais Brasileiros)

---

## At a Glance

| Lane | Duration | Team at Peak | Indicative Price Range |
|---|---|---|---|
| **Traditional** (offshore-weighted) | 29–54 semanas | 12–15 pessoas | See Approved Commercials below |
| **Quantum Leap** (AI-native, senior-core) | 25–49 semanas | 10–11 pessoas | See Approved Commercials below |
| **Delta** | ~14-9% faster | ~17-27% fewer | ~34-36% lower |

**QL qualification**: ✓ Committed-delivery (Dataprev qualifies for AI-native joint operating model)

---

## Approved Commercials

### Traditional Lane — Indicative Price Range

**R$ 12.072.207 – R$ 31.270.806** (bill rates COM impostos, daily basis)

**Effort basis (top-down from engagement shape):**
- Duration: 29–54 semanas (203–378 dias úteis, 5-day workweek)
- Capacity by class:
  - Onshore-architect (R$ 7.195/day blended): 4–5 range
  - Onshore-developer (R$ 5.563/day blended): 3–4 range
  - Offshore (R$ 3.500/day assumed): 4–7 range

**Arithmetic**: Σ(class rate × class capacity) × duration
- Low: (R$ 7.195 × 4 + R$ 5.563 × 3 + R$ 3.500 × 4) × 203 = R$ 59.469/day × 203 = **R$ 12.072.207**
- High: (R$ 7.195 × 5 + R$ 5.563 × 4 + R$ 3.500 × 7) × 378 = R$ 82.727/day × 378 = **R$ 31.270.806**

### Quantum Leap Lane — Indicative Price Range

**R$ 7.957.075 – R$ 19.971.861** (bill rates COM impostos, daily basis)

**Effort basis (top-down from engagement shape):**
- Duration: 25–49 semanas (175–343 dias úteis, 5-day workweek) — Traditional compressed by efficiency Low readiness ~10-14%
- Capacity by class:
  - Onshore-architect (R$ 7.195/day blended): 4–5 range
  - Onshore-developer (R$ 5.563/day blended): 3–4 range
  - Offshore: **0** (agents absorb build volume)

**Arithmetic**: Σ(class rate × class capacity) × duration
- Low: (R$ 7.195 × 4 + R$ 5.563 × 3 + R$ 0 × 0) × 175 = R$ 45.469/day × 175 = **R$ 7.957.075**
- High: (R$ 7.195 × 5 + R$ 5.563 × 4 + R$ 0 × 0) × 343 = R$ 58.227/day × 343 = **R$ 19.971.861**

> **Validated-Rate Disclaimer**: Indicative pricing range derived from bill rates (COM impostos, daily basis 8h/dia) mapped from Salesforce PS Brasil contract rates table, validated by Solution Lead on 2026-07-19, multiplied by top-down effort basis (benchmark-derived duration × lane-specific capacity by class). This is decision-support data for planning and budget allocation — not a cost estimate, not a margin calculation, not a fixed-fee commitment. Offshore rate R$ 3.500/day is an assumption (market-typical Brasil nearshore rate; not on contract table) — validate applicability or adjust. Actual commercial terms, cost structure, margin, and final pricing are subject to Salesforce PS's capacity assessment, delivery model selection, and formal commercial negotiation.

> **Benchmark Disclaimer (Duration)**: Timeline ranges derived from Salesforce PS historical engagement data (model-training-data) via parametric classification of engagement shape (size distribution, clouds in scope, integration count, regulatory context). This is decision-support data, not a commitment or guarantee. Actual duration depends on client-side capacity (Phase 0 approvals, TI API access provisioning, volumetrics audit speed), scope changes, and unforeseen technical blockers. Use for planning and budget allocation; validate assumptions in Phase 0 before locking timeline.

> **Benchmark Disclaimer (Capacity)**: Team shape ranges (capacity by class) derived top-down from engagement shape — discipline coverage, phase overlap, and complexity — benchmarked against Salesforce PS historical delivery patterns (model-training-data). People are multi-disciplinary — one person commonly fills multiple roles (e.g., a senior dev covering Apex + integration; a BA covering release management on a small team). Headcount is therefore typically less than the count of disciplines identified. This is decision-support data for planning, not a staffing commitment. Actual team sizing, FTE counts, and resourcing require Salesforce PS capacity assessment and delivery model confirmation.

---

## Traditional Lane (Offshore-Weighted)

### Duration
**29–54 semanas** (Multi-Cloud High + risk adders)

**Provenance**: Parametric row Multi-Cloud High (10 epics, predominant L/XL: 2 XL + 3 L out of 10, 7 legacy systems integrated, baseline 26-40 weeks). Risk adders: +15% regulated industry (LGPD Art. 48 + TCU audit trail + perfil de acesso governance TI+Jurídico+DPO), +10% new client (first-time Dataprev, unknown org quality, Protheus governance blocker G1002 unresolved), +10% confidence widening (68 gaps, G1002 blocker, volumetrias pending, Experience Design gap, Governance gap — many Unknowns/Assumed). Total adders +35% (under +50% cap). From `.project-metadata.json.timeline.derived`.

### Capacity
**12–15 pessoas at peak (Phase 2)**

**Team shape (scope-scaling, offshore-weighted):**

**Onshore core (continuous Phase 0 → hypercare):**
- R01 — Senior Technical Architect (architecture, security, governance, NFR validation LGPD/TCU, CoE charter)
- R03 — MuleSoft Technical Architect (7-system API exposure hub, governance model, perfil de acesso middleware)
- R06 — Solution Architect (Service Cloud IF Clarity migration chosen F2, Slack Enterprise Grid config, Slack EKM AWS KMS)
- R10 — Solution Consultant (BA, Phase 0 gap resolution G1002 blocker escalation, volumetrics audit coordination, UAT, RACI facilitation, baseline metrics)

**Onshore fractional specialists (consumed when needed):**
- R02 — Agentforce Technical Consultant (F1-F3: 9 agents J1-J10, RAG grounding E04 KB Normativas, conversational design voice/text)
- R04 — MuleSoft Technical Consultant (F1-F3: API connectivity 7 legacy systems, Phase 0 API discovery spike Clarity G0801)
- R05 — Data Cloud Technical Architect (F3 only: streaming architecture Pronto + CRM Totvs CDC ingestion, unified data model, predictive segmentation)
- R07 — Change Management Lead (F0-F2 peak: multi-persona CM training, early adopters 20-50 pilot, executive mandate Saulo, adoption monitoring, Experience Design coordination)
- R08 — UX Researcher / Service Designer (F0-F2: UX research 10k+ external users baseline, F1 pilot usability testing J1/J2 conversational flows 20-50 users, service design Slack Canvas UX, content strategy help library, accessibility WCAG 2.1 AA)
- R09 — Einstein Analytics Developer (F3 only: Einstein Discovery models SLA breach + pipeline churn, model training + eval loops, Data Cloud segmentation activation)
- R11 — Quality Assurance Consultant (F1/F2/F3 surge hardening: 7-system API integration testing read-only F1 + controlled writes F2, Data Cloud streaming + predictive model accuracy F3, LGPD/TCU audit trail verification, Agentforce conversational flow testing voice/text NLP + error handling + escalation paths)

**Offshore build pod (scope-scaling under onshore oversight):**
- 3–5 offshore developers (7 legacy API connectors build, 9 Agentforce agents config, Data Cloud setup, test execution)
- 1–2 offshore QA (surge hardening F1/F2/F3 go-live, regression testing)

**Peak capacity Phase 2**: ~4 onshore core + ~5 onshore fractional (R02, R04, R07, R08, R11 all active F2) + ~5-6 offshore pod = **~14 pessoas** (range 12-15 accounting for ramp/phase overlap).

### Capacity by Class
- **Onshore-architect** (senior rates): R01, R03, R05 (F3), R06, R07 (F0-F2) → **4–5 range**
- **Onshore-developer** (mid rates): R02, R04, R08, R09 (F3), R11 (surge) → **3–4 range**
- **Offshore** (assumed Brasil nearshore): offshore dev pod + QA → **4–7 range**

### Indicative Price
See "Approved Commercials" section above for arithmetic and validated-rate disclaimer.

---

## Quantum Leap Lane (AI-Native, Senior-Core)

### Duration
**25–49 semanas** (Traditional compressed by AI efficiency Low readiness)

**Provenance**: Traditional baseline 29-54 weeks compressed by efficiency Low readiness realized band ~10-14% (from `efficiency.json.project_level`). Readiness score 2/8 (AI tooling posture 0/2, delivery velocity 1/2, data hygiene 1/2, legal/compliance 0/2) drives Low scenario. Task-level ~30-40% × realization factor 0.40-0.45 = ~12-18% project-level; Low readiness reduces to ~10-14% (accounts for Amdahl's law, review/AI-tax overhead, unmoved human-barrier work).

**Provisional note**: Compression band provisional until QL actuals accumulate (`decisions/0011`). Moving to High readiness ~18-22% requires 5 unlocks: (1) AI tooling approval for PS delivery team (GitHub Copilot, Claude, Cursor currently not adopted), (2) G1002 Protheus governance resolution pre-kick-off, (3) LGPD/TCU-compliant AI-assisted delivery policy (level of human review for model-generated code/config/docs), (4) volumetrias audit (G0102/G0201/G0302/G0701 capacity planning), (5) data model reconciliation plan across 7 legacy systems.

### Capacity
**10–11 pessoas at peak (Phase 2)**

**Team shape (derived to need via 5 QL adjustments):**

**QL Adjustment 1 — Volume → agents, not bodies.** Traditional offshore build pod (4-7 pessoas) + onshore developer build volume absorbed by agent fleet under existing senior core. **Confirmed: no human builder** (agents absorb entire build volume — 7 legacy API connectors, 9 Agentforce agents, Data Cloud config, test execution). Offshore pod drops to **0**; onshore developers R02/R04 continue as **agent directors** (prompting/orchestrating agents, not hand-coding).

**QL Adjustment 2 — Keep un-delegatable accountabilities human.** QA R11 is **agent-amplified, never replaced** (independent check on agent output) and **surges** in F1/F2/F3 hardening windows (LGPD/TCU compliance + fixed parliamentary recess deployment window + 7-system API integration testing justify surge, not flat capacity).

**QL Adjustment 3 — Sequencing multiplies senior coverage.** Hard problems taken one-at-a-time by seniors directing agents → core can cover more scope than in Traditional. R02 Agentforce + R04 MuleSoft dev (confirmed continuous F1-F3) direct agents sequentially — already lean, no reduction.

**QL Adjustment 4 — Breadth sets core; volume sets duration.** Continuous core tracks **6 distinct concurrent hard-problem domains**: (1) Architecture/Security/Governance (R01), (2) MuleSoft integration hub (R03), (3) Agentforce agents (R02), (4) MuleSoft connectors (R04), (5) Slack/Service (R06), (6) BA/release (R10). Core holds **flat F0-F3** (doesn't grow with work volume); duration compresses instead.

**QL Adjustment 5 — Buy depth fractionally; surge in risk windows.** Fractional specialists (R05 Data Cloud F3, R07 CM F0-F2 peak, R08 UX F0-F2, R09 Analytics F3, R11 QA surge) arrive **when consumed** — no change from Traditional (already fractional by design).

**Onshore senior core (continuous Phase 0 → hypercare):**
- R01 — Senior Technical Architect (same as Traditional)
- R02 — Agentforce Technical Consultant (**agent director** — prompting/orchestrating agent fleet for 9 agents J1-J10, not hand-coding)
- R03 — MuleSoft Technical Architect (same as Traditional)
- R04 — MuleSoft Technical Consultant (**agent director** — prompting/orchestrating agent fleet for 7 legacy API connectors, not hand-coding)
- R06 — Solution Architect (same as Traditional)
- R10 — Solution Consultant (same as Traditional)

**Onshore fractional specialists (consumed when needed):**
- R05, R07, R08, R09, R11 — **same as Traditional** (Data Cloud F3, CM F0-F2 peak, UX F0-F2, Analytics F3, QA surge F1/F2/F3)

**Offshore:**
- **0** (agents are the build team under senior core oversight)

**Peak capacity Phase 2**: ~6 core + ~5 fractional (R02, R04, R07, R08, R11 all active F2, R02/R04 as agent directors) + 0 offshore = **~11 pessoas** (range 10-11 accounting for ramp/phase overlap).

### Capacity by Class
- **Onshore-architect** (senior rates): R01, R03, R05 (F3), R06, R07 (F0-F2) → **4–5 range** (same as Traditional)
- **Onshore-developer** (mid rates): R02 (agent director), R04 (agent director), R08, R09 (F3), R11 (surge) → **3–4 range** (same as Traditional — roles persist as agent directors, not eliminated)
- **Offshore**: **0** (agents absorb build volume)

### Indicative Price
See "Approved Commercials" section above for arithmetic and validated-rate disclaimer.

### Qualification
**QL committed-delivery** — Dataprev qualifies for AI-native joint operating model:
- ✓ Daily decision-maker availability (Saulo/Pedro/Maik executive sponsorship confirmed, early adopters 20-50 pilot F1 → scale F2/F3)
- ✓ Empowered business owners (Pedro/Maik + TI + Comercial + Pessoas stakeholders can validate rules/acceptance criteria)
- ✓ AI-first mandate (Agentforce as build team, agents absorb offshore build volume — organizational commitment to AI-native delivery confirmed by SSSL)

---

## Delta Decomposed — Why QL Differs

| Dimension | Traditional | Quantum Leap | Delta |
|---|---|---|---|
| **Duration** | 29–54 semanas | 25–49 semanas | **~14-9% faster** (AI efficiency Low readiness ~10-14% compression) |
| **Team at peak** | 12–15 pessoas | 10–11 pessoas | **~17-27% fewer** (offshore pod eliminated, agents absorb build volume) |
| **Indicative price** | See Approved Commercials | See Approved Commercials | **~34-36% lower** (compressed duration + no offshore rates, onshore senior-core only) |

**Why QL is 34-36% lower price:**

1. **Compressed duration** (25-49w vs 29-54w): AI efficiency Low readiness ~10-14% compression (task-level ~30-40% gains × realization factor 0.40-0.45 = ~12-18% project-level, readiness score 2/8 reduces to Low scenario ~10-14%). **Time is the comparison currency** — faster delivery at same quality.

2. **Team derived to need** (10-11 pessoas vs 12-15): Senior core (6 continuous F0-F3) + fractional specialists (5 consumed when needed) + **0 offshore** (agents absorb offshore build pod 4-7 pessoas — 7 legacy API connectors, 9 Agentforce agents, Data Cloud config, test execution under senior core oversight R02/R04 as agent directors). **~17-27% fewer bodies** because volume → agents, not scope-scaling offshore pod.

3. **Rate-class mix shift** (100% onshore senior vs offshore-weighted blend): Traditional = onshore architect 4-5 + onshore dev 3-4 + offshore 4-7 (blended daily rate per Approved Commercials); QL = onshore architect 4-5 + onshore dev 3-4 + offshore 0 (blended daily rate per Approved Commercials). **No offshore rates** → lower blended daily rate despite same onshore senior headcount.

**"QL is cheaper" is indefensible; the decomposition is the defense.** The delta is not a discount — it's a fundamentally different delivery model (AI-native joint operating model with agents as build team) that changes the effort basis (compressed duration + no offshore) and therefore the indicative price. The client pays for **time × capacity**, not body count — QL delivers **faster with fewer people** because agents absorb volume under senior core oversight.

---

## Rate Mapping (Transparency)

**11 perfis do projeto mapeados às taxas do contrato Salesforce PS Brasil:**

| Perfil Projeto | Perfil Contrato Equivalente | Classe |
|---|---|---|
| R01 — Senior Technical Architect | Senior Technical Architect | Onshore-architect |
| R02 — Agentforce Technical Consultant | Technical Consultant | Onshore-developer |
| R03 — MuleSoft Technical Architect | Mulesoft - Technical Architect | Onshore-architect |
| R04 — MuleSoft Technical Consultant | Mulesoft - Technical Consultant | Onshore-developer |
| R05 — Data Cloud Technical Architect | Technical Architect | Onshore-architect |
| R06 — Solution Architect | Solution Architect | Onshore-architect |
| R07 — Change Management Lead | Senior Business Strategy Consultant | Onshore-architect |
| R08 — UX Researcher / Service Designer | Technical Consultant | Onshore-developer |
| R09 — Einstein Analytics Developer | Analytics - Technical Consultant | Onshore-developer |
| R10 — Solution Consultant | Solution Consultant | Onshore-developer |
| R11 — Quality Assurance Consultant | Quality Assurance Consultant | Onshore-developer |

**Detailed rates (COM impostos, daily 8h/dia) and blended class rates**: See "Approved Commercials" section above for validated rates, arithmetic, and disclaimers. Offshore rate assumption (Traditional only, market-typical Brasil nearshore) also detailed there.

---

## Assumptions & Caveats

- **Scope ownership**: 100% PS-delivered (all 10 epics including Change Management E10). 0 client-staffed roles confirmed by SSSL.
- **Shared scope base**: Epics + T-shirt sizes from `data/epics.json` + `data/estimates.json` (2 XL, 3 L, 3 M, 1 S) — same complexity regardless of delivery model. Confidence distribution 45% Confirmed, 50% Assumed, 5% Unknown (typical for first draft; Phase 0 resolves 68 gaps to 70-80% Confirmed).
- **Duration ranges are benchmark-derived**, not commitments. Actual duration depends on client-side capacity (Phase 0 approvals, TI API access provisioning speed, volumetrics audit), scope changes, and unforeseen blockers (G1002 Protheus governance blocker still unresolved; escalate to seller before proposal submission).
- **Capacity ranges are benchmark-derived**, not staffing commitments. People are multi-disciplinary — headcount typically less than role count. Actual resourcing requires Salesforce PS capacity assessment and delivery model confirmation.
- **Indicative pricing is bill-rate-based** (what the client is charged), not cost-based. No margin calculation, no fixed-fee commitment. Offshore rate assumption (market-typical Brasil nearshore; not on contract table) detailed in Approved Commercials section — validate or adjust. Actual commercial terms subject to formal negotiation.
- **QL compression band is provisional** until QL actuals accumulate (`decisions/0011`). Low readiness ~10-14% is the current state (readiness score 2/8); moving to High readiness ~18-22% requires 5 unlocks listed in QL Duration section.
- **QL qualification is committed-delivery** (Dataprev meets AI-native joint operating model criteria) — not conditional. If qualification changes, QL lane becomes "if you can commit to this way of working, here's what it would cost" (motivator, not achievable without named commitment).
- **No hours, no per-hour rates, no FTE/person-month math** in this estimate. Time is the comparison currency (weeks); capacity is engagement-level top-down (class-based ranges). Never a bottoms-up hours roll-up.

---

## Next Steps

1. **Validate offshore rate assumption** — Traditional lane offshore rate (detailed in Approved Commercials section) is market-typical Brasil nearshore; confirm applicability to Dataprev engagement or adjust to actual contracted offshore rate if available.
2. **Escalate G1002 Protheus governance blocker** — TI+Jurídico+DPO tri-party approval pending pre-kick-off. This is a pre-sales qualification gate; if unresolved, Phase 1 J1 journey (Consultas Financeiras Self-Service E01) infeasible. Escalate to seller before proposal submission.
3. **Run Phase 0 Discovery & Architecture Refinement** — 68 gaps exceed 15-gap threshold. Phase 0 resolves blockers (G1002 governance, volumetrics audit G0102/G0201/G0302/G0701, Workspace Slack segregation G0101, Clarity API validation G0801), improves confidence from 45% to 70-80% Confirmed.
4. **Lock Experience Design + Governance workstreams** — add UX Researcher R08 + Service Designer Phase 0/Phase 1 (G0104/G0402/G0505 gap — 10k+ external users onboarding), run Phase 0 RACI workshop (G9901/G1001/G1003 gap — multi-team ownership, data stewardship, CoE structure).
5. **Consider AI efficiency unlocks** — if Salesforce PS wants to capture High readiness ~18-22% (vs current Low ~10-14%), unlock requirements: approve AI tooling for delivery team, resolve G1002 pre-kick-off, define LGPD/TCU-compliant AI-assisted delivery policy, complete volumetrics audit, establish data model reconciliation plan across 7 legacy systems.
6. **Run `validate` → `narratives` → `export`** — validate data quality, generate executive summary with dual-track comparison, package client-ready deliverables into Excel workbook. If presentation deck needed, run `slides`.

---

**Document control:**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07-19 | Scopezilla estimate skill | SSSL-approved dual-track comparison — Traditional vs Quantum Leap |
