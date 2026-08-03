# Fase 0 — Arranque, Provisionamento & Arquitetura (17/ago – 30/ago · Sem. 1-2) (DATAPREV-PAT)

> 🛑 **NÃO CONSTRUA A PARTIR DESTE ARQUIVO — ESBOÇO (STUB).**
> Fase 0 não foi preparada (staged) com um brief de construção real. As seções abaixo contêm apenas placeholders.
> Regere esta fase via a skill `quantum-leap` antes de qualquer ação de planejamento ou construção mirá-la.
> Se o usuário pedir para você planejar ou construir a Fase 0, **pare** e diga a ele que o bundle precisa ser regerado.

## Metadados da fase (apenas planejamento — não é alvo de construção)

- **Duração de planejamento:** 2 semanas (compromisso do usuário)
- **Resultado (do roadmap):** Início em 17/ago/2026. Destravar os pré-requisitos de arranque que têm lead-time externo e competem com a janela fixa: (1) provisionamento da INSTÂNCIA DEDICADA E APARTADA do MTE/PAT em ambiente 100% GREENFIELD (ADR 0002/0005) — pedido junto ao fornecedor/plataforma tem prazo próprio; (2) INFRAESTRUTURA MuleSoft ON-PREMISE pronta e acessível (ADR 0005) — instalação na infra soberana Dataprev/gov, pré-requisito de marco; (3) SELEÇÃO DO PROVEDOR DO GATEWAY / banco custódia (G0309, ADR 0003) — contratação de terceiro no caminho crítico do financeiro; (4) os blockers de arquitetura: fronteira campo-a-campo da residência híbrida (G0801, ratificar com Jair Bogo), inventário de contratos/Swaggers de API dos sistemas externos (G0501, Novo PAT sem API hoje), identidade Experience Cloud Partner Community × CPF-não-persiste (G0106). Iniciar engajamento CTID/ANPD e inventário das APIs das facilitadoras.
- **Medido por (do roadmap):** Org dedicada greenfield provisionada e acessível; MuleSoft on-premise instalado e acessível na infra soberana; provedor do gateway selecionado/contratação iniciada com escopo de integração acordado; ADR 0001 ratificado com fronteira campo-a-campo definida; inventário de contratos de API por sistema (existe/não existe). MARCO DE PROJETO: kick-off e ambiente pronto ao fim da Sem. 2.

## Épicas tentativamente no escopo desta fase

Estas são as épicas que o roadmap.json atribuiu à Fase 0. Elas se tornarão um alvo de construção real quando esta fase for preparada (staged) via a skill `quantum-leap` — até lá, **não construa a partir delas**.

_(nenhuma épica vinculada a esta fase)_

## Dependências e riscos (do roadmap)

**Dependências:** Nenhuma — é a fase que precede tudo. Requer disponibilidade da arquitetura Dataprev (Jair Bogo), dos donos dos sistemas externos, a INFRA (org + MuleSoft on-premise) pronta nos marcos, e a decisão do cliente sobre o provedor do gateway.

**Riscos:** PROVISIONAMENTO DA ORG + INFRA MuleSoft ON-PREMISE + CONTRATAÇÃO DO GATEWAY SÃO O MAIOR RISCO À DATA FIXA — três lead-times de terceiros que consomem a janela e não estão sob controle da entrega. Se qualquer um atrasar além da Fase 0, o go-live de 15/nov fica em risco e o financeiro (E03) é o primeiro candidato a fatiar. Se a infra on-premise não estiver pronta no marco, a Fundação não arranca. Novo PAT sem API mantém E05 mock-first — caminho crítico aberto.

---

Para preparar esta fase como um alvo de construção real, rode novamente a skill `quantum-leap` e selecione Fase 0. A skill produzirá intenção, restrições pré-decididas, perguntas do modo Plan, alvos de construção e aceite de dupla forma para o agente usar.
