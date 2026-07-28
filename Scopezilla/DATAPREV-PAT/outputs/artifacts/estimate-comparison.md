# Estimativa Dual-Track — Marketplace Digital do PAT (DATAPREV-PAT)

> Comparação traditional vs. **AI-native** sobre uma base de escopo única e validada. **Âncora: AI-native** — é o número comprometido; a trilha tradicional é um *gross-up notional* ("o que custaria do jeito antigo"). Assinado pelo Solution Lead em 28/07/2026 como ponto de partida defensável — os números finais são refinados e confirmados no acordo comercial.

## So What

- **AI-native (comprometido):** ~**11–27 semanas** · ~**8,6 FTE** média-programa · preço indicativo em **Approved Commercials**.
- **Tradicional (gross-up notional):** ~**18–38 semanas** · ~**10,3 FTE** média-programa · preço indicativo em **Approved Commercials**.
- **Delta:** o modelo AI-native remove ~**42%** do gross-up notional — ~⅔ por duração comprimida, ~⅓ por volume de build absorvido por agentes.
- **Risco #1:** a âncora AI-native repousa em uma banda de eficiência **condicional/provisória** com prontidão do cliente **Low (2/8)**. Compromisso do Solution Lead; a tensão é real e está registrada abaixo.

## Base compartilhada (validada uma vez)

- **9 épicas** · distribuição de complexidade **2 XL · 4 L · 3 M** · confiança **Assumed** em todos os 9 sizes (atrás dos 4 blockers de arquitetura; a Fase 0 aperta as faixas).
- **Ownership:** Salesforce PS entrega as 9 épicas (build completo); **Dataprev** é dona da origem dos dados sensíveis e da tokenização (ADR 0001). *(Confirmado pelo usuário.)*
- **Range-drivers** (os 2–3 épicos que fixam o teto): **E05** (hub de integração, sem contratos de API — risco #1), **E03** (financeiro: split/conciliação), **E08** (fronteira de residência não ratificada).

## Trilha AI-native — ÂNCORA (número comprometido)

- **Duração:** ~**11–27 semanas**. *Baseline benchmark 18–38 sem comprimida pela `native_band` da eficiência (~28–38%, condicional/provisória — decisions/0033).*
- **Time:** ~**8,6 FTE média-programa** (pico ~13 pessoas distintas no meio do build).
- **Qualificação:** o Solution Lead atesta que o cliente qualifica para o modelo operacional AI-native.

> **Duração** — *Este número é baseado em benchmark, derivado dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Trilha Tradicional — gross-up notional

- **Duração:** ~**18–38 semanas** (gross-up notional a partir da AI-native comprometida, `native_band` invertida; coincide com a baseline benchmark top-down-shape).
- **Time:** ~**10,3 FTE média-programa** (pico ~15 pessoas; pod de build offshore que escala com volume + oversight sênior onshore).

> **Duração** — *Este número é baseado em benchmark, derivado dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Roster (mesmas funções nas duas trilhas; a magnitude difere)

Uma linha por pessoa. `phases_active` = time-box (não fração); `allocation` = fração enquanto ativo. Rates sem imposto (tabela Dataprev validada).

| Função (tabela Dataprev) | Sen. | Local | Trad. | AI-nat. | Rate/h (s/imp) |
|---|---|---|---|---|---|
| Engagement Manager | sênior | onshore | 1 | 1 | 884,68 |
| Senior Solution Architect | sênior | onshore | 1 | 1 | 884,68 |
| Senior Technical Architect (MuleSoft/integração) | sênior | onshore | 1 | 1 | 884,68 |
| Project Manager | regular | onshore | 1 | 1 | 789,88 |
| Developer Core/Service (pod) | regular | offshore | **3** | **2** | 668,78 |
| MuleSoft Technical Consultant | regular | offshore | **2** | **1** | 668,78 |
| Experience Architect | regular | offshore | 1 | 1 | 789,88 |
| Quality Assurance Consultant | regular | offshore | 2 | 2 | 573,98 |
| Technical Consultant — Agentforce (½) | sênior | offshore | 1 | 1 | 668,78 |
| Change & Adoção → Solution Consultant (½) ⚠︎ | regular | onshore | 1 | 1 | 573,98 |
| Technical Consultant — Data Migration (½) | regular | offshore | 1 | 1 | 668,78 |

**As 5 alavancas AI-native aplicadas:** (1) volume→agentes: pod Core 3→2, MuleSoft 2→1, builders remanescentes no caminho crítico; (2) QA **amplificado, não substituído** — mantido em 2 com surge no hardening financeiro regulado; (3) sequenciamento sênior mantém arquitetura full-time; (4) breadth fixa o núcleo (mantido flat); (5) especialistas fracionais (Experience/Agentforce/Change/Data) inalterados.

### Cobertura do cliente (input do gate AI-native — sem esforço/preço PS)
Product Owner/Decisor empoderado (0–4) · SMEs por épica (1–4) · Data Steward (4) · Client IT/Plataforma (1–3) · Capacidade de UAT (3–4) · Sponsor executivo (0–4). **⚠ Um Product Owner empoderado e disponível ainda não está confirmado — é precisamente o gap de prontidão que a qualificação AI-native testa.**

## Delta decomposto (o que o AI-native remove do gross-up notional)

1. **Duração comprimida** (~⅔ do delta) — 18–38 → 11–27 sem via `native_band`. Menos semanas-programa × FTE é o maior componente.
2. **Volume de build absorvido por agentes** (~⅓) — pod Core 3→2, MuleSoft 2→1 (10,3→8,6 FTE média). Núcleo sênior mantido; QA mantido e com surge; especialistas fracionais inalterados.
3. **Mix de rate** (contra-pressão pequena) — AI-native pende levemente mais sênior (blended ~2% acima, sem imposto), porque saem assentos offshore baratos de build. O ganho de duração+volume domina.

**Resultado:** ~**42%** de redução no midpoint (ver as cifras indicativas em **Approved Commercials**).

## Approved Commercials

Preço indicativo por trilha, derivado da tabela de rates da Dataprev que você forneceu e validou. Fórmula: **Σ(FTE-efetiva do papel × rate sem imposto) × semanas × 40**, com FTE-efetiva = count × allocation × fração-de-fase-ativa. **Com imposto = sem imposto ÷ 0,9345.**

| Trilha | Sem imposto | **Com imposto** | Duração | FTE média |
|---|---|---|---|---|
| **AI-native (âncora)** | R$ 2,83M – 6,94M | **R$ 3,0M – 7,4M** | 11–27 sem | ~8,6 |
| Tradicional (notional) | R$ 5,44M – 11,48M | **R$ 5,8M – 12,3M** | 18–38 sem | ~10,3 |

> *Valores são indicativos e apenas para discussão de planejamento. Estimativas finais, modelo de esforço e estrutura comercial serão confirmados por meio do acordo comercial aplicável. Viagens e despesas são faturadas conforme incorridas e não estão incluídas nas estimativas.*

> *Esta faixa é baseada na tabela de rates da Dataprev que você forneceu e validou em 28/07/2026. Indicativa apenas para planejamento; a estrutura comercial final é confirmada por meio do acordo comercial aplicável.*

## Nota de honestidade sobre o roster e a âncora

Estes números são um **ponto de partida defensável para o Solution Lead refinar**, não um compromisso de staffing nem um preço fechado. As contagens do roster são *ganhas* — cada linha carrega a justificativa de por que aquele papel, aquantos, e em quais fases — mas todos os 9 sizes seguem **Assumed** atrás dos quatro blockers de arquitetura, então as duas faixas são largas por construção e apertam com a Fase 0. **A âncora AI-native é a tensão material:** o número comprometido usa uma banda de compressão que a análise de eficiência marcou **condicional e provisória**, enquanto a prontidão de IA medida do cliente é **Low (2/8)** — gates TCU/CGU/ANPD, ADI/STF e Fase 0 travada apontam para a postura *oposta* à do modelo operacional AI-native. Comprometer-se com a faixa AI-native é comprometer-se com o cliente adotar um modo de trabalho que ele não exibe hoje; essa é a decisão que o Solution Lead possui. Por fim, a função **Change & Adoção** não tem correspondente exato na tabela de rates da Dataprev e foi mapeada à role **Solution Consultant** (rate na tabela validada) — a confirmar.
