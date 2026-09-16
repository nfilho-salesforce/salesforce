# AI Delivery Efficiency Analysis — DATAPREV-SEFIN-CE

## So What

**~12–19% realized delivery efficiency at Mid readiness** (current client posture). A pace and quality lift within the same team shape — not headcount reduction, not a pricing input.

Where the gains show up on this project:
- **Documentation & Knowledge Management** (~18–28%): UX Research E05 (persona docs, usability findings ~5-10 pages, accessibility report ~10-15 pages WCAG 2.1 AA adapted) + LGPD compliance docs (security baseline, consent disclosures, data retention policy) + HSM templates (3-5 templates Meta approval) — highest reliability per [2][7][11]
- **Analysis & Design** (~12–24%): Einstein Bot dialog drafting (4 flows IPTU/TMRSU/ISS/Cadastral) + Journey Builder (1 jornada proativa IPTU vencido régua D-15, D-5, D+1) — ~40% task-level drafting gains per [2][11], but stakeholder refinement (SEFIN-CE 17 Qs, ISS flow Q-04/Q-05, Bot Maintainer Q-15) stays human-bound
- **Technical Engineering & QA** (~8–18%): Apex callouts (4 SEFIN APIs) + Einstein Bot validators (CPF checksum) gain ~20% task-level drafting per [1][4], but LGPD compliance review burden (CPF/CNPJ Art. 11) + API specs pending (G0301/G0302 BLOCKER) + connectivity validation (ping/curl G0303) raise the AI tax — code cloning 8.3% → 12.3%, refactoring 25% → <10% per [8]

**Roles that capture the most**: Experience Architect (~18–28%), Technical Architect (~14–23%), Technical Consultant (~8–18%), Project Manager (~6–12%).

**Where AI does not help**: Phase 0 gap resolution (133 gaps + 17 client questions — SEFIN-CE stakeholders provide answers, not AI), Meta WhatsApp Business approval (2-8w human approval cycle G0103), LGPD legal interpretation (TDE vs Shield G0611, proactive marketing consent G0809 — SEFIN-CE DPO decides), Stakeholder alignment (Alex Siqueira + Oswaldo Melo + SEFIN-CE + DATAPREV CTID approval cycles), Conflict resolution (ISS flow Q-04/Q-05, Bot Maintainer permissions Q-15) — plus the highest-AI-tax work: LGPD compliance review (mandatory audit trail, connectivity validation, NLU training ownership G0202).

**To move up to High readiness (~22–26%)**: Approve Copilot/Claude for in-IDE use (Salesforce PS team + DATAPREV), Publish LGPD AI data-handling policy (CPF/CNPJ prompts permitted), Faster approval cycles (SEFIN-CE stakeholders responsive <2 weeks for gap resolution).

---

## Headline

**Realized: ~12–19%** (Mid readiness, current state) · **Task-level blend: ~32–48%** · **Realization factor: 0.35–0.45** — Regulated industry (LGPD Art. 11), mixed config + custom dev, standard enterprise government client, government approval overhead (SEFIN-CE, DATAPREV CTID, Meta) · **Confidence: Assumed**

---

## Client-Readiness Scenarios

| Scenario | Realized Band | Notes |
|---|---|---|
| Low readiness | ~9–11% | Gains stay modest until AI tooling approved and LGPD policy published. No IDE AI tools, government approval cycles slow. |
| **Mid readiness** (✓ current) | **~12–19%** | Standard government project readiness — greenfield ORG favors gains, but AI tooling policy and slow approval cycles cap upside. Gains cluster in documentation (UX reports, security baseline) and Einstein Bot NLU drafting; coding and API integration carry the AI tax (review burden on LGPD compliance + connectivity validation). |
| High readiness | ~22–26% | Conditions favor the upper end — AI tooling approved, LGPD policy clear, fast client. A faster government client with approved AI-in-IDE captures more. Not expected given current signals, but achievable if DATAPREV/SEFIN-CE accelerate policy. |

**Current scenario**: Mid readiness (score 3/8)

### Signals behind the score

- **AI tooling posture**: 0/2 — Discovery shows no mention of approved AI tools for Salesforce PS team or SEFIN-CE stakeholders; government client (slower procurement for AI tooling); DATAPREV as intermediary may have policy barriers; no IDE AI (Copilot/Claude) confirmed.
- **Delivery velocity / speed bias**: 1/2 — Government project (SEFIN municipal + DATAPREV federal intermediary) → quarterly/slow-moving procurement typical; BUT: urgency to replace incumbent MUTANTE (R$ 1.7M/yr dissatisfaction) + greenfield ORG (no legacy migration burden) → mid-range velocity; Phase 0 'target <3 semanas' shows some urgency.
- **Data & environment hygiene**: 1/2 — Greenfield ORG (clean start, no legacy tech debt) + Hyperforce Brazil (modern DevOps) → positive signals; BUT: 133 gaps (missing req, API specs pending, ambiguities) + 17 open questions + 4 BLOCKERS (G0301/G0302 API specs, Meta approval timeline, ISS flow undefined) → data/requirements hygiene moderate, not excellent.
- **Legal / security / compliance posture**: 1/2 — LGPD Art. 11 (CPF/CNPJ sensitive data) + government regulatory environment → mandatory security review; Hyperforce Brazil data residency validation pending (P-22) + TDE vs Shield legal interpretation unclear (G0611) + LGPD consent for proactive marketing undefined (G0809) → policy in-draft, not published; NOT comfortable with AI-in-IDE / proprietary code in prompts (no evidence of approval).

### What it takes to move up

- **Low → Mid**: Approve Copilot/Claude for in-IDE use (Salesforce PS team + DATAPREV), Publish AI data-handling policy (LGPD-compliant for CPF/CNPJ sensitive data in prompts)
- **Mid → High**: Approve AI-in-IDE for PS team (Copilot/Claude), Publish LGPD AI data-handling policy (CPF/CNPJ prompts permitted), Faster approval cycles (SEFIN-CE stakeholders responsive <2 weeks for gap resolution)

---

## By Category

### Technical Engineering & QA — realized ~8–18% (task-level ~20–45%)

- **Driving epics**: E02 (L — Einstein Bot 4 flows), E03 (M — API Integration 4 SEFIN APIs), E06 (M — Security + data retention Apex)
- **How it shows up here**: Einstein Bot Apex validators (CPF checksum, slot filling regex) and 4 API REST callouts (EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais) benefit from code drafting (~20% task-level per [1][4] realistic enterprise row), but **LGPD compliance review burden** (CPF/CNPJ sensitive data Art. 11) + connectivity validation (ping/curl test G0303) + API specs pending (G0301/G0302 BLOCKER) **raise the AI tax** — code cloning rose 8.3% → 12.3%, refactoring fell 25% → <10% per [8]. Test data generation (NLU training utterances 50-100/intent, mock API responses) gains ~35% task-level per [3][11], but NLU training ownership undefined (G0202) caps realized gain to ~15% after review cycles.

### Analysis & Design — realized ~12–24% (task-level ~30–60%)

- **Driving epics**: E02 (L — Einstein Bot dialog drafting), E04 (S — Satisfaction survey flow), E06 (M — Profile requirements), E08 ADD-ON (L — Journey Builder drafting)
- **How it shows up here**: Einstein Bot dialog drafting (4 flows IPTU/TMRSU/ISS/Cadastral) and Journey Builder (1 jornada proativa IPTU vencido régua D-15, D-5, D+1) benefit from drafting compression ~40% task-level per [2][11]. **BUT:** stakeholder refinement (SEFIN-CE, DATAPREV CTID approval cycles) stays human-bound and often dominates total time — 17 client questions (Q-01 to Q-17), ISS flow ambiguity (Q-04/Q-05 decision), Bot Maintainer permissions (Q-15 validation). Drafting yes, decision no.

### Documentation & Knowledge Management — realized ~18–28% (task-level ~45–70%)

- **Driving epics**: E01 (M — ORG provisioning config docs, LGPD baseline), E04 (S — LGPD consent disclosure drafting), E05 (M — Persona docs, usability report ~5-10 pages, accessibility report ~10-15 pages WCAG 2.1 AA adapted conversational UI), E06 (M — Security baseline compliance design), E08 ADD-ON (L — HSM templates design, LGPD legal validation drafting)
- **How it shows up here**: **UX Research E05 is the highest-reliability win** — persona docs (12 interviews → 2 PDF PT-BR), usability findings report (~5-10 pages), accessibility report (~10-15 pages WCAG adapted) all leverage drafting compression ~35% task-level per [2][7][11]. LGPD compliance docs (security baseline, consent disclosures, data retention policy) and HSM templates (3-5 templates Meta approval) also benefit from document generation. Meeting operations (Generate Meeting Notes ~65% task-level [7][11]) not applicable this engagement — no dedicated meeting-recording/summarization role in resource-plan.json.

### Project Management & Operations — realized ~6–12% (task-level ~15–30%)

- **Driving epics**: E01 (M — Phase 0 gap resolution coordination), E02 (L — Phase 2 dependency management), E03 (M — Connectivity validation orchestration), E04 (S — Phase 1 Meta approval critical path), E05 (M — Phase 3 UX testing logistics), E06 (M — LGPD compliance stakeholder coordination), E08 ADD-ON (L — Phase 4 HSM approval timeline)
- **How it shows up here**: **Lowest-performing category** — Project Status Reports drafting ~30% task-level, but the coordination core (Phase 0 gap resolution 133 gaps + 17 client questions, Meta approval 2-8w critical path G0103, stakeholder alignment Alex Siqueira + Oswaldo Melo + SEFIN-CE + DATAPREV CTID) remains human per [1][5]. Government approval cycles (SEFIN-CE slow responsiveness, DATAPREV CTID sign-off) are **not AI-compressible** — stakeholder alignment, conflict resolution, approval gates stay ~0% per benchmarks.

---

## By Role Type

### Technical Architect (R01, R05) — realized ~14–23% (task-level ~35–58%)

- **Amplified**: Generation of Analysis Models (bot flow logic, API integration patterns, LGPD compliance design), Analyze Code (connectivity validation, API error handling review, data retention Apex batch job review), Visual Design Brainstorm (adaptado: conversational UI flow design WCAG 2.1 AA, not visual mockups)
- **Still human-only**: Phase 0 gap resolution orchestration (133 gaps, 17 Qs, 2 API specs BLOCKER), Hyperforce Brazil vs US-East decisão (P-22 legal validation), TDE vs Shield legal interpretation (G0611 SEFIN-CE DPO), Stakeholder alignment (SEFIN-CE + DATAPREV CTID + Meta)
- **How the day changes**: Architect drafts solution design docs (LGPD compliance baseline, integration pattern Flow Orchestration + Apex + 4 APIs, Einstein Bot NLU architecture) ~30% faster task-level per [2], but government client decision gates (SEFIN-CE gap responses, DATAPREV CTID sign-off, Meta approval 2-8w) stay human-bound — realized gain ~18% after review cycles and stakeholder coordination overhead.

### Technical Consultant (R02, R03) — realized ~8–18% (task-level ~20–45%)

- **Amplified**: Create Code (realistic enterprise — 4 Apex REST callouts + Einstein Bot Apex validators CPF checksum + data retention batch job), Analyze Code & Fix Defects (connectivity validation ping/curl G0303, API error handling, retry logic 1x), Generate Test Data (NLU training utterances 50-100/intent, mock API responses), Write Test Classes (unit tests for Apex callouts + validators)
- **Still human-only**: API specs pending (G0301/G0302 BLOCKER — cannot start E03 until specs obtained Phase 0), NLU training data ownership (G0202 — SEFIN-CE provides or PS infers?), Stakeholder alignment (LGPD compliance review with SEFIN-CE DPO)
- **How the day changes**: Developer drafts Apex REST callouts (~20% task-level realistic enterprise per [1][4]) and Einstein Bot validators (~25% task-level), but **LGPD compliance review burden** (CPF/CNPJ sensitive data Art. 11) + API specs pending (G0301/G0302) + connectivity validation (ping/curl test) raise the AI tax — code cloning 8.3% → 12.3% per [8], more review cycles pre-prod. Test data generation (NLU utterances, mock APIs) gains ~35% task-level per [3][11], but NLU ownership undefined (G0202) requires human coordination with SEFIN-CE. Realized gain ~13% after review + coordination overhead.

### Experience Architect (R04) — realized ~18–28% (task-level ~45–70%)

- **Amplified**: Generate Documents (persona docs 12 interviews → 2 PDF PT-BR, usability findings report ~5-10 pages, accessibility report ~10-15 pages WCAG 2.1 AA adapted conversational UI), Visual Design Brainstorm (adaptado: conversational UI flow refinement post-usability testing, not visual mockups)
- **Still human-only**: UX research execution ownership ambiguity (G0501 — PS conducts or DATAPREV conducts with PS guidance?), LGPD consent forms for persona interviews + usability testing (G0514), Accessibility testing with PcD (G0509 — expert review vs user testing unclear)
- **How the day changes**: **Highest reliability role on this engagement** — UX Researcher drafts persona docs, usability findings, accessibility reports ~35% faster task-level per [2][7][11] (documentation category most reliable). BUT: conducting interviews (12 remote Zoom sessions), facilitating usability testing (15 sessions 3 fluxos × 5 usuários), and expert accessibility review (WCAG heuristic evaluation) stay human — AI drafts the artifacts, human conducts the research. Realized gain ~23% after research execution stays human-bound.

### Project Manager (R06) — realized ~6–12% (task-level ~15–30%)

- **Amplified**: Project Status Reports (~30% task-level drafting [7][11]), Search & Info Retrieval (~25% task-level [7][11])
- **Still human-only**: Phase 0 gap resolution coordination (133 gaps, 17 client questions Q-01 to Q-17, 2 API specs BLOCKER G0301/G0302), Phase 1 Meta approval critical path orchestration (G0103 2-8w timeline negotiation), Stakeholder alignment (Alex Siqueira AP PS + Oswaldo Melo SE + SEFIN-CE + DATAPREV CTID approval cycles), Conflict resolution (ISS flow decisão Q-04/Q-05, Bot Maintainer permissions Q-15, TDE vs Shield legal interpretation G0611), Coordination Meeting Time (SEFIN-CE slow responsiveness, government quarterly approval cycles)
- **How the day changes**: PM drafts status reports ~30% faster task-level per [7][11], but **coordination core stays human** — Phase 0 gap resolution (133 gaps, 17 Qs), Meta approval negotiation (2-8w), SEFIN-CE stakeholder alignment (slow government response cycles), DATAPREV CTID sign-off gates are **not AI-compressible** per [1][5]. Realized gain ~9% after coordination overhead dominates.

---

## Human-Only Work

- **Project Pulse Reports** — Trust-building work that AI can summarize but not facilitate.
- **Stakeholder Alignment** — Human-to-human negotiation; AI drafts positions, people decide. Phase 0 gap resolution (17 client questions Q-01 to Q-17), ISS flow decisão (Q-04/Q-05), Bot Maintainer permissions (Q-15), Hyperforce Brazil vs US-East (P-22), TDE vs Shield (G0611) — SEFIN-CE + DATAPREV CTID + Meta approval cycles stay human-bound.
- **Conflict Resolution** — Human judgment. ISS flow ambiguity (Q-04/Q-05 — link only or upgrade to DAM emission?), Bot Maintainer profile scope (Q-15 — Einstein Bot + conversation review or broader access?), TDE vs Shield legal interpretation (G0611 — SEFIN-CE DPO decides), LGPD consent for proactive marketing (G0809 — legitimate public interest or opt-in required?) — AI provides compliance analysis, legal/stakeholders decide.
- **Phase 0 Gap Resolution** — AI drafts the 133 gaps + 17 client questions list (Q-01 to Q-17), but SEFIN-CE stakeholders provide the answers — human negotiation on API specs (G0301/G0302 BLOCKER), ISS flow decisão (Q-04/Q-05), Bot Maintainer permissions (Q-15), Hyperforce Brazil (P-22), TDE vs Shield (G0611). SEFIN-CE response time (target <3 semanas) is human-bound, not AI-compressible.
- **Meta WhatsApp Business Approval** — Phase 1 critical path (G0103 2-8 weeks timeline) — human approval from Meta WhatsApp Business team, not automated. AI drafts the approval request docs (domínio personalizado, business verification, use case description), Meta human reviewers decide. Timeline variability (2-8w) is external approval cycle, not PS delivery.
- **LGPD Legal Interpretation** — TDE vs Shield for Art. 11 CPF/CNPJ sensitive data (G0611), LGPD consent for proactive marketing (G0809 — tax payment reminders = legitimate public interest Art. 7, IX?), data retention policy 90-day vs 12-month (G0610 Art. 15 minimization) — SEFIN-CE DPO + DATAPREV legal decide, AI provides compliance analysis only. Legal interpretation is human judgment, not AI-replaceable.

---

## Assumptions & Caveats

- Task-level gains come from published 2022–2026 studies; realization factor (0.35–0.45) accounts for Amdahl's law, review/AI-tax overhead (LGPD compliance audit trail, API specs pending G0301/G0302, NLU training ownership G0202, government approval cycles), and unmoved human-barrier work (Phase 0 gap resolution 133 gaps + 17 Qs, Meta approval 2-8w, SEFIN-CE stakeholder alignment, DATAPREV CTID sign-off).
- **Honest range for coding**: RCT evidence spans −19% (METR 2025 [1], mature OSS) to +21% (Paradis/Google 2024 [4], complex enterprise) to +55% (Peng/GitHub 2022 [3], greenfield lab). The realistic-enterprise row (~20%, −5% to +35%) is the defensible starting point for Salesforce integration and custom Apex work on this engagement.
- Individual gains ≠ team gains: DORA 2024 [5] measured individual productivity rising while delivery stability and throughput fell. Ground claims in project-level outcomes, not developer self-report.
- Model capability is racing ahead of realized workflow gains (Stanford HAI 2026 [9]); that gap is why project-level bands stay in ~10–25%.
- Bands are qualitative and project-specific — no hours, FTE, or cost implications are computed or implied.
- **LGPD compliance** (CPF/CNPJ Art. 11 sensitive data) + **government approval cycles** (SEFIN-CE slow responsiveness, DATAPREV CTID sign-off, Meta approval 2-8w) materially reduce realized gain — compliance adds mandatory review burden (audit trail, TDE encryption validation, data retention Apex batch job testing, connectivity validation ping/curl G0303) that is not AI-compressible. Regulatory projects typically land at the floor of the realized band per [5][8].
- **NLU training data ownership ambiguity** (G0202 — SEFIN-CE provides or PS infers?) and **API specs pending** (G0301/G0302 BLOCKER — CRM SEFIN + Dados Cadastrais endpoint/payload/auth undefined) are critical-path gates that AI cannot resolve — these are stakeholder coordination tasks (human-to-human negotiation Phase 0) that dominate the timeline regardless of coding/drafting speed gains.

---

## Sources

1. METR (July 2025) — RCT of experienced OSS developers; measured ~19% slowdown despite perceived ~20% speedup.
2. BCG × Harvard (2023, 2025 pilots) — 12.2–40% time savings on in-scope tasks; "jagged frontier" degrades on out-of-scope tasks.
3. Peng et al., GitHub (2022) — lab RCT, 95 devs on a greenfield HTTP-server task; ~55% faster, 95% CI [21%, 89%].
4. Paradis et al., Google (arXiv 2410.12944, 2024) — RCT of 96 Google engineers on a complex enterprise task; ~21% time reduction with wide CI. Counterweight to [1].
5. DORA 2024 State of DevOps — first rigorous team-level measurement that individual AI productivity gains coexist with decreased delivery stability and throughput.
6. DORA 2025 — "AI is an amplifier" of existing sociotechnical systems; qualitative, supplement to [5].
7. McKinsey State of AI (2025) — function-level productivity gains reported by enterprises cluster at 10–30% for software and marketing functions.
8. GitClear AI Code Quality (2025 update, 211M LOC) — code cloning rose 8.3% → 12.3%; refactoring fell 25% (2021) → <10% (2024). Strongest longitudinal evidence for "AI tax" during review + maintenance.
9. Stanford HAI AI Index 2026 (April 2026) — SWE-bench Verified rose 60% → near 100% of human baseline; 88% organizational adoption; 50-point expert/public gap on AI's workplace impact.
10. Salesforce Agentforce internal pilots (2024–2025, public-facing) — 30–50% deflection on Tier-1 support; admin/config drafting uplift ~20–40%.
11. Scopezilla internal observations (2025–2026) — directional only; documentation and meeting-operations pilots consistently report the highest reliable gains.
