# ARI Vivo — Estimativa de Projeto (ciclo completo Salesforce PS)

**Projeto:** ARI Vivo · Atendimento B2C
**Gerado em:** 2026-08-25
**Escopo da estimativa:** ciclo completo da metodologia Salesforce Professional Services — Prepare & Design → Build/Delivery → SIT → UAT → Deploy → Scale/Hypercare — construído sobre o ROM de Build revalidado.
**Status:** estimativa completa, **preço diferido** (nenhuma taxa validada em arquivo — o produto entregue é tempo, esforço e roster; o preço é a última camada, produzida via `commercials` com taxa validada).

---

## 1. Como ler esta estimativa

Esta é uma estimativa **de duas trilhas** sobre uma **única base de escopo**:

- **Trilha AI-native (âncora comprometida)** — o número dimensionado a partir do escopo, no modelo de entrega AI-native. É a trilha de referência.
- **Trilha Tradicional (notional)** — quanto o mesmo escopo custaria no modelo de entrega tradicional. É ilustrativa (gross-up), não derivada de forma independente.

**Duas premissas de método governam tudo abaixo:**

1. **O ROM ingerido cobre APENAS a fase de Build/Delivery.** Prepare & Design, SIT, UAT, Deploy, Scale/Hypercare e governança de programa são **aditivos** — o ROM os exclui explicitamente (premissa 16 do ROM). Referência: ADR `decisions/0001`.
2. **Sem teto de valor.** O dimensionamento é 100% orientado pelo escopo (ROM + ciclo PS completo). Nenhum valor externo foi usado como alvo ou limite.

---

## 2. Esforço por cenário — Trilha AI-native

| Cenário | Horas produtivas (6h/dia) | Horas contratadas (÷ 0,75) |
|---|---:|---:|
| Otimista | 20.485 | 27.313 |
| **Central (base)** | **32.379** | **43.172** |
| Pessimista | 49.230 | 65.639 |

- **Horas produtivas** = tempo efetivo de trabalho a 6h/dia útil (base do ROM).
- **Horas contratadas** = produtivas ÷ 0,75 (jornada de 8h — inclui cerimônias, overhead e tempo não-produtivo).

**Duração (cenário central):** ~40 semanas (~9,5 meses).
**Equipe (FTE médio de programa):** ~27 pessoas, com pico maior no meio do Build e cauda mais leve em UAT/Deploy/Scale.

---

## 3. Esforço por fase — cenário central (horas produtivas)

| Fase | Horas | Base / fator | Conteúdo |
|---|---:|---|---|
| **Prepare & Design (P&D)** | 2.940 | 15% do Build | Refino de histórias + Sprint 0 + captura de baseline de TMA/FCR e plano de medição + trilha *right-sized* de experience/service/conversation design nas superfícies de alto impacto (console do agente, fluxos conversacionais, entrevista CPM-04 de 300 passos) |
| **Build / Delivery** | 19.600 | supplied (ROM) | 17.040 de build (5 squads) + 2.556 de QA/transversal (+15%). SIT embutido no ajuste de teste (+12,5%) do ROM |
| **UAT** | 1.568 | 8% do Build | Ciclos de aceitação de negócio, correção de defeitos, sign-off |
| **Deploy** | 1.372 | 7% do Build | Cutover, release, go-live coordenado com dependências de infra (SCV/Amazon Connect) |
| **Scale / Hypercare** | 1.960 | 10% do Build | Estabilização pós-go-live, hypercare, adoção |
| **Governança / PM (overlay)** | 4.939 | 18% overlay | Gestão de programa/entrega, Scrum Masters, PMO — excluídos do ROM (premissa 16), adicionados aqui |
| **Total** | **32.379** | | |

*Nota:* P&D não é um discovery greenfield. A premissa é que épicos e o plano técnico já existem (o ROM e seu mapa de histórias). P&D é, portanto, refino + Sprint 0 mais duas atividades aditivas que são o **mecanismo** do resultado ARI, não decoração: (a) baseline de TMA/FCR auditável; (b) design *right-sized* das superfícies de alto impacto.

---

## 4. Matriz Papel × Fase — cenário central

Horas produtivas (base 6h/dia). Contratadas = produtivas ÷ 0,75. Trilha AI-native.

| Papel | P&D | Build | UAT | Deploy | Scale | Gov | Produtivas | Contratadas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Program/Delivery Lead | — | — | — | — | 160 | 2.000 | 2.160 | 2.880 |
| Solution Architect (programa) | 500 | — | 168 | 100 | — | — | 768 | 1.024 |
| Technical Architect / Agent Orchestrator | 400 | — | — | 300 | 200 | — | 900 | 1.200 |
| Engenharia de Build (5 squads, ROM) | — | 17.040 | 600 | 272 | 1.100 | — | 19.012 | 25.349 |
| QA / Test Automation | — | 2.556 | 700 | — | — | — | 3.256 | 4.341 |
| Experience/Service/Conversation Designer | 1.100 | — | — | — | — | — | 1.100 | 1.467 |
| Analista de Baseline TMA/FCR (BI) | 540 | — | — | — | — | — | 540 | 720 |
| Release / DevOps Engineer | — | — | — | 700 | — | — | 700 | 933 |
| Adoption / Change Architect | 400 | — | 100 | — | 500 | — | 1.000 | 1.333 |
| Scrum Masters + PMO | — | — | — | — | — | 2.939 | 2.939 | 3.919 |
| **Total** | **2.940** | **19.596** | **1.568** | **1.372** | **1.960** | **4.939** | **32.375** | **43.167** |

*As diferenças de arredondamento (32.375 vs 32.379 produtivas) são de arredondamento de linha; não são materiais.*

---

## 5. Roster comprometido — Trilha AI-native

**Lado Salesforce PS.** Os squads de Build seguem o ROM (§5): 5 squads / 27 pessoas na janela de Build. As demais são funções de overlay que o ROM não cobre.

| Função | Senioridade | Local | Qtd | Fases ativas | Alocação |
|---|---|---|---:|---|---|
| Program/Delivery Lead | senior | onshore | 1 | P&D→Scale | full |
| Solution Architect (programa) | senior | onshore | 1 | P&D, UAT, Deploy | meia |
| Technical Architect / Agent Orchestrator | senior | onshore | 1 | P&D, Deploy, Scale | meia |
| Squad 1 — Foundation & Ops | regular | offshore | 5 | Build | full |
| Squad 2 — Interaction/Relationship/Capture (caminho crítico) | regular | offshore | 6 | Build | full |
| Squad 3 — Problem & Guided Flows | regular | offshore | 5 | Build | full |
| Squad 4 — Channels & Agentforce | regular | offshore | 6 | Build | full |
| Squad 5 — Integration/Core (**condicional**) | senior | onshore | 5 | Build | full |
| QA / Test Automation | senior | offshore | 2 | Build, UAT | full |
| Experience/Service/Conversation Designer | senior | onshore | 1 | P&D | full |
| Analista de Baseline TMA/FCR (BI) | regular | offshore | 1 | P&D | meia |
| Release / DevOps Engineer | senior | offshore | 1 | Deploy | full |
| Adoption / Change Architect | senior | onshore | 1 | P&D, UAT, Scale | quarto |
| Scrum Masters | regular | offshore | 3 | Build, UAT | full |

**Lado Cliente (prerequisitos de prontidão — a qualificação AI-native depende deles).**

| Função | Qtd | Fases ativas | Por que é load-bearing |
|---|---:|---|---|
| Product Owner / Decisor de Negócio | 1 | P&D→Scale | Decisor disponível diariamente e empoderado — porta da qualificação AI-native |
| Business Owners / SMEs de Contact-Center | 3 | P&D, Build, UAT | Donos empoderados por domínio para refino e aceitação |
| Time MuleSoft / Dono do contrato de facades | 1 | P&D, Build | Dono do contrato dos 17 facades (G1004/G1005); se net-new, é programa fora-de-banda do cliente |
| Dono de Telefonia / AWS Connect | 1 | P&D, Build, Deploy | Tenant Amazon Connect + migração Genesys→Connect (EOL Dez-2027); bloqueia voz OMNI se não pronto |

---

## 6. Trilha Tradicional (notional)

Gross-up da trilha AI-native comprometida, aplicando a banda-padrão de compressão AI-native de 35–40% de forma invertida (÷ 0,60 a ÷ 0,65) sobre as horas contratadas.

| Cenário | Horas contratadas (tradicional, notional) |
|---|---:|
| Otimista | 42.020 – 45.522 |
| **Central** | **66.419 – 71.954** |
| Pessimista | 100.984 – 109.399 |

**Isto é ilustrativo** ("quanto custaria do modo tradicional"). Não há `efficiency.json` com banda fundamentada neste projeto — a banda de 35–40% é o padrão AI-native. Para uma banda de compressão fundamentada neste engajamento específico, rodar o skill `efficiency`.

---

## 7. Qualificação da trilha AI-native

A trilha AI-native comprometida é **condicional** a três compromissos. Sem eles, ela permanece um motivador dimensionado por escopo, não um número atingível:

1. **Modelo operacional conjunto** — decisor disponível diariamente, business owners empoderados, mandato AI-first.
2. **Inventário de facades MuleSoft (G1004)** — quais dos 17 facades existem em produção vs. precisam ser construídos. Fixa o piso do domínio de Integração.
3. **Contagem de usuários (OMNI-28)** — agentes B2C + ~18k parceiros Aliado (Experience Cloud).

---

## 8. Sinalizadores e riscos

- 🔴 **Piso de Integração (INT) é condicional** ao inventário de facades MuleSoft (G1004). Facade net-new = trabalho de programa **fora-de-banda**, NÃO coberto pela contingência de 50% do domínio INT. É o **deliverable #1 da Fase 0**. Não foi retro-embutido na contingência.
- 🔴 **Dependências de infra** — o subdomínio de voz OMNI depende de SCV + Amazon Connect provisionados e da migração Genesys→Connect (EOL Dez-2027). É prerequisito de infra **fora** do build Salesforce (G0802). Bloqueia ~40% das histórias OMNI se não estiver pronto.
- 🔴 **Fase 0 fortemente recomendada** — 72 gaps + 14 conflitos de fonte. Inventário de facades (G1004) é o deliverable #1.
- 🟡 **Contagem de usuários assumida** — faixa de agentes B2C + ~18k Aliado (OMNI-28). G0801 aponta subdecomposição do Aliado (licenciamento/sharing/onboarding). Confirmar na Fase 0.

---

## 9. Disclaimers

*Esta figura é baseada em benchmark, derivada de dados de treinamento do modelo de IA e padrões gerais de entrega (não validados pela Salesforce) — não é um compromisso. Os números finais são confirmados através do acordo comercial aplicável.* (Aplica-se às faixas de duração e às formas derivadas top-down.)

**Sem preço:** nenhuma taxa validada consta em arquivo neste projeto. Esta estimativa é de tempo, esforço e roster. O preço é a última camada — produzido via `commercials`, a partir de uma taxa que o usuário fornece e valida, carregando o disclaimer de taxa validada.

*Valores são indicativos e apenas para discussão de planejamento. Estimativas finais, modelo de esforço e estrutura comercial serão confirmados através do acordo comercial aplicável. Viagens e despesas são faturadas conforme incorridas e não estão incluídas nas estimativas.*
