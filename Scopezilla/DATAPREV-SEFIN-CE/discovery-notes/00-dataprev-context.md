# Contexto Dataprev — SEFIN Fortaleza (Revisão v2.0)

## Identificação
- **Projeto:** SEFIN Fortaleza — Bot WhatsApp Tributos Municipais
- **Cliente:** DATAPREV — Empresa de Tecnologia e Informações da Previdência
- **Cliente Final:** SEFIN (Secretaria Municipal de Finanças de Fortaleza)
- **Município:** Fortaleza/CE
- **Público:** Cidadãos de Fortaleza (contribuintes PF/PJ)

## Contexto Competitivo
- **Fornecedor atual:** MUTANTE — Bot WhatsApp tributos
- **Valor contrato MUTANTE:** R$ 1,7 milhão/ano
- **Situação:** Cliente insatisfeito com serviço MUTANTE
- **Objetivo:** Substituir solução MUTANTE por Salesforce Service Cloud + Einstein Bot

## Produtos Salesforce in-scope

### ESCOPO PRINCIPAL (CORE)
- **Service Cloud** — Plataforma base + Einstein Bot
- **Einstein Bot** — Bot WhatsApp para autoatendimento (400k conversas/ano)
- **WhatsApp Channel** — Canal único de comunicação (sem Digital Engagement)
- **Nova ORG Setup** — Setup completo Salesforce from scratch (era ADD-ON, agora CORE)

### ADD-ONs (Opcionais — Estimativa Separada)
1. **Knowledge Base Externa com Vetorização**
   - Ingestão de base de conhecimento externa ao Salesforce
   - Vetorização no Data Cloud
   - Einstein Bot responde dúvidas via KB
   
2. **Marketing Cloud para Régua Proativa**
   - Setup Marketing Cloud
   - 1 jornada de comunicação (ex: cidadãos com IPTU vencido)
   - 1 fonte de dados zero-copy no Data Cloud
   - 1 segmentação (sem Identity Resolution)
   - Volume: 4,86M msgs/ano

## Objetivo do Projeto

Bot WhatsApp para **atendimento automatizado** de tributos municipais (IPTU, TMRSU, ISS) e **alteração cadastral**, com:
- Autoatendimento via Einstein Bot (Service Cloud)
- Emissão de DAM (Documento de Arrecadação Municipal)
- Integração com APIs SEFIN (EmitirDamUnico, ConsultaImovel)
- Alteração cadastral online
- Pesquisa de satisfação pós-atendimento

## Fase Atual
**Discovery / RFP** — revisão de escopo 2026-07-03

## Volumes para Sizing

### Escopo Principal (Einstein Bot Core)
- **Inbound (chatbot):** 400.000 conversas/ano = ~33.333/mês

### ADD-ON 2 — Marketing Cloud (Opcional)
- **Outbound (proativo):** 4.860.000 msgs WhatsApp/ano = ~405.000/mês = ~13.500/dia

## Usuários Service Cloud
- **3 usuários System Administrator** — gestão plataforma
- **~7 usuários perfil customizado** — manutenção/evolução Einstein Bot + revisão conversas
- **Total:** 10 usuários Service Cloud

## APIs SEFIN Mapeadas

### API 1 — EmitirDamUnico (CONFIRMADA)
Emite o DAM (Documento de Arrecadação Municipal) — boleto de pagamento de tributos.

**Parâmetros:**
- `tipoDebito` (Integer 3): TMRSU=980, IPTU=10, ISS=??? (a confirmar)
- `tipoPessoa` (String 1): F = física, J = jurídica
- `cpfcnpj` (String 14): Somente números
- `inscricao` (Integer 7): Inscrição municipal do imóvel (opcional)
- `digito` (Integer 1): Obrigatório se inscricao informada
- `tipoPagamento` (String 9): COTAUNICA ou PARCELADO
- `AnoDebito` (Integer 4): Ano do débito (opcional)
- `periodoParcelas` (Date): Obrigatório se PARCELADO

**Retorno:** Link PDF do DAM pronto para download/envio via WhatsApp.

### API 2 — ConsultaImovel (CONFIRMADA)
Dois métodos: por inscrição do imóvel ou por documento (CPF/CNPJ).

**Por-inscricao:**
- Inscrição(8) + Dígito(1) + Exercício(4)
- Retorna: Cartografia, Localização, Correspondência, Lista de Sujeitos Passivos

**Por-documento:**
- Tipo(Física/Jurídica) + Documento(CPF/CNPJ) + Data(nasc./abertura) + Exercício(4)
- Retorna: Inscrição do imóvel, Endereço, Cartografia, Titular

### API 3 — CRM SEFIN (NOVA — A DEFINIR)
API para log de pesquisa de satisfação.

**Premissas:**
- Protocolo: REST
- Autenticação: API Key
- Payload: dados cadastrais apenas (CPF/CNPJ, nome, nota satisfação, justificativa)

**A definir com cliente:**
- Endpoint URL
- Formato payload exato
- Headers necessários
- Resposta esperada

### API 4 — Dados Cadastrais (NOVA — A DEFINIR)
API para atualização cadastral do contribuinte.

**Premissas:**
- Protocolo: REST
- Autenticação: API Key
- Payload: dados cadastrais (nome, telefone, email, endereço completo)

**A definir com cliente:**
- Endpoint URL
- Formato payload exato
- Headers necessários
- Validações necessárias (CEP, telefone, email?)
- CPF/CNPJ é enviado apenas como chave (não editável)

## Fluxo de Integração Revisado

```
Cidadão inicia conversa WhatsApp
  → Einstein Bot saúda e apresenta menu (linguagem natural)
  
Cidadão escolhe serviço:
  
  [IPTU ou TMRSU]
    → Bot coleta CPF/CNPJ + data nascimento/abertura
    → Flow/Apex chama ConsultaImovel (por-documento)
    → Bot apresenta inscrições do contribuinte
    → Cidadão seleciona 1 ou mais inscrições
    → Loop: para cada inscrição selecionada
        → Bot confirma emissão DAM
        → Se SIM: Flow/Apex chama EmitirDamUnico → envia PDF via WhatsApp
        → Se NÃO: pula para próxima inscrição
    → Pesquisa de satisfação (1-5 estrelas)
    → Se nota ≤3: coleta justificativa
    → Flow/Apex chama API CRM SEFIN (log satisfação)
    → Despedida + link Portal SEFIN
    
  [ISS]
    → Bot informa link site SEFIN (sem coleta CPF/CNPJ)
    → Pesquisa de satisfação
    → Flow/Apex chama API CRM SEFIN
    → Despedida + link Portal SEFIN
    
  [ALTERAÇÃO CADASTRAL]
    → Bot coleta CPF/CNPJ + data nascimento/abertura
    → Flow/Apex chama ConsultaImovel ou API busca dados cadastrais (a definir)
    → Bot apresenta campos cadastrais atuais:
        - CPF/CNPJ (não editável)
        - Nome
        - Telefone
        - Email
        - Endereço (logradouro, número, complemento, bairro, CEP, cidade, estado)
    → Bot pergunta: "Confirma dados ou deseja alterar?"
    → Se CONFIRMA: prossegue
    → Se ALTERAR: para cada campo editável
        - Bot solicita novo valor
        - Máximo 2 tentativas se digitação inválida
    → Bot apresenta resumo final
    → Cidadão confirma alteração
    → Flow/Apex chama API Dados Cadastrais (salva alterações)
    → Pesquisa de satisfação
    → Flow/Apex chama API CRM SEFIN
    → Despedida + link Portal SEFIN
```

## Funcionalidades do Bot Confirmadas

1. **Menu inicial em linguagem natural** (sem botões rígidos)
2. **Consulta IPTU** → API ConsultaImovel + EmitirDamUnico → PDF DAM
3. **Boleto taxa do lixo (TMRSU)** → mesmo fluxo, tipoDebito=980
4. **ISS** → informa link site SEFIN (sem emissão DAM — a confirmar se muda)
5. **Alteração Cadastral** → consulta dados atuais → coleta alterações → salva via API
6. **Pesquisa de satisfação** — obrigatória ao final de cada atendimento (1-5 estrelas + justificativa se ≤3)
7. **Log via API CRM SEFIN** — registra nota e justificativa de satisfação

## Premissas Consolidadas (v2.0)

### Fluxo e Experiência
| # | Premissa |
|---|---|
| P-01 | Todo encerramento = Pesquisa de satisfação → API CRM SEFIN (log) → Despedida com link Portal SEFIN |
| P-02 | Sem transbordo humano — bot encerra automaticamente apresentando link Portal SEFIN |
| P-03 | Pesquisa de satisfação em todos os fluxos (IPTU, TMRSU, ISS, Alteração Cadastral) |
| P-04 | Notas ≤3 estrelas → bot coleta justificativa antes de encerrar |
| P-05 | Máximo 2 tentativas de digitação inválida em qualquer campo, depois encerra |
| P-06 | Usuário já identificado na sessão → pula identificação e vai direto ao Menu |
| P-07 | Sem horário de atendimento — bot disponível 24/7 |

### Alteração Cadastral
| # | Premissa |
|---|---|
| P-08 | Campos cadastrais: CPF/CNPJ (não editável), nome, telefone, email, endereço completo |
| P-09 | Endereço completo: logradouro, número, complemento, bairro, CEP, cidade, estado |
| P-10 | CPF/CNPJ é chave única — não pode ser alterado pelo cidadão |
| P-11 | Sem validação automática de CEP, telefone ou email na v1.0 (a confirmar com cliente) |

### APIs e Integrações
| # | Premissa |
|---|---|
| P-12 | API EmitirDamUnico e ConsultaImovel já existem e estão prontas para consumo |
| P-13 | API CRM SEFIN (log satisfação) será entregue pelo cliente — REST + API Key |
| P-14 | API Dados Cadastrais (alteração) será entregue pelo cliente — REST + API Key |
| P-15 | ISS continua apenas informando link do site (sem emissão DAM) — a confirmar |
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
| P-25 | Service Cloud AS-IS: apenas Einstein Bot + WhatsApp (sem Case Management, sem Service Console) |
| P-26 | 10 usuários Service Cloud: 3 System Admin + 7 perfil customizado (bot maintainer) |
| P-27 | Treinamento de administradores não incluído no escopo core |
| P-28 | DATAPREV assume sustentação (AMS) pós-implantação |
| P-29 | Loop de emissão de DAM se repete para todas as inscrições selecionadas |
| P-30 | Sem limite de inscrições — bot apresenta todas retornadas pela API |

## Perguntas em Aberto para o Cliente (v2.0)

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

## Documentos Disponíveis

- Fluxo de atendimento v1.0 (anterior): `/Users/nfilho/claude/SEFIN_CE_Fluxo_v1_FINAL.png`
- Fluxo v2.0 (revisado): a ser gerado após confirmação

## Contexto Regulatório e Técnico

- **LGPD obrigatória** — dados de CPF/CNPJ são dados pessoais; débitos tributários dados sensíveis (Art. 11)
- **Licitação pública:** Lei 14.133/2021 (Nova Lei de Licitações)
- **Integrações:** APIs SEFIN via Flow/Apex (sem MuleSoft)
- **Infraestrutura:** DATAPREV opera híbrido (on-premise + cloud gov OCI/GovCloud)
- **Aprovações:** CTID DATAPREV, possível envolvimento ANPD
- **Idioma:** PT-BR
- **Moeda:** BRL
- **Imposto LATAM Brasil:** 75,35% sobre valor líquido

## Próximos Passos

1. Validar perguntas Q-01 a Q-16 com cliente (SEFIN / DATAPREV)
2. Executar skill `/dataprev` completo com novo escopo
3. Gerar artefatos:
   - Fluxo revisado (diagrama + transcrição)
   - Épicas e gap analysis
   - Arquitetura e design decisions
   - Efficiency analysis
   - Narratives
   - Investimento (PS + Licenças)
4. Publicar plano completo no Heroku com sidebar navegável
