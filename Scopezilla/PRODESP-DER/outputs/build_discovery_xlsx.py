# -*- coding: utf-8 -*-
"""Gera o Guia de Discovery Profundo (PRODESP-DER / DER-SP) em .xlsx."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

OUT_PATH = "/Users/nfilho/claude/Scopezilla/PRODESP-DER/outputs/scoping-deliverables.xlsx"

# ---------- estilos ----------
NAVY = "16325C"
GOLD = "FFB81C"
LIGHT = "EEF2F7"
WHITE = "FFFFFF"

header_font = Font(name="Calibri", size=11, bold=True, color=WHITE)
header_fill = PatternFill("solid", fgColor=NAVY)
block_font = Font(name="Calibri", size=10, bold=True, color=NAVY)
block_fill = PatternFill("solid", fgColor=LIGHT)
title_font = Font(name="Calibri", size=16, bold=True, color=NAVY)
subtitle_font = Font(name="Calibri", size=11, italic=True, color="555555")
body_font = Font(name="Calibri", size=10)
wrap = Alignment(wrap_text=True, vertical="top")
wrap_center = Alignment(wrap_text=True, vertical="center", horizontal="center")
thin = Side(style="thin", color="D0D0D0")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def style_header(ws, row, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = wrap_center
        cell.border = border

def write_question_sheet(wb, name, columns, widths, blocks, freeze="A2"):
    ws = wb.create_sheet(name)
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.append(columns)
    style_header(ws, 1, len(columns))
    ws.freeze_panes = freeze
    ws.auto_filter.ref = f"A1:{get_column_letter(len(columns))}1"
    r = 2
    n = 1
    for block_name, rows in blocks:
        ws.cell(row=r, column=1, value=block_name)
        ws.cell(row=r, column=1).font = block_font
        ws.cell(row=r, column=1).fill = block_fill
        for c in range(2, len(columns) + 1):
            ws.cell(row=r, column=c).fill = block_fill
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(columns))
        r += 1
        for row in rows:
            ws.cell(row=r, column=1, value=n)
            for c, val in enumerate(row, start=2):
                cell = ws.cell(row=r, column=c, value=val)
                cell.alignment = wrap
                cell.font = body_font
                cell.border = border
            ws.cell(row=r, column=1).alignment = wrap_center
            ws.cell(row=r, column=1).font = body_font
            ws.cell(row=r, column=1).border = border
            n += 1
            r += 1
    return ws

wb = openpyxl.Workbook()
wb.remove(wb.active)

# =========================================================================
# SHEET 0 — CAPA / INSTRUÇÕES
# =========================================================================
ws0 = wb.create_sheet("Capa")
ws0.column_dimensions["A"].width = 110
ws0.sheet_view.showGridLines = False

ws0["A1"] = "PRODESP-DER — Guia de Discovery Profundo"
ws0["A1"].font = Font(name="Calibri", size=20, bold=True, color=NAVY)
ws0["A2"] = "Field Service + Agentforce via WhatsApp — Atendimento de Ocorrências em Rodovia (DER-SP)"
ws0["A2"].font = Font(name="Calibri", size=13, color="333333")
ws0["A3"] = f"Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} — Scopezilla / PRODESP-DER"
ws0["A3"].font = subtitle_font

intro = [
    "",
    "COMO USAR ESTE GUIA",
    "Este guia foi construído a partir do documento de POC (\"Sistema de Gestão de Atendimento de Ocorrências "
    "em Rodovia — DER-SP\", v01 de 20/08/2026) e é destinado às sessões de discovery profundo que seguem a POC "
    "desta semana. Ele NÃO substitui a conversa — é um roteiro de perguntas que amplia o que a POC já definiu, "
    "cobre padrões de indústria de Field Service, os pontos que sempre validamos em projetos de setor público, "
    "e os riscos que mais comprometem esse tipo de operação.",
    "",
    "ABAS DESTE ARQUIVO",
    "1. Discovery — MVP Atendimento Emergencial: aprofunda exatamente o que a POC descreve (fluxo, despacho, "
    "status, canais, dados, KPIs) — o que já está confirmado no documento e o que ainda precisa de validação "
    "para ir de POC a produção real.",
    "2. Discovery — Field Service (Indústria): casos de uso padrão de Field Service que normalmente aparecem "
    "em operações de manutenção/atendimento em campo e que podem entrar em ondas futuras (conservação de "
    "rodovia, inspeções programadas, gestão de frota/equipes terceirizadas).",
    "3. Discovery — Agentforce & WhatsApp: perguntas específicas do canal conversacional — provisionamento, "
    "handoff humano, guardrails, consentimento, continuidade de sessão.",
    "4. Discovery — Setor Público (padrão): bloco de perguntas que aplicamos em todo projeto de setor público "
    "(governança, LGPD, licitação, acessibilidade, integração com outros órgãos, continuidade de serviço "
    "essencial).",
    "5. Riscos: matriz de risco potencial com pergunta de validação para cada risco — cobre os riscos já "
    "citados na POC (matriz de risco por cenário, alarme de 5 min) e riscos adicionais de escala, dados e "
    "governança.",
    "6. Roadmap — Catálogo DER: mapeamento indicativo de TODOS os serviços listados na Carta de Serviços do "
    "DER-SP, agrupados em ondas de discussão a partir do MVP (atendimento emergencial). É um mapa de discussão "
    "para orientar o roadmap, não um cronograma comprometido — sequenciamento, prazos e equipe são definidos "
    "depois, com as skills de roadmap/estimate.",
    "",
    "LEGENDA",
    "'Confirmado na POC' = a POC já responde isso explicitamente. 'A validar' = a POC assume ou não define; "
    "precisa confirmação do DER na sessão. 'Gap' = não aparece na POC e é um ponto novo a explorar.",
]
r = 5
for line in intro:
    cell = ws0.cell(row=r, column=1, value=line)
    if line.isupper() or (line and line == line.upper() and len(line) < 60 and not line.startswith(("1.", "2.", "3.", "4.", "5.", "6."))):
        cell.font = Font(name="Calibri", size=12, bold=True, color=NAVY)
    else:
        cell.font = body_font
        cell.alignment = wrap
    r += 1

# =========================================================================
# SHEET 1 — MVP ATENDIMENTO EMERGENCIAL (grounded na POC)
# =========================================================================
cols_mvp = ["Nº", "Bloco", "Pergunta de Discovery", "Por que perguntamos",
            "Status na POC", "Resposta do DER (sessão)", "Observações"]
widths_mvp = [5, 4, 45, 42, 16, 30, 30]
# columns order handled by write_question_sheet: first col Nº is auto; we pass columns w/o Nº duplication
cols_mvp2 = ["Bloco", "Pergunta de Discovery", "Por que perguntamos", "Status na POC",
             "Resposta do DER (sessão)", "Observações"]
widths2 = [4, 22, 46, 42, 16, 30, 30]

blocks_mvp = [
("A. Escopo e Objetivo do Atendimento Emergencial", [
    ["A POC cobre hoje apenas Guincho Leve e Inspeção. Quais outros recursos de emergência viária existem no DER (guincho pesado, ambulância/resgate, sinalização de emergência, remoção de carga, viatura de fiscalização) e em que ordem entram depois da POC?", "Define o roadmap de recursos pós-POC — a regra de despacho (aderência/disponibilidade/proximidade) precisa escalar para N tipos de recurso, não só 2.", "Confirmado na POC (só 2 recursos testados)", "", ""],
    ["O DER opera a conservação/socorro mecânico com equipe própria, terceirizada ou mista (concessionárias, empresas de guincho contratadas)?", "Muda o modelo de dados de 'Recurso/Operador' (é funcionário DER ou prestador?) e o modelo de SLA/contrato que a solução precisa refletir.", "Gap — não mencionado na POC", "", ""],
    ["Qual é a meta de cobertura da malha viária estadual (km de rodovia, nº de trechos, DRs envolvidas) para a fase pós-POC?", "Dimensiona o salto de 'ambiente reduzido de teste' para operação real — volume de ocorrências e recursos simultâneos.", "A validar — POC só cita 'número reduzido'", "", ""],
    ["Existe hoje algum sistema ou processo de atendimento emergencial em operação que este projeto substitui ou complementa (planilha, sistema legado, rádio/telefonia pura)?", "Se há sistema legado, entra migração de dados/histórico e período de transição/paralelo; se não há, é greenfield.", "Gap — não mencionado na POC", "", ""],
]),
("B. Canais de Abertura de Ocorrência", [
    ["Confirmar: o WhatsApp será o canal primário de abertura pelo usuário na POC — qual o número/linha que será usado e já existe conta WhatsApp Business API ou é preciso provisionar?", "Provisionamento de WhatsApp Business API (Meta) tem lead time próprio e depende de aprovação de template de mensagem — pode ser bloqueador de cronograma da POC.", "Confirmado na POC (canal = WhatsApp)", "", ""],
    ["Como o usuário chega ao número de WhatsApp (placa/QR nas rodovias, número já divulgado, SAU 0800 atual, integração com Waze/apps de navegação)?", "Define a estratégia de divulgação e adoção do canal — sem isso, o volume real de uso é imprevisível mesmo com o sistema pronto.", "Gap — não mencionado na POC", "", ""],
    ["Ligação e SMS aparecem como canais da 'versão full' da ferramenta — confirmar se entram na POC ou só na fase seguinte, e se há uma central telefônica (URA/PABX) já existente para integrar.", "A POC pode ficar limitada a WhatsApp por licenciamento; isso precisa estar claro para não gerar expectativa equivocada nos testes.", "A validar — POC condiciona a canais 'disponíveis na versão full'", "", ""],
    ["O usuário pode abrir ocorrência anonimamente (sem identificar-se) ou o DER exige identificação mínima sempre (nome, telefone, placa)?", "Afeta o modelo de qualificação minimamente obrigatório e casos de uso de terceiros reportando acidente que não são o próprio envolvido.", "Confirmado na POC (nome, telefone, localização, veículo, placa) — validar obrigatoriedade", "", ""],
]),
("C. Qualificação e Triagem da Ocorrência", [
    ["A qualificação via WhatsApp hoje é conversacional (o Agentforce pergunta e extrai) ou existe também abertura por menu/botões estruturados? Qual o nível de tolerância a informação incompleta antes de escalar para o C2C?", "Define o desenho do agente conversacional — quão autônomo ele pode ser antes de precisar de um humano no loop, crítico em cenário de emergência.", "A validar — POC define os dados mínimos, não o mecanismo de coleta", "", ""],
    ["Quais tipos de ocorrência além de pane mecânica/elétrica, pane seca, pneu furado e sinistro devem ser classificados (ex: animal na pista, objeto na pista, incêndio em veículo, atropelamento, ocorrência com produto perigoso)?", "A POC lista uma matriz de risco parcial (documento cita explicitamente que não é completa) — a classificação completa afeta a regra de despacho e a integração com outros órgãos.", "A validar — POC afirma explicitamente que a matriz de risco 'não é completa'", "", ""],
    ["Como o sistema deve tratar um relato de vítima ou risco à vida (sinistro com ferido) — há triagem diferenciada e acionamento automático de terceiros (SAMU/Bombeiros) ou isso permanece manual pelo C2C?", "É o cenário de maior risco operacional e legal da solução — decide se o sistema é só de gestão de recursos DER ou também um ponto de triagem de emergência de vida.", "Gap — POC trata 'sinistro' como tipo de ocorrência, não fala de vítimas", "", ""],
    ["O reconhecimento automático de telefone e geolocalização via WhatsApp (mencionado na POC) depende de o usuário compartilhar localização no app — o que ocorre quando ele não compartilha ou está sem sinal de GPS?", "Fallback de qualificação por referência textual (km, sentido, ponto de referência) precisa existir — comum em rodovia com sinalização de km.", "Confirmado na POC (aproveitamento automático 'quando disponível') — validar fallback", "", ""],
]),
("D. Cadastro e Gestão de Recursos (VTRs)", [
    ["Como é hoje o controle de disponibilidade dos guinchos/veículos de inspeção (escala de turno, pausas, manutenção do próprio veículo) fora da POC?", "A POC menciona 'controles de abertura de turno e pausas' no modelo de dados, mas não descreve a regra de negócio de escala — precisa ser desenhada.", "A validar — citado no modelo de dados, sem regra definida", "", ""],
    ["Cada recurso pertence a uma base fixa (garagem/pátio) com raio de atuação, ou circula livremente pela malha viária sendo despachado por proximidade real-time?", "Define se 'distância/tempo estimado' (Critério 1 do despacho) é calculado a partir de base fixa ou posição GPS ao vivo — impacta a precisão do algoritmo de despacho.", "A validar — POC assume 'posição atual' via geolocalização, não descreve base", "", ""],
    ["Quantos operadores de campo e VTRs reais existem hoje por Divisão Regional, para dimensionar a operação pós-POC?", "Sem esse número, não é possível avaliar se o algoritmo de despacho e o dashboard aguentam o volume real (a POC é 'ambiente reduzido').", "Gap — não mencionado na POC", "", ""],
    ["Existe equipamento de rastreamento GPS já instalado nos veículos (telemetria/GPS veicular) ou o rastreamento dependerá só do celular/app do operador de campo?", "Define se a geolocalização vem de hardware veicular (mais confiável, cobertura em túneis/serra) ou só do app mobile (depende de sinal do celular do operador).", "A validar — POC fala em 'posição do recurso' sem especificar a fonte", "", ""],
]),
("E. Regras de Despacho Inteligente", [
    ["O parâmetro N (tempo limite antes de acionar recurso adicional não aderente) — quem no DER tem autoridade para definir/alterar esse valor, e ele deve variar por tipo de ocorrência ou é único para toda a operação?", "A POC deixa explícito que 'o documento de regras de negócio não define seu valor' — é uma decisão de negócio pendente, não uma lacuna técnica.", "A validar — POC declara explicitamente que N está indefinido", "", ""],
    ["A 'matriz de risco definida para priorização dos eventos' citada na POC (usada em caso de saturação/simultaneidade) — existe hoje formalizada em algum documento do DER, ou precisa ser construída durante o discovery?", "Sem essa matriz formal, a lógica de priorização em cenário de múltiplas ocorrências simultâneas (comum em chuva/acidente múltiplo) fica sem base objetiva.", "A validar — POC referencia a matriz mas não a inclui por completo", "", ""],
    ["Quando não há nenhum recurso aderente disponível (ex: só há Guincho Leve e a ocorrência exige Guincho Pesado), qual é o comportamento esperado — fila de espera, transbordo para terceiro/concessionária, ou escalonamento manual ao C2C?", "Cenário de saturação real (rodovia com alta demanda simultânea) não está coberto pela regra N/N-10, que assume que existe recurso não aderente disponível.", "Gap — POC não cobre ausência total de recurso compatível", "", ""],
    ["O direcionamento manual pelo C2C substitui a sugestão automática — existe algum registro/aprovação obrigatória quando o operador C2C sai da recomendação do sistema (para auditoria de por que um recurso mais distante foi escolhido)?", "Importante para governança e auditoria em órgão público — decisões manuais que desviam da lógica automática podem ser questionadas depois (ex: por outro prestador não escolhido).", "Gap — POC permite override manual sem descrever rastreabilidade", "", ""],
]),
("F. Fluxo Operacional e Máquina de Status", [
    ["A máquina de status descrita (Aberto → Em fila → Acionado → Aceito → Iniciado → Concluído → Encerrado) é fixa para todo tipo de ocorrência, ou alguns tipos pulam etapas (ex: ocorrência já resolvida antes da chegada do recurso)?", "Ocorrências resolvidas pelo próprio usuário antes da chegada (ex: pneu trocado por terceiro) precisam de um caminho de cancelamento/encerramento antecipado não descrito na POC.", "Confirmado na POC (máquina de status) — validar exceções", "", ""],
    ["Quando todos os recursos recusam o atendimento e o evento retorna a 'Aberto' (regra descrita na POC), há um limite de re-tentativas antes de escalar para intervenção humana obrigatória do C2C?", "Sem um teto, um evento pode ciclar indefinidamente entre recusas — risco operacional em ocorrência de emergência real.", "A validar — POC descreve o retorno ao status Aberto, não o limite de ciclos", "", ""],
    ["A 'lista de pendências de atendimento' (quando o atendimento não se conclui naturalmente) tem um dono/responsável formal e um SLA de resolução, ou fica só como lista de monitoramento?", "Sem responsável e prazo, pendências podem se acumular sem tratativa — item citado na POC como algo a 'demonstrar', mas sem regra de gestão.", "A validar — POC menciona a lista, não a governança dela", "", ""],
]),
("G. Comunicação entre Atores", [
    ["A comunicação entre C2C e usuário via WhatsApp deve ser em linguagem natural livre (Agentforce responde qualquer pergunta) ou restrita a atualizações de status pré-definidas (template) por causa das regras do WhatsApp Business?", "O WhatsApp Business API exige templates aprovados para mensagens iniciadas pela empresa fora da janela de 24h — isso limita o que pode ser proativo vs. reativo.", "Gap — POC não distingue mensagem livre de template", "", ""],
    ["Quando o Operador de Campo recusa um atendimento, o motivo é sempre em texto livre ou existe uma lista fechada de motivos (para gerar indicador de motivo de recusa)?", "Texto livre não é agregável em dashboard; lista fechada permite indicador de 'motivo de recusa mais comum' — decisão de UX que afeta o relatório gerencial.", "Confirmado na POC (obrigatório registrar motivo) — validar formato", "", ""],
    ["O usuário consegue acompanhar visualmente o deslocamento do recurso em tempo real (mapa) diretamente no WhatsApp, ou isso é uma tela separada (link/mini-app) que o WhatsApp apenas notifica?", "WhatsApp nativamente não renderiza mapa interativo — normalmente isso é um link para uma página/Experience Cloud. Afeta arquitetura e licenciamento.", "Confirmado na POC (o objetivo cita 'acompanhamento visual em tempo real') — validar mecanismo", "", ""],
]),
("H. Geolocalização e Monitoramento de Deslocamento", [
    ["Em trechos de serra, túnel ou zona rural sem cobertura de sinal (comuns na malha estadual), qual o comportamento esperado do alarme de 5 minutos sem atualização de posição — ele deve diferenciar 'sem sinal' de 'parado/inativo'?", "Sem essa distinção, o C2C recebe falso alarme constante em trechos com cobertura ruim, o que gera descrédito no alerta (fadiga de alarme).", "Gap — POC define o alarme mas não trata ausência de sinal", "", ""],
    ["A precisão de localização depende do app mobile do operador — qual dispositivo/OS os operadores de campo usam hoje (smartphone corporativo, BYOD) e há política de conectividade de dados móveis garantida?", "Sem dispositivo/plano de dados padronizado, a confiabilidade do rastreamento em campo (pré-requisito do alarme e do dashboard) fica incerta.", "Gap — não mencionado na POC", "", ""],
]),
("I. Alarmes, Exceções e Auditoria", [
    ["Quem recebe o alarme além do C2C (supervisor/gestor regional) em caso de escalonamento por tempo de atendimento acima da média histórica, e existe SLA de resposta ao alarme pelo próprio C2C?", "A POC cria o alarme mas não define a cadeia de escalonamento quando o C2C não trata a exceção a tempo — risco de alarme sem dono.", "A validar — POC define o alarme, não a escalada", "", ""],
    ["Todo o histórico de status, comunicações e ações (mencionado na POC) precisa ficar disponível para auditoria externa (TCE, Ouvidoria, Controladoria) por quanto tempo, e em que formato de exportação?", "Órgão público tem obrigação de guarda de registros por prazo legal e pode ser auditado — política de retenção de dados não é uma escolha técnica, é requisito de compliance.", "Gap — não mencionado na POC", "", ""],
]),
("J. Dashboard e Indicadores", [
    ["Os indicadores da POC (tempo de resposta, deslocamento, atendimento, TMA, recursos acionados, alarmes, atendimentos por tipo) são consumidos só pelo C2C/Gestor, ou também precisam alimentar relatórios oficiais do DER (ex: Anuário Rodoviário de Acidentes, já publicado no site do DER)?", "Se há obrigação de reporte externo/institucional, o dashboard da POC precisa nascer compatível com esse formato, evitando retrabalho de integração depois.", "Gap — POC não menciona consumo institucional dos indicadores", "", ""],
    ["Há meta/SLA formal de tempo de resposta e atendimento hoje (mesmo que em outro sistema/planilha), para calibrar o que o dashboard deve considerar 'dentro da média' vs. 'alarme'?", "O alarme de tempo de atendimento (regra 9) depende de uma 'média histórica ou meta previamente definida' que a POC cita como configurável mas não informa o valor.", "A validar — POC cita meta configurável sem valor definido", "", ""],
]),
("K. Modelo de Dados e Integrações Externas", [
    ["A POC cita 'verificar a possibilidade' de aproveitar dados de carros inteligentes de montadoras e de outros órgãos (PM, Defesa Civil, Bombeiros) — esse é objetivo da POC atual ou fica para uma fase 2 de integração?", "Integrações com terceiros (montadoras, outros órgãos) estão fora do controle direto do DER/Salesforce — dependem de acordo/API externa e não devem ser tratadas como certas para o cronograma da POC.", "Confirmado como intenção futura na POC ('verificar possibilidade') — não é escopo fechado", "", ""],
    ["Existe hoje algum acordo ou canal formal de troca de informação com PM, Corpo de Bombeiros ou Defesa Civil para ocorrências em rodovia, ou isso seria uma integração nova a ser negociada institucionalmente?", "Sem convênio/acordo prévio, essa integração é um risco de escopo e prazo que vai além do que a Salesforce PS controla — precisa ser tratado como dependência externa, não feature.", "Gap — não mencionado na POC", "", ""],
]),
("L. Transição da POC para Produção", [
    ["Quais critérios objetivos o DER vai usar para decidir 'a POC funcionou, seguimos para piloto/produção' — os 12 itens de 'premissas a serem observadas' da POC são o critério final de aceite ou há critérios de negócio adicionais (ex: nº de ocorrências reais atendidas, satisfação do usuário)?", "Sem critério de sucesso combinado, a avaliação de 'viabilidade' citada no objetivo da POC fica subjetiva e pode gerar divergência sobre se a POC foi bem-sucedida.", "A validar — POC lista o que deve ser demonstrado, não o critério de aceite", "", ""],
    ["Qual o licenciamento Salesforce definido ou em avaliação para a fase de produção (a POC já assume que canais completos dependem da 'versão full' da ferramenta)?", "Sem clareza de licenciamento, funcionalidades testadas na POC podem não estar disponíveis na primeira fase real, criando expectativa que a solução não entrega de imediato.", "Confirmado como pendência na própria POC ('próximas etapas recomendadas')", "", ""],
]),
]

write_question_sheet(
    wb, "Discovery - MVP Emergencial",
    ["Bloco", "Pergunta de Discovery", "Por que perguntamos", "Status na POC",
     "Resposta do DER (sessão)", "Observações"],
    [22, 46, 42, 18, 30, 28],
    blocks_mvp,
)

# =========================================================================
# SHEET 2 — FIELD SERVICE (INDÚSTRIA) — ONDAS FUTURAS
# =========================================================================
blocks_fsl = [
("A. Conservação e Manutenção Programada de Rodovia", [
    ["Além do atendimento emergencial reativo, o DER realiza manutenção preventiva/programada da malha (patrolamento, tapa-buraco, roçada, sinalização horizontal/vertical, limpeza de drenagem)? Isso é candidato a uma onda futura de Field Service?", "Caso de uso padrão de Field Service: Work Order programado por ativo (segmento de rodovia) com recorrência — bem diferente do despacho reativo por ocorrência da POC.", "[KA-5937] Field Service — agendamento e despacho padrão", "", ""],
    ["Como é organizado hoje o ciclo de inspeção de pavimento, pontes e estruturas (viadutos, OAEs) — por equipe própria, terceirizada, com que periodicidade e checklist?", "Modelo de 'ativo hierárquico' (rodovia > trecho > km > estrutura) é um padrão de Field Service para gestão de infraestrutura linear — decide se cabe Asset Management do Field Service.", "Padrão de indústria — Field Service Asset Hierarchy para infraestrutura linear", "", ""],
]),
("B. Gestão de Equipes e Terceiros em Campo", [
    ["Equipes de campo trabalham sozinhas (1 operador por VTR) ou em turma/crew (múltiplos operadores, múltiplos veículos por atendimento)? Isso muda a modelagem de 'Recurso' no Field Service (technician único vs. crew-based).", "Field Service nativo assume técnico único por padrão; atendimento crew-based (comum em rodovia — sinalização, guincho + apoio) exige modelagem de Crew/Service Crew.", "[KA-5996] Field Service — ações e notificações por appointment/crew", "", ""],
    ["Empresas terceirizadas (guincho, conservação) teriam usuários e login próprios no sistema, ou apenas recebem acionamento por canal externo (WhatsApp/telefone) sem acesso à plataforma?", "Decide se o modelo de licenciamento inclui usuários externos (portal/Experience Cloud para parceiros) ou se o terceiro é só 'destinatário' de notificação.", "Gap comercial/de licenciamento — não é decisão técnica", "", ""],
]),
("C. Mobilidade e Aplicativo de Campo", [
    ["O operador de campo usará o aplicativo móvel oficial do Field Service (Field Service Mobile) ou uma interface simplificada via WhatsApp/PWA? Há política de dispositivo corporativo definida?", "Field Service Mobile nativo já resolve boa parte do que a POC pede manualmente (aceitar, iniciar, concluir, evidências) — mas exige licenciamento e dispositivo compatível.", "[KA-6546] Field Service Mobile — geolocalização e appointment assistant", "", ""],
    ["Áreas remotas da malha viária têm conectividade de dados intermitente — o app de campo precisa funcionar offline (registrar evidências/status sem sinal e sincronizar depois)?", "Modo offline é um requisito de arquitetura mobile que muda a escolha entre app nativo (com offline-first) e uma solução puramente web/WhatsApp (que exige conectividade constante).", "Padrão de indústria — Field Service Mobile suporta modo offline nativo", "", ""],
]),
("D. Inventário, Peças e Equipamentos", [
    ["Guinchos e viaturas de inspeção carregam peças/insumos (ex: pneu reserva, sinalização de emergência, cones, EPI) cujo controle de estoque hoje é feito como?", "Se há necessidade de rastrear consumo de peças por atendimento, entra o módulo de Inventário/Product Consumed do Field Service — não mencionado na POC.", "Padrão de indústria — Field Service Inventory Management", "", ""],
]),
("E. SLA e Contratos de Serviço", [
    ["Existe algum SLA formal de tempo de atendimento por tipo de ocorrência ou por rodovia/concessão (ex: rodovias com concessão privada podem ter regras próprias) que o sistema precise respeitar e reportar separadamente?", "Diferentes SLAs por contrato/concessão são um padrão de Field Service (Entitlement Management) — decide se o dashboard precisa segmentar por contrato, não só por tipo de ocorrência.", "Padrão de indústria — Field Service Entitlements/Service Contracts", "", ""],
]),
("F. Sazonalidade e Picos de Demanda", [
    ["Períodos de chuva intensa, enchentes ou feriados prolongados geram picos conhecidos de ocorrência — o DER já tem um plano de contingência de reforço de recursos nesses períodos que o sistema deveria refletir (escala especial, recursos extras)?", "Capacidade elástica em picos sazonais é um caso de uso clássico de Field Service (scheduling policies dinâmicas) — se não for planejado, o algoritmo de despacho da POC vai saturar exatamente nos piores momentos.", "Padrão de indústria — Field Service Scheduling Policies / capacity planning", "", ""],
]),
]

write_question_sheet(
    wb, "Discovery - Field Service Ind.",
    ["Bloco", "Pergunta de Discovery", "Por que perguntamos", "Referência / Caso de uso padrão",
     "Resposta do DER (sessão)", "Observações"],
    [30, 46, 42, 34, 28, 26],
    blocks_fsl,
)

# =========================================================================
# SHEET 3 — AGENTFORCE & WHATSAPP
# =========================================================================
blocks_agf = [
("A. Provisionamento e Canal", [
    ["O número de WhatsApp Business já existe e está verificado no Meta Business Manager, ou precisa ser criado do zero? Quem é o responsável institucional por essa conta (DER, PRODESP, terceiro)?", "Verificação de número/conta Meta Business tem prazo próprio (dias a semanas) e pode ser bloqueador de cronograma se não iniciado em paralelo à configuração Salesforce.", "[KA-8087] Rotear WhatsApp via Omni-Channel Flow", "", ""],
    ["Já existem templates de mensagem aprovados pela Meta para notificações proativas (ex: 'seu guincho está a caminho'), ou isso precisa ser submetido e aprovado durante o projeto?", "Mensagens iniciadas pela empresa fora da janela de 24h exigem template pré-aprovado pela Meta — sem isso, atualizações proativas de status não funcionam como a POC descreve.", "[KA-4608] Canais de comunicação do Service — WhatsApp/SMS", "", ""],
]),
("B. Escopo Conversacional do Agente", [
    ["O Agentforce deve conduzir toda a qualificação da ocorrência de forma autônoma, ou apenas capturar dados livres que um humano (C2C) sempre revisa antes da classificação final?", "Define o nível de autonomia do agente — em cenário de emergência, autonomia total tem risco maior de classificação incorreta (ex: confundir gravidade de sinistro).", "Padrão de indústria — desenho de topic/action scope do Agentforce Service", "", ""],
    ["Quais tópicos o agente deve conseguir responder sozinho (status da ocorrência, tempo estimado, reabertura) e em quais ele deve sempre transferir para um humano (reclamação, situação com vítima, dúvida jurídica)?", "Guardrails de escopo evitam que o agente tente responder algo fora de sua competência (ex: questão de multa/CTB) num canal criado para emergência viária.", "Boa prática — Agentforce topic scoping e handoff rules", "", ""],
]),
("C. Handoff Humano e Escalonamento", [
    ["Quando o agente transfere para o C2C, o histórico completo da conversa migra automaticamente para o operador humano, ou o usuário precisa se re-identificar/repetir informações?", "Perda de contexto no handoff é a principal fonte de frustração em canais conversacionais — a POC já exige 'visão única e rastreável', que depende disso.", "Boa prática de UX conversacional — continuidade de contexto no handoff", "", ""],
    ["Existe horário de atendimento humano no C2C (24x7 ou turnos), e o que o agente deve responder ao usuário fora desse horário, considerando que ocorrência de emergência viária tende a ser 24x7?", "Se o C2C não é 24x7 mas o canal aceita abertura a qualquer hora, precisa haver uma resposta clara de expectativa (ex: recursos de plantão reduzido) para não gerar falsa sensação de atendimento imediato.", "Gap — POC não trata cobertura horária do C2C", "", ""],
]),
("D. Identidade, Consentimento e LGPD", [
    ["O número de telefone do WhatsApp é usado para vincular automaticamente ocorrências anteriores do mesmo usuário (histórico)? Se sim, como é obtido o consentimento LGPD para esse tratamento de dado pessoal?", "Dado de geolocalização e telefone são dados pessoais sensíveis sob a LGPD — vinculação automática de histórico exige base legal e aviso de privacidade claro no canal.", "[KA-9528] Public Sector — segurança e compliance", "", ""],
    ["Como o sistema deve tratar denúncias de terceiros que não são o próprio envolvido no sinistro (ex: outro motorista reporta acidente que viu)? A identidade do denunciante é tratada com o mesmo rigor de dado pessoal?", "Amplia o modelo de 'Solicitante' da POC (que assume o próprio usuário abrindo) para um caso de uso de terceiro-denunciante, comum em rodovia.", "Gap — POC assume que o solicitante é o envolvido", "", ""],
]),
("E. Qualidade, Monitoria e Idioma", [
    ["Existe hoje (ou é esperado) volume relevante de usuários que não falam português como língua principal (turistas, motoristas de carga internacional) nas rodovias cobertas pela POC?", "Se sim, entra requisito de multilíngue no agente — não mencionado na POC, mas comum em rodovias de acesso a porto/fronteira.", "Gap — não mencionado na POC", "", ""],
    ["Quem no DER/C2C será responsável por monitorar a qualidade das respostas do agente (QA de conversas, taxa de escalonamento, falsos positivos de classificação) após o go-live?", "Sem um dono de QA conversacional, erros de classificação do agente (ex: pane classificada como sinistro) só são percebidos quando já geraram despacho incorreto.", "Boa prática — governança de Agentforce pós-produção", "", ""],
]),
("F. Continuidade e Multicanalidade", [
    ["Se o usuário iniciar por WhatsApp e depois ligar para o número de telefone do C2C (ou vice-versa), o histórico da ocorrência é o mesmo registro único, ou cria-se um registro novo por canal?", "A POC exige 'identificador único e histórico integral do evento' — isso só se sustenta se a identidade do solicitante for resolvida de forma consistente entre canais (telefone como chave).", "Confirmado como objetivo na POC (identificador único) — validar mecanismo multicanal", "", ""],
]),
]

write_question_sheet(
    wb, "Discovery - Agentforce WhatsApp",
    ["Bloco", "Pergunta de Discovery", "Por que perguntamos", "Referência / Caso de uso padrão",
     "Resposta do DER (sessão)", "Observações"],
    [30, 46, 42, 34, 28, 26],
    blocks_agf,
)

# =========================================================================
# SHEET 4 — SETOR PÚBLICO (PADRÃO PARA TODO PROJETO)
# =========================================================================
blocks_pub = [
("A. Governança e Estrutura Decisória", [
    ["Quem é o sponsor executivo e quem compõe o comitê gestor do projeto dentro do DER? Há um RACI formal entre DER, PRODESP e Salesforce para decisões de escopo?", "Em setor público, decisões de escopo frequentemente dependem de mais de um órgão (DER + PRODESP, nesse caso) — sem RACI claro, aprovações demoram e retrabalham.", "", "", ""],
    ["Existe processo formal de change control para alterações de escopo depois de aprovado (comum em contratos públicos vinculados a termo de referência), e quem assina essa alteração?", "Contratos públicos costumam ter aditivos formais — mudanças de escopo sem esse rito podem gerar questionamento de auditoria (TCE) mais tarde.", "", "", ""],
]),
("B. Compliance, LGPD e Segurança da Informação", [
    ["O DER/PRODESP tem política de segurança da informação e de proteção de dados (LGPD) própria que a solução precisa seguir, além dos requisitos padrão da Salesforce?", "Órgãos estaduais de SP costumam ter norma própria de segurança (ex: vinculada à Secretaria de Governo Digital) que pode impor requisito adicional de hospedagem/criptografia.", "[KA-9528] Public Sector — Security Setup Overview", "", ""],
    ["Dados de ocorrência com potencial de vítima (sinistro) são classificados como dado sensível pela política interna do DER? Há exigência de anonimização em relatórios/dashboards expostos externamente?", "Dado de saúde/acidente pode ser tratado como categoria sensível sob a LGPD, exigindo controle de acesso mais restrito do que dado operacional comum.", "", "", ""],
]),
("C. Contratação, Orçamento e Ciclo de Licitação", [
    ["Este projeto está vinculado a que instrumento contratual (ata de registro de preços, contrato PRODESP-Salesforce, termo de referência específico) e qual o teto orçamentário/fonte de recurso já aprovado para além da POC?", "Define se a evolução da POC para piloto/produção depende de novo processo licitatório ou já está coberta pelo instrumento vigente — decide o timing real do roadmap.", "", "", ""],
    ["Há prazo fiscal (encerramento de exercício, necessidade de empenho) que pressiona quando a fase pós-POC precisa iniciar?", "Orçamento público tem janela de execução por ano fiscal — perder o prazo de empenho pode significar esperar o próximo ciclo orçamentário inteiro.", "", "", ""],
]),
("D. Acessibilidade e Inclusão Digital", [
    ["O canal de WhatsApp/Agentforce precisa suportar usuários com deficiência visual/auditiva ou baixa literacia digital (ex: opção de atendimento por voz/ligação como alternativa ao chat)?", "Serviço público tem obrigação de acessibilidade mais rígida que o setor privado — a POC já prevê ligação e mensagem de voz como canais da versão full, o que ajuda, mas precisa ser confirmado como requisito e não só 'nice to have'.", "", "", ""],
]),
("E. Integração com Sistemas de Governo e Outros Órgãos", [
    ["Além de PM/Bombeiros/Defesa Civil (já citados na POC), há integração esperada com sistemas estaduais como SEI-SP (protocolo), Fala.SP/Ouvidoria, ou o Portal de Serviços ao Cidadão (servicos.sp.gov.br)?", "O DER já opera SEI-SP e Ouvidoria/Fala.SP para outros serviços (visto na Carta de Serviços) — se o atendimento emergencial precisa aparecer nesses canais institucionais, é integração adicional não coberta pela POC.", "", "", ""],
    ["A solução precisa gerar dado aberto (Dados Abertos do DER, já publicados hoje) a partir dos indicadores operacionais do atendimento emergencial?", "Transparência ativa é obrigação legal em vários órgãos estaduais de SP — se o indicador de atendimento emergencial precisa alimentar o portal de dados abertos, isso é requisito de integração/exportação.", "", "", ""],
]),
("F. Continuidade de Serviço Essencial e Disponibilidade", [
    ["Atendimento emergencial em rodovia é considerado serviço essencial 24x7 pelo DER — qual a expectativa de disponibilidade (SLA de uptime) e plano de contingência em caso de indisponibilidade do canal WhatsApp ou da plataforma Salesforce?", "Diferente de um canal de atendimento comercial, uma indisponibilidade aqui tem risco direto à segurança viária — precisa de plano de fallback (ex: retorno a rádio/telefone) formalmente desenhado, não implícito.", "", "", ""],
]),
("G. Mudança, Capacitação e Adoção", [
    ["Os operadores de campo e operadores C2C atuais têm familiaridade com apps móveis/sistemas digitais, ou isso representa uma mudança grande de rotina de trabalho para eles?", "Nível de maturidade digital da força de trabalho de campo define o esforço de capacitação e change management necessário — crítico para adoção real além da POC.", "", "", ""],
    ["Há representação sindical dos operadores de campo que precisa ser informada/consultada sobre mudanças de processo de trabalho (ex: rastreamento de geolocalização do operador)?", "Rastreamento de posição do trabalhador é tema sensível sindicalmente — melhor mapear resistência esperada agora do que depois do go-live.", "", "", ""],
]),
]

write_question_sheet(
    wb, "Discovery - Setor Público",
    ["Bloco", "Pergunta de Discovery", "Por que perguntamos", "Referência",
     "Resposta do DER (sessão)", "Observações"],
    [30, 46, 42, 20, 28, 26],
    blocks_pub,
)

# =========================================================================
# SHEET 5 — RISCOS
# =========================================================================
ws_risk = wb.create_sheet("Riscos")
risk_cols = ["Categoria", "Risco Potencial", "Pergunta de Validação (sessão)", "Por que importa",
             "Sinal de Alerta na Resposta", "Mitigação Possível (indicativa)"]
risk_widths = [20, 34, 46, 40, 34, 34]
for i, w in enumerate(risk_widths, start=1):
    ws_risk.column_dimensions[get_column_letter(i)].width = w
ws_risk.append(risk_cols)
style_header(ws_risk, 1, len(risk_cols))
ws_risk.freeze_panes = "A2"
ws_risk.auto_filter.ref = f"A1:{get_column_letter(len(risk_cols))}1"

risk_rows = [
["Conectividade/Cobertura", "Perda de sinal em trechos de serra/túnel/zona rural gera falso alarme de 'parado' e falha na atualização de posição em tempo real.",
 "Existem trechos conhecidos de baixa cobertura de sinal na malha atendida pela POC/fase 1? Como a operação lida com isso hoje?",
 "O alarme de 5 minutos (regra da POC) dispara em falso continuamente em zonas sem sinal, gerando fadiga de alarme e descrédito do C2C no sistema.",
 "Resposta vaga sobre cobertura de rede ('não sabemos', 'varia muito') sem mapeamento de blackspots.",
 "Diferenciar no design 'sem atualização por falta de sinal' de 'sem atualização por inatividade'; considerar GPS veicular além do celular do operador."],
["Escala POC→Produção", "O algoritmo de despacho e o dashboard testados em ambiente reduzido (poucos usuários/VTRs) não sustentam o volume real da malha estadual completa.",
 "Qual o salto esperado de volume entre o ambiente de teste da POC e a operação real (nº de ocorrências/dia, nº de recursos simultâneos)?",
 "Se o salto for de 1-2 ordens de grandeza, requer validação de performance e possivelmente redesenho de índices/arquitetura antes do rollout.",
 "Ausência de qualquer estimativa de volume real, ou resposta 'vamos descobrir na produção'.",
 "Planejar uma fase piloto intermediária (mais que POC, menos que estadual) antes do rollout total — decisão de roadmap, não de arquitetura."],
["Dados Sensíveis / LGPD", "Dados de sinistro com potencial de vítima, combinados a geolocalização e telefone do solicitante, são tratados como dado sensível sem base legal/consentimento clara.",
 "Existe uma avaliação de impacto à privacidade (DPIA) prevista para este projeto, ou o tratamento de dados pessoais ainda não foi formalmente endereçado?",
 "Sem base legal e política de retenção claras, o projeto corre risco de não conformidade com a LGPD assim que sair de ambiente de teste controlado.",
 "Nenhuma menção a DPO, política de retenção ou base legal quando perguntado diretamente.",
 "Envolver o DPO do DER/PRODESP antes da fase de produção; definir política de retenção e anonimização para relatórios."],
["Dependência de Terceiros", "Integrações com APIs de montadoras (carros inteligentes) e outros órgãos (PM, Bombeiros, Defesa Civil) estão fora do controle direto do projeto e podem não se materializar no prazo esperado.",
 "Há algum acordo, contato ou piloto já em andamento com esses terceiros, ou é uma intenção ainda não iniciada institucionalmente?",
 "Se tratado como 'dado adquirido' no roadmap sem acordo real, gera atraso não controlável pela equipe de implementação.",
 "Resposta do tipo 'ainda não conversamos com eles' quando perguntado sobre o status do acordo.",
 "Tratar como dependência externa explícita no roadmap (marcador de risco), nunca como entrega garantida da fase."],
["Licenciamento", "Canais completos de comunicação (SMS, ligação, ligação por WhatsApp, mensagem de voz) dependem da 'versão full' da ferramenta, ainda não confirmada/contratada.",
 "Qual o licenciamento Salesforce (Service Cloud, Field Service, Agentforce, canais) já contratado ou em processo de aquisição para a fase pós-POC?",
 "Funcionalidades demonstradas na POC podem não estar disponíveis no primeiro go-live real se o licenciamento não acompanhar, quebrando expectativa criada.",
 "Ausência de clareza sobre qual SKU/edição está sendo negociada.",
 "Confirmar o licenciamento-alvo antes de comprometer qualquer canal como parte do MVP de produção."],
["Governança de Despacho", "Overrides manuais do C2C na sugestão automática de despacho não têm rastreabilidade/auditoria formal, expondo o DER a questionamento sobre critério de escolha de prestador.",
 "Como decisões manuais de despacho são hoje documentadas/justificadas (se já existe processo análogo fora do sistema)?",
 "Em órgão público, escolha de prestador fora da regra automática pode ser questionada por concorrentes ou auditoria — falta de registro formal é passivo.",
 "Nenhum processo de justificativa/registro de override mencionado.",
 "Exigir campo obrigatório de justificativa em todo override manual, com trilha de auditoria completa."],
["Continuidade de Serviço", "Atendimento emergencial 24x7 depende de disponibilidade da plataforma e do canal WhatsApp; não há plano de contingência formal para indisponibilidade.",
 "Existe hoje um canal alternativo (rádio, telefone direto) que continua funcionando independente do sistema, para servir de fallback?",
 "Sem fallback formal, uma indisponibilidade do WhatsApp/Salesforce interrompe literalmente o atendimento emergencial na rodovia.",
 "Resposta de que 'o sistema é o único canal' sem mencionar contingência.",
 "Manter e documentar formalmente um canal de fallback (rádio/telefone) como parte do plano de continuidade, não como acidente de arquitetura antiga."],
["Adoção / Change Management", "Resistência de operadores de campo ao rastreamento de geolocalização pessoal e à mudança de rotina de registro manual para digital.",
 "Há experiência anterior de digitalização de processo de campo no DER? Como foi a adoção?",
 "Rastreamento de posição é tema sensível trabalhista/sindical — subestimar a resistência pode comprometer a adoção mesmo com a tecnologia funcionando bem.",
 "Nenhum plano de comunicação/capacitação para operadores mencionado ao ser perguntado.",
 "Plano de change management dedicado aos operadores de campo, com comunicação clara sobre uso do dado de geolocalização."],
["Qualidade do Agente Conversacional", "Classificação incorreta pelo Agentforce (ex: confundir gravidade/tipo de ocorrência) leva a despacho de recurso inadequado em cenário de emergência real.",
 "Quem será o responsável por monitorar e ajustar a qualidade das respostas do agente após o go-live (QA de conversas)?",
 "Sem monitoria contínua, erros de classificação só aparecem quando já causaram atraso ou recurso incorreto no local.",
 "Nenhum dono de QA conversacional identificado.",
 "Definir processo de amostragem e revisão periódica de conversas, com fallback claro para escalonamento humano em caso de baixa confiança."],
["Saturação Simultânea", "Múltiplas ocorrências simultâneas (ex: acidente múltiplo, chuva forte) sem matriz de risco completa geram priorização inconsistente.",
 "Existe hoje (fora do sistema) algum critério de priorização usado em situação de múltiplas emergências simultâneas?",
 "A POC afirma explicitamente que a matriz de risco fornecida não cobre todos os tipos de ocorrência — cenário real de saturação pode não ter regra objetiva.",
 "Resposta indicando que priorização em cenário de saturação é 'sempre decisão do C2C na hora', sem critério registrado.",
 "Formalizar a matriz de risco completa antes do rollout além da POC, com prioridade de negócio explícita por tipo/gravidade."],
]
for row in risk_rows:
    ws_risk.append(row)
    r = ws_risk.max_row
    for c in range(1, len(risk_cols) + 1):
        cell = ws_risk.cell(row=r, column=c)
        cell.alignment = wrap
        cell.font = body_font
        cell.border = border

# =========================================================================
# SHEET 6 — ROADMAP: MAPA DE SERVIÇOS DER (indicativo)
# =========================================================================
ws_rm = wb.create_sheet("Roadmap - Catalogo DER")
rm_cols = ["Onda (indicativa)", "Categoria", "Serviço (Carta de Serviços DER-SP)", "Público-alvo",
           "Canal Atual (hoje)", "Racional da Onda"]
rm_widths = [30, 26, 40, 30, 22, 46]
for i, w in enumerate(rm_widths, start=1):
    ws_rm.column_dimensions[get_column_letter(i)].width = w

ws_rm["A1"] = "Mapa de Serviços do DER-SP — Visão de Roadmap (indicativo, para discussão)"
ws_rm["A1"].font = Font(name="Calibri", size=13, bold=True, color=NAVY)
ws_rm.merge_cells("A1:F1")
ws_rm["A2"] = ("Fonte: Carta de Serviços do DER-SP (https://www.der.sp.gov.br/der/institucional/carta_de_servicos), lida em "
               + datetime.now().strftime("%d/%m/%Y") + ". Este mapa agrupa TODOS os serviços publicados pelo DER em ondas de "
               "discussão a partir do MVP da POC (atendimento emergencial). É uma visão indicativa de escopo/coverage para "
               "orientar a conversa de roadmap — NÃO contém prazos, esforço ou equipe. Sequenciamento real, duração e "
               "recursos são definidos depois, com as skills roadmap/estimate, e dependem de decisão do DER e de "
               "licenciamento.")
ws_rm["A2"].font = Font(name="Calibri", size=9, italic=True, color="666666")
ws_rm["A2"].alignment = wrap
ws_rm.merge_cells("A2:F2")
ws_rm.row_dimensions[2].height = 60

header_row = 4
for i, col in enumerate(rm_cols, start=1):
    cell = ws_rm.cell(row=header_row, column=i, value=col)
ws_rm.append([])  # placeholder not used; we'll write manually below
ws_rm.delete_rows(ws_rm.max_row)  # remove the accidental blank append
style_header(ws_rm, header_row, len(rm_cols))
ws_rm.freeze_panes = f"A{header_row + 1}"
ws_rm.auto_filter.ref = f"A{header_row}:{get_column_letter(len(rm_cols))}{header_row}"

ONDA0 = "Onda 0 — MVP / POC em curso"
ONDA1 = "Onda 1 — Extensão natural do canal (curto prazo)"
ONDA2 = "Onda 2 — Autorizações e trâmites de alto volume"
ONDA3 = "Onda 3 — Trâmites de baixa recorrência / alta complexidade documental"
FORA = "Fora do atendimento ao cidadão (back-office institucional)"

catalog = [
(ONDA0, "Atendimento Emergencial", "Central de Operações e Informações - C2C (atendimento de ocorrências em rodovia)", "Usuário da via / motorista", "WhatsApp (POC) — evolução para full", "Já é o objeto da POC em curso — Guincho Leve e Inspeção."),
(ONDA0, "Atendimento Emergencial", "Contato Emergências", "Usuário da via / motorista", "Telefone / a integrar", "Mesmo domínio de atendimento emergencial do MVP — candidato a unificação de canal com a POC."),

(ONDA1, "Informação de Rodovia em Tempo Real", "Condições das Rodovias", "Usuário da via", "Site / Portal", "Mesma persona (motorista na via) e mesmo canal-alvo (WhatsApp/Agentforce) do MVP — baixo esforço incremental de conteúdo."),
(ONDA1, "Informação de Rodovia em Tempo Real", "Câmeras Online", "Usuário da via", "Site / Portal", "Consulta informativa, sem transação — bom caso de uso conversacional 'onde está o trânsito agora'."),
(ONDA1, "Informação de Rodovia em Tempo Real", "Interdições", "Usuário da via", "Site / Portal", "Informação de alto valor para quem já está na rodovia — mesma jornada do atendimento emergencial."),
(ONDA1, "Informação de Rodovia em Tempo Real", "Radares", "Usuário da via", "Site / Portal", "Consulta informativa recorrente, baixo risco, alto volume esperado — bom para agente autônomo."),
(ONDA1, "Informação de Rodovia em Tempo Real", "Pedágio", "Usuário da via", "Site / Portal", "Consulta informativa — pode reaproveitar a mesma infraestrutura conversacional do MVP."),
(ONDA1, "Informação de Rodovia em Tempo Real", "Web Rotas / Localização", "Usuário da via", "Site / Portal", "Complementa a jornada de 'estou na rodovia, preciso de informação' já atendida pelo MVP."),
(ONDA1, "Informação de Rodovia em Tempo Real", "Balança / Peso Oficial de Veículos de Carga / Pontos de Pesagem", "Transportador", "Site / Portal", "Público correlato (motorista/transportador na via) — avaliar se cabe no mesmo agente ou é persona separada."),

(ONDA2, "Autorizações de Transporte de Carga", "Autorização Especial de Trânsito - AET", "Empresas transportadoras", "Digital (Via Digital)", "Alto volume, já 100% digital — bom candidato a assistente conversacional para status/dúvidas, mantendo o fluxo digital existente."),
(ONDA2, "Autorizações de Transporte de Carga", "Credenciamento para fins de Escolta", "Empresas de escolta", "Digital (Via Digital)", "Mesma família de trâmite da AET — possível reaproveitar o mesmo desenho de agente."),
(ONDA2, "Autorizações de Transporte de Carga", "Autorização para circulação em trechos com restrição (cartão-caminhão)", "Transportadores", "Via postal / Presencial", "Alto volume documental — Agentforce pode orientar documentação e status, reduzindo idas presenciais."),
(ONDA2, "Multas e Recursos", "Indicação de Condutor", "Proprietário de veículo autuado", "Digital (e-Indicação)", "Altíssimo volume e prazo legal apertado (30 dias) — forte candidato a atendimento conversacional guiado."),
(ONDA2, "Multas e Recursos", "Defesa prévia contra autuação de trânsito", "Proprietário / condutor", "Digital (e-Defesa)", "Mesmo domínio de Indicação de Condutor — mesma persona e mesmo canal digital já existente."),
(ONDA2, "Multas e Recursos", "Penalidade de Advertência por Escrito - PAE", "Proprietário / condutor", "Digital (e-PAE)", "Mesma família de trâmites de multa — possível unificar num único fluxo conversacional de 'gestão de multas'."),
(ONDA2, "Multas e Recursos", "Recurso 1ª Instância (JARI)", "Proprietário / condutor", "Digital (e-Recurso)", "Mesma família de trâmites de multa."),
(ONDA2, "Multas e Recursos", "Recurso 2ª Instância (CETRAN)", "Proprietário / condutor", "Digital (e-CETRAN)", "Mesma família de trâmites de multa."),
(ONDA2, "Multas e Recursos", "Restituição de Multa Paga", "Proprietário / condutor", "Digital (e-mail)", "Volume relevante, hoje por e-mail — oportunidade clara de digitalização assistida."),
(ONDA2, "Multas e Recursos", "Baixa de multa por pagamento", "Proprietário do veículo", "Digital (e-mail)", "Trâmite simples e recorrente — bom caso para autoatendimento guiado."),
(ONDA2, "Multas e Recursos", "CADIN Estadual", "Pessoa física/jurídica", "Digital (e-mail)", "Consulta e regularização de pendência — pode ser resolvido conversacionalmente com integração ao sistema de multas."),
(ONDA2, "Multas e Recursos", "Liberação de veículos recolhidos em pátios", "Proprietário do veículo", "Digital", "Urgência do usuário (veículo apreendido) é similar em intensidade ao atendimento emergencial — bom fit de canal WhatsApp."),
(ONDA2, "Canais Institucionais", "Ouvidoria", "Usuário dos serviços do DER", "Digital (ouvidoria.sp.gov.br)", "Alto volume institucional — Agentforce pode triar e direcionar antes de abrir manifestação formal."),
(ONDA2, "Canais Institucionais", "Serviço de Informação ao Cidadão - SIC", "Usuário dos serviços do DER", "Digital (sic.sp.gov.br)", "Mesmo racional da Ouvidoria — triagem conversacional antes do processo formal de LAI."),

(ONDA3, "Faixa de Domínio / Uso do Solo", "Ocupação de Faixa de Domínio", "Órgãos públicos, concessionárias, PJ", "Presencial / Via postal", "Baixo volume, alto valor documental e técnico (projeto de engenharia) — pouco aderente a autoatendimento conversacional."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Credenciamento de empresa para ocupação da faixa de domínio", "PJ / concessionárias", "Digital (e-mail)", "Baixo volume, processo predominantemente documental."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Declaração de área confrontante com a faixa de domínio", "Proprietário de imóvel", "Presencial / Via postal", "Baixo volume, uso jurídico/cartorário — não é caso de uso conversacional natural."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Autorização para Abertura de acesso", "Empresas / proprietários de imóvel", "Presencial / Via postal", "Envolve projeto técnico e análise de engenharia — trâmite de aprovação, não atendimento."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Autorização para implantação de ponto de parada de ônibus", "Permissionárias de transporte / prefeituras", "Presencial / Via postal", "Baixo volume, público institucional (não o cidadão comum da via)."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Instalação de postos de venda de produtos hortifrutigranjeiros", "Produtores rurais", "Presencial / Via postal", "Baixíssimo volume — baixa prioridade para automação."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Credenciamento de empresa para exploração de anúncios", "PJ (empresas de publicidade)", "Digital (SEI-SP)", "Já digitalizado via SEI-SP — integração futura possível, não substituição."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Concessão de licença para exploração de anúncios (painéis)", "PJ (empresas de publicidade)", "Presencial / Via postal", "Processo técnico de engenharia/design — baixa aderência a autoatendimento."),
(ONDA3, "Faixa de Domínio / Uso do Solo", "Autorização para realizar evento na rodovia", "PJ, entidades da sociedade civil", "Presencial / Via postal", "Processo complexo (seguro, caução, plano de segurança viária) — exige análise humana especializada."),
(ONDA3, "Autorizações de Transporte", "Transporte de Trabalhador Rural", "Empresas de transporte rural", "Presencial / Via postal", "Baixo volume, documentação extensa — baixa prioridade."),
(ONDA3, "Autorizações de Transporte", "Credenciamento para fins de vistoria em veículos", "Engenheiros / técnicos credenciados", "Presencial / Via postal", "Público profissional especializado, não o cidadão comum."),
(ONDA3, "Indenizações", "Ressarcimento de danos em veículos (condição da rodovia)", "Usuário lesado", "Presencial / Via postal", "Processo de perícia/orçamento — exige análise humana, mas pode ganhar triagem conversacional inicial."),
(ONDA3, "Indenizações", "Defesa/Recurso — danos ao patrimônio do DER", "Infrator identificado", "Presencial / Via postal", "Baixo volume, natureza jurídico-administrativa."),
(ONDA3, "Desapropriação", "Declaração de inexistência de projeto/processo de desapropriação", "Pessoa física/jurídica", "Digital (SEI-SP)", "Já digitalizado via SEI-SP — integração futura possível."),

(FORA, "Back-office / Institucional", "Contratos e compras públicas, licitações, obras públicas (Transparência)", "Órgãos de controle, sociedade civil", "Portal de Transparência", "Não é atendimento ao cidadão-usuário da via — é publicação institucional obrigatória, fora do escopo de Field Service/Agentforce."),
(FORA, "Back-office / Institucional", "Financeiro (cauções, notas fiscais, pagamento a fornecedores)", "Fornecedores do DER", "Sistemas internos", "Processo interno de gestão financeira — não é serviço ao cidadão."),
(FORA, "Back-office / Institucional", "Leilão de veículos", "Público em geral / arrematantes", "Digital / Presencial", "Processo pontual e específico, sem relação com atendimento em rodovia."),
(FORA, "Back-office / Institucional", "Servidores públicos (diárias, remuneração)", "Servidores do DER", "Portal de Transparência", "Transparência de gestão de pessoal — não é serviço ao cidadão-usuário."),
]

r = header_row + 1
for row in catalog:
    for c, val in enumerate(row, start=1):
        cell = ws_rm.cell(row=r, column=c, value=val)
        cell.alignment = wrap
        cell.font = body_font
        cell.border = border
    r += 1

wb.save(OUT_PATH)
print(f"OK -> {OUT_PATH}")
print(f"Sheets: {wb.sheetnames}")
