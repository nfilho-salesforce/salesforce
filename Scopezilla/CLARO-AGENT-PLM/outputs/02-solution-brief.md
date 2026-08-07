# Solution Brief — Claro Agente PLM
## POC PLM & Agentforce — Claro Brasil

**Prepared by:** Salesforce Professional Services LATAM  
**Date:** June 2026  
**Version:** 1.0

---

## Executive Summary

Claro Brasil's product catalog is governed by 127 business rules that require a full engineering deployment cycle to change — each new offer, bundle, or pricing adjustment means a sprint, a cross-org deploy, and a window of operational risk. At the same time, large-volume validation batches overflow CPU and heap limits, creating unstable operations and silent failure modes in the product-to-money chain.

This POC replaces the legacy rule engine with an Agentforce-powered Product Lifecycle Management (PLM) platform in 8 weeks. The result: catalog rules authored in Portuguese by business analysts in minutes — no deployment required — and batch validation stable at 10,000+ rows with full failure capture and AI-generated diagnostic reports.

---

## What We're Building

The solution has three interlocking layers, delivered in parallel across an 8-week sprint:

### Layer 1 — The Engine: Fast, Stable, Deterministic Validation

A custom Apex evaluation engine (AST Walker) replaces the legacy rule engine. Rules are compiled once into a structured JSON specification by the Einstein LLM; from that point forward, the validation runs in pure Apex — no AI in the critical path, no unpredictable latency. Each record is evaluated in under 50 milliseconds.

Large CSV files (up to 10,000 rows / 6 million characters) are processed through a resilient asynchronous chain — no more CPU overflows. Every failure is captured in a Dead Letter Queue; no transaction disappears silently.

### Layer 2 — The Intelligence: Business-Led Rule Authoring

An Agentforce Admin Agent gives catalog analysts a natural-language interface to the rule engine. A business analyst describes a new product validation rule in Portuguese — the agent compiles it to a structured specification, presents the result for review, and activates it on approval. No developer. No deployment window. No sprint cycle.

Rule change time: from days to minutes. `KPI-TI-002`

The Agentforce Ops Agent provides an operations interface to the validation pipeline — triggering batch runs, checking statuses, retrying failed items, and generating diagnostic reports, all via conversational commands.

### Layer 3 — The Governance: LGPD-Compliant, Auditable by Design

Every rule carries an immutable identity: a stable Spec Key and a SHA-256 fingerprint of its source. Every compilation is snapshotted with timestamp, user, and version. Every LLM interaction routes through Einstein Trust Layer — Zero-Data Retention Policy active, no Claro pricing data reaching external models.

This audit trail satisfies LGPD requirements and provides the rule lineage ANATEL Res. 680/2020 demands. Claro's legal team reviews and signs off before go-live.

---

## Scope — What's Included

| Epic | What It Delivers |
|---|---|
| **Async CSV Ingestion** | Resilient upload wizard handling files up to 6M characters / 10k rows without CPU overflow |
| **LLM Rule Compilation** | Einstein-powered compiler converts pt-BR business rules to executable JSON specifications |
| **AST Rule Evaluation** | Deterministic Apex engine — <50ms/record, no LLM at runtime, full severity routing (ERRO / AVISO / INFO) by product type (Fone / Banda Larga / TV) |
| **Observability & DLQ** | Zero silent failures — Platform Events, Dead Letter Queues, Transaction Finalizers, ZombieReaper service |
| **AI Diagnostic Narrative** | Automated HTML diagnostic reports per batch — reduces analyst investigation from hours to seconds |
| **Agentforce Admin Agent** | Natural-language rule authoring and management — zero deployments required |
| **Agentforce Ops Agent** | Conversational batch management, error retry, and status monitoring |
| **UX & LWC Components** | Admin and Ops interfaces — upload wizard, evaluation panel, rule catalog manager |
| **Security & Platform Config** | Access model, CMDT configuration, SSO (Okta/SailPoint), permission sets |
| **AI Governance & LGPD** | Einstein Trust Layer activation, rule lineage architecture, Claro legal sign-off |

**Explicitly out of scope for this POC:**
- Bulk API 2.0 ingest for files above 6MB
- Batchable evaluation engine for batches above 50,000 rows
- NBO system integration (Agent 3)
- Platform Encryption (Salesforce Shield)
- Historical data migration

---

## What Success Looks Like

| KPI | Baseline | Target | When |
|---|---|---|---|
| Rule evaluation time per record | Minutes (legacy batch) | < 50ms | Week 8 (UAT validated) |
| Rule authoring & update time | Days (requires deploy) | 0 minutes (no redeploy) | Week 8 (go-live) |
| Batch ingestion capacity | Unstable at large volumes | ≤ 10,000 rows/batch stable | Week 8 (UAT validated) |
| Silent failure rate | Untracked | 0% — 100% DLQ capture | Week 8 |
| AI diagnostic accuracy | Manual investigation (hours) | 95% agent precision in UAT | UAT cycle |

---

## What We Need from Claro

The following dependencies are **Week 1 critical** — if they miss, the Build sprint cannot start on schedule:

| # | What | Owner | When |
|---|---|---|---|
| 1 | 10–15 Knowledge Articles with Data Categories — curated and live in target sandbox | Lucas / Fabrício | Before Build Week 3 |
| 2 | Agentforce Unlimited license + Einstein Flex Credits active on sandbox | Luciano | End of Week 2 |
| 3 | Sandbox chain provisioned: Developer + Partial Copy (SIT) + Full Copy / Ibuy (UAT) | Luciano / DevOps | End of Week 1 |
| 4 | `RunSpecifiedTests` class registry agreed with PS team | Luciano / DevOps | Weeks 1–2 |
| 5 | Sample production Demanda CSVs (3–5 files) for volume profiling | Lucas | Week 1 |
| 6 | Claro legal review window allocated (Week 6) for LGPD sign-off | Legal | Scheduled by Week 2 |

---

## Delivery Phases

| Phase | Weeks | Focus |
|---|---|---|
| **Phase 0: Discovery & Architecture** | 1–2 | Technical alignment, schema finalization, sandbox setup, client dependency confirmation |
| **Phase 1: Build Sprints** | 3–5 | Engine build (E01–E05), agent configuration (E06–E07), UX (E08), security (E09) |
| **Phase 2: UAT & Fine-Tuning** | 6–7 | Concurrency testing, agent precision validation, LGPD review, parallel run vs. legacy BRE |
| **Phase 3: Go-Live & Hypercare** | 8 | Production deploy (RunSpecifiedTests), hypercare, knowledge transfer |

---

## Team

| Role | Allocation | Responsibilities |
|---|---|---|
| Technical Architect (PS) | Full — 8 weeks | Architecture decisions, engine design, LGPD controls, agent configuration |
| Technical Consultant (PS) | Full — 8 weeks | Apex development (E01–E05), LWC components (E08), deployment pipeline |
| QA Specialist (PS) | 1.5 — 8 weeks | Test strategy, concurrency testing, UAT support, RunSpecifiedTests registry |
| Project Manager (PS) | Dedicated — billable | Delivery governance, milestone tracking, client dependency coordination |

**Claro team required:** Lucas (SME, weekly), Luciano (DevOps/infra), Fabrício (business sign-off), Legal (Week 6 LGPD review), Analistas operacionais (UAT Week 6–7).

---

## Architecture at a Glance

```
  Business Analyst                    Ops User
       │ "New rule: BL must have..."       │ "Run batch for Demanda #42"
       ▼                                   ▼
  ┌──────────────────┐            ┌────────────────────┐
  │  Admin Agent     │            │  Ops Agent         │
  │  (compile-time)  │            │  (runtime)         │
  └────────┬─────────┘            └────────┬───────────┘
           │ ConnectApi                     │ Apex Invocable
           ▼                               ▼
  ┌─────────────────────┐       ┌────────────────────────┐
  │  Einstein LLM       │       │  Async CSV Ingest      │
  │  (Trust Layer)      │       │  → AST Walker          │
  │  pt-BR → AST JSON   │       │  → DLQ / Finalizer     │
  └─────────────────────┘       │  → Diagnostic Narrative│
                                └────────────────────────┘
                     Foundation: Observability + DLQ + LGPD Controls
```

---

*For the full technical architecture, see the Architecture Reference document.*  
*Salesforce Professional Services LATAM — Confidential*
