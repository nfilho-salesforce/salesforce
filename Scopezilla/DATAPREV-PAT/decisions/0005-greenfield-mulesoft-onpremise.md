# 0005 — Ambiente 100% greenfield e MuleSoft on-premise para isolamento e soberania de dados

**Date:** 2026-07-31 · **Status:** accepted · **Source:** scopezilla-recommended

## Context
O programa lida com dado previdenciário e financeiro sensível sob LGPD Art. 11 e escrutínio de TCU/CGU/ANPD, numa instância Salesforce dedicada e apartada (`decisions/0002`). A decisão de hospedagem do MuleSoft estava em aberto (G0504 — CloudHub vs. Runtime Fabric). Premissa assumida pela equipe (31/jul/2026): **ambiente 100% greenfield — nenhuma ORG existente é reaproveitada, inclusive para o MuleSoft, cuja premissa é instalação on-premise, com infraestrutura pronta nos marcos do projeto.** O objetivo é **isolar este ambiente de qualquer outro da Dataprev e de possíveis administradores** que teriam acesso a essas informações; o **MuleSoft on-premise cumpre as exigências de soberania de dados**.

## Decision
- **Greenfield total**: a instância Salesforce dedicada (`decisions/0002`) é provisionada do zero; nenhuma org, metadado ou administração compartilhada com outros ambientes Dataprev. Isolamento por construção, não por configuração.
- **MuleSoft on-premise** (resolve G0504): a camada de integração roda **na infraestrutura da Dataprev/gov**, não em CloudHub. É o ponto de de-tokenização do CPF (`decisions/0001`) e o trilho de soberania — o dado sensível não sai do perímetro soberano.
- **Infraestrutura como pré-requisito de marco**: a prontidão da infra (org dedicada provisionada, MuleSoft on-premise instalado e acessível) é **premissa de arranque** — precisa estar pronta nos marcos do projeto, senão o cronograma escorrega. Entra na Fase 0 com lead-time externo, ao lado do provisionamento da org e da contratação do gateway PCI.

## Consequences
- **E08 reforçado**: greenfield + MuleSoft on-premise passam a ser a materialização concreta da soberania de dados e do isolamento — não só tokenização (`decisions/0001`) e instância dedicada (`decisions/0002`), mas o **trilho de integração dentro do perímetro soberano**.
- **E05 re-shapeado**: MuleSoft deixa de ter hospedagem em aberto — é **on-premise**; isso muda o modelo operacional (deploy, observabilidade, escalonamento sob responsabilidade da infra Dataprev) e adiciona **dependência dura de infra pronta nos marcos** (risco de cronograma).
- **Fecha G0504** (hospedagem MuleSoft) como decidido: on-premise. A de-tokenização do CPF ocorre no perímetro soberano.
- **Fase 0 ganha um terceiro pré-requisito de lead-time externo**: prontidão da infraestrutura (org + MuleSoft on-premise), somada ao provisionamento da org dedicada e à contratação do gateway PCI. É o maior risco à data fixa.
- Reverter (usar CloudHub ou reaproveitar org/admin existente) quebraria o argumento de soberania/isolamento e re-shapearia E05/E08 — daí ser premissa.

## Grounds
Premissa assumida pela equipe Salesforce em 31/jul/2026 (ditada pelo Solution Manager), **a validar com o cliente e a arquitetura Dataprev**. Amplifica e concretiza [[0001-residencia-dados-hibrida]] (soberania — dado sensível não sai do perímetro) e [[0002-instancia-dedicada-mte-pat]] (isolamento — nenhum admin de outro ambiente enxerga estes dados). Resolve o gap G0504. `scopezilla-recommended`, marcada Assumed até ratificação.
