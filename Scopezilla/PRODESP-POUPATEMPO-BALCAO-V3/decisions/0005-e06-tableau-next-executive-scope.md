# 0005 — E06 é construído em Tableau Next, entregando relatório executivo formal (não apenas exposição operacional nativa)

**Date:** 2026-09-24 · **Status:** accepted · **Source:** client-supplied (AskUserQuestion, 2026-09-23)

## Context

E06 citava "Tableau" sem especificar produto — classic Tableau, CRM Analytics e Tableau Next são três SKUs de licenciamento, modelos de conectividade e esforços de build distintos (G0601); a knowledge base do projeto só cobre Tableau Next. Separadamente, o Omni-Channel já expõe ociosidade/disponibilidade de fila nativamente e em tempo real via Command Center for Service — E06 não dizia se o pedido era (a) expor essa visão nativa, (b) uma camada histórica/trend, ou (c) um entregável executivo/client-facing com cadência recorrente (G0602/G0604). Como o account owner adicionou E06 nesta sessão sem precedente em nenhuma fonte de discovery original, nenhuma dessas escolhas podia ser inferida do material do cliente — eram forks genuínos, roteados ao usuário via AskUserQuestion em vez de decididos silenciosamente.

O usuário escolheu, para ambas as perguntas, a opção de maior escopo: Tableau Next como produto, e relatório executivo formal (não a exposição nativa/operacional interna que havia sido recomendada como default menor).

## Decision

E06 é construído em **Tableau Next**. O entregável é um **relatório executivo formal e client-facing**, com camada histórica/trend própria (não apenas a visão nativa em tempo real do Command Center) e cadência de atualização recorrente — não um dashboard operacional interno de baixo esforço. Isso implica, como corolário direto: (i) a instrumentação de custo/resposta do WhatsApp (G0603) e o funil de causa/frequência de fila-vazia (ver decisions/0002) tornam-se escopo explícito de build de E06, pois o relatório executivo depende desses dados existirem; (ii) o tier de licenciamento e o esforço de integração de dados são dimensionados para Tableau Next, não para as alternativas mais baratas descartadas.

## Consequences

- Sizing/estimate de E06 parte de uma base maior do que a recomendação original (exposição nativa quase-zero-esforço) — este ADR existe justamente para que design/estimate não subestimem E06 revertendo silenciosamente ao default menor.
- E06 herda dependência direta da instrumentação de decisions/0002 — sem ela, o relatório executivo não tem dado de causa/funil para mostrar.
- Reversão desta premissa (redimensionar E06 para exposição nativa) é uma decisão de corte de escopo, não uma correção de ambiguidade — deve voltar ao usuário, não ser assumida.

## Grounds

`data/gaps.json` G0601, G0602, G0603, G0604 — citando o inventário BPMN (Command Center for Service, knowledge/tableau_next_4-10-2026.md:7303-7393). Decisão do usuário via AskUserQuestion, 2026-09-23: "Tableau Next" e "Relatório executivo formal" — ambas as respostas de maior escopo, não as recomendadas por padrão.
