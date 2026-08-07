import os
import json
import markdown2
from flask import Flask, render_template_string, abort, request, Response, stream_with_context
import urllib.request
import urllib.error

app = Flask(__name__)

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "content")

INFERENCE_URL   = os.environ.get("INFERENCE_URL", "https://us.inference.heroku.com")
INFERENCE_KEY   = os.environ.get("INFERENCE_KEY", "")
INFERENCE_MODEL = os.environ.get("INFERENCE_MODEL_ID", "claude-4-5-sonnet")

PAGES = [
    {"id": "01-contexto",    "title": "Contexto e Objetivo",      "icon": "info",            "section": "Plano de Trabalho"},
    {"id": "02-premissas",   "title": "Premissas",                "icon": "checklist",       "section": "Plano de Trabalho"},
    {"id": "03-escopo",      "title": "Escopo",                   "icon": "rule",            "section": "Plano de Trabalho"},
    {"id": "04-fases",       "title": "Fases e Atividades",       "icon": "view_timeline",   "section": "Plano de Trabalho"},
    {"id": "05-esforco",     "title": "Esforço e Recursos",       "icon": "groups",          "section": "Plano de Trabalho"},
    {"id": "06-timeline",    "title": "Timelines",                "icon": "calendar_month",  "section": "Plano de Trabalho"},
    {"id": "07-flex-credits","title": "Flex Credits (CPQD)",      "icon": "payments",        "section": "Plano de Trabalho"},
    {"id": "08-perguntas",   "title": "Perguntas em Aberto",      "icon": "help_outline",    "section": "Plano de Trabalho"},
    {"id": "09-riscos",      "title": "Riscos",                   "icon": "warning_amber",   "section": "Plano de Trabalho"},
    {"id": "10-stakeholders","title": "Stakeholders",             "icon": "people_alt",      "section": "Plano de Trabalho"},
]

SYSTEM_PROMPT = """Você é um assistente especializado no projeto **Dataprev — Nova ORG Produtiva Dedicada** da Salesforce Professional Services LATAM.

Contexto do projeto (v3.0 — revisado pelo arquiteto técnico em 24/06/2026):
- Cliente: Dataprev (empresa pública federal de TI da Previdência Social)
- Objetivo: Provisionar uma nova ORG de produção Salesforce dedicada a testes de estresse e homologação massiva pelo CPQD
- Decisão estratégica (Vinícius Machuca + Aline Sabino, 11/06/2026): nova ORG produtiva, não sandbox
- Clouds: Agentforce + Service Cloud + Data Cloud + Digital Engagement (WhatsApp) — Marketing Cloud FORA do escopo
- 6 agentes Wave 2: MEC, MDS, MS, Primeira Infância, MTE, IBAMA + orquestrador
- Scale Test Add-On: complementar (não alternativa) para slots de burst controlado
- Duração: 4 semanas | Esforço total: 245h (roles) | MuleSoft removido do escopo
- Roles: PM 35h (R$789,88/h) · TC 140h (R$668,78/h) · TA 70h (R$884,68/h)
- Valor total: R$ 183.202,60 s/ impostos | R$ 196.043,45 c/ impostos
- Carga semanal: 70h (S1–S3) e 35h (S4)
- Fases 1–5 concluídas até fim S2; F6–F8 nas semanas 3–4
- F2 revisada: 96h → 20h (orquestrador removido, Data Cloud básico, sem provisionamento CPQD direto)
- F3 revisada: 104h → 16h (6 agentes em ciclo único, baseado em experiência com ambientes de homologação)
- F4 revisada: 28h → 12h (WhatsApp end-to-end em tarefa única)
- F5 revisada: 78h → 16h (endpoints consolidados, MuleSoft removido)
- Flex Credits CPQD: ~3.110 pacotes / R$ 3,11M por 6 meses (12 ciclos/mês)
- 14 perguntas em aberto (Q-01 a Q-14), 5 bloqueadoras antes do kick-off
- Responsável PS: Nelson Stebulaitis Filho

Responda sempre em português. Seja direto, técnico e consultivo — como um arquiteto sênior da Salesforce PS que conhece todos os detalhes deste projeto. Quando não souber algo específico, indique claramente."""

LAYOUT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page_title }} — DTP Nova ORG Produtiva</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <style>
    :root {
      --slds-brand-primary:       #0176D3;
      --slds-brand-dark:          #032D60;
      --slds-color-bg-1:          #F3F3F3;
      --slds-color-bg-2:          #FFFFFF;
      --slds-color-border:        #DDDBDA;
      --slds-color-border-focus:  #0176D3;
      --slds-color-text-default:  #181818;
      --slds-color-text-weak:     #706E6B;
      --slds-color-success:       #2E844A;
      --slds-color-warning:       #E07B00;
      --slds-color-error:         #BA0517;
      --slds-color-info:          #0176D3;
      --slds-color-success-bg:    #EEF5EE;
      --slds-color-warning-bg:    #FFF3E0;
      --slds-color-error-bg:      #FDECEA;
      --slds-color-info-bg:       #EEF4FF;
      --slds-radius-medium:       4px;
      --slds-radius-large:        8px;
      --slds-shadow-small:        0 2px 4px rgba(0,0,0,0.12);
      --slds-shadow-medium:       0 4px 12px rgba(0,0,0,0.14);
      --slds-sidebar-w:           272px;
      --slds-chat-w:              360px;
      --slds-font:                'Inter', 'Salesforce Sans', Arial, sans-serif;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: 14px; }
    body {
      font-family: var(--slds-font);
      background: var(--slds-color-bg-1);
      color: var(--slds-color-text-default);
      display: flex; min-height: 100vh;
    }

    /* Sidebar */
    #sidebar {
      width: var(--slds-sidebar-w);
      background: var(--slds-brand-dark);
      display: flex; flex-direction: column;
      position: fixed; top: 0; left: 0; height: 100vh;
      overflow-y: auto; z-index: 100;
    }
    .sidebar-brand {
      padding: 20px 16px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .sidebar-brand .sf-logo {
      display: flex; align-items: center; gap: 8px; margin-bottom: 10px;
    }
    .sidebar-brand .sf-logo .cloud-icon {
      width: 28px; height: 28px; background: var(--slds-brand-primary);
      border-radius: 6px; display: flex; align-items: center; justify-content: center;
    }
    .sidebar-brand .sf-logo .cloud-icon .material-icons { font-size: 16px; color: #fff; }
    .sidebar-brand .sf-logo span { font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.6); letter-spacing: 0.5px; text-transform: uppercase; }
    .sidebar-brand .project-name { font-size: 13.5px; font-weight: 700; color: #fff; line-height: 1.4; }
    .sidebar-brand .project-meta { font-size: 11px; color: rgba(255,255,255,0.45); margin-top: 4px; }

    .sidebar-section { padding: 16px 16px 4px; font-size: 10px; font-weight: 700; color: rgba(255,255,255,0.3); text-transform: uppercase; letter-spacing: 1px; }

    #sidebar nav a {
      display: flex; align-items: center; gap: 10px;
      padding: 9px 16px; font-size: 13px; font-weight: 500;
      color: rgba(255,255,255,0.7); text-decoration: none;
      border-left: 3px solid transparent; transition: all 0.15s;
    }
    #sidebar nav a .material-icons { font-size: 18px; opacity: 0.7; }
    #sidebar nav a:hover { background: rgba(255,255,255,0.07); color: #fff; }
    #sidebar nav a:hover .material-icons { opacity: 1; }
    #sidebar nav a.active { background: rgba(1,118,211,0.2); color: #fff; border-left-color: var(--slds-brand-primary); }
    #sidebar nav a.active .material-icons { opacity: 1; color: var(--slds-brand-primary); }

    .sidebar-chips { padding: 16px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid rgba(255,255,255,0.08); margin-top: 8px; }
    .sidebar-chip {
      background: rgba(255,255,255,0.06); border-radius: var(--slds-radius-medium);
      padding: 6px 10px; font-size: 11px;
    }
    .sidebar-chip .chip-label { color: rgba(255,255,255,0.4); }
    .sidebar-chip .chip-value { color: #fff; font-weight: 600; }

    .sidebar-footer { margin-top: auto; padding: 14px 16px; font-size: 10px; color: rgba(255,255,255,0.2); border-top: 1px solid rgba(255,255,255,0.06); }

    /* Main area */
    #main {
      margin-left: var(--slds-sidebar-w);
      flex: 1; display: flex; flex-direction: column;
      min-height: 100vh;
      margin-right: var(--slds-chat-w);
      transition: margin-right 0.25s;
    }
    #main.chat-closed { margin-right: 0; }

    /* Top bar */
    #topbar {
      background: var(--slds-color-bg-2);
      border-bottom: 1px solid var(--slds-color-border);
      padding: 0 28px; height: 52px;
      display: flex; align-items: center; gap: 12px;
      position: sticky; top: 0; z-index: 50;
    }
    #topbar .breadcrumb { font-size: 12px; color: var(--slds-color-text-weak); }
    #topbar .breadcrumb span { color: var(--slds-brand-dark); font-weight: 600; }
    #topbar .topbar-actions { margin-left: auto; display: flex; align-items: center; gap: 8px; }
    .btn-primary {
      display: flex; align-items: center; gap: 6px;
      background: var(--slds-brand-primary); color: #fff;
      border: none; border-radius: var(--slds-radius-medium);
      padding: 0 14px; height: 32px; font-size: 13px; font-weight: 600;
      cursor: pointer; font-family: var(--slds-font); transition: background 0.15s;
    }
    .btn-primary:hover { background: #015aad; }
    .btn-primary .material-icons { font-size: 16px; }

    /* Content */
    #content { padding: 28px 32px; max-width: 980px; }

    #content h1 { font-size: 22px; font-weight: 700; color: var(--slds-brand-dark); margin: 28px 0 6px; }
    #content h1:first-child { margin-top: 0; }
    #content h2 {
      font-size: 16px; font-weight: 700; color: var(--slds-brand-dark);
      margin: 28px 0 10px; padding-bottom: 8px;
      border-bottom: 2px solid var(--slds-brand-primary);
    }
    #content h3 { font-size: 14px; font-weight: 700; color: var(--slds-brand-dark); margin: 20px 0 6px; }
    #content h4 { font-size: 12px; font-weight: 600; color: var(--slds-color-text-weak); margin: 14px 0 4px; text-transform: uppercase; letter-spacing: 0.5px; }
    #content p { line-height: 1.7; margin-bottom: 12px; font-size: 13.5px; }
    #content ul, #content ol { margin: 8px 0 14px 20px; }
    #content li { line-height: 1.7; font-size: 13.5px; margin-bottom: 3px; }
    #content strong { color: var(--slds-brand-dark); font-weight: 600; }
    #content em { color: var(--slds-color-text-weak); }
    #content code {
      background: var(--slds-color-info-bg); color: var(--slds-brand-dark);
      padding: 2px 6px; border-radius: var(--slds-radius-medium);
      font-size: 12px; font-family: 'SFMono-Regular', Consolas, monospace;
    }
    #content pre {
      background: #1b1f2d; color: #cdd6f4;
      padding: 16px 20px; border-radius: var(--slds-radius-large);
      overflow-x: auto; margin: 14px 0; border: 1px solid #2a2f44;
    }
    #content pre code { background: none; color: inherit; padding: 0; font-size: 12.5px; }
    #content blockquote {
      border-left: 4px solid var(--slds-brand-primary);
      background: var(--slds-color-info-bg);
      padding: 12px 16px; margin: 14px 0;
      border-radius: 0 var(--slds-radius-large) var(--slds-radius-large) 0;
      font-size: 13px; color: var(--slds-color-text-weak);
    }
    #content hr { border: none; border-top: 1px solid var(--slds-color-border); margin: 24px 0; }
    #content table {
      width: 100%; border-collapse: collapse; margin: 14px 0;
      font-size: 13px; border: 1px solid var(--slds-color-border);
      border-radius: var(--slds-radius-large); overflow: hidden;
      box-shadow: var(--slds-shadow-small);
    }
    #content thead tr { background: var(--slds-brand-dark); color: #fff; }
    #content thead th { padding: 10px 14px; text-align: left; font-weight: 600; font-size: 12px; }
    #content tbody tr:nth-child(even) { background: #F8F8F8; }
    #content tbody tr:nth-child(odd) { background: var(--slds-color-bg-2); }
    #content tbody tr:hover { background: var(--slds-color-info-bg); }
    #content tbody td { padding: 9px 14px; border-bottom: 1px solid var(--slds-color-border); vertical-align: top; line-height: 1.5; }

    /* Summary strip */
    .slds-summary-strip { display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0 28px; }
    .slds-chip {
      display: flex; align-items: center; gap: 6px;
      background: var(--slds-color-bg-2); border: 1px solid var(--slds-color-border);
      border-radius: 20px; padding: 5px 12px;
      font-size: 12px; font-weight: 600; color: var(--slds-brand-dark);
      box-shadow: var(--slds-shadow-small);
    }
    .slds-chip .material-icons { font-size: 14px; color: var(--slds-brand-primary); }
    .slds-chip .chip-val { color: var(--slds-color-text-weak); font-weight: 400; margin-left: 2px; }

    /* Cards */
    .slds-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; margin-top: 8px; }
    .slds-card {
      background: var(--slds-color-bg-2); border: 1px solid var(--slds-color-border);
      border-radius: var(--slds-radius-large); padding: 18px 20px;
      text-decoration: none; color: inherit;
      transition: box-shadow 0.15s, transform 0.1s;
      display: block; box-shadow: var(--slds-shadow-small);
    }
    .slds-card:hover { box-shadow: var(--slds-shadow-medium); transform: translateY(-2px); }
    .slds-card .card-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
    .slds-card .card-icon {
      width: 36px; height: 36px; background: var(--slds-color-info-bg);
      border-radius: var(--slds-radius-medium);
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .slds-card .card-icon .material-icons { font-size: 20px; color: var(--slds-brand-primary); }
    .slds-card .card-title { font-size: 14px; font-weight: 700; color: var(--slds-brand-dark); }
    .slds-card .card-desc { font-size: 12px; color: var(--slds-color-text-weak); line-height: 1.5; }

    /* Badges */
    .badge { display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; }
    .badge-error   { background: var(--slds-color-error-bg);   color: var(--slds-color-error); }
    .badge-warning { background: var(--slds-color-warning-bg); color: var(--slds-color-warning); }
    .badge-success { background: var(--slds-color-success-bg); color: var(--slds-color-success); }
    .badge-info    { background: var(--slds-color-info-bg);    color: var(--slds-color-info); }

    /* Alert */
    .slds-alert {
      display: flex; gap: 10px; align-items: flex-start;
      padding: 12px 16px; border-radius: var(--slds-radius-large);
      margin-bottom: 20px; border: 1px solid;
    }
    .slds-alert .material-icons { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
    .slds-alert.info    { background: var(--slds-color-info-bg);    border-color: var(--slds-brand-primary); color: var(--slds-brand-dark); }
    .slds-alert.info    .material-icons { color: var(--slds-brand-primary); }
    .slds-alert.warning { background: var(--slds-color-warning-bg); border-color: var(--slds-color-warning); color: #5A3800; }
    .slds-alert.warning .material-icons { color: var(--slds-color-warning); }

    /* Chat panel */
    #chat-panel {
      position: fixed; top: 0; right: 0; bottom: 0;
      width: var(--slds-chat-w);
      background: var(--slds-color-bg-2);
      border-left: 1px solid var(--slds-color-border);
      display: flex; flex-direction: column;
      z-index: 80; transition: transform 0.25s;
    }
    #chat-panel.hidden { transform: translateX(100%); }

    .chat-header {
      padding: 14px 16px; border-bottom: 1px solid var(--slds-color-border);
      display: flex; align-items: center; gap: 10px;
      background: var(--slds-brand-dark);
    }
    .chat-header .chat-avatar {
      width: 32px; height: 32px; background: var(--slds-brand-primary);
      border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .chat-header .chat-avatar .material-icons { font-size: 18px; color: #fff; }
    .chat-header .chat-info { flex: 1; }
    .chat-header .chat-title { font-size: 13px; font-weight: 700; color: #fff; }
    .chat-header .chat-subtitle { font-size: 11px; color: rgba(255,255,255,0.5); }
    .chat-header .chat-close { cursor: pointer; color: rgba(255,255,255,0.5); transition: color 0.15s; }
    .chat-header .chat-close:hover { color: #fff; }
    .chat-header .chat-close .material-icons { font-size: 20px; }

    #chat-messages {
      flex: 1; overflow-y: auto; padding: 16px;
      display: flex; flex-direction: column; gap: 12px;
      background: #F8F9FB;
    }

    .chat-msg { display: flex; gap: 8px; align-items: flex-start; }
    .chat-msg.user { flex-direction: row-reverse; }
    .msg-avatar {
      width: 28px; height: 28px; border-radius: 50%; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700;
    }
    .chat-msg.user .msg-avatar { background: var(--slds-brand-primary); color: #fff; }
    .chat-msg.assistant .msg-avatar { background: var(--slds-brand-dark); color: #fff; }
    .chat-msg.assistant .msg-avatar .material-icons { font-size: 16px; }
    .msg-bubble {
      max-width: 80%; padding: 10px 14px; border-radius: 12px;
      font-size: 13px; line-height: 1.6;
    }
    .chat-msg.user .msg-bubble { background: var(--slds-brand-primary); color: #fff; border-radius: 12px 12px 4px 12px; }
    .chat-msg.assistant .msg-bubble { background: var(--slds-color-bg-2); color: var(--slds-color-text-default); border: 1px solid var(--slds-color-border); border-radius: 12px 12px 12px 4px; box-shadow: var(--slds-shadow-small); }
    .msg-bubble p { margin: 0; }
    .msg-bubble p + p { margin-top: 6px; }
    .msg-bubble strong { font-weight: 600; }
    .msg-bubble ul, .msg-bubble ol { margin: 6px 0 6px 16px; }
    .msg-bubble li { margin-bottom: 2px; }
    .msg-bubble code { background: rgba(0,0,0,0.07); padding: 1px 4px; border-radius: 3px; font-size: 11.5px; }
    .chat-msg.user .msg-bubble code { background: rgba(255,255,255,0.2); }

    .chat-typing {
      display: flex; gap: 4px; padding: 10px 14px;
      background: var(--slds-color-bg-2); border: 1px solid var(--slds-color-border);
      border-radius: 12px 12px 12px 4px; width: fit-content;
    }
    .chat-typing span {
      width: 6px; height: 6px; background: var(--slds-color-text-weak);
      border-radius: 50%; animation: bounce 1.2s infinite;
    }
    .chat-typing span:nth-child(2) { animation-delay: 0.2s; }
    .chat-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes bounce { 0%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-6px); } }

    .chat-suggestions { padding: 8px 16px 0; display: flex; flex-wrap: wrap; gap: 6px; }
    .suggestion-btn {
      background: var(--slds-color-info-bg); border: 1px solid var(--slds-brand-primary);
      color: var(--slds-brand-dark); border-radius: 14px;
      padding: 4px 12px; font-size: 11.5px; font-weight: 500;
      cursor: pointer; font-family: var(--slds-font); transition: background 0.15s;
    }
    .suggestion-btn:hover { background: #D4E8FB; }

    .chat-input-area {
      padding: 12px 16px; border-top: 1px solid var(--slds-color-border);
      background: var(--slds-color-bg-2);
    }
    .chat-input-row { display: flex; gap: 8px; align-items: flex-end; }
    #chat-input {
      flex: 1; border: 1px solid var(--slds-color-border);
      border-radius: var(--slds-radius-large);
      padding: 9px 14px; font-size: 13px; font-family: var(--slds-font);
      resize: none; outline: none; line-height: 1.5; max-height: 120px;
      transition: border-color 0.15s;
    }
    #chat-input:focus { border-color: var(--slds-color-border-focus); box-shadow: 0 0 0 3px rgba(1,118,211,0.15); }
    #chat-send {
      width: 36px; height: 36px; background: var(--slds-brand-primary);
      border: none; border-radius: 50%; display: flex; align-items: center; justify-content: center;
      cursor: pointer; flex-shrink: 0; transition: background 0.15s;
    }
    #chat-send:hover { background: #015aad; }
    #chat-send:disabled { background: #D8D9DB; cursor: not-allowed; }
    #chat-send .material-icons { font-size: 18px; color: #fff; }
    .chat-hint { font-size: 11px; color: var(--slds-color-text-weak); margin-top: 6px; }
  </style>
</head>
<body>
  <div id="sidebar">
    <div class="sidebar-brand">
      <div class="sf-logo">
        <div class="cloud-icon"><span class="material-icons">cloud</span></div>
        <span>Salesforce PS LATAM</span>
      </div>
      <div class="project-name">DTP Nova ORG Produtiva</div>
      <div class="project-meta">Dataprev · Junho 2026</div>
    </div>
    <nav>
      <a href="/" class="{{ 'active' if current == 'home' else '' }}">
        <span class="material-icons">home</span> Início
      </a>
      {% set ns = namespace(last_section='') %}
      {% for p in pages %}
        {% if p.section != ns.last_section %}
          {% set ns.last_section = p.section %}
          <div class="sidebar-section">{{ p.section }}</div>
        {% endif %}
        <a href="/{{ p.id }}" class="{{ 'active' if current == p.id else '' }}">
          <span class="material-icons">{{ p.icon }}</span> {{ p.title }}
        </a>
      {% endfor %}
    </nav>
    <div class="sidebar-chips">
      <div class="sidebar-chip"><span class="chip-label">Duração</span> <span class="chip-value">4 semanas</span></div>
      <div class="sidebar-chip"><span class="chip-label">Esforço</span> <span class="chip-value">245h</span></div>
      <div class="sidebar-chip"><span class="chip-label">Valor</span> <span class="chip-value">R$ 196.043,45</span></div>
      <div class="sidebar-chip"><span class="chip-label">Flex Credits</span> <span class="chip-value">R$ 3,11M / 6 meses</span></div>
    </div>
    <div class="sidebar-footer">Nelson Stebulaitis Filho · PS LATAM<br>© 2026 Salesforce</div>
  </div>

  <div id="main" class="{{ '' if chat_open else 'chat-closed' }}">
    <div id="topbar">
      <span class="breadcrumb">DTP Nova ORG Produtiva &rsaquo; <span>{{ page_title }}</span></span>
      <div class="topbar-actions">
        <button class="btn-primary" onclick="toggleChat()" id="chat-toggle-btn">
          <span class="material-icons">smart_toy</span> Assistente IA
        </button>
      </div>
    </div>
    <div id="content">{{ content | safe }}</div>
  </div>

  <div id="chat-panel" class="{{ '' if chat_open else 'hidden' }}">
    <div class="chat-header">
      <div class="chat-avatar"><span class="material-icons">smart_toy</span></div>
      <div class="chat-info">
        <div class="chat-title">Assistente do Projeto</div>
        <div class="chat-subtitle">DTP Nova ORG · Claude claude-4-5-sonnet</div>
      </div>
      <div class="chat-close" onclick="toggleChat()"><span class="material-icons">close</span></div>
    </div>
    <div id="chat-messages">
      <div class="chat-msg assistant">
        <div class="msg-avatar"><span class="material-icons">smart_toy</span></div>
        <div class="msg-bubble">
          <p>Olá! Sou o assistente do projeto <strong>DTP Nova ORG Produtiva</strong>.</p>
          <p>Posso responder sobre escopo, fases, estimativas, perguntas em aberto, riscos e estratégia.</p>
        </div>
      </div>
    </div>
    <div class="chat-suggestions">
      <button class="suggestion-btn" onclick="sendSuggestion('Quais são as perguntas bloqueadoras antes do kick-off?')">Bloqueadoras kick-off</button>
      <button class="suggestion-btn" onclick="sendSuggestion('Explica o sizing de Flex Credits do CPQD')">Flex Credits CPQD</button>
      <button class="suggestion-btn" onclick="sendSuggestion('Por que nova ORG produtiva e não sandbox?')">Por que nova ORG?</button>
      <button class="suggestion-btn" onclick="sendSuggestion('Qual o risco maior do projeto?')">Maiores riscos</button>
    </div>
    <div class="chat-input-area">
      <div class="chat-input-row">
        <textarea id="chat-input" rows="1" placeholder="Pergunte sobre o projeto…" onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
        <button id="chat-send" onclick="sendMessage()"><span class="material-icons">send</span></button>
      </div>
      <div class="chat-hint">Powered by Claude · Heroku AI Add-on</div>
    </div>
  </div>

  <script>
    let chatOpen = {{ 'true' if chat_open else 'false' }};

    function toggleChat() {
      chatOpen = !chatOpen;
      document.getElementById('chat-panel').classList.toggle('hidden', !chatOpen);
      document.getElementById('main').classList.toggle('chat-closed', !chatOpen);
    }

    function autoResize(el) {
      el.style.height = 'auto';
      el.style.height = Math.min(el.scrollHeight, 120) + 'px';
    }

    function handleKey(e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
    }

    function sendSuggestion(text) {
      document.getElementById('chat-input').value = text;
      sendMessage();
    }

    async function sendMessage() {
      const input = document.getElementById('chat-input');
      const text = input.value.trim();
      if (!text) return;
      appendMsg('user', text);
      input.value = '';
      input.style.height = 'auto';
      document.getElementById('chat-send').disabled = true;
      const typingId = appendTyping();
      try {
        const resp = await fetch('/api/chat', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({message: text})
        });
        removeTyping(typingId);
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        if (resp.headers.get('content-type')?.includes('text/event-stream')) {
          const msgId = appendMsg('assistant', '');
          const reader = resp.body.getReader();
          const decoder = new TextDecoder();
          let buffer = '';
          while (true) {
            const {done, value} = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, {stream: true});
            const lines = buffer.split('\\n');
            buffer = lines.pop();
            for (const line of lines) {
              if (line.startsWith('data: ')) {
                const data = line.slice(6);
                if (data === '[DONE]') break;
                try {
                  const parsed = JSON.parse(data);
                  const delta = parsed.delta?.text || '';
                  if (delta) appendDelta(msgId, delta);
                } catch {}
              }
            }
          }
        } else {
          const data = await resp.json();
          appendMsg('assistant', data.reply || 'Sem resposta.');
        }
      } catch (err) {
        removeTyping(typingId);
        appendMsg('assistant', 'Erro ao conectar com o assistente. Tente novamente.');
      }
      document.getElementById('chat-send').disabled = false;
      document.getElementById('chat-input').focus();
    }

    let msgCounter = 0;
    function appendMsg(role, text) {
      const id = 'msg-' + (++msgCounter);
      const msgs = document.getElementById('chat-messages');
      const div = document.createElement('div');
      div.className = 'chat-msg ' + role;
      div.id = id;
      const avatar = role === 'user'
        ? '<div class="msg-avatar">N</div>'
        : '<div class="msg-avatar"><span class="material-icons">smart_toy</span></div>';
      div.innerHTML = avatar + '<div class="msg-bubble" id="bubble-' + id + '">' + renderMd(text) + '</div>';
      msgs.appendChild(div);
      msgs.scrollTop = msgs.scrollHeight;
      return id;
    }

    function appendDelta(id, delta) {
      const bubble = document.getElementById('bubble-' + id);
      if (!bubble) return;
      bubble.dataset.raw = (bubble.dataset.raw || '') + delta;
      bubble.innerHTML = renderMd(bubble.dataset.raw);
      document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
    }

    function appendTyping() {
      const id = 'typing-' + Date.now();
      const msgs = document.getElementById('chat-messages');
      const div = document.createElement('div');
      div.className = 'chat-msg assistant';
      div.id = id;
      div.innerHTML = '<div class="msg-avatar"><span class="material-icons">smart_toy</span></div><div class="chat-typing"><span></span><span></span><span></span></div>';
      msgs.appendChild(div);
      msgs.scrollTop = msgs.scrollHeight;
      return id;
    }

    function removeTyping(id) {
      const el = document.getElementById(id);
      if (el) el.remove();
    }

    function renderMd(text) {
      if (!text) return '';
      return text
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.+?)\*/g, '<em>$1</em>')
        .replace(/`(.+?)`/g, '<code>$1</code>')
        .replace(/^#{1,3} (.+)$/gm, '<strong>$1</strong>')
        .replace(/^- (.+)$/gm, '• $1')
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>');
    }
  </script>
</body>
</html>"""

HOME_CONTENT = """
<h1>DTP — Nova ORG Produtiva Dedicada</h1>
<p>Plano de Projeto PS · Salesforce Professional Services LATAM · Junho 2026 · <strong>v3.0 — Revisado pelo Arquiteto Técnico</strong></p>

<div class="slds-summary-strip">
  <div class="slds-chip"><span class="material-icons">business</span> Dataprev <span class="chip-val">Cliente</span></div>
  <div class="slds-chip"><span class="material-icons">schedule</span> 4 semanas <span class="chip-val">Duração</span></div>
  <div class="slds-chip"><span class="material-icons">engineering</span> 245h <span class="chip-val">Esforço (roles)</span></div>
  <div class="slds-chip"><span class="material-icons">payments</span> R$ 196k <span class="chip-val">c/ impostos</span></div>
  <div class="slds-chip"><span class="material-icons">group</span> TA + TC + PM <span class="chip-val">Equipe PS</span></div>
</div>

<div class="slds-alert info">
  <span class="material-icons">info</span>
  <div><strong>Revisão técnica (24/06/2026):</strong> F2–F5 consolidadas com escopo focado nos testes CPQD. Projeto reduzido de 7 → <strong>4 semanas</strong>. F1+F2 na S1 · F3+F4+F5+F6 início na S2 · F6+F7 na S3 · F7+F8 na S4. MuleSoft removido do escopo.</div>
</div>

<h2>Plano de Trabalho</h2>
<div class="slds-cards">
  <a class="slds-card" href="/01-contexto">
    <div class="card-header"><div class="card-icon"><span class="material-icons">info</span></div><div class="card-title">1. Contexto e Objetivo</div></div>
    <div class="card-desc">Situação atual · Decisão estratégica · 6 objetivos mensuráveis</div>
  </a>
  <a class="slds-card" href="/02-premissas">
    <div class="card-header"><div class="card-icon"><span class="material-icons">checklist</span></div><div class="card-title">2. Premissas</div></div>
    <div class="card-desc">24 premissas técnicas, contratuais, operacionais e de IA</div>
  </a>
  <a class="slds-card" href="/03-escopo">
    <div class="card-header"><div class="card-icon"><span class="material-icons">rule</span></div><div class="card-title">3. Escopo</div></div>
    <div class="card-desc">Dentro e fora do escopo · Marketing Cloud explicitamente excluído</div>
  </a>
  <a class="slds-card" href="/04-fases">
    <div class="card-header"><div class="card-icon"><span class="material-icons">view_timeline</span></div><div class="card-title">4. Fases e Atividades</div></div>
    <div class="card-desc">8 fases · 556h · TC1+TC2 paralelos · detalhamento completo por atividade</div>
  </a>
  <a class="slds-card" href="/05-esforco">
    <div class="card-header"><div class="card-icon"><span class="material-icons">groups</span></div><div class="card-title">5. Esforço e Recursos</div></div>
    <div class="card-desc">Carga semanal por papel · pico S4 · comparativo v1.0 vs v2.0</div>
  </a>
  <a class="slds-card" href="/06-timeline">
    <div class="card-header"><div class="card-icon"><span class="material-icons">calendar_month</span></div><div class="card-title">6. Timelines</div></div>
    <div class="card-desc">Gantt por fases · visão por entregáveis macro · 6 milestones</div>
  </a>
  <a class="slds-card" href="/07-flex-credits">
    <div class="card-header"><div class="card-icon"><span class="material-icons">payments</span></div><div class="card-title">7. Flex Credits (CPQD)</div></div>
    <div class="card-desc">R$ 3,11M · 3.110 pacotes · 12 ciclos/mês · 6 meses</div>
  </a>
  <a class="slds-card" href="/08-perguntas">
    <div class="card-header"><div class="card-icon"><span class="material-icons">help_outline</span></div><div class="card-title">8. Perguntas em Aberto</div></div>
    <div class="card-desc">14 perguntas · 5 bloqueadoras pré-kick-off · donos identificados</div>
  </a>
  <a class="slds-card" href="/09-riscos">
    <div class="card-header"><div class="card-icon"><span class="material-icons">warning_amber</span></div><div class="card-title">9. Riscos</div></div>
    <div class="card-desc">8 riscos mapeados · probabilidade · impacto · plano de mitigação</div>
  </a>
  <a class="slds-card" href="/10-stakeholders">
    <div class="card-header"><div class="card-icon"><span class="material-icons">people_alt</span></div><div class="card-title">10. Stakeholders</div></div>
    <div class="card-desc">Papéis e fases críticas · RACI simplificado das decisões-chave</div>
  </a>
</div>

<h2>Milestones</h2>
<ul>
  <li><span class="badge badge-info">M1 · S1</span> Arquitetura aprovada · nova ORG ativa com Data Cloud · RACI assinado</li>
  <li><span class="badge badge-info">M2 · S2</span> 6 agentes Wave 2 operacionais · WhatsApp configurado · 11 endpoints validados</li>
  <li><span class="badge badge-info">M3 · S3</span> 1º ciclo CPQD executado · homologação Dataprev concluída · testes de volume OK</li>
  <li><span class="badge badge-success">M4 · S4</span> Go-live em janela protegida · hypercare ativo</li>
  <li><span class="badge badge-success">M5 · S4</span> Runbook entregue · dashboards Splunk ativos</li>
  <li><span class="badge badge-success">M6 · S4</span> Encerramento formal e aceite do cliente</li>
</ul>

<h2>Perguntas Bloqueadoras (pré-kick-off)</h2>
<ul>
  <li><span class="badge badge-error">Q-01</span> Volume de licenças Agentforce for Service — <em>Saulo / Milton (Dataprev)</em></li>
  <li><span class="badge badge-error">Q-02</span> Volume de DSCs (Data Cloud) — <em>Saulo / Milton (Dataprev)</em></li>
  <li><span class="badge badge-error">Q-04</span> Aprovação orçamentária do ambiente adicional — <em>Fernanda (AE)</em></li>
  <li><span class="badge badge-error">Q-05</span> Flex Credits aprovados: R$ 3,11M / 6 meses — <em>Vinícius Machuca / Aline Sabino</em></li>
  <li><span class="badge badge-warning">Q-09</span> MuleSoft contratual? (+35h se confirmado) — <em>Jurídico / Comercial</em></li>
</ul>
"""

conversation_history = {}

@app.route("/")
def home():
    return render_template_string(LAYOUT, page_title="Início", content=HOME_CONTENT, pages=PAGES, current="home", chat_open=False)

@app.route("/<page_id>")
def page(page_id):
    meta = page_meta(page_id)
    if not meta:
        abort(404)
    raw = read_md(page_id)
    if not raw:
        abort(404)
    html = markdown2.markdown(raw, extras=["tables", "fenced-code-blocks", "strike", "header-ids"])
    return render_template_string(LAYOUT, page_title=meta["title"], content=html, pages=PAGES, current=page_id, chat_open=False)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_msg = data.get("message", "").strip()
    if not user_msg:
        return {"reply": "Mensagem vazia."}, 400

    session_id = request.headers.get("X-Session-Id", "default")
    if session_id not in conversation_history:
        conversation_history[session_id] = []

    conversation_history[session_id].append({"role": "user", "content": user_msg})
    history = conversation_history[session_id][-20:]

    payload = json.dumps({
        "model": INFERENCE_MODEL,
        "max_tokens": 1024,
        "system": SYSTEM_PROMPT,
        "messages": history,
        "stream": True,
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{INFERENCE_URL}/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {INFERENCE_KEY}",
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    def generate():
        full_reply = []
        try:
            with urllib.request.urlopen(req) as resp:
                for raw_line in resp:
                    line = raw_line.decode("utf-8").rstrip()
                    if line.startswith("data: "):
                        chunk = line[6:]
                        if chunk == "[DONE]":
                            yield "data: [DONE]\n\n"
                            break
                        try:
                            parsed = json.loads(chunk)
                            delta = parsed.get("delta", {}).get("text", "")
                            if delta:
                                full_reply.append(delta)
                            yield f"data: {chunk}\n\n"
                        except Exception:
                            yield f"data: {chunk}\n\n"
        except urllib.error.HTTPError as e:
            err = e.read().decode()
            yield f"data: {json.dumps({'delta': {'text': f'Erro API: {err[:200]}'}})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'delta': {'text': f'Erro: {str(e)[:200]}'}})}\n\n"
            yield "data: [DONE]\n\n"

        if full_reply:
            conversation_history[session_id].append({"role": "assistant", "content": "".join(full_reply)})

    return Response(stream_with_context(generate()), content_type="text/event-stream")

def read_md(page_id):
    path = os.path.join(CONTENT_DIR, f"{page_id}.md")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()

def page_meta(page_id):
    for p in PAGES:
        if p["id"] == page_id:
            return p
    return None

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)
