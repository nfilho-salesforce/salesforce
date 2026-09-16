# Executive Summary — DATAPREV-SEFIN-CE
**Audiência:** Técnica (Arquitetos, Delivery Leads)
**Data:** 2026-09-16 (revisão — incorpora E09, ADD-ON 3)
**Projeto:** SEFIN Fortaleza — Bot WhatsApp Tributos Municipais + Transbordo Humano

---

## At a Glance

- **Dor atual**: SEFIN Fortaleza insatisfeita com fornecedor MUTANTE (R$ 1,7M/ano) — bot WhatsApp tributos com UX ruim e integrações frágeis; 400k conversas/ano sem self-service robusto e sem caminho de escalonamento humano quando o bot não resolve
- **Visão transformação**: Substituir MUTANTE por Service Cloud + Einstein Bot para autoatendimento tributos (IPTU, TMRSU, ISS, alteração cadastral) com WhatsApp Channel, 4 APIs SEFIN integradas via Flow Orchestration + Apex, UX research in-scope, e **transbordo humano via Enhanced Omni-Channel/Service Console (E09, novo)** para os casos que o bot não resolve dentro do horário comercial
- **Top value drivers**: Redução custo operacional (substituir R$ 1,7M/ano MUTANTE), Melhor experiência cidadão (UX research + WCAG 2.1 AA conversational UI + continuidade de contexto no transbordo humano), Compliance LGPD Art. 11 (CPF/CNPJ dados sensíveis, Hyperforce Brazil data residency)
- **Maior risco**: Phase 0 gap resolution (133 gaps, 17 perguntas cliente Q-01 a Q-17, 2 API specs BLOCKER G0301/G0302 — CRM SEFIN + Dados Cadastrais endpoint/payload/auth indefinidos) + Meta WhatsApp Business approval 2-8 semanas (critical path G0103). **E09 não adiciona bloqueadora nova** — as 4 confirmações de configuração (licença, edição Omni-Channel, headcount, horário) já foram obtidas do cliente.
- **Próximo passo recomendado**: Executar Phase 0 (2-3 semanas) — obter API specs bloqueadoras (G0301/G0302), decidir ISS flow (link ou DAM emission Q-04/Q-05), validar Bot Maintainer permissions (Q-15), confirmar Hyperforce Brazil (P-22), responder 17 perguntas cliente antes de kick-off

---

## Scope Summary

**8 épicas em escopo** (7 CORE 2L+4M+1S, 2 ADD-ONs L+M):

### CORE (Service Cloud + Einstein Bot + WhatsApp)
1. **E01 — ORG Foundation & WhatsApp Channel** (M): Hyperforce Brazil ORG setup from scratch + WhatsApp Channel + Named Credentials 4 SEFIN APIs + Meta WhatsApp Business approval (2-8w critical path G0103). **Delta E09**: provisionamento da licença Digital Engagement (já confirmada disponível, G0901 resolvido).
2. **E02 — Einstein Bot Conversational Flows** (L): 4 fluxos conversacionais linguagem natural (IPTU loop DAM emission multi-inscription, TMRSU mesmo fluxo tipoDebito=980, ISS link site ou upgrade DAM Q-04/Q-05, Cadastral 9-field edit) + NLU intent classification 5 intents + slot filling 6 entities (CPF/CNPJ regex + Apex checksum validation) + WhatsApp 24h window + HSM templates session resume. **Delta E09**: ponto de transferência bot → humano adicionado aos 4 fluxos, levando contexto da sessão (CPF/CNPJ, serviço, transcript) ao Case.
3. **E03 — API Integration Layer** (M): 4 REST APIs SEFIN (EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais) via Flow Orchestration + Apex @future/@queueable callouts + Named Credentials API Key secure storage + retry logic 1x + connectivity validation ping/curl pre-prod (G0303) + 2 API specs BLOCKER (Q-01/Q-02)
4. **E04 — Feedback & Satisfaction Tracking** (S): Pesquisa satisfação obrigatória todos fluxos (1-5 stars + justificativa if ≤3) + API CRM SEFIN callout Fire-and-Forget async + LGPD consent disclosure + despedida link Portal SEFIN. **Delta E09**: pesquisa disparando também no fechamento do Case pelo agente humano.
5. **E05 — UX Research & Accessibility** (M): 12 persona interviews (6 PF + 6 PJ remote Zoom) + 15 usability sessions (3 fluxos × 5 usuários) + 2 reports (usability ~5-10 pages, accessibility ~10-15 pages WCAG 2.1 AA adapted conversational UI) + bot flows refinados
6. **E06 — Security & User Profiles** (M): LGPD compliance baseline (TDE encryption, Field History Tracking, Event Monitoring) + custom profiles (System Admin clone, Bot Maintainer scoped Einstein Bot + conversation review) + data retention Apex batch job (90-day bot logs, 12-month satisfaction). **Delta E09**: novo profile **Agente Humano SEFIN** (acesso LGPD-aware a CPF/CNPJ + Service Console).

### ADD-ONs (Expansão de escopo confirmada)
7. **E08 (ADD-ON 2) — Proactive Outreach Journey** (L): Marketing Cloud Engagement (Core/Pro edition G0801 validation) + SFTP batch ingestion (SEFIN arquivo cidadãos IPTU vencido) + Journey Builder 1 jornada proativa (régua ex: D-15, D-5, D+1 reminders) + 3-5 HSM templates Meta approval 1-3 weeks + opt-out mechanism + LGPD compliance validation (G0809 legitimate public interest Art. 7, IX?) + 4,86M msgs/ano = ~13,5K/dia
8. **E09 (ADD-ON 3, novo) — Transbordo Humano via Omni-Channel/Service Console** (M — todas as 4 confirmações de escopo já obtidas): Enhanced Omni-Channel (Presence Statuses, Routing Configuration) + Service Console app para 3 PAs em turno único + Case/Messaging Session como objeto de trabalho roteado + ponto de transferência nos 4 fluxos do E02 + Business Hours real 08h-17h seg-sex + profile Agente Humano SEFIN (delta E06) + pesquisa de satisfação estendida ao fechamento humano (delta E04)

**Épica descartada**: E07 — KB Vectorization (OUT-OF-SCOPE) — cliente confirmou sem Data Cloud e sem Agentforce → KB externa inviável

---

## Solution Highlights — Architecture & Key Decisions

### Architectural Skeleton

**Platform**: Service Cloud + Einstein Bot (NOT Agentforce per v2.0 scope adjustment) + WhatsApp Channel (Salesforce Messaging via Digital Engagement) + **Enhanced Omni-Channel/Service Console (E09, novo)**

**Integration Pattern**: Flow Orchestration (business logic) + Apex @future/@queueable (REST callouts) — standard Salesforce pattern, **sem MuleSoft**

**Data Model**:
- **Contact** as primary citizen entity (PF/PJ via `Tipo_Pessoa__c` picklist)
- Custom fields: `CPF_CNPJ__c` (External ID, encrypted TDE), `Inscricao_Municipal__c`, `Digito_Inscricao__c`
- **CPF/CNPJ validation**: Regex pattern matching + Apex class `CPFValidator` (checksum Dígitos Verificadores)
- **E09**: reaproveita o modelo de dados existente (Contact/Case) — não introduz objeto customizado; Case/Messaging Session é o único objeto de trabalho do transbordo, sem campos customizados fora do padrão Salesforce

**4 SEFIN APIs** (REST + API Key auth):
1. **EmitirDamUnico** — Emite DAM PDF (IPTU tipoDebito=10, TMRSU tipoDebito=980, ISS Q-05 a confirmar)
2. **ConsultaImovel** — Busca inscrições por CPF/CNPJ (por-documento method)
3. **API CRM SEFIN** — Log satisfação (spec pending Q-01 BLOCKER)
4. **API Dados Cadastrais** — Atualização cadastral (spec pending Q-02 BLOCKER)

**LGPD Compliance** (Art. 11 CPF/CNPJ dados sensíveis):
- **Data residency**: Hyperforce Brazil ORG (São Paulo data center) — validation pending P-22 (Hyperforce Brazil vs US-East contractual unclear)
- **Encryption**: Standard TDE (Transparent Data Encryption) at-rest; Shield optional per legal interpretation G0611 (~30% license uplift if required)
- **Audit trail**: Field History Tracking (CPF/CNPJ, satisfaction fields — 24-month retention), Event Monitoring (API callout events, login events — G0604 add-on license, custo a confirmar com o pricing Salesforce)
- **Data retention**: Apex batch job scheduled weekly deletion (90-day bot logs, 12-month satisfaction data — LGPD Art. 15 minimization G0610 validation)
- **E09**: novo profile Agente Humano SEFIN acessa o mesmo dado sensível (CPF/CNPJ) já protegido por TDE/FLS — sem novo vetor de exposição, apenas nova superfície de acesso (Service Console) a governar via permissões do profile

**Einstein Bot NLU**:
- **5 intents**: IPTU, TMRSU, ISS, Alteração Cadastral, Fallback
- **6 entities** (slot filling): CPF/CNPJ (regex + Apex checksum), Data Nascimento/Abertura, Inscrições (multi-select loop), Nome, Telefone, Email, Endereço (9 sub-fields)
- **NLU training**: 50-100 utterances per intent — ownership undefined G0202 (SEFIN-CE provides or PS infers?)
- **WhatsApp 24h messaging window**: HSM (Highly Structured Messages) templates for session resume if >24h (G0208 validation)

**Loop DAM Emission Pattern** (P-29):
- **Multi-inscription support**: Cidadão seleciona 1+ inscrições → loop para cada inscrição → Flow Orchestration confirma emissão → Apex callout `EmitirDamUnico` → envia PDF via WhatsApp
- **Retry logic**: 1x retry after 1-2s delay → fallback message "tente novamente mais tarde" (P-16)
- **API response time**: <2s target for conversational UX (G0304 timeout handling if >10s, G0217 EmitirDamUnico timeout risk)

**Custom Profiles** (3, incluindo E09):
- **System Admin** (3 users): Clone standard System Administrator
- **Bot Maintainer** (7 users): Custom profile scoped to Einstein Bot Setup + Conversation Review **ONLY** (sem Flow Builder, sem API logs — Q-15 validation pending; Named Credentials API Keys hidden via FLS)
- **Agente Humano SEFIN** (3 users, novo — E09): Custom profile scoped ao Service Console + Case/Messaging Session da fila "Atendimento Tributário" — acesso a CPF/CNPJ, serviço solicitado e transcript do bot já carregado no Case, sem redigitação; **Supervisor** (perfil adicional, gestão de fila em tempo real) completa os 2 perfis do E09

**Marketing Cloud Integration** (ADD-ON E08):
- **SFTP batch ingestion** (SEM Data Cloud zero-copy): Marketing Cloud consome arquivo SEFIN diário/semanal cidadãos IPTU vencido → Data Extension 1 fonte dados → Journey Builder (1 jornada proativa régua D-15, D-5, D+1 reminders)
- **HSM templates**: 3-5 templates design + Meta approval 1-3 weeks (G0819 critical path risk)
- **Opt-out mechanism**: Reply STOP + Marketing Cloud attribute update
- **LGPD compliance**: Tax payment reminders = legitimate public interest Art. 7, IX? (G0809 legal validation pending SEFIN-CE DPO)
- **WhatsApp Business Account Tier 2+**: 13,5K msgs/day (G0808 upgrade from Tier 1 if needed)

**Transbordo Humano — Omni-Channel/Service Console** (ADD-ON 3, E09 — todas as premissas de escopo confirmadas 2026-09-14/16):
- **Enhanced Omni-Channel** (não Standard — EOL Summer '26 [KB: service_cloud_3-27-2026.md:13560-13591]): Presence Statuses + 1 única Routing Configuration (fila "Atendimento Tributário", first-available, sem critério de segmentação por skill/prioridade/tributo)
- **Digital Engagement license**: já disponível no cliente (G0901 resolvido) — Messaging (canal WhatsApp) exige Digital Engagement para ser roteável via Omni-Channel a um agente humano [KB: service_cloud_3-27-2026.md:1257-1259]
- **Handoff de contexto**: DHA (Dentro do Horário de Atendimento, 08h-17h seg-sex, G0904 confirmado) → coleta nome se ainda não coletado → Flow monta contexto (CPF/CNPJ, serviço, transcript da sessão do bot) → cria Case/Messaging Session → roteia via Enhanced Omni-Channel
- **Service Console**: app único para as 3 PAs (turno único, G0903 confirmado) — visão do Case + histórico completo da conversa do bot, sem redigitação de dados já coletados
- **Continuidade de thread**: agente humano assume a mesma thread WhatsApp — cidadão não percebe troca de canal
- **Fechamento**: agente fecha o Case ao concluir → dispara a pesquisa de satisfação automaticamente (mesma pesquisa 1-5 estrelas do fluxo bot, delta E04) — sem etapa manual do agente
- **Sem bloqueadoras remanescentes**: as 4 confirmações de configuração (licença G0901, edição Omni-Channel G0902, headcount G0903, horário do DHA G0904) foram todas resolvidas pelo cliente entre 2026-09-14 e 2026-09-16

---

## Implementation Approach

**6 Phases** (0-5) — sequência e dependências, **sem commitment semanas** (usuário escolheu "no commitment" no roadmap; a faixa 18-30 semanas abaixo é benchmark-derivada, não um compromisso):

### Phase 0 — Discovery Resolution & API Specs (MANDATORY)
**Objetivo**: Resolver 133 gaps antes de kick-off

**Epics included**: Nenhuma (fase de entrada)

**Success criteria**:
- 2 API specs bloqueadoras obtidas (CRM SEFIN endpoint/payload/auth Q-01, Dados Cadastrais endpoint/payload/auth Q-02)
- ISS flow decisão documentada (link site ou upgrade para DAM emission Q-04/Q-05)
- Bot Maintainer profile scope validado (Q-15 — Einstein Bot + conversation review ONLY ou broader access?)
- Meta WhatsApp Business status confirmado (aprovação já obtida ou timeline para obter G0103)
- Hyperforce Brazil vs US-East decisão formalizada (P-22 data residency contractual validation)
- 17 perguntas cliente (Q-01 a Q-17) respondidas

**Dependencies**: Nenhuma

**Risks**: SEFIN-CE demora >3 semanas responder perguntas (atrasa kick-off); API specs incompletas ou ambíguas (requer iteração); Meta approval timeline >8 semanas (impacta go-live); decisões arquiteturais mudam escopo (ex: ISS upgrade para DAM emission adiciona complexity)

**Target duration**: <3 semanas (per risk mitigation)

---

### Phase 1 — Foundation & ORG Setup
**Objetivo**: Provisionar Hyperforce Brazil ORG + WhatsApp Channel + Named Credentials + Security baseline LGPD + licença Digital Engagement (delta E09)

**Epics included**: E01, E06

**Success criteria**:
- Hyperforce Brazil ORG provisionada e acessível
- WhatsApp Channel aprovado Meta + conectado ao Service Cloud
- **Digital Engagement license provisionada** (delta E09 — já confirmada disponível, G0901 resolvido)
- 4 Named Credentials configuradas com API Keys (FLS Bot Maintainer hidden)
- Custom profiles ativos (System Admin clone + Bot Maintainer scoped to Einstein Bot + conversation review)
- TDE encryption at-rest enabled
- Field History Tracking (CPF/CNPJ, satisfaction fields)
- Event Monitoring configured (API callout events, login events)
- Data retention Apex batch job deployed (90-day bot logs, 12-month satisfaction data)

**Dependencies**: Phase 0 complete (API specs obtained, Meta approval timeline validated, Hyperforce Brazil confirmed)

**Risks**:
- **G0103 (BLOCKER)**: Meta WhatsApp Business approval 2-8 semanas — critical path blocker; domínio personalizado SEFIN undefined G0102 blocks approval; recommend start Meta approval process parallel to Phase 0 if domínio confirmed
- **G0104**: Hyperforce Brazil vs US-East data residency ambiguity — regulatory breach LGPD Art. 11 if wrong; P-22 contractual validation mandatory before provisioning
- **G0111**: MFA enforcement unclear — security audit finding if not enabled; recommend mandatory MFA for all 13 users (3 Admin + 7 Bot Maintainer + 3 Agente Humano SEFIN)
- **G0611**: TDE vs Shield legal interpretation — Shield adds ~30% license uplift (valor exato a confirmar com o pricing Salesforce) se SEFIN-CE DPO exigir criptografia field-level para CPF/CNPJ além do TDE padrão

---

### Phase 2 — Einstein Bot + API Integration
**Objetivo**: Construir 4 Einstein Bot conversational flows + integrar 4 SEFIN APIs + implementar satisfaction survey + adicionar ponto de transferência bot→humano nos 4 fluxos (delta E09)

**Epics included**: E02, E03, E04

**Success criteria**:
- 4 Einstein Bot dialogs configurados (IPTU/TMRSU loop DAM, ISS link ou DAM per Q-04/Q-05, Cadastral 9-field edit)
- NLU model treinado com 50-100 utterances por intent
- Slot filling + validation (CPF/CNPJ regex + Apex checksum)
- 4 Apex classes (REST callouts EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais) + retry logic (1x)
- Flow Orchestration (loop DAM emission multi-inscription P-29, validation, async invocation)
- Satisfaction survey integrado (1-5 stars + justificativa if ≤3) + API CRM SEFIN callout
- **Ponto de transferência para humano adicionado nos 4 fluxos** (delta E09 — decisão point DHA + coleta de nome, sem construir ainda o roteamento, que é entregue na Phase 5)
- Connectivity validation (ping/curl test Salesforce → SEFIN APIs pre-prod)
- Error logging via Event Log Files

**Dependencies**: Phase 1 complete (ORG + WhatsApp Channel + Named Credentials + Security baseline)

**Risks**:
- **G0202 (BLOCKER)**: NLU training data ownership — SEFIN-CE provides utterances or PS infers from discovery + client validation loop? Recommend PS drafts 50 utterances/intent from discovery docs, SEFIN-CE validates/expands to 100/intent during Phase 2 UAT
- **G0201**: ISS flow ambiguity — link only (E02 S size) or upgrade para DAM emission (E02 stays L, E03 grows to M+)? Q-04/Q-05 validation Phase 0 critical
- **G0208**: WhatsApp 24h window vs session persistence >24h — HSM templates needed for session resume; recommend 2 HSM templates (session resume "Oi [Nome], vamos continuar?", error fallback "Ocorreu um erro, tente novamente")
- **G0217**: API EmitirDamUnico timeout >10s risk — PDF generation pode demorar; recommend async pattern (Apex @future callout → poll status → send PDF when ready) if sync callout timeout confirmed >10s during connectivity validation pre-prod
- **G0301/G0302 (BLOCKER)**: API specs CRM SEFIN + Dados Cadastrais incomplete — blocks Phase 2 start if Phase 0 failed; recommend mock APIs Phase 1 parallel to Phase 0 for dev environment (stub responses), replace with real APIs Phase 2 once specs obtained
- **G0303**: Connectivity IP validation ping/curl pre-prod required — Salesforce IP ranges → SEFIN firewall whitelist; recommend obtain SEFIN firewall contact Phase 0, schedule connectivity test Phase 1 end

---

### Phase 3 — UX Research & Refinement
**Objetivo**: Executar UX research + refinar bot flows para atingir SUS >70 e task completion >80%

**Epics included**: E05

**Success criteria**:
- 12 persona interviews completas (6 PF: 2 baixa/2 média/2 alta renda + 6 PJ: 2 MEI/2 pequena/2 média empresa) via Zoom remote
- 2 persona docs gerados (PDF PT-BR, 1 PF + 1 PJ)
- 15 usability sessions executadas (3 fluxos IPTU/TMRSU/Cadastral × 5 usuários) via Zoom + working WhatsApp bot pre-production
- Usability findings report (~5-10 pages) com task completion rate >80%, time on task <5 min, SUS score >70, error rate <15%
- Accessibility report (~10-15 pages) WCAG 2.1 AA adapted conversational UI (plain language Flesch >60 PT-BR, screen reader VoiceOver+TalkBack testing)
- Bot flows refinados baseado em findings (NLU utterances expandidas, slot filling error messages ajustadas, satisfaction survey flow otimizado)
- LGPD consent forms for all participants (G0514)

**Dependencies**: Phase 2 complete (working WhatsApp bot pre-production para usability testing com cidadãos reais). **Pode correr em paralelo à Phase 5 (E09)** — disciplinas diferentes.

**Risks**:
- **G0501**: UX research ownership — PS conducts (E05 stays M) or DATAPREV conducts with PS guidance (E05 shrinks to S — PS delivers persona template, usability script, accessibility checklist only)?
- **G0507**: WCAG 2.1 AA não aplicável a conversational UI — W3C Conversational Accessibility Guidelines needed; recommend adapt WCAG 2.1 AA heuristics (plain language Flesch >60 PT-BR, 1 question at a time minimal cognitive load, screen reader VoiceOver+TalkBack testing) + note limitation in accessibility report
- **G0514**: LGPD consent form for persona interviews + usability testing — require explicit opt-in Art. 7 before research session; recommend DATAPREV legal drafts consent form Phase 1, PS reviews Phase 2
- **G0509**: Accessibility testing with PcD — expert review (E05 M size) vs user testing with PcD participants (E05 grows to L)? Recommend expert review Phase 3 + user testing Phase 4 optional if budget allows
- Usability findings requerem refactor significativo bot flows — if task completion <70% or SUS <60, may require Phase 2 rework (NLU model retrain, slot filling logic redesign, Flow Orchestration loop simplification); recommend allocate 1-2 weeks contingency buffer Phase 3 end for major redesign if needed

---

### Phase 4 (ADD-ON 2) — Marketing Cloud Proactive Journey
**Objetivo**: Setup Marketing Cloud + SFTP batch ingestion + Journey Builder 1 jornada proativa + HSM templates Meta approval

**Epics included**: E08

**Success criteria**:
- Marketing Cloud account provisionada (Core/Pro edition — G0801 validation needed) + WhatsApp connector configured (Meta Business API)
- SFTP batch ingestion configurada (Marketing Cloud Data Extension 1 fonte dados cidadãos IPTU vencido — arquivo SEFIN diário/semanal G0820 format/frequency defined)
- 1 segmentação configurada (sem Identity Resolution)
- Journey Builder (1 jornada proativa IPTU vencido régua ex: D-15, D-5, D+1 reminders — triggers/régua per Q-G/Q-H)
- 3-5 HSM templates design + Meta approval obtained (1-3 weeks timeline)
- Opt-out mechanism configured (reply STOP + Marketing Cloud attribute update)
- LGPD compliance validation (tax payment reminders = legitimate public interest? — G0809 legal validation Art. 7, IX)
- WhatsApp Business Account Tier 2+ upgrade if needed (13,5K msgs/day — G0808)

**Dependencies**: Phase 2 complete (WhatsApp Channel + Meta approval já obtidos para Service Cloud); SEFIN batch file format/frequency definido (G0820 — pode ser paralelo Phase 0-2 se SEFIN fornece specs cedo). **Pode correr em paralelo à Phase 5 (E09)** — disciplinas diferentes.

**Risks**:
- **G0801**: Marketing Cloud edition undefined — Core, Pro, or Premium (SKU e valor exatos a confirmar com o pricing Salesforce)? Core sufficient for 1 jornada + 1 Data Extension + 13,5K msgs/day; Pro needed if >1 jornada or A/B testing; recommend Core edition Phase 4 unless client requires multi-journey roadmap
- **G0809 (BLOCKER)**: LGPD consent for proactive marketing — tax payment reminders = legitimate public interest Art. 7, IX (no opt-in required) or requires explicit consent (opt-in before first message)? Legal validation SEFIN-CE DPO mandatory Phase 0; if opt-in required, Journey Builder adds consent validation step before message send (E08 grows to XL)
- **G0808**: WhatsApp Business Account Tier 2+ required — 13,5K msgs/day; Meta Tier 1 limit ~1K msgs/day; if current SEFIN-CE WhatsApp Business Account is Tier 1, upgrade to Tier 2 required (fee e pricing per-conversation a confirmar com Meta); recommend validate current Tier Phase 0
- **G0820 (BLOCKER)**: SEFIN batch file format/frequency undefined — daily/weekly? CSV/JSON/XML? Columns (CPF/CNPJ, Inscrição, Valor Débito, Data Vencimento)? Recommend obtain SEFIN batch file sample + SFTP credentials Phase 0; if SEFIN batch file não existe hoje, SEFIN IT team needs to build batch export job (out-of-scope PS, may delay Phase 4 start)
- **G0819**: HSM templates Meta approval timeline 1-3 weeks — critical path risk for Phase 4 go-live; recommend submit HSM templates for Meta approval Phase 3 (parallel to UX research) to absorb approval latency before Phase 4 start

---

### Phase 5 (ADD-ON 3, novo) — Transbordo Humano via Omni-Channel/Service Console
**Objetivo**: Provisionar Enhanced Omni-Channel + Service Console para as 3 PAs + roteamento do Case/Messaging Session + profile Agente Humano SEFIN

**Epics included**: E09

**Success criteria**:
- Enhanced Omni-Channel configurado — Presence Statuses + 1 única Routing Configuration (fila "Atendimento Tributário", first-available, sem critério de segmentação)
- Service Console app ativo para as 3 PAs (turno único) com painel de contexto SEFIN (CPF/CNPJ, serviço solicitado, transcript do bot)
- Case/Messaging Session recebendo o contexto completo da sessão do bot — sem redigitação
- Business Hours real configurado (08h-17h, segunda a sexta — G0904 confirmado)
- Profile **Agente Humano SEFIN** ativo (delta E06) + profile **Supervisor** (visibilidade de fila, PAs disponíveis/ocupadas, Cases abertos em tempo real, sem relatório customizado)
- Fechamento do Case dispara a pesquisa de satisfação automaticamente (delta E04)

**Dependencies**: Phase 1 completo (E01 — Digital Engagement + WhatsApp Channel provisionados); Phase 2 completo (E02 — 4 fluxos do bot existentes para os pontos de handoff). **Pode correr em paralelo às Phases 3 e 4** — disciplinas diferentes (configuração Omni-Channel/Service Console não compete com UX research nem Marketing Cloud).

**Risks**: Nenhuma bloqueadora remanescente — G0901 (licença), G0902 (edição Omni-Channel), G0903 (headcount) e G0904 (horário DHA) foram todas confirmadas pelo cliente entre 2026-09-14 e 2026-09-16. Risco residual: volume de escalonamento real pode exceder a capacidade de 3 PAs/turno único (ver `size_if_assumption_breaks` no estimate — E09 subiria de M para L se isso ocorrer).

---

## Effort Summary

**T-shirt distribution** (8 epics em escopo): 2L + 5M + 1S (CORE 6 epics) + 1L + 1M (2 ADD-ONs)

**Complexity drivers**:
- **Large (L) epics**: E02 (Einstein Bot 4 flows + NLU + slot filling + loop DAM multi-inscription + WhatsApp 24h window + HSM templates + novo ponto de transferência para humano), E08 ADD-ON (Marketing Cloud + SFTP batch + Journey Builder + HSM templates Meta approval + LGPD consent validation + opt-out)
- **Moderate (M) epics**: E01 (ORG setup + WhatsApp Channel + Meta approval 2-8w critical path + Named Credentials + licença Digital Engagement), E03 (4 REST APIs + Flow Orchestration + Apex + retry logic + connectivity validation + 2 API specs BLOCKER), E05 (UX research 12 interviews + 15 usability sessions + 2 reports WCAG adapted), E06 (LGPD compliance TDE + custom profiles + Field History Tracking + Event Monitoring + data retention Apex batch job + novo profile Agente Humano SEFIN), **E09 (ADD-ON 3, novo) — Enhanced Omni-Channel + Service Console 3 PAs + handoff de contexto + Business Hours real + profile Agente Humano SEFIN; nenhuma dimensão em L após G0901/G0903 resolvidos**
- **Small (S) epic**: E04 (Satisfaction survey 1-5 stars + justificativa conditional + API CRM SEFIN callout Fire-and-Forget + extensão ao fechamento humano)

**Disciplines required** (6 roles by phase — E09 não introduz papel novo, apenas estende o trabalho do Technical Architect e do Technical Consultant Security+Profiles):

| Discipline | Phases Active | Rationale |
|------------|---------------|-----------|
| **Technical Architect** | 0,1,2,3,4,5 | Solution architecture ownership across all phases — Hyperforce Brazil vs US-East decisão, Einstein Bot NLU design, integration patterns (Flow Orchestration + Apex + 4 SEFIN APIs), LGPD compliance + TDE encryption baseline, Marketing Cloud SFTP batch ingestion pattern, HSM templates Meta approval orchestration, UX accessibility adaptado conversational UI, **Enhanced Omni-Channel/Service Console setup (E09) — Presence Statuses, Routing Configuration, fila única "Atendimento Tributário"** |
| **Technical Consultant** | 1,2,4,5 | Build E01 (ORG Foundation + WhatsApp Channel + Named Credentials + licença Digital Engagement), E02 (4 Einstein Bot flows — IPTU/TMRSU loop DAM, ISS link ou DAM, Cadastral 9-field edit + NLU training 50-100 utterances + slot filling + validation + ponto de transferência para humano), E03 (4 Apex REST callouts + Flow Orchestration loop multi-inscription P-29 + retry logic + connectivity validation ping/curl), E04 (satisfaction survey 1-5 stars + API CRM SEFIN callout + extensão fechamento humano), E08 ADD-ON (Marketing Cloud SFTP batch ingestion + Journey Builder 1 jornada proativa + HSM templates design), **E09 ADD-ON 3 (Flow de handoff de contexto bot→Case nos 4 fluxos + Service Console layout config)** |
| **Technical Consultant (Security + Profiles)** | 1,2,5 | E06 (Security & Profiles) — custom profiles (System Admin clone + Bot Maintainer scoped Einstein Bot + conversation review), Field History Tracking (CPF/CNPJ, satisfaction), Event Monitoring (API callout + login events), data retention Apex batch job (90-day bot logs, 12-month satisfaction), Named Credentials API Keys FLS Bot Maintainer hidden, **profile Agente Humano SEFIN + Supervisor (E09) — acesso LGPD-aware a CPF/CNPJ via Service Console** |
| **Experience Architect** | 3 | E05 (UX Research & Accessibility) — 12 persona interviews (6 PF: 2 baixa/2 média/2 alta renda + 6 PJ: 2 MEI/2 pequena/2 média empresa) via Zoom remote, 2 persona docs (PDF PT-BR), 15 usability sessions (3 fluxos IPTU/TMRSU/Cadastral × 5 usuários) via Zoom + working WhatsApp bot pre-production, usability findings report (~5-10 pages) task completion >80% + time on task <5min + SUS >70 + error rate <15%, accessibility report (~10-15 pages) WCAG 2.1 AA adapted conversational UI (plain language Flesch >60 PT-BR, screen reader VoiceOver+TalkBack testing), bot flows refinados baseado em findings, LGPD consent forms all participants (G0514). **Why UX Research here**: Adoption / rework risk if deferred — without persona validation and usability testing, bot flows risk 15-30% rework post-go-live per industry benchmarks (BCG 2023 digital transformation study); conversational UI accessibility (WCAG adapted) mitigates PcD exclusion risk (LGPD Art. 5 non-discrimination principle). |
| **Technical Architect (Phase 0)** | 0 | Phase 0 gap resolution orchestration — coordenar respostas SEFIN-CE 17 perguntas (Q-01 a Q-17), obter API specs bloqueadoras (CRM SEFIN + Dados Cadastrais endpoint/payload/auth — G0301/G0302), validar Meta WhatsApp Business approval timeline, definir ISS flow decisão (link ou DAM emission Q-04/Q-05), confirmar Hyperforce Brazil data residency (P-22), negociar Bot Maintainer permissions (Q-15), documentar decisões arquiteturais |
| **Project Manager** | 0,1,2,3,4,5 | Cross-phase delivery orchestration — Phase 0 gap resolution coordination (133 gaps, 17 perguntas cliente, 2 API specs bloqueadoras), sequencing Phase 1 Meta approval critical path (G0103 2-8 semanas), Phase 2 dependency management (working WhatsApp bot pre-production required for Phase 3 UX testing), Phase 4 ADD-ON HSM templates Meta approval timeline (G0819 1-3 semanas critical path), **Phase 5 ADD-ON 3 sequencing (E09 depende de E01+E02, corre em paralelo às Phases 3/4)**, stakeholder communication (Alex Siqueira AP PS + Oswaldo Melo SE + SEFIN-CE DPO + Meta Business API team). **Why Governance not flagged**: Project scope is single-team config ownership (13 users, 1 ORG); no multi-team coordination, no CoE setup, no change-management epic — governance overhead minimal for this engagement size. |

**Framing note**: One person may fill multiple roles; one role may be filled by multiple people. Team sizing, FTE counts, and staffing are not within this artifact's scope.

**Benchmark-based duration**: 18-30 weeks (top-down from engagement shape) — Service Cloud Medium complexity (12-18w base) + 35-45% risk adders (new client greenfield ORG, LGPD regulated CPF/CNPJ Art. 11, Meta approval critical path 2-8w) **+ 2-4 semanas incrementais para E09 (ADD-ON 3, tamanho M, majoritariamente configuração — Enhanced Omni-Channel, Service Console 3 PAs, handoff nos 4 fluxos do bot)**. **Benchmark-based, not a commitment** — per user choice "no commitment" in roadmap. For a committed timeline, validate this range or specify an alternative.

**Indicative PS range**: R$ 1.781.136 – R$ 4.882.236 BRL (18-30 weeks × capacity 2-3 architects + 1-2 developers, engagement-level top-down from DATAPREV validated bill rates COM IMPOSTO: Architect R$ 7.032,56/dia, Developer R$ 5.725,28/dia). E09 não introduziu papel novo — mesma composição de equipe do range anterior (sem E09: R$ 1.583.232 – R$ 4.231.269 BRL), o incremento vem inteiramente do acréscimo de 2-4 semanas de duração. **Input-derived, not a fixed fee** — rates supplied and validated by user 2026-07-03; multiplied by top-down effort basis. Travel, expenses, and third-party costs (Salesforce licenses, Meta WhatsApp Business API fees, Digital Engagement/Omni-Channel Enhanced license) billed as actual and not included.

**AI delivery efficiency**: ~12-19% realized efficiency at Mid readiness (score 3/8) — greenfield ORG favors gains, but AI tooling policy and slow government approval cycles cap upside. Gains cluster in documentation (UX reports ~18-28%, security baseline LGPD ~18-28%) and Einstein Bot NLU drafting (~12-24%); coding/API integration carry the AI tax (~8-18% — LGPD review burden CPF/CNPJ Art. 11 + API specs pending G0301/G0302 BLOCKER + connectivity validation). E09's largely declarative configuration (Omni-Channel setup, Business Hours, profiles) is a natural fit for the higher end of the documentation/config efficiency band, though this hasn't been separately re-run in `efficiency.json`. **Not headcount reduction, not a pricing input** — pace and quality lift within the same team shape.

---

## Risks and Mitigations

### Critical Path Risks (BLOCKER)

1. **Phase 0 Gap Resolution (133 gaps, 17 Qs cliente, 2 API specs BLOCKER)**
   - **Risk**: SEFIN-CE demora >3 semanas responder perguntas (atrasa kick-off); API specs CRM SEFIN (Q-01) + Dados Cadastrais (Q-02) incomplete/ambiguous (blocks Phase 2 E03 start)
   - **Impact**: Phase 1 start delayed; Phase 2 E03 blocked without API specs; ISS flow ambiguity (Q-04/Q-05) may change E02 size S→L if upgrade to DAM emission
   - **Mitigation**: Recommend Phase 0 target <3 semanas; schedule SEFIN-CE stakeholder alignment session (Alex Siqueira AP PS + Oswaldo Melo SE + SEFIN-CE DPO + SEFIN IT lead) within 1st week of Phase 0 to prioritize 17 Qs + 2 API specs bloqueadoras; parallel track Meta approval process Phase 0 if domínio confirmed; draft mock APIs Phase 1 for dev environment (stub responses) to unblock Phase 2 dev parallel to Phase 0 real API specs obtainment

2. **Meta WhatsApp Business Approval (G0103 2-8 semanas critical path Phase 1)**
   - **Risk**: Meta approval >8 semanas (delays Phase 1 complete, impacts go-live); domínio personalizado SEFIN undefined (G0102 blocks Meta approval request)
   - **Impact**: Phase 1 extends beyond 8 weeks; Phase 2 start delayed (WhatsApp Channel prerequisite); Phase 5 (E09) also delayed, since it depends on E01's WhatsApp Channel + Digital Engagement provisioning
   - **Mitigation**: Start Meta approval process parallel to Phase 0 gap resolution (requires domínio personalizado SEFIN confirmed Q-03); if domínio undefined, recommend SEFIN-CE IT obtain domínio within 1st week Phase 0 (e.g., atendimento.sefin.fortaleza.ce.gov.br); escalate to Meta Business API support if approval >6 semanas to expedite review

3. **LGPD Compliance Legal Interpretation (G0611 TDE vs Shield, G0809 proactive consent)**
   - **Risk**: SEFIN-CE DPO requires Shield field-level encryption beyond standard TDE (adds ~30% license uplift, valor exato a confirmar com o pricing Salesforce); proactive marketing requires explicit consent opt-in (E08 ADD-ON grows to XL)
   - **Impact**: License budget increase 30% if Shield required; Phase 4 ADD-ON complexity increases if opt-in required (Journey Builder adds consent validation step before message send)
   - **Mitigation**: Obtain SEFIN-CE DPO written opinion Phase 0 on TDE sufficiency for LGPD Art. 11 CPF/CNPJ sensitive data (recommend standard TDE sufficient per Salesforce security white paper + Hyperforce Brazil data residency); obtain SEFIN-CE DPO + DATAPREV legal written opinion Phase 0 on proactive marketing legitimate public interest Art. 7, IX (recommend tax payment reminders = legitimate public interest, no opt-in required per LGPD precedent governo municipal Fortaleza IPTU)

### Technical Risks

4. **NLU Training Data Ownership (G0202)**
   - **Risk**: SEFIN-CE não fornece utterances; PS infers from discovery + client validation loop adds 2-3 weeks Phase 2
   - **Impact**: Phase 2 E02 NLU model training delayed; bot accuracy <70% if utterances insufficient or não representam linguagem real cidadãos Fortaleza
   - **Mitigation**: PS drafts 50 utterances/intent from discovery docs Phase 1; SEFIN-CE validates/expands to 100/intent during Phase 2 sprint 1; conduct mini pilot 10-20 real conversations Phase 2 sprint 2 to validate NLU accuracy >70% before Phase 3 UX testing

5. **API EmitirDamUnico Timeout (G0217)**
   - **Risk**: PDF generation >10s (Salesforce callout timeout limit); sync callout fails, cidadão sees error
   - **Impact**: User experience degraded; citizen abandons flow; satisfaction score <3; rework Phase 2 to async pattern adds 1-2 weeks
   - **Mitigation**: Conduct connectivity validation ping/curl test Phase 1 end; if EmitirDamUnico response time confirmed >10s, implement async pattern Phase 2 sprint 2 (Apex @future callout → poll status endpoint every 2s for max 30s → send PDF when ready → fallback "DAM sendo gerado, receberá em 1-2 minutos" if >30s)

6. **WhatsApp 24h Messaging Window (G0208)**
   - **Risk**: Session persistence >24h not supported by WhatsApp Business API; bot cannot resume conversation after 24h without HSM template
   - **Impact**: Citizen who abandons conversation cannot resume same session; must restart from menu initial; UX friction; satisfaction <3
   - **Mitigation**: Implement 2 HSM templates Phase 2 sprint 3 (session resume "Oi [Nome], vamos continuar onde paramos?", error fallback "Ocorreu um erro, tente novamente"); submit HSM templates for Meta approval Phase 2 sprint 3 (1-3 weeks approval timeline); if Meta approval delayed, fallback to restart conversation from menu initial (document limitation in usability report Phase 3)

7. **Volume de escalonamento acima da capacidade de 3 PAs (E09, residual)**
   - **Risk**: Fração real de conversas que resultam em transbordo (hoje sem dado histórico — bot é novo) excede a capacidade de 3 PAs em turno único, gerando fila de espera excessiva
   - **Impact**: Tempo de espera no transbordo degrada a experiência que o E09 deveria melhorar; pode pressionar o cliente a pedir headcount adicional ou turnos extras fora do escopo atual (E09 sobe de M para L, conforme `size_if_assumption_breaks`)
   - **Mitigation**: Monitorar taxa de transbordo real nas primeiras 4-6 semanas pós-go-live (meta: dimensionar contra o volume observado, não o assumido); Supervisor tem visibilidade de fila em tempo real para escalar internamente se necessário; se o volume estrutural exceder a capacidade, tratar como change request de headcount/turnos, não como retrabalho de arquitetura (a fila única e o roteamento first-available absorvem mais PAs sem redesenho)

### Governance Risks

8. **UX Research Ownership (G0501)**
   - **Risk**: PS conducts UX research (E05 M size, 12 interviews + 15 usability sessions) OR DATAPREV conducts with PS guidance (E05 S size, PS delivers templates only)?
   - **Impact**: If PS conducts, E05 effort stays M (~8-12 weeks inclusive interview scheduling + report drafting); if DATAPREV conducts, E05 shrinks to S (~2-3 weeks PS template delivery + DATAPREV executes), but rework risk if DATAPREV lacks UX research experience (usability findings may miss critical friction points → 15-30% rework Phase 2 post-go-live)
   - **Mitigation**: Recommend PS conducts UX research Phase 3 (E05 M size) to mitigate rework risk; if budget constraint forces DATAPREV execution, PS delivers detailed persona template (20-page guide), usability script (30-page protocol step-by-step), accessibility checklist (WCAG 2.1 AA adapted 15-page rubric) + conducts 1-day training session DATAPREV UX team Phase 2 end

9. **Hyperforce Brazil Data Residency (P-22)**
   - **Risk**: Hyperforce Brazil vs US-East contractual unclear; LGPD Art. 11 CPF/CNPJ sensitive data requires data stored in Brazil (São Paulo data center)?
   - **Impact**: If US-East ORG provisioned incorrectly, regulatory breach LGPD Art. 11 (data stored outside Brazil); SEFIN-CE DPO audit finding; potential fine ANPD (Autoridade Nacional de Proteção de Dados, teto legal de até 2% do faturamento) — exposição financeira e reputacional relevante
   - **Mitigation**: Obtain SEFIN-CE DPO + DATAPREV legal written opinion Phase 0 on Hyperforce Brazil data residency requirement; if Hyperforce Brazil mandatory, provision Hyperforce Brazil ORG Phase 1 (confirm São Paulo data center via Salesforce Support ticket); if US-East acceptable with TDE encryption + contractual Data Processing Addendum (DPA), provision US-East ORG Phase 1 (faster provisioning, lower latency to Salesforce APIs) + document contractual DPA in LGPD compliance baseline

---

## Assumptions and Confidence Level

**Overall Confidence (8 épicas em escopo, excluindo E07 out-of-scope)**: 62,5% Confirmed (5/8: E01, E02, E04, E05, E09), 37,5% Assumed (3/8: E03, E06, E08), 0% Unknown. **Melhora em relação à revisão anterior (53%/40%/7%)** — E09 entra como Confirmed porque as 4 confirmações de escopo do cliente (licença, edição Omni-Channel, headcount, horário) já foram obtidas.

**Key Assumptions**:

1. **Phase 0 duration**: <3 semanas target (SEFIN-CE responsiveness assumption); if >3 semanas, Phase 1 start delayed proportionally
2. **UX research ownership**: PS conducts (E05 M size assumption per P-31); if DATAPREV conducts with PS guidance, E05 shrinks to S (~50% effort reduction), but rework risk 15-30% post-go-live if DATAPREV lacks UX research experience
3. **Meta WhatsApp Business approval**: 2-8 semanas timeline assumption (G0103); if >8 semanas, Phase 1 critical path extended (also delays Phase 5/E09, which depends on E01's WhatsApp Channel provisioning); recommend parallel track Phase 0 to absorb latency
4. **Hyperforce Brazil data residency**: Hyperforce Brazil available and validated for LGPD Art. 11 CPF/CNPJ sensitive data compliance assumption (P-22); if only US-East available, legal risk escalation SEFIN-CE DPO required Phase 0 (may add governance effort)
5. **Marketing Cloud edition**: Core or Pro edition assumption (G0801 Phase 4 ADD-ON); if Premium required, licensing cost impact substancial (valor a confirmar com o pricing Salesforce) e disciplina adicional de Marketing Cloud Consultant pode ser necessária (aumenta capacidade de developer no topo da faixa)
6. **API specs bloqueadoras**: CRM SEFIN + Dados Cadastrais API specs obtained during Phase 0 assumption (G0301/G0302); if specs incomplete/ambiguous or unavailable, Phase 2 blocked (duration high-end increases, or mock APIs fallback adds rework risk when real APIs delivered)
7. **ISS flow decisão**: Link site only assumption (E02 L size per current scope); if Q-04/Q-05 validation Phase 0 → upgrade to DAM emission, E02 stays L but E03 grows to M+ (additional API EmitirDamUnico logic for ISS tipoDebito)
8. **Bot Maintainer permissions**: Einstein Bot + conversation review ONLY assumption (Q-15); if broader access required (e.g., Flow Builder, API logs, Named Credentials), Bot Maintainer profile complexity increases (additional permissions audit + FLS config)
9. **LGPD consent for proactive marketing**: Tax payment reminders = legitimate public interest Art. 7, IX assumption (no opt-in required per G0809); if explicit consent required, Journey Builder adds consent validation step before message send (E08 ADD-ON grows to XL)
10. **SEFIN batch file**: SEFIN IT team provides batch file cidadãos IPTU vencido diário/semanal assumption (G0820 Phase 4 ADD-ON); if batch file não existe hoje, SEFIN IT team needs to build batch export job (out-of-scope PS, may delay Phase 4 start 2-4 weeks)
11. **Volume de transbordo (E09)**: 3 PAs em turno único assumption (G0903, confirmado pelo cliente); se o volume real de escalonamento pós-go-live exceder essa capacidade, E09 sobe de M para L (ver `size_if_assumption_breaks`) — trata-se de change request de headcount/turnos, não de retrabalho de arquitetura, dado que a fila única absorve mais PAs sem redesenho

---

## Next Steps and Recommendations

### Immediate Actions (Before Phase 0 Kick-off)

1. **Schedule Phase 0 alignment session** (target: within 1 week of approval)
   - **Attendees**: Alex Siqueira (AP PS), Oswaldo Melo (SE), SEFIN-CE DPO, SEFIN-CE IT lead, DATAPREV CTID, Salesforce PS Technical Architect
   - **Agenda**: Prioritize 17 perguntas cliente (Q-01 a Q-17) + 2 API specs bloqueadoras (G0301/G0302 CRM SEFIN + Dados Cadastrais endpoint/payload/auth) + ISS flow decisão (Q-04/Q-05 link ou DAM emission) + Bot Maintainer permissions (Q-15 Einstein Bot + conversation review ONLY or broader?) + Hyperforce Brazil vs US-East decisão (P-22 data residency validation)
   - **Deliverable**: Phase 0 completion target date (recommend <3 semanas from kick-off)

2. **Obtain SEFIN-CE domínio personalizado** (G0102 BLOCKER Meta approval)
   - **Owner**: SEFIN-CE IT lead
   - **Deliverable**: Domínio DNS (e.g., atendimento.sefin.fortaleza.ce.gov.br) + DNS records configured (CNAME, TXT for Meta verification)
   - **Timeline**: Within 1st week Phase 0 (parallel track Meta approval process to absorb 2-8 semanas latency)

3. **Initiate Meta WhatsApp Business approval process** (G0103 2-8 semanas critical path)
   - **Owner**: Salesforce PS Technical Architect + SEFIN-CE stakeholder
   - **Deliverable**: Meta WhatsApp Business account Tier 2+ approved + WhatsApp Channel connected to Salesforce ORG
   - **Timeline**: Start parallel to Phase 0 gap resolution (requires domínio personalizado SEFIN confirmed); escalate to Meta Business API support if >6 semanas

4. **LGPD legal opinions Phase 0** (G0611 TDE vs Shield, G0809 proactive consent)
   - **Owner**: SEFIN-CE DPO + DATAPREV legal
   - **Deliverable**: Written opinions (1-2 pages each) on (a) TDE sufficiency for LGPD Art. 11 CPF/CNPJ sensitive data (recommend standard TDE sufficient per Salesforce security white paper + Hyperforce Brazil data residency), (b) Proactive marketing legitimate public interest Art. 7, IX (recommend tax payment reminders = legitimate public interest, no opt-in required)
   - **Timeline**: Within 2 weeks Phase 0 (blocks Phase 1 ORG provisioning decision Hyperforce Brazil vs US-East, blocks Phase 4 ADD-ON scope Journey Builder consent validation)

### Phase 0 Deliverables (Target <3 Semanas)

1. **API Specs Bloqueadoras** (G0301/G0302)
   - CRM SEFIN API spec (Q-01): endpoint, payload (CPF/CNPJ + nota satisfação 1-5 + justificativa text), auth (API Key), error codes
   - API Dados Cadastrais spec (Q-02): endpoint, payload (CPF/CNPJ + 9 fields nome/telefone/email/endereço), auth (API Key), error codes
   - Recommend SEFIN-CE IT fornece OpenAPI 3.0 spec or Postman collection Phase 0 week 1 for PS validation

2. **Gap Resolution Report** (137 gaps → 0 gaps, dos quais os 4 ligados a E09 já resolvidos: G0901 licença, G0902 edição Omni-Channel, G0903 headcount, G0904 horário DHA)
   - 17 perguntas cliente (Q-01 a Q-17) respondidas
   - ISS flow decisão documentada (Q-04/Q-05 link site ou upgrade DAM emission)
   - Bot Maintainer permissions validadas (Q-15 Einstein Bot + conversation review ONLY confirmed)
   - Meta WhatsApp Business approval status confirmed (timeline 2-8 semanas from domínio DNS configured)
   - Hyperforce Brazil vs US-East decisão formalizada (P-22 data residency legal opinion obtained)

3. **Architecture Decision Record (ADR)**
   - Document architectural decisions from Phase 0: Hyperforce Brazil ORG (São Paulo data center), Standard TDE encryption (Shield optional per G0611 legal opinion), Named Credentials 4 SEFIN APIs (API Key FLS Bot Maintainer hidden), Einstein Bot NLU 5 intents (IPTU, TMRSU, ISS, Cadastral, Fallback), Loop DAM emission pattern (multi-inscription P-29), HSM templates (session resume + error fallback), Marketing Cloud Core edition (Phase 4 ADD-ON G0801 validation), **Enhanced Omni-Channel + fila única "Atendimento Tributário" (Phase 5 ADD-ON 3, E09)**
   - Recommend Salesforce PS Technical Architect drafts ADR Phase 0 week 3, SEFIN-CE + DATAPREV CTID review/approve before Phase 1 kick-off

### Long-Term Recommendations (Post-Go-Live)

1. **Sustentação AMS** (DATAPREV assumes per discovery v2.0 decision)
   - PS delivers documentation only: Admin Guide (~20-30 pages ORG config + Named Credentials + custom profiles + data retention Apex batch job), Bot Maintenance Guide (~30-40 pages Einstein Bot dialog config + NLU training utterances expand + slot filling validation adjust + Flow Orchestration loop DAM logic), API Integration Guide (~20-30 pages 4 SEFIN APIs endpoint/payload/auth + retry logic + connectivity troubleshooting), UX Refinement Guide (~15-20 pages usability testing protocol + accessibility WCAG 2.1 AA checklist + bot flows refine based on citizen feedback satisfaction <3), **Service Console/Omni-Channel Guide (~10-15 pages fila management, profile Agente Humano SEFIN, Supervisor dashboard usage — novo, E09)**
   - Recommend DATAPREV trains 6-8 pessoas (2 Bot Maintainer profile + 1 System Admin + 3 Agente Humano SEFIN + 1-2 Supervisor) during Phase 2-3/5 shadowing PS Technical Consultant for knowledge transfer (budget 40-60h knowledge transfer per Phase 2-3, +15-20h para Phase 5/E09)

2. **Continuous UX Improvement Roadmap** (Post-Go-Live +3 months)
   - Monitor satisfaction score 1-5 stars (target: média ≥4,0 across all 4 flows IPTU/TMRSU/ISS/Cadastral, incluindo fechamento humano via E09)
   - If satisfaction <3 rate >15% any flow, conduct targeted usability testing (5-10 citizens that flow) + refine bot flows (NLU utterances expand, slot filling error messages clarify, Flow Orchestration loop simplify)
   - Recommend DATAPREV Bot Maintainer team reviews satisfaction data weekly first 3 months post-go-live, monthly thereafter; Supervisor reviews fila do transbordo (tempo de espera, volume) na mesma cadência

3. **Phase 4 ADD-ON Go-Decision Timing** (Marketing Cloud Proactive Journey)
   - Recommend defer Phase 4 ADD-ON go-decision until Phase 2-3 complete (working WhatsApp bot production + UX research findings available)
   - If CORE bot satisfaction ≥4,0 and SEFIN-CE budget approves Marketing Cloud (licenciamento + esforço PS da Phase 4 — valores a confirmar via `commercials` quando o ADD-ON for priorizado), initiate Phase 4 ADD-ON
   - If CORE bot satisfaction <3,5 or budget constraint, defer Phase 4 ADD-ON to FY27 H2 and focus Phase 3-4 effort on CORE bot refinement + monitoring + knowledge transfer DATAPREV AMS team

4. **Phase 5 (E09) capacity monitoring** (novo)
   - Monitorar taxa real de transbordo (% de conversas que escalonam para humano) nas primeiras 4-6 semanas pós-go-live
   - Se o volume exceder a capacidade de 3 PAs/turno único de forma estrutural (não pontual), tratar como change request de headcount/turnos adicionais — a fila única "Atendimento Tributário" e o roteamento first-available do Enhanced Omni-Channel absorvem PAs adicionais sem redesenho de arquitetura

---

**Próximo passo**: `export` packages all deliverables into the client-ready Excel workbook and Word docs (PPTX/site já existentes deverão ser regenerados para refletir E09, o range comercial e a timeline atualizados). Say 'export the deliverables' or 'give me the files'. If you also need a deck, `slides` builds it.
