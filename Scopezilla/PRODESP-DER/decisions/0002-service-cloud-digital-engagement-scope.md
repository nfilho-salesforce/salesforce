# 0002 — Service Cloud (Digital Engagement + Agentforce Contact Center Enterprise) entra no MVP, escopado ao canal WhatsApp

**Data:** 2026-09-17 · **Status:** accepted · **Source:** scopezilla-recommended (ratificado pelo usuário na resolução de gaps de E01)

## Context

A discovery registrou "Service Cloud fora do MVP" como premissa geral (sem caso de uso de atendimento geral confirmado). Mas o canal WhatsApp/Agentforce do MVP depende, por natureza, de objetos nativos de mensageria (MessagingEndUser, MessagingSession, Case) que vivem sob Service Cloud/Digital Engagement — conflito identificado como gap `G0101` e citado como "não resolvido" no Discrepancy Scan do Discovery Brief (item 3) e como Open Question #6.

## Decision

O MVP **inclui** Service Cloud com **Agentforce Contact Center Enterprise (50 licenças)**, escopado especificamente ao canal WhatsApp de socorro emergencial:
- Setup mínimo: 1 fila única de atendimento humano, 24x7, com roteamento simples (sem skills-based routing) — premissa assumida, sujeita a revalidação com o cliente.
- Jornada: o cidadão contata via WhatsApp (texto ou áudio); o Agentforce tenta identificar a emergência e o local; se não conseguir, ou o cidadão preferir, transborda para a fila humana única.
- Divisão de responsabilidade: o Agentforce/Service Cloud cria a ordem de serviço (protocolo) e a devolve ao cidadão; o **Field Service é responsável pelo Work Order** e pelo encaminhamento/gestão de recursos de campo — Service Cloud não gerencia despacho.
- **Não inclui** Salesforce Voice (Native Telephony) — "WhatsApp voz" é só recepção/processamento de mensagens de áudio dentro do canal de mensageria, tratada pela mesma esteira de texto, sem o recurso de telefonia nativa. A ADR 0001 (URA/CTI/voz principal fora do MVP, fase de Roadmap) permanece intacta e sem alteração.
- Esta ADR **substitui** a leitura anterior de "Service Cloud fora do MVP" apenas para este canal — a exclusão geral de Service Cloud para casos de uso de atendimento amplo (fora do canal WhatsApp de socorro) continua válida.

## Consequences

- Resolve em cascata: `G0101`, `G0103`, `G0108` (E01) e antecipa a resolução de `G0210` (E02) e `G0513` (E05), que dependiam da mesma decisão.
- Muda o dimensionamento de licenciamento do Estimate: 50 licenças de Agentforce Contact Center Enterprise entram no MVP, não no Roadmap.
- O setup de fila única/roteamento simples (sem skills) é premissa assumida — precisa de revalidação formal com o cliente antes do design final do console.
- Reversão desta ADR reabriria o desenho de console do atendente humano (E01), o canal de entrega do link de rastreamento (E05), e possivelmente o registro manual via 0800 (E02).

## Grounds

Resposta direta do usuário na sessão de resolução de gaps de `requirements` (2026-09-17), ao gap `G0101`/`G0102`/`G0103`/`G0104` de `data/gaps.json`. Sem documento de discovery que confirme isso por escrito ainda — recomendação registrada como premissa assumida pelo usuário, incluída na lista de itens a revalidar formalmente com o DER/AE antes de fechar o Estimate de licenciamento.
