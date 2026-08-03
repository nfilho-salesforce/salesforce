# Plano de Entrega — DATAPREV-PAT (Reforma do PAT / MTE)

**Duração total do programa: 13 semanas (compromisso do usuário).** Modo **data-fixa, planejado de trás pra frente**, com datas comprometidas: **início 17/ago/2026 → homologação (UAT) início nov → go-live PRODUÇÃO 15/nov/2026** (marco de interoperabilidade total do Decreto 12.712/2025 + entrada do financeiro em produção).

> **A data é o âncora; o escopo é a variável de flexão.** O programa não comprime 18–38 semanas de trabalho em 13 — ele entrega um **MVP** dimensionado para a janela e mantém um conjunto de **candidatos a de-escopo** como buffer de cronograma. Se um risco de caminho crítico se materializar (org greenfield, MuleSoft on-premise, gateway, contratos de API), o buffer é acionado antes da data.

> **Estratégia de execução (premissa de arranque).** Definir o **modelo de dados fundacional** — objetos nativos Sales Cloud (Opportunity = demanda; Quote = resposta via API; termo de aceite) — **com o time de implementação inteiro primeiro**; só então **paralelizar as frentes de baixa/nenhuma dependência**. A paralelização é o que torna a data fixa viável.

## Marcos do programa (projeto · decreto · jornadas — UAT e PROD)

| Data | Tipo | Marco | Capacidades principais |
|------|------|-------|------------------------|
| 17/ago/2026 | Projeto | Kick-off / início | — |
| 30/ago/2026 | Projeto | Ambiente pronto | Org greenfield + MuleSoft on-premise + gateway selecionado |
| 27/set/2026 | Projeto | Modelo de dados fundacional ratificado | Habilita a paralelização das frentes |
| ~18/out/2026 | Jornada (UAT) | Marketplace + Credenciamento | Leilão reverso (Opportunity/Quote), credenciamento + vigilância sanitária |
| ~8/nov/2026 | Jornada (UAT) | Financeiro | Folha→boleto→conciliação→split completo |
| 01/nov/2026 | Jornada (UAT) | Homologação início | Todas as jornadas em ambiente de homologação |
| 15/nov/2026 | Projeto (PROD) | **Go-live produção** | Identidade gov.br, leilão reverso, credenciamento, financeiro folha→split |
| 15/nov/2026 | Decreto | Interoperabilidade total — Decreto 12.712/2025 | Reforma do PAT em vigor |

**Leitura honesta do arquiteto:** esta é uma janela **agressiva** para o escopo em jogo — uma épica XL (E03) + build sobre objetos nativos adaptados, três pré-requisitos externos de lead-time (org greenfield, MuleSoft on-premise, gateway), integração multi-sistema sem contratos (Novo PAT sem API). É entregável **como MVP** com o de-escopo abaixo tratado como buffer real, disciplina de caminho crítico na Fase 0/1 e uma janela de estabilização mínima. **Não é entregável como escopo completo, e a data de 15/nov pode não ser alcançável só com esforço se um pré-requisito da Fase 0 escorregar** — nesse caso o de-escopo (E03 primeiro) é o único trilho. As alavancas de segurança do cronograma estão nomeadas — não escondidas.

---

## Caminho crítico

**Fase 0 (org greenfield + MuleSoft on-premise + seleção do gateway) → Fase 1 (modelo de dados fundacional, com o time inteiro) → E05 (hub de integração) → E03 (folha, motor de split & conciliação) → homologação → estabilização.**

Três pré-requisitos externos de lead-time na Fase 0 — **provisionamento da org 100% greenfield** (ADR 0002/0005), **infra do MuleSoft on-premise** (ADR 0005, também o mecanismo de soberania de dados) e **seleção do gateway** — são o **maior risco** à data fixa; não estão sob controle da entrega. Depois deles, o **modelo de dados fundacional** (Fase 1) é o segundo gargalo: nada paraleliza até os objetos nativos estarem definidos. E01/E02/E04 dependem de E05; E03 depende de E05 + E08 + o gateway selecionado. Qualquer atraso cascateia direto para o go-live de 15/nov.

---

## Sequência de fases

### Fase 0 — Arranque, Provisionamento & Arquitetura (17/ago – 30/ago · 2 semanas)
- **Épicas:** — (fase de destrave, sem build)
- Provisionar a **org 100% greenfield** — instância nova, apartada de qualquer ambiente/admins Dataprev (ADR 0002/0005); **provisionar a infra do MuleSoft on-premise** (ADR 0005 — pré-requisito de marco *e* mecanismo de soberania de dados); **selecionar o provedor do gateway** (G0309, ADR 0003 — intermedia conta custódia, executa transações bancárias); resolver os blockers de arquitetura (fronteira de residência G0801, "Novo PAT sem API hoje" G0501, identidade × CPF-não-persiste G0106).
- **Sai com:** org greenfield acessível, MuleSoft on-premise no ar, gateway selecionado, ADR 0001 ratificado, inventário de integrações (com a lacuna do Novo PAT explicitada).

### Fase 1 — Fundação: Modelo de Dados + Identidade + Integração + Residência (31/ago – 27/set · 4 semanas) · *depende de: Fase 0*
- **Arranque com o TIME DE IMPLEMENTAÇÃO INTEIRO:** definição dos **objetos fundacionais nativos Sales Cloud** e **mapeamento de dados** — Account (facilitadora/beneficiária PJ), **Opportunity = demanda de leilão reverso da beneficiária**, **Quote = resposta de leilão da facilitadora via API**, termo de aceite (ADR 0004). **Este é o marco que libera a paralelização** — nenhuma frente de baixa dependência arranca antes dele.
- **Épicas (após o marco fundacional):** E05 (hub MuleSoft **on-premise**, mock-first — Novo PAT sem API obriga mock; gateway como alvo; **expõe o endpoint de consulta de demandas abertas às facilitadoras** — pull no MVP, push é futuro), E08 (residência/tokenização + isolamento greenfield/on-premise), E01 (portal **Experience Cloud — Partner Community** + login gov.br).
- Fase de maior carga; risco #1 (integração sem contratos) atacado primeiro. Comunicação de mudança (E09) arranca aqui.

### Fase 2 — Marketplace & Credenciamento (28/set – 18/out · 3 semanas) · *frente paralelizada · depende de: Fase 1 (marco fundacional, E01, E05)*
- **Épicas:** E02 (leilão reverso sobre **Opportunity/Quote nativos** — a facilitadora descobre as demandas abertas por **endpoint de consulta / pull via API** — API-only, sem push ativo no MVP; equidade por construção, seleção manual travada até o fechamento da vigência, **termo de aceite**; contrato **sem CLM** — PDF imutável versionado; **MVP sem Data Cloud**), E04 (credenciamento gov.br PJ/CNPJ + **vigilância sanitária** — 5000+ padrões, triagem IA com transbordo, alertas de vencimento de licença; consulta à Base Nacional Unificada de Estabelecimentos + API de adquirente).
- **Marco de entrega de jornada (UAT):** leilão reverso + credenciamento em homologação.

### Fase 3 — Financeiro: Folha, Motor de Split & Conciliação (19/out – 8/nov · 3 semanas) · *depende de: Fase 0 (gateway), Fase 1 (E05, E08)*
- **Épicas:** E03 (**XL** — o fluxo folha→pagamento→split completo, 8 passos): upload CSV da folha (portal/API) → validação de layout + integridade → crítica via melhor alternativa Salesforce (Einstein/agente); **linhas da folha NÃO persistem em objeto** (roadmap futuro) → facilitadora baixa por contrato/vigência → retorna "processado" + valor via API → plataforma envia valor ao **gateway** (intermedia conta custódia) → recebe **boleto registrado** + metadados/link → boleto disponível à beneficiária no portal → plataforma recebe movimentações bancárias do gateway → **identificação de pagamento em lotes incrementais via agendamento MuleSoft** → consulta regras de split → calcula repasse à facilitadora + demais → registra todo o racional/datas/split/ordens de transferência, entregando via MuleSoft ao **gateway (executor único das transações bancárias)**.
- Fase XL mais sensível à data fixa; **a homologação início nov abre ao fim desta fase.** Se algo escorrega, a pressão de de-escopo bate aqui primeiro.

### Fase 4 — Homologação, Carga Mínima, Adoção & Go-live PROD (9/nov – 15/nov · 1 semana) · *depende de: Fase 1 (E05)*
- **Épicas:** E07 (carga inicial **mínima**; Novo PAT permanece system-of-record), E09 (adoção enxuta, pico da comunicação).
- **Marcos:** projeto (**go-live PROD 15/nov**), decreto (interoperabilidade total — Decreto 12.712/2025), jornada (UAT→PROD). Janela de estabilização/hypercare mínima. Carga massiva e adoção completa ficam pós-go-live.

---

## Candidatos a de-escopo (buffer de cronograma)

Ordenados por primeiro-a-cair. Tratados como buffer — entram no MVP só se a janela permitir; saem primeiro se um risco de caminho crítico se materializar.

| # | Item | Épica | Justificativa |
|---|------|-------|---------------|
| 1 | **Agentforce — atendimento inteligente** | E06 (inteira) | Valor real, mas não é pré-requisito do go-live regulatório; canal WhatsApp/BSP + guardrails públicos somam risco e prazo. Fora do MVP. |
| 2 | **Data Cloud — enriquecimento/perfil** | E02 | Adição Assumed; o leilão reverso sobre Opportunity/Quote nativos funciona sem ele. |
| 3 | **Marketing Cloud / alertas** | E02/E06 | Ambiguidade de escopo (G0209); não bloqueia o fluxo core. A decisão de posicioná-lo depende do **canal da notificação ativa às facilitadoras** (roadmap futuro, G0211) — não travar enquanto o canal não for definido. |
| 4 | **Carga massiva de dados** | E07 | MVP carrega o mínimo; volume completo pós-go-live. |
| 5 | **Adoção completa** | E09 | MVP entrega capacitação essencial; programa completo de adoção pós-go-live. |

---

## Roadmap futuro (pós-MVP)

Distinto do buffer de de-escopo acima: estes itens **não fazem parte do MVP por decisão de escopo** (não há requisito para 15/nov), e ficam registrados como candidatos de versões seguintes. São capacidades conscientemente adiadas, não candidatos a corte.

| # | Item | Épica | Por que fora do MVP | Confirmação |
|---|------|-------|---------------------|-------------|
| 1 | **Persistência das linhas de folha em objeto da plataforma** (carga linha-a-linha, relatório de folha por trabalhador) | E03 | Sem requisito para 15/nov — no MVP a plataforma valida a integridade do CSV e o disponibiliza para download da facilitadora, mas **não carrega as linhas** em objeto. A persistência linha-a-linha habilita relatório de folha detalhado e é a base de uma futura conciliação por trabalhador. | Confirmado no grill 31/jul (G0310). |
| 2 | **Contract lifecycle management (CLM) + validação automatizada de contrato** | E02 | No MVP o contrato é PDF imutável versionado (upload de nova versão para aditivos/renovações), sem ferramenta de ciclo de vida nem validação automática. | Transcrição 31/jul (kb_sources E02). |
| 3 | **Notificação ativa (push) às facilitadoras quando uma beneficiária publica uma demanda** | E02 / E05 | No MVP a facilitadora descobre as demandas abertas por **endpoint de consulta (pull via API/MuleSoft)** — coerente com facilitadora API-only (ADR 0004); **não há push ativo**. A notificação ativa fica para versão futura, e **o canal ainda é indefinido** (e-mail, webhook/evento, WhatsApp/BSP, in-app ou jornada Marketing Cloud) — **a escolha do canal é o que decide se posicionamos ou não Marketing Cloud** (G0209/G0211). | Decisão 31/jul (G0207 resolvido para pull; G0211 aberto para o canal). |

---

## Processos padrão (transversais, não repetidos por fase)

- **Testes:** contínuos; QA amplifica-se e **surge** na janela de estabilização (financeiro regulado, data fixa) — não encolhe sob IA.
- **Deploy:** entregas incrementais na org dedicada; release management coordenado ao longo das fases.
- **Capacitação/adoção:** E09 transversal, comunicação desde a Fase 1, pico na Fase 4.

---

## Tabela de riscos consolidada

| Risco | Fase | Mitigação | Gap |
|-------|------|-----------|-----|
| Lead-time de provisionamento da org greenfield | 0 | Pedido no dia 1 da Fase 0; escalonar com a plataforma | ADR 0002/0005 |
| Infra MuleSoft on-premise não pronta no marco | 0 | Provisionar no dia 1; é pré-requisito de marco *e* soberania de dados | ADR 0005 |
| Seleção/integração do gateway atrasa | 0→3 | Selecionar cedo; contrato de integração mock na Fase 1 | G0309 |
| Modelo de dados fundacional atrasa (bloqueia paralelização) | 1 | Time inteiro no arranque; marco explícito antes de abrir frentes | ADR 0004 |
| Novo PAT sem API hoje (mock→real) | 1 | Mock-first obrigatório; governança de virada; lacuna explicitada na Fase 0 | G0501 |
| Fronteira de residência não ratificada | 0→1 | Ratificar com Jair Bogo antes do data model | G0801 |
| Regras de split/conciliação indefinidas | 3 | Definir na Fase 0/1; especialista de arquitetura financeira | G0304 |
| Data fixa 15/nov agressiva para o escopo XL do financeiro | 3→4 | De-escopo E03 como buffer; QA surge; ⚠ sinalizar se pré-requisito escorregar | — |
| Volume de carga desconhecido | 4 | Carga mínima no MVP; massiva pós-go-live | G0701 |

---

## Equipe

As disciplinas e o roster nomeado para entregar isto — com contagens defensáveis, por lane — vêm do **`estimate`**. Este documento é funcionalidade ao longo do tempo; não nomeia time. Observação para o `estimate`: E03 agora XL exige um **especialista de arquitetura financeira/bancária (split)** no roster de ambas as lanes, e a janela fixa de ~13 semanas precisa ser reconciliada com as faixas de duração derivadas.
