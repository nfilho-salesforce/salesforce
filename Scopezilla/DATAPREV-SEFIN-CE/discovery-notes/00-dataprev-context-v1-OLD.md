# Contexto Dataprev — SEFIN-CE

## Identificação
- Projeto: SEFIN-CE — Secretaria da Fazenda do Estado do Ceará
- Cliente: Dataprev — Empresa de Tecnologia e Informações da Previdência
- Tipo: Governo Federal Brasileiro
- Cliente Final: CFIN (Coordenadoria de Finanças — SEFIN-CE) / Prefeitura de Fortaleza

## Produtos Salesforce in-scope

### ESCOPO PRINCIPAL
- **Agentforce** — Bot WhatsApp para autoatendimento
- **WhatsApp Channel** — Canal único de comunicação

### ADD-ONs (Opcionais — Estimativa Separada)
1. **Setup Agentforce + Data Cloud**
   - Cenário A: Nova ORG (setup completo from scratch)
   - Cenário B: ORG Existente Dataprev (configuração incremental)

2. **Marketing Cloud para Régua Proativa**
   - Setup Marketing Cloud
   - 1 jornada de comunicação (ex: cidadãos com IPTU vencido)
   - 1 fonte de dados zero-copy no Data Cloud
   - 1 segmentação (sem Identity Resolution)
   - Premissa: CPF/CNPJ + Nro de Inscrição confiável na base fonte
   - Volume: 4,86M msgs/ano

3. **Knowledge Base Externa com Vetorização**
   - Ingestão de base de conhecimento externa ao Salesforce
   - Vetorização no Data Cloud
   - Agente responde "outros assuntos" via KB (substitui redirecionamento ao site)

## Objetivo do Projeto

Bot WhatsApp para **régua de cobrança proativa** de tributos municipais (IPTU, TMRSU — Taxa de Manejo de Resíduos Sólidos Urbanos), com:
- Autoatendimento via Agentforce
- Emissão de DAM (Documento de Arrecadação Municipal)
- Integração com APIs SEFIN-CE (EmitirDamUnico, ConsultaImovel)
- Consulta de débitos e geração de boletos
- Atualização cadastral

## Fase Atual
**Discovery / RFP** — reunião realizada 2026-07-01

## Volumes para Sizing

### Escopo Principal (Agentforce Core)
- **Inbound (chatbot)**: 400.000 conversas/ano = ~33.333/mês

### ADD-ON 2 — Marketing Cloud (Opcional)
- **Outbound (proativo)**: 4.860.000 msgs WhatsApp/ano = ~405.000/mês = ~13.500/dia

## APIs SEFIN-CE Mapeadas

### API 1 — EmitirDamUnico
Emite o DAM (Documento de Arrecadação Municipal) — boleto de pagamento de tributos.

**Parâmetros:**
- `tipoDebito` (Integer 3): TMRSU=980, IPTU=10
- `tipoPessoa` (String 1): F = física, J = jurídica
- `cpfcnpj` (String 14): Somente números
- `inscricao` (Integer 7): Inscrição municipal do imóvel (opcional)
- `digito` (Integer 1): Obrigatório se inscricao informada
- `tipoPagamento` (String 9): COTAUNICA ou PARCELADO
- `AnoDebito` (Integer 4): Ano do débito (opcional)
- `periodoParcelas` (Date): Obrigatório se PARCELADO

**Retorno:** Link PDF do DAM pronto para download/envio via WhatsApp.

### API 2 — ConsultaImovel
Dois métodos: por inscrição do imóvel ou por documento (CPF/CNPJ).

**Por-inscricao:**
- Inscrição(8) + Dígito(1) + Exercício(4)
- Retorna: Cartografia, Localização, Correspondência, Lista de Sujeitos Passivos

**Por-documento:**
- Tipo(Física/Jurídica) + Documento(CPF/CNPJ) + Data(nasc./abertura) + Exercício(4)
- Retorna: Inscrição do imóvel, Endereço, Cartografia, Titular

## Fluxo de Integração

```
Gatilho (vencimento/débito — ADD-ON 2: Marketing Cloud)
  → Salesforce Flow busca CPF/CNPJ do contribuinte
  → Flow/Apex chama ConsultaImovel (por-documento)
    → Valida dados do titular + imóvel
  → Flow/Apex chama EmitirDamUnico (COTAUNICA ou PARCELADO)
    → Obtém link PDF do DAM
  → WhatsApp proativo com link do boleto (ADD-ON 2)
  OU
  → Cidadão inicia conversa → Agentforce (chatbot) assume
    → Pode emitir DAM, tirar dúvidas, consultar débitos
```

## Funcionalidades do Bot Confirmadas

1. **Menu inicial em linguagem natural** (sem botões rígidos estilo RCS)
2. **Consulta IPTU** → API ConsultaImovel + EmitirDamUnico → PDF DAM
3. **Boleto taxa do lixo (TMRSU)** → mesmo fluxo, tipoDebito=980
4. **Atualização cadastral** → subfluxo via API
5. **Coleta de CNPJ/CPF/inscrição** → via Flow nativo
6. **Geração e envio de PDF** → via Apex

## Estimativa Prévia

**Situação (2026-07-01):**
- Estimativa de 800h foi passada por **Fernanda** (AE anterior) para DATAPREV
- Augusto (DATAPREV) entende que 800h é **mais do que o necessário**
- Alex Siqueira (AE) vai revisar com Nelson se quantidade de horas é compatível
- Valor ~R$ 1,3M já inclui markup DATAPREV (não é o valor Salesforce puro)
- Referência interna: ~R$ 715/h por developer (tabela DTP)

**Novo escopo (2026-07-02):**
- **ESCOPO PRINCIPAL:** Agentforce + WhatsApp (sem Service Cloud/Digital Engagement)
- **Estimativa a fazer:** Horas para Agentforce core apenas
- **ADD-ONs separados:** Setup ORG, Marketing Cloud, KB externa

## Documentos Disponíveis

- Fluxo de atendimento v1.0 validado: `/Users/nfilho/claude/SEFIN_CE_Fluxo_v1_FINAL.png`
- Script DOT: `/Users/nfilho/claude/sefin_ce_fluxo_final.dot`
- Apresentação PPTX: `/Users/nfilho/claude/SEFIN_CE_Fluxo_Premissas_Perguntas.pptx`
- PDF NotebookLM: `/Users/nfilho/claude/DTP_SEFIN_CE_NotebookLM.pdf`

## Premissas Consolidadas (15)

| # | Premissa |
|---|---|
| P-01 | Todo encerramento = Pesquisa de satisfação → API de registro → Despedida. **Exceção: falha de API após retentativa encerra sem pesquisa** |
| P-02 | Sem transbordo humano no escopo — DHA dentro do horário sinaliza [TRANSBORDO — a definir] |
| P-03 | DHA fora do horário = informa indisponibilidade + encerra normalmente |
| P-04 | API de registro recebe: CPF/CNPJ, nome, serviço executado, resultado, nota de satisfação, justificativa |
| P-05 | Pesquisa de satisfação em todos os encerramentos, inclusive erros e abandonos. **Exceção: falha de API após retentativa** |
| P-06 | Notas ≤3 estrelas → agente coleta justificativa antes de encerrar |
| P-07 | Máximo 2 tentativas de digitação inválida em qualquer campo, depois encerra |
| P-08 | Usuário já identificado na sessão → pula identificação e vai direto ao Menu de Serviços |
| P-09 | ISS = informa link do site SEFIN-CE, sem identificação do cidadão |
| P-10 | Falha de API = 1 retentativa → se falhar novamente informa falha + contato registrado + alguém entrará em contato → AJUDO COM ALGO MAIS? |
| P-11 | CONFIRMA EMISSÃO DO DAM? = NÃO → AJUDO COM ALGO MAIS? (sem chamar API) |
| P-12 | Loop de emissão de DAM se repete para todas as inscrições selecionadas, uma a uma |
| P-13 | Sem limite de inscrições — agente apresenta todas retornadas pela API |
| P-14 | Régua proativa via Marketing Cloud Journey Builder (ADD-ON 2) |
| P-15 | "Preciso de ajuda" → coleta CPF/CNPJ + nome → consulta KB (ADD-ON 3) → se KB não responde → [TRANSBORDO — a definir] |

## Perguntas em Aberto para o Cliente (11)

| # | Pergunta |
|---|---|
| Q-A | O que é HSM no contexto do fluxo original? |
| Q-B | Qual será o mecanismo de transbordo humano? Como se dará tecnicamente sem Service Cloud/Digital Engagement? |
| Q-C | Quais são os parâmetros de entrada da API de registro de contato (incluindo nota e justificativa de satisfação)? |
| Q-D | O registro da pesquisa de satisfação é feito na mesma API de log ou em endpoint separado? |
| Q-E | Qual é a URL do site da SEFIN-CE para direcionamento no fluxo ISS? |
| Q-F | É possível disponibilizar uma base de conhecimento (KB)? Se sim, quem mantém e em qual formato? |
| Q-G | Há uma régua de comunicação proativa já definida? Se não, o cliente aceita adotar a régua sugerida via Marketing Cloud Journey Builder? |
| Q-H | Qual é a fonte de dados que alimenta os gatilhos da régua? Como o Marketing Cloud acessa esses dados? |
| Q-I | O cidadão pode solicitar opt-out das mensagens proativas? Se sim, como é registrado e respeitado? |
| Q-J | Qual é o horário comercial de atendimento humano? (dias da semana, início e fim) |
| Q-K | O limite de 7 inscrições no fluxo original é limitação do bot atual, da API ou regra de negócio? A nova solução pode receber todas sem limite? |

## Contexto Regulatório e Técnico (pré-carregado)

- **LGPD obrigatória** — dados de CPF/CNPJ são dados pessoais; débitos tributários podem ser considerados dados sensíveis dependendo do contexto (Art. 11 LGPD)
- **Licitação pública**: contrato via Lei 14.133/2021 (Nova Lei de Licitações)
- **Integrações legacy críticas**: APIs SEFIN-CE (EmitirDamUnico, ConsultaImovel)
- **Infraestrutura**: DATAPREV opera em ambiente híbrido (on-premise + cloud gov — OCI/GovCloud)
- **Usuários típicos**: cidadãos contribuintes (pessoas físicas e jurídicas)
- **Aprovações internas**: CTID DATAPREV (Comitê de TI e Dados), possível envolvimento ANPD se dados sensíveis
- **Idioma de entrega**: Português (PT-BR)
- **Moeda**: BRL (conversão USD → BRL via rate corrente)
- **Imposto padrão LATAM Brasil**: 75,35% sobre valor líquido (multiplicar por 0,9345 para obter valor com imposto)

## Próximos Passos

1. Executar DISCOVER para mapear requisitos completos
2. Validar perguntas Q-A a Q-K com cliente (Osvaldo / Augusto)
3. Estimar ESCOPO PRINCIPAL (Agentforce + WhatsApp)
4. Estimar ADD-ONs separadamente
5. Preparar ROM consolidado para DATAPREV
