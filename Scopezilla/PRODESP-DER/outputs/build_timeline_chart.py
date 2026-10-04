#!/usr/bin/env python3
"""Gantt-style timeline PNG for PRODESP-DER — chart only, no page header/footer.

Basis: data/roadmap.json (6 committed phases, 20 weeks, duration_source="user"
on every phase) + data/epics.json (capabilities, per-epic deliverable detail)
+ data/resource-plan.json (PS-11/PS-12 sustainment roster referenced in Fase 5).
Fase 5 — Operação Assistida (Hypercare) + Handover à Sustentação — is
committed canonical scope (user decision 2026-09-24, duration adjusted
8→6 weeks on 2026-10-04, propagated via `revise`), not a proposal.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D

# ---- Phases: (row_label, start_week, end_week, color, headline deliverable) ----
PHASES = [
    ("Fase 0 · Resolução de Discovery", 1, 2, "#8a8f98",
        "Gaps bloqueadores resolvidos e escopo de Change Management dimensionado"),
    ("Fase 1 · Fundação (Registro + Integrações)", 2, 5, "#3B78E7",
        "Registro da ocorrência e integrações SIGOR/SIGEO operacionais"),
    ("Fase 2 · Despacho Automatizado + Canal Digital", 5, 8, "#2FA36B",
        "Despacho automatizado nas 14 CGRs e canal digital (WhatsApp + CTI) ativos"),
    ("Fase 3 · Execução em Campo", 8, 11, "#E0A72E",
        "App de campo em produção nas 14 CGRs — 1.152 operadores"),
    ("Fase 4 · Rastreamento, Visibilidade e Estabilização", 11, 15, "#C4432B",
        "UAT estadual assinado e go-live pleno"),
    ("Fase 5 · Op. Assistida e Handover à Sustentação", 15, 21, "#8E5FC9",
        "Hypercare de 6 semanas com handover formal à Sustentação"),
]

TOTAL_WEEKS = 21  # S1..S20 build/hypercare + handover marker at S21

MILESTONES = [
    (2,  "M0", "Discovery resolvido"),
    (5,  "M1", "Fundação pronta"),
    (8,  "M2", "Despacho + Canal Digital ativos"),
    (11, "M3", "Execução em campo em produção"),
    (15, "M4", "Go-live estadual pleno"),
    (21, "M5", "Handover p/ Sustentação"),
]

fig, ax = plt.subplots(figsize=(18, 6.2), dpi=200)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

n = len(PHASES)
row_spacing = 0.95
bar_h = 0.42

for i, (label, s, e, color, headline) in enumerate(PHASES):
    y = (n - i) * row_spacing  # top row = Fase 0
    ax.add_patch(FancyBboxPatch(
        (s, y - bar_h / 2), e - s, bar_h,
        boxstyle="round,pad=0,rounding_size=0.08",
        linewidth=0, facecolor=color, alpha=0.92, zorder=3,
    ))
    ax.text(s + (e - s) / 2, y, f"{e - s} sem.", ha="center", va="center",
            fontsize=9, fontweight="bold", color="white", zorder=4)
    # one headline deliverable beneath the bar — executive-level, not a checklist
    ax.text(s + 0.15, y - bar_h / 2 - 0.13, f"• {headline}", ha="left", va="top",
            fontsize=9.3, color="#2b2f36", zorder=4)
    # row label on the left
    ax.text(0.6, y, label, ha="right", va="center", fontsize=10.3,
            fontweight="bold", color="#1a1d23", zorder=4)

# milestone verticals + diamonds
top_y = n * row_spacing
for wk, code, name in MILESTONES:
    ax.axvline(wk, color="#9aa1ab", linestyle=(0, (4, 3)), linewidth=1, zorder=1)
    ax.plot(wk, top_y + 0.85, marker="D", markersize=9, color="#1a1d23", zorder=5)
    ax.text(wk, top_y + 1.15, code, ha="center", va="bottom", fontsize=9.5,
            fontweight="bold", color="#1a1d23", zorder=5)

# week axis
ax.set_xlim(0.5, TOTAL_WEEKS + 0.5)
ax.set_ylim(-0.9, top_y + 1.4)
week_ticks = list(range(1, TOTAL_WEEKS + 1, 1))
ax.set_xticks(week_ticks)
ax.set_xticklabels([f"S{w}" for w in week_ticks], fontsize=8, color="#4a4f58")
ax.set_yticks([])
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#c7cbd1")
ax.tick_params(axis="x", length=3, color="#c7cbd1")
ax.set_axisbelow(True)
ax.grid(axis="x", color="#eceef1", linewidth=0.7, zorder=0)

# phase separator between committed build (S1-15) and hypercare block (S15-23)
ax.axvline(15, color="#1a1d23", linestyle="-", linewidth=1.3, alpha=0.35, zorder=2)

# legend: milestone codes + lane color key (this is the requested "legenda", not a page footer)
legend_lines = [f"{code} — {name}" for _, code, name in MILESTONES]
legend_text = "Marcos:   " + "    ".join(legend_lines)
ax.text(0.5, -0.55, legend_text, ha="left", va="top", fontsize=8.6,
        color="#4a4f58", transform=ax.transData)

handles = [
    Line2D([0], [0], color="#3B78E7", lw=8, label="Fases de build (comprometido, 14 sem.)"),
    Line2D([0], [0], color="#8E5FC9", lw=8, label="Operação Assistida + Handover — comprometido (6 sem.)"),
    Line2D([0], [0], marker="D", color="#1a1d23", linestyle="None", markersize=8, label="Marco de fase"),
]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1.11),
          ncol=3, frameon=False, fontsize=9.5)

fig.subplots_adjust(left=0.26, right=0.99, top=0.90, bottom=0.11)

out_path = "outputs/artifacts/der-timeline.png"
fig.savefig(out_path, facecolor="white")
print("wrote", out_path)
