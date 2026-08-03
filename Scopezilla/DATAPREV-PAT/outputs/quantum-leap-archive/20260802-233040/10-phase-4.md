# Phase 4 — Homologação, Carga Mínima, Adoção & Go-live PROD (9/nov – 15/nov · Sem. 13) (DATAPREV-PAT)

> **Phase orchestration — what's in/out of phase, dependencies, starting state.** Read this first to orient. Per-capability buildable specs live in `11-intents-4.md` (when present) — that's what you actually build against, one intent at a time.
> Phase duration: **1 weeks (per user commitment)**.

## Intent

- **For:** A equipe de go-live e hypercare, as beneficiárias e facilitadoras (adoção/capacitação), e o Novo PAT/MTE como system-of-record das cargas iniciais.
- **Outcome:** Fechar a homologação (UAT) aberta no início de novembro e virar para PRODUÇÃO em 15/nov/2026. Popular a plataforma com a carga inicial MÍNIMA necessária ao go-live (E07 — beneficiárias, facilitadoras, estabelecimentos a partir do Novo PAT, que permanece system-of-record) e conduzir a adoção enxuta (E09 — capacitação e materiais essenciais, com o pico da comunicação já iniciado na Etapa 1).
- **Measured by:** Homologação (UAT) concluída sobre as jornadas entregues (portal, marketplace, credenciamento, financeiro); cadastros mínimos carregados com dedup e reconciliação (INT-046, INT-047, INT-048); facilitadoras e beneficiárias com capacitação essencial (INT-049); GO-LIVE PROD 15/nov estabilizado com hypercare ativo.
- **Must not:** Não carregar dado sensível/CPF na org — só referências não-sensíveis (ADR 0001, INT-046). Não recriar registros em recarga — a carga é idempotente por external ID (INT-046). Não fazer batimento pesado de dedup na Fase 1 — entrar marcado, sem batimento profundo (INT-047, temperado pelo discovery). Não expandir E09 além de adoção enxuta (change management, não build pesado).

## Pre-decided (do not re-litigate)
- **Novo PAT permanece system-of-record** dos cadastros; a plataforma recebe a carga mínima ao go-live (roadmap, decision_log).
- **Carga idempotente**: Bulk API 2.0 + upsert por external ID (INT-046 — dimensionado para o pico ~28/s / 1M registros analisado em 2026-07-31).
- **Dedup leve na Fase 1**: entrar marcado por chave não-sensível, sem batimento profundo (INT-047).
- **E09 é transversal e enxuto**: a comunicação começou na Etapa 1 e culmina aqui; capacitação e materiais essenciais, não uma frente de build.
- **Data fixa imóvel**: go-live PROD 15/nov/2026 (ADR de modo data-fixa; decision_log).

## Starting state (from Financeiro — Folha, Motor de Split & Conciliação (19/out – 8/nov · Sem. 10-12))

You should find these already deployed in the sandbox:
- **Financeiro — Folha, Motor de Split & Conciliação (19/out – 8/nov · Sem. 10-12) outcome:** MARCO DE ENTREGA DE JORNADA (UAT/homologação): upload de folha → validação de layout/integridade → crítica → download pela facilitadora → 'processado'+valor via API → gateway emite boleto registrado → beneficiária vê o boleto no portal → conciliação por lotes incrementais via MuleSoft → motor calcula o split → ordens de transferência entregues ao gateway com trilha e idempotência; UI simplificada a status consolidado 'crédito concedido'. Capacidade principal: fluxo financeiro folha→boleto→conciliação→split completo. HOMOLOGAÇÃO INÍCIO NOVEMBRO abre ao fim desta fase.

## Plan-mode questions (resolve before switching to Build mode)
- ⚠ **VIABILIDADE DA DATA FIXA — SINALIZAR**: 13 semanas para um build XL regulado sobre 3 pré-requisitos externos de lead-time (org greenfield, MuleSoft on-premise, gateway) é cronograma agressivo; a janela de 1 semana entre o fim do build (8/nov), a homologação e o PROD (15/nov) é o ponto mais frágil. Se algo escorregar, o de-escopo (E03 primeiro) é o trilho.
- Qual o conjunto mínimo de cadastros para o go-live e sua fonte exata no Novo PAT (INT-046)?
- Chave de dedup não-sensível acordada (INT-047) — qual campo, dado que CPF não persiste?
- Critérios de aceite da reconciliação pós-carga (INT-048): tolerância de divergência aceitável.

## Build-mode questions (ask only if the situation arises)
- Jobs Bulk API 2.0: tamanho de lote, janela de execução, ordem de carga entre objetos (INT-046).
- Relatório de reconciliação pós-carga: formato e destinatário (INT-048).
- Conteúdo e canal dos materiais de adoção essenciais (INT-049).

## Epics in scope for this phase

The phase brief is authoritative. Epics below are listed for cross-reference only — when an automation cites `(E04)`, this is what it refers to. For deeper epic narrative, see `90-epics-context.md`.

- **E07: Migração & Carga Inicial de Cadastros** — Carga inicial de cadastros de beneficiárias, facilitadoras e estabelecimentos a partir do Novo PAT / bases MTE. Novo PAT permanece system-of-record (sem migração massiva); foco em qualidade, deduplicação e referências não-sensíveis (ADR 0001).
- **E09: Gestão de Mudança & Adoção** — Change management e plano de adoção para o alcance do programa (600-700 facilitadoras + centenas de milhares de beneficiárias): comunicação, capacitação, materiais de apoio e acompanhamento de adoção. Entrega Salesforce PS. Escopo detalhado e fronteira com a Dataprev a confirmar.

## Build targets — orchestration summary

These sections orient the build agent on the shape of the phase. Per-capability buildable detail (Outcome, Build target, Guardrails, Out of scope, Acceptance, Open questions) lives in `11-intents-4.md` per intent. When a section below cites `INT-NNN`, look up the intent there.

### Data model
Deduplicação na carga por chave não-sensível (INT-047) — dado que CPF não persiste, a chave de unicidade é um external ID não-sensível vindo do Novo PAT. Sem novos objetos de negócio nesta fase; a carga popula os objetos fundacionais das Etapas 1–3.

### Automation
Carga inicial idempotente de referências não-sensíveis via Bulk API 2.0 com upsert por external ID (INT-046 — a arquitetura assíncrona que evita o teto de Apex concorrente) e validação de qualidade + reconciliação pós-carga (INT-048). O detalhe vive nesses intents.

### UI & navigation
Painel de adoção do portal da beneficiária (INT-049) — Lightning Record Page/monitoramento leve para a adoção enxuta. Sem novas jornadas de negócio nesta fase.

### Security & access
Herda a residência híbrida (ADR 0001): a carga traz apenas referências não-sensíveis; nenhum CPF entra na org. Acesso por papel e trilha de auditoria já estabelecidos na Etapa 1.

### Reports & dashboards
[TODO: phase brief body not yet generated — populate via the `quantum-leap` skill]

### Sample data
_(optional — load only on user request)_

### Data sources

Novo PAT/MTE como origem da carga inicial via MuleSoft (INT-046, camada E05 da Etapa 1). Novo PAT permanece system-of-record.

## Acceptance — user-outcome checks (phase-level)

Phase-level user-outcome claims a stakeholder would walk through to feel "Phase 4 is done." Run them in conversation with the user; mark `- [x]` only when the user agrees. Per-intent acceptance walkthroughs live in `11-intents-4.md`.

A homologação percorre as jornadas entregues (portal gov.br, leilão reverso, credenciamento, financeiro) e é aprovada; a carga mínima do Novo PAT popula a plataforma sem duplicar registros nem trazer CPF; beneficiárias e facilitadoras recebem a capacitação essencial; em 15/nov a plataforma entra em PRODUÇÃO com hypercare ativo e um painel de adoção acompanhando os primeiros acessos.

## Acceptance — metadata-shaped checks (phase-level)

Phase-level metadata-shaped checks — queries the build agent runs against the target org without human help. Run via the Metadata skill (describe / tooling / SOQL). Per-intent acceptance is in `11-intents-4.md`.

Verifica-se: (a) a carga é idempotente — recarregar não cria duplicatas (upsert por external ID, INT-046); (b) registros duplicados entram marcados por chave não-sensível, sem batimento pesado (INT-047); (c) a reconciliação pós-carga confere contagens e sinaliza divergências dentro da tolerância acordada (INT-048); (d) nenhum CPF/dado sensível foi carregado na org (ADR 0001); (e) o painel de adoção reflete os acessos ao portal (INT-049); (f) o go-live PROD 15/nov está estável com hypercare.

## Out of scope for Phase 4

If you find yourself needing to build any of these, stop and surface it — it belongs to a later phase or is explicitly excluded.

_(none surfaced in gaps.json — confirm with user during plan-mode review)_

## Dependencies and risks

**Dependencies:** Etapa 1 (E05 para extração/carga). E07 depende de E05. E09 é transversal — sua comunicação começa na Etapa 1 e culmina aqui. A homologação depende do encerramento das jornadas da Etapa 2 e 3.

**Risks:** ⚠ VIABILIDADE DA DATA FIXA — SINALIZAR: 13 semanas para um build XL regulado (financeiro com split, conciliação e emissão de boleto) sobre 3 pré-requisitos externos de lead-time (org greenfield, MuleSoft on-premise, gateway) é um cronograma AGRESSIVO com margem mínima. A janela de estabilização de 1 semana entre o fim do build (8/nov), a homologação e o PROD (15/nov) é o ponto mais frágil: se qualquer pré-requisito da Etapa 0 atrasar, ou a homologação achar defeito no financeiro, a data de 15/nov não é alcançável com esforço adicional — nesse caso o de-escopo (E03 financeiro é o primeiro candidato, adiando parte do split/conciliação para pós-go-live) é o único trilho para preservar a data. Volume de carga desconhecido (G0701, ~450k) pode estourar a janela; resistência das facilitadoras (perda de margem no modelo transparente). Adoção completa e carga massiva ficam pós-go-live (buffer).

## Story citations covered in this phase

- (US-0701) Como Sistema de integração, quero extrair os cadastros de beneficiárias, facilitadoras e estabelecimentos das bases de origem (Novo PAT / bases MTE) via API MuleSoft, para disponibilizar os dados brutos para a carga inicial sem replicar o Novo PAT como system-of-record.
- (US-0702) Como Data Steward, quero definir e manter o mapeamento de-para entre os campos das bases de origem e os objetos/atributos da plataforma, para garantir que cada cadastro seja carregado no destino correto respeitando a fronteira de dados não-sensíveis.
- (US-0703) Como Admin da plataforma, quero executar a carga inicial de beneficiárias a partir da área de staging, para que as empresas participantes existam na plataforma prontas para publicar cotações no go-live de 15/nov.
- (US-0704) Como Admin da plataforma, quero executar a carga inicial das facilitadoras (600-700 fornecedores) a partir da área de staging, para que possam receber e responder cotações via API desde o go-live.
- (US-0705) Como Admin da plataforma, quero executar a carga inicial de estabelecimentos credenciados a partir da área de staging, para que restaurantes e mercados estejam disponíveis na plataforma no go-live.
- (US-0706) Como Data Steward, quero identificar e resolver registros duplicados de beneficiárias, facilitadoras e estabelecimentos durante a carga, para evitar cadastros redundantes que corromperiam cotações e folhas.
- (US-0707) Como Data Steward, quero aplicar regras de qualidade e validação sobre os dados em staging antes da carga, para garantir que apenas cadastros consistentes e completos entrem na plataforma.
- (US-0708) Como Sistema, quero carregar apenas referências não-sensíveis tokenizadas (sem persistir CPF ou dados sensíveis do trabalhador na plataforma), para cumprir a diretriz de residência de dados híbrida da Dataprev/LGPD.
- (US-0709) Como Sistema, quero reconciliar periodicamente os cadastros carregados com o Novo PAT (system-of-record), para manter as referências da plataforma alinhadas à fonte oficial sem migração massiva.
- (US-0710) Como Admin da plataforma, quero um relatório consolidado de carga e erros ao final de cada execução, para comprovar a qualidade da migração inicial e priorizar o saneamento antes do go-live.
- (US-0901) Como Gestor de mudança, quero conduzir uma avaliação de impacto de mudança por público (beneficiárias, facilitadoras, estabelecimentos e equipe MTE), para dimensionar esforço de comunicação e capacitação e antecipar focos de resistência antes do go-live de 15/nov/2026.
- (US-0902) Como Gestor de mudança, quero um plano de comunicação segmentado por público (beneficiárias, facilitadoras, estabelecimentos e equipe MTE), para que cada audiência receba a mensagem certa nos canais certos ao longo da transição para o marketplace.
- (US-0903) Como Beneficiária (empresa contratante), quero materiais de capacitação e treinamento sobre como publicar cotações, comparar propostas e enviar folha no portal, para operar o marketplace com autonomia desde o primeiro uso.
- (US-0904) Como Facilitadora (emissora de VA/VR), quero um pacote de onboarding técnico para integração via API (envio de propostas, processamento de folha, split/repasse), para conectar meus sistemas ao marketplace dentro da janela de homologação.
- (US-0905) Como Estabelecimento (rede credenciada), quero guias e FAQ sobre credenciamento unificado via gov.br e sobre o novo modelo de repasse (até 15 dias, taxa até 3,6%), para entender o que muda para o meu negócio no marketplace.
- (US-0906) Como Beneficiária, quero guias e FAQ contextuais dentro do portal (ajuda em tela, 'Precisa de ajuda?'), para resolver dúvidas sem abrir chamado enquanto navego pelo marketplace.
- (US-0907) Como Gestor de mudança, quero definir e medir métricas e KPIs de adoção do marketplace, para acompanhar o uso real por público e agir onde a adoção estiver abaixo do esperado.
- (US-0908) Como Gestor de mudança, quero estabelecer uma rede de multiplicadores (facilitadores/champions) por público, para escalar a adoção junto a 600-700 facilitadoras e centenas de milhares de beneficiárias sem depender apenas de suporte central.
- (US-0909) Como Equipe MTE, quero um plano de suporte à transição pós-go-live (hypercare) com canais, SLA e triagem de dúvidas por público, para sustentar a adoção nas primeiras semanas após 15/nov/2026.

## Recipe boundary

When this phase is accepted, ask the user: *"Save this run as a recipe so we can repeat for Phase 5?"* The recipe should capture: the data-model decisions made above, the naming patterns confirmed in `03-glossary-and-naming.md`, and any Build-mode question resolutions that emerged.
