# Intent Statements — Phase 1 (DATAPREV-PAT)

> Reference role: the **load-bearing build target** for Phase 1. Each intent below is one capability — one firing trigger or user action, one outcome, one walkthrough. Build one at a time. The phase brief (`10-phase-1.md`) is orchestration; this file is what to build.
>
> **For architects:** walk these with the customer to assign priority and answer open questions. Edit `data/intents.json` (canonical) or this file directly — the next quantum-leap run re-renders from JSON.

## INT-001 — Contract-first mock harness for external systems (mock→real governance)

epic `E05` · priority _(unassigned)_ · confidence _Confirmed_ · surface `integration`

### 1. Outcome

Every external system the Novo PAT marketplace depends on is reachable through a versioned, contract-first mock behind a stable System API, so build proceeds before any real Swagger exists and swaps to the real endpoint without rework.

### 2. Build target

- Author a ratified OpenAPI contract per external system (Novo PAT, GOV.BR/Geride, eSocial, SDC, INIS PJ/Kinis PJ, gateway/banco custódia, adquirente) before dev, versioned in source
- Stand up a mock service per contract on the on-premise MuleSoft runtime that returns contract-shaped responses (happy path + named error/edge cases)
- Add automated contract tests that assert both the mock and (later) the real endpoint conform to the ratified contract
- Provide a per-system toggle (mock ↔ real) resolved by config, so cutover is a switch, not a rebuild
- Keep a dependency register of each contract with owner + committed availability date

### 3. Guardrails

- Must not code any consumer against an unratified or assumption-based contract — the OpenAPI spec is ratified first, then dev
- Must not let a mock diverge from its contract silently — a contract change breaks the contract test before it breaks the build
- Must not persist real payloads captured for mocking that contain CPF or other sensitive worker data

### 4. Out of scope

- Must not build the real external endpoints themselves — those are owned by each source system (Novo PAT, gateway, adquirente, federal sources)
- Must not deliver the mock harness as a production runtime — it retires as each real contract lands

### 5. Acceptance

A MuleSoft developer points the Novo PAT regularity consumer at the mock, runs the marketplace flow end-to-end, and it returns a contract-shaped 'situação regular' response; the developer then flips the config toggle to 'real', the contract test suite runs, and the same consumer calls the (later-available) real Novo PAT endpoint with no code change — only the toggle moved.

### 6. Dependencies

- **External:** Novo PAT / GOV.BR / eSocial / SDC / INIS PJ / gateway / adquirente — Ratified OpenAPI/Swagger contract per system with a committed delivery date and named owner _(owner: MTE/Dataprev integration owners (contracts do not exist today — G0501))_

### 7. Grounding

- **Source artifact:** decision: 0005 — Greenfield + MuleSoft on-premise _(decisions/0005-greenfield-mulesoft-onpremise.md)_
- **Source artifact:** decision: 0001 — Residência de dados híbrida _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] What is the committed availability date and owner for each external system's API contract? (No Swaggers exist today — highest integration risk.) (Resolver: MTE/Dataprev integration lead)
- [ ] Will mocks follow a ratified, versioned contract (contract-first/OpenAPI) with contract tests, or be assumption-based? Governance for mock→real without rework is undefined. (Resolver: Integration architect / Dataprev)

---

## INT-002 — CPF de-tokenization / identity-resolution service on-premise

epic `E05` · priority _(unassigned)_ · confidence _Confirmed_ · surface `integration`

### 1. Outcome

The Salesforce core references workers and establishments by non-sensitive token; nominal/CPF data is resolved at runtime, only when authorized, inside the Dataprev sovereign perimeter and never persisted in the Salesforce cloud.

### 2. Build target

- Build a de-tokenization/resolution API on the on-premise MuleSoft runtime that maps a non-sensitive reference token to nominal/CPF data held at source (Dataprev bases)
- Enforce authorization on every resolution call, so nominal data is returned only for an authorized actor and purpose
- Emit an audit trail of each resolution (who, when, why) without writing CPF into the audit record
- Ensure Salesforce-bound responses carry only the token plus non-sensitive attributes; nominal fields are resolved to the UI/experience layer at runtime, not stored

### 3. Guardrails

- Must not persist CPF or nominal worker data in any Salesforce object or Salesforce-hosted store
- Must not run the resolution point outside the Dataprev sovereign perimeter (on-premise only, never CloudHub)
- Must not return nominal data to an unauthorized caller or without a logged purpose

### 4. Out of scope

- Must not build the sovereign source data stores themselves (Dataprev/Oracle on-premise bases) — those are Dataprev-owned
- Must not own the portal login/authorization decision — that is the Experience/portal capability; this service enforces the decision it is handed

### 5. Acceptance

A monitoring analyst opens a flagged transaction in Salesforce that shows only a token and non-sensitive attributes; when authorized, the UI requests resolution, MuleSoft on-premise returns the worker's nominal data at runtime, an audit entry is written without storing the CPF, and no CPF ever lands in a Salesforce object.

### 6. Dependencies

- **External:** Dataprev sovereign data bases — Runtime lookup interface from token to nominal/CPF data at source _(owner: Dataprev architecture (Jair Bogo))_
- **External:** On-premise MuleSoft infrastructure — Provisioned, accessible on-premise runtime by the project milestone _(owner: Dataprev infra (Fase 0 lead-time prerequisite))_

### 7. Grounding

- **Source artifact:** decision: 0001 — Residência de dados híbrida (dado sensível fora da nuvem SF) _(decisions/0001-residencia-dados-hibrida.md)_
- **Source artifact:** decision: 0005 — MuleSoft on-premise = ponto de de-tokenização _(decisions/0005-greenfield-mulesoft-onpremise.md)_

### Open questions

- [ ] Which exact fields are tokenized and where is the residency boundary drawn (final data-flow design under LGPD)? (Resolver: Dataprev architecture (Jair Bogo))

---

## INT-003 — External-caller authentication & rate-limited token validation gateway

epic `E05` · priority _(unassigned)_ · confidence _Confirmed_ · surface `security`

### 1. Outcome

External callers (facilitadoras, adquirente) authenticate by CNPJ via client-credentials flow against a scope-restricted connected app; tokens are validated with rate limiting and caching before any integration endpoint runs.

### 2. Build target

- Configure a connected app per external caller class with least-privilege OAuth scopes
- Implement client-credentials (server-to-server) flow keyed to the caller's CNPJ identity
- Validate the presented token on every inbound call, with a token cache to avoid revalidation storms and per-caller rate limiting
- Define secret storage, rotation, and trust-store handling for the caller credentials on the on-premise runtime

### 3. Guardrails

- Must not grant a connected app broader scope than the endpoints that caller class is entitled to
- Must not accept an unvalidated or expired token, and must not let the cache serve a revoked token past its TTL
- Must not hard-code or log caller secrets; secrets are stored and rotated, not embedded

### 4. Out of scope

- Must not build citizen/portal login (GOV.BR OIDC / procuração digital) — that is the Experience/portal authentication capability
- Must not define the per-system auth standard for federal sources (mTLS, ICP-Brasil, gov.br OIDC) beyond what a ratified contract specifies — see open question

### 5. Acceptance

A facilitadora's system presents its CNPJ-scoped client credentials, MuleSoft issues a token, and a subsequent call to the open-demand consultation endpoint is admitted only after token validation succeeds; a burst of calls from the same facilitadora is throttled at the configured rate, and a revoked credential is rejected within the cache TTL.

### 6. Dependencies

- **External:** Federal source systems — Declared auth standard per system (OAuth2 client-credentials, mTLS, ICP-Brasil cert, gov.br OIDC) _(owner: Dataprev / each federal system owner (not specified today — G0505))_

### 7. Grounding

- **Source artifact:** decision: 0002 — Instância dedicada e apartada _(decisions/0002-instancia-dedicada-mte-pat.md)_

### Open questions

- [ ] What auth/authz standard does each external system require, and how are secrets, rotation, and trust store managed across 600–700 facilitadoras plus federal systems? (Resolver: Integration security architect / Dataprev)

---

## INT-004 — Federal-source read & validation System APIs (mock-first)

epic `E05` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

The platform validates a beneficiária's/facilitadora's regular standing and reads required reference data from federal sources (Novo PAT regularity, GOV.BR/Geride, eSocial, SDC) through System APIs, running on mocks now and cutting over to real endpoints when contracts land.

### 2. Build target

- Build a System API per federal source that normalizes its response into a canonical, non-sensitive shape for the core
- Implement the Novo PAT 'situação regular' validation call used to gate marketplace participation (Novo PAT has no API today — mock-first is mandatory)
- Wire read integrations for GOV.BR/Geride (identity/auth reference), eSocial and SDC as reference-data reads
- Route each System API through the de-tokenization and auth capabilities rather than handling sensitive data or credentials itself

### 3. Guardrails

- Must not persist sensitive federal-source data in Salesforce — reads resolve at runtime and reference by token
- Must not block the build on real endpoints — every federal source runs mock-first until its contract is ratified
- Must not treat a mock response shape as authoritative once the real contract is available without re-running contract tests

### 4. Out of scope

- Must not build or host the federal systems' APIs — Novo PAT, GOV.BR, eSocial, SDC endpoints are owned outside the Salesforce/MuleSoft build
- Must not own the CTPS Digital 'expectativa de crédito' notification — that is monitoring-only in the MVP and its ownership boundary is unresolved

### 5. Acceptance

A beneficiária's regularity is checked during marketplace onboarding: the core calls the Novo PAT System API, MuleSoft returns a canonical 'regular/irregular' result from the mock, and the marketplace gates participation accordingly; when the real Novo PAT contract lands, the same System API serves live data after contract tests pass.

### 6. Dependencies

- **External:** Novo PAT (novopat.trabalho.gov.br) — Real API contract for regularity validation — none exists today (mock-first mandatory) _(owner: MTE / Novo PAT)_
- **External:** GOV.BR/Geride, eSocial, SDC — Ratified read contracts and auth standards _(owner: Respective federal system owners)_

### 7. Grounding

- **Source artifact:** decision: 0001 — Residência de dados híbrida _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] Is the CTPS Digital 'crédito concedido' activation notification in Salesforce (via MuleSoft) scope, or MTE/Novo PAT responsibility? Does a CTPS Digital API contract exist? (Resolver: MTE / Dataprev integration lead)

---

## INT-005 — INIS PJ / Kinis PJ termo-de-aceite data ingest

epic `E05` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

The platform ingests the acceptance-term data originated in INIS PJ/Kinis PJ — worker counts by salary band and matriz/filial structure — as the source of the beneficiária's termo de aceite, referenced by non-sensitive identifier in the core.

### 2. Build target

- Build a System API that reads the INIS PJ/Kinis PJ acceptance-term dataset: number of workers by salary band and matriz/filial breakdown
- Normalize it into a canonical shape the marketplace/quote flow consumes to shape the beneficiária's demand
- Reference the beneficiária/establishment by non-sensitive identifier; resolve any sensitive fields at runtime via the de-tokenization service
- Run mock-first against a ratified contract until the real INIS PJ endpoint is available

### 3. Guardrails

- Must not persist sensitive worker-level data from INIS PJ in Salesforce — ingest aggregates (counts by band) and reference by token
- Must not proceed on an assumed INIS PJ payload shape — the contract is ratified before dev
- Must not silently drop matriz/filial structure — the split/quote logic downstream depends on it

### 4. Out of scope

- Must not compute the split or quote itself — that is the E03 split-rules engine; this capability delivers the input data
- Must not own the INIS PJ source system

### 5. Acceptance

When a beneficiária begins a demand, the platform reads the INIS PJ termo-de-aceite via MuleSoft and receives worker counts by salary band plus matriz/filial structure in canonical form (mock now); the quote flow uses those counts to shape the demand, and no worker-level sensitive data is stored in Salesforce.

### 6. Dependencies

- **External:** INIS PJ / Kinis PJ — Ratified contract for acceptance-term data (worker counts by salary band, matriz/filial) _(owner: MTE/Dataprev (contract not available today — G0501))_

### 7. Grounding

- **Source artifact:** decision: 0001 — Residência de dados híbrida _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] Confirm the INIS PJ/Kinis PJ contract shape for salary-band buckets and matriz/filial, and whether any field crosses the sensitive-data boundary. (Resolver: Dataprev architecture)

---

## INT-006 — Facilitadora standard contract: Quote hand-off, processed-return, open-demand pull endpoint

epic `E05` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

Every one of the ~600–700 facilitadoras integrates through one standard API contract: it receives Quotes, returns the processed result plus value, and can pull the open demands in the current vigência — a certifiable single contract, not a bespoke connector per facilitadora.

### 2. Build target

- Define one standard, versioned API contract all facilitadoras integrate against (no N-to-N bespoke connectors)
- Build the outbound Quote hand-off from the marketplace to the facilitadora and the inbound processed-result + value return
- Expose a consultation (pull) endpoint that returns the beneficiária demands open during the current vigência (MVP is pull only)
- Route facilitadora calls through the CNPJ auth gateway; reference beneficiárias/establishments by token

### 3. Guardrails

- Must not build per-facilitadora custom connectors — the scale (600–700) requires one standard contract behind a certification path
- Must not expose sensitive data on the pull endpoint — open demands are returned by non-sensitive reference
- Must not admit an unauthenticated facilitadora call — every call passes the CNPJ client-credentials gateway

### 4. Out of scope

- Must not build active push notification to facilitadoras when a demand is published — push (channel undefined) is roadmap-future; the MVP delivers pull only
- Must not build a self-service certification portal/sandbox in Phase 1 unless the onboarding model is ratified — see open question
- Must not execute the financial split — the returned value feeds E03, it is not computed here

### 5. Acceptance

A facilitadora, authenticated by its CNPJ credentials, calls the consultation endpoint and receives the list of open demands in the current vigência (by reference, no sensitive data); it submits a processed Quote result with value through the standard contract, and the marketplace records the return against the correct demand.

### 6. Dependencies

- **External:** Facilitadoras (~600–700, e.g. Visa Vale, Pluxee, Caju) — Adoption of and certification against the standard API contract _(owner: Facilitadoras + MTE onboarding process (model undefined — G0503))_

### 7. Grounding

- **Source artifact:** decision: 0003 — Fronteira CRM não-transacional _(decisions/0003-fronteira-crm-nao-transacional.md)_

### Open questions

- [ ] What is the facilitadora onboarding model — one standard contract with self-service certification sandbox, or per-facilitadora connectors? Is there a homologation/versioning process? (Dominant MuleSoft sizing driver.) (Resolver: MTE / Dataprev integration lead)
- [ ] For the future active-push notification to facilitadoras when a demand is published, which channel (webhook/event to facilitadora API, email, WhatsApp/BSP, in-app, Marketing Cloud)? MVP is pull only. (Resolver: Client / MTE)

---

## INT-007 — Adquirente credenciamento-check API & transaction-monitoring ingest

epic `E05` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

An adquirente can query an establishment's accreditation status before processing a transaction, and sends all transactions into the platform for monitoring — the a-posteriori visibility feed for the MTE.

### 2. Build target

- Expose a credenciamento-status query API the adquirente calls (by establishment identifier) before processing a transaction, returning accredited/not-accredited
- Build the inbound transaction-monitoring ingest that receives all transactions from the adquirente (establishment, value, date/time, buyer reference)
- Reference the buyer by token; resolve CPF only at runtime for authorized monitoring, never persist it
- Route adquirente calls through the CNPJ auth gateway; apply rate limiting to the transaction feed

### 3. Guardrails

- Must not persist the buyer's CPF in Salesforce — the monitoring feed references by token and resolves nominal data only when authorized
- Must not return accreditation status to an unauthenticated adquirente
- Must not process or settle the transaction — the platform monitors a-posteriori, it does not authorize the payment

### 4. Out of scope

- Must not build the anomaly-detection/monitoring analytics itself — that is the E04 monitoring capability; this delivers the ingest feed and the credential-check API
- Must not own the adquirente's transaction system

### 5. Acceptance

Before processing, the adquirente calls the credenciamento-check API with an establishment identifier and receives 'accredited'; it then processes and sends the transaction to the monitoring ingest, which lands it (referencing the buyer by token) for the MTE's a-posteriori visibility — with the CPF resolvable only under authorization and never stored.

### 6. Dependencies

- **External:** Adquirente(s) — Ratified contract for the credenciamento-check call and the transaction-monitoring feed, plus expected volumes/peaks _(owner: Adquirente + MTE (contract not available today — G0501))_

### 7. Grounding

- **Source artifact:** decision: 0001 — Residência de dados híbrida _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] What are the expected transaction volumes/peaks from the adquirente feed, and the resilience RNFs (idempotency, retry/backoff, dead-letter) required for the monitoring ingest? (Resolver: Integration architect / MTE)

---

## INT-008 — Scheduled incremental bank-movement reconciliation feed (gateway → CRM)

epic `E05` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

On a MuleSoft schedule, the platform pulls the registered boleto and the incremental bank movements returned by the gateway/banco custódia and lands them in the CRM so the split boletagem can be matched to what was actually paid.

### 2. Build target

- Build a scheduled MuleSoft job that pulls, on an interval, the incremental bank movements and registered-boleto confirmations from the gateway/banco custódia (batch incremental, not real-time — ADR 0003)
- Track a high-water mark so each run pulls only new movements (incremental, not full re-pull)
- Land the movements into the CRM as non-transactional records to update boleto/contract status for reconciliation
- Make ingestion idempotent so a re-run or overlapping window cannot double-post a movement (financial duplicate risk)

### 3. Guardrails

- Must not execute or custody any financial transaction — the platform receives movements for reconciliation; execution and custody are the external gateway's (ADR 0003)
- Must not double-post a movement — ingestion is idempotent, keyed on the gateway's movement identifier
- Must not re-pull the full dataset each run — the feed is incremental via high-water mark

### 4. Out of scope

- Must not emit the boletagem or compute the split — that is the E03 split-rules engine; this capability ingests the gateway's return
- Must not build the matching/conciliation business logic UI — this delivers the feed the reconciliation consumes (name the owning E03 capability)
- Must not build the gateway/banco custódia itself

### 5. Acceptance

On its scheduled run, the MuleSoft job pulls only bank movements newer than the last high-water mark from the gateway, posts each once (a re-run of the same window posts nothing new), and updates the corresponding boleto's status in the CRM so a reconciliation view can match emitted boletagem to settled payments.

### 6. Dependencies

- **External:** Gateway PCI / banco custódia — Provider selection plus a contract returning registered boleto and incremental bank movements; PCI provider is undefined _(owner: Client (gateway not yet contracted — Fase 0 prerequisite, ADR 0003))_

### 7. Grounding

- **Source artifact:** decision: 0003 — Fronteira CRM não-transacional; gateway devolve movimentações _(decisions/0003-fronteira-crm-nao-transacional.md)_

### Open questions

- [ ] What are the resilience RNFs for the financial feed — idempotency guarantees, retry/backoff, dead-letter, reconciliation SLA — given duplicate-payment risk under the 15-day repasse (Decreto 12.712/2025)? (Resolver: Integration architect / banking-finance specialist)
- [ ] Who is the PCI gateway/banco custódia provider, and what is the committed contract-availability date? (Undefined third-party dependency against the fixed 15/nov/2026 go-live.) (Resolver: Client / MTE)

---

## INT-009 — Modelo de dados de referências tokenizadas — CPF e dados sensíveis nunca persistem na org

epic `E08` · priority _(unassigned)_ · confidence _Assumed_ · surface `data-model`

### 1. Outcome

Os objetos do PAT (cotação, proposta, contrato, folha, beneficiária, estabelecimento) referenciam pessoas e estabelecimentos por um identificador não-sensível; nenhum CPF ou dado pessoal sensível é gravado em campo, anexo, histórico ou log da org Salesforce.

### 2. Build target

- Definir, campo a campo, quais atributos podem transitar/persistir na org e quais permanecem exclusivamente na infraestrutura Dataprev (a fronteira de residência do ADR 0001)
- Modelar os objetos de negócio para chavear por um identificador tokenizado (referência opaca, não derivável do CPF) em vez do CPF ou de qualquer dado pessoal
- Garantir que campos de exibição do dado nominal sejam calculados/preenchidos em runtime e não gravados em repouso (sem persistência do valor resolvido)
- Aplicar Shield Platform Encryption aos campos-fronteira que, por decisão ratificada, precisarem transitar, como defesa em profundidade

### 3. Guardrails

- Nenhum CPF ou dado pessoal sensível pode ser gravado em campo, texto livre, anexo, histórico de campo ou log da org
- O identificador tokenizado não pode ser reversível para o CPF por lógica dentro da org (a resolução só ocorre no perímetro soberano Dataprev)
- Não modelar a fronteira campo-a-campo sem ratificação escrita da arquitetura Dataprev (Jair Bogo) — modelar sobre suposição re-desenha E01/E02/E03/E06

### 4. Out of scope

- Persistência de qualquer dado sensível em repouso na nuvem Salesforce
- Armazenamento do CPF como chave natural ou identificador externo dos objetos
- Cópia de tabelas transacionais vinculadas a CPF para dentro da org

### 5. Acceptance

Um encarregado de dados (DPO) inspeciona o modelo de dados e uma amostra de registros de beneficiária, estabelecimento, cotação e contrato e não encontra CPF nem dado pessoal sensível gravado em nenhum campo, anexo, histórico ou log; toda referência a pessoa/estabelecimento aparece como identificador tokenizado não-reversível, e o dado nominal só aparece quando resolvido em runtime.

### 6. Dependencies

- **External:** Arquitetura de dados Dataprev — Ratificação escrita da fronteira campo-a-campo de residência (quais atributos persistem na org vs. permanecem exclusivamente na infra Dataprev) _(owner: Dataprev (Jair Bogo))_

### 7. Grounding

- **Source artifact:** decision: ADR 0001 — Residência de dados híbrida _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] Qual a fronteira exata de residência campo a campo — quais atributos podem transitar/persistir na org e quais ficam exclusivamente na infra Dataprev (CPF, transações vinculadas)? (Resolver: Arquitetura Dataprev (Jair Bogo) — ratificação escrita)

---

## INT-010 — Contrato de de-tokenização em runtime via MuleSoft on-premise

epic `E08` · priority _(unassigned)_ · confidence _Assumed_ · surface `data-model`

### 1. Outcome

Quando um usuário autorizado precisa ver o dado nominal de uma beneficiária/estabelecimento, a org resolve o identificador tokenizado em runtime por uma chamada ao MuleSoft on-premise, que de-tokeniza no perímetro soberano Dataprev — sem que o dado resolvido seja gravado na org.

### 2. Build target

- Definir o contrato de resolução em runtime (entrada: identificador tokenizado + contexto de autorização; saída: dado nominal apenas para exibição transitória) exposto pelo MuleSoft on-premise
- Modelar o acesso ao dado sensível como objeto/entidade externa ou callout — o dado vive na origem e é lido sob demanda, nunca replicado
- Tratar timeout, indisponibilidade e negação de autorização com caminho de exceção explícito (degradação previsível, sem vazar dado parcial nem persistir cache)
- Registrar cada resolução como evento de acesso a dado sensível (alimenta a trilha de auditoria)

### 3. Guardrails

- O dado nominal resolvido não pode ser persistido, cacheado em repouso nem gravado em campo/log após a exibição transitória
- A de-tokenização não pode ocorrer dentro da org — só no MuleSoft on-premise, dentro do perímetro soberano
- Toda resolução deve carregar contexto de autorização; uma chamada sem direito de acesso não retorna o dado nominal

### 4. Out of scope

- Hospedagem do MuleSoft em CloudHub ou fora da infra soberana Dataprev (ADR 0005: on-premise)
- De-tokenização executada por lógica interna da org Salesforce
- Cache persistente do dado sensível resolvido para desempenho

### 5. Acceptance

Um auditor acompanha um atendente autorizado abrindo o cadastro de uma beneficiária: o nome/CPF aparece na tela resolvido em runtime; ao inspecionar a org após fechar a tela, o auditor confirma que nada do dado nominal foi gravado; uma tentativa da mesma leitura por usuário sem direito de acesso não retorna o dado, e a indisponibilidade do MuleSoft degrada de forma previsível sem expor dado parcial.

### 6. Dependencies

- **External:** MuleSoft on-premise (infra Dataprev) — Serviço de de-tokenização/resolução no perímetro soberano, pronto e acessível nos marcos do projeto (pré-requisito de arranque, lead-time externo) _(owner: Dataprev)_

### 7. Grounding

- **Source artifact:** decision: ADR 0001 — Residência híbrida (data-at-source / tokenização) _(decisions/0001-residencia-dados-hibrida.md)_
- **Source artifact:** decision: ADR 0005 — Greenfield + MuleSoft on-premise (soberania) _(decisions/0005-greenfield-mulesoft-onpremise.md)_

### Open questions

- [ ] Como criar/gerenciar o usuário do portal (Experience Cloud) sem persistir CPF — via identificador tokenizado resolvido em runtime — e como isso é compatível com SSO gov.br e a sessão do Experience Cloud? (Resolver: Arquitetura Dataprev (Jair Bogo) + time de Experience Cloud)

---

## INT-011 — Trilha de auditoria imutável de acesso a dado sensível

epic `E08` · priority _(unassigned)_ · confidence _Assumed_ · surface `security`

### 1. Outcome

Todo acesso a dado sensível (resolução de identificador, leitura de campo-fronteira, ação sobre registro financeiro) gera um registro de trilha imutável — quem, o quê, quando — que sustenta escrutínio de TCU/CGU/ANPD e não pode ser alterado nem apagado por administrador.

### 2. Build target

- Definir o conjunto de eventos auditáveis: resolução de dado nominal via MuleSoft, acesso a campos-fronteira, ações sobre objetos financeiros (split, boletagem, conciliação)
- Materializar a trilha com Field Audit Trail e Event Monitoring (produtos reais), retendo o histórico pelo horizonte regulatório exigido
- Garantir a imutabilidade da trilha — nem administrador da org pode editar ou apagar registros de acesso
- Expor a trilha de forma consultável por auditor/DPO (quem acessou qual referência, quando, sob qual autorização)

### 3. Guardrails

- Registros de trilha de acesso a dado sensível não podem ser editáveis nem deletáveis por nenhum perfil, inclusive administrador
- A trilha não pode registrar o valor do dado sensível em claro — registra a referência tokenizada e o evento de acesso, não o CPF
- A retenção não pode ser menor que o horizonte regulatório a confirmar com o cliente

### 4. Out of scope

- Trilha de auditoria de eventos não relacionados a dado sensível ou a operações financeiras (fora do gatilho regulatório)
- Ferramenta externa de SIEM/observabilidade fora da org (responsabilidade da infra Dataprev)

### 5. Acceptance

Um auditor do TCU/CGU consulta a trilha por um período e vê, para cada acesso a dado sensível, quem acessou, qual referência tokenizada, quando e sob qual autorização; ao tentar alterar ou apagar um registro da trilha — mesmo com perfil de administrador — a ação é negada, comprovando a imutabilidade.

### 7. Grounding

- **Source artifact:** decision: ADR 0002 — Instância dedicada (auditabilidade TCU/CGU/ANPD) _(decisions/0002-instancia-dedicada-mte-pat.md)_

### Open questions

- [ ] Qual o horizonte de retenção da trilha de auditoria exigido pelo cliente/regulador (TCU/CGU/ANPD)? (Resolver: Cliente MTE + jurídico/compliance)

---

## INT-012 — Mascaramento de CPF em logs, depuração e mensagens de erro

epic `E08` · priority _(unassigned)_ · confidence _Assumed_ · surface `security`

### 1. Outcome

CPF e dados pessoais sensíveis nunca aparecem em claro em logs de sistema, logs de depuração, mensagens de erro, notificações ou telas de diagnóstico — são mascarados ou substituídos pela referência tokenizada em toda saída observável.

### 2. Build target

- Estabelecer o padrão de mascaramento (ex.: exibir só a referência tokenizada, ou dígitos parcialmente ocultos) aplicado a toda saída de log/erro/diagnóstico
- Garantir que integrações (callouts MuleSoft, gateway PCI) não ecoem CPF em payloads de erro ou logs de request/response gravados na org
- Cobrir os pontos onde dado sensível pode vazar por engano: mensagens de exceção, notificações, debug logs, telas de erro para o usuário

### 3. Guardrails

- CPF em claro não pode aparecer em log de sistema, debug log, mensagem de exceção, notificação ou tela de diagnóstico
- Payloads de erro de integração não podem gravar o dado nominal na org
- O mascaramento não pode ser contornável por elevação de log level ou por perfil de administrador

### 4. Out of scope

- Mascaramento em sistemas de log da infra Dataprev fora da org (responsabilidade Dataprev)
- Anonimização de dados para ambientes de teste (tratado em provisionamento/dados de sandbox, não aqui)

### 5. Acceptance

Um engenheiro de operações eleva o nível de log e reproduz um erro numa transação com dado sensível; ao inspecionar debug logs, mensagens de erro e notificações resultantes, um DPO confirma que nenhum CPF aparece em claro — só a referência tokenizada ou dígitos mascarados.

### Open questions

_(no open questions captured)_

---

## INT-013 — Modelo de isolamento e acesso de menor privilégio na org dedicada

epic `E08` · priority _(unassigned)_ · confidence _Assumed_ · surface `security`

### 1. Outcome

Dentro da instância dedicada e apartada do MTE/PAT, o acesso a dado sensível e a operações financeiras é concedido por menor privilégio via permission sets e modelo de compartilhamento, de modo que só perfis autorizados resolvem dado nominal e nenhum administrador de outro ambiente Dataprev enxerga estes dados.

### 2. Build target

- Definir os perfis/personas e mapear quem pode resolver dado nominal, quem vê apenas referências tokenizadas e quem opera funções financeiras
- Implementar o acesso por permission sets (concessão aditiva, menor privilégio) e desenhar o modelo de compartilhamento (org-wide defaults restritivos + compartilhamento explícito) para os objetos sensíveis/financeiros
- Assegurar que a autorização de resolução em runtime (contrato MuleSoft) respeite o mesmo modelo de permissão da org
- Documentar a matriz de acesso como evidência para auditoria

### 3. Guardrails

- Nenhum administrador ou perfil de outro ambiente Dataprev pode ter acesso a esta org ou a estes dados (isolamento por construção — greenfield, ADR 0005)
- O acesso a dado sensível e a operações financeiras não pode ser concedido por padrão — só por permission set explícito, menor privilégio
- A resolução de dado nominal em runtime não pode contornar o modelo de permissão da org

### 4. Out of scope

- Provisionamento físico da org dedicada e do MuleSoft on-premise (pré-requisito de Fase 0, procurement — dependência externa, não build Salesforce)
- Modelo de administração de outros ambientes Dataprev (esta org é apartada)
- Integração de identidade/SSO gov.br em si (tratado em E01, aqui só o alinhamento do modelo de permissão)

### 5. Acceptance

Um administrador de segurança verifica que um atendente sem o permission set de dado sensível vê apenas referências tokenizadas e não consegue disparar a resolução em runtime; que um operador financeiro só acessa o que sua função exige; e o cliente confirma que nenhum administrador de outro ambiente Dataprev tem qualquer acesso a esta org.

### 6. Dependencies

- **External:** Provisionamento de infra (org dedicada + MuleSoft on-premise) — Instância dedicada e apartada provisionada do zero (greenfield) e MuleSoft on-premise instalado, prontos nos marcos do projeto — lead-time externo que compete com a data fixa 15/nov/2026 _(owner: Dataprev / MTE)_

### 7. Grounding

- **Source artifact:** decision: ADR 0002 — Instância dedicada e apartada (isolamento forçado, administração pelo MTE) _(decisions/0002-instancia-dedicada-mte-pat.md)_
- **Source artifact:** decision: ADR 0005 — Greenfield + MuleSoft on-premise (isolamento por construção) _(decisions/0005-greenfield-mulesoft-onpremise.md)_

### Open questions

- [ ] A decisão de instância dedicada e apartada (Cenário B) ainda é verbal (call 30/jul/2026) — precisa de ratificação escrita do cliente antes do build. (Resolver: Cliente MTE (diretoria) — ratificação escrita na proposta)
- [ ] Como o User/Contact do portal Experience Cloud é criado/gerenciado sob menor privilégio sem persistir CPF, de forma compatível com SSO gov.br? (Resolver: Arquitetura Dataprev (Jair Bogo) + time de Experience Cloud)

---

## INT-014 — Autenticação gov.br via OpenID Connect no Experience Cloud

epic `E01` · priority _(unassigned)_ · confidence _Assumed_ · surface `security`

### 1. Outcome

Uma representante de uma empresa beneficiária entra no portal do PAT usando sua conta gov.br, sem senha própria da plataforma — a identidade gov.br é a única porta de entrada.

### 2. Build target

- Auth Provider OpenID Connect (OIDC) customizado apontando para o provedor gov.br, com o portal registrado como Relying Party (client_id/redirect_uri de produção)
- Registration Handler em Apex que resolve a pessoa autenticada para um User de portal do Experience Cloud, sem persistir CPF (referência tokenizada, aderente à residência híbrida)
- Botão único 'Entrar com gov.br' na landing/login do portal (tema LWR), sem cadastro local de credenciais
- Nível mínimo de garantia da conta gov.br (Bronze/Prata/Ouro) checado/exigido no fluxo de login

### 3. Guardrails

- Must not persistir CPF (nem identificador pessoal derivado que seja dado sensível) no User/Contact do portal — a identidade se resolve por referência tokenizada em runtime
- Must not oferecer cadastro/senha local: gov.br é o único provedor de identidade da beneficiária
- Must not tratar a facilitadora como usuária de portal — ela é API-only (E05) e não autentica pela tela

### 4. Out of scope

- Must not autenticar o estabelecimento por identidade PJ distinta (e-CNPJ/certificado) nesta capacidade — tratado à parte se confirmado (G0402)
- Must not implementar o provedor de identidade gov.br em si — apenas consumi-lo como Relying Party

### 5. Acceptance

Uma analista de RH da empresa beneficiária abre o portal, clica em 'Entrar com gov.br', é redirecionada ao gov.br, autentica com a conta no nível de garantia exigido e retorna ao portal já reconhecida como usuária, sem ter criado ou digitado qualquer senha da plataforma. Nenhum CPF fica gravado no registro de usuário do Salesforce.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009
- **External:** gov.br — Credenciamento do portal como Relying Party (client_id/redirect_uri de produção) e definição do nível mínimo de garantia (Prata/Ouro) _(owner: MTE/Dataprev junto ao gov.br)_

### 7. Grounding

- **Source artifact:** decision: 0001 — residência de dados híbrida (CPF não persiste no SF) _(decisions/0001-residencia-dados-hibrida.md)_
- **Source artifact:** wireframe: Protótipo Figma tela 1 — Landing/Login, botão único 'Entrar com gov.br' _(.discovery-context.md)_

### Open questions

- [ ] O gov.br autoriza o cadastro do marketplace como Relying Party em produção (client_id/redirect_uri) e qual o nível mínimo de conta (Prata/Ouro) exigido da beneficiária? (Resolver: MTE/Dataprev junto ao gov.br)
- [ ] Como criar/gerir o User de portal sem persistir CPF, mantendo compatibilidade com a sessão do Experience Cloud e o SSO gov.br (identificador tokenizado resolvido via MuleSoft)? (Resolver: Arquitetura Dataprev (Jair Bogo))

---

## INT-015 — Seleção 'representar empresa' dirigida por procuração

epic `E01` · priority _(unassigned)_ · confidence _Assumed_ · surface `experience-cloud`

### 1. Outcome

Após o login, a representante vê apenas os CNPJs que sua procuração digital a autoriza a operar, escolhe uma empresa (Matriz ou Filial) e passa a navegar o portal naquele contexto — podendo trocar de empresa pelo menu superior.

### 2. Build target

- Tela pós-login 'Selecionar empresa que deseja representar' (LWC no Experience Cloud) listando os vínculos válidos da pessoa: Razão Social + CNPJ + tipo (Matriz/Filial) + situação (Ativa)
- Busca por Razão Social/CNPJ e ação Selecionar/Continuar; estado 'empresa selecionada' que estabelece o contexto de operação
- Troca de empresa a qualquer momento pelo menu superior, sem novo login
- Contexto de empresa selecionada propagado às telas subsequentes (Cotações, Folha) — a beneficiária opera Opportunity (demanda) e Quote (comparação/seleção) no escopo daquele CNPJ

### 3. Guardrails

- Must not exibir empresa para a qual a pessoa não tenha vínculo válido e ativo — a lista é a interseção da procuração vigente
- Must not deixar a sessão sem contexto de empresa: nenhuma operação de negócio ocorre antes de uma seleção válida
- Must not permitir operar dados de uma empresa após a troca para outra (isolamento por contexto selecionado)

### 4. Out of scope

- Must not ser a fonte de verdade do vínculo CPF→CNPJ — a autorização vem do gov.br/Novo PAT; esta capacidade consome e apresenta o vínculo validado
- Must not tratar a comparação/seleção de propostas em si (é E02) — aqui só se estabelece o contexto de empresa

### 5. Acceptance

Uma representante autorizada a operar três empresas entra no portal e vê exatamente esses três cards (com Matriz/Filial e chip 'Ativa'); busca por Razão Social, seleciona uma Filial, confirma em Continuar e passa a ver as cotações daquela Filial. Pelo menu superior troca para outra empresa e o portal recarrega o contexto sem pedir novo login.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009

### 7. Grounding

- **Source artifact:** wireframe: Protótipo Figma telas 2 e 3 — 'Selecionar/Empresa selecionada', vínculos válidos, Matriz/Filial, troca pelo menu superior _(.discovery-context.md)_
- **Source artifact:** decision: 0004 — beneficiária opera Opportunity/Quote no portal (driver de licença) _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] A autorização de representante (procuração) vem do próprio gov.br (procuração eletrônica/e-CNPJ/Novo PAT) ou o marketplace mantém seu próprio modelo de vínculo pessoa-empresa? Quem é a fonte de verdade e como se revoga? (Resolver: MTE/Dataprev (Ramon Pontes / Jair Bogo))
- [ ] Regra de Matriz/Filial: uma procuração no CNPJ raiz autoriza todas as filiais, ou o vínculo é por estabelecimento (CNPJ completo)? Como isso mapeia para os cards exibidos? (Resolver: MTE/Dataprev)
- [ ] Versão da licença Experience Cloud da beneficiária (Partner Community vs Customer Community Plus) — Customer Community Plus não expõe Opportunity/Quote nativamente; a operação desses objetos no portal empurra para Partner Community, a requalificar contra volume/padrão de acesso. (Resolver: Arquitetura Salesforce + Dataprev (G0103/G0108))

---

## INT-016 — Validação de vínculo CPF↔CNPJ via Geride

epic `E01` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

A lista de empresas que a representante pode operar reflete os vínculos válidos e ativos apurados na fonte oficial em tempo de acesso — vínculo revogado ou empresa irregular não aparece nem é operável.

### 2. Build target

- Chamada de validação (via MuleSoft) ao Geride/gov.br que retorna os vínculos válidos CPF→CNPJ da pessoa autenticada, com situação (ativo/revogado) e tipo (Matriz/Filial)
- Resolução em runtime dos vínculos para o contexto de portal, sem persistir CPF no Salesforce (referência tokenizada)
- Filtro que expõe à tela de seleção somente vínculos válidos e ativos; tratamento de exceção quando a pessoa não tem nenhum vínculo válido (mensagem/fluxo de saída)

### 3. Guardrails

- Must not confiar em cache local de vínculo como fonte de verdade — a autorização é apurada contra a fonte oficial no acesso
- Must not expor vínculo revogado, suspenso ou de empresa irregular no Novo PAT
- Must not logar/persistir CPF na chamada de validação nem no registro do vínculo (aderente à residência híbrida e à trilha de auditoria sem CPF)

### 4. Out of scope

- Must not construir o Geride nem o cadastro de procuração — esta capacidade apenas consome o contrato de API de validação
- Must not orquestrar o split ou qualquer fluxo financeiro (E03/E05)

### 5. Acceptance

Uma representante que teve a procuração de uma das empresas revogada no gov.br entra no portal; ao carregar a seleção, a validação via Geride retorna apenas os vínculos ainda ativos e a empresa revogada não aparece na lista — sem que qualquer CPF tenha sido gravado no Salesforce.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009
- **External:** gov.br/Geride — Contrato de API (Swagger) de validação de vínculo/situação e autenticação de acesso ao Geride _(owner: Dataprev (Geride) / gov.br)_

### 7. Grounding

- **Source artifact:** decision: 0001 — residência híbrida; resolução tokenizada em runtime _(decisions/0001-residencia-dados-hibrida.md)_
- **Source artifact:** wireframe: Protótipo Figma tela 2 — aviso 'apenas empresas com vínculos válidos' _(.discovery-context.md)_

### Open questions

- [ ] Existe contrato de API (Swagger) do Geride para validação de vínculo, e qual o padrão de autenticação (OAuth2/mTLS/certificado ICP-Brasil)? Cronograma de disponibilização mock→real. (Resolver: Dataprev (Jair Bogo) — registro de dependências de API)

---

## INT-017 — Controle de acesso e navegação do portal por papel

epic `E01` · priority _(unassigned)_ · confidence _Assumed_ · surface `security`

### 1. Outcome

Cada tipo de usuário vê e opera somente o que seu papel permite — a representante da beneficiária navega cotação/folha da(s) empresa(s) que representa; o estabelecimento vê seu próprio escopo; o administrador do MTE tem sua visão de gestão — sem cruzar dados entre empresas.

### 2. Build target

- Permission sets por papel (beneficiária, estabelecimento, administrador MTE) governando objetos, campos e componentes visíveis
- Menu lateral do portal renderizado conforme o papel (ex.: beneficiária vê Início, Cotação, Folha de Pagamento, Empresas Credenciadas, Facilitadores, Sair)
- Modelo de sharing que isola registros ao contexto de empresa selecionada — a beneficiária só alcança dados dos CNPJs que representa
- Base de identidade e acesso sobre a qual E02/E03/E04 são renderizados (fundação, não as telas de negócio em si)

### 3. Guardrails

- Must not permitir que uma beneficiária veja dados de outra beneficiária ou de qualquer facilitadora
- Must not conceder acesso a objetos/telas fora do permission set do papel (princípio do menor privilégio)
- Must not depender de segurança apenas na camada de UI — o isolamento é imposto por sharing/permission set, não só por ocultar itens de menu

### 4. Out of scope

- Must not implementar Apex managed sharing para ocultar Quotes entre facilitadoras concorrentes — a equidade é por construção (facilitadora é API-only, sem UI; ADR 0004)
- Must not construir as telas de negócio de cotação/folha/credenciamento — são E02/E03/E04; aqui só o arcabouço de papel/acesso

### 5. Acceptance

Uma representante de beneficiária entra e vê o menu e os registros apenas das empresas que representa; ao tentar acessar por URL um registro de outra empresa, o sharing nega. Um administrador do MTE, com outro permission set, vê sua visão de gestão e não as telas operacionais da beneficiária.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009

### 7. Grounding

- **Source artifact:** wireframe: Protótipo Figma — menu lateral da Beneficiária (Início/Registros/Empresas Credenciadas/Cotação/Folha/Facilitadores/Sair) _(.discovery-context.md)_
- **Source artifact:** decision: 0004 — equidade por construção; facilitadora API-only sem licença de portal _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] O estabelecimento acessa o portal (e como se autentica — identidade PJ distinta?) ou é apenas objeto de credenciamento operado por outros papéis? Define se há um terceiro perfil de portal (G0402). (Resolver: MTE/Dataprev)
- [ ] O administrador do MTE opera dentro do Experience Cloud (portal) ou na org interna (não é usuário de portal)? Define se seu acesso consome licença de portal ou de plataforma. (Resolver: Arquitetura Salesforce + Dataprev)

---

## INT-018 — Sessão e logout federado gov.br

epic `E01` · priority _(unassigned)_ · confidence _Assumed_ · surface `experience-cloud`

### 1. Outcome

A sessão do portal tem começo e fim claros: ao sair, a representante encerra a sessão do Experience Cloud e o vínculo com a identidade gov.br, sem deixar contexto de empresa aberto para um próximo acesso indevido.

### 2. Build target

- Ação 'Sair' no portal que encerra a sessão do Experience Cloud e limpa o contexto de empresa selecionada
- Comportamento de logout coerente com o provedor gov.br (encerramento/expiração da sessão federada) e destino pós-logout definido (landing pública)
- Política de timeout/expiração de sessão do portal apropriada para acesso a dado sensível

### 3. Guardrails

- Must not manter o contexto de empresa selecionada ativo após o logout ou a expiração da sessão
- Must not deixar a sessão do portal viva de forma indefinida — timeout coerente com a sensibilidade dos dados

### 4. Out of scope

- Must not gerir a sessão do provedor gov.br em si — apenas coordenar o encerramento no lado do Relying Party
- Must not implementar trilha de auditoria de acesso a CPF (é E08/residência) — aqui só o ciclo de vida da sessão

### 5. Acceptance

Uma representante clica em 'Sair'; a sessão do portal é encerrada, o contexto de empresa é limpo e ela é levada à landing pública. Ao voltar, precisa autenticar novamente pelo gov.br antes de reselecionar uma empresa.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009

### 7. Grounding

- **Source artifact:** wireframe: Protótipo Figma — item 'Sair' no menu lateral da Beneficiária _(.discovery-context.md)_

### Open questions

- [ ] O logout deve encerrar também a sessão gov.br (single logout) ou apenas a sessão do portal? Qual o destino pós-logout e a política de timeout exigida para dado sensível? (Resolver: MTE/Dataprev + Arquitetura Salesforce)

