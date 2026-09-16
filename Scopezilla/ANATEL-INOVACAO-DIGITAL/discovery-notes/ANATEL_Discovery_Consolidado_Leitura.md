# ANATEL — Descoberta Consolidada (Leitura Completa)
**Data:** 07/07/2026  
**Analista:** Nelson Stebulaitis Filho  
**Fontes:** Google Drive — Pasta de Licenças + Documentos de Discovery

---

## 1. DOCUMENTOS LIDOS E PROCESSADOS

### 1.1 Documentos Estratégicos
- ✅ **Relatório Consolidado: Discovery ANATEL – Respostas e Gaps de Projeto** (Google Doc)
- ✅ **Memória de Projeto: Transformação Digital ANATEL** (Google Doc)
- ✅ **USD - Documento de Escopo Unificado (Unified Scoping Document)** (Google Doc)
- ✅ **Discovery Mapping ANATEL v1** (Google Sheets — 6 abas)

### 1.2 Documentos Técnicos Identificados
- 📄 Manual MMAR-Marítimo_set_25 (múltiplas versões PDF/DOCX/HTML)
- 📄 USB_UNIFIED_SOLUTION_BLUEPRINT_ANATEL_v2.docx
- 📄 ANATEL Digital Transformation Project - Functional Scope Overview.pdf

---

## 2. VISÃO CONSOLIDADA DO PROJETO

### 2.1 Objetivo Estratégico
Modernizar a regulação de telecomunicações no Brasil através da superação da fragmentação sistêmica, migrando de sistemas legados (Mosaico/MMAR, Call Center 1331) para uma arquitetura integrada Salesforce, promovendo:
- **Eficiência Operacional**: Automação de fluxos e redução de TMA
- **Governança e Integridade**: Centralização de dados com rastreabilidade UIT
- **Modernização do Relacionamento**: Peticionamento digital intuitivo
- **Conformidade Normativa**: Alinhamento com RGC, RGL, LGPD

### 2.2 Sizing Geral do Programa
**XL (Extra Large)** — Programa de alta complexidade governamental multi-módulo

---

## 3. OS 4 PILARES FUNCIONAIS (CONFIRMADOS)

### 3.1 MMAR — Licenciamento Marítimo e Aeronáutico
**Sizing:** XL  
**Produto SF:** Public Sector Solutions (PSS) — Licensing & Permitting + BRE

**O que faz:**
- Digitalização completa do Módulo Marítimo e Aeronáutico do sistema Mosaico
- Licenciamento online de estações de rádio para aeronaves e embarcações (médio/grande porte)
- 6 tipos de estação: Embarcação, Embarcação em Teste, Radiobaliza (Física/Virtual), Costeira, Portuária, Móvel

**Complexidade XL justificada por:**
1. **Automação de Regras Legais (Risco Crítico):** Traduzir regras de análise legal do Mosaico legado para BRE Salesforce — documentação incompleta = risco de Functional Alignment Failure
2. **Segurança de Vida:** MMAR lida com segurança marítima e aeronáutica — erro no BRE pode gerar licença ilegal ou bloqueio indevido
3. **Integrações Externas Críticas:** Marinha do Brasil + DECEA — se não houver APIs públicas, será necessário desenvolver adaptadores proprietários
4. **Fluxos Multinível:** Dados técnicos altamente específicos (MMSI, faixas de frequência, DSC, ganho de antenas)

**Ciclo de Vida Automatizado:**
1. **MMAR-CI-01** (Cadastramento): Preenchimento de formulário + validação síncrona via e-mail
2. **MMAR-AT-01** (Aguardando Análise): Entrada automática na fila de distribuição
3. **MMAR-AT-02** (Em Análise): Analista técnico assume → aprova (com/sem débito) ou reprova
4. **MMAR-PG-01** (Aguardando Pagamento): Solicitação aprovada com ônus → aguarda compensação TFI/PPDUR
5. **MMAR-SF-01** (Aguardando Impressão): Baixa bancária identificada → libera botão "Imprimir Licença"
6. **MMAR-SF-02** (Aguardando Arquivamento): Licença gerada → aguarda assinatura de despacho
7. **MMAR-SF-03** (Arquivada): Finalizado + logs imutáveis por 7 anos

**Regras de Onerosidade Financeira:**
| Ação | Onerosidade | Documentação | Observação |
|------|-------------|--------------|------------|
| Inclusão | Sim (TFI + PPDUR) | PDF ≤150MB | Requer homologação de equipamento |
| Alteração | Apenas mudança município | Justificativa técnica | TFI devida se mudar município |
| Exclusão | Não | Dispensa documentação | Baixa imediata da licença |
| Transferência Eletrônica | Não (Taxas) / Sim (PPDUR)* | Aceite via sistema | *PPDUR se receptor não tiver RF |
| Transferência Documental | Não (Taxas) / Sim (PPDUR) | Comprovação de anuência | Para licenças não "marcadas" |
| Renovação | Sim (PPDUR) | Certidões regularidade RF | Extensão validade RF e Licença |

**Motor de MMSI para Boias Virtuais:**
- Cálculo automático de número MMSI direcionado para boias virtuais
- Baseado em coordenadas geográficas decimais dinâmicas
- Conformidade GMDSS/UIT sem validação de equipamento físico

---

### 3.2 TFF/TFI — Arrecadação FISTEL
**Sizing:** L  
**Produto SF:** Revenue Cloud Billing + MuleSoft Batch

**O que faz:**
- Automação da arrecadação anual de taxas de fiscalização
- **TFI** (Taxa de Fiscalização de Instalação): cobrada na inclusão/alteração onerosa de estação
- **TFF** (Taxa de Fiscalização de Funcionamento): cobrada anualmente, vencimento 31/março
- **PPDUR** (Preço Público pelo Direito de Uso de Radiofrequências): cobrado na outorga/renovação de RF

**Volumetria e Processamento:**
- **~10 milhões de registros** processados em lote por ciclo anual
- **Congelamento de dados:** 31/12 (estações fixas) e 20º dia útil do ano (estações em bloco)
- **Fontes de dados:** 3 bancos diferentes
  - SITARWEB (SQL Server)
  - DB_TELECOM (SQL Server)
  - SMS/FISTEL (MongoDB)
- **Mais de 10 sistemas** de origem alimentam essas bases

**Processamento Batch via MuleSoft:**
- 5 milhões de registros de estações divididos em blocos de 50k
- Enriquecimento de preços com base em população (dados IBGE)
- Pipeline: normalização → transformação → consolidação (DataWeave) → deduplicação por chave composta → roteamento para SQL Arrecadação
- Error handling + auditoria + scheduler
- Testes de volume (10M) obrigatórios

**Integração Bancária:**
- GRU (Guia de Recolhimento da União) — modelo atual: emitido pelo site ANATEL
- Modelo futuro: a definir se SF emite boleto diretamente ou orquestra sistema legado
- Conciliação bancária para quitação automática

**Regras Geo-financeiras Automatizadas:**
- Alteração de município = alteração onerosa → gera nova incidência de TFI
- Cálculo dinâmico de PPDUR baseado no prazo de validade escolhido pelo requerente
- Validação de RF ativa na transferência de ativos marítimos

**Gerências Envolvidas (6):**
GIDS, GIMR, GIIB, ORLE, ORER, AFO — fluxo não formalizado, mobiliza ~10 pessoas

**⚠️ PRAZO REGULATÓRIO CRÍTICO:**
Boletos TFF devem ser gerados até 31/março — **NÃO NEGOCIÁVEL**

---

### 3.3 Atendimento Agêntico (Omnichannel)
**Sizing:** XL  
**Produto SF:** Service Cloud + Agentforce + WhatsApp Core + Data Cloud

**O que faz:**
- Unificação de canais digitais de atendimento ao consumidor de telecomunicações
- Visão 360° do Cidadão
- Agentes autônomos de IA Generativa para triagem, classificação e resolução em escala
- Transbordo humanizado e contextualizado para servidores públicos

**5 Canais de Entrada:**
| Canal | Processo de Tratamento |
|-------|------------------------|
| WhatsApp (0800 610 1331) | Registro e consulta automatizada via Chatbot + transição para humano |
| Telefone (1331) | Atendimento humano (Dias úteis, 08h-20h) integrado ao Service Cloud |
| App Anatel Consumidor | Interface mobile para registro de demandas e avaliação de prestadoras |
| Web (Portal) | Área logada para acompanhamento de protocolos e peticionamento eletrônico |
| Presencial (Salas do Cidadão) | Atendimento físico nas capitais para suporte a cidadãos e advogados |

**Regras de Negócio e SLAs:**
- **Travas de Segurança:** Máximo de **3 reclamações/dia** e **15 solicitações/mês** por CPF/CNPJ
- **SLA de Resposta:** Operadoras têm **10 dias corridos (D+10)** para responder
- **Fluxo de Reabertura:** Consumidor pode reabrir **uma única vez** em até 10 dias após resposta da operadora. Novo SLA: **5 dias corridos (D+1)**
- **Retenção de Histórico:** Protocolos online por **6 meses**, gravações por no mínimo **90 dias**

**3 Agentes Inteligentes (Agentforce):**
1. **Agente MMAR/MOSAICO:**
   - FAQ sobre licenciamento marítimo
   - Consulta de status de solicitações
   - Abertura de chamados MMAR
   - Informações sobre pendências

2. **Agente Consumidor:**
   - FAQ sobre reclamações e direitos do consumidor
   - Consulta de status de protocolos
   - Abertura de reclamações/denúncias
   - Avaliação de prestadoras

3. **Agente Ouvidoria:**
   - FAQ sobre Ouvidoria e LAI
   - Consulta de status de manifestações
   - Abertura de demandas de Ouvidoria
   - Informações sobre prazos

**Capacidades RAG (Retrieval-Augmented Generation):**
- Consumo do "Caderno de Respostas" e normativas vigentes
- Lógica Temporal Regulatória (ex: 90 dias guarda de gravações, 10 dias resposta RGC, 5 anos registros Lei 12.850/2013)
- Segurança LGPD: Confirmação de dados (CPF, nascimento, e-mail) antes de liberar informações sensíveis

**GAP Crítico (G03):**
Limites de Autonomia ainda não definidos — quais protocolos (ex: alteração de e-mail, consulta de IMEIs) podem ser encerrados sem intervenção humana?

**Integração Celular Seguro (MJSP):**
- Interoperabilidade com CEMI (Cadastro de Estações Móveis Impedidas)
- Bloqueio Total e Modo Recuperação
- Tempos de resposta das APIs das operadoras não mapeados

**Roteamento Atual:**
Feito de forma manual, por área funcional, conhecimento e especialização (não há algoritmo automático)

---

### 3.4 Ouvidoria Baseada em Dados
**Sizing:** L  
**Produto SF:** Service Cloud / Public Sector Case Management

**O que faz:**
- Ouvidoria que consome nativamente a Visão 360° unificada gerada pelos módulos MMAR, TFF e Atendimento
- Atuação cirúrgica em conflitos
- Controle rigoroso de SLAs regulatórios
- Auditoria pública completa
- Transparência ativa (LAI — Lei de Acesso à Informação)

**Capacidades:**
- Agentes inteligentes para chamados principais
- Painéis de monitoramento de Pados (Procedimentos de Apuração de Descumprimento de Obrigações)
- Rankings públicos de reclamações de operadoras por município/estado
- Tratamento de denúncias anônimas vs. identificadas
- Preservação 100% dos dados de denunciantes

**Nota Importante:**
A Ouvidoria **NÃO** gera visão 360° — ela **CONSOME** a visão gerada pelos outros módulos. As chaves de unificação de identidade entre sistemas legados continuam fragmentadas (pendência técnica).

---

## 4. ECOSSISTEMA DE INTEGRAÇÕES (MULESOFT)

### 4.1 Sistemas Legados a Integrar
| Sistema | Função | Ponto de Integração |
|---------|--------|---------------------|
| **SEI (Anatel)** | Repositório oficial de processos, procurações, peticionamento | Consumo de metadados via APIs REST + upload de PDFs ≤150MB |
| **MOSAICO / MMAR** | Portal de licenciamento Móvel Marítimo e outorgas | Sincronização de status de licenças + validação de Certificados de Homologação |
| **Anatel Busca Ofertas** | Plataforma de comparação de planos (Banda Larga, Móvel) | Submissão de arquivos JSON de ofertas pelas prestadoras (Res. 765/2023) |
| **Anatel Consumidor** | Gestão de reclamações, denúncias, pedidos de informação | Consumo de protocolos + histórico de interações (últimos 6 meses) |
| **Fala.BR** | Plataforma de Ouvidoria e LAI | Integração para desbloqueio de cadastros via Gov.br Prata/Ouro |
| **Painéis de Dados** | BI e visualização de indicadores e Pados | Extração de rankings e dados de qualidade para base da IA |

### 4.2 Gaps Técnicos de Integração
| ID | Gap | Impacto | Status |
|----|-----|---------|--------|
| **G01** | Limites de rate limiting e janelas de manutenção das APIs legadas | 🔴 ALTO | Sem Detalhes |
| **G05** | Camada de antivirus/sandbox para uploads externos no SEI | 🔴 ALTO | Sem Detalhes |

**Risco G01:** Falta de dados sobre TPS (Transações Por Segundo) pode derrubar sistemas legados durante cargas batch de 5M de registros.

**Risco G05:** Upload direto de PDFs ≤150MB sem scanning intermediário expõe ecossistema a brechas cibernéticas.

---

## 5. ARQUITETURA DE DADOS E SEGURANÇA

### 5.1 Autenticação e Acesso
- **Login Único Gov.br:** Acesso mandatório
- **Níveis Prata/Ouro:** Requisitos para desbloqueio via Fala.BR e licenciamento oneroso
- **Usuário Externo SEI:** Cadastro prévio obrigatório via Termo de Concordância e Veracidade (Manual MMAR p.4)
- **IdP Corporativo ANATEL:** Não confirmado — LDAP, Azure AD ou Gov.br? (GAP Q-ANA-TEC-04)

### 5.2 Retenção e Auditoria
- **7 anos:** Retenção obrigatória de dados fiscais/regulatórios
- **Estratégia:** Big Objects + Salesforce Shield (Platform Encryption + Event Monitoring)
- **10 anos:** Auditoria de logs para sigilo fiscal
- **GAP Q-ANA-TEC-02:** Online vs. cold storage não definido

### 5.3 Segurança (LGPD + Sigilo Fiscal)
- **Salesforce Shield Core Deployment:** Obrigatório
- **Platform Encryption:** Criptografia em repouso de dados protegidos por sigilo fiscal
- **Event Monitoring:** Auditoria de exportação de relatórios
- **GAP Q-ARQ-05:** Campos específicos que exigem criptografia em nível de campo não mapeados

### 5.4 Volumes de Dados
- **MMAR:** ~5 milhões de registros ativos + históricos (MongoDB)
- **TFF/TFI:** ~10 milhões de registros processados por ciclo anual
- **Atendimento:** Volumetria não especificada (histórico 6 meses online)
- **Complexidade do Modelo:** Alta — 13 tabelas customizadas no Service Cloud Object Model

---

## 6. PRODUTOS SALESFORCE MAPEADOS

### 6.1 Núcleo de Engajamento e IA
- **Service Cloud - Agentforce 1 Edition:** 38 Users (Curadoria de IA)
- **Flex Credits Atendimento:** 1.270M Créditos Conversacionais
- **Agentforce:** 3 agentes inteligentes externos (MMAR, Consumidor, Ouvidoria)

### 6.2 Automação de Contratos e Outorgas
- **Salesforce Contracts - Unlimited Edition:** 14 Editores
- **Salesforce Shield:** Platform Encryption + Retenção 10 anos

### 6.3 Orquestração de Dados e Marketing
- **Customer Data 360 Starter & Flex Credits:** 260k Perfis Unificados
- **Marketing Cloud Engagement Enterprise:** 3 jornadas planejadas
  1. Renovação de Outorga (integração CLM → MC Journey Builder → ação D-0)
  2. Adimplência TFF/TFI (dados de vencimento via MuleSoft)
  3. Onboarding Novo Licenciado (trigger em aprovação de outorga no CLM)
- **WhatsApp Message Credits:**
  - Marketing: 8.760 pacotes de 1.000 mensagens (5.865 MMAR, 1.710 Atendimento, 1.000 TFF, 185 Ouvidoria)
  - Utilities: 3.035 pacotes de 1.000 mensagens (1.915 MMAR, 560 Atendimento, 500 TFF, 60 Ouvidoria)

### 6.4 Integração e Analytics
- **MuleSoft Anypoint Platform Base (Titanium):** Cores Dedicados (4 Pre-Prod / 4 Production)
- **Tableau Cloud Plus:** 10 Creators / 10 Explorers / 10 Viewers
  - Painéis: Observability Agentes + TFF/TFI (2 painéis com 8 métricas/KPIs cada)

---

## 7. ESTIMATIVA DE ESFORÇO CONSOLIDADA

### 7.1 Estimativa v2 (Última Revisão — Google Sheets)

**RESUMO GERAL:**
- **Total de Horas:** 9.620 horas
- **Custo Base (sem impostos):** R$ 7.042.239,60
- **Custo com Impostos:** R$ 7.535.836,92
- **% Gestão:** 18,77% (1.520 horas de PM)

### 7.2 Detalhamento por Frente

#### Frente 1 — AGENTES + MULESOFT de ATENDIMENTO
- **Horas Totais:** 3.790 horas
- **Custo:** R$ 2.939.797,32 (com impostos)
- **% do Total:** 39,4%
- **Duração:** 13 semanas (S1-S13)

**Perfis:**
- Project Manager: 480h
- Solution Architect: 300h
- Technical Architect: 390h
- Experience Architect: 230h
- Developer: 1.080h (3 devs)
- Quality Assurance Consultant: 240h
- MuleSoft Technical Architect: 350h
- MuleSoft Technical Consultant: 720h (2 consultores)

**Marcos de Entrega:**
- S1-S2: SETUP
- S3-S4: Orquestrador
- S5: APIs Gov.br + FAQ
- S6-S10: Desenvolvimento dos 3 Agentes (MMAR, Consumidor, Ouvidoria) + APIs de integração
- S11-S12: UAT e Deploy
- S13: Observability e Fine-tune

---

#### Frente 2 — CLM (Contracts & Licensing Management)
- **Horas Totais:** 2.630 horas
- **Custo:** R$ 2.096.791,44 (com impostos)
- **% do Total:** 27,3%
- **Duração:** 15 semanas (S1-S15)

**Perfis:**
- Senior Project Manager: 600h (cross-project)
- Solution Architect: 350h
- Technical Architect: 320h
- Experience Architect: 240h
- Solution Consultant: 400h
- Technical Consultant: 440h
- Quality Assurance Consultant: 120h
- MuleSoft Technical Consultant: 160h

**Marcos de Entrega:**
- S1-S4: Discovery, Define, Design — Setup, modelagem de dados, permissões, sandbox
- S5-S6: Templates dinâmicos (5 modelos) + fluxo de 5 etapas + Integração MuleSoft/MOSAICO (2 APIs) + Shield
- S7-S10: Aprovação multi-nível + alertas/notificações + versionamento + suporte migração de Contratos legados ATIVOS
- S11-S12: QA, UAT, ajustes, relatórios OOTB
- S13-S15: Go-live support, handover

**Premissas CLM:**
- 5 templates dinâmicos (médio)
- Aprovação multi-nível (gerente + jurídico + diretoria)
- **FORA:** Assinatura digital ICP-Brasil/DocuSign, Track changes com contraparte, >2 fluxos de aprovação, >5 templates

---

#### Frente 3 — MC (Marketing Cloud)
- **Horas Totais:** 1.350 horas
- **Custo:** R$ 1.026.361,90 (com impostos)
- **% do Total:** 14,0%
- **Duração:** 11 semanas (S0-S10)

**Perfis:**
- Project Manager: 220h
- Marketing Cloud Solution Architect: 250h
- Marketing Cloud Technical Architect: 120h
- Technical Consultant: 560h (2 consultores)
- Quality Assurance Consultant: 200h

**Marcos de Entrega:**
- S0-S3: Setup MCE, WABA, domínio de e-mail, arquitetura de DEs
- S4-S7: Jornada 1 (Renovação de Outorga) + integração CLM → DE + ação D-0
- S4-S7: Jornada 2 (Adimplência TFF/TFI) + templates e-mail
- S6-S9: Jornada 3 (Onboarding) + NPS + relatórios OOTB
- S6-S9: QA end-to-end, UAT, ajustes, go-live

**Premissas MC:**
- Criativos fornecidos pelo cliente (ANATEL) — PS faz apenas configuração técnica
- ~5M contatos/entidades reguladas
- **FORA:** Criação de criativos/copywriting, aprovação WABA (responsabilidade cliente), >3 jornadas, canais além de E-mail/WhatsApp

---

#### Frente 4 — MULESOFT TFF (Batch Arrecadação)
- **Horas Totais:** 1.150 horas
- **Custo:** R$ 929.217,98 (com impostos)
- **% do Total:** 12,0%
- **Duração:** 14 semanas (S0, S5-S17)

**Perfis:**
- Project Manager: 80h (sobreposição com PM de Agentes)
- MuleSoft Technical Architect: 420h
- MuleSoft Solution Architect: 210h
- MuleSoft Technical Consultant: 440h

**Marcos de Entrega:**
- S5-S7: Design de arquitetura, setup de environment, definição da chave composta
- S8-S9: Conectores MOSAICO (legacy — maior risco) + DB_TELECOM (SQL Server)
- S10-S11: Conectores SITARWEB (REST) + SMS/FISTEL (MongoDB)
- S12-S13: Pipeline de normalização + transformação + consolidação (DataWeave)
- S14-S15: Deduplicação por chave composta + roteamento para SQL Arrecadação + Error handling + auditoria + scheduler
- S16-S17: QA end-to-end, testes de volume (10M), ajustes, go-live

**Complexidade:**
- Chave composta para deduplicação (maior variação de esforço)
- MOSAICO via banco direto (JDBC/proprietário) — sem API
- Documentação parcial de APIs (🔴 RISCO ALTO)

---

#### Frente 5 — TABLEAU (Analytics)
- **Horas Totais:** 700 horas
- **Custo:** R$ 543.668,27 (com impostos)
- **% do Total:** 7,3%
- **Duração:** 9 semanas (S0, S10-S17)

**Perfis:**
- Project Manager: 140h (sobreposição com PM de MC)
- Analytics Technical Architect: 200h
- Technical Consultant: 280h
- Quality Assurance Consultant: 80h

**Marcos de Entrega:**
- S10-S11: Setup Tableau Cloud + discovery analítico das 2 fontes (Mosaico + Arrecadação)
- S12-S13: Pacote Observability para os Agentes + Conexões das 2 fontes
- S14-S16: Desenvolvimento de 2 painéis TFF/TFI (8 métricas e KPIs por painel)
- S17: UAT e Deploy

---

### 7.3 Distribuição de Esforço por Perfil (Consolidado)

**Perfis de Gestão:**
- Senior Project Manager (CLM cross): 600h
- Project Manager (distribuído): 920h
- **Total Gestão:** 1.520h (18,77%)

**Perfis de Arquitetura:**
- Solution Architect: 650h
- Technical Architect: 710h
- MuleSoft Solution Architect: 210h
- MuleSoft Technical Architect: 770h
- Marketing Cloud Solution Architect: 250h
- Marketing Cloud Technical Architect: 120h
- Analytics Technical Architect: 200h
- Experience Architect: 470h
- **Total Arquitetura:** 3.380h (35,1%)

**Perfis de Desenvolvimento:**
- Developer: 1.080h
- Technical Consultant: 1.280h
- MuleSoft Technical Consultant: 1.160h
- Solution Consultant: 400h
- **Total Desenvolvimento:** 3.920h (40,7%)

**Perfis de Qualidade:**
- Quality Assurance Consultant: 520h
- **Total QA:** 520h (5,4%)

---

## 8. GAPS CONSOLIDADOS (PRIORIZAÇÃO CRÍTICA)

### 8.1 Gaps de ALTO Impacto (Bloqueadores)

| ID | Bloco | Pergunta/Gap | Risco | Status |
|----|-------|--------------|-------|--------|
| **G01** | Integração | Limites de rate limiting e janelas de manutenção das APIs legadas | Indisponibilidade do Ecossistema | 🔴 SEM DETALHES |
| **G03** | Agentforce | Limites de autonomia para encerramento de chamados sem validação humana | Brecha de Segurança (LGPD) | 🔴 SEM DETALHES |
| **G05** | Integração | Camada de antivirus/sandbox para uploads externos no SEI | Ataque Cibernético | 🔴 SEM DETALHES |
| **Q-ANA-AUT-01** | MMAR | Regras de análise legal do Mosaico para automação (BRE) | Functional Alignment Failure | 🔴 SEM DETALHES |
| **Q-ANA-AUT-04** | Arrecadação | SF emite GRU ou orquestra sistema legado? | Falha na Arrecadação FISTEL | 🔴 SEM DETALHES |
| **Q-ANA-TEC-04** | Segurança | IdP corporativo ANATEL (LDAP, Azure AD, Gov.br)? | Bloqueio de Acesso SSO | 🔴 SEM DETALHES |

### 8.2 Gaps de MÉDIO Impacto

| ID | Bloco | Pergunta/Gap | Risco | Status |
|----|-------|--------------|-------|--------|
| **G02** | Arrecadação | Lógica de PPDUR na transferência — validade proporcional ou cálculo integral? | Litígio Regulatório | 🟡 SEM DETALHES |
| **G04** | MMAR | UI dinâmica para Boias Físicas vs. Virtuais | Confusão de Usuário | 🟡 SEM DETALHES |
| **Q-ANA-AUT-02** | MMAR | APIs Marinha do Brasil e DECEA disponíveis? | Aumento de Escopo | 🟡 PARCIAL |
| **Q-ANA-AUT-03** | Arrecadação | Fórmulas TFI/TFF completas (variações regionais, inflação, multas) | Cálculos Incorretos | 🟡 PARCIAL |
| **Q-ANA-TEC-01** | Arquitetura | Federação de dados para visão 360° | Visão Incompleta | 🟡 PARCIAL |
| **Q-ANA-TEC-02** | Arquitetura | Retenção 7 anos — online vs cold storage | Custo Elevado | 🟡 SEM DETALHES |

### 8.3 Gaps de BAIXO Impacto

| ID | Bloco | Pergunta/Gap | Risco | Status |
|----|-------|--------------|-------|--------|
| **G06** | Governança | Expurgo de IMEIs bloqueados após 5 anos (Lei 12.850/2013) | Não Conformidade Legal | 🟢 SEM DETALHES |
| **Q-ANA-SRV-01** | Atendimento | Árvores de decisão e top motivos de chamado | Agente Mal Calibrado | 🟢 SEM DETALHES |
| **Q-ANA-SRV-02** | Atendimento | Canais digitais Dia 1 (só WhatsApp confirmado) | Experiência Incompleta | 🟢 PARCIAL |
| **Q-ANA-TEC-03** | Arquitetura | APIs para Gov.br, TCU | Integração Futura | 🟢 PARCIAL (Resposta: Não) |

---

## 9. GOVERNANÇA E BASES LEGAIS

### 9.1 Arcabouço Regulatório
- **Resolução nº 715/2019:** Certificação e homologação de produtos
- **Resolução nº 765/2023 (RGC):** Direitos do consumidor e obrigações de atendimento
- **Resolução nº 777/2025 (RGST):** Regulamento Geral dos Serviços de Telecomunicações
- **Resolução nº 719/2020 (RGL):** Regras gerais para licenciamento de estações
- **Lei nº 12.965/2014 (Marco Civil):** Neutralidade de rede e proteção de logs
- **Lei nº 12.527/2011 (LAI):** Prazos e transparência ativa
- **Lei nº 12.850/2013:** Retenção de registros de chamadas por 5 anos
- **LGPD:** Proteção de dados pessoais e sigilo fiscal

### 9.2 Gerências Mobilizadas (6)
- **GIDS** — Gerência de Infraestrutura e Dados de Suporte
- **GIMR** — Gerência de Infraestrutura Móvel e Rádio
- **GIIB** — Gerência de Infraestrutura de Banda Larga
- **ORLE** — Outorgas e Licenciamento (Leste)
- **ORER** — Outorgas e Recursos de Espectro (Regional)
- **AFO** — Administração Financeira e Orçamentária

---

## 10. ROADMAP E TIMELINE

### 10.1 Cronograma Macro (USD)
**Duração Total:** 38 semanas consecutivas (metodologia ágil)

**Fase 1: Discovery & Blueprint Técnico (Semanas 1-6)**
- Mapeamento refinado de arquitetura SOA
- Saneamento dos gaps de alto impacto
- Congelamento de escopo

**Fase 2: Build & Configuration Iterative (Semanas 7-26)**
- Desenvolvimento paralelo dos Salesforce Screen Flows
- Motores de arrecadação financeira
- Barramento de APIs MuleSoft
- Calibração das intenções do Agentforce

**Fase 3: Testing, Homologação & SIT (Semanas 27-32)**
- Testes integrados de carga Omnichannel
- Simulação de processamento massivo batch de 5M de estações
- Validação dos mecanismos de criptografia Shield

**Fase 4: Data Migration, Cut-Over & Go-Live (Semanas 33-38)**
- Carga final de dados históricos da UIT/1331
- Transição de acessos Gov.br
- Desligamento definitivo dos formulários manuais do SEI

### 10.2 Marcos Estratégicos (Milestones)

**M1 [Semana 12]: Unificação de Canais Digitais (Omnichannel)**
- Entrada em produção da infraestrutura unificada
- WhatsApp + Call Center 1331 + Salas do Cidadão corporativas

**M2 [Semana 24]: Virada Sistêmica da Arrecadação Marítima**
- Substituição completa do módulo MMAR legado
- Workflows automatizados integrados com emissão eletrônica de TFI
- Motor MMSI para boias virtuais

**M3 [Semana 38]: Automação Total de Peticionamento e Desligamento Legado**
- Migração completa de dados históricos
- Ativação final dos agentes inteligentes
- Homologação de encerramento do blueprint

### 10.3 Roadmap Alternativo v3 (Memória de Projeto — 5 Fases)
**Duração Total:** ~18 meses | Início previsto: Abril/2026

| Fase | Módulo | Duração | Go-Live | Outcome |
|------|--------|---------|---------|---------|
| **F0** | Fundação & Data Model | 10 sem | Jun/2026 | "A ANATEL enxerga o cidadão pela primeira vez em um único lugar" |
| **F1** | Omnichannel Agêntico | 16 sem | Out/2026 | "O cidadão resolve sozinho. O servidor atende com contexto completo." |
| **F2** | TFF/TFI Arrecadação Inteligente | 21 sem | **Mar/2027** 🔴 | "Reduzir inadimplência antes do prazo de março." |
| **F3** | MMAR Licenciamento Digital | 18 sem | Ago/2027 | "Licença marítima e aeronáutica emitida em horas, não semanas." |
| **F4** | Ouvidoria 360° & Inteligência | 13 sem | Nov/2027 | "A ANATEL decide com dados. O cidadão tem resolução cirúrgica." |

**⚠️ PRAZO REGULATÓRIO CRÍTICO (F2):**
Go-live planejado para **início de março/2027** — 4 semanas antes do prazo legal de 31/março para geração de boletos TFF. Prazo não negociável.

---

## 11. RISCOS DO PROGRAMA (CONSOLIDADOS)

| Risco | Prob. | Impacto | Mitigação |
|-------|-------|---------|-----------|
| **Prazo TFF 31/março não respeitado** | Média | 🔴 Crítico | Go-live Fase 2 em início de março — 4 semanas de margem |
| **Qualidade dos dados nas 3 fontes TFF** | Alta | 🔴 Alto | Data profiling na Fase 0; Data Cloud com regras de qualidade |
| **Documentação parcial APIs MuleSoft** | Alta | 🔴 Alto | Discovery técnico obrigatório antes do kick-off |
| **MOSAICO via banco direto (sem API)** | Média | 🔴 Alto | Confirmar acesso e permissões de leitura |
| **Regras MMAR não documentadas** | Média | 🔴 Alto | Risco de Functional Alignment Failure |
| **Lead time licenciamento OmniStudio** | Média | 🔴 Alto | Aquisição obrigatória durante Fase 1 |
| **Aprovação Meta WhatsApp Business** | Média | 🔴 Alto | Processo iniciado Fase 0; email como fallback |
| **Resistência ao change management (6 gerências)** | Alta | 🔴 Alto | Sponsor executivo + UX HCC nas Fases 0, 1 e 3 |
| **API do Mosaico indisponível/sem documentação** | Média | 🔴 Alto | Discovery técnico do Mosaico durante Fase 2 |
| **Regras TFF com alta variabilidade não mapeada** | Alta | 🔴 Alto | Discovery dedicado antes Fase 2; motor fiscal permanece externo |
| **Chave composta com exceções** | Média | 🟡 Médio | Mapear casos sem chave válida no data profiling |
| **Schema destino "premissa"** | Média | 🟡 Médio | Validar formalmente com equipe ANATEL |

---

## 12. PREMISSAS CRÍTICAS DO PROGRAMA

### 12.1 Licenciamento (Pré-Kick-off)
- ✅ MuleSoft licenciado antes do kick-off Fase 0
- ✅ Data Cloud licenciado antes do início Fase 2
- ⚠️ OmniStudio (Industries/Vlocity) licenciado antes Fase 3 — **aquisição deve iniciar na Fase 1**
- ✅ CRM Analytics (Tableau CRM) licenciado antes Fase 4
- ⚠️ WhatsApp Business API (Meta): aprovação iniciada na Fase 0

### 12.2 Acesso a Dados (Fase 2)
- ✅ Acesso às 3 bases TFF (SITARWEB, DB_TELECOM, MongoDB) garantido
- ⚠️ Regras de cálculo TFF **documentadas**
- ⚠️ API do Mosaico **documentada**

### 12.3 Governança
- ✅ PO dedicado ANATEL com poder de decisão em todas as fases
- ✅ Sponsor executivo com autoridade sobre as 6 gerências (GIDS, GIMR, GIIB, ORLE, ORER, AFO)

---

## 13. EXCLUSÕES DE ESCOPO (FORA DO PROJETO)

### 13.1 MMAR
- ❌ Integração com Marinha do Brasil (se não houver API pública)
- ❌ Integração com ANAC (Aviação Civil)
- ❌ Integração com Receita Federal
- ❌ Assinatura digital ICP-Brasil
- ❌ Módulo aeronáutico se regras divergirem (fase incremental)

### 13.2 TFF/TFI
- ❌ Motor de cálculo fiscal (permanece externo ao MuleSoft)
- ❌ SIAFI
- ❌ Contestação ou recurso de TFF
- ❌ Histórico de cálculos anteriores à migração
- ❌ Mais de 5 etapas de consolidação/transformação
- ❌ Mais de 4 fontes de origem

### 13.3 CLM
- ❌ Assinatura digital ICP-Brasil ou DocuSign
- ❌ Track changes / redline com participação da contraparte
- ❌ Negociação de cláusulas com sugestões externas
- ❌ Mais de 2 fluxos de aprovação
- ❌ Mais de 5 templates
- ❌ Relatórios customizados com KPIs específicos
- ❌ Integração com SEI, SIAFI ou outros sistemas além de MOSAICO/MuleSoft

### 13.4 Marketing Cloud
- ❌ Criação de criativos, copywriting ou design de templates
- ❌ Aprovação da WABA junto à Meta (responsabilidade do cliente)
- ❌ Mais de 3 jornadas
- ❌ Canais além de E-mail e WhatsApp (SMS, Push, etc.)
- ❌ Personalização avançada com Einstein AI fora das 3 jornadas definidas

### 13.5 Atendimento
- ❌ CTI/PABX
- ❌ SEI/SIPAC
- ❌ Histórico de atendimentos pré-migração
- ❌ Automações financeiras no atendimento

### 13.6 Ouvidoria
- ❌ e-OUV
- ❌ Open Data
- ❌ ML customizado
- ❌ AMS pós-go-live

---

## 14. PERGUNTAS ABERTAS (25 QUESTÕES — GOOGLE SHEETS)

### 14.1 Status das Respostas
- **Respondido:** 14 questões
- **Sem Detalhes:** 7 questões
- **Parcial:** 4 questões

### 14.2 Questões Críticas Sem Detalhes (7)

**Q2 — Marketing Cloud:**
Quais são as campanhas? Qtde e t-shirt size referência. A ANATEL pretende ter especialistas próprios para calibração pós-lançamento? Campanha de atualização cadastral considerada?

**Q6 — Arrecadação:**
Como é feita a conciliação bancária atual da arrecadação da taxa destinada ao FISTEL?

**Q7 — Arquitetura:**
O requisito de retenção de dados por 7 anos exige que os dados fiquem online para relatórios operacionais imediatos ou podem migrar para cold storage?

**Q8 — Segurança:**
Dados fiscais retidos por 7 anos precisam ser criptografados individualmente no nível de campo? Quais campos específicos de dados das entidades reguladas exigem mascaramento ou criptografia via Salesforce Shield?

**Q9 — Segurança:**
Qual é o IdP corporativo da ANATEL — LDAP, Azure AD, ou Gov.br? Existe autenticação MFA vigente para servidores? Qual protocolo — SAML 2.0, OAuth 2.0, ou OIDC?

**Q10 — MMAR:**
Quais são as validações técnicas e de segurança obrigatórias que a automação do Salesforce PSS deve aplicar para dispensar a análise humana na emissão das licenças de rádio marítimo? Quando a análise humana é mandatória por lei?

**Q11 — Arrecadação:**
O sistema de arrecadação legado da ANATEL gera boletos (GRU) externamente ou o Salesforce deverá emitir os códigos de barra de pagamento e consumir os arquivos de retorno bancário para quitação?

---

## 15. AÇÕES ABERTAS — NELSON FILHO (REAVALIADAS)

Com base na leitura completa dos documentos de discovery, as seguintes ações permanecem abertas:

- [ ] **Conversar com Mari ou Fernanda** para definir nível de precisão necessário para a proposta comercial
- [ ] **Compilar perguntas de discovery** (25 questões) e priorizar as 7 Sem Detalhes críticas
- [ ] **Alinhar com Ju, Salas, Line, Gaston e Franco** sobre incertezas técnicas e estratégia de escopo
- [ ] **Comunicar a Ju** o status atual (discovery completo, 7 gaps críticos pendentes) e prazo de entrega
- [ ] **Validar estimativa v2** (9.620h / R$ 7.5M) com time técnico
- [ ] **Confirmar premissas CLM, MC e MuleSoft TFF** com cliente
- [ ] **Preparar materiais para reunião de validação** com ANATEL

---

## 16. PRÓXIMOS PASSOS RECOMENDADOS

### 16.1 Curto Prazo (Esta Semana)
1. **Validar entendimento** com Ju sobre os 7 gaps críticos
2. **Priorizar resolução** dos gaps G01, G03, G05, Q-ANA-AUT-01, Q-ANA-AUT-04, Q-ANA-TEC-04
3. **Agendar workshop técnico** com ANATEL para sanar gaps de integração e segurança
4. **Revisar estimativa v2** com time de arquitetura (especialmente MuleSoft e MMAR)

### 16.2 Médio Prazo (Próximas 2 Semanas)
5. **Preparar documento de premissas** para assinatura da ANATEL
6. **Validar roadmap** — escolher entre USD (38 semanas) ou v3 (18 meses/5 fases)
7. **Confirmar licenciamento** de OmniStudio, Data Cloud, Marketing Cloud, MuleSoft, Tableau
8. **Iniciar processo de aprovação** WhatsApp Business API (Meta)
9. **Mapear sponsor executivo** com autoridade sobre as 6 gerências

### 16.3 Longo Prazo (Pré-Kick-off)
10. **Discovery técnico dedicado** para documentação de APIs (MOSAICO, SITARWEB, DB_TELECOM, MongoDB)
11. **Data profiling** das 3 bases TFF para validar qualidade e chave composta
12. **Calibração de Agentforce** — definir limites de autonomia e tom institucional
13. **Definir estratégia de change management** com as 6 gerências

---

## 17. CONCLUSÃO

**✅ DISCOVERY COMPLETO E PROCESSADO**

Todos os documentos disponibilizados pela equipe de licenças foram lidos e consolidados. O projeto ANATEL — Inovação Digital apresenta:

**Escopo Confirmado:**
- 4 pilares funcionais (MMAR, TFF/TFI, Atendimento Agêntico, Ouvidoria)
- 9.620 horas de esforço PS
- R$ 7.535.836,92 (com impostos)
- 38 semanas (USD) ou 18 meses (Roadmap v3)
- Sizing XL (programa de alta complexidade)

**Riscos Críticos Mapeados:**
- 7 gaps sem detalhes (Alto impacto)
- Prazo regulatório TFF 31/março (não negociável)
- Documentação parcial de APIs legadas
- Regras MMAR não documentadas (risco Functional Alignment Failure)

**Produtos Salesforce Validados:**
- Service Cloud + Agentforce (3 agentes)
- Contracts + Shield
- Data Cloud + Marketing Cloud
- MuleSoft Anypoint Platform (Titanium)
- Tableau Cloud Plus

**Próximo Marco:**
Reunião de validação com ANATEL para sanar os 7 gaps críticos e congelar escopo técnico antes do kick-off da Fase 1.

---

**Documento gerado em:** 07/07/2026  
**Autor:** Nelson Stebulaitis Filho  
**Versão:** 1.0 (Consolidado Final)
