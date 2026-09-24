# Risk Review — PRODESP · Poupatempo Balcão (V3)

**Projeto:** PRODESP - Poupatempo Balcão V3 · **Data:** 2026-09-24 · **Conta:** Prodesp - Empresa de TI do Estado de São Paulo
**Estrutura comercial:** Fixed Fee · **Escopo avaliado:** as 7 épicas atuais (E01-E07), MVP das duas jornadas BPMN + autoprovisionamento + observabilidade Tableau — não um programa maior que este MVP possa abrir caminho para.

*Este documento é preparação interna para o gate de revisão de risco (SDS/DealStrat/GSRM). Recomenda, não decide — o compromisso final é do revisor humano.*

---

## Overall Risk Rating

| | Rating | Racional (resumo) |
|---|---|---|
| **Recomendado (Scopezilla)** | **High** | Riscos técnicos bem mitigados por desenho (guardrail de alucinação do Agentforce, premissa de integração Slackbot↔T7). O que pesa é a combinação: Fixed Fee contra uma faixa de 18-34 semanas ainda não travada + dois gaps client-only pesados (R04, R05) no caminho crítico ou colado a ele, com só uma expectativa — não um compromisso contratual — de resposta na Fase 0 + velocidade de governança da PRODESP genuinamente desconhecida (sem base V1/V2). |
| **Counter-case independente** | Not Recommended | Especificamente contra travar o preço Fixed Fee **hoje**, antes da Fase 0 resolver o caminho crítico (E05, primeiro nó, é Unknown; E03 é Unknown e bloqueia E01 por RN-13; E04 — funcionalmente inseparável de E01 — tem sua lógica de seleção ainda inexistente). Fato que mais reduziria essa leitura: um gate de Fase 0 **com dentes contratuais** (preço/escopo travado só após G0401/G0501/G0508/G0309/G0509 resolverem com aceite do cliente e prazo definido). |
| **Comprometido (usuário)** | **High** | Usuário optou pela recomendação do Scopezilla sobre a leitura mais cautelosa do counter-case — ver nota abaixo. |

**Nota sobre o counter-case:** por desenho deste processo, o counter-case é gerado por um agente independente, seedado só com a evidência (não com a leitura do Scopezilla), para argumentar a favor do polo mais cauteloso possível. Ele não é adotado automaticamente — fica registrado aqui para que o revisor veja a leitura mais dura ao lado da recomendação, não só o resultado comprometido.

---

## Register de Riscos

Ordenado por categoria RBS, mais pesado primeiro dentro de cada categoria.

### F — Customer & Governance

| ID | Risco | Nível | Residual | Mitigação | Owner | Status |
|---|---|---|---|---|---|---|
| R03 | Governança/velocidade de decisão da PRODESP — unknown genuíno, sem base V1/V2 | **High** | High | Check-in de cadência de governança na Fase 0 antes de comprometer cronograma Fixed Fee | PS + sponsor cliente | open |
| R01 | LGPD/gov.br/biometria (fluxo E01) — framework maduro do cliente citado, mas aplicação a este fluxo não confirmada | Medium *(recomendado High → Medium após confirmação do usuário)* | Medium | Confirmação por escrito de jurídico/DPO sobre o fluxo específico, antes da Fase 2 (novo gap G0110) | customer (jurídico/DPO) | open |
| R09 | Sem sponsor nomeado para E06 (terminal do caminho crítico) | Medium | Medium *(deliberadamente não mitigado)* | Nenhuma — decisão do usuário de manter no escopo, risco sinalizado | customer | open |
| R10 | Governança LGPD de dados de funcionário (E05) deliberadamente fora do escopo | Medium | Medium *(deliberadamente não mitigado)* | Nenhuma — decisão consciente do usuário | customer (jurídico/DPO) | open-deferred-by-user |
| R11 | Sem dono de conteúdo da base de conhecimento por especialidade (E07) — degradação silenciosa pós-go-live | Medium | Medium *(deliberadamente não mitigado)* | Nenhuma — decisão consciente do usuário | customer | open-deferred-by-user |

### E — Financials & Contract

| ID | Risco | Nível | Residual | Mitigação | Owner | Status |
|---|---|---|---|---|---|---|
| R02 | Fixed Fee contra faixa de 18-34 sem. não travada, com 4/7 épicas Unknown | **High** | High | Nenhuma mitigação de escopo — alavancas comerciais: apertar a faixa antes de assinar, ou T&M/híbrido na Fase 0 | PS deal team | open |

### C — Scope

| ID | Risco | Nível bruto | Residual | Mitigação | Owner | Status |
|---|---|---|---|---|---|---|
| R04 | G0501/G0508 — sistema de RH de E05 não identificado, no caminho crítico | High | **Medium** | Fase 0 como gate — expectativa (não compromisso contratual) de resposta | customer (TI/RH) | open |
| R05 | G0401 — regras de seleção de E04 indefinidas, acoplado 1:1 a E01 | High | **Medium** | Fase 0 como gate — mesma ressalva de falta de dentes contratuais | customer | open |
| R07 | G0309 — 1 vs 2 deployments legados indecidido (E03) | Medium | Medium | Confirmar com TI do cliente na Fase 0/1 | customer (TI) | open |
| R08 | G0304 — mapeamento de campo do sistema legado não pode ser assumido | Medium | Medium | Levantar com TI do cliente no build da Fase 1 | customer (TI) | open-client-only |
| R13 | G0509 — fronteira de provisionamento do canal Slack, risco de scope-creep | Low | Low | Tratar como processo separado do cliente | customer | open |

### A — Technology & Product

| ID | Risco | Nível | Residual | Mitigação | Owner | Status |
|---|---|---|---|---|---|---|
| R06 | G0703 — contrato Slackbot↔Agente T7 é premissa provisória, não confirmada | Medium | Medium | Premissa arquitetural já desenhada; L-34 segue como pergunta formal | customer + PS | open-with-provisional-premise |
| R12 | G0702 — alucinação do Agentforce em contexto de serviço público | Medium (bruto) | **Low** | Guardrail já desenhado: confiança mínima + citação + confirmação do atendente | PS (aplicado) | resolved |

### D — Staffing

**Não avaliada.** `data/resource-plan.json` ainda não existe — a skill `estimate` não rodou. Revisitar esta categoria quando o roster nomeado existir; não força-se um rating sobre um roster inexistente.

---

## Guia de Facilitação — perguntas para a call de revisão

1. **Fixed Fee vs. caminho crítico não travado (R02, R04, R05).** O comercial está disposto a travar Fixed Fee hoje, ou o gate de Fase 0 deveria ganhar dentes contratuais (prazo + direito de repreço) antes da assinatura?
2. **Governança/velocidade de decisão (R03).** Existe algum canal informal com quem trabalhou em V1/V2 que possa dar uma leitura, mesmo que não documentada?
3. **LGPD do fluxo E01 (R01, G0110).** Quem no lado PRODESP é o contato de jurídico/DPO para confirmar a revisão deste fluxo específico?
4. **E06 sem sponsor (R09).** Isso é aceitável para seguir para contrato, ou deveria ser uma condição de entrada na Fase 0?
5. **Os dois itens deliberadamente deferidos (R10, R11).** Confirmar que o cliente entende que ficam como risco registrado, não como obrigação contratual nossa — vale uma linha explícita no SOW/contrato?

---

## Itens Abertos (sem mitigação de escopo, só comercial/contratual)

- R02 — Fixed Fee vs. faixa de 18-34 semanas não travada.
- R03 — governança/velocidade de decisão da PRODESP, unknown genuíno.
- R04/R05 — residual Medium depende do gate de Fase 0 ganhar dentes contratuais; hoje é só expectativa.
- Categoria D (Staffing) — não avaliada, sem `resource-plan.json`.

---

*Preparação interna para o gate de revisão de risco — o gate continua sendo do revisor humano. Este documento não substitui a conversa, ele a direciona.*
