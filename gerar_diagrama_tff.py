import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(18, 11))
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis('off')
fig.patch.set_facecolor('#0f1623')

# ── Helpers ──────────────────────────────────────────────────────────────────

def box(ax, x, y, w, h, facecolor, edgecolor, radius=0.25):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={radius}",
                       facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5, zorder=3)
    ax.add_patch(p)

def label(ax, x, y, text, size=9, color='white', weight='normal', ha='center', va='center'):
    ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=4)

def arrow(ax, x1, y1, x2, y2, color='#38bdf8', lw=1.8, style='->', dash=False):
    ls = (0, (5, 4)) if dash else 'solid'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                linestyle=ls, connectionstyle='arc3,rad=0'),
                zorder=5)

def section_header(ax, x, y, w, text, color):
    box(ax, x, y, w, 0.45, facecolor='#1a2535', edgecolor=color, radius=0.18)
    label(ax, x + w/2, y + 0.225, text, size=8, color=color, weight='bold')

# ── Fundo das colunas ─────────────────────────────────────────────────────────

col_bg = [
    (0.3,  0.5, 3.0,  10.2, '#111c2b', '#1e2d42'),   # Fontes
    (4.1,  0.5, 3.4,  10.2, '#1a1005', '#3d1f03'),   # MuleSoft
    (8.3,  0.5, 4.2,  10.2, '#051520', '#0e3450'),   # SF Platform
    (13.3, 0.5, 4.4,  10.2, '#120d22', '#2a1a4e'),   # Saídas
]
for (x, y, w, h, fc, ec) in col_bg:
    box(ax, x, y, w, h, fc, ec, radius=0.35)

# ── Cabeçalhos de coluna ──────────────────────────────────────────────────────

section_header(ax, 0.3,  10.3, 3.0, 'FONTES DE DADOS',    '#94a3b8')
section_header(ax, 4.1,  10.3, 3.4, 'ORQUESTRADOR',       '#fb923c')
section_header(ax, 8.3,  10.3, 4.2, 'SALESFORCE PLATFORM','#38bdf8')
section_header(ax, 13.3, 10.3, 4.4, 'SAÍDAS / USUÁRIO',   '#a78bfa')

# ── FONTES ────────────────────────────────────────────────────────────────────

sources = [
    (0.55, 8.2, 'SITARWEB', 'Sistema de fiscalização\nde estações de rádio', 'Legacy / API REST', '#f97316', '#2d1e10'),
    (0.55, 5.5, 'DB_TELECOM', 'Obrigações e contribuintes\nTFF principais', 'SQL Server / JDBC', '#60a5fa', '#0e2040'),
    (0.55, 2.8, 'SMS / FISTEL', 'Registros e histórico\nde arrecadação', 'MongoDB Connector', '#4ade80', '#0d2b18'),
]
for (x, y, title, desc, tag, tc, bg) in sources:
    box(ax, x, y, 2.55, 1.5, facecolor=bg, edgecolor=tc, radius=0.2)
    label(ax, x + 1.275, y + 1.1,  title, size=10, color=tc, weight='bold')
    label(ax, x + 1.275, y + 0.65, desc,  size=8,  color='#94a3b8')
    box(ax, x + 0.5, y + 0.1, 1.55, 0.38, facecolor='#1a2535', edgecolor=tc, radius=0.1)
    label(ax, x + 1.275, y + 0.29, tag, size=7.5, color=tc, weight='bold')

# Alerta fontes
box(ax, 0.55, 0.75, 2.55, 1.6, facecolor='#1f1008', edgecolor='#92400e', radius=0.2)
label(ax, 1.825, 1.8, '⚠  ~10M registros', size=8.5, color='#f59e0b', weight='bold')
label(ax, 1.825, 1.38, 'Identidade fragmentada', size=8, color='#fbbf24')
label(ax, 1.825, 1.08, 'entre as 3 fontes', size=8, color='#fbbf24')
label(ax, 1.825, 0.78, 'Deduplicação no MuleSoft', size=7.5, color='#d97706')

# ── SETAS Fontes → MuleSoft ───────────────────────────────────────────────────

arrow(ax, 3.1, 8.95,  4.1, 6.4, color='#f97316', lw=2)
arrow(ax, 3.1, 6.25,  4.1, 6.1, color='#60a5fa', lw=2)
arrow(ax, 3.1, 3.55,  4.1, 5.85, color='#4ade80', lw=2)

label(ax, 3.55, 8.0,  'API REST',  size=7, color='#a78bfa')
label(ax, 3.52, 6.27, 'JDBC',      size=7, color='#a78bfa')
label(ax, 3.55, 4.4,  'Mongo\nConn.', size=7, color='#a78bfa')

# ── MULESOFT (bloco central) ───────────────────────────────────────────────────

box(ax, 4.3, 2.2, 3.0, 7.4, facecolor='#271305', edgecolor='#f97316', radius=0.35)
label(ax, 5.8, 9.1,  '⚙',          size=22, color='#f97316')
label(ax, 5.8, 8.45, 'MuleSoft',   size=13, color='#fb923c', weight='bold')
label(ax, 5.8, 8.0,  'Anypoint Platform', size=8, color='#d97706')

box(ax, 4.65, 7.35, 2.3, 0.35, facecolor='#7c2d12', edgecolor='#ea580c', radius=0.12)
label(ax, 5.8, 7.52, 'ORQUESTRADOR', size=7.5, color='#fed7aa', weight='bold')

features = [
    ('Normalização de esquemas',    6.8),
    ('Transformação de dados',      6.35),
    ('Deduplicação de registros',   5.9),
    ('Roteamento por tipo',         5.45),
    ('Error handling & retry',      5.0),
    ('Auditoria de transações',     4.55),
    ('Rate limiting / throttling',  4.1),
    ('Monitoramento (Anypoint)',     3.65),
]
for (feat, fy) in features:
    label(ax, 4.85, fy, '▸', size=9, color='#f97316', ha='left')
    label(ax, 5.1,  fy, feat, size=8, color='#92400e', ha='left')

# Protocolo saída
box(ax, 4.65, 2.35, 2.3, 0.65, facecolor='#3d1f03', edgecolor='#ea580c', radius=0.12)
label(ax, 5.8, 2.84, 'Salesforce REST API', size=8, color='#fdba74', weight='bold')
label(ax, 5.8, 2.52, 'Platform Events / Bulk API', size=7.5, color='#d97706')

# ── SETAS MuleSoft → SF Platform ─────────────────────────────────────────────

sf_targets_y = [8.7, 6.9, 5.1, 3.3]
for ty in sf_targets_y:
    arrow(ax, 7.3, 6.15, 8.3, ty, color='#38bdf8', lw=1.8)

# ── SF PLATFORM ───────────────────────────────────────────────────────────────

sf_cards = [
    (8.5, 7.9, 'Flow Builder',     'Jornada anti-inadimplência\nD-30/D-15/D-7/D+1/D+15',   'Automação',   '#0f3050', '#93c5fd', '#7dd3fc'),
    (8.5, 6.1, 'Service Cloud',    'Fila unificada de atendimento\ne gestão de casos TFF',   'Case Mgmt',   '#051b2e', '#38bdf8', '#38bdf8'),
    (8.5, 4.3, 'Big Objects',      'Retenção imutável de 7 anos\nauditável (TCU/compliance)', 'Compliance',  '#0a1e35', '#60a5fa', '#60a5fa'),
    (8.5, 2.5, 'Experience Cloud', 'Portal do contribuinte:\nconsulta e pagamento TFF/TFI',  'Portal',      '#051520', '#38bdf8', '#7dd3fc'),
]
for (x, y, title, desc, tag, bg, ec, tc) in sf_cards:
    box(ax, x, y, 3.6, 1.5, facecolor=bg, edgecolor=ec, radius=0.2)
    label(ax, x + 1.8, y + 1.12, title, size=10, color=tc, weight='bold')
    label(ax, x + 1.8, y + 0.65, desc,  size=8,  color='#94a3b8')
    box(ax, x + 1.05, y + 0.1, 1.5, 0.38, facecolor='#0c3b5e', edgecolor=ec, radius=0.1)
    label(ax, x + 1.8,  y + 0.29, tag, size=7.5, color=tc, weight='bold')

# ── SETAS SF Platform → Saídas ────────────────────────────────────────────────

out_pairs = [
    (8.1, 7.15, 1),  # → WhatsApp/Email
    (8.1, 6.4, 2),   # → Atendimento
    (8.1, 5.1, 3),   # → Auditoria
    (8.1, 2.8, 4),   # → Portal
]
out_y = [8.5, 6.7, 4.9, 3.1]
for i, oy in enumerate(out_y):
    arrow(ax, 12.1, [8.65, 6.85, 5.05, 3.25][i], 13.3, oy, color='#a78bfa', lw=1.8)

# ── SAÍDAS ────────────────────────────────────────────────────────────────────

outputs = [
    (13.5, 7.9, 'WhatsApp + E-mail',  'Notificações automáticas\nda jornada com link de pagamento', 'Omnichannel', '#1a2e1a', '#4ade80', '#4ade80'),
    (13.5, 6.1, 'Atendimento TFF',    'Servidor com contexto completo\ndo contribuinte e histórico SF',  'Service Cloud', '#051b2e', '#7dd3fc', '#7dd3fc'),
    (13.5, 4.3, 'Trilha de Auditoria','7 anos imutáveis para\nconformidade fiscal e TCU',               'Big Objects',  '#0a1e35', '#a78bfa', '#c4b5fd'),
    (13.5, 2.5, 'Portal Contribuinte','Consulta, histórico e\npagamento de obrigações TFF/TFI',         'Self-service', '#16102b', '#a78bfa', '#a78bfa'),
]
for (x, y, title, desc, tag, bg, ec, tc) in outputs:
    box(ax, x, y, 3.9, 1.5, facecolor=bg, edgecolor=ec, radius=0.2)
    label(ax, x + 1.95, y + 1.12, title, size=10, color=tc, weight='bold')
    label(ax, x + 1.95, y + 0.65, desc,  size=8,  color='#94a3b8')
    box(ax, x + 1.2, y + 0.1, 1.5, 0.38, facecolor='#16102b', edgecolor=ec, radius=0.1)
    label(ax, x + 1.95, y + 0.29, tag, size=7.5, color=tc, weight='bold')

# ── TÍTULO E RODAPÉ ───────────────────────────────────────────────────────────

label(ax, 9.0, 10.75, 'ANATEL — TFF/TFI Arrecadação Inteligente',
      size=15, color='white', weight='bold')
label(ax, 9.0, 10.35, 'Fase 2  ·  Arquitetura de Dados  ·  MuleSoft como Orquestrador',
      size=9, color='#64748b')

# Alerta regulatório
box(ax, 4.1, 0.05, 9.6, 0.62, facecolor='#1f1008', edgecolor='#92400e', radius=0.18)
label(ax, 8.9, 0.36,
      '⚠  Prazo regulatório crítico: Go-live início de março/2027 — margem de 4 semanas antes do prazo de 31/03/2027 para geração de boletos TFF',
      size=8, color='#f59e0b')

# Legenda
legend_items = [
    ('#f97316', 'Ingestão — MuleSoft Connectors'),
    ('#38bdf8', 'Distribuição — Salesforce APIs'),
    ('#a78bfa', 'Entrega ao usuário'),
]
lx = 0.4
for (lc, lt) in legend_items:
    ax.annotate('', xy=(lx + 0.55, 0.28), xytext=(lx, 0.28),
                arrowprops=dict(arrowstyle='->', color=lc, lw=1.5), zorder=6)
    label(ax, lx + 0.65, 0.28, lt, size=7.5, color='#64748b', ha='left')
    lx += 3.5

plt.tight_layout(pad=0.3)
plt.savefig('/Users/nfilho/claude/ANATEL_TFF_Arquitetura.pdf',
            format='pdf', dpi=200, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print('PDF gerado com sucesso.')
