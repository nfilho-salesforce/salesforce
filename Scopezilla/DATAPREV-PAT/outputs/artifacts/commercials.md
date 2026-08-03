# Precificação Indicativa — Marketplace Digital do PAT (DATAPREV-PAT)

**Trilha:** AI-native (trilha comprometida — MVP na data fixa de 15/nov/2026)
**Base de esforço:** roster nomeado (11 linhas PS) × janela fixa comprometida de **13 semanas** × 40h/semana, alocação-consciente
**Moeda:** BRL (R$)

Esta é uma **faixa de preço indicativa**, não um custo, uma margem, nem um preço fechado (fixed-fee). É o valor *cobrado ao cliente*, derivado dos rates que você forneceu e validou multiplicados pelo esforço top-down do roster comprometido.

---

## Approved Commercials

**Preço indicativo do MVP (trilha AI-native, janela fixa de 13 semanas):**

| Medida | Valor |
|---|---|
| Horas-pessoa PS | **4.620 h** |
| Sem imposto | **R$ 3.495.949,60** |
| **Com imposto** (÷ 0,9345) | **R$ 3.740.984,06** |

*Ponto indicativo na janela fixa — não faixa. As 13 semanas são compromisso do usuário (planejamento de trás pra frente a partir do go-live de 15/nov/2026); o escopo é a variável de flexão, com E06/Agentforce, Data Cloud e Marketing Cloud de-escopados como buffer de cronograma.*

> *This range is based on the rate of the official Salesforce PS LATAM rate table (per-role, R$ 573,98–R$ 884,68/h sem imposto, mapeado por função no roster) you supplied and validated on 2026-07-31. Indicative for planning only; final commercial structure is confirmed through the applicable commercial agreement.*

> *Amounts are indicative and for planning discussion only. Final estimates, effort model, and commercial structure will be confirmed through the applicable commercial agreement. Travel and expenses billed as actual and are not included in estimates.*

---

### Base da aritmética (transparente e reproduzível)

Preço = Σ sobre as linhas do roster de (horas-por-pessoa × contagem × rate sem imposto por função). Horas-por-pessoa derivadas por `derive-hours.py` (alocação × fases ativas × 13 semanas × 40h — meia-alocação e fase-única contam proporcionalmente, não full-time). Valor com imposto = valor sem imposto ÷ 0,9345.

| Função (roster) | Função tabela Dataprev | Qtd | h/pessoa | Rate s/ imp. (R$/h) | Rate c/ imp. (R$/h) | Subtotal s/ imp. (R$) | Subtotal c/ imp. (R$) |
|---|---|---:|---:|---:|---:|---:|---:|
| Project/Program Manager | Engagement Manager | 1 | 520 | 884,68 | 946,69 | 460.034 | 492.279 |
| Solution Architect | Senior Solution Architect | 1 | 520 | 884,68 | 946,69 | 460.034 | 492.279 |
| Technical Architect | Senior Technical Architect | 1 | 480 | 884,68 | 946,69 | 424.646 | 454.411 |
| Payments/Financial Architecture Specialist ⚠ | Senior Technical Architect | 1 | 300 | 884,68 | 946,69 | 265.404 | 284.007 |
| Project Manager | Project Manager | 1 | 440 | 789,88 | 845,24 | 347.547 | 371.906 |
| Developer | Developer | 2 | 440 | 668,78 | 715,66 | 588.526 | 629.781 |
| Developer (MuleSoft) | Mulesoft - Technical Consultant | 1 | 400 | 668,78 | 715,66 | 267.512 | 286.264 |
| Experience Design | Experience Architect | 1 | 280 | 789,88 | 845,24 | 221.166 | 236.667 |
| Quality Assurance | Quality Assurance Consultant | 2 | 280 | 573,98 | 614,21 | 321.429 | 343.958 |
| Change & Adoption ⚠ | Solution Consultant | 1 | 220 | 573,98 | 614,21 | 126.276 | 135.126 |
| Developer (carga mínima, Fase 4) | Technical Consultant | 1 | 20 | 668,78 | 715,66 | 13.376 | 14.313 |
| **TOTAL PS** | | | **4.620** | | | **3.495.950** | **3.740.984** |

*Subtotais com imposto arredondados por linha; o total é o valor sem imposto exato (R$ 3.495.949,60) ÷ 0,9345 = **R$ 3.740.984,06**. Rate com imposto por função = rate sem imposto da tabela oficial ÷ 0,9345 (Engagement Manager/Sr Architect 884,68→946,69; PM/Experience Architect 789,88→845,24; Developer/Technical Consultant 668,78→715,66; QA/Solution Consultant 573,98→614,21).*

⚠ Dois papéis sem correspondente exato na tabela Dataprev, mapeados por nome mais semelhante (Payments/Financial Architecture Specialist → **Senior Technical Architect** R$ 884,68/946,69; Change & Adoption → **Solution Consultant** R$ 573,98/614,21). Taxa de conversão a confirmar com você.

**Provenance dos rates:** tabela oficial Salesforce PS LATAM (sem imposto), fornecida e validada por Nelson em 2026-07-21 e reafirmada nesta precificação (2026-07-31). Também marcada `validated_by: user` em `estimate-comparison.json`.

### O que este número NÃO é

- **Não é custo nem margem** — é o valor cobrado ao cliente (bill rate), não o que a entrega custa.
- **Não é preço fechado (fixed-fee)** — é indicativo para planejamento; a estrutura comercial final é confirmada no acordo comercial aplicável.
- **Não é conversão de T-shirt sizes** — deriva do roster nomeado × janela comprometida, não de tamanhos × rate.
- Carrega os *sizes Assumed* atrás dos blockers de Fase 0 (provisionamento da org greenfield, MuleSoft on-premise, gateway PCI). Se um pré-requisito escorregar, o de-escopo (E03 primeiro) é o trilho — e o número se move com o escopo.
