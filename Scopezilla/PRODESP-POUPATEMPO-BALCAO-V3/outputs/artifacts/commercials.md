# Precificação Indicativa — PRODESP · Poupatempo Balcão (V3)

**Projeto:** PRODESP - Poupatempo Balcão V3 · **Data:** 2026-09-24 · **Lane precificado:** Aumentada (ANCHOR)

## Metodologia de Rate

Esta precificação usa o **padrão de rates PS LATAM por role** (não o grid onshore/offshore padrão da ferramenta), a pedido explícito do usuário nesta sessão. As rates são as do **contrato DATAPREV**, aplicadas por mapeamento "de/para" (nome mais semelhante) entre as roles do roster deste projeto e o vocabulário de roles PS LATAM.

**Regra de imposto (permanente):** valor **com imposto** = valor **sem imposto** ÷ 0,9345.

### De/Para — Roster → Role PS LATAM → Rate

| Roster | Role no roster | Role PS LATAM (de/para) | R$/h sem imposto | R$/h com imposto |
|---|---|---|---|---|
| R01 | Project/Program Manager (regular, onshore) | Project Manager | 789,88 | 845,24 |
| R02 | Solution Architect (senior, onshore) | Senior Solution Architect | 884,68 | 946,69 |
| R03 | Technical Architect (senior, onshore) | Senior Technical Architect | 884,68 | 946,69 |
| R04 | Developer — integração MuleSoft (senior, offshore) | Mulesoft-TC / Developer | 668,78 | 715,66 |
| R05 | Developer (regular, offshore) | Developer | 668,78 | 715,66 |
| R06 | Developer — Slack (regular, offshore) | Developer | 668,78 | 715,66 |
| R07 | Quality Assurance (regular, offshore) | Quality Assurance Consultant | 573,98 | 614,21 |
| R08 | Functional Consultant (regular, offshore) | Solution Consultant (nome mais semelhante) | 573,98 | 614,21 |
| R09 | Change & Adoption (regular, onshore) | Solution Consultant (papel advisory/change) | 573,98 | 614,21 |
| R10 | Experience Design (regular, offshore) | Experience Architect | 789,88 | 845,24 |

## Base de Esforço

Sem cronograma comprometido (`timeline.user_commitment` ainda não fechado) — a banda usa a **faixa de duração do lane Aumentada** (15-34 semanas, `estimate-comparison.json`) sobre o roster de 10 papéis PS gravado em `resource-plan.json` (mesma equipe do lane Tradicional, ritmo acelerado por tooling de IA — sem redução de headcount).

Fórmula: `Σ (count × fração de alocação × semanas da faixa × 40h × rate)` por linha do roster — banda honestamente ampla, refletindo o próprio intervalo de duração de 15 a 34 semanas.

## Approved Commercials

| | Baixo (15 sem.) | Alto (34 sem.) |
|---|---|---|
| **Sem imposto** | R$ 3.195.105,00 | R$ 7.241.958,00 |
| **Com imposto** | R$ 3.419.053,00 | R$ 7.749.554,00 |

*Esta faixa é baseada na rate do contrato DATAPREV, mapeada por role PS LATAM (tabela de/para acima), que você validou em 2026-09-24. Indicativo apenas para planejamento; a estrutura comercial final é confirmada através do contrato comercial aplicável.*

## Como Ler Este Número

- **Indicativo, não é preço fechado.** É bill rate × esforço top-down — nunca custo/margem, nunca um fixed-fee.
- **Banda ampla por design**: reflete a própria incerteza de duração do lane Aumentada (15-34 semanas). Quando o cronograma for comprometido (`timeline.user_commitment`), re-rodar `commercials` para uma banda mais fechada via `derive-hours.py`.
- **Rates são as do contrato DATAPREV**, não uma tabela padrão desta ferramenta — refletem o padrão que o usuário aplica em todos os projetos PS LATAM.
- Papéis client-side (C01-C03 em `resource-plan.json`) não entram nesta precificação — são custeados pelo cliente.

## Disclaimer

*Este range é baseado nas rates do contrato DATAPREV, mapeadas por role PS LATAM (ver tabela de/para acima), que você validou em 2026-09-24. Indicativo apenas para planejamento; a estrutura comercial final é confirmada através do contrato comercial aplicável.*
