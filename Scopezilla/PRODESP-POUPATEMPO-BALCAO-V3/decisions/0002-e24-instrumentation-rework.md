# 0002 — E-24 é retrabalhado para instrumentar causa e frequência, não apenas o destino do fluxo

**Date:** 2026-09-24 · **Status:** accepted · **Source:** scopezilla-recommended

## Context

O inventário BPMN (E-24) faz gov.br indisponível, falha de autenticação, desistência do cidadão e timeout convergirem para "o mesmo destino" no fluxo — sem preservar qual das quatro causas terminou o atendimento (G0104). Ao mesmo tempo, R-07 (inventário §6) só se realiza se a fila viva estiver vazia com frequência suficiente no momento da ociosidade — métrica hoje não medida (G0102) — e R-08 propõe "medir taxa de conclusão da autenticação no piloto", o que exige distinguir as quatro causas por estágio de funil (G0606). E06 (observabilidade), como escopado, mede ociosidade/disponibilidade do lado do atendente, não a frequência de fila-vazia do ponto de vista do robô que R-07 realmente precisa (G0605).

Sem retrabalhar E-24, nenhum desses três gaps (G0102, G0104, G0605/G0606) pode ser resolvido isoladamente — todos dependem da mesma mudança de fluxo.

## Decision

E-24 passa a gravar, como dado estruturado no Case, a causa de encerramento (gov.br indisponível / falha de autenticação / desistência / timeout) em ramos distintos, em vez de um destino colapsado único. Adicionalmente, o gateway de antecipação (E01) passa a incrementar um contador de frequência de fila-vazia-no-momento-da-ociosidade, do ponto de vista do robô — dado que E06 consome e expõe.

## Consequences

- E01 ganha escopo de build adicional (ramos de fluxo + contador), não apenas configuração.
- E06 passa a ter uma fonte de dados real para o funil de abandono (R-08) e para a métrica de frequência de fila-vazia (R-07) — sem isso, o business case da Jornada 1 não teria como se validar no piloto.
- Reversão desta premissa devolve E-24 ao destino colapsado único e torna G0102/G0104/G0605/G0606 novamente abertos e bloqueantes para qualquer dashboard de causa/funil em E06.

## Grounds

`data/gaps.json` G0102, G0104, G0605, G0606 — citando inventário BPMN E-24, R-07 (inventário §6) e R-08 diretamente. Nenhuma fonte do cliente confirma esta instrumentação como já prevista; é premissa nossa para tornar o business case medível, a validar com o cliente em design.
