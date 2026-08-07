# Catálogo de Blocos Replicáveis PS — DATAPREV
## Modelo "À la Carte" — Capacidades Atômicas com PS + Licenças Fixas

**Versão:** 1.0 | **Data:** 2026-07-03  
**Contexto:** Blocos modulares de capacidades Salesforce para DATAPREV, cada um com esforço PS fixo, perfis definidos e licenças necessárias

---

## 🎯 COMO USAR ESTE CATÁLOGO

Este documento funciona como um **cardápio de restaurante**:
- Cada item = 1 capacidade atômica independente
- Cada item tem PS fixo (semanas, perfis, horas) + licenças fixas
- Cliente monta o "pedido" combinando N itens
- Total do projeto = soma dos blocos selecionados

**Exemplo de combinação:**
```
Cliente quer: Mensageria WhatsApp proativa + Bot autoatendimento

Seleção no catálogo:
→ BLOCO M-01: Jornada Marketing Cloud WhatsApp (1 caso de uso)
→ BLOCO A-01: Agentforce WhatsApp Bot (até 3 topics)

Total PS = 6 sem + 8 sem = 14 semanas
Total Licenças = MC Engagement + Agentforce + WhatsApp API
```

---

## 📊 LEGENDAS E CONVENÇÕES

### Sizing de Perfis
- **40h/sem** = full-time (FT)
- **20h/sem** = part-time (PT)

### Licenças — Preços Anuais BRL (tabela DATAPREV)
Todos os valores de licença são **com imposto incluído** (já aplicado ×0,9345).

### PS — Valores por Hora (com imposto incluído)
| Perfil | R$/h c/imp |
|---|---:|
| Senior Technical Architect | R$ 826,73 |
| Senior Solution Architect | R$ 826,73 |
| MuleSoft Technical Architect | R$ 767,68 |
| Technical Consultant | R$ 624,97 |
| Solution Consultant | R$ 536,39 |
| QA Consultant | R$ 536,39 |
| Program Manager | R$ 738,14 |
| Agentforce Specialist | R$ 624,97 |
| Analytics Technical Consultant | R$ 624,97 |
| Change Manager | R$ 536,39 |

---

# 📦 CATÁLOGO DE BLOCOS

## [M] MARKETING CLOUD — Jornadas de Mensageria

### M-01 | Jornada Marketing Cloud WhatsApp — 1 Caso de Uso
**Capacidade:** Envio proativo de mensagens WhatsApp para 1 caso de uso (ex: cidadãos com IPTU vencido)

#### Escopo Técnico
- Setup Marketing Cloud Engagement (se ORG nova) ou aproveitamento de instância existente
- Configuração de 1 jornada no Journey Builder (até 5 steps)
- Conexão com 1 fonte de dados zero-copy no Data Cloud
- Criação de 1 segmentação (sem Identity Resolution — premissa: CPF/CNPJ confiável)
- Configuração WhatsApp Business API (1 número)
- Envio de mensagens proativas com template HSM aprovado pela Meta

#### Premissas
- [ ] Templates HSM já aprovados pela Meta (fora do escopo PS)
- [ ] Dados fonte têm CPF/CNPJ + nome + telefone válidos
- [ ] Número WhatsApp Business já provisionado (se não, add 1 semana setup)
- [ ] Jornada linear (não inclui múltiplas ramificações A/B/C)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Marketing Cloud Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **Solution Consultant** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **360h** | **R$ 223.413,20** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Marketing Cloud Engagement - Enterprise Plus EE | 1 | R$ 520.577,76 | R$ 520.577,76 |
| Additional Contacts (pacote 1.000) | volume/1000 | R$ 2,40 | variável |
| Salesforce Message Credits - WhatsApp Marketing (1.000 msgs) | volume/1000 | R$ 4,01 | variável |
| **TOTAL LICENÇAS (base)** | | | **R$ 520.577,76** |

**Exemplo de volume:**
- 405.000 msgs/mês = 4,86M msgs/ano
- Message Credits necessários: 4.860 pacotes × R$ 4,01 = **R$ 19.488,60/ano**
- Contacts: 50.000 cidadãos = 50 pacotes × R$ 2,40 = **R$ 120,00/ano**

#### Entregáveis
- [ ] Marketing Cloud instância configurada
- [ ] 1 jornada Journey Builder publicada e testada
- [ ] Data Extension mapeada (zero-copy ou import)
- [ ] 1 segmentação configurada
- [ ] WhatsApp Business API integrado
- [ ] Documentação técnica da jornada
- [ ] Runbook operacional (ativação, pausa, monitoramento)

#### Extensões Opcionais
- **+1 caso de uso adicional**: +2 semanas PS, +80h TC
- **Identity Resolution (dedup)**: +1 semana PS, +40h TC
- **A/B Testing (2 variantes)**: +1 semana PS, +40h TC
- **Integração com sistema legado via MuleSoft**: ver BLOCO I-01

---

### M-02 | Jornada SMS — 1 Caso de Uso
**Capacidade:** Envio proativo de SMS para 1 caso de uso (ex: lembrete de vencimento)

#### Escopo Técnico
Idêntico ao M-01, substituindo WhatsApp por SMS.

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Marketing Cloud Technical Consultant** | 40h/sem | 3 sem | 120h | R$ 74.996,40 |
| **Solution Consultant** | 20h/sem | 3 sem | 60h | R$ 32.183,40 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 3 sem | 60h | R$ 44.288,40 |
| **TOTAL PS** | | **4 semanas** | **280h** | **R$ 172.923,80** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Marketing Cloud Engagement - Enterprise Plus EE | 1 | R$ 520.577,76 | R$ 520.577,76 |
| Salesforce Message Credits - SMS (1.000 msgs) | volume/1000 | ~R$ 2,00 | variável |

**Nota:** SMS é ~50% mais barato que WhatsApp em credits.

---

### M-03 | Jornada Multi-Canal (WhatsApp + SMS + Email)
**Capacidade:** Régua multi-canal com fallback automático (tentativa WhatsApp → se falhar → SMS → se falhar → Email)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Marketing Cloud Technical Consultant** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **Solution Consultant** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **QA Consultant** | 20h/sem | 3 sem | 60h | R$ 32.183,40 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **8 semanas** | **540h** | **R$ 335.119,80** |

#### Licenças Necessárias
Base M-01 (MC Engagement) + Message Credits para 3 canais.

---

## [A] AGENTFORCE — Bots Conversacionais

### A-01 | Agentforce WhatsApp Bot — Até 3 Topics
**Capacidade:** Bot conversacional WhatsApp com identificação de usuário, menu principal e até 3 fluxos completos (topics)

#### Escopo Técnico
- Configuração Agentforce Agent Builder
- 1 agente WhatsApp com:
  - Identificação de usuário (coleta CPF/CNPJ/nome)
  - Menu principal em linguagem natural
  - Até 3 topics completos (ex: Consulta IPTU, Boleto Taxa Lixo, Atualização Cadastral)
  - Knowledge Base básica (até 20 artigos)
  - Pesquisa de satisfação (CSAT)
  - Handoff para humano (se Service Cloud disponível)
- Integrações com até 2 APIs externas via Flow/Apex

#### Premissas
- [ ] WhatsApp Business API já provisionado (ver M-01)
- [ ] APIs externas documentadas e acessíveis
- [ ] Knowledge Base fornecida pelo cliente (fora do escopo criar conteúdo)
- [ ] Sem transbordo humano = escopo core; com transbordo = adicionar Service Cloud (ver S-01)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Agentforce Specialist** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **QA Consultant** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **8 semanas** | **600h** | **R$ 381.476,00** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Service Cloud - Agentforce 1 Edition | 1 | R$ 4.627,92 | R$ 4.627,92 |
| Agentforce Conversations - Unlimited Ed. (conversas ilimitadas) | 1 | R$ 68,88 | R$ 68,88 |
| Flex Credits (100k sessões) | pacotes | R$ 1.776,10 | variável |
| **TOTAL LICENÇAS (base)** | | | **R$ 4.696,80** |

**Exemplo de volume:**
- 400.000 conversas/ano = 400k sessões
- Flex Credits necessários: 4 pacotes × R$ 1.776,10 = **R$ 7.104,40/ano**

#### Entregáveis
- [ ] Agentforce Agent configurado e publicado
- [ ] 3 topics implementados e testados
- [ ] Knowledge Base carregada
- [ ] Integrações com APIs funcionais
- [ ] Pesquisa de satisfação configurada
- [ ] Documentação técnica (topics, APIs, fluxos)
- [ ] Runbook operacional (monitoramento, ajustes)

#### Extensões Opcionais
- **+1 topic adicional**: +1 semana PS, +40h Agentforce Specialist
- **+1 API adicional**: +0,5 semana PS, +20h TC
- **Knowledge Base externa vetorizada (Data Cloud)**: ver BLOCO D-02
- **Transbordo humano (Service Cloud)**: ver BLOCO S-01

---

### A-02 | Agentforce Slack Bot Interno — Até 5 Topics
**Capacidade:** Bot conversacional Slack para atendimento interno (servidores, colaboradores)

#### Escopo Técnico
- Configuração Agentforce Agent Builder
- 1 agente Slack com:
  - Identificação automática via Slack SSO
  - Menu de comandos natural
  - Até 5 topics (ex: Consulta Folha, Reposição Erário, Auxílio Funeral, Plano Saúde, Isenção IR)
  - Knowledge Base interna (até 50 artigos)
  - Escalação para equipe específica
- Integrações com até 3 sistemas legados (SIAP, CIAP, SEI)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Agentforce Specialist** | 40h/sem | 8 sem | 320h | R$ 199.990,40 |
| **Technical Consultant** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **QA Consultant** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **Program Manager** | 20h/sem | 8 sem | 160h | R$ 118.102,40 |
| **TOTAL PS** | | **10 semanas** | **840h** | **R$ 532.452,40** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Service Cloud - Agentforce 1 Edition | 1 | R$ 4.627,92 | R$ 4.627,92 |
| Agentforce Conversations - Unlimited Ed. | 1 | R$ 68,88 | R$ 68,88 |
| Flex Credits (100k sessões) | pacotes | R$ 1.776,10 | variável |
| Slack Enterprise Grid (se não contratado) | users | consultar | — |

---

### A-03 | Agentforce Voice (Telefone) — Até 3 Topics
**Capacidade:** Bot de voz (telefone) com IVR conversacional via IA generativa

#### Escopo Técnico
- Configuração Agentforce Voice
- URA conversacional (não menu rígido de opções)
- Até 3 topics por voz
- Transcrição automática
- Handoff para agente humano

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Agentforce Specialist** | 40h/sem | 8 sem | 320h | R$ 199.990,40 |
| **Technical Consultant** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **QA Consultant** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **Program Manager** | 20h/sem | 8 sem | 160h | R$ 118.102,40 |
| **TOTAL PS** | | **10 semanas** | **840h** | **R$ 532.452,40** |

#### Licenças Necessárias
Consultar — Voice é add-on específico com cobrança por minuto.

---

## [S] SERVICE CLOUD — Atendimento Humano

### S-01 | Service Cloud Console — Até 20 Agentes
**Capacidade:** Console de atendimento humano multi-canal (email, chat, telefone, WhatsApp) para até 20 agentes

#### Escopo Técnico
- Configuração Service Cloud Console
- Omni-Channel routing (distribuição automática)
- Até 4 canais configurados (email, chat, telefone via CTI, WhatsApp)
- Dashboards operacionais (SLA, backlog, CSAT)
- Relatórios gerenciais
- Treinamento de 20 agentes (2 turmas de 10)

#### Premissas
- [ ] CTI já contratado (Twilio, Genesys, ou similar)
- [ ] Licenças Service Cloud Unlimited já disponíveis

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Architect** | 40h/sem | 6 sem | 240h | R$ 198.415,20 |
| **Technical Consultant** | 40h/sem | 8 sem | 320h | R$ 199.990,40 |
| **Solution Consultant** | 40h/sem | 6 sem | 240h | R$ 128.733,60 |
| **QA Consultant** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **Change Manager** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **Program Manager** | 20h/sem | 8 sem | 160h | R$ 118.102,40 |
| **TOTAL PS** | | **12 semanas** | **1.160h** | **R$ 752.519,60** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Service Cloud - Unlimited Edition | 20 | R$ 3.346,56 | R$ 66.931,20 |
| Digital Engagement - Unlimited Edition | 20 | R$ 717,12 | R$ 14.342,40 |
| Digital Engagement - Additional Conversations (100) | pacotes | R$ 152,23 | variável |
| **TOTAL LICENÇAS (base)** | | | **R$ 81.273,60** |

---

### S-02 | Service Cloud — Extensão +20 Agentes
**Capacidade:** Expansão de console existente para +20 agentes adicionais

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Consultant** | 20h/sem | 2 sem | 40h | R$ 24.998,80 |
| **Change Manager** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 2 sem | 40h | R$ 29.525,60 |
| **TOTAL PS** | | **2 semanas** | **120h** | **R$ 75.980,00** |

#### Licenças Necessárias
+20 × Service Cloud Unlimited + Digital Engagement (mesmos valores unitários S-01)

---

## [D] DATA CLOUD — Unificação de Dados

### D-01 | Data Cloud — Setup Base + 1 Data Stream
**Capacidade:** Configuração inicial Data Cloud com 1 fonte de dados (zero-copy ou batch ingestion)

#### Escopo Técnico
- Setup Data Cloud Starter Edition
- Configuração de 1 data stream (zero-copy ou batch)
- Identity Resolution básica (1 regra: CPF/CNPJ match)
- 1 segmentação simples
- Data Actions configurados (1 ação para Marketing Cloud ou Agentforce)

#### Premissas
- [ ] Fonte de dados tem API disponível ou export batch viável

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Architect** | 40h/sem | 4 sem | 160h | R$ 132.276,80 |
| **Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **440h** | **R$ 312.778,80** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Customer Data Cloud Starter - Unlimited Ed. | 1 | R$ 228.334,68 | R$ 228.334,68 |
| (Inclui 100 pacotes de 100k credits + 10TB storage) | | | |

---

### D-02 | Data Cloud — Knowledge Base Externa Vetorizada
**Capacidade:** Ingestão de KB externa (PDFs, sites, documentos) + vetorização para busca semântica via Agentforce

#### Escopo Técnico
- Ingestão de até 500 documentos (PDFs, DOCs, páginas web)
- Processamento e vetorização via Einstein Search
- Configuração de busca semântica
- Integração com Agentforce Agent (topic "Outros Assuntos")

#### Premissas
- [ ] Cliente fornece documentos estruturados
- [ ] Não inclui curadoria de conteúdo (cliente deve revisar antes de carregar)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Architect** | 40h/sem | 3 sem | 120h | R$ 99.207,60 |
| **Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **Agentforce Specialist** | 20h/sem | 4 sem | 80h | R$ 49.997,60 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **480h** | **R$ 329.707,20** |

#### Licenças Necessárias
Incluído no Data Cloud Starter (D-01) — sem custo incremental de licença.

---

### D-03 | Data Cloud — +1 Data Stream Adicional
**Capacidade:** Adicionar 1 fonte de dados extra ao Data Cloud já configurado

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Consultant** | 40h/sem | 2 sem | 80h | R$ 49.997,60 |
| **QA Consultant** | 20h/sem | 1 sem | 20h | R$ 10.727,80 |
| **Program Manager** | 20h/sem | 2 sem | 40h | R$ 29.525,60 |
| **TOTAL PS** | | **2 semanas** | **140h** | **R$ 90.251,00** |

---

## [I] INTEGRAÇÕES — MuleSoft & APIs

### I-01 | MuleSoft — Setup Anypoint Platform Base
**Capacidade:** Configuração inicial MuleSoft Anypoint Platform Titanium (pre-prod + prod)

#### Escopo Técnico
- Setup Anypoint Platform (Design Center, Exchange, API Manager)
- Configuração de ambientes (pre-prod + prod)
- Setup VPC/VPN (1 unidade)
- Políticas de segurança base (OAuth2, rate limiting)
- Documentação de padrões

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **MuleSoft Technical Architect** | 40h/sem | 4 sem | 160h | R$ 122.828,80 |
| **Technical Architect (SF side)** | 20h/sem | 4 sem | 80h | R$ 66.138,40 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **360h** | **R$ 269.474,00** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| MuleSoft Anypoint Platform Base - Titanium Ed. | 1 | R$ 388.441,44 | R$ 388.441,44 |
| MuleSoft Anypoint VPC/VPN - Titanium | 1 | R$ 15.963,36 | R$ 15.963,36 |
| **TOTAL LICENÇAS (base)** | | | **R$ 404.404,80** |

---

### I-02 | MuleSoft — 1 API REST Completa
**Capacidade:** Desenvolvimento de 1 API REST bidirecional (Salesforce ↔ Sistema Legado)

#### Escopo Técnico
- Análise de requisitos da integração
- Desenvolvimento de 1 API REST (RAML spec + implementação)
- Transformações de dados (XML ↔ JSON, enriquecimento)
- Testes unitários + testes de carga
- Publicação no API Manager (pre-prod + prod)
- Documentação técnica (Swagger/OAS)

#### Premissas
- [ ] Sistema legado tem API disponível ou banco de dados acessível
- [ ] Documentação da API legada disponível
- [ ] Sem orquestrações complexas (apenas 1-to-1 mapping)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **MuleSoft Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **4 semanas** | **280h** | **R$ 180.502,00** |

#### Licenças Necessárias
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| MuleSoft Additional vCore Pre-Production - Titanium | 1 | R$ 79.816,68 | R$ 79.816,68 |
| MuleSoft Additional vCore Production - Titanium | 1 | R$ 79.816,68 | R$ 79.816,68 |
| MuleSoft API Manager Pre-Production - Titanium | 1 | R$ 9.050,16 | R$ 9.050,16 |
| MuleSoft API Manager Production - Titanium | 1 | R$ 9.050,16 | R$ 9.050,16 |
| MuleSoft API Governance - Titanium | 1 | R$ 3.193,68 | R$ 3.193,68 |
| **TOTAL LICENÇAS (por API)** | | | **R$ 180.927,36** |

---

### I-03 | MuleSoft — API Orquestração Complexa
**Capacidade:** Desenvolvimento de 1 API de orquestração (chamar 3+ sistemas, regras de negócio, error handling avançado)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **MuleSoft Technical Architect** | 20h/sem | 6 sem | 120h | R$ 92.121,60 |
| **MuleSoft Technical Consultant** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **QA Consultant** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **8 semanas** | **560h** | **R$ 373.602,40** |

#### Licenças Necessárias
Base I-01 + adicional de 1 vCore (pré-prod + prod) para performance.

---

### I-04 | Integração Nativa (Flow/Apex) — 1 API Simples
**Capacidade:** Integração via Flow ou Apex sem MuleSoft (para APIs simples, baixo volume)

#### Escopo Técnico
- Análise da API externa
- Desenvolvimento de Flow com HTTP Callout ou Apex REST callout
- Tratamento de erros básico
- Testes e validação

#### Premissas
- [ ] API externa é REST simples (JSON) e bem documentada
- [ ] Volume baixo (<10k chamadas/dia)
- [ ] Sem transformações complexas

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Consultant** | 40h/sem | 2 sem | 80h | R$ 49.997,60 |
| **QA Consultant** | 20h/sem | 1 sem | 20h | R$ 10.727,80 |
| **Program Manager** | 20h/sem | 2 sem | 40h | R$ 29.525,60 |
| **TOTAL PS** | | **2 semanas** | **140h** | **R$ 90.251,00** |

#### Licenças Necessárias
Nenhuma adicional (usa Platform padrão).

---

## [E] EXPERIENCE CLOUD — Portais Self-Service

### E-01 | Experience Cloud — Portal Cidadão (até 10k membros)
**Capacidade:** Portal público self-service para cidadãos consultarem processos, emitirem boletos, atualizarem cadastro

#### Escopo Técnico
- Configuração Experience Cloud site (template customizado)
- Integração SSO (Gov.br ou SAML corporativo)
- Até 5 páginas funcionais (ex: Consulta IPTU, Emissão DAM, Atualização Cadastral, FAQ, Contato)
- Mobile-responsive e acessível (WCAG 2.1 AA)
- Dashboards de uso

#### Premissas
- [ ] SSO Gov.br já configurado ou SAML endpoint disponível
- [ ] Conteúdo das páginas fornecido pelo cliente

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Experience Architect** | 40h/sem | 6 sem | 240h | R$ 177.211,20 |
| **Technical Consultant** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **Solution Consultant** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **QA Consultant** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **10 semanas** | **800h** | **R$ 523.058,80** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Customer Community Plus - Unlimited - Members | 10.000 | R$ 14,40 | R$ 144.000,00 |

**Nota:** Experience Cloud cobra por membro ativo. 10k membros = R$ 144k/ano.

---

### E-02 | Experience Cloud — Portal Interno (até 500 colaboradores)
**Capacidade:** Portal interno para servidores/colaboradores (self-service RH, folha, benefícios)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Experience Architect** | 40h/sem | 4 sem | 160h | R$ 118.140,80 |
| **Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **Solution Consultant** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **520h** | **R$ 341.554,00** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Customer Community - Unlimited - Members | 500 | R$ 4,80 | R$ 2.400,00 |

---

## [T] TABLEAU — Analytics & Dashboards

### T-01 | Tableau — Setup + 3 Dashboards Executivos
**Capacidade:** Configuração Tableau + desenvolvimento de 3 dashboards executivos (KPIs, tendências, drill-downs)

#### Escopo Técnico
- Configuração Tableau Server (8-core base) ou Tableau Cloud
- Conexão com Data Cloud ou Salesforce Platform
- Desenvolvimento de 3 dashboards:
  - Dashboard 1: Visão executiva (KPIs principais)
  - Dashboard 2: Operacional (backlog, SLA, produtividade)
  - Dashboard 3: Análise de tendências (série histórica, forecasting)
- Treinamento de 5 power users

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Analytics Technical Consultant** | 40h/sem | 6 sem | 240h | R$ 149.992,80 |
| **Solution Consultant** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **8 semanas** | **520h** | **R$ 324.392,00** |

#### Licenças Necessárias (Anuais)
| Produto | Qtd | Valor Unit. (R$) | Total (R$) |
|---|:---:|---:|---:|
| Tableau - 8 Core Base (Server) | 1 | R$ 673.147,44 | R$ 673.147,44 |
| Tableau Plus Creator | 5 | R$ 8.414,40 | R$ 42.072,00 |
| Tableau Plus Viewer | 50 | R$ 2.524,32 | R$ 126.216,00 |
| **TOTAL LICENÇAS** | | | **R$ 841.435,44** |

**Alternativa Tableau Cloud:**
- Mesmos perfis PS
- Licenças: Tableau Plus Creator (5) + Explorer (20) + Viewer (50)

---

### T-02 | Tableau — +1 Dashboard Adicional
**Capacidade:** Desenvolvimento de 1 dashboard adicional sobre ambiente Tableau já configurado

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Analytics Technical Consultant** | 40h/sem | 2 sem | 80h | R$ 49.997,60 |
| **QA Consultant** | 20h/sem | 1 sem | 20h | R$ 10.727,80 |
| **Program Manager** | 20h/sem | 2 sem | 40h | R$ 29.525,60 |
| **TOTAL PS** | | **2 semanas** | **140h** | **R$ 90.251,00** |

---

## [G] GOVERNANÇA & COMPLIANCE

### G-01 | LGPD Audit & Remediation
**Capacidade:** Auditoria completa de conformidade LGPD + plano de remediação + implementação de controles

#### Escopo Técnico
- Auditoria LGPD completa (mapeamento de dados sensíveis, bases legais)
- Relatório de não-conformidades (classificadas por severidade)
- Plano de remediação técnico + processual
- Implementação de controles:
  - Shield encryption (campos sensíveis)
  - Field Audit Trail
  - Privacy Center (opcional, add-on)
- Documentação para ANPD (RIPD, DPA)
- Treinamento de DPO e time

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Senior Solution Architect (LGPD specialist)** | 40h/sem | 6 sem | 240h | R$ 198.415,20 |
| **Technical Architect** | 20h/sem | 6 sem | 120h | R$ 99.207,60 |
| **Business Analyst** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **8 semanas** | **600h** | **R$ 450.566,40** |

#### Licenças Necessárias
Shield já contratado no case DATAPREV (zero incremental).
Privacy Center (opcional): consultar tabela linha 13.

---

### G-02 | Center of Excellence (CoE) Setup
**Capacidade:** Estruturação de CoE interno com governança, padrões, processos e treinamento de time

#### Escopo Técnico
- Modelo de governança (comitês, processos de aprovação, change management)
- Center of Excellence estruturado (roles, responsabilidades, KPIs)
- Guias de desenvolvimento (coding standards, security baseline, CI/CD)
- Biblioteca de componentes reutilizáveis
- Processo de onboarding de novos projetos
- Treinamento de CoE team (5-10 pessoas)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Principal Program Manager** | 40h/sem | 8 sem | 320h | R$ 236.204,80 |
| **Senior Technical Architect** | 40h/sem | 6 sem | 240h | R$ 198.415,20 |
| **Senior Solution Architect** | 20h/sem | 6 sem | 120h | R$ 99.207,60 |
| **Change Manager** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **TOTAL PS** | | **12 semanas** | **800h** | **R$ 598.194,40** |

---

### G-03 | Hypercare Pós-Go-Live (30 dias)
**Capacidade:** Suporte intensivo 30 dias pós-go-live para resolver issues críticos e otimizar

#### Escopo Técnico
- Plantão diário de suporte (stand-up com time cliente)
- Correção de bugs críticos (SLA 4h)
- Ajustes de configuração (relatórios, dashboards, automações)
- Monitoramento de performance e logs
- Recomendações de otimização
- Relatório de estabilização (30d)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Architect** | 20h/sem | 4 sem | 80h | R$ 66.138,40 |
| **Technical Consultant** | 40h/sem (S1-S2) + 20h/sem (S3-S4) | 4 sem | 120h | R$ 74.996,40 |
| **QA Consultant** | 20h/sem | 4 sem | 80h | R$ 42.911,20 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **4 semanas** | **360h** | **R$ 243.097,20** |

---

### G-04 | Hypercare Estendido (60 dias)
Mesmo escopo G-03, mas 60 dias com intensidade reduzida após primeiros 30 dias.

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Architect** | 20h/sem | 8 sem | 160h | R$ 132.276,80 |
| **Technical Consultant** | 40h/sem (S1-S2) + 20h/sem (S3-S8) | 8 sem | 200h | R$ 124.994,00 |
| **QA Consultant** | 20h/sem (S1-S4) | 4 sem | 80h | R$ 42.911,20 |
| **Program Manager** | 20h/sem | 8 sem | 160h | R$ 118.102,40 |
| **TOTAL PS** | | **8 semanas** | **600h** | **R$ 418.284,40** |

---

## [O] OTIMIZAÇÃO & INOVAÇÃO

### O-01 | Health Check — Auditoria Técnica Completa
**Capacidade:** Auditoria técnica de org Salesforce em produção + roadmap de otimizações

#### Escopo Técnico
- Auditoria técnica completa (código, configurações, segurança, performance)
- Relatório de Health Check (score por área + priorização de riscos)
- Roadmap de otimizações (quick-wins + melhorias estruturais)
- Análise de licenças (usuários inativos, subutilização)
- Recomendações de governança

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Senior Technical Architect** | 40h/sem | 4 sem | 160h | R$ 132.276,80 |
| **Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **Solution Architect** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **480h** | **R$ 350.374,40** |

---

### O-02 | AI Automation Boost — Einstein Features
**Capacidade:** Implementação de features Einstein para automatizar processos manuais (Next Best Action, Prediction Builder, GPT in Flows)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Agentforce Specialist** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **Technical Architect** | 20h/sem | 4 sem | 80h | R$ 66.138,40 |
| **Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **QA Consultant** | 20h/sem | 2 sem | 40h | R$ 21.455,60 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **6 semanas** | **520h** | **R$ 346.635,60** |

---

## [C] CHANGE MANAGEMENT & TREINAMENTO

### C-01 | Change Management — Até 100 Usuários
**Capacidade:** Gestão de mudança completa para projetos com até 100 usuários

#### Escopo Técnico
- Plano de gestão de mudança (stakeholders, comunicação, cronograma)
- Materiais de treinamento (manuais, vídeos, FAQs)
- Sessões de treinamento (end-users, power users, admins)
- Programa de Champions (embaixadores internos)
- Pesquisas de prontidão e feedback
- Suporte pós-go-live (30 dias)

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Change Manager** | 40h/sem | 6 sem | 240h | R$ 128.733,60 |
| **Business Analyst** | 20h/sem | 6 sem | 120h | R$ 64.366,80 |
| **Program Manager** | 20h/sem | 6 sem | 120h | R$ 88.576,80 |
| **TOTAL PS** | | **8 semanas** | **480h** | **R$ 281.677,20** |

---

### C-02 | Admin & Developer Bootcamp (5 pessoas)
**Capacidade:** Capacitação técnica de admins e devs internos para autonomia operacional

#### Escopo Técnico
- Bootcamp de Administradores (ADM-201 prep)
- Bootcamp de Desenvolvedores (Apex, Flows, LWC basics)
- Documentação técnica detalhada (runbooks, arquitetura)
- Sessões de shadowing (PS trabalhando junto com time interno)
- Certificação path recomendado

#### Esforço PS
| Perfil | Alocação | Duração | Total Horas | Valor c/imp |
|---|---|---|---:|---:|
| **Technical Architect** | 20h/sem | 4 sem | 80h | R$ 66.138,40 |
| **Senior Technical Consultant** | 40h/sem | 4 sem | 160h | R$ 99.995,20 |
| **Program Manager** | 20h/sem | 4 sem | 80h | R$ 59.051,20 |
| **TOTAL PS** | | **5 semanas** | **320h** | **R$ 225.184,80** |

---

# 📊 RESUMO — BLOCOS MAIS DEMANDADOS DATAPREV

Baseado nos projetos ativos (SGP, SEFIN-CE, Bolsão 3, DECIPEX):

| Ranking | Bloco | Frequência | ROI Típico | Observação |
|---------|-------|------------|-----------|------------|
| **1º** | **A-01** Agentforce WhatsApp Bot (3 topics) | 80% projetos | Muito Alto | Deflexão 30-60%, ROI <12m |
| **2º** | **M-01** Jornada MC WhatsApp (1 caso) | 70% projetos | Alto | Proativo + bot = solução completa |
| **3º** | **I-02** MuleSoft 1 API REST | 60% projetos | Alto | Viabiliza integração legados |
| **4º** | **D-01** Data Cloud Setup + 1 stream | 50% projetos | Alto | Unificação cadastral crítica |
| **5º** | **S-01** Service Cloud Console (20 agentes) | 40% projetos | Médio | Transbordo humano essencial |
| **6º** | **G-01** LGPD Audit & Remediation | 50% projetos | Muito Alto | Evita multa até R$ 50M |
| **7º** | **G-03** Hypercare 30 dias | 100% projetos | Alto | Estabilização pós-go-live |
| **8º** | **E-01** Experience Cloud Portal Cidadão | 30% projetos | Médio | Self-service reduz 20-40% carga |
| **9º** | **T-01** Tableau 3 dashboards | 40% projetos | Médio | Visibilidade executiva |
| **10º** | **C-01** Change Management (<100 users) | 30% projetos | Alto | Aumenta adoção 2-3× |

---

# 🛠️ COMO MONTAR UMA PROPOSTA

## Passo 1: Identificar necessidades do cliente
Exemplo: SEFIN-CE quer régua WhatsApp proativa + bot autoatendimento

## Passo 2: Selecionar blocos do catálogo
- **M-01** Jornada MC WhatsApp (1 caso): 6 sem, R$ 223k PS + R$ 520k licenças
- **A-01** Agentforce WhatsApp Bot (3 topics): 8 sem, R$ 381k PS + R$ 11k licenças
- **I-04** Integração nativa (2 APIs): 2×2 sem, R$ 180k PS + R$ 0 licenças
- **G-03** Hypercare 30 dias: 4 sem, R$ 243k PS + R$ 0 licenças

## Passo 3: Somar esforços
| Item | Duração | PS (R$) | Licenças (R$) |
|---|:---:|---:|---:|
| M-01 | 6 sem | 223.413 | 520.578 |
| A-01 | 8 sem | 381.476 | 11.801 |
| I-04 (×2) | 4 sem | 180.502 | 0 |
| G-03 | 4 sem | 243.097 | 0 |
| **TOTAL** | **22 sem** | **R$ 1.028.488** | **R$ 532.379** |

**Investimento Total: R$ 1.560.867** (PS + Licenças ano 1)

## Passo 4: Ajustar por paralelização
Se M-01 e A-01 podem rodar parcialmente em paralelo:
- Duração real: ~14-16 semanas (não 22)

## Passo 5: Adicionar contingência
- Contingência recomendada: +10% PS (riscos de integração)
- Valor final PS: R$ 1.131.337

---

# 🎯 CASOS DE USO COMPLETOS (COMBINAÇÕES)

## CASO 1: Cobrança Proativa WhatsApp (SEFIN-CE)
**Necessidade:** Régua de cobrança + bot autoatendimento

**Blocos:**
- M-01 Jornada MC WhatsApp (1 caso)
- A-01 Agentforce WhatsApp Bot (3 topics: IPTU, TMRSU, Cadastro)
- D-01 Data Cloud Setup + 1 stream (fonte: base tributária)
- I-04 Integração nativa (2 APIs: ConsultaImovel, EmitirDAM)
- G-03 Hypercare 30 dias

**Total:**
- **Duração:** 16-18 semanas (com paralelização)
- **PS:** R$ 1.131.337 c/contingência
- **Licenças ano 1:** R$ 761.513
- **TOTAL:** R$ 1.892.850

---

## CASO 2: Atendimento Multi-Ministério (Bolsão 3)
**Necessidade:** Agentes Slack internos + governança + monitoramento

**Blocos:**
- A-02 Agentforce Slack Bot (5 topics)
- S-01 Service Cloud Console (20 agentes para escalação)
- G-02 Center of Excellence Setup
- G-04 Hypercare Estendido 60 dias
- T-01 Tableau 3 dashboards (monitoramento operacional)

**Total:**
- **Duração:** 24-28 semanas
- **PS:** R$ 2.517.482
- **Licenças ano 1:** R$ 927.605
- **TOTAL:** R$ 3.445.087

---

## CASO 3: Gestão de Inativos (DECIPEX)
**Necessidade:** CRM atendimento + automação triagem SEI + analytics

**Blocos:**
- S-01 Service Cloud Console (20 agentes)
- A-02 Agentforce Slack Bot (5 topics: triagem processos SEI)
- D-01 Data Cloud Setup + 3 streams (CNIS, SIAP, CIAP)
- I-01 MuleSoft Setup Base
- I-02 MuleSoft 3 APIs REST (CNIS, SIAP, CIAF)
- T-01 Tableau 3 dashboards
- G-01 LGPD Audit & Remediation
- C-01 Change Management (100 usuários)
- G-04 Hypercare 60 dias

**Total:**
- **Duração:** 32-36 semanas
- **PS:** R$ 4.200.000 (aprox.)
- **Licenças ano 1:** R$ 2.800.000 (aprox.)
- **TOTAL:** R$ 7.000.000

---

## CASO 4: DFT/MGI (SGP)
**Necessidade:** Orquestração 19 sistemas legados + IA dimensionamento força trabalho

**Blocos:**
- S-01 Service Cloud Console (200 usuários DFT/MGI)
- A-01 Agentforce Bot (2 agentes: análise entregas + resumo executivo)
- D-01 Data Cloud Setup + 8 streams (PGD, SEI, PEI, etc.)
- I-01 MuleSoft Setup Base
- I-02 MuleSoft 8 APIs REST (1 por sistema legado)
- I-03 MuleSoft 1 API Orquestração (SISDIP central)
- E-01 Experience Cloud Portal (Carta de Serviços)
- T-01 Tableau 3 dashboards
- G-01 LGPD Audit
- C-02 Admin Bootcamp (5 pessoas Dataprev)
- G-04 Hypercare 60 dias

**Total (referência ROM real SGP v4.0):**
- **Duração:** 11 semanas (Otimista IA) / 14 semanas (Estimado)
- **PS:** R$ 1.655.170 c/imp
- **Licenças incrementais ano 1:** R$ 580.992
- **TOTAL:** R$ 2.236.162

---

# 📋 CHECKLIST DE PREMISSAS POR BLOCO

Antes de fechar proposta, validar premissas de cada bloco selecionado:

## Marketing Cloud (M-01, M-02, M-03)
- [ ] Templates HSM aprovados pela Meta
- [ ] Número WhatsApp Business provisionado
- [ ] Dados fonte têm CPF/CNPJ + telefone válidos
- [ ] Opt-in/Opt-out process definido
- [ ] Volume estimado de mensagens/mês

## Agentforce (A-01, A-02, A-03)
- [ ] APIs externas documentadas
- [ ] Knowledge Base fornecida pelo cliente
- [ ] Transbordo humano necessário? (adicionar Service Cloud)
- [ ] Volume de conversas/mês estimado

## Service Cloud (S-01, S-02)
- [ ] CTI já contratado (Twilio, Genesys)
- [ ] Licenças Service Cloud Unlimited disponíveis
- [ ] Canais definidos (email, chat, telefone, WhatsApp)

## Data Cloud (D-01, D-02, D-03)
- [ ] Fontes de dados têm API ou export viável
- [ ] Volume de registros estimado
- [ ] Identity Resolution necessária?

## MuleSoft (I-01, I-02, I-03)
- [ ] Sistema legado tem API ou banco acessível
- [ ] Documentação de API legada disponível
- [ ] Volume de chamadas/dia estimado
- [ ] Necessidade de orquestração complexa?

## Experience Cloud (E-01, E-02)
- [ ] SSO Gov.br ou SAML endpoint disponível
- [ ] Conteúdo das páginas fornecido
- [ ] Volume de membros estimado

## Tableau (T-01, T-02)
- [ ] Fontes de dados para dashboards definidas
- [ ] Quantidade de viewers estimada

## Governança (G-01, G-02, G-03, G-04)
- [ ] Requisitos LGPD mapeados
- [ ] Stakeholders de CoE identificados
- [ ] Duração de Hypercare acordada

---

# 🔄 ATUALIZAÇÕES FUTURAS DESTE CATÁLOGO

Este catálogo será atualizado conforme:
1. Novos blocos validados em projetos DATAPREV
2. Ajustes de sizing baseados em lições aprendidas
3. Novas capacidades Salesforce lançadas (ex: Agentforce Voice GA)
4. Feedback de AEs e clientes sobre granularidade/combinações

**Última atualização:** 2026-07-03  
**Próxima revisão:** 2026-08-01 (após conclusão SEFIN-CE e SGP)

---

**Contato:** Nelson Stebulaitis Filho | Services Sales Solution Manager | Salesforce PS LATAM
