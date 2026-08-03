#!/usr/bin/env python3
"""One-shot localizer: translate the English template scaffolding/headings of the
quantum-leap bundle's phase files + open-questions file to PT-BR. Bodies are already
PT-BR. Idempotent: re-running is a no-op once strings are translated."""
import re, pathlib

BUNDLE = pathlib.Path("/Users/nfilho/claude/Scopezilla/DATAPREV-PAT/outputs/quantum-leap")

# Exact full-string replacements (order matters: longer/more specific first).
COMMON = [
    # --- non-stub phase file scaffolding ---
    ("> **Phase orchestration — what's in/out of phase, dependencies, starting state.** Read this first to orient. Per-capability buildable specs live in ",
     "> **Orquestração da fase — o que está dentro/fora da fase, dependências, estado inicial.** Leia isto primeiro para se orientar. As especificações construíveis por capacidade vivem em "),
    (" (when present) — that's what you actually build against, one intent at a time.",
     " (quando presente) — é contra elas que você de fato constrói, um intent por vez."),
    ("> Phase duration: **", "> Duração da fase: **"),
    (" weeks (per user commitment)**.", " semanas (compromisso do usuário)**."),
    ("## Intent\n", "## Intenção\n"),
    ("- **For:**", "- **Para:**"),
    ("- **Outcome:**", "- **Resultado:**"),
    ("- **Measured by:**", "- **Medido por:**"),
    ("- **Must not:**", "- **Não deve:**"),
    ("## Pre-decided (do not re-litigate)", "## Pré-decidido (não re-litigar)"),
    ("## Plan-mode questions (resolve before switching to Build mode)",
     "## Perguntas do modo Plan (resolver antes de passar ao modo Build)"),
    ("## Build-mode questions (ask only if the situation arises)",
     "## Perguntas do modo Build (perguntar só se a situação surgir)"),
    ("## Epics in scope for this phase", "## Épicas no escopo desta fase"),
    ("The phase brief is authoritative. Epics below are listed for cross-reference only — when an automation cites ",
     "O brief de fase é autoritativo. As épicas abaixo estão listadas apenas para referência cruzada — quando uma automação cita "),
    (", this is what it refers to. For deeper epic narrative, see ",
     ", é a isto que ela se refere. Para a narrativa mais profunda da épica, veja "),
    ("## Build targets — orchestration summary", "## Alvos de construção — resumo de orquestração"),
    ("These sections orient the build agent on the shape of the phase. Per-capability buildable detail (Outcome, Build target, Guardrails, Out of scope, Acceptance, Open questions) lives in ",
     "Estas seções orientam o agente de construção sobre o formato da fase. O detalhe construível por capacidade (Resultado, Alvo de construção, Guardrails, Fora de escopo, Aceite, Perguntas em aberto) vive em "),
    (" per intent. When a section below cites ", " por intent. Quando uma seção abaixo cita "),
    (", look up the intent there.", ", consulte o intent lá."),
    ("### Data model", "### Modelo de dados"),
    ("### Automation", "### Automação"),
    ("### UI & navigation", "### UI & navegação"),
    ("### Security & access", "### Segurança & acesso"),
    ("### Reports & dashboards", "### Relatórios & dashboards"),
    ("### Sample data", "### Dados de exemplo"),
    ("_(optional — load only on user request)_", "_(opcional — carregar só a pedido do usuário)_"),
    ("### Data sources", "### Fontes de dados"),
    ("## Acceptance — user-outcome checks (phase-level)",
     "## Aceite — verificações de resultado para o usuário (nível de fase)"),
    ("Phase-level user-outcome claims a stakeholder would walk through to feel \"Phase 1 is done.\" Run them in conversation with the user; mark ",
     "Afirmações de resultado para o usuário, no nível da fase, que um stakeholder percorreria para sentir que \"a Fase 1 está pronta\". Rode-as em conversa com o usuário; marque "),
    (" only when the user agrees. Per-intent acceptance walkthroughs live in ",
     " somente quando o usuário concordar. Os walkthroughs de aceite por intent vivem em "),
    ("## Acceptance — metadata-shaped checks (phase-level)",
     "## Aceite — verificações em forma de metadados (nível de fase)"),
    ("Phase-level metadata-shaped checks — queries the build agent runs against the target org without human help. Run via the Metadata skill (describe / tooling / SOQL). Per-intent acceptance is in ",
     "Verificações em forma de metadados, no nível da fase — consultas que o agente de construção roda contra a org alvo sem ajuda humana. Rode via a skill Metadata (describe / tooling / SOQL). O aceite por intent está em "),
    ("If you find yourself needing to build any of these, stop and surface it — it belongs to a later phase or is explicitly excluded.",
     "Se você perceber que precisa construir qualquer um destes, pare e sinalize — pertence a uma fase posterior ou está explicitamente excluído."),
    ("_(none surfaced in gaps.json — confirm with user during plan-mode review)_",
     "_(nenhum surgiu em gaps.json — confirme com o usuário na revisão do modo Plan)_"),
    ("## Dependencies and risks (from roadmap)", "## Dependências e riscos (do roadmap)"),
    ("## Dependencies and risks", "## Dependências e riscos"),
    ("**Dependencies:**", "**Dependências:**"),
    ("**Risks:**", "**Riscos:**"),
    ("## Story citations covered in this phase", "## Citações de histórias cobertas nesta fase"),
    ("## Recipe boundary", "## Fronteira de recipe"),
    ("When this phase is accepted, ask the user: ", "Quando esta fase for aceita, pergunte ao usuário: "),
    ("The recipe should capture: the data-model decisions made above, the naming patterns confirmed in ",
     "A recipe deve capturar: as decisões de modelo de dados feitas acima, os padrões de nomenclatura confirmados em "),
    (", and any Build-mode question resolutions that emerged.",
     ", e quaisquer resoluções de perguntas do modo Build que surgiram."),
    ("Save this run as a recipe so we can repeat for ", "Salvar esta execução como recipe para repetirmos na "),
    # --- stub phase scaffolding ---
    ("> 🛑 **DO NOT BUILD AGAINST THIS FILE — STUB.**",
     "> 🛑 **NÃO CONSTRUA A PARTIR DESTE ARQUIVO — ESBOÇO (STUB).**"),
    (" has not been staged with a real build brief. The sections below contain placeholders only.",
     " não foi preparada (staged) com um brief de construção real. As seções abaixo contêm apenas placeholders."),
    ("> Regenerate this phase via the ", "> Regere esta fase via a skill "),
    (" skill before any planning or build action targets it.",
     " antes de qualquer ação de planejamento ou construção mirá-la."),
    (" skill before any planning or build action targets it.\n",
     " antes de qualquer ação de planejamento ou construção mirá-la.\n"),
    (", **stop** and tell them the bundle needs to be regenerated.",
     ", **pare** e diga a ele que o bundle precisa ser regerado."),
    ("## Phase metadata (planning only — not a build target)",
     "## Metadados da fase (apenas planejamento — não é alvo de construção)"),
    ("- **Planning duration:**", "- **Duração de planejamento:**"),
    ("- **Outcome (from roadmap):**", "- **Resultado (do roadmap):**"),
    ("- **Measured by (from roadmap):**", "- **Medido por (do roadmap):**"),
    ("## Epics tentatively in scope for this phase", "## Épicas tentativamente no escopo desta fase"),
    ("These are the epics roadmap.json assigned to ", "Estas são as épicas que o roadmap.json atribuiu à "),
    (". They will become a real build target when this phase is staged via the ",
     ". Elas se tornarão um alvo de construção real quando esta fase for preparada (staged) via a skill "),
    (" skill — until then, **do not build against them**.",
     " — até lá, **não construa a partir delas**."),
    ("_(no epics tied to this phase)_", "_(nenhuma épica vinculada a esta fase)_"),
    ("_(no epics tied to this phase)_\n", "_(nenhuma épica vinculada a esta fase)_\n"),
    ("To stage this phase as a real build target, re-run the ",
     "Para preparar esta fase como um alvo de construção real, rode novamente a skill "),
    (" skill and select ", " e selecione "),
    (". The skill will produce intent, pre-decided constraints, plan-mode questions, build targets, and dual-shaped acceptance for the agent to use.",
     ". A skill produzirá intenção, restrições pré-decididas, perguntas do modo Plan, alvos de construção e aceite de dupla forma para o agente usar."),
    # --- 92 open questions scaffolding ---
    ("# Open Engagement Questions — DATAPREV-PAT", "# Perguntas em Aberto do Engajamento — DATAPREV-PAT"),
    ("> Reference role: cross-phase or engagement-level open questions only. Per-phase questions live **inside** the phase brief (under \"Plan-mode questions\" or \"Build-mode questions\"). This file exists to hold what doesn't belong to a single phase.",
     "> Papel de reference: apenas perguntas em aberto que cruzam fases ou de nível de engajamento. As perguntas por fase vivem **dentro** do brief de fase (em \"Perguntas do modo Plan\" ou \"Perguntas do modo Build\"). Este arquivo existe para guardar o que não pertence a uma única fase."),
    ("If this list is empty for an engagement, no file is generated — its absence means \"no cross-phase questions remain.\"",
     "Se esta lista estiver vazia para um engajamento, nenhum arquivo é gerado — sua ausência significa \"não restam perguntas que cruzam fases\"."),
    ("## How to use this file", "## Como usar este arquivo"),
    ("- Walk it once at engagement-start, before planning Phase 1.",
     "- Percorra-o uma vez no início do engajamento, antes de planejar a Fase 1."),
    ("- For each item, surface to the user; capture the answer; append ",
     "- Para cada item, leve ao usuário; capture a resposta; anexe "),
    (" underneath.", " logo abaixo."),
    ("**Resolved:** <answer>", "**Resolvido:** <resposta>"),
    ("  - Notes:", "  - Notas:"),
    # gap-type labels in 92
    ("— Capability Gap**", "— Lacuna de Capacidade**"),
    ("— Missing Requirement**", "— Requisito Ausente**"),
    ("— Ambiguity**", "— Ambiguidade**"),
    ("— Source Conflict**", "— Conflito de Fonte**"),
    ("— Logical Gap**", "— Lacuna Lógica**"),
    ("— Potential Risk**", "— Risco Potencial**"),
    ("— Assumption**", "— Premissa**"),
]

def localize(text):
    for old, new in COMMON:
        text = text.replace(old, new)
    # regex: phase numbers in titles/prose ("Phase 1" -> "Fase 1")
    text = re.sub(r"\bPhase (\d+)\b", r"Fase \1", text)
    # "Out of scope for Fase N" heading (## variant)
    text = text.replace("## Out of scope for Fase", "## Fora do escopo da Fase")
    return text

targets = sorted(BUNDLE.glob("10-phase-*.md")) + [BUNDLE / "92-open-engagement-questions.md"]
for p in targets:
    if not p.exists():
        continue
    original = p.read_text(encoding="utf-8")
    updated = localize(original)
    if updated != original:
        p.write_text(updated, encoding="utf-8")
        print(f"localized: {p.name}")
    else:
        print(f"no change: {p.name}")
