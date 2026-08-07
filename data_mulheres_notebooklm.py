from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT = "/Users/nfilho/claude/DATA_MULHERES_NotebookLM.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2.5*cm,
    bottomMargin=2*cm,
    title="DATA MULHERES — Base de Conhecimento do Projeto",
    author="Salesforce Professional Services LATAM"
)

styles = getSampleStyleSheet()

# Custom styles
sf_blue = colors.HexColor("#0070D2")
sf_dark = colors.HexColor("#032D60")
sf_light = colors.HexColor("#F3F3F3")
sf_orange = colors.HexColor("#FF6900")
sf_green = colors.HexColor("#2E844A")
sf_red = colors.HexColor("#BA0517")
sf_yellow = colors.HexColor("#FFC928")

title_style = ParagraphStyle("title", parent=styles["Title"],
    fontSize=22, textColor=sf_dark, spaceAfter=6, alignment=TA_CENTER, fontName="Helvetica-Bold")

subtitle_style = ParagraphStyle("subtitle", parent=styles["Normal"],
    fontSize=11, textColor=sf_blue, spaceAfter=16, alignment=TA_CENTER, fontName="Helvetica")

h1_style = ParagraphStyle("h1", parent=styles["Heading1"],
    fontSize=14, textColor=colors.white, spaceAfter=6, spaceBefore=14,
    fontName="Helvetica-Bold", backColor=sf_dark,
    leftIndent=-0.5*cm, rightIndent=-0.5*cm, borderPad=6)

h2_style = ParagraphStyle("h2", parent=styles["Heading2"],
    fontSize=12, textColor=sf_dark, spaceAfter=4, spaceBefore=10,
    fontName="Helvetica-Bold", borderPad=2)

h3_style = ParagraphStyle("h3", parent=styles["Heading3"],
    fontSize=10, textColor=sf_blue, spaceAfter=3, spaceBefore=6,
    fontName="Helvetica-BoldOblique")

body_style = ParagraphStyle("body", parent=styles["Normal"],
    fontSize=9.5, spaceAfter=4, spaceBefore=2, leading=14,
    fontName="Helvetica", alignment=TA_JUSTIFY)

bullet_style = ParagraphStyle("bullet", parent=styles["Normal"],
    fontSize=9.5, spaceAfter=3, spaceBefore=1, leading=13,
    leftIndent=14, fontName="Helvetica", bulletIndent=4)

bold_style = ParagraphStyle("bold", parent=styles["Normal"],
    fontSize=9.5, spaceAfter=3, fontName="Helvetica-Bold")

note_style = ParagraphStyle("note", parent=styles["Normal"],
    fontSize=8.5, textColor=colors.HexColor("#444444"), spaceAfter=3,
    fontName="Helvetica-Oblique", leftIndent=8, borderPad=4,
    backColor=colors.HexColor("#FFF8E1"))

def h1(text): return Paragraph(f"&nbsp;&nbsp;{text}", h1_style)
def h2(text): return Paragraph(text, h2_style)
def h3(text): return Paragraph(text, h3_style)
def body(text): return Paragraph(text, body_style)
def bullet(text): return Paragraph(f"• &nbsp;{text}", bullet_style)
def note(text): return Paragraph(f"ℹ️  {text}", note_style)
def sp(n=1): return Spacer(1, n*0.3*cm)
def hr(): return HRFlowable(width="100%", thickness=0.5, color=sf_blue, spaceAfter=6, spaceBefore=6)

def table(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F0F4FF")]),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
    ]
    if header:
        style += [
            ("BACKGROUND", (0,0), (-1,0), sf_dark),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,0), 9.5),
        ]
    t.setStyle(TableStyle(style))
    return t

def badge(text, color):
    return Paragraph(
        f'<font color="{color.hexval()}" size="10"><b>{text}</b></font>', body_style)

# ─── BUILD STORY ────────────────────────────────────────────────────────────
story = []

# CAPA
story += [
    sp(2),
    Paragraph("SALESFORCE PROFESSIONAL SERVICES LATAM", ParagraphStyle("cap",
        parent=styles["Normal"], fontSize=10, textColor=sf_blue,
        alignment=TA_CENTER, fontName="Helvetica-Bold")),
    sp(1),
    Paragraph("DATA MULHERES", ParagraphStyle("maintitle",
        parent=styles["Title"], fontSize=28, textColor=sf_dark,
        alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("Base de Conhecimento do Projeto", ParagraphStyle("sub",
        parent=styles["Normal"], fontSize=14, textColor=sf_blue,
        alignment=TA_CENTER, fontName="Helvetica")),
    sp(1),
    HRFlowable(width="60%", thickness=2, color=sf_orange, spaceAfter=12, spaceBefore=6),
    Paragraph("Observatório Brasil de Igualdade de Gênero", ParagraphStyle("s2",
        parent=styles["Normal"], fontSize=12, textColor=colors.HexColor("#444444"),
        alignment=TA_CENTER, fontName="Helvetica-Oblique")),
    Paragraph("Dataprev × Ministério das Mulheres × Salesforce / Tableau", ParagraphStyle("s3",
        parent=styles["Normal"], fontSize=10, textColor=colors.HexColor("#666666"),
        alignment=TA_CENTER, fontName="Helvetica")),
    sp(2),
    table([
        ["Status", "🟠 Discovery completo — ROM gerado — Proposta/OS em montagem"],
        ["Versão do documento", "1.0 — Gerado em 28/05/2026"],
        ["Destinatário", "Time de Delivery Salesforce PS LATAM"],
        ["Canal Slack", "#dataprev-datamulheres-dashes-mule"],
    ], [4*cm, 12.5*cm], header=False),
    sp(3),
]

# ─── 1. CONTEXTO ESTRATÉGICO ────────────────────────────────────────────────
story += [
    h1("1. CONTEXTO ESTRATÉGICO"),
    sp(),
    h2("1.1 Visão Geral"),
    body("O projeto DATA MULHERES tem como objetivo a criação de um painel público de Business Intelligence conectado à Plataforma DataMulheres, que integra o Observatório Brasil de Igualdade de Gênero. O painel será disponibilizado publicamente para consulta de indicadores sociais relacionados à igualdade de gênero no Brasil, com granularidade até o nível municipal."),
    sp(),
    h2("1.2 Partes Envolvidas"),
    table([
        ["Organização", "Papel", "Ponto de Contato"],
        ["Dataprev (DTP)", "Cliente contratante / Operador de dados", "Adriana (ponto focal);\nMilena Micheli e Lidiane Costa (dados)"],
        ["Ministério das Mulheres", "Demandante final / Stakeholder político", "Ministra (patrocinadora)"],
        ["Salesforce PS LATAM", "Delivery lead / Presales", "Nelson (presales),\nClaudio Salas (delivery lead),\nJuliana Brites (PS ops),\nLuciano (PM candidato)"],
        ["Salesforce Tableau", "Account Executive / Licenciamento", "Viviani Hupp (AE Tableau)"],
        ["Parceiro PTB", "Execução técnica Tableau (a definir)", "Rejane (identificação do parceiro)"],
    ], [3.5*cm, 5*cm, 8*cm]),
    sp(),
    note("Restrição contratual — Cláusula 14 do contrato DTP: PM e Arquiteto Tableau devem obrigatoriamente ser recursos PTB (parceiro homologado pela Dataprev). Recursos PS internos podem atuar como PM e UX/UI Designer, mas precisam ser validados frente à cláusula."),
    sp(),
]

# ─── 2. ESCOPO TÉCNICO ──────────────────────────────────────────────────────
story += [
    h1("2. ESCOPO TÉCNICO"),
    sp(),
    h2("2.1 Arquitetura da Solução"),
    body("A solução adota Tableau Server On-Premise como plataforma de visualização, obedecendo ao requisito de soberania de dados da Dataprev — que impede a utilização de soluções cloud para armazenamento ou processamento de dados governamentais. A única fonte de dados é um banco PostgreSQL já populado pela DTP com aproximadamente 700 milhões de registros."),
    sp(),
    table([
        ["Componente", "Detalhe", "Decisão"],
        ["Plataforma BI", "Tableau Server On-Premise", "Soberania de dados DTP — cloud fora do escopo"],
        ["Fonte de dados", "PostgreSQL (único)", "~700M registros — conexão direta"],
        ["ETL / Transformação", "SEM ETL", "Apenas camada de visualização"],
        ["Acesso público", "Guest Viewer via Tableau Server Core", "Confirmado pela AE Viviani Hupp"],
        ["Acessibilidade", "WCAG 2.1 AA", "Requisito legal — portal público gov"],
        ["Exportação", "CSV / XLSX / PDF", "Requisito funcional confirmado"],
        ["Georreferenciamento", "Shapefiles públicos IBGE", "Shapefiles DTP indisponíveis — alternativa validada"],
        ["Performance", "Live vs. Extract a definir", "A ser decidido na Semana 1 do projeto"],
    ], [3.5*cm, 4.5*cm, 8.5*cm]),
    sp(),
    h2("2.2 Estrutura do Painel"),
    body("O painel será composto por 1 publicação principal com 8 abas temáticas e aproximadamente 35 visualizações individuais. Filtros globais aplicados a todas as abas: Ano, Região, UF, Município e Cor/Raça."),
    sp(),
    table([
        ["#", "Aba Temática", "Indicadores-Chave (referência)"],
        ["1", "Visão Geral", "Painel consolidado de todos os domínios"],
        ["2", "Demografia", "Composição populacional por gênero, faixa etária, raça"],
        ["3", "Autonomia Econômica", "Renda, empregabilidade, liderança empresarial"],
        ["4", "Educação", "Escolaridade, acesso, permanência escolar"],
        ["5", "Saúde", "Mortalidade materna, acesso a serviços de saúde"],
        ["6", "Violência", "Feminicídio, violência doméstica, denúncias"],
        ["7", "Poder e Decisão", "Representatividade política e corporativa"],
        ["8", "Comunicação e Acesso", "Acesso digital, mídia, conectividade"],
    ], [0.8*cm, 4.5*cm, 11.2*cm]),
    sp(),
    note("Os 35 indicadores estão PARCIALMENTE documentados pela DTP. Um workshop de alinhamento com o Ministério das Mulheres é necessário para consolidar fórmulas SQL e definições de cada indicador antes do início do desenvolvimento."),
    sp(),
]

# ─── 3. ROM ─────────────────────────────────────────────────────────────────
story += [
    h1("3. ESTIMATIVA ROM — 600 HORAS"),
    sp(),
    h2("3.1 Composição do Time (Modelo Híbrido PS + Parceiro)"),
    table([
        ["Perfil", "Horas", "Fonte", "Custo Est.", "Observação"],
        ["Project Manager", "80h", "PS Interno (Luciano)", "—", "Sujeito à cláusula 14"],
        ["Tableau Architect", "120h", "Parceiro PTB", "~$9.600\n($80/h)", "Obrigatório ser PTB"],
        ["Tableau Developer 1", "160h", "Parceiro PTB", "~$7.200\n($45/h)", "Obrigatório ser PTB"],
        ["Tableau Developer 2", "160h", "Parceiro PTB", "~$7.200\n($45/h)", "Obrigatório ser PTB"],
        ["UX/UI Designer", "80h", "PS Interno", "—", "Sujeito à cláusula 14"],
        ["TOTAL", "600h", "—", "~$24.000\n(custo parceiro)", ""],
    ], [3.5*cm, 1.5*cm, 3.5*cm, 2.5*cm, 5.5*cm]),
    sp(),
    h2("3.2 Timeline de Entrega"),
    table([
        ["Marco", "Detalhe"],
        ["Início", "3–4 semanas após OS assinada + infra Tableau Server provisionada"],
        ["Entrega parcial", "Junho/2026 — aceita pela Adriana como estratégia de valor antecipado"],
        ["Ciclo de desenvolvimento", "4 sprints semanais"],
        ["Entrega final", "A definir após OS assinada e infra confirmada"],
    ], [4*cm, 12.5*cm]),
    sp(),
]

# ─── 4. RISCOS ───────────────────────────────────────────────────────────────
story += [
    h1("4. RISCOS E DEPENDÊNCIAS CRÍTICAS"),
    sp(),
    table([
        ["ID", "Risco", "Severidade", "Mitigação / Status"],
        ["R1", "Infra Tableau Server sem previsão de provisão pela DTP\n(CAMINHO CRÍTICO — bloqueia início)", "🔴 CRÍTICO", "Vivi enviará requisitos de máquina à Adriana.\nSem infra, não há início."],
        ["R2", "OS/assinatura até fim de maio/2026 sem garantia\n(Adriana não assina sozinha)", "🔴 ALTO", "Nelson e Claudio Salas devem escalar para\npatrocinador executivo DTP"],
        ["R3", "700M registros — decisão live vs. extract impacta\nperformance e arquitetura", "🟠 ALTO", "Decidir na Semana 1 com Milena/Lidiane (dados DTP)"],
        ["R4", "Shapefiles georreferenciados indisponíveis na DTP", "🟡 MÉDIO", "Alternativa validada: shapefiles públicos IBGE.\nPendente aceite formal da DTP"],
        ["R5", "~35 indicadores sem fórmula SQL definida", "🟡 MÉDIO", "Workshop com Ministério das Mulheres\nnecessário antes do Sprint 1"],
        ["R6", "Cláusula 14 — restrição PTB para PM e Arquiteto", "🟡 MÉDIO", "Rejane está mapeando parceiros PTB disponíveis\npara junho/2026"],
    ], [0.8*cm, 5.5*cm, 2.2*cm, 8*cm]),
    sp(),
]

# ─── 5. PRÓXIMOS PASSOS ──────────────────────────────────────────────────────
story += [
    h1("5. PRÓXIMOS PASSOS E RESPONSÁVEIS"),
    sp(),
    table([
        ["Ação", "Responsável", "Prazo / Status"],
        ["Montar proposta/OS e validar com Claudio + Juliana", "Nelson", "Esta semana — URGENTE"],
        ["Criar oportunidade PS + DSR no sistema", "Juliana Brites", "Esta semana"],
        ["Identificar parceiro PTB disponível para junho", "Rejane", "Esta semana"],
        ["Enviar requisitos de máquina Tableau Server à Adriana", "Viviani Hupp", "Esta semana"],
        ["Confirmar aceite de shapefiles IBGE pela DTP", "Nelson / Adriana", "A confirmar"],
        ["Agendar workshop de indicadores com Ministério das Mulheres", "Claudio Salas / Adriana", "Pós-OS assinada"],
        ["Definir live vs. extract com Milena/Lidiane (DTP dados)", "Tableau Architect (PTB)", "Semana 1 do projeto"],
        ["Provisionar infra Tableau Server On-Premise", "Dataprev (Adriana)", "CAMINHO CRÍTICO"],
    ], [6.5*cm, 3.5*cm, 6.5*cm]),
    sp(),
]

# ─── 6. PREMISSAS E EXCLUSÕES ────────────────────────────────────────────────
story += [
    h1("6. PREMISSAS E EXCLUSÕES DE ESCOPO"),
    sp(),
    h2("6.1 Premissas"),
    bullet("PostgreSQL da DTP está populado e acessível ao time de desenvolvimento."),
    bullet("Dataprev provisiona infra Tableau Server On-Premise conforme especificações técnicas enviadas pela Vivi."),
    bullet("PO da Dataprev (Adriana) centraliza backlog e alinhamento com Ministério das Mulheres."),
    bullet("Indicadores e fórmulas SQL serão formalizados em workshop antes do Sprint 1."),
    bullet("Shapefiles IBGE são aceitos como substitutos para georreferenciamento."),
    bullet("PM e Arquiteto Tableau serão recursos PTB (cláusula 14 do contrato DTP)."),
    sp(),
    h2("6.2 Fora do Escopo (V1)"),
    bullet("ETL, transformação ou movimentação de dados — responsabilidade exclusiva da DTP."),
    bullet("Desenvolvimento ou manutenção do banco PostgreSQL."),
    bullet("Integração com outras fontes além do PostgreSQL DTP."),
    bullet("Migração ou saneamento de dados históricos."),
    bullet("Desenvolvimento de APIs externas ou sistemas de autenticação (além de Guest Viewer)."),
    bullet("Treinamento de usuários finais do Ministério das Mulheres (fora do SOW atual)."),
    bullet("Segmentos ou painéis adicionais além das 8 abas do V1."),
    sp(),
]

# ─── 7. GLOSSÁRIO ────────────────────────────────────────────────────────────
story += [
    h1("7. GLOSSÁRIO E REFERÊNCIAS"),
    sp(),
    table([
        ["Termo", "Definição"],
        ["DataMulheres", "Plataforma digital do Ministério das Mulheres para dados de igualdade de gênero"],
        ["DTP / Dataprev", "Empresa de Tecnologia e Informações da Previdência — operadora de dados e cliente contratante"],
        ["Guest Viewer", "Modalidade de acesso Tableau que permite visualização pública sem login individual"],
        ["Tableau Server Core", "Licenciamento Tableau por núcleo de servidor — viabiliza Guest Viewer público"],
        ["PTB", "Parceiro homologado pela Dataprev — obrigatório para perfis técnicos (cláusula 14)"],
        ["WCAG 2.1 AA", "Web Content Accessibility Guidelines — padrão de acessibilidade exigido para portais públicos gov"],
        ["ROM", "Rough Order of Magnitude — estimativa de alto nível de horas e custos do projeto"],
        ["OS", "Ordem de Serviço — instrumento contratual para formalização do engajamento na DTP"],
        ["Sprint", "Ciclo semanal de desenvolvimento ágil — 4 sprints previstos no projeto"],
        ["Live / Extract", "Modalidades de conexão Tableau: Live = consulta direta em tempo real; Extract = snapshot otimizado"],
        ["Shapefile IBGE", "Arquivo geoespacial público do IBGE para georreferenciamento de mapas por UF/Município"],
    ], [3.5*cm, 13*cm]),
    sp(),
]

# ─── RODAPÉ ──────────────────────────────────────────────────────────────────
story += [
    hr(),
    Paragraph(
        "Documento gerado em 28/05/2026 | Salesforce Professional Services LATAM | "
        "Uso restrito ao time de delivery — não compartilhar externamente sem aprovação de Nelson (presales) e Claudio Salas (delivery lead).",
        ParagraphStyle("footer", parent=styles["Normal"],
            fontSize=7.5, textColor=colors.HexColor("#888888"),
            alignment=TA_CENTER, fontName="Helvetica-Oblique")
    ),
]

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
