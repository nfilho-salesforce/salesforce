# AI Delivery Efficiency Analysis
## CLARO Agente PLM — POC PLM & Agentforce

**Audience:** Internal PS team (TA, TC, PM) — not client-facing  
**Version:** 1.0 · 2026-06-17  
**Source:** Benchmark-based — model training data on Agentforce/Apex AI-assisted delivery  

> **Disclaimer:** Efficiency estimates are benchmark-based. Actual compression depends on team AI-tooling proficiency, Claro data availability, and sandbox stability. For internal planning only — not a client commitment.

---

## The Core Point

The 8-week timeline is fixed and non-negotiable. AI-native delivery on this engagement does **not** compress the calendar — it converts **schedule risk into quality headroom** in the Build sprint (Weeks 3–5), which is the highest-risk phase of any SC-complexity POC.

Without AI leverage, a 3-week Build window for 10 epics at Super Custom complexity would require near-perfect execution with no rework. With AI tooling, the PS team spends less time on boilerplate authoring and test scaffolding, and more time on the things that actually require human judgment: spike validation, Prompt Template iteration, agent instruction tuning, and parallel-run verification.

---

## AI Leverage by Epic

| Epic | Leverage | Est. Build Compression | Primary Driver |
|---|---|---|---|
| E01 Async CSV Ingestion | 🔴 **High** | 30–40% | Queueable chain + cursor boilerplate; AI unit test generation reaches 85% faster |
| E02 LLM Rule Compilation | 🟠 **Medium-High** | 25–35% | ConnectApi service scaffolding; Prompt Template few-shot drafting |
| E03 AST Rule Evaluation | 🔴 **High** | 30–40% | AST walker algorithm well-known to AI; static Map cache + cursor reuse from E01 |
| E04 Observability + DLQ | 🔴 **High** | 30–40% | Platform Event, Finalizer, Schedulable, DLQ patterns — highly repetitive; all fast with AI |
| E05 AI Diagnostic Narrative | 🟠 **Medium-High** | 25–35% | Context builder scaffolding; Prompt Template system prompt drafting |
| E06 PLM Admin Agent | 🟡 **Medium** | 15–25% | Subagent instruction drafting; invocable scaffolding — Agentforce Builder UI still requires human |
| E07 PLM Ops Agent | 🟡 **Medium** | 15–25% | 6 subagent instructions drafted by AI — more repetitive than E06 |
| E08 UX & LWC Components | 🟡 **Medium** | 20–30% | Component scaffolding fast; ceiling is Claro SME iteration cycle |
| E09 Security + Platform Config | 🟡 **Medium** | 15–25% | Permset XML + CMDT seed rows generated from schema — structural, repetitive |
| E10 AI Governance + LGPD | 🟢 **Low** | 10–15% | ETL docs drafted faster; constraint is legal sign-off gate, not PS effort |

**Build phase weighted compression (Weeks 3–5):** **25–35%** of PS build effort  
*Applies to: E01–E08 build work. Does not apply to: P0 dependency resolution, P2 UAT, LGPD gate, production deploy.*

---

## What This Means Per Sprint

### Sprint 1 — Foundation (Week 3)
- **Without AI:** E01 + E09 fills the week; CPU spike competes with delivery work.
- **With AI:** E01 Queueable chain + permset XML drafted in ~60% of normal time. Remaining buffer absorbs the CPU spike + peer review. **Sprint 1 finishes clean with no cascade risk into S2.**

### Sprint 2 — Core Engine (Week 4)
- **Without AI:** E02 + E03 + E04 in one week is the highest-risk sprint — three SC-complexity epics.
- **With AI:** E01 cursor pattern reused in E03 (same Queueable/Id-cursor shape). E04 Platform Event + Finalizer boilerplate AI-generated in parallel. AST Walker algorithm well-suited to AI code generation. **Three epics complete within the week; Sub-50ms + Finalizer quota spikes resolved with time to spare.**

### Sprint 3 — Intelligence & UX (Week 5)
- **Without AI:** Four epics (E05, E06, E07, E08) + SIT→UAT deploy in one week is very tight.
- **With AI:** E05 context builder scaffolded fast; E08 LWC shells generated from component specs. **Time reclaimed is invested in E06/E07 agent instruction quality and first agent UAT pass — the thing that most affects the 95% precision KPI.**

---

## Where AI Tooling Helps Most

1. **Apex boilerplate** — Queueable patterns, Schedulable, Batchable, Finalizer, Platform Event publisher/subscriber. All are well-documented, pattern-driven code that AI generates accurately.
2. **Unit test scaffolding** — AI reaches ≥85% Apex coverage faster and more systematically than manual authoring. Async test patterns (Test.startTest/stopTest, mock callouts) are in AI training data.
3. **Prompt Template authoring** — AI drafts system prompts and few-shot examples; human iterates on quality with real Claro rule data. Net: fewer iteration cycles needed.
4. **Subagent instruction drafting** — Natural-language instructions for Atlas Reasoning Engine are a strong AI use case. TA reviews and refines rather than authors from blank.
5. **CMDT and permset XML** — Structural, repetitive configuration data. AI generates from a schema spec in minutes; human validates correctness.
6. **Documentation** — LGPD evidence package, test plans, RunSpecifiedTests registry — AI drafts, TA reviews. Reduces documentation overhead that competes with build time.

---

## Where AI Tooling Does NOT Help

These are the real constraints on this engagement. No amount of AI tooling moves them:

| Constraint | Why AI can't help |
|---|---|
| GAP-001: Knowledge Articles | Claro content ownership — must be human-curated |
| GAP-002: Agentforce license | Salesforce provisioning process — calendar-bound |
| GAP-003: Sandbox chain | Claro IT provisioning — calendar-bound |
| GAP-005: LGPD legal sign-off | Human legal review — Week 6 gate is fixed |
| CPU spike (E01/E03) | Governor limits require live profiling — AI cannot substitute |
| Finalizer quota (E04) | Platform quota validation requires sandbox test — AI cannot predict |
| Agent precision (E06/E07) | 95% UAT target requires iteration with real Claro users and KB content |
| Parallel run parity (E03 vs BRE) | Requires live comparison with real production rule outputs |

**The binding constraint on this engagement is P0 client dependencies — not PS build capacity.** AI leverage is a safety net for the Build sprint; the real delivery risk is whether Claro resolves all 6 GAPs before Week 3.

---

## Recommended AI Tooling Stack for This Engagement

| Tool | Use Cases |
|---|---|
| **Claude Code / Claude Sonnet** | Apex class scaffolding, unit test generation, Prompt Template drafting, subagent instruction authoring, documentation drafting, permset/CMDT XML generation |
| **GitHub Copilot** | In-IDE real-time completion for Apex patterns (Queueable, Finalizer, Platform Events) |
| **Salesforce Prompt Builder** (native) | PLM_Rule_Compiler and PLM_Diagnostico_Narrativa Prompt Template configuration and iteration |
| **Agentforce Builder** (native) | Subagent/topic configuration — no AI acceleration available; this is UI-driven |

---

## Summary Verdict

The AI-native delivery advantage on this POC is **real but bounded**. It turns the Build sprint from a high-risk three-week sprint into a manageable one with quality headroom. The risk it does not reduce is the six client dependencies in P0 — those are the actual critical path. The PM's job in Weeks 1–2 is more important to on-time delivery than any efficiency gain in Weeks 3–5.

*Benchmark-based — model training data. For internal PS planning only.*
