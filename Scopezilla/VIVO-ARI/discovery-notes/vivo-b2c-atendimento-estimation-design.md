# Vivo B2C Atendimento — ROM Estimation Design

> **Saída de estimativa da Phase 0.** Deriva do story map não-estimado
> `architecture/vivo-b2c-atendimento-story-map.md` (199 itens: 163 Core + 36 INT) e adiciona
> Story Points, modelo de squad, caminho crítico e FTE-horas conforme
> `architecture/governance/ROM-ASSUMPTIONS.md`. Os números são **ROM** (Rough Order of
> Magnitude) — uma faixa de esforço para decisão de investimento, não um plano de sprint.
>
> **Escopo em uma linha:** a **camada de atendimento/serviço** nativa em Salesforce para quatro
> capacidades eTOM Customer — Customer Interaction, Customer Problem, Customer Relationship e
> Customer Order Processing (envelope de atendimento) — **mais a captura de pedido** (Product
> Order Capture): eligibility → serviceability → resource reservation → configuration →
> submission, por família × operação. A **gestão** de product-order (catálogo, CPQ, precificação,
> decomposição, fulfillment, provisionamento) é **delegada** a sistemas externos via MCP e está
> fora de escopo.
>
> **Total ROM:** **1.117–2.156 SP** com ajuste de teste e contingência (base 732–1.421 SP);
> caminho crítico **8–20 sprints** (~3,7–9,2 meses) com um **build de 27 pessoas em 5 squads**;
> QA e o transversal técnico entram como **+15% do esforço de build** (não pela duração do
> caminho crítico), o que mantém as horas monotônicas no esforço.
>
> **Três revisões de escopo reprocessadas nesta ROM (2026-07-23).** Não são um changelog — são
> as **premissas** que passam a valer e que reformam a estimativa. (1) **Regra de Roteamento de
> Integração:** 7 leituras de dado-de-cliente/360 saíram de cliente-Core-por-serviço para
> **federação Data 360** (foundation-por-família em FND), afinando a trilha INT (43→36 clientes).
> (2) **Fluxos determinísticos guiados construídos, não invocados:** os workflows regulados
> pesados (contestação de fatura ≈ 300+ passos, negociação de dívida, despacho técnico) **não são
> exponíveis** pela Vivo como recursos limpos — passam a ser construídos nativamente sobre o
> runtime FND-04, engrossando o CPM. (3) **Order _capture_ é nosso, order _management_ é
> delegado:** a captura agêntica de pedido é capability de Service Cloud + Agentforce — vira o
> novo **Domínio PROCP**; o COPM reduz a envelope puro.
>
> **Calibração do modelo de esforço (2026-07-23).** A velocidade por squad é **nominal** — o custo
> de a Vivo não ter as respostas prontas (definição/elaboração conjunta) é absorvido pela
> contingência (§7), não deduzido da velocidade, mantendo os dois eixos independentes. O caminho
> crítico é de **construção pura** — mede quantos sprints o build consome, sem trava por falta de
> definição ou dependência externa. Com cinco squads em vez de sete, o paralelismo é menor e o
> cronograma é mais longo e realista para uma reconstrução deste porte. O **S2 (Interaction,
> Relationship & Capture)** é o caminho crítico em todos os cenários. QA e transversal, computados
> como fração do esforço de build, tornam as horas **monotônicas no esforço** — mais escopo nunca
> reduz horas.

---

## 1. ROM Assumptions

As premissas de estimativa que esta ROM adota, ordenadas por impacto. Adaptadas de
`ROM-ASSUMPTIONS.md` à realidade Vivo (as premissas do template — greenfield puro, no-add-on,
MuleSoft-como-camada — foram **revistas** onde a realidade Vivo diverge; as revisões estão
marcadas).

| #   | Premissa                                                                                | Detalhe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Percentuais de derivação**                                                            | Aplicados às histórias marcadas Derived no map. Cross-persona **22,5%**, cross-pattern **27,5%**, intra-capacidade (elaboração) **30%** — usa-se o ponto médio da banda. Cada limite derivado é arredondado ao inteiro mais próximo, piso de 1 SP; SP derivado não precisa ser Fibonacci. Cadeias resolvem pela faixa _computada_ do referente imediato.                                                                                                                                                                                                                                                                                                                                                  |
| 2   | **Story Points — faixa Fibonacci**                                                      | Fibonacci (1, 2, 3, 5, 8, 13, 21), faixa min–max por história. **Primary** com SP cheio, ambos os limites Fibonacci; **Derived** ao percentual da premissa 1, não restrito a Fibonacci.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3   | **Cone de incerteza (contingência)**                                                    | Total apresentado como faixa. Buffer de contingência: **35% global**, **50% para INT (integração)**, **50% para CPM (Customer Problem)** e **50% para PROCP (Product Order Capture)** — os três eixos de maior incerteza (ver premissas 8–9 e Riscos #1/#2/#3).                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 4   | **Testes funcionais como Definition of Done**                                           | Cada história de desenvolvimento inclui automação de teste funcional na DoD. Fator de ajuste **+12,5%** aplicado à base de SP dos squads que produzem código — **todos exceto FND, OPS e INT** (FND/OPS são majoritariamente configuração/plataforma; INT carrega sua própria estratégia de teste de contrato).                                                                                                                                                                                                                                                                                                                                                                                           |
| 5   | **Multi-squad, velocidade nominal; caminho crítico de construção pura** ⟳ _(revisada)_  | Cinco squads com composições distintas operam em paralelo desde o Sprint 0; a duração é o **caminho crítico**, não a soma. A velocidade de cada squad segue os patamares nominais por trilha: 30–40 SP/sprint no mainstream, 25–35 no CPM, 25–30 no INT — o custo de definição/elaboração conjunta com a Vivo (que não tem as respostas prontas) é absorvido pela contingência (§7), não deduzido da velocidade. O caminho crítico mede **construção pura**: quantos sprints o build consome, sem embutir trava por falta de definição funcional ou dependência externa. Menos paralelismo (5 squads, não 7) alonga o cronograma para um patamar realista de reconstrução.                                |
| 6   | **Cadência**                                                                            | Sprints de 2 semanas, velocidade diferenciada por squad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 7   | **Horas produtivas**                                                                    | 6h/dia × 10 dias/sprint = 60 FTE-h/pessoa/sprint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 8   | **Port de brownfield para org nova — sem dívida técnica** ⟳ _(revisada)_                | **NÃO é greenfield puro nem construção sobre legado.** É um **port das capacidades de uma operação brownfield para uma org Salesforce nova, sem dívida técnica herdada**. As jornadas de atendimento B2C da Vivo hoje não estão de fato implementadas em Salesforce — os atendentes operam sistemas legados (WDE, GPS, Next, Siebel) via Alt+Tab / iframe mal-integrado. Construímos essas jornadas do zero na org nova. A incerteza **não** vem de dívida técnica na org-alvo; vem do **volume e da fragilidade da malha de integração de origem** (premissa 9) e da **profundidade dos workflows regulados guiados** (Risco #2).                                                                        |
| 9   | **Integração é um dos eixos de maior incerteza** ⟳ _(revisada)_                         | A preocupação de integração **permanece alta**: a telemetria Splunk de produção mostra **~2,3M callouts/dia útil** (pico ~2,9M) e **~22% de respostas não-2xx** — parte é falha sistêmica, parte é resposta de negócio legítima (400/404 esperados em regras de elegibilidade/consulta). Cada cliente reconstruído no Core (Apex/LWC) precisa adicionar o tratamento de erro resiliente que o estado atual não tem. Daí o buffer de 50% no domínio INT. A **Regra de Roteamento** (premissa 17) afinou a trilha — 7 leituras de dado-de-cliente foram federadas para o Data 360 — de 43 para **36 clientes Core**, mas os que restam concentram a orquestração e as escritas transacionais mais difíceis. |
| 10  | **Tech stack**                                                                          | Salesforce Core (LWC + Apex, **OmniStudio descartado**) + Agentforce + Data 360 (federação) + Service Cloud Voice / Amazon Connect + Digital Engagement + MuleSoft (cirúrgico).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 11  | **Add-ons IN na baseline** ⟳ _(revisada)_                                               | Ao contrário do default no-add-on, **Digital Engagement, Data 360 e Agentforce estão dentro da baseline** — são o núcleo da solução-alvo (interface agentic, federação de dados, canais digitais), não candidatos opcionais.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 12  | **Federação de dados via Data 360**                                                     | A Vivo é dona do customer master; premissa = apenas dados mínimos-residentes em Salesforce, o resto federado em tempo de consulta. Sete famílias de dado-de-cliente/360 (Customer Bill, Product Inventory, Party/Profile, Party Interaction, Usage, Agreement/Loyalty, Trouble Ticket) são federadas como **foundation-por-família em FND-09..15** (Regra de Roteamento, premissa 17).                                                                                                                                                                                                                                                                                                                    |
| 13  | **eTOM em escopo**                                                                      | Customer Interaction Management, Customer Problem Management, Customer Relationship Management, Customer Order Processing (**envelope de atendimento**) **+ Product Order _Capture_** (eligibility → serviceability → reservation → configuration → submission, por família × operação).                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 14  | **eTOM fora de escopo**                                                                 | Product Order **Management** (decomposição→orquestração, submit TMF622 downstream), camadas Product/Service/Resource, catálogo/PCM/CPQ, precificação, DRO fulfillment, provisionamento TMF641/639.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 15  | **Ambiguidade**                                                                         | Alta — telco tier-1, processos regulados (Anatel, LGPD, fim de concessão STFC), integrações legadas frágeis, workflows de entrevista de 300+ passos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 16  | **Gestão de projeto não incluída**                                                      | A ROM cobre capacidade de engenharia e arquitetura (build, QA e transversal técnico). PM, Scrum Master, Agile Coach e Delivery Manager **não** estão incluídos e precisam ser dimensionados à parte pelos APs — não é responsabilidade de delivery calculá-los, mas tampouco é do cliente: continua sendo esforço que precisa ser alocado.                                                                                                                                                                                                                                                                                                                                                                |
| 17  | **Regra de Roteamento de Integração** ⟳ _(nova — 2026-07-23)_                           | Cada integração é dispositionada por **natureza do dado/chamada**, não caso a caso: **Transacional** (reserva, agendamento, serviceabilidade, diagnóstico, status volátil, documento) → cliente Core **direto** (CORE); **dado de cliente/visão-360** (fatura, produtos, perfil, interação, uso, contratos, identidade) → **Data 360** (FEDERATE, foundation-por-família em FND); **exposição de API do Core** → **MuleSoft** com zero Integration Procedure (MULE); **escrita/orquestração multi-hop** → facade MuleSoft (MULE). Costura canônica da fatura: **lê federado, escreve transacional** (INT-08).                                                                                             |
| 18  | **Fluxos determinísticos guiados — construídos, não invocados** ⟳ _(nova — 2026-07-23)_ | Os workflows regulados pesados (contestação de fatura ≈ 300+ passos, negociação de dívida, despacho técnico) **não são exponíveis** pela Vivo como recursos limpos — são iterativos, em estilo entrevista. São **construídos nativamente** como motor de entrevista determinística sobre o runtime FND-04, e as jornadas concretas entram no escopo (CPM-04 Primary + derivadas por família CPM-20..25, COPM-05 portabilidade, COPM-06 dívida). O que permanece **delegado** é a _decisão de negócio_ downstream, não a condução do atendimento.                                                                                                                                                          |
| 19  | **Order _capture_ é nosso; order _management_ é delegado** ⟳ _(nova — 2026-07-23)_      | A **captura** de pedido (eligibility, serviceability, resource reservation, configuration, submission) é capability de Service Cloud + Agentforce — **nossa** (Domínio PROCP, decomposto por família × operação). A **gestão** (decomposição, orquestração, fulfillment, provisionamento) é delegada ao Pillar 2 via MCP. Catálogo e precificação são **consumidos** do Pillar 2 como ferramentas MCP, não autorados.                                                                                                                                                                                                                                                                                     |

---

## 2. Functional Scope

### Em escopo — 4 capacidades eTOM Customer + captura de pedido

| Capacidade eTOM Customer                                       | Fronteira                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Customer Interaction Management**                            | `request-to-answer/` — captura de contato, roteamento, consulta, satisfação, classificação de motivo de contato.                                                                                                                                                                                                              |
| **Customer Problem Management**                                | ramos Problem / Technical Complaint / Termination + ciclo de vida de Case (triagem técnica remota, agendamento de visita, **contestação de fatura como fluxo determinístico guiado por família de produto**, fraude, jurídico, migrações mandatórias).                                                                        |
| **Customer Relationship Management**                           | `customer-relationship-management-v360/` — cockpit Customer 360, next-best-action, consentimento LGPD, titularidade, churn/SHAP.                                                                                                                                                                                              |
| **Customer Order Processing (COPM) — envelope de atendimento** | **envelope puro** — identificar asset, submeter o pedido _capturado_ à gestão (MCP) e reconciliar o handoff, acompanhar, notificar/fechar; **mais as jornadas reguladas guiadas** (portabilidade, negociação de dívida, logística reversa). **NÃO** a gestão de product-order.                                                |
| **Product Order Capture (PROCP)** ⟳ _(novo)_                   | a **captura** agêntica de pedido — eligibility → serviceability → resource reservation → configuration → submission — por **família de produto × operação** (activate / change-plan / change-attribute / move / change-ownership / device-upgrade / disconnect). Catálogo, pricing e gestão downstream **invocados via MCP**. |

Domínios habilitadores dimensionados junto: **FND** (fundação/enablement — a fatia de atendimento
do Pillar-3, incluindo as 7 famílias de federação Data 360), **OMNI** (roteamento omnichannel),
**SDP** (Agentforce / service dynamic plan), **OPS** (operation support — palitagem, SLA,
Knowledge), **INT** (clientes Core de integração).

### Fora de escopo (delegado / dependência)

- **Product Order Management** e as camadas Product/Service/Resource — decomposição→plano de
  orquestração, submit TMF622 downstream, fulfillment, provisionamento TMF641/639. Alcançado via
  **MCP** com recursos expostos por produto/família; o PROCP **submete** a esta gestão, não a executa.
- **Autoria de catálogo/PCM, configuração de CPQ, precificação, crédito, setup de billing,
  geração de contrato.** Catálogo e pricing são **consumidos** do Pillar 2 como ferramentas MCP.
- **Jornadas de venda/aquisição** (`r2a-sales-journey-b2c/`, `b2b-selling/`, `catalog/`) —
  domínio de vendas/product-order, adjacente.
- **Plataforma Headless-360 enterprise transversal** (compartilhada com B2X Commerce, Billing,
  ERP) — dependência de programa, não dimensionada; a FND dimensiona apenas a configuração e o
  enablement específicos de atendimento sobre ela.

---

## 3. Product Catalog

Product Design está majoritariamente **fora** deste escopo de atendimento. O portfólio abaixo
(de `../vivob2c/Portfólio de Produtos Vivo B2C.md` + referências dos fluxos) existe para dar
forma aos produtos que as jornadas de atendimento referenciam — **não** é um backlog de autoria
de catálogo. Ele importa duplamente nesta ROM porque o **PROCP decompõe por família × operação** e
o **CPM decompõe a contestação de fatura por família**: cada família de produto é um eixo de
derivação, não só um pano de fundo.

- **Fixo / Fibra:** Vivo Fibra (tiers de banda larga), linha fixa legada, IPTV (Vivo Play / TV).
- **Móvel:** Controle, Easy, Pré-pago, planos pós-pagos; MSISDN/SIM como recursos.
- **Convergente:** Vivo Total (combos fixo + móvel + TV).
- **VAS / add-ons:** streaming (bundles Gemini/Perplexity, OTT), Casa Inteligente.
- **Transversal:** tier/"ilha" do cliente (Gold/Silver/Platinum/Púrpura/Prime/VivoV/VPR/Alto
  Valor/Carteira); serviceabilidade regional; tenure/fidelização de contrato.

Histórias de especificação de produto (autoria de catálogo) são **fronteira delegada** — não
decompostas nem dimensionadas nesta ROM.

---

## 4. Integration Map

Reconciliado dos **74 serviços `WebService__c` reais** na operação Vivo B2C viva (catálogo em
tempo de design), confirmados contra telemetria de callout de produção (Splunk, ~2,7M
callouts/dia útil, ~23% não-2xx, 72% originados de OmniStudio). Cada serviço foi normalizado a
uma família **TM Forum Open API** e recebeu uma **disposition** na solução-alvo, governada pela
**Regra de Roteamento de Integração** (premissa 17). Apenas as três disposições que exigem um
cliente Core são histórias estimáveis (**36**); as outras 38 carregam zero esforço de cliente Core.

| Disposition                          | Contagem | Cliente Core?                                  | Dimensionado onde                                     |
| ------------------------------------ | -------- | ---------------------------------------------- | ----------------------------------------------------- |
| CORE (cliente sync direto)           | 18       | Sim                                            | Domínio INT (histórias estimáveis)                    |
| MULE (cliente fino para facade Mule) | 17       | Sim (só o cliente; serviço Mule = dependência) | Domínio INT                                           |
| EVENT (pub/sub)                      | 1        | Sim                                            | Domínio INT (INT-43)                                  |
| FEDERATE (Data 360 absorve)          | 17       | Não                                            | foundation-por-família FND-09..15 + identidade FND-03 |
| RETIRE (morre com a nova UX/AI)      | 19       | Não                                            | risco de migração                                     |
| DELEGATE (fronteira do Pillar-2)     | 2        | Não                                            | fora de escopo                                        |
| **Total de serviços reais**          | **74**   | **36 precisam de cliente**                     | —                                                     |

**Efeito da Regra de Roteamento (revisão 2026-07-23).** Sete leituras de dado-de-cliente/360 que
a estimativa anterior tratava como clientes Core diretos — INT-05/06/07 (Customer Bill), INT-09
(identidade), INT-10 (histórico de interação), INT-20/21 (contratos/loyalty) — migraram para
**federação Data 360** e agora vivem como **foundation-por-família em FND-09..15** (+ identidade
em FND-03). Suas escritas transacionais correspondentes (INT-08 ajuste de fatura, INT-11 escrita
de interação, INT-22 parcelamento) **permanecem clientes Mule** e foram re-ancoradas como
Primary. O passo é **estrutural**, não uma redução de escopo: o esforço não sumiu, mudou de
domínio (INT→FND) e de natureza (cliente-por-serviço → scaffold-de-federação-por-família).

**Estimativa da trilha de integração (INT):** 36 histórias de cliente Core (17 Primary / 19
Derived, Primary/Derived por família de API TMF). Base **139–217 SP**; com contingência de 50%
(sem ajuste de teste — a trilha de integração carrega sua própria estratégia de teste de
contrato), **208–326 SP**. Continua uma das trilhas de maior massa e maior incerteza; corre em
paralelo sem ser o gargalo (o caminho crítico é o S2), definindo o piso transacional — ver §8 e
Risco #3.

**Postura de design:** MuleSoft **não** é indiscriminadamente mandatório — aplicado
cirurgicamente onde o Core faz orquestração/agregação que não deveria (os 17 MULE), com objetivo
de **zero Integration Procedure**. Chamadas sync single-purpose críticas para a jornada
permanecem **diretas** (os 18 CORE). Dados de referência read-heavy são **federados** via Data
360 (os 17 FEDERATE). O Core permanece passivo: constrói clientes, não orquestração.

O detalhamento por serviço (as 36 histórias INT com família TMF, disposition e história Core
servida) está em §6; a batimetria completa dos 74 serviços está no story map de origem
(`architecture/vivo-b2c-atendimento-story-map.md`, apêndice _Integration Reconciliation_).

---

## 5. Team Composition and Squad Model

O modelo de squad é **orientado a domínio** — cada squad é dono de um ou mais dos domínios que
esta ROM realmente constrói. São **cinco squads de build** operando em paralelo. O paralelismo é
deliberadamente moderado (cinco, não sete): uma reconstrução deste porte não tem gente nem
definições prontas para sustentar frentes altamente paralelas, e concentrar domínios afins num
mesmo squad reflete melhor a realidade de entrega.

| Squad                                      | Domínios                 | Composição                                                     | Velocidade nominal (SP/sprint) | Produz código?                 |
| ------------------------------------------ | ------------------------ | -------------------------------------------------------------- | ------------------------------ | ------------------------------ |
| **S1** Foundation & Operation Support      | FND + OPS                | 5 (1 TA + 4 devs SF/plataforma)                                | 30–40                          | Config/plataforma (sem +12,5%) |
| **S2** Interaction, Relationship & Capture | CIM + CRM + COPM + PROCP | 6 (1 SA + 1 TA + 4 devs SF)                                    | 30–40                          | Sim                            |
| **S3** Problem & Guided Flows              | CPM                      | 5 (1 SA + 1 TA + 3 devs SF)                                    | 25–35                          | Sim                            |
| **S4** Channels & Agentforce               | OMNI + SDP               | 6 (1 TA + 5 devs SCV/Amazon Connect/DE/agentic)                | 30–40                          | Sim                            |
| **S5** Integration / Core Clients          | INT                      | 5 (1 arquiteto de integração + 3 devs SF + 1 liaison MuleSoft) | 25–30                          | Sim                            |

**Headcount de build: 27.** QA e transversal técnico **não** entram como headcount alocado por
calendário — entram como **+15% do esforço de build** (ver §9), de modo que as horas escalam com o
esforço, não com a duração do cronograma.

**Notas do modelo:**

- **Velocidade nominal, incerteza na contingência.** As velocidades (30–40 para os squads de maior
  maturidade, 25–35/25–30 para as trilhas de maior incerteza) são os patamares nominais por trilha.
  O custo de a Vivo não ter todas as respostas prontas — workshops, reconciliação de regras
  regulatórias, alinhamento de contrato de integração — é absorvido pela **contingência** (35%
  global; 50% em CPM, PROCP e INT, §7), o eixo do cone de incerteza de escopo, **não** deduzido da
  velocidade. Manter velocidade e incerteza em eixos separados evita descontar o mesmo risco duas
  vezes.
- **S1** combina FND (fundação — incluindo as 7 famílias de federação Data 360) e OPS (operation
  support) porque ambos são majoritariamente configuração de plataforma/governança — daí a
  exclusão do ajuste de teste de +12,5%.
- **S2** é o squad de maior massa: concentra interação, relacionamento/V360, o envelope de
  atendimento (COPM) e a captura de pedido (PROCP). É o **caminho crítico em todos os cenários** —
  quatro frentes de atendimento num só squad. Reequilibrar domínios para fora do S2 é a principal
  alavanca de aceleração de cronograma (ver §8).
- **S3** é dedicado ao Problem Management: os fluxos determinísticos guiados (motor de entrevista +
  contestação por família + agendamento guiado + migrações) tornaram o CPM pesado. Velocidade
  25–35, com a novidade do runtime de entrevista determinística de 300+ passos absorvida pelo
  buffer de contingência de 50%.
- **S4** reúne os canais (OMNI — SCV/Amazon Connect/Digital Engagement) e a camada agentic (SDP —
  Agentforce Actions/MCP), ambos de stack nova, num squad de canal-e-experiência.
- **S5** (INT) tem a menor velocidade (25–30) por ser uma trilha de alta incerteza: reconstrução
  de clientes contra a malha de integração de origem, com tratamento de erro resiliente ausente
  hoje. Corre em paralelo sem ser o gargalo, mas define o piso transacional.

---

## 6. Story Map by Epic (com Story Points)

SP em faixa min–max. Primary em Fibonacci cheio; Derived ao percentual de derivação da faixa
computada do referente. Os subtotais aqui são **base** (antes de ajuste de teste e
contingência — esses entram em §7).

### S1 · Domínio FND — Foundation / Enablement

A FND cresceu de 8 para 15 histórias: as 7 famílias de federação Data 360 (FND-09..15) que a
Regra de Roteamento moveu de cliente-Core-por-serviço para foundation-por-família. Cada uma é o
scaffold de query federada + mapeamento de DTO + freshness + masking na AI Trust Layer daquela
família — derivada do modelo Data-360 de atendimento (FND-02).

| Story ID | P/D              |    Min |     Max | Nota                                                                                        |
| -------- | ---------------- | -----: | ------: | ------------------------------------------------------------------------------------------- |
| FND-01   | Primary          |     13 |      21 | AI Trust Layer para agentes de atendimento (grounding, masking, toxidade, auditoria)        |
| FND-02   | Primary          |      8 |      21 | Modelo Data-360 de atendimento + federação de dados mínimos-residentes                      |
| FND-03   | Derived (FND-02) |      2 |       6 | Resolução de identidade federada SF+master+legado                                           |
| FND-04   | Primary          |      8 |      21 | Runtime de orquestração determinística (o "IT determinístico"; base dos fluxos guiados CPM) |
| FND-05   | Primary          |      5 |      13 | Modelo de segurança & sharing Passive-Core                                                  |
| FND-06   | Primary          |      8 |      21 | Standup Service Cloud Voice + Amazon Connect                                                |
| FND-07   | Derived (FND-06) |      2 |       6 | Standup canais Digital Engagement                                                           |
| FND-08   | Primary          |      5 |      13 | Ambiente, pipeline DevOps, observabilidade                                                  |
| FND-09   | Derived (FND-02) |      2 |       6 | Federar família Customer Bill (fatura, itens, créditos) — TMF678                            |
| FND-10   | Derived (FND-02) |      2 |       6 | Federar família Product Inventory (produtos/ofertas/ativos) — TMF637                        |
| FND-11   | Derived (FND-02) |      2 |       6 | Federar família Party / Profile (perfil, cadastro read-only) — TMF632                       |
| FND-12   | Derived (FND-02) |      2 |       6 | Federar família Party Interaction (histórico/protocolo) — TMF683                            |
| FND-13   | Derived (FND-02) |      2 |       6 | Federar família Usage / Consumo — TMF635                                                    |
| FND-14   | Derived (FND-02) |      2 |       6 | Federar família Agreement / Contract / Loyalty — TMF651/658                                 |
| FND-15   | Derived (FND-02) |      2 |       6 | Federar família Trouble Ticket history — TMF621                                             |
| **FND**  | 6P/9D            | **65** | **164** |                                                                                             |

### S1 · Domínio OPS — Operation Support

| Story ID | P/D              |    Min |     Max | Nota                                                                              |
| -------- | ---------------- | -----: | ------: | --------------------------------------------------------------------------------- |
| OPS-01   | Primary          |      5 |      13 | Árvore de classificação (palitagem) como metadados hierárquicos + mapeamento eTOM |
| OPS-02   | Derived (OPS-01) |      2 |       4 | Publicar/versionar mudança (effective-dated)                                      |
| OPS-03   | Derived (OPS-01) |      2 |       4 | Mapear disposição → RecordType/Origin/Queue                                       |
| OPS-04   | Derived (OPS-01) |      2 |       4 | Níveis obrigatórios vs opcionais por canal                                        |
| OPS-05   | Derived (OPS-01) |      2 |       4 | Import/export em massa com validação                                              |
| OPS-06   | Derived (OPS-01) |      2 |       4 | Aposentar/depreciar nós preservando histórico                                     |
| OPS-07   | Primary          |      5 |      13 | Captura de disposição obrigatória no wrap-up                                      |
| OPS-08   | Derived (OPS-07) |      2 |       4 | Seletor guiado/progressivo (árvore em cascata)                                    |
| OPS-09   | Derived (OPS-07) |      2 |       4 | Disposições secundárias/multi-issue                                               |
| OPS-10   | Derived (OPS-07) |      2 |       4 | Ações pós-caso dirigidas por disposição                                           |
| OPS-11   | Primary          |      5 |      13 | Entitlement Process + Milestones (SLA) por tier                                   |
| OPS-12   | Derived (OPS-11) |      2 |       4 | Calendário de horário comercial/feriado                                           |
| OPS-13   | Derived (OPS-11) |      2 |       4 | Notificação de breach/warning de SLA                                              |
| OPS-14   | Derived (OPS-11) |      2 |       4 | Pause/resume de SLA por status                                                    |
| OPS-15   | Primary          |      5 |      13 | Workflow de autoria de Knowledge                                                  |
| OPS-16   | Derived (OPS-15) |      2 |       4 | Taxonomia de Data Category                                                        |
| OPS-17   | Derived (OPS-15) |      2 |       4 | Analytics de uso/gap de artigos                                                   |
| OPS-18   | Derived (OPS-15) |      2 |       4 | Governança de expiração/revisão                                                   |
| OPS-19   | Primary          |      3 |       8 | Biblioteca de templates de mensagem (WhatsApp aprovados)                          |
| OPS-20   | Primary          |      5 |      13 | Dashboards operacionais (AHT/ASA/abandono)                                        |
| OPS-21   | Derived (OPS-20) |      2 |       4 | Relatório de compliance de SLA                                                    |
| OPS-22   | Derived (OPS-20) |      2 |       4 | Dashboard de performance/qualidade do agente                                      |
| **OPS**  | 6P/16D           | **60** | **137** |                                                                                   |

> **S1 base: 125–301 SP.** (FND 65–164 + OPS 60–137.)

### S2 · Domínio CIM — Customer Interaction Management

| Story ID | P/D                            |    Min |     Max | Nota                                                                     |
| -------- | ------------------------------ | -----: | ------: | ------------------------------------------------------------------------ |
| CIM-01   | Primary                        |      5 |      13 | Capturar & registrar interação (EngagementInteraction) em qualquer canal |
| CIM-02   | Derived cross-persona (CIM-01) |      1 |       3 | Interação de canal digital/social                                        |
| CIM-03   | Derived (CIM-01)               |      2 |       4 | Normalizar/formatar dados capturados                                     |
| CIM-04   | Primary                        |      5 |       8 | Buscar & unificar identidade (Data 360/legado)                           |
| CIM-05   | Primary                        |      8 |      21 | Verificar identidade/KYC com badge de autorização                        |
| CIM-06   | Derived (CIM-01)               |      2 |       4 | Elegibilidade de self-service + redirecionar                             |
| CIM-07   | Primary                        |      5 |      13 | Identificar tipo de requisição e rotear                                  |
| CIM-08   | Derived (CIM-01)               |      2 |       4 | Interação de prospect/anônimo                                            |
| CIM-09   | Primary                        |      8 |      21 | Gerenciar consulta geral (caso, Knowledge, resposta)                     |
| CIM-10   | Derived (CIM-09)               |      2 |       6 | Rotear caso para fila de especialista                                    |
| CIM-11   | Derived (CIM-09)               |      2 |       6 | Capturar motivo/gap de insatisfação                                      |
| CIM-12   | Primary                        |      3 |       5 | Disparar pesquisa de satisfação                                          |
| CIM-13   | Derived (CIM-12)               |      1 |       2 | Registrar não-resposta no prazo                                          |
| CIM-14   | Primary                        |      2 |       3 | Segunda via de fatura por email/WhatsApp                                 |
| CIM-15   | Derived (CIM-09)               |      2 |       6 | Consulta de saldo/recarga com handoff                                    |
| CIM-16   | Derived (CIM-15)               |      1 |       2 | Consulta de consumo/uso                                                  |
| CIM-17   | Primary                        |      5 |      13 | Atualização de dados cadastrais                                          |
| CIM-18   | Derived (CIM-07)               |      2 |       4 | Classificar motivo de contato de entrada                                 |
| CIM-19   | Derived (CIM-18)               |      1 |       1 | Fase conversacional para analytics TMA/FCR                               |
| **CIM**  | 8P/11D                         | **59** | **139** |                                                                          |

### S3 · Domínio CPM — Customer Problem Management

O CPM engrossou de 19 para 25 histórias com os **fluxos determinísticos guiados** (premissa 18).
A mudança de fundo: **CPM-04 foi reclassificada de Derived para Primary** — deixou de ser um
"envelope de contestação" derivado da consulta de fatura e passou a ser o **motor de entrevista
determinística** (contestação Móvel pós/Controle, grava ajuste transacional via INT-08), o
scaffold reusado por todas as demais famílias. As derivadas por família (CPM-20..24) e o
agendamento guiado (CPM-25) reusam esse motor. As migrações mandatórias (CPM-18/19) também são
entrevistas guiadas.

| Story ID | P/D                            |     Min |     Max | Nota                                                                                                                                                                                          |
| -------- | ------------------------------ | ------: | ------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPM-01   | Primary                        |      13 |      21 | Abrir e classificar caso de problema (ciclo de vida de Case — fundação de todo o problem handling)                                                                                            |
| CPM-02   | Derived (CPM-01)               |       4 |       6 | Caso de reclamação técnica                                                                                                                                                                    |
| CPM-03   | Primary                        |       5 |      13 | Consultar & apresentar fatura (externo/federado)                                                                                                                                              |
| CPM-04   | **Primary** ‡                  |      13 |      21 | **Motor de entrevista determinística** — contestação de fatura guiada nativa (Móvel pós/Controle), grava ajuste transacional (INT-08), acompanha (C2S). Ancora o motor reusado por CPM-18..25 |
| CPM-05   | Primary                        |       8 |      13 | Triagem técnica remota antes de despacho (P2S)                                                                                                                                                |
| CPM-06   | Derived (CPM-05)               |       2 |       4 | Network refresh / ação técnica remota                                                                                                                                                         |
| CPM-07   | Primary                        |       5 |       8 | Agendar visita técnica                                                                                                                                                                        |
| CPM-08   | Derived (CIM-12)               |       1 |       1 | Notificar mudança/cancelamento de visita                                                                                                                                                      |
| CPM-09   | Derived cross-persona (CIM-10) |       1 |       1 | Escalar para Ouvidoria/Anatel                                                                                                                                                                 |
| CPM-10   | Derived (CPM-09)               |       1 |       1 | Sincronizar status de reconsideração Anatel                                                                                                                                                   |
| CPM-11   | Primary                        |       8 |      13 | Capturar requisição de rescisão/cancelamento                                                                                                                                                  |
| CPM-12   | Derived cross-persona (CPM-11) |       2 |       3 | Contexto de churn + contraproposta                                                                                                                                                            |
| CPM-13   | Primary                        |       8 |      21 | Tratativa de fraude — bloqueio/desprogramação                                                                                                                                                 |
| CPM-14   | Derived (CPM-13)               |       2 |       6 | Escalação & investigação de fraude                                                                                                                                                            |
| CPM-15   | Primary                        |       8 |      21 | Tratativa jurídica/serviços especiais (legal-hold)                                                                                                                                            |
| CPM-16   | Derived (CPM-01)               |       4 |       6 | Contato multi-issue                                                                                                                                                                           |
| CPM-17   | Derived (CPM-12)               |       1 |       1 | Retenção proativa pré-gatilho                                                                                                                                                                 |
| CPM-18   | Derived cross-pattern (CPM-01) |       4 |       6 | Migração mandatória cobre→fibra (fim STFC) — entrevista guiada (reusa motor CPM-04)                                                                                                           |
| CPM-19   | Derived (CPM-18)               |       1 |       2 | Descomissionamento DTH→IPTV (agendamento + logística reversa)                                                                                                                                 |
| CPM-20   | Derived (CPM-04)               |       4 |       6 | Contestação de fatura **Fibra / banda larga fixa** via motor de entrevista guiado                                                                                                             |
| CPM-21   | Derived (CPM-04)               |       4 |       6 | Contestação de fatura **TV (IPTV/Vivo Play/DTH)** via motor de entrevista guiado                                                                                                              |
| CPM-22   | Derived (CPM-04)               |       4 |       6 | Contestação de fatura **Convergente (Vivo Total)** — atribuir item à perna correta                                                                                                            |
| CPM-23   | Derived (CPM-04)               |       4 |       6 | Contestação de fatura **VAS / add-ons** (streaming, Casa Inteligente)                                                                                                                         |
| CPM-24   | Derived (CPM-04)               |       4 |       6 | Disputa de crédito/recarga **Pré-pago** (sem fatura mensal)                                                                                                                                   |
| CPM-25   | Derived (CPM-04)               |       4 |       7 | **Agendamento & despacho técnico guiado** (janelas, elegibilidade de slot, reagendamento) — serve CPM-05/07                                                                                   |
| **CPM**  | 8P/17D                         | **115** | **205** |                                                                                                                                                                                               |

> **S3 base: 115–205 SP.** Carrega o buffer de contingência de 50% (ver §7 e Riscos #1/#2).
>
> ‡ **CPM-04 reclassificada Primary** (era Derived cross-persona from CPM-03). Decisão do
> Arquiteto refletindo a premissa 18: o motor de entrevista determinística de 300+ passos que
> grava ajuste transacional e é reusado por 6 famílias é o item mais estrutural do domínio de
> problema — não uma derivação da consulta de fatura. As 5 contestações por família (CPM-20..24)
> e o agendamento guiado (CPM-25) derivam **dele**.

### S2 · Domínio PROCP — Product Order Capture

Domínio **novo** (2026-07-23, premissa 19). Decompõe a **captura** de pedido (eligibility →
serviceability → resource reservation → configuration → submission) por **família × operação**.
PROCP-01 é o motor de captura agêntico (ancorado em ativação Móvel), reusado por todas as famílias;
PROCP-07 ancora o padrão de _change_ e PROCP-17 o de _disconnect_. Absorve as ex-histórias de captura
do COPM (ex-COPM-03/04/05). Matriz honesta — nem toda operação se aplica a toda família.

| Story ID  | P/D                |    Min |     Max | Nota                                                                                                                                    |
| --------- | ------------------ | -----: | ------: | --------------------------------------------------------------------------------------------------------------------------------------- |
| PROCP-01  | Primary            |     13 |      21 | **Motor de captura agêntico** — eligibility→serviceability→reservation→config→submission (MCP), ancorado em ativação Móvel pós/Controle |
| PROCP-02  | Derived (PROCP-01) |      4 |       6 | Ativar **Fibra** — serviceabilidade + reserva de CPE + slot de instalação                                                               |
| PROCP-03  | Derived (PROCP-01) |      4 |       6 | Ativar **TV (IPTV/Vivo Play)** — reserva de decoder + pacote                                                                            |
| PROCP-04  | Derived (PROCP-01) |      4 |       6 | Ativar **Convergente (Vivo Total)** — elegibilidade cross-família + bundle                                                              |
| PROCP-05  | Derived (PROCP-01) |      2 |       4 | Ativar **Pré-pago** — reserva de SIM/MSISDN (leve, sem crédito)                                                                         |
| PROCP-06  | Derived (PROCP-01) |      3 |       5 | **Adicionar VAS novo** (streaming, Casa Inteligente) via catálogo MCP                                                                   |
| PROCP-07  | Primary            |      8 |      13 | Capturar **mudança de plano** (up/downgrade) Móvel — ancora o padrão de change _(absorve ex-COPM-04)_                                   |
| PROCP-08  | Derived (PROCP-07) |      2 |       4 | Mudança de plano — **Fibra**                                                                                                            |
| PROCP-09  | Derived (PROCP-07) |      3 |       5 | Mudança de plano — **Convergente** (recomposição de bundle)                                                                             |
| PROCP-10  | Derived (PROCP-07) |      2 |       4 | **Atributo** — velocidade da Fibra (re-serviceabilidade)                                                                                |
| PROCP-11  | Derived (PROCP-07) |      2 |       4 | **Atributo** — franquia/perfil de dados Móvel (bolt-on)                                                                                 |
| PROCP-12  | Derived (PROCP-06) |      1 |       2 | **Add/Remove VAS** em assinatura existente _(absorve ex-COPM-03)_                                                                       |
| PROCP-13  | Derived (PROCP-07) |      2 |       4 | **Mudança de MSISDN** — disponibilidade + reserva de número _(absorve ex-COPM-05)_                                                      |
| PROCP-14  | Derived (PROCP-07) |      3 |       5 | **Move** — mudança de endereço (re-serviceabilidade + re-agendamento) Fibra/Convergente                                                 |
| PROCP-15  | Derived (PROCP-07) |      2 |       4 | **Change ownership** — troca de titularidade do asset (coordena CRM-11)                                                                 |
| PROCP-16  | Derived (PROCP-07) |      3 |       7 | **Upgrade/troca de aparelho** com financiamento — elegibilidade + estoque + parcelamento                                                |
| PROCP-17  | Primary            |      5 |       8 | Capturar **desconexão** de serviço único — penalidade/tenure, gatilho de logística reversa, cease. Ancora o padrão de disconnect        |
| PROCP-18  | Derived (PROCP-17) |      2 |       2 | **Desconexão parcial** de bundle convergente (dropar 1 perna)                                                                           |
| PROCP-19  | Derived (PROCP-17) |      1 |       2 | **Desconexão de VAS / add-on** (auto-renovação de terceiro)                                                                             |
| **PROCP** | 3P/16D             | **66** | **112** |                                                                                                                                         |

> **S4 base (com COPM): 91–153 SP.** Carrega o buffer de contingência de 50% no eixo PROCP
> (captura agêntica nova + dependência do contrato de handoff Pillar 2, Risco #7).

### S2 · Domínio COPM — Order Processing (envelope de atendimento)

Reduzido de 10 para 7 histórias: as 3 histórias de captura (ex-COPM-03/04/05) migraram para o
PROCP. O COPM fica como **envelope puro** — identificar asset, submeter à gestão e reconciliar o
handoff, acompanhar, notificar/fechar — mais as jornadas reguladas guiadas (portabilidade e
dívida reusam o motor de entrevista CPM-04; logística reversa).

| Story ID | P/D                              |    Min |    Max | Nota                                                                                           |
| -------- | -------------------------------- | -----: | -----: | ---------------------------------------------------------------------------------------------- |
| COPM-01  | Primary                          |      3 |      5 | Identificar asset/subscription ativo para iniciar requisição                                   |
| COPM-02  | Primary                          |      8 |     13 | Submeter pedido **capturado** (PROCP) à gestão via MCP + reconciliar handoff                   |
| COPM-03  | Derived cross-pattern (CRM-06) † |      2 |      2 | Acompanhar status do pedido + atualizar cliente                                                |
| COPM-04  | Derived (CPM-08)                 |      1 |      1 | Notificar conclusão + fechar requisição                                                        |
| COPM-05  | Primary                          |      8 |     13 | Portabilidade numérica como fluxo guiado nativo (motor CPM-04) + handoff ao clearinghouse      |
| COPM-06  | Derived (COPM-02)                |      2 |      4 | Negociação de dívida guiada (motor CPM-04) — simulação de parcelas, grava acordo (INT-22)      |
| COPM-07  | Derived (COPM-03)                |      1 |      3 | Envelope de logística reversa de comodato na rescisão — captura devolução, pro-rata, acompanha |
| **COPM** | 3P/4D                            | **25** | **41** |                                                                                                |

> **S2 parcial (PROCP + COPM): 91–153 SP.** (PROCP 66–112 + COPM 25–41.) O S2 completo — CIM,
> CRM, COPM e PROCP — é consolidado ao final do domínio CRM abaixo.
>
> † **COPM-03** recebeu piso de 2 SP: a derivação em cadeia a colapsaria para 1–1, mas é
> substância genuína (polling de status + atualização de UI), nunca 1 SP.

### S2 · Domínio CRM — Customer Relationship / V360

| Story ID | P/D                            |    Min |    Max | Nota                                              |
| -------- | ------------------------------ | -----: | -----: | ------------------------------------------------- |
| CRM-01   | Primary                        |      8 |     13 | Cockpit Customer 360 unificado (LWC), sem Alt+Tab |
| CRM-02   | Derived (CRM-01)               |      2 |      4 | Painel de perfil/segmento/NPS/valor               |
| CRM-03   | Derived (CRM-01)               |      2 |      4 | Painel de endereços/contatos/billing              |
| CRM-04   | Derived (CRM-01)               |      2 |      4 | Painel de status financeiro/billing               |
| CRM-05   | Derived (CRM-01)               |      2 |      4 | Painel de product-inventory/assets                |
| CRM-06   | Derived (CRM-01)               |      2 |      4 | Acompanhamento de pedidos abertos/pendentes       |
| CRM-07   | Derived (CRM-01)               |      2 |      4 | Timeline de histórico de interações               |
| CRM-08   | Primary                        |      5 |      8 | Next-best-action contextual a partir do 360       |
| CRM-09   | Primary                        |      3 |      5 | Service Contract / tier de entitlement na Account |
| CRM-10   | Primary                        |      5 |      8 | Consentimento LGPD + data-subject-request         |
| CRM-11   | Primary                        |      5 |      8 | Troca de titularidade com validação de documento  |
| CRM-12   | Derived cross-pattern (CIM-05) |      1 |      4 | SIM swap / desbloqueio com re-verificação         |
| CRM-13   | Derived cross-pattern (CRM-08) |      1 |      2 | Sinal de churn explicável (SHAP) no 360           |
| **CRM**  | 5P/8D                          | **40** | **72** |                                                   |

> **S2 base (completo): 190–364 SP.** (CIM 59–139 + CRM 40–72 + COPM 25–41 + PROCP 66–112.) É o
> squad de maior massa e o caminho crítico em todos os cenários.

### S4 · Domínio OMNI — Omnichannel Routing

| Story ID | P/D               |    Min |     Max | Nota                                                                |
| -------- | ----------------- | -----: | ------: | ------------------------------------------------------------------- |
| OMNI-01  | Primary           |      5 |      13 | Roteamento Omni-Channel (prioridade, capacidade) por canal          |
| OMNI-02  | Derived (OMNI-01) |      2 |       4 | Roteamento por skills                                               |
| OMNI-03  | Derived (OMNI-01) |      2 |       4 | Filas mapeadas a filas Amazon Connect                               |
| OMNI-04  | Derived (OMNI-01) |      2 |       4 | Status de presença mapeados ao Amazon Connect                       |
| OMNI-05  | Derived (OMNI-01) |      2 |       4 | Unified Routing — voz na mesma engine Omni                          |
| OMNI-06  | Primary           |      8 |      21 | Omni flow de voz de entrada (identificar, rotear, Case, screen-pop) |
| OMNI-07  | Primary           |      8 |      21 | Softphone de voz/CTI (click-to-dial, controles)                     |
| OMNI-08  | Derived (OMNI-07) |      2 |       6 | Transferência quente/fria com contexto                              |
| OMNI-09  | Derived (OMNI-08) |      1 |       2 | Transferência aprimorada (capacidade do alvo)                       |
| OMNI-10  | Primary           |      8 |      21 | Transcrição de chamada ao vivo (Amazon Connect)                     |
| OMNI-11  | Derived (OMNI-10) |      2 |       6 | Persistir transcrição pós-chamada                                   |
| OMNI-12  | Primary           |      5 |      13 | Deflexão IVR/URA com fallback                                       |
| OMNI-13  | Derived (OMNI-12) |      2 |       4 | Passagem de contexto IVR→Salesforce                                 |
| OMNI-14  | Derived (OMNI-06) |      2 |       6 | Fallback de resiliência de voz                                      |
| OMNI-15  | Derived (OMNI-06) |      2 |       6 | Callback enfileirado                                                |
| OMNI-16  | Derived (OMNI-11) |      1 |       2 | Roteamento/playback de voicemail                                    |
| OMNI-17  | Primary           |      5 |      13 | Roteamento Digital Engagement (WhatsApp/chat/email)                 |
| OMNI-18  | Derived (OMNI-17) |      2 |       4 | Ciclo de vida de sessão async                                       |
| OMNI-19  | Derived (OMNI-17) |      2 |       4 | Múltiplas sessões concorrentes por agente                           |
| OMNI-20  | Derived (OMNI-06) |      2 |       6 | Channel-to-Case com dedupe                                          |
| OMNI-21  | Derived (OMNI-17) |      2 |       4 | Tratamento de anexos WhatsApp/chat                                  |
| OMNI-22  | Derived (OMNI-17) |      2 |       4 | Tempo de espera estimado bot→humano                                 |
| OMNI-23  | Primary           |      5 |      13 | Barge-in/listen/whisper de supervisor                               |
| OMNI-24  | Derived (OMNI-23) |      2 |       4 | Omni Supervisor — backlog/status em tempo real                      |
| OMNI-25  | Derived (OMNI-24) |      1 |       1 | Reatribuição em massa sincronizada ao Amazon Connect                |
| OMNI-26  | Derived (OMNI-01) |      2 |       4 | After Conversation Work Time                                        |
| OMNI-27  | Primary           |      5 |      13 | Outbound proativo / agendamento de callback                         |
| OMNI-28  | Primary           |     13 |      21 | Superfície de atendimento Parceiro/Aliado (Experience Cloud, ~18k)  |
| **OMNI** | 9P/19D            | **97** | **228** |                                                                     |

> **S4 parcial (OMNI): 97–228 SP.** O S4 completo — OMNI + SDP — é consolidado ao final do
> domínio SDP abaixo.

### S4 · Domínio SDP — Agentforce / Service Dynamic Plan

| Story ID | P/D                            |    Min |     Max | Nota                                                              |
| -------- | ------------------------------ | -----: | ------: | ----------------------------------------------------------------- |
| SDP-01   | Primary                        |     13 |      21 | Catálogo de ações invocáveis (Agentforce Actions/MCP)             |
| SDP-02   | Derived (SDP-01)               |      4 |       6 | Montar service dynamic plan da intenção                           |
| SDP-03   | Primary                        |     13 |      21 | Superfície agentic/conversacional (LWC + Agentforce)              |
| SDP-04   | Derived (SDP-01)               |      4 |       6 | Consumir transcrição SCV/Amazon Connect                           |
| SDP-05   | Derived (SDP-02)               |      1 |       2 | Copiloto de IA ativo (sugere e executa)                           |
| SDP-06   | Derived cross-pattern (CRM-08) |      1 |       2 | NBA contextual                                                    |
| SDP-07   | Derived (SDP-05)               |      1 |       1 | Sumarização de caso na abertura                                   |
| SDP-08   | Derived (SDP-05)               |      1 |       1 | Recomendações de resposta editáveis                               |
| SDP-09   | Derived (SDP-07)               |      1 |       1 | Sumarização de caso no fechamento                                 |
| SDP-10   | Derived cross-pattern (OPS-07) |      1 |       4 | Sugestão de disposição assistida (palitagem)                      |
| SDP-11   | Derived (SDP-01)               |      4 |       6 | Recomendação de artigo de Knowledge                               |
| SDP-12   | Derived (SDP-05)               |      1 |       1 | Nudge de coaching por sentimento em tempo real                    |
| SDP-13   | **Primary** ‡                  |      8 |      13 | Active Retention Agent — resolução autônoma de atrito de cobrança |
| SDP-14   | **Primary** ‡                  |      8 |      13 | Active Retention Agent — detecção proativa de intenção de compra  |
| SDP-15   | **Primary** ‡                  |      5 |       8 | Active Retention Agent — handoff inteligente para vendas humano   |
| **SDP**  | 5P/10D                         | **66** | **106** |                                                                   |

> **S4 base (completo): 163–334 SP.** (OMNI 97–228 + SDP 66–106; consolidação com
> teste+contingência em §7.)
>
> ‡ **SDP-13/14/15 reclassificadas Primary** (eram Derived). Decisão do Arquiteto (override
> explícito de assumption): o Active Retention Agent é o item mais estratégico e menos provado
> do escopo — decisão autônoma + execução vinculada a política é materialmente mais difícil que
> uma feature de sugestão. Sob a matemática de derivação em cadeia colapsariam para 1–2 SP cada,
> subestimando o risco. Registrado como override, não desvio silencioso da regra Fibonacci.

### S5 · Domínio INT — Integration / Core Clients

Primary/Derived por **família de API TMF**: o primeiro cliente de uma família estabelece o
scaffold (auth, tratamento de erro, mapeamento de DTO, retry) = Primary; operações adicionais na
mesma família o reutilizam = Derived (30%). Clientes CORE carregam mais peso que MULE (a facade
Mule absorve a coreografia). **36 clientes** após a Regra de Roteamento (7 leituras federadas
saíram para FND-09..15 + FND-03; ver §4). IDs preservam a numeração original — lacunas são
intencionais (serviços federados/aposentados), não passos faltando.

| Story ID | Cliente                            | Família TMF                 | Disp  | P/D     |     Min |     Max |
| -------- | ---------------------------------- | --------------------------- | ----- | ------- | ------: | ------: |
| INT-01   | GeographicAddressCallout           | TMF673                      | CORE  | Primary |       5 |       8 |
| INT-02   | GeographicAddressValidationCallout | TMF673                      | CORE  | Derived |       2 |       2 |
| INT-03   | SreAddress                         | TMF673                      | CORE  | Derived |       2 |       2 |
| INT-04   | ServiceCoverageAvailabilityCallout | TMF645                      | CORE  | Primary |       8 |      13 |
| INT-08   | CalculatePlanProrationCallout      | TMF678 (bill adj.)          | MULE  | Primary |       5 |       8 |
| INT-11   | CIMServiceCallout (mTLS)           | TMF683                      | MULE  | Primary |       5 |       8 |
| INT-12   | DocumentRepository (mTLS)          | TMF667                      | CORE  | Primary |       8 |      13 |
| INT-13   | BiometryHistoryCallout             | TMF720                      | CORE  | Primary |       8 |      13 |
| INT-14   | WorkForceManagementCallout         | TMF697                      | CORE  | Primary |       8 |      13 |
| INT-15   | WfmGetWorkOrderById (mTLS)         | TMF697                      | CORE  | Derived |       2 |       4 |
| INT-16   | WFMSearchByWorkOrderCallout        | TMF697                      | CORE  | Derived |       2 |       4 |
| INT-17   | RetrieveOrderDetailsCallout        | TMF622 (status volátil)     | CORE  | Primary |       8 |      13 |
| INT-18   | RetrieveOrdersListCallout          | TMF622                      | CORE  | Derived |       2 |       4 |
| INT-19   | RtdNbaNboServiceCallout            | TMF680                      | CORE  | Primary |       8 |      13 |
| INT-22   | PaymentAgreementCallout            | TMF651                      | MULE  | Primary |       5 |       8 |
| INT-23   | CommunicationSendEmail             | TMF681                      | MULE  | Primary |       3 |       5 |
| INT-24   | API_GW_SendMailCSS                 | TMF681                      | MULE  | Derived |       1 |       2 |
| INT-25   | GPSQueryServiceFlowsCallout        | GPS diag.                   | CORE  | Primary |       8 |      13 |
| INT-26   | ServiceFlowDiagnosticCallout       | GPS diag.                   | CORE  | Derived |       2 |       4 |
| INT-27   | ServiceFlowFormCallout             | GPS diag.                   | CORE  | Derived |       2 |       4 |
| INT-28   | ServiceFlowProtocolCallout         | GPS diag.                   | CORE  | Derived |       2 |       4 |
| INT-29   | ServiceFlowGPSCreateSSCallout      | GPS (create)                | MULE  | Derived |       2 |       4 |
| INT-30   | MassiveFixedCallout                | TMF656                      | CORE  | Primary |       5 |       8 |
| INT-31   | MassiveSuspicionCallout            | TMF656                      | CORE  | Derived |       2 |       2 |
| INT-32   | CustomerProblemManagement          | TMF656                      | MULE  | Derived |       2 |       2 |
| INT-33   | PointOfServiceCallout              | POS/Queue                   | MULE  | Primary |       5 |       8 |
| INT-34   | PointOfServiceAttendanceCallout    | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-35   | PointOfServiceAttendantCallout     | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-36   | PointOfServiceTicketsCallout       | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-37   | OperationalInformationsCallout     | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-38   | QueueInformationAttendanceCallout  | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-39   | QueueInformationStatusCallout      | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-40   | UpdateWorkPositionCallout          | POS/Queue                   | MULE  | Derived |       2 |       2 |
| INT-41   | CamundaTicketInformation (eSIM GW) | orquestração det.           | MULE  | Primary |       5 |       8 |
| INT-42   | ServiceAuthorizationPID            | Service Auth                | MULE  | Primary |       5 |       8 |
| INT-43   | KafkaEvents                        | pub/sub                     | EVENT | Primary |       3 |       5 |
| **INT**  |                                    | 18 CORE + 17 MULE + 1 EVENT |       | 17P/19D | **139** | **217** |

> **S5 base: 139–217 SP.** Carrega o buffer de contingência de 50% (ver §7 e Risco #3). As três
> escritas transacionais re-ancoradas como Primary (INT-08 ajuste de fatura, INT-11 escrita de
> interação, INT-22 parcelamento) refletem a costura "lê federado, escreve transacional" da Regra
> de Roteamento.

### Consolidação base por domínio (§6)

| Domínio   | Histórias | Primary | Derived |  SP min |    SP max |
| --------- | --------: | ------: | ------: | ------: | --------: |
| FND       |        15 |       6 |       9 |      65 |       164 |
| OPS       |        22 |       6 |      16 |      60 |       137 |
| CIM       |        19 |       8 |      11 |      59 |       139 |
| CPM       |        25 |       8 |      17 |     115 |       205 |
| CRM       |        13 |       5 |       8 |      40 |        72 |
| COPM      |         7 |       3 |       4 |      25 |        41 |
| PROCP     |        19 |       3 |      16 |      66 |       112 |
| OMNI      |        28 |       9 |      19 |      97 |       228 |
| SDP       |        15 |       5 |      10 |      66 |       106 |
| INT       |        36 |      17 |      19 |     139 |       217 |
| **Total** |   **199** |  **70** | **129** | **732** | **1.421** |

> **Nota sobre contagens Primary/Derived.** O story map de origem registra 67P/132D. Esta ROM
> reclassificou **3 histórias como Primary** por decisão do Arquiteto (SDP-13/14/15 — o Active
> Retention Agent), levando a **70P/129D**. (CPM-04 já é Primary no map; a promoção descrita em §6
> foi feita no próprio map na revisão de fluxos guiados.) As contagens de histórias por domínio
> permanecem idênticas ao map (199 itens); só a classificação Primary/Derived dessas 3 mudou.

---

## 7. General Consolidation

Duas camadas aplicadas à base: **(a)** ajuste de teste +12,5% a todos os domínios exceto FND, OPS
e INT; **(b)** contingência — 50% para INT, CPM e PROCP, 35% para os demais.

| Domínio   | Base min–max  | +Teste (12,5%) | +Contingência   | Cont% |
| --------- | ------------- | -------------- | --------------- | :---: |
| FND       | 65–164        | 65–164         | **88–221**      |  35%  |
| OPS       | 60–137        | 60–137         | **81–185**      |  35%  |
| CIM       | 59–139        | 66–156         | **89–211**      |  35%  |
| CPM       | 115–205       | 129–231        | **194–346**     |  50%  |
| CRM       | 40–72         | 45–81          | **61–109**      |  35%  |
| COPM      | 25–41         | 28–46          | **38–62**       |  35%  |
| PROCP     | 66–112        | 74–126         | **111–189**     |  50%  |
| OMNI      | 97–228        | 109–257        | **147–346**     |  35%  |
| SDP       | 66–106        | 74–119         | **100–161**     |  35%  |
| INT       | 139–217       | 139–217        | **208–326**     |  50%  |
| **Total** | **732–1.421** | —              | **1.117–2.156** |       |

### Consolidação por squad

| Squad                                  | Domínios                 | SP base       | SP c/ teste+contingência        | Velocidade nominal |
| -------------------------------------- | ------------------------ | ------------- | ------------------------------- | ------------------ |
| S1 Foundation & Ops                    | FND + OPS                | 125–301       | **169–406**                     | 30–40              |
| S2 Interaction, Relationship & Capture | CIM + CRM + COPM + PROCP | 190–364       | **299–571**                     | 30–40              |
| S3 Problem & Guided Flows              | CPM                      | 115–205       | **194–346**                     | 25–35              |
| S4 Channels & Agentforce               | OMNI + SDP               | 163–334       | **247–507**                     | 30–40              |
| S5 Integration/Core                    | INT                      | 139–217       | **208–326**                     | 25–30              |
| **Total**                              |                          | **732–1.421** | **1.117–2.156** (mid **1.636**) |                    |

---

## 8. Parallelism and Critical Path Schedule

Os **cinco squads** de build operam em paralelo desde o Sprint 0. A duração do projeto é o
**caminho crítico** — o squad que precisa de mais sprints — não a soma. Sprints = SP (com
contingência) ÷ velocidade **nominal**, arredondado ao próximo sprint inteiro. O caminho crítico é
de **construção pura**: mede quantos sprints o build consome, sem embutir trava por falta de
definição funcional ou dependência externa — esse risco vive na contingência (§7), não aqui
(premissa 5).

| Squad                                      | SP c/ cont. | Vel. nominal | Sprints (otim.) | Sprints (central) | Sprints (pess.) |
| ------------------------------------------ | ----------- | ------------ | --------------: | ----------------: | --------------: |
| S1 Foundation & Ops                        | 169–406     | 30–40        |               5 |                 9 |              14 |
| **S2 Interaction, Relationship & Capture** | **299–571** | **30–40**    |           **8** |            **13** |          **20** |
| S3 Problem & Guided Flows                  | 194–346     | 25–35        |               6 |                 9 |              14 |
| S4 Channels & Agentforce                   | 247–507     | 30–40        |               7 |                11 |              17 |
| S5 Integration/Core                        | 208–326     | 25–30        |               7 |                10 |              14 |

- **Otimista:** SP **min** (c/ cont.) ÷ velocidade **alta**.
- **Central:** SP **midpoint** ÷ velocidade **média**.
- **Pessimista:** SP **max** (c/ cont.) ÷ velocidade **baixa**.

### O caminho crítico é o S2 em todos os cenários

| Cenário        | Caminho crítico                            | Sprints | Duração             | Segundo mais longo |
| -------------- | ------------------------------------------ | ------: | ------------------- | ------------------ |
| **Otimista**   | **S2 Interaction, Relationship & Capture** |       8 | 16 sem (~3,7 meses) | S4 / S5 (7)        |
| **Central**    | **S2 Interaction, Relationship & Capture** |      13 | 26 sem (~6,0 meses) | S4 Channels (11)   |
| **Pessimista** | **S2 Interaction, Relationship & Capture** |      20 | 40 sem (~9,2 meses) | S4 Channels (17)   |

**Mensagem estratégica — o gargalo é a massa concentrada no S2, e o cronograma é mais longo e
realista.** Com cinco squads em vez de sete, quatro domínios de atendimento (Customer Interaction,
Relationship/V360, o envelope COPM e a captura PROCP) correm num único squad — o **S2**, que é o
caminho crítico em todos os cenários. Duas escolhas deliberadas de calibração explicam por que o
cronograma alongou ante a revisão anterior:

- **Menos paralelismo, por design.** Sete squads assumiam uma capacidade de coordenação que uma
  reconstrução deste porte, com a Vivo definindo regras em tempo real, não sustenta. Consolidar
  para cinco reconhece que o trabalho de atendimento é fortemente acoplado (mesma superfície,
  mesmos dados, mesmas regras regulatórias) e não se distribui sem atrito.
- **Velocidade nominal, incerteza na contingência.** A velocidade de cada squad é o patamar
  nominal por trilha; o tempo gasto em workshops, reconciliação regulatória e alinhamento de
  contrato de integração — a Vivo não tem as respostas prontas — é absorvido pela contingência
  (§7), não pela velocidade. O caminho crítico mede **construção pura**: quantos sprints o build
  consome, sem trava por falta de definição ou dependência externa.

**O que isto diz à liderança:** o cronograma se decide **num único lugar — o S2**. Acelerar exige
rebalancear massa para fora do S2: extrair PROCP (captura de pedido) ou COPM (envelope) para um
sexto squad encurtaria o caminho crítico, ao custo de mais coordenação e headcount. É a alavanca
de cronograma mais direta, e uma decisão de investimento explícita para a liderança.

**Alavancas de aceleração:**

1. **Rebalancear o S2** — mover PROCP e/ou COPM para um squad dedicado é a alavanca de cronograma
   número um; tudo mais é secundário enquanto o S2 concentrar quatro domínios.
2. **Fluxos guiados (S3)** — provar cedo o runtime de entrevista determinística (FND-04) e o motor
   CPM-04; as contestações por família derivam dele, então o motor é a alavanca (Risco #2).
3. **Integração (S5)** — facades MuleSoft confirmadas, contratos de API limpos, uma fábrica de
   clientes resilientes reutilizável (liga-se ao Risco #3); mantém o piso transacional sem virar
   gargalo.

---

## 9. Effort Estimate in FTE-hours

O esforço de build de cada squad é **headcount × sprints do próprio squad × 60 FTE-h/sprint** —
alocado pela trilha do squad, não pela duração do caminho crítico. QA e o transversal técnico
entram como **+15% do esforço de build** (não como headcount alocado por calendário):

```
horas = Σ(headcount × sprints × 60) do build × 1,15
```

Este acoplamento ao esforço — e não à duração — é deliberado. Um modelo que alocava QA/transversal
pela duração do caminho crítico produzia o artefato indefensável de **mais escopo gerando menos
horas** (quando o cronograma encurtava, o overhead encolhia mesmo com mais build). Ancorar o
overhead ao esforço de build torna as horas **monotônicas**: mais escopo ⇒ mais build ⇒ mais QA e
transversal ⇒ mais horas, sempre.

### Cenário Central (caminho crítico S2, 13 sprints, ~6,0 meses)

| Time                                     | Headcount | Sprints |   FTE-horas |
| ---------------------------------------- | --------: | ------: | ----------: |
| S1 Foundation & Ops                      |         5 |       9 |       2.700 |
| S2 Interaction, Relationship & Capture   |         6 |      13 |       4.680 |
| S3 Problem & Guided Flows                |         5 |       9 |       2.700 |
| S4 Channels & Agentforce                 |         6 |      11 |       3.960 |
| S5 Integration/Core                      |         5 |      10 |       3.000 |
| **Subtotal build**                       |    **27** |         |  **17.040** |
| QA + transversal técnico (+15% do build) |         — |       — |       2.556 |
| **Total**                                |           |         | **~19.600** |

### Total por cenário — horas produtivas × horas contratadas

As FTE-horas que a ROM computa são **horas produtivas** (trabalho efetivo de entrega). O fator de
produtividade já está embutido na fonte — a base de **6h/dia** (premissa 7) e a **velocidade
nominal** por squad. Para planejamento comercial, essas horas produtivas convertem-se em **horas
contratadas** (8h/dia, 40h/semana) pela operação **inversa** — divide-se pela produtividade,
porque é preciso _contratar mais horas do que se consome em trabalho efetivo_:

```
horas contratadas = horas produtivas ÷ fator de produtividade
```

Apresentamos as duas bases lado a lado: **75%** (= `6h ÷ 8h`, apenas desfaz a trava embutida e
devolve o equivalente a 8h/dia) e **70%** (fator comercial mais conservador).

| Cenário        | Duração (caminho crítico S2) | Produtivas (engenharia) | Contratadas — equivalente 8h/dia (@ 75%) | Contratadas — ajuste comercial (@ 70%) |
| -------------- | ---------------------------- | ----------------------: | ---------------------------------------: | -------------------------------------: |
| **Otimista**   | 8 sprints (~3,7 meses)       |               ~12.400 h |                                ~16.600 h |                              ~17.700 h |
| **Central**    | 13 sprints (~6,0 meses)      |               ~19.600 h |                                ~26.100 h |                              ~28.000 h |
| **Pessimista** | 20 sprints (~9,2 meses)      |               ~29.800 h |                                ~39.700 h |                              ~42.600 h |

**Não redescontar (evitar double-count).** As horas produtivas **já são líquidas** — o overhead
(cerimônia, context-switching) foi descontado na base de 6h/dia. _Multiplicá-las_ por um fator de
produtividade desconta o overhead **duas vezes** e subestima o esforço (ex.: `19.600 × 0,70 =
13.720` está **errado**). A conversão correta é sempre a divisão acima; as colunas contratadas
são maiores que as produtivas, nunca menores. Escolha **uma** base (75% ou 70%) e seja
consistente — não empilhe as duas.

**Contingência ≠ produtividade — eixos independentes.** A contingência (35% global; 50% em CPM,
INT e PROCP, §7) é o buffer do _cone de incerteza de escopo_ (ambiguidade tier-1, malha de
integração frágil, workflows de entrevista de 300+ passos, captura agêntica nova), **não** uma
folga de capacidade/eficiência do time. Um eixo não cobre o outro: usar contingência para
absorver déficit de produtividade — ou vice-versa — desbalanceia ambos.

> Estas horas cobrem **engenharia e arquitetura** — build, QA e o transversal técnico. **Não**
> incluem gestão de projetos (PM, Scrum Master, Agile Coach, Delivery Manager), que precisa ser
> dimensionada à parte pelos APs — não é responsabilidade de delivery calculá-la, mas tampouco é do
> cliente: continua sendo esforço que precisa ser alocado. A conversão produtiva → contratada é um
> passo comercial, apresentado aqui apenas para não ser reinventado nem mal-aplicado.

---

## 10. Identified Risks

Gaps e questões que dirigem a contingência. Os riscos #1, #2 e #3 são os que mais influenciam a
faixa e justificam os buffers de 50% em CPM, PROCP e INT.

1. **Jornadas de maior dor não modeladas (dirige parte do buffer de 50% do CPM).** Os ramos
   Problem, Technical Complaint e Termination estavam **declarados mas não desenhados** nos fluxos
   de origem. Sua substância veio do corpus de dor Vivo + pesquisa de plataforma, não de um fluxo
   UPN modelado — maior incerteza de design. Estas são as maiores dores da Vivo, então o risco é
   material.

2. **Fluxos determinísticos guiados — agora dimensionados, não invocados (dirige o buffer de 50%
   do CPM; reverte o risco anterior).** A revisão anterior tratava os workflows regulados pesados
   (contestação de fatura ≈ 300+ passos, negociação de dívida, despacho técnico) como
   **invocados** — o risco era "e se os sistemas externos não forem invocáveis via APIs/MCP
   limpas". A devolutiva da liderança mostrou que a Vivo **não consegue expô-los** como recursos
   limpos: são iterativos, em estilo entrevista. Portanto passam a ser **construídos nativamente**
   sobre o runtime FND-04 (motor CPM-04 + derivadas por família CPM-20..24 + agendamento CPM-25 +
   portabilidade COPM-05 + dívida COPM-06). O risco residual deixa de ser "e se não forem
   invocáveis" e passa a ser **incerteza de esforço** — a profundidade real de 300+ passos e a
   variação regulatória por produto podem exceder a estimativa; contingência CPM de 50% cobre isto.
   O que permanece **delegado** é a _decisão de negócio_ downstream (product order,
   provisionamento), não a condução do atendimento. A **fatia de atendimento** do substrato
   determinístico é dimensionada em FND (AI Trust Layer, modelo Data-360, runtime de orquestração
   FND-04, standup de voz/DE); o que permanece **dependência** é a plataforma Headless-360
   enterprise transversal (compartilhada com B2X/Billing/ERP) — se atrasar, a FND não pousa e a
   superfície agentic degrada.

3. **Malha de integração de origem — volume + fragilidade (dirige o buffer de 50% do INT).** Não é
   dívida técnica na org-alvo (construímos limpo), mas a telemetria Splunk de produção mostra que a
   operação de origem dispara **~2,3M callouts/dia útil** (pico ~2,9M) com **~22% de respostas
   não-2xx** — parte é falha sistêmica, parte é resposta de negócio legítima (400/404 esperados em
   elegibilidade/consulta), a proporção exata não é separável só do log de callout. Cada um dos
   **36 clientes Core** reconstruídos
   precisa adicionar tratamento de erro resiliente ausente hoje. Dois amplificadores: (a) as
   disposições **MULE (17) assumem que a facade MuleSoft já existe** — se esses serviços Mule
   também precisarem ser construídos, esse esforço fica **fora desta ROM Core** (programa de
   integração); (b) qualquer história Core que afirme uma dependência sem cliente listado é um gap
   que escala o esforço. A Regra de Roteamento afinou a trilha (43→36), mas os clientes que restam
   concentram as escritas transacionais e a orquestração mais difíceis.

4. **Federação Data 360 vs latência de atendimento (risco de esforço na trilha FND).**
   A federação de queries e "dados mínimos residentes" não estão comprovadas na escala Vivo para
   latência de atendimento sub-segundo por voz/chat. As **7 famílias de federação (FND-09..15)** que
   a Regra de Roteamento criou dependem do mesmo scaffold de query federada — se a latência não for
   atingível, é possível redesenho de replicação seletiva, o que engrossaria a FND e poderia
   pressionar o cronograma por acoplamento com o S2. Validar cedo.

5. **Contrato de fronteira de product-order (dirige parte do buffer de 50% do PROCP).** As histórias
   de PROCP e COPM assumem um contrato de handoff estável com a **gestão** de product-order do Pillar
   2, alcançável via MCP: catálogo/pricing consumidos como ferramentas MCP e o pedido capturado
   submetido à gestão (COPM-02). A captura agêntica (PROCP) é capability nova e não provada na escala
   Vivo; se o contrato MCP com o Pillar 2 não estiver estável, a submissão (COPM-02) e a
   reconciliação de handoff bloqueiam, e a captura não tem para onde submeter. Buffer de 50% no PROCP
   cobre a novidade da captura agêntica; a dependência do contrato é de posse fora deste escopo.

6. **Qualidade de dados dos fluxos de origem.** Todos em `state: draft`; numeração de atividade
   não mapeia a IDs de nó; `reserve-resources` com Notes vazias; fluxo de identidade com descrição
   errada por copy-paste; add/remove-VAS com atividade de billing duplicada. Reconciliar antes do
   detalhamento de histórias individuais de PROCP/COPM/identidade na Phase 2.

7. **Escala do canal Parceiro/Aliado.** A persona dominante (~18k Aliado Externo via Experience
   Cloud) está representada por uma única história (OMNI-28, dimensionada 13–21 no topo da banda
   por isso). Licenciamento de partner-community, sharing e paridade da superfície para o canal
   externo provavelmente estão sub-decompostos — sinalizar passada de decomposição dedicada se o
   canal Aliado estiver no escopo de entrega.

8. **Pré-requisito de Voz/Amazon Connect.** Provisionamento SCV + Amazon Connect, migração de
   telefonia (Genesys EOL Dez-2027) e contratos AWS CCaaS são pré-requisitos para todo o
   subconjunto de voz OMNI — dependência de infraestrutura fora da construção Salesforce.

9. **Pico de volume de migração mandatória (regulatório).** Cobre→fibra (fim de concessão STFC) e
   DTH→IPTV (ambos vivos em 2026) geram picos de volume nas jornadas de migração — CPM-18/19 são
   dimensionadas como envelopes únicos, mas a _escala_ da campanha (base de cobre restante + ~300k
   clientes DTH) pode justificar um plano de capacidade de outbound proativo dedicado (liga-se a
   OMNI-27, CPM-08). Sinalizar para dimensionamento de capacidade, não histórias adicionais.

10. **Reconciliações de refinamento (impacto numérico marginal, resolver na Phase 2).** Itens
    identificados na estimativa e já ajustados nesta ROM, registrados para rastreabilidade: (a)
    **CPM-04** promovida a Primary (motor de entrevista determinística reusado por 6 famílias);
    (b) **SDP-13/14/15** reclassificadas Primary por override do Arquiteto (Active Retention Agent
    — autonomia + execução vinculada a política); (c) **COPM-03** recebeu piso de 2 SP (derivação
    em cadeia a colapsaria a 1–1 apesar de ser polling de status + atualização de UI). Nenhum
    altera as contagens de histórias; apenas classificação e magnitude.

11. **Product Design fora de escopo (dependência de entrega).** Autoria de catálogo/PCM,
    configuração de CPQ, precificação, crédito, setup de billing, geração de contrato e fulfillment
    estão excluídos e devem ser entregues por outro time/agente. O PROCP **consome** catálogo/pricing
    do Pillar 2 via MCP e **submete** à gestão do Pillar 2; não os autora. A ausência deles é uma
    dependência de entrega, não uma linha da ROM.

---

## 11. Elements × Stories Traceability

| Epic / Domínio                                              | Fluxo(s) de origem                                                                                                                                                                                              | Caminho no repo                                                                                                                                |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| FND                                                         | Presentation Pillar 3 (Headless 360 / AI Trust Layer / fundações determinísticas) + as 7 famílias de federação Data 360 (Regra de Roteamento) — apenas fatia de atendimento                                     | devolutiva Alex Salgado; premissas 3–6/17; `architecture/governance/`                                                                          |
| CIM                                                         | Manage Contact; Manage and Route Request; Initiate Inquiry Management; Validate Customer Satisfaction                                                                                                           | `architecture/flows/request-to-answer/`                                                                                                        |
| CPM                                                         | Manage and Route Request (nós de ramo Problem/Technical/Termination 33/35/39) + corpus de dor Vivo + fluxos determinísticos guiados (premissa 18)                                                               | `architecture/flows/request-to-answer/request-to-answer-manage-and-route-request.md`; `../vivob2c/docs/vivo-desafios-atendimento-compilado.md` |
| CRM / V360                                                  | V360 Consult and Action Customer 360 Context; V360 Capability Map                                                                                                                                               | `architecture/flows/customer-relationship-management-v360/`                                                                                    |
| COPM                                                        | Request to Change; E2E Order to Payment (referência de envelope) — envelope de atendimento puro                                                                                                                 | `architecture/flows/request-to-change/`; `architecture/flows/order-to-payment/`                                                                |
| PROCP                                                       | Request to Change (Add/Remove VAS; MSISDN Change; Plan Migration); Order to Payment (placement); reusable (serviceability, reserve-resources, configure-products) — captura por família × operação              | `architecture/flows/request-to-change/`; `architecture/flows/order-to-payment/`; `architecture/flows/reusable-processes/`                      |
| OMNI                                                        | Pesquisa Service Cloud Voice / Amazon Connect / Omni-Channel / Digital Engagement                                                                                                                               | pesquisa; premissas                                                                                                                            |
| SDP                                                         | Premissa Agentforce / service-dynamic-plan + arquitetura CRM+                                                                                                                                                   | premissas; `../vivob2c/docs/`                                                                                                                  |
| SDP-13/14/15                                                | Proposta "Salesforce & vivo: Our Way Forward" (Active Retention Agent)                                                                                                                                          | devolutiva Alex Salgado                                                                                                                        |
| OPS                                                         | Pesquisa de plataforma (palitagem, entitlements, Knowledge) + corpus Vivo §3                                                                                                                                    | pesquisa; `../vivob2c/`                                                                                                                        |
| INT                                                         | **Ancorado na realidade:** os 74 serviços `WebService__c` vivos normalizados para TM Forum Open APIs + telemetria de callout de produção (Splunk) como cross-check; 36 clientes Core após a Regra de Roteamento | org viva `WebService__c`; logs `apout` do Splunk; catálogo TMF (`tmforum-apis`)                                                                |
| CIM-18/19, CPM-17/18/19/20-25, CRM-13, COPM-07, PROCP-14/15 | Relatório TM Forum eTOM independente (contact-driver, migrações R2C, churn SHAP, contestação por família)                                                                                                       | `~/Downloads/Fluxos de Atendimento e Motivos de Contato em Telecomunicações (Padrões TM Forum).md`                                             |

O story map de origem (`architecture/vivo-b2c-atendimento-story-map.md`) carrega a traceability
completa por história, a taxonomia de motivos de contato e a batimetria dos 74 serviços.

---

## 12. Exclusions

Explicitamente fora de escopo, com racional:

| Excluído                                                                                              | Racional                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product Order Management** (decomposição→orquestração, submit TMF622 downstream, fulfillment)       | Fronteira delegada (premissa 19); pertence ao Pillar 2 (B2X Commerce), alcançável via MCP. O PROCP **captura e submete**; a gestão executa.                                   |
| **Camadas Product/Service/Resource** (Deliver Mobile/Internet/TV, provisionamento TMF641/639)         | Fora das 4 capacidades eTOM Customer + captura em escopo.                                                                                                                     |
| **Autoria de catálogo/PCM, CPQ, precificação, crédito, billing setup, geração de contrato**           | Product Design — fronteira delegada; **consumido** pelo PROCP como ferramentas MCP do Pillar 2, não autorado aqui.                                                            |
| **Jornadas de venda/aquisição** (`r2a-sales-journey-b2c/`, `b2b-selling/`, `catalog/`, `sales-home/`) | Domínio de vendas/product-order — adjacente, fora da camada de atendimento.                                                                                                   |
| **Plataforma Headless-360 enterprise transversal** (compartilhada com B2X, Billing, ERP)              | Dependência de programa; dimensioná-la contra uma ROM de atendimento sobrecarregaria o atendimento. A FND dimensiona apenas o enablement específico de atendimento sobre ela. |
| **Serviços Mule (a facade em si), para as 17 disposições MULE**                                       | Assumidos como pré-existentes; se precisarem ser construídos, é esforço do programa de integração, fora desta ROM Core.                                                       |
| **Migração de voz B2B-adjacente (PBX/ATA)**                                                           | Esta ROM é B2C; a variante corporativa está fora, anotada como fronteira.                                                                                                     |
| **Gestão de projeto** (PM, SM, Agile Coach, Delivery Manager)                                         | Premissa 16 — fora da capacidade de engenharia/arquitetura; dimensionada à parte pelos APs (nem delivery nem cliente a calculam, mas é esforço que precisa ser alocado).      |

---

> **Fim da ROM.** Derivada de `architecture/vivo-b2c-atendimento-story-map.md` (199 itens). Números
> são ROM (faixa de esforço para decisão de investimento), não um plano de sprint comprometido. O
> refinamento por história (Phase 1/2) ajusta magnitudes individuais dentro destas faixas.
