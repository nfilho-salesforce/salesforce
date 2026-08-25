# 0001 — The ingested ROM prices Build/Delivery only; the ARI estimate must span the full Salesforce PS lifecycle

**Date:** 2026-08-25 · **Status:** accepted · **Source:** client-supplied (scoper directive)

## Context
The project's grounding document — `discovery-notes/vivo-b2c-atendimento-estimation-design.md` — is a near-final ROM (199 stories, 1.117–2.156 SP with contingency, ~12.4k–29.8k productive engineering hours, 27-person / 5-squad build). By its own assumptions (§ premissa 16, § "Fim da ROM") it scopes **engineering and architecture only**: build, QA-as-a-percentage, and technical cross-cutting. It explicitly excludes project governance (PM, Scrum Master, Agile Coach, Delivery Manager) and does **not** cover Prepare & Design, SIT, UAT, Deploy, or Scale/Hypercare.

The scoper (Nelson) requires a **complete PS project plan and estimate**: all Salesforce PS methodology phases, with a full role × phase × hours breakdown.

## Decision
The ARI Vivo estimate treats the ingested ROM's build hours as the **grounded Build/Delivery anchor** and wraps the full PS lifecycle around it:
- **Prepare & Design (P&D)** — scoped as story refinement + sprint mobilization (Sprint 0), on the premise that epics and the technical plan already exist (the ROM + its source story map). Not a greenfield discovery.
- **Build / Delivery** — inherited from the ROM (do not re-derive; revalidate).
- **SIT → UAT → Deploy → Scale/Hypercare** — added as new phases.
- **Governance / program management** — added as roles the ROM excluded.

## Consequences
- Total hours and roster grow well beyond the ROM's build-only figure; the ROM number is a component, never the total.
- Phase-loading factors (P&D, testing, deploy, scale as functions of build effort/duration) and governance loading become load-bearing assumptions that must be surfaced and confirmed, not invented.
- The build slice stays as the ROM states it; revalidation may adjust sizes but the phase-wrapping is additive.

## Grounds
`discovery-notes/vivo-b2c-atendimento-estimation-design.md` §5 (squad model), §7 (consolidation), §9 (FTE-hours, "cobrem engenharia e arquitetura… não incluem gestão de projetos"), §12 (exclusions); scoper directive 2026-08-25.
