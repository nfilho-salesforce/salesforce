# Estimate Comparison — PRODESP · Poupatempo Balcão V2

*Estimativa completa, com preço indicativo.* Comparação de prazo, esforço, equipe nomeada e preço indicativo entre 3 trilhas de entrega, a partir de rates validadas pelo usuário em 2026-09-17 no projeto PRODESP-DER e reutilizadas por instrução explícita do usuário em 2026-09-22 (ver `## Approved Commercials` abaixo).

## Base compartilhada

Escopo: 10 épicos, 100% entregue pela Salesforce PS (confirmado pelo usuário) — sem redução por subtração; os papéis client-side abaixo são coverage necessária, não escopo removido. E03/E06/E09 carregam `confidence: Unknown` em `data/estimates.json`, o que amplia o teto das 3 trilhas.

**Trilha ancorada: Augmented.** Mesmo roster e mesmos rates do Traditional, comprimido apenas por ferramenta de IA (`efficiency.json.realized_band`) — o número a defender. Traditional fica como contexto ("quanto custaria sem ferramentas de IA"); AI-native é o motivador condicional.

## As 3 trilhas

| Trilha | Duração | Basis | Confiança |
|---|---|---|---|
| **Traditional** | 15–30 semanas | Benchmark top-down do formato do engagement, sem compressão | Assumed |
| **Augmented (ANCHOR)** | 14–25 semanas | Faixa traditional comprimida por `efficiency.json.realized_band` (~10-18%) | Assumed |
| **AI-native** (condicional) | 10–18 semanas | Faixa traditional comprimida por `efficiency.json.native_band` (~35-40%) — gate de qualificação ainda não atendido | Assumed |

**Delta traditional → augmented**: ~7-17% mais curto, mesmo roster, tooling de IA sobre o modelo operacional inalterado.

**Delta traditional → AI-native**: ~33-40% mais curto, **mas condicional** a um compromisso operacional (decisor diário, product owner nomeado e disponível, mandato AI-first) que a Prodesp ainda não assumiu. Hoje é um motivador — "se a Prodesp se comprometer com esse modelo de trabalho, esta seria a faixa" — nunca uma entrega alcançável sem nomear o compromisso.

## Gate de qualificação AI-native: condicional

O owner de governança de agentes de IA do lado Prodesp ainda não foi nomeado (gap consolidado em 9 gaps/7 épicos, ver `data/gaps.json`); nenhuma evidência de discovery sobre mandato AI-first ou decisor de negócio disponível diariamente. O roster client-side desta trilha (CL-01, Product Owner/Decision-maker) reflete exatamente esse gap — ainda não está preenchido. Este é o sinal, não o número, que mantém a trilha rotulada condicional.

## Roster nomeado

### Traditional & Augmented (mesma forma de equipe)

A ferramenta de IA muda o ritmo de entrega dentro dos mesmos papéis e contagens na trilha augmented — não a composição do time. Roster completo em `data/resource-plan.json` (16 linhas).

| Papel | Senioridade | Local | Qtd | Alocação | Fases | Lado |
|---|---|---|---|---|---|---|
| Program Manager | Sênior | Onshore | 1 | Full | 0-5 | PS |
| Solution Architect | Sênior | Onshore | 1 | Full | 0-5 | PS |
| Technical Architect | Sênior | Onshore | 1 | Full | 1-5 | PS |
| Functional Consultant | Sênior | Onshore | 1 | Full | 1-3 | PS |
| Functional Consultant | Regular | Offshore | 1 | Full | 2-5 | PS |
| Developer | Sênior | Onshore | 1 | Full | 1-4 | PS |
| Developer (pod de build) | Regular | Offshore | 3 | Full | 1-5 | PS |
| QA | Sênior | Onshore | 1 | Full | 1-5 | PS |
| QA (execução) | Regular | Offshore | 2 | Full | 2-5 | PS |
| Change & Adoption | Regular | Onshore | 1 | Full | 1-5 | PS |
| Product Owner/Decision-maker | Regular | Onshore | 1 (GAP) | Quarter | 0-5 | Cliente |
| Functional SME | Regular | Onshore | 2 | Half | 1-4 | Cliente |
| Functional SME (biometria/LGPD) | Regular | Onshore | 1 | Quarter | 3-4 | Cliente |
| Change & Adoption (data steward) | Regular | Onshore | 1 | Half | 1-5 | Cliente |
| Technical Architect (coordenação externa) | Regular | Onshore | 1 | Quarter | 0,3 | Cliente |
| QA (UAT) | Regular | Onshore | 1 | Quarter | 2-5 | Cliente |

### AI-native (piso de accountability core + 5 ajustes de delta)

Piso presente: Program Lead ✓, Intent Architect ✓, Agent Orchestrator ✓ (Technical Architect — escolhido pela complexidade de integração MuleSoft/E09), Adoption Architect ✓ (ganho pelo escopo real de E05/244 postos + 900 totens). Nenhuma accountability core ausente.

| Papel (rótulo AI-native) | Senioridade | Local | Qtd | Alocação | Fases | Lado |
|---|---|---|---|---|---|---|
| Program Lead | Sênior | Onshore | 1 | Full | 0-5 | PS |
| Intent Architect | Sênior | Onshore | 1 | Full | 0-5 | PS |
| Agent Orchestrator | Sênior | Onshore | 1 | Full | 1-5 | PS |
| Adoption Architect | Regular | Onshore | 1 | Half | 1,4 | PS |
| Developer | Sênior | Onshore | 1 | Full | 1-5 | PS |
| QA | Sênior | Onshore | 1 | Full | 1-5 | PS |
| QA (offshore, execução) | Regular | Offshore | 1 | Full | 2-5 | PS |
| Product Owner/Decision-maker | Regular | Onshore | 1 (GAP) | Quarter | 0-5 | Cliente |
| Functional SME | Regular | Onshore | 2 | Half | 1-4 | Cliente |
| Functional SME (biometria/LGPD) | Regular | Onshore | 1 | Quarter | 3-4 | Cliente |
| Change & Adoption (data steward) | Regular | Onshore | 1 | Half | 1-5 | Cliente |
| Technical Architect (coordenação externa) | Regular | Onshore | 1 | Quarter | 0,3 | Cliente |
| QA (UAT) | Regular | Onshore | 1 | Quarter | 2-5 | Cliente |

**O que muda vs. traditional/augmented**: o pod de 3 Developers offshore colapsa para 1 senior dirigindo agentes (E09/E07 mantêm builder humano no caminho crítico); pod de QA offshore colapsa de 2 para 1 (agent-amplificado, nunca agent-substituído, surge em E07/E08); PM/SA/TA se tornam Program Lead/Intent Architect/Agent Orchestrator, cobrindo mais escopo por sequenciamento de problemas difíceis um a um.

## Leitura de equipe (sem FTE numérico)

Não há `user_commitment` de semanas — apenas a faixa derivada (15-30 semanas) — e `derive-hours.py` corretamente se recusa a derivar horas/FTE de uma faixa, só de um compromisso. Inventar um número aqui violaria a mesma regra.

Leitura qualitativa: trilha traditional/augmented soma **10 papéis PS** (pico de ~12-13 pessoas simultâneas nas Fases 1-4, incluindo o pod de 3 Developers + 2 QA offshore) + **6 papéis client-side**. Trilha AI-native cai para **7 papéis PS** (pico de ~5-6 pessoas) com os pods de Developer e QA colapsados para 1 senior cada. Um FTE numérico real fica disponível se/quando a Prodesp comprometer um número de semanas (`roadmap` Step 0.6).

## Approved Commercials

Rates fornecidas e validadas pelo usuário em 2026-09-17 no projeto PRODESP-DER, a partir da tabela oficial de rates PS LATAM — reutilizadas neste projeto por decisão explícita do usuário em 2026-09-22 (mesma conta Prodesp, mesmo rate card institucional). Valores COM imposto (sem imposto ÷ 0,9345). Moeda: **BRL**.

**Rates aplicadas (R$/hora, com imposto):**

| Bucket | Cobre | Rate/h |
|---|---|---|
| Architect-class sênior onshore | Program Manager, Solution Architect, Technical Architect · Program Lead, Intent Architect, Agent Orchestrator (AI-native) | R$ 946,69 |
| Entrega sênior onshore, ou qualquer papel offshore regular | Functional Consultant/Developer/QA sênior onshore · Functional Consultant/Developer/QA regular offshore | R$ 715,66 |
| Change & Adoption regular onshore | Change & Adoption · Adoption Architect (AI-native) | R$ 614,21 |

**Faixa indicativa de preço por trilha** (Σ(count × alocação × rate) × 40h × faixa de duração da própria trilha, ponderada por fração de fases ativas — sem hora/FTE exato por semana, sem `user_commitment`):

| Trilha | Duração | Faixa indicativa (BRL) |
|---|---|---|
| **Traditional** | 15-30 semanas | **R$ 4.708.080,15 – R$ 9.416.160,30** |
| **Augmented (ANCHOR)** | 14-25 semanas | **R$ 4.394.208,14 – R$ 7.846.800,25** |
| **AI-native** (condicional) | 10-18 semanas | **R$ 1.781.807,60 – R$ 3.207.253,68** |

> *Esta faixa é baseada nas rates de R$946,69/h (architect-class sênior onshore), R$715,66/h (entrega sênior onshore/qualquer offshore regular) e R$614,21/h (change & adoption regular onshore) validadas em 2026-09-17 no projeto PRODESP-DER e reutilizadas aqui por decisão do usuário. Indicativo para planejamento apenas; a estrutura comercial final é confirmada através do acordo comercial aplicável.*

A faixa AI-native permanece condicional ao gate de qualificação (owner de governança de agentes de IA ainda não nomeado) — é um motivador ("se a Prodesp se comprometer com esse modelo de trabalho, esta seria a faixa de investimento"), nunca uma entrega comprometida sem nomear o compromisso.

**Decomposição do delta**: Traditional → Augmented tem como único driver a duração comprimida por `realized_band` — mesmo roster, mesmos rates. Traditional → AI-native combina dois drivers: duração comprimida por `native_band` **e** roster reformatado (mais sênior e mais enxuto, run-rate semanal ~43% menor) — por isso a redução de preço (~62-66%) supera a redução de duração (~33-40%).

Este é um preço **indicativo**, não custo/margem, e não uma proposta de fixed fee — o número que sai daqui é o que o cliente é cobrado (bill rate), nunca o que a entrega custa internamente.

---
*Esta comparação é benchmark-based, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Faixas de duração e a faixa AI-native carregam a incerteza herdada de `confidence: Unknown` em E03/E06/E09.*

## Deliverables
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/estimate-comparison.json`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/resource-plan.json`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/artifacts/estimate-comparison.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/csv/13-estimate-comparison.csv`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/csv/04-roles.csv`
