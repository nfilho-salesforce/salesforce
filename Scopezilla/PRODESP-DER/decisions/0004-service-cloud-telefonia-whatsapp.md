# 0004 — Service Cloud + Telefonia + WhatsApp entram no MVP

**Data:** 2026-09-20 · **Status:** accepted · **Source:** scopezilla-recommended (ratificado pelo usuário) + client-supplied (clarificação de escopo CTI)

## Context

`decisions/0002` (2026-09-17) trouxe Service Cloud (Digital Engagement + Agentforce Contact Center Enterprise) para o MVP, escopado ao canal WhatsApp, e declarou explicitamente que `decisions/0001` (CTI/voz fora do MVP) permanecia "intacta e sem alteração". Como `decisions/0001` foi superseded por `decisions/0003` (CTI entra no MVP — ver aquele ADR), essa declaração de intangibilidade ficou obsoleta e precisa ser reconciliada.

## Decision

O MVP **inclui** Service Cloud com **Agentforce Contact Center Enterprise**, agora cobrindo dois canais de entrada:

1. **WhatsApp** (como em `decisions/0002`): 1 fila humana única 24x7, roteamento simples sem skills-based routing (premissa assumida, sujeita a revalidação). Jornada: o cidadão contata via WhatsApp (texto ou áudio); o Agentforce tenta identificar a emergência e o local; se não conseguir, ou o cidadão preferir, transborda para a fila humana única.
2. **Telefonia via integração CTI** com a URA (per `decisions/0003`): acionamento de chamada/caso a partir da URA (atual ou futura substituta), com contexto/screen-pop apresentado ao atendente no Service Console no momento do transbordo.

Divisão de responsabilidade mantida: o Agentforce/Service Cloud cria a ordem de serviço (protocolo) e a devolve ao cidadão; o **Field Service** é responsável pelo Work Order e pelo encaminhamento/gestão de recursos de campo — Service Cloud não gerencia despacho.

**Não inclui** Salesforce Voice (telefonia nativa) nem a substituição da URA/0800 — per `decisions/0003`, isso é um projeto de infraestrutura de telefonia separado, ainda em viabilização entre DER e PRODESP. "WhatsApp voz" no MVP continua sendo apenas áudio dentro do canal de mensageria, não telefonia nativa.

Esta ADR **substitui integralmente** `decisions/0002` — mesma decisão de fundo (Service Cloud/ACC Enterprise no MVP), com o escopo de canais corrigido para refletir `decisions/0003`.

## Consequences

- Resolve em cascata: `G0101`, `G0103`, `G0108` (E01) e antecipa a resolução de `G0210` (E02) e `G0513` (E05), que dependiam da mesma decisão — mesma cascata de `decisions/0002`.
- Muda o dimensionamento de licenciamento do Estimate: licenças de Agentforce Contact Center Enterprise entram no MVP, não no Roadmap — o número exato de licenças (antes citado como 50) precisa ser revalidado à luz do canal de telefonia adicional.
- O setup de fila única/roteamento simples (sem skills) é premissa assumida — precisa de revalidação formal com o cliente antes do design final do console, agora incluindo o fluxo de transbordo de CTI com screen-pop.
- O design do Service Console/atendente humano (E01) agora precisa acomodar o contexto de chamada CTI (screen-pop), não só o contexto de mensageria WhatsApp — isso é escopo novo em relação à versão anterior desta ADR.
- Reversão desta ADR reabriria o desenho de console do atendente humano (E01), o canal de entrega do link de rastreamento (E05), e possivelmente o registro manual via 0800 (E02) — mesmo blast radius de `decisions/0002`, mais o fluxo CTI.

## Grounds

- Resposta direta do usuário na sessão de resolução de gaps de `requirements` (2026-09-17), ao gap `G0101`/`G0102`/`G0103`/`G0104` de `data/gaps.json` — mesma base de `decisions/0002`.
- Instrução direta do usuário na sessão de revisão pós-scoping (2026-09-20), reconciliada via `decisions/0003`.
- Sem documento de discovery que confirme isso por escrito ainda — recomendação registrada como premissa assumida pelo usuário, incluída na lista de itens a revalidar formalmente com o DER/AE antes de fechar o Estimate de licenciamento.
