# UNA-FUND1 — Distribuição de Horas por Roles e Macro Entregáveis
**Total do Projeto: 3.612 horas**

---

## 📊 Visão Executiva

| Macro Entregável | Horas Base (OS1) | Horas Adicional (OS2) | Total | % do Total |
|------------------|------------------|-----------------------|-------|------------|
| **1. Project Management & Engagement** | 306h | 84h | **390h** | **10.8%** |
| **2. Technical & Solution Architecture** | 580h | 354h | **934h** | **25.9%** |
| **3. Development & Quality Assurance** | 1.060h | 354h | **1.414h** | **39.1%** |
| **4. Integrations & Interoperability (MuleSoft)** | 400h | 224h | **624h** | **17.3%** |
| **5. Artificial Intelligence (AgentForce)** | 250h | 0h | **250h** | **6.9%** |
| **TOTAL** | **2.596h** | **1.016h** | **3.612h** | **100%** |

---

## 🎯 Distribuição por Macro Entregável

### 1️⃣ Project Management & Engagement (390h | 10.8%)

#### Escopo Base (OS1): 306h
- Planejamento e setup do projeto
- Rituais de governança (kick-off, weekly sync, steering)
- Execução e monitoramento
- Comunicação com Dataprev
- Risk management

#### Escopo Adicional (OS2): 84h
- Governança estendida para complexidade de dados em cloud
- Alinhamento entre times Service Cloud e MuleSoft
- Risk management para armazenamento de dados em nuvem
- Change management procedures

#### Roles Principais:
- **Project Manager (PM)**: Coordenação geral, timeline, riscos
- **Engagement Manager**: Relacionamento com cliente, alinhamento estratégico

---

### 2️⃣ Technical & Solution Architecture (934h | 25.9%)

#### Escopo Base (OS1): 580h
- Arquitetura de alto nível (Zero Persistence Strategy)
- Design de segurança e escalabilidade
- Portal (Experience Cloud) + Case Management (Service Cloud)
- Integração CTI/Comunix
- Estratégia de canais digitais (WhatsApp, Web Chat)

#### Escopo Adicional (OS2): 354h
- Design de data model complexo (Person Accounts)
- Novos Record Types de Case (Denúncia, Informações, Orientação, Manifestação)
- Catálogo de serviços dinâmico
- Regras de segurança e anonimização para dados de denúncia em Salesforce
- Sharing rules para exposição de cases no portal cidadão
- Arquitetura de APIs bidirecionais MuleSoft

#### Roles Principais:
- **Senior Technical Architect (TA)**: 220h no subset Case Management (1.100h)
- **Senior Solution Architect (SA)**: 160h no subset Case Management (1.100h)
- **MuleSoft Technical Architect**: 60h no subset Case Management (1.100h)

**Composição estimada para 934h totais:**
- Senior Technical Architect: ~350h
- Senior Solution Architect: ~300h
- MuleSoft Technical Architect: ~150h
- Architects adicionais (AI, Integration): ~134h

---

### 3️⃣ Development & Quality Assurance (1.414h | 39.1%)

**🔴 Maior alocação de esforço do projeto**

#### Escopo Base (OS1): 1.060h
- Configuração da plataforma Salesforce
- Desenvolvimento de componentes visuais (LWC)
- Lógica de negócio (Apex, Flows)
- Experience Cloud (portal Gov.br)
- Service Console para agentes
- Omni-Channel routing
- Einstein Bot (rule-based)
- Knowledge Base integration
- Ciclos de testes (SIT/UAT)

#### Escopo Adicional (OS2): 354h
- Configuração complexa de Flows/Workflows (até 5 processos)
- Lightning Pages e Dynamic Forms baseados em catálogo de serviços
- Lógica de negócio para regras de obrigatoriedade
- Sharing adjustments para exposição segura de cases no portal
- Ciclo completo de testes (SIT/UAT) para novo motor de case management
- Testes de integração bidirecional com UNA

#### Roles Principais:
- **Technical Consultant (Dev)**: 260h no subset Case Management (1.100h)
- **Quality Assurance Consultant**: 120h no subset Case Management (1.100h)
- **Salesforce Developers**: Desenvolvimento de LWC, Apex, Flows
- **Functional Consultants**: Configuração declarativa, Dynamic Forms

**Composição estimada para 1.414h totais:**
- Technical Consultant (Dev): ~600h
- Senior Technical Consultant: ~400h
- QA Consultant: ~300h
- Functional Consultants (AgentForce): ~114h

---

### 4️⃣ Integrations & Interoperability - MuleSoft (624h | 17.3%)

#### Escopo Base (OS1): 400h
- Construção de APIs na plataforma Anypoint
- Orquestração de fluxo de dados conectando Salesforce ao sistema legado UNA
- APIs para consulta de dados (pull)
- CTI integration com Comunix
- Testes de integração

#### Escopo Adicional (OS2): 224h
- Design e construção de APIs bidirecionais
- Listening no Salesforce para criação/classificação de cases
- Orquestração on-premise para replicar no banco de dados legado UNA
- Manutenção de custódia de dados para Dataprev
- Processos de Upsert bidirecional
- Testes de sincronização perfeita entre Salesforce cloud e UNA on-premise

**Setup Distribution para OS2 (224h):**
- MuleSoft On-Premise Setup: 22% do orçamento adicional (1.016h)
- Design de APIs bidirecionais
- Orquestração on-premise
- Testes de replicação

#### Roles Principais:
- **MuleSoft Technical Architect**: 60h no subset Case Management (1.100h)
- **MuleSoft Technical Consultant (Dev)**: 180h no subset Case Management (1.100h)

**Composição estimada para 624h totais:**
- MuleSoft Technical Architect: ~180h
- MuleSoft Senior Developer: ~270h
- MuleSoft Developer: ~174h

---

### 5️⃣ Artificial Intelligence - AgentForce (250h | 6.9%)

#### Escopo (apenas OS1): 250h
- Criação e configuração de agentes autônomos
- Unificação de dados
- Self-service para cidadãos
- Suporte em tempo real para agentes humanos
- Testes de IA

**Nota:** Nenhuma hora adicional na OS2 — escopo de IA permanece fiel ao foundational, focado estritamente em case management estruturado e storage.

#### Roles Principais:
- **AI Architects**: Design de agentes
- **Functional Consultants (AI)**: Configuração de AgentForce
- **Developers (AI)**: Implementação de lógica de agentes
- **QA (AI focus)**: Testes de comportamento de IA

**Composição estimada para 250h:**
- AI Architect: ~80h
- Functional Consultant (AgentForce): ~90h
- Developer (AI): ~60h
- QA (AI): ~20h

---

## 👥 Distribuição por Role (Consolidada)

### Roles de Liderança e Arquitetura (1.060h | 29.3%)

| Role | Horas Estimadas | % do Total |
|------|-----------------|------------|
| **Senior Technical Architect** | 350h | 9.7% |
| **Senior Solution Architect** | 300h | 8.3% |
| **MuleSoft Technical Architect** | 180h | 5.0% |
| **AI Architect** | 80h | 2.2% |
| **Project Manager** | 150h | 4.1% |
| **SUBTOTAL** | **1.060h** | **29.3%** |

### Roles de Desenvolvimento (1.780h | 49.3%)

| Role | Horas Estimadas | % do Total |
|------|-----------------|------------|
| **Technical Consultant (Dev)** | 600h | 16.6% |
| **Senior Technical Consultant** | 400h | 11.1% |
| **MuleSoft Senior Developer** | 270h | 7.5% |
| **MuleSoft Developer** | 174h | 4.8% |
| **Functional Consultant (AgentForce)** | 90h | 2.5% |
| **Salesforce Developer** | 180h | 5.0% |
| **Developer (AI)** | 60h | 1.7% |
| **UX Designer** | 6h | 0.2% |
| **SUBTOTAL** | **1.780h** | **49.3%** |

### Roles de Qualidade e Gestão (772h | 21.4%)

| Role | Horas Estimadas | % do Total |
|------|-----------------|------------|
| **QA Consultant** | 300h | 8.3% |
| **QA (AI focus)** | 20h | 0.6% |
| **Engagement Manager** | 240h | 6.6% |
| **Project Manager (restante)** | 212h | 5.9% |
| **SUBTOTAL** | **772h** | **21.4%** |

**TOTAL GERAL: 3.612 horas**

---

## 📈 Análise de Distribuição

### Por Tipo de Atividade:

```
┌─────────────────────────────────────────────────────┐
│ DESENVOLVIMENTO & QA                     39.1%      │ ████████████████████████████████████████
├─────────────────────────────────────────────────────┤
│ ARQUITETURA                              25.9%      │ ██████████████████████████
├─────────────────────────────────────────────────────┤
│ INTEGRAÇÕES (MuleSoft)                   17.3%      │ ██████████████████
├─────────────────────────────────────────────────────┤
│ PROJECT MANAGEMENT                       10.8%      │ ███████████
├─────────────────────────────────────────────────────┤
│ INTELIGÊNCIA ARTIFICIAL                   6.9%      │ ███████
└─────────────────────────────────────────────────────┘
```

### Por Nível de Senioridade:

```
┌─────────────────────────────────────────────────────┐
│ DESENVOLVEDORES (Mid-Level)             49.3%      │ █████████████████████████████████████████████████
├─────────────────────────────────────────────────────┤
│ ARQUITETOS & LÍDERES (Senior)           29.3%      │ █████████████████████████████
├─────────────────────────────────────────────────────┤
│ QA & GESTÃO                              21.4%      │ █████████████████████
└─────────────────────────────────────────────────────┘
```

---

## 🔍 Insights Críticos

### 1. Concentração em Desenvolvimento
**39.1% do esforço (1.414h)** está em Development & QA — isso reflete:
- Complexidade de configuração do Service Cloud
- Dynamic Forms baseados em catálogo de serviços
- Lógica de negócio complexa (Flows/Apex)
- Ciclos de teste extensos (SIT/UAT)

### 2. Peso Significativo de Arquitetura
**25.9% (934h)** em Arquitetura — justificado por:
- Zero Persistence Strategy (complexidade arquitetural)
- Design de data model sofisticado (Person Accounts, múltiplos Record Types)
- Regras de segurança e anonimização para dados governamentais sensíveis
- Arquitetura de APIs bidirecionais MuleSoft

### 3. MuleSoft como Espinha Dorsal
**17.3% (624h)** dedicados a integrações — crítico para:
- Manutenção de custódia de dados no sistema legado UNA
- Sincronização bidirecional perfeita
- Orquestração on-premise
- Garantia de conformidade regulatória

### 4. IA Moderadamente Dimensionada
**6.9% (250h)** para AgentForce — escopo conservador porque:
- Foco em Einstein Bot rule-based (não generative AI)
- Knowledge Base integration simples
- Fundação para evolução futura, não autonomous agents complexos no MVP

### 5. Gestão Proporcional
**10.8% (390h)** para PM/Engagement — adequado para:
- Projeto de 3.612h (equivalente a ~7-8 FTEs por 6-8 meses)
- Governança entre múltiplos times (Service Cloud, MuleSoft, AI)
- Risk management para dados sensíveis em cloud governamental

---

## 💰 Implicações Financeiras

### Blended Rate por Macro Entregável:

Assumindo rates LATAM Brasil (c/Imp, fator 0.9345):

| Entregável | Horas | Blended Rate Estimado | Investimento |
|------------|-------|----------------------|--------------|
| **Project Management** | 390h | R$ 845/h | R$ 329.550 |
| **Architecture** | 934h | R$ 879/h | R$ 820.986 |
| **Development & QA** | 1.414h | R$ 715/h | R$ 1.011.010 |
| **MuleSoft Integration** | 624h | R$ 820/h | R$ 511.680 |
| **AI (AgentForce)** | 250h | R$ 750/h | R$ 187.500 |
| **TOTAL** | **3.612h** | **R$ 791/h** (média) | **R$ 2.860.726** |

**Nota:** Blended rates são estimativas baseadas na composição de roles dentro de cada entregável. Rates reais variam por perfil e devem ser ajustados conforme tabela Salesforce PS LATAM vigente.

---

## 🎯 Comparação com UNA-FUND2

| Métrica | UNA-FUND1 | UNA-FUND2 | Diferença |
|---------|-----------|-----------|-----------|
| **Horas Totais** | 3.612h | 488h (v2.0) | +640% |
| **Investimento Estimado** | R$ 2.86M | R$ 2.93M | -2.4% |
| **Duração Estimada** | ~32 semanas | 8 semanas | +300% |
| **Escopo** | Full (OS1+OS2) | Reduzido | FUND1 > FUND2 |

**Análise:** UNA-FUND2 teve **redução de 73%** com IA (488h final vs. tradicional). UNA-FUND1 ainda não aplicou otimização de IA — há oportunidade de **reduzir 30-45%** (vide análise ANATEL anterior).

---

## 📋 Próximos Passos Recomendados

1. ✅ **Validar macro alocação** com stakeholders técnicos
2. ⚙️ **Aplicar otimização de IA** (potencial −30-45% = 1.950-2.530h finais)
3. 📊 **Refinar composição de roles** dentro de cada entregável
4. 💰 **Calibrar blended rates** por entregável para precificação
5. 🗓️ **Definir fases e milestones** (sugestão: 4 fases × 8 semanas = 32 sem)
6. 🔍 **Identificar riscos** por macro entregável
7. 📈 **Gerar ROM v1.0** formatado para apresentação cliente

---

**Documento gerado:** 10/jul/2026  
**Fonte:** NotebookLM Project UNA (33 fontes)  
**Próximo artefato:** ROM-UNA-FUND1-v1.0.md (otimizado com IA)
