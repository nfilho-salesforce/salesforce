# 0006 — MuleSoft reusa a instalação on-premise existente (não é mais greenfield)

**Date:** 2026-08-03 · **Status:** accepted · **Source:** scopezilla-recommended

## Context
A [[0005-greenfield-mulesoft-onpremise]] assumia ambiente **100% greenfield, inclusive o MuleSoft**, cuja instalação on-premise entraria na Etapa 0 com lead-time externo de aprovisionamento — o maior risco à data fixa de 15/nov/2026. Ao confirmar a arquitetura com a Dataprev (03/ago/2026), ficou claro que a **Dataprev já opera uma instalação MuleSoft on-premise em produção**, com a infraestrutura, a observabilidade e o modelo operacional já em pé. Não há razão para aprovisionar uma nova instância: o programa **reusa a instalação existente**. Isso remove um pré-requisito de lead-time e permite mesclar a definição de arquitetura ao Planning & Design da Fundação.

## Decision
- **MuleSoft = reuso da instalação on-premise existente** da Dataprev — não uma nova instância greenfield. A camada de integração API-led do programa é implantada **sobre a plataforma MuleSoft que já roda** no perímetro soberano da Dataprev.
- **Etapa 0 (aprovisionamento) eliminada** no que toca ao MuleSoft: sem lead-time de instalação/aprovisionamento da plataforma de integração. As 2 semanas iniciais antes dedicadas a esse aprovisionamento saem do cronograma.
- **Arquitetura mesclada ao P&D**: a "Definição de Arquitetura" antes isolada na Etapa 0 passa a ser conduzida **dentro do Planning & Design da Fundação**. A Fundação continua com 4 semanas, mas **inicia na Semana 1** (17/ago).
- **A instância Salesforce dedicada permanece 100% greenfield** (`decisions/0002`) — este reuso é **exclusivo do MuleSoft**. O isolamento da org Salesforce não muda.
- **A camada API-led ainda precisa ser desenhada e construída**: reuso da plataforma ≠ reuso das APIs. Contratos, roteamento, de-tokenização do CPF em runtime (`decisions/0001`), conciliação por lotes e integração do gateway PCI (`decisions/0003`) são net-new — representados como uma **frente MuleSoft contínua (E05)** que se estende por todo o P&D e DEV (S1-S11), com um **Arquiteto Técnico MuleSoft** dedicado (integral nas 4 primeiras semanas, 20h/sem nas semanas de dev).

## Consequences
- **Cronograma comprimido sem perder escopo**: as 2 semanas de aprovisionamento saem; a Fundação arranca na Sem. 1. Sobra folga que foi redistribuída em janelas de desenvolvimento mais longas (Marketplace S5-S10, Financeiro S6-S11 em paralelo, UAT antecipado a partir da entrega do Marketplace S8-S13), **reduzindo o risco de prazo** em vez de encurtar a duração total do build (13 semanas de build mantidas).
- **Risco de infra reduzido, não eliminado**: some o risco de "instalação on-premise não pronta a tempo"; permanece a dependência de **acessos, ambientes e capacidade** na instalação existente (Client IT / Plataforma).
- **E05 re-derivada como frente contínua**: o build da integração cresce (frente MuleSoft por todo o P&D+DEV + Arquiteto Técnico MuleSoft novo) — o esforço de integração não some com o reuso; apenas o aprovisionamento some.
- **Scale/Hypercare (novo)**: 4 semanas pós-go-live (16/nov-13/dez) para sustentar, manter e conduzir o cutover sobre a plataforma reusada.
- **G0504 permanece resolvido como on-premise**; muda apenas de "instalar on-premise" para "reusar on-premise".
- Reverter (voltar a aprovisionar uma instância nova) devolveria o lead-time da Etapa 0 e re-expandiria o cronograma — daí ser premissa.

## Grounds
Premissa confirmada com a arquitetura Dataprev em 03/ago/2026 (ditada pelo Solution Manager). Supersede parcialmente [[0005-greenfield-mulesoft-onpremise]] — mantém o trilho on-premise como ponto de de-tokenização e soberania (`decisions/0001`) e a instância Salesforce dedicada greenfield (`decisions/0002`), alterando apenas a premissa de aprovisionamento do MuleSoft (greenfield → reuso). Amplifica [[0003-e03-financeiro-xl-split-conciliacao]] (a integração do gateway PCI permanece net-new sobre a plataforma reusada). `scopezilla-recommended`, marcada accepted; a confirmar formalmente por escrito com a Dataprev junto à ratificação da instância dedicada.
