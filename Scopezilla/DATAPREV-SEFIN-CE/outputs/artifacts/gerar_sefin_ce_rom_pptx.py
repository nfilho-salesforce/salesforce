#!/usr/bin/env python3
"""
Gera PPTX DATAPREV-SEFIN-CE ROM v2.0
Conteúdo completo do site Heroku para apresentação executiva
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

def create_title_slide(prs, title, subtitle):
    """Cria slide de título"""
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle
    return slide

def create_section_slide(prs, title):
    """Cria slide de seção (divisória)"""
    slide = prs.slides.add_slide(prs.slide_layouts[2])
    slide.shapes.title.text = title
    return slide

def create_content_slide(prs, title):
    """Cria slide de conteúdo com título"""
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    return slide

def add_text_box(slide, left, top, width, height, text, font_size=14, bold=False):
    """Adiciona caixa de texto"""
    textbox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    text_frame = textbox.text_frame
    text_frame.word_wrap = True
    p = text_frame.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    return textbox

def add_bullet_points(slide, left, top, width, height, bullets, font_size=14):
    """Adiciona bullet points"""
    textbox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    for i, bullet in enumerate(bullets):
        if i > 0:
            p = text_frame.add_paragraph()
        else:
            p = text_frame.paragraphs[0]
        p.text = bullet
        p.level = 0
        p.font.size = Pt(font_size)

    return textbox

def add_table(slide, left, top, width, height, rows, cols):
    """Adiciona tabela"""
    table = slide.shapes.add_table(rows, cols, Inches(left), Inches(top), Inches(width), Inches(height)).table
    return table

def main():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1 - Capa
    slide = create_title_slide(prs,
        "DATAPREV-SEFIN-CE v2.0",
        "Einstein Bot WhatsApp Agentforce\nROM Professional Services\n\nJulho 2026")

    # Slide 2 - Contexto e Objetivo
    slide = create_content_slide(prs, "Contexto e Objetivo")
    bullets = [
        "Cliente: DATAPREV prestando serviços para SEFIN-CE (Secretaria da Fazenda do Ceará)",
        "Sistema Atual (MUTANTE): Atendimento presencial + telefone | 200K+ cidadãos/ano",
        "Objetivo: Automatizar 90% do atendimento cidadão com Einstein Bot via WhatsApp",
        "Fluxos: 4 bot flows (IPTU, TMRSU, ISS, Alteração Cadastral)",
        "Benefícios: Redução 60-70% custo operacional | Atendimento 24/7 | <3 min tempo médio"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 16)

    # Slide 3 - Tributos em Escopo
    slide = create_content_slide(prs, "Tributos em Escopo")
    table = add_table(slide, 0.5, 1.5, 9, 4, 5, 3)

    # Headers
    table.cell(0, 0).text = "Tributo"
    table.cell(0, 1).text = "Descrição"
    table.cell(0, 2).text = "Status"

    # Rows
    table.cell(1, 0).text = "IPTU"
    table.cell(1, 1).text = "Imposto Predial e Territorial Urbano (2ª via DAM)"
    table.cell(1, 2).text = "CORE"

    table.cell(2, 0).text = "TMRSU"
    table.cell(2, 1).text = "Taxa Municipal Resíduos Sólidos Urbanos (2ª via DAM)"
    table.cell(2, 2).text = "CORE"

    table.cell(3, 0).text = "ISS"
    table.cell(3, 1).text = "Imposto Sobre Serviços (link Portal SEFIN)"
    table.cell(3, 2).text = "CORE"

    table.cell(4, 0).text = "Cadastral"
    table.cell(4, 1).text = "Alteração dados cadastrais (9 campos)"
    table.cell(4, 2).text = "CORE"

    # Slide 4 - Tecnologia Salesforce
    slide = create_content_slide(prs, "Tecnologia Salesforce")
    bullets = [
        "Service Cloud Enterprise (10 users: 3 System Admin + 7 Bot Maintainer)",
        "Einstein Bot (400K conversas/ano, NLU 5 intents, 4 fluxos)",
        "WhatsApp Business API (contrato Meta/Facebook — approval 2-8 semanas)",
        "Hyperforce Brazil (São Paulo — LGPD Art. 11 compliance)",
        "4 APIs REST SEFIN (ConsultaImovel, EmitirDamUnico, CRM SEFIN, Dados Cadastrais)"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 16)

    # Slide 5 - Escopo e Entregáveis
    slide = create_content_slide(prs, "Escopo e Entregáveis")
    bullets = [
        "E01 — Fundação e Setup Service Cloud + WhatsApp Channel",
        "E02 — Fluxo Alteração Cadastral (9 campos editáveis)",
        "E03 — Fluxos Tributos (IPTU, TMRSU, ISS link)",
        "E04 — Feedback & Satisfaction Tracking",
        "E05 — UX Research (12 personas + 15 usability sessions)",
        "E06 — Segurança LGPD (TDE, Event Monitoring, 2 perfis customizados)",
        "",
        "ADD-ON E08 — Marketing Cloud Jornadas Proativas (4,86M msgs/ano)"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 14)

    # Slide 6 - Macro Atividades (Timeline)
    slide = create_content_slide(prs, "Macro Atividades — 5 Fases")
    table = add_table(slide, 0.5, 1.5, 9, 4.5, 6, 4)

    # Headers
    table.cell(0, 0).text = "Fase"
    table.cell(0, 1).text = "Duração"
    table.cell(0, 2).text = "Pessoas"
    table.cell(0, 3).text = "% ROM"

    # Rows
    table.cell(1, 0).text = "Phase 0 — Discovery Resolution"
    table.cell(1, 1).text = "<3 semanas"
    table.cell(1, 2).text = "1-2"
    table.cell(1, 3).text = "~8-12%"

    table.cell(2, 0).text = "Phase 1 — Foundation & ORG Setup"
    table.cell(2, 1).text = "4 semanas"
    table.cell(2, 2).text = "3-4"
    table.cell(2, 3).text = "~18-22%"

    table.cell(3, 0).text = "Phase 2 — Einstein Bot + API Integration"
    table.cell(3, 1).text = "8 semanas"
    table.cell(3, 2).text = "5-6"
    table.cell(3, 3).text = "~45-50%"

    table.cell(4, 0).text = "Phase 3 — UX Research & Refinement"
    table.cell(4, 1).text = "4 semanas"
    table.cell(4, 2).text = "3-4"
    table.cell(4, 3).text = "~15-18%"

    table.cell(5, 0).text = "Phase 4 — Marketing Cloud ADD-ON"
    table.cell(5, 1).text = "6 semanas"
    table.cell(5, 2).text = "2-3"
    table.cell(5, 3).text = "Separado"

    # Slide 7 - Premissas Chave (Top 10)
    slide = create_content_slide(prs, "Premissas Chave (Top 10 de 30)")
    bullets = [
        "P-02: Sem transbordo humano — bot encerra automaticamente com link Portal",
        "P-07: Sem horário de atendimento — bot disponível 24/7",
        "P-13: API CRM SEFIN será entregue pelo cliente (Q-01 BLOCKER)",
        "P-14: API Dados Cadastrais será entregue pelo cliente (Q-02 BLOCKER)",
        "P-15: ISS continua apenas link do site (Q-04/Q-05 decisão)",
        "P-17: Cliente possui conectividade IP Service Cloud ↔ APIs SEFIN",
        "P-22: Hyperforce Brazil (BLOCKER decisão DATAPREV CTID — LGPD)",
        "P-24: Salesforce PS não fornece licenças — cliente contrata direto",
        "P-25: Service Cloud AS-IS — sem Case Management/Omnichannel",
        "P-29: Loop emissão DAM se repete para todas inscrições selecionadas"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 13)

    # Slide 8 - Perguntas em Aberto (Resumo)
    slide = create_content_slide(prs, "Perguntas em Aberto — 16 Perguntas")
    bullets = [
        "BLOCKERS (2):",
        "  • Q-01: API CRM SEFIN spec (endpoint, payload, autenticação)",
        "  • Q-02: API Dados Cadastrais spec (endpoint, payload, autenticação)",
        "",
        "HIGH (5):",
        "  • Q-04: ISS continua link ou muda para emissão DAM?",
        "  • Q-10: Base contribuintes CPF/CNPJ válido para Marketing Cloud?",
        "  • Q-11: Data vencimento contrato MUTANTE?",
        "  • Q-12: Deadline desejado go-live?",
        "  • Q-15: Perfil Bot Maintainer precisa permissões além de Einstein Bot?",
        "",
        "MEDIUM/LOW (9): Validações técnicas, UX, timeline"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 14)

    # Slide 9 - Riscos (Top BLOCKERs)
    slide = create_content_slide(prs, "Riscos — 4 BLOCKERs + 8 High/Medium")
    bullets = [
        "🔴 BLOCKERS Phase 0:",
        "  • G0301: API CRM SEFIN spec indefinida → Phase 2 blocked",
        "  • G0302: API Dados Cadastrais spec indefinida → Phase 2 blocked",
        "  • G0103: Meta WhatsApp approval 2-8 semanas (critical path)",
        "  • P-22: Hyperforce Brazil vs US-East decisão DATAPREV CTID",
        "",
        "🟠 HIGH (5): NLU training ownership, ISS flow ambiguity, IP conectividade, WhatsApp 24h window, Bot Maintainer profile scope",
        "",
        "🟡 MEDIUM (3): UX research ownership, WCAG 2.1 AA conversational UI, LGPD consent forms"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 14)

    # Slide 10 - Timeline
    slide = create_content_slide(prs, "Timeline — 16-26 Semanas")
    bullets = [
        "ROM Duration Range: 16-26 semanas (3-5 pessoas pico)",
        "Critical Path: Meta WhatsApp Business approval 2-8 semanas + Phase 0 <3 semanas",
        "",
        "Mínimo 16 semanas: Cenário ideal (nenhum gap impactante, APIs prontas, ISS link only)",
        "Máximo 26 semanas: Cenário conservador (P0 longa, ISS upgrade DAM, UX extenso)",
        "",
        "Sequência:",
        "  • Phase 0: <3 semanas (gap resolution BLOCKER)",
        "  • Phase 1: 4 semanas (foundation + ORG setup)",
        "  • Phase 2: 8 semanas (bot build + API integration)",
        "  • Phase 3: 4 semanas (UX research + refinement)",
        "  • Phase 4: 6 semanas (Marketing Cloud ADD-ON opcional)"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 14)

    # Slide 11 - Investimento PS (ROM)
    slide = create_content_slide(prs, "Investimento PS — ROM Indicativa")
    add_text_box(slide, 0.5, 1.5, 9, 0.8,
                 "R$ 1.583.232 – R$ 4.231.269 BRL (com impostos)",
                 font_size=24, bold=True)

    bullets = [
        "Base: 16-26 semanas × 3-5 pessoas × taxa diária validada PS",
        "Tier: ROM indicativa — não é custo nem fee fixo",
        "",
        "Capacidade (per class):",
        "  • Onshore Architect: 1 pessoa (full-time)",
        "  • Onshore Developer: 2-3 pessoas (build team)",
        "  • Offshore: 1-2 pessoas (support roles)",
        "",
        "Premissas ROM:",
        "  • Phase 0 <3 semanas — se gaps demorarem mais, ROM aumenta",
        "  • ISS continua link only — se mudar para DAM emission, ROM +5-8%",
        "  • ADD-ON Marketing Cloud Phase 4 é investimento separado"
    ]
    add_bullet_points(slide, 0.5, 2.5, 9, 4, bullets, 13)

    # Slide 12 - Investimento Licenças CORE
    slide = create_content_slide(prs, "Investimento Licenças — CORE")
    table = add_table(slide, 0.5, 1.5, 9, 3, 4, 3)

    # Headers
    table.cell(0, 0).text = "Componente"
    table.cell(0, 1).text = "Quantidade"
    table.cell(0, 2).text = "Investimento Anual (USD)"

    # Rows
    table.cell(1, 0).text = "Service Cloud Enterprise"
    table.cell(1, 1).text = "10 users"
    table.cell(1, 2).text = "USD 18.000"

    table.cell(2, 0).text = "Einstein Bot Conversations"
    table.cell(2, 1).text = "400K conversas/ano"
    table.cell(2, 2).text = "USD 160.000"

    table.cell(3, 0).text = "WhatsApp Business API (Meta)"
    table.cell(3, 1).text = "2M msgs/ano"
    table.cell(3, 2).text = "USD 140.000 – 240.000"

    add_text_box(slide, 0.5, 5, 9, 0.5,
                 "TOTAL CORE (Year 1): USD 318.000 – 418.000",
                 font_size=18, bold=True)

    # Slide 13 - Investimento Licenças ADD-ONs
    slide = create_content_slide(prs, "Investimento Licenças — ADD-ONs (Opcional)")
    table = add_table(slide, 0.5, 1.5, 9, 2.5, 3, 3)

    # Headers
    table.cell(0, 0).text = "Componente"
    table.cell(0, 1).text = "Quantidade"
    table.cell(0, 2).text = "Investimento Anual (USD)"

    # Rows
    table.cell(1, 0).text = "Marketing Cloud + WhatsApp overage"
    table.cell(1, 1).text = "4,86M msgs/ano"
    table.cell(1, 2).text = "USD 403.800"

    table.cell(2, 0).text = "Data Cloud (se profile 360 necessário)"
    table.cell(2, 1).text = "400K profiles"
    table.cell(2, 2).text = "USD 156.000"

    add_text_box(slide, 0.5, 4.5, 9, 0.5,
                 "TOTAL CORE + ADD-ONs (Year 1): USD 877.800 – 977.800",
                 font_size=18, bold=True)

    # Slide 14 - Arquitetura Alto Nível
    slide = create_content_slide(prs, "Arquitetura em Alto Nível — 6 Camadas")
    bullets = [
        "Layer 1 — Presentation: WhatsApp Business API + Einstein Bot (4 fluxos)",
        "Layer 2 — Orchestration: Bot Dialogs + Flow + NLU (5 intents) + Session Mgmt",
        "Layer 3 — Integration: Apex REST Callouts + Named Credentials (4 APIs)",
        "Layer 4 — APIs SEFIN: Tributos, Emissão DAM, CRM, Cadastral (external)",
        "Layer 5 — Security & Compliance: Hyperforce Brazil + TDE + Event Monitoring + 2 perfis LGPD",
        "Layer 6 — ADD-ONs: Marketing Cloud (MCAE) + Journey Builder + Data Cloud (opcional)",
        "",
        "Decisões técnicas chave:",
        "  • Service Cloud AS-IS (sem Case Management) — bot 100% self-service",
        "  • Apex REST (não MuleSoft) — 4 APIs simples, conectividade IP cliente",
        "  • 24/7 atendimento — bot sem horário comercial (P-07)"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 12)

    # Slide 15 - Próximos Passos
    slide = create_content_slide(prs, "Próximos Passos — Phase 0 Discovery Resolution")
    bullets = [
        "🔴 CRÍTICO (<3 semanas):",
        "  • Obter 2 API specs BLOCKER (G0301 CRM SEFIN, G0302 Dados Cadastrais)",
        "  • Responder 17 perguntas cliente (Q-01 a Q-17, 2 BLOCKERs)",
        "  • Validar Meta WhatsApp Business approval status (2-8 semanas G0103)",
        "  • Confirmar Hyperforce Brazil data residency (P-22 DATAPREV CTID)",
        "  • Definir ISS flow decisão: link do site ou DAM emission (Q-04/Q-05)",
        "",
        "Sem Phase 0 completa:",
        "  • Phase 1 Foundation não pode iniciar (133 gaps bloqueadores)",
        "  • ROM pode aumentar 10-20% se gaps demorarem >3 semanas",
        "",
        "Meta: Phase 0 completa antes de kick-off oficial"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 14)

    # Slide 16 - Disclaimer ROM
    slide = create_content_slide(prs, "Disclaimer ROM")
    bullets = [
        "ROM (Rough Order of Magnitude) indicativa, baseada em:",
        "  • Taxa diária validada × engagement shape top-down",
        "  • Duração 16-26 semanas × capacidade 3-5 pessoas",
        "",
        "Não é custo interno, não é fee fixo, não é proposta de preço.",
        "",
        "Range R$ 1.583.232 – R$ 4.231.269 BRL reflete incerteza:",
        "  • Phase 0 (133 gaps a resolver)",
        "  • Meta approval 2-8 semanas critical path",
        "  • ISS flow ambiguity (Q-04/Q-05)",
        "  • UX research ownership (G0501)",
        "",
        "Para transformar ROM em proposta comercial formal:",
        "  • Resolver BLOCKERs Phase 0",
        "  • Confirmar Meta approval timeline",
        "  • Definir ISS flow + validar UX ownership"
    ]
    add_bullet_points(slide, 0.5, 1.5, 9, 5, bullets, 13)

    # Salvar
    output_path = "DATAPREV_SEFIN_CE_ROM_v2.0.pptx"
    prs.save(output_path)
    print(f"✓ PPTX gerado: {output_path}")
    print(f"  • 16 slides completos")
    print(f"  • Conteúdo do site Heroku formatado para apresentação")
    print(f"  • ROM R$ 1.583.232 – R$ 4.231.269 BRL")
    print(f"  • Licenças USD 318K–978K/ano")

if __name__ == '__main__':
    main()
