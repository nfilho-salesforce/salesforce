# Atendimento Digital — Caso de Uso e Desenho de Solução (Isolado)

*Gerado em 23/09/2026 · Consolidação de sync interna Salesforce de 22/09/2026 (participantes: Nelson Stebulaitis Filho, Larisse Gois, Juliana Brites, Pedro Ganem Filho, Renata Vendramini, Osvaldo Melo, Rafael Marques, Juliane Lopes, Viviani Hupp).*

> **Status: exploração isolada.** Este documento reflete a interpretação de uma reunião interna de alinhamento — não uma decisão fechada com a Prodesp. Por decisão explícita, **não foi incorporado** a `data/epics.json`, `data/gaps.json` ou qualquer outro arquivo canônico do projeto Scopezilla, e nenhuma skill de revisão (`revise`, `grill-me-on-scope`) foi executada sobre ele. Mantém-se separado até o fechamento do desenho de solução.

---

## 1. Objetivo do caso de uso

Estender o atendimento presencial do Poupatempo para um canal digital que permite (a) antecipar digitalmente um atendimento já agendado, e (b) redirecionar a demanda de uma unidade sobrecarregada para um atendente ocioso em outra unidade — sem exigir que a cidadã se desloque novamente ou que a Prodesp contrate capacidade adicional.

Não é uma fila digital em tempo real: o gatilho é sempre um agendamento pré-existente na mesma API externa que o Agentforce já consulta hoje. Sem agendamento prévio, não há antecipação digital — está fora de escopo nesta fase.

## 2. Atores

- **Cidadã** — já possui um agendamento; recebe a oferta de antecipação via WhatsApp e, se aceitar, é atendida remotamente.
- **Atendente** — opera pelo Slack (front-end); pode atender casos da própria unidade ou, quando ocioso, casos originados em outra unidade.
- **Motor de notificação e roteamento** — camada de decisão que identifica a janela de antecipação, avalia disponibilidade de atendentes e decide o roteamento cross-posto.

## 3. Fluxo de processo e informação

| # | Etapa | O que acontece | Sistema tocado | Status |
|---|---|---|---|---|
| 1 | Cidadã possui agendamento ativo | Ponto de partida sempre é um agendamento já existente na mesma API externa que o Agentforce já consulta hoje | Sistema externo de agendamento | Confirmado na sync |
| 2 | Motor de notificação identifica janela de antecipação | Duas soluções técnicas em avaliação em paralelo (uma já apresentada, outra propondo uma camada intermediária adicional entre Slack e o back-end) | Motor de disparo proativo | **Em aberto** — maior dúvida da sync (risco de estabilidade) |
| 3 | WhatsApp institucional oferece antecipação | Canal dedicado, somente recepção — 100% da demanda digital, sem transbordo para atendimento tradicional | WhatsApp institucional | Confirmado na sync |
| 4 | Cidadã aceita → caso entra na fila de roteamento | O caso passa a ser gerenciado pelo motor de roteamento, desacoplado da unidade física de origem | Service Cloud | Confirmado na sync |
| 5 | Sinal de disponibilidade do atendente | Omni-Channel padrão (atendente fica "online") vs. flow customizado no Slack (atendente se declara disponível); camada preditiva sugerida por Rafael Marques para pré-atribuir o caso | Presença — Omni-Channel ou Slack | **Em aberto** — decisão para o discovery formal |
| 6 | Roteamento entre postos | Atendente ocioso em outra unidade (ex.: Santo Amaro) assume virtualmente o caso de uma cidadã agendada em unidade sobrecarregada (ex.: Sé); agendamento original permanece amarrado à unidade de origem para registro | Motor de roteamento cross-posto | Confirmado na sync |
| 7 | Atendimento no posto de trabalho | Atendente conduz o atendimento pelo Slack; Service Cloud sustenta o back-end de caso e fila — a cidadã nunca vê Service Cloud | Slack (front) + Service Cloud (back) | Confirmado na sync |
| 8 | Encerramento e indicadores | Caso fechado, registro atualizado; indicadores cross-sistema (WhatsApp + Slack + Service Cloud + agendamento externo) sem fonte da verdade definida | Analytics / Tableau | **Em aberto** — risco levantado por Renata Vendramini, reconhecido por Rafael Marques |

## 4. Arquitetura da solução

| Camada | Componente | Descrição |
|---|---|---|
| 1 | Canal da cidadã | WhatsApp institucional, dedicado e somente recepção |
| 2 | Motor de notificação e roteamento | Disparo proativo (2 soluções em avaliação) + sinal de disponibilidade (Omni-Channel ou Slack) + roteamento cross-posto — núcleo de decisão do fluxo |
| 3 | Posto de trabalho do atendente | Slack (front-end) + Service Cloud (back-end) |
| 4 | Sistemas externos & indicadores | API externa de agendamento (fora do Salesforce) + Tableau — fonte da verdade cross-sistema ainda em discussão |

**Decisão de arquitetura citada na sync (não fechada):** internalizar o agendamento no Scheduler nativo do Service Cloud foi proposto por Renata Vendramini para melhorar visibilidade, mas Rafael Marques contrapôs que a Prodesp não tem controle total da agenda hoje (sistema externo dispara) — internalizar criaria uma dependência arriscada. Discussão parada para fórum futuro, não é uma decisão tomada.

## 5. Pontos em aberto desta sync

1. **Motor de disparo proativo** (Camada 2) — duas soluções técnicas em avaliação, ainda não reconciliadas.
2. **Modelo de disponibilidade do atendente** (Camada 2) — Omni-Channel vs. Slack customizado; camada preditiva sugerida, não decidida.
3. **Fonte da verdade dos indicadores** (Camada 4) — agendamento externo ao Service Cloud, sem definição de fonte cross-sistema.
4. **Scheduler nativo do Service Cloud** (Camada 4) — proposto, mas com dependência de controle de agenda ainda 100% externa.
5. **Granularidade de dashboards/Tableau** (Camada 4) — risco de repetir esforço custoso observado em outro projeto (dados fragmentados, parte só na Meta).
6. **Sinal de ocupação/fila por posto** (Camada 2) — ainda sem fonte identificada; mesmo gap já mapeado no escopo formal do programa (G0315).

## 6. Modelo comercial mencionado

Capacidade fixa por nuvem (Service/SLC, Omni, Tableau), paga por entrega — não escopo fixo, revisada a cada detalhamento. Ainda não formalizada em `data/commercials.json`.

## 7. Encaminhamentos da própria sync

- Nelson bloqueou a agenda do dia seguinte (23/09) para detalhar o desenho de solução, consultando Rafael Marques e Osvaldo Melo caso a caso.
- Juliana Brites leva à proposta um mapa de arquitetura inicial + cronograma por casos de uso + estimativa muito inicial.
- Pedro Ganem Filho confirmou que a proposta de licenciamento já está pronta para compartilhar.
- Larisse Gois vai preparar um documento interno complementar consolidando o validado nesta call.

---

**Nota de rastreabilidade:** os pontos em aberto listados aqui não foram escritos em `data/gaps.json`. Quando o desenho de solução for fechado e a incorporação formal ao projeto for decidida, os itens 1–6 acima são os candidatos naturais a entrar no gap register formal (ou a alimentar uma rodada de `revise`).
