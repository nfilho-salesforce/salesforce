# Roadmap — DATAPREV-SEFIN-CE

**Total program duration**: per user commitment (TBD). Phases below show sequence and dependencies only.

---

## Phase 0 — Discovery Resolution & API Specs

**Objectives**: Resolver 133 gaps identificados no requirements antes de kick-off; obter specs completas APIs CRM SEFIN + Dados Cadastrais (BLOCKER G0301/G0302); validar Meta WhatsApp Business approval timeline; decidir ISS flow (link ou DAM emission Q-04/Q-05); definir Bot Maintainer permissions (Q-15); confirmar Hyperforce Brazil data residency (P-22).

**Success Criteria**: 2 API specs bloqueadoras obtidas (CRM SEFIN endpoint/payload/auth, Dados Cadastrais endpoint/payload/auth); ISS flow decisão documentada; Bot Maintainer profile scope validado; Meta WhatsApp Business status confirmado (aprovação já obtida ou timeline para obter); Hyperforce Brazil vs US-East decisão formalizada; 17 perguntas cliente (Q-01 a Q-17) respondidas.

**Dependencies**: Nenhuma — fase de entrada.

**Risks**: SEFIN-CE demora >3 semanas responder perguntas (atrasa kick-off); API specs incompletas ou ambíguas (requer iteração); Meta approval timeline >8 semanas (impacta go-live); decisões arquiteturais mudam escopo (ex: ISS upgrade para DAM emission adiciona complexity).

---

## Phase 1 — Foundation & ORG Setup

**Epics**: E01 (ORG Foundation & WhatsApp Channel), E06 (Security & Profiles)

**Objectives**: Provisionar Hyperforce Brazil ORG + WhatsApp Channel + Named Credentials para 4 SEFIN APIs + Security baseline LGPD (TDE encryption, Field History Tracking, Event Monitoring, custom profiles).

**Success Criteria**: Hyperforce Brazil ORG provisionada e acessível; WhatsApp Channel aprovado Meta + conectado ao Service Cloud; 4 Named Credentials configuradas com API Keys (FLS Bot Maintainer hidden); Custom profiles ativos (System Admin clone + Bot Maintainer scoped to Einstein Bot + conversation review); TDE encryption at-rest enabled; Field History Tracking (CPF/CNPJ, satisfaction fields); Event Monitoring configured (API callout events, login events); Data retention Apex batch job deployed (90-day bot logs, 12-month satisfaction data).

**Dependencies**: Phase 0 complete (API specs obtained, Meta approval timeline validated, Hyperforce Brazil confirmed).

**Risks**: G0103 (Meta WhatsApp Business approval 2-8 semanas — critical path blocker); G0104 (Hyperforce Brazil vs US-East data residency ambiguity — regulatory breach if wrong); G0102 (domínio personalizado SEFIN undefined — blocks WhatsApp approval); G0111 (MFA enforcement unclear — security audit finding); G0611 (TDE vs Shield legal interpretation — Shield adds ~30% license cost if required).

---

## Phase 2 — Einstein Bot + API Integration

**Epics**: E02 (Einstein Bot Conversational Flows), E03 (API Integration Layer), E04 (Feedback & Satisfaction Survey)

**Objectives**: Construir 4 Einstein Bot conversational flows (IPTU, TMRSU, ISS, Cadastral) + integrar 4 SEFIN APIs via Flow Orchestration + Apex + implementar satisfaction survey obrigatória.

**Success Criteria**: 4 Einstein Bot dialogs configurados (IPTU/TMRSU loop DAM, ISS link ou DAM per Q-04/Q-05, Cadastral 9-field edit); NLU model treinado com 50-100 utterances por intent; Slot filling + validation (CPF/CNPJ regex + Apex checksum); 4 Apex classes (REST callouts EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais) + retry logic (1x); Flow Orchestration (loop DAM emission multi-inscription P-29, validation, async invocation); Satisfaction survey integrado (1-5 stars + justificativa if ≤3) + API CRM SEFIN callout; Connectivity validation (ping/curl test Salesforce → SEFIN APIs pre-prod); Error logging via Event Log Files.

**Dependencies**: Phase 1 complete (ORG + WhatsApp Channel + Named Credentials + Security baseline).

**Risks**: G0202 (NLU training data ownership — SEFIN-CE provides or PS infers?); G0201 (ISS flow ambiguity — link only or DAM emission upgrade?); G0208 (WhatsApp 24h window vs session persistence >24h — HSM templates needed); G0217 (API EmitirDamUnico timeout >10s risk); G0301/G0302 (API specs CRM SEFIN + Dados Cadastrais incomplete — blocks Phase 2 start if Phase 0 failed); G0303 (connectivity IP validation ping/curl pre-prod required).

---

## Phase 3 — UX Research & Refinement

**Epics**: E05 (UX Research & Accessibility)

**Objectives**: Executar UX research (personas cidadãos PF/PJ, usability testing 3 fluxos, accessibility WCAG 2.1 AA conversational UI) + refinar bot flows baseado em findings para atingir SUS >70 e task completion >80%.

**Success Criteria**: 12 persona interviews completas (6 PF: 2 baixa/2 média/2 alta renda + 6 PJ: 2 MEI/2 pequena/2 média empresa) via Zoom remote; 2 persona docs gerados (PDF PT-BR, 1 PF + 1 PJ); 15 usability sessions executadas (3 fluxos IPTU/TMRSU/Cadastral × 5 usuários) via Zoom + working WhatsApp bot pre-production; Usability findings report (~5-10 pages) com task completion rate >80%, time on task <5 min, SUS score >70, error rate <15%; Accessibility report (~10-15 pages) WCAG 2.1 AA adapted conversational UI (plain language Flesch >60 PT-BR, screen reader VoiceOver+TalkBack testing); Bot flows refinados baseado em findings (NLU utterances expandidas, slot filling error messages ajustadas, satisfaction survey flow otimizado); LGPD consent forms for all participants (G0514).

**Dependencies**: Phase 2 complete (working WhatsApp bot pre-production para usability testing com cidadãos reais).

**Risks**: G0501 (UX research ownership — PS conducts or DATAPREV conducts with PS guidance?); G0507 (WCAG 2.1 AA não aplicável a conversational UI — W3C Conversational Accessibility Guidelines needed); G0514 (LGPD consent form for persona interviews + usability testing); G0509 (accessibility testing with PcD — expert review vs user testing unclear); Usability findings requerem refactor significativo bot flows (impacta timeline Phase 2 if major redesign needed).

---

## Phase 4 (ADD-ON) — Marketing Cloud Proactive Journey

**Epics**: E08 (Marketing Cloud Journey Builder)

**Objectives**: Setup Marketing Cloud Engagement + SFTP batch ingestion (SEFIN arquivo cidadãos IPTU vencido) + Journey Builder (1 jornada proativa régua D-15, D-5, D+1 reminders) + HSM templates Meta approval + opt-out mechanism.

**Success Criteria**: Marketing Cloud account provisionada (Core/Pro edition — G0801 validation needed) + WhatsApp connector configured (Meta Business API); SFTP batch ingestion configurada (Marketing Cloud Data Extension 1 fonte dados cidadãos IPTU vencido — arquivo SEFIN diário/semanal G0820 format/frequency defined); 1 segmentação configurada (sem Identity Resolution); Journey Builder (1 jornada proativa IPTU vencido régua ex: D-15, D-5, D+1 reminders — triggers/régua per Q-G/Q-H); 3-5 HSM templates design + Meta approval obtained (1-3 weeks timeline); Opt-out mechanism configured (reply STOP + Marketing Cloud attribute update); LGPD compliance validation (tax payment reminders = legitimate public interest? — G0809 legal validation Art. 7, IX); WhatsApp Business Account Tier 2+ upgrade if needed (13.5K msgs/day — G0808).

**Dependencies**: Phase 2 complete (WhatsApp Channel + Meta approval já obtidos para Service Cloud); SEFIN batch file format/frequency definido (G0820 — pode ser paralelo Phase 0-2 se SEFIN fornece specs cedo).

**Risks**: G0801 (Marketing Cloud edition undefined — Core/Pro/Premium? impacts licensing cost); G0809 (LGPD consent for proactive marketing — legal validation Art. 7, IX needed from SEFIN-CE DPO); G0808 (WhatsApp Business Account Tier 2+ required — 13.5K msgs/day; upgrade from Tier 1 if current account insufficient); G0820 (SEFIN batch file format/frequency undefined — daily/weekly? impacts data freshness D-1 or D-7); G0819 (HSM templates Meta approval timeline 1-3 weeks — critical path risk for Phase 4 go-live).

---

## Phase 5 (ADD-ON 3) — Transbordo Humano via Omni-Channel/Service Console

**Epics**: E09 (Transbordo Humano Omni-Channel)

**Objectives**: Provisionar Enhanced Omni-Channel (Presence Statuses, Routing Configuration, Service Channel para Messaging) + Service Console app para as 3 PAs (turno único) + ponto de transferência nos 4 fluxos do bot (E02) + Business Hours real + profile Agente Humano SEFIN (delta E06) + pesquisa de satisfação estendida ao fechamento humano (delta E04).

**Success Criteria**: Enhanced Omni-Channel configurado (Presence Statuses, Routing Configuration fila/skill-based); Service Console app ativo para as 3 PAs com painel de contexto SEFIN; ponto de transferência funcional nos 4 fluxos IPTU/TMRSU/ISS/Cadastral + fluxo de KB; Case/Messaging Session recebendo contexto da sessão do bot (CPF/CNPJ, serviço, transcript); Business Hours real configurado; profile Agente Humano SEFIN ativo; pesquisa de satisfação disparando também no fechamento humano.

**Dependencies**: Phase 1 completo (E01 — Digital Engagement + WhatsApp Channel provisionados); Phase 2 completo (E02 — 4 fluxos do bot existentes para os pontos de handoff). Pode correr em paralelo ao Phase 3 (UX Research) e Phase 4 (Marketing Cloud) — disciplinas diferentes.

**Risks**: Nenhum risco aberto — G0901 (Digital Engagement license, resolvido), G0902 (Enhanced Omni-Channel confirmado, resolvido 14/09/2026), G0903 (3 PAs turno único, resolvido), G0904 (Business Hours 08h-17h seg-sex, resolvido 16/09/2026).

---

## Standard Processes

**Testing**: Unit testing (Apex test coverage >75% per Salesforce requirement); integration testing (Salesforce → SEFIN APIs pre-prod connectivity validation ping/curl); UAT (SEFIN-CE users test 3 fluxos IPTU/TMRSU/Cadastral via working WhatsApp bot sandbox).

**Deployment**: Sandbox → Pre-Prod → Production; change sets ou Salesforce CLI metadata deployment; Hyperforce Brazil data residency validated at each stage; Meta WhatsApp Business approval finalized before Production deployment.

**Training**: DATAPREV assumes AMS pós-implantação (per discovery v2.0 decision); PS entrega documentação apenas — Admin Guide (ORG setup, Named Credentials, profiles, data retention batch job, Event Monitoring), Bot Maintenance Guide (NLU retraining, slot filling updates, Flow Orchestration adjustments, satisfaction survey configuration), API Integration Guide (4 Apex classes retry logic, connectivity troubleshooting, error logging Event Log Files), UX Refinement Guide (NLU utterances expansion, slot filling error messages, accessibility plain language Flesch >60 PT-BR).

---

## Consolidated Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **G0301/G0302 — API specs CRM SEFIN + Dados Cadastrais pending** | BLOCKER — blocks Phase 2 start | Phase 0 escalation SEFIN-CE + Alex Siqueira AP PS; fallback mock APIs for Phase 1 ORG setup parallel work |
| **G0103 — Meta WhatsApp Business approval 2-8 semanas** | Critical path blocker Phase 1 | Initiate Meta approval application during Phase 0 parallel; domínio personalizado SEFIN confirmed (G0102); Meta Business API team stakeholder communication |
| **G0104 — Hyperforce Brazil vs US-East data residency ambiguity** | Regulatory breach LGPD Art. 11 CPF/CNPJ sensitive data | Phase 0 escalation Salesforce Account Team + SEFIN-CE DPO; legal validation P-22 Hyperforce Brazil availability + data residency compliance |
| **G0501 — UX research ownership (PS conducts or DATAPREV conducts with PS guidance?)** | Phase 3 scope/effort ambiguity | Phase 0 stakeholder confirmation; if DATAPREV conducts, PS provides UX Research Protocol (persona interview script, usability testing scenarios, WCAG 2.1 AA conversational UI checklist, LGPD consent form template) |
| **G0809 — LGPD consent for proactive marketing (tax payment reminders = legitimate public interest?)** | Phase 4 ADD-ON legal compliance risk | SEFIN-CE DPO legal validation Art. 7, IX before Phase 4 kick-off; opt-out mechanism reply STOP + Marketing Cloud attribute update mandatory |
| **Usability findings require significant bot flow refactor** | Phase 3 findings impact Phase 2 timeline if major redesign needed | Phase 3 quick-turn iteration window (1-2 weeks) post-usability testing; prioritize critical findings (task completion <80%, SUS <70, error rate >15%) vs nice-to-have refinements |
