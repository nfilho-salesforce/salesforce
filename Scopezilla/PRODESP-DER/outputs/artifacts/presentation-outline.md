# Outline de Apresentação — PRODESP · DER-SP
*Gerado em 2026-09-17 23:54 -03*

## Fundações Socráticas

- **Objetivo real**: o cliente sai da apresentação com escopo alinhado (MVP, arquitetura, gaps/riscos, linha do tempo, capacidades/tecnologia, roadmap) e decide seguir com a Salesforce PS — a conclusão que buscamos é "eles entenderam o que a DER precisa."
- **Audiência**: DER-SP / PRODESP / Stefanini — lideranças de processo e operação. Fluentes no processo de negócio de socorro rodoviário, já viram valor concreto na PoC de Cubatão/Taubaté. Não são técnicos de TI/plataforma.
- **Fluência**: Parcialmente fluente — nomes de produto aparecem diretos (Field Service, Agentforce, Service Cloud, Experience Cloud), mas todo padrão interno (Skills, Service Territory, trilha de auditoria) é explicado em uma frase na primeira menção. Sem jargão Scopezilla (sem E01-E05 expostos como códigos — aparecem como nomes de capacidade).
- **Big Idea**: Este projeto leva o DER a uma nova fase de escalabilidade e inovação — coloca a tecnologia em prol dos processos e, no fim da linha, do cidadão na pista.

**Nomes de produto travados para o deck**: Field Service, Agentforce (Contact Center Enterprise), Service Cloud (escopado ao canal WhatsApp), Experience Cloud, WhatsApp. Buscarei consistência dos mesmos termos que já constam em `01-solution.md`/`executive-summary.md`.

## Cadeia Lógica e Tom

- **Arco**: Situação Atual → Visão de Transformação → Caminho (arquitetura, MVP, roadmap, riscos administrados) → Fechamento com o Ask. Escolhido porque a audiência já acredita no valor (viu a PoC) — o trabalho da apresentação é provar que entendemos a escala real do problema e temos um caminho executável, não convencer do valor em si.
- **Tom**: Autoritativo — direto, baseado em evidência, sem hedging — moderado por uma leitura de "parceria" na seção de change management (é uma jornada que a equipe de 1.152 operadores faz junto).

---

## Slide 1 — Capa

**Action Title**: PRODESP-DER: da PoC de Cubatão/Taubaté para uma nova fase de escala estadual
**Motivo**: Ancora o Big Idea antes de qualquer dado — a audiência sabe onde a história termina antes de percorrer o caminho.
**Conteúdo**: Nome do programa · DER-SP · Field Service + Agentforce · data
**Visual**: Capa limpa, wordmark + big idea como subtítulo
**Densidade**: sparse
**Fonte de dados**: `.project-metadata.json` (nome do projeto, produtos em escopo)

## Slide 2 — Situação Atual

**Action Title**: Hoje, o socorro na rodovia não tem um protocolo único do pedido ao encerramento
**Motivo**: Estabelece a dor antes da visão — sem isso, "nova fase de inovação" é abstrato.
**Conteúdo**: Atendimento fragmentado em chamados distintos (pedido/despacho/encerramento); sem identificador único; sem rastreamento em tempo real para o cidadão na pista; único canal hoje é a voz (0800) — WhatsApp existente pertence à ouvidoria, não ao socorro emergencial.
**Visual**: Stat/quote dominante ("0 protocolo único") + 3 bullets de apoio
**Densidade**: sparse
**Fonte de dados**: `strategy.json.business_outcomes` (pain_removed de V1/V2), `executive-summary.md` Visão Geral

## Slide 3 — Visão de Transformação

**Action Title**: A tecnologia a serviço do processo — e, no fim da linha, do cidadão na pista
**Motivo**: É o Big Idea, dito uma vez de forma central e memorável antes de entrar em arquitetura/MVP.
**Conteúdo**: Protocolo único e rastreável do primeiro contato ao encerramento; despacho automático apoiado pelo Field Service; entrada pelo canal que o motorista já usa (voz ou WhatsApp); a escala real é 14 CGRs, não só o piloto.
**Visual**: Texto hero central, sem gráfico competindo
**Densidade**: sparse
**Fonte de dados**: `strategy.json.transformation_strategy.vision_statement`

## Slide 4 — Resultados de Valor Confirmados

**Action Title**: Quatro resultados de valor confirmados com o DER orientam todo o desenho da solução
**Motivo**: Conecta a visão a compromissos concretos e verificáveis antes de mostrar arquitetura — mostra que entendemos o "porquê" tanto quanto o "o quê".
**Conteúdo**: V1 Protocolo único e rastreável · V2 Canal digital complementar ao 0800 · V3 Despacho automatizado com governança de exceção · V4 Auditabilidade do ciclo de atendimento — cada um com a dor que remove.
**Visual**: 4 linhas categoria-chip (chip = V#, conteúdo = outcome + dor removida)
**Densidade**: balanced
**Fonte de dados**: `strategy.json.business_outcomes[]` (V1-V4, todos confidence: Confirmed)

## Slide 5 — Arquitetura da Solução

**Action Title**: Uma única arquitetura: o Field Service comanda o despacho, o Agentforce abre a porta do WhatsApp
**Motivo**: É a prova técnica (em linguagem de negócio) de que a solução é coerente, não uma colagem de produtos.
**Conteúdo**: Org única Salesforce · Field Service como motor central de despacho (Work Order/Service Appointment/Service Territory, modelo de Skills para aderência) · Agentforce Contact Center Enterprise cobrindo o canal WhatsApp · Service Cloud escopado a esse canal (não atendimento amplo) · Experience Cloud para o link de rastreamento do cidadão · duas integrações com os sistemas legados SIGOR/SIGEO.
**Visual**: Hub-and-spoke — Salesforce (org única) no centro, com Field Service/Agentforce/Service Cloud/Experience Cloud como módulos e SIGOR/SIGEO como sistemas externos alimentando/recebendo dados
**Densidade**: dense
**Fonte de dados**: `outputs/01-solution.md` (Arquitetura Foundations + Destaques da Solução), `data/epics.json` (products)

## Slide 6 — Alcance do MVP

**Action Title**: O MVP cobre toda a produção estadual — 14 CGRs, 298 viaturas, 1.152 operadores
**Motivo**: Fecha de vez a pergunta "isso é só o piloto?" — o MVP já é a escala real, não uma extensão futura.
**Conteúdo**: 14 CGRs (não apenas Cubatão/Taubaté) · 298 viaturas · 1.152 operadores de campo em 14 empresas terceirizadas · 5 capacidades entregues integralmente pela Salesforce PS, em org única.
**Visual**: Linha de stat tiles (14 / 298 / 1.152 / 5) + tabela dos 5 épicos (nome + tamanho)
**Densidade**: balanced
**Fonte de dados**: `.project-metadata.json.geographic_scope`, `executive-summary.md` Escopo, `data/epics.json`

## Slide 7 — Complexidade e Tecnologia por Capacidade

**Action Title**: Quatro das cinco capacidades concentram alta complexidade — despacho e mobilidade de campo puxam o esforço
**Motivo**: Mostra honestidade sobre onde está o esforço real, sem inflar nem esconder — credibilidade técnica em linguagem de negócio.
**Conteúdo**: Canal Digital (M) · Registro e Classificação (L) · Despacho Automatizado (L) · Execução em Campo (L) · Rastreamento em Tempo Real (L) — tecnologia por capacidade: catálogo de +100 subtipos, motor de aderência com Skills, app único de Field Service Mobile, site de convidado no Experience Cloud.
**Visual**: Distribuição de tamanhos (1 M, 4 L) + tabela capacidade→tecnologia
**Densidade**: dense
**Fonte de dados**: `data/estimates.json` (t_shirt_size), `outputs/01-solution.md` (solução por épico)

## Slide 8 — Gaps Mapeados e a Fase 0

**Action Title**: 79 gaps mapeados na discovery, sete deles conflitos de fonte — por isso a Fase 0 é necessária antes do build
**Motivo**: Antecipa a objeção "por que uma fase extra antes de começar?" com o número, não com uma justificativa vaga.
**Conteúdo**: Missing Requirement 26 · Logical Gap 14 · Ambiguity 10 · Potential Risk 8 · Out of Scope 6 · Capability Gap 6 · Source Conflict 7 · Assumption 2. Limite que aciona recomendação de Fase 0: >15 gaps ou >5 conflitos de fonte — ambos excedidos.
**Visual**: Barra/distribuição das 8 categorias, com Source Conflict destacado
**Densidade**: dense
**Fonte de dados**: `data/gaps.json` (contagem por categoria)

## Slide 9 — Riscos Críticos e Mitigações

**Action Title**: Dois riscos bloqueiam decisão do DER antes do build — trilha de auditoria e limite contratual das UBAs por CGR
**Motivo**: Nomeia os únicos dois itens que realmente travam o cronograma, separando do ruído dos outros riscos monitorados.
**Conteúdo**: G0305 — trilha de auditoria do despacho sem desenho definido (padrão nativo tem limite de 20 campos/18-24 meses de retenção); G0309 — limite contratual das UBAs por CGR não confirmado, despacho por proximidade pode indicar viatura de CGR vizinha. Mitigações: resolver ambos na Fase 0, antes de configurar console/território.
**Visual**: 2 callouts vermelhos (bloqueadores) + 3-4 callouts amarelos (riscos monitorados: enforcement offline, LGPD/DPIA, licença Field Service Community)
**Densidade**: balanced
**Fonte de dados**: `data/gaps.json` (Potential Risk, G0305/G0309), `executive-summary.md` Riscos e Mitigações

## Slide 10 — Roadmap: Cinco Fases

**Action Title**: Cinco fases levam a solução da fundação ao rastreamento em tempo real em 16 a 30 semanas
**Motivo**: É a resposta central a "quando" — com uma faixa otimista mas honesta, não uma data solta.
**Conteúdo**: Fase 0 Resolução de Discovery · Fase 1 Fundação (Registro da Ocorrência e Integrações) · Fase 2 Despacho Automatizado + Canal Digital · Fase 3 Execução em Campo · Fase 4 Rastreamento e Estabilização. Caminho crítico E02→E03→E04→E05. Faixa derivada do formato do engagement (benchmark), 16-30 semanas — ponta alta ampliada por mobile/site 100% customizados e overlay de governança/auditoria em aberto. Nota de urgência: contrato da URA atual expira abril/2027, mesma janela da produção-alvo.
**Visual**: Timeline horizontal das 5 fases + faixa de duração com disclaimer de benchmark
**Densidade**: dense
**Fonte de dados**: `data/roadmap.json` (fases/épicos), `.project-metadata.json.timeline` (faixa derivada, driver de urgência)

## Slide 11 — Adoção e Change Management

**Action Title**: 1.152 operadores em 14 empresas terceirizadas — por isso o DER pediu até dois meses de operação assistida
**Motivo**: Mostra que a escala humana da mudança foi ouvida e planejada, não é um risco escondido.
**Conteúdo**: Change management não é adição do time de entrega — foi pedido explícito do DER; operação assistida + treinamento personalizado por persona, foco nos técnicos de campo das 14 UBAs; a experiência do cidadão (link de rastreamento) já foi validada na PoC, sem necessidade de pesquisa de UX adicional.
**Visual**: Stat tile (1.152 / 14 / até 2 meses) + narrativa curta
**Densidade**: balanced
**Fonte de dados**: `executive-summary.md` Esforço e Disciplinas (parágrafo de Change Management)

## Slide 12 — Fechamento: o Ask

**Action Title**: Fechar agora leva o DER a uma nova fase de escalabilidade e inovação — a tecnologia em prol do processo e do cidadão
**Motivo**: Repete o Big Idea como último pensamento na sala e converte em três ações concretas — é o slide que precisa gerar a decisão.
**Conteúdo**: Ask em 3 passos: (1) aprovar o escopo dos 5 épicos e a faixa de roadmap apresentada; (2) validar com Salesforce PS os dois riscos bloqueadores (auditoria, limite de UBAs) na sessão de Fase 0; (3) iniciar a Fase 0 com o roteiro já mapeado.
**Visual**: Big Idea repetida como hero + 3 bullets de ask numerados
**Densidade**: sparse
**Fonte de dados**: `executive-summary.md` Próximos Passos e Recomendações

---

## Notas de Palco (resumo por slide)

1. Abrir com confiança — este é o resultado da PoC, não uma nova venda.
2. Não passar rápido demais aqui — é a única vez que a dor aparece explicitamente antes da solução.
3. Pausa de 2-3 segundos após ler o Big Idea — deixar a frase assentar.
4. Se perguntarem "por que só 4 outcomes", responder: são os que o DER confirmou — o resto é tático, não estratégico.
5. Se perguntarem sobre outras nuvens Salesforce fora de escopo, reforçar: Service Cloud está deliberadamente limitado ao canal WhatsApp — não é atendimento amplo.
6. Âncora numérica — repetir "14, 298, 1.152" verbalmente, não só ler o slide.
7. Honestidade aqui gera confiança — "sim, é complexo, e sabemos exatamente onde".
8. Framear como "encontramos isso porque olhamos com profundidade" — não como uma falha da PoC.
9. Ser direto: "estes dois itens precisam de uma decisão do DER, não da Salesforce, antes do build."
10. Nomear a janela do contrato da URA em voz alta — é o argumento de urgência mais forte que existe.
11. Deixar claro: esse plano já reflete o pedido do próprio DER, não é overhead nosso.
12. Terminar em silêncio após o ask — não preencher o espaço, deixar a decisão ser deles.

---

## Reclassificação: este artefato é o ROM

Confirmado com o usuário — o entregável final não é só um deck de venda, é o **ROM (Rough Order of Magnitude)** de PRODESP-DER: o documento único que leva escopo, arquitetura, gaps/riscos, linha do tempo, épicos/casos de uso e investimento ao cliente para decisão de fechamento. Estrutura adotada, seguindo o padrão de ROM já usado em `DATAPREV-PAT/outputs/artifacts/rom-cliente.html` (grupos de nav: Análise · Desenho · Escopo · Gestão · Estimativa & Entrega):

1. **Visão Executiva** — Capa, Situação Atual, Visão de Transformação, Resultados de Valor (Slides 1-4)
2. **Arquitetura & Solução** — Arquitetura, Alcance do MVP (Slides 5-6)
3. **Escopo** — Épicos & Casos de Uso (nova seção abaixo), Complexidade por Capacidade, Gaps e Fase 0 (Slide 7-8 + nova seção)
4. **Gestão** — Riscos Críticos, Adoção/Change Management (Slides 9, 11)
5. **Estimativa & Entrega** — Linha do Tempo detalhada, Investimento com/sem impostos (novas seções abaixo)
6. **Fechamento** — o Ask (Slide 12)

## Linha do Tempo — Detalhamento (Estimativa & Entrega)

**Ação**: Cinco fases levam da fundação ao rastreamento em tempo real; a faixa de investimento varia por modelo de entrega.

| Fase | Épicos incluídos | Objetivo |
|---|---|---|
| Fase 0 — Resolução de Discovery | — | Resolver G0305 (auditoria de despacho) e G0309 (limite de UBAs por CGR) antes do build |
| Fase 1 — Fundação | E02 | Registro da Ocorrência e Integrações (SIGOR/SIGEO) |
| Fase 2 — Despacho e Canal Digital | E03, E01 | Despacho Automatizado + Canal Digital (WhatsApp/Agentforce) |
| Fase 3 — Execução em Campo | E04 | App mobile único, travas de negócio |
| Fase 4 — Rastreamento e Estabilização | E05 | Link de rastreamento do cidadão, painel de gestores |

**Caminho crítico**: E02 → E03 → E04 → E05.

**Três lanes de duração** (não há `duration_weeks` por fase — `roadmap.json` não carrega essa granularidade; a faixa é derivada top-down por lane, não somada bottom-up):

| Lane | Duração | Basis |
|---|---|---|
| **Traditional** (âncora) | 16-30 semanas | Derivada do formato do engagement (benchmark top-down), sem compressão |
| **Augmented** | 14-25 semanas | Faixa traditional comprimida por `efficiency.json.realized_band` (~10-18%) |
| **AI-native** (condicional) | 10-18 semanas | Faixa traditional comprimida por `efficiency.json.native_band` (~35-40%) — gate de qualificação ainda não atendido |

**Urgência**: o contrato atual de URA (Instinct) expira abril/2027 — mesma janela da meta de produção do cliente (homologação jan/fev 2027, produção abril 2027). O contrato administrativo renova em 30/nov/2026, pressionando a decisão Open CTI vs. Salesforce Voice.

**Fonte de dados**: `data/roadmap.json` (fases/épicos/objetivos), `data/estimate-comparison.json.lanes` (durações por lane), `.project-metadata.json.timeline` (faixa derivada, driver de urgência).

## Épicos e Casos de Uso (Escopo)

Cada épico segue o padrão "o que entrega / capacidade Salesforce / casos de uso habilitados" — mesmo formato usado no ROM de referência.

### E01 — Canal Digital de Atendimento ao Cidadão (WhatsApp + Agentforce) · Tamanho M
**O que entrega**: abertura de chamado de socorro via WhatsApp (texto/áudio) com triagem automatizada, sempre com transbordo garantido para fila humana com contexto completo — a IA nunca decide a gravidade da vítima. Complementa, nunca substitui, o 0800.
**Capacidade Salesforce**: Service Cloud (Agentforce Contact Center Enterprise, 50 licenças) + Digital Engagement + Service Console.
**Casos de uso habilitados**: abertura de chamado via WhatsApp · triagem automatizada pelo Agentforce · transbordo garantido para fila humana · criação automática de ordem de serviço e protocolo.

### E02 — Registro e Classificação da Ocorrência · Tamanho L
**O que entrega**: criação do chamado a partir de qualquer canal, classificação por catálogo de 100+ subtipos desde o dia 1, com trilha de auditoria e integração com os sistemas legados SIGOR/SIGEO.
**Capacidade Salesforce**: Field Service (Work Order, Work Type) + Service Console + integrações ponto a ponto.
**Casos de uso habilitados**: registro do chamado multi-canal (WhatsApp/0800) · catálogo de classificação (100+ subtipos) · segunda viatura no mesmo chamado · reclassificação com trilha de auditoria · deduplicação por alerta ao C2C · sincronização SIGOR/SIGEO.

### E03 — Despacho Automatizado de Recursos de Campo · Tamanho L
**O que entrega**: motor de despacho por aderência operando nas 14 CGRs, 100% reativo em tempo real, com escalonamento de espera e reprocessamento automático em recusa.
**Capacidade Salesforce**: Field Service (Skills, Service Territory, Console do Dispatcher).
**Casos de uso habilitados**: motor de despacho por aderência (Skills) · escalonamento de espera por tempo (regra N/N-10) · reprocessamento automático em recusa · console do Dispatcher · alarme e escalonamento ao supervisor da CGR · trilha de auditoria de overrides manuais.

### E04 — Execução em Campo (App Mobile) · Tamanho L
**O que entrega**: aplicativo único de Field Service Mobile para os 1.152 operadores de campo das 14 UBAs, com recebimento de despacho via push nativo e encerramento por checklist condicional.
**Capacidade Salesforce**: Field Service Mobile (licença Field Service Community).
**Casos de uso habilitados**: app único de Field Service Mobile · recebimento de despacho via push nativo · modo offline com fila de sincronização · encerramento por checklist condicional por subtipo · travas de negócio (recusa com motivo, foto, check-in geolocalizado) · sharing restrito à CGR de origem.

### E05 — Rastreamento e Visibilidade em Tempo Real · Tamanho L
**O que entrega**: protocolo único acompanhável do pedido ao encerramento — link de rastreamento para o cidadão, mapa/Gantt para o C2C, painel agregado para gestores.
**Capacidade Salesforce**: Experience Cloud (site guest + LWC/Apex) + Field Service (Aerial Routing nativo).
**Casos de uso habilitados**: link de rastreamento para o cidadão (Experience Cloud guest) · mapa/Gantt do C2C com Aerial Routing · painel agregado para gestores (4 indicadores) · governança de dados de geolocalização (DER-SP steward).

**Fonte de dados**: `data/epics.json` (capabilities, description), `data/estimates.json` (t_shirt_size).

## Approved Commercials — Investimento (ROM), valores com e sem impostos (Estimativa & Entrega)

Regra permanente de precificação PS LATAM: **valor COM imposto = valor SEM imposto ÷ 0,9345**. As rates abaixo já foram validadas pelo usuário em 2026-09-17 (com imposto); o valor sem imposto é obtido multiplicando por 0,9345 — mesma fonte, sem novo dado inventado.

**Rates aplicadas (R$/hora):**

| Bucket | Sem imposto | Com imposto |
|---|---|---|
| Architect-class sênior onshore (PM/SA/TA · Program Lead/Intent Architect/Agent Orchestrator) | R$ 884,68 | R$ 946,69 |
| Entrega sênior onshore ou qualquer offshore regular (FC/Developer/QA sênior onshore · qualquer papel offshore regular) | R$ 668,78 | R$ 715,66 |
| Change & Adoption regular onshore (Change & Adoption · Adoption Architect) | R$ 573,98 | R$ 614,21 |

**Faixa indicativa de investimento por lane (BRL, sem e com impostos):**

| Lane | Duração | Sem imposto | Com imposto |
|---|---|---|---|
| **Traditional** (âncora) | 16-30 semanas | R$ 5.918.133,18 – R$ 11.096.499,71 | R$ 6.332.940,80 – R$ 11.874.264,00 |
| **Augmented** | 14-25 semanas | R$ 5.178.366,53 – R$ 9.247.083,09 | R$ 5.541.323,20 – R$ 9.895.220,00 |
| **AI-native** (condicional) | 10-18 semanas | R$ 2.227.507,84 – R$ 4.009.514,12 | R$ 2.383.636,00 – R$ 4.290.544,80 |

> *Esta faixa é baseada nas rates de R$946,69/h (architect-class sênior onshore), R$715,66/h (entrega sênior onshore/qualquer offshore regular) e R$614,21/h (change & adoption regular onshore) que você forneceu e validou em 2026-09-17. Indicativo para planejamento apenas; a estrutura comercial final é confirmada através do acordo comercial aplicável.*

A faixa AI-native permanece condicional ao gate de qualificação (nenhum sponsor executivo nomeado, mandato AI-first ainda não assumido) — é um motivador, nunca uma entrega comprometida sem nomear o compromisso.

Este é um preço **indicativo**, não custo/margem, e não uma proposta de fixed fee.

*Esta comparação é benchmark-based, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Faixas de duração e a faixa AI-native carregam a incerteza herdada de `confidence: Assumed` em todos os 5 épicos.*

**Fonte de dados**: `data/estimate-comparison.json` (rates, lanes, indicative_price_range — Approved Commercials, validado pelo Solution Lead em 2026-09-17), `outputs/artifacts/estimate-comparison.md` (`## Approved Commercials`), regra de imposto ÷0,9345 (diretriz permanente do usuário).

---

## Renderização

Este outline (Fundações + Slides 1-12 + Linha do Tempo detalhada + Épicos/Casos de Uso + Investimento) é a fonte única de conteúdo para dois entregáveis:

1. **ROM HTML** — `outputs/artifacts/rom-cliente.html`, menu lateral esquerdo, modelado em `DATAPREV-PAT/outputs/artifacts/rom-cliente.html` (PT-BR apenas, sem toggle bilíngue).
2. **Prompt para Gemini gerar o PPTX** — `outputs/artifacts/rom-gemini-prompt.md`, um prompt único cobrindo todo o conteúdo acima (incluindo investimento e linha do tempo) para colar no Gemini e gerar a apresentação em PowerPoint/Google Slides.

Ambos carregam os mesmos disclaimers verbatim (benchmark, rate validada, faixa AI-native condicional) — nenhum dos dois some com a lente de risco/preço que o outro mostra.
