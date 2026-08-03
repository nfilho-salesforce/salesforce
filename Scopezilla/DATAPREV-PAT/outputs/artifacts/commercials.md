# Precificação Indicativa — Marketplace Digital do PAT (DATAPREV-PAT)

**Trilha:** AI-native (trilha comprometida — Build/Fase 1 com go-live PROD em 15/nov/2026, seguido de Scale/Hypercare até 13/dez/2026)
**Base de esforço:** roster nomeado (15 linhas PS: 11 no Build + 4 no Scale/Hypercare) × janela fixa comprometida de **17 semanas (13 de build + 4 de Scale/Hypercare)** × 40h/semana, alocação-consciente
**Moeda:** BRL (R$)

Esta é uma **faixa de preço indicativa**, não um custo, uma margem, nem um preço fechado (fixed-fee). É o valor *cobrado ao cliente*, derivado dos rates que você forneceu e validou multiplicados pelo esforço top-down do roster comprometido.

---

## Approved Commercials

**Preço indicativo do Programa (trilha AI-native, janela fixa de 17 semanas — 13 de build + 4 de Scale/Hypercare):**

| Medida | Horas | Sem imposto | Com imposto (÷ 0,9345) |
|---|---:|---:|---:|
| Build (Fase 1) | **4.880 h** | **R$ 3.679.104,40** | **R$ 3.936.976,35** |
| Scale/Hypercare | **240 h** | **R$ 177.779,20** | **R$ 190.239,91** |
| **TOTAL PROGRAMA** | **5.120 h** | **R$ 3.856.883,60** | **R$ 4.127.216,27** |

*Ponto indicativo na janela fixa — não faixa. As 17 semanas são compromisso do usuário (planejamento de trás pra frente a partir do go-live de 15/nov/2026, seguido de 4 semanas de Scale/Hypercare até 13/dez/2026); o escopo é a variável de flexão, com E06/Agentforce, Data Cloud e Marketing Cloud de-escopados como buffer de cronograma. Pico de 13 pessoas no build.*

> *This range is based on the rate of the official Salesforce PS LATAM rate table (per-role, R$ 573,98–R$ 884,68/h sem imposto, mapeado por função no roster) you supplied and validated on 2026-07-31. Indicative for planning only; final commercial structure is confirmed through the applicable commercial agreement.*

> *Amounts are indicative and for planning discussion only. Final estimates, effort model, and commercial structure will be confirmed through the applicable commercial agreement. Travel and expenses billed as actual and are not included in estimates.*

---

### Base da aritmética (transparente e reproduzível)

Preço = Σ sobre as linhas do roster de (horas-por-pessoa × contagem × rate sem imposto por função). Horas-por-pessoa derivadas por `derive-hours.py` (alocação × fases ativas × semanas × 40h — meia-alocação e fase-única contam proporcionalmente, não full-time). Valor com imposto = valor sem imposto ÷ 0,9345.

**Build (Fase 1) — 4.880h:**

| Função (roster) | Horas | Rate s/ imp. (R$/h) | Rate c/ imp. (R$/h) | Subtotal s/ imp. (R$) | Subtotal c/ imp. (R$) |
|---|---:|---:|---:|---:|---:|
| Senior Solution Architect | 520 | 884,68 | 946,69 | 460.033,60 | 492.277,80 |
| Senior Technical Architect | 480 | 884,68 | 946,69 | 424.646,40 | 454.410,27 |
| MuleSoft Technical Architect (NOVO) | 300 | 884,68 | 946,69 | 265.404,00 | 284.006,42 |
| Payments/Financial Architecture Specialist ⚠ | 320 | 884,68 | 946,69 | 283.097,60 | 302.940,18 |
| Senior Project Manager | 520 | 884,68 | 946,69 | 460.033,60 | 492.277,80 |
| Developer ×2 | 1.040 | 668,78 | 715,66 | 695.531,20 | 744.281,65 |
| MuleSoft Technical Consultant | 440 | 668,78 | 715,66 | 294.263,20 | 314.888,39 |
| Experience Architect | 320 | 789,88 | 845,24 | 252.761,60 | 270.477,90 |
| Quality Assurance ×2 | 640 | 573,98 | 614,21 | 367.347,20 | 393.094,92 |
| Change & Adoption / Solution Consultant ⚠ | 260 | 573,98 | 614,21 | 149.234,80 | 159.694,81 |
| Technical Consultant (carga) | 40 | 668,78 | 715,66 | 26.751,20 | 28.626,22 |
| **SUBTOTAL BUILD** | **4.880** | | | **3.679.104,40** | **3.936.976,35** |

**Scale/Hypercare (S14-S17) — 240h, reusa perfis do build:**

| Função (roster) | Horas | Rate s/ imp. (R$/h) | Rate c/ imp. (R$/h) | Subtotal s/ imp. (R$) | Subtotal c/ imp. (R$) |
|---|---:|---:|---:|---:|---:|
| 0,5 Consultor Técnico (20h/sem) | 80 | 668,78 | 715,66 | 53.502,40 | 57.252,43 |
| 0,5 Dev MuleSoft (20h/sem) | 80 | 668,78 | 715,66 | 53.502,40 | 57.252,43 |
| Arquiteto Técnico (10h/sem) | 40 | 884,68 | 946,69 | 35.387,20 | 37.867,52 |
| Senior PM (10h/sem) | 40 | 884,68 | 946,69 | 35.387,20 | 37.867,52 |
| **SUBTOTAL SCALE** | **240** | | | **177.779,20** | **190.239,91** |
| **TOTAL PROGRAMA** | **5.120** | | | **3.856.883,60** | **4.127.216,27** |

*Rate com imposto por função = rate sem imposto da tabela oficial ÷ 0,9345 (Senior Architect/PM/MuleSoft TA 884,68→946,69; Experience Architect 789,88→845,24; Developer/Technical Consultant 668,78→715,66; QA/Solution Consultant 573,98→614,21).*

⚠ Dois papéis sem correspondente exato na tabela Dataprev, mapeados por nome mais semelhante (Payments/Financial Architecture Specialist → tier **Senior** R$ 884,68/946,69; Change & Adoption → **Solution Consultant** R$ 573,98/614,21). Taxa de conversão a confirmar com você. O Engagement Manager foi removido do roster — sua accountability foi absorvida pelo Senior Project Manager (alocação plena, tier sênior 884,68).

**Provenance dos rates:** tabela oficial Salesforce PS LATAM (sem imposto), fornecida e validada por Nelson em 2026-07-21 e reafirmada nesta precificação (2026-07-31). Também marcada `validated_by: user` em `estimate-comparison.json`.

### O que este número NÃO é

- **Não é custo nem margem** — é o valor cobrado ao cliente (bill rate), não o que a entrega custa.
- **Não é preço fechado (fixed-fee)** — é indicativo para planejamento; a estrutura comercial final é confirmada no acordo comercial aplicável.
- **Não é conversão de T-shirt sizes** — deriva do roster nomeado × janela comprometida, não de tamanhos × rate.
- Carrega os *sizes Assumed* atrás dos blockers de arquitetura: provisionamento da org Salesforce 100% greenfield (ADR 0002), seleção de gateway (ADR 0003/G0309), e acessos/ambientes/capacidade na instalação MuleSoft on-premise **existente** da Dataprev (ADR 0006 — reuso, não greenfield). Se um pré-requisito escorregar, o de-escopo (E03 primeiro) é o trilho — e o número se move com o escopo.
