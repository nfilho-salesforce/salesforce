# Roles & Skills — Disciplines Required

This document identifies the disciplines this engagement requires. One person may fill multiple roles; one role may be filled by multiple people. Team sizing, FTE counts, and staffing are not within this artifact's scope — those require human judgment based on Salesforce PS's capacity, delivery model, and commercial terms.

---

## Executive Summary

This engagement requires expertise across six disciplines: **Technical Architect** (solution architecture ownership Phase 0 gap resolution + Phases 1-4 technical decisions), **Technical Consultant** (build Bot + Integration + Marketing Cloud ADD-ON), **Technical Consultant (Security + Profiles)** (LGPD compliance baseline + custom profiles), **Experience Architect** (UX research + accessibility WCAG 2.1 AA conversational UI), **Technical Architect** (Phase 0 orchestration gap resolution + API specs bloqueadoras), and **Project Manager** (cross-phase delivery orchestration). Phase 0 is critical — 133 gaps, 17 perguntas cliente, 2 API specs bloqueadoras (G0301/G0302) must resolve before Phase 1 kick-off. Phase 1 Meta WhatsApp Business approval (G0103 2-8 semanas) is critical path. Phase 3 requires working WhatsApp bot pre-production for usability testing with cidadãos reais.

---

## Disciplines by Phase

| Discipline | Phases Active | Rationale |
|-----------|---------------|-----------|
| **Technical Architect** | 0, 1, 2, 3, 4 | Solution architecture ownership across all phases — Hyperforce Brazil vs US-East decisão, Einstein Bot NLU design, integration patterns (Flow Orchestration + Apex + 4 SEFIN APIs), LGPD compliance + TDE encryption baseline, Marketing Cloud zero-copy batch ingestion pattern, HSM templates Meta approval orchestration, UX accessibility adaptado conversational UI |
| **Technical Consultant** | 1, 2, 4 | Build E01 (ORG Foundation + WhatsApp Channel + Named Credentials), E02 (4 Einstein Bot flows — IPTU/TMRSU loop DAM, ISS link ou DAM, Cadastral 9-field edit + NLU training 50-100 utterances + slot filling + validation), E03 (4 Apex REST callouts + Flow Orchestration loop multi-inscription P-29 + retry logic + connectivity validation ping/curl), E04 (satisfaction survey 1-5 stars + API CRM SEFIN callout), E08 ADD-ON (Marketing Cloud SFTP batch ingestion + Journey Builder 1 jornada proativa + HSM templates design) |
| **Technical Consultant (Security + Profiles)** | 1, 2 | E06 (Security & Profiles) — custom profiles (System Admin clone + Bot Maintainer scoped Einstein Bot + conversation review), Field History Tracking (CPF/CNPJ, satisfaction), Event Monitoring (API callout + login events), data retention Apex batch job (90-day bot logs, 12-month satisfaction), Named Credentials API Keys FLS Bot Maintainer hidden |
| **Experience Architect** | 3 | E05 (UX Research & Accessibility) — 12 persona interviews (6 PF: 2 baixa/2 média/2 alta renda + 6 PJ: 2 MEI/2 pequena/2 média empresa) via Zoom remote, 2 persona docs (PDF PT-BR), 15 usability sessions (3 fluxos IPTU/TMRSU/Cadastral × 5 usuários) via Zoom + working WhatsApp bot pre-production, usability findings report (~5-10 pages) task completion >80% + time on task <5min + SUS >70 + error rate <15%, accessibility report (~10-15 pages) WCAG 2.1 AA adapted conversational UI (plain language Flesch >60 PT-BR, screen reader VoiceOver+TalkBack testing), bot flows refinados baseado em findings, LGPD consent forms all participants (G0514) |
| **Technical Architect** | 0 | Phase 0 gap resolution orchestration — coordenar respostas SEFIN-CE 17 perguntas (Q-01 a Q-17), obter API specs bloqueadoras (CRM SEFIN + Dados Cadastrais endpoint/payload/auth — G0301/G0302), validar Meta WhatsApp Business approval timeline, definir ISS flow decisão (link ou DAM emission Q-04/Q-05), confirmar Hyperforce Brazil data residency (P-22), negociar Bot Maintainer permissions (Q-15), documentar decisões arquiteturais |
| **Project Manager** | 0, 1, 2, 3, 4 | Cross-phase delivery orchestration — Phase 0 gap resolution coordination (133 gaps, 17 perguntas cliente, 2 API specs bloqueadoras), sequencing Phase 1 Meta approval critical path (G0103 2-8 semanas), Phase 2 dependency management (working WhatsApp bot pre-production required for Phase 3 UX testing), Phase 4 ADD-ON HSM templates Meta approval timeline (G0819 1-3 semanas critical path), stakeholder communication (Alex Siqueira AP PS + Oswaldo Melo SE + SEFIN-CE DPO + Meta Business API team) |

---

## Assumptions

- **Phase 0 is mandatory** — 133 gaps, 17 perguntas cliente, 2 API specs bloqueadoras (G0301/G0302 CRM SEFIN + Dados Cadastrais) must resolve before Phase 1 kick-off. Phase 0 duration depends on SEFIN-CE responsiveness (target <3 semanas per risk mitigation).
- **UX research ownership (G0501)** — assumes PS conducts UX research (12 persona interviews + 15 usability sessions + 2 reports). If DATAPREV conducts with PS guidance, Experience Architect role shifts to UX Research Protocol delivery (interview script, testing scenarios, WCAG checklist, LGPD consent form template).
- **Bot Maintainer profile scope (Q-15)** — assumes Bot Maintainer profile is scoped to Einstein Bot configuration + conversation review only (no System Admin permissions, no Named Credentials access per FLS hidden). Phase 0 validates with SEFIN-CE.
- **Marketing Cloud edition (G0801)** — Phase 4 ADD-ON assumes Core or Pro edition. If Premium required, licensing cost impact (~30-50% increase) and additional Marketing Cloud Consultant discipline may be needed for advanced Journey Builder features.
- **Meta WhatsApp Business approval (G0103)** — assumes 2-8 semanas timeline. If >8 semanas, Phase 1 critical path impacted. Mitigation: initiate Meta approval application during Phase 0 parallel work; domínio personalizado SEFIN confirmed (G0102).
- **Hyperforce Brazil data residency (P-22)** — assumes Hyperforce Brazil available and validated for LGPD Art. 11 CPF/CNPJ sensitive data compliance. If only US-East available, legal risk escalation SEFIN-CE DPO required Phase 0.

---

## Risks

- **Phase 0 duration >3 semanas** — SEFIN-CE delays responding to 17 perguntas or API specs bloqueadoras incomplete/ambiguous. Mitigation: Alex Siqueira AP PS escalation; parallel Phase 1 ORG setup work with mock APIs fallback.
- **G0501 UX research ownership ambiguity** — if DATAPREV conducts UX research, PS role reduces to protocol delivery (lower effort, but usability findings quality risk if DATAPREV lacks UX expertise). Mitigation: Phase 0 stakeholder confirmation + PS UX Research Protocol template delivery.
- **G0507 WCAG 2.1 AA não aplicável a conversational UI** — W3C Conversational Accessibility Guidelines (not yet WCAG formal standard) may be required. Experience Architect expertise adaptation needed. Mitigation: Phase 3 accessibility report documents plain language Flesch >60 PT-BR + screen reader VoiceOver+TalkBack testing as conversational UI proxy for WCAG 2.1 AA.
- **Phase 3 findings require significant bot flow refactor** — usability testing reveals task completion <80%, SUS <70, error rate >15% requiring major Einstein Bot NLU + Flow Orchestration redesign. Mitigation: Phase 3 quick-turn iteration window (1-2 weeks) prioritizing critical findings vs nice-to-have refinements.
- **Phase 4 ADD-ON HSM templates Meta approval timeline (G0819 1-3 semanas)** — critical path risk for Phase 4 go-live if HSM templates rejected or require multiple iterations. Mitigation: Phase 4 HSM templates design aligned with Meta Business API content policy + SEFIN-CE branding guidelines early validation.
