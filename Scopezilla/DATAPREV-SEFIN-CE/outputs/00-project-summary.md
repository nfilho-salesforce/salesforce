# Project Summary — DATAPREV SEFIN Fortaleza

**Data:** 2026-07-03  
**Fase:** Discovery / RFP  
**Revisão:** v2.0 (Agentforce → Service Cloud + Einstein Bot)

---

## Executive Summary

SEFIN Fortaleza (Secretaria Municipal de Finanças) busca substituir o bot WhatsApp atual (fornecedor MUTANTE, R$ 1,7M/ano) por solução Salesforce Service Cloud + Einstein Bot para atendimento automatizado de tributos municipais (IPTU, TMRSU, ISS) e alteração cadastral. Projeto greenfield (nova ORG from scratch) com 400.000 conversas/ano inbound + 4,86M msgs/ano proativo opcional (ADD-ON Marketing Cloud). Escopo CORE inclui UX research; DATAPREV assume sustentação (AMS) pós-implantação.

---

## Company and Industry Context

### Cliente Final
- **Nome:** SEFIN — Secretaria Municipal de Finanças de Fortaleza
- **Município:** Fortaleza/CE
- **Público-alvo:** Cidadãos contribuintes (pessoas físicas e jurídicas)
- **Setor:** Administração Pública Municipal — arrecadação tributos

### Intermediário
- **Nome:** DATAPREV — Empresa de Tecnologia e Informações da Previdência
- **Tipo:** Empresa Pública Federal Brasileira
- **Papel:** Contrata Salesforce PS em nome de SEFIN; assume sustentação (AMS) após go-live

### Contexto Competitivo
- **Fornecedor atual:** MUTANTE — Bot WhatsApp tributos
- **Valor contrato MUTANTE:** R$ 1,7 milhão/ano
- **Situação:** Cliente insatisfeito com serviço MUTANTE
- **Objetivo estratégico:** Substituir MUTANTE por solução Salesforce com melhor UX e integrações robustas

---

## Current vs. Target Salesforce Landscape

### Current State
- **Nenhuma ORG Salesforce existente** — projeto greenfield

### Target State (v2.0 — Revisado 2026-07-03)

#### ESCOPO PRINCIPAL (CORE)
1. **Service Cloud** — Plataforma base
2. **Einstein Bot** — Bot WhatsApp para autoatendimento (400k conversas/ano)
   - Licenciamento: Einstein Bot Conversations (400.000 conversas/ano)
3. **WhatsApp Channel** — Canal único de comunicação (sem Digital Engagement)
4. **Nova ORG Setup** — Setup completo Salesforce from scratch (era ADD-ON v1.0, agora CORE)
5. **UX Research** — Incluído no escopo PS: personas, testes usabilidade, análise acessibilidade (WCAG)

#### ADD-ONs (Opcionais — Estimativa Separada)
1. **Knowledge Base Externa com Vetorização**
   - Ingestão de base de conhecimento externa ao Salesforce
   - Vetorização no Data Cloud
   - Einstein Bot responde dúvidas via KB
   - **Status:** Volume e formato a definir (Q-F v1.0)

2. **Marketing Cloud para Régua Proativa**
   - Setup Marketing Cloud
   - 1 jornada de comunicação (ex: cidadãos com IPTU vencido)
   - 1 fonte de dados zero-copy no Data Cloud
   - 1 segmentação (sem Identity Resolution)
   - **Volume:** 4,86M msgs WhatsApp/ano = ~405.000/mês = ~13.500/dia
   - **Status:** Opcional; cliente decide se inclui

### Usuários
- **3 usuários System Administrator** — gestão plataforma
- **7 usuários perfil customizado "Bot Maintainer"** — manutenção/evolução Einstein Bot + revisão conversas
  - **Premissa:** Permissões limitadas a Einstein Bot + revisão conversas (sem Flows, sem API logs)
  - **Validação:** Q-15 para cliente confirmar escopo de permissões
- **Total:** 10 usuários Service Cloud

---

## Project Scope and Objectives

### Objetivo Principal
Bot WhatsApp para **atendimento automatizado** de tributos municipais (IPTU, TMRSU, ISS) e **alteração cadastral**, com:
- Autoatendimento via Einstein Bot (Service Cloud)
- Emissão de DAM (Documento de Arrecadação Municipal) — boleto pagamento tributos
- Integração com APIs SEFIN via Flow Orchestration + Apex (sem MuleSoft)
- Alteração cadastral online (nome, telefone, email, endereço completo)
- Pesquisa de satisfação pós-atendimento (obrigatória)

### Funcionalidades do Bot Confirmadas

#### 1. Menu Inicial
- Linguagem natural (sem botões rígidos)
- Bot apresenta 4 opções:
  1. Consulta IPTU
  2. Boleto taxa do lixo (TMRSU)
  3. ISS (Imposto Sobre Serviços)
  4. Alteração cadastral
  5. Preciso de ajuda (KB externa — ADD-ON 1)

#### 2. Fluxo IPTU / TMRSU
1. Bot coleta CPF/CNPJ + data nascimento/abertura
2. Flow/Apex chama **API ConsultaImovel** (por-documento)
3. Bot apresenta inscrições municipais do contribuinte
4. Cidadão seleciona 1 ou mais inscrições
5. **Loop:** para cada inscrição selecionada
   - Bot confirma emissão DAM
   - Se SIM: Flow/Apex chama **API EmitirDamUnico** → envia PDF via WhatsApp
   - Se NÃO: pula para próxima inscrição
6. Pesquisa de satisfação (1-5 estrelas)
7. Se nota ≤3: coleta justificativa
8. Flow/Apex chama **API CRM SEFIN** (log satisfação)
9. Despedida + link Portal SEFIN

#### 3. Fluxo ISS
- **Escopo atual (confirmado):** Bot informa link site SEFIN (sem coleta CPF/CNPJ, sem emissão DAM)
- **Validação pendente:** Q-04/Q-05 — cliente pode decidir mudar para emissão DAM via API como IPTU/TMRSU

#### 4. Fluxo Alteração Cadastral
1. Bot coleta CPF/CNPJ + data nascimento/abertura
2. Flow/Apex chama API (ConsultaImovel ou **API Dados Cadastrais** — a definir Q-02)
3. Bot apresenta campos cadastrais atuais:
   - CPF/CNPJ (não editável)
   - Nome
   - Telefone
   - Email
   - Endereço (logradouro, número, complemento, bairro, CEP, cidade, estado)
4. Bot pergunta: "Confirma dados ou deseja alterar?"
5. Se ALTERAR: para cada campo editável
   - Bot solicita novo valor
   - Máximo 2 tentativas se digitação inválida
6. Bot apresenta resumo final
7. Cidadão confirma alteração
8. Flow/Apex chama **API Dados Cadastrais** (salva alterações)
9. Pesquisa de satisfação
10. Flow/Apex chama **API CRM SEFIN**
11. Despedida + link Portal SEFIN

#### 5. Pesquisa de Satisfação (Obrigatória)
- Executada ao final de todos os fluxos (IPTU, TMRSU, ISS, Alteração Cadastral)
- 1-5 estrelas
- Se nota ≤3: coleta justificativa livre
- Log via **API CRM SEFIN** (REST + API Key)

---

## Data and Integration Architecture

### APIs SEFIN Mapeadas

#### API 1 — EmitirDamUnico (CONFIRMADA)
Emite o DAM (Documento de Arrecadação Municipal) — boleto de pagamento de tributos.

**Parâmetros:**
- `tipoDebito` (Integer 3): TMRSU=980, IPTU=10, ISS=??? (a confirmar Q-05)
- `tipoPessoa` (String 1): F = física, J = jurídica
- `cpfcnpj` (String 14): Somente números
- `inscricao` (Integer 7): Inscrição municipal do imóvel (opcional)
- `digito` (Integer 1): Obrigatório se inscricao informada
- `tipoPagamento` (String 9): COTAUNICA ou PARCELADO
- `AnoDebito` (Integer 4): Ano do débito (opcional)
- `periodoParcelas` (Date): Obrigatório se PARCELADO

**Retorno:** Link PDF do DAM pronto para download/envio via WhatsApp.

#### API 2 — ConsultaImovel (CONFIRMADA)
Dois métodos: por inscrição do imóvel ou por documento (CPF/CNPJ).

**Por-inscricao:**
- Inscrição(8) + Dígito(1) + Exercício(4)
- Retorna: Cartografia, Localização, Correspondência, Lista de Sujeitos Passivos

**Por-documento:**
- Tipo(Física/Jurídica) + Documento(CPF/CNPJ) + Data(nasc./abertura) + Exercício(4)
- Retorna: Inscrição do imóvel, Endereço, Cartografia, Titular

#### API 3 — CRM SEFIN (NOVA — A DEFINIR)
API para log de pesquisa de satisfação.

**Premissas:**
- Protocolo: REST
- Autenticação: API Key
- Payload: dados cadastrais apenas (CPF/CNPJ, nome, nota satisfação, justificativa)

**A definir com cliente (Q-01):**
- Endpoint URL
- Formato payload exato
- Headers necessários
- Resposta esperada

#### API 4 — Dados Cadastrais (NOVA — A DEFINIR)
API para atualização cadastral do contribuinte.

**Premissas:**
- Protocolo: REST
- Autenticação: API Key
- Payload: dados cadastrais (nome, telefone, email, endereço completo)

**A definir com cliente (Q-02):**
- Endpoint URL
- Formato payload exato
- Headers necessários
- Validações necessárias (CEP, telefone, email?)
- CPF/CNPJ é enviado apenas como chave (não editável)

### Padrão de Integração
- **Flow Orchestration + Apex** (sem MuleSoft)
- **Conectividade:** Service Cloud → APIs SEFIN via IP direto (P-17: cliente possui conectividade)
- **Autenticação:** API Key (todas as APIs)
- **Retentativa:** Falha API = 1 retentativa → se falhar informa "tente novamente mais tarde" → encerra (P-16)

### Data Migration
- **Greenfield** — sem migração de dados (P-18: nova ORG from scratch)

---

## Compliance and Regulatory

### LGPD (Lei Geral de Proteção de Dados)
- **Art. 11:** Dados de CPF/CNPJ são dados pessoais
- **Dados sensíveis:** Débitos tributários podem ser considerados dados sensíveis dependendo do contexto
- **Residência de dados:** Salesforce região geograficamente aprovada (conforme contrato DATAPREV — P-22)

### Licitação Pública
- **Lei 14.133/2021** (Nova Lei de Licitações)
- **Número processo licitatório:** Q-13 (a confirmar com cliente)

### Aprovações Internas
- **CTID DATAPREV** — Comitê de TI e Dados (P-23: aprovação Service Cloud já obtida)
- **ANPD** — Autoridade Nacional de Proteção de Dados (possível envolvimento se dados sensíveis)

---

## Volume and Sizing

### Escopo Principal (Einstein Bot Core)
- **Inbound (chatbot):** 400.000 conversas/ano = ~33.333/mês
- **Licenciamento:** Einstein Bot Conversations (400.000 conversas/ano)

### ADD-ON 2 — Marketing Cloud (Opcional)
- **Outbound (proativo):** 4.860.000 msgs WhatsApp/ano = ~405.000/mês = ~13.500/dia
- **Licenciamento:** WhatsApp Messaging (4,86M msgs/ano)

---

## Premissas Consolidadas (v2.0)

### Fluxo e Experiência
| # | Premissa |
|---|---|
| P-01 | Todo encerramento = Pesquisa de satisfação → API CRM SEFIN (log) → Despedida com link Portal SEFIN |
| P-02 | Transbordo humano confirmado via Omni-Channel Enhanced/Service Console (E09). DHA dentro do horário coleta nome e cria Case/Messaging Session roteado para 1 das 3 PAs (turno único) |
| P-03 | Pesquisa de satisfação em todos os fluxos (IPTU, TMRSU, ISS, Alteração Cadastral) |
| P-04 | Notas ≤3 estrelas → bot coleta justificativa antes de encerrar |
| P-05 | Máximo 2 tentativas de digitação inválida em qualquer campo, depois encerra |
| P-06 | Usuário já identificado na sessão → pula identificação e vai direto ao Menu |
| P-07 | Bot self-service disponível 24/7; transbordo humano restrito ao Business Hours 08h-17h, segunda a sexta (G0904 resolvido — E09) |

### Alteração Cadastral
| # | Premissa |
|---|---|
| P-08 | Campos cadastrais: CPF/CNPJ (não editável), nome, telefone, email, endereço completo |
| P-09 | Endereço completo: logradouro, número, complemento, bairro, CEP, cidade, estado |
| P-10 | CPF/CNPJ é chave única — não pode ser alterado pelo cidadão |
| P-11 | Sem validação automática de CEP, telefone ou email na v1.0 (a confirmar com cliente Q-03) |

### APIs e Integrações
| # | Premissa |
|---|---|
| P-12 | API EmitirDamUnico e ConsultaImovel já existem e estão prontas para consumo |
| P-13 | API CRM SEFIN (log satisfação) será entregue pelo cliente — REST + API Key |
| P-14 | API Dados Cadastrais (alteração) será entregue pelo cliente — REST + API Key |
| P-15 | ISS continua apenas informando link do site (sem emissão DAM) — a confirmar Q-04/Q-05 |
| P-16 | Falha de API = 1 retentativa → se falhar informa "tente novamente mais tarde" → encerra |
| P-17 | Cliente possui conectividade IP entre Service Cloud e APIs SEFIN (sem MuleSoft) |

### Infraestrutura e Segurança
| # | Premissa |
|---|---|
| P-18 | Nova ORG Salesforce from scratch (não há ORG existente) |
| P-19 | LGPD obrigatória — dados de CPF/CNPJ são dados pessoais sensíveis (Art. 11) |
| P-20 | Contratação canal WhatsApp Business é com Meta/Facebook, não Salesforce |
| P-21 | Licitação pública via Lei 14.133/2021 (Nova Lei de Licitações) |
| P-22 | Residência de dados: Salesforce região geograficamente aprovada (conforme contrato DATAPREV) |
| P-23 | DATAPREV já possui aprovação CTID para uso Service Cloud |

### Escopo e Entrega
| # | Premissa |
|---|---|
| P-24 | Salesforce PS não fornece licenças — cliente contrata diretamente |
| P-25 | Service Cloud AS-IS: Einstein Bot + WhatsApp + Omni-Channel/Service Console para transbordo humano (E09); sem Case Management ou Contact/Account Management completos |
| P-26 | 10 usuários Service Cloud: 3 System Admin + 7 perfil customizado (bot maintainer) |
| P-27 | DATAPREV assume treinamento dos 10 usuários — PS entrega documentação apenas (sem sessões ao vivo) |
| P-28 | DATAPREV assume sustentação (AMS) pós-implantação |
| P-29 | Loop de emissão de DAM se repete para todas as inscrições selecionadas |
| P-30 | Sem limite de inscrições — bot apresenta todas retornadas pela API |

### UX e Acessibilidade (NEW v2.0)
| # | Premissa |
|---|---|
| P-31 | **UX Research incluída no escopo PS:** personas, testes usabilidade, análise acessibilidade (WCAG) |

---

## Budget and Funding

### Envelope Orçamentário
- **Budget formal:** < R$ 1,7 milhão/ano (valor contrato MUTANTE)
- **Previsão licenças Salesforce:** R$ 1,2–1,5 milhão/ano
- **Referência histórica DATAPREV:** ~R$ 715/h por developer (tabela interna)
- **Estimativa anterior (Fernanda AE):** 800h considerada "mais do que o necessário" (Augusto DATAPREV)

---

## Stakeholders

### Salesforce Professional Services
- **Alex Siqueira** — AP (Account Partner) PS Salesforce
- **Oswaldo Melo** — SE (Solution Engineer) Salesforce

### DATAPREV
- **Augusto** — mencionado em contexto de estimativa horas

### SEFIN Fortaleza
- **Sponsors a definir** — Q-17 (incluir nome/cargo tomadores de decisão SEFIN)

---

## Key Risks and Constraints

### Riscos Técnicos
1. **Dependência APIs cliente** — Q-01/Q-02: especificações APIs CRM SEFIN e Dados Cadastrais pendentes
2. **Conectividade IP** — P-17: Service Cloud ↔ APIs SEFIN precisa ser validada em ambiente de testes
3. **Canal WhatsApp Business** — P-20: contratação via Meta/Facebook (não Salesforce); latência aprovação Meta pode atrasar go-live

### Riscos de Gestão
4. **Licitação pública** — Q-13: número processo licitatório desconhecido; possíveis bloqueios jurídicos
5. **Deadline desconhecido** — Q-11/Q-12/Q-14: data vencimento contrato MUTANTE e janela go-live não definidas
6. **Janela de manutenção** — Q-14: possível blackout em período arrecadação IPTU (janeiro/fevereiro)

### Riscos de Escopo
7. **ISS indeciso** — Q-04/Q-05: fluxo ISS pode mudar de "link site" para "emissão DAM via API" (impacta esforço)
8. **Perfil Bot Maintainer** — Q-15: permissões não validadas com cliente (impacta security model)
9. **ADD-ONs opcionais** — KB externa e Marketing Cloud não decididos; podem ser incluídos no meio do projeto

---

## Open Questions for Client (Q-01 to Q-17)

### APIs e Integrações
| # | Pergunta |
|---|---|
| Q-01 | API CRM SEFIN (log satisfação): qual endpoint, payload exato, headers, autenticação? |
| Q-02 | API Dados Cadastrais: qual endpoint, payload exato, headers, autenticação? |
| Q-03 | Validação campos cadastrais: deve validar CEP (ViaCEP)? Telefone? Email? Ou apenas salva? |
| Q-04 | ISS: continua apenas link do site ou muda para emissão DAM via API (como IPTU/TMRSU)? |
| Q-05 | Se ISS mudar para emissão DAM: qual `tipoDebito` usar na API EmitirDamUnico? |

### Experiência do Usuário
| # | Pergunta |
|---|---|
| Q-06 | Qual é a URL do Portal SEFIN para link de despedida? |
| Q-07 | Mensagem de despedida padrão: tem texto preferencial ou deixamos genérico? |
| Q-08 | Cidadão pode solicitar opt-out de mensagens proativas (ADD-ON Marketing Cloud)? |

### Dados e Volume
| # | Pergunta |
|---|---|
| Q-09 | MUTANTE entrega dados históricos de volume/uso para sizing mais preciso? |
| Q-10 | Base contribuintes SEFIN com CPF/CNPJ válido e atualizado para Marketing Cloud (ADD-ON)? |

### Timeline e Contrato
| # | Pergunta |
|---|---|
| Q-11 | Qual a data de vencimento do contrato MUTANTE? |
| Q-12 | Deadline desejado para go-live? |
| Q-13 | Número do processo licitatório? |
| Q-14 | Há janela de manutenção ou blackout para evitar (ex: período de arrecadação IPTU)? |

### Usuários e Perfis
| # | Pergunta |
|---|---|
| Q-15 | Perfil customizado "Bot Maintainer": precisa de permissões além de Einstein Bot + revisão conversas? |
| Q-16 | Usuários revisam conversas via Service Cloud Console ou via relatório/dashboard? |

### Stakeholders (NEW v2.0)
| # | Pergunta |
|---|---|
| Q-17 | Quem são os sponsors/tomadores de decisão do lado SEFIN Fortaleza? (nome, cargo, papel na decisão) |

---

## Research Findings

### Competitive Context
- **MUTANTE:** Fornecedor atual de bot WhatsApp tributos municipais
- **Contrato:** R$ 1,7 milhão/ano
- **Satisfação:** Cliente insatisfeito (motivação substituição)
- **Benchmark Salesforce:** Solução deve ser mais robusta (integração nativa, UX superior, escalabilidade)

### Market Context
- **Governo Municipal Brasileiro:** Setor em transformação digital (Lei 14.133/2021 incentiva licitações para soluções cloud)
- **LGPD:** Compliance obrigatório para dados de CPF/CNPJ (Art. 11)
- **WhatsApp Business:** Canal preferencial de comunicação governo-cidadão no Brasil (penetração >90%)

### Salesforce Ecosystem
- **Einstein Bot:** Produto maduro para autoatendimento WhatsApp (desde 2019)
- **Service Cloud:** Plataforma líder Gartner Magic Quadrant Customer Service & Support
- **Flow Orchestration + Apex:** Padrão Salesforce para integrações REST API (sem MuleSoft)

---

## Next Steps

1. **Validar perguntas Q-01 a Q-17 com cliente (SEFIN / DATAPREV)**
2. **Executar skill `requirements`** — definir épicas, gap analysis, user stories
3. **Executar skill `design`** — arquitetura de solução, integrações, security model
4. **Executar skill `roadmap`** — plano de entregas, milestones, dependências
5. **Executar skill `efficiency`** — análise de otimizações + ganho de IA (≥25%)
6. **Executar skill `narratives`** — briefing executivo, pitch de valor, resumo técnico
7. **Executar skill `export`** — gerar PPT, PDF, site Heroku (SLDS)

---

**Documento gerado automaticamente via Scopezilla — Salesforce PS LATAM**
