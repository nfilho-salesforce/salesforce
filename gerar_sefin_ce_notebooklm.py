from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak, Image)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import os

OUTPUT = "/Users/nfilho/claude/DTP_SEFIN_CE_NotebookLM.pdf"
FLUXO_IMG = "/Users/nfilho/claude/SEFIN_CE_Fluxo_v1_FINAL.png"

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2.5*cm, bottomMargin=2*cm,
    title="DTP-SEFIN-CE — Base de Conhecimento do Projeto",
    author="Salesforce Professional Services LATAM"
)

styles = getSampleStyleSheet()
sf_dark   = colors.HexColor("#032D60")
sf_blue   = colors.HexColor("#0096FF")
sf_light  = colors.HexColor("#D4EEFF")
sf_orange = colors.HexColor("#FF6B00")
sf_green  = colors.HexColor("#2E7D32")
sf_red    = colors.HexColor("#7B1A1A")
sf_teal   = colors.HexColor("#00695C")
sf_gray   = colors.HexColor("#F4F6F9")
sf_warn   = colors.HexColor("#E65100")

title_s = ParagraphStyle("title", parent=styles["Title"],
    fontSize=22, textColor=sf_dark, spaceAfter=6,
    alignment=TA_CENTER, fontName="Helvetica-Bold")
sub_s = ParagraphStyle("sub", parent=styles["Normal"],
    fontSize=11, textColor=sf_blue, spaceAfter=4,
    alignment=TA_CENTER, fontName="Helvetica-Oblique")
h1_s = ParagraphStyle("h1", parent=styles["Heading1"],
    fontSize=13, textColor=colors.white, spaceAfter=6, spaceBefore=14,
    fontName="Helvetica-Bold", backColor=sf_dark,
    leftIndent=-0.3*cm, rightIndent=-0.3*cm, borderPad=5)
h2_s = ParagraphStyle("h2", parent=styles["Heading2"],
    fontSize=11, textColor=sf_dark, spaceAfter=4, spaceBefore=10,
    fontName="Helvetica-Bold")
h3_s = ParagraphStyle("h3", parent=styles["Heading3"],
    fontSize=10, textColor=sf_blue, spaceAfter=3, spaceBefore=6,
    fontName="Helvetica-BoldOblique")
body_s = ParagraphStyle("body", parent=styles["Normal"],
    fontSize=9, spaceAfter=4, spaceBefore=2, leading=13,
    fontName="Helvetica", alignment=TA_JUSTIFY)
bullet_s = ParagraphStyle("bullet", parent=styles["Normal"],
    fontSize=9, spaceAfter=3, spaceBefore=1, leading=13,
    leftIndent=0.5*cm, fontName="Helvetica")
code_s = ParagraphStyle("code", parent=styles["Normal"],
    fontSize=8, spaceAfter=3, leading=12,
    fontName="Courier", backColor=colors.HexColor("#F4F6F9"),
    leftIndent=0.3*cm, borderPad=4)
warn_s = ParagraphStyle("warn", parent=styles["Normal"],
    fontSize=9, spaceAfter=3, leading=13,
    fontName="Helvetica-Bold", textColor=sf_warn)
footer_s = ParagraphStyle("footer", parent=styles["Normal"],
    fontSize=7.5, textColor=colors.HexColor("#888888"),
    alignment=TA_CENTER, fontName="Helvetica-Oblique")

def h1(t): return Paragraph(t, h1_s)
def h2(t): return Paragraph(t, h2_s)
def h3(t): return Paragraph(t, h3_s)
def p(t):  return Paragraph(t, body_s)
def b(t):  return Paragraph(f"• {t}", bullet_s)
def w(t):  return Paragraph(f"⚠ {t}", warn_s)
def sp(n=6): return Spacer(1, n)
def hr(): return HRFlowable(width="100%", thickness=1,
                             color=sf_blue, spaceAfter=6, spaceBefore=6)

def table(data, colWidths, header_bg=sf_dark):
    t = Table(data, colWidths=colWidths, repeatRows=1)
    nrows = len(data)
    style = [
        ('BACKGROUND', (0,0), (-1,0), header_bg),
        ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
        ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0,0), (-1,0), 9),
        ('FONTNAME',   (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',   (0,1), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F4F6F9")]),
        ('GRID',       (0,0), (-1,-1), 0.4, colors.HexColor("#CCCCCC")),
        ('VALIGN',     (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]
    t.setStyle(TableStyle(style))
    return t

story = []

# ═══════════════════════════════════════════════════════════════════════════════
# CAPA
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    sp(40),
    Paragraph("DTP-SEFIN-CE", title_s),
    Paragraph("Base de Conhecimento do Projeto", sub_s),
    sp(8),
    hr(),
    sp(6),
    Paragraph("Salesforce Professional Services LATAM  ·  DATAPREV / SEFIN Fortaleza", sub_s),
    Paragraph("Régua de Cobrança Proativa via WhatsApp — Agentforce", sub_s),
    sp(6),
    hr(),
    sp(60),
    Paragraph("Gerado em: 02/07/2026", sub_s),
    Paragraph("Confidencial — uso restrito ao time de projeto", footer_s),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 1. CONTEXTO E VISÃO GERAL
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("1. CONTEXTO E VISÃO GERAL DO PROJETO"),
    sp(),
    h2("1.1 Origem da Demanda"),
    p("A SEFIN-CE (Secretaria Municipal de Finanças de Fortaleza) solicitou à DATAPREV uma proposta de solução "
      "Salesforce para implementação de uma régua de cobrança proativa via WhatsApp, visando reduzir a inadimplência "
      "de tributos municipais (IPTU e TMRSU) e modernizar o atendimento ao contribuinte cearense."),
    sp(),
    h2("1.2 Dados Principais"),
    table([
        ["Parâmetro", "Valor"],
        ["Canal principal", "WhatsApp (proativo + reativo)"],
        ["Volume WhatsApp proativo (régua)", "4.860.000 mensagens/ano"],
        ["Volume chatbot autoatendimento", "400.000 conversas/ano"],
        ["Posições de atendimento humano (PAs)", "10 agentes"],
        ["Tributos atendidos", "IPTU (cód. 10) e Taxa do Lixo / TMRSU (cód. 980)"],
        ["ISS", "Redirecionamento para site SEFIN-CE (sem atendimento no bot)"],
        ["Valor estimado do projeto", "~R$ 1.300.000 (inclui markup DATAPREV)"],
        ["Prazo estimado", "5 meses"],
        ["Perfis PS", "1 Developer Service Cloud + 1 Developer Marketing Cloud + 1 PM"],
    ], [6*cm, 10.5*cm]),
    sp(),
    h2("1.3 Participantes Identificados"),
    table([
        ["Nome", "Papel", "Empresa"],
        ["Nelson Stebulaitis Filho", "Presales / Solutions Manager", "Salesforce PS LATAM"],
        ["Alex Siqueira", "Account Executive", "Salesforce"],
        ["Augusto Cesar Martins", "Delivery Lead / Técnico", "DATAPREV"],
        ["Osvaldo Melo", "Arquiteto de Solução", "DATAPREV"],
        ["Fernanda", "AE anterior (levantamento inicial 800h)", "Salesforce"],
    ], [5*cm, 5.5*cm, 6*cm]),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 2. PRODUTOS SALESFORCE
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("2. PRODUTOS SALESFORCE — ESCOPO CONFIRMADO"),
    sp(),
    p("Confirmado na reunião de 01/07/2026 com Augusto e Osvaldo. "
      "NÃO há MuleSoft nem Data Cloud no escopo — integração via Flow/Apex direto."),
    sp(),
    table([
        ["Produto", "Função no Projeto", "Status"],
        ["Service Cloud — Digital Engagement",
         "Canal WhatsApp nativo; 10 PAs; roteamento omnichannel", "✅ Confirmado"],
        ["Agentforce",
         "Agente WhatsApp: IPTU, Taxa Lixo, ISS (link), ajuda via KB", "✅ Confirmado"],
        ["Marketing Cloud — Journey Builder",
         "Disparos proativos: 4,86M msgs/ano da régua de cobrança", "✅ Confirmado"],
        ["Flow Orchestration + Apex",
         "Orquestração dos subfluxos; geração PDF DAM via Apex", "✅ Confirmado"],
        ["Customer Data Cloud Starter",
         "Apenas para habilitar plataforma core", "✅ Confirmado"],
        ["MuleSoft", "FORA DO ESCOPO — APIs via Flow/Apex direto", "❌ Removido"],
        ["Data Cloud", "FORA DO ESCOPO", "❌ Removido"],
    ], [4.5*cm, 7.5*cm, 4.5*cm]),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 3. APIs MAPEADAS
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("3. APIs DO SISTEMA ARREC — SEFIN-CE"),
    sp(),
    h2("3.1 API EmitirDamUnico"),
    p("Emite o DAM (Documento de Arrecadação Municipal) — boleto de pagamento. "
      "Retorna link PDF para download/envio via WhatsApp."),
    sp(),
    table([
        ["Parâmetro", "Tipo", "Obrig.", "Descrição"],
        ["tipoDebito",     "Integer(3)", "S", "TMRSU=980, IPTU=10"],
        ["tipoPessoa",     "String(1)",  "S", "F = física, J = jurídica"],
        ["cpfcnpj",        "String(14)", "S", "Somente números"],
        ["inscricao",      "Integer(7)", "N", "Inscrição municipal do imóvel"],
        ["digito",         "Integer(1)", "N", "Obrigatório se inscricao informada"],
        ["tipoPagamento",  "String(9)",  "S", "COTAUNICA ou PARCELADO"],
        ["AnoDebito",      "Integer(4)", "N", "Ano do débito"],
        ["periodoParcelas","Date",       "N", "Obrigatório se PARCELADO"],
    ], [3.5*cm, 2.5*cm, 1.5*cm, 9*cm]),
    sp(),
    p("<b>Retorno:</b> Link PDF do DAM pronto para download e envio via WhatsApp."),
    sp(),
    h2("3.2 API ConsultaImovel"),
    p("Dois métodos: por inscrição do imóvel (por-inscricao) ou por documento CPF/CNPJ (por-documento)."),
    sp(),
    h3("Método por-documento (utilizado no fluxo do agente):"),
    table([
        ["Parâmetro", "Tipo", "Obrig.", "Descrição"],
        ["Tipo",       "String(8)",  "S", "Física ou Jurídica"],
        ["Documento",  "String(14)", "S", "CPF ou CNPJ formatado"],
        ["Data",       "Date ISO8601","S","Data de nascimento (PF) ou abertura na RFB (PJ)"],
        ["Exercicio",  "Number(4)",  "S", "Exercício fiscal a pesquisar"],
    ], [3.5*cm, 2.5*cm, 1.5*cm, 9*cm]),
    sp(),
    p("<b>Retorno por-documento:</b> Inscrição do imóvel + Endereço + Cartografia + Titular + mensagensErro."),
    sp(),
    h2("3.3 API de Registro de Contato (A ENTREGAR — premissa)"),
    p("API a ser entregue pelo cliente. Receberá ao final de toda conversa:"),
    b("CPF/CNPJ do cidadão"),
    b("Nome do cidadão"),
    b("Serviço executado ou tentado"),
    b("Resultado da interação (sucesso, falha, abandono)"),
    b("Nota de satisfação (1–5 estrelas)"),
    b("Justificativa de insatisfação (quando nota ≤ 3)"),
    sp(),
    h2("3.4 Fluxo de Integração"),
    Paragraph(
        "Gatilho (vencimento/débito) → Agentforce inicia conversa WhatsApp → "
        "Coleta CPF/CNPJ + nome + data → Chama ConsultaImovel (por-documento) → "
        "Valida titular + inscrições → Chama EmitirDamUnico → Envia link PDF via WhatsApp → "
        "Pesquisa satisfação → Chama API Registro de Contato → Despedida",
        code_s),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 4. FLUXO DE ATENDIMENTO — TRANSCRIÇÃO COMPLETA
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("4. FLUXO DE ATENDIMENTO — TRANSCRIÇÃO COMPLETA v1.0"),
    sp(),
    p("Fluxo validado por Nelson Stebulaitis Filho em 02/07/2026. "
      "Baseado no HLD v4 da SEFIN-CE, revisado e adaptado para Agentforce sem transbordo humano."),
    sp(),
    h2("4.1 Entrada"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["INÍCIO",         "Evento",    "Cidadão envia mensagem ao canal WhatsApp da SEFIN-CE"],
        ["SAUDAÇÃO",       "Ação Agente","Agente envia boas-vindas ao canal SEFIN-CE"],
        ["Veio de HSM?",   "Condicional","SIM → apresenta contexto do HSM [Q-A: a confirmar]\nNÃO → segue para Menu"],
        ["MENU DE SERVIÇOS","Ação Agente","1. Boleto IPTU\n2. Boleto Taxa do Lixo (TMRSU)\n3. ISS\n4. Preciso de ajuda / Outros"],
    ], [3*cm, 2.5*cm, 11*cm]),
    sp(),
    h2("4.2 Identificação do Cidadão"),
    p("Disparada para IPTU, Taxa do Lixo e Preciso de Ajuda. ISS não requer identificação."),
    table([
        ["Nó", "Tipo", "Ação"],
        ["Já identificado?", "Condicional", "SIM + mesmo CPF → reutiliza sessão, vai para API\nSIM + CPF diferente ou NÃO → solicita CPF/CNPJ"],
        ["Validação CPF/CNPJ", "Condicional", "Válido → solicita Nome\nInválido → até 2 tentativas → esgotou → Pesquisa → Encerra"],
        ["Solicita NOME", "Ação Agente", "Coleta nome do cidadão"],
        ["Solicita DATA", "Ação Agente", "Data de Nascimento (PF) ou Data de Abertura RFB (PJ)"],
        ["Validação Data", "Condicional", "Válida → chama API\nInválida → até 2 tentativas → esgotou → Pesquisa → Encerra"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    h2("4.3 Consulta Imóvel — API"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["API ConsultaImovel", "Chamada API", "Envia CPF/CNPJ + nome + data"],
        ["Serviço OK?", "Condicional", "NÃO → 1 retentativa automática\nNÃO (2ª vez) → Informa falha + registra + AJUDO COM ALGO MAIS?"],
        ["Possui inscrições?", "Condicional", "NÃO → AJUDO COM ALGO MAIS?"],
        ["Possui inscrições em aberto?", "Condicional", "NÃO → AJUDO COM ALGO MAIS?"],
        ["Apresenta inscrições", "Ação Agente", "Apresenta TODAS as inscrições em aberto (sem limite — P-13)"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    h2("4.4 Emissão DAM — IPTU / Taxa do Lixo"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["Cidadão seleciona inscrição", "Ação Usuário", "Seleciona uma inscrição da lista apresentada"],
        ["DAM só no ano vigente?", "Condicional", "SIM → Confirma emissão diretamente\nNÃO → Escolhe Cota Única ou Parcelamento"],
        ["Cota Única / Parcelamento", "Ação Usuário", "COTA ÚNICA → confirma emissão\nPARCELADO → seleciona parcelas\nEscolhe ano → ano vigente ou todos os anos"],
        ["CONFIRMA EMISSÃO?", "Condicional", "SIM → chama API EmitirDamUnico\nNÃO → AJUDO COM ALGO MAIS?"],
        ["API EmitirDamUnico", "Chamada API", "Envia CPF/CNPJ + tipoDebito + tipoPagamento + ano/parcelas"],
        ["Serviço OK?", "Condicional", "NÃO → 1 retentativa\nNÃO (2ª vez) → informa falha + AJUDO COM ALGO MAIS? (sem pesquisa)"],
        ["Envia PDF", "Ação Agente", "Envia link PDF do DAM via WhatsApp"],
        ["Outra inscrição pendente?", "Condicional", "SIM → Quer emitir outra? → SIM = loop para seleção / NÃO = AJUDO COM ALGO MAIS?"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    h2("4.5 ISS"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["ISS Info", "Ação Agente", "Informa link do site SEFIN-CE para resolução de ISS [Q-E: URL a confirmar]\nNão requer identificação do cidadão"],
        ["Segue para", "Fluxo", "AJUDO COM ALGO MAIS?"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    h2("4.6 Preciso de Ajuda / Outros"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["Solicita CPF/CNPJ", "Ação Agente", "Reutiliza fluxo de identificação (2 tentativas)"],
        ["Solicita Nome", "Ação Agente", "Coleta nome para registro"],
        ["Consulta KB", "Chamada API", "Agente consulta Knowledge Base [Q-F: KB a definir com cliente]"],
        ["KB respondeu?", "Condicional", "SIM → entrega resposta → AJUDO COM ALGO MAIS?\nNÃO → DHA (horário de atendimento)"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    h2("4.7 DHA — Dentro do Horário de Atendimento"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["DHA?", "Condicional", "FORA → informa que atendimento humano só em horário comercial [Q-J] → AJUDO COM ALGO MAIS?\nDENTRO → coleta nome (se não coletado) → [TRANSBORDO — A DEFINIR Q-B]"],
        ["[TRANSBORDO]", "Nó a definir", "Mecanismo não confirmado — sem Service Cloud/Digital Engagement no escopo\nSegue para Pesquisa de Satisfação"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    h2("4.8 Encerramento Universal"),
    table([
        ["Nó", "Tipo", "Ação"],
        ["AJUDO COM ALGO MAIS?", "Condicional", "SIM → volta ao Menu de Serviços\nNÃO → Pesquisa de Satisfação"],
        ["PESQUISA DE SATISFAÇÃO", "Ação Agente", "⭐ Muito ruim  ⭐⭐ Ruim  ⭐⭐⭐ Razoável  ⭐⭐⭐⭐ Bom  ⭐⭐⭐⭐⭐ Muito bom"],
        ["Nota ≤ 3?", "Condicional", "SIM → solicita descrição da insatisfação → API Registro\nNÃO → API Registro direto"],
        ["API Registro de Contato", "Chamada API", "CPF/CNPJ + nome + serviço + resultado + nota + justificativa"],
        ["DESPEDIDA", "Encerramento", "Agente se despede e encerra a conversa"],
    ], [3.5*cm, 2.5*cm, 10.5*cm]),
    sp(),
    w("EXCEÇÃO: Falha de API após 2 tentativas → informa falha + registra contato + AJUDO COM ALGO MAIS? → SEM pesquisa de satisfação neste caminho"),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 5. IMAGEM DO FLUXO
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("5. DIAGRAMA DO FLUXO DE ATENDIMENTO v1.0"),
    sp(),
    p("Diagrama gerado automaticamente a partir das premissas e decisões do projeto. "
      "Validado por Nelson Stebulaitis Filho em 02/07/2026."),
    sp(),
]

if os.path.exists(FLUXO_IMG):
    img = Image(FLUXO_IMG, width=16.5*cm, height=17.6*cm)
    story.append(img)
else:
    story.append(w(f"Imagem não encontrada: {FLUXO_IMG}"))

story += [sp(), PageBreak()]

# ═══════════════════════════════════════════════════════════════════════════════
# 6. PREMISSAS CONSOLIDADAS
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("6. PREMISSAS CONSOLIDADAS DO PROJETO"),
    sp(),
    table([
        ["#", "Premissa"],
        ["P-01", "Todo encerramento = Pesquisa de satisfação → API de registro → Despedida.\nExceção: falha de API após retentativa encerra SEM pesquisa de satisfação."],
        ["P-02", "Sem transbordo humano confirmado no escopo. DHA dentro do horário sinaliza [TRANSBORDO — a definir]."],
        ["P-03", "DHA fora do horário = informa indisponibilidade + encerra normalmente com pesquisa."],
        ["P-04", "API de registro recebe: CPF/CNPJ, nome, serviço executado, resultado, nota, justificativa."],
        ["P-05", "Pesquisa de satisfação em TODOS os encerramentos, inclusive erros e abandonos.\nExceção: falha de API após retentativa."],
        ["P-06", "Notas ≤ 3 estrelas → agente coleta justificativa da insatisfação antes de encerrar."],
        ["P-07", "Máximo 2 tentativas de digitação inválida em qualquer campo. Esgotou → encerra com pesquisa."],
        ["P-08", "Usuário já identificado na sessão → pula identificação e vai direto ao Menu de Serviços."],
        ["P-09", "ISS = informa link do site SEFIN-CE, sem identificação do cidadão."],
        ["P-10", "Falha de API = 1 retentativa automática. Se falhar novamente: informa + registra + AJUDO COM ALGO MAIS? (sem pesquisa)."],
        ["P-11", "CONFIRMA EMISSÃO DO DAM? = NÃO → AJUDO COM ALGO MAIS? direto, sem chamar API."],
        ["P-12", "Loop de emissão de DAM se repete para cada inscrição selecionada, chamando EmitirDamUnico individualmente."],
        ["P-13", "Sem limite de inscrições apresentadas. Agente exibe TODAS retornadas pela API (ignora limite 7 do HLD original)."],
        ["P-14", "Régua proativa via Salesforce Marketing Cloud Journey Builder (sugestão a validar com cliente)."],
        ["P-15", "Preciso de Ajuda → coleta CPF/CNPJ + nome → consulta KB → se KB não responde → DHA → [TRANSBORDO]."],
    ], [1.2*cm, 15.3*cm]),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 7. PERGUNTAS EM ABERTO
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("7. PERGUNTAS EM ABERTO PARA O CLIENTE"),
    sp(),
    p("Itens a esclarecer com DATAPREV / SEFIN-CE antes de finalizar o escopo e iniciar o projeto."),
    sp(),
    table([
        ["#", "Pergunta", "Para quem"],
        ["Q-A", "O que é HSM no contexto do fluxo original? Quais parâmetros e conteúdo das mensagens proativas enviadas?", "Osvaldo / Augusto"],
        ["Q-B", "Qual será o mecanismo de transbordo humano? Como se dará tecnicamente dado que não há Service Cloud/Digital Engagement no escopo?", "Augusto / SEFIN-CE"],
        ["Q-C", "Quais são os parâmetros de entrada da API de registro de contato? (campos esperados, autenticação, endpoint)", "Osvaldo"],
        ["Q-D", "O registro da pesquisa de satisfação é feito na mesma API de log ou em endpoint separado?", "Osvaldo"],
        ["Q-E", "Qual é a URL do site da SEFIN-CE para direcionamento no fluxo ISS?", "SEFIN-CE"],
        ["Q-F", "É possível disponibilizar uma base de conhecimento (KB) para o agente responder dúvidas? Se sim, quem mantém e em qual formato?", "SEFIN-CE / Augusto"],
        ["Q-G", "Há uma régua de comunicação proativa já definida? Se não, o cliente aceita adotar a régua sugerida via Marketing Cloud Journey Builder?", "SEFIN-CE"],
        ["Q-H", "Qual é a fonte de dados que alimenta os gatilhos da régua proativa? Como o Marketing Cloud acessa esses dados (quem está em débito e quando disparar)?", "SEFIN-CE / TI"],
        ["Q-I", "O cidadão pode solicitar opt-out das mensagens proativas? Se sim, como esse opt-out é registrado e respeitado nos disparos seguintes?", "SEFIN-CE"],
        ["Q-J", "Qual é o horário comercial de atendimento humano? (dias da semana, horário de início e fim)", "SEFIN-CE"],
        ["Q-K", "O limite de 7 inscrições no fluxo original é uma limitação do bot atual, da API ConsultaImovel ou regra de negócio? A nova solução pode receber e apresentar todas sem limite?", "Osvaldo / SEFIN-CE"],
    ], [1*cm, 11.5*cm, 4*cm]),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 8. RÉGUA DE COBRANÇA SUGERIDA — MARKETING CLOUD
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("8. RÉGUA DE COBRANÇA SUGERIDA — MARKETING CLOUD JOURNEY BUILDER"),
    sp(),
    p("Proposta de régua proativa via WhatsApp a ser validada com SEFIN-CE. "
      "Baseada em gatilhos de vencimento alimentados pelo sistema tributário ARREC."),
    sp(),
    table([
        ["Etapa", "Gatilho", "Mensagem Sugerida", "Ação Cidadão"],
        ["D-15", "Vencimento em 15 dias", "Lembrete preventivo: seu IPTU vence em 15 dias. Emita seu boleto agora.", "Toca no link → entra no agente"],
        ["D-5",  "Vencimento em 5 dias",  "Alerta: seu IPTU vence em 5 dias. Não deixe para última hora.", "Toca no link → entra no agente"],
        ["D+1",  "Dia seguinte ao vencimento", "Seu IPTU está em aberto. Regularize agora e evite multa.", "Toca no link → entra no agente"],
        ["D+15", "15 dias em atraso", "Atenção: seu débito acumula juros. Parcele ou quite hoje.", "Toca no link → entra no agente"],
        ["Saída", "Pagamento confirmado\n(se API disponível)", "Confirmação: recebemos seu pagamento. Obrigado!", "Não requer ação"],
    ], [1.5*cm, 3.5*cm, 6.5*cm, 5*cm]),
    sp(),
    w("Dependência crítica: o Marketing Cloud precisa receber os dados de quem está em débito e quando vence "
      "(Q-H). Pode ser via API, SFTP batch diário ou Direct Connect ao ARREC."),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 9. SIZING E ROM PRELIMINAR
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("9. SIZING E ROM PRELIMINAR"),
    sp(),
    h2("9.1 Contexto da Estimativa"),
    p("Estimativa inicial de 800 horas foi elaborada pela AE Fernanda e passada para a DATAPREV. "
      "Augusto entende que 800h é mais do que o necessário. Alex Siqueira comprometeu revisão com Nelson. "
      "Valor de ~R$ 1,3M inclui markup DATAPREV — não é o valor Salesforce PS puro."),
    sp(),
    h2("9.2 Perfis Confirmados (sem MuleSoft / Data Cloud)"),
    table([
        ["Perfil", "Escopo", "Referência Rate DTP"],
        ["Developer Service Cloud", "Agentforce, Flow, Apex, Digital Engagement, 10 PAs", "~R$ 715/h"],
        ["Developer Marketing Cloud", "Journey Builder, disparos WhatsApp, régua de cobrança", "~R$ 715/h"],
        ["Project Manager", "Gestão proporcional às horas dos devs", "A confirmar"],
    ], [4.5*cm, 7.5*cm, 4.5*cm]),
    sp(),
    h2("9.3 Sizing de Volumes"),
    table([
        ["Volume", "Qtd", "Período"],
        ["Msgs WhatsApp proativas (régua)", "4.860.000", "Ano"],
        ["Msgs WhatsApp proativas (régua)", "405.000", "Mês"],
        ["Msgs WhatsApp proativas (régua)", "13.500", "Dia"],
        ["Conversas chatbot inbound", "400.000", "Ano"],
        ["Conversas chatbot inbound", "33.333", "Mês"],
        ["Posições de atendimento humano", "10 PAs", "—"],
    ], [8*cm, 4*cm, 4.5*cm]),
    sp(),
    h2("9.4 Próximos Passos ROM"),
    b("Nelson e Alex revisam escopo de 800h → confirmam se é compatível com 2 devs + PM em 5 meses"),
    b("Alex comunica retorno a Augusto com valor PS real (sem markup DATAPREV)"),
    b("DATAPREV fecha proposta com CFIN (Coordenadoria de Finanças SEFIN-CE)"),
    b("Avaliar expansão do modelo para PGM (Procuradoria Geral do Município) e CMF"),
    sp(),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════════════════════
# 10. PRÓXIMOS PASSOS
# ═══════════════════════════════════════════════════════════════════════════════
story += [
    h1("10. PRÓXIMOS PASSOS E RESPONSÁVEIS"),
    sp(),
    table([
        ["Ação", "Responsável", "Status"],
        ["Osvaldo envia documentação APIs para Alex e Nelson", "Osvaldo Melo", "✅ 01/07/2026"],
        ["Fluxo de atendimento v1.0 validado", "Nelson", "✅ 02/07/2026"],
        ["Revisar escopo 800h e confirmar valor PS real com Alex", "Nelson + Alex", "🔴 Urgente"],
        ["Alex comunica retorno a Augusto com valor e escopo", "Alex Siqueira", "🔴 Urgente"],
        ["Enviar perguntas Q-A a Q-K para DATAPREV / SEFIN-CE", "Nelson / Augusto", "⏳ Pendente"],
        ["Preparar ROM definitivo para DATAPREV fechar com CFIN", "Nelson", "⏳ Pendente"],
        ["Avaliar expansão PGM e CMF (mesmo modelo)", "Augusto + Alex", "⏳ Futuro"],
    ], [7*cm, 4*cm, 5.5*cm]),
    sp(),
    hr(),
    sp(),
    Paragraph(
        "Documento gerado em 02/07/2026  |  Salesforce Professional Services LATAM  |  "
        "DTP-SEFIN-CE  |  Uso restrito ao time de projeto.",
        footer_s),
]

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
print(f"Tamanho: {os.path.getsize(OUTPUT)/1024/1024:.1f} MB")
