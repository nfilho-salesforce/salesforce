# 0002 — Gap de licenciamento: Experience Cloud não contemplado na contratação do Experience Hub

**Date:** 2026-08-04 · **Status:** accepted · **Source:** client-supplied

## Context
O Tech Assessment registrou explicitamente, nos Highlights, que o **Experience Cloud não foi contemplado na contratação do Experience Hub** da BV. Os portais em escopo (Governança, Parceiros, Parceiros Interno) são sites Experience Cloud e dependem de licenças/entitlements de Experience Cloud (member-based ou login-based) que hoje não estão cobertos pelo contrato vigente. Usuário confirmou que o gap está **em aberto / a resolver** (2026-08-04).

## Decision
O projeto de Professional Services **não inclui** a aquisição de licenças. Fica registrado como **premissa e bloqueador comercial**: BV precisa contratar/regularizar as licenças de Experience Cloud dimensionadas para os tipos de usuário externos e internos dos portais **antes do go-live**. O escopo de serviços PS assume que as licenças estarão disponíveis nos ambientes no momento em que cada portal for ativado.

## Consequences
- Bloqueador de go-live: sem as licenças, os portais não podem ser publicados a usuários finais, independentemente do build estar pronto.
- Dependência comercial paralela ao SOW de serviços (trilha de licenciamento own-by-BV/account team).
- O dimensionamento de licenças depende da contagem de usuários por persona — hoje **desconhecida** (ver Open Questions do Discovery Brief).
- Também registrada a **limitação do Anypoint da MuleSoft** como constraint técnico correlato (Highlights do assessment).

## Grounds
`discovery-notes/v4_BV - Experience Cloud - Professional Services _ ROM_DD FY26.pdf` (slide "Highlights": "Não foi contemplado Experience Cloud na contratação do Experience Hub"; "Limitação do anyponit da MuleSoft") + confirmação direta do usuário (2026-08-04).
