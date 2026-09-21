# Data 360 Headless: Built for the "Agent Persona"
Source: STAAR — 5.1 - Data (Data Cloud) / 5.1.5. Data 360 + Informatica + MuleSoft
File: Data 360 Headless - R Loganathan 2026.03.30.pdf (partial extract: slides 1–8 of a longer deck; the rest is a live demo walkthrough, lower relevance for this project)
Relevance: This project's Fase 1 tactical design already uses Data 360 as the Agentforce-in-Slack context lookup (cadastro/histórico da cidadã), and the Fase 2+ vision leans on Data 360 as part of the Headless platform. This deck is the concrete "how" behind that pattern — Data 360 designed to be operated by an agent inside Slack, not by a human through a UI.

## The problem this addresses

"Data 360 is powerful & too hard to use" — provisioning/setup takes minutes, but configuration and onboarding take weeks; requires specialized expertise (CI, segments, identity, schema); too many steps across disconnected workflows; value is delayed, so adoption suffers. Headless Data 360 exists to move that complexity into the system/AI layer instead of the (human) user.

## What "Headless Data 360" means concretely

- **No UI required for most workflows** — operated through natural language + agents, embedded in daily tools.
- **Embedded anywhere**: Slack, Claude, SFDC Apps named explicitly as the surfaces.
- **"Users don't 'use Data 360'" — Data 360 works through everything else; complexity moves to AI.**

## Architecture pattern: "Agent Persona" over Data 360

Two families of UI sit on top of the same headless Data 360 core:
- **Conversational interfaces** (GPT interfaces, Claude, **Slack/Slackbot**, Agentforce) → produce a custom/liquid UI/UX.
- **Clicks-and-navigation interface** → produces the opinionated, classic UI/UX.

Both paths call into a shared "Headless for 'Agent Persona'" layer, which in turn sits on Data 360. This is the same "agent operates the platform, human directs" pattern as `staar-headless-360-doctrine.md`, applied specifically to the data layer.

## Roadmap framing ("The road to #1 Agentic CRM")

Named first pillar: **"Slack-first, MCP-powered conversations: from plan → implement → monitor → evolve, across Slack, Claude, etc."** — i.e. Salesforce's own internal roadmap treats Slack as the primary conversational surface for agent-driven data operations, which directly supports (and de-risks, from a platform-roadmap perspective) the Poupatempo Fase 1 bet of putting the attendant's Agentforce interaction inside Slack rather than a custom UI.

## Why this matters for scoping, not for pricing

This deck describes a Salesforce-side platform capability and roadmap, not a PRODESP-specific commitment or a rate. It supports the technical feasibility of "Agentforce reads Data 360 context from inside a Slack channel" (IF-03 in `.discovery-context.md`'s architecture section) as an already-supported pattern rather than a bespoke build — useful for a design/requirements conversation, not a source for any dollar figure.
