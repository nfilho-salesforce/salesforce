# Plano de Entrega — DATAPREV-PAT (Reforma do PAT / MTE)

**Duração do programa: 17 semanas — 13 de build (Fase 1) + 4 de Scale/Hypercare.** Modo **data-fixa, planejado de trás pra frente**, com datas comprometidas: **build 17/ago/2026 → homologação (UAT) a partir da entrega do Marketplace → go-live PRODUÇÃO 15/nov/2026** (marco de interoperabilidade total do Decreto 12.712/2025 + entrada do financeiro em produção) → **Scale/Hypercare 16/nov – 13/dez/2026**. Em **paralelo**, a partir de S10, corre a **frente de Painéis Analíticos (Tableau, E10)** — off-critical-path, sem exigência de terminar em 15/nov.

> **A data é o âncora; o escopo é a variável de flexão.** O programa não comprime 18–38 semanas de trabalho em 13 — ele entrega um **Fase 1** dimensionado para a janela e mantém um conjunto de **candidatos a de-escopo** como buffer de cronograma. Se um risco de caminho crítico se materializar (org greenfield, gateway, contratos de API), o buffer é acionado antes da data.

> **MuleSoft reusa a instalação on-premise existente (ADR 0006).** A Dataprev já opera MuleSoft on-premise em produção; o programa **reusa** essa plataforma em vez de aprovisionar uma nova. Isso **elimina as 2 semanas iniciais de aprovisionamento** (antiga Etapa 0) e permite **mesclar a Definição de Arquitetura ao Planning & Design da Fundação** — a Fundação continua com 4 semanas, mas **inicia na Semana 1**. A folga liberada foi redistribuída em **janelas de desenvolvimento mais longas e em paralelo**, reduzindo o risco de prazo. A instância **Salesforce dedicada permanece 100% greenfield** (ADR 0002) — o reuso é exclusivo do MuleSoft.

> **Estratégia de execução (premissa de arranque).** Definir o **modelo de dados fundacional** — objetos nativos Sales Cloud (Opportunity = demanda; Quote = resposta via API; termo de aceite) — **com o time de implementação inteiro primeiro**, dentro da Fundação; só então **paralelizar as frentes de baixa/nenhuma dependência** (Marketplace e Financeiro correm em paralelo). A paralelização é o que torna a data fixa viável.

## Marcos do programa (projeto · decreto · jornadas — UAT e PROD)

| Data | Tipo | Marco | Capacidades principais |
|------|------|-------|------------------------|
| 17/ago/2026 (S1) | Projeto | Kick-off / início | Fundação arranca na Sem. 1 (arquitetura mesclada ao P&D) |
| 13/set/2026 (S4) | Projeto | Modelo de dados fundacional ratificado | Habilita a paralelização das frentes; frente MuleSoft em curso |
| ~11/out/2026 (S8) | Jornada (UAT) | Início da homologação — a partir da entrega do Marketplace | Leilão reverso (Opportunity/Quote), credenciamento + vigilância sanitária |
| 25/out/2026 (S10) | Jornada (UAT) | Marketplace + Credenciamento completos | Leilão reverso e credenciamento em homologação |
| 1/nov/2026 (S11) | Jornada (UAT) | Financeiro completo | Folha→boleto→conciliação→split completo |
| 15/nov/2026 (S13) | Projeto (PROD) | **Go-live produção** | Identidade gov.br, leilão reverso, credenciamento, financeiro folha→split |
| 15/nov/2026 | Decreto | Interoperabilidade total — Decreto 12.712/2025 | Reforma do PAT em vigor |
| 16/nov – 13/dez/2026 (S14-S17) | Projeto | **Scale / Hypercare** | Sustentar, manter e conduzir o cutover à Dataprev |
| 19/out – 23/nov/2026 (S10-S15) | Projeto (paralelo) | **Painéis Analíticos (Tableau)** — off-critical-path | Até 3 painéis (Negócio/Projeto/MTE), até 12 componentes, sobre a instalação Tableau existente |

**Leitura honesta do arquiteto:** esta continua sendo uma janela **agressiva** para o escopo em jogo — uma épica XL (E03) + build sobre objetos nativos adaptados, integração multi-sistema sem contratos (Novo PAT sem API). O **reuso do MuleSoft on-premise (ADR 0006)** removeu um dos três pré-requisitos de lead-time e devolveu folga ao cronograma, que foi reinvestida em **janelas de dev mais longas e paralelas** — menor risco de prazo, não menor duração de build. É entregável **como Fase 1** com o de-escopo abaixo tratado como buffer real, disciplina de caminho crítico na Fundação e uma janela de estabilização de 2 semanas seguida de 4 semanas de Scale/Hypercare. **Não é entregável como escopo completo, e a data de 15/nov pode não ser alcançável só com esforço se um pré-requisito escorregar** (org greenfield, gateway, acessos à plataforma MuleSoft existente) — nesse caso o de-escopo (E03 primeiro) é o único trilho. As alavancas de segurança do cronograma estão nomeadas — não escondidas.

---

## Caminho crítico

**Fundação (modelo de dados fundacional + arquitetura, com o time inteiro, S1-S4) → E05 frente MuleSoft contínua (hub de integração, S1-S11) → E03 (folha, motor de split & conciliação, frente Financeiro paralela S6-S11) → homologação (UAT S8-S13) → carga mínima (S12-S13) → go-live 15/nov → Scale/Hypercare (S14-S17).**

Com o **reuso do MuleSoft on-premise (ADR 0006)**, some o pré-requisito "instalação on-premise pronta a tempo". Restam dois destravamentos externos: **provisionamento da org 100% greenfield** (ADR 0002) e **seleção/contratação do gateway** (ADR 0003) — mais **acessos, ambientes e capacidade** na instalação MuleSoft existente (Client IT). O **modelo de dados fundacional** (Fundação) é o gargalo interno: nada paraleliza até os objetos nativos estarem definidos, e isso agora acontece já na Sem. 1-4. E01/E02/E04 dependem de E05; E03 depende de E05 + E08 + o gateway. A **frente MuleSoft (E05)** corre continuamente por todo o P&D e DEV (S1-S11), sob um Arquiteto Técnico MuleSoft dedicado.

---

## Sequência de fases

### Fundação — Modelo de Dados + Arquitetura + Identidade + Integração + Residência (17/ago – 13/set · 4 semanas · S1-S4) · *inicia na Semana 1*
- **Arranque com o TIME DE IMPLEMENTAÇÃO INTEIRO:** definição dos **objetos fundacionais nativos Sales Cloud** e **mapeamento de dados** — Account (facilitadora/beneficiária PJ), **Opportunity = demanda de leilão reverso da beneficiária**, **Quote = resposta de leilão da facilitadora via API**, termo de aceite (ADR 0004). **A Definição de Arquitetura foi mesclada a esta fase (ADR 0006)** — sem uma Etapa 0 isolada. **Este é o marco que libera a paralelização** — nenhuma frente de baixa dependência arranca antes dele.
- **Destrave em paralelo ao P&D:** resolver os blockers de arquitetura (fronteira de residência G0801 com Jair Bogo, "Novo PAT sem API hoje" G0501, identidade × CPF-não-persiste G0106); **confirmar acessos/ambientes/capacidade na instalação MuleSoft on-premise existente** (ADR 0006); **provisionar a org 100% greenfield** (ADR 0002); **selecionar o provedor do gateway** (G0309, ADR 0003).
- **Épicas:** E05 (frente MuleSoft **on-premise reusado**, mock-first — Novo PAT sem API obriga mock; gateway como alvo; **expõe o endpoint de consulta de demandas abertas às facilitadoras** — pull na Fase 1, push é futuro), E08 (residência/tokenização + isolamento; org greenfield + MuleSoft on-premise reusado), E01 (portal **Experience Cloud — Partner Community** + login gov.br).
- Fase de maior carga fundacional; risco #1 (integração sem contratos) atacado primeiro. Comunicação de mudança (E09) arranca aqui.
- **Sai com:** modelo de dados fundacional ratificado, org greenfield acessível, acessos ao MuleSoft on-premise confirmados, gateway selecionado, ADR 0001 ratificado, inventário de integrações (com a lacuna do Novo PAT explicitada).

### Marketplace & Credenciamento (14/set – 25/out · 6 semanas · S5-S10, 2 sprints de 3 semanas) · *frente paralelizada · depende de: Fundação (marco fundacional, E01, E05)*
- **Épicas:** E02 (leilão reverso sobre **Opportunity/Quote nativos** — a facilitadora descobre as demandas abertas por **endpoint de consulta / pull via API** — API-only, sem push ativo na Fase 1; equidade por construção, seleção manual travada até o fechamento da vigência, **termo de aceite**; contrato **sem CLM** — PDF imutável versionado; **Fase 1 sem Data Cloud**), E04 (credenciamento gov.br PJ/CNPJ + **vigilância sanitária** — 5000+ padrões, triagem IA com transbordo, alertas de vencimento de licença; consulta à Base Nacional Unificada de Estabelecimentos + API de adquirente).
- **2 sprints de 3 semanas** dão janelas de dev mais longas e menor risco. **A entrega do Marketplace ancora o início da UAT (S8).**
- **Marco de entrega de jornada (UAT):** leilão reverso + credenciamento em homologação ao fim de S10.

### Financeiro — Folha, Motor de Split & Conciliação (21/set – 1/nov · 6 semanas · S6-S11) · *frente paralelizada, arranca junto com o Marketplace · depende de: Fundação (E05, E08), gateway*
- **Épicas:** E03 (**XL** — o fluxo folha→pagamento→split completo, 8 passos): upload CSV da folha (portal/API) → validação de layout + integridade → crítica via melhor alternativa Salesforce (Einstein/agente); **linhas da folha NÃO persistem em objeto** (roadmap futuro) → facilitadora baixa por contrato/vigência → retorna "processado" + valor via API → plataforma envia valor ao **gateway** (intermedia conta custódia) → recebe **boleto registrado** + metadados/link → boleto disponível à beneficiária no portal → plataforma recebe movimentações bancárias do gateway → **identificação de pagamento em lotes incrementais via agendamento MuleSoft** → consulta regras de split → calcula repasse à facilitadora + demais → registra todo o racional/datas/split/ordens de transferência, entregando via MuleSoft ao **gateway (executor único das transações bancárias)**.
- **Paralelizada com o Marketplace** (arranca em S6, logo após o marco fundacional), com um **Consultor Técnico** dedicado à frente Financeiro em tempo integral e a frente MuleSoft dando suporte contínuo. Fase XL mais sensível à data fixa; se algo escorrega, a pressão de de-escopo bate aqui primeiro.

### Homologação (UAT) — a partir da entrega do Marketplace (5/out – 14/nov · 6 semanas · S8-S13) · *depende das entregas incrementais das frentes*
- **UAT antecipado:** arranca a partir da **entrega do Marketplace (S8)** e corre em paralelo às frentes, ganhando **+1 semana de UAT** frente ao plano anterior. QA em teste contínuo, com **surge** no hardening pré-go-live (financeiro regulado, data fixa).
- Homologa jornada a jornada conforme cada frente entrega: Marketplace/Credenciamento (S10), Financeiro (S11), depois estabilização integrada.

### Carga Mínima, Adoção & Go-live PROD (2/nov – 15/nov · 2 semanas · S12-S13) · *depende de: Fundação (E05)*
- **Épicas:** E07 (**carga inicial mínima em 2 semanas — as duas últimas**; Novo PAT permanece system-of-record), E09 (adoção enxuta, pico da comunicação).
- **Marcos:** projeto (**go-live PROD 15/nov**), decreto (interoperabilidade total — Decreto 12.712/2025), jornada (UAT→PROD). Carga massiva e adoção completa ficam pós-go-live.

### Scale / Hypercare (16/nov – 13/dez · 4 semanas · S14-S17) · *pós-go-live*
- **Time enxuto de sustentação, escopo estritamente delimitado.** Responsabilidade **restrita a três atividades: sustentar, manter e conduzir o cutover** para a Dataprev. **Não há novo desenvolvimento de escopo** nesta fase.
- **Time (reusa perfis do build):** **1 Consultor Técnico integral** (40h/sem — reforçado de 0,5 para 1,0 em 03/ago, pois sustentar/manter a plataforma sob dinheiro real é trabalho de período integral), **0,5 Dev MuleSoft** (20h/sem), **10h/sem de Arquiteto Técnico** e **10h/sem de Senior PM** (o mesmo arquiteto e o mesmo PM do build) — nas 4 semanas.
  - **Sustentar:** estabilização em produção, triagem e correção de defeitos, apoio aos primeiros ciclos financeiros reais.
  - **Manter:** manter rotas MuleSoft on-premise, conciliação e split operando; ajustes finos de configuração.
  - **Cutover:** transferência ordenada de operação e conhecimento à Dataprev (handover) ao fim da Sem. 17.

### Painéis Analíticos — Tableau (19/out – 23/nov · 6 semanas · S10-S15) · *frente paralela, OFF-CRITICAL-PATH · incremento 04/ago*
- **Frente nova, delimitada, fora do caminho crítico.** Inicia em S10 e **não tem exigência de terminar em 15/nov** — roda em paralelo ao build e ao início do Scale, sem gatear o go-live regulatório.
- **Escopo (E10):** até **3 painéis** — **Visão Negócio**, **Visão Projeto** e **Visão MTE** — com até **12 componentes no total** entre gráficos e tabelas. Reusa a **instalação Tableau EXISTENTE** do cliente (sem provisionamento de infra).
- **Fonte de dados (premissa):** ~80% nativa Salesforce (E02/E03/E04 via Salesforce connector) + 1 blend leve; **RLS por perfil** com 3 layouts de audiência. Métricas/campos exatos por painel a detalhar em workshop de descoberta no arranque da janela (G1001-G1003).
- **Time (esforço real, 280h):** 1 **Analytics - Technical Consultant** integral (240h) + **Solution Architect** fracional (40h, reusa o SA do build). Estimada pelo esforço real conforme diretriz — não só por T-shirt.

---

## Candidatos a de-escopo (buffer de cronograma)

Ordenados por primeiro-a-cair. Tratados como buffer — entram na Fase 1 só se a janela permitir; saem primeiro se um risco de caminho crítico se materializar.

| # | Item | Épica | Justificativa |
|---|------|-------|---------------|
| 1 | **Agentforce — atendimento inteligente** | E06 (inteira) | Valor real, mas não é pré-requisito do go-live regulatório; canal WhatsApp/BSP + guardrails públicos somam risco e prazo. Fora da Fase 1. |
| 2 | **Data Cloud — enriquecimento/perfil** | E02 | Adição Assumed; o leilão reverso sobre Opportunity/Quote nativos funciona sem ele. |
| 3 | **Marketing Cloud / alertas** | E02/E06 | Ambiguidade de escopo (G0209); não bloqueia o fluxo core. A decisão de posicioná-lo depende do **canal da notificação ativa às facilitadoras** (roadmap futuro, G0211) — não travar enquanto o canal não for definido. |
| 4 | **Carga massiva de dados** | E07 | Fase 1 carrega o mínimo (2 semanas); volume completo pós-go-live. |
| 5 | **Adoção completa** | E09 | Fase 1 entrega capacitação essencial; programa completo de adoção pós-go-live. |

---

## Roadmap futuro (Fase 2)

Distinto do buffer de de-escopo acima: estes itens **não fazem parte da Fase 1 por decisão de escopo** (não há requisito para 15/nov), e ficam registrados como candidatos de versões seguintes. São capacidades conscientemente adiadas, não candidatos a corte.

| # | Item | Épica | Por que fora da Fase 1 | Confirmação |
|---|------|-------|---------------------|-------------|
| 1 | **Persistência das linhas de folha em objeto da plataforma** (carga linha-a-linha, relatório de folha por trabalhador) | E03 | Sem requisito para 15/nov — na Fase 1 a plataforma valida a integridade do CSV e o disponibiliza para download da facilitadora, mas **não carrega as linhas** em objeto. A persistência linha-a-linha habilita relatório de folha detalhado e é a base de uma futura conciliação por trabalhador. | Confirmado no grill 31/jul (G0310). |
| 2 | **Contract lifecycle management (CLM) + validação automatizada de contrato** | E02 | Na Fase 1 o contrato é PDF imutável versionado (upload de nova versão para aditivos/renovações), sem ferramenta de ciclo de vida nem validação automática. | Transcrição 31/jul (kb_sources E02). |
| 3 | **Notificação ativa (push) às facilitadoras quando uma beneficiária publica uma demanda** | E02 / E05 | Na Fase 1 a facilitadora descobre as demandas abertas por **endpoint de consulta (pull via API/MuleSoft)** — coerente com facilitadora API-only (ADR 0004); **não há push ativo**. A notificação ativa fica para versão futura, e **o canal ainda é indefinido** (e-mail, webhook/evento, WhatsApp/BSP, in-app ou jornada Marketing Cloud) — **a escolha do canal é o que decide se posicionamos ou não Marketing Cloud** (G0209/G0211). | Decisão 31/jul (G0207 resolvido para pull; G0211 aberto para o canal). |

---

## Processos padrão (transversais, não repetidos por fase)

- **Testes:** contínuos; QA amplifica-se e **surge** na janela de estabilização/UAT (financeiro regulado, data fixa) — não encolhe sob IA. UAT antecipado a partir da entrega do Marketplace (S8).
- **Deploy:** entregas incrementais na org dedicada; release management coordenado ao longo das fases.
- **Capacitação/adoção:** E09 transversal, comunicação desde a Fundação, pico na carga/go-live.
- **Integração:** frente MuleSoft (E05) contínua por todo o P&D e DEV (S1-S11) sobre a plataforma on-premise reusada.

---

## Tabela de riscos consolidada

| Risco | Fase | Mitigação | Gap |
|-------|------|-----------|-----|
| Lead-time de provisionamento da org greenfield | Fundação | Pedido no dia 1; escalonar com a plataforma | ADR 0002 |
| Acessos/ambientes/capacidade na instalação MuleSoft on-premise existente | Fundação | Confirmar no dia 1; reuso (ADR 0006) remove a instalação, não os acessos | ADR 0006 |
| Seleção/integração do gateway atrasa | Fundação→Financeiro | Selecionar cedo; contrato de integração mock na Fundação | G0309 |
| Modelo de dados fundacional atrasa (bloqueia paralelização) | Fundação | Time inteiro no arranque; marco explícito antes de abrir frentes | ADR 0004 |
| Novo PAT sem API hoje (mock→real) | Fundação→frente MuleSoft | Mock-first obrigatório; governança de virada; frente MuleSoft contínua | G0501 |
| Fronteira de residência não ratificada | Fundação | Ratificar com Jair Bogo antes do data model | G0801 |
| Regras de split/conciliação indefinidas | Financeiro | Definir na Fundação; Consultor Técnico dedicado à frente Financeiro | G0304 |
| Data fixa 15/nov agressiva para o escopo XL do financeiro | Financeiro→carga | De-escopo E03 como buffer; QA surge; ⚠ sinalizar se pré-requisito escorregar | — |
| Volume de carga desconhecido | Carga | Carga mínima em 2 semanas na Fase 1; massiva pós-go-live | G0701 |

---

## Equipe

As disciplinas e o roster nomeado para entregar isto — com contagens defensáveis, por lane — vêm do **`estimate`**. Este documento é funcionalidade ao longo do tempo; não nomeia time. Observação para o `estimate`: o build foi **re-derivado por janela** (não por índice de fase) sobre o plano paralelizado; E05 é uma **frente MuleSoft contínua** (S1-S11) com um **Arquiteto Técnico MuleSoft** dedicado (integral nas 4 primeiras semanas, 20h/sem nas semanas de dev); E03 XL exige um **Consultor Técnico** dedicado à frente Financeiro (split/conciliação) em tempo integral; e há **4 semanas de Scale/Hypercare** (S14-S17) com time enxuto reusando perfis do build (1,0 Consultor Técnico integral + 0,5 Dev MuleSoft + 10h/sem Arquiteto Técnico + 10h/sem Senior PM). A accountability antes atribuída a um Engagement Manager separado foi **absorvida pelo Senior PM** em dedicação integral. **Frente Tableau (E10, incremento 04/ago):** 1 **Analytics - Technical Consultant** integral (240h) + **Solution Architect** fracional (40h, reusa o SA do build) na janela paralela S10-S15 = 280h, estimadas pelo **esforço real**.
