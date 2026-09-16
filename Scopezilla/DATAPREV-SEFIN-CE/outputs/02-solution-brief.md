# Solution Brief — DATAPREV SEFIN-CE WhatsApp Bot

**Data:** 2026-07-03  
**Cliente:** SEFIN Fortaleza (via DATAPREV)  
**Projeto:** Substituição bot MUTANTE por Service Cloud + Einstein Bot

---

## Executive Summary

Solução Salesforce Service Cloud + Einstein Bot para atendimento automatizado de tributos municipais via WhatsApp, substituindo fornecedor atual MUTANTE (R$ 1,7M/ano). Projeto greenfield (nova ORG) com 400.000 conversas/ano inbound, 4 fluxos conversacionais (IPTU, TMRSU, ISS, Alteração Cadastral), integração com 4 APIs SEFIN via Flow + Apex, e pesquisa satisfação obrigatória. Escopo CORE inclui UX Research (personas, usabilidade, WCAG). DATAPREV assume sustentação AMS pós-implantação.

**Budget Target:** < R$ 1,7M/ano (valor contrato MUTANTE)  
**Licenciamento Estimado:** R$ 1,2–1,5M/ano (Service Cloud + Einstein Bot Conversations)

---

## Solution Architecture by Epic

### E01 — Salesforce ORG Foundation & WhatsApp Channel

**Business Context:**  
Setup completo nova ORG Service Cloud from scratch + Einstein Bot licensing + WhatsApp Channel (sem Digital Engagement). Inclui domínio personalizado, data residency Brasil (LGPD), aprovação Meta WhatsApp Business.

**Technical Approach:**  
- Nova ORG Hyperforce Brasil para LGPD Art. 11 compliance (dados CPF/CNPJ sensíveis) [assumption: Hyperforce Brazil — validate DATAPREV geography approval]
- Service Cloud AS-IS (Einstein Bot + WhatsApp — sem Case Management, sem Service Console) [assumption: Service Cloud Messaging for WhatsApp supports bot deflection without Digital Engagement Add-On]
- 10 usuários: 3 System Administrator + 7 Bot Maintainer (perfil customizado) [assumption: Bot Maintainer restricts to Einstein Bot Setup + Conversation Review only]
- WhatsApp Business Account via Meta/Facebook — Tier 2+ requerido (10K msgs/dia mínimo) [assumption: upgrade from Tier 1 if current account exists]
- Domínio personalizado SEFIN (a definir) + SSL certificate [assumption: domain provisioning 1-2 weeks]

**Deliverables:**
- ORG provisionada e configurada (Hyperforce Brazil)
- WhatsApp Channel ativo e aprovado Meta
- 2 perfis usuários configurados (System Admin + Bot Maintainer)
- Named Credentials para 4 APIs SEFIN (API Key hidden from Bot Maintainer)

**Risks & Dependencies:**
- Meta WhatsApp Business approval timeline 2-8 semanas (critical path)
- Domínio personalizado DNS propagation 24-48h
- Data residency Hyperforce Brazil vs. US-East contractual (Q-22 validation)

---

### E02 — Einstein Bot Conversational Flows

**Business Context:**  
Configuração Einstein Bot com 4 fluxos conversacionais via linguagem natural (sem botões): (1) IPTU, (2) TMRSU, (3) ISS (link site — Q-04/Q-05 validação), (4) Alteração Cadastral. Menu inicial NLU, máx 2 tentativas digitação inválida, sessão persistente.

**Technical Approach:**  
- **NLU Intent Classification** — 4 intents principais (IPTU, TMRSU, ISS, Alteração Cadastral) + fallback intent [assumption: NLU training data provided by SEFIN-CE or PS infers from spec]
- **Slot Filling Entities** — CPF/CNPJ (formato XXX.XXX.XXX-XX), data nascimento/abertura, nome, telefone, email, endereço [assumption: Einstein Bot Entity extraction supports CPF regex]
- **Validation Logic** — CPF checksum (Dígitos Verificadores) via Apex antes de API callout [assumption: reduces API 400 errors]
- **Loop Emissão DAM (P-29)** — Para cada inscrição selecionada → confirma → API EmitirDamUnico → PDF via WhatsApp [assumption: WhatsApp file upload <16MB]
- **Session Timeout** — WhatsApp 24h messaging window + HSM templates para resume (se necessário) [assumption: HSM design + Meta approval in scope]

**Deliverables:**
- 4 Einstein Bot dialogs configurados (IPTU, TMRSU, ISS, Alteração Cadastral)
- NLU model treinado com ~50-100 utterances por intent
- Slot filling + validation Flows configurados
- Fallback handling (máx 2 tentativas → link Portal SEFIN)

**Risks & Dependencies:**
- G0202 — NLU training data ownership (SEFIN-CE fornece ou PS infere?)
- G0201 — ISS flow ambiguity (link site vs. DAM emission — Q-04/Q-05 validação)
- G0208 — WhatsApp 24h window vs. session persistence >24h (HSM required)

---

### E03 — API Integration Layer

**Business Context:**  
Integração 4 APIs SEFIN via Flow Orchestration + Apex (sem MuleSoft): (1) EmitirDamUnico (DAM PDF), (2) ConsultaImovel (inscrições por CPF/CNPJ), (3) API CRM SEFIN (log satisfação — Q-01 spec pendente), (4) API Dados Cadastrais (update cadastral — Q-02 spec pendente). Protocolo REST + API Key, retentativa 1x em caso falha.

**Technical Approach:**  
- **Integration Pattern:** Flow Orchestration (business logic) + Apex @future/@queueable (REST callouts) [assumption: Flow for orchestration + Apex for async at scale — standard Salesforce pattern]
- **Authentication:** Named Credentials (API Key hidden from Bot Maintainer profile via FLS) [assumption: Named Credentials + External Credential prevents API key exposure]
- **API ConsultaImovel** — Synchronous callout from Einstein Bot dialog (latency <2s target) [assumption: API response time <2s for conversational UX]
- **API EmitirDamUnico** — Synchronous callout (PDF generation <5s; fallback if timeout) [assumption: timeout 10s + retry 1x]
- **API CRM SEFIN** — Asynchronous Fire-and-Forget callout (satisfaction logging) [assumption: async acceptable for non-critical log]
- **API Dados Cadastrais** — Synchronous callout (cadastral update <3s) [assumption: synchronous for user confirmation]
- **Connectivity:** IP direto Service Cloud → APIs SEFIN (P-17 cliente possui) [assumption: TLS 1.2+ supported by SEFIN APIs]
- **Error Handling:** 1 retentativa → falha informa "tente novamente mais tarde" → encerra (P-16) [assumption: retry delay 1-2s]

**Deliverables:**
- 4 Named Credentials configurados (API Key secure storage)
- Apex classes para 4 REST callouts (EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais)
- Flow Orchestration para business logic (loop DAM, validation, retry)
- Error logging + monitoring (Event Log Files)

**Risks & Dependencies:**
- **G0301/G0302 BLOCKER** — API CRM SEFIN + Dados Cadastrais specs pendentes (obtain before kick-off)
- G0303 — Conectividade IP validation (ping/curl test Salesforce → SEFIN APIs pré-prod)
- G0306 — API error logging strategy (Event Monitoring license required?)

---

### E04 — Feedback & Satisfaction Tracking

**Business Context:**  
Pesquisa satisfação obrigatória ao final de todos fluxos bot (IPTU, TMRSU, ISS, Cadastral). Coleta nota 1-5 estrelas + justificativa se ≤3. Log via API CRM SEFIN (Q-01). Despedida com link Portal SEFIN (Q-06 URL pendente).

**Technical Approach:**  
- **Satisfaction Survey Widget** — Einstein Bot survey component (1-5 stars) OU custom Flow com quick-reply buttons se widget indisponível [assumption: Einstein Bot survey widget exists — G0414 capability gap validation needed]
- **Justificativa Free-Text** — Max 500 chars (sanitização profanity filter + special chars) [assumption: API CRM SEFIN accepts 500 chars max]
- **API CRM SEFIN Callout** — Asynchronous Fire-and-Forget (log satisfação + justificativa + CPF/CNPJ + serviço executado) [assumption: payload schema pending Q-01]
- **Despedida Message** — Template com link Portal SEFIN (Q-06 URL) [assumption: generic farewell vs. contextual (success vs. failure)]
- **LGPD Consent** — Disclosure antes de survey: "Sua avaliação será registrada junto ao CPF para melhoria do serviço. Concorda?" [assumption: explicit opt-in required LGPD Art. 7]

**Deliverables:**
- Satisfaction survey Flow configurado (1-5 stars + justificativa condicional)
- API CRM SEFIN integration (Apex callout + Named Credential)
- Despedida message templates (success, failure, timeout scenarios)
- LGPD consent disclosure message

**Risks & Dependencies:**
- **G0401 BLOCKER** — API CRM SEFIN spec pendente (Q-01 — obtain endpoint, payload, auth)
- G0403 — Satisfaction UI format ambiguity (stars vs. emoji vs. buttons)
- G0410 — LGPD consent for satisfaction data (explicit opt-in before survey)

---

### E05 — UX Research & Accessibility

**Business Context:**  
UX Research incluída no escopo PS (P-31): (1) Personas cidadãos contribuintes PF/PJ Fortaleza, (2) Testes usabilidade bot WhatsApp (fluxos IPTU/TMRSU/Cadastral), (3) Análise acessibilidade WCAG 2.1 AA para interface conversacional.

**Technical Approach:**  
- **Personas Research** — n=6 PF interviews + n=6 PJ interviews = 12 total (remote via Zoom) [assumption: remote research — no travel to Fortaleza]
- **Deliverable:** 2 persona docs (1 PF + 1 PJ) PDF format com stock photos [assumption: 4-6h effort per persona]
- **Usability Testing** — 3 fluxos (IPTU, TMRSU, Cadastral) × 5 usuários = 15 sessões [assumption: n=5 per flow industry standard]
- **Deliverable:** Test scripts PT-BR (self-guided for DATAPREV execution) + findings report [assumption: DATAPREV executes testing with PS scripts]
- **Accessibility Analysis** — Expert review (heuristic evaluation) WCAG 2.1 AA adapted for conversational UI [assumption: expert review vs. user testing with PcD — G0509]
- **Deliverable:** Accessibility report (~10-15 pages) with remediation recommendations [assumption: report-only — remediation out of scope]

**Deliverables:**
- 2 persona documents (PDF, PT-BR)
- Usability test scripts (PT-BR, self-guided)
- Usability findings report (~5-10 pages)
- Accessibility analysis report (~10-15 pages, WCAG 2.1 AA adapted)

**Risks & Dependencies:**
- G0501 — UX research ownership (PS conducts vs. DATAPREV conducts with PS guidance?)
- G0507 — WCAG 2.1 AA não aplicável a conversational UI (W3C Conversational Accessibility Guidelines needed)
- G0514 — LGPD consent form for persona interviews + usability testing

---

### E06 — Security Model & User Profiles

**Business Context:**  
Configuração segurança LGPD Art. 11 (dados CPF/CNPJ sensíveis) + 2 perfis usuários: (1) 3 System Administrator (gestão completa ORG), (2) 7 Bot Maintainer customizado (apenas Einstein Bot + revisão conversas — Q-15 validação permissões). Data residency Brasil, audit trail ativo, encryption at rest/in transit.

**Technical Approach:**  
- **LGPD Art. 11 Compliance** — CPF/CNPJ as sensitive data [assumption: standard TDE encryption sufficient vs. Shield Platform Encryption — G0611 legal interpretation]
- **Data Residency:** Hyperforce Brazil (ou US-East contractual com LGPD controls) [assumption: Hyperforce Brazil — validate DATAPREV approval]
- **Encryption at Rest:** Standard TDE (Transparent Data Encryption) [assumption: TDE sufficient — Shield add-on ~30% license uplift if required]
- **Encryption in Transit:** TLS 1.2+ for all API callouts [assumption: SEFIN APIs support TLS 1.2+ — G0606 validation]
- **Audit Trail:** Field History Tracking (CPF/CNPJ fields) + Event Monitoring (API callouts, login events) [assumption: Event Monitoring add-on required — G0604]
- **Bot Maintainer Profile:** Custom profile restricting to Einstein Bot Setup + Conversation Review (sem Flow Builder, sem API logs) [assumption: Q-15 validation pending — G0602]
- **MFA:** Optional (not specified) [assumption: MFA recommended LGPD Art. 46 — G0608]
- **Data Retention Policy:** 90-day bot logs, 12-month satisfaction data (deletion automation via Apex batch) [assumption: LGPD Art. 15 retention minimization — G0610]

**Deliverables:**
- 2 custom profiles configured (System Admin clone + Bot Maintainer)
- Field History Tracking enabled (CPF/CNPJ, satisfaction fields)
- Event Monitoring configured (API callout events, login events)
- Data retention Apex batch job (scheduled weekly deletion)
- Security documentation (LGPD compliance memo)

**Risks & Dependencies:**
- G0602 — Bot Maintainer profile scope undefined (Q-15 validation pending)
- G0611 — TDE vs. Shield for LGPD Art. 11 (legal interpretation needed)
- G0604 — Event Monitoring add-on license, custo a confirmar com o pricing Salesforce

---

## Optional ADD-ONs (Separate Estimate)

### E07 — Knowledge Base Vectorization (ADD-ON 1)

**Business Context:**  
Ingestão base conhecimento externa Salesforce → vetorização Data Cloud → Einstein Bot responde dúvidas via KB (substitui redirecionamento site). Volume KB, formato e fonte a confirmar com cliente (Q-F v1.0).

**Technical Approach:**  
**⚠️ BLOCKER G0704:** Einstein Bot (legacy Service Cloud) does NOT natively support Data Cloud vector search. Alternatives:
1. Upgrade to Agentforce (different licensing model + AI credits)
2. Custom Apex integration: Query Data Cloud vector API + inject results into Einstein Bot dialog
3. Use Einstein Search for Service (separate license)

**Risks & Dependencies:**
- **G0704 BLOCKER** — Einstein Bot + Data Cloud capability not validated
- **G0705 BLOCKER** — Data Cloud licensing edition undefined (Starter/Growth/Advanced?)
- G0713 — Q-F v1.0 discovery doc missing (KB volume/format specs)

**Recommendation:** Validate Einstein Bot + Data Cloud integration capability before scoping. If native integration unavailable, recommend Agentforce upgrade OR descope ADD-ON 1.

---

### E08 — Proactive Outreach Journey (ADD-ON 2)

**Business Context:**  
Setup Marketing Cloud + 1 jornada comunicação proativa WhatsApp (ex: cidadãos IPTU vencido). 1 fonte dados zero-copy Data Cloud, 1 segmentação (sem Identity Resolution), 4,86M msgs/ano (~13.500/dia). Opt-out cidadão (Q-08).

**Technical Approach:**  
- **Marketing Cloud Engagement** (Core/Pro edition) + Journey Builder [assumption: Journey Builder included — G0801 edition validation]
- **Data Cloud Zero-Copy** integration via Direct Connect [assumption: SEFIN source supports streaming — G0805 blocker if batch-only]
- **Journey Design:** 1 jornada proativa (ex: IPTU vencido D-15, D-5, D+1 reminders) [assumption: triggers/régua pending Q-G/Q-H]
- **HSM Templates:** Meta approval 1-3 semanas (proactive messaging templates) [assumption: template design + submission in scope]
- **Opt-Out Mechanism:** Reply STOP + Data Cloud attribute update [assumption: Q-08 validation pending]
- **LGPD Compliance:** Tax payment reminders = legitimate public interest (não requer consent explícito?) [assumption: legal validation G0809]

**Deliverables:**
- Marketing Cloud account provisioned + WhatsApp connector configured
- Data Cloud zero-copy integration (Direct Connect to SEFIN source)
- 1 Journey Builder journey configured (IPTU vencido régua)
- 3-5 HSM templates approved by Meta
- Opt-out handling (STOP keyword + Data Cloud update)

**Risks & Dependencies:**
- **G0805 BLOCKER** — Data Cloud zero-copy feasibility (validate SEFIN source supports streaming)
- G0801 — Marketing Cloud edition undefined (Core/Pro/Premium?)
- G0809 — LGPD consent for proactive marketing (legal validation Art. 7, IX)
- G0808 — WhatsApp Business Account Tier 2+ required (13.5K msgs/day)

---

### E09 — Transbordo Humano via Omni-Channel/Service Console (ADD-ON 3 — pesquisa/expansão de escopo)

**Business Context:**  
Adiciona escalonamento humano ao bot WhatsApp hoje bot-only (P-02: "sem transbordo humano — bot encerra automaticamente apresentando link Portal SEFIN"). Levantamento iniciado 2026-09-14 a título de pesquisa de expansão de escopo, formalizado como epic após validação com o cliente de dois pontos-chave: Digital Engagement license já disponível/aprovada, e headcount de 3 PAs (Posições de Atendimento) em turno único.

**Technical Approach:**
- **Digital Engagement license** — pré-requisito confirmado disponível (G0901 resolvido). Messaging (canal WhatsApp) exige Digital Engagement para ser roteável a um agente humano via Omni-Channel; Case routing por si só funciona com Service Cloud puro, mas a mensageria não `[KB: service_cloud_3-27-2026.md:1257-1259]`.
- **Enhanced Omni-Channel** (não Standard) — Standard Omni-Channel atinge End of Life no release Summer '26 `[KB: service_cloud_3-27-2026.md:13560-13591]`. Presence Statuses, Routing Configuration (fila/skill-based), Service Channel para Messaging.
- **Case/Messaging Session como objeto de trabalho roteado** `[extends: padrão KB de case routing + messaging, aplicado ao handoff originado pelo bot]`.
- **Ponto de transferência nos 4 fluxos do bot (delta E02)** — IPTU, TMRSU, ISS, Cadastral passam a ter um branch de "transferir para atendente" (além do fluxo de KB/P-15), levando CPF/CNPJ + serviço solicitado + transcript para o Case `[extends: pontos de decisão já existentes no E02, agora roteando para humano em vez de encerrar]`.
- **Service Console app para as 3 PAs** — widget Omni-Channel + visão da conversa de Messaging + painel de contexto SEFIN (dados já obtidos via ConsultaImovel/EmitirDamUnico na sessão do bot, delta E03) `[assumption: padrão-base de configuração de Service Console; validar fluxo de trabalho com operação SEFIN]`.
- **Business Hours real (G0904)** — DHA (P-02/P-03) passa de mensagem informativa para objeto Business Hours de fato, amarrado à disponibilidade de roteamento `[extends: premissa P-03 já validada]`.
- **Novo profile "Agente Humano SEFIN" (delta E06)** — licença de usuário Omni-Channel, acesso a Case/Messaging escopado à fila, LGPD-aware para CPF/CNPJ `[assumption: padrão Salesforce de profile de agente Omni-Channel]`.
- **Pesquisa de satisfação no fechamento humano (delta E04)** — mesmo fluxo de P-01/P-05, agora também disparado no Case fechado pelo agente humano `[extends: premissas P-01/P-05 já validadas]`.
- **Continuidade de conversa no WhatsApp** — thread único preservado do bot para o humano `[assumption: comportamento padrão do Digital Engagement Messaging; validar na configuração já aprovada do canal WhatsApp bot-only]`.

**Deliverables:**
- Digital Engagement + Enhanced Omni-Channel provisionados (Presence Statuses, Routing Configuration, Service Channel)
- Service Console app configurado para as 3 PAs (turno único)
- Ponto de transferência adicionado aos 4 fluxos do bot + fluxo de KB (E02)
- Case/Messaging Session com handoff de contexto (CPF/CNPJ, serviço, transcript)
- Business Hours real configurado (pendente G0904 — horário exato do DHA)
- Profile "Agente Humano SEFIN" + permission set (delta E06)
- Pesquisa de satisfação estendida ao fechamento humano (delta E04)

**Risks & Dependencies:**
- G0902 — Confirmar edição Enhanced Omni-Channel (Standard atinge EOL Summer '26)
- G0904 — Horário exato do DHA (dias/hora) para Business Hours real (reaproveita Q-J)
- ~~G0901~~ — Digital Engagement license: **resolvido** (confirmado disponível 2026-09-14)
- ~~G0903~~ — Headcount de PAs: **resolvido** (3 PAs, turno único, confirmado 2026-09-14)

**Recommendation:** Prosseguir com Enhanced Omni-Channel desde o início (evita retrabalho de migração antes do Summer '26). Reconfirmar horário do DHA (G0904) junto com as demais perguntas abertas ao cliente (Q-01 a Q-17).

---

## T-Shirt Size Distribution

| Epic | Size | Rationale |
|------|------|-----------|
| E01 — ORG Foundation & WhatsApp | **M** | Standard ORG setup + WhatsApp Channel config + Meta approval coordination |
| E02 — Einstein Bot Flows | **L** | 4 conversational flows + NLU training + complex loop logic (multi-inscription DAM) |
| E03 — API Integration | **M** | 4 REST API integrations via Apex + Flow orchestration + retry logic |
| E04 — Feedback & Satisfaction | **S** | Satisfaction survey + API CRM SEFIN callout + templates |
| E05 — UX Research & Accessibility | **M** | 12 persona interviews + 15 usability sessions + WCAG expert review |
| E06 — Security & Profiles | **M** | LGPD compliance + custom profile + audit trail + data retention |
| E07 — KB Vectorization (ADD-ON) | **XL** | ⚠️ BLOCKER G0704 — requires Data Cloud + custom integration or Agentforce upgrade |
| E08 — MC Journey (ADD-ON) | **L** | Marketing Cloud setup + Data Cloud zero-copy + Journey Builder + HSM approval |
| E09 — Transbordo Humano Omni-Channel (ADD-ON 3) | **M** | Enhanced Omni-Channel + Service Console para 3 PAs + handoff de contexto nos 4 fluxos do bot; sem bloqueadora de licenciamento (resolvido) |

**Note:** Sizes are **relative complexity, not effort** — not hour-convertible, not to be multiplied by a rate to derive a price. For timeline range use `roadmap` skill; for indicative pricing use `commercials` skill (validated rate).

**CORE Scope:** 2 L + 4 M + 1 S = Moderate-to-Significant complexity  
**ADD-ONs:** 1 XL (BLOCKER) + 2 L/M = High-to-moderate complexity; E07 carries the technical feasibility risk, E08/E09 are standard-pattern configuration

---

## Next Steps

1. **Phase 0 (2-3 semanas)** — Resolver 4 blockers (G0704, G0705, G0805, G0301/G0302) + 17 perguntas cliente (Q-01 a Q-17)
2. **Design Refinement** — Validate architecture decisions (Hyperforce Brazil, TDE vs. Shield, Einstein Bot + Data Cloud)
3. **Roadmap** — Phase epics into implementation waves + define roles needed
4. **Commercials** — Indicative pricing (ROM) with validated BRL rate
5. **Narratives** — Executive summary, pitch de valor, resumo técnico
6. **Export** — Generate PPT, PDF, site Heroku (SLDS)

---

**Documento gerado automaticamente via Scopezilla — Salesforce PS LATAM**
