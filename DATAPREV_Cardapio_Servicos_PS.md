# Cardápio de Serviços — Salesforce Professional Services
## DATAPREV | Governo Federal Brasil

**Versão:** 1.0 | **Data:** 2026-07-03  
**Contexto:** Serviços especializados para transformação digital no setor público federal

---

## 🎯 Visão Geral

Este cardápio apresenta serviços modulares de Professional Services (PS) Salesforce desenhados para o contexto específico da Dataprev e governo federal brasileiro, considerando:

- ✅ Conformidade LGPD obrigatória (dados sensíveis previdenciários)
- ✅ Licitação pública (Lei 14.133/2021)
- ✅ Integrações com sistemas legados críticos (CNIS, SIAPE, eSocial)
- ✅ Aprovações CTID, ANPD, CGU/TCU
- ✅ Ciclo orçamentário PLOA
- ✅ Idioma: Português (PT-BR) | Moeda: BRL | Imposto: 75,35%

---

## 📋 Categorias de Serviços

**[A] Discovery & Strategy** — Antes da implementação  
**[B] Implementation & Integration** — Entrega core  
**[C] Adoption & Enablement** — Pós-go-live  
**[D] Optimization & Innovation** — Valor adicional  
**[E] Governance & Compliance** — Específico setor público  

---

# [A] DISCOVERY & STRATEGY

## A1. Discovery Workshop & Scoping
**Tagline:** *"Do RFP ao ROM: mapeamento completo de requisitos, riscos e estimativa"*

### O que resolve
- Cliente tem RFP/edital mas precisa traduzir para escopo técnico Salesforce
- Necessidade de ROM estruturado para aprovação CTID/Diretoria
- Incerteza sobre viabilidade técnica ou timeline

### Entregáveis
- Project Summary (contexto, stakeholders, integrações legacy mapeadas)
- Extraction Matrix (requisitos estruturados por épica)
- Mapa de integrações com sistemas legados
- ROM v1.0 (esforço, timeline, investimento c/ e s/ imposto)
- Documento de premissas, riscos e perguntas em aberto
- Site Heroku interativo com navegação SLDS (para apresentação executiva)

### Perfis PS
- Technical Architect (40h)
- Solution Architect (40h)
- Business Analyst (40h)
- Program Manager (20h)

### Exemplo DATAPREV
**DECIPEX** — Discovery de 19 sistemas legados, 9 dores críticas mapeadas, 30 perguntas estruturadas, matriz esforço×valor com 50 diagnósticos. Output: ROM preparado + 2 apps Heroku (diagnóstico + bootcamp).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1 cloud, <5 integrações) | 2-3 semanas | 160-240h | R$ 120k-180k |
| **Medium** (2 clouds, 5-10 integrações) | 3-4 semanas | 240-320h | R$ 180k-240k |
| **Large** (3+ clouds, 10+ integrações, MuleSoft) | 4-6 semanas | 320-480h | R$ 240k-360k |

---

## A2. Architecture Design & Blueprint
**Tagline:** *"Arquitetura de solução detalhada, diagramas técnicos e estratégia de integrações"*

### O que resolve
- Necessidade de validação técnica antes de contratar implementação
- Definir estratégia de integrações com CNIS, SIAPE, eSocial, Conectividade Social
- Aprovação de arquitetura por CTID/time de segurança/ANPD

### Entregáveis
- Documento de Arquitetura de Solução (SAD)
- Diagramas técnicos (arquitetura de integrações, fluxo de dados, segurança)
- Estratégia de residência de dados (Brasil) e conformidade LGPD
- Mapa de dependências e sequenciamento de entregas
- Protótipo de integrações críticas (POC técnica)

### Perfis PS
- Senior Technical Architect (80h)
- MuleSoft Technical Architect (quando aplicável, 40h)
- Solution Architect (40h)
- Program Manager (20h)

### Exemplo DATAPREV
**SGP/MGI** — Arquitetura completa para integração MuleSoft + Agentforce + Service Cloud, incluindo estratégia de migração de 19 sistemas legados, mapa de integrações síncronas/assíncronas, e conformidade LGPD para dados previdenciários sensíveis.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1-2 integrações) | 2 semanas | 120-160h | R$ 90k-120k |
| **Medium** (3-5 integrações, MuleSoft light) | 3-4 semanas | 160-240h | R$ 120k-180k |
| **Large** (5+ integrações, MuleSoft full, APIs customizadas) | 4-6 semanas | 240-400h | R$ 180k-300k |

---

## A3. Proof of Concept (POC)
**Tagline:** *"Validação de viabilidade técnica em ambiente controlado antes do full rollout"*

### O que resolve
- Validar tecnologia específica (Agentforce, Slack integrations, MuleSoft patterns)
- Reduzir riscos de implementação full-scale
- Demonstrar valor ao negócio e stakeholders (CTID, Diretoria)

### Entregáveis
- Ambiente Salesforce POC configurado
- Casos de uso priorizados implementados (2-3 jornadas)
- Integrações críticas funcionais (1-2 sistemas legacy)
- Demonstração ao vivo + documento de resultados
- Recomendação: Go/No-Go + ajustes de escopo para fase full

### Perfis PS
- Technical Architect (40h)
- Senior Technical Consultant (80h)
- MuleSoft TA (se aplicável, 40h)
- QA Consultant (20h)
- Program Manager (20h)

### Exemplo DATAPREV
**CLARO Agente PLM** — POC 8 semanas, $193,882.40, validação de Agentforce para gestão de ciclo de vida de produtos, integração com sistemas PLM legados, 6 GAPs identificados e ROI demonstrado antes de greenlight para produção.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1 cloud, 1-2 jornadas) | 4-6 semanas | 200-280h | R$ 150k-210k |
| **Medium** (2 clouds, 2-3 jornadas, integrações) | 6-8 semanas | 280-400h | R$ 210k-300k |
| **Large** (3+ clouds, Agentforce, MuleSoft, multi-canal) | 8-12 semanas | 400-600h | R$ 300k-450k |

---

# [B] IMPLEMENTATION & INTEGRATION

## B1. Core Platform Implementation
**Tagline:** *"Implementação completa de Sales/Service/Platform Cloud com setup de governança"*

### O que resolve
- Implementar CRM Salesforce do zero ou substituir sistema legado
- Configurar automações, fluxos de aprovação, regras de negócio
- Setup de usuários, perfis, permissões (modelo setor público)

### Entregáveis
- Org Salesforce configurada (sandbox + produção)
- Objetos customizados e data model
- Automações (Flows, Apex quando necessário)
- Relatórios e dashboards executivos
- Migração de dados (se aplicável)
- Documentação técnica e funcional
- Treinamento de administradores

### Perfis PS
- Technical Architect (160h)
- Senior Technical Consultant (320h)
- Technical Consultant (160h)
- QA Consultant (160h)
- Business Analyst (80h)
- Program Manager (120h)

### Exemplo DATAPREV
**UNA FUND2** — Extensão incremental sobre MVP existente: Platform + Service Cloud + Experience Cloud + Shield. 488h (vs. 630h tradicional, −22% com IA), 14 semanas, R$ 2,93M investimento total (PS + licenças).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (<50 usuários, 1 cloud, config-only) | 8-12 sem | 600-900h | R$ 450k-675k |
| **Medium** (50-200 usuários, 2 clouds, integrações) | 12-20 sem | 900-1.500h | R$ 675k-1,1M |
| **Large** (200+ usuários, 3+ clouds, custom dev) | 20-32 sem | 1.500-2.500h | R$ 1,1M-1,9M |

---

## B2. MuleSoft Integration Platform
**Tagline:** *"Integração enterprise-grade de sistemas legados com Salesforce via MuleSoft"*

### O que resolve
- Integrar CNIS, SIAPE, eSocial, Conectividade Social e outros sistemas legacy
- Criar APIs reutilizáveis e governadas
- Garantir segurança, auditoria e performance em integrações críticas

### Entregáveis
- Anypoint Platform configurado (pre-prod + prod)
- APIs REST desenvolvidas e publicadas no API Manager
- Integrações bidirecionais (Salesforce ↔ sistemas legacy)
- Documentação de APIs (Swagger/OAS)
- Testes de carga e segurança
- Runbooks operacionais

### Perfis PS
- MuleSoft Technical Architect (160h)
- MuleSoft Technical Consultant (320h)
- Technical Architect (Salesforce side, 80h)
- QA Consultant (80h)
- Program Manager (60h)

### Exemplo DATAPREV
**SGP/MGI** — MuleSoft Anypoint Platform Titanium Edition integrando 19 sistemas legados com Service Cloud + Agentforce. 2.085h totais (incluindo PS Salesforce core), R$ 1.655.170,45 c/imp apenas PS.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (2-3 integrações simples) | 8-10 sem | 400-600h | R$ 300k-450k |
| **Medium** (4-6 integrações, transformações) | 10-16 sem | 600-1.000h | R$ 450k-750k |
| **Large** (7+ integrações, orquestração complexa) | 16-24 sem | 1.000-1.600h | R$ 750k-1,2M |

---

## B3. Agentforce Implementation
**Tagline:** *"Agentes inteligentes autônomos para atendimento multi-canal (WhatsApp, Slack, Web)"*

### O que resolve
- Automatizar atendimento de alta complexidade com IA generativa
- Reduzir carga de call center / help desk
- Oferecer atendimento 24/7 em múltiplos canais (WhatsApp ANATEL-compliant, Slack interno)

### Entregáveis
- Agentforce configurado e treinado (knowledge base, topics, actions)
- Integrações com canais (WhatsApp Business API, Slack, Web)
- Knowledge Base estruturada (artigos, FAQs, procedimentos)
- Fluxos de escalação para humanos
- Dashboards de performance (CSAT, tempo de resolução, taxa de deflexão)
- Governança pós-go-live (ver seção C3)

### Perfis PS
- Agentforce Specialist (160h)
- Technical Architect (80h)
- Senior Technical Consultant (160h)
- QA Consultant (80h)
- Change Manager (40h)
- Program Manager (80h)

### Exemplo DATAPREV
**SEFIN-CE** — Agentforce para WhatsApp cobrança, 15 premissas documentadas, 11 perguntas em aberto, 3 ADD-ONs scoped (Marketing Cloud jornada, Data Cloud zero-copy, KB vectorization).

**Bolsão 3** — Governança de Agentes pós-go-live para 9 ministérios, 20M mensagens/mês, Agentforce + Slack.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1 canal, <10 topics, KB básica) | 6-8 sem | 320-480h | R$ 240k-360k |
| **Medium** (2 canais, 10-20 topics, integrações) | 8-12 sem | 480-720h | R$ 360k-540k |
| **Large** (3+ canais, 20+ topics, IA treinada, multi-idioma) | 12-18 sem | 720-1.200h | R$ 540k-900k |

---

## B4. Data Cloud & Analytics
**Tagline:** *"Unificação de dados + analytics preditiva para decisões baseadas em dados"*

### O que resolve
- Consolidar dados de múltiplas fontes (Salesforce + legacy) em Customer 360
- Criar segmentação avançada para campanhas e atendimento
- Dashboards executivos e preditivos (Tableau, CRM Analytics)

### Entregáveis
- Data Cloud configurado (ingestion, identity resolution, segmentation)
- Conectores de dados (sistemas legacy, APIs, flat files)
- Segmentos e audiências configurados
- Dashboards executivos (Tableau ou CRM Analytics)
- Data governance policies (LGPD-compliant)
- Documentação de data model

### Perfis PS
- Analytics Technical Architect (120h)
- Technical Consultant (160h)
- Analytics Solution Consultant (80h)
- QA Consultant (40h)
- Program Manager (40h)

### Exemplo DATAPREV
**ADD-ON SEFIN-CE** — Data Cloud zero-copy integration proposta como add-on para unificar dados de cobrança de múltiplas secretarias sem duplicação de storage.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (2-3 fontes, segmentação básica) | 6-8 sem | 280-400h | R$ 210k-300k |
| **Medium** (4-6 fontes, ML-driven segments) | 8-12 sem | 400-640h | R$ 300k-480k |
| **Large** (7+ fontes, real-time, preditiva) | 12-18 sem | 640-1.000h | R$ 480k-750k |

---

## B5. Experience Cloud (Portais)
**Tagline:** *"Portais self-service para beneficiários, servidores ou parceiros externos"*

### O que resolve
- Reduzir carga de atendimento via self-service
- Oferecer portal transparente para consulta de processos (benefícios, solicitações)
- Integrar cidadão/beneficiário diretamente ao Salesforce (Gov.br login)

### Entregáveis
- Experience Cloud site configurado (templates customizados)
- Integração com SSO (Gov.br, CAF, ou SAML corporativo)
- Funcionalidades self-service (consultas, protocolos, downloads)
- Mobile-responsive e acessível (WCAG 2.1 AA)
- Dashboards de uso e engajamento

### Perfis PS
- Experience Architect (80h)
- Technical Consultant (160h)
- Solution Consultant (80h)
- QA Consultant (80h)
- Program Manager (40h)

### Exemplo DATAPREV
**UNA FUND2** — Experience Cloud para acesso externo de beneficiários, integrado com Shield para criptografia de dados sensíveis e auditoria completa (requisito LGPD).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (portal simples, <5 páginas) | 6-8 sem | 280-400h | R$ 210k-300k |
| **Medium** (portal complexo, integrações, SSO) | 8-12 sem | 400-640h | R$ 300k-480k |
| **Large** (multi-portal, Gov.br, acessibilidade avançada) | 12-16 sem | 640-960h | R$ 480k-720k |

---

# [C] ADOPTION & ENABLEMENT

## C1. Change Management & Training
**Tagline:** *"Gestão de mudança e capacitação para alta adoção e baixa resistência"*

### O que resolve
- Resistência à mudança de servidores públicos acostumados a sistemas legados
- Baixa adoção pós-go-live (usuários continuam usando planilhas/sistemas antigos)
- Necessidade de capacitação técnica de administradores internos

### Entregáveis
- Plano de gestão de mudança (stakeholders, comunicação, cronograma)
- Materiais de treinamento (manuais, vídeos, FAQs)
- Sessões de treinamento (end-users, power users, admins)
- Programa de Champions (embaixadores internos)
- Pesquisas de prontidão e feedback
- Suporte pós-go-live (30-60 dias)

### Perfis PS
- Change Manager (160h)
- Business Analyst (80h)
- Program Manager (40h)

### Exemplo DATAPREV
Não há exemplo standalone nos projetos atuais, mas este serviço é **crítico** para projetos >500 usuários ou alta sensibilidade política (recomendado em SGP/MGI, SUNE).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (<100 usuários, 1 role) | 4-6 sem | 120-200h | R$ 90k-150k |
| **Medium** (100-500 usuários, 3+ roles) | 6-10 sem | 200-360h | R$ 150k-270k |
| **Large** (500+ usuários, multi-ministério, político) | 10-16 sem | 360-600h | R$ 270k-450k |

---

## C2. Admin & Developer Enablement
**Tagline:** *"Capacitação técnica do time interno Dataprev para autonomia operacional"*

### O que resolve
- Dataprev não tem capacidade interna de manter/evoluir Salesforce sem PS contínuo
- Necessidade de treinar admins para manutenções e configs simples
- Transferência de conhecimento técnico (Apex, Flows, integrações)

### Entregáveis
- Bootcamp de Administradores (ADM-201 prep)
- Bootcamp de Desenvolvedores (Apex, Flows, LWC basics)
- Documentação técnica detalhada (runbooks, arquitetura)
- Sessões de shadowing (PS trabalhando junto com time interno)
- Certificação path recomendado (ADM, Platform App Builder, PD1)

### Perfis PS
- Technical Architect (40h)
- Senior Technical Consultant (80h)
- Program Manager (20h)

### Exemplo DATAPREV
**DECIPEX Bootcamp App** — App Heroku com 50 diagnósticos + assistente IA para capacitação rápida do time cliente em melhores práticas Salesforce.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1-2 admins, treinamento básico) | 2-3 sem | 80-120h | R$ 60k-90k |
| **Medium** (3-5 admins, +devs, shadowing) | 3-5 sem | 120-240h | R$ 90k-180k |
| **Large** (5+ admins, full dev team, certificações) | 5-8 sem | 240-400h | R$ 180k-300k |

---

## C3. Hypercare & Stabilization (Pós-Go-Live)
**Tagline:** *"Suporte intensivo 30-90 dias pós-go-live para resolver issues críticos e otimizar"*

### O que resolve
- Bugs e problemas não detectados em QA aparecem em produção
- Ajustes de performance, relatórios, automações após feedback de usuários reais
- Evitar rollback ou abandono da plataforma nas primeiras semanas críticas

### Entregáveis
- Plantão diário de suporte (stand-up com time cliente)
- Correção de bugs críticos (SLA 4h)
- Ajustes de configuração (relatórios, dashboards, automações)
- Monitoramento de performance e logs
- Recomendações de otimização
- Relatório de estabilização (30d, 60d, 90d)

### Perfis PS
- Technical Architect (part-time, 20h/sem)
- Technical Consultant (full-time, 40h/sem primeiras 2 semanas, depois 20h/sem)
- QA Consultant (20h/sem)
- Program Manager (20h/sem)

### Exemplo DATAPREV
**Bolsão 3** — Governança Agentes pós-go-live para 9 ministérios, 20M msg/mês. Serviço de monitoramento contínuo + ajustes de topics/knowledge base + escalação de issues.

### Sizing típico
| Duração | Intensidade | Esforço | Investimento (c/imp) |
|---------|-------------|---------|----------------------|
| **30 dias** | Alta (40h/sem TC) | 240-320h | R$ 180k-240k |
| **60 dias** | Média (20h/sem TC) | 320-480h | R$ 240k-360k |
| **90 dias** | Baixa (monitoramento) | 480-640h | R$ 360k-480k |

---

# [D] OPTIMIZATION & INNOVATION

## D1. Health Check & Optimization
**Tagline:** *"Auditoria técnica da org Salesforce + roadmap de otimizações"*

### O que resolve
- Org Salesforce em produção há >1 ano acumulando débito técnico
- Performance degradada, automações redundantes, código não-otimizado
- Necessidade de validar conformidade contínua (LGPD, Shield, auditoria)

### Entregáveis
- Auditoria técnica completa (código, configurações, segurança, performance)
- Relatório de Health Check (score por área + priorização de riscos)
- Roadmap de otimizações (quick-wins + melhorias estruturais)
- Análise de licenças (usuários inativos, subutilização de features)
- Recomendações de governança

### Perfis PS
- Senior Technical Architect (80h)
- Technical Consultant (80h)
- Solution Architect (40h)
- Program Manager (20h)

### Exemplo DATAPREV
Não há exemplo específico, mas seria aplicável a **SGP/MGI 6-12 meses pós-go-live** ou **UNA FUND2 fase 2** para garantir que otimizações de IA continuam gerando valor.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1 cloud, audit básico) | 2-3 sem | 120-160h | R$ 90k-120k |
| **Medium** (2-3 clouds, deep-dive) | 3-4 sem | 160-280h | R$ 120k-210k |
| **Large** (3+ clouds, MuleSoft, full audit) | 4-6 sem | 280-480h | R$ 210k-360k |

---

## D2. AI-Powered Automation Boost
**Tagline:** *"Aplicar Einstein AI e Agentforce para automatizar processos ainda manuais"*

### O que resolve
- Processos manuais/repetitivos que escaparam do escopo inicial
- Oportunidade de usar IA generativa para ganho adicional de eficiência
- ROI adicional sobre investimento já feito (upsell de Einstein/Agentforce add-ons)

### Entregáveis
- Análise de processos candidatos a automação com IA
- Implementação de Einstein features (Next Best Action, Prediction Builder, GPT in Flows)
- Agentforce add-ons (sales, service, custom actions)
- KPIs de eficiência (tempo economizado, redução de erros)
- Documentação e treinamento

### Perfis PS
- Agentforce Specialist (80h)
- Technical Architect (40h)
- Technical Consultant (80h)
- QA Consultant (40h)

### Exemplo DATAPREV
**ADD-ON SEFIN-CE** — Marketing Cloud jornada automatizada + Data Cloud + KB vectorization (Einstein Search) para melhorar deflexão de Agentforce.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1-2 processos, Einstein básico) | 4-6 sem | 160-240h | R$ 120k-180k |
| **Medium** (3-5 processos, Agentforce add-on) | 6-10 sem | 240-400h | R$ 180k-300k |
| **Large** (5+ processos, ML customizado) | 10-16 sem | 400-640h | R$ 300k-480k |

---

## D3. Data Migration & Legacy Decommissioning
**Tagline:** *"Migração segura de dados legados + desligamento de sistemas antigos"*

### O que resolve
- Sistemas legados rodando em paralelo aumentam custo operacional
- Dados históricos críticos presos em sistemas antigos (CNIS, SIAPE antigos)
- Necessidade de descomissionamento seguro com auditoria TCU

### Entregáveis
- Plano de migração de dados (extract, transform, load)
- Scripts ETL e validação de integridade
- Migração executada (sandbox → produção)
- Plano de rollback e contingência
- Documentação de auditoria (rastreabilidade de dados LGPD)
- Desligamento controlado de sistema legado

### Perfis PS
- Technical Architect (80h)
- Senior Technical Consultant (160h)
- MuleSoft TA (se ETL via MuleSoft, 80h)
- QA Consultant (80h)
- Program Manager (60h)

### Exemplo DATAPREV
**SGP/MGI** — Estratégia de migração de 19 sistemas legados documentada (não executada no ROM inicial, mas scoped para fase 2).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Small** (1 sistema, <1M registros) | 6-8 sem | 280-400h | R$ 210k-300k |
| **Medium** (2-3 sistemas, 1-10M registros) | 8-14 sem | 400-720h | R$ 300k-540k |
| **Large** (3+ sistemas, >10M registros, multi-object) | 14-24 sem | 720-1.200h | R$ 540k-900k |

---

# [E] GOVERNANCE & COMPLIANCE

## E1. LGPD Compliance Audit & Remediation
**Tagline:** *"Auditoria de conformidade LGPD + correções para evitar multas ANPD"*

### O que resolve
- Org Salesforce processando dados sensíveis sem governança adequada
- Risco de multa ANPD (até 2% do faturamento ou R$ 50M)
- Necessidade de demonstrar conformidade para CTID/CGU/TCU

### Entregáveis
- Auditoria LGPD completa (mapeamento de dados sensíveis, bases legais, consentimentos)
- Relatório de não-conformidades (classificadas por severidade)
- Plano de remediação (técnica + processual)
- Implementação de controles (Shield encryption, Field Audit Trail, Privacy Center)
- Documentação para ANPD (RIPD, contratos DPA)
- Treinamento de DPO e time interno

### Perfis PS
- Senior Solution Architect (especialista LGPD, 80h)
- Technical Architect (40h)
- Business Analyst (40h)
- Program Manager (20h)

### Exemplo DATAPREV
**UNA FUND2** — Shield implementado para criptografia de dados sensíveis (Art. 11 LGPD) + auditoria completa de acessos. Privacy Center considerado mas não incluído no escopo inicial (add-on).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Audit only** (sem remediação) | 2-3 sem | 80-120h | R$ 60k-90k |
| **Audit + remediation light** | 4-6 sem | 120-240h | R$ 90k-180k |
| **Audit + full remediation + Privacy Center** | 6-10 sem | 240-400h | R$ 180k-300k |

---

## E2. Platform Governance & Center of Excellence (CoE)
**Tagline:** *"Estabelecer governança contínua e CoE interno para escalar Salesforce na organização"*

### O que resolve
- Múltiplos projetos Salesforce (diferentes ministérios/diretorias) sem governança central
- Risco de duplicação de esforços, silos de dados, inconsistência de processos
- Necessidade de CoE para escalar Salesforce enterprise-wide

### Entregáveis
- Modelo de governança (comitês, processos de aprovação, change management)
- Center of Excellence estruturado (roles, responsabilidades, KPIs)
- Guias de desenvolvimento (coding standards, security baseline, CI/CD)
- Biblioteca de componentes reutilizáveis
- Processo de onboarding de novos projetos
- Treinamento de CoE team

### Perfis PS
- Principal Program Manager (80h)
- Senior Technical Architect (80h)
- Senior Solution Architect (40h)
- Change Manager (40h)

### Exemplo DATAPREV
**Bolsão 3** — Governança de Agentes pós-go-live para **9 ministérios**, garantindo consistência de topics, knowledge base e escalação entre diferentes órgãos.

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Foundation** (CoE básico, <5 projetos) | 6-8 sem | 240-320h | R$ 180k-240k |
| **Enterprise** (CoE robusto, 5-10 projetos) | 8-12 sem | 320-480h | R$ 240k-360k |
| **Multi-Org** (governança multi-ministério) | 12-16 sem | 480-720h | R$ 360k-540k |

---

## E3. Audit & Compliance Reporting (TCU/CGU)
**Tagline:** *"Preparação de documentação e relatórios para auditorias TCU, CGU, ANPD"*

### O que resolve
- Auditoria TCU/CGU solicitando rastreabilidade de gastos, decisões técnicas, mudanças
- Necessidade de demonstrar ROI e conformidade contratual (Lei 14.133/2021)
- ANPD solicitando RIPD (Relatório de Impacto à Proteção de Dados)

### Entregáveis
- Relatórios de auditoria customizados (despesas, atividades, entregas)
- Documentação de decisões técnicas (ADRs — Architecture Decision Records)
- RIPD (quando aplicável)
- Dashboards de acompanhamento (Tableau/CRM Analytics para gestores/auditores)
- Processo de auditoria contínua (automação de reports)

### Perfis PS
- Business Analyst (80h)
- Solution Architect (40h)
- Program Manager (40h)

### Exemplo DATAPREV
Não há exemplo específico, mas este serviço seria aplicável a **qualquer projeto DATAPREV em produção** quando auditoria é solicitada (comum em contratos >R$ 1M).

### Sizing típico
| Porte | Duração | Esforço | Investimento (c/imp) |
|-------|---------|---------|----------------------|
| **Ad-hoc report** (pontual) | 1-2 sem | 40-80h | R$ 30k-60k |
| **Auditoria completa** (documentação full) | 3-4 sem | 80-160h | R$ 60k-120k |
| **Continuous audit setup** (automação) | 4-6 sem | 160-280h | R$ 120k-210k |

---

# 📊 RESUMO EXECUTIVO — SERVIÇOS MAIS DEMANDADOS

Baseado nos projetos DATAPREV ativos/recentes, os serviços de **maior demanda e ROI** são:

| Ranking | Serviço | Frequência | ROI Típico | Observação |
|---------|---------|------------|-----------|------------|
| **1º** | **B1. Core Platform Implementation** | 100% projetos | Alto | Base para todos os demais |
| **2º** | **A1. Discovery Workshop & Scoping** | 90% projetos | Muito Alto | Reduz risco de overrun 40%+ |
| **3º** | **B3. Agentforce Implementation** | 70% projetos | Muito Alto | Deflexão 30-60%, ROI <12m |
| **4º** | **B2. MuleSoft Integration Platform** | 60% projetos | Alto | Viabiliza integração legados |
| **5º** | **C3. Hypercare & Stabilization** | 50% projetos | Médio | Evita rollback/abandono |
| **6º** | **E1. LGPD Compliance Audit** | 50% projetos | Muito Alto | Evita multa até R$ 50M |
| **7º** | **A2. Architecture Design** | 40% projetos | Alto | Reduz risco técnico 50%+ |
| **8º** | **B5. Experience Cloud** | 30% projetos | Médio | Self-service reduz 20-40% carga |
| **9º** | **C1. Change Management** | 30% projetos | Alto | Aumenta adoção 2-3× |
| **10º** | **E2. Platform Governance (CoE)** | 20% projetos | Muito Alto | Escala Salesforce enterprise-wide |

---

# 💰 MODELOS DE ENGAJAMENTO

## Modelo 1: Fixed-Price (Preço Fechado)
**Quando usar:** Escopo bem definido, ROM aprovado, baixo risco de mudanças  
**Exemplo:** Implementação Core Platform (B1), POC (A3), Migration (D3)

**Vantagens cliente:**
- Previsibilidade de custo
- Risco de overrun é do PS, não do cliente

**Desvantagens cliente:**
- Change requests geram custos adicionais
- Menos flexibilidade para ajustes mid-flight

---

## Modelo 2: Time & Materials (T&M)
**Quando usar:** Escopo incerto, discovery em andamento, projeto iterativo  
**Exemplo:** Discovery (A1), Health Check (D1), Hypercare (C3)

**Vantagens cliente:**
- Máxima flexibilidade
- Paga apenas pelo que usa
- Pode pausar/retomar

**Desvantagens cliente:**
- Custo final incerto (mitigado com cap mensal ou trimestral)
- Requer gestão ativa de escopo

---

## Modelo 3: Retainer (Retenção Mensal)
**Quando usar:** Suporte contínuo, CoE, otimizações recorrentes  
**Exemplo:** CoE (E2), Hypercare estendido (C3), AI Automation (D2)

**Estrutura típica:**
- Pacote mensal de horas (ex: 80h/mês, 160h/mês)
- Mix de perfis (TA + TC + PM)
- SLA de resposta (4h crítico, 24h normal)
- Roll-over de horas não-utilizadas (até 20%)

**Vantagens cliente:**
- Custo previsível mensal
- Acesso garantido a time PS
- Evita re-onboarding a cada projeto

---

## Modelo 4: Outcome-Based (Baseado em Resultados)
**Quando usar:** ROI mensurável, KPIs claros, maturidade do cliente alta  
**Exemplo:** Agentforce (B3) — pagamento vinculado a deflexão atingida

**Estrutura típica:**
- Pagamento base (60-70% do valor)
- Bônus por atingimento de KPIs (30-40%)
- KPIs exemplos: taxa de deflexão >50%, CSAT >4.5, tempo resolução <30% baseline

**Vantagens cliente:**
- Alinhamento total de incentivos
- PS compartilha risco de sucesso

**Desvantagens cliente:**
- Requer medição rigorosa (dashboards, baselines)
- PS pode precificar prêmio de risco

---

# 🎯 PRÓXIMOS PASSOS

## Para usar este cardápio:

1. **Identificar necessidade do cliente** (discovery, implementação, otimização, compliance)
2. **Selecionar serviço(s) aplicável(is)** desta lista
3. **Customizar escopo** baseado em contexto específico (ex: número de integrações, usuários, clouds)
4. **Gerar ROM** usando tabela de rate cards DATAPREV (seção 10.6 do skill /dataprev)
5. **Propor modelo de engajamento** adequado (fixed-price, T&M, retainer, outcome-based)

## Para combinar serviços (bundles):

**Bundle "Quick Start"** (novo cliente):  
A1 (Discovery) → A2 (Architecture) → A3 (POC) → **Decision Point: Go/No-Go**

**Bundle "Full Implementation"** (greenfield):  
A1 + A2 → B1 (Core) + B2 (MuleSoft) + B3 (Agentforce) → C3 (Hypercare)

**Bundle "Optimization"** (cliente existente):  
D1 (Health Check) → D2 (AI Automation) → E1 (LGPD Audit) → E2 (CoE)

**Bundle "Compliance First"** (foco regulatório):  
E1 (LGPD Audit) → remediation → E3 (Audit Reporting) → continuous monitoring

---

# 📞 CONTATO

**Nelson Stebulaitis Filho**  
Services Sales Solution Manager  
Salesforce Professional Services LATAM  
Reporting to: Paulo Iudicibus (VP GM LATAM AMER Services)

**Para discussão de qualquer serviço deste cardápio:**
- Agendar ROM Workshop (2h) — mapeamento de necessidades + proposta preliminar
- Solicitar case studies específicos DATAPREV
- Customizar bundle de serviços para contexto específico

---

**Versão:** 1.0 | **Última atualização:** 2026-07-03  
**Documento vivo:** Este cardápio será atualizado conforme novos serviços sejam validados em projetos DATAPREV.
