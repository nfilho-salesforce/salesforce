# Architecture Reference — DATAPREV SEFIN-CE (Internal)

**Data:** 2026-07-03 (atualizado 2026-09-16 — E09 Transbordo Humano)  
**Projeto:** Service Cloud + Einstein Bot WhatsApp for SEFIN Fortaleza  
**Audience:** Internal PS team — technical reference grounding the solution brief

**Nota v2.0:** E09 (Transbordo Humano via Omni-Channel/Service Console) foi aprovada como 8ª épica em escopo em 2026-09-14. A arquitetura detalhada do transbordo (fluxo 4.7-B, roteamento Case/Messaging Session, 3 PAs) está em `outputs/artifacts/SEFIN_CE_Transcricao_Fluxo_v2_Transbordo.md`. Este documento foi atualizado nas seções §2.1 e §2.2 para remover a contradição que ainda listava Service Console/Omni-Channel Routing como fora de escopo.

---

## 1. Architecture Overview

### 1.1 Solution Landscape

```
┌─────────────────────────────────────────────────────────────────┐
│ CITIZEN (WhatsApp)                                              │
│   └─> Conversa via WhatsApp Business API                       │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ SALESFORCE SERVICE CLOUD (Hyperforce Brazil)                   │
│                                                                 │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ Einstein Bot (Enhanced Bot)                            │   │
│  │  • 4 Conversational Flows (IPTU, TMRSU, ISS, Cadastral)│  │
│  │  • NLU Intent Classification + Slot Filling           │   │
│  │  • Satisfaction Survey (1-5 stars + justificativa)    │   │
│  └─────────────┬──────────────────────────────────────────┘   │
│                │                                               │
│                ▼                                               │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ Flow Orchestration + Apex Callouts                     │   │
│  │  • Loop DAM Emission (multi-inscription)               │   │
│  │  • Validation Logic (CPF checksum, field format)       │   │
│  │  • Retry Logic (1x retry → fallback)                   │   │
│  └─────────────┬──────────────────────────────────────────┘   │
│                │                                               │
└────────────────┼───────────────────────────────────────────────┘
                 │
                 ▼ (REST + API Key via Named Credentials)
┌─────────────────────────────────────────────────────────────────┐
│ SEFIN APIs (IP direto Service Cloud → SEFIN)                   │
│                                                                 │
│  1. API ConsultaImovel      (lookup inscrições por CPF/CNPJ)   │
│  2. API EmitirDamUnico      (geração PDF DAM tributos)          │
│  3. API CRM SEFIN           (log satisfação — Q-01 spec)        │
│  4. API Dados Cadastrais    (update cadastral — Q-02 spec)      │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Key Architecture Decisions

| Decision | Rationale | Alternatives Rejected | Source |
|----------|-----------|----------------------|--------|
| Service Cloud + Einstein Bot (NOT Agentforce) | Discovery v2.0 revision — budget constraint < R$ 1.7M/ano MUTANTE; Agentforce AI credits pricing uncertain | Agentforce (ruled out due to pricing + Einstein Bot legacy sufficient for 4 simple flows) | [assumption: Enhanced Bot adequate for slot-filling patterns — validate Service Cloud Implementation Guide] |
| Flow Orchestration + Apex (NO MuleSoft) | P-17: cliente possui conectividade IP direta Service Cloud → SEFIN APIs; MuleSoft adds cost without clear integration complexity justification | MuleSoft Anypoint (overkill for 4 REST APIs + greenfield) | [assumption: Flow + Apex standard pattern for async at scale — Salesforce Integration Patterns doc] |
| Named Credentials (API Key) | Hide API keys from Bot Maintainer profile via FLS; secure credential storage | Custom Metadata (rejected — FLS exposure risk) | [assumption: Named Credentials + External Credential prevents API key exposure — Security Implementation Guide] |
| Hyperforce Brazil (data residency) | LGPD Art. 11 — CPF/CNPJ dados sensíveis requerem residência Brasil | US-East with contractual LGPD controls (uncertain legal interpretation) | [assumption: Hyperforce Brazil — validate DATAPREV geography approval P-22] |
| Standard TDE encryption (NOT Shield) | P-19 LGPD compliance; Shield adds ~30% license cost; TDE encrypts at-rest database files | Shield Platform Encryption (rejected unless legal requires field-level encryption) | [assumption: TDE sufficient LGPD Art. 11 — legal interpretation G0611] |
| Contact as primary citizen entity (NO Account/Lead) | Greenfield municipal gov context; citizens are individuals (PF) or businesses (PJ), not B2B accounts | Account + Contact model (overkill for simple citizen lookup) | [assumption: Contact sufficient — no Lead/Account for municipal gov] |
| Custom Bot Maintainer profile (NO Salesforce Standard) | Q-15: restrict to Einstein Bot + Conversation Review only (sem Flow Builder, sem API logs) | Standard Service Cloud User (rejected — over-permissioned) | [assumption: Bot Maintainer scoped permissions — Q-15 validation pending] |

---

## 2. Salesforce Products & Licensing

### 2.1 Service Cloud Configuration

**Edition:** Service Cloud Enterprise (minimum for Einstein Bot + API integrations)

**Features In-Scope:**
- Einstein Bot (Enhanced Bot) — 400.000 conversas/ano
- WhatsApp Channel via Messaging for Web/Mobile, com Digital Engagement license (G0901 resolvido — confirmada disponível para suportar o transbordo humano de E09)
- Flow Builder (unlimited Flows)
- Apex (unlimited classes/triggers)
- REST API callouts (10K/day limit — validate vs. 400K conversas/ano = ~1.1K/day avg)
- Service Console + Enhanced Omni-Channel Routing (E09 — Transbordo Humano; G0902 resolvido, cliente confirmou Enhanced Omni-Channel em 2026-09-14) — Case/Messaging Session como objeto de trabalho roteado para fila "Atendimento Tributário", 3 PAs em turno único (G0903 resolvido)

**Features Out-of-Scope:**
- Case Management fora do fluxo de transbordo (E09 já cobre o Case como objeto de trabalho do Service Console; qualquer uso de Case além disso permanece opcional — depende de Q-15 Bot Maintainer "revisão conversas")
- Knowledge (KB externa = ADD-ON 1 via Data Cloud, not native Knowledge)

### 2.2 Einstein Bot Conversations Licensing

**Volume:** 400.000 conversas/ano = ~33.333/mês

**Licensing Model:** Einstein Bot Conversations (pay-per-conversation, tiered — valor por tier a confirmar com o pricing Salesforce)  
- **Project volume:** ~33K conversas/mês (400K conversas/ano)

**Conversation Definition:** 1 conversation = 1 WhatsApp session from first user message to bot close OR 24h timeout (whichever comes first)

### 2.3 WhatsApp Channel Setup

**Provider:** Meta WhatsApp Business API (via Salesforce Messaging for Web/Mobile connector)

**Licensing:** Included in Service Cloud (no separate Digital Engagement Add-On required) [assumption: Service Cloud Messaging supports WhatsApp — validate licensing doc]

**Meta Costs (NOT Salesforce):**
- WhatsApp Business API account (Meta charges separate conversation fees)
- Tier pricing (Tier 1: 1K msgs/day, Tier 2: 10K msgs/day, Tier 3+: 100K+ msgs/day)
- **Project requires Tier 2+** (~13.5K msgs/day if ADD-ON 2 proactive enabled; ~1.1K/day if CORE only)

---

## 3. Data Model

### 3.1 Standard Objects

#### Contact (Primary Citizen Entity)

**Standard Fields Used:**
- `FirstName` / `LastName` (Nome completo)
- `Email`
- `Phone` / `MobilePhone` (WhatsApp number)
- `MailingStreet` / `MailingCity` / `MailingState` / `MailingPostalCode` (Endereço)

**Custom Fields Added:**
- `CPF_CNPJ__c` (Text 14, External ID, Unique) — CPF ou CNPJ (somente números)
- `Tipo_Pessoa__c` (Picklist: Física, Jurídica)
- `Data_Nascimento_Abertura__c` (Date) — Data nascimento (PF) ou abertura empresa (PJ)
- `Inscricao_Municipal__c` (Text 8) — Inscrição imóvel principal (se aplicável)
- `Digito_Inscricao__c` (Number 1)

**Field-Level Security:**
- `CPF_CNPJ__c` — Hidden from Bot Maintainer profile (Read-only for System Admin)
- Standard TDE encryption at-rest [assumption: TDE sufficient — Shield optional G0611]

**Data Retention:**
- Contact records: No automatic deletion (citizen master data persistent)
- Field History Tracking enabled: `CPF_CNPJ__c`, `Email`, `Phone`, `MailingStreet` (24-month retention)

#### Case (Optional — Conversation Log)

**Usage:** IF Q-15 Bot Maintainer "revisão conversas" requires Salesforce-native transcript storage

**Custom Fields:**
- `Bot_Conversation_ID__c` (Text 18, External ID) — Einstein Bot session ID
- `WhatsApp_Phone__c` (Phone) — Citizen WhatsApp number
- `Bot_Flow__c` (Picklist: IPTU, TMRSU, ISS, Alteração Cadastral)
- `Satisfaction_Rating__c` (Number 1) — 1-5 estrelas
- `Satisfaction_Justification__c` (Long Text 500) — Justificativa se ≤3

**Alternative:** Custom object `Chat_Transcript__c` se Case semantics não adequadas

### 3.2 Custom Objects (If Needed)

#### Chat_Transcript__c (Conditional)

**Purpose:** Store bot conversation history IF native Einstein Bot logging insufficient

**Fields:**
- `Name` (Auto-Number: CHAT-{0000})
- `Contact__c` (Lookup to Contact)
- `Conversation_Start__c` (DateTime)
- `Conversation_End__c` (DateTime)
- `Bot_Flow__c` (Picklist: IPTU, TMRSU, ISS, Alteração Cadastral)
- `Transcript__c` (Long Text Area 32K) — Full conversation JSON
- `Satisfaction_Rating__c` (Number 1)
- `Satisfaction_Justification__c` (Long Text 500)

**OWD:** Private (restrict to System Admin + Bot Maintainer profiles via Sharing Rules)

**Data Retention:** 90-day deletion via Apex batch job (scheduled weekly) [assumption: LGPD Art. 15 minimization]

---

## 4. Einstein Bot Design

### 4.1 Intent Classification (NLU)

**Intents:**
1. `IPTU_Intent` — Keywords: "IPTU", "imposto predial", "boleto IPTU", "pagar IPTU"
2. `TMRSU_Intent` — Keywords: "TMRSU", "taxa do lixo", "coleta de lixo", "boleto lixo"
3. `ISS_Intent` — Keywords: "ISS", "imposto sobre serviços", "nota fiscal", "serviços"
4. `Alteracao_Cadastral_Intent` — Keywords: "alterar cadastro", "atualizar endereço", "mudar telefone", "correção dados"
5. `Fallback_Intent` — Catch-all for unrecognized utterances (max 2 attempts → link Portal SEFIN)

**Training Data:** ~50-100 utterances per intent [assumption: SEFIN-CE provides sample citizen questions OR PS infers from spec — G0202 gap]

**NLU Confidence Threshold:** 70% (utterances <70% → Fallback)

### 4.2 Slot Filling Entities

**Entity: CPF_CNPJ**
- **Type:** Pattern (regex)
- **Regex:** `\d{11}|\d{14}` (11 digits PF ou 14 digits PJ)
- **Validation:** Apex callout `CPFValidator.isValid(String cpf)` — Dígitos Verificadores checksum
- **Error Message:** "CPF/CNPJ inválido. Digite novamente (11 dígitos PF ou 14 dígitos PJ, somente números)."
- **Max Retries:** 2 (P-05)

**Entity: Data_Nascimento_Abertura**
- **Type:** Date
- **Format:** DD/MM/YYYY
- **Validation:** Flow formula `TODAY() - Data > 18 anos` (PF) OU `TODAY() - Data > 0 anos` (PJ)
- **Error Message:** "Data inválida. Digite no formato DD/MM/YYYY."
- **Max Retries:** 2

**Entity: Inscricao_Municipal**
- **Type:** Number (8 digits)
- **Validation:** Flow callout `API ConsultaImovel` → 404 = inscrição não encontrada
- **Error Message:** "Inscrição municipal não encontrada. Verifique o número e tente novamente."

**Entity: Nome / Email / Telefone / Endereco**
- **Type:** Text (free-form)
- **Validation:** Minimal (email regex, phone 10-11 digits) [assumption: no ViaCEP validation — Q-03 gap]

### 4.3 Dialog Flow Structure

#### Flow 1: IPTU / TMRSU (Shared Logic)

```
1. Intent Recognition → IPTU_Intent OR TMRSU_Intent
2. Greeting: "Olá! Vou ajudar você com [IPTU/TMRSU]. Preciso de alguns dados."
3. Slot: CPF_CNPJ → Validation Apex callout
4. Slot: Data_Nascimento_Abertura
5. API Callout: ConsultaImovel (por-documento) → Returns List<Inscricao>
6. IF List.size() == 0:
     "Nenhuma inscrição encontrada para este CPF/CNPJ. Verifique seus dados."
     → Fallback (link Portal SEFIN)
7. IF List.size() > 0:
     Bot lista inscrições: "Encontrei [N] inscrições: [Inscrição 1], [Inscrição 2], ..."
     "Selecione as inscrições para emitir DAM (separadas por vírgula)."
8. LOOP (para cada inscrição selecionada):
     8a. "Confirma emissão DAM para Inscrição [X]? (Sim/Não)"
     8b. IF Sim:
          API Callout: EmitirDamUnico (tipoDebito = 10 IPTU OR 980 TMRSU)
          → Returns PDF_URL
          Send PDF via WhatsApp: "Seu DAM foi gerado! [PDF_URL]"
     8c. IF Não:
          "Ok, pulando Inscrição [X]."
9. END LOOP
10. Satisfaction Survey (1-5 stars)
11. IF Rating ≤3:
     "Lamento que a experiência não foi boa. Pode nos dizer o motivo?"
     Slot: Justificativa (Long Text 500)
12. API Callout: CRM SEFIN (log satisfação + justificativa + CPF/CNPJ + serviço)
13. Despedida: "Obrigado! Acesse o Portal SEFIN para mais serviços: [Q-06 URL]"
14. Close Session
```

#### Flow 2: ISS (Simplified — Link Only)

```
1. Intent Recognition → ISS_Intent
2. Greeting: "Olá! Para consulta ISS, acesse o portal SEFIN: [Q-E URL]"
3. Satisfaction Survey (1-5 stars)
4. API Callout: CRM SEFIN
5. Despedida
6. Close Session
```

**Note:** Q-04/Q-05 validation pending — se cliente aprovar, ISS flow expands to match IPTU/TMRSU (DAM emission via API EmitirDamUnico com tipoDebito = ISS code)

#### Flow 3: Alteração Cadastral

```
1. Intent Recognition → Alteracao_Cadastral_Intent
2. Greeting: "Olá! Vou ajudar você a atualizar seu cadastro."
3. Slot: CPF_CNPJ → Validation Apex
4. Slot: Data_Nascimento_Abertura
5. API Callout: API Dados Cadastrais (GET) OR ConsultaImovel (Q-02 pending)
   → Returns: Nome, Telefone, Email, Endereço atual
6. Bot apresenta dados atuais:
   "Dados cadastrais atuais:
    Nome: [Nome]
    Telefone: [Telefone]
    Email: [Email]
    Endereço: [Logradouro, Número, Complemento, Bairro, CEP, Cidade, Estado]"
7. "Confirma dados ou deseja alterar? (Confirmar/Alterar)"
8. IF Alterar:
     8a. For each campo editável (Nome, Telefone, Email, Endereço components):
          "Novo [Campo]?" → Slot
          Max 2 retries se formato inválido
     8b. Bot apresenta resumo: "Confirma alterações? [Lista mudanças] (Sim/Não)"
     8c. IF Sim:
          API Callout: API Dados Cadastrais (PUT/PATCH) → Update
          "Cadastro atualizado com sucesso!"
     8d. IF Não:
          "Ok, nenhuma alteração foi feita."
9. Satisfaction Survey
10. API Callout: CRM SEFIN
11. Despedida
12. Close Session
```

### 4.4 Session Management

**Session Timeout:** WhatsApp 24h messaging window (Meta policy)

**Session Persistence:**
- IF cidadão abandona conversa (não responde): session expires após 24h
- IF cidadão retorna >24h: bot inicia nova sessão (perde contexto)
- **Mitigation:** HSM (High-Structure Message) templates para session resume (ADD-ON 2 Marketing Cloud feature)

**Session State Storage:**
- Einstein Bot native session variables (in-memory during conversation)
- IF "revisão conversas" required: persist to Case OR Chat_Transcript__c (Q-15 validation)

---

## 5. Integration Architecture

### 5.1 Named Credentials Setup

**Named Credential 1: SEFIN_ConsultaImovel**
- **Endpoint:** `https://api.sefin.fortaleza.ce.gov.br/consulta-imovel` (example — validate with client)
- **Auth Type:** Custom (API Key in header)
- **Header:** `X-API-Key: {!$Credential.Password}`
- **External Credential:** `SEFIN_API_Credential` (API Key stored secure)
- **FLS:** Hidden from Bot Maintainer profile

**Named Credential 2: SEFIN_EmitirDamUnico**
- **Endpoint:** `https://api.sefin.fortaleza.ce.gov.br/emitir-dam`
- **Auth Type:** Custom (API Key)

**Named Credential 3: SEFIN_CRM**
- **Endpoint:** Pending Q-01
- **Auth Type:** Pending Q-01

**Named Credential 4: SEFIN_DadosCadastrais**
- **Endpoint:** Pending Q-02
- **Auth Type:** Pending Q-02

### 5.2 Apex Integration Classes

#### Class: SEFINAPIService.cls

```apex
public class SEFINAPIService {
    
    // API 1: ConsultaImovel (por-documento)
    @future(callout=true)
    public static void consultaImovelPorDocumento(String cpfcnpj, String tipoPessoa, Date dataNascAbertura, Integer exercicio) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:SEFIN_ConsultaImovel/por-documento');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        
        Map<String, Object> body = new Map<String, Object>{
            'tipo' => tipoPessoa,
            'documento' => cpfcnpj,
            'dataNascimentoAbertura' => dataNascAbertura.format(),
            'exercicio' => exercicio
        };
        req.setBody(JSON.serialize(body));
        
        Http http = new Http();
        HttpResponse res = http.send(req);
        
        if (res.getStatusCode() == 200) {
            // Parse response → List<Inscricao>
            List<InscricaoWrapper> inscricoes = (List<InscricaoWrapper>) JSON.deserialize(res.getBody(), List<InscricaoWrapper>.class);
            // Store in session variable OR return to Flow
        } else {
            // Retry logic: 1x retry after 2s delay
            // IF still fails: throw exception → Flow catches → fallback message
        }
    }
    
    // API 2: EmitirDamUnico
    @future(callout=true)
    public static void emitirDam(Integer tipoDebito, String tipoPessoa, String cpfcnpj, Integer inscricao, Integer digito, String tipoPagamento, Integer anoDebito) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:SEFIN_EmitirDamUnico');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setTimeout(10000); // 10s timeout
        
        Map<String, Object> body = new Map<String, Object>{
            'tipoDebito' => tipoDebito,
            'tipoPessoa' => tipoPessoa,
            'cpfcnpj' => cpfcnpj,
            'inscricao' => inscricao,
            'digito' => digito,
            'tipoPagamento' => tipoPagamento,
            'AnoDebito' => anoDebito
        };
        req.setBody(JSON.serialize(body));
        
        Http http = new Http();
        HttpResponse res = http.send(req);
        
        if (res.getStatusCode() == 200) {
            // Parse response → PDF_URL
            Map<String, Object> responseMap = (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
            String pdfUrl = (String) responseMap.get('pdfUrl');
            // Return to Flow → Send via WhatsApp
        } else {
            // Retry 1x → IF fails: throw exception
        }
    }
    
    // API 3: CRM SEFIN (log satisfação)
    @future(callout=true)
    public static void logSatisfacao(String cpfcnpj, String nome, Integer rating, String justificativa, String servicoExecutado) {
        // Fire-and-Forget (asynchronous — no retry if fails)
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:SEFIN_CRM'); // Q-01 pending
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setTimeout(5000); // 5s timeout
        
        Map<String, Object> body = new Map<String, Object>{
            'cpfcnpj' => cpfcnpj,
            'nome' => nome,
            'rating' => rating,
            'justificativa' => justificativa,
            'servico' => servicoExecutado,
            'timestamp' => Datetime.now().format('yyyy-MM-dd\'T\'HH:mm:ss\'Z\'')
        };
        req.setBody(JSON.serialize(body));
        
        Http http = new Http();
        HttpResponse res = http.send(req);
        
        // No retry — log error to Event Log Files if fails
        if (res.getStatusCode() != 200) {
            System.debug('SEFIN CRM API error: ' + res.getBody());
        }
    }
    
    // API 4: Dados Cadastrais (GET + PUT)
    // Q-02 pending — implement after spec received
}
```

#### Class: CPFValidator.cls

```apex
public class CPFValidator {
    public static Boolean isValid(String cpf) {
        // Remove non-numeric characters
        cpf = cpf.replaceAll('[^0-9]', '');
        
        if (cpf.length() != 11) return false;
        
        // Check if all digits are the same (invalid CPF)
        if (cpf == '00000000000' || cpf == '11111111111' || /* ... */ cpf == '99999999999') {
            return false;
        }
        
        // Calculate first verification digit
        Integer sum = 0;
        for (Integer i = 0; i < 9; i++) {
            sum += Integer.valueOf(cpf.substring(i, i+1)) * (10 - i);
        }
        Integer firstDigit = 11 - Math.mod(sum, 11);
        if (firstDigit >= 10) firstDigit = 0;
        
        // Check first digit
        if (firstDigit != Integer.valueOf(cpf.substring(9, 10))) {
            return false;
        }
        
        // Calculate second verification digit
        sum = 0;
        for (Integer i = 0; i < 10; i++) {
            sum += Integer.valueOf(cpf.substring(i, i+1)) * (11 - i);
        }
        Integer secondDigit = 11 - Math.mod(sum, 11);
        if (secondDigit >= 10) secondDigit = 0;
        
        // Check second digit
        if (secondDigit != Integer.valueOf(cpf.substring(10, 11))) {
            return false;
        }
        
        return true;
    }
}
```

### 5.3 Flow Orchestration

**Flow: Einstein_Bot_IPTU_TMRSU**
- **Trigger:** Invoked by Einstein Bot dialog
- **Input Variables:** `cpfcnpj`, `tipoPessoa`, `dataNascAbertura`, `tipoDebito` (10=IPTU, 980=TMRSU)
- **Logic:**
  1. Decision: Validate CPF via `CPFValidator.isValid(cpfcnpj)`
  2. IF invalid: Exit with error message
  3. IF valid: Action `SEFINAPIService.consultaImovelPorDocumento()`
  4. Wait 2s (async callout completion)
  5. Loop Collection: For each inscricao returned
       5a. Prompt user confirmation
       5b. IF confirmed: Action `SEFINAPIService.emitirDam()`
       5c. Wait 5s
       5d. Send PDF via WhatsApp (Einstein Bot action)
  6. Exit to Satisfaction Survey

**Flow: Einstein_Bot_Satisfaction_Survey**
- **Trigger:** Invoked by all bot dialogs (IPTU, TMRSU, ISS, Cadastral)
- **Input Variables:** `cpfcnpj`, `nome`, `servicoExecutado`
- **Logic:**
  1. Screen: Display 1-5 star rating buttons (OR Einstein Bot survey widget if available)
  2. Decision: IF rating ≤3 → Prompt justificativa (Long Text)
  3. Action: `SEFINAPIService.logSatisfacao(cpfcnpj, nome, rating, justificativa, servicoExecutado)`
  4. Screen: Despedida message + link Portal SEFIN (Q-06 URL)
  5. Exit

---

## 6. UX Research & Accessibility

### 6.1 Persona Research Plan

**Method:** Remote interviews via Zoom (no travel to Fortaleza)

**Sample:**
- **PF (Pessoas Físicas):** n=6 interviews
  - 2× baixa renda (IPTU isento ou valor <R$ 500)
  - 2× média renda (IPTU R$ 500-2.000)
  - 2× alta renda (IPTU >R$ 2.000)
- **PJ (Pessoas Jurídicas):** n=6 interviews
  - 2× MEI (Microempreendedor Individual)
  - 2× Pequena Empresa (1-49 funcionários)
  - 2× Média Empresa (50-249 funcionários)

**Screener Questions:**
1. Você é contribuinte de IPTU/TMRSU/ISS em Fortaleza?
2. Com que frequência você acessa serviços digitais da prefeitura?
3. Já usou WhatsApp para atendimento de empresas/governo?
4. Qual seu nível de conforto com tecnologia? (1-5 escala)

**Interview Script (45 min):**
- Apresentação (5 min)
- Contexto contribuinte (10 min) — histórico pagamento tributos, dores atuais
- Expectativas bot WhatsApp (15 min) — o que funcionaria bem, o que seria frustrante
- Demo protótipo (10 min) — mostrar fluxo IPTU mockup, coletar feedback
- Encerramento (5 min) — agradecimento + LGPD consent confirmation

**Deliverable:** 2 persona docs (PDF, PT-BR) — 1 PF + 1 PJ, cada com:
- Nome fictício + foto stock
- Dados demográficos (idade, renda, profissão)
- Goals & Frustrations
- Technology Comfort Level
- Quote representativa

### 6.2 Usability Testing Plan

**Method:** Remote moderated testing via Zoom + working WhatsApp bot (pre-production)

**Sample:** 3 fluxos × 5 usuários = 15 sessões
- **IPTU Flow:** 5 usuários (3 PF + 2 PJ)
- **TMRSU Flow:** 5 usuários (3 PF + 2 PJ)
- **Alteração Cadastral Flow:** 5 usuários (4 PF + 1 PJ)

**Test Script (30 min):**
1. Pré-teste (5 min) — contexto, consentimento LGPD
2. Tarefa 1: "Emita um DAM de IPTU para a inscrição XXX" (10 min)
3. Tarefa 2: "Atualize seu endereço cadastral" (10 min)
4. Pós-teste (5 min) — SUS (System Usability Scale) questionnaire + open feedback

**Success Metrics:**
- Task completion rate >80%
- Time on task <5 min per flow
- SUS score >70 (acceptable usability)
- Error rate <15% (invalid input / retry scenarios)

**Deliverable:** Usability findings report (~5-10 pages, PT-BR) com:
- Executive summary
- Task completion rates + time on task
- SUS scores
- Top 5 usability issues (severity: critical/high/medium/low)
- Recommendations for improvement

### 6.3 Accessibility Analysis

**Method:** Expert review (heuristic evaluation) — WCAG 2.1 AA adapted for conversational UI

**WCAG 2.1 AA Criteria Adapted:**
- **1.1.1 Non-text Content:** WhatsApp bot uses text-only (N/A for images/audio)
- **1.3.1 Info and Relationships:** Conversational structure clear (sequential Q&A)
- **1.4.3 Contrast:** N/A (WhatsApp client controls visual contrast)
- **2.1.1 Keyboard:** N/A (WhatsApp client controls input method)
- **2.4.7 Focus Visible:** N/A (conversational UI has no visual focus indicator)
- **3.1.1 Language of Page:** PT-BR declared in bot welcome message
- **3.2.1 On Focus:** N/A
- **3.3.1 Error Identification:** Bot provides clear error messages (e.g., "CPF inválido")
- **3.3.2 Labels or Instructions:** Bot provides instructions before each slot (e.g., "Digite seu CPF")
- **4.1.2 Name, Role, Value:** WhatsApp screen reader support (iOS VoiceOver, Android TalkBack)

**Additional Conversational UI Checks:**
- Plain language (Flesch Reading Ease >60 for PT-BR)
- Minimal cognitive load (1 question at a time)
- Forgiving input (accepts "sim"/"s"/"1" for confirmation)
- Timeout warnings (30s before session timeout)

**Deliverable:** Accessibility report (~10-15 pages, PT-BR) com:
- Executive summary
- WCAG 2.1 AA adapted criteria checklist
- Screen reader testing notes (VoiceOver + TalkBack compatibility)
- Plain language analysis (reading level)
- Top 5 accessibility recommendations

---

## 7. Security & Compliance

### 7.1 LGPD Art. 11 Implementation

**Data Classification:**
- **Sensitive Data:** CPF/CNPJ (Art. 11 — dados pessoais sensíveis)
- **Personal Data:** Nome, telefone, email, endereço, data nascimento/abertura

**Technical Controls:**
- **Encryption at Rest:** Standard TDE (Transparent Data Encryption) — encrypts database files [assumption: TDE sufficient — Shield optional G0611]
- **Encryption in Transit:** TLS 1.2+ for all API callouts [assumption: SEFIN APIs support TLS 1.2+]
- **Data Residency:** Hyperforce Brazil (data stored in São Paulo data center) [assumption: Hyperforce Brazil — validate DATAPREV approval]
- **Audit Trail:** Field History Tracking (CPF/CNPJ fields) + Event Monitoring (API callout events, login events)
- **Data Retention:** 90-day bot logs, 12-month satisfaction data → Apex batch job deletion (scheduled weekly)

**Organizational Controls:**
- **Data Controller:** SEFIN Fortaleza (public sector entity)
- **Data Processor:** Salesforce (cloud provider) + DATAPREV (AMS sustentação)
- **DPO (Data Protection Officer):** SEFIN-CE DPO (to be confirmed Q-17)
- **LGPD Consent:** Explicit consent for satisfaction survey data collection (opt-in before survey)

### 7.2 User Profiles & Permissions

#### System Administrator Profile (3 users)

**Clone of:** System Administrator (standard)

**Permissions:** Full ORG access (all objects, all fields, all setup)

**Login Restrictions:**
- IP Ranges: DATAPREV VPN/office IPs (to be provided)
- Login Hours: 24/7 (no restriction)
- MFA: Recommended (not mandatory)

#### Bot Maintainer Profile (7 users — Custom)

**Cloned From:** Minimum Access - Salesforce (standard)

**Object Permissions:**
- **Einstein Bot:** Read, Create, Edit (restricted to Bot objects only)
- **Contact:** Read-only (no Edit/Delete)
- **Case OR Chat_Transcript__c:** Read-only (if "revisão conversas" in scope Q-15)

**System Permissions:**
- View Setup: YES (restricted to Einstein Bot Setup only)
- Customize Application: YES (restricted to Bot dialogs only)
- API Enabled: NO
- View All Data: NO
- Modify All Data: NO

**Field-Level Security:**
- `Contact.CPF_CNPJ__c`: Read-only (no Edit)
- Named Credentials: Hidden (no View/Edit)

**Login Restrictions:**
- IP Ranges: SEFIN-CE office IPs (to be provided)
- Login Hours: Business hours only (8am-6pm Brasília UTC-3)
- MFA: Recommended

**Rationale:** Q-15 validation pending — Bot Maintainer should only access Einstein Bot configuration + review conversations, without Flow Builder, API logs, or Named Credentials exposure [assumption: prevents privilege escalation + API key exposure]

### 7.3 Named Credentials Security

**FLS (Field-Level Security):**
- All Named Credentials objects hidden from Bot Maintainer profile
- External Credentials (`Password` field) encrypted at rest (standard Salesforce encryption)

**Rotation Policy:**
- API Keys rotated every 90 days (DATAPREV AMS responsibility)
- Rotation procedure documented in Admin Guide

---

## 8. Technical Risks & Mitigations

| Risk ID | Risk | Probability | Impact | Mitigation | Owner |
|---------|------|-------------|--------|------------|-------|
| **G0704** | Einstein Bot (legacy) does NOT natively support Data Cloud vector search (ADD-ON 1 KB Vectorization blocked) | HIGH | CRITICAL | Validate Einstein Bot + Data Cloud capability. IF native integration unavailable: (1) Upgrade to Agentforce OR (2) Custom Apex integration OR (3) Descope ADD-ON 1 | PS + DATAPREV |
| **G0301/G0302** | API CRM SEFIN + Dados Cadastrais specs pendente (E03/E04 integration blocked) | MEDIUM | HIGH | Obtain full API specs (endpoint, payload, auth) before kick-off. IF delayed: design mock/stub APIs for parallel dev + UAT | SEFIN-CE + PS |
| **G0805** | Data Cloud zero-copy feasibility unvalidated (ADD-ON 2 may require full batch ingestion vs. zero-copy) | MEDIUM | HIGH | Validate SEFIN source system supports streaming/Direct Connect. IF batch-only: pivot to SFTP batch ingestion (impacts data freshness) | DATAPREV + PS |
| **G0202** | NLU training data ownership undefined (poor bot NLU accuracy if corpus insufficient) | MEDIUM | MEDIUM | Confirm SEFIN-CE provides sample citizen questions (50-100/intent). IF not available: PS infers from spec + 2-week training data collection buffer | SEFIN-CE + PS |
| **G0507** | WCAG 2.1 AA não aplicável a conversational UI (accessibility deliverable may miss client expectations) | LOW | MEDIUM | Propose adapted framework (W3C Conversational Accessibility Guidelines draft) + screen reader testing (VoiceOver + TalkBack) | PS |
| **G0208** | WhatsApp 24h messaging window vs. session persistence >24h (citizen loses progress if abandons mid-flow) | LOW | MEDIUM | Design HSM templates for session resume (requires Meta approval 1-3 weeks). Fallback: inform citizen "session expired, start new conversation" | PS + SEFIN-CE |
| **G0103** | Meta WhatsApp Business approval timeline 2-8 weeks (critical path blocker) | MEDIUM | HIGH | Start Meta approval process ASAP (pre-kick-off if possible). Parallel track: test bot with personal WhatsApp number (not recommended for LGPD but unblocks dev) | SEFIN-CE + PS |
| **G0611** | TDE vs. Shield legal interpretation (LGPD Art. 11 field-level encryption requirement unclear) | LOW | HIGH | Obtain legal opinion from SEFIN-CE DPO. IF Shield required: add ~30% license cost to budget | SEFIN-CE Legal + DATAPREV |

---

## 9. Open Architecture Questions

**To be resolved in Phase 0 (2-3 weeks):**

1. **Q-01:** API CRM SEFIN full spec (endpoint, payload, headers, auth)?
2. **Q-02:** API Dados Cadastrais full spec (endpoint, payload, headers, auth)?
3. **Q-04/Q-05:** ISS flow — link site (current) OR DAM emission via API (upgrade)?
4. **Q-06:** Portal SEFIN URL for despedida message?
5. **Q-15:** Bot Maintainer profile — permissions beyond Einstein Bot + conversation review?
6. **G0704:** Einstein Bot + Data Cloud native integration capability validated?
7. **G0705:** Data Cloud licensing edition (Starter/Growth/Advanced)?
8. **G0805:** SEFIN source system supports streaming/Direct Connect for zero-copy?
9. **P-22:** Data residency — Hyperforce Brazil OR US-East with contractual LGPD controls?
10. **G0611:** LGPD Art. 11 legal interpretation — TDE sufficient OR Shield Platform Encryption required?

---

**Documento gerado automaticamente via Scopezilla — Salesforce PS LATAM (Internal Reference)**
