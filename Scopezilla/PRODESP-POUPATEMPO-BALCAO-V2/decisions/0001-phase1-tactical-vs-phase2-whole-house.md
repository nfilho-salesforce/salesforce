# 0001 — Scope this engagement as the Phase 1 tactical counter pilot; treat the whole-house Headless platform as Phase 2+ vision, not this SOW

**Date:** 2026-09-21 · **Status:** accepted · **Source:** scopezilla-recommended

## Context

Two design decks arrived in the same week (September 2026) describing what looks like one initiative but are actually two different bets:

- **Deck 1 — "Poupatempo Balcão V2"** (Jackson Ulisses, created 01/09/2026): what Slack already does, out of the box, for the attendant at the counter — service channels, Canvas, huddles, cross-posto idle-capacity routing, outage broadcast workflows. No integration build, no price, "no ar em semanas."
- **Deck 2 — "Atendimento Poupatempo"** (Vinicius Ferraz, 69 slides, created 03/09, last edited 10/09): the whole-house vision — WhatsApp pre-service outreach, Slack-based remote document validation, agentic 24/7 WhatsApp attendance with human-in-the-loop, MuleSoft into gov.br/biometria/legado. Schedule and pricing slides are explicitly blank in the deck itself.

In the account's own internal committee (Juliana Brites × Juliane Lopes, 08–09/09/2026), the sequencing was already stated: Check-in and PPA sit ahead of Slack Headless in the account's implementation queue; Slack Headless (deck 2, whole-house) enters *after* those, it does not replace them. The Professional Services request made explicit on 09/09 is for the guichê cut (deck 1) — there is no SOW, commercial registration, timeline, or price for either cut yet.

Treating these two decks as one undifferentiated scope would either (a) inflate this proposal with unscoped, unpriced whole-house integration work that the account itself has queued behind other initiatives, or (b) force a premature choice between "small pilot" and "big platform" language that the client hasn't asked for and PRODESP hasn't budgeted.

## Decision

This engagement scopes **Phase 1 only**: the tactical counter-side pilot described in the Jackson deck — Slack channels, Canvas, huddle-based specialist escalation, idle-capacity cross-posto routing, and outage broadcast workflows, running on top of the Slack Enterprise Plus and Agentforce/Flex Credits capacity already validated in the account (1,800 users, July 2026). No MuleSoft build to gov.br/biometria/legado, no WhatsApp pre-service journeys, no agentic 24/7 attendance.

The whole-house Headless 360 vision (Vinicius deck) is carried forward as **Phase 2+**: directional, unscheduled, unpriced context for where this could go — never treated as committed scope, never used to justify Phase 1 pricing or timeline, and never silently merged into Phase 1 epics.

## Consequences

- `requirements`/`design`/`roadmap` should scope epics against Phase 1 only (Slack + Agentforce-in-channel + existing Data 360 context lookups). MuleSoft-to-gov.br integration, WhatsApp pre-service journeys, and agentic 24/7 attendance are explicitly **out of scope** for this SOW, not deferred sub-epics of it.
- Any Flex Credits / cost-order-of-magnitude estimate produced downstream should be bottom-up from Phase 1's own volume assumptions (per-posto or network-wide "% of presencial cases that fall outside script" — currently unmeasured), never derived from or blended with Phase 2+'s whole-house volumes.
- The USD 1M commercial target cited by Juliana Brites (10/09) is a **licensing** target for Slack-Prodesp overall, not a Phase 1 PS price — it must never be presented as this engagement's number.
- Reversing this decision (i.e., scoping the whole-house platform now) would require the account to actually sequence Slack Headless ahead of Check-in/PPA, and would re-shape every downstream epic, integration list, and cost estimate in this project.

## Grounds

`discovery-notes/PRODESP-Slack-Balcao-BSA.md` §1 ("Duas frentes da mesma conta, com datas e donos diferentes"; "Sequência da conta em 9 de setembro"), §5 ("Order Form ilustrativa: o que atenderia este caso" — Professional Services listed as its own unscoped line), and the side-by-side deck comparison table ("Os dois desenhos que chegaram em setembro"). Cross-checked against `discovery-notes/Poupatempo Balcao - V2.pptx.pdf` (Jackson deck, "Sem projeto de anos") and `discovery-notes/Prodesp - Atendimento Poupatempo.pdf` (Vinicius deck, blank Investimentos/Cronograma slides).
