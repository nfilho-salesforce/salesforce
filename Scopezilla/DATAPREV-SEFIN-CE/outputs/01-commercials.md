# Commercials — DATAPREV-SEFIN-CE

## Approved Commercials

**Indicative Professional Services Range (Traditional Lane)**:  
**R$ 1.781.136 – R$ 4.882.236 BRL**

*(Revisado 2026-09-14 para incorporar E09 — Transbordo Humano via Omni-Channel/Service Console, ADD-ON 3. Range anterior sem E09: R$ 1.583.232 – R$ 4.231.269 BRL.)*

---

### Effort Basis

**Duration**: 18–30 weeks (benchmark-derived from Service Cloud Medium complexity base 12–18 weeks + 35–45% risk adders + 2–4 weeks incrementais para E09 ADD-ON 3)

**Risk Adders Applied**:
- **New client (no prior org access)**: +10–15% — Greenfield Hyperforce Brazil ORG, SEFIN-CE sem histórico Salesforce
- **Highly regulated (LGPD Art. 11 sensitive data)**: +15–20% — CPF/CNPJ como dado sensível, Hyperforce Brazil data residency validation (P-22), TDE encryption mandatory, Field History Tracking, Event Monitoring
- **Compressed timeline risk (Meta approval 2–8 semanas critical path G0103)**: +10% — Phase 1 bloqueada por Meta WhatsApp Business approval, ISS flow decision ambiguity (Q-04/Q-05), 2 API specs bloqueadoras (G0301/G0302)
- **Total risk adder**: +35–45%

**Capacity** (engagement-level, top-down from resource plan):
- **Onshore-architect**: 2–3 people (Technical Architect phases 0–4, Experience Architect phase 3, Project Manager phases 0–4)
- **Onshore-developer**: 1–2 people (Technical Consultant phases 1,2,4 + Technical Consultant Security+Profiles phases 1,2)
- **Offshore**: 0 people (delivery 100% onshore Brasil DATAPREV)
- **Team size range**: 3–5 people

---

### Arithmetic

ROM indicativo calculado como:

**Σ over classes of (validated bill rate × class capacity) × duration**

**Architect component**:
- Low: R$ 7.032,56/dia × 2 people × 18 weeks × 5 days/week = R$ 1.265.861
- High: R$ 7.032,56/dia × 3 people × 30 weeks × 5 days/week = R$ 3.164.652

**Developer component**:
- Low: R$ 5.725,28/dia × 1 person × 18 weeks × 5 days/week = R$ 515.275
- High: R$ 5.725,28/dia × 2 people × 30 weeks × 5 days/week = R$ 1.717.584

**Total**: R$ 1.781.136 (low) – R$ 4.882.236 (high)

---

### Bill Rates Used (Validated 2026-07-03)

| Class | Daily Rate (BRL) | Hourly Rate (BRL) | Source |
|-------|-----------------|-------------------|--------|
| Onshore-architect | R$ 7.032,56 | R$ 879,07 | DATAPREV tabela COM IMPOSTO — Technical Architect rate (8h/dia) |
| Onshore-developer | R$ 5.725,28 | R$ 715,66 | DATAPREV tabela COM IMPOSTO — Technical Consultant rate (8h/dia) |
| Offshore | R$ 0 | R$ 0 | Delivery 100% onshore Brasil |

---

### Validated-Rate Disclaimer

**This indicative range is derived from bill rates you supplied and validated on 2026-07-03, multiplied by a top-down engagement-level effort basis (duration 18–30 weeks × capacity 2–3 architects + 1–2 developers).** It is not a fixed-fee quote, not a cost estimate (margin is out of scope), and not a bottoms-up hours sum. The range reflects the engagement shape (8 epics: 2L + 5M + 1S core/ADD-ON mix, 1L + 1M ADD-ON) and the risk profile (new client, LGPD regulated, Meta approval critical path). Duration is benchmark-derived from model-training-data (Service Cloud Medium complexity parametric row + risk adders + E09 ADD-ON 3 increment); carry the Benchmark Disclaimer wherever the duration appears. Travel, expenses, and third-party costs (e.g., Salesforce licenses, Meta WhatsApp Business API fees) are billed as actual and not included in this range.

---

## Scope Summary

**6 CORE Epics + 2 ADD-ONs**:
- **E01** (ORG Foundation & WhatsApp Channel) — M
- **E02** (Einstein Bot Conversational Flows) — L: 4 flows (IPTU, TMRSU, ISS, Cadastral) + NLU training 50–100 utterances + slot filling + validation
- **E03** (API Integration Layer) — M: 4 SEFIN APIs (EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais) via Flow Orchestration + Apex REST callouts + retry logic + connectivity validation
- **E04** (Feedback & Satisfaction Survey) — S: satisfaction survey 1–5 stars + justificativa if ≤3 + API CRM SEFIN callout
- **E05** (UX Research & Accessibility) — M: 12 persona interviews + 15 usability sessions + 2 reports (usability ~5–10 pages, accessibility ~10–15 pages WCAG 2.1 AA adapted conversational UI) + bot flows refinados
- **E06** (Security & Profiles) — M: LGPD compliance baseline (TDE encryption, Field History Tracking, Event Monitoring) + custom profiles (System Admin clone, Bot Maintainer scoped Einstein Bot + conversation review) + data retention Apex batch job (90-day bot logs, 12-month satisfaction)
- **E08 (ADD-ON)** (Marketing Cloud Proactive Journey) — L: Marketing Cloud Engagement + SFTP batch ingestion (SEFIN arquivo cidadãos IPTU vencido) + Journey Builder 1 jornada proativa (régua ex: D-15, D-5, D+1 reminders) + 3–5 HSM templates Meta approval + opt-out mechanism
- **E09 (ADD-ON 3)** (Transbordo Humano via Omni-Channel/Service Console) — M: Enhanced Omni-Channel + Service Console app para 3 PAs (turno único) + handoff de contexto nos 4 fluxos do bot + Business Hours real + profile Agente Humano SEFIN + pesquisa de satisfação estendida ao fechamento humano. Licenciamento Digital Engagement e headcount já confirmados pelo cliente — sem bloqueadoras.

**Phase 0 Mandatory**: 137 gaps resolution + 17 perguntas cliente (Q-01 a Q-17) + 2 API specs bloqueadoras (G0301/G0302 CRM SEFIN + Dados Cadastrais) before Phase 1 kick-off.

**Critical Path**: Phase 1 Meta WhatsApp Business approval (G0103 2–8 semanas); Phase 4 ADD-ON HSM templates Meta approval (G0819 1–3 semanas); Phase 5 ADD-ON (E09) depende de Phase 1 (E01) + Phase 2 (E02), pode correr em paralelo aos Phases 3/4.

---

## Assumptions

1. **Duration**: 18–30 weeks benchmark-derived (Service Cloud Medium + risk adders + 2–4 weeks incrementais para E09 ADD-ON 3). This is decision-support, not a commitment — the user chose "sequence only, no commitment" in roadmap. For a committed timeline, the user must validate this range or specify an alternative.
2. **Phase 0 duration**: Not priced separately — included in the 18–30 week range. Phase 0 depends on SEFIN-CE responsiveness (target <3 semanas per risk mitigation).
3. **UX research ownership (G0501)**: ROM assumes PS conducts UX research (12 persona interviews + 15 usability sessions + 2 reports). If DATAPREV conducts with PS guidance, effort reduces (Experience Architect role shifts to UX Research Protocol delivery only).
4. **Meta WhatsApp Business approval (G0103)**: ROM assumes 2–8 semanas timeline. If >8 semanas, Phase 1 critical path impacted (duration high-end increases).
5. **Hyperforce Brazil data residency (P-22)**: ROM assumes Hyperforce Brazil available and validated for LGPD Art. 11 CPF/CNPJ sensitive data compliance. If only US-East available, legal risk escalation SEFIN-CE DPO required Phase 0 (may add governance effort).
6. **Marketing Cloud edition (G0801)**: Phase 4 ADD-ON ROM assumes Core or Pro edition. If Premium required, licensing cost impact (~30–50% increase) and additional Marketing Cloud Consultant discipline may be needed (increases developer capacity high-end).
7. **API specs bloqueadoras (G0301/G0302)**: ROM assumes CRM SEFIN + Dados Cadastrais API specs obtained during Phase 0. If specs incomplete/ambiguous or unavailable, Phase 2 blocked (duration high-end increases, or mock APIs fallback adds rework risk).

---

## Out of Scope

- **Salesforce licenses**: Einstein Bot Conversations (400.000 conversations/year), Service Cloud user licenses, Marketing Cloud Engagement (Phase 4 ADD-ON), WhatsApp Business API fees (Meta), Hyperforce Brazil data residency premium (if any) — billed as actual by Salesforce.
- **Meta WhatsApp Business API fees**: Conversation-based pricing (inbound + outbound messages) + HSM templates submission fees — billed as actual by Meta.
- **SEFIN-CE responsibilities**: Fornecimento API specs bloqueadoras (CRM SEFIN + Dados Cadastrais endpoint/payload/auth G0301/G0302), resposta 17 perguntas cliente (Q-01 a Q-17), domínio personalizado SEFIN para Meta WhatsApp Business approval (G0102), arquivo diário/semanal cidadãos IPTU vencido for Marketing Cloud SFTP batch ingestion (G0820 format/frequency definition).
- **AMS (Application Managed Services)**: DATAPREV assumes AMS pós-implantação per discovery v2.0 decision. PS entrega documentação apenas (Admin Guide, Bot Maintenance Guide, API Integration Guide, UX Refinement Guide).
- **Training**: DATAPREV assumes training delivery. PS provides documentation only.
- **Travel & expenses**: Billed as actual if required (e.g., on-site UX research sessions if Zoom remote not feasible per G0505).
