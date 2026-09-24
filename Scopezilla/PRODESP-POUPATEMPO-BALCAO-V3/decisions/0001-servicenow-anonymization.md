# 0001 — ServiceNow is confirmed as the underlying legacy CRM/ServiceDesk platform, but never named in any deliverable

**Date:** 2026-09-23 · **Status:** accepted · **Source:** client-supplied

## Context

The 69-slide Vinicius deck (`discovery-notes/brief-Prodesp - Atendimento Poupatempo.pdf.md`) shows a 7-system architecture diagram (page 63) that does not name ServiceNow anywhere — the diagram lists Atendimento, Biometria, Gov.br, T7, Agentes de IA, API de terceiros, and Sistema Semântico. This absence contradicted the inventário's systems table (`discovery-notes/00-inventario-de-solucao-poupatempo.md` §... systems table), which marks ServiceNow as **Confirmed via Ata** — sourced from the 23/09/2026 meeting minutes — as the protocol source and legacy service desk, with zero migration in scope.

Asked directly (AskUserQuestion Q4, 2026-09-23) whether ServiceNow is confirmed in scope despite its absence from the deck, Nelson confirmed it is the real platform underneath, but imposed a documentation constraint: the product name must never appear in any deliverable for this engagement.

## Decision

ServiceNow **is** the legacy CRM + ServiceDesk platform Poupatempo runs today (protocol/ticket source, zero migration planned). Every deliverable for this project — Discovery Brief, epics, SOW, proposal, slides, any client-facing or internal artifact — refers to it only as:
- **"Sistema de CRM legado"**
- **"Sistema de ServiceDesk legado"**

The literal string "ServiceNow" must not appear anywhere in project outputs, going forward.

## Consequences

- Every epic, integration reference, or architecture diagram touching this system uses the anonymized names, not the product name.
- Anyone re-reading a deliverable without this context would not know the underlying platform is ServiceNow — that mapping lives only here and in `discovery-notes/`.
- If a future deliverable needs to reference the *actual* integration mechanics (APIs, tables, ServiceNow-specific behavior), that detail can still be described functionally ("the legacy ServiceDesk's ticket API") without using the brand name.
- Reversing this would require the client's explicit release to name the vendor — until then, this rule is absolute for all outputs.

## Grounds

Client-supplied instruction, verbatim (Nelson Stebulaitis Filho, AskUserQuestion Q4, 2026-09-23): *"Sim confirmado porém devemos anonimizar o ServiceNow, nao devemos usar o nome do produto apesar de ser esta mesmo a plataforma. Sistema de CRM e Sistema de ServiceDesk legados."* Cross-checked against `discovery-notes/00-inventario-de-solucao-poupatempo.md` (systems table, ServiceNow row, Confirmed via Ata) and the absence noted in `discovery-notes/brief-Prodesp - Atendimento Poupatempo.pdf.md` (page 63 architecture diagram).
