#!/usr/bin/env python3
"""
Gera PPTX resumo DATAPREV-SEFIN-CE v2.0
Estilo Salesforce padrão
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import json
import os

# Cores Salesforce
SALESFORCE_BLUE = RGBColor(1, 118, 211)  # #0176D3
SALESFORCE_ORANGE = RGBColor(255, 158, 44)  # #FF9E2C
SALESFORCE_GREEN = RGBColor(4, 132, 75)  # #04844B
SALESFORCE_RED = RGBColor(234, 0, 30)  # #EA001E
SALESFORCE_DARK = RGBColor(8, 7, 7)  # #080707
SALESFORCE_GRAY = RGBColor(112, 110, 107)  # #706E6B

def add_title_slide(prs, title, subtitle):
    """Slide 1: Título"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

    # Background blue bar
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
    tf.text = "Salesforce Professional Services LATAM | 2026"
    p = tf.paragraphs[0]
    p.font.size = Pt(12)
    p.font.color.rgb = SALESFORCE_GRAY

    return slide

def add_content_slide(prs, title, bullets):
    """Slide genérico com título e bullets"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

    # Title bar
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

    # Content area
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

def add_image_slide(prs, title, image_path):
    """Slide com imagem"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

    # Title
    left = Inches(0.5)
    top = Inches(0.3)
    width = Inches(9)
    height = Inches(0.6)
    title_box = slide.shapes.add_textbox(left, top, width, height)
    tf = title_box.text_frame
    tf.text = title
    p = tf.paragraphs[0]
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = SALESFORCE_BLUE

    # Image (centered, scaled to fit)
    left = Inches(1.5)
    top = Inches(1.2)
    height = Inches(5.5)
    slide.shapes.add_picture(image_path, left, top, height=height)

    return slide

def main():
    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Load data
    with open('data/commercials.json', 'r', encoding='utf-8') as f:
        commercials = json.load(f)

    # Slide 1: Título
    add_title_slide(
        prs,
        "DATAPREV-SEFIN-CE",
        "Service Cloud + Einstein Bot + WhatsApp Channel | Tributos Municipais Fortaleza"
    )

    # Slide 2: Resumo do Projeto
    resumo_bullets = [
        "🎯 OBJETIVO: Substituir fornecedor MUTANTE (R$ 1,7M/ano) por Service Cloud + Einstein Bot para autoatendimento tributos municipais via WhatsApp",
        "",
        "📊 ESCOPO: 4 fluxos conversacionais (IPTU, TMRSU, ISS, Alteração Cadastral) + 400k conversas/ano",
        "",
        "💰 ROM INDICATIVO: R$ 1.583.232 – R$ 4.231.269 | 16-26 semanas | 2-3 arquitetos + 1-2 desenvolvedores",
        "",
        "🏛️ SECRETARIA: SEFIN Fortaleza (Secretaria da Fazenda Municipal)",
        "",
        "⚠️ BLOCKERS: 2 specs API (CRM SEFIN Q-01, Dados Cadastrais Q-02) + Meta WhatsApp approval 2-8 semanas (critical path)"
    ]
    add_content_slide(prs, "Resumo Executivo — Visão Geral", resumo_bullets)

    # Slide 3: Capacidades Salesforce (parte 1)
    cap1_bullets = [
        "SERVICE CLOUD",
        "Plataforma base para gestão atendimento cidadão — Case Management, Contact Management, omnichannel routing (WhatsApp + transbordo humano futuro)",
        "",
        "EINSTEIN BOT",
        "4 fluxos conversacionais linguagem natural (IPTU, TMRSU, ISS, Cadastral) — NLU 5 intents, slot filling (CPF/CNPJ regex + Apex checksum), loop DAM multi-inscrição, pesquisa satisfação 1-5 estrelas",
        "",
        "WHATSAPP CHANNEL",
        "Integração nativa Meta Business API — 24h messaging window, HSM templates session resume, aprovação Meta 2-8 semanas (G0103 BLOCKER)"
    ]
    add_content_slide(prs, "Capacidades Salesforce — Parte 1", cap1_bullets)

    # Slide 4: Capacidades Salesforce (parte 2)
    cap2_bullets = [
        "FLOW ORCHESTRATION + APEX",
        "4 REST APIs SEFIN (EmitirDamUnico, ConsultaImovel, CRM SEFIN, Dados Cadastrais) — Named Credentials API Key auth, retry logic 1x, connectivity validation IP whitelist",
        "",
        "LGPD COMPLIANCE",
        "Hyperforce Brazil ORG (data residency São Paulo), TDE encryption at-rest, Field History Tracking (CPF/CNPJ), Event Monitoring (API callouts), Data retention Apex batch (90d bot logs, 12m satisfaction)",
        "",
        "MARKETING CLOUD (ADD-ON)",
        "Journey Builder jornada proativa IPTU vencido (régua D-15, D-5, D+1) — SFTP batch ingestion SEFIN arquivo diário/semanal, 4,86M msgs/ano, opt-out mechanism (LGPD)"
    ]
    add_content_slide(prs, "Capacidades Salesforce — Parte 2", cap2_bullets)

    # Slide 5: Fluxo do Bot (imagem)
    if os.path.exists('SEFIN_CE_Bot_Tree.png'):
        add_image_slide(prs, "Árvore de Conversação — Einstein Bot", 'SEFIN_CE_Bot_Tree.png')

    # Slide 6: Transcrição do Fluxo (parte 1)
    flow1_bullets = [
        "1. ENTRADA: Cidadão inicia conversa WhatsApp → Menu Inicial (5 opções: IPTU, TMRSU, ISS, Cadastral, Outros)",
        "",
        "2. IDENTIFICAÇÃO: CPF (PF) ou CNPJ (PJ) com validação regex + Apex checksum",
        "",
        "3. FLUXO IPTU: ConsultaImovel API → Lista inscrições (loop multi-inscrição P-29) → Escolhe tipo débito (Total/Cota/Parcela) → EmitirDamUnico API → Envia PDF WhatsApp",
        "",
        "4. FLUXO TMRSU: ConsultaImovel API → Lista inscrições (loop) → EmitirDamUnico API (tipoDebito=980) → Envia PDF WhatsApp"
    ]
    add_content_slide(prs, "Transcrição do Fluxo — Parte 1", flow1_bullets)

    # Slide 7: Transcrição do Fluxo (parte 2)
    flow2_bullets = [
        "5. FLUXO ISS: Envia link Portal SEFIN para emissão Nota Fiscal (Q-04/Q-05: upgrade para DAM emission?)",
        "",
        "6. FLUXO CADASTRAL: Dados Cadastrais API (Q-02 BLOCKER) → Exibe 9 campos editáveis (Nome, Email, Telefone, Endereço...) → Validação formato/regex → Salva alterações PUT/PATCH → Confirmação",
        "",
        "7. PESQUISA SATISFAÇÃO: Obrigatória 1-5 estrelas + justificativa se ≤3 → Log API CRM SEFIN (Q-01 BLOCKER) Fire-and-Forget",
        "",
        "8. DESPEDIDA: Link Portal SEFIN (Q-06) + opção nova consulta (loop ao menu)"
    ]
    add_content_slide(prs, "Transcrição do Fluxo — Parte 2", flow2_bullets)

    # Slide 8: Premissas (parte 1 - Fluxo e Experiência)
    premissas1_bullets = [
        "FLUXO E EXPERIÊNCIA (P-01 a P-07):",
        "• P-01: Todo encerramento = Pesquisa satisfação → API CRM SEFIN → Despedida com link Portal",
        "• P-02: Sem transbordo humano — bot encerra automaticamente com link Portal SEFIN",
        "• P-03: Pesquisa satisfação em todos os fluxos (IPTU, TMRSU, ISS, Alteração Cadastral)",
        "• P-04: Notas ≤3 estrelas → bot coleta justificativa antes de encerrar",
        "• P-05: Máximo 2 tentativas digitação inválida em qualquer campo, depois encerra",
        "• P-06: Usuário já identificado na sessão → pula identificação e vai direto ao Menu",
        "• P-07: Sem horário de atendimento — bot disponível 24/7"
    ]
    add_content_slide(prs, "Premissas — Parte 1", premissas1_bullets)

    # Slide 9: Premissas (parte 2 - Alteração Cadastral)
    premissas2_bullets = [
        "ALTERAÇÃO CADASTRAL (P-08 a P-11):",
        "• P-08: Campos: CPF/CNPJ (não editável), nome, telefone, email, endereço completo",
        "• P-09: Endereço completo: logradouro, número, complemento, bairro, CEP, cidade, estado",
        "• P-10: CPF/CNPJ é chave única — não pode ser alterado pelo cidadão",
        "• P-11: Sem validação automática CEP/telefone/email na v1.0 (a confirmar)",
        "",
        "APIS E INTEGRAÇÕES (P-12 a P-17):",
        "• P-12: API EmitirDamUnico e ConsultaImovel já existem e prontas para consumo",
        "• P-13: API CRM SEFIN (log satisfação) será entregue pelo cliente — REST + API Key",
        "• P-14: API Dados Cadastrais será entregue pelo cliente — REST + API Key",
        "• P-15: ISS continua apenas link do site (sem emissão DAM) — a confirmar",
        "• P-16: Falha API = 1 retentativa → se falhar informa 'tente novamente' → encerra",
        "• P-17: Cliente possui conectividade IP entre Service Cloud e APIs SEFIN (sem MuleSoft)"
    ]
    add_content_slide(prs, "Premissas — Parte 2", premissas2_bullets)

    # Slide 10: Premissas (parte 3 - Infraestrutura e Escopo)
    premissas3_bullets = [
        "INFRAESTRUTURA E SEGURANÇA (P-18 a P-23):",
        "• P-18: Nova ORG Salesforce from scratch (não há ORG existente)",
        "• P-19: LGPD obrigatória — CPF/CNPJ são dados pessoais sensíveis (Art. 11)",
        "• P-20: Contratação canal WhatsApp Business é com Meta/Facebook, não Salesforce",
        "• P-21: Licitação pública via Lei 14.133/2021 (Nova Lei de Licitações)",
        "• P-22: Residência de dados: região Salesforce geograficamente aprovada (conforme DATAPREV)",
        "• P-23: DATAPREV já possui aprovação CTID para uso Service Cloud",
        "",
        "ESCOPO E ENTREGA (P-24 a P-30):",
        "• P-24: Salesforce PS não fornece licenças — cliente contrata diretamente",
        "• P-25: Service Cloud AS-IS: Einstein Bot + WhatsApp (sem Case Management/Console)",
        "• P-26: 10 usuários: 3 System Admin + 7 perfil customizado (bot maintainer)",
        "• P-27: Treinamento de administradores não incluído no escopo core",
        "• P-28: DATAPREV assume sustentação (AMS) pós-implantação",
        "• P-29: Loop emissão DAM se repete para todas as inscrições selecionadas",
        "• P-30: Sem limite de inscrições — bot apresenta todas retornadas pela API"
    ]
    add_content_slide(prs, "Premissas — Parte 3", premissas3_bullets)

    # Slide 11: Perguntas ao Cliente (parte 1 - APIs)
    q1_bullets = [
        "APIS E INTEGRAÇÕES (Q-01 a Q-05):",
        "• Q-01: API CRM SEFIN (log satisfação): endpoint, payload exato, headers, autenticação?",
        "• Q-02: API Dados Cadastrais: endpoint, payload exato, headers, autenticação?",
        "• Q-03: Validação campos: deve validar CEP (ViaCEP)? Telefone? Email? Ou apenas salva?",
        "• Q-04: ISS: continua apenas link do site ou muda para emissão DAM (como IPTU/TMRSU)?",
        "• Q-05: Se ISS mudar para emissão DAM: qual tipoDebito usar na API EmitirDamUnico?"
    ]
    add_content_slide(prs, "Perguntas ao Cliente — Parte 1", q1_bullets)

    # Slide 12: Perguntas ao Cliente (parte 2 - Experiência)
    q2_bullets = [
        "EXPERIÊNCIA DO USUÁRIO (Q-06 a Q-08):",
        "• Q-06: Qual é a URL do Portal SEFIN para link de despedida?",
        "• Q-07: Mensagem de despedida padrão: tem texto preferencial ou deixamos genérico?",
        "• Q-08: Cidadão pode solicitar opt-out de mensagens proativas (ADD-ON Marketing Cloud)?",
        "",
        "DADOS E VOLUME (Q-09 a Q-10):",
        "• Q-09: MUTANTE entrega dados históricos de volume/uso para sizing mais preciso?",
        "• Q-10: Base contribuintes SEFIN com CPF/CNPJ válido e atualizado para Marketing Cloud?"
    ]
    add_content_slide(prs, "Perguntas ao Cliente — Parte 2", q2_bullets)

    # Slide 13: Perguntas ao Cliente (parte 3 - Timeline e Usuários)
    q3_bullets = [
        "TIMELINE E CONTRATO (Q-11 a Q-14):",
        "• Q-11: Qual a data de vencimento do contrato MUTANTE?",
        "• Q-12: Deadline desejado para go-live?",
        "• Q-13: Número do processo licitatório?",
        "• Q-14: Há janela de manutenção ou blackout para evitar (ex: período arrecadação IPTU)?",
        "",
        "USUÁRIOS E PERFIS (Q-15 a Q-16):",
        "• Q-15: Perfil customizado 'Bot Maintainer': precisa permissões além de Einstein Bot + revisão conversas?",
        "• Q-16: Usuários revisam conversas via Service Cloud Console ou via relatório/dashboard?"
    ]
    add_content_slide(prs, "Perguntas ao Cliente — Parte 3", q3_bullets)

    # Save
    output_path = 'DATAPREV_SEFIN_CE_Resumo_v3.pptx'
    prs.save(output_path)
    print(f"✅ PPTX gerado: {output_path}")
    print(f"   {len(prs.slides)} slides criados")
    print(f"   - 30 premissas completas (P-01 a P-30)")
    print(f"   - 16 perguntas completas (Q-01 a Q-16)")

if __name__ == '__main__':
    main()
