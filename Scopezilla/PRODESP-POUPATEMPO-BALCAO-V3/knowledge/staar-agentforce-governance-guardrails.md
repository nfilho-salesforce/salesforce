# Making AI Work: Governance and Guardrails for your Agentforce Transformation
Source: STAAR — 5.2 - Generative & Agentic A.I. / 5.2.4. - AI & Agentic Resp., Gov. & CoE, Value (& XD, FDEs)
File: Agentforce - Governance and Guardrails - Making AI Work - SF PS Webinar -.pptx (42 slides, Salesforce PS webinar)
Relevance: Governance/adoption was explicitly confirmed in scope for this project (user, 2026-09-21), and LGPD is a first-order design driver (moving inter-posto coordination off personal WhatsApp into auditable Slack channels; no raw biometric data in text channels). This deck is the generic Salesforce PS framework for defining an agent's guardrails and governance model — directly applicable to the Agentforce-in-Slack agent this project's Fase 1 design would deploy.

## Bots vs. Agentforce vs. People — why governance differs

- **Bots**: fixed rules, deterministic, scripted phrases, static data. Governed like process diagrams/decision trees.
- **Agentforce**: converses in natural language, decides what to do in the course of interaction, uses information to communicate and reason (not just fetch it). Governed by Jobs To Be Done, Policy & Guardrails, an Agent Management Strategy, Agent Monitoring Requirements.
- **People**: execute based on knowledge/experience, apply judgment in novel situations.

Because Agentforce "decides" rather than just "executes a script," it needs a different governance toolkit than a bot would — relevant since the Poupatempo Fase 1 design explicitly puts Agentforce (not a scripted bot) inside the attendant's Slack channel.

## The 5 attributes of an agent (design checklist)

1. **Role** — what job should it do
2. **Data** — what knowledge can it access
3. **Actions** — what capabilities does it have
4. **Channel** — where does it work
5. **Guardrails** — what shouldn't it do (anchored in Trust)

**Worked example in the source ("Order Status Agent"), directly analogous to this project's guichê agent:**
- Role: provide order status to a customer inquiring about their own order.
- Data: order number, contents, ship/delivery dates, signature requirements.
- Actions: confirm customer identity → identify their order → display status.
- Channel: company website chat, messaging "help," clickable link in order emails.
- Guardrails: **provide incorrect information**, **reveal PII or address data to unauthenticated users** — named explicitly as failure modes to design against.

The PII/unauthenticated-disclosure guardrail is the same shape of risk this project already flagged for the CIN/biometria use case (no raw biometric data should transit the Slack text channel) — this framework gives a structured way to state that guardrail formally in a future design/requirements deliverable.

## Risks of Generative AI (named categories, useful for a compliance section)

- **Inaccuracy** — hallucination; in a sensitive/public-service context this "could result in denial of services/rights and physical harm" if depended on without a human check.
- **Bias & Toxicity** — offensive/unsafe content, bias against demographic groups.
- **Privacy & Security** — risk of revealing PII, or creating security risk; third-party models not always transparent about consented data.
- **Societal Impacts** — sustainability, economic, and societal disruption at scale.

## Guardrail-design method (People / Business / Technology / Data lens)

For each use case, cross a **Risk Area** (People/Business/Technology/Data) against a **Specific Concern**, then define a **Guardrail/Mitigation** and which layer owns it: "Some guardrails will be built into Agentforce to mitigate concerns, some will be configured in Agentforce and/or other Salesforce settings, and some will be outside of the technology" (e.g. process/organizational controls). This three-way split (product-native / configured / organizational) is a useful structure for a future requirements-phase guardrail table for the Poupatempo guichê agent.

## CoE / governance operating model (only if this project later needs an operating-model conversation)

Named roles: Executive Sponsor, CoE Owner, CoE Business Leads, CoE Architecture & Technical Leads, Product Manager, Data Admin — plus a 3-phase CoE rollout (Setup → Improve Efficiency → Scale & Enhance, 3/6/6+ months). Lower relevance to the Fase 1 pilot itself, higher relevance if the account later pursues a broader Agentforce CoE conversation with PRODESP (adjacent to, not part of, this SOW).

## Why this matters for this project, not for pricing

Purely a Salesforce PS methodology/framework reference — no PRODESP-specific content, no rate, no commercial figure. Use it to structure a future guardrail/compliance section in `requirements`/`design`, not as a source for scope or cost.
