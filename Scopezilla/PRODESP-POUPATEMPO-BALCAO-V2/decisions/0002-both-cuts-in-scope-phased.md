# 0002 — Both cuts in scope for this SOW, phased (Corte 1 tactical → Corte 2 whole-house), not Corte 2 as out-of-scope vision

**Date:** 2026-09-21 · **Status:** accepted · **Source:** client-supplied (Nelson, confirmed directly in interactive session, overriding `decisions/0001`)

## Context

`decisions/0001` scoped this SOW to Deck 1 ("Poupatempo Balcão V2" — Jackson Ulisses, tactical Slack-at-the-counter) only, treating Deck 2 ("Atendimento Poupatempo" — Vinicius Ferraz, whole-house Headless platform) as unscheduled, unpriced Phase 2+ vision outside this contract. That ADR was written by a background discover run without a direct scope confirmation from the user.

When asked directly — first "which cut should be the committed scope," then a proposed middle ground of "Phase 1 immediate + 1-2 Headless elements folded in as Phase 2 of the same contract" — the user rejected the partial-selection framing outright: *"tratar corte e corte 2 completo, nao apenas corte 1"* (treat Corte 1 and Corte 2 in full, not just Corte 1). The whole-house platform is not a someday-vision to gesture at; it is contractable scope for this same SOW, phased behind the tactical cut.

## Decision

This engagement scopes **both decks in full, phased within one SOW**:

- **Phase 1 (tactical, Corte 1 — Jackson deck):** Slack as the attendant's counter workstation — service channels, Canvas, huddle-based specialist escalation, idle-capacity cross-posto routing, outage broadcast workflows. Runs on Slack Enterprise Plus + Agentforce/Flex Credits capacity already validated in the account.
- **Phase 2 (whole-house, Corte 2 — Vinicius deck, in full):** WhatsApp pre-service outreach to the citizen before the scheduled visit, Slack-based remote document validation by idle attendants at other postos, agentic 24/7 WhatsApp attendance with human-in-the-loop supervision, and MuleSoft integration into gov.br, state biometria, and Prodesp legacy systems (Sistema Semântico, "Atendimento," T7 — identities still open, see Discovery Brief Open Questions).

Both phases are **committed scope of this same SOW** — Phase 2 is not deferred vision, an option, or a separate future engagement to pitch later. It is sequenced after Phase 1 within the same contract.

## Consequences

- `requirements`/`design`/`roadmap` must scope epics for **both** phases — Phase 1 (Slack + Agentforce-in-channel + existing Data 360 lookups) **and** Phase 2 (WhatsApp pre-service journeys, remote validation, agentic 24/7 attendance, MuleSoft-to-gov.br/biometria/legado integration).
- The account's own internal sequencing (Check-in/PPA ahead of Slack Headless, per `decisions/0001`'s grounds) still governs *when* Phase 2 starts relative to other account initiatives — it does not remove Phase 2 from this SOW's scope.
- Neither deck's blank timeline/investment slides are resolved by this decision — Phase 2's schedule and price remain open (see Discovery Brief Open Questions); this ADR fixes *scope*, not *commercials*.
- The open architecture identities (T7, Sistema Semântico, "Atendimento," Biometria) become more load-bearing now that Phase 2's MuleSoft integration is committed scope, not deferred vision — resolving them is higher priority for `requirements`.
- Reversing this decision (narrowing back to Phase 1 only) would require the user to explicitly re-scope down again; the default going forward is both phases, in full.

## Grounds

Direct user confirmation in this session, overriding `decisions/0001`. Source material unchanged: `discovery-notes/PRODESP-Slack-Balcao-BSA.md`, `discovery-notes/Poupatempo Balcao - V2.pptx.pdf` (Jackson/Corte 1), `discovery-notes/Prodesp - Atendimento Poupatempo.pdf` (Vinicius/Corte 2, including the visually-recovered "Arquitetura Salesforce" diagram on the Gestão de Comunicação slide).
