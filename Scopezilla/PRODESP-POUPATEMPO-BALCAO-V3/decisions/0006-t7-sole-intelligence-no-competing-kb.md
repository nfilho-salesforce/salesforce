# 0006 — Agente do T7 é a fonte única de resposta a dúvidas do atendente; Salesforce não constrói uma base de conhecimento por especialidade concorrente
**Date:** 2026-09-24 · **Status:** accepted · **Source:** client-supplied

## Context
O inventário de discovery registrava dois sinais conflitantes sobre quem responde à dúvida do atendente no guichê (G0706): a tabela de mapeamento de produtos (linha 89, estado **Assumed**) propunha o Agentforce configurado sobre uma base de conhecimento por especialidade Salesforce ("Resumo do histórico e apoio à dúvida do atendente"); a Ata do cliente (RN-22, linha 121) já registrava que "o Slackbot é a porta única das dúvidas do atendente; dúvida de FAQ é encaminhada ao agente do T7 por integração." A rodada de fechamento de gaps de 23/09 resolveu essa ambiguidade com uma premissa provisória (corpora distintos, classificação de intenção pelo Slackbot) em vez de arbitrar entre as duas fontes. Em 24/09, o usuário instruiu explicitamente: o Slackbot não responderá com base em aprendizado de KB Salesforce — ele integra com o T7, que já é a inteligência da PRODESP/POUPATEMPO com esse conhecimento de oferecer respostas/opções de resolução de dúvidas ou acionamento de especialistas.

## Decision
O Agente do T7 é a fonte única de resposta a dúvidas de FAQ do atendente e de decisão de acionamento de especialista (RN-22). Não há, em paralelo, uma base de conhecimento por especialidade Salesforce nem um Agentforce configurado para responder dúvida por retrieval sobre conteúdo próprio — essa capacidade proposta (linha 89 do inventário, estado Assumed) é descartada. O Agentforce mantém apenas a capacidade de resumir o histórico de atendimento do cidadão (RN-05, decisions/0003), inalterada por esta decisão — é uma capacidade distinta, não uma resposta a dúvida. A governança de conteúdo do T7 é do cliente, fora do nosso controle e do nosso escopo formal.

## Consequences
- E07 deixa de ser "construir uma base de conhecimento por especialidade + Agentforce que responde dúvida" e passa a ser "integrar o Slackbot com o Agente do T7" — redimensionado de L para M.
- G0701 (governança de conteúdo da base por especialidade) fecha — não há mais base própria a governar.
- G0705 (suficiência de dados do Data 360 para retrieval) fecha — Data 360 perde a única justificativa que tinha em E07; sai do escopo do épico.
- G0706 (ambiguidade sobre qual sistema responde) fecha — resolvida a favor do T7/RN-22.
- G0703 (contrato técnico Slackbot↔T7: síncrono/assíncrono, tratamento de indisponibilidade) permanece aberto — a direção está decidida, o "como" técnico não.
- G0702 (guardrail de alucinação) permanece, reformulado: confirmação do atendente antes de repassar a resposta do T7 ao cidadão, em vez de citação de fonte na base por especialidade.
- Resourcing: R06/estimate-comparison Q07 perdem a justificativa de Data 360 — Q07 removido do roster do lane Quantum Leap; R06 reescrito para refletir a integração com o T7 em vez da base de conhecimento.

## Grounds
Instrução direta do usuário em 2026-09-24: "precisamos remover do escopo que o slackbot responderá com base no aprendizado de KB salesforce, pois nao sera, o slackbot vai integrar com o T7 que já é essa inteligencia criada pela PRODESP/POUPATEMPO que já tem esse conhecimento de oferecer as resposta/opcoes de resolucao de duvidas ou acionamento de especialistas." Consistente com RN-22 e a descrição do Agente do T7 já registradas em `discovery-notes/00-inventario-de-solucao-poupatempo.md` linhas 75 e 121 (Ata do cliente) — a linha 89 (tabela de mapeamento de produtos, estado Assumed) é a proposta descartada por esta decisão.
