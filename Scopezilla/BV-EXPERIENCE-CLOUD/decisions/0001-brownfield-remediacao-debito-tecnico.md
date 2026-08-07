# 0001 — Engajamento brownfield: remediação de débito técnico + ativação de recursos sobre portais Experience Cloud já em produção

**Date:** 2026-08-04 · **Status:** accepted · **Source:** client-supplied

## Context
O Banco BV já possui três portais construídos sobre Salesforce Experience Cloud em produção — Portal Governança (ciclo de vida de APIs), Portal Parceiros (portal externo de desenvolvedores/parceiros) e Portal Parceiros Interno. A Salesforce Professional Services (arquitetos Antonio Torres e David Pendeza) realizou um Tech Assessment (jun/2025, FY26) cujo objetivo declarado foi "mapear as ações prioritárias — técnicas e funcionais — necessárias para a correção de débitos técnicos e a ativação de recursos prioritários", garantindo estabilidade, performance e evolução contínua. Confirmado pelo usuário: os portais já estão no ar.

## Decision
O escopo é tratado como **brownfield** — construímos dentro de uma solução Experience Cloud + MuleSoft existente e viva, não do zero. Cada tarefa do backlog é ou (a) correção de débito técnico sobre algo existente, ou (b) ativação/configuração de recurso prioritário adicional. A ordem de trabalho, a estratégia de deploy e a linguagem de estado-inicial refletem que há produção a preservar.

## Consequences
- Estimativa e roadmap assumem regressão/preservação do que já existe: gestão de release, testes de não-regressão e coexistência com dados/configuração vivos entram no esforço.
- O handoff de build (se houver `quantum-leap`) captura o estado do org como brownfield.
- Migração de catálogos/APIs existentes é parte do escopo (não é carga inicial de org limpo).
- Reverter esta premissa (tratar como greenfield) reescreveria abordagem de fases, testes e migração.

## Grounds
`discovery-notes/v4_BV - Experience Cloud - Professional Services _ ROM_DD FY26.pdf` (slide "Tech Assessment: O que vimos?" — "correção de débitos técnicos e a ativação de recursos prioritários" na plataforma Experience Cloud da BV) + confirmação direta do usuário (2026-08-04).
