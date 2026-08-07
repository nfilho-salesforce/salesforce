# DATAPREV Data Ágil — Project Summary

**Project Name:** DATAPREV Data Ágil  
**Customer:** DATAPREV (Empresa de Tecnologia e Informações da Previdência — Governo Federal Brasileiro)  
**Vertical:** Public Sector (Government)  
**Created:** 2026-07-18  
**Discovery Phase:** Concluded 2026-07-14  

---

## Executive Summary

A Dataprev opera a tecnologia de praticamente todo o INSS brasileiro e atende ~2.500 clientes B2B (ministérios, entes públicos) e 3.000+ colaboradores internos. O relacionamento com clientes cresceu 166× (de 15 para 2.500 clientes) sem evolução infraestrutural equivalente. Hoje gerencia ~30.000 tickets/mês de atendimento e ~4.500 demandas evolutivas ativas através de sistemas legados (Pronto/ServiceNow para chamados, Clarity/Broadcom para demandas).

**Propósito do projeto:** Criar plataforma de autosserviço e comunicação ativa integrando clientes externos e colaboradores internos aos sistemas da Dataprev via **Slack + Agentforce**, reduzindo dependência de atendimento humano, acelerando resolução de consultas operacionais e melhorando visibilidade executiva sobre pipeline comercial e operacional.

**Resultado esperado:** Redução de 97 minutos/dia/colaborador em consultas repetitivas (métrica Slack oficial), aumento de adoção do CRM comercial (via integração conversacional), melhoria de SLA de resposta a clientes (consultas financeiras e status de chamados em segundos via agente), e ganho de governança sobre processos críticos (alçadas de aprovação, normativas, forecasting).

---

## Arquitetura de Solução — Visão Consolidada

### Stack Tecnológico

| Camada | Tecnologia | Papel |
|--------|-----------|-------|
| **Canal (UX)** | Slack (Ultimate tier — já contratado) | Interface conversacional para clientes externos e colaboradores internos |
| **Orquestração** | Agentforce | Agente nativo Salesforce, orquestra fluxos multi-sistemas, processa linguagem natural |
| **Integração** | MuleSoft / MCP | Camada de APIs sobre sistemas legados (Pronto, Clarity, Protheus, CRM Totvs, portal Conexão) |
| **Sistemas Origem** | ServiceNow (Pronto), Broadcom Clarity, Protheus (ERP), Totvs CRM, Microsoft Teams, Portal Conexão (SharePoint), SEI (gov) | Sistemas de registro mantidos **sem substituição** na Fase 1 |
| **Governança** | Service Cloud (Fase 2+) | Futura camada de visibilidade unificada sobre chamados e demandas |

**Decisão arquitetural crítica:** Agentforce como **orquestrador nativo**, não como camada acima de outro bot. Slack invoca Agentforce diretamente via MCP/API, Agentforce acessa sistemas via MuleSoft e retorna ao Slack. Essa decisão elimina latência de LLM duplicado e mantém a rastreabilidade Salesforce.

**Pivotagem WhatsApp → Slack:** Decisão tomada na reunião de discovery (14/jul/2026), com apoio imediato de Pedro Oliveira e Maik (Dataprev) e respaldo executivo prévio de Saulo (Superintendente). Rationale técnico documentado: governança, segurança, rastreabilidade, integrações nativas, experiência multiplataforma.

---

## Públicos e Volumetria

### 1. Clientes Externos (B2B Institucional)
- **Quem:** Ministérios, autarquias, entes públicos (INSS é o maior, gera maioria dos chamados)
- **Volumetria:** ~2.500 organizações clientes
- **Estimativa de licenças Slack:** ~10.000 (assumindo 2-4 usuários ativos/cliente)
- **Jornadas prioritárias (Fase 1):**
  - J1: Consulta financeira via Protheus (valores em aberto, pagamentos, contratos)
  - J2: Status de chamados do Pronto (quantos abertos, status crítico, SLA)
  - J5: Briefing executivo de projeto via CRM Totvs (preparação pré-reunião executiva)

### 2. Colaboradores Internos (Dataprev)
- **Quem:** Empregados Dataprev (comercial, atendimento N1/N2, TI, executivos)
- **Volumetria:** ~3.000 colaboradores
- **Estimativa de licenças Slack:** ~3.000 (total geral: **~13.000 licenças**)
- **Jornadas prioritárias (Fase 1):**
  - J7: Consulta a normativas internas (portal Conexão: políticas RH, delegação de competência, compliance)
  - J8: Agendamento automático (via Teams/calendário corporativo)
  - J4: Atualização de CRM Totvs via conversação (aumentar adoção de forecast/pipeline)

---

## Roadmap de Jornadas (Discovery Completo)

| ID | Jornada | Público | Sistemas | Prioridade | Fase |
|----|---------|---------|----------|------------|------|
| **J1** | Consulta financeira (valores, pagamentos, contratos) | Clientes | Protheus (ERP) | **Alta** | F1 |
| **J2** | Status de chamados técnicos | Clientes | Pronto (ServiceNow) | **Alta** | F1 |
| **J5** | Briefing executivo de projeto | Internos (executivos) | CRM Totvs | **Alta** | F1 |
| **J7** | Consulta a normativas internas | Internos (todos) | Portal Conexão | **Alta** | F1 |
| **J8** | Agendamento automático | Internos | Microsoft Teams | Média | F1 |
| **J4** | Atualização de CRM por voz/texto | Internos (comercial) | CRM Totvs | Média | F2 |
| **J3** | Abertura de chamado (voz ou texto estruturado) | Clientes + Internos | Pronto | Média | F2 |
| **J6** | Consulta/criação de demandas evolutivas | Clientes + Internos | Clarity | Baixa | F3 |
| **J9** | Análise preditiva de SLA e alertas proativos | Internos (N1/N2) | Pronto + Data Cloud | Baixa | F3 |
| **J10** | Recomendação de próximas ações comerciais | Internos (comercial) | CRM + Data Cloud | Baixa | F3 |

**Lógica de faseamento:**
- **F1 (Quick Wins):** Consultas read-only, zero escrita em sistemas legados, retorno imediato de valor
- **F2 (Expansion):** Escrita controlada (abrir chamado, atualizar CRM), processos transacionais simples
- **F3 (Proactive):** Análise preditiva, alertas proativos, recomendações baseadas em Data Cloud

---

## Mandala de Sistemas (Inventário Completo)

### Sistemas Mapeados

| Sistema | Tipo | Fornecedor | Acesso | Papel no Projeto |
|---------|------|-----------|--------|-----------------|
| **Pronto** | Service Desk | ServiceNow | Internet (clientes + internos) | Gestão de chamados técnicos (~13-14k/mês). **Mantido**, Slack oferece consulta/abertura periférica |
| **Clarity** | Gestão de Demandas | Broadcom | Internet | Gestão de demandas evolutivas (~4.500 ativas). **Mantido**, integração read-only F1, write F2+ |
| **Protheus** | ERP Financeiro | Totvs | Interno | Dados financeiros sensíveis (contratos, pagamentos). Acesso via MuleSoft, governança TI+Jurídico+DPO |
| **CRM Totvs** | CRM Comercial | Totvs | Interno | Pipeline, forecast, contratos macro. ~50 usuários ativos. Baixa adoção → agente conversacional aumenta uso |
| **Portal Conexão** | Intranet/Knowledge | SharePoint (interno) | VPN/Intranet | Normativas, políticas RH, delegação de competência, notícias. ~3k acessos/mês. Read-only via agente |
| **Microsoft Teams** | Comunicação | Microsoft | Internet (AD Dataprev) | Agendas corporativas. Integração Slack → Teams para agendamento automático |
| **SEI** | Processo Administrativo | Gov Federal | Internet | Sistema de assinatura digital de propostas/contratos. Consultivo, sem integração F1 |

### Decisões de Integração Críticas

#### Protheus (ERP Financeiro)
- **Sensibilidade:** Dados financeiros sigilosos, acesso restrito
- **Governança:** TI + Jurídico + DPO da Dataprev devem autorizar perfis de acesso por usuário
- **Solução:** MuleSoft como camada de autorização + log de auditoria. Agente não acessa diretamente banco, passa por API controlada

#### Clarity vs. CRM Totvs (Sobreposição de Demandas)
- **Clarity:** Gestão operacional demanda-a-demanda (N1/N2 executam), volumetria alta (milhares)
- **CRM Totvs:** Visão estratégica macro (contratos, pipeline, forecast executivo), volumetria baixa (~50 usuários)
- **Cenário de conflito:** Se Salesforce virar sistema de origem de demandas (via Service Cloud em F2+), Clarity vira sistema legado de consulta. **Decisão não tomada ainda**, necessária discussão arquitetural em F2.

#### Portal Conexão (SharePoint)
- **Volumetria de conteúdo:** Normativas RH, atos semanais, estrutura organizacional, delegação de competência, PDFs extensos
- **Solução:** Knowledge base Agentforce indexa conteúdo via embeddings, responde perguntas interpretativas ("Quanto tempo de licença paternidade?", "Quem assina proposta de 2 milhões de reais?")
- **KPI:** Redução de acionamentos ao time de Pessoas (RH) por dúvidas normativas repetitivas

---

## Business Objectives e KPIs

### Objetivos Declarados (Discovery)

1. **Reduzir tempo de consultas repetitivas:** "97 minutos/dia economizados por colaborador" (fonte: material Slack oficial, validar antes de uso externo)
2. **Aumentar adoção do CRM:** Comercial atualiza pipeline via conversação (voz/texto), reduz atrito de login manual → melhora qualidade de forecast executivo
3. **Melhorar SLA de resposta a clientes:** Consultas financeiras e status de chamados resolvidas em segundos (hoje dependem de fila N1)
4. **Reduzir erros de compliance:** Consulta automática a delegação de competência elimina alçadas erradas em propostas/contratos
5. **Preparação executiva ágil:** "Maik foi convocado ao ministério, no caminho pergunta ao agente 'Como está projeto X?', chega pautado sem reunião de alinhamento prévia"

### KPIs Propostos (a validar com Dataprev)

| KPI | Baseline Atual | Meta F1 (3 meses) | Fonte de Medição |
|-----|----------------|-------------------|------------------|
| **Tempo médio de resposta a consultas financeiras** | Não medido (assumir fila N1 → 2-4h) | < 1 minuto via agente | Logs Agentforce + Protheus API |
| **Acionamentos ao time de Pessoas (RH) sobre normativas** | Não medido (estimativa: ~X/semana) | -50% (via agente Conexão) | Ticketing interno ou survey |
| **Taxa de adoção CRM (atualização semanal de pipeline)** | ~50 usuários (~30% do comercial) | +40% (via interface conversacional) | Auditoria CRM Totvs |
| **Satisfação colaboradores (NPS interno)** | Baseline a coletar | +20 pontos | Survey pós-F1 |
| **Chamados Pronto resolvidos sem escalação N2** | 80% N1 / 20% N2 | +10% resolução N1 (via self-service) | Métricas Pronto |

**Nota:** Pedro (Dataprev) mencionou que portal Conexão não tem campanha constante de medição de satisfação, mas já houve pesquisa anterior (~5-6 anos atrás, na migração DTPNET → Conexão). Recomendação: coletar baseline NPS/CSAT antes de F1 para comparação pós-implantação.

---

## Timeline e Milestones

### Marcos Confirmados (Discovery)

| Data | Evento | Status | Participantes |
|------|--------|--------|---------------|
| **10 Jul 2026** | Reunião de alinhamento inicial | ✅ Concluído | Salesforce + Dataprev (visão geral, Slack confirmado) |
| **14 Jul 2026** | Reunião de jornadas detalhadas | ✅ Concluído | Mandala de sistemas percorrida, volumetrias levantadas, Change Management incluído |
| **20 Jul 2026** | Prévia de validação de escopo | 📋 Próximo (15h) | Salesforce apresenta solução, cronograma macro, volumetria licenças |
| **22 Jul 2026** | Proposta consolidada e faseada | 💼 Agendado (16h) | Juliana Brites apresenta estimativa esforço + licenciamento + fases |
| **TBD** | Início F1 (Quick Wins) | 🚀 Após aprovação OS | Jornadas J1, J2, J5, J7 priorizadas |

### Cadência de Trabalho (Discovery)

- **Checkpoint semanal:** Quarta-feira (equipe Dataprev Serviço na Ponta) — Maik foi convidado para acompanhar evolução técnica do Slack/Agentforce já em desenvolvimento
- **Alçadas de aprovação:**
  - **Fase 1 (Quick Wins):** Saulo (Superintendente) tem alçada direta
  - **Fase 2+ (Expansion/Proactive):** Requer diretoria (possivelmente presidente, dependendo do valor)

---

## Stakeholders

### Lado Dataprev

| Nome | Papel | Envolvimento | Status |
|------|-------|--------------|--------|
| **Saulo** | Superintendente (Patrocinador Executivo) | Aprova F1, já mencionou Slack antes da discovery | ✅ Confirmado |
| **Pedro Oliveira** | Ponto Focal do Projeto (ou indicará outro) | Coordena lado Dataprev, interface com Salesforce | ⏳ A confirmar indicação |
| **Maik Naveca Lima** | Gerente (Projeto Serviço na Ponta + Data Ágil) | Execução técnica, alinhamento arquitetural | ✅ Ativo |
| **Marcos Alirio** | Especialista Processos + CRM | Entusiasta CRM, governança de processos, Change Management | ✅ Ativo |
| **Responsáveis de Sistemas** | Clarity, Protheus, Pronto, SEI | A envolver (APIs, segurança, autorizações) | ⏳ Pendente |
| **TI / Arquitetura** | Infraestrutura, APIs, Segurança | A envolver (MuleSoft, governança Protheus) | ⏳ Pendente |

### Lado Salesforce

| Nome | Papel | Envolvimento |
|------|-------|--------------|
| **Juliane Lopes** | Arquitetura Estratégica, Discovery, Oportunidades | ✅ Ativo |
| **Juliana Brites** | Relacionamento Comercial, Contratação, OS | ✅ Ativo |
| **Rafael Roquette** | Gerente de Programa, Coordenação | ✅ Ativo |
| **Time Implementação (a alocar)** | Agentforce, Slack, MuleSoft/MCP | ⏳ Pendente alocação |

**Nota crítica:** Pedro enfatizou necessidade de **equipe dedicada separada** do time Serviço na Ponta, para não comprometer qualidade de nenhum dos dois projetos. OS separada dentro do mesmo pool de consumo (alinhamento Juliana Brites confirmado).

---

## Riscos e Constraints

### Riscos Identificados no Discovery

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| **Volumetria de licenças Slack subestimada** | Média | Alto | Pedro inicialmente estimou 3k, depois corrigiu para ~10k (2.500 clientes × 2-4 usuários). Juliana Brites confirmou validação detalhada de termos contratuais antes de iniciar projeto (trauma anterior: "projeto inviabilizado por interpretação dúbia de licenças vezes 1000") |
| **Governança de acesso ao Protheus não definida** | Alta | Alto | Dados financeiros sensíveis requerem autorização TI + Jurídico + DPO por perfil de usuário. Decisão de governança Dataprev, não Salesforce. Bloqueador pré-kick-off F1. |
| **Conflito Clarity vs. Service Cloud como sistema de origem** | Média | Médio | Se Salesforce vira origem de demandas (F2+), Clarity vira legado. Decisão de arquitetura a tomar em F2, impacta modelo de dados e integrações bidirecionais. |
| **Adoção interna (Change Management)** | Média | Alto | Cultura de uso de ferramentas digitais varia. Juliana Brites incluiu Change Management como **pilar formal**, não acessório. Time dedicado Salesforce vai estruturar treinamentos/capacitação. |
| **Workspace Slack único vs. separado (clientes + internos)** | Baixa | Médio | Separar workspaces aumenta controle de segurança mas multiplica esforço de configuração. Workspace único com canais segregados é mais simples, exige políticas de acesso detalhadas. Decisão pendente. |

### Constraints Técnicas

- **Legacy system APIs:** Pronto, Clarity, Protheus, CRM Totvs não têm APIs REST modernas documentadas. Assumir necessidade de camada MuleSoft/MCP customizada com reverse-engineering parcial.
- **Defeso (recesso parlamentar):** Pedro mencionou que projeto precisa de "dono do lado do cliente que não seja engolido pelas demandas do dia a dia quando o defeso terminar". Implicação: equipe dedicada é condição sine qua non para sucesso.
- **Licenciamento já existente (vantagem):** Slack Ultimate já contratado, custo por usuário previsível, sem valor exorbitante. Remove principal risco financeiro levantado por Pedro.

---

## Change Management (Pilar Formal do Projeto)

Juliana Brites (Salesforce) reforçou que Change Management **não é acessório**, entra como escopo dedicado com time exclusivo. Rationale:

> "Não adianta a gente definir as ferramentas, fazer a implementação e não fazer um trabalho forte com as pessoas que realmente têm que usar o Slack. A tecnologia por si só não garante eficiência sem capacitação e suporte para garantir que os colaboradores da Dataprev adotem as novas ferramentas."

### Estratégias de Adoção Identificadas

1. **Customer Zero (precedente Salesforce interno):** Juliane Lopes mencionou experiência interna Salesforce, onde time comercial aumentou adoção de CRM via Slackbot como "source of truth". Usar mesmo modelo na Dataprev.
2. **Executive mandate (Saulo como exemplo):** Saulo (Superintendente) já criou bots internos para validação de documentos (base ChatGPT) e disse: *"Se alguém me perguntar, eu não respondo mais. Vai lá no bot."* Essa postura executiva é crítica para adoção forçada inicial.
3. **Tangibilização precoce:** Maik foi convidado para checkpoint de quarta (Serviço na Ponta) para *"ver a evolução de um dos fluxos que a gente tá desenvolvendo no Slack, para tangibilizar como a coisa tá sendo construída"*. Demonstração real acelera confiança.
4. **Treinamento estruturado:** Time Salesforce vai mapear personas (executivos, N1/N2, comercial, clientes) e criar jornadas de capacitação específicas.

### KPI de Adoção (Change Management)

- **Taxa de uso semanal do Slackbot:** Meta: >60% dos colaboradores internos usam pelo menos 1x/semana até final de F1
- **Redução de resistência (survey):** Baseline a coletar pré-F1, meta: <20% de percepção negativa pós-treinamento

---

## Salesforce Products In Scope

### Confirmados (Discovery)

| Product | Tier/SKU | Uso no Projeto |
|---------|----------|----------------|
| **Slack** | Ultimate (já contratado) | Canal conversacional principal (clientes + internos) |
| **Agentforce** | Standard (a contratar) | Orquestrador nativo, processa linguagem natural, acessa sistemas via MCP |
| **MuleSoft / MCP** | Anypoint Platform (assumir) | Camada de integração sobre legados (Pronto, Clarity, Protheus, CRM) |

### Futuros (Fase 2+)

| Product | Uso Potencial |
|---------|---------------|
| **Service Cloud** | Unificar visibilidade sobre chamados (hoje Pronto) + demandas (hoje Clarity). Decisão arquitetural F2: substituir ou integrar? |
| **Data Cloud** | F3 (Proactive): análise preditiva de SLA, alertas proativos, recomendações comerciais baseadas em padrões históricos |

**Agentforce Product Overlay Detected:** Sim, múltiplas menções a "Agentforce", "Slackbot", "agente IA", "automação via agente". Confirmando overlay de discovery específico para Agentforce (se disponível no products.json).

---

## Compliance & Regulatory

- **Dados sensíveis (Protheus):** Financeiros, contratos, pagamentos. Governança TI + Jurídico + DPO obrigatória (mencionada por Pedro)
- **Público setor (governo federal):** Dataprev é empresa pública, atende ministérios. Assumir requisitos LGPD (Brasil) + normas de segurança gov federal (sem detalhamento específico no discovery).
- **Auditoria de acesso:** Logs de quem acessou quais dados via agente (rastreabilidade Salesforce/MuleSoft) serão requisito de governança.

**Gap identificado:** Nenhuma menção explícita a LGPD, GDPR, ou normas específicas de segurança governo federal. **Recomendação:** Levantar com TI Dataprev + Jurídico na fase de arquitetura detalhada (pré-kick-off F1).

---

## Budget & Funding

### Sinais de Budget (Discovery)

- **Faseamento solicitado por Pedro:** *"Se a gente conseguir fasear, vai ficar mais fácil para as alçadas internas aqui a gente dar celeridade nas aprovações."* → Implicação: budget aprovado em tranches, não lump-sum.
- **Alçada F1 (Saulo):** Superintendente aprova sozinho → assumir budget F1 dentro de sua delegação de competência (valor não revelado, mas inferência: < limiar diretoria).
- **Alçada F2+ (Diretoria/Presidente):** Valores maiores requerem escalação → assumir budget multi-fase total significativo para org pública.
- **Trauma anterior de licenciamento:** Pedro mencionou projeto passado inviabilizado por "interpretação dúbia de licenças × 1000". Juliana Brites garantiu análise detalhada de termos antes de start → Dataprev tem aversão a risco financeiro não mapeado.

**Ordem de grandeza esperada (não confirmada):** Assumir projeto de 6-12 meses, 5-8 FTEs Salesforce, esforço 800-1200h PS + licenças Slack ~10k usuários + Agentforce ~50-100 licenses (clientes corporativos + N1/N2 internos como usuários do agente) + MuleSoft Anypoint.

---

## Handoff Signals (Proposta vs. Delivery)

### Estado Atual: Pré-Proposta

- **Próxima entrega (20/jul/2026):** Juliane Lopes apresenta prévia de solução técnica + cronograma macro + volumetria licenças
- **Proposta final (22/jul/2026):** Juliana Brites apresenta estimativa esforço PS + licenciamento detalhado + faseamento aprovável

### Handoff Futuro: Proposta → Delivery

**Quando aprovar OS:**
1. **Requirements detalhados (Fase 1):** User stories para J1, J2, J5, J7 (4 jornadas prioritárias F1)
2. **Architecture design:** Diagrama de integração MuleSoft/MCP (Pronto, Clarity, Protheus, CRM, Conexão, Teams) + modelo de segurança Protheus
3. **Backlog sprint-ready:** Épicos → Stories → Tarefas técnicas (Agentforce prompts, MCP connectors, Slack workflows)
4. **Acceptance criteria por jornada:** Testes de aceitação usuário final (clientes + internos)

**Artefatos necessários para kick-off delivery:**
- Acesso a ambientes sandbox (Pronto, Clarity, Protheus, CRM Totvs)
- Documentação de APIs legadas (ou acesso a times de produto para reverse-engineering)
- Aprovação de governança TI+Jurídico+DPO sobre acesso Protheus
- Workspace Slack configurado (único vs. separado — decisão pendente)
- Lista nominal de usuários piloto F1 (20-50 early adopters internos + 2-3 clientes piloto)

---

## Open Questions (Para Próximas Reuniões)

### Pendentes com Dataprev

1. **Volumetrias detalhadas (solicitado por Juliane Lopes):**
   - Quantos chamados/mês no Pronto (por tipo: logística, TI interna, cliente)?
   - Quantas demandas/mês no Clarity (abertas, em execução, encerradas)?
   - Quantos acessos/mês portal Conexão (se disponível)?
   - Quantos usuários ativos CRM Totvs (atual) e meta de expansão?

2. **Workspace Slack: único vs. separado?**
   - Clientes externos + internos no mesmo workspace com canais segregados?
   - Ou workspaces separados (mais segurança, mais complexidade)?

3. **Quem é o ponto focal definitivo do projeto (lado Dataprev)?**
   - Pedro Oliveira ou indicado por ele?

4. **Baseline de satisfação (NPS/CSAT)?**
   - Já existe pesquisa recente sobre portal Conexão ou atendimento Pronto?
   - Se não, coletar antes de F1 para comparação pós-implantação?

5. **Pilotos F1: quais clientes e quais colaboradores?**
   - Sugestão: INSS (maior volumetria) + 1-2 clientes menores para validação
   - Internos: time comercial (CRM) + N1 Pronto + 2-3 executivos (briefing)

### Pendentes com Salesforce (Interno)

1. **Validar métricas Slack "97 minutos/dia":** Confirmar fonte oficial antes de uso externo
2. **Licenciamento Agentforce para caso de uso B2B multi-tenant:** Clientes externos (ministérios) acessam via Slack → quantas licenças Agentforce? Modelo de cobrança por conversação vs. por usuário nomeado?
3. **MuleSoft: assumir Anypoint Platform ou propor alternativa MCP-only?** (decisão arquitetural com time de delivery)

---

## Delivery Assumptions (Para Estimativa)

### Sprints & Cadência
- **Sprint:** 2 semanas (padrão Salesforce)
- **FTE workweek:** 40h
- **Duração F1 (Quick Wins):** 8-12 semanas (4 jornadas priorizadas: J1, J2, J5, J7)
- **Duração F2 (Expansion):** 12-16 semanas (3 jornadas: J4, J3, J8 + escrita em sistemas)
- **Duração F3 (Proactive):** 16-20 semanas (3 jornadas: J9, J10, J6 + Data Cloud + analytics)

### Roles Estimados (Ballpark)

| Role | F1 (Quick Wins) | F2 (Expansion) | F3 (Proactive) |
|------|-----------------|----------------|----------------|
| **Solution Architect** | 0.5 FTE (lead técnico, arquitetura MuleSoft/MCP) | 0.3 FTE (refinamento) | 0.2 FTE (Data Cloud design) |
| **Agentforce Specialist / Prompt Engineer** | 1.0 FTE (4 jornadas, prompts, knowledge base) | 0.8 FTE (3 jornadas + refinamento) | 0.5 FTE (analytics + recomendações) |
| **Integration Developer (MuleSoft/MCP)** | 1.5 FTE (5 sistemas: Pronto, Clarity, Protheus, CRM, Conexão) | 1.0 FTE (escrita APIs) | 0.5 FTE (Data Cloud connectors) |
| **Slack Workflow Developer** | 0.8 FTE (workflows conversacionais, UX) | 0.5 FTE (refinamento) | 0.3 FTE (alertas proativos) |
| **QA / Testing** | 0.5 FTE (testes integração + UAT) | 0.5 FTE | 0.3 FTE |
| **Change Management Specialist** | 0.5 FTE (treinamentos, materiais, adoção) | 0.3 FTE (capacitação expandida) | 0.2 FTE (monitoramento adoção) |
| **Project Manager** | 0.3 FTE (coordenação, cerimônias) | 0.3 FTE | 0.2 FTE |

**Total Esforço Estimado (Rough Order of Magnitude):**
- **F1:** ~400-500h PS (8-12 semanas, ~5 FTEs blended)
- **F2:** ~500-600h PS (12-16 semanas, ~4 FTEs blended)
- **F3:** ~400-500h PS (16-20 semanas, ~3 FTEs blended)
- **Total Projeto:** ~1.300-1.600h PS (full lifecycle 36-48 semanas)

**Nota:** Valores acima são ballpark pré-requirements detalhados. Refinamento após reunião 22/jul/2026 com escopo validado.

---

## Success Criteria (Definition of Done — Fase 1)

### Entregáveis Técnicos F1
- [ ] 4 jornadas (J1, J2, J5, J7) funcionais em produção
- [ ] Integração MuleSoft/MCP com 5 sistemas (Pronto, Clarity, Protheus, CRM, Conexão)
- [ ] Knowledge base Agentforce indexada (portal Conexão completo)
- [ ] Workspace Slack configurado (canais, permissões, governança)
- [ ] Logs de auditoria Agentforce + MuleSoft ativos (rastreabilidade)

### Entregáveis Change Management F1
- [ ] Treinamento realizado (20-50 early adopters)
- [ ] Materiais de capacitação (videos, FAQs, guias rápidos)
- [ ] 2-3 clientes piloto onboarded e treinados
- [ ] Survey de satisfação pós-piloto coletado

### KPIs F1 (3 meses pós-go-live)
- [ ] Tempo médio resposta consulta financeira (J1): < 1 minuto
- [ ] Acionamentos RH sobre normativas (J7): -50% vs. baseline
- [ ] Taxa de uso semanal Slackbot: >60% early adopters
- [ ] NPS interno: +20 pontos vs. baseline pré-F1

---

## Contexto Estratégico (Por Que Este Projeto Agora?)

### Crescimento Explosivo Sem Infraestrutura
Dataprev cresceu 166× em base de clientes (15 → 2.500) sem evolução infraestrutural equivalente. Pedro (discovery): *"Esse projeto, como é nós mesmos, interesse nosso, tem tudo para ir pra frente."*

### Janela de Oportunidade (Defeso)
Mencionado que projeto precisa de equipe dedicada "que não seja engolida pelas demandas do dia a dia quando o defeso terminar" → recesso parlamentar cria janela temporal favorável para implantação sem pressão operacional crítica.

### Patrocínio Executivo de Baixo para Cima
Saulo (Superintendente) já defendeu Slack antes da discovery oficial. Maik e Pedro têm autonomia para propor solução técnica. Arquitetura aprovada bottom-up, não top-down → maior chance de adoção real (não é "mais um projeto mandado de cima").

### Reutilização de Arquitetura (Serviço na Ponta)
Infraestrutura Slack + Agentforce já está sendo construída para outro projeto (Serviço na Ponta). Data Ágil é **extensão estratégica**, não greenfield. Reduz risco técnico, acelera delivery, amortiza investimento arquitetural sobre dois casos de uso.

---

## Closing Note

Este projeto tem todos os sinais de um **caso de sucesso iminente:**
- Patrocínio executivo real (não forçado)
- Equipe técnica Dataprev engajada (Maik, Pedro, Marcos)
- Problema de negócio claro e quantificável (166× crescimento sem infra)
- Arquitetura já em construção (Serviço na Ponta)
- Budget implícito (faseamento para facilitar aprovações)
- Timeline definido (reuniões 20/jul e 22/jul confirmadas)

**Próximo passo crítico:** Proposta consolidada 22/jul/2026 deve trazer faseamento claro + estimativa esforço + licenciamento detalhado. Se aprovada, kick-off F1 acontece semanas depois.

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-18  
**Prepared by:** Scopezilla Discovery (Nelson Stebulaitis Filho — Salesforce PS LATAM)  
**Sources:** HTML discovery doc + Gemini meeting notes (14/jul/2026) + meeting transcript (1h08min)  

---

## Appendix: Discovery Artifact Inventory

| Artifact | Type | Date | Status |
|----------|------|------|--------|
| `/discovery-notes/dataprev-data-agil.html` | HTML (comprehensive discovery doc) | 2026-07-14 | ✅ Processed |
| `/discovery-notes/[Data Agil] Jornadas dos Processos - 2026_07_14 16_01 GMT-03_00 - Notes by Gemini.md` | Meeting notes (Gemini) | 2026-07-14 | ✅ Processed |
| `/discovery-notes/[Data Agil] Jornadas dos Processos - 2026_07_14 16_01 GMT-03_00 - Recording.mp4` | Video recording (1h08min) | 2026-07-14 | ⚠️ Not converted (binary) |

**Note on .mp4:** Binary converter unavailable. Transcript was extracted and included in Gemini notes, so content is captured. Video remains as reference for tone/context if needed later.
