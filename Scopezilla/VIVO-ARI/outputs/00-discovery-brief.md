# ARI Vivo — Discovery Brief

> Documento-espinha da fase de discovery. O que ouvimos + o que segue aberto. Fonte primária:
> `discovery-notes/vivo-b2c-atendimento-estimation-design.md` (ROM 2026-07-23). Números do ROM são
> **esforço de build/engenharia** — este projeto os estende ao ciclo completo da metodologia PS.

## Resumo executivo

A Vivo (Telefônica Brasil) vai reconstruir sua **camada de atendimento B2C** nativamente em
Salesforce — hoje os atendentes operam sistemas legados (WDE, GPS, Next, Siebel) via Alt+Tab /
iframe mal-integrado. Já existe um ROM técnico detalhado (199 histórias, 10 domínios, build de 27
pessoas em 5 squads, caminho crítico 3,7–9,2 meses) que dimensiona **apenas a engenharia e
arquitetura de delivery**. O objetivo do ARI Vivo é revalidar esse ROM e produzir um **plano de
projeto e estimativa completos**, cobrindo **todas as fases da metodologia Salesforce PS** — com o
desdobramento completo de **perfis e horas** que o ROM propositalmente deixa de fora.

## Contexto de empresa e indústria

- **Cliente:** Vivo / Telefônica Brasil — operadora tier-1, segmento B2C.
- **Regulatório:** Anatel, LGPD, fim de concessão STFC (cobre→fibra), descomissionamento DTH→IPTV —
  fluxos regulados de atendimento em estilo entrevista de 300+ passos (contestação de fatura,
  negociação de dívida, migrações mandatórias).
- **Estado atual:** não há atendimento em Salesforce; malha legada frágil, ~2,3M callouts/dia útil
  (Splunk), ~22% respostas não-2xx.

## Landscape Salesforce — atual vs. alvo

- **Atual:** sem Salesforce na camada de atendimento; CRM/telefonia/diagnóstico em legado.
- **Alvo:** Salesforce Core (LWC + Apex, **OmniStudio descartado**) + **Agentforce** (superfície
  agentic + Active Retention Agent) + **Data 360** (federação de 7 famílias de dado de cliente) +
  **Service Cloud Voice / Amazon Connect** + **Digital Engagement** (WhatsApp/chat/email) +
  **Experience Cloud** (canal Parceiro/Aliado, ~18k) + **MuleSoft** (cirúrgico, facades pré-existentes).

## Escopo e objetivos do projeto

**Escopo funcional (do ROM):** 4 capacidades eTOM Customer — Customer Interaction, Customer
Problem, Customer Relationship (V360), Customer Order Processing (envelope) — **mais Product Order
Capture** (eligibility→serviceability→reservation→configuration→submission por família × operação).
Gestão de product-order, catálogo, CPQ, pricing e provisionamento são **delegados** ao Pillar 2 via
MCP (fora de escopo).

**Objetivo do ARI Vivo (diretriz do scoper):** revalidar o ROM e entregar um **plano de projeto PS
completo** com estimativa de **perfis × fases × horas**, estendendo o ROM (build-only) às fases que
ele exclui. Ver `decisions/0001`.

### Modelo de fases (a confirmar — ver Open Questions)
- **P&D (Prepare & Design):** refinamento de histórias + mobilização de sprint (Sprint 0). Premissa:
  épicos e plano técnico **já existem** — não é discovery greenfield.
- **Build / Delivery:** herdado do ROM (revalidar, não re-derivar).
- **SIT → UAT → Deploy → Scale/Hypercare:** fases novas, ausentes do ROM.
- **Governança:** PM, Scrum Master, Agile Coach, Delivery Manager — excluídos pelo ROM, incluídos aqui.

## Dados e considerações de compliance

- **Migração de dados:** modelo é **federação Data 360** (dado permanece na origem), não carga bulk;
  dados mínimos residentes em Salesforce. Risco de latência de atendimento sub-segundo por voz/chat.
- **Compliance:** LGPD (consentimento, DSR), Anatel (Ouvidoria, reconsideração), retenção legal.

## Riscos e dependências herdados do ROM

1. Jornadas de maior dor (Problem/Technical/Termination) declaradas mas não modeladas → buffer 50% CPM.
2. Fluxos determinísticos guiados construídos nativamente (não invocáveis) → incerteza de esforço, buffer 50% CPM.
3. Malha de integração de origem (volume + fragilidade) → buffer 50% INT; 36 clientes Core a reconstruir com error-handling resiliente.
4. Federação Data 360 vs. latência de atendimento — validar cedo.
5. Contrato de fronteira product-order (MCP com Pillar 2) → buffer 50% PROCP.
6–11. Qualidade de dados de fluxos-fonte; escala do canal Aliado (sub-decomposto); pré-requisito
   Voz/Amazon Connect (Genesys EOL Dez-2027); pico de migração mandatória regulatória; Product Design
   fora de escopo; reconciliações de refinamento marginais.

## Open Questions

Itens que decidem a estimativa completa e precisam de confirmação antes de gerar números por fase:

1. **Modelo de fases PS** — confirmar a lista canônica (Prepare & Design · Build · SIT · UAT · Deploy ·
   Scale/Hypercare) e se seguimos o Salesforce PS Delivery Framework. *(Por que importa: define as
   colunas do plano e da estimativa.)*
2. **Fatores de loading por fase** — P&D, SIT/UAT, Deploy, Scale como % do esforço de build (ou
   role-loading por duração). Precisamos das premissas para não inventar horas. *(Por que importa:
   determina as horas das fases não-build.)*
3. **Governança/PM em escopo** — incluir PM/SM/Agile Coach/Delivery Manager na estimativa completa?
   *(Assumido: sim.)*
4. **Base de horas** — build em horas **produtivas** (~19,6k central) ou **contratadas** (÷0,75 / ÷0,70)?
   A estimativa PS que mapeia a rates costuma usar contratadas. *(Por que importa: muda a base de todas as horas.)*
5. **Tradicional vs. AI-native** — a velocidade do ROM é **nominal (tradicional)**. Aplicar compressão
   AI-native (como em projetos anteriores) ou manter tradicional? *(Por que importa: maior alavanca de horas.)*
6. **Cenário de referência** — otimista / central / pessimista como âncora do plano. *(Assumido: central.)*
7. **Contagem de usuários internos** — nº de atendentes/agentes não consta (só ~18k canal externo).
   *(Por que importa: dimensiona UAT, treinamento, adoção, Scale.)*
