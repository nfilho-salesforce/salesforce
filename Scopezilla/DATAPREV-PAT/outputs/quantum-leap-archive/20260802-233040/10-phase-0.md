# Phase 0 — Arranque, Provisionamento & Arquitetura (17/ago – 30/ago · Sem. 1-2) (DATAPREV-PAT)

> 🛑 **DO NOT BUILD AGAINST THIS FILE — STUB.**
> Phase 0 has not been staged with a real build brief. The sections below contain placeholders only.
> Regenerate this phase via the `quantum-leap` skill before any planning or build action targets it.
> If the user asks you to plan or build Phase 0, **stop** and tell them the bundle needs to be regenerated.

## Phase metadata (planning only — not a build target)

- **Planning duration:** 2 weeks (per user commitment)
- **Outcome (from roadmap):** Início em 17/ago/2026. Destravar os pré-requisitos de arranque que têm lead-time externo e competem com a janela fixa: (1) provisionamento da INSTÂNCIA DEDICADA E APARTADA do MTE/PAT em ambiente 100% GREENFIELD (ADR 0002/0005) — pedido junto ao fornecedor/plataforma tem prazo próprio; (2) INFRAESTRUTURA MuleSoft ON-PREMISE pronta e acessível (ADR 0005) — instalação na infra soberana Dataprev/gov, pré-requisito de marco; (3) SELEÇÃO DO PROVEDOR DO GATEWAY / banco custódia (G0309, ADR 0003) — contratação de terceiro no caminho crítico do financeiro; (4) os blockers de arquitetura: fronteira campo-a-campo da residência híbrida (G0801, ratificar com Jair Bogo), inventário de contratos/Swaggers de API dos sistemas externos (G0501, Novo PAT sem API hoje), identidade Experience Cloud Partner Community × CPF-não-persiste (G0106). Iniciar engajamento CTID/ANPD e inventário das APIs das facilitadoras.
- **Measured by (from roadmap):** Org dedicada greenfield provisionada e acessível; MuleSoft on-premise instalado e acessível na infra soberana; provedor do gateway selecionado/contratação iniciada com escopo de integração acordado; ADR 0001 ratificado com fronteira campo-a-campo definida; inventário de contratos de API por sistema (existe/não existe). MARCO DE PROJETO: kick-off e ambiente pronto ao fim da Sem. 2.

## Epics tentatively in scope for this phase

These are the epics roadmap.json assigned to Phase 0. They will become a real build target when this phase is staged via the `quantum-leap` skill — until then, **do not build against them**.

_(no epics tied to this phase)_

## Dependencies and risks (from roadmap)

**Dependencies:** Nenhuma — é a fase que precede tudo. Requer disponibilidade da arquitetura Dataprev (Jair Bogo), dos donos dos sistemas externos, a INFRA (org + MuleSoft on-premise) pronta nos marcos, e a decisão do cliente sobre o provedor do gateway.

**Risks:** PROVISIONAMENTO DA ORG + INFRA MuleSoft ON-PREMISE + CONTRATAÇÃO DO GATEWAY SÃO O MAIOR RISCO À DATA FIXA — três lead-times de terceiros que consomem a janela e não estão sob controle da entrega. Se qualquer um atrasar além da Fase 0, o go-live de 15/nov fica em risco e o financeiro (E03) é o primeiro candidato a fatiar. Se a infra on-premise não estiver pronta no marco, a Fundação não arranca. Novo PAT sem API mantém E05 mock-first — caminho crítico aberto.

---

To stage this phase as a real build target, re-run the `quantum-leap` skill and select Phase 0. The skill will produce intent, pre-decided constraints, plan-mode questions, build targets, and dual-shaped acceptance for the agent to use.
