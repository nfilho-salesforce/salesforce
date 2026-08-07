#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstrói data-agil-rom.html a partir de data-agil-rom-LIVE-base.html
   aplicando a revisão de escopo (15 jornadas, R$5M, Ago-Dez 2026)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "data-agil-rom-LIVE-base.html")
OUT  = os.path.join(HERE, "data-agil-rom.html")

orig = open(BASE, encoding="utf-8").read().split("\n")

# ─────────────────────────────────────────────────────────────
# Helpers de fluxo de jornada
# ─────────────────────────────────────────────────────────────
ARROW = '<div style="display:flex;align-items:center;flex-shrink:0;color:var(--text-muted);font-size:13px;padding:0 3px;">→</div>'

CENA_LABEL = ['Gatilho', 'No canal', 'O agente', 'Bastidor', 'Resultado']

def flow(steps, sei=False):
    pal = [
        ('#EFF6FF', '#BFDBFE', '#1E40AF', '#3B82F6'),
        ('#F3E8FF', '#D8B4FE', '#7E22CE', '#9333EA'),
        ('#EFF6FF', '#BFDBFE', '#071D41', '#636363'),
        ('#CFFAFE', '#67E8F9', '#0E7490', '#06B6D4'),
        ('#DCFCE7', '#86EFAC', '#168821', '#16A34A'),
    ]
    if sei:
        pal[3] = ('#FFF6E0', '#F3C766', '#8A5300', '#A9720B')
        pal[4] = ('#FFF6E0', '#F3C766', '#8A5300', '#A9720B')
    out = ['<div style="display:flex;align-items:stretch;gap:0;overflow-x:auto;padding-bottom:4px;margin-bottom:14px;">']
    for i, (emoji, title, desc) in enumerate(steps):
        bg, bd, tc, dc = pal[i]
        r = 'border-radius:8px 0 0 8px;' if i == 0 else ('border-radius:0 8px 8px 0;' if i == len(steps) - 1 else '')
        cena = CENA_LABEL[i] if i < len(CENA_LABEL) else ''
        out.append(
            f'<div style="flex-shrink:0;background:{bg};border:1px solid {bd};{r}padding:11px 13px;min-width:118px;text-align:center;position:relative;">'
            f'<div style="display:flex;align-items:center;justify-content:center;gap:5px;margin-bottom:4px;">'
            f'<span style="width:16px;height:16px;border-radius:50%;background:{tc};color:#fff;font-size:9.5px;font-weight:800;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;">{i+1}</span>'
            f'<span style="font-size:8.5px;font-weight:800;letter-spacing:.4px;text-transform:uppercase;color:{dc};">{cena}</span></div>'
            f'<div style="font-size:17px;margin-bottom:3px;">{emoji}</div>'
            f'<div style="font-size:10.5px;font-weight:700;color:{tc};">{title}</div>'
            f'<div style="font-size:10.5px;color:{dc};margin-top:3px;">{desc}</div></div>')
        if i < len(steps) - 1:
            out.append(ARROW)
    out.append('</div>')
    return ''.join(out)

def ul(items):
    return '<ul style="font-size:12.5px;color:var(--text-main);margin:0;padding-left:16px;">' + ''.join(f'<li style="margin-bottom:4px;">{x}</li>' for x in items) + '</ul>'

def card(j):
    accent = {1: 'var(--green-dark)', 2: 'var(--blue-accent)', 3: 'var(--purple)'}[j['onda']]
    ondapill = {1: ('pill-green', 'Onda 1 · Quick Win'), 2: ('pill-blue', 'Onda 2 · Expansão'), 3: ('pill-purple', 'Onda 3 · Escrita/Gov')}[j['onda']]
    boxbg = {1: '#E6F9EF', 2: 'var(--blue-light)', 3: '#F3E8FF'}[j['onda']]
    sei_pill = '<span class="pill" style="background:#FFF6E0;color:#8A5300;border:1px solid #F3C766;">📑 SEI</span>' if j.get('sei') else ''
    valor_pill = f'<span class="pill" style="background:#FEF6DF;color:#8A5300;border:1px solid #F3C766;">💰 {j["valor"]}</span>'
    pd = j['pd']
    persona_band = f'''
        <div style="background:{boxbg};border:1px solid {accent};border-radius:12px;padding:14px 16px;margin-bottom:16px;">
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:12px;">
            <div style="width:46px;height:46px;background:#fff;border:2px solid {accent};border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;">{pd['avatar']}</div>
            <div style="flex:1;min-width:180px;">
              <div style="font-size:15px;font-weight:800;color:var(--blue-dark);">{pd['nome']}</div>
              <div style="font-size:12px;color:{accent};font-weight:700;">{pd['cargo']}</div>
              <div style="font-size:11.5px;color:var(--text-muted);margin-top:2px;">{pd['ctx']}</div>
            </div>
            <span class="pill pill-gray" style="font-size:10px;">👤 Persona ilustrativa</span>
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;">
            <div style="background:#fff;border-radius:8px;padding:10px 12px;border-top:3px solid {accent};">
              <div style="font-size:10px;font-weight:800;letter-spacing:.4px;color:var(--text-muted);text-transform:uppercase;margin-bottom:4px;">🎯 O que ela(e) quer</div>
              <div style="font-size:12px;color:var(--text-main);">{pd['meta']}</div>
            </div>
            <div style="background:#fff;border-radius:8px;padding:10px 12px;border-top:3px solid #C23934;">
              <div style="font-size:10px;font-weight:800;letter-spacing:.4px;color:var(--text-muted);text-transform:uppercase;margin-bottom:4px;">😖 Dor hoje</div>
              <div style="font-size:12px;color:var(--text-main);">{pd['dor']}</div>
            </div>
            <div style="background:#fff;border-radius:8px;padding:10px 12px;border-top:3px solid #16A34A;">
              <div style="font-size:10px;font-weight:800;letter-spacing:.4px;color:var(--text-muted);text-transform:uppercase;margin-bottom:4px;">✨ Momento de valor</div>
              <div style="font-size:12px;color:var(--text-main);">{pd['ganho']}</div>
            </div>
          </div>
        </div>'''
    return f'''
      <div class="card" style="border-left:5px solid {accent};margin-bottom:16px;">
        <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:14px;">
          <div style="display:flex;align-items:center;gap:12px;">
            <div style="width:40px;height:40px;background:{boxbg};border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;">{j['emoji']}</div>
            <div>
              <div style="font-size:15px;font-weight:800;color:var(--blue-dark);">{j['id']} · {j['title']}</div>
              <div style="font-size:12px;color:var(--text-muted);">{j['subtitle']}</div>
            </div>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span class="pill {ondapill[0]}">{ondapill[1]}</span>
            <span class="pill pill-gray">{j['rw']}</span>
            {sei_pill}
            {valor_pill}
          </div>
        </div>
        {persona_band}
        <div style="font-size:11px;font-weight:800;letter-spacing:.4px;color:var(--text-muted);text-transform:uppercase;margin-bottom:8px;">🎬 O percurso de {pd['nome'].split()[0]}, em 5 cenas</div>
        {flow(j['flow'], sei=j.get('sei', False))}
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px;">
          <div style="background:var(--gray-bg);border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:6px;">ESCOPO &amp; ATIVIDADE</div>
            {ul(j['escopo'])}
          </div>
          <div style="background:var(--gray-bg);border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:6px;">REQUISITOS TÉCNICOS</div>
            {ul(j['requisitos'])}
          </div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:12px;">
          <div style="border:1px solid var(--gray-border);border-radius:8px;padding:10px 12px;">
            <div style="font-size:10.5px;font-weight:700;color:var(--text-muted);margin-bottom:4px;">👥 PÚBLICO</div>
            <div style="font-size:12px;color:var(--text-main);">{j['publico']}</div>
          </div>
          <div style="border:1px solid var(--gray-border);border-radius:8px;padding:10px 12px;">
            <div style="font-size:10.5px;font-weight:700;color:var(--text-muted);margin-bottom:4px;">📌 PREMISSA</div>
            <div style="font-size:12px;color:var(--text-main);">{j['premissa']}</div>
          </div>
          <div style="border:1px solid var(--gray-border);border-radius:8px;padding:10px 12px;">
            <div style="font-size:10.5px;font-weight:700;color:var(--text-muted);margin-bottom:4px;">🎯 PRIORIDADE · VALOR × ESFORÇO</div>
            <div style="font-size:12px;color:var(--text-main);">{j['prioridade']}</div>
          </div>
        </div>
        <div class="quote-block" style="margin:0;">
          <p>{j['persona']}</p>
          <div class="quote-author">{j['autor']}</div>
        </div>
      </div>'''

# ─────────────────────────────────────────────────────────────
# 15 JORNADAS
# ─────────────────────────────────────────────────────────────
J = []

# ---- Onda 1 ----
J.append(dict(id='J1', emoji='💰', title='Consulta Financeira', subtitle='Cliente externo + Interno · Financeiro (Protheus)',
    onda=1, rw='Leitura', valor='R$ 263.158', publico='Diretores financeiros dos órgãos clientes e time comercial interno.',
    premissa='Protheus expõe API de leitura por ID de contrato/órgão; consulta somente do próprio órgão.',
    prioridade='Alto valor (demanda diária), baixo esforço (só leitura). Peso 3.',
    flow=[('🏛️','Cliente','"Quanto devo à Dataprev?"'),('💬','Slack','Canal do órgão'),('🧠','Agentforce','Agente Financeiro'),('🔌','MuleSoft','Consulta Protheus por ID'),('✅','Resposta','Card com posição atualizada')],
    escopo=['Agente especialista Financeiro','Action de consulta de posição/faturas','Card de resposta no canal do órgão'],
    requisitos=['API de leitura do Protheus','Permissão por ID de contrato/órgão','SSO no Slack (perfil externo)'],
    persona='"Muitos clientes questionam diariamente: quanto tá a dívida com a Dataprev, tá aumentando? Não precisam de ofício nem reunião, consultam no canal e o agente retorna."',
    autor='Diretora financeira de órgão cliente'))

J.append(dict(id='J2', emoji='🎫', title='Status de Chamado', subtitle='Cliente externo + Interno · Chamados (service desk)',
    onda=1, rw='Leitura', valor='R$ 263.158', publico='Clientes que abrem chamados e equipes internas de atendimento (N1/N2).',
    premissa='Service desk (Pronto! Cliente) expõe consulta de status por protocolo.',
    prioridade='~30k chamados/mês; deflection alto. Baixo esforço. Peso 3.',
    flow=[('🏛️','Cliente','"Como está o chamado XPTO?"'),('💬','Slack','Canal do órgão'),('🧠','Agentforce','Agente Suporte'),('🔌','MuleSoft','Consulta service desk'),('✅','Resposta','Status, SLA restante, responsável')],
    escopo=['Agente Suporte + extração de protocolo','Action de status + notificação proativa de mudança','Card com SLA e responsável'],
    requisitos=['API de consulta de chamado','Webhook/polling de mudança de status','Mapa de permissões por órgão'],
    persona='"A fila do INSS beira 13 a 14 mil chamados. Escalar pessoas é caro; escalar autoatendimento e triagem inteligente é o caminho sustentável."',
    autor='Pedro Oliveira, DERC · Dataprev'))

J.append(dict(id='SEI-J1', emoji='⏰', title='Alerta de Prazo / cumprimento tácito', subtitle='Interno · SEI (mod-wssei v2 · polling)',
    onda=1, rw='Leitura', valor='R$ 350.877', sei=True, publico='Servidores e responsáveis por processos com prazo no SEI.',
    premissa='Sem push no SEI: alerta depende de polling agendado + cache de estado no MuleSoft/MCP.',
    prioridade='Evita perda por decurso de prazo (risco alto). Esforço médio (polling+lógica). Peso 4.',
    flow=[('👤','Servidor','Processos sob sua responsabilidade'),('💬','Slack','DM proativa'),('🧠','Agentforce','Agente SEI · regra de prazo'),('📑','MuleSoft/MCP','Polling mod-wssei v2'),('✅','Alerta','"Prazo X vence em 2 dias"')],
    escopo=['Agendador de polling + cache de estado','Regra de prazo tácito e antecedência','Alerta proativo no Slack com deep-link'],
    requisitos=['REST mod-wssei v2 (JWT)','Agendador + store de estado','LGPD: só metadados no Slack'],
    persona='"Perder um prazo por decurso tácito custa caro. Um alerta antes do vencimento, no canal que já uso, muda o jogo."',
    autor='Analista de processos · unidade Dataprev'))

J.append(dict(id='SEI-J2', emoji='🔎', title='Consulta em linguagem natural', subtitle='Interno · SEI (mod-wssei v2 · polling)',
    onda=1, rw='Leitura', valor='R$ 350.877', sei=True, publico='Servidores que hoje navegam o SEI manualmente para achar processos.',
    premissa='Consulta traduzida para chamadas mod-wssei; conteúdo sensível via deep-link, não no Slack.',
    prioridade='Reduz tempo de consulta processual (~70%). Esforço médio (NLU→API). Peso 4.',
    flow=[('👤','Servidor','"Onde está o processo 123?"'),('💬','Slack','Mensagem direta'),('🧠','Agentforce','Agente SEI · interpreta'),('📑','MuleSoft/MCP','Consulta mod-wssei v2'),('✅','Resposta','Metadados + link ao SEI')],
    escopo=['Agente SEI com intents de consulta','Mapeamento linguagem natural → endpoints','Resposta com metadados e deep-link'],
    requisitos=['REST mod-wssei v2','Catálogo de endpoints de consulta','Controle de acesso por perfil'],
    persona='"Em vez de abrir o SEI e caçar, pergunto no Slack e recebo o essencial com o link para abrir direto."',
    autor='Servidor · unidade Dataprev'))

J.append(dict(id='SEI-J3', emoji='📬', title='Notificação recebido/tramitado', subtitle='Interno · SEI (mod-wssei v2 · polling)',
    onda=1, rw='Leitura', valor='R$ 263.158', sei=True, publico='Unidades que recebem processos tramitados e precisam reagir a tempo.',
    premissa='Notificação por polling de novas tramitações para a unidade do usuário.',
    prioridade='Encurta o "tempo até saber". Baixo esforço (leitura+polling). Peso 3.',
    flow=[('📑','SEI','Processo tramitado para a unidade'),('📑','MuleSoft/MCP','Polling detecta evento'),('🧠','Agentforce','Agente SEI · monta aviso'),('💬','Slack','Canal da unidade'),('✅','Notificação','"Chegou o processo X"')],
    escopo=['Polling de tramitações por unidade','Deduplicação e cache de eventos','Notificação no canal com link'],
    requisitos=['REST mod-wssei v2','Mapa unidade → canal Slack','Store de estado de eventos'],
    persona='"Hoje descubro que um processo chegou quando abro o SEI. A notificação no canal antecipa a ação."',
    autor='Coordenador de unidade · Dataprev'))

# ---- Onda 2 ----
J.append(dict(id='J3', emoji='📊', title='Briefing de Projeto em Tempo Real', subtitle='Interno (gestores) · Clarity (PPM)',
    onda=2, rw='Leitura', valor='R$ 263.158', publico='Executivos e gestores convocados sem tempo de preparar ponto de controle.',
    premissa='Clarity expõe leitura de status/marcos por projeto; consolidação feita pelo agente.',
    prioridade='Elimina reunião de preparação. Esforço baixo/médio. Peso 3.',
    flow=[('👨‍💼','Executivo','"Como está o projeto X?"'),('💬','Slackbot','DM (texto ou áudio)'),('🧠','Agentforce','Agente Projetos'),('🔌','MuleSoft','Consulta Clarity'),('✅','Resposta','Briefing estruturado em segundos')],
    escopo=['Agente de Projetos/Briefing','Consolidação de status e marcos','Resposta por texto ou áudio no DM'],
    requisitos=['API de leitura do Clarity','Transcrição de áudio (voz→texto)','Perfil de gestor autorizado'],
    persona='"O Maik foi convocado ao ministério sem tempo de ponto de controle. No caminho pergunta como está o projeto, o agente compila do Clarity e ele chega pautado."',
    autor='Pedro Oliveira, DERC · Dataprev'))

J.append(dict(id='J7', emoji='🏠', title='FAQ Interno via Conexão', subtitle='Interno · CRM/Conexão (RAG)',
    onda=2, rw='Leitura (RAG)', valor='R$ 263.158', publico='Empregados com dúvidas de RH/políticas; desonera o time de Pessoas.',
    premissa='Conexão como fonte de verdade; leitura de mão única via API ou índice de busca (RAG).',
    prioridade='Alta frequência, deflection ~50%. Baixo/médio esforço. Peso 3.',
    flow=[('👨‍💼','Empregado','"Quantos dias de licença tenho?"'),('💬','Slack','Slackbot interno'),('🧠','Agentforce','Agente Interno · RAG'),('🏠','Conexão','Leitura do artigo publicado'),('✅','Resposta','Responde com link para a fonte')],
    escopo=['Agente Interno com RAG','Índice de busca (Data Library do Agentforce)','Resposta com citação da fonte'],
    requisitos=['API/busca do Conexão ou crawler de leitura','Índice/embeddings do conteúdo','Curadoria mantida no Conexão'],
    persona='"A informação existe na Conexão. O problema é o acesso: um agente inverte isso e leva a resposta ao empregado no canal que ele já usa."',
    autor='Time de Pessoas · Dataprev'))

J.append(dict(id='SEI-J4', emoji='🗂️', title='Meu painel de processos', subtitle='Interno · SEI (mod-wssei v2 · polling)',
    onda=2, rw='Leitura', valor='R$ 263.158', sei=True, publico='Servidores que precisam da visão consolidada dos seus processos.',
    premissa='Agregação por usuário via polling; visão pessoal montada sob demanda.',
    prioridade='Substitui varredura manual do SEI. Baixo esforço. Peso 3.',
    flow=[('👤','Servidor','"Meus processos abertos"'),('💬','Slack','DM'),('🧠','Agentforce','Agente SEI · agrega'),('📑','MuleSoft/MCP','Consulta por usuário'),('✅','Painel','Lista priorizada com prazos')],
    escopo=['Agregação por usuário/unidade','Ordenação por prazo/prioridade','Card de painel no Slack'],
    requisitos=['REST mod-wssei v2','Vínculo usuário Dataprev ↔ SEI','Cache de estado'],
    persona='"Quero ver num lugar só o que está comigo e o que vence primeiro, sem abrir vários filtros no SEI."',
    autor='Servidor · unidade Dataprev'))

J.append(dict(id='SEI-J5', emoji='📈', title='Digest de unidade', subtitle='Interno (gestor) · SEI (mod-wssei v2 · polling)',
    onda=2, rw='Leitura', valor='R$ 263.158', sei=True, publico='Gestores de unidade que acompanham fluxo e gargalos de processos.',
    premissa='Resumo periódico (diário/semanal) por unidade via polling agregado.',
    prioridade='Visão de gestão sem esforço manual. Baixo esforço. Peso 3.',
    flow=[('📑','SEI','Processos da unidade'),('📑','MuleSoft/MCP','Polling agregado'),('🧠','Agentforce','Agente SEI · sumariza'),('💬','Slack','Canal de gestão'),('✅','Digest','Entradas, pendências, prazos')],
    escopo=['Digest agendado por unidade','Indicadores de fluxo e gargalo','Publicação no canal de gestão'],
    requisitos=['REST mod-wssei v2','Agendador de digest','Mapa unidade → canal'],
    persona='"Todo início de dia quero um resumo da minha unidade: o que entrou, o que está parado, o que vence."',
    autor='Gestor de unidade · Dataprev'))

J.append(dict(id='SEI-J6', emoji='❓', title='"Qual tipo de processo eu uso?" + RAG', subtitle='Interno · SEI + base normativa (RAG)',
    onda=2, rw='Leitura (RAG)', valor='R$ 350.877', sei=True, publico='Servidores em dúvida sobre o tipo/documento correto a abrir.',
    premissa='RAG sobre normas/tipos do SEI; recomendação com citação, sem decidir pelo usuário.',
    prioridade='Reduz erro de enquadramento. Esforço médio (RAG). Peso 4.',
    flow=[('👤','Servidor','"Que tipo uso para X?"'),('💬','Slack','Mensagem direta'),('🧠','Agentforce','Agente SEI · RAG'),('📑','MuleSoft/MCP','Base de tipos/normas'),('✅','Resposta','Tipo sugerido + norma citada')],
    escopo=['Índice RAG de tipos/normas','Agente com recomendação citada','Resposta com link à norma'],
    requisitos=['Base normativa indexada','REST mod-wssei v2 (catálogo de tipos)','Curadoria da base'],
    persona='"Nunca sei se é ofício, memorando ou despacho. Uma recomendação com a norma citada evita retrabalho."',
    autor='Servidor · unidade Dataprev'))

J.append(dict(id='SEI-J7', emoji='✒️', title='Status de assinatura + deep-link', subtitle='Interno · SEI (mod-wssei v2 · polling)',
    onda=2, rw='Leitura', valor='R$ 263.158', sei=True, publico='Quem aguarda assinaturas para dar andamento a um processo.',
    premissa='Status de assinatura por polling; ação de assinar via deep-link no SEI (LGPD).',
    prioridade='Destrava andamento parado por assinatura. Baixo esforço. Peso 3.',
    flow=[('👤','Servidor','"Falta quem assinar o doc?"'),('💬','Slack','DM'),('🧠','Agentforce','Agente SEI'),('📑','MuleSoft/MCP','Status de assinatura'),('✅','Resposta','Pendências + link para assinar')],
    escopo=['Consulta de status de assinatura','Lista de assinantes pendentes','Deep-link para a ação no SEI'],
    requisitos=['REST mod-wssei v2','Mapa de assinantes/perfis','Deep-link autenticado ao SEI'],
    persona='"Preciso saber quem ainda não assinou e mandar um lembrete, sem abrir o SEI a cada meia hora."',
    autor='Servidor · unidade Dataprev'))

# ---- Onda 3 ----
J.append(dict(id='J4', emoji='🗓️', title='Agendamento Inteligente por Voz', subtitle='Interno · Agenda/MS Office/Teams (Graph)',
    onda=3, rw='Escrita', valor='R$ 438.596', publico='Gestores e equipes que agendam reuniões em deslocamento.',
    premissa='Integração Slack ↔ MS Graph com permissão de criar eventos; confirmação humana.',
    prioridade='Tarefa de alto atrito diário. Esforço maior (voz + escrita Graph). Peso 5.',
    flow=[('👨‍💼','Usuário','Áudio: "Agenda com fulano"'),('💬','Slackbot','Voz → texto'),('🧠','Agentforce','Extrai pessoas/horário'),('🔌','MuleSoft','MS Graph · disponibilidade'),('✅','Convite','Sugere janela e cria evento')],
    escopo=['Voz→texto + extração de participantes','Consulta de disponibilidade (Graph)','Criação de convite com confirmação'],
    requisitos=['Integração Slack ↔ MS Graph/Teams','Diretório de usuários via API','Permissão de escrita em calendário'],
    persona='"O chefe pediu para marcar uma agenda. Em vez de repetir \'não esquece\' o caminho todo, mando um áudio no Slack e chego em casa tranquilo."',
    autor='Pedro Oliveira, DERC · Dataprev'))

J.append(dict(id='SEI-J8', emoji='👁️', title='Ciência de documento', subtitle='Interno · SEI (mod-wssei v2 · escrita leve)',
    onda=3, rw='Escrita leve', valor='R$ 350.877', sei=True, publico='Servidores que precisam registrar ciência em documentos.',
    premissa='Escrita leve no SEI (registrar ciência) via ação autenticada; trilha de auditoria.',
    prioridade='Primeira escrita SEI; depende da Fase 0 (G1002). Esforço médio. Peso 4.',
    flow=[('👤','Servidor','"Dar ciência no doc X"'),('💬','Slack','Confirmação da ação'),('🧠','Agentforce','Agente SEI · valida'),('📑','MuleSoft/MCP','Registra ciência (escrita)'),('✅','Confirmação','Ciência registrada + trilha')],
    escopo=['Ação de registrar ciência','Confirmação explícita do usuário','Registro em trilha de auditoria'],
    requisitos=['Endpoint de escrita mod-wssei v2','Governança G1002 concluída (Fase 0)','Auditoria da ação'],
    persona='"Dar ciência é rápido, mas hoje exige abrir o SEI. Confirmar no Slack, com trilha, economiza cliques todo dia."',
    autor='Servidor · unidade Dataprev'))

J.append(dict(id='SEI-J9', emoji='➡️', title='Tramitar via aprovação', subtitle='Interno · SEI (escrita + governança)',
    onda=3, rw='Escrita + Gov', valor='R$ 526.316', sei=True, publico='Servidores e gestores que tramitam processos entre unidades.',
    premissa='Escrita com fluxo de aprovação e governança; ação só após Fase 0 (G1002).',
    prioridade='Alto valor operacional, maior esforço (escrita+aprovação). Peso 6.',
    flow=[('👤','Servidor','"Tramitar para unidade Y"'),('💬','Slack','Fluxo de aprovação'),('🧠','Agentforce','Agente SEI · valida regra'),('📑','MuleSoft/MCP','Tramita (escrita)'),('✅','Confirmação','Tramitado + trilha completa')],
    escopo=['Fluxo de aprovação no Slack','Ação de tramitação autenticada','Governança e trilha de auditoria'],
    requisitos=['Endpoints de escrita mod-wssei v2','Matriz de alçada/aprovação','Governança G1002 (Fase 0)'],
    persona='"Tramitar direto do canal, com a aprovação registrada, elimina idas e vindas e deixa rastro do que foi decidido."',
    autor='Gestor de unidade · Dataprev'))

J.append(dict(id='SEI-J10', emoji='🆕', title='Abrir processo', subtitle='Interno · SEI (escrita + governança)',
    onda=3, rw='Escrita + Gov', valor='R$ 526.316', sei=True, publico='Servidores que iniciam novos processos no SEI.',
    premissa='Abertura assistida com validação de tipo (SEI-J6) e governança; após Fase 0 (G1002).',
    prioridade='Maior esforço (escrita completa + governança). Peso 6.',
    flow=[('👤','Servidor','"Abrir processo do tipo X"'),('💬','Slack','Formulário guiado'),('🧠','Agentforce','Agente SEI · valida tipo'),('📑','MuleSoft/MCP','Cria processo (escrita)'),('✅','Confirmação','Nº do processo + link')],
    escopo=['Formulário guiado (Block Kit)','Validação de tipo/documento','Criação com trilha de auditoria'],
    requisitos=['Endpoints de criação mod-wssei v2','Integração com SEI-J6 (tipos)','Governança G1002 (Fase 0)'],
    persona='"Abrir um processo pelo Slack, com o agente conferindo o tipo, reduz erro e evita reabrir depois."',
    autor='Servidor · unidade Dataprev'))

# ─────────────────────────────────────────────────────────────
# PERSONAS — protagonista nomeado(a) por jornada (ilustrativa)
# nome · cargo · contexto (quem é) · meta (o que quer) · dor (hoje) · ganho (momento de valor)
# ─────────────────────────────────────────────────────────────
PERSONAS = {
    # Onda 1
    'J1': dict(avatar='🏛️', nome='Cláudia Menezes', cargo='Diretora Financeira · órgão cliente da Dataprev',
        ctx='Responde pela posição financeira do órgão junto à Dataprev.',
        meta='Saber a qualquer momento quanto o órgão deve, sem abrir chamado nem pedir ofício.',
        dor='Hoje depende de e-mail e reunião para saber a dívida; a informação chega atrasada.',
        ganho='Pergunta no canal do órgão e recebe o card com a posição atualizada em segundos.'),
    'J2': dict(avatar='🎫', nome='Rafael Torres', cargo='Analista de TI · órgão cliente (abre chamados)',
        ctx='Acompanha os chamados do órgão no service desk da Dataprev.',
        meta='Acompanhar o andamento dos chamados sem ligar para o suporte.',
        dor='Reabre o portal e liga para descobrir SLA e responsável — espera e retrabalho.',
        ganho='Consulta o protocolo no canal e recebe status, SLA restante e responsável.'),
    'SEI-J1': dict(avatar='⏰', nome='Marina Alves', cargo='Analista de Processos · unidade Dataprev',
        ctx='Cuida de processos com prazo legal no SEI.',
        meta='Nunca perder um prazo por decurso tácito.',
        dor='Só percebe um prazo apertado se lembrar de abrir o SEI e checar processo a processo.',
        ganho='Recebe uma mensagem proativa "Prazo X vence em 2 dias" com link direto ao processo.'),
    'SEI-J2': dict(avatar='🔎', nome='Bruno Carvalho', cargo='Servidor · unidade Dataprev',
        ctx='Consulta dezenas de processos por semana no SEI.',
        meta='Achar um processo rápido, sem caçar em filtros do SEI.',
        dor='Abre o SEI e navega vários filtros até localizar o processo certo.',
        ganho='Pergunta em linguagem natural no Slack e recebe os metadados com o link para abrir.'),
    'SEI-J3': dict(avatar='📬', nome='Patrícia Nunes', cargo='Coordenadora de unidade · Dataprev',
        ctx='Recebe processos tramitados para a unidade e precisa reagir a tempo.',
        meta='Reagir assim que um processo chega à unidade.',
        dor='Só descobre que um processo chegou quando abre o SEI.',
        ganho='Recebe a notificação no canal da unidade no instante em que o processo é tramitado.'),
    # Onda 2
    'J3': dict(avatar='📊', nome='Maik', cargo='Gestor de projeto · Dataprev',
        ctx='É convocado a reuniões-relâmpago no ministério, muitas vezes em deslocamento.',
        meta='Chegar às reuniões já pautado sobre o status do projeto.',
        dor='É convocado sem tempo de montar o ponto de controle no Clarity.',
        ganho='No caminho, pergunta por áudio e recebe um briefing consolidado do projeto.'),
    'J7': dict(avatar='🏠', nome='Sofia Ramos', cargo='Empregada · Dataprev',
        ctx='Tira dúvidas de RH e políticas internas com frequência.',
        meta='Resolver dúvidas de RH na hora, no canal que já usa.',
        dor='A resposta existe na Conexão, mas achá-la exige garimpar a intranet.',
        ganho='Pergunta ao Slackbot e recebe a resposta com o link para o artigo-fonte.'),
    'SEI-J4': dict(avatar='🗂️', nome='Diego Farias', cargo='Servidor · unidade Dataprev',
        ctx='Toca vários processos em paralelo e precisa se organizar por prazo.',
        meta='Ver num lugar só o que está com ele e o que vence primeiro.',
        dor='Varre o SEI com vários filtros para montar a visão pessoal.',
        ganho='Pede "meus processos" no Slack e recebe a lista priorizada por prazo.'),
    'SEI-J5': dict(avatar='📈', nome='Helena Prado', cargo='Gestora de unidade · Dataprev',
        ctx='Acompanha o fluxo e os gargalos de processos da sua unidade.',
        meta='Começar o dia com o retrato da unidade — o que entrou, parou e vence.',
        dor='Monta manualmente o panorama de fluxo e gargalos.',
        ganho='Recebe um digest agendado no canal de gestão, sem esforço manual.'),
    'SEI-J6': dict(avatar='❓', nome='Lucas Moreira', cargo='Servidor · unidade Dataprev',
        ctx='Abre processos de tipos variados e nem sempre tem certeza do enquadramento.',
        meta='Abrir o tipo e o documento certos de primeira.',
        dor='Não sabe se é ofício, memorando ou despacho e erra o enquadramento.',
        ganho='Recebe a recomendação do tipo com a norma citada, antes de abrir.'),
    'SEI-J7': dict(avatar='✒️', nome='Fernanda Lima', cargo='Servidora · unidade Dataprev',
        ctx='Depende de assinaturas de terceiros para dar andamento aos processos.',
        meta='Destravar processos parados à espera de assinatura.',
        dor='Abre o SEI de meia em meia hora para ver quem ainda não assinou.',
        ganho='Consulta as pendências e recebe o deep-link para cobrar ou assinar.'),
    # Onda 3
    'J4': dict(avatar='🗓️', nome='Pedro Oliveira', cargo='DERC · Dataprev',
        ctx='Agenda reuniões o dia todo, muitas vezes em trânsito.',
        meta='Marcar reuniões sem parar o que está fazendo.',
        dor='Precisa lembrar de agendar o caminho todo — atrito diário.',
        ganho='Manda um áudio no Slack, o agente sugere a janela e cria o evento.'),
    'SEI-J8': dict(avatar='👁️', nome='André Batista', cargo='Servidor · unidade Dataprev',
        ctx='Registra ciência em documentos com frequência ao longo do dia.',
        meta='Dar ciência em documentos sem abrir o SEI a cada vez.',
        dor='É uma ação simples, mas exige entrar no SEI e navegar até o documento.',
        ganho='Confirma a ciência no Slack, com trilha de auditoria registrada.'),
    'SEI-J9': dict(avatar='➡️', nome='Roberta Dias', cargo='Gestora de unidade · Dataprev',
        ctx='Tramita processos entre unidades e responde por aprovações.',
        meta='Tramitar processos entre unidades com a aprovação registrada.',
        dor='Enfrenta idas e vindas por e-mail e SEI para aprovar e tramitar.',
        ganho='Aprova no fluxo do canal e a tramitação acontece com trilha completa.'),
    'SEI-J10': dict(avatar='🆕', nome='Thiago Nogueira', cargo='Servidor · unidade Dataprev',
        ctx='Inicia novos processos e quer evitar retrabalho de enquadramento.',
        meta='Abrir um processo correto de primeira, sem reabrir depois.',
        dor='Erra o tipo ou o documento e precisa reabrir o processo.',
        ganho='Usa um formulário guiado no Slack, com o agente conferindo o tipo.'),
}
for j in J:
    j['pd'] = PERSONAS[j['id']]

def section_divider(t):
    return f'      <div class="section-divider"><h2>{t}</h2></div>\n'

def onda_intro():
    return '''
      <div class="hero" style="background:linear-gradient(135deg,#071D41 0%,#1a4a8a 50%,#0d6e4e 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">🗺️ 15 jornadas de escopo · 5 agentes + 10 SEI</div>
        <h1 style="font-size:26px;">O escopo completo, <span style="color:#F7C948;">jornada por jornada</span></h1>
        <p class="hero-sub">
          As 15 jornadas priorizadas do DATA ÁGIL, organizadas em três ondas de entrega entre agosto e dezembro de 2026. Cada card traz o fluxo, o escopo e a atividade, os requisitos técnicos, a premissa, o público atendido, o critério de priorização (valor × esforço) e um exemplo com persona. Prioridade = valor ÷ esforço: leitura de alto volume primeiro, escrita e governança por último.
        </p>
        <div class="hero-tags">
          <span class="hero-tag highlight">Onda 1 · Quick Wins (5)</span>
          <span class="hero-tag">Onda 2 · Expansão (6)</span>
          <span class="hero-tag">Onda 3 · Escrita/Gov (4)</span>
        </div>
      </div>

      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px;">
        <div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:8px 14px;">
          <div style="width:12px;height:12px;border-radius:3px;background:var(--green-dark);"></div>
          <span style="font-size:12px;font-weight:700;color:var(--text-main);">Onda 1 · Ago–Set</span>
          <span style="font-size:11px;color:var(--text-muted);">leitura, alto valor / baixo esforço · go-live fim de Set</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:8px 14px;">
          <div style="width:12px;height:12px;border-radius:3px;background:var(--blue-accent);"></div>
          <span style="font-size:12px;font-weight:700;color:var(--text-main);">Onda 2 · Out–Nov</span>
          <span style="font-size:11px;color:var(--text-muted);">leitura + RAG + painéis</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:8px 14px;">
          <div style="width:12px;height:12px;border-radius:3px;background:var(--purple);"></div>
          <span style="font-size:12px;font-weight:700;color:var(--text-main);">Onda 3 · Nov–Dez</span>
          <span style="font-size:11px;color:var(--text-muted);">escrita, voz, governança (após Fase 0)</span>
        </div>
      </div>
'''

jornadas_body = ['    <section class="section" id="jornadas">\n', onda_intro()]
jornadas_body.append(section_divider('Onda 1 · Quick Wins (Ago–Set · go-live fim de Set)'))
for j in J:
    if j['onda'] == 1:
        jornadas_body.append(card(j))
jornadas_body.append(section_divider('Onda 2 · Expansão (Out–Nov)'))
for j in J:
    if j['onda'] == 2:
        jornadas_body.append(card(j))
jornadas_body.append(section_divider('Onda 3 · Escrita, voz e governança (Nov–Dez + hypercare)'))
for j in J:
    if j['onda'] == 3:
        jornadas_body.append(card(j))
jornadas_body.append('\n    </section><!-- /jornadas -->')
JORNADAS = ''.join(jornadas_body)

print("build_page.py: jornadas geradas =", len(J))
open(os.path.join(HERE, "_jornadas_preview.html"), "w", encoding="utf-8").write(JORNADAS)

# ─────────────────────────────────────────────────────────────
# Helpers de formatação
# ─────────────────────────────────────────────────────────────
def brl(n):
    return "R$ " + f"{n:,}".replace(",", ".")

def parse_valor(v):
    return int(v.replace("R$", "").replace(".", "").strip())

WHORAS = {263158: (3, 402), 350877: (4, 537), 438596: (5, 671), 526316: (6, 805)}

TH = 'style="text-align:left;padding:9px 12px;font-size:11px;font-weight:700;color:#fff;background:var(--blue-mid);border:1px solid var(--blue-mid);"'
TDL = 'style="text-align:left;padding:8px 12px;font-size:12.5px;color:var(--text-main);border:1px solid var(--gray-border);"'
TDR = 'style="text-align:right;padding:8px 12px;font-size:12.5px;color:var(--text-main);border:1px solid var(--gray-border);"'
TDC = 'style="text-align:center;padding:8px 12px;font-size:12.5px;color:var(--text-main);border:1px solid var(--gray-border);"'

# ═══════════════════════════════════════════════════════════
# NAV
# ═══════════════════════════════════════════════════════════
NAV = '''  <nav>
    <div class="nav-section-title">Visão Geral</div>
    <a class="nav-item active" onclick="showSection('capa')">
      <span class="icon">🏠</span> Capa &amp; Contexto
      <span class="nav-badge nb-teal">1</span>
    </a>

    <div class="nav-section-title">Diagnóstico</div>
    <a class="nav-item" onclick="showSection('problema')">
      <span class="icon">⚠️</span> O Problema Real
      <span class="nav-badge nb-orange">2</span>
    </a>
    <a class="nav-item" onclick="showSection('whatsapp')">
      <span class="icon">📱</span> Por que não WhatsApp
      <span class="nav-badge nb-yellow">3</span>
    </a>

    <div class="nav-section-title">Solução</div>
    <a class="nav-item" onclick="showSection('arquitetura')">
      <span class="icon">🏗️</span> Arquitetura Macro
      <span class="nav-badge nb-teal">4</span>
    </a>
    <a class="nav-item" onclick="showSection('publicos')">
      <span class="icon">👥</span> Públicos &amp; Demo
      <span class="nav-badge nb-teal">5</span>
    </a>
    <a class="nav-item" onclick="showSection('jornadas')">
      <span class="icon">🗺️</span> 15 Jornadas de Escopo
      <span class="nav-badge nb-green">6</span>
    </a>
    <a class="nav-item" onclick="showSection('sistemas')">
      <span class="icon">🗄️</span> Sistemas &amp; Volumetria
      <span class="nav-badge nb-teal">7</span>
    </a>

    <div class="nav-section-title">Estimativa &amp; ROM</div>
    <a class="nav-item" onclick="showSection('estimativa')">
      <span class="icon">📊</span> Estimativa &amp; Bolsão R$5M
      <span class="nav-badge nb-blue">E1</span>
    </a>
    <a class="nav-item" onclick="showSection('ondas')">
      <span class="icon">📅</span> Ondas Ago–Dez 2026
      <span class="nav-badge nb-teal">E2</span>
    </a>
    <a class="nav-item" onclick="showSection('cronograma')">
      <span class="icon">🗓️</span> Cronograma por Jornada
      <span class="nav-badge nb-blue">E2b</span>
    </a>
    <a class="nav-item" onclick="showSection('perfis')">
      <span class="icon">👤</span> Perfis &amp; Horas
      <span class="nav-badge nb-green">E3</span>
    </a>
    <a class="nav-item" onclick="showSection('comparativo')">
      <span class="icon">⚖️</span> Tradicional × IA-Native
      <span class="nav-badge nb-purple">E4</span>
    </a>
    <a class="nav-item" onclick="showSection('kpis')">
      <span class="icon">🎯</span> KPIs Propostos
      <span class="nav-badge nb-orange">E5</span>
    </a>

    <div class="nav-section-title">Execução</div>
    <a class="nav-item" onclick="showSection('clouds')">
      <span class="icon">☁️</span> Clouds Necessárias
      <span class="nav-badge nb-purple">8</span>
    </a>
    <a class="nav-item" onclick="showSection('hcc')">
      <span class="icon">🔄</span> HCC · Change &amp; UX
      <span class="nav-badge nb-green">9</span>
    </a>
  </nav>'''

# ═══════════════════════════════════════════════════════════
# PROBLEMA · agregação SEI (inserido antes do fechamento)
# ═══════════════════════════════════════════════════════════
PROBLEMA_SEI = '''
      <div class="section-divider"><h2>O caso SEI · o mesmo problema, em escala de processo</h2></div>
      <div class="card" style="border-left:5px solid #C77700;margin-bottom:16px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
          <div style="width:40px;height:40px;background:#FFF6E0;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;">📑</div>
          <div>
            <div style="font-size:15px;font-weight:800;color:var(--blue-dark);">O problema real do SEI não é falta de sistema — é falta de proatividade</div>
            <div style="font-size:12px;color:var(--text-muted);">Sistema Eletrônico de Informações · uso interno intensivo</div>
          </div>
        </div>
        <p style="font-size:13px;color:var(--text-main);margin:0 0 14px;">
          O SEI concentra a vida processual da Dataprev, mas obriga o servidor a <strong>ir até o sistema</strong> para saber o que mudou. Ninguém é avisado quando um processo chega, quando um prazo se aproxima do decurso tácito, ou quando falta uma assinatura. O resultado é o mesmo padrão de escala das demais dores: informação existe, o acesso é reativo e manual.
        </p>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">
          <div style="background:#FFF6E0;border:1px solid #F3C766;border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:#8A5300;margin-bottom:4px;">⏰ PRAZOS TÁCITOS</div>
            <div style="font-size:12px;color:var(--text-main);">Perda por decurso de prazo porque o alerta depende de o servidor lembrar de abrir o SEI.</div>
          </div>
          <div style="background:#FFF6E0;border:1px solid #F3C766;border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:#8A5300;margin-bottom:4px;">🔎 CONSULTA MANUAL</div>
            <div style="font-size:12px;color:var(--text-main);">Achar um processo, ver quem falta assinar ou o que chegou exige navegar filtros — tempo perdido diariamente.</div>
          </div>
          <div style="background:#FFF6E0;border:1px solid #F3C766;border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:#8A5300;margin-bottom:4px;">🔒 SEM PUSH · LGPD</div>
            <div style="font-size:12px;color:var(--text-main);">O mod-wssei v2 não empurra eventos (polling obrigatório) e o conteúdo é sensível — só metadados no Slack, ação via deep-link.</div>
          </div>
        </div>
        <div style="margin-top:14px;background:var(--blue-light);border-left:4px solid var(--blue-accent);border-radius:6px;padding:12px 14px;">
          <strong style="color:var(--blue-dark);font-size:13px;">Diagnóstico:</strong>
          <span style="font-size:13px;color:var(--text-main);"> o SEI vira 10 das 15 jornadas de escopo — cinco de alerta/consulta (leitura, quick win) e cinco de transação (escrita/governança), tratadas na Onda 3 após a Fase 0.</span>
        </div>
      </div>
'''

# ═══════════════════════════════════════════════════════════
# ARQUITETURA · diagrama revisado 3 pilares + SEI
# ═══════════════════════════════════════════════════════════
ARQ_DIAGRAM = '''
      <div class="section-divider"><h2>Arquitetura revisada · 3 pilares + SEI (compartilhável com o cliente)</h2></div>
      <div class="card" style="margin-bottom:16px;">
        <p style="font-size:13px;color:var(--text-main);margin:0 0 16px;">
          Três pilares, uma fundação. O <strong>Slack</strong> é o front conversacional (dois workspaces); os <strong>agentes especialistas (Agentforce)</strong> — um por sistema de origem — interpretam a intenção; e o <strong>MuleSoft</strong> integra e expõe um <strong>MCP server</strong> dos legados. O SEI entra por este mesmo caminho, via REST mod-wssei v2 com <strong>polling</strong>.
        </p>
        <div style="display:flex;flex-direction:column;gap:14px;">
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#F3E8FF;border:1px solid #D8B4FE;border-radius:10px;padding:14px;">
            <div style="font-size:22px;">💬</div>
            <div style="flex:1;min-width:200px;">
              <div style="font-size:13px;font-weight:800;color:#7E22CE;">Pilar 3 · Slack + Slack bot (front conversacional)</div>
              <div style="font-size:12px;color:var(--text-main);">Workspace <strong>interno</strong> (colaboradores + gestores) e workspace <strong>externo</strong> (clientes) — separados pelo compartilhamento de canais públicos.</div>
            </div>
          </div>
          <div style="text-align:center;color:var(--text-muted);font-size:18px;">↓</div>
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:14px;">
            <div style="font-size:22px;">🧠</div>
            <div style="flex:1;min-width:200px;">
              <div style="font-size:13px;font-weight:800;color:#1E40AF;">Pilar 2 · Agentes especialistas (Agentforce)</div>
              <div style="font-size:12px;color:var(--text-main);">Um agente por sistema: Financeiro, Suporte, Projetos, Interno/RH e <strong>Agente SEI</strong>. Cada um com seus tópicos, actions e (quando aplicável) RAG.</div>
            </div>
          </div>
          <div style="text-align:center;color:var(--text-muted);font-size:18px;">↓</div>
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#CFFAFE;border:1px solid #67E8F9;border-radius:10px;padding:14px;">
            <div style="font-size:22px;">🔌</div>
            <div style="flex:1;min-width:200px;">
              <div style="font-size:13px;font-weight:800;color:#0E7490;">Pilar 1 · MuleSoft (integração + MCP server)</div>
              <div style="font-size:12px;color:var(--text-main);">Camada de integração que expõe os legados como MCP server. Para o SEI: agendador de <strong>polling</strong> + cache de estado (não há push/webhook).</div>
            </div>
          </div>
          <div style="text-align:center;color:var(--text-muted);font-size:18px;">↓</div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <div style="flex:1;min-width:120px;text-align:center;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:10px;"><div style="font-size:18px;">💰</div><div style="font-size:11px;font-weight:700;">Protheus</div></div>
            <div style="flex:1;min-width:120px;text-align:center;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:10px;"><div style="font-size:18px;">🎫</div><div style="font-size:11px;font-weight:700;">Service Desk</div></div>
            <div style="flex:1;min-width:120px;text-align:center;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:10px;"><div style="font-size:18px;">📊</div><div style="font-size:11px;font-weight:700;">Clarity</div></div>
            <div style="flex:1;min-width:120px;text-align:center;background:#fff;border:1px solid var(--gray-border);border-radius:8px;padding:10px;"><div style="font-size:18px;">🏠</div><div style="font-size:11px;font-weight:700;">Conexão / MS Graph</div></div>
            <div style="flex:1;min-width:120px;text-align:center;background:#FFF6E0;border:1px solid #F3C766;border-radius:8px;padding:10px;"><div style="font-size:18px;">📑</div><div style="font-size:11px;font-weight:700;color:#8A5300;">SEI · mod-wssei v2</div></div>
          </div>
        </div>
        <div style="margin-top:14px;background:var(--blue-light);border-left:4px solid var(--blue-accent);border-radius:6px;padding:12px 14px;font-size:12.5px;color:var(--text-main);">
          <strong>SEI no fluxo:</strong> leitura por polling agendado (alertas, consultas, painéis); escrita (ciência, tramitação, abertura) somente após a <strong>Fase 0 / G1002</strong>, com confirmação humana e trilha de auditoria. Conteúdo sensível nunca trafega no Slack — apenas metadados + deep-link (LGPD).
        </div>
      </div>
'''

# ═══════════════════════════════════════════════════════════
# PUBLICOS + DEMO merge (substitui fronteira 2217-2221)
# ═══════════════════════════════════════════════════════════
PUBLICOS_MERGE = '''
      <div class="section-divider"><h2>Acessos por público &amp; ambiente Slack</h2></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;">
        <div class="card" style="border-left:5px solid var(--blue-accent);">
          <div style="font-size:14px;font-weight:800;color:var(--blue-dark);margin-bottom:8px;">👥 Público interno · workspace Dataprev</div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:8px;">Colaboradores + gestores</div>
          <ul style="font-size:12.5px;color:var(--text-main);margin:0;padding-left:16px;">
            <li>Acesso completo às 15 jornadas, inclusive as 10 do <strong>SEI</strong> (alertas, consulta, painéis, digest e — após Fase 0 — ciência, tramitação e abertura).</li>
            <li>Vínculo usuário Dataprev ↔ SEI para painel pessoal e alertas de prazo.</li>
            <li>Jornadas internas: Projetos (Clarity), FAQ/RH (Conexão), Agendamento por voz (MS Graph).</li>
          </ul>
        </div>
        <div class="card" style="border-left:5px solid var(--green-dark);">
          <div style="font-size:14px;font-weight:800;color:var(--blue-dark);margin-bottom:8px;">🏛️ Público externo · workspace de clientes</div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:8px;">Órgãos clientes</div>
          <ul style="font-size:12.5px;color:var(--text-main);margin:0;padding-left:16px;">
            <li>Somente jornadas de leitura pertinentes ao próprio órgão: <strong>Consulta Financeira (J1)</strong> e <strong>Status de Chamado (J2)</strong>.</li>
            <li><strong>Sem</strong> acesso a jornadas SEI internas.</li>
            <li>Autenticação por perfil; escopo de dados restrito por ID de contrato/órgão.</li>
          </ul>
        </div>
      </div>
      <div class="card" style="border-left:5px solid var(--slack-purple);margin-bottom:20px;">
        <div style="font-size:14px;font-weight:800;color:var(--blue-dark);margin-bottom:6px;">💬 Ambiente Slack · dois workspaces separados</div>
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">
          Interno e externo são <strong>workspaces distintos</strong> — necessário porque canais públicos são compartilhados dentro do workspace. A separação impede que dados de um cliente fiquem visíveis a outro e isola o ambiente interno da Dataprev. Cada workspace tem seu conjunto de agentes e permissões.
        </p>
      </div>
      <div class="section-divider"><h2>Demo · 3 perfis</h2></div>
'''

# ═══════════════════════════════════════════════════════════
# SISTEMAS · card SEI + volumetria (inserido antes do fechamento)
# ═══════════════════════════════════════════════════════════
SISTEMAS_SEI = '''
      <div class="section-divider"><h2>SEI · Sistema Eletrônico de Informações</h2></div>
      <div class="card" style="border-left:5px solid #C77700;margin-bottom:16px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
          <div style="width:40px;height:40px;background:#FFF6E0;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;">📑</div>
          <div>
            <div style="font-size:15px;font-weight:800;color:var(--blue-dark);">SEI (mod-wssei v2)</div>
            <div style="font-size:12px;color:var(--text-muted);">Fonte de 10 das 15 jornadas · uso interno</div>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">
          <div style="background:var(--gray-bg);border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:4px;">INTEGRAÇÃO</div>
            <div style="font-size:12px;color:var(--text-main);">REST mod-wssei v2 (JWT), ~150+ endpoints (MdWsSeiServicosV2.php). Leitura e escrita.</div>
          </div>
          <div style="background:var(--gray-bg);border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:4px;">PADRÃO DE ACESSO</div>
            <div style="font-size:12px;color:var(--text-main);">Sem push/webhook → <strong>polling obrigatório</strong> + cache de estado no MuleSoft/MCP.</div>
          </div>
          <div style="background:var(--gray-bg);border-radius:8px;padding:12px;">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);margin-bottom:4px;">LGPD</div>
            <div style="font-size:12px;color:var(--text-main);">Somente metadados no Slack; conteúdo do processo via deep-link autenticado ao SEI.</div>
          </div>
        </div>
        <div style="margin-top:12px;background:#FFF6E0;border:1px solid #F3C766;border-radius:8px;padding:12px 14px;font-size:12.5px;color:var(--text-main);">
          <strong style="color:#8A5300;">Volumetria (pendente · gap G1102):</strong> volume de processos/tramitações por unidade a ser fornecido na Fase 0 para dimensionar a frequência de polling e calibrar os KPIs. Frequência de polling define latência percebida vs. custo de chamadas.
        </div>
      </div>
'''

# ═══════════════════════════════════════════════════════════
# CLOUDS (apenas as necessárias)
# ═══════════════════════════════════════════════════════════
CLOUDS = '''    <!-- ══════════════════════════════════════
         SEÇÃO 8, CLOUDS NECESSÁRIAS
    ══════════════════════════════════════ -->
    <section class="section" id="clouds">
      <div class="hero" style="background:linear-gradient(135deg,#071D41 0%,#4A154B 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">☁️ Somente o essencial</div>
        <h1 style="font-size:26px;">Três clouds — <span style="color:#F7C948;">nada além do necessário</span></h1>
        <p class="hero-sub">A solução se apoia em três plataformas. Data Cloud não é obrigatória nesta fase.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:20px;">
        <div class="card" style="border-top:5px solid var(--slack-purple);">
          <div style="font-size:28px;margin-bottom:8px;">💬</div>
          <div style="font-size:16px;font-weight:800;color:var(--blue-dark);">Slack (Grid)</div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px;">Front conversacional · dual-workspace</div>
          <p style="font-size:12.5px;color:var(--text-main);margin:0;">Canais e Slack bot para interno e externo. Licença por usuário/mês. Enterprise Grid habilita múltiplos workspaces com governança central.</p>
        </div>
        <div class="card" style="border-top:5px solid var(--blue-accent);">
          <div style="font-size:28px;margin-bottom:8px;">🧠</div>
          <div style="font-size:16px;font-weight:800;color:var(--blue-dark);">Agentforce (Public Sector)</div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px;">Agentes especialistas</div>
          <p style="font-size:12.5px;color:var(--text-main);margin:0;">Um agente por sistema de origem. Ref.: Public Sector - Service - Agentforce 1 Edition. Data Library cobre o RAG (J7, SEI-J6) sem Data Cloud.</p>
        </div>
        <div class="card" style="border-top:5px solid var(--teal);">
          <div style="font-size:28px;margin-bottom:8px;">🔌</div>
          <div style="font-size:16px;font-weight:800;color:var(--blue-dark);">MuleSoft (Anypoint Titanium)</div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px;">Integração + MCP server</div>
          <p style="font-size:12.5px;color:var(--text-main);margin:0;">Conecta os legados e expõe o MCP server. Ref.: Anypoint Platform Base - Titanium. Suporta o polling e cache de estado do SEI.</p>
        </div>
      </div>
      <div class="card" style="border-left:5px solid var(--yellow);">
        <div style="font-size:13px;font-weight:800;color:var(--blue-dark);margin-bottom:6px;">⚠️ Data Cloud — condicional, fora do escopo base</div>
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">Não é obrigatória nesta fase. O RAG das jornadas J7 e SEI-J6 usa a Data Library do Agentforce. Data Cloud só entra se a volumetria (G1102) exigir indexação/unificação de dados em escala — decisão tomada na Fase 0.</p>
      </div>
    </section><!-- /clouds -->'''

# ═══════════════════════════════════════════════════════════
# HCC · Change & UX
# ═══════════════════════════════════════════════════════════
HCC = '''    <!-- ══════════════════════════════════════
         SEÇÃO 9, HCC · CHANGE & UX
    ══════════════════════════════════════ -->
    <section class="section" id="hcc">
      <div class="hero" style="background:linear-gradient(135deg,#168821 0%,#0C326F 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">🔄 Human Change & Conversational Care</div>
        <h1 style="font-size:26px;">Adoção do Slack + <span style="color:#F7C948;">experiência conversacional</span></h1>
        <p class="hero-sub">A tecnologia entrega valor só se as pessoas usarem e se a conversa for boa. Duas frentes: gestão da mudança para adoção do Slack e desenho de UX/UI conversacional dos agentes e do bot.</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <div class="card" style="border-top:5px solid var(--green-dark);">
          <div style="font-size:16px;font-weight:800;color:var(--blue-dark);margin-bottom:10px;">🚀 Gestão da mudança · adoção do Slack</div>
          <ul style="font-size:12.5px;color:var(--text-main);margin:0;padding-left:16px;">
            <li><strong>Champions por unidade:</strong> multiplicadores que ancoram o hábito de "perguntar no Slack".</li>
            <li><strong>Onboarding por onda:</strong> comunicação e treino no ritmo dos go-lives (Set / Nov / Dez).</li>
            <li><strong>Playbook de canais:</strong> convenções de canais interno/externo, etiqueta e privacidade (LGPD).</li>
            <li><strong>Medição de adoção:</strong> usuários ativos, jornadas resolvidas sem humano, feedback loop.</li>
            <li><strong>Gestão de resistência:</strong> do "abro o sistema" para "pergunto ao agente".</li>
          </ul>
        </div>
        <div class="card" style="border-top:5px solid var(--blue-accent);">
          <div style="font-size:16px;font-weight:800;color:var(--blue-dark);margin-bottom:10px;">🎨 UX/UI conversacional · agentes + bot</div>
          <ul style="font-size:12.5px;color:var(--text-main);margin:0;padding-left:16px;">
            <li><strong>Tom e persona:</strong> voz consistente por agente (Financeiro, Suporte, SEI…), clara e institucional.</li>
            <li><strong>Desenho de diálogo:</strong> intents, desambiguação, fallback e handoff a humano.</li>
            <li><strong>Block Kit:</strong> cards, botões e formulários (ex.: abrir processo SEI-J10) para reduzir atrito.</li>
            <li><strong>Confirmação &amp; confiança:</strong> em escrita (SEI-J8/J9/J10), confirmação explícita + trilha.</li>
            <li><strong>Acessibilidade e voz:</strong> áudio→texto (J3, J4) e respostas legíveis em mobile.</li>
          </ul>
        </div>
      </div>
      <div class="card" style="border-left:5px solid var(--teal);margin-top:16px;">
        <div style="font-size:13px;font-weight:800;color:var(--blue-dark);margin-bottom:6px;">👤 Perfis dedicados no roster</div>
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">Change &amp; Adoption Manager (400h) conduz a frente de mudança; UX Conversacional / Experience Architect (520h) desenha os diálogos e o Block Kit. Ambos atravessam as três ondas.</p>
      </div>
    </section><!-- /hcc -->'''

# ═══════════════════════════════════════════════════════════
# ESTIMATIVA CLUSTER (E1..E5) — gerado
# ═══════════════════════════════════════════════════════════
# E1 — cardápio por onda
def cardapio_rows():
    out = []
    for onda, nome in [(1, "Onda 1 · Ago–Set"), (2, "Onda 2 · Out–Nov"), (3, "Onda 3 · Nov–Dez")]:
        sub = 0
        out.append(f'<tr><td colspan="5" style="padding:7px 12px;font-size:11px;font-weight:800;color:#fff;background:var(--teal);border:1px solid var(--teal);">{nome}</td></tr>')
        for j in J:
            if j['onda'] != onda:
                continue
            v = parse_valor(j['valor'])
            peso, horas = WHORAS[v]
            sub += v
            out.append(f'<tr><td {TDL}>{j["id"]} · {j["title"]}</td><td {TDC}>{peso}</td><td {TDR}>{horas}h</td><td {TDR}><strong>{brl(v)}</strong></td><td {TDC}>{j["rw"]}</td></tr>')
        out.append(f'<tr><td {TDL} style="padding:7px 12px;font-size:12px;font-weight:700;color:var(--blue-dark);border:1px solid var(--gray-border);background:var(--gray-bg);">Subtotal {nome}</td><td {TDC} style="background:var(--gray-bg);border:1px solid var(--gray-border);"></td><td {TDC} style="background:var(--gray-bg);border:1px solid var(--gray-border);"></td><td {TDR} style="padding:7px 12px;font-weight:800;color:var(--blue-dark);border:1px solid var(--gray-border);background:var(--gray-bg);">{brl(sub)}</td><td {TDC} style="background:var(--gray-bg);border:1px solid var(--gray-border);"></td></tr>')
    return "".join(out)

TOTAL = sum(parse_valor(j['valor']) for j in J)

E1 = f'''    <!-- ══════════════════════════════════════
         SEÇÃO E1, ESTIMATIVA & BOLSÃO
    ══════════════════════════════════════ -->
    <section class="section" id="estimativa">
      <div class="hero" style="background:linear-gradient(135deg,#071D41 0%,#1351B4 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">📊 Bolsão fixo · valor por jornada visível</div>
        <h1 style="font-size:26px;">R$ 5,0 milhões, <span style="color:#F7C948;">15 jornadas, uma conta transparente</span></h1>
        <p class="hero-sub">Teto fixo com imposto. O escopo cabe no teto por priorização de ondas — não por corte de qualidade. Cada jornada carrega sua parcela da fundação compartilhada.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px;">
        <div class="card" style="text-align:center;"><div style="font-size:26px;font-weight:900;color:var(--green-dark);">{brl(TOTAL)}</div><div style="font-size:11px;color:var(--text-muted);">teto com imposto</div></div>
        <div class="card" style="text-align:center;"><div style="font-size:26px;font-weight:900;color:var(--blue-accent);">R$ 4.672.500</div><div style="font-size:11px;color:var(--text-muted);">sem imposto (÷0,9345)</div></div>
        <div class="card" style="text-align:center;"><div style="font-size:26px;font-weight:900;color:var(--blue-dark);">~7.650h</div><div style="font-size:11px;color:var(--text-muted);">blended ~R$ 653/h c/imp</div></div>
      </div>
      <div class="section-divider"><h2>O bolsão por dentro · R$ 5 M jornada por jornada</h2></div>
      <div class="card" style="border-left:5px solid var(--blue-accent);margin-bottom:16px;">
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">Cada valor já inclui a parcela proporcional da <strong>plataforma compartilhada</strong> — MuleSoft core + MCP, setup Slack dual-workspace, framework de agentes, Fase 0 (governança G1002), PM, QA, Change e UX baseline. <strong>~45%</strong> de cada número é fundação construída uma vez e reutilizada por todas as jornadas.</p>
      </div>
      <div style="overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;margin-bottom:8px;">
        <thead><tr><th {TH}>Jornada</th><th {TH} style="text-align:center;color:#fff;">Peso</th><th {TH} style="text-align:right;color:#fff;">Horas</th><th {TH} style="text-align:right;color:#fff;">R$ c/imp</th><th {TH} style="text-align:center;color:#fff;">Tipo</th></tr></thead>
        <tbody>
        {cardapio_rows()}
        <tr><td {TDL} style="font-weight:800;color:#fff;background:var(--blue-dark);border:1px solid var(--blue-dark);">TOTAL · 15 jornadas</td><td {TDC} style="font-weight:800;color:#fff;background:var(--blue-dark);border:1px solid var(--blue-dark);">57</td><td {TDR} style="font-weight:800;color:#fff;background:var(--blue-dark);border:1px solid var(--blue-dark);">~7.650h</td><td {TDR} style="font-weight:900;color:#F7C948;background:var(--blue-dark);border:1px solid var(--blue-dark);">{brl(TOTAL)}</td><td {TDC} style="background:var(--blue-dark);border:1px solid var(--blue-dark);"></td></tr>
        </tbody>
      </table>
      </div>
      <p style="font-size:11.5px;color:var(--text-muted);margin-top:6px;">Pesos por drivers de complexidade: leitura simples = 3; leitura + RAG/polling + lógica = 4; voz + escrita MS Graph = 5; escrita SEI + fluxo de aprovação/governança = 6. Valores indicativos para planejamento, sujeitos a calibração no fechamento.</p>
    </section>'''

# E2 — Ondas
def ondas_rows():
    data = [
        ("Fase 0", "Ago", "—", "Governança G1002 (perfis Protheus/SEI, workspace externo, LGPD Art. 48/TCU)", "Gate para escrita SEI"),
        ("Onda 1 · Quick Wins", "Ago–Set", "fim de Set", "J1, J2, SEI-J1, SEI-J2, SEI-J3 (5)", "Leitura · alto valor/baixo esforço"),
        ("Onda 2 · Expansão", "Out–Nov", "fim de Nov", "J3, J7, SEI-J4, SEI-J5, SEI-J6, SEI-J7 (6)", "Leitura + RAG + painéis"),
        ("Onda 3 · Escrita/Transação", "Nov–Dez", "meados de Dez + hypercare", "J4, SEI-J8, SEI-J9, SEI-J10 (4)", "Escrita, voz, governança"),
    ]
    return "".join(f'<tr><td {TDL}><strong>{o}</strong></td><td {TDC}>{jan}</td><td {TDC}>{gl}</td><td {TDL}>{js}</td><td {TDL}>{pf}</td></tr>' for o, jan, gl, js, pf in data)

E2 = f'''    <section class="section" id="ondas">
      <div class="hero" style="background:linear-gradient(135deg,#0C326F 0%,#377EC1 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">📅 Agosto → Dezembro 2026 · ~22 semanas</div>
        <h1 style="font-size:26px;">Três ondas — <span style="color:#F7C948;">valor cedo, risco baixo</span></h1>
        <p class="hero-sub">Prioridade = valor ÷ esforço. Leitura primeiro; escrita e governança por último, após a Fase 0.</p>
      </div>
      <div class="card" style="border-left:5px solid var(--orange);margin-bottom:16px;">
        <div style="font-size:13px;font-weight:800;color:var(--blue-dark);margin-bottom:4px;">🚧 Fase 0 (Agosto · obrigatória)</div>
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">Resolve o bloqueador de governança <strong>G1002</strong> (perfis de acesso Protheus/SEI, aprovação do workspace externo, LGPD Art. 48 / requisitos TCU). É o gate das jornadas de escrita SEI (Onda 3).</p>
      </div>
      <div style="overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;">
        <thead><tr><th {TH}>Onda</th><th {TH} style="text-align:center;color:#fff;">Janela</th><th {TH} style="text-align:center;color:#fff;">Go-live</th><th {TH}>Jornadas</th><th {TH}>Perfil</th></tr></thead>
        <tbody>{ondas_rows()}</tbody>
      </table>
      </div>
    </section>'''

# E3 — Perfis
def perfis_rows():
    data = [
        ("MuleSoft Technical Architect (Sr)", "1", "36", "22", "800", "R$ 614.144"),
        ("MuleSoft Technical Consultant ×2", "1", "40", "22", "1.560", "R$ 974.953"),
        ("Agentforce Specialist / TC ×2", "2", "40", "22", "1.560", "R$ 974.953"),
        ("Solution Architect (Slack/plataforma)", "3", "32", "20", "560", "R$ 413.358"),
        ("UX Conversacional / Experience Architect", "3", "30", "18", "520", "R$ 383.833"),
        ("QA Consultant ×2", "—", "40", "18", "1.293", "R$ 693.552"),
        ("Program Manager", "—", "24", "22", "528→997*", "R$ 735.926"),
        ("Change &amp; Adoption Manager", "—", "18", "16", "400", "R$ 295.256"),
    ]
    return "".join(f'<tr><td {TDL}>{p}</td><td {TDC}>{pi}</td><td {TDC}>{hs}</td><td {TDC}>{sm}</td><td {TDR}>{h}</td><td {TDR}>{c}</td></tr>' for p, pi, hs, sm, h, c in data)

E3 = f'''    <section class="section" id="perfis">
      <div class="hero" style="background:linear-gradient(135deg,#168821 0%,#0C326F 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">👤 Roster Ago–Dez 2026 · regras Dataprev aplicadas</div>
        <h1 style="font-size:26px;">Perfis &amp; horas — <span style="color:#F7C948;">time balanceado</span></h1>
        <p class="hero-sub">Nenhum recurso &lt; 20h/sem · ratio QA (1:2 TC/Dev) · PM ≥ 15% do time · ganho de IA ≥ 25%.</p>
      </div>
      <div style="overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;margin-bottom:8px;">
        <thead><tr><th {TH}>Perfil</th><th {TH} style="text-align:center;color:#fff;">Pilar</th><th {TH} style="text-align:center;color:#fff;">h/sem</th><th {TH} style="text-align:center;color:#fff;">Sem.</th><th {TH} style="text-align:right;color:#fff;">Horas</th><th {TH} style="text-align:right;color:#fff;">Custo c/imp</th></tr></thead>
        <tbody>{perfis_rows()}
        <tr><td {TDL} style="font-weight:800;color:#fff;background:var(--blue-dark);border:1px solid var(--blue-dark);">TOTAL</td><td {TDC} style="background:var(--blue-dark);border:1px solid var(--blue-dark);"></td><td {TDC} style="background:var(--blue-dark);border:1px solid var(--blue-dark);"></td><td {TDC} style="background:var(--blue-dark);border:1px solid var(--blue-dark);"></td><td {TDR} style="font-weight:800;color:#fff;background:var(--blue-dark);border:1px solid var(--blue-dark);">~7.650h</td><td {TDR} style="font-weight:900;color:#F7C948;background:var(--blue-dark);border:1px solid var(--blue-dark);">~R$ 5.000.000</td></tr>
        </tbody>
      </table>
      </div>
      <p style="font-size:11.5px;color:var(--text-muted);">* PM elevado a ~997h para cumprir a regra "PM ≥ 15% do time técnico"; a linha mostra a base operacional (24h/sem) e o ajuste regulatório. Blended ~R$ 653/h c/imp.</p>
    </section>'''

# E4 — Comparativo
E4 = '''    <section class="section" id="comparativo">
      <div class="hero" style="background:linear-gradient(135deg,#7B2FBE 0%,#071D41 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">⚖️ Mandato Dataprev · ganho de IA ≥ 25%</div>
        <h1 style="font-size:26px;">Tradicional × <span style="color:#F7C948;">IA-Native</span></h1>
        <p class="hero-sub">O ganho de IA é o que faz o mesmo escopo caber na janela Ago–Dez e no teto de R$ 5 M.</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
        <div class="card" style="border-top:5px solid var(--text-muted);text-align:center;">
          <div style="font-size:12px;color:var(--text-muted);">Sem ferramentas de IA</div>
          <div style="font-size:38px;font-weight:900;color:var(--text-muted);">~30 sem</div>
          <div style="font-size:12px;color:var(--text-main);">baseline p/ 15 jornadas + 3 pilares</div>
        </div>
        <div class="card" style="border-top:5px solid var(--green-dark);text-align:center;">
          <div style="font-size:12px;color:var(--green-dark);font-weight:700;">Com IA-Native</div>
          <div style="font-size:38px;font-weight:900;color:var(--green-dark);">~22 sem</div>
          <div style="font-size:12px;color:var(--text-main);">cabe em Ago–Dez 2026 · <strong>−27%</strong></div>
        </div>
      </div>
      <div class="card" style="border-left:5px solid var(--blue-accent);">
        <div style="font-size:13px;font-weight:800;color:var(--blue-dark);margin-bottom:6px;">Atividades comprimidas pela IA</div>
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">Geração de fluxos de integração MuleSoft, prompts/tópicos dos agentes, testes automatizados, documentação técnica e geração de artefatos. Sem IA, o mesmo escopo não caberia nem no bolsão nem na janela.</p>
      </div>
    </section>'''

# E5 — KPIs
def kpi_rows():
    data = [
        ("Financeiro (J1)", "Tempo médio de resposta a consulta financeira", "horas → segundos"),
        ("Financeiro (J1)", "% consultas self-service via Slack", "— → 70%"),
        ("Chamados (J2)", "Deflection de chamados de status", "— → 40%"),
        ("Clarity / Briefing (J3)", "Tempo de preparação de reunião executiva", "−60%"),
        ("Agendamento (J4)", "Tempo para agendar reunião", "minutos → 1 comando"),
        ("FAQ / Conexão (J7)", "Deflection de perguntas repetitivas RH/suporte", "— → 50%"),
        ("SEI prazos (SEI-J1)", "Perdas por decurso de prazo tácito", "−80%"),
        ("SEI consulta (SEI-J2/J4)", "Tempo de consulta processual", "−70%"),
        ("SEI transação (SEI-J9/J10)", "Tempo de tramitação / abertura", "−50%"),
        ("Transversal", "Usuários ativos (adoção Slack)", "≥ 70%"),
        ("Transversal", "% jornadas resolvidas sem escalar a humano", "≥ 65%"),
        ("Transversal", "Ganho de eficiência de IA (mandato Dataprev)", "≥ 25%"),
    ]
    return "".join(f'<tr><td {TDL}>{p}</td><td {TDL}>{k}</td><td {TDC}><strong>{m}</strong></td></tr>' for p, k, m in data)

E5 = f'''    <section class="section" id="kpis">
      <div class="hero" style="background:linear-gradient(135deg,#E67E22 0%,#071D41 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">🎯 ROI por processo · KPIs propostos</div>
        <h1 style="font-size:26px;">Como provar o <span style="color:#F7C948;">ganho de cada jornada</span></h1>
        <p class="hero-sub">Investimento de R$ 5 M → retorno por (a) horas liberadas de trabalho manual, (b) redução de perdas por decurso de prazo no SEI e (c) deflection de atendimento.</p>
      </div>
      <div class="card" style="border-left:5px solid var(--yellow);margin-bottom:16px;">
        <div style="font-size:13px;font-weight:800;color:var(--blue-dark);margin-bottom:6px;">📐 Metodologia de ROI</div>
        <p style="font-size:12.5px;color:var(--text-main);margin:0;">Entregamos a <strong>metodologia + metas ilustrativas</strong>. Os números finais dependem da volumetria da Dataprev (gap <strong>G1102</strong>), a ser fornecida na Fase 0 — por isso, nenhum número comprometido nesta fase.</p>
      </div>
      <div style="overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;">
        <thead><tr><th {TH}>Processo / Jornada</th><th {TH}>KPI proposto</th><th {TH} style="text-align:center;color:#fff;">Baseline → Meta (ilustrativo)</th></tr></thead>
        <tbody>{kpi_rows()}</tbody>
      </table>
      </div>
    </section>'''

# E2b — CRONOGRAMA gráfico por jornada (Gantt · Ago–Dez · 22 semanas)
# Tupla por jornada: (build_start, build_end, uat_start, prod_golive, finetune_end) em nº de semana (1..22)
SCHED = {
    'J1':     (3, 5, 6, 8, 10),  'J2':     (3, 5, 6, 8, 10),
    'SEI-J1': (4, 5, 6, 8, 10),  'SEI-J2': (4, 6, 7, 8, 10),  'SEI-J3': (4, 6, 7, 8, 10),
    'J3':     (9, 11, 12, 13, 15), 'J7':    (9, 11, 12, 13, 15),
    'SEI-J4': (9, 11, 12, 13, 15), 'SEI-J5': (10, 12, 13, 15, 17),
    'SEI-J6': (10, 13, 14, 15, 17), 'SEI-J7': (10, 13, 14, 15, 17),
    'J4':     (14, 17, 18, 19, 21), 'SEI-J8': (15, 17, 18, 19, 21),
    'SEI-J9': (16, 18, 19, 20, 22), 'SEI-J10': (16, 18, 19, 20, 22),
}
MONTHS = [("AGO", 4), ("SET", 4), ("OUT", 5), ("NOV", 4), ("DEZ", 5)]  # soma = 22
ONDA_C = {1: 'var(--green-dark)', 2: 'var(--blue-accent)', 3: 'var(--purple)'}
ONDA_L = {1: '#DCFCE7', 2: '#DBEAFE', 3: '#F3E8FF'}
GRID = 'grid-template-columns:210px repeat(22,minmax(30px,1fr));'

def _gridlines():
    # 22 células de fundo com linha vertical, para dar referência de semana
    cells = []
    for i in range(22):
        # início de mês recebe linha mais forte
        acc = 0; strong = False
        for _, n in MONTHS:
            if i == acc:
                strong = True; break
            acc += n
        bd = '2px solid var(--gray-border)' if strong else '1px solid #EEF1F5'
        cells.append(f'<div style="grid-column:{i + 2};grid-row:1;border-left:{bd};height:36px;"></div>')
    return ''.join(cells)

def _bar(a, b, css, grow='grid-row:1;'):
    return f'<div style="grid-column:{a + 1} / {b + 2};{grow}align-self:center;{css}"></div>'

def timeline_row(jid):
    j = next(x for x in J if x['id'] == jid)
    b0, b1, u0, p, f1 = SCHED[jid]
    c = ONDA_C[j['onda']]; lt = ONDA_L[j['onda']]
    segs = [_gridlines()]
    # BUILD
    wide = (b1 - b0) >= 2
    lbl = '<span style="font-size:9px;font-weight:700;color:#fff;line-height:18px;padding-left:6px;">Build</span>' if wide else ''
    segs.append(f'<div style="grid-column:{b0 + 1} / {b1 + 2};grid-row:1;align-self:center;background:{c};border-radius:5px;height:18px;overflow:hidden;">{lbl}</div>')
    # UAT (u0 .. p-1)
    segs.append(f'<div style="grid-column:{u0 + 1} / {p + 1};grid-row:1;align-self:center;background:{lt};border:1.5px dashed {c};border-radius:5px;height:18px;" title="UAT"></div>')
    # GO-LIVE produção (diamante no marco p)
    segs.append(f'<div style="grid-column:{p + 1} / {p + 2};grid-row:1;align-self:center;justify-self:center;color:#B8860B;font-size:15px;line-height:1;" title="Go-live Produção · S{p}">&#9670;</div>')
    # FINE-TUNING / hypercare (p+1 .. f1)
    if f1 >= p + 1:
        segs.append(f'<div style="grid-column:{p + 2} / {f1 + 2};grid-row:1;align-self:center;background:repeating-linear-gradient(90deg,{lt},{lt} 5px,transparent 5px,transparent 9px);border:1px dotted {c};border-radius:4px;height:13px;" title="Fine-tuning / Hypercare"></div>')
    label = (f'<div style="grid-column:1;grid-row:1;align-self:center;display:flex;align-items:center;gap:7px;padding-right:8px;overflow:hidden;">'
             f'<span style="font-size:15px;flex-shrink:0;">{j["emoji"]}</span>'
             f'<span style="font-size:11px;font-weight:700;color:var(--blue-dark);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{j["id"]} · {j["title"]}</span></div>')
    return f'<div style="display:grid;{GRID}align-items:center;border-bottom:1px solid #F3F5F8;">{label}{"".join(segs)}</div>'

def cronograma():
    # cabeçalho de meses
    mhdr = [f'<div style="grid-column:1;grid-row:1;"></div>']
    acc = 0
    for name, n in MONTHS:
        mhdr.append(f'<div style="grid-column:{acc + 2} / {acc + n + 2};grid-row:1;text-align:center;font-size:11px;font-weight:800;color:var(--blue-dark);background:var(--gray-bg);border-left:2px solid var(--gray-border);padding:4px 0;">{name}</div>')
        acc += n
    # cabeçalho de semanas
    whdr = ['<div style="grid-column:1;grid-row:1;"></div>']
    for i in range(22):
        whdr.append(f'<div style="grid-column:{i + 2};grid-row:1;text-align:center;font-size:8.5px;color:var(--text-muted);border-left:1px solid #EEF1F5;padding:2px 0;">S{i + 1}</div>')
    # faixa Fase 0
    fase0 = (f'<div style="display:grid;{GRID}align-items:center;border-bottom:2px solid var(--gray-border);">'
             f'<div style="grid-column:1;grid-row:1;align-self:center;display:flex;align-items:center;gap:7px;padding-right:8px;">'
             f'<span style="font-size:15px;">🚧</span><span style="font-size:11px;font-weight:800;color:var(--orange);white-space:nowrap;">Fase 0 · Governança G1002</span></div>'
             f'{_gridlines()}'
             f'<div style="grid-column:2 / 6;grid-row:1;align-self:center;background:repeating-linear-gradient(45deg,var(--orange),var(--orange) 6px,#E8890B 6px,#E8890B 12px);border-radius:5px;height:18px;overflow:hidden;"><span style="font-size:9px;font-weight:700;color:#fff;line-height:18px;padding-left:8px;">Gate escrita SEI</span></div></div>')

    def wave_header(txt, color):
        return (f'<div style="display:grid;{GRID}"><div style="grid-column:1 / 24;grid-row:1;background:{color};color:#fff;'
                f'font-size:11px;font-weight:800;padding:5px 12px;margin-top:2px;">{txt}</div></div>')

    rows = [fase0]
    rows.append(wave_header('Onda 1 · Quick Wins · leitura (go-live S8 · fim de Set)', 'var(--green-dark)'))
    rows += [timeline_row(x['id']) for x in J if x['onda'] == 1]
    rows.append(wave_header('Onda 2 · Expansão · leitura + RAG + painéis (go-live S13/S15 · Out–Nov)', 'var(--blue-accent)'))
    rows += [timeline_row(x['id']) for x in J if x['onda'] == 2]
    rows.append(wave_header('Onda 3 · Escrita, voz e governança · após Fase 0 (go-live S19/S20 · Dez)', 'var(--purple)'))
    rows += [timeline_row(x['id']) for x in J if x['onda'] == 3]

    legend = ('<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin-top:16px;padding:12px 14px;background:var(--gray-bg);border-radius:8px;">'
              '<div style="display:flex;align-items:center;gap:7px;"><div style="width:26px;height:13px;background:var(--blue-accent);border-radius:4px;"></div><span style="font-size:11.5px;color:var(--text-main);font-weight:600;">Build / construção</span></div>'
              '<div style="display:flex;align-items:center;gap:7px;"><div style="width:26px;height:13px;background:#DBEAFE;border:1.5px dashed var(--blue-accent);border-radius:4px;"></div><span style="font-size:11.5px;color:var(--text-main);font-weight:600;">Entrega p/ UAT (janela de homologação)</span></div>'
              '<div style="display:flex;align-items:center;gap:7px;"><span style="color:#B8860B;font-size:16px;">&#9670;</span><span style="font-size:11.5px;color:var(--text-main);font-weight:600;">Go-live em Produção</span></div>'
              '<div style="display:flex;align-items:center;gap:7px;"><div style="width:26px;height:11px;background:repeating-linear-gradient(90deg,#DBEAFE,#DBEAFE 5px,transparent 5px,transparent 9px);border:1px dotted var(--blue-accent);border-radius:3px;"></div><span style="font-size:11.5px;color:var(--text-main);font-weight:600;">Fine-tuning / Hypercare</span></div>'
              '</div>')

    return f'''    <section class="section" id="cronograma">
      <div class="hero" style="background:linear-gradient(135deg,#0C326F 0%,#1351B4 55%,#168821 100%);margin-bottom:24px;">
        <div class="hero-eyebrow">🗓️ Linha do tempo por jornada · Ago → Dez 2026</div>
        <h1 style="font-size:26px;">Cronograma — <span style="color:#F7C948;">cada jornada, do build ao go-live</span></h1>
        <p class="hero-sub">As 15 jornadas posicionadas semana a semana (22 semanas). Cada barra mostra a construção, a entrega para UAT, o marco de go-live em produção e o período de fine-tuning/hypercare. As três ondas encadeiam entregas contínuas: enquanto uma jornada está em hypercare, a próxima já está em build.</p>
        <div class="hero-tags">
          <span class="hero-tag highlight">Onda 1 · go-live S8</span>
          <span class="hero-tag">Onda 2 · go-live S13–S15</span>
          <span class="hero-tag">Onda 3 · go-live S19–S20</span>
        </div>
      </div>
      <div class="card" style="margin-bottom:16px;">
        <div style="overflow-x:auto;">
          <div style="min-width:880px;">
            <div style="display:grid;{GRID}">{''.join(mhdr)}</div>
            <div style="display:grid;{GRID}margin-bottom:4px;">{''.join(whdr)}</div>
            {''.join(rows)}
          </div>
        </div>
        {legend}
        <p style="font-size:11.5px;color:var(--text-muted);margin-top:12px;">Semanas indicativas para planejamento (S1 = 1ª semana de agosto/2026). A Onda 3 (escrita/governança SEI) só inicia build após o gate <strong>G1002</strong> concluído na Fase 0. Datas finais e janelas de UAT confirmadas no kick-off, após a volumetria (G1102).</p>
      </div>
    </section>'''

CRONOGRAMA = cronograma()

ESTIMATIVA_CLUSTER = "\n".join([E1, E2, CRONOGRAMA, E3, E4, E5])

# ═══════════════════════════════════════════════════════════
# ASSEMBLER — splice por linha original (bottom-up)
# ═══════════════════════════════════════════════════════════
work = list(orig)

def close_insert(idx1, block):
    return block + "\n" + orig[idx1 - 1]

ops = [
    (781, 859, NAV),
    (1376, 1376, close_insert(1376, PROBLEMA_SEI)),
    (1959, 1959, close_insert(1959, ARQ_DIAGRAM)),
    (2217, 2222, PUBLICOS_MERGE),
    (2372, 3095, JORNADAS),      # 2372 (não 2371) preserva o "-->" que fecha o banner de comentário da SEÇÃO 6
    (3462, 3462, close_insert(3462, SISTEMAS_SEI)),
    (3464, 3701, None),          # remove seção SEI (preserva </section> de sistemas na 3463)
    (3702, 4034, CLOUDS),
    (4035, 4312, HCC),
    (4313, 5573, ESTIMATIVA_CLUSTER),  # 5573 = </section> órfão do comparativo no base
    # ajustes pontuais
    (777, 777, '    <p>Agilizar e otimizar os serviços e o relacionamento da Dataprev, com autosserviço e automação via Slack, Agentforce e MuleSoft · 15 jornadas · Ago–Dez 2026 · Rascunho v5.0</p>'),
    (874, 874, '      <span class="date-badge">Atualizado 28 Jul 2026</span>'),
]

for start, end, text in sorted(ops, key=lambda o: o[0], reverse=True):
    repl = [] if text is None else text.split("\n")
    work[start - 1:end] = repl

open(OUT, "w", encoding="utf-8").write("\n".join(work))
print("OK ->", OUT)
print("linhas finais:", len("\n".join(work).split("\n")))
