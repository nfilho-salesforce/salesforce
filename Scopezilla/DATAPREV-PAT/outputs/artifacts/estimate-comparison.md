# Estimativa Dual-Track — Marketplace Digital do PAT (DATAPREV-PAT)

> Comparação traditional vs. **AI-native** sobre uma base de escopo única e validada. **Âncora: AI-native** — é o número comprometido; a trilha tradicional é um *gross-up notional* ("o que custaria do jeito antigo"). Assinado pelo Solution Lead em 28/07/2026 como ponto de partida defensável — os números finais são refinados e confirmados no acordo comercial.

## So What

- **AI-native (comprometido):** **17 semanas (13 de build + 4 de Scale/Hypercare)** · ~**9,4 FTE** média no build (pico de 13 pessoas) · preço indicativo em **Approved Commercials**.
- **Tradicional (gross-up notional):** ~**18–38 semanas** · ~**10,6 FTE** média-programa (pico ~16 pessoas) · preço indicativo em **Approved Commercials**.
- **Delta:** o modelo AI-native remove ~**42%** do gross-up notional — ~⅔ por duração comprimida, ~⅓ por volume de build absorvido por agentes.
- **Risco #1:** a âncora AI-native repousa em uma banda de eficiência **condicional/provisória** com prontidão do cliente **Low (2/8)**. Compromisso do Solution Lead; a tensão é real e está registrada abaixo.

## Base compartilhada (validada uma vez)

- **9 épicas** · distribuição de complexidade **2 XL · 4 L · 3 M** · confiança **Assumed** em todos os 9 sizes (atrás dos 3 blockers de arquitetura: org Salesforce 100% greenfield — ADR 0002; seleção de gateway — ADR 0003/G0309; acessos/ambientes/capacidade na instalação MuleSoft on-premise existente — ADR 0006).
- **Ownership:** Salesforce PS entrega as 9 épicas (build completo); **Dataprev** é dona da origem dos dados sensíveis e da tokenização (ADR 0001). *(Confirmado pelo usuário.)*
- **Range-drivers** (os 2–3 épicos que fixam o teto): **E05** (hub de integração, sem contratos de API — risco #1), **E03** (financeiro: split/conciliação), **E08** (fronteira de residência não ratificada).

## Trilha AI-native — ÂNCORA (número comprometido)

- **Duração:** **17 semanas comprometidas = 13 de build (Fase 1, S1-S13, go-live 15/nov/2026) + 4 de Scale/Hypercare (S14-S17, 16/nov–13/dez/2026)**. *A faixa 11–27 sem é a derivação benchmark independente (baseline 18–38 sem comprimida pela `native_band` da eficiência, ~28–38%, condicional/provisória — decisions/0033); as 13 semanas de build caem no extremo inferior dessa faixa.*
- **Time:** ~**9,4 FTE média** no build (pico de **13 pessoas** distintas no meio do build); Scale/Hypercare reusa perfis do build em fração.
- **Qualificação:** o Solution Lead atesta que o cliente qualifica para o modelo operacional AI-native.

> **Duração** — *Este número é baseado em benchmark, derivado dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Trilha Tradicional — gross-up notional

- **Duração:** ~**18–38 semanas** (gross-up notional a partir da AI-native comprometida, `native_band` invertida; coincide com a baseline benchmark top-down-shape). NÃO alcança a data fixa de 15/nov/2026 em nenhum ponto da faixa.
- **Time:** ~**10,6 FTE média-programa** (pico ~16 pessoas; pod de build offshore que escala com volume + oversight sênior onshore).

> **Duração** — *Este número é baseado em benchmark, derivado dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Roster (mesmas funções nas duas trilhas; a magnitude difere)

Uma linha por pessoa. `phases_active` = time-box (não fração); `allocation` = fração enquanto ativo. Rates sem imposto (tabela Dataprev validada).

| Função (tabela Dataprev) | Sen. | Local | Trad. | AI-nat. | Rate/h (s/imp) |
|---|---|---|---|---|---|
| Senior Solution Architect | sênior | onshore | 1 | 1 | 884,68 |
| Senior Technical Architect | sênior | onshore | 1 | 1 | 884,68 |
| MuleSoft Technical Architect (NOVO — reuso on-premise, ADR 0006) | sênior | onshore | 1 | 1 | 884,68 |
| Senior Project Manager (absorve accountability do Engagement Manager, removido) | sênior | onshore | 1 | 1 | 884,68 |
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

1. **Duração comprimida** (~⅔ do delta) — 18–38 sem notional → 13 sem de build comprometidas via `native_band`. Menos semanas-programa × FTE é o maior componente.
2. **Volume de build absorvido por agentes** (~⅓) — pod Core 3→2, MuleSoft 2→1 (10,6→9,4 FTE média no build). Núcleo sênior mantido (+ nova frente MuleSoft contínua com Arquiteto Técnico dedicado); QA mantido e com surge; especialistas fracionais inalterados.
3. **Mix de rate** (contra-pressão pequena) — AI-native pende levemente mais sênior (blended ~2% acima, sem imposto), porque saem assentos offshore baratos de build. O ganho de duração+volume domina.

**Resultado:** ~**42%** de redução no midpoint (ver as cifras indicativas em **Approved Commercials**).

## Approved Commercials

Preço indicativo por trilha, derivado da tabela de rates da Dataprev que você forneceu e validou. AI-native é um **ponto comprometido** (roster nomeado × janela fixa); Tradicional segue **faixa notional**: **Σ(FTE-efetiva do papel × rate sem imposto) × semanas × 40**, com FTE-efetiva = count × allocation × fração-de-fase-ativa. **Com imposto = sem imposto ÷ 0,9345.**

| Trilha | Horas | Sem imposto | **Com imposto** | Duração | FTE média |
|---|---:|---|---|---|---|
| **AI-native — Build (âncora)** | 4.880h | R$ 3.679.104,40 | **R$ 3.936.976,35** | 13 sem | ~9,4 |
| **AI-native — Scale/Hypercare** | 240h | R$ 177.779,20 | **R$ 190.239,91** | 4 sem | fracional |
| **AI-native — TOTAL PROGRAMA** | 5.120h | **R$ 3.856.883,60** | **R$ 4.127.216,27** | 17 sem | — |
| Tradicional (notional, escopo completo) | 7.420–15.670h | R$ 5,44M – 11,48M | **R$ 5,8M – 12,3M** | 18–38 sem | ~10,6 |

> *Valores são indicativos e apenas para discussão de planejamento. Estimativas finais, modelo de esforço e estrutura comercial serão confirmados por meio do acordo comercial aplicável. Viagens e despesas são faturadas conforme incorridas e não estão incluídas nas estimativas.*

> *Esta faixa é baseada na tabela de rates da Dataprev que você forneceu e validou em 28/07/2026. Indicativa apenas para planejamento; a estrutura comercial final é confirmada por meio do acordo comercial aplicável.*

## Nota de honestidade sobre o roster e a âncora

Estes números são um **ponto de partida defensável para o Solution Lead refinar**, não um compromisso de staffing nem um preço fechado. As contagens do roster são *ganhas* — cada linha carrega a justificativa de por que aquele papel, aquantos, e em quais fases — mas todos os 9 sizes seguem **Assumed** atrás dos três blockers de arquitetura (org Salesforce 100% greenfield — ADR 0002; seleção de gateway — ADR 0003/G0309; acessos/ambientes/capacidade na instalação MuleSoft on-premise existente — ADR 0006), então as duas faixas são largas por construção e apertam conforme esses blockers se resolvem. **A âncora AI-native é a tensão material:** o número comprometido usa uma banda de compressão que a análise de eficiência marcou **condicional e provisória**, enquanto a prontidão de IA medida do cliente é **Low (2/8)** — gates TCU/CGU/ANPD, ADI/STF e os blockers de arquitetura ainda em aberto apontam para a postura *oposta* à do modelo operacional AI-native. Comprometer-se com a faixa AI-native é comprometer-se com o cliente adotar um modo de trabalho que ele não exibe hoje; essa é a decisão que o Solution Lead possui. Por fim, a função **Change & Adoção** não tem correspondente exato na tabela de rates da Dataprev e foi mapeada à role **Solution Consultant** (rate na tabela validada) — a confirmar.
