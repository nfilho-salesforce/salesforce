# Resumo Executivo — PRODESP · Poupatempo Balcão (V3)

**Projeto:** PRODESP - Poupatempo Balcão V3 · **Data:** 2026-09-24 · **Conta:** Prodesp - Empresa de TI do Estado de São Paulo

---

## Visão Geral em 5 Pontos

- **Dor atual:** guichês do Poupatempo perdem capacidade quando um atendente fica ocioso e a fila viva está vazia — o agendamento futuro só é atendido na data marcada, mesmo com capacidade disponível antes disso.
- **Visão de transformação:** duas jornadas complementares — antecipação digital do atendimento agendado via WhatsApp para o cidadão, e apoio ao atendimento presencial via Slack para o atendente — condução do atendente 100% dentro do Slack, sem passar pela Service Console.
- **Principais motores de valor:** captura de capacidade hoje desperdiçada (Jornada 1), redução de bloqueios operacionais no balcão via apoio de conhecimento/IA (Jornada 2), e visibilidade executiva formal sobre o ganho real (observabilidade em Tableau Next).
- **Maior risco/incerteza:** estrutura comercial de Fixed Fee sobre um escopo em que 4 dos 7 épicos (E03, E04, E05, E07) ainda têm sizing classificado como Unknown — travado por gaps que só o cliente pode resolver.
- **Primeiro passo recomendado:** Fase 0 dedicada a fechar os gaps client-only antes de travar cronograma e equipe — o ponto de maior retorno por esforço neste momento.

---

## Visão Geral

O Poupatempo Balcão V3 propõe transformar dois momentos hoje manuais e subaproveitados do atendimento presencial: a capacidade ociosa de atendentes entre agendamentos, e a falta de um canal formal de apoio quando um atendente trava num procedimento no guichê. A solução amarra sete épicos em torno de duas jornadas apoiadas por Slack como interface principal do atendente — uma escolha arquitetural desta rodada de revisão, validada com o cliente via PoC, que substitui a Service Console como frontend da Jornada 1. Não há `strategy.json` neste projeto (a etapa de estratégia formal não foi executada), então este resumo sintetiza a narrativa diretamente do desenho de epics, gaps e roadmap, sem um caso de negócio formalmente redigido pelo cliente.

## Resumo do Escopo

Sete épicos, sizing T-shirt hoje com mix L/XL-dominante (4 L + 1 XL + 2 M):

| Épico | Escopo | Tamanho | Confiança |
|---|---|---|---|
| E01 — Antecipação de Atendimento Agendado | WhatsApp + gov.br, Presence Status/Routing nativos, atendente conduz 100% no Slack | L | Confirmed |
| E02 — Apoio ao Atendimento Presencial via Slack | Slackbot com escalonamento first-to-claim | M | Confirmed |
| E03 — Integração com Sistemas Legados | Dois sistemas distintos (CRM + ServiceDesk, nomes anonimizados), orquestração via MuleSoft, novo terceiro caminho de escrita para cancelamento de agendamento | L | **Unknown** |
| E04 — Serviço de Seleção de Antecipação | API de seleção que respeita o sistema externo de agendamento como fonte de verdade | M | **Unknown** |
| E05 — Autoprovisionamento de Atendentes | Integração com sistema de RH da PRODESP + criação do canal pessoal de Slack por atendente | XL | **Unknown** |
| E06 — Observabilidade e Analytics | Relatório executivo formal em Tableau Next com camada histórica/trend | L | Assumed |
| E07 — Base de Conhecimento e IA no Slackbot | Agentforce + Data 360, relação com o Agente do T7 ainda indefinida | L | **Unknown** |

## Destaques da Solução

Três decisões arquiteturais desta rodada moldam a entrega:

1. **Dois sistemas legados, não um** — o "Sistema de CRM legado" (jornada do cidadão) e o "Sistema de ServiceDesk legado" (jornada do atendente) são plataformas distintas, confirmadas pelo account owner. Se são dois deployments realmente separados ou o mesmo produto com dois alvos lógicos permanece aberto (`G0309`) e muda o dimensionamento de E03, não a lógica.
2. **Configuração nativa no lugar de automação customizada** — o gatilho da Jornada 1 é uma mudança de Presence Status do atendente no Omni-Channel, não um Flow customizado consultando fila vazia. Menos build, mais configuração.
3. **Atendente conduz 100% no Slack** — uma ponte Apex monitorando Platform Events, com base em um PoC já validado com o cliente, leva toda a interação do atendente para dentro do Slack (canal pessoal, thread por caso). O autoprovisionamento (E05) passa a incluir a criação desse canal, o que subiu seu sizing de L para XL.

O risco tecnicamente mais relevante embutido nessa arquitetura é o limite de Platform Events que rege a ponte Apex↔Slack: a premissa de design é um mecanismo trigger-based (Publishing Allocation, 250k/hora), mas se o mecanismo real precisar ser listener-based, vale a Delivery Allocation, bem mais restritiva (50k/24h) — se esse teto for atingido, novas antecipações não podem acontecer até o próximo ciclo.

## Abordagem de Implementação

Cinco fases, com caminho crítico **E05 → E01 → E06** (e, em paralelo, **E03 → E02 → E07**):

- **Fase 0 — Resolução de Gaps Críticos:** sem épicos; fecha G0309 (E03), G0501/G0508 (E05 — sistema de RH), G0703 (E07 — contrato Slackbot↔T7) e as regras de seleção de E04, hoje não especificadas pelo cliente. 57 gaps registrados (limiar de Fase 0 é >15) tornam esta fase necessária antes de travar o design em profundidade.
- **Fase 1 — Fundação:** E03 + E05 — integração com os dois legados e pipeline de provisionamento de atendentes, pré-requisito técnico de ambas as jornadas.
- **Fase 2 — Jornada 1 (Antecipação Digital):** E01 + E04, funcionalmente inseparáveis — o Presence Status de E01 dispara o serviço de seleção de E04 a cada oferta.
- **Fase 3 — Jornada 2 (Apoio Presencial + Conhecimento/IA):** E02 + E07 — o Slackbot de apoio ao atendente, depois a camada de conhecimento/IA que o alimenta.
- **Fase 4 — Observabilidade e Analytics:** E06, consumindo os dados instrumentados nas Fases 1-2.

Cronograma (faixa de duração, sem cronograma comprometido pelo cliente): **18-37 semanas** no lane Tradicional (piso benchmark, sem compressão por IA) e **15-34 semanas** no lane Aumentado — o lane de referência deste engajamento — comprimido pela banda de eficiência de prontidão Média (`efficiency.json`). Um terceiro lane, AI-native, projetaria 12-30 semanas, mas permanece condicional: o gate de qualificação (Product Owner do cliente nomeado e disponível em cadência diária) ainda não foi atendido — `C01` no roster do cliente está em aberto.

## Resumo de Esforço

O roster nomeado do lane Aumentado soma 10 papéis de Salesforce PS (~8,5 FTE nominal, com pico maior no meio da entrega) mais 3 papéis do lado do cliente. Dois sinais de disciplina merecem nome próprio, não só headcount:

- **Design de Experiência (R10, offshore, Fase 2)** — necessidade real de UX/acessibilidade para a jornada WhatsApp+gov.br do cidadão (E01). Sem esse trabalho formal, o risco é retrabalho na jornada digital depois que o cidadão já estiver interagindo com ela em produção.
- **Change & Adoption (R09, onshore, Fases 2-3)** — a maior barreira humana identificada no engajamento: dois públicos de atendentes precisam mudar de rotina (autodeclaração de ociosidade + migração do frontend de atendimento da Service Console para o Slack). Sem esse trabalho, o risco é de adoção — a solução pode funcionar tecnicamente e não ser usada como desenhada.

Do lado do cliente, dois papéis permanecem gaps abertos: **C01 (Product Owner/Decision-Maker)**, ainda sem nome — o mesmo gap que bloqueia a qualificação do lane AI-native — e **C02 (Acesso a Sistemas/IT do cliente)**, ainda não confirmado. Apenas **C03 (Testadores UAT/Atendentes)** está confirmado, com 2 pessoas disponíveis.

## Riscos e Mitigações

Classificação geral de risco: **Alta** (14 riscos registrados). O risco de maior peso estrutural:

- **R02 (Alto) — Fixed Fee sobre escopo com 4 épicos Unknown.** A combinação de uma estrutura comercial de preço fechado com um sizing ainda incerto em mais da metade do escopo é o risco dominante do engajamento. Não há mitigação de escopo disponível — apenas fechar os drivers que alargam a faixa (abaixo) ou negociar T&M para a Fase 0.
- **R04/R05 (client-only, caminho crítico)** — G0401 (regras de elegibilidade/prioridade/fallback de seleção de E04) e G0501/G0508 (sistema de RH não identificado, exposição de API não confirmada para E05) só o cliente resolve. Ambos bloqueiam sizing definitivo antes da Fase 1.
- **R14 (Médio) — limite de Platform Events na ponte Apex↔Slack**, detalhado acima nos Destaques da Solução — ainda não confirmado contra a implementação real do PoC.
- **R01 (Médio, residual não zero) — LGPD/gov.br/biometria.** Dado pessoal do cidadão trafegando por WhatsApp, autenticação de identidade via gov.br e biometria condicional, sem decisão de arquitetura de dados (residência, criptografia de campo) tomada. Recomendamos levar esta conversa à mesa comercial antes do fechamento do MVP, não deixá-la para o design detalhado.
- Riscos aceitos deliberadamente pelo cliente, sem mitigação ativa: sem sponsor nomeado para E06 (R09-risco, não confundir com o R09 do roster), governança de dados de RH em E05 (R10-risco), governança de conteúdo da base de conhecimento em E07 (R11-risco).

## Premissas e Nível de Confiança

Distribuição de confiança no projeto: **43% Confirmed / 29% Assumed / 29% Unknown** (14 itens avaliados) — um nível de confirmação baixo que justifica uma sessão de validação com o cliente antes de fechar o escopo definitivamente. Os 4 épicos Unknown carregam gaps concretos, não uma incerteza genérica:

- **E03** — G0309: 1 ou 2 deployments legados realmente separados?
- **E04** — G0401: regras de elegibilidade/prioridade/fallback de seleção ainda não definidas pelo cliente.
- **E05** — G0501/G0508: sistema de RH da PRODESP não identificado, exposição de API não confirmada.
- **E07** — G0703: contrato de integração Slackbot ↔ Agente do T7 indefinido.

57 gaps no total, acima do limiar de 15 que recomenda uma Fase 0 formal.

## Próximos Passos e Recomendações

1. **Nomear um Product Owner do cliente (C01)** com autoridade de decisão e cadência de disponibilidade definida — desbloqueia tanto a Fase 0 quanto (eventualmente) a qualificação do lane AI-native.
2. **Rodar a Fase 0 antes de travar cronograma e roster** — resolver G0309, G0401, G0501/G0508 e G0703 revalida os quatro sizes Unknown e estreita as faixas de duração acima.
3. **Levar a decisão de compliance/LGPD (R01) à conversa comercial** — residência de dados, criptografia de campo e o requisito de opt-out (WhatsApp) precisam de uma decisão explícita antes do fechamento do MVP, não durante o design detalhado.
4. **Confirmar o mecanismo real da ponte Apex↔Slack (trigger vs. listener) com o time de licenças** que já validou o PoC — resolve R14 antes que ele se torne um bloqueador em produção.

---

*Este resumo não contém valores de investimento. A faixa de precificação indicativa deste engajamento está em `outputs/artifacts/commercials.md`, sob validação de rates com o usuário.*
