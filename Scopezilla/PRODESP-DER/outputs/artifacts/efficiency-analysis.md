# AI Delivery Efficiency Analysis — PRODESP - DER

## So What

**~6-13% realized delivery efficiency at Low readiness.** A pace and quality lift within the same team shape — not headcount reduction, not a pricing input.

Where the gains show up on this project:
- **Technical Engineering & QA** (~5-14%): E01-E04, todos L — integração CTI/URA, sincronização SIGOR/SIGEO, lógica de despacho e travas de negócio em LWC. Padrões técnicos ainda não fixados (CTI, SIGOR/SIGEO) limitam o ganho.
- **Analysis & Design** (~5-14%): E01, E03 — desenho de tópicos do Agentforce e regras de escalonamento cross-CGR ganham no rascunho; validação com DER/Stefanini continua humana.
- **Documentation & Knowledge Management** (~5-13%): E01, E02 — volume alto de artefatos de discovery e SOW ganha em rascunho; o aceite por marco exige revisão humana.

**Papéis que capturam mais**: Quality Assurance, Developer, Functional Consultant.

**Onde a IA não ajuda**: fechamento dos gaps bloqueadores G0305/G0309/G0524 com DER/Stefanini, treinamento presencial de 1.152 operadores — mais o maior "AI tax" do projeto, o padrão CTI/URA ainda não fixado.

**Para subir a High readiness (~9-19%)**: resolver LGPD/DPIA e a trilha de auditoria (G0305), aprovar um conjunto restrito de ferramentas de IA, fechar a especificação SIGOR/SIGEO.

## Headline

**Realizado: ~7-16%** (Low readiness) · **Blend de nível de tarefa: ~30-45%** · **Fator de realização: 0,25-0,35** — perfil regulado + legado pesado (setor público, integrações SIGOR/SIGEO sem API fechada) · **Confiança: Assumed**

## Cenários de Prontidão do Cliente

| Cenário | Banda Realizada | Notas |
|---|---|---|
| Low readiness (atual: ✓) | ~6-13% | Estado atual — ganhos modestos até a cadeia DER→PRODESP→Stefanini amadurecer e LGPD/auditoria serem resolvidos. |
| Mid readiness | ~7-16% | Faixa base se a cadência de decisão e a postura de dados melhorarem moderadamente. |
| High readiness | ~9-19% | Favorece a ponta alta se o órgão adotar cadência ágil — improvável no perfil atual, mas não descartado. |

**Cenário atual**: Low readiness (score 2/8)

### Sinais por trás da pontuação
- **AI tooling posture**: 1/2 — nenhuma menção a política de IA aprovada na discovery (Unknown, tratado como neutro).
- **Delivery velocity / speed bias**: 0/2 — cadeia DER→PRODESP→Stefanini; ciclo de contratação pública multi-camada.
- **Data & environment hygiene**: 1/2 — org Salesforce greenfield, mas SIGOR/SIGEO sem API fechada.
- **Legal / security / compliance posture**: 0/2 — sem LGPD/DPIA formal; trilha de auditoria de overrides (G0305) é gap bloqueador aberto.

### O que leva para subir
- **Low → Mid**: aprovar ferramentas de IA restritas para IDE/documentação; fechar a especificação SIGOR/SIGEO.
- **Mid → High**: adotar cadência ágil de decisão e maturidade de ambiente de dados/integração — improvável no perfil de contratação pública atual.

## Por Categoria

### Technical Engineering & QA — realizado ~5-14% (nível de tarefa ~20-40%)
- **Épicos impulsionadores**: E01 (L), E02 (L), E03 (L), E04 (L)
- **Como aparece aqui**: Densidade alta em triagem Agentforce, integração CTI/URA, sincronização SIGOR/SIGEO e travas de negócio em LWC. O ganho fica no fim do range porque três padrões técnicos ainda não estão fixados (G0524 CTI, payload SIGOR/SIGEO) — AI tax de retrabalho é real aqui per [1].

### Analysis & Design — realizado ~5-14% (nível de tarefa ~20-40%)
- **Épicos impulsionadores**: E01, E03
- **Como aparece aqui**: Desenho de tópicos/ações do Agentforce e das regras de escalonamento se beneficiam no rascunho, mas a validação de premissas de roteamento com DER/Stefanini permanece humana per [2].

### Documentation & Knowledge Management — realizado ~5-13% (nível de tarefa ~20-35%)
- **Épicos impulsionadores**: E01, E02
- **Como aparece aqui**: Volume alto de artefatos (discovery brief, SOW, especificação SIGOR/SIGEO) ganha em rascunho, mas o aceite formal por marco exige revisão humana linha a linha per [7].

### Project Management & Operations — realizado ~2-11% (nível de tarefa ~10-30%)
- **Épicos impulsionadores**: (cross-cutting, nenhum épico específico)
- **Como aparece aqui**: 6 fases de roadmap e governança a três organizações mantêm o núcleo de coordenação humano — a categoria de menor ganho per [5].

## Por Papel

### Developer — realizado ~5-14% (nível de tarefa ~20-40%)
- **Amplificado**: Create Code, Analyze Code & Fix Defects
- **Ainda só humano**: Fechamento de padrão técnico CTI (G0524) com DER/Stefanini
- **Como o dia muda**: Ganho concentrado em LWC de E04 e conectores de E01/E02, limitado pela ausência de padrão CTI fixado.

### Quality Assurance — realizado ~5-16% (nível de tarefa ~20-45%)
- **Amplificado**: Write Test Classes, QA Test Creation, Generate Test Data
- **Ainda só humano**: Validação do critério de aceite por marco com o DER
- **Como o dia muda**: Geração de dados/casos de teste para os 3 canais de entrada é o ganho mais confiável do papel.

### Functional Consultant — realizado ~5-14% (nível de tarefa ~20-40%)
- **Amplificado**: Write User Stories, Generate Documents, Knowledge Transfer
- **Ainda só humano**: Alinhamento de premissas de roteamento com o DER
- **Como o dia muda**: Rascunho de user stories e documentação ganha; revalidação de premissas permanece 100% humana.

### Solution Architect — realizado ~5-14% (nível de tarefa ~20-40%)
- **Amplificado**: Generation of Analysis Models, Analyze Code & Fix Defects
- **Ainda só humano**: Decisão de arquitetura CTI vs. Salesforce Voice (decisions/0001)
- **Como o dia muda**: Modelagem de integração ganha em rascunho; a decisão de arquitetura de voz é humana.

### Technical Architect — realizado ~5-14% (nível de tarefa ~20-40%)
- **Amplificado**: Analyze Code & Fix Defects, Create Code
- **Ainda só humano**: Governança técnica do handover à Sustentação na Fase 5
- **Como o dia muda**: Suporte à resolução dos padrões técnicos abertos é onde a IA ajuda menos.

### Project / Program Manager — realizado ~2-11% (nível de tarefa ~10-30%)
- **Amplificado**: Project Status Reports, Search & Info Retrieval
- **Ainda só humano**: Governança de escopo e relacionamento DER/PRODESP/Stefanini
- **Como o dia muda**: Relatórios de status ganham; a cadeia de decisão a três organizações é o núcleo humano.

### Change & Adoption — realizado ~3-13% (nível de tarefa ~15-35%)
- **Amplificado**: Generate Documents, Onboard Team Members
- **Ainda só humano**: Treinamento presencial de 1.152 operadores em 14 CGRs
- **Como o dia muda**: Material de treinamento ganha em rascunho; adoção efetiva depende de capacitação presencial.

## Trabalho Exclusivamente Humano
- **Project Pulse Reports** — trabalho de construção de confiança que a IA pode resumir, não facilitar.
- **Stakeholder Alignment** — negociação humano-a-humano; a IA rascunha posições, pessoas decidem.
- **Conflict Resolution** — julgamento humano.
- **Resolução dos gaps bloqueadores G0305/G0309/G0524 com DER/Stefanini** — decisões de arquitetura e governança sob incerteza regulatória/contratual.

## Premissas e Ressalvas
- Ganhos de nível de tarefa vêm de estudos publicados 2022-2026; um fator de realização (por formato do projeto, de `efficiency-model.json`) contabiliza a lei de Amdahl, a sobrecarga de revisão/AI-tax e o trabalho humano não movido.
- **Range honesto para codificação**: evidência de RCT vai de -19% (METR 2025 [1], OSS maduro) a +21% (Paradis/Google 2024 [4], enterprise complexo) a +55% (Peng/GitHub 2022 [3], greenfield lab). A linha enterprise-legado é o ponto de partida defensável para integração Salesforce e desenvolvimento custom.
- Ganhos individuais ≠ ganhos de equipe: DORA 2024 [5] mediu produtividade individual subindo enquanto estabilidade e throughput de entrega caíam. Ancorar afirmações em resultados de nível de projeto, não em autorrelato.
- A capacidade do modelo está avançando mais rápido que os ganhos de fluxo de trabalho realizados (Stanford HAI 2026 [9]); esse gap é por que as bandas de nível de projeto ficam em ~10-25%.
- Bandas são qualitativas e específicas do projeto — nenhuma implicação de horas, FTE ou custo é computada ou implícita.

## Fontes
1. METR (julho 2025) — RCT de devs experientes de OSS; mediu ~19% de lentidão apesar de ~20% de aceleração percebida.
2. BCG × Harvard (2023, pilotos 2025) — 12,2-40% de economia de tempo em tarefas no escopo; "jagged frontier" degrada fora dele.
3. Peng et al., GitHub (2022) — RCT em lab, 95 devs em tarefa greenfield de servidor HTTP; ~55% mais rápido, IC 95% [21%, 89%].
4. Paradis et al., Google (arXiv 2410.12944, 2024) — RCT de 96 engenheiros do Google em tarefa enterprise complexa; ~21% de redução de tempo com IC amplo. Contrapeso de [1].
5. DORA 2024 State of DevOps — primeira medição rigorosa de nível de equipe de que ganhos individuais de IA coexistem com queda de estabilidade e throughput de entrega.
6. DORA 2025 — IA como "amplificador" de sistemas sociotécnicos existentes; qualitativo, suplemento a [5].
7. McKinsey State of AI (2025) — ganhos de 10-30% em nível de função; ranges amplamente inalterados desde 2024.
8. GitClear AI Code Quality (atualização 2025, 211M LOC, 2020-2024) — clonagem 8,3%→12,3%, refatoração 25% (2021)→<10% (2024).
9. Stanford HAI AI Index (abril 2026) — SWE-bench Verified subiu de 60% para quase 100% do baseline humano em um ano; adoção organizacional de 88%; gap de 50 pontos entre especialistas e público sobre o impacto da IA no trabalho.
10. Salesforce Agentforce pilotos internos (2024-2025, públicos).
11. Scopezilla observações internas (2025-2026).
