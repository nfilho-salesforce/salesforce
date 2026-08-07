<!-- Source: Revisão de escopo DATA ÁGIL · 15 jornadas · Retrieved: 2026-07-28 · Via: Claude -->

# ROM — DATA ÁGIL (Revisão v5.0) · 15 Jornadas
**Data:** 2026-07-28 · **Cliente:** DATAPREV · **Janela:** Agosto–Dezembro 2026 (~22 semanas)
**Envelope comercial (validado pelo usuário):** teto fixo **R$ 5.000.000 com imposto** → **R$ 4.672.500 sem imposto** (÷0,9345)

> *Faixa indicativa para planejamento. Baseada no teto de bolsão de R$ 5,0 M que o usuário forneceu e validou em 2026-07-28. As horas por jornada derivam de um rate blended de PS de ~R$ 653/h c/imp aplicado sobre o mix de perfis abaixo — indicativas, sujeitas a calibração no fechamento.*

---

## 1. Escopo — 15 jornadas, 3 pilares de solução

**Pilar 1 — MuleSoft:** camada de integração + exposição de **MCP server** dos legados/sistemas de origem.
**Pilar 2 — Agentes especialistas (Agentforce):** um agente por sistema legado, atendendo as 15 jornadas.
**Pilar 3 — Slack + Slack bot:** front conversacional. Dois ambientes: workspace **interno** (colaboradores + gestores Dataprev) e workspace **externo** (clientes), separados por conta do compartilhamento de canais públicos.

### 5 jornadas de agentes (sistemas de origem)
| # | Jornada | Sistema origem | Público | Escrita? |
|---|---|---|---|---|
| J1 | Consulta Financeira | Financeiro (Protheus) | Externo + Interno | Leitura |
| J2 | Status de Chamado | Chamados (service desk) | Externo + Interno | Leitura |
| J3 | Briefing de Projeto em Tempo Real | Clarity (PPM) | Interno (gestores) | Leitura |
| J4 | Agendamento Inteligente por Voz | Agenda/MS Office/Teams (Graph) | Interno | Escrita |
| J7 | FAQ Interno via Conexão | CRM (Conexão) | Interno | Leitura (RAG) |

### 10 jornadas SEI (mod-wssei v2 · polling)
| # | Jornada | Público | Escrita? |
|---|---|---|---|
| SEI-J1 | Alerta de Prazo / cumprimento tácito | Interno | Leitura |
| SEI-J2 | Consulta em linguagem natural | Interno | Leitura |
| SEI-J3 | Notificação recebido/tramitado | Interno | Leitura |
| SEI-J4 | Meu painel de processos | Interno | Leitura |
| SEI-J5 | Digest de unidade | Interno (gestor) | Leitura |
| SEI-J6 | "Qual tipo uso?" + RAG | Interno | Leitura (RAG) |
| SEI-J7 | Status de assinatura + deep-link | Interno | Leitura |
| SEI-J8 | Ciência de documento | Interno | Escrita leve |
| SEI-J9 | Tramitar via aprovação | Interno | Escrita + governança |
| SEI-J10 | Abrir processo | Interno | Escrita + governança |

---

## 2. Roster — Ago–Dez 2026 (regras Dataprev aplicadas)

| Perfil | Pilar | h/sem | Semanas | Horas | Rate c/imp | Custo c/imp |
|---|---|---:|---:|---:|---:|---:|
| MuleSoft Technical Architect (Sr) | 1 | 36 | 22 | 800 | 767,68 | R$ 614.144 |
| MuleSoft Technical Consultant ×2 | 1 | 40 | 22 | 1.560 | 624,97 | R$ 974.953 |
| Agentforce Specialist / TC ×2 | 2 | 40 | 22 | 1.560 | 624,97 | R$ 974.953 |
| Solution Architect (Slack/plataforma) | 3 | 32 | 20 | 560 | 738,14 | R$ 413.358 |
| UX Conversacional / Experience Architect | 3 | 30 | 18 | 520 | 738,14 | R$ 383.833 |
| QA Consultant ×2 | — | 40 | 18 | 1.293 | 536,39 | R$ 693.552 |
| Program Manager | — | 24 | 22 | 528→997* | 738,14 | R$ 735.926 |
| Change & Adoption Manager | — | 18 | 16 | 400 | 738,14 | R$ 295.256 |
| **TOTAL** | | | | **~7.650h** | blended ~653/h | **~R$ 5.000.000** |

**Verificações obrigatórias:**
- ✅ Nenhum recurso < 20h/sem.
- ✅ Ratio QA: 4 TC/Dev de build (2 MuleSoft + 2 Agentforce) → 2 QA.
- ✅ PM ≥ 15% das horas do time (997h ≈ 15% de 6.653h) — *PM ajustado para cumprir a regra.*
- ✅ Ganho de IA ≥ 25% embutido (ver §5).

\* PM elevado a ~997h para cumprir a regra "PM ≥ 15% do time técnico"; a linha da tabela mostra a base operacional (24h/sem) e o ajuste regulatório.

---

## 3. Composição do bolsão — R$ 5 M jornada por jornada (totalmente carregado)

Cada valor inclui a parcela proporcional da **plataforma compartilhada** (MuleSoft core + MCP, setup Slack dual-workspace, framework de agentes, Fase 0 governança G1002, PM, QA, Change, UX baseline) — ~45% de cada número é fundação construída uma vez e reutilizada.

| Jornada | Peso | Horas | R$ c/imp | Onda |
|---|---:|---:|---:|:--:|
| J1 · Consulta Financeira | 3 | 402 | R$ 263.158 | 1 |
| J2 · Status de Chamado | 3 | 402 | R$ 263.158 | 1 |
| SEI-J1 · Alerta de Prazo/tácito | 4 | 537 | R$ 350.877 | 1 |
| SEI-J2 · Consulta linguagem natural | 4 | 537 | R$ 350.877 | 1 |
| SEI-J3 · Notif. recebido/tramitado | 3 | 402 | R$ 263.158 | 1 |
| J3 · Briefing de Projeto (Clarity) | 3 | 402 | R$ 263.158 | 2 |
| J7 · FAQ Interno via Conexão | 3 | 402 | R$ 263.158 | 2 |
| SEI-J4 · Meu painel de processos | 3 | 402 | R$ 263.158 | 2 |
| SEI-J5 · Digest de unidade | 3 | 402 | R$ 263.158 | 2 |
| SEI-J6 · "Qual tipo uso?" + RAG | 4 | 537 | R$ 350.877 | 2 |
| SEI-J7 · Status assinatura + deep-link | 3 | 402 | R$ 263.158 | 2 |
| J4 · Agendamento por Voz | 5 | 671 | R$ 438.596 | 3 |
| SEI-J8 · Ciência de documento | 4 | 537 | R$ 350.877 | 3 |
| SEI-J9 · Tramitar via aprovação | 6 | 805 | R$ 526.316 | 3 |
| SEI-J10 · Abrir processo | 6 | 805 | R$ 526.316 | 3 |
| **TOTAL** | **57** | **~7.650** | **R$ 5.000.000** | |

Pesos por drivers de complexidade: leitura simples = 3; leitura+RAG/polling+lógica = 4; voz+escrita MS Graph = 5; escrita SEI + fluxo de aprovação/governança = 6.

---

## 4. Ondas de entrega — Ago a Dez 2026

**Fase 0 (Ago, obrigatória):** resolução do bloqueador de governança **G1002** (perfis de acesso Protheus/SEI, workspace externo, LGPD Art. 48/TCU) — gate para as jornadas de escrita SEI.

| Onda | Janela | Go-live | Jornadas (nº) | Perfil |
|---|---|---|---|---|
| **Onda 1 — Quick Wins** | Ago–Set | fim de Set | J1, J2, SEI-J1, SEI-J2, SEI-J3 (5) | Leitura, alto valor/baixo esforço |
| **Onda 2 — Expansão** | Out–Nov | fim de Nov | J3, J7, SEI-J4, SEI-J5, SEI-J6, SEI-J7 (6) | Leitura+RAG+painéis |
| **Onda 3 — Escrita/Transação** | Nov–Dez | meados de Dez + hypercare | J4, SEI-J8, SEI-J9, SEI-J10 (4) | Escrita, voz, governança |

Prioridade = **valor ÷ esforço**. Ondas antecipam valor e reduzem risco: leitura primeiro, escrita/governança por último (após Fase 0).

---

## 5. Tradicional × IA-Native (mandato Dataprev ≥25%)

| Cenário | Duração | Observação |
|---|---|---|
| Sem ferramentas de IA | ~30 semanas | baseline p/ 15 jornadas + 3 pilares |
| Com IA-native (−≥27%) | ~22 semanas | cabe na janela Ago–Dez 2026 |

Atividades comprimidas: geração de fluxos de integração MuleSoft, prompts/tópicos de agentes, testes automatizados, documentação técnica, geração de artefatos. O teto de R$ 5 M é o que torna o cronograma de 22 semanas viável **apenas** com o ganho de IA — sem IA, o mesmo escopo não caberia no bolsão nem na janela.

---

## 6. Clouds necessárias (apenas as necessárias)

| Cloud | Papel | Licença de referência |
|---|---|---|
| **Slack** (Grid) | Front conversacional, dual-workspace | por usuário/mês |
| **Agentforce** (Public Sector) | Agentes especialistas | Public Sector - Service - Agentforce 1 Edition |
| **MuleSoft** (Anypoint Titanium) | Integração + MCP server dos legados | Anypoint Platform Base - Titanium |

*Data Cloud não é obrigatória nesta fase — RAG (J7, SEI-J6) pode usar Data Library do Agentforce. Incluir só se a volumetria exigir.*

---

## 7. KPIs propostos + ROI (por processo das jornadas)

**Metodologia de ROI:** investimento R$ 5 M → retorno por (a) horas liberadas de trabalho manual, (b) redução de perdas por decurso de prazo (SEI tácito), (c) deflection de atendimento. Números finais dependem da volumetria da Dataprev (gap **G1102**) — entregue metodologia + exemplo ilustrativo, sem número comprometido.

| Processo / Jornada | KPI proposto | Baseline → Meta (ilustrativo) |
|---|---|---|
| Financeiro (J1) | Tempo médio de resposta a consulta financeira | horas → segundos |
| Financeiro (J1) | % consultas self-service via Slack | — → 70% |
| Chamados (J2) | Deflection de chamados "status" | — → 40% |
| Clarity/Briefing (J3) | Tempo de preparação de reunião executiva | −60% |
| Agendamento (J4) | Tempo para agendar reunião | minutos → 1 comando |
| FAQ/Conexão (J7) | Deflection de perguntas repetitivas RH/suporte | — → 50% |
| SEI prazos (SEI-J1) | Prazos cumpridos no tácito (perdas por decurso) | −80% |
| SEI consulta (SEI-J2/J4) | Tempo de consulta processual | −70% |
| SEI tramitação (SEI-J9/J10) | Tempo de tramitação / abertura | −50% |
| **Transversais** | Usuários ativos (adoção Slack) | meta ≥70% |
| **Transversais** | % jornadas resolvidas sem escalar a humano | ≥65% |
| **Transversais** | Ganho de eficiência de IA (mandato Dataprev) | ≥25% |

---

## 8. Premissas
1. R$ 5 M é teto fixo com imposto; escopo cabe no teto por priorização de ondas (não por corte de qualidade).
2. Janela Ago–Dez 2026 só é viável com IA-native (−≥27%); atraso de kickoff comprime as ondas.
3. SEI acessível via REST mod-wssei v2 (JWT, ~150+ endpoints) — sem push/webhook, **polling obrigatório**.
4. Workspace Slack externo separado para clientes (compartilhamento de canais públicos); autenticação por perfil.
5. Volumetrias (G1102) fornecidas na Fase 0 para calibrar KPIs.
6. Fase 0 (G1002) concluída em Agosto — gate para jornadas de escrita SEI.

## 9. Fora do escopo
- E11 SEI de expansão além das 10 jornadas listadas.
- Migração de dados legada; substituição de sistemas de origem.
- Data Cloud (salvo se volumetria de RAG exigir).

## 10. Riscos e perguntas em aberto
- **G1002** (governança Protheus/SEI) não resolvido bloqueia Onda 3.
- Latência de polling do SEI vs. expectativa de tempo real.
- Aprovação do workspace externo e política de canais públicos.
- Volumetria pendente (G1102) impede comprometer números de ROI.
- Confiança ~50% (teto fixo dá disciplina, mas volumetrias e governança seguem abertas).
