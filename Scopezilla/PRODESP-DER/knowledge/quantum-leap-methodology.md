# Quantum Leap — Salesforce PS AI-Native Delivery Methodology
Source: SFPS Quantum Leap (Internal — Archived First Call Deck)
Relevance: DER-SP has Agentforce in scope (WhatsApp triage agent for the emergency MVP, and a pending Coworker-vs-Service-Agent decision for the general Service Cloud attendance). Use to inform phase structure, effort distribution, and — critically — the Entry Criteria checklist, since this account currently has several Day-1 readiness gaps open (environment/licensing undefined, N parameter undefined, risk matrix incomplete).

## Core Commitment
- Fastest path = highest-quality path (Speed & Quality = Trust)
- AI-native PS at scale: Professionals as Trusted Guides
- KPIs: 50-80% Time-to-Value Reduction | 2x Throughput | Zero Critical Defects

## 4 Pillars
1. Selective Customers — fit criteria enforced before engagement
2. Continuous Collaboration — daily validation replaces bi-weekly demos
3. Day Zero Readiness — environments, data, exec sponsor ready on Day 1
4. Orchestrated Execution — intent-based delivery with agent orchestration

## Non-Negotiables
- Human Judgment: AI generates. Humans decide.
- Trust is the Product: quality and speed must coexist
- Quality and Speed Together: not a trade-off
- Learn from Every Engagement: closed-loop feedback into practice memory

## Methodology Phases
Prepare → Intent → Build & Refine → Validate (Customer Owned) → Deploy → Govern

### AI-Native Effort Distribution (% of Total)
- Intent Definition: 15%
- Agentic Build: 15%
- Refinement & Validation: 55% (New Critical Path)
- Orchestration & Change (Deploy + Adoption): 15%

## Customer Readiness Checklist

### Intent Phase — Customer Must Provide:
- Confirm Executive Sponsor
- Named Biz/IT Stakeholders + PM available Day 1
- Environments Provisioned & Access Granted
- Documentation (Process maps, Integration diagrams)
- Data Table Inventory delivered Day 1
- IT Gates Cleared
- Confirm Org Strategy
- Named Customer Data Engineering Lead
Impact if missed: Build starts with epics blocked. All architecture becomes conditional.

**DER-SP status against this checklist (as of 2026-09-17):** Environment/licensing NOT confirmed (BSA deck: "Produto e licença ainda não estão fechados"); Org strategy NOT confirmed (single-org vs. multi-org for FS + Service Cloud/CTI not discussed); geographic cutover scope open (Cubatão/Taubaté pilot vs. all 14 CGRs). These are exactly the gaps the Adaptive Interview below surfaces.

### Build & Refine — Customer Must Provide:
- Process Owners engaged daily in standups + architecture sessions
- UX/Design and Data model decisions within the week
- DevOps pipeline decisions by Week X
- Scope governance: Executive Sponsor signs — no new scope post-Build
- Metadata-driven prompt architecture validated feasible by Week X
- Prompt Review Cycles scheduled before Build starts
- Data extraction mechanisms confirmed by Week X
Impact if missed: Build delayed 1-2 weeks. Rework required. Timeline extends 2-4 weeks.

### Deploy Phase — Customer Must Provide:
- Enablement champions co-build training guides
- Change management ownership
- Training scheduled BEFORE go-live
- Go/No-Go Authority (delay if confidence <80%)
Impact if missed: Adoption 3x slower. Executive Sponsor loses confidence.

## AI Native Customer Fit Criteria

QUALIFY (Must have all 3):
1. Strong Salesforce Partnership — executive sponsor committed, multi-year relationship
2. Structured Governance — clear decision-making authority, product owner identified, Agent Manager and Data Architects named
3. Data Rigor — data readiness Day 1, known operational cadences, org decisions confirmed

Entry Criteria (4 Gates):
1. Desire to go fast — customer identified desire to go fast AND identified Agent Manager, Product Owner, Data Architects
2. Org & Data Readiness — data readiness Day 1, org decisions known
3. PSA is Complete — don't let contracting hold you up
4. Subprocessor Alignment — customer aligns to our subprocessors

AVOID (Disqualifying Signals):
- Poor data governance or data quality issues
- Limited customer resources or availability
- Unclear decision-making authority
- Restricted AI tool usage in customer environment
- No executive sponsor or executive ambivalence

## Operational Risks
- Legacy Drag (High Impact): Forcing AI delivery speeds through legacy CAB and manual code reviews. Mitigation: fast-track governance lane for AI-generated code that passes automated testing.
- Stakeholder Fatigue (High Probability): Business users burn out from daily feedback demands. Mitigation: async feedback tools, rotate SME pools.
- Quality-Speed Paradox (High Impact): Low-quality tech debt generated faster than ever. Mitigation: strict Guardianship roles — no code hits integration without human architectural validation.
