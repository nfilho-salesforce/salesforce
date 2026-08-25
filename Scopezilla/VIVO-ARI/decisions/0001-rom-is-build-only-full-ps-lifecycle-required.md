# 0001 — The ingested ROM prices Build/Delivery only; the ARI estimate must span the full Salesforce PS lifecycle

**Date:** 2026-08-25 · **Status:** accepted · **Source:** client-supplied (scoper directive)

## Context
The project's grounding document — `discovery-notes/vivo-b2c-atendimento-estimation-design.md` — is a near-final ROM (199 stories, 1.117–2.156 SP with contingency, ~12.4k–29.8k productive engineering hours, 27-person / 5-squad build). By its own assumptions (§ premissa 16, § "Fim da ROM") it scopes **engineering and architecture only**: build, QA-as-a-percentage, and technical cross-cutting. It explicitly excludes project governance (PM, Scrum Master, Agile Coach, Delivery Manager) and does **not** cover Prepare & Design, SIT, UAT, Deploy, or Scale/Hypercare.

The scoper (Nelson) requires a **complete PS project plan and estimate**: all Salesforce PS methodology phases, with a full role × phase × hours breakdown.

## Decision
The ARI Vivo estimate treats the ingested ROM's build hours as the **grounded Build/Delivery anchor** and wraps the full PS lifecycle around it:
- **Prepare & Design (P&D)** — scoped as story refinement + sprint mobilization (Sprint 0), on the premise that epics and the technical plan already exist (the ROM + its source story map). Not a greenfield discovery. **Two additive activities confirmed in-scope in the grill 2026-08-25 (scoper directive), beyond pure story refinement:** (a) **TMA/FCR baseline capture + measurement plan** — freeze current-state TMA/FCR from existing contact-center reporting and fix the post-go-live measurement point that reconciles Amazon Connect (queue/IVR) with Salesforce Omni-Channel (human routing), so the ARI's −15% TMA / +FCR outcome is auditable (resolves G0507, G0903, G0803); (b) a **right-sized experience / service / conversation-design track**, scoped to the high-impact surfaces only (agent console, conversational agent flows, the CPM-04 300-step interview) — NOT greenfield UX research across all domains (resolves G0505, G0807, G0908, G0405, G0607, G0306). Both are the mechanism of the ARI outcome, not decoration; they land in P&D and add to the estimate.
- **Build / Delivery** — inherited from the ROM (do not re-derive; revalidate).
- **SIT → UAT → Deploy → Scale/Hypercare** — added as new phases.
- **Governance / program management** — added as roles the ROM excluded.

## Consequences
- Total hours and roster grow well beyond the ROM's build-only figure; the ROM number is a component, never the total.
- Phase-loading factors (P&D, testing, deploy, scale as functions of build effort/duration) and governance loading become load-bearing assumptions that must be surfaced and confirmed, not invented.
- The build slice stays as the ROM states it; revalidation may adjust sizes but the phase-wrapping is additive.

## Grounds
`discovery-notes/vivo-b2c-atendimento-estimation-design.md` §5 (squad model), §7 (consolidation), §9 (FTE-hours, "cobrem engenharia e arquitetura… não incluem gestão de projetos"), §12 (exclusions); scoper directive 2026-08-25. **Reconfirmado em primeira mão pelo scoper na grelha de escopo 2026-08-25: "aditivo, o ROM do knowledge cobre apenas BUILD" — P&D, SIT, UAT, Deploy, Scale/Hypercare e governança são todos aditivos; o roster do ROM não absorve nenhuma dessas fases.**
