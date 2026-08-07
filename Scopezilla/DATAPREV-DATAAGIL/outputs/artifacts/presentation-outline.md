# Apresentação — DATAPREV Data Ágil

**Projeto:** DATAPREV DATAAGIL  
**Audiência:** Sponsors Técnicos + Negócio (mix técnico/negócio Dataprev)  
**Objetivo:** Alinhamento de escopo pré-assinatura SOW  
**Idioma:** Português Brasil  
**Data:** 2026-07-20

---

## Fundações Socráticas

**True Goal**: Alinhar escopo antes de assinatura SOW

**Audience**: Mix de sponsors técnicos e negócio Dataprev (Pedro, Saulo, Maik, equipes TI/Jurídico/DPO)

**Audience Fluency**: Partially fluent — entendem contexto técnico e negócio, mas spelamos capacidades Salesforce na primeira menção e evitamos jargão interno (epic IDs, termos Scopezilla)

**Big Idea**: *Uma plataforma de autosserviço e comunicação ativa, conectando os clientes e empregados da Dataprev aos seus sistemas internos, via Slack + Agentforce, sem depender de horário de atendimento.*

**Logic Chain**: Current → Future → Path (padrão de transformação: onde você está, onde isso leva, como chegamos lá)

**Tone**: Collaborative — "Eis o que ouvimos na discovery, eis o que propomos, vamos alinhar antes de assinar" — convida reação e ajuste

**Produtos Locked**: Slack, Agentforce, Data Cloud, MuleSoft (baseado em knowledge base e strategy.json)

---

## Slide 1: CAPA

**Título**: Data Ágil — DATAPREV  
**Subtítulo**: Plataforma de Autosserviço e Inteligência via Slack + Agentforce

**Conteúdo**:
- Projeto: DATAPREV DATAAGIL
- Audiência: Sponsors Técnicos + Negócio
- Objetivo: Alinhamento de escopo pré-assinatura SOW
- Data: Julho 2026

**Conceito Visual**: Capa limpa, título em destaque, logo Dataprev, sem imagem de fundo  
**Densidade**: Sparse  
**Data Source**: N/A (capa)

**Razão para Existência**: Estabelecer contexto e profissionalismo desde o início.

**Speaker Notes**:
*"Bom dia/tarde. Hoje vamos alinhar o escopo do Data Ágil antes de finalizarmos o SOW. O objetivo é garantir que todos — técnicos e negócio — estejam alinhados sobre o que vamos construir, o que assumimos verdadeiro, e quais são os riscos críticos. Ao final, queremos saber: há algo que precisa ser ajustado antes de assinarmos? Vamos começar entendendo onde a Dataprev está hoje."*

---

## Slide 2: ONDE ESTAMOS HOJE — O CONTEXTO DATAPREV

**Título de Ação**: Crescimento exponencial sem evolução infraestrutural criou gargalos operacionais críticos

**Conteúdo**:
- **166× crescimento de base B2B** (15 → 2.500 clientes: ministérios, INSS, entes públicos) sem escalada equivalente de infraestrutura
- **7 sistemas legados fragmentados** sem camada unificada: Pronto (ServiceNow), Clarity (Broadcom), Protheus ERP, CRM Totvs, Portal Conexão, MS Teams, SEI
- **~30k tickets/mês** gerenciados manualmente, SLA degradado (horas de latência vs. meta <1min)
- **Adoção CRM ~30%** compromete qualidade de forecast executivo
- **Pressão regulatória crescente**: breach 2.8M CPFs (mai/2026), auditoria TCU ativa, mainframe recém-descomissionado (jan/2026)

**Conceito Visual**: Diagrama hub-and-spoke — 7 sistemas desconectados em círculo, sem centro unificador (visual de fragmentação)  
**Densidade**: Balanced  
**Data Source**: `data/strategy.json` (challenges 1-6), `outputs/05-executive-summary.md` (linha 11, 21)

**Razão para Existência**: Estabelecer a dor — audiência precisa sentir a urgência antes de ver a solução.

**Speaker Notes**:
*"Vamos começar pelo contexto. A Dataprev cresceu 166 vezes sua base B2B nos últimos anos — de 15 para 2.500 clientes, incluindo ministérios e o INSS. Mas a infraestrutura não acompanhou esse crescimento. Hoje temos 7 sistemas legados desconectados — cada um com seu login, sua interface, sua lógica. Resultado: 30 mil tickets por mês gerenciados manualmente, SLA degradado, e adoção baixa do CRM comercial, o que compromete a qualidade do forecast executivo. Somado a isso, a pressão regulatória aumentou — tivemos o breach de 2.8 milhões de CPFs em maio, a auditoria TCU está ativa, e o mainframe foi descomissionado em janeiro. Essa fragmentação não é sustentável."*

---

## Slide 3: IMPACTOS NO NEGÓCIO

**Título de Ação**: Fragmentação operacional degrada experiência do cliente e expõe Dataprev a riscos de compliance e competitivos

**Conteúdo**:
- **SLA degradado**: Consultas que deveriam ser instantâneas (valores em aberto, status de chamados) dependem de filas N1 humanas com latência de horas
- **Risco de perda de contratos governamentais**: Expectativas de self-service digital e automação IA tornando-se requisitos tácitos em renovações — SERPRO (estatal similar) já tem automação/IA em produção
- **Baixa produtividade interna**: Sobrecarga N1/N2 com consultas repetitivas consome tempo que poderia ser valor agregado
- **Exposição TCU**: Sem rastreabilidade de consultas financeiras sensíveis (Protheus ERP), risco de não-conformidade em auditorias

**Conceito Visual**: Tabela 2 colunas — Impacto | Consequência (4 linhas, sem cores alarmistas, factual)  
**Densidade**: Balanced  
**Data Source**: `data/strategy.json` (business_impacts), `outputs/05-executive-summary.md` (linha 21-23)

**Razão para Existência**: Traduzir dor técnica em consequências de negócio — risco de receita, compliance, competitividade.

**Speaker Notes**:
*"Essa fragmentação tem impactos concretos no negócio. Primeiro, o SLA está degradado — consultas que deveriam ser instantâneas levam horas porque dependem de filas humanas. Segundo, há risco competitivo: o SERPRO, uma estatal similar, já tem automação e IA em produção. Se não acompanharmos, corremos risco de perder contratos governamentais nas renovações. Terceiro, produtividade: as equipes N1 e N2 estão sobrecarregadas com consultas repetitivas, quando poderiam estar agregando valor. E quarto, exposição ao TCU: hoje não temos rastreabilidade de quem consultou o quê no Protheus — dados financeiros sensíveis. Esse é o risco que viemos resolver."*

---

## Slide 4: JANELA DE OPORTUNIDADE

**Título de Ação**: Momento convergente — pressão + capacidade + mandato executivo alinham agora

**Conteúdo**:
- **Arquitetural**: Mainframe descomissionado (jan/2026) abre janela de modernização sem dependência legada crítica
- **Executivo**: Sponsorship bottom-up já estabelecido — Saulo já championed Slack antes de discovery oficial
- **Operacional**: Recesso parlamentar cria janela de deployment sem pressão operacional crítica
- **Competitivo**: Gap vs. SERPRO em automação/IA — ação agora estabelece paridade tecnológica no setor público federal
- **Regulatório**: Breach recente + auditoria TCU ativa = mandato de governança hardening NOW

**Conceito Visual**: 5 chips verticais lado a lado (Arquitetural / Executivo / Operacional / Competitivo / Regulatório), cada um com ícone + 1 frase  
**Densidade**: Balanced  
**Data Source**: `outputs/05-executive-summary.md` (linhas 23, 29)

**Razão para Existência**: Estabelecer urgência — "por que agora?" precede "o que fazemos".

**Speaker Notes**:
*"Mas há uma boa notícia: várias forças estão convergindo agora. Arquiteturalmente, o mainframe foi descomissionado em janeiro — temos uma janela de modernização aberta. Executivamente, o Saulo já defendeu o Slack internamente antes mesmo da discovery oficial — temos sponsorship estabelecido. Operacionalmente, o recesso parlamentar cria uma janela de deployment sem pressão crítica. Competitivamente, precisamos alcançar o SERPRO. E regulatoriamente, o breach recente e a auditoria TCU ativa criam um mandato para hardening de governança agora. Se não agirmos agora, perdemos essa janela. Então, o que propomos?"*

---

## Slide 5: A VISÃO — PLATAFORMA DE AUTOSSERVIÇO E INTELIGÊNCIA

**Título de Ação**: Uma plataforma conversacional conecta clientes e empregados aos sistemas internos, 24/7, sem depender de horário de atendimento

**Conteúdo**:
- **Slack como Agentic OS**: Interface conversacional unificada substitui 7 logins/sistemas diferentes
- **Agentforce orquestra 9 agentes**: 5 read-only Fase 1, 2 escrita controlada Fase 2, 2 preditivos Fase 3
- **MuleSoft/MCP integra legados**: Camada segura sobre Pronto, Clarity, Protheus, CRM Totvs, Portal Conexão, MS Teams — rastreabilidade LGPD/TCU em cada consulta
- **Data Cloud habilita inteligência preditiva** Fase 3: alertas proativos de breach SLA, recomendações comerciais baseadas em pipeline histórico
- **De reativo para proativo**: Consultas instantâneas (<1min) + alertas antes do problema + recomendações antes da reunião

**Conceito Visual**: Arquitetura em camadas — Slack no topo (camada de engajamento), Agentforce no meio (orquestração), MuleSoft embaixo (integração), 7 sistemas legados na base  
**Densidade**: Balanced  
**Data Source**: `outputs/05-executive-summary.md` (linhas 25-27), `data/epics.json` (E10 description)

**Razão para Existência**: Big Idea visual — "isto é o que vamos construir juntos". Transição de problema → visão.

**Speaker Notes**:
*"A visão do Data Ágil é simples: uma plataforma conversacional que conecta os 2.500 clientes B2B e os 3.000 colaboradores internos aos sistemas que eles precisam — Protheus, Pronto, CRM Totvs, Portal Conexão — tudo via Slack. O Agentforce orquestra 9 agentes inteligentes que entendem contexto e executam ações. O MuleSoft garante integração segura com os legados, com rastreabilidade LGPD/TCU em cada consulta. E na Fase 3, o Data Cloud habilita inteligência preditiva — alertas antes do problema, recomendações antes da reunião. Saímos do modelo reativo de 'esperar ser acionado' para o modelo proativo de 'antecipar e resolver'. Agora vamos ver como chegamos lá."*

---

## Slide 6: ESCOPO — 10 ÉPICAS EM 3 FASES + GOVERNANÇA

**Título de Ação**: Faseamento maximiza ROI precoce e reduz risco — valor na Fase 1, escala na Fase 3

**Conteúdo**:

**Fase 0 — Discovery & Architecture Refinement (pré-requisito)**
- Resolver bloqueador G1002 (governança Protheus TI+Jurídico+DPO)
- Auditoria de volumetrias (capacidade MuleSoft/Agentforce/Heroku)
- Decisões arquiteturais (Workspace Slack segregação, Clarity API)

**Fase 1 — Foundation (Quick Wins, read-only)**
- E01: Consultas Financeiras Self-Service (Protheus ERP)
- E02: Autoatendimento Chamados Técnicos (Pronto)
- E03: Intelligence Executiva Mobile (CRM Totvs)
- E04: Knowledge Base Normativas RH (SharePoint)
- E05: Agendamento Automatizado (MS Teams)

**Fase 2 — Expansion (escrita controlada)**
- E06: Adoção CRM via Conversação (+40% adoção)
- E07: Abertura de Chamados Assistida (Pronto write)

**Fase 3 — Proactive Intelligence**
- E08: Gestão de Demandas Evolutivas (Clarity)
- E09: Intelligence Preditiva (Data Cloud + alertas SLA)

**E10 — Governança/Compliance/CM (cross-cutting todas as fases)**

**Conceito Visual**: Grid 4 colunas (F0/F1/F2/F3) com épicas listadas por coluna, E10 como barra horizontal embaixo atravessando todas  
**Densidade**: Dense  
**Data Source**: `data/epics.json` (10 épicas), `data/roadmap.json` (4 fases)

**Razão para Existência**: Mostrar escopo completo de uma vez — audiência precisa ver a jornada inteira antes de mergulhar nas fases.

**Speaker Notes**:
*"O escopo tem 10 épicas organizadas em 3 fases mais uma Fase 0 obrigatória. A Fase 0 resolve blockers críticos — governança do Protheus, auditoria de volumetrias, decisões arquiteturais. A Fase 1 entrega Quick Wins read-only — 5 jornadas que geram valor imediato e estabelecem confiança. A Fase 2 habilita escrita controlada — adoção do CRM e abertura de chamados. A Fase 3 traz inteligência preditiva — alertas proativos e recomendações. E a épica E10, Governança/Compliance/CM, atravessa todas as fases — rastreabilidade, treinamento, mandato executivo. Vamos detalhar cada fase."*

---

## Slide 7: FASE 1 — QUICK WINS (5 JORNADAS LIVE)

**Título de Ação**: Fase 1 entrega valor imediato e estabelece confiança antes de habilitar escritas

**Conteúdo**:

**O que entra**:
- **J1 — Consultas Financeiras**: Clientes B2B consultam valores em aberto no Protheus via Slack, sem escalação N1. Governança TI+Jurídico+DPO, rastreabilidade LGPD/TCU.
- **J2 — Autoatendimento Chamados**: Status de ~30k tickets/mês Pronto (ServiceNow) — quantos abertos, críticos, SLA, histórico. Reduz dependência fila N1.
- **J5 — Intelligence Executiva**: Maik convocado ao ministério, pergunta ao agente no caminho sobre pipeline CRM Totvs, chega pautado.
- **J7 — KB Normativas**: Consulta automática SharePoint — políticas RH, alçadas de aprovação (quem assina >R$2M?). -50% acionamentos repetitivos ao RH.
- **J8 — Agendamento**: Pedro sai de reunião, manda áudio "Agenda reunião amanhã com X, Y, Z" → MS Teams calendário.

**Critérios de sucesso Fase 1**:
- 5 jornadas live read-only
- Early adopters 20-50 piloto treinados
- Audit trail operacional (todo API call: user ID + timestamp + query/response status)
- Mandato executivo Saulo: >60% uso semanal

**Conceito Visual**: 5 chips de jornada lado a lado (J1/J2/J5/J7/J8), cada um com ícone + caso de uso de 1 frase  
**Densidade**: Balanced  
**Data Source**: `data/epics.json` (E01-E05), `data/roadmap.json` (phase 1 success_criteria)

**Razão para Existência**: Detalhar Fase 1 — audiência precisa sentir o valor tangível ("Maik pautado", "Pedro tranquilo").

**Speaker Notes**:
*"A Fase 1 é sobre Quick Wins e construir confiança. Entregamos 5 jornadas, todas read-only. J1: clientes B2B consultam valores financeiros no Protheus sem depender de N1. J2: autoatendimento de chamados — status dos 30 mil tickets mensais. J5: o Maik é convocado ao ministério, pergunta ao agente no caminho sobre o pipeline, chega pautado. J7: KB de normativas RH — quem assina acima de R$2 milhões? Reduz 50% dos acionamentos repetitivos ao RH. J8: o Pedro sai da reunião, manda um áudio 'Agenda reunião amanhã com X, Y, Z', chega em casa tranquilo. Critério de sucesso: 5 jornadas live, early adopters treinados, audit trail operacional, e mandato executivo do Saulo — acima de 60% de uso semanal. Só depois que a Fase 1 estabelecer confiança, habilitamos escritas na Fase 2."*

---

## Slide 8: FASES 2 E 3 — ESCALA + INTELIGÊNCIA PREDITIVA

**Título de Ação**: Fase 2 aumenta adoção CRM; Fase 3 transforma reativo em proativo

**Conteúdo**:

**Fase 2 — Expansion (Controlled Writes)**
- **J4 — Adoção CRM Conversacional**: Comercial atualiza pipeline/forecast por voz/texto Slack → CRM Totvs. Meta: +40% adoção (baseline 30% → 70% final).
- **J3 — Abertura Chamados Assistida**: Clientes B2B + internos abrem tickets Pronto via Slack (escrita controlada, validação de campos obrigatórios).
- **Dependência**: Fase 1 adoption >60% uso semanal — confiança estabelecida antes de habilitar writes.

**Fase 3 — Proactive Intelligence**
- **J9 — Alertas Proativos SLA**: Data Cloud ingere eventos Pronto → identifica cohort alto risco → Agentforce alerta N2/manager ANTES do breach.
- **J10 — Recomendações Comerciais**: Pipeline histórico CRM Totvs → modelo preditivo → sugestões de próxima ação para comercial (cohort churn-risk).
- **J6 — Gestão Demandas Evolutivas**: Clarity (Broadcom) ~4.5k demandas. Decisão arquitetural Fase 2: co-living (Agentforce escreve Clarity via MuleSoft) OU migração (Service Cloud vira sistema de origem, Clarity vira arquivo consulta).

**Conceito Visual**: Tabela 2 colunas (Fase 2 | Fase 3), 3-4 linhas por coluna com épica + 1 frase de valor  
**Densidade**: Balanced  
**Data Source**: `data/epics.json` (E06-E09), `data/roadmap.json` (phases 2-3 objectives)

**Razão para Existência**: Mostrar escala progressiva — não é só quick wins, tem caminho para inteligência preditiva.

**Speaker Notes**:
*"Fase 2 é sobre escala. Habilitamos escrita controlada: o comercial atualiza o CRM por voz direto no Slack, meta de +40% de adoção. E clientes abrem chamados assistidos no Pronto. Só entramos na Fase 2 se a Fase 1 tiver acima de 60% de uso semanal — confiança estabelecida. A Fase 3 traz inteligência preditiva. O Data Cloud ingere eventos do Pronto e do CRM Totvs. J9: alertas proativos de breach de SLA — o Agentforce avisa o gerente antes do problema estourar. J10: recomendações comerciais — o modelo preditivo sugere a próxima ação para o comercial baseado em pipeline histórico. E temos uma decisão arquitetural importante na Fase 2: o Clarity — 4.5 mil demandas ativas. Decisão: co-living, onde o Agentforce escreve no Clarity via MuleSoft, ou migração para o Service Cloud, onde o Clarity vira arquivo de consulta. Essa decisão é um gate na Fase 2."*

---

## Slide 9: ARQUITETURA TÉCNICA — SLACK AGENTIC OS

**Título de Ação**: Arquitetura nativa Salesforce com governança LGPD/TCU embutida

**Conteúdo**:

**Camada de Engajamento** (topo):
- Slack Enterprise Grid (Agentic OS): 2.500 clientes B2B + 3.000 colaboradores internos
- Slack Connect (B2B), Slack AI KB (J7 Normativas), Workflow Builder (J8 Agendamento)

**Camada de Orquestração** (meio):
- Agentforce: 9 agentes (5 F1, 2 F2, 2 F3) com Atlas Reasoning Engine nativo
- Slack EKM: master keys AWS KMS sob controle CISO
- Rastreabilidade: todo API call logged (user ID + timestamp + query/mutation + response status)

**Camada de Integração** (baixo):
- MuleSoft/MCP dual deployment: Anypoint (governança legados, reutilizável) + MCP Server (Slack-specific federation)
- System APIs: Protheus (ERP), Pronto (ServiceNow), CRM Totvs, SharePoint (Portal Conexão), MS Teams, SEI, Clarity (Broadcom)

**Camada de Inteligência** (Fase 3):
- Data Cloud: streaming Pronto + CRM Totvs → perfis unificados → segmentação → ativação (alertas J9, recomendações J10)

**Conceito Visual**: Diagrama de camadas horizontais empilhadas (4 camadas: Engajamento / Orquestração / Integração / Inteligência), 7 sistemas legados na base  
**Densidade**: Balanced  
**Data Source**: `outputs/02-architecture-reference.md`, `data/epics.json` (E10 description)

**Razão para Existência**: Mostrar "como" tecnicamente — sponsors técnicos precisam ver a stack antes de aprovar.

**Speaker Notes**:
*"Tecnicamente, a arquitetura tem 4 camadas. No topo, o Slack Enterprise Grid — a camada de engajamento onde os 2.500 clientes B2B e 3.000 colaboradores internos interagem. Slack Connect para B2B, Slack AI KB para normativas, Workflow Builder para agendamento. No meio, o Agentforce — orquestra 9 agentes com o Atlas Reasoning Engine nativo. Slack EKM garante que as master keys estão sob controle do CISO. Rastreabilidade LGPD/TCU: todo API call é logged — user ID, timestamp, query, response status. Embaixo, o MuleSoft — dual deployment: Anypoint para governança dos legados e reutilização, MCP Server para federação Slack-specific. System APIs para os 7 legados: Protheus, Pronto, CRM Totvs, SharePoint, MS Teams, SEI, Clarity. E na Fase 3, o Data Cloud ingere streaming do Pronto e CRM Totvs, cria perfis unificados, segmenta, e ativa alertas e recomendações. Stack nativa Salesforce, governança embutida."*

---

## Slide 10: TIMELINE BENCHMARK — 29-54 SEMANAS

**Título de Ação**: Timeline derivado top-down da complexidade do engagement — não é compromisso, é ponto de partida para discussão

**Conteúdo**:

**Faixa benchmark**: 29-54 semanas (Multi-Cloud High)
- **Baseline**: 10 épicas, predominante L/XL (2 XL + 3 L de 10), 7 sistemas legados integrados → 26-40 semanas base
- **Ajustes de risco** (+35% total, sob cap +50%):
  - +15% indústria regulada (LGPD Art. 48 + TCU audit trail + governança Protheus TI+Jurídico+DPO)
  - +10% cliente novo (primeiro engagement Dataprev, qualidade org desconhecida, bloqueador G1002 Protheus não resolvido)
  - +10% alargamento de confiança (68 gaps, bloqueador G1002, volumetrias pendentes, gaps Experience Design e Governança — muitos Unknowns/Assumed)

**Fases indicativas** (se 40 semanas mid-range alocadas):
- F0 Discovery: 4-6 semanas
- F1 Foundation: 12-16 semanas
- F2 Expansion: 10-14 semanas
- F3 Proactive: 8-12 semanas

**Disclaimer**: *Baseado em benchmarks de engagements similares (model-training-data). Não é compromisso — é base para discussão de escopo/prazo. Duração final depende de decisões arquiteturais Fase 0, resolução de gaps, e capacidade de staffing.*

**Conceito Visual**: Barra horizontal com 4 fases coloridas sequenciais (F0/F1/F2/F3), faixa 29-54 semanas acima, ajustes de risco listados embaixo  
**Densidade**: Balanced  
**Data Source**: `.project-metadata.json.timeline.derived`, `data/roadmap.json` (phases)

**Razão para Existência**: Dar senso de magnitude temporal — "alinhamento de escopo" inclui entender duração, mas sem comprometer número antes de Phase 0.

**Speaker Notes**:
*"Sobre timeline: derivamos uma faixa benchmark de 29 a 54 semanas. Baseline é Multi-Cloud High — 10 épicas com predominância L/XL, 7 sistemas legados integrados, o que nos dá 26 a 40 semanas base. Aplicamos 3 ajustes de risco, total de +35%, sob o cap de +50%. Primeiro, +15% por indústria regulada — LGPD, TCU, governança Protheus com TI+Jurídico+DPO. Segundo, +10% por cliente novo — primeiro engagement com a Dataprev, qualidade org desconhecida, bloqueador G1002 ainda não resolvido. Terceiro, +10% por alargamento de confiança — temos 68 gaps, volumetrias pendentes, gaps de Experience Design e Governança. Se alocarmos 40 semanas no mid-range, indicativamente: 4-6 semanas na Fase 0, 12-16 na Fase 1, 10-14 na Fase 2, 8-12 na Fase 3. Importante: isso não é compromisso. É baseado em benchmarks de engagements similares, e é o ponto de partida para discussão. A duração final depende das decisões arquiteturais da Fase 0, da resolução dos gaps, e da capacidade de staffing."*

---

## Slide 11: PRINCIPAIS RISCOS E MITIGAÇÕES

**Título de Ação**: 5 riscos críticos identificados — todos têm mitigação definida ou gate de decisão

**Conteúdo**:

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| **G1002 Protheus governance blocker** — TI+Jurídico+DPO não aprovam acesso a dados financeiros sensíveis | Fase 1 J1 inviável, atraso kick-off | **Phase 0 mandatória**: tri-party meeting pré-kick-off. Fallback: defer J1 para F2, lançar F1 com 4 jornadas (J2/J5/J7/J8) |
| **Experience Design gap** — 10k+ usuários externos onboarding sem UX research | Baixa adoção, rework Fase 1 | Adicionar UX Researcher Phase 0/Phase 1 para service design + content strategy + onboarding journey |
| **Volumetrias desconhecidas** — capacidade Pronto/Protheus/CRM Totvs/Heroku não auditada | Sizing MuleSoft/Agentforce/Heroku errado, over-provisioning ou throttling | Phase 0 audit (2 semanas): volumetrias por sistema, peak load, concurrent users |
| **APIs legados não validadas** — CRM Totvs write, Clarity API, Pronto case creation | Bloqueio técnico Fase 2/3, retrabalho integração | Phase 0 API discovery sprint: Swagger/OpenAPI specs + sandbox credentials + field mapping validate |
| **Governance/CoE indefinido** — ownership multi-team (Agentforce config, MuleSoft APIs, Slack admin, CRM vs Salesforce) | Deadlock operacional pós go-live, ninguém resolve incidents | Phase 0 RACI workshop: roles/responsabilidades locked antes Phase 1 build |

**Conceito Visual**: Tabela 3 colunas (Risco | Impacto | Mitigação), 5 linhas, sem cores alarmistas  
**Densidade**: Dense  
**Data Source**: `data/roadmap.json` (risks per phase), `data/gaps.json` (G1002, G0104, G0102, G0801, G9901)

**Razão para Existência**: Transparência de riscos — "alinhamento de escopo" inclui alinhar no que pode dar errado e como mitigamos.

**Speaker Notes**:
*"Vamos falar de riscos. Identificamos 5 críticos, todos com mitigação definida. Primeiro: G1002, o bloqueador de governança do Protheus. Se TI+Jurídico+DPO não aprovam acesso a dados financeiros, a jornada J1 é inviável. Mitigação: Fase 0 mandatória com tri-party meeting. Fallback: diferir J1 para Fase 2, lançar Fase 1 com 4 jornadas. Segundo: gap de Experience Design. Temos 10 mil usuários externos entrando sem UX research — risco de baixa adoção. Mitigação: adicionar UX Researcher na Fase 0 e Fase 1. Terceiro: volumetrias desconhecidas. Sem auditoria, o sizing do MuleSoft, Agentforce e Heroku pode estar errado. Mitigação: audit de 2 semanas na Fase 0. Quarto: APIs legados não validadas — CRM Totvs write, Clarity, Pronto case creation. Bloqueio técnico na Fase 2/3. Mitigação: API discovery sprint na Fase 0, Swagger/OpenAPI specs, sandbox, field mapping. Quinto: Governance/CoE indefinido. Multi-team ownership não alinhado gera deadlock pós go-live. Mitigação: RACI workshop na Fase 0. Todos esses riscos são endereçados antes de começarmos a Fase 1."*

---

## Slide 12: DISCIPLINAS NECESSÁRIAS

**Título de Ação**: Engagement requer 11 disciplinas — uma pessoa pode cobrir múltiplas roles, múltiplas pessoas podem cobrir uma role

**Conteúdo**:

**Arquitetura e Liderança Técnica**:
- Senior Technical Architect (Salesforce + Security + Governance)
- MuleSoft Technical Architect
- Data Cloud Technical Architect
- Solution Architect (Salesforce + Slack Admin)

**Implementação Especializada**:
- Agentforce Technical Consultant (9 agentes J1-J10)
- MuleSoft Technical Consultant (7 System APIs legados)
- Einstein Analytics Developer (dashboards Fase 3)
- Solution Consultant (BA + Release Manager)

**Qualidade e Adoção**:
- Quality Assurance Consultant (surge hardening F1/F2/F3 go-live)
- UX Researcher (Phase 0/Phase 1 — service design + onboarding 10k+ externos)
- Change Management Lead (treinamento por persona, executive mandate, KPIs adoção)

**Nota**: Headcount não é soma de roles — pessoas são multi-disciplinares. Sizing de equipe e staffing não estão no escopo deste alinhamento; requerem julgamento humano baseado em capacidade Salesforce PS, modelo de entrega, e termos comerciais.

**Conceito Visual**: Grid 3 blocos (Arquitetura / Implementação / Qualidade), roles listadas por bloco com 1 frase de rationale cada  
**Densidade**: Balanced  
**Data Source**: `data/resource-plan.json` (11 roles), `outputs/04-roles.md`

**Razão para Existência**: Mostrar expertise necessária sem criar expectativa de FTE count — guardrail "no team sizing" aplicado.

**Speaker Notes**:
*"Sobre disciplinas: o engagement requer 11 roles organizadas em 3 blocos. Arquitetura e liderança técnica: Senior Technical Architect que cobre Salesforce, Security e Governance; MuleSoft Technical Architect; Data Cloud Technical Architect; Solution Architect que cobre Salesforce e Slack Admin. Implementação especializada: Agentforce Technical Consultant para os 9 agentes; MuleSoft Technical Consultant para os 7 System APIs; Einstein Analytics Developer para dashboards da Fase 3; Solution Consultant que cobre BA e Release Manager. Qualidade e adoção: QA Consultant que surge nos hardenings de go-live; UX Researcher para service design e onboarding dos 10 mil externos; Change Management Lead para treinamento, mandato executivo, KPIs de adoção. Importante: headcount não é soma de roles. Pessoas são multi-disciplinares — uma pessoa pode cobrir múltiplas roles, múltiplas pessoas podem cobrir uma role. Sizing de equipe e staffing não estão no escopo deste alinhamento — requerem julgamento humano baseado em capacidade Salesforce PS, modelo de entrega, e termos comerciais."*

---

## Slide 13: PREMISSAS E EXCLUSÕES

**Título de Ação**: O que assumimos verdadeiro e o que explicitamente NÃO está no escopo

**Conteúdo**:

**Premissas (o que assumimos)**:
- Slack Enterprise Grid já contratado e provisionado
- TI Dataprev fornece Swagger/OpenAPI specs + sandbox credentials para 7 sistemas legados (Pronto, Clarity, Protheus, CRM Totvs, SharePoint, MS Teams, SEI) em Phase 0
- Workspace Slack decisão (B2B segregado vs único workspace) será locked Phase 0
- Volumetrias auditadas Phase 0 — concurrent users, peak load por sistema, data volumes
- AWS KMS master keys disponíveis sob controle CISO para Slack EKM
- Dataprev staffa 0% roles técnicas (100% Salesforce PS)

**Exclusões (o que NÃO está no escopo)**:
- Migração de dados históricos (Pronto tickets, CRM Totvs opportunities, Clarity demands) — apenas integração read/write APIs
- Customizações legados (Protheus, CRM Totvs, Pronto) — integramos "as-is"
- Treinamento usuários finais 2.500 clientes B2B — Dataprev conduz, Salesforce PS treina train-the-trainer
- Licenças Salesforce — assumidas provisionadas separadamente
- Service Cloud migration (E08 Clarity replacement) — decision gate Phase 2, execução fora deste SOW se aprovada

**Conceito Visual**: Tabela 2 colunas (Premissas | Exclusões), 5-6 linhas cada, factual e direto  
**Densidade**: Balanced  
**Data Source**: `data/gaps.json` (assumptions), `outputs/05-executive-summary.md` (assumptions section)

**Razão para Existência**: Evitar surpresas pós-assinatura SOW — "alinhamento de escopo" inclui o que NÃO fazemos.

**Speaker Notes**:
*"Vamos alinhar premissas e exclusões. Premissas — o que assumimos verdadeiro: Slack Enterprise Grid já contratado. TI Dataprev fornece Swagger/OpenAPI specs e sandbox para os 7 legados na Fase 0. A decisão de Workspace Slack — B2B segregado ou workspace único — será locked na Fase 0. Volumetrias auditadas na Fase 0. AWS KMS master keys disponíveis sob controle do CISO para Slack EKM. E Dataprev staffa 0% de roles técnicas — é 100% Salesforce PS. Exclusões — o que NÃO fazemos: não fazemos migração de dados históricos — apenas integração read/write APIs. Não customizamos os legados — integramos as-is. Não treinamos os 2.500 clientes B2B diretamente — Dataprev conduz, nós treinamos train-the-trainer. Licenças Salesforce são provisionadas separadamente. E a migração do Service Cloud — se a decisão na Fase 2 for migrar o Clarity, a execução é fora deste SOW. Alguma premissa ou exclusão que precisa ser ajustada?"*

---

## Slide 14: PRÓXIMOS PASSOS — PHASE 0 OBRIGATÓRIA

**Título de Ação**: Phase 0 resolve blockers críticos antes de Phase 1 build — 4-6 semanas, não pulável

**Conteúdo**:

**O que acontece em Phase 0** (Discovery & Architecture Refinement):
1. **Tri-party meeting TI+Jurídico+DPO** → resolve G1002 Protheus governance blocker. Fallback: defer J1 para F2.
2. **Volumetrias audit** (2 semanas) → Pronto/Protheus/CRM Totvs/Clarity concurrent users, peak load, data volumes. Desbloqueio: sizing MuleSoft/Agentforce/Heroku.
3. **API discovery sprint** (2 semanas) → TI fornece Swagger/OpenAPI specs + sandbox para 7 legados. Field mapping validate (CRM Totvs write, Clarity, Pronto case creation).
4. **Workspace Slack decision** → B2B segregado (Slack Connect externo) vs workspace único. Impacto: licensing + security model.
5. **RACI workshop Governance/CoE** → ownership multi-team locked (Agentforce config, MuleSoft APIs, Slack admin, CRM vs Salesforce).

**Entregáveis Phase 0**:
- G1002 approved ou fallback locked
- Volumetrias documented → capacity plan
- API specs validated → integration backlog
- Workspace Slack locked → licensing model
- RACI documented → governance playbook

**Gate Phase 1**: Phase 0 entregáveis aprovados por sponsors técnicos + negócio antes de Phase 1 kick-off.

**Conceito Visual**: Fluxo sequencial 5 blocos (1→2→3→4→5) com gate no final antes de "Phase 1 Kick-off"  
**Densidade**: Balanced  
**Data Source**: `data/roadmap.json` (phase 0 objectives + success_criteria)

**Razão para Existência**: Deixar claro que Phase 0 não é opcional — 68 gaps + blockers críticos requerem resolução antes de build.

**Speaker Notes**:
*"Fase 0 é mandatória. 4 a 6 semanas resolvendo blockers críticos antes de começarmos a Fase 1. Primeiro: tri-party meeting TI+Jurídico+DPO para resolver o G1002 — governança do Protheus. Se não aprovar, fallback é diferir J1 para Fase 2. Segundo: audit de volumetrias, 2 semanas. Concurrent users, peak load, data volumes por sistema. Desbloqueio: sizing correto de MuleSoft, Agentforce, Heroku. Terceiro: API discovery sprint, 2 semanas. TI fornece Swagger/OpenAPI specs e sandbox para os 7 legados. Validamos field mapping — CRM Totvs write, Clarity, Pronto case creation. Quarto: decisão de Workspace Slack — B2B segregado com Slack Connect externo, ou workspace único? Impacto em licensing e security model. Quinto: RACI workshop de Governance/CoE. Quem é dono do quê? Agentforce config, MuleSoft APIs, Slack admin, CRM vs Salesforce. Entregáveis da Fase 0: G1002 approved ou fallback locked, volumetrias documentadas, API specs validadas, Workspace Slack locked, RACI documentado. Todos esses entregáveis precisam ser aprovados pelos sponsors técnicos e negócio antes de kick-off da Fase 1. Fase 0 não é pulável."*

---

## Slide 15: CALL TO ACTION — ALINHAMENTO E PRÓXIMOS PASSOS

**Título de Ação**: Hoje alinhamos escopo; próximos 10 dias finalizamos comerciais e assinamos SOW

**Conteúdo**:

**O que precisamos alinhar hoje**:
- ✓ Escopo aprovado? 10 épicas em 3 fases + E10 governança cross-cutting
- ✓ Phase 0 obrigatória? 4-6 semanas resolvendo blockers antes de Phase 1
- ✓ Riscos conhecidos e mitigações? Top 5 identificados, gates de decisão definidos
- ✓ Premissas e exclusões? O que assumimos e o que NÃO fazemos

**Próximos passos (10 dias)**:
1. **Hoje**: Feedback e ajustes finais no escopo
2. **Semana 1**: Comerciais finalizados (pricing lane aprovado com Solution Lead)
3. **Semana 2**: SOW redigido e circulado para aprovação
4. **Dia 10**: Assinatura SOW + kick-off Phase 0 agendado

**Pergunta para os sponsors**:
*"Há algo no escopo, premissas, ou riscos que precisa ser ajustado antes de finalizarmos o SOW?"*

**Conceito Visual**: Checklist 4 itens alinhamento + timeline horizontal 4 marcos (Hoje / Semana 1 / Semana 2 / Dia 10) + pergunta em destaque  
**Densidade**: Sparse  
**Data Source**: N/A (call to action)

**Razão para Existência**: Fechar colaborativamente — convidar reação, não impor decisão. Tone collaborative até o fim.

**Speaker Notes**:
*"Para fechar: o que precisamos alinhar hoje? Escopo aprovado — 10 épicas em 3 fases mais E10 governança cross-cutting? Phase 0 obrigatória — 4 a 6 semanas resolvendo blockers antes da Fase 1? Riscos conhecidos e mitigações — top 5 identificados, gates de decisão definidos? Premissas e exclusões — o que assumimos e o que não fazemos? Próximos passos nos próximos 10 dias: hoje, feedback e ajustes finais no escopo. Semana 1, comerciais finalizados — pricing lane aprovado com Solution Lead. Semana 2, SOW redigido e circulado para aprovação. Dia 10, assinatura do SOW e kick-off da Fase 0 agendado. A pergunta para vocês, sponsors: há algo no escopo, premissas, ou riscos que precisa ser ajustado antes de finalizarmos o SOW? Vamos abrir para discussão."*

---

## Fim da Apresentação

**Total de slides**: 15

**Estrutura**:
- Slides 1-4: Current (Situação atual + dor + impacto + janela)
- Slide 5: Future (Visão)
- Slides 6-10: Path (Escopo + fases + arquitetura + timeline)
- Slides 11-15: Path (Riscos + disciplinas + premissas + próximos passos + fechamento)

**Próximos passos para o apresentador**:
- Revisar speaker notes antes da apresentação
- Preparar backup para perguntas técnicas detalhadas (arquitetura MuleSoft, volumetrias)
- Ter `data/gaps.json` e `data/roadmap.json` disponíveis para consulta rápida se sponsors pedirem mais detalhe
- Timeboxing sugerido: 45-60 minutos apresentação + 15-30 minutos Q&A
