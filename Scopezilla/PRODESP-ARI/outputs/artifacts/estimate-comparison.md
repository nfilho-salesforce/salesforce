# Estimativa Dual-Track — ARI PRODESP / Desenvolve SP

*Migração da esteira de crédito de Sales Cloud + Experience Cloud para Financial Services Cloud (FSC) + Experience Cloud, no mesmo org de produção, in-place. Estimativa **com precificação diferida** — prazo + esforço (horas) + roster (perfis) por fase e entregável. Gerada em 2026-08-25.*

## So What

**Lane comprometida — Aumentada (IA-tooling + 2 squads): 12–22 semanas, ~3.630–7.010 horas PS, ~7,6–8,0 FTE média de programa (10 pessoas nomeadas).** É a Via Aumentada da discovery, alocada por complexidade. Cabe dentro da janela até 30/11/2026 se o kickoff ocorrer a tempo.

- **Tradicional (sem IA)**: ~14–26 semanas, ~4.100–8.350h — o custo "do jeito antigo" (gross-up notional). Não é a lane comprometida.
- **AI-native (condicional)**: ~10–16 semanas, ~2.160–3.680h, ~5,4–5,8 FTE — **só atrás do portão** de operação conjunta (decisor empoderado, cadência diária, mandato AI-first), que não está atendido hoje.

**Onde o número mora**: caminho crítico E07→E08→E10→E11. A Fase 3 (Núcleo — E04 XL) é o pico de esforço. A Fase 5 (regressão in-place + cutover irreversível de Person Accounts) é o maior risco e onde o QA faz surge.

**Precificação**: diferida. Nenhum valor foi calculado — rodar `commercials` com uma rate que você forneça e valide para a camada indicativa (só a lane comprometida).

## Comparação Dual-Track

| Lane | Base | Prazo | Esforço PS | FTE média | Gate |
|---|---|---|---|---|---|
| **Tradicional** (sem IA) | derivada (notional) | 14–26 sem | ~4.100–8.350h | ~8–9 | — |
| **Aumentada** (IA-tooling + 2 squads) ✅ **committed** | supplied (discovery) | **12–22 sem** | **~3.630–7.010h** | **~7,6–8,0** | aberta |
| **AI-native** (condicional) | derivada (native_band) | 10–16 sem | ~2.160–3.680h | ~5,4–5,8 | **condicional** |

- **Aumentada vs Tradicional**: ~12–16% menos esforço/prazo (`realized_band` — IA-tooling, operação inalterada). Ganho de ritmo e qualidade na mesma forma de time.
- **AI-native vs Tradicional**: ~30–38% menos, **condicional** ao portão. Numa data fixa (30/11), a compressão compra time mais enxuto/senior + buffer de cronograma — não um go-live antecipado.

> **Portão AI-native (não atendido hoje)**: aprovação multi-fornecedor antes de cada pilar (SF/DSP/Sinqia/Evertec) e dependência de SLA 24h são exatamente o risco. Overlap ~25–35% com a Aumentada — **o portão, não o número, distingue as lanes**. Magnitude provisória/vendor-reported; diagnóstico ancorado em DORA/METR (o gargalo é coordenação, não ferramenta).

## Roster Committed (Lane Aumentada) — os Perfis

**Um work stream, entregue por 2 squads (capacidade, não governança separada).** 10 pessoas nomeadas do lado PS; FTE média (~7,6–8,0) fica abaixo do headcount por time-box (`phases_active`) e cauda fracionada (Change).

| Perfil | Senioridade | Local | Qtd | Alocação | Fases | O que possui |
|---|---|---|---|---|---|---|
| Project/Program Manager | senior | onshore | 1 | full | F0–F5 | Relacionamento, governança de gates multi-fornecedor, plano |
| Solution Architect | senior | onshore | 1 | full | F0–F5 | "O quê"/qualidade; ratificação FSC nativo (G0012); jornadas/UX |
| Technical Architect | senior | onshore | 1 | full | F0–F5 | Modelo de dados (Person Accounts), 30 integrações, migração/cutover, ETL |
| Functional Consultant | regular¹ | offshore¹ | 2 | full | F1–F4 | Config declarativa FSC (PCM/BRE), story authoring — 1 por squad |
| Developer | senior | onshore | 1 | full | F1–F5 | Caminho crítico + reaponte E09; Apex/Platform Events; cutover |
| Developer | regular | offshore | 2 | full | F1–F5 | Pod de build (E04 XL, E02, LWC, conversão ETL) |
| Quality Assurance | senior | onshore | 1 | full | F2–F5 | Estratégia/execução de teste; **surge na F5** (regressão + cutover) |
| Change & Adoption | regular | onshore | 1 | quarter | F4–F5 | Treinamento backoffice + runbooks de cutover/hypercare |

¹ *Os 2 Functional Consultants na prática são 1 senior onshore + 1 regular offshore (mix), um por squad.*

### Lado cliente (Desenvolve SP / Sinqia / Evertec) — não staffado por PS
Sub-staffar o lado cliente é o principal risco de entrega — e é o gatilho da qualificação AI-native.

| Perfil | Owner | Por que é load-bearing |
|---|---|---|
| Product Owner / decisor empoderado | Desenvolve SP | Decisões de gate, ratificação Fase 0 (G0012), sign-off de escopo. Ausência = risco que mantém a AI-native condicional. |
| SME de negócio/crédito | Desenvolve SP | Valida elegibilidade/enquadramento (BRE/PCM), jornadas PJ/PF, fronteira P3↔P5 |
| Owner de integração core banking | Sinqia/Evertec | Contratos/Swagger das 30 System APIs, write-back PUT/PATCH (G0013 — maior risco de cronograma) |
| Sign-off regulatório | Desenvolve SP | LGPD, antifraude/biometria — responsabilidade auditável |

## Horas por Fase e Entregável (Lane Aumentada)

| Fase | Entregável | Épicos | Semanas (12→22) | Horas (baixa→alta) |
|---|---|---|---|---|
| **F0** Discovery & Foundation | Ratificação do modelo-alvo (G0012), inventário das 30 APIs, volume, fronteira P3↔P5 | — | 2 | 240 |
| **F1** Fundação FSC & Modelo de Dados | Person Accounts (sandbox) + PCM/BRE/DecisionTable | E07, E08 | 2→4 | 640→1.280 |
| **F2** Esteira de Entrada | Lead→LoanApplicant; pré-qualificação sobre RLA; elegibilidade | E01, E02 | 2→3 | 720→1.080 |
| **F3** Proposta, Estruturação & Aprovação | Núcleo pesado — tomador→LoanApplicant, garantias→LoanApplicantAsset, efetivação via Platform Event | E03, E04, E05 | 3→8 | 1.080→2.880 |
| **F4** Formalização | CCB (download/upload), Meus Contratos | E06 | 1 | 370 |
| **F5** Migração, Regressão & Cutover | ETL/conversão, descomissionamento, SIT/UAT, regressão in-place, cutover irreversível, hypercare | E10, E11 | 2→4 | 580→1.160 |
| **F6** Reapontamento de Integrações *(parallel track)* | 30 APIs reapontadas do lado Salesforce | E09 | concorre com F2–F4 | *(dentro da janela do Dev senior)* |
| | | | **12→22 sem** | **~3.630→7.010h** |

*E09 (30 integrações) roda em trilha paralela às Fases 2–4 — as horas do reaponte estão dentro da janela F1–F5 do Developer senior onshore, não somadas ao caminho crítico.*

## Comparação — Roster AI-native (condicional)

Se o portão de operação conjunta for comprometido, o time re-rotula e fica mais enxuto/senior (~5,4–5,8 FTE, 6 perfis + 1 offshore time-boxed):

- **Program Lead** (PM sr onshore) — coordenação multi-fornecedor não comprime com IA, segue full
- **Intent Architect** (Solution Architect sr onshore) — absorve adoção (escopo fino)
- **Agent Orchestrator** (Technical Architect sr onshore) — dirige a frota de agentes; migração/integração/cutover
- **Functional Consultant** agent-assisted (sr onshore) — 1 senior cobre as 2 squads (sequenciamento)
- **Logic & Integration Engineer** (Dev sr onshore) + 1 regular offshore time-boxed no E09
- **Logic Validator** (QA sr onshore) — **surge na F5**, NÃO encolhe (checagem independente, contexto regulado)

## Premissas Load-Bearing

- **Adoção FSC nativa (G0012)** em REVISAR — gate da Fase 0. Se não ratificada, a prioridade 3 muda de escopo (reaponte leve vs. migração de modelo) e o sizing dos pilares se desloca.
- **30 integrações MuleSoft apenas reapontadas** do lado Salesforce, não reconstruídas; contratos das System APIs estáveis (G0013). 29/30 sem Swagger é o maior risco de cronograma (~+42% no teto do Parecer).
- **Volume de produção a confirmar** (G1004) — contagens atuais são do sandbox HML; E10 (Migração/Regressão) fica `Assumed` e alarga as bandas para cima.

## Ressalvas

- **Precificação diferida** — nenhuma taxa, valor ou custo foi calculado ou implícito. Rodar `commercials` (rate fornecida e validada) para a camada indicativa, só a lane comprometida.
- **T-shirt sizes não são horas** — as horas aqui derivam do roster committed × faixa de semanas, não de multiplicar tamanho por rate.
- **A faixa 12–22 semanas** é a base de compromisso (Via Aumentada + 2 squads da discovery), não um número inventado; a Tradicional é gross-up notional e a AI-native é condicional/provisória.
- **Data 30/11/2026** é alvo externo (Parecer de Viabilidade); numa data fixa, compressão de IA compra time enxuto + buffer, não go-live antecipado.
- **Sign-off pendente** — o Solution Lead (SSSL) refina para os números finais e assina.
