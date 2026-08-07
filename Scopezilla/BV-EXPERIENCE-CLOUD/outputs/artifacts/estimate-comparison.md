# Estimativa Dual-Track — BV (Experience Cloud + MuleSoft)

**Cliente:** BV Financeira (Banco BV) · Financial Services · Brasil
**Natureza:** engajamento *brownfield* — remediação de débito técnico e ativação de recursos prioritários sobre três portais Experience Cloud em produção e uma camada de integração MuleSoft/Apigee viva.

**Preço deferido — prazo, esforço e resourcing estão completos; adicione um preço indicativo fornecendo bill rates (rode `commercials`).** Este é o estado deliberado do deal: o BV não tem rates na base. A leitura de tempo/esforço/resourcing É a estimativa e se sustenta sozinha.

**Base compartilhada (validada uma vez):** 6 épicos entregues pela Salesforce PS (E01/E06 XL, E02/E03 L, E04/E05 M). O BV é dono de release, UAT, gestão de mudança e treinamento; a PS entrega o enablement embutido nas páginas de conteúdo do E02 (G0408). Anchor da comparação = **Tradicional** (o número real; a AI-native é derivada comprimindo-o).

---

## Comparativo lado a lado

| Dimensão | **Tradicional** (anchor) | **AI-native** (condicional) |
|---|---|---|
| **Prazo** | **~18–34 semanas** (wall-clock) | **~11–24 semanas** |
| **Time (FTE nominal/peak)** | **~7,0 FTE** | **~4,5 FTE** |
| **Preço** | *deferido — sem rates* | *deferido — sem rates* |
| Base | derivada aqui | derivada (comprimida) |

> FTE nominal/peak = Σ(count × allocation), **ignora o time-box das fases** — a média-programa é menor, pois vários papéis são limitados a janelas de fase. Sem prazo comprometido, não há como calcular a média-programa; a nominal/peak é o teto honesto, não a média.

### Prazo — proveniência

- **Tradicional (~18–34 sem):** linha paramétrica Experience Cloud / Partner Portal (straddle Standard→Full, baseline 18–24 sem); +42% de risk adders — banco regulado +18%, UI customizada (render OPA/Wizard) +12%, migração E05/volume legado desconhecido +12% (dentro do cap de +50%). Clock = wall-clock elapsed; latência do cliente dentro da banda.
- **AI-native (~11–24 sem):** baseline tradicional comprimida pela `native_band` da eficiência (~30–38%, gated + provisória): 18×(1−0,38) ≈ 11; 34×(1−0,30) ≈ 24. Pareamento assimétrico mantém a faixa honestamente ampla.

> *This figure is benchmark-based, derived from the AI model's training data and general delivery patterns (not Salesforce-validated) — not a commitment. Final figures are confirmed through the applicable commercial agreement.*

**Range drivers (o que aperta a faixa):** **E05** (volume/qualidade dos dados legados — confirmar contagem + fonte) · **E06** (tier do Anypoint contratado R2/G0602 + overhead de arquitetura G0610 — caracterizar) · **E01** (fronteira Wizard/render OPA — confirmar escopo MVP).

---

## Roster — Trilha Tradicional (anchor)

Núcleo sênior onshore + pod de build offshore que escala com volume + QA constante. Headline: **~7,0 FTE nominal/peak** (média-programa menor pelas janelas de fase).

| # | Papel | Senioridade | Local | Alocação | Fases | Justificativa |
|---|---|---|---|---|---|---|
| R01 | Solution Architect | sênior | onshore | full | 0–4 | Design ponta a ponta dos três portais; dobra segurança/perfis/sharing na escala MVP. Onshore pelo acoplamento com sistemas vivos/SMEs. |
| R02 | Technical Architect | sênior | onshore | full | 1–2 | TA/Integração dedicado: caminho crítico E06 MuleSoft (XL) + overhead G0610. Onshore pela iteração com Apigee/sistemas vivos. |
| R03 | Developer (MuleSoft) | regular | offshore | full | 1–2 | Builder MuleSoft: XAPIs/SAPIs, OAS, batch ETL, testes E2E do E06. Dirigido pelo TA. |
| R04 | Developer (Exp Cloud) ×2 | regular | offshore | full | 2–4 | Pod de build escalável dos três portais: config + custom (render OPA, Wizard, LWC, sharing). |
| R05 | QA | regular | onshore | full | 2–4 | 1 QA full-program: não-regressão em produção viva + fluxo OPA + hardening financeiro. |
| R06 | Project Manager / EM | sênior | onshore | full | 0–4 | Coordenação transversal às 5 fases + alinhamento e release/UAT com o BV. |

**Lado-cliente (BV — todos nomeados/disponíveis):** Product Owner/decisor (C01, F0–4) · SMEs por portal (C02, F1–4) · Data Steward para E05 (C03, F2) · TI/plataforma para E06/IdP (C04, F0–2) · Capacidade de UAT (C05, F2–4) · Sponsor executivo (C06, F0–4).

---

## Roster — Trilha AI-native (delta)

Núcleo sênior onshore agente-amplificado + 1 builder humano ½-time no caminho crítico + QA amplificado constante. Headline: **~4,5 FTE nominal/peak**.

| # | Papel | Senioridade | Local | Alocação | Fases | Justificativa |
|---|---|---|---|---|---|---|
| R01 | Solution Architect | sênior | onshore | full | 0–4 | Núcleo agente-amplificado; dirige a frota nos builds dos portais. Senioridade cobre mais escopo sequenciando (adj. 3). |
| R02 | Technical Architect | sênior | onshore | full | 1–2 | Dirige a frota no E06; integração/arquitetura permanecem julgamento un-delegável (adj. 2, 4). |
| R03 | Developer (builder humano) | sênior | onshore | half | 2–3 | Build de alta integridade (OPA, Wizard, MuleSoft) COM agentes; substitui o pod de 2 devs offshore + dev MuleSoft (adj. 1). |
| R04 | QA | regular | onshore | full | 2–4 | Agente-AMPLIFICADO, nunca substituído: check independente sobre o output dos agentes + hardening regulado (adj. 2). |
| R05 | Project Manager / EM | sênior | onshore | full | 0–4 | Pulso de programa, relacionamento e accountability — un-delegável (adj. 2). |

**Lado-cliente:** idêntico à trilha tradicional (o BV é dono e nomeou todos os papéis) — a cadência de SMEs e decisor tende a ser mais intensa no ritmo AI-native.

---

## Delta decomposto

A AI-native comprime ~30–38% do prazo base (via `native_band`) **e** troca a forma do time — de um pod offshore que escala com volume (~7,0 FTE nominal) para um núcleo sênior onshore + frota de agentes com 1 builder humano ½-time no build de alta integridade (~4,5 FTE nominal), com QA amplificado (não substituído).

**"AI-native é mais barata" é indefensável isolado.** A defesa é a decomposição: **forma do roster** (pod escalável → núcleo sênior + agentes) + **duração comprimida** (~30–38%) + **mix de senioridade/location** (mais sênior, menos volume offshore). A magnitude AI-native é provisória até haver actuals.

### Gate de qualificação AI-native — condicional

A compressão AI-native (~30–38%) só é **real** se o BV se comprometer com o modelo operacional conjunto: **decisor disponível diariamente, business owners empoderados, mandato AI-first.** O BV tem todo o lado-cliente nomeado e disponível — sinal **favorável**, e um product owner empoderado é exatamente o que o gate testa. Mas o gate lê o **compromisso com o modo de operar**, não o staffing; o BV ainda não confirmou o modelo AI-first. Logo a trilha permanece **condicional**: *"se o BV se comprometer com esse jeito de trabalhar, é isto que custaria."*

**Nota de honestidade (dois lados):** o diagnóstico — que um modelo operacional AI-first comprime o overhead de coordenação — é sustentado por DORA/METR; a **magnitude** (~30–38%) é majoritariamente reportada por fornecedor e **não calibrada** neste engajamento. As bandas aumentada (~10–18%) e AI-native (~30–38%) se sobrepõem — é o **status de qualificação**, não o número, que distingue as trilhas.

---

## Proveniência dos inputs

- **Fornecido pelo SSSL:** estrutura TA dedicado + builder MuleSoft; QA full-program constante; BV é dono de mudança/UAT/release (PS só enablement embutido); staffing completo do lado-cliente (todos os quatro grupos nomeados).
- **Derivado:** faixas de prazo (shape top-down); banda de compressão (efficiency.json); tamanhos de épico (design).
- **Assumed (range drivers):** volume/qualidade dos dados E05; tier do Anypoint E06.

## Nota de honestidade sobre o roster

Este roster e as FTEs são um **ponto de partida derivado por modelo que requer validação do Solution Lead** — o BV/PS é dono do time final. As decisões de **folding e alocação são julgamento**: a menos certa é ter um Technical Architect dedicado (R02) em vez de fundi-lo no Solution Architect — o caminho crítico do E06 MuleSoft justifica a separação, mas vale pressionar. **Resourcing é uma capacidade ainda em refino**: trate a forma como decision-support que te deixa perto, não um plano de staffing comprometido.

---

*Estado: completo em prazo, esforço e resourcing. **Preço deferido** — rode `commercials` por trilha ao ter bill rates para adicionar uma faixa indicativa sobre esta base.*

*Fontes: `data/estimate-comparison.json`, `data/resource-plan.json`, `data/efficiency.json`, `data/epics.json`, `data/estimates.json`, `data/roadmap.json`. Benchmark: model-training-data.*
