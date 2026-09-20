# 0003 — CTI entra no MVP; Salesforce Voice/substituição da URA fica fora, como projeto separado

**Date:** 2026-09-20 · **Status:** accepted · **Source:** client-supplied (clarificação direta em revisão pós-scoping)

## Context

`decisions/0001` (2026-09-17) excluiu toda a integração de voz/URA (CTI) do MVP, deferindo-a para uma fase dedicada do Roadmap, motivado pela decisão pendente Open CTI vs. Salesforce Voice (Open CTI com retirada prevista fev/2028; contrato da URA atual — vendor "Instinct" — até abril/2027).

Em revisão pós-scoping (2026-09-20), o cliente esclareceu que essa exclusão foi registrada de forma mais ampla do que a intenção real: o que precisa ficar fora do MVP é especificamente o **Salesforce Voice / substituição nativa da URA do 0800** — um projeto de infraestrutura de telefonia ainda em viabilização entre DER e PRODESP, distinto deste programa. A **integração CTI** com a URA (atual ou uma futura substituta) para acionamento de chamada/caso e apresentação de contexto ao atendente — **entra** no MVP.

Pesquisa técnica nesta sessão (central KB Salesforce, `kb-search.py`) confirmou um ponto que não pode ficar implícito: a **Open CTI clássica está descontinuada** — modo de manutenção, indisponível para orgs Agentforce Service recém-criados, retirada prevista fevereiro/2028 — e a própria Salesforce recomenda migrar para Salesforce Voice em qualquer implementação nova (`[KA-5475]`, `[KA-5474]`, `[KA-5437]`). Por instrução do cliente nesta sessão, esta ADR **não fixa** a Open CTI como o padrão exigido — o padrão técnico exato de integração com a URA fica como premissa a confirmar, não como fato assumido.

## Decision

A integração **CTI com a URA entra no MVP**: acionamento de chamada/caso a partir da URA (atual, vendor "Instinct", ou uma futura substituta), com apresentação de contexto/screen-pop ao atendente no Service Console, via uma API de CTI compatível com o padrão técnico vigente no momento do build.

- O padrão exato (Open CTI remanescente, ou um caminho de integração equivalente) **não é nomeado nesta ADR** — depende de (i) confirmar se o org Salesforce do DER é anterior ao corte de disponibilidade da Open CTI para orgs Agentforce Service, e (ii) confirmar com o fornecedor de telefonia qual API de CTI ele expõe. Registrado como premissa a validar em `data/gaps.json` (`category: Assumption`), não como fato.
- **Fica fora do MVP**: Salesforce Voice (telefonia nativa) e a substituição da própria URA/0800 — tratado como projeto de infraestrutura de telefonia separado, cuja viabilidade ainda está sendo definida entre DER e PRODESP. "WhatsApp voz" no MVP continua sendo apenas áudio dentro do canal de mensageria (per `decisions/0002`/`0004`), não telefonia nativa.

## Consequences

- O MVP agora carrega escopo de integração CTI (acionamento via API da URA, contexto/screen-pop no Service Console) — isso pode sizar epics de atendimento (E01/E02/E03) que antes não carregavam esse escopo; revisar `data/estimates.json` para esses épicos.
- `decisions/0002` referenciava esta ADR (na versão original) como "intacta e sem alteração" — essa frase fica obsoleta e foi corrigida via `decisions/0004`, que também reconcilia o título e o corpo.
- O Roadmap não carrega mais uma fase dedicada de "CTI/voz" no nível de detalhe da versão anterior — a fase futura passa a ser especificamente "Salesforce Voice / substituição da URA do 0800", não a integração CTI em si.
- Reverter esta premissa (tirar a integração CTI do MVP de novo) reabriria o dimensionamento dos épicos de atendimento e o desenho do Console do Dispatcher/Service Console.
- G0518 (`gaps.json`, categoria Out of Scope) precisa ser reescrito para refletir o escopo correto — o que fica fora é o Salesforce Voice/substituição da URA, não a integração CTI.

## Grounds

- Instrução direta do usuário na sessão de revisão pós-scoping (2026-09-20): *"o CTI entra no MVP, recebendo o acionamento via API da URA (independentemente de ser a atual ou nova desde que atenda as premissas do CTI)... O que está fora do MVP é o Salesforce Voice e substituição da URA de atendimento 0800, isso é para nós um outro projeto que estamos ainda viabilizando a infraestrutura de telefonia com a DER e PRODESP."*
- Central KB (`kb-search.py`, 2026-09-20): `[KA-5475]` "Avoid new implementations on Open CTI; migrate to Salesforce Voice (retiring Feb 2028)"; `[KA-5474]` "Selecting a Salesforce Voice Solution: Open CTI vs Salesforce Voice vs Sales Dialer"; `[KA-5437]` "Open CTI Methods for Lightning Experience (Deprecation and Method Index)" — todos maturity: official.
- Escolha de não nomear a Open CTI como padrão exigido: resposta direta do usuário via AskUserQuestion nesta sessão (2026-09-20), opção "Não nomear o padrão agora".
