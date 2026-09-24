# Plano de Entrega — PRODESP · Poupatempo Balcão (V3)

**Projeto:** PRODESP - Poupatempo Balcão V3 · **Data:** 2026-09-24 · **Conta:** Prodesp - Empresa de TI do Estado de São Paulo

---

**Duração do programa (benchmark):** 18–37 semanas, derivada de forma top-down a partir do formato do engagement (7 épicos, mix de tamanho agora L/XL-dominante — 4 L + 1 XL + 2 M, após o redimensionamento de E05 em 2026-09-24 — integrações com dois sistemas legados + sistema externo de agendamento, 6 clouds/produtos em escopo — Slack, Service Cloud, Agentforce, MuleSoft, Data 360, Tableau). Classificação: tabela Multi-Cloud + Integração de Dados, no limite entre Média (16–24 sem.) e Alta (26–40 sem.) — 7 épicos está perto do piso da faixa Média por contagem, mas o mix de tamanho pesa mais forte para o perfil da faixa Alta do que antes (a aparição de um XL, não só mais L's), o que subiu a baseline de 18–28 para 18–30 semanas. Ajuste de +15% por risco regulatório/compliance (LGPD, autenticação gov.br, biometria — não endereçado em nenhuma fonte de discovery) eleva o teto para ~35; o alargamento por mistura de confiança (4 de 7 épicos com confiança Unknown — E03, E04, E05, E07, inalterado) empurra o teto final a 37.

*Este figura é baseada em benchmark, derivada de padrões gerais de entrega e dos dados de treinamento do modelo de IA (não validado pela Salesforce) — não é um compromisso. Números finais são confirmados através do contrato comercial aplicável.*

**O que mais alargaria a faixa (resolver estes reduz a incerteza, não o esforço):**
- **E03** — G0309: os dois sistemas legados são deployments realmente separados ou o mesmo produto com dois alvos lógicos? Muda a contagem de Named Credentials/contratos de erro.
- **E05** — G0501/G0508: qual é o sistema de dados de funcionários da PRODESP e ele expõe API?
- **E07** — G0703: qual é o contrato de integração entre o Slackbot e o Agente do T7?

---

## Fase 0 — Resolução de Gaps Críticos de Discovery (posição 1 de 5)

Sem épicos — fase de resolução de gaps. 55 gaps registrados (limiar de Fase 0: >15) tornam esta fase necessária antes de travar o design em profundidade.

- **Objetivo:** resolver G0309, G0501/G0508, G0109 (comportamento WhatsApp/gov.br), G0703, G0111 (mecanismo real da ponte Apex/Platform Events↔Slack — trigger vs. listener) e as regras de seleção de E04, hoje não especificadas. G0509 (fronteira do canal Slack) já foi resolvido nesta rodada — E05 passa a incluir o provisionamento do canal.
- **Critério de sucesso:** gaps bloqueantes resolvidos ou formalmente aceitos como premissa; T-shirt sizes Unknown (E03/E04/E05/E07) revalidados.
- **Dependências:** nenhuma — ponto de partida.
- **Risco:** LGPD/compliance (dado pessoal via WhatsApp, biometria, autenticação de identidade) não endereçado em nenhuma fonte — precisa entrar na conversa comercial antes do fechamento do MVP.

## Fase 1 — Fundação: Integração de Legados + Autoprovisionamento (posição 2 de 5)

**Épicos:** E03 (Integração com Sistemas Legados), E05 (Autoprovisionamento de Atendentes)

- **Objetivo:** camada MuleSoft com os dois sistemas legados + pipeline de provisionamento de atendentes (User → Service Resource → Queue/Skill → Routing Configuration), agora incluindo a criação do canal pessoal de Slack por atendente (onboarding-time primário + exceção on-demand no roteamento, revertendo `G0509`) — pré-requisito técnico das duas jornadas.
- **Critério de sucesso:** Named Credentials/OAuth ativos e testados para os dois sistemas legados; atendente de teste provisionado ponta a ponta, com canal pessoal de Slack criado, e visível na fila.
- **Dependências:** nenhuma — fundação.
- **Risco:** G0309 aberto muda a contagem de conexões/contratos de erro de E03; G0501/G0508 pode bloquear E05 até resolução na Fase 0. Nova superfície de integração (Slack API) soma complexidade a E05, que subiu de L para XL — o fluxo de exceção on-demand no roteamento ainda não foi testado ponta a ponta.

## Fase 2 — Jornada 1: Antecipação Digital de Atendimento (posição 3 de 5)

**Épicos:** E01 (Antecipação de Atendimento Agendado), E04 (Serviço de Seleção de Antecipação)

- **Objetivo:** entregar a jornada WhatsApp+gov.br de antecipação junto com o serviço que decide qual agendamento ofertar — os dois épicos são funcionalmente inseparáveis (Presence Status de E01 dispara o serviço de E04 a cada oferta). Inclui a ponte Apex/Platform Events que leva 100% da interação do atendente para o Slack (canal pessoal, thread por caso — Service Console deixa de ser o frontend desta jornada) e o cancelamento automático do agendamento presencial (via E03) quando a resolução remota é 100% bem-sucedida.
- **Critério de sucesso:** fluxo ponta a ponta — ociosidade declarada → Presence Status → Routing Configuration → seleção → oferta WhatsApp → autenticação gov.br → Case roteado → atendente conduz 100% no Slack via a ponte Apex/Platform Events (PoC já validado com o cliente) → agendamento presencial cancelado automaticamente se a resolução remota for completa.
- **Dependências:** depende de E03, E05 (Fase 1) — protocolo do CRM legado, canal pessoal de Slack do atendente e atendente já provisionado na fila.
- **Risco:** R-07 (fila raramente vazia) — a antecipação pode nunca se realizar na frequência esperada; tensão contador customizado vs. métrica nativa de Idle/%Idle ainda não resolvida. G0111/R14 — limite de Platform Events que rege a ponte Apex↔Slack ainda não confirmado como trigger-based (Publishing Allocation, 250k/hora) vs. listener-based (Delivery Allocation, mais restritiva); se atingido, novas antecipações não podem acontecer.

## Fase 3 — Jornada 2: Apoio Presencial + Base de Conhecimento/IA (posição 4 de 5)

**Épicos:** E02 (Apoio ao Atendimento Presencial via Slack), E07 (Base de Conhecimento e Apoio de IA no Slackbot)

- **Objetivo:** Slackbot de apoio ao atendente de guichê, depois a camada de conhecimento/IA que o alimenta (Agentforce + Data 360) — E07 constrói sobre a infraestrutura de canal que E02 entrega.
- **Critério de sucesso:** Slackbot em produção com escalonamento first-to-claim; Agentforce resumindo histórico pós-go-live (zero-lookback aceito) com guardrail de confiança mínima + citação + confirmação do atendente.
- **Dependências:** depende de E03 (Fase 1).
- **Risco:** G0703 (contrato Slackbot↔T7 indefinido); governança de conteúdo da base de conhecimento fora do escopo formal — risco de degradação silenciosa pós-go-live, registrado e não mitigado.

## Fase 4 — Observabilidade e Analytics (Tableau Next) (posição 5 de 5)

**Épicos:** E06 (Observabilidade e Analytics)

- **Objetivo:** instrumentar e publicar o relatório executivo em Tableau Next, consumindo os dados de causa/frequência e ociosidade instrumentados na Fase 2.
- **Critério de sucesso:** relatório executivo publicado com camada histórica/trend e cadência de atualização recorrente.
- **Dependências:** depende de E01, E05 (Fases 1–2).
- **Risco:** sem sponsor/decisão nomeado para E06 (sinalizado, não mitigado); mesma tensão contador-customizado-vs-métrica-nativa de E01.

---

## Caminho crítico

**E05 → E01 → E06** (e, em paralelo, **E03 → E02 → E07**) — estas cadeias governam o cronograma; atraso em qualquer um dos elos se propaga adiante. E03 também é pré-requisito direto de E01 (protocolo do CRM legado, bloqueante por RN-13).

## Riscos consolidados

| Risco | Fase(s) afetada(s) | Nota |
|---|---|---|
| LGPD/compliance não endereçada | Fase 0, transversal | Dado pessoal via WhatsApp, biometria, autenticação gov.br — sem decisão de residência/criptografia tomada. |
| G0309 — 1 vs 2 sistemas legados | Fase 1, 2, 3 | Muda dimensionamento de E03 (contagem de conexões/contratos de erro). |
| R-07 — fila raramente vazia | Fase 2 | Antecipação pode nunca se realizar na frequência esperada; medir antes de dimensionar o ganho. |
| Contador customizado vs. métrica nativa | Fase 2, 4 | Pode reduzir esforço de build de E01/E06 se a métrica nativa do Command Center bastar. |
| G0703 — contrato Slackbot↔T7 indefinido | Fase 3 | RN-22 é nosso posicionamento, não resposta fechada do cliente. |
| G0111/R14 — limite de Platform Events na ponte Apex↔Slack | Fase 2 | Trigger-based (Publishing, 250k/hora) é a premissa de design; se listener-based, vale a Delivery Allocation (50k/24h) — se atingida, novas antecipações não podem acontecer. |
| E05 subiu de L para XL (revisão do G0509) | Fase 1 | Provisionamento do canal Slack por atendente entrou no épico — segunda superfície de integração real, soma-se à incerteza do sistema de RH. |
| Sem sponsor nomeado para E06 | Fase 4 | Sinalizado, não mitigado — decisão do cliente. |

---

As disciplinas e o roster nomeado para entregar este plano — com contagens defensáveis, por fase — vêm do `estimate`.
