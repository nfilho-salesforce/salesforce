from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT = "/Users/nfilho/claude/ANATEL_Inovacao_Digital_NotebookLM.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2.5*cm,
    bottomMargin=2*cm,
    title="ANATEL Inovação Digital — Base de Conhecimento do Projeto",
    author="Salesforce Professional Services LATAM"
)

styles = getSampleStyleSheet()

sf_dark   = colors.HexColor("#032D60")
sf_blue   = colors.HexColor("#0070D2")
sf_light  = colors.HexColor("#E8F4FD")
sf_orange = colors.HexColor("#FF6900")
sf_green  = colors.HexColor("#2E844A")
sf_red    = colors.HexColor("#BA0517")
sf_yellow = colors.HexColor("#FFC928")
sf_gray   = colors.HexColor("#F3F3F3")

title_style = ParagraphStyle("title", parent=styles["Title"],
    fontSize=24, textColor=sf_dark, spaceAfter=6, alignment=TA_CENTER, fontName="Helvetica-Bold")

h1_style = ParagraphStyle("h1", parent=styles["Heading1"],
    fontSize=13, textColor=colors.white, spaceAfter=6, spaceBefore=14,
    fontName="Helvetica-Bold", backColor=sf_dark,
    leftIndent=-0.3*cm, rightIndent=-0.3*cm, borderPad=5)

h2_style = ParagraphStyle("h2", parent=styles["Heading2"],
    fontSize=11, textColor=sf_dark, spaceAfter=4, spaceBefore=10,
    fontName="Helvetica-Bold")

h3_style = ParagraphStyle("h3", parent=styles["Heading3"],
    fontSize=10, textColor=sf_blue, spaceAfter=3, spaceBefore=6,
    fontName="Helvetica-BoldOblique")

body_style = ParagraphStyle("body", parent=styles["Normal"],
    fontSize=9, spaceAfter=4, spaceBefore=2, leading=13,
    fontName="Helvetica", alignment=TA_JUSTIFY)

bullet_style = ParagraphStyle("bullet", parent=styles["Normal"],
    fontSize=9, spaceAfter=2, spaceBefore=1, leading=12,
    leftIndent=12, fontName="Helvetica", bulletIndent=4)

subbullet_style = ParagraphStyle("subbullet", parent=styles["Normal"],
    fontSize=9, spaceAfter=2, spaceBefore=1, leading=12,
    leftIndent=24, fontName="Helvetica")

bold_body = ParagraphStyle("bold_body", parent=styles["Normal"],
    fontSize=9, spaceAfter=3, fontName="Helvetica-Bold")

alert_style = ParagraphStyle("alert", parent=styles["Normal"],
    fontSize=9, textColor=colors.HexColor("#7D1D00"), spaceAfter=4,
    fontName="Helvetica-Bold", backColor=colors.HexColor("#FFF0E6"),
    leftIndent=8, borderPad=5)

note_style = ParagraphStyle("note", parent=styles["Normal"],
    fontSize=8.5, textColor=colors.HexColor("#444444"), spaceAfter=3,
    fontName="Helvetica-Oblique", leftIndent=8, backColor=colors.HexColor("#EEF4FF"),
    borderPad=4)

footer_style = ParagraphStyle("footer", parent=styles["Normal"],
    fontSize=7.5, textColor=colors.HexColor("#888888"),
    alignment=TA_CENTER, fontName="Helvetica-Oblique")

def h1(text): return Paragraph(f"&nbsp;&nbsp;{text}", h1_style)
def h2(text): return Paragraph(text, h2_style)
def h3(text): return Paragraph(text, h3_style)
def body(text): return Paragraph(text, body_style)
def b(text): return Paragraph(text, bullet_style)
def bb(text): return Paragraph(f"&nbsp;&nbsp;&nbsp;◦ {text}", subbullet_style)
def bold(text): return Paragraph(text, bold_body)
def alert(text): return Paragraph(f"⚠️  {text}", alert_style)
def note(text): return Paragraph(f"ℹ️  {text}", note_style)
def sp(n=1): return Spacer(1, n*0.28*cm)
def hr(): return HRFlowable(width="100%", thickness=0.5, color=sf_blue, spaceAfter=5, spaceBefore=5)
def pb(): return PageBreak()

def tbl(data, col_widths, header=True, header_color=None):
    if header_color is None:
        header_color = sf_dark
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 8.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F0F4FF")]),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ]
    if header:
        style += [
            ("BACKGROUND", (0,0), (-1,0), header_color),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,0), 9),
        ]
    t.setStyle(TableStyle(style))
    return t

# ════════════════════════════════════════════════════════════════════════════
story = []

# ── CAPA ────────────────────────────────────────────────────────────────────
story += [
    sp(2),
    Paragraph("SALESFORCE PROFESSIONAL SERVICES LATAM", ParagraphStyle("cap",
        parent=styles["Normal"], fontSize=10, textColor=sf_blue,
        alignment=TA_CENTER, fontName="Helvetica-Bold")),
    sp(1),
    Paragraph("ANATEL", ParagraphStyle("mt", parent=styles["Title"],
        fontSize=32, textColor=sf_dark, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("Inovação Digital", ParagraphStyle("mt2", parent=styles["Normal"],
        fontSize=18, textColor=sf_blue, alignment=TA_CENTER, fontName="Helvetica")),
    sp(0.5),
    HRFlowable(width="60%", thickness=2, color=sf_orange, spaceAfter=10, spaceBefore=6),
    Paragraph("Base de Conhecimento do Projeto", ParagraphStyle("s2",
        parent=styles["Normal"], fontSize=12, textColor=colors.HexColor("#444444"),
        alignment=TA_CENTER, fontName="Helvetica-Oblique")),
    Paragraph("Transformação Digital do Framework Regulatório de Telecomunicações do Brasil", ParagraphStyle("s3",
        parent=styles["Normal"], fontSize=10, textColor=colors.HexColor("#666666"),
        alignment=TA_CENTER, fontName="Helvetica")),
    sp(2),
    tbl([
        ["Status", "🟠 Discovery parcial — Roadmap v3 gerado — Proposta em elaboração"],
        ["Versão do documento", "1.0 — Gerado em 29/05/2026"],
        ["Destinatário", "Time de Delivery Salesforce PS LATAM"],
        ["Duração total estimada", "~18 meses | Início: Abr/2026 | Go-Live final: Nov/2027"],
        ["Classificação do programa", "Extra Large (XL)"],
    ], [4*cm, 12.5*cm], header=False),
    sp(3),
]

# ── 1. VISÃO ESTRATÉGICA ────────────────────────────────────────────────────
story += [
    h1("1. VISÃO ESTRATÉGICA DO PROJETO"),
    sp(),
    body("Modernizar o framework regulatório de telecomunicações do Brasil através da integração de inteligência artificial e automação via plataforma Salesforce. O propósito central é substituir processos manuais e burocráticos por um ecossistema fluido com visão 360° do usuário, garantindo maior transparência e eficiência no serviço público. A centralização de dados e a comunicação via canais como WhatsApp visam otimizar a conformidade regulatória e elevar significativamente a experiência do cidadão."),
    sp(),
    h2("4 Pilares Fundamentais"),
    tbl([
        ["#", "Pilar", "Descrição", "Sizing"],
        ["1", "MMAR — Licenciamento Digital", "Agilização do licenciamento para embarcações e aeronaves. Sistema Mosaico digitalizado.", "XL"],
        ["2", "TFF/TFI — Arrecadação Inteligente", "Automação da arrecadação de taxas de fiscalização. ~10M registros. Prazo regulatório 31/março.", "L"],
        ["3", "Atendimento Omnichannel", "Agentes autônomos Agentforce substituindo chatbots de árvore fixa. WhatsApp + Service Cloud.", "XL"],
        ["4", "Ouvidoria 360°", "Visão 360° do cidadão, SLA rigoroso, transparência pública e inteligência preditiva.", "L"],
    ], [0.6*cm, 4*cm, 8.4*cm, 3.5*cm]),
    sp(),
    h2("Partes Envolvidas"),
    tbl([
        ["Organização", "Papel", "Contatos"],
        ["ANATEL", "Cliente — órgão regulador federal de telecomunicações", "6 gerências: GIDS, GIMR, GIIB, ORLE, ORER, AFO"],
        ["Salesforce PS LATAM", "Delivery lead / Presales", "Nelson (presales), Ju (ops), Salas, Line, Gaston, Franco (delivery/especialistas)"],
        ["Parceiros/Consultores", "A definir conforme estratégia comercial", "Mari / Fernanda (precisão da proposta)"],
    ], [3.5*cm, 4.5*cm, 8.5*cm]),
    sp(),
]

# ── 2. SIZING E ARQUITETURA ──────────────────────────────────────────────────
story += [
    h1("2. SIZING CONSOLIDADO E ARQUITETURA DE SOLUÇÃO"),
    sp(),
    h2("2.1 Sizing por Dimensão (Programa: XL)"),
    tbl([
        ["Módulo / Dimensão", "Sizing", "Produto Salesforce"],
        ["MMAR — Licenciamento Marítimo/Aeronáutico", "XL", "Public Sector Solutions (PSS) — Licensing & Permitting + BRE"],
        ["TFF/TFI — Arrecadação FISTEL", "L", "Revenue Cloud Billing"],
        ["Atendimento Agêntico", "XL", "Service Cloud + Agentforce + WhatsApp Core"],
        ["Ouvidoria Baseada em Dados", "L", "Service Cloud PSS Case Management"],
        ["Arquitetura de Dados / Volumes", "XL", "Data Cloud + Big Objects + Shield"],
        ["Integração (APIs)", "L", "MuleSoft Anypoint Platform"],
        ["Segurança & Compliance", "L", "Salesforce Shield (FLS + Audit Trail + Event Monitoring)"],
        ["Migração de Dados", "XL", "ETL + MuleSoft Data Loader"],
        ["Customização", "M", "Apex + LWC"],
    ], [6*cm, 1.5*cm, 9*cm]),
    sp(),
    h2("2.2 Gaps Técnicos Identificados (USD Parte 6)"),
    b("Cálculos fiscais complexos → OmniStudio Expression Sets + Apex (precisão decimal auditável)"),
    b("Retenção 7 anos → Big Objects + Data Cloud Data Spaces (sem degradar performance operacional)"),
    b("Transbordo agêntico → Einstein Conversation Insights + resumos automáticos no handoff"),
    sp(),
    h2("2.3 Materiais de Discovery Processados"),
    tbl([
        ["Documento", "Conteúdo"],
        ["Discovery Mapping ANATEL v1.xlsx", "6 abas: Resumo Executivo, Sizing, Questionário 1 e 2, USD, Ballpark"],
        ["ANATEL Digital Transformation — Functional Scope Overview.pdf", "Escopo funcional detalhado dos 4 módulos"],
        ["ANATEL USD — Unified Scoping Document.docx", "USD formal com 9 partes, sizing consolidado e gap analysis"],
        ["Roadmap & Estimativa v3 (canvas IA)", "5 fases, recursos por fase, premissas críticas e riscos do programa"],
    ], [7*cm, 9.5*cm]),
    sp(),
]

# ── 3. DETALHAMENTO DO MÓDULO MMAR ──────────────────────────────────────────
story += [
    h1("3. MÓDULO MMAR — LICENCIAMENTO DIGITAL (SIZING: XL)"),
    sp(),
    body("Modernização do Módulo Marítimo e Aeronáutico do sistema Mosaico. Licenciamento de estações de rádio para aeronaves e embarcações de médio e grande porte de forma totalmente online, com segurança jurídica e máxima agilidade na emissão de outorgas críticas. Transformação de processo burocrático e fragmentado para experiência unificada — do pedido inicial à integração financeira e emissão das licenças."),
    sp(),
    h2("3.1 Solução Técnica"),
    tbl([
        ["Componente", "Detalhe"],
        ["PSS Licensing & Permitting + BRE", "Automação da análise jurídica de conformidade — dispensar análise humana onde a lei permitir"],
        ["Integrações externas", "Marinha do Brasil e DECEA — bidirecionais. Risco: APIs podem não existir → adaptadores proprietários"],
        ["Revenue Cloud", "Orquestração de guias TFI (Taxa de Fiscalização de Instalação) durante o registro"],
        ["Agentforce v3", "Agentes para abertura de registros, consulta de status e resolução de pendências MMAR"],
        ["OmniStudio", "Fluxo guiado de solicitação de licença para embarcações e aeronaves"],
    ], [5*cm, 11.5*cm]),
    sp(),
    h2("3.2 Tipos de Estação no Escopo (6 tipos)"),
    tbl([
        ["Tipo", "Dados Técnicos Específicos"],
        ["Embarcação", "Código MMSI, faixas de frequência, DSC (Chamada Seletiva Digital)"],
        ["Embarcação em Teste", "Frequências temporárias, período de validade"],
        ["Radiobaliza", "Frequência 406 MHz, código de identificação internacional"],
        ["Costeira", "Faixas HF/VHF, especificações de antena (ganho, ângulo de meia potência)"],
        ["Portuária", "Raio de cobertura, integração com sistemas portuários"],
        ["Móvel", "Itinerância, múltiplas faixas de frequência"],
    ], [3.5*cm, 13*cm]),
    sp(),
    h2("3.3 Desafios de Alta Complexidade (justificativa sizing XL)"),
    tbl([
        ["#", "Desafio", "Risco", "Implicação"],
        ["1", "Automação de Regras Legais", "CRÍTICO", "Documentação incompleta do Mosaico legado — risco de gap no BRE. Necessário mapear quando análise humana é obrigatória por lei."],
        ["2", "Segurança e Falha de Alinhamento Funcional", "CRÍTICO", "MMAR lida com segurança de vida no mar e no ar. Erro no BRE = emissão ilegal ou bloqueio indevido."],
        ["3", "Integrações Externas (Marinha/DECEA)", "ALTO", "Se APIs não existirem, adaptadores proprietários aumentam escopo e custo significativamente."],
        ["4", "Fluxos Multinível + Dados Técnicos Específicos", "ALTO", "6 tipos de estação com atributos MMSI, DSC, frequências, antenas — cada um com fluxo de aprovação distinto."],
    ], [0.6*cm, 4*cm, 2*cm, 10*cm]),
    sp(),
]

# ── 4. ROADMAP ──────────────────────────────────────────────────────────────
story += [
    pb(),
    h1("4. ROADMAP — 5 FASES (~18 MESES)"),
    sp(),
    tbl([
        ["Fase", "Módulo", "Duração", "Go-Live", "Outcome"],
        ["Fase 0", "Fundação & Data Model", "10 semanas", "Jun/2026", "A ANATEL enxerga o cidadão pela primeira vez em um único lugar"],
        ["Fase 1", "Omnichannel Agêntico", "16 semanas", "Out/2026", "O cidadão resolve sozinho. O servidor atende com contexto completo."],
        ["Fase 2", "TFF/TFI Arrecadação Inteligente", "21 semanas", "Mar/2027 ⚠️", "Reduzir inadimplência antes do prazo de março"],
        ["Fase 3", "MMAR Licenciamento Digital", "18 semanas", "Ago/2027", "Licença marítima e aeronáutica emitida em horas, não semanas"],
        ["Fase 4", "Ouvidoria 360° & Inteligência", "13 semanas", "Nov/2027", "A ANATEL decide com dados. O cidadão tem resolução cirúrgica."],
    ], [1.5*cm, 4.5*cm, 2.5*cm, 2.5*cm, 5.5*cm]),
    sp(),
    alert("PRAZO REGULATÓRIO CRÍTICO — Fase 2: Go-live planejado para início de março/2027 com 4 semanas de margem antes do prazo de 31/março para geração de boletos TFF. Este prazo NÃO PODE ser comprometido."),
    sp(),

    h2("Fase 0 — Fundação & Data Model (Abr–Jun/2026)"),
    bold("Entregáveis:"),
    b("Data model unificado: Ente Regulado, Cidadão, Estação, Caso, Obrigação"),
    b("Integração inicial leve de uma fonte por módulo (apenas leitura)"),
    b("Dashboard executivo: volume de licenças, inadimplência TFF, casos abertos, reclamações"),
    b("Estrutura de perfis, times e permissões para as 6 gerências"),
    b("Ambientes Salesforce configurados (DEV, QA, PROD) + processo de release"),
    b("Journey map e pesquisa de UX com usuários internos das gerências"),
    bold("Exclusões: Data Cloud, OmniStudio, Agentforce, MuleSoft em produção, treinamento de usuários, migração de dados históricos."),
    sp(),

    h2("Fase 1 — Omnichannel Agêntico (Jun–Out/2026)"),
    bold("Entregáveis:"),
    b("Service Cloud configurado com fila unificada (email, web, telefone)"),
    b("WhatsApp Oficial integrado nativamente (aprovação Meta iniciada na Fase 0)"),
    b("Visão 360° do consumidor no console do agente"),
    b("Agentforce v1: triage autônoma (status de licença, 2ª via de boleto, prazo de análise)"),
    b("Transbordo humanizado e contextualizado para servidores"),
    b("SLA tracking e relatórios operacionais de atendimento"),
    b("Treinamento dos servidores para novo modelo de atendimento"),
    note("OmniStudio (Industries/Vlocity): processo de aquisição deve ser iniciado NESTA FASE — lead time de licenciamento. Não está incluso no Service Cloud padrão."),
    bold("Exclusões: CTI/PABX, SEI/SIPAC, histórico de atendimentos, automações de cobrança/financeiro."),
    sp(),

    h2("Fase 2 — TFF/TFI Arrecadação Inteligente (Out/2026–Mar/2027)"),
    bold("Entregáveis:"),
    b("Integração MuleSoft das 3 fontes: SITARWEB, DB_TELECOM (SQL Server) e SMS (MongoDB)"),
    b("Data Cloud como hub consolidado dos ~10 milhões de registros"),
    b("Resolução de identidade do ente regulado entre os 3 sistemas de origem"),
    b("Segmentação: adimplente / em risco / inadimplente / reincidente"),
    b("Jornada anti-inadimplência via WhatsApp + Email: D-30, D-15, D-7, D+1, D+15"),
    b("Reemissão de boleto autônoma via Agentforce v2 (sem agente humano)"),
    b("Portal do contribuinte: consulta de débitos e download de boleto"),
    b("Big Objects para histórico auditável com retenção de 7 anos"),
    b("Trilha de auditoria por registro: regra aplicada, resultado, responsável"),
    b("Workspace colaborativo para as 6 gerências (GIDS, GIMR, GIIB, ORLE, ORER, AFO)"),
    b("Agentforce v2: detecção de anomalias em cálculos (variação anormal YoY)"),
    bold("Exclusões: Motor de cálculo fiscal (permanece externo), SIAFI, contestação/recurso de TFF, histórico de cálculos anteriores."),
    sp(),

    h2("Fase 3 — MMAR Licenciamento Digital (Jan–Ago/2027)"),
    note("Inicia em paralelo com o final da Fase 2 — compartilha infraestrutura MuleSoft e Data Cloud já provisionados."),
    bold("Entregáveis:"),
    b("Integração com Sistema Mosaico via MuleSoft"),
    b("OmniStudio: fluxo guiado de solicitação de licença para embarcações e aeronaves"),
    b("Agentforce v3: status, pendências e próximos passos do licenciamento MMAR"),
    b("Trilha de auditoria jurídica por solicitação"),
    b("Portal do requerente: acompanhamento em tempo real do status da licença"),
    b("Design de fluxo validado com usuários reais (UX HCC) + treinamento de servidores"),
    bold("Exclusões: Integração com Marinha do Brasil, ANAC, Receita Federal; assinatura digital ICP-Brasil; migração de processos em andamento no legado."),
    sp(),

    h2("Fase 4 — Ouvidoria 360° & Inteligência (Ago–Nov/2027)"),
    bold("Entregáveis:"),
    b("Ouvidoria consumindo Visão 360° completa de todos os módulos"),
    b("Agentforce avançado para primeiros atendimentos da Ouvidoria com contexto total"),
    b("CRM Analytics (Tableau CRM): painel preditivo de inadimplência, volume de licenças, tendências"),
    b("Detecção de anomalias no TFF por tipo de serviço e estação"),
    b("Relatórios de fiscalização sob demanda para todas as gerências"),
    b("Compliance de transparência pública (requisito da administração pública federal)"),
    bold("Exclusões: e-OUV, Open Data, ML customizado, AMS pós-go-live."),
    sp(),
]

# ── 5. RECURSOS ─────────────────────────────────────────────────────────────
story += [
    h1("5. RECURSOS CONSOLIDADOS POR FASE"),
    sp(),
    tbl([
        ["Perfil", "F0\n10sem", "F1\n16sem", "F2\n21sem", "F3\n18sem", "F4\n13sem"],
        ["Solution Architect", "100%", "75%", "100%", "75%", "75%"],
        ["MuleSoft Integration Architect", "—", "—", "100%", "—", "—"],
        ["Senior SF Developer", "100%", "100%", "100%", "100%", "100%"],
        ["SF Developer", "—", "100%", "100%", "100%", "—"],
        ["SF Developer (OmniStudio)", "—", "—", "—", "100%", "—"],
        ["Data Architect", "50%", "—", "100%", "—", "75%"],
        ["MuleSoft Developer", "50%", "50%", "—", "75%", "—"],
        ["Agentforce / AI Specialist", "—", "100%", "75%", "50%", "100%"],
        ["Service Cloud Consultant", "—", "100%", "—", "—", "—"],
        ["UX / HCC Consultant", "50%", "75%", "—", "75%", "—"],
        ["QA Engineer", "50%", "100%", "100%", "100%", "100%"],
        ["Project Manager", "100%", "100%", "100%", "100%", "100%"],
    ], [5.5*cm, 2*cm, 2*cm, 2*cm, 2*cm, 2*cm]),
    sp(),
]

# ── 6. PREMISSAS CRÍTICAS ────────────────────────────────────────────────────
story += [
    h1("6. PREMISSAS CRÍTICAS DO PROGRAMA"),
    sp(),
    tbl([
        ["Premissa", "Quando", "Responsável"],
        ["MuleSoft licenciado e provisionado", "Antes do kick-off Fase 0", "ANATEL / Salesforce"],
        ["Data Cloud licenciado e provisionado", "Antes do início Fase 2", "ANATEL / Salesforce"],
        ["OmniStudio (Industries/Vlocity) licenciado", "Antes do início Fase 3 — aquisição DEVE iniciar na Fase 1", "ANATEL / Salesforce"],
        ["CRM Analytics (Tableau CRM) licenciado", "Antes do início Fase 4", "ANATEL / Salesforce"],
        ["WhatsApp Business API (Meta) aprovado", "Processo iniciado na Fase 0", "ANATEL + Salesforce"],
        ["Acesso às 3 bases TFF (SITARWEB, DB_TELECOM, MongoDB)", "Garantido antes da Fase 2", "TI da ANATEL"],
        ["Regras de cálculo TFF/TFI documentadas e validadas", "Antes do início Fase 2", "Equipe jurídica/técnica ANATEL"],
        ["API do Sistema Mosaico documentada e disponível", "Antes do início Fase 3", "TI da ANATEL"],
        ["PO dedicado ANATEL com poder de decisão", "Todas as fases (min. 50% dedicação)", "ANATEL"],
        ["Sponsor executivo com autoridade sobre as 6 gerências", "Ativo em todas as fases", "ANATEL"],
        ["SSO / autenticação corporativa mapeada", "Antes do kick-off Fase 0", "TI da ANATEL"],
        ["Change management conduzido pelo lado ANATEL", "Todas as fases com suporte SF", "ANATEL + Salesforce"],
    ], [6.5*cm, 4*cm, 6*cm]),
    sp(),
]

# ── 7. RISCOS ────────────────────────────────────────────────────────────────
story += [
    h1("7. RISCOS DO PROGRAMA"),
    sp(),
    tbl([
        ["Risco", "Prob.", "Impacto", "Mitigação"],
        ["Prazo TFF 31/março não respeitado", "Média", "CRÍTICO", "Go-live Fase 2 planejado para início de março/2027 — 4 semanas de margem operacional supervisionada"],
        ["Qualidade dos dados nas 3 fontes TFF", "Alta", "Alto", "Data profiling na Fase 0; Data Cloud com regras de qualidade antes da Fase 2"],
        ["Lead time licenciamento OmniStudio", "Média", "Alto", "Processo de aquisição iniciado obrigatoriamente durante a Fase 1"],
        ["Aprovação Meta para WhatsApp Business", "Média", "Alto", "Processo iniciado na Fase 0; canal de email como fallback na Fase 1"],
        ["Resistência ao change management nas 6 gerências", "Alta", "Alto", "Sponsor executivo ativo; UX HCC nas Fases 0, 1 e 3 para co-criação com usuários"],
        ["API do Mosaico indisponível ou sem documentação", "Média", "Alto", "Discovery técnico do Mosaico realizado durante a Fase 2 (antes de iniciar Fase 3)"],
        ["Regras TFF com alta variabilidade não mapeada", "Alta", "Alto", "Discovery dedicado de regras antes da Fase 2; motor fiscal permanece externo ao SF"],
        ["Automação BRE/MMAR com regras legais incompletas", "Alta", "CRÍTICO", "Q-ANA-AUT-01 deve ser respondida antes de desenhar a solução BRE. Risco de Functional Alignment Failure."],
        ["APIs Marinha do Brasil / DECEA inexistentes", "Média", "Alto", "Discovery Q-ANA-AUT-02 — se não houver API, adaptar escopo com adaptadores proprietários (aumento de custo)"],
    ], [5*cm, 1.5*cm, 2*cm, 8*cm]),
    sp(),
]

# ── 8. PERGUNTAS ABERTAS ─────────────────────────────────────────────────────
story += [
    h1("8. PERGUNTAS ABERTAS (11 — PENDENTES DE RESPOSTA DA ANATEL)"),
    sp(),
    h2("8.1 MMAR — Licenciamento"),
    tbl([
        ["ID", "Pergunta", "Status"],
        ["Q-ANA-AUT-01", "Regras de análise legal do Mosaico para automação no BRE — documentação disponível? Quando análise humana é obrigatória por lei?", "SEM DETALHES\n(Risco Crítico)"],
        ["Q-ANA-AUT-02", "Integração com Marinha do Brasil e DECEA: bidirecional ou só consulta? Há API disponível ou será necessário RPA/batch?", "SEM DETALHES"],
        ["Q-ANA-AUT-03", "Fórmulas TFI/TFF: variações regionais, índices de inflação, multas por atraso — estão documentadas?", "PARCIAL"],
        ["Q-ANA-AUT-04", "Conciliação bancária FISTEL: GRU externo ou Salesforce emite boleto? Quem integra com o banco?", "SEM DETALHES"],
    ], [2.5*cm, 10*cm, 4*cm]),
    sp(),
    h2("8.2 Atendimento Agêntico"),
    tbl([
        ["ID", "Pergunta", "Status"],
        ["Q-ANA-SRV-01", "Quais são os top 10 motivos de chamado hoje? Há base de conhecimento (FAQ, scripts, árvores de decisão) para alimentar o Agentforce?", "SEM DETALHES"],
        ["Q-ANA-SRV-02", "Quais canais digitais devem estar ativos no Dia 1? (além do WhatsApp: email, chat web, telefonia com STT?)", "PARCIAL\n(só WhatsApp confirmado)"],
        ["Q-ANA-SRV-03", "Algoritmo de roteamento/transbordo: critério para escalar do agente para servidor público? SLA definido por tipo de solicitação?", "SEM DETALHES"],
    ], [2.5*cm, 10*cm, 4*cm]),
    sp(),
    h2("8.3 Arquitetura & Segurança"),
    tbl([
        ["ID", "Pergunta", "Status"],
        ["Q-ANA-TEC-01", "Federação de dados para visão 360°: dados de múltiplos módulos consolidados no Data Cloud ou objeto customizado?", "PARCIAL"],
        ["Q-ANA-TEC-02", "Retenção de 7 anos: acesso online (consultável) ou cold storage aceitável? Define Big Objects vs. Data Cloud Data Spaces vs. solução externa.", "SEM DETALHES"],
        ["Q-ANA-TEC-03", "APIs para portais governamentais externos: Gov.br, TCU — quais? Em qual fase?", "PARCIAL\n(resposta preliminar 'Não')"],
        ["Q-ANA-TEC-04", "IdP corporativo da ANATEL (LDAP, Azure AD, Gov.br) — crítico para estratégia SSO e autenticação dos portais Experience Cloud.", "SEM DETALHES\n(Crítico para SSO)"],
    ], [2.5*cm, 10*cm, 4*cm]),
    sp(),
]

# ── 9. ALINHAMENTO INTERNO ───────────────────────────────────────────────────
story += [
    h1("9. ALINHAMENTO INTERNO E AÇÕES ABERTAS"),
    sp(),
    h2("Reunião de Alinhamento Pro Serv ANATEL — 14/MAI/2026"),
    body("A reunião definiu o escopo inicial e as próximas etapas da proposta. A iniciativa será tratada de forma independente, priorizando a validação técnica dos requisitos antes de fechar o comprometimento comercial."),
    sp(),
    tbl([
        ["Decisão / Risco", "Detalhe"],
        ["Foco confirmado", "Integração via APIs (MuleSoft) + automatização das taxas de fiscalização (TFF/TFI)"],
        ["Tecnologia confirmada", "Agentes inteligentes substituindo chatbots de árvore fixa — sistemas legados mantidos"],
        ["Risco comercial", "Falta de detalhes técnicos e regras de negócio gera risco de subestimativa de esforço"],
        ["Status da proposta", "Nível de abstração elevado — alerta de prazo ativo"],
        ["Contexto", "Reunião anterior foi despriorizada e encerrada antecipadamente por falta de tempo"],
    ], [4*cm, 12.5*cm], header=False),
    sp(),
    h2("Ações Abertas — Nelson Stebulaitis Filho"),
    tbl([
        ["Ação", "Com quem", "Status"],
        ["Definir nível de precisão necessário para a proposta comercial", "Mari ou Fernanda", "ABERTO — URGENTE"],
        ["Alinhar sobre incertezas, escopo e estratégia de entrega", "Ju, Salas, Line, Gaston e Franco", "ABERTO"],
        ["Comunicar status atual (abstração elevada) e alertar sobre prazo", "Ju (ops)", "ABERTO — URGENTE"],
        ["Consolidar perguntas de discovery por módulo para levar ao alinhamento", "Time interno SF", "GERADO — aguardando alinhamento"],
    ], [6.5*cm, 3.5*cm, 6.5*cm]),
    sp(),
    note("Pergunta-chave para Mari/Fernanda: 'A ANATEL aceita uma estimativa ROM com faixa de variação (±30%) baseada nos dados atuais, ou é necessário um P&D pago antes de apresentar o valor final?' — Essa resposta define T&M com premissas ou fase de Plan & Design."),
    sp(),
]

# ── GLOSSÁRIO ────────────────────────────────────────────────────────────────
story += [
    h1("10. GLOSSÁRIO E REFERÊNCIAS"),
    sp(),
    tbl([
        ["Termo", "Definição"],
        ["ANATEL", "Agência Nacional de Telecomunicações — órgão regulador federal"],
        ["MMAR", "Módulo Marítimo e Aeronáutico — parte do sistema Mosaico legado da ANATEL"],
        ["TFF / TFI", "Taxa de Fiscalização de Funcionamento / Taxa de Fiscalização de Instalação — tributos regulatórios"],
        ["FISTEL", "Fundo de Fiscalização das Telecomunicações — base de arrecadação das taxas TFF/TFI"],
        ["Mosaico", "Sistema legado da ANATEL para licenciamento de estações de rádio"],
        ["MMSI", "Maritime Mobile Service Identity — código único de identificação de embarcações no serviço rádio"],
        ["DSC", "Digital Selective Calling — Chamada Seletiva Digital usada em comunicações marítimas de segurança"],
        ["DECEA", "Departamento de Controle do Espaço Aéreo — integração necessária para MMAR aeronáutico"],
        ["BRE", "Business Rules Engine — motor de regras de negócio nativo do Salesforce PSS"],
        ["PSS", "Public Sector Solutions — nuvem Salesforce para setor público com Licensing & Permitting"],
        ["OmniStudio", "Ferramenta Salesforce Industries/Vlocity para fluxos guiados — licença separada do Service Cloud"],
        ["GRU", "Guia de Recolhimento da União — documento de pagamento de tributos federais"],
        ["ICP-Brasil", "Infraestrutura de Chaves Públicas Brasileira — padrão de assinatura digital (fora do escopo V1)"],
        ["USD", "Unified Scoping Document — documento formal de escopo consolidado do projeto"],
        ["ROM", "Rough Order of Magnitude — estimativa de alto nível de horas e custos"],
        ["SITARWEB", "Sistema de Informações de Telecomunicações — uma das 3 fontes TFF"],
        ["DB_TELECOM", "Base SQL Server com dados de telecomunicações — uma das 3 fontes TFF"],
        ["SMS (MongoDB)", "Sistema de arrecadação MongoDB — uma das 3 fontes TFF"],
        ["XL / L / M", "Classificação de sizing: Extra Large / Large / Medium — complexidade e esforço estimado"],
        ["6 Gerências", "GIDS, GIMR, GIIB, ORLE, ORER, AFO — áreas da ANATEL envolvidas no projeto"],
    ], [3.5*cm, 13*cm]),
    sp(),
]

# ── RODAPÉ ───────────────────────────────────────────────────────────────────
story += [
    hr(),
    Paragraph(
        "Documento gerado em 29/05/2026 | Salesforce Professional Services LATAM | "
        "Uso restrito ao time de delivery — não compartilhar externamente sem aprovação de Nelson (presales).",
        footer_style
    ),
]

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
