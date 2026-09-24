# 0004 — A fila viva sempre tem prioridade sobre uma oferta de antecipação em voo

**Date:** 2026-09-24 · **Status:** accepted · **Source:** scopezilla-recommended (extends client-supplied rule)

## Context

RN-17 (client-supplied) já estabelece que a fila viva tem precedência sobre a antecipação — a antecipação só é tentada quando a fila está vazia. Mas o desenho não cobre a condição de corrida: nosso serviço de seleção (E04) despacha uma oferta de antecipação no instante em que a fila fica vazia, e um cidadão espontâneo entra na fila viva antes de o cidadão da oferta responder (G0405). Relacionado: RN-16 mantém cancelamento cross-channel manual no MVP, então o serviço de seleção pode estar oferecendo um agendamento já cancelado, cujo status ficou stale entre a consulta e a resposta do cidadão (G0406); e L-31 pergunta se uma pessoa na fila espontânea que também tem agendamento futuro precisa ser suprimida/cancelada na seleção de antecipação, para não ser atendida duas vezes (G0407). As três situações são a mesma regra de precedência aplicada em pontos diferentes do fluxo.

## Decision

A fila viva sempre vence. Se um cidadão espontâneo entra na fila viva enquanto uma oferta de antecipação está em voo (aguardando resposta), a oferta em voo é cancelada — o cidadão da fila viva nunca espera por uma antecipação em andamento. O status do agendamento é reconsultado no momento da oferta (não apenas na seleção); staleness residual entre essa consulta e a resposta do cidadão é aceito como risco conhecido do MVP, coberto por RN-16 (cancelamento manual). A mesma regra de precedência cobre a coordenação entre o caminho espontâneo e o caminho de antecipação: presença simultânea na fila viva suprime/cancela uma oferta de antecipação pendente para a mesma pessoa.

## Consequences

- E04 precisa implementar cancelamento de oferta em voo como reação a um evento de entrada na fila viva, não apenas checagem de status na seleção inicial.
- O risco de staleness residual (RN-16 ainda manual) permanece aceito e documentado, não eliminado — se o cliente quiser cancelamento automático cross-channel, isso é uma mudança de escopo, não desta premissa.
- Reversão desta premissa reabre G0405/G0406/G0407 como comportamento indefinido, com risco real de dupla-marcação ou de o atendente ficar bloqueado por uma oferta que já deveria ter cedido à fila viva.

## Grounds

`data/gaps.json` G0405, G0406, G0407 — citando RN-17, RN-16 e L-31 do inventário. RN-17 é client-supplied; a resolução da condição de corrida e a extensão a G0407 são nossas, a confirmar em design.
