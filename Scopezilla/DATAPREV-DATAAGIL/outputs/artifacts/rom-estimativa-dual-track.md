# ROM — DATAPREV Data Ágil
## Estimativa, Timeline, Perfis & Horas, e Comparativo Tradicional × IA-Native

**Projeto:** DATAPREV Data Ágil
**Cliente:** Dataprev — Empresa de Tecnologia e Informações da Previdência (Governo Federal Brasileiro)
**Produtos Salesforce in-scope:** Slack (Enterprise Grid), Agentforce, MuleSoft / MCP
**Data:** 2026-07-20
**Moeda:** BRL (Reais) — todos os valores COM impostos
**Status:** ROM — decision-support para planejamento e alocação orçamentária (não é proposta comercial fechada)

---

## Sumário Executivo

| Métrica | Tradicional (offshore-weighted) | IA-Native / Quantum Leap (senior-core + agentes) | Delta |
|---|---|---|---|
| **Timeline** | 29–54 semanas | 25–49 semanas | **~9–14% mais rápido** |
| **Equipe no pico (Fase 2)** | 12–15 pessoas | 10–11 pessoas | **~17–27% menos pessoas** |
| **Faixa indicativa de preço** | R$ 12,07M – R$ 31,27M | R$ 7,96M – R$ 19,97M | **~34–36% menor** |
| **Working-point (ponto de trabalho)** | ~R$ 16,9M · 40 sem · 25.254h | ~R$ 10,4M · 36 sem · 12.949h | **~38% menor** |

> **A vantagem da lane IA-Native não é desconto — é um modelo de entrega diferente.** Duração comprimida pela eficiência de IA + o build volume absorvido por agentes sob supervisão de um núcleo sênior (pod offshore eliminado). O cliente paga por **tempo × capacidade**, não por número de corpos.

**KPI de eficiência de IA (mandato Dataprev ≥25%):** atendido na dimensão **esforço/custo (~38% de redução de horas e ~34–36% de preço)**. Na dimensão **duração isolada**, a compressão é de **~10–14%** (readiness atual 2/8 — Low). Chegar a ≥25% de compressão de *prazo* exige os 5 desbloqueios listados na seção "Riscos e Perguntas em Aberto".

---

## a) Briefing Comercial Executivo

A **Dataprev** é a espinha dorsal tecnológica da Previdência Social e de programas sociais do Governo Federal, processando dados sensíveis (Art. 11 LGPD) para dezenas de ministérios e milhões de beneficiários. Opera sob três pressões simultâneas:

- **Orçamentária (PLOA/LOA):** o ciclo orçamentário federal condiciona janelas de contratação e go-live; entregas precisam demonstrar ROI mensurável para sustentar renovação.
- **Regulatória (TCU / CGU / ANPD):** trilha de auditoria, governança de perfil de acesso (TI + Jurídico + DPO) e conformidade LGPD são pré-condições, não opcionais.
- **Transformação digital interna:** a Dataprev busca reduzir dependência de atendimento humano N1, dar autonomia self-service a clientes B2B (ministérios/entes públicos) e modernizar a experiência de servidores e beneficiários.

**Onde a Salesforce PS gera ROI demonstrável:** deslocar consultas financeiras, chamados técnicos e consultas normativas para self-service conversacional (Slack + Agentforce), com rastreabilidade LGPD/TCU nativa, sobre uma camada de integração governada (MuleSoft) que expõe os 6 sistemas legados sem reescrevê-los. O modelo IA-Native permite entregar o mesmo escopo com equipe menor e prazo comprimido — diretamente alinhado à pressão orçamentária.

---

## b) Objetivo, Escopo e Alcance

### Objetivo estratégico (o "porquê")
Dar à Dataprev uma **camada de atendimento conversacional governada** que reduza escalação humana N1, aumente a autonomia self-service de clientes B2B e servidores, e gere trilha de auditoria LGPD/TCU nativa — tudo sobre os 6 sistemas legados existentes (Protheus, Pronto/ServiceNow, CRM Totvs, Portal Conexão/SharePoint, Microsoft Teams, Clarity/Broadcom), sem reescrevê-los.

### Dentro do escopo (10 épicas)
Consultas financeiras, autoatendimento de chamados, intelligence executiva, base de conhecimento normativo, agendamento, adoção de CRM por conversação, abertura assistida de chamados, gestão de demandas evolutivas, intelligence preditiva, e o workstream transversal de governança/compliance/change management.

### Fronteiras — Fora do escopo
Ver seção **h)**.

### Alcance
Entrega 100% Salesforce PS (todas as 10 épicas, incluindo Change Management E10). 0 papéis client-staffed confirmados. Faseamento F0 → F3 (ver seção **d/f**).

---

## c) Proposta de Solução — Estimativa (Épicas + T-shirt Sizes)

O escopo e a complexidade são **os mesmos independentemente do modelo de entrega** — as duas lanes projetam sobre esta mesma base validada.

| Épica | Nome | Tamanho | Confiança | Produto principal |
|---|---|---|---|---|
| **E01** | Consultas Financeiras Self-Service | L | Assumed | Agentforce + MuleSoft (Protheus) |
| **E02** | Autoatendimento Chamados Técnicos | M | Assumed | Agentforce + Slack |
| **E03** | Intelligence Executiva Mobile | M | Assumed | Agentforce + Analytics |
| **E04** | Knowledge Base Normativas RH | L | Assumed | Agentforce (RAG) |
| **E05** | Agendamento Automatizado | S | **Confirmed** | Agentforce + Slack |
| **E06** | Adoção CRM via Conversação | L | Assumed | Agentforce + CRM Totvs |
| **E07** | Abertura de Chamados Assistida | M | Assumed | Agentforce |
| **E08** | Gestão de Demandas Evolutivas | **XL** | **Unknown** | Agentforce + MuleSoft |
| **E09** | Intelligence Preditiva e Recomendações | **XL** | Assumed | Data Cloud + Einstein |
| **E10** | Governança, Compliance e Change Management | **XL** | Assumed | Transversal (todas as fases) |

**Distribuição:** 3 XL · 3 L · 3 M · 1 S. **Confiança:** 1 Confirmed / 8 Assumed / 1 Unknown — típico de primeiro rascunho; a Fase 0 resolve 68 gaps e eleva para 70–80% Confirmed.

> **Nota sobre T-shirt sizes:** expressam **complexidade relativa**, não esforço. Não são hora-conversíveis diretamente. As horas nas tabelas abaixo são derivadas **top-down do shape do engajamento** (roster × semanas de fase), não somando horas-por-tamanho.

**Arquitetura de alto nível:** Slack (superfície de conversação) → Agentforce (orquestração de agentes, RAG, NLP) → MuleSoft/MCP (hub de exposição de APIs dos 6 legados, com enforcement de perfil de acesso) → Data Cloud + Einstein (F3, camada preditiva). Governança LGPD/TCU e trilha de auditoria são transversais (E10).

---

## d) Entregáveis e Milestones (por fase)

| Fase | Entregáveis principais | Milestone / critério de aceite |
|---|---|---|
| **F0 — Discovery & Architecture Refinement** | Resolução do bloqueador G1002 (governança Protheus TI+Jurídico+DPO); auditoria de volumetrias; validação da API Clarity; segregação de Workspace Slack (G0101); RACI + charter de governança | Bloqueadores resolvidos; arquitetura assinada; confiança ≥70% |
| **F1 — Foundation / Quick Wins** | E01–E05, E10 (read-only); 5 agentes de Fase 1 (J1, J2, J5, J7, J8); piloto 20–50 early adopters | Jornadas read-only em produção; piloto validado |
| **F2 — Expansion / Controlled Writes** | E06, E07, E10; escritas controladas; conectores MuleSoft dos 6 legados | Escritas governadas em produção; scale do piloto |
| **F3 — Proactive Intelligence** | E08, E09, E10; Data Cloud (Pronto + CRM Totvs CDC), modelos Einstein (SLA breach, churn de pipeline) | Camada preditiva ativa; hypercare |

---

## e) KPIs de Eficiência de Negócio (ROI pós-implantação)

- **Taxa de deflexão N1** — % de consultas resolvidas por self-service sem escalação humana (meta: linha de base → +X% por fase).
- **Tempo médio de atendimento** (antes × depois) nas jornadas J1–J10.
- **Taxa de resolução no primeiro contato** (first-contact resolution) via agente conversacional.
- **Adoção da plataforma** — % de usuários ativos (early adopters 20–50 → scale F2/F3).
- **Redução de retrabalho** em processos manuais de consulta/abertura de chamado.
- **Conformidade de trilha de auditoria** — % de interações com registro LGPD/TCU completo (meta: 100%).

---

## f) Macro Atividades por Fase (nível L1/L2)

- **F0:** discovery técnico · auditoria de volumetrias · resolução de bloqueadores de governança · desenho de arquitetura · setup de Workspace/Enterprise Grid · workshop RACI.
- **F1:** exposição de APIs read-only (MuleSoft) · configuração de agentes Agentforce · RAG da base normativa · design conversacional · piloto + usability testing · CM/treinamento inicial.
- **F2:** conectores dos 6 legados · escritas controladas · integração CRM Totvs · testes de integração · hardening · scale de adoção.
- **F3:** ingestão Data Cloud (streaming/CDC) · modelos preditivos Einstein · ativação de segmentação · analytics executivo · hypercare · handoff de sustentação.

---

## g) Perfis & Horas Calculadas (com as taxas validadas)

**Base de taxas:** as 11 funções do projeto foram mapeadas às taxas do contrato Salesforce PS Brasil (COM impostos, daily rate 8h/dia), validadas pelo Solution Lead em 2026-07-19. Taxa/hora = taxa/dia ÷ 8.

| Classe | Taxa/dia (COM imp.) | Taxa/hora | Funções |
|---|---|---|---|
| Onshore-architect (blended) | R$ 7.195 | R$ 899,38 | R01, R03, R05, R06, R07 |
| Onshore-developer (blended) | R$ 5.563 | R$ 695,38 | R02, R04, R08, R09, R10, R11 |
| Offshore (assumption) | R$ 3.500 | R$ 437,50 | pod de build (só Tradicional) |

Taxas individuais: R01 R$7.573 · R02 R$5.725 · R03 R$7.033 · R04 R$5.725 · R05 R$7.033 · R06 R$6.762 · R07 R$7.573 · R08 R$5.725 · R09 R$5.725 · R11 R$4.914/dia.

### g.1 — LANE TRADICIONAL (working-point 40 semanas · F0=6 F1=10 F2=14 F3=10)

| Perfil | Fases | h/sem | Total (h) | R$/h | Custo (R$) |
|---|---|---|---|---|---|
| R01 — Senior Technical Architect | F0–F3 | 40 | 1.600 | 946,62 | 1.514.600 |
| R03 — MuleSoft Technical Architect | F0–F3 | 40 | 1.600 | 879,12 | 1.406.600 |
| R06 — Solution Architect | F1–F3 | 40 | 1.360 | 845,25 | 1.149.540 |
| R05 — Data Cloud Technical Architect | F3 | 40 | 400 | 879,12 | 351.650 |
| R07 — Change Management Lead | F0–F3 | 20 | 800 | 946,62 | 757.300 |
| R02 — Agentforce Technical Consultant | F1–F3 | 40 | 1.360 | 715,62 | 973.250 |
| R04 — MuleSoft Technical Consultant | F1–F3 | 40 | 1.360 | 715,62 | 973.250 |
| R08 — UX Researcher / Service Designer | F0–F2 | 20 | 600 | 715,62 | 429.375 |
| R09 — Einstein Analytics Developer | F3 | 40 | 400 | 715,62 | 286.250 |
| R10 — Solution Consultant (BA) | F0–F3 | 40 | 1.600 | 695,38 | 1.112.600 |
| R11 — Quality Assurance Consultant | F1–F3 | 40 | 1.360 | 614,25 | 835.380 |
| **Offshore build pod** (5 dev + 2 QA) | F1–F3 | — | 9.520 | 437,50 | 4.165.000 |
| **Program Manager** (regra 15%) | F0–F3 | — | 3.294 | 899,38 | 2.962.541 |
| **TOTAL** | | | **25.254** | | **≈ 16.917.336** |

### g.2 — LANE IA-NATIVE / QUANTUM LEAP (working-point 36 semanas · F0=5 F1=9 F2=13 F3=9 · offshore=0)

| Perfil | Fases | h/sem | Total (h) | R$/h | Custo (R$) |
|---|---|---|---|---|---|
| R01 — Senior Technical Architect | F0–F3 | 40 | 1.440 | 946,62 | 1.363.140 |
| R03 — MuleSoft Technical Architect | F0–F3 | 40 | 1.440 | 879,12 | 1.265.940 |
| R06 — Solution Architect | F1–F3 | 40 | 1.240 | 845,25 | 1.048.110 |
| R05 — Data Cloud Technical Architect | F3 | 40 | 360 | 879,12 | 316.485 |
| R07 — Change Management Lead | F0–F3 | 20 | 720 | 946,62 | 681.570 |
| R02 — Agentforce Consultant (*agent director*) | F1–F3 | 40 | 1.240 | 715,62 | 887.375 |
| R04 — MuleSoft Consultant (*agent director*) | F1–F3 | 40 | 1.240 | 715,62 | 887.375 |
| R08 — UX Researcher / Service Designer | F0–F2 | 20 | 540 | 715,62 | 386.438 |
| R09 — Einstein Analytics Developer | F3 | 40 | 360 | 715,62 | 257.625 |
| R10 — Solution Consultant (BA) | F0–F3 | 40 | 1.440 | 695,38 | 1.001.340 |
| R11 — Quality Assurance Consultant | F1–F3 | 40 | 1.240 | 614,25 | 761.670 |
| **Offshore** | — | — | **0** | — | **0** |
| **Program Manager** (regra 15%) | F0–F3 | — | 1.689 | 899,38 | 1.519.044 |
| **TOTAL** | | | **12.949** | | **≈ 10.376.112** |

### g.3 — Verificações obrigatórias FASE 10

- ✅ **Mínimo 20h/semana:** nenhum recurso abaixo de 20h/sem (R07 e R08 em 20h part-time; demais 40h).
- ✅ **Ratio QA:** R11 (onshore, todas as fases de build) + 2 QA offshore na Tradicional cobrem os ~7 recursos de build (2 dev onshore + 5 offshore) — ratio ~1:2. Na IA-Native, R11 é *agent-amplified* e faz surge nas janelas de hardening.
- ✅ **PM ≥15%:** PM = 15% das horas técnicas totais em ambas as lanes (Tradicional 3.294h; IA-Native 1.689h). **Flag:** o roster nomeado de 11 perfis **não inclui** uma função dedicada de Program Manager — a linha de PM acima é uma **adição obrigatória FASE 10** a validar (taxa proxy = architect blended R$7.195/dia; ajustar quando a taxa contratual de PM estiver disponível). Volume Tradicional (~77h/sem) sugere **1–2 FTE de PM**.
- ✅ **Ganho de IA ≥25%:** atendido na dimensão esforço/custo (~38% de redução de horas, ~34–36% de preço).

---

## Comparativo Tradicional × IA-Native — Delta Decomposto

| Dimensão | Tradicional | IA-Native / Quantum Leap | Delta |
|---|---|---|---|
| **Duração** | 29–54 sem | 25–49 sem | **~9–14% mais rápido** (compressão de eficiência de IA, readiness Low ~10–14%) |
| **Equipe no pico** | 12–15 pessoas | 10–11 pessoas | **~17–27% menos** (pod offshore eliminado) |
| **Preço indicativo (faixa validada)** | R$ 12,07M – R$ 31,27M | R$ 7,96M – R$ 19,97M | **~34–36% menor** |
| **Working-point (bottom-up)** | ≈ R$ 16,9M / 25.254h | ≈ R$ 10,4M / 12.949h | **~38% menor / ~49% menos horas** |

**Por que a IA-Native é ~34–36% mais barata (três vetores, não um desconto):**

1. **Duração comprimida** (25–49 sem vs 29–54 sem): ganho task-level de IA ~30–40% × fator de realização 0,40–0,45 = ~12–18% project-level; readiness 2/8 reduz para a banda Low ~10–14%. **O tempo é a moeda de comparação.**
2. **Equipe derivada à necessidade** (10–11 vs 12–15 pessoas): núcleo sênior contínuo (6 F0–F3) + especialistas fracionais (5, consumidos quando necessário) + **0 offshore** — os agentes absorvem o volume de build (6 conectores de API legados, 10 jornadas Agentforce J1–J10, config Data Cloud, execução de testes) sob supervisão do núcleo sênior; R02/R04 atuam como *agent directors*.
3. **Mix de classe de taxa** (100% onshore sênior vs blend offshore-weighted): sem taxas offshore → daily rate blended menor com o mesmo headcount sênior onshore.

**Reconciliação:** o bottom-up por perfil (g.1/g.2) cai **dentro** de ambas as faixas top-down validadas e reproduz o delta de ~34–38% — a estimativa é internamente consistente.

---

## g.4 — Timeline Proposta

**Faixa benchmark: 29–54 semanas (Tradicional) / 25–49 semanas (IA-Native).**

Derivada top-down do shape do engajamento: linha Multi-Cloud High (10 épicas, predominância L/XL, 6 sistemas legados, baseline 26–40 sem) + adders: **+15%** indústria regulada (LGPD Art. 48 + trilha TCU + governança de perfil de acesso), **+10%** cliente novo (primeira vez Dataprev, bloqueador G1002 não resolvido), **+10%** alargamento de confiança (68 gaps, volumetrias pendentes). Total +35% (sob o teto de +50%). A lane IA-Native comprime essa faixa pela banda realizada de eficiência (readiness Low ~10–14%).

**Faseamento (working-point Tradicional 40 sem):** F0 Discovery (6 sem) → F1 Foundation (10 sem) → F2 Expansion (14 sem, pico) → F3 Proactive Intelligence (10 sem).

---

## g) Premissas

1. Escopo 100% Salesforce PS — todas as 10 épicas, 0 papéis client-staffed (confirmado SSSL).
2. As taxas do contrato Salesforce PS Brasil (COM impostos, 8h/dia) foram validadas em 2026-07-19 e são a base de todo cálculo de preço.
3. A taxa **offshore R$ 3.500/dia é uma assumption** (nearshore Brasil, market-typical) — **não consta na tabela do contrato**; validar aplicabilidade ou ajustar.
4. A função **Program Manager não está no roster nomeado** de 11 perfis; a linha PM (15%) é adição obrigatória FASE 10, com taxa proxy = architect blended (ajustar à taxa contratual de PM).
5. A taxa de **R10 (Solution Consultant)** usa o developer blended R$ 5.563/dia (não listada individualmente no mapeamento) — validar.
6. Working-points (40 sem Tradicional / 36 sem IA-Native) são pontos representativos **dentro** das faixas benchmark, para materializar a tabela de horas — não são compromissos de prazo.
7. A banda de compressão de IA (~10–14%) é **provisória** até acumular actuals de entregas IA-Native (readiness 2/8, Low).
8. A alocação por fase respeita mín. 20h/sem, ratio QA e PM ≥15% (regras FASE 10).

---

## h) Fora do Escopo

- Reescrita ou substituição dos 6 sistemas legados (a solução os expõe via MuleSoft, não os refatora).
- Migração de dados históricos além do necessário para as jornadas em escopo.
- Licenças Salesforce (Slack, Agentforce, Data Cloud, MuleSoft) — objeto de contratação separada.
- Infraestrutura/hospedagem gov (OCI/GovCloud) e provisionamento de acesso do lado Dataprev.
- Sustentação/AMS pós-hypercare (contrato separado).
- Qualquer épica não listada na seção c).

---

## i) Riscos e Perguntas em Aberto

### Riscos
- **🔴 Bloqueador G1002 (Protheus):** aprovação tri-party TI + Jurídico + DPO pendente pré-kick-off. Se não resolvido, a jornada J1 (E01 Consultas Financeiras) é inviável. **Escalar ao seller antes da submissão da proposta.**
- **68 gaps** excedem o limiar de 15 → **Fase 0 obrigatória** para elevar confiança de 45% para 70–80%.
- **Volumetrias pendentes** (G0102/G0201/G0302/G0701): dimensionamento de capacidade sem baseline.
- **Turnover de gestores públicos / dependência de aprovação CTID/ANPD** em milestones.
- **E08 confiança Unknown, XL:** maior fonte de incerteza de sizing.

### 5 desbloqueios para elevar a compressão de IA (Low ~10–14% → High ~18–22%)
1. Aprovação de ferramentas de IA para o time de entrega PS (Copilot, Claude, Cursor — hoje não adotadas).
2. Resolução do G1002 Protheus pré-kick-off.
3. Política de entrega assistida por IA conforme LGPD/TCU (nível de revisão humana de código/config/docs gerados).
4. Auditoria de volumetrias.
5. Plano de reconciliação de modelo de dados entre os 6 sistemas legados.

### Perguntas em aberto (responder antes de fechar a estimativa final)
1. A taxa offshore R$ 3.500/dia é aplicável ou há taxa offshore contratada?
2. Qual a taxa contratual de Program Manager (para substituir o proxy)?
3. Confirma o número de processo licitatório / previsão de edital?
4. Restrições de residência de dados exigem 100% onshore (elimina lane offshore)?
5. Exigência de certificação (ISO 27001, SOC2, ISAE 3402)?

---

## Disclaimers

> **Disclaimer de Taxa Validada:** faixa de preço indicativa derivada de bill rates (COM impostos, base diária 8h/dia) mapeados da tabela de taxas do contrato Salesforce PS Brasil, validados pelo Solution Lead em 2026-07-19, multiplicados pela base de esforço top-down (duração benchmark × capacidade por classe / roster × horas). Isto é decision-support para planejamento e alocação orçamentária — **não** é estimativa de custo, cálculo de margem, nem compromisso de preço fixo. A taxa offshore R$ 3.500/dia é assumption (não consta na tabela do contrato). Termos comerciais, estrutura de custo, margem e preço final estão sujeitos à avaliação de capacidade da Salesforce PS, seleção do modelo de entrega e negociação comercial formal.

> **Disclaimer de Benchmark (Duração & Capacidade):** faixas de timeline e de equipe derivadas de dados históricos de engajamentos Salesforce PS (model-training-data) via classificação paramétrica do shape do engajamento. Decision-support, não compromisso. Duração real depende de capacidade do lado cliente (aprovações Fase 0, provisionamento de acesso a APIs, velocidade da auditoria de volumetrias), mudanças de escopo e bloqueadores imprevistos. Pessoas são multidisciplinares — headcount tipicamente menor que a contagem de disciplinas. Dimensionamento final requer avaliação de capacidade da Salesforce PS.

---

**Controle do documento:**

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 2026-07-20 | Scopezilla (Dataprev FASE 10) | ROM consolidado — estimativa + timeline + perfis/horas + comparativo dual-track |
