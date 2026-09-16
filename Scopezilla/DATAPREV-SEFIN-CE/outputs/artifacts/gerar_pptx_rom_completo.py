#!/usr/bin/env python3
"""
Gera PPTX ROM Completo DATAPREV-SEFIN-CE v2.0
Foco: Entregas, Escopo, Timeline, Roles, Investimento
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import json

# Cores Salesforce
SALESFORCE_BLUE = RGBColor(1, 118, 211)  # #0176D3
SALESFORCE_ORANGE = RGBColor(255, 158, 44)  # #FF9E2C
SALESFORCE_GREEN = RGBColor(4, 132, 75)  # #04844B
SALESFORCE_RED = RGBColor(234, 0, 30)  # #EA001E
SALESFORCE_DARK = RGBColor(8, 7, 7)  # #080707
SALESFORCE_GRAY = RGBColor(112, 110, 107)  # #706E6B

def add_title_slide(prs, title, subtitle):
    """Slide título"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Blue background bar
    left = top = Inches(0)
    width = prs.slide_width
    height = Inches(2.5)
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = SALESFORCE_BLUE
    shape.line.fill.background()

    # Title
    left = Inches(0.5)
    top = Inches(0.8)
    width = Inches(9)
    height = Inches(1)
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.text = title
    p = tf.paragraphs[0]
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)

    # Subtitle
    left = Inches(0.5)
    top = Inches(1.8)
    width = Inches(9)
    height = Inches(0.6)
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.text = subtitle
    p = tf.paragraphs[0]
    p.font.size = Pt(18)
    p.font.color.rgb = RGBColor(255, 255, 255)

    # Footer
    left = Inches(0.5)
    top = Inches(6.8)
    width = Inches(9)
    height = Inches(0.4)
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.text = "Salesforce Professional Services LATAM | ROM v2.0 | 2026"
    p = tf.paragraphs[0]
    p.font.size = Pt(12)
    p.font.color.rgb = SALESFORCE_GRAY

    return slide

def add_content_slide(prs, title, bullets):
    """Slide genérico com bullets"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Title
    left = Inches(0.5)
    top = Inches(0.3)
    width = Inches(9)
    height = Inches(0.8)
    title_box = slide.shapes.add_textbox(left, top, width, height)
    tf = title_box.text_frame
    tf.text = title
    p = tf.paragraphs[0]
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = SALESFORCE_BLUE

    # Content
    left = Inches(0.8)
    top = Inches(1.5)
    width = Inches(8.4)
    height = Inches(5)
    content_box = slide.shapes.add_textbox(left, top, width, height)
    tf = content_box.text_frame
    tf.word_wrap = True

    for i, bullet_text in enumerate(bullets):
        if i > 0:
            p = tf.add_paragraph()
        else:
            p = tf.paragraphs[0]

        p.text = bullet_text
        p.level = 0
        p.font.size = Pt(14)
        p.font.color.rgb = SALESFORCE_DARK
        p.space_before = Pt(6)
        p.space_after = Pt(6)

    return slide

def main():
    # Load data
    with open('data/commercials.json', 'r', encoding='utf-8') as f:
        commercials = json.load(f)

    with open('data/roadmap.json', 'r', encoding='utf-8') as f:
        roadmap = json.load(f)

    with open('data/resource-plan.json', 'r', encoding='utf-8') as f:
        resources = json.load(f)

    with open('data/epics.json', 'r', encoding='utf-8') as f:
        epics = json.load(f)

    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1: Título
    add_title_slide(
        prs,
        "DATAPREV-SEFIN-CE",
        "ROM v2.0 — Investimento Professional Services + Timeline + Roles"
    )

    # Slide 2: Resumo Executivo ROM
    rom_low = commercials['indicative_range']['low']
    rom_high = commercials['indicative_range']['high']
    duration = commercials['effort_basis']['duration_weeks_range']
    team = commercials['effort_basis']['team_size_range']

    exec_bullets = [
        f"💰 ROM INVESTIMENTO PS: R$ {rom_low:,.0f} – R$ {rom_high:,.0f} BRL (com impostos)",
        "",
        f"📅 TIMELINE: {duration} semanas | {team} pessoas (pico 2 arquitetos + 2 desenvolvedores)",
        "",
        "🎯 ESCOPO BASE (CORE): Service Cloud ORG Setup + Einstein Bot 4 fluxos conversacionais WhatsApp + 4 APIs SEFIN + UX Research + Security LGPD",
        "",
        "➕ ADD-ONs (investimento separado): E08 Marketing Cloud Jornada Proativa + E07 Knowledge Base Vectorization",
        "",
        "⚠️ PREMISSAS CRÍTICAS: Licenças Salesforce não incluídas (cliente contrata direto); Meta WhatsApp approval 2-8 semanas (critical path); 2 API specs BLOCKER (CRM SEFIN + Dados Cadastrais)"
    ]
    add_content_slide(prs, "Resumo Executivo — ROM v2.0", exec_bullets)

    # Slide 3: Escopo BASE vs ADD-ONs
    escopo_bullets = [
        "ESCOPO BASE (CORE) — 6 Épicas:",
        "• E01 — Salesforce ORG Foundation + WhatsApp Channel (Hyperforce Brazil, Meta approval)",
        "• E02 — Einstein Bot 4 Fluxos (IPTU, TMRSU, ISS, Alteração Cadastral) + NLU 5 intents",
        "• E03 — API Integration Layer (4 APIs SEFIN: EmitirDamUnico, ConsultaImovel, CRM, Dados Cadastrais)",
        "• E04 — Feedback & Satisfaction Tracking (1-5 estrelas obrigatória, log API CRM SEFIN)",
        "• E05 — UX Research & Accessibility (12 personas, 15 usability sessions, WCAG 2.1 AA)",
        "• E06 — Security Model LGPD (2 perfis: 3 Admin + 7 Bot Maintainer, TDE encryption, audit)",
        "• E09 — Transbordo Humano via Omni-Channel/Service Console (ADD-ON aprovado, incorporado ao ROM base)",
        "",
        "ADD-ONs (Investimento e Escopo Separados):",
        "• E08 — Marketing Cloud Proactive Journey (4,86M msgs/ano, régua D-15/D-5/D+1, SFTP batch)",
        "• E07 — Knowledge Base Vectorization Data Cloud (base externa → bot responde dúvidas)",
        "",
        "❌ FORA DE ESCOPO: Case Management completo, Contact/Account Management completo, treinamento administradores"
    ]
    add_content_slide(prs, "Escopo — BASE vs ADD-ONs", escopo_bullets)

    # Slide 4: Timeline — 6 Fases
    timeline_bullets = [
        f"TIMELINE: {duration} semanas | 6 Fases (Phase 0 a 5)",
        "",
        "Phase 0 — Discovery Resolution & API Specs",
        "Resolver 133 gaps, obter 2 API specs BLOCKER (CRM SEFIN + Dados Cadastrais), validar Meta approval timeline, confirmar Hyperforce Brazil",
        "",
        "Phase 1 — Foundation & ORG Setup (E01, E06)",
        "Provisionar Hyperforce Brazil ORG + WhatsApp Channel + Named Credentials 4 APIs + Security LGPD baseline",
        "",
        "Phase 2 — Einstein Bot + API Integration (E02, E03, E04)",
        "4 Einstein Bot flows + NLU training + 4 Apex REST callouts + Flow Orchestration + Satisfaction survey",
        "",
        "Phase 3 — UX Research & Refinement (E05)",
        "12 persona interviews (6 PF + 6 PJ) + 15 usability sessions + accessibility WCAG 2.1 AA + bot refinement",
        "",
        "Phase 4 — Marketing Cloud Proactive Journey ADD-ON (E08)",
        "Setup MC + SFTP batch ingestion + Journey Builder régua proativa + HSM templates Meta approval + opt-out",
        "",
        "Phase 5 — Transbordo Humano via Omni-Channel/Service Console ADD-ON (E09)",
        "Enhanced Omni-Channel + Service Console para 3 PAs (turno único) + Business Hours 08h-17h seg-sex + pesquisa de satisfação estendida ao fechamento humano. Depende de Phase 1+2, roda em paralelo às Phases 3/4. Incorporado ao ROM base."
    ]
    add_content_slide(prs, "Timeline — 6 Fases", timeline_bullets)

    # Slide 5: Roles & Disciplinas
    roles_bullets = [
        "6 DISCIPLINAS (multi-disciplinar — 1 pessoa pode exercer múltiplos papéis):",
        "",
        "R01 + R05 — Technical Architect (Phases 0-4)",
        "Solution architecture ownership, Hyperforce Brazil decisão, Einstein Bot NLU design, integration patterns Flow+Apex+4 APIs, LGPD compliance TDE encryption, MC zero-copy batch, UX accessibility conversational UI, Phase 0 gap resolution orchestration",
        "",
        "R02 — Technical Consultant (Phases 1, 2, 4)",
        "Build E01 ORG Foundation + E02 Einstein Bot 4 flows + E03 Apex 4 APIs + E04 satisfaction survey + E08 ADD-ON MC Journey Builder",
        "",
        "R03 — Technical Consultant Security + Profiles (Phases 1, 2)",
        "E06 Security — custom profiles (Admin + Bot Maintainer), Field History, Event Monitoring, data retention batch, Named Credentials FLS hidden",
        "",
        "R04 — Experience Architect (Phase 3)",
        "E05 UX Research — 12 persona interviews, 15 usability sessions, accessibility report WCAG 2.1 AA conversational UI, bot refinement, LGPD consent forms",
        "",
        "R06 — Project Manager (Phases 0-4)",
        "Delivery orchestration, Phase 0 gap resolution 133 gaps + 17 perguntas, Meta approval critical path management, stakeholder communication (Alex Siqueira + Oswaldo Melo + SEFIN-CE DPO + Meta)"
    ]
    add_content_slide(prs, "Roles & Disciplinas — 6 Papéis", roles_bullets)

    # Slide 6: Investimento BASE (PS)
    invest_bullets = [
        f"INVESTIMENTO PROFESSIONAL SERVICES — ESCOPO BASE (6 épicas CORE):",
        "",
        f"💰 ROM: R$ {rom_low:,.0f} – R$ {rom_high:,.0f} BRL (com impostos 75,35%)",
        "",
        f"📅 PRAZO: {duration} semanas",
        "",
        f"👥 EQUIPE: {team} pessoas (pico: 2 arquitetos + 2 desenvolvedores)",
        "",
        "📊 COMPOSIÇÃO TAXAS DIÁRIAS (BRL com impostos):",
        f"• Onshore Architect: R$ {commercials['rates'][0]['rate']:,.2f}/dia",
        f"• Onshore Developer: R$ {commercials['rates'][1]['rate']:,.2f}/dia",
        "• Offshore: não aplicável (0 offshore neste projeto)",
        "",
        "⚠️ DISCLAIMER: ROM indicativo baseado em bill rates validadas pelo cliente em 2026-07-03. Não inclui licenças Salesforce (cliente contrata diretamente). Estimativa top-down engagement-level — não é preço fixo nem FTE commitment."
    ]
    add_content_slide(prs, "Investimento BASE — Professional Services", invest_bullets)

    # Slide 7: Licenças Salesforce (referência)
    lic_bullets = [
        "LICENÇAS SALESFORCE (Cliente contrata diretamente — não incluídas no ROM PS):",
        "",
        "SERVICE CLOUD + EINSTEIN BOT:",
        "• 10 usuários Service Cloud (3 System Admin + 7 Bot Maintainer customizado)",
        "• Einstein Bot add-on (400k conversas/ano)",
        "• WhatsApp Channel connector",
        "• Hyperforce Brazil ORG (data residency LGPD)",
        "",
        "MARKETING CLOUD ADD-ON (Opcional — E08):",
        "• Marketing Cloud Engagement (Core ou Pro edition — validar com cliente G0801)",
        "• WhatsApp for Marketing Cloud connector",
        "• Volume: 4,86M msgs WhatsApp/ano (~405k/mês)",
        "",
        "DATA CLOUD ADD-ON (Opcional — E07 KB Vectorization):",
        "• Data Cloud licenses (zero-copy + vector embedding)",
        "• Volume KB a definir com cliente",
        "",
        "📌 OBSERVAÇÃO: Valores licenças não fazem parte deste ROM. Cliente negocia diretamente com Account Executive Salesforce (Alex Siqueira). Investimento PS acima é exclusivamente Professional Services."
    ]
    add_content_slide(prs, "Licenças Salesforce — Referência", lic_bullets)

    # Slide 8: ADD-ON E08 Marketing Cloud
    mc_bullets = [
        "ADD-ON E08 — Marketing Cloud Proactive Journey (Investimento Separado):",
        "",
        "ESCOPO:",
        "• Setup Marketing Cloud Engagement (Core/Pro edition)",
        "• SFTP batch ingestion (SEFIN arquivo cidadãos IPTU vencido diário/semanal)",
        "• 1 Data Extension (1 fonte dados zero-copy)",
        "• 1 segmentação (sem Identity Resolution)",
        "• Journey Builder: 1 jornada proativa régua (ex: D-15, D-5, D+1 reminders IPTU vencido)",
        "• 3-5 HSM templates design + Meta approval (1-3 semanas)",
        "• Opt-out mechanism (reply STOP + MC attribute update)",
        "• LGPD compliance validation (tax reminders = legitimate public interest Art. 7 IX)",
        "• WhatsApp Business Account Tier 2+ upgrade se necessário (13,5K msgs/dia)",
        "",
        "VOLUME: 4,86M msgs WhatsApp/ano (~405k/mês, ~13,5k/dia)",
        "",
        "TIMELINE: Phase 4 (após Phase 2 complete — WhatsApp Channel + Meta approval já obtidos)",
        "",
        "INVESTIMENTO: A DEFINIR (estimativa separada — não incluído no ROM BASE acima)"
    ]
    add_content_slide(prs, "ADD-ON E08 — Marketing Cloud Journey", mc_bullets)

    # Slide 9: ADD-ON E07 Knowledge Base
    kb_bullets = [
        "ADD-ON E07 — Knowledge Base Vectorization Data Cloud (Investimento Separado):",
        "",
        "ESCOPO:",
        "• Ingestão base de conhecimento externa Salesforce → Data Cloud",
        "• Vetorização Data Cloud (vector embedding)",
        "• Einstein Bot responde dúvidas via KB (substitui redirecionamento site SEFIN)",
        "• Integração Einstein Bot + Data Cloud RAG (Retrieval-Augmented Generation)",
        "",
        "PREMISSAS:",
        "• Volume KB a confirmar com cliente (Q-F discovery anterior)",
        "• Formato KB a definir (PDF, HTML, structured data?)",
        "• Fonte KB: SEFIN-CE fornece ou PS extrai de site público?",
        "• Manutenção KB: SEFIN-CE atualiza ou PS assume operação?",
        "",
        "DEPENDÊNCIAS:",
        "• Data Cloud licenses (cliente contrata)",
        "• Base conhecimento SEFIN disponível e estruturada",
        "",
        "TIMELINE: Pode ser paralelo Phase 2-3 se KB disponível cedo",
        "",
        "INVESTIMENTO: A DEFINIR (estimativa separada — não incluído no ROM BASE acima)",
        "",
        "STATUS: Confidence UNKNOWN — aguardando confirmação cliente se KB existe e qual volume"
    ]
    add_content_slide(prs, "ADD-ON E07 — Knowledge Base Vectorization", kb_bullets)

    # Slide 10: Riscos & Dependências Críticas
    risks_bullets = [
        "RISCOS & DEPENDÊNCIAS CRÍTICAS:",
        "",
        "🔴 BLOCKERS Phase 0:",
        "• G0301: API CRM SEFIN spec (endpoint/payload/auth) — Q-01 BLOCKER",
        "• G0302: API Dados Cadastrais spec (endpoint/payload/auth) — Q-02 BLOCKER",
        "• G0103: Meta WhatsApp Business approval 2-8 semanas — CRITICAL PATH",
        "• P-22: Hyperforce Brazil vs US-East data residency decisão — LGPD compliance",
        "",
        "🟠 RISCOS Phase 1-2:",
        "• G0202: NLU training data ownership (SEFIN fornece ou PS infers?)",
        "• G0201: ISS flow ambiguity (link site ou DAM emission upgrade Q-04/Q-05)",
        "• G0303: Conectividade IP Salesforce → SEFIN APIs (ping/curl pre-prod validation)",
        "• G0208: WhatsApp 24h window vs session persistence >24h (HSM templates needed)",
        "",
        "🟡 RISCOS Phase 3:",
        "• G0501: UX research ownership (PS conducts ou DATAPREV with PS guidance?)",
        "• G0507: WCAG 2.1 AA não aplicável a conversational UI (W3C guidelines adaptation)",
        "• G0514: LGPD consent forms persona interviews + usability testing",
        "",
        "🟢 RISCOS Phase 4 ADD-ON:",
        "• G0801: Marketing Cloud edition undefined (Core/Pro impacts licensing cost)",
        "• G0809: LGPD consent proactive marketing (legal validation Art. 7 IX SEFIN-CE DPO)",
        "• G0820: SEFIN batch file format/frequency undefined (daily/weekly impacts freshness)"
    ]
    add_content_slide(prs, "Riscos & Dependências — Critical Path", risks_bullets)

    # Slide 11: Próximos Passos
    next_bullets = [
        "PRÓXIMOS PASSOS:",
        "",
        "1️⃣ VALIDAÇÃO ROM (Cliente DATAPREV + SEFIN-CE):",
        f"   • Aprovar investimento PS ESCOPO BASE R$ {rom_low:,.0f} – R$ {rom_high:,.0f} BRL (inclui E09 incorporado)",
        f"   • Aprovar timeline {duration} semanas",
        "   • Confirmar se ADD-ONs E07/E08 entram no escopo (estimativa separada)",
        "",
        "2️⃣ PHASE 0 — Discovery Resolution (Target <3 semanas):",
        "   • Responder 17 perguntas cliente (Q-01 a Q-17)",
        "   • Obter 2 API specs BLOCKER (CRM SEFIN + Dados Cadastrais endpoint/payload/auth)",
        "   • Validar Meta WhatsApp Business approval status (já obtida ou timeline para obter)",
        "   • Confirmar Hyperforce Brazil data residency (vs US-East)",
        "   • Definir ISS flow decisão (link site ou DAM emission)",
        "",
        "3️⃣ CONTRATAÇÃO LICENÇAS SALESFORCE (Cliente contrata diretamente):",
        "   • Service Cloud 10 usuários + Einstein Bot 400k conversas/ano + WhatsApp Channel",
        "   • Se ADD-ON E08: Marketing Cloud Engagement Core/Pro edition",
        "   • Se ADD-ON E07: Data Cloud licenses",
        "",
        "4️⃣ KICK-OFF Phase 1 (Após Phase 0 complete):",
        "   • Provisionar Hyperforce Brazil ORG",
        "   • Iniciar aprovação Meta WhatsApp Business (2-8 semanas critical path)"
    ]
    add_content_slide(prs, "Próximos Passos — Validação & Kick-off", next_bullets)

    # Save
    output_path = 'DATAPREV_SEFIN_CE_ROM_Completo_v2.pptx'
    prs.save(output_path)
    print(f"✅ PPTX ROM Completo gerado: {output_path}")
    print(f"   {len(prs.slides)} slides criados")
    print(f"   ROM: R$ {rom_low:,.0f} – R$ {rom_high:,.0f} BRL")
    print(f"   Timeline: {duration} semanas | {team} pessoas")

if __name__ == '__main__':
    main()
