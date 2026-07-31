# 0003 — Salesforce é o CRM e o motor de regras de split; a execução financeira é de um gateway PCI externo

**Date:** 2026-07-31 · **Status:** accepted · **Source:** client-supplied

## Context
A solução do PAT movimenta dinheiro — recarga pré-paga, conta custódia de banco público, split/distribuição entre facilitadora, estabelecimento e governo, repasse em até 15 dias (Decreto 12.712/2025). Como o Salesforce/Dataprev **não é instituição regulada pelo Banco Central**, não pode executar transações financeiras nem custodiar dinheiro diretamente. Na sync técnica de 30/jul/2026 (00:14:40–00:16:43) travou-se a fronteira de escopo, com uma **correção do Solution Manager** sobre onde vive o motor de regras.

## Decision
A fronteira, corrigida:

- **Salesforce (CRM) — DENTRO do escopo Salesforce PS:**
  - **Motor de regras de split** — o Salesforce **calcula e aplica** as regras de rateio do pagamento (split governo/facilitadora/estabelecimento, percentuais, teto de MDR 3,6%, repasse 15 dias).
  - **Emissão da boletagem já com o split aplicado** — o CRM emite as instruções de boleto/cobrança contendo o rateio calculado.
  - **Orquestração e conciliação** — solicitação de boletos após o processamento da folha, monitoramento da conta custódia, **casamento** dos lançamentos com o boleto pago, exibição de status (BOE/racional).
  - **Recepção das movimentações bancárias** devolvidas pelo gateway, para atualizar status/contratos no CRM.

- **Gateway PCI (banco custódia) — FORA do escopo Salesforce PS, contratado pelo cliente:**
  - **Recebe as boletagens do Salesforce** (já com as regras de split aplicadas).
  - **Executa as transações bancárias** na conta custódia (movimentação de dinheiro de fato).
  - **Devolve as movimentações bancárias ao CRM** (confirmação de pagamento, liquidação).

Ou seja: **as regras são do Salesforce; a execução e a custódia são do gateway.** O Salesforce calcula, aplica e explica; não transaciona nem custodia.

## Consequences
- **E03 ganha lógica financeira real** — o motor de regras de split dentro do Salesforce é exatamente o gatilho do `size_if_assumption_breaks` de E03: **candidato forte a re-size L→XL**. Não é "instruir e esquecer"; é calcular, ratear, emitir e conciliar.
- **Out-of-scope explícito na proposta:** execução de transação financeira, custódia de dinheiro e integração com trilhos bancários de liquidação = componente externo (gateway PCI), contratado pelo cliente.
- **Nova dependência de terceiro (gap/risco):** o **provedor do gateway PCI não está definido** — dependência aberta que impacta entrega e o prazo fixo de 15/nov/2026. Envolver especialista de arquitetura bancária/financeira.
- **E05** ganha o gateway PCI como **novo alvo de integração** (recebe boletagem, devolve movimentação via webhook).
- Resolve parte do gap **G0301** (a plataforma orquestra e calcula o split; a execução é externa) e dá forma ao **G0304** (conciliação = casamento no CRM). Casa com o Decreto 12.712/2025: o *cálculo* do split/repasse é nosso, a *execução* é do gateway.
- Reverter (ex.: cliente decidir que o gateway também calcula o split) removeria o motor de regras do Salesforce e re-shapearia E03/E05 — daí ser premissa.

## Grounds
`discovery-notes/03-sync-pat-arquitetura-brief.md` §"Sinal de maior peso" (00:14:40–00:16:43) + correção do Solution Manager na sessão de revisão de 31/jul/2026 (motor de regras = Salesforce, não o gateway). Reunião **interna** Salesforce×Dataprev, a validar com o cliente. Cruza com [[0001-residencia-dados-hibrida]] (dado sensível na origem) e `discovery-notes/decreto-12712-2025-resumo-linha-do-tempo.md` (regras financeiras vigentes).
