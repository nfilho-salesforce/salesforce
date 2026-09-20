# Estimate Comparison — PRODESP · DER-SP

*Estimativa completa, com preço indicativo.* Comparação de prazo, esforço, equipe nomeada e preço indicativo entre 3 lanes de entrega, a partir de rates validadas pelo usuário em 2026-09-17 (ver `## Approved Commercials` abaixo).

## Base compartilhada

Escopo: 5 épicos (E01-E05), 100% entregue pela Salesforce PS (confirmado pelo usuário) — sem redução por subtração, os papéis client-side abaixo são coverage necessária, não escopo removido. Todos os 5 épicos carregam `confidence: Assumed` em `data/estimates.json`, o que amplia o risco realizado das 3 lanes para a ponta alta das faixas.

**Lane-âncora: Traditional.** A faixa benchmark é o número real; as lanes de IA são derivadas por compressão dessa faixa — a postura de pitch, já que o DER/PRODESP ainda não se comprometeu com o modelo operacional AI-native.

## As 3 lanes

| Lane | Duração | Basis | Confiança |
|---|---|---|---|
| **Traditional** (âncora) | **16-31 semanas** | Derivada do formato do engagement (benchmark top-down), sem compressão | Assumed |
| **Augmented** (metodologia tradicional + tooling de IA) | **14-25 semanas** | Faixa traditional comprimida por `efficiency.json.realized_band` (~10-18%) | Assumed |
| **AI-native** (condicional) | **10-19 semanas** | Faixa traditional comprimida por `efficiency.json.native_band` (~35-40%) — gate de qualificação ainda não atendido | Assumed |

Faixa traditional re-derivada nesta revisão pelo resize E01 M→L (canal de telefonia via CTI) / E05 L→S (Appointment Assistant nativo substituindo o site guest customizado) — ver `data/roadmap.json` e `.project-metadata.json.timeline.derived`.

**Delta traditional → augmented**: ~2-6 semanas mais rápido, mesma equipe, tooling de IA sobre o modelo operacional inalterado.

**Delta traditional → AI-native**: ~6-12 semanas mais rápido, **mas condicional** a um compromisso operacional (decisão diária, product owner nomeado e disponível, mandato AI-first) que o DER/PRODESP ainda não assumiu. Hoje é um motivador — "se você se comprometer com este modelo de trabalho, esta seria a faixa" — nunca uma entrega alcançável sem nomear o compromisso.

## Gate de qualificação AI-native: condicional

Confirmado pelo usuário: nenhum sponsor executivo nomeado identificado na discovery (Discovery Brief item #12); cadeia de decisão em 3 camadas DER→PRODESP→Stefanini; nenhum mandato AI-first declarado. O roster client-side desta lane (Product Owner/Decision-maker) reflete exatamente esse gap — ainda não está preenchido. Este é o sinal, não o número, que mantém a lane rotulada condicional.

## Roster nomeado

### Traditional & Augmented (mesma forma de equipe)

A ferramenta de IA muda o ritmo de entrega dentro dos mesmos papéis e contagens na lane augmented — não a composição do time. Roster completo em `data/resource-plan.json` (16 papéis).

| Papel | Senioridade | Local | Qtd | Alocação | Fases | Lado |
|---|---|---|---|---|---|---|
| Project/Program Manager | Sênior | Onshore | 1 | Full | 0-4 | PS |
| Solution Architect | Sênior | Onshore | 1 | Full | 0-4 | PS |
| Technical Architect | Sênior | Onshore | 1 | Full | 1-4 | PS |
| Functional Consultant (config crítica) | Sênior | Onshore | 1 | Full | 0-2 | PS |
| Functional Consultant (volume) | Regular | Offshore | 1 | Full | 1-4 | PS |
| Developer (caminho crítico) | Sênior | Onshore | 1 | Full | 1-3 | PS |
| Developer (pod de build — E01/E02/E03/E04) | Regular | Offshore | 3 | Full | 1-4 | PS |
| Quality Assurance (estratégia/auditoria) | Sênior | Onshore | 1 | Full | 1-4 | PS |
| Quality Assurance (execução) | Regular | Offshore | 2 | Full | 2-4 | PS |
| Change & Adoption | Regular | Onshore | 1 | Full | 3-4 | PS |
| Product Owner/Decision-maker | Regular | Onshore | 1 | Half | 0-4 | Cliente |
| Functional Consultant (SME C2C) | Regular | Onshore | 1 | Quarter | 1-2 | Cliente |
| Functional Consultant (SME UBA) | Regular | Onshore | 1 | Quarter | 2-3 | Cliente |
| Change & Adoption (Data Steward) | Regular | Onshore | 1 | Quarter | 1,4 | Cliente |
| Technical Architect (IT liaison) | Regular | Onshore | 1 | Quarter | 0-1 | Cliente |
| Quality Assurance (amostra UAT) | Regular | Onshore | 1 | Quarter | 4 | Cliente |

### AI-native (piso de accountability core + 5 ajustes de delta)

Piso presente: Program Lead ✓, Intent Architect ✓, Agent Orchestrator ✓ (Technical Architect — escolhido pela complexidade de governança/auditoria estadual), Adoption Architect ✓ (ganho pelo escopo real de G0515). Nenhuma accountability core ausente.

| Papel (rótulo AI-native) | Senioridade | Local | Qtd | Alocação | Fases | Lado |
|---|---|---|---|---|---|---|
| Program Lead | Sênior | Onshore | 1 | Full | 0-4 | PS |
| Intent Architect | Sênior | Onshore | 1 | Full | 0-4 | PS |
| Agent Orchestrator | Sênior | Onshore | 1 | Full | 1-4 | PS |
| Adoption Architect | Regular | Onshore | 1 | Full | 3-4 | PS |
| Logic & Integration Engineer | Sênior | Onshore | 1 | Full | 1-4 | PS |
| Functional Consultant (agent-assisted) | Regular | Offshore | 1 | Half | 1-2 | PS |
| Logic Validator | Sênior | Onshore | 1 | Full | 1-4 | PS |
| Logic Validator (surge) | Regular | Offshore | 1 | Full | 4 | PS |
| Product Owner/Decision-maker | Regular | Onshore | 1 | Half | 0-4 | Cliente |
| Functional Consultant (SME C2C) | Regular | Onshore | 1 | Quarter | 1-2 | Cliente |
| Functional Consultant (SME UBA) | Regular | Onshore | 1 | Quarter | 2-3 | Cliente |
| Change & Adoption (Data Steward) | Regular | Onshore | 1 | Quarter | 1,4 | Cliente |
| Technical Architect (IT liaison) | Regular | Onshore | 1 | Quarter | 0-1 | Cliente |
| Quality Assurance (amostra UAT) | Regular | Onshore | 1 | Quarter | 4 | Cliente |

**O que muda vs. traditional/augmented**: o pod de 3 Developers offshore colapsa para 1 senior dirigindo agentes (volume → agentes, não corpos); QA permanece amplificada por agentes, nunca substituída, com surge na Fase 4; sequenciamento multiplica a cobertura sênior (mesmo número de "cabeças core", mais escopo coberto por cada uma).

## Leitura de equipe (sem FTE numérico)

Não há `user_commitment` de semanas — apenas a faixa derivada (16-31 semanas) — e `derive-hours.py` corretamente se recusa a derivar horas/FTE de uma faixa, só de um compromisso. Inventar um número aqui violaria a mesma regra.

Leitura qualitativa aprovada pelo Solution Lead: lane traditional/augmented soma **10 papéis PS** (pico de ~7-8 pessoas simultâneas nas Fases 1-3, incluindo o pod de 3 Developers offshore) + **6 papéis client-side**. Lane AI-native cai para **8 papéis PS** (pico de ~5-6 pessoas) com o pod de Developers colapsado de 3 para 1 sênior amplificado por agentes. Um FTE numérico real fica disponível se/quando o DER/PRODESP comprometer um número de semanas (`roadmap` Step 0.6).

## Approved Commercials

Rates fornecidas e validadas pelo usuário em 2026-09-17, a partir da tabela oficial de rates PS LATAM (não específica deste projeto — reaproveitada por decisão explícita do usuário). Valores COM imposto (sem imposto ÷ 0,9345). Moeda: **BRL** (assumida a partir da tabela de origem e do fato de o cliente ser uma entidade estadual paulista — não confirmada em USD).

**Rates aplicadas (R$/hora, com imposto):**

| Bucket | Cobre | Rate/h |
|---|---|---|
| Architect-class sênior onshore | PM, Solution Architect, Technical Architect · Program Lead, Intent Architect, Agent Orchestrator (AI-native) | R$ 946,69 |
| Entrega sênior onshore, ou qualquer papel offshore regular | Functional Consultant/Developer/QA sênior onshore · Functional Consultant/Developer/QA regular offshore · Logic & Integration Engineer, Logic Validator (AI-native) | R$ 715,66 |
| Change & Adoption regular onshore | Change & Adoption · Adoption Architect (AI-native) | R$ 614,21 |

**Faixa indicativa de preço por lane** (Σ(count × alocação × rate) × 40h × faixa de duração da própria lane — faixa "honestamente larga", sem descontar por `phases_active`):

| Lane | Duração | Faixa indicativa (BRL) |
|---|---|---|
| **Traditional** (âncora) | 16-31 semanas | **R$ 6.332.940,80 – R$ 12.270.072,80** |
| **Augmented** | 14-25 semanas | **R$ 5.541.323,20 – R$ 9.895.220,00** |
| **AI-native** (condicional) | 10-19 semanas | **R$ 2.383.636,00 – R$ 4.528.908,40** |

> *Esta faixa é baseada nas rates de R$946,69/h (architect-class sênior onshore), R$715,66/h (entrega sênior onshore/qualquer offshore regular) e R$614,21/h (change & adoption regular onshore) que você forneceu e validou em 2026-09-17. Indicativo para planejamento apenas; a estrutura comercial final é confirmada através do acordo comercial aplicável.*

A faixa AI-native permanece condicional ao gate de qualificação (nenhum sponsor executivo nomeado, mandato AI-first ainda não assumido) — é um motivador ("se você se comprometer com este modelo de trabalho, esta seria a faixa de investimento"), nunca uma entrega comprometida sem nomear o compromisso.

Este é um preço **indicativo**, não custo/margem, e não uma proposta de fixed fee — o número que sai daqui é o que o cliente é cobrado (bill rate), nunca o que a entrega custa internamente.

---
*Esta comparação é benchmark-based, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Faixas de duração e a faixa AI-native carregam a incerteza herdada de `confidence: Assumed` em todos os 5 épicos.*
