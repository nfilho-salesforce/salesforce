# Headless is the Beginning of a New Software Model
Source: STAAR — 5.2 - Generative & Agentic A.I. / 5.2.4. - AI & Agentic Resp., Gov. & CoE, Value (& XD, FDEs)
File: Headless is the Beginning of a New Software Model (PStokes).pdf
Author: Patrick Stokes (internal Salesforce essay)
Relevance: This project's Fase 2+ vision deck (Vinicius Ferraz, "Atendimento Poupatempo") repeatedly invokes "Headless 360" as the umbrella architecture for the whole-house Poupatempo platform, but the term is undefined in the discovery-notes themselves. This is the primary internal doctrine document behind that name — it grounds what "Headless 360" actually means as a product/architecture bet, distinct from a mere API layer.

## Core claim

Headless 360 is not "our products now have APIs." It is a new operating model for enterprise software: **agents execute, humans direct, and the platform mediates trust, permissions, workflow, data, metadata, policy, and governance between them.** Treating headless as a technical attribute (bolt APIs/MCP tools onto existing products) is a real but small first step; the real shift is a rethink of what each cloud is *for*.

## Two products in parallel

Every cloud becomes two products at once, with different users, buyers, roadmaps, and success metrics:
- **A runtime that serves agents** — the durable substrate (metadata, workflow, permissions, policy) that an agent can operate safely on a human's behalf.
- **An intent surface that serves humans** — not "no UI," but UI whose job shifts from operating every record/field/report directly to directing work, reviewing recommendations, approving actions, correcting mistakes, setting policy, building trust.

## The doctrine, in one line

**Humans direct, agents execute, the platform governs.** Every product leader (and, by extension, every PS architect scoping an engagement) should be able to answer: what does this cloud become when the primary operator is no longer a human clicking through a UI, but an agent acting on a human's intent?

## Shared horizontal agent infrastructure (platform-level, cannot be reinvented cloud by cloud)

Auth, permissions, policy enforcement, tool catalogs, observability, audit trails, human handoff, evaluation, testing, rollback, trust signals. The agent operates across Sales, Service, Marketing, Commerce, Data, Tableau, **Slack, MuleSoft**, and third-party systems in a single flow of work — it does not respect internal cloud/P&L boundaries.

## Why this grounds the Poupatempo Fase 2+ vision

The Vinicius deck's "Headless" claim (Salesforce running "atrás," the citizen/attendant never opening a classic screen) is exactly the doctrine described here: WhatsApp (citizen intent surface) and Slack (attendant intent surface) sit on top of a Salesforce runtime (Data 360, MuleSoft-mediated access to gov.br/biometria/legado) that an agent operates, with humans directing and the platform governing. Because this doctrine explicitly frames pricing, buyer, and org model as needing to change alongside the architecture, it reinforces `decisions/0001`'s caution: the Fase 2+ platform bet is not just an integration scope question, it is a different commercial conversation than the Fase 1 tactical pilot.

## Risk named in the source (relevant to positioning, not to this SOW's scope)

"If we underbuild this, the agents will still come. They will just operate somewhere else... The customer's intent layer will move away from Salesforce." — i.e., the strategic case *for* eventually pursuing the Fase 2+ platform is that a citizen/attendant AI experience will get built on top of PRODESP's systems one way or another; the open question is whether it runs on the governed Salesforce trust boundary or around it. Useful framing for an executive conversation about Fase 2+, not a claim about this project's committed scope.
