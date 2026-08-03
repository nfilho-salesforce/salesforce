# Engagement Intent — DATAPREV-PAT

> Reference role: the *why* of the build. The phase briefs are how. When weighing a Plan-mode trade-off, weigh against this.
>
> If you need scoping context (current-state challenges, business impacts, confidence summary), see `93-scoping-context.md` (emitted only when scoping data is present).

## Intent

- **Outcome:** Tornar o PAT um mercado digital único, transparente e concorrencial — onde qualquer empresa brasileira, do MEI à grande corporação, cota, contrata e gere o benefício alimentação de seus trabalhadores em uma jornada 100% gov.br, com propostas comparáveis lado a lado, taxas dentro do novo teto regulatório (3,6%) e repasses garantidos em 15 dias. Operado pela Dataprev para o Ministério do Trabalho e Emprego, o marketplace substitui a negociação fragmentada e opaca de hoje por um leilão aberto entre facilitadoras, dando ao governo visibilidade sistêmica sobre bilhões de reais em benefícios e ao trabalhador a confiança de um programa moderno, auditável e interoperável.
- **Measured by:** _Arranque, Provisionamento & Arquitetura (17/ago – 30/ago · Sem. 1-2):_ Org dedicada greenfield provisionada e acessível; MuleSoft on-premise instalado e acessível na infra soberana; provedor do gateway selecionado/contratação iniciada com escopo de integração acordado; ADR 0001 ratificado com fronteira campo-a-campo definida; inventário de contratos de API por sistema (existe/não existe). MARCO DE PROJETO: kick-off e ambiente pronto ao fim da Sem. 2. · _Fundação — Modelo de Dados + Identidade + Integração + Residência (31/ago – 27/set · Sem. 3-6):_ MODELO DE DADOS FUNDACIONAL definido e ratificado com o time inteiro (objetos nativos Opportunity/Quote/Account + termo de aceite) — MARCO que libera a paralelização das demais frentes; camada API-led MuleSoft on-premise de pé com mocks (incluindo o contrato de integração com o gateway); modelo de referência tokenizada implementado e resolvendo em runtime na org greenfield dedicada; portal Partner Community com login gov.br funcional e Contact por referência tokenizada. Base pronta para o marketplace. · _Marketplace & Credenciamento — Frentes Paralelas (28/set – 18/out · Sem. 7-9):_ MARCO DE ENTREGA DE JORNADA (UAT): beneficiária publica a demanda (Opportunity), facilitadoras enviam Quotes via API (ocultas até o fechamento), tela 'Comparar Propostas' operante, seleção manual registra o vencedor; estabelecimentos se credenciam via gov.br PJ (CNPJ) com aprovação da facilitadora e checagem de vigilância sanitária. Capacidades principais: leilão reverso + credenciamento. · (+3 more — see the `10-phase-*` files)

## Engagement at a glance

DATAPREV-PAT

- **Clouds in scope:** Agentforce, Data Cloud, Experience Cloud, Marketing Cloud, MuleSoft, Sales Cloud
- **Phases planned:** 6
- **Target org:** `DATAPREV-PAT Greenfield` (scratch)
- **Build allowed:** yes

## Vision

Tornar o PAT um mercado digital único, transparente e concorrencial — onde qualquer empresa brasileira, do MEI à grande corporação, cota, contrata e gere o benefício alimentação de seus trabalhadores em uma jornada 100% gov.br, com propostas comparáveis lado a lado, taxas dentro do novo teto regulatório (3,6%) e repasses garantidos em 15 dias. Operado pela Dataprev para o Ministério do Trabalho e Emprego, o marketplace substitui a negociação fragmentada e opaca de hoje por um leilão aberto entre facilitadoras, dando ao governo visibilidade sistêmica sobre bilhões de reais em benefícios e ao trabalhador a confiança de um programa moderno, auditável e interoperável.

## Value drivers (how to break ties between approach A and B)

- **Jornada única gov.br para beneficiárias com comparação de propostas lado a lado** — Substitui negociação bilateral fragmentada por experiência transparente e padronizada.
- **Leilão automatizado entre facilitadoras** — Cotação → propostas → seleção substitui processo manual; reduz tempo e assimetria de informação.
- **Fluxo financeiro digital (folha, conta custódia, split) conforme repasse de 15 dias** — Upload de folha, geração de boleto/Pix, split governo/facilitadora automatizados.
- **Conformidade e auditabilidade da reforma** — Instrumento para o MTE fiscalizar teto de 3,6%, prazo de 15 dias e interoperabilidade; trilha LGPD/TCU.
- **Visibilidade sistêmica do programa para o MTE** — Base para monitoramento a posteriori de taxas, aceitação e irregularidades.

## Guiding principles

- **gov.br-first** — Identidade e procuração digital como porta única de acesso, aderente ao padrão do governo federal.
- **Dado sensível na origem** — Salesforce orquestra; a Dataprev persiste o dado sensível (CPF) — ADR 0001, residência híbrida.
- **Configurar antes de customizar** — Acelerar a entrega dentro de uma timeline agressiva (set→nov/2026) e reduzir custo de sustentação.
- **Mock-first nas integrações** — Desbloquear o desenvolvimento sem esperar Swagger/definição das APIs (Novo PAT, GOV.BR, eSocial), reduzindo risco de cronograma.
