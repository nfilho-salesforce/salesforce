# Solution — Portal Desenvolve SP no Salesforce (MVP)

**Project:** DesenvolveSP · **Prepared:** 2026-08-13 · **Atualizado:** 2026-08-19 · **Scope:** jornada de crédito aprovada na *Apresentação Final* — 6 pilares, 3 esteiras (Digital, Julgamental, Agro), 24 funcionalidades · **30 integrações (planilha Discovery v3.1)** · 33 componentes. Go-live consolidado para **fim de novembro/2026** (meta original de 30/09 abandonada na reunião de 19/08). **Foco no portal do cliente (Experience Cloud); backoffice na estrutura padrão do Salesforce, apenas o mínimo necessário** — o backoffice completo permanece no Sinqia (operação dual). Dos 30, **19 endpoints** são testados via VPN antes do desenvolvimento.

> Grounding note: `knowledge/` (Salesforce product PDFs) is empty, so load-bearing claims cite the client's own **agentic-delivery repo** (`discovery-notes/desenvolvesp-develop-dsp/`) and the **approved presentation** (`Apresentação Final - Cliente Viabilidade.pdf`) — both stronger primary sources. Tags: `[KB: <path>]` = ratified artifact/ADR; `[assumption: …]` = general knowledge, what would validate it named.

---

## Architecture Foundations (cross-cutting)

**Org strategy — single, brownfield.** New work lands in the existing production org (`Desenvolve SP`, `00Das000005XO3tEAG`) alongside the already-built Captação stage (public simulator, login/MFA, Lead→Person Account conversion, JUCESP vínculo, Serasa R6 antifraud). No regression: existing behavior is preserved until explicitly decommissioned. `[KB: desenvolvesp-develop-dsp/architecture/HIGH-LEVEL-E2E.md:9-44]`

**Platform & licensing.** Financial Services Cloud (internal LEX users) + Experience Cloud LWR Customer Community (borrowers, cooperatives, guest). The licensed baseline is broader than FSC + Community — **Business Rules Engine** (Designer/Runtime/Community, 52k seats), **Enterprise Product Catalog**, **Salesforce Pricing**, **Context Service**, **Digital Lending** are confirmed *Active in production* and are in-baseline, not add-on candidates. Data Cloud / Einstein / Agentforce are excluded (No Add-on Policy); service methods stay headless so they can be exposed to agents later without rework. `[KB: .../decisions/012-product-catalog-and-native-eligibility.md]`

**Integration — event-first, zero-callout core.** Salesforce never calls Sinqia directly; all integration is orchestrated by **MuleSoft Anypoint**. Salesforce publishes to the `OpportunityInfo__e` Platform Event topic; MuleSoft subscribes, runs Sinqia + the credit/vínculo birôs, and enriches Opportunity/Account back through **standard Salesforce APIs**. **Exactly one** synchronous callout remains — the Captação simulation — via a MuleSoft façade, never Sinqia. Status is read via the **status consulta** as a state-machine for blocking steps (e.g. SERPRO); pendências are **generated in Salesforce through a dedicated API** (human actions + notifications), with the **ocorrência as the historical log**, not the primary read-trigger (client-confirmed 13/08). The portal carries **30 integrações** (grão corrente da planilha Discovery v3.1, confirmado na reunião de 19/08) across System (28) + Process (5) layers; **19 endpoints** são os que precisam de teste via VPN antes do desenvolvimento (grão operacional). *(A contagem de 19 da jornada era o grão anterior; reconciliado para 30 em 19/08 — ver gap G1002.)* **The Salesforce portal consumes a single API-Led Experience API gateway (API-31)** — an aggregating, cached, rate-limited façade — rather than fanning out to individual System/Process APIs; caching, rate-limiting, and versioning live in that Experience layer (MuleSoft-owned). `[KB: .../decisions/011-event-first-zero-callout-core.md]` — ratified locally as [decisions/0001](../decisions/0001-salesforce-never-calls-sinqia-directly.md); the Experience-gateway refinement as [decisions/0002](../decisions/0002-experience-api-gateway-for-salesforce.md). *(The MuleSoft partner's integration-lane estimate — hours, pod, ~12-week duration — is parallel grounding, not folded into this program's sizing.)*

**Journey rules are data-driven (BRE Decision Matrix).** Stage/sub-stage transitions and which birôs run at each point live in a Business Rules Engine decision table, not Apex — a transition or birô mapping changes without a deploy. `[KB: .../decisions/015-bre-decision-matrix-orchestration.md]`

**Business logic is headless.** Process orchestration lives in annotation-free service classes; controllers are thin adapters. LWC + Apex is the pro-code default; Flow for simple automation; OmniStudio a justified last resort. `[KB: .../decisions/010-headless-service-layer-for-process-orchestration.md]` `[KB: .../decisions/002-pro-code-over-omnistudio.md]`

**Sharing model.** OWD private on credit data; the guest simulator surface gets explicit minimal sharing + a dedicated FLS review. Cross-account community visibility — a borrower seeing the accounts their Contact links to (ACR), and a cooperative seeing associated empresas (AAR) — is delivered by **Apex Managed Sharing**, because native sharing sets / account hierarchy don't traverse a lateral or dynamic relationship. `[KB: .../decisions/014-cooperative-company-visibility-via-managed-sharing.md]`

**Authentication.** Platform-managed throughout — Named/External Credentials for the single callout, External Client App with JWT Bearer / Client Credentials for the MuleSoft M2M event-bus subscriber. `[KB: .../decisions/003-platform-managed-authentication.md]` `[KB: .../decisions/018-client-credentials-for-mulesoft-m2m.md]`

**Ownership boundary.** Salesforce PS delivers the **SF Core only** (LWC/Apex/metadata/config, event publish-subscribe, BRE matrix, the ocorrência↔pendência mapping as BA). **MuleSoft flows + Sinqia endpoints are Client/Evertec-owned** integration contracts (SOUL.md scope boundary).

**DevOps & governance.** Source-driven development (SF CLI + Git) with regression gates on each release — brownfield, multi-vendor (Salesforce + Evertec + Comtech + MuleSoft + DSP/Prodesp). `[assumption: standard multi-team brownfield practice; validate against the delivery repo's CICD.md]` Governance across the dual Salesforce+Sinqia operation is an open buyer conversation (gap G0004).

---

## Solution by Business Process (os 6 pilares da jornada)

A jornada é uma **estrutura única adaptativa** — a mesma para Digital, Julgamental e Agro; o sistema oculta ou exibe etapas conforme a linha de crédito e o perfil do tomador. O roteamento entre esteiras é transparente ao cliente. Cada pilar abaixo traz sua arquitetura de suporte in-line.

### Pilar 1 — Captação *(E01)*

**Business context.** Login (associação CPF/CNPJ), enriquecimento via JUCESP, cadastro manual de contas, simulação e gestão de contas/cooperativas. Substancialmente construído (Captação Sprint 0 — 19 feature files, 165 testes de regressão).

**Solution approach.** Reuso/extensão dos LWCs guest (`simulacaoDeCredito`, `simulacaoDetalhes`, `creditResultsGrid`); Lead como captura; conversão Lead→Person Account por OTP; enriquecimento JUCESP no login (bloqueia edição para evitar inconsistências); cadastro manual de contingência para produtor rural PF fora da JUCESP (não sobrescreve contas homologadas antes do backoffice).

**Supporting architecture.** Visibilidade de cooperativas via Apex managed sharing sobre AccountAccountRelation (ADR-014). Remediação brownfield: aposentar `Simulacao__c`/`Parcela__c` e o callout direto `callout:SimuladorCredito` em favor do evento Opportunity (in/out do MVP — gap G0102). *Escopo: 5 func · 2 integr · 9 comp.* `[KB: Apresentação Final p.6 · Pilar 1]`

### Pilar 2 — Pré-qualificação *(E02)*

**Business context.** Pedidos de crédito, entrada síncrona no core, biometria, validações Serpro e compliance socioambiental. O pilar mais pesado: **14 componentes, 6 integrações.** Não construído.

**Solution approach.** Formulário de pedido adaptativo (jornada única) que ajusta campos por produto; **validação facial BioValid não-obrigatória nesta entrega** — o fluxo manual (sem-CNH: análise/videochamada) é o caminho MVP, fora do caminho crítico (confirmado 13/08); exclusão socioambiental + isenção de QRSA (setor público, capital de giro digital, agro); compartilhamento de faturamento via Serpro/e-CAC; envio síncrono ao core na submissão (evita propostas incompletas).

**Supporting architecture.** O cálculo de rating socioambiental + Sensibilidade DSP deve residir no Sinqia (API-25) — local de cálculo não confirmado (gap G0601); se o Sinqia não expuser, replicar no Salesforce contraria a regra "lógica no Sinqia". Antifraude R6 + matriz BRE já construídos na Captação. `[assumption: obter spec Serpro/SENATRAN da BioValid + SLA do fallback]` `[KB: Apresentação Final p.7 · Pilar 2]`

### Pilar 3 — Proposta *(E03)*

**Business context.** Acompanhamento de propostas e tomada de decisão comercial. Lista/home parcialmente na Captação. *Escopo: 3 func · 1 integr · 6 comp.*

**Solution approach.** Componente de lista de solicitações na home (ativas + histórico, com filtros); tela de detalhes com status sincronizado do Sinqia (três estados: Simulação / Em Análise / Proposta); aceite síncrono da proposta digital que grava, liquida e consolida a operação no core.

**Supporting architecture.** Parcelas modeladas como itens de linha da Oportunidade. Status via **consulta de status** (máquina de estados, Pilar 5); frequência/SLA de frescor a definir (gap G0701). Avançar com risco Médio/Alto ou análise não concluída é bloqueado por modal. `[KB: Apresentação Final p.8 · Pilar 3]`

### Pilar 4 — Estruturação *(E04)*

**Business context.** Preenchimento cadastral profundo de PF/PJ, documentação complementar pré-comitê e gestão de arquivos. A maior superfície de formulário. Não construído. *Escopo: 6 func · 5 integr.*

**Solution approach.** Ficha PJ com reaproveitamento (identificação, dados complementares, sócios/administradores, participações, anexos); Ficha PF de pessoas relacionadas (sócios, garantidores, cônjuges), com cônjuge condicional ao estado civil e declaração PEP; geração de PDF estático da ficha; bloqueio rígido de edição pós-envio; upload assíncrono de arquivos (otimiza tráfego); pendências de documentação complementar via portal (extingue e-mail para Julgamental/Agro).

**Supporting architecture.** Sócios/participações como registros filhos (junctions Account↔Contact / Account↔Account). Validação de campos sem API de metadados do Sinqia — regras especificadas no LWC contra o mapa validado pela área de crédito (gap G0501). **Escrita PUT/PATCH ao Sinqia não confirmada** (gap G0502) — se ausente, edições ficam SF-only ou exigem workaround. Anexos em Salesforce Files (async). `[KB: Apresentação Final p.9 · Pilar 4]`

### Pilar 5 — Aprovação *(E05) — backbone de integração*

**Business context.** Sincronização de status finais de crédito. Contagem baixa (1 func · 1 integr · 1 comp) MAS complexidade técnica alta — é o backbone event-first que habilita o status em tempo real de todos os pilares.

**Solution approach.** Orquestração de workflow no modelo confirmado em 13/08: uma **API dedicada GERA pendências no Salesforce** (ações humanas + notificações); a **ocorrência é o log histórico** de conclusão, não o gatilho principal de leitura; a **consulta de status é a máquina de estados** para etapas bloqueantes (ex.: SERPRO); o **cancelamento é gerido só por status**, sem ocorrência/pendência. Pendências têm duas origens — automática (via integração) e manual (backoffice). A publicação do evento `OpportunityInfo__e` carrega o seletor de birôs definido pela matriz BRE (ADR-015/016).

**Supporting architecture.** O **catálogo ocorrências↔pendências** (código + tipo + status que precisa notificar/agir) é esforço de BA real (gap G1001); documentos/anexos enviados geram ocorrência automática no sistema, centralizando o atendimento no backoffice e eliminando a dependência de e-mail. Estratégia de erro/retry (DLQ) a definir (gap G1003); reversão cancelado→ativo (manual vs automática) em aberto (gap G0704). `[KB: Apresentação Final p.10 · Pilar 5; ADR-011; Decisões · Alinhada 13/08]`

### Pilar 6 — Formalização *(E06)*

**Business context.** Envio de CCB, garantias pós-comitê, assinatura externa e acompanhamento de contratos. Disbursement fora de escopo. Não construído. *Escopo: 4 func · 4 integr · 3 comp.*

**Solution approach.** Download da CCB em PDF estático; upload da CCB assinada (firma reconhecida ou plataforma externa) — **assinatura manual no MVP**, sem provedor de assinatura digital nativo; atendimento de pendências de garantias complexas pelo portal (Julgamental/Agro); sessão "Meus Contratos" com integração síncrona ao Sinqia para detalhes financeiros em tempo real.

**Supporting architecture.** Recuperação do arquivo de CCB reaproveita a API de contrato do Sinqia (API-03/04); a *geração* da CCB (API-30) pode reaproveitar a capacidade do BPP, mas a extensão às jornadas DSP/Julgamental não está confirmada (gap G0802). `[assumption: assinatura manual aceitável no primeiro release; validar validade legal do upload com DSP]` `[KB: Apresentação Final p.11 · Pilar 6]`

---

## T-shirt sizing

Sizes são **complexidade relativa, não esforço** — não convertíveis em horas, não multiplicáveis por tarifa. Para faixa de prazo veja `outputs/02-delivery-plan.md`; para preço, `commercials`. O detalhe dimensional por pilar está em `data/estimates.json`.

| Pilar | Épico | Size | Func · Integr · Comp | Driver dominante |
|-------|-------|------|----------------------|------------------|
| 1 Captação *(reaproveitado/QA)* | E01 | S | 5 · 2 · 9 | Construído; remediação + SIT/UAT |
| 2 Pré-qualificação | E02 | L | 5 · 6 · 14 | Maior payload de UI + integração (jornada única, QRSA, Serpro, core; BioValid opcional nesta entrega) |
| 3 Proposta | E03 | M | 3 · 1 · 6 | Aceite síncrono no core |
| 4 Estruturação | E04 | L | 6 · 5 · — | Fichas PF/PJ profundas + modelo de sócios + sync ao core |
| 5 Aprovação (backbone) | E05 | L | 1 · 1 · 1 | Contagem baixa, complexidade alta — hub que habilita o status de todos |
| 6 Formalização | E06 | M | 4 · 4 · 3 | Assinatura manual segura o tamanho em M |

**Distribuição:** 3 L · 2 M · 1 S. *(Confiança: E02, E04, E05, E06 = Assumed; alarga a faixa a jusante.)*
