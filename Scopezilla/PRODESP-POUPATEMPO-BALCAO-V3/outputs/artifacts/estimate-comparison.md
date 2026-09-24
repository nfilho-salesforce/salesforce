# Estimativa Comparativa — PRODESP · Poupatempo Balcão (V3)

**Projeto:** PRODESP - Poupatempo Balcão V3 · **Data:** 2026-09-24 · **Estimativa: pricing deferido** (nenhuma taxa validada no dossiê — a estimativa de prazo + esforço + roster é o entregável completo hoje)

---

## Anchor: Aumentada

O lane **Aumentada** é o comprometido/real para este engagement — metodologia tradicional + tooling de IA, mesma equipe, ritmo mais rápido. **Tradicional** fica como piso contextual de comparação ("o que custaria sem tooling de IA"), não um valor derivado por gross-up. **AI-native** é um upside condicional — mostrado como motivador, não como número comprometido, porque o gate de qualificação (product owner do cliente nomeado e empoderado) ainda não foi atendido.

*Este figura é baseada em benchmark, derivada de padrões gerais de entrega e dos dados de treinamento do modelo de IA (não validado pela Salesforce) — não é um compromisso. Números finais são confirmados através do contrato comercial aplicável.*

## Comparação das 3 Lanes

| | Tradicional (contextual) | **Aumentada (ANCHOR)** | AI-native (condicional) |
|---|---|---|---|
| Duração | 18-37 semanas | **15-34 semanas** | 12-30 semanas |
| Compressão | — (piso, sem compressão) | ~8-18% (realized_band, cenário Mid) | ~20-32% (native_band, gated) |
| Equipe (nominal/peak FTE) | ~8,5 FTE | **~8,5 FTE** | ~4,25 FTE |
| Composição | 10 papéis PS | 10 papéis PS (mesma equipe) | 7 papéis (piso de 4 contas núcleo + 3 fracionais) |
| Qualificação | — | — | **Condicional — gate não atendido** |
| Preço indicativo | pricing deferido | pricing deferido | pricing deferido |

**Delta**: Aumentada comprime o piso tradicional de 18-37 para 15-34 semanas via tooling de IA, mesma equipe. AI-native comprimiria a 12-30 semanas com um núcleo ~2× mais magro — mas depende de um product owner do cliente nomeado e empoderado, hoje um gap confirmado, não um gate atendido.

## Lane: Tradicional (contextual, não é o anchor)

**Duração**: 18-37 semanas — benchmark top-down do formato do engagement (7 épicos, mix L/XL-dominante, 2 integrações legadas + ponte Apex/Platform Events, 6 clouds/produtos), sem compressão.

**Equipe (~8,5 FTE nominal/peak)**:
| Papel | Senioridade | Local | Fases | Alocação | Por quê |
|---|---|---|---|---|---|
| Project/Program Manager | Regular | Onshore | 0-4 | Full | Fio condutor client-facing; dois caminhos críticos em paralelo |
| Solution Architect | Senior | Onshore | 0-4 | Half | Owns o quê através de 6 clouds; dono da tradução LGPD |
| Technical Architect | Senior | Onshore | 0-3 | Full | Integração acoplada por timezone (E03, ponte Apex/Platform Events) |
| Developer (integração) | Senior | Offshore | 1-2 | Full | MuleSoft + classe Apex — maior risco técnico |
| Developer | Regular | Offshore | 1-2 | Full | E05 (autoprovisionamento + canal Slack) + config E01 |
| Developer (Slack/Agentforce) | Regular | Offshore | 3 | Full | Slackbot E02 + base de conhecimento/Data 360 E07 |
| Quality Assurance | Regular | Offshore | 1-4 | Half (Full na Fase 2) | Surge na Fase 2 — fluxo citizen-facing + limite Platform Events |
| Functional Consultant | Regular | Offshore | 0-3 | Full | Fecha regras de E04 e contrato Slackbot↔T7 de E07 |
| Change & Adoption | Regular | Onshore | 2-3 | Quarter | Maior barreira só-humana — migração do atendente para Slack |
| Experience Design | Regular | Offshore | 2 | Quarter | UX/acessibilidade da jornada WhatsApp+gov.br |

## Lane: Aumentada (ANCHOR — comprometido)

**Duração**: 15-34 semanas — baseline tradicional comprimido pelo `realized_band` do cenário Mid readiness (`efficiency.json`, ~8-18%): `18×(1-0,18)=15`, `37×(1-0,08)=34`.

**Equipe**: idêntica à do lane Tradicional (mesma tabela acima) — o tooling de IA acelera o ritmo dentro do mesmo formato de time; **não** reduz headcount nem é um input de preço (per `efficiency.json`). Este é o roster gravado em `data/resource-plan.json` como o comprometido.

## Lane: AI-native (condicional — upside, não comprometido)

**Duração**: 12-30 semanas — baseline tradicional comprimido pelo `native_band` (`efficiency.json`, ~20-32%, gated + provisório): `18×(1-0,32)=12`, `37×(1-0,20)=30`.

**Qualificação**: **Condicional** — o gate exige um product owner do cliente nomeado e empoderado, cadência de decisão rápida e mandato AI-first. Nesta sessão (2026-09-24), o usuário confirmou que **não há PO nomeado ainda** — o gate segue não atendido. *"Se a PRODESP se comprometer a esse jeito de trabalhar, é isto que custaria"* — motivador, nunca apresentado como alcançável sem nomear o compromisso.

**Equipe (~4,25 FTE nominal/peak — piso de responsabilidade contínua + cauda fracionária)**:
| Papel (rótulo AI-native) | Senioridade | Local | Fases | Alocação | Por quê |
|---|---|---|---|---|---|
| Program Lead (PM) | Senior | Onshore | 0-4 | Full | Relacionamento com o cliente, decisões de gate, o plano |
| Intent Architect (SA) | Senior | Onshore | 0-4 | Full | Owns o intent/guardrails nos domínios ambíguos (G0309, G0501/G0508, G0703, E04) |
| Agent Orchestrator (TA) | Senior | Onshore | 1-3 | Full | Dirige a frota de agentes; retém build humano na integração de maior risco |
| Adoption Architect | Regular | Onshore | 2-3 | Half | Presente — adoção é escopo real e nomeado (mudança Service Console→Slack) |
| Quality Assurance (amplificado) | Regular | Offshore | 1-4 | Quarter (Full na Fase 2) | Amplificado, nunca substituído — surge na Fase 2 |
| Experience Design (fracional) | Regular | Offshore | 2 | Quarter | UX/acessibilidade da jornada cidadã |
| Developer (Data 360/Agentforce, fracional) | Senior | Offshore | 3 | Quarter | Domínio distinto não coberto pelo piso — schema Data 360 + retrieval de E07 |

**Provisório**: banda AI-native (~20-32%, já abaixo do típico ~35-40% pela carga de legado/compliance deste projeto) não calibrada — magnitude reportada por fornecedor, diagnóstico fundamentado em DORA/METR.

## Cobertura Client-Side (aplica-se aos 3 lanes)

A necessidade de cobertura do cliente não muda por modelo de entrega — vive uma única vez em `data/resource-plan.json`:

| Papel | Status | Nota |
|---|---|---|
| Product Owner / Decision-Maker | 🔴 **Gap confirmado** (2026-09-24) | Não nomeado — bloqueia G0309/G0501/G0508/G0703 e o sponsor ausente de E06; é também o sinal-chave do gate de qualificação AI-native |
| Client IT / Systems Access | 🔴 **Gap confirmado** (2026-09-24) | Acesso/credenciais não confirmados para os 2 legados + sistema externo de agendamento — bloqueia Named Credentials/OAuth de E03 |
| UAT / Atendente Testers | 🟢 **Confirmado disponível** (2026-09-24) | Cobertura das duas jornadas (E01/E04 e E02/E07) |

## Disclaimer

*Este figura é baseada em benchmark, derivada de padrões gerais de entrega e dos dados de treinamento do modelo de IA (não validado pela Salesforce) — não é um compromisso. Números finais são confirmados através do contrato comercial aplicável.* Bandas de eficiência são qualitativas e específicas deste projeto (`efficiency.json`); nenhuma implicação de horas, FTE ou custo é computada a partir delas além da compressão de duração já mostrada acima. Pricing indicativo requer uma taxa validada pelo usuário via `commercials` — hoje deferido.

## Como Usar Isto

- **Sign-off do SSSL**: aprovado nesta sessão (2026-09-24) — roster e as 3 durações.
- Quando houver taxa de bill rate validada, rodar `commercials` por lane para camada de preço indicativo sobre esta base de prazo/esforço/roster já pronta.
- Re-rodar `efficiency` para subir de fidelidade `category-only` → `category+role` agora que `data/resource-plan.json` existe.
- O gate de qualificação AI-native muda no momento em que um product owner do cliente for nomeado e empoderado — revisitar a coluna condicional quando esse gap fechar.
