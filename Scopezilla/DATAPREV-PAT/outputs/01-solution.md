# Solução — DATAPREV-PAT (Marketplace Digital do PAT)

> **Nível ROM, sobre premissas.** Este documento desenha a arquitetura da solução em nível de proposta, sobre cinco premissas de arquitetura já formalizadas — residência de dados híbrida (ADR 0001), **instância dedicada e apartada (ADR 0002)**, **fronteira CRM-não-transacional / motor de regras de split (ADR 0003)**, **plataforma sobre Sales Cloud reusando objetos nativos Opportunity/Quote (ADR 0004)** e **ambiente 100% greenfield + MuleSoft on-premise para soberania de dados (ADR 0005)** — e três decisões ainda em aberto (fronteira campo-a-campo da residência, identidade Experience Cloud × CPF, contratos de API), além da seleção do provedor do gateway. Essas decisões, o provisionamento da org greenfield, a prontidão da infra MuleSoft on-premise e a contratação do gateway se resolvem numa **Fase 0** antes do compromisso final de escopo. As premissas ADR 0004/0005 foram **assumidas pela equipe em 31/jul/2026 e ainda a validar com o cliente** — carregam etiqueta Assumed. Cada decisão load-bearing carrega sua etiqueta de origem — `[KB: …]`, `[extends: …]` ou `[assumption: …]`.

---

## Fundações de Arquitetura (transversais)

Decisões horizontais que nenhuma épica individual possui — a base sobre a qual o mapa por processo, adiante, se apoia.

### Estratégia de org — instância dedicada e apartada (ADR 0002)

Os quatro domínios do programa (marketplace de cotação, credenciamento, financeiro/split e atendimento) vivem numa **única org**, mas essa org é **dedicada e apartada** das demais orgs de clientes da Dataprev. O isolamento não é preferência — é **forçado** por segurança e sensibilidade financeira, pela volumetria (~800 mil estabelecimentos, ~450 mil beneficiárias — a ratificar), pela auditabilidade perante TCU/CGU/ANPD e pela administração da instância pelo próprio MTE (que não pode enxergar "a cozinha" dos demais clientes). O provisionamento tem lead-time externo e é **pré-requisito de arranque (Fase 0)**. A separação entre domínios internos segue por objeto, perfil e modelo de compartilhamento. `[decisions/0002-instancia-dedicada-mte-pat]` — premissa ainda **verbal, a ratificar por escrito**.

### Plataforma sobre Sales Cloud, reusando objetos nativos (ADR 0004)

A plataforma é construída sobre **Sales Cloud**, mapeando o leilão reverso em **objetos nativos** em vez de objetos 100% custom, em prol do curto tempo de implantação sob a data fixa. **Opportunity (nativo)** = a demanda que a beneficiária cadastra (nº de trabalhadores, valor, vigência, distribuição por UF, recursos obrigatórios) — reusa estágios, ownership, activity history e relatórios nativos. **Quote (nativo)** = a resposta da facilitadora ao leilão reverso, recebida **via API** (MuleSoft), uma por facilitadora, associada à Opportunity. A facilitadora é **API-only** (sem tela, sem assento de portal): descobre as demandas abertas na vigência consultando um **endpoint de consulta (pull via API)** no MVP — **não há push ativo** (a notificação ativa é roadmap futuro, com o canal a definir — o que decide se posicionamos ou não Marketing Cloud). A **equidade é por construção**: como a facilitadora não tem tela, não enxerga a proposta concorrente — **sem Apex managed sharing**. A camada custom fica reservada ao que os nativos não entregam: a tela "Comparar Propostas" (LWC) para a beneficiária, a **trava de seleção até o fechamento da janela de vigência** (a beneficiária vê as cotações conforme chegam, mas só seleciona quando a janela fecha — não é seleção cega) e a transição seleção→contrato. `[decisions/0004-sales-cloud-objetos-nativos]` — premissa assumida em 31/jul, **a validar com o cliente** (Assumed). A complexidade migra de "construir do zero" para "adaptar o nativo sell-side ao padrão comprador→N-vendedores".

### Greenfield + MuleSoft on-premise — soberania e isolamento (ADR 0005)

Ambiente **100% greenfield**: a instância Salesforce dedicada é provisionada do zero, sem reaproveitar nenhuma org, metadado ou administração de outros ambientes Dataprev — isolamento por construção. O **MuleSoft roda on-premise** (na infraestrutura Dataprev/gov, não em CloudHub): é o ponto de de-tokenização do CPF (ADR 0001) e o trilho de soberania — o dado sensível não sai do perímetro soberano. A prontidão da infra (org greenfield provisionada + MuleSoft on-premise instalado) é **pré-requisito de marco na Fase 0**, com lead-time externo. `[decisions/0005-greenfield-mulesoft-onpremise]` — **resolve G0504** (hospedagem MuleSoft = on-premise), premissa assumida em 31/jul, a validar (Assumed).

### Seleção de produtos e licenciamento

| Produto | Papel |
|---|---|
| **Sales Cloud** | Plataforma de gestão das jornadas — objetos **nativos Opportunity (demanda) + Quote (resposta via API)** para o leilão reverso (ADR 0004), automação, motor de regras |
| Experience Cloud — **Partner Community** | Portal externo — expõe objetos nativos do Sales (Opportunity/Quote) a **beneficiárias e estabelecimentos** (a facilitadora é **API-only**, sem assento de portal); procuração digital (ADR 0004 — Partner Community, não Customer Community Plus) |
| MuleSoft Anypoint — **on-premise** | Camada de integração API-led para todos os sistemas externos, o **gateway** e as ~600-700 facilitadoras; roda na infra soberana Dataprev (ADR 0005) |
| Agentforce | Atendimento inteligente (E06 — **fora do MVP**, candidato a de-escopo) |
| Gateway / banco custódia | **Fora do escopo Salesforce** — contratado pelo cliente; executa transações bancárias e custodia (ver ADR 0003) |

`[KB: salesforce-revenue-cloud-marketplace-arch.md:41-45]` — arquitetura Experience Cloud + MuleSoft confirmada contra fonte primária Salesforce; Revenue Cloud fora desta rodada (é sell-side, sem RFQ/leilão reverso nativo).

**Licenciamento.** Licenças internas (Sales/Platform) para a operação MTE; **Experience Cloud external — Partner Community** (não Customer Community Plus) para **beneficiárias e estabelecimentos**, porque o portal precisa **expor objetos nativos do Sales** (Opportunity/Quote), o que a Partner Community habilita e a Customer Community Plus não cobre adequadamente (ADR 0004). **As ~600-700 facilitadoras são API-only — integrações via MuleSoft (E05), não assentos de portal — e NÃO consomem licença de Experience Cloud** (correção de licenciamento do ADR 0004): o driver de licença de portal é a beneficiária, não a facilitadora. O modelo (login-based vs. member-based) e a volumetria da beneficiária precisam ser requalificados contra a versão Partner Community — custo diferente da Customer Community Plus. `[assumption: modelo de licença Partner Community depende do volume de usuários ativos da beneficiária e da requalificação contra a nova versão — G0103/G0108]`

### Modelo de compartilhamento (OWD / sharing)

OWD **Private** em todos os objetos transacionais (Opportunity, Quote, folha, contrato, split): a beneficiária vê apenas seus próprios registros. A **equidade do leilão é por construção**: a facilitadora é **API-only** (sem tela) e acessa apenas o escopo da própria Quote/contrato via API — não enxerga as Quotes concorrentes, **dispensando Apex managed sharing** para ocultar propostas entre concorrentes. A beneficiária, dona da Opportunity, vê as Quotes recebidas na sua demanda. Perfis guest/external do portal Partner Community (beneficiária/estabelecimento) ficam travados no mínimo necessário. `[extends: padrão Experience Cloud Partner Community external-user OWD Private + sharing sets, aplicado ao modelo comprador→N-vendedores sobre Opportunity/Quote nativos — facilitadora API-only, equidade por construção]`

### DevOps e governança

Desenvolvimento source-driven (Salesforce CLI + Git) com pipeline Dev → QA → UAT → Produção; a equipe multi-perfil e a janela fixa comprimida justificam pipeline versionado em vez de Change Sets. Full sandbox para o UAT com dado representativo. `[assumption: padrão PS para equipe multi-perfil + go-live regulado; validar toolchain e política de deploy da Dataprev — G0809]`

### Segurança e residência de dados — a fundação (ADR 0001)

CPF e dados sensíveis **não persistem** na nuvem Salesforce. A org guarda **referências tokenizadas**, resolvidas em runtime via MuleSoft contra a infraestrutura Dataprev. É premissa transversal a E01, E02, E03 e E06, e o desenho concreto vive em E08. Combinada com o isolamento da instância dedicada (ADR 0002), forma a espinha de segurança/auditoria do programa. Diagrama de fluxo de dados sob LGPD Art. 11 e trilha de auditoria para TCU/CGU/ANPD acompanham.

**Três decisões de arquitetura em aberto que esta fundação carrega até a Fase 0:**
- `[assumption: G0801 — fronteira campo-a-campo exata da residência (o que é token vs. o que pode persistir) a ratificar com Jair Bogo; governa o data model de E01/E02/E03/E06]`
- `[assumption: G0106 — Experience Cloud Partner Community exige User/Contact com identidade; conciliar com "CPF não persiste" via Contact por referência tokenizada + resolução runtime]`
- `[assumption: G0501 — sem Swagger/contrato de API de nenhum sistema externo (Novo PAT não tem API hoje); integração é mock-first até os contratos existirem — risco #1, caminho crítico]`

*(G0504 — hospedagem MuleSoft — **resolvido pela ADR 0005**: on-premise na infra soberana Dataprev; é onde ocorre a de-tokenização do CPF.)*

### Fronteira CRM × financeiro — o Salesforce é o motor de regras, não o banco (ADR 0003)

O Salesforce **calcula e aplica as regras de split** (rateio governo/facilitadora/estabelecimento) sob o teto de administração (MDR) de 3,6% e o repasse em até 15 dias do Decreto 12.712/2025, **emite a boletagem já com o split aplicado**, orquestra e **concilia por casamento**, e **recebe** as movimentações bancárias. Ele **não transaciona nem custodia dinheiro**: a execução das transações bancárias e a custódia ficam no **gateway PCI**, contratado pelo cliente, que recebe as boletagens com split do Salesforce, executa e devolve as movimentações para o CRM conciliar. `[decisions/0003-fronteira-crm-nao-transacional]` — é o que dimensiona E03 como XL e coloca a seleção/contratação do gateway PCI como pré-requisito de Fase 0 (G0309).

---

## Solução por Processo de Negócio

Ordem por fluxo de criação de valor: identidade → cotação → credenciamento → financeiro/split → atendimento → (integração, migração, segurança, mudança — transversais ao final).

### E01 — Portal & Identidade gov.br

**Contexto de negócio.** A beneficiária precisa entrar no marketplace com a identidade gov.br já existente e agir em nome da empresa, sem um cadastro paralelo. É a porta de entrada de todo o programa.

**Abordagem de solução.** Experience Cloud **Partner Community** (ADR 0004 — para expor objetos nativos do Sales aos participantes externos) com login gov.br via OpenID Connect, procuração digital e fluxo "representar empresa". É a base de identidade e navegação sobre a qual E02, E03 e E04 renderizam.

**Arquitetura de suporte.** Autenticação federada gov.br (OIDC) via Named Credentials/Auth Provider, com a resolução de identidade sensível intermediada por MuleSoft (ADR 0001 — o Contact carrega referência tokenizada, não o CPF). `[assumption: Experience Cloud + gov.br OIDC é padrão de produto, mas o conector nativo não cobre gov.br diretamente — validar o fluxo específico e a procuração digital — G0101/G0102]`

### E02 — Marketplace de Cotação e Contratação

**Contexto de negócio.** O coração da reforma: a beneficiária publica uma demanda (nº de trabalhadores, valor, vigência, distribuição por UF, recursos obrigatórios), N facilitadoras enviam propostas **via API** (a facilitadora não tem tela, logo não vê as concorrentes — equidade por construção); a beneficiária compara lado a lado conforme as cotações chegam, mas **só seleciona quando a janela de vigência fecha** (seleção travada, não cega), e a seleção manual vira contrato. É o "leilão reverso". Antecede a demanda um **termo de aceite** (a empresa informa a contagem de trabalhadores por faixa salarial por CNPJ, com tratamento de matriz/filial, gerando um Novo PAT via INIS PJ). Beneficiárias **PAT e não-PAT** seguem regras de cálculo distintas. O contrato **não usa CLM no MVP** — é um PDF imutável versionado.

**Abordagem de solução (ADR 0004).** Sobre **Sales Cloud com objetos nativos**: **Opportunity** = a demanda da beneficiária; **Quote** = a resposta de cada facilitadora, recebida **via API** (MuleSoft). A facilitadora é **API-only** e descobre as demandas abertas por **endpoint de consulta (pull)** no MVP — sem push ativo (a notificação ativa é roadmap futuro, canal a definir). A comparação lado a lado e a seleção manual operam sobre as Quotes. A **equidade é por construção** — a facilitadora não tem tela, logo não vê as concorrentes, **sem Apex managed sharing**. A camada custom cobre o que o nativo não entrega: a LWC da tela "Comparar Propostas" (para a beneficiária), a **trava de seleção até o fechamento da vigência**, a transição seleção→contrato e o passo de termo de aceite (faixa salarial por CNPJ + matriz/filial → Novo PAT via INIS PJ). Contrato **sem CLM** — PDF imutável versionado.

**Arquitetura de suporte.** Modelo comprador→N-vendedores sobre Opportunity/Quote nativos com **equidade por construção**: a facilitadora é API-only (sem tela, sem assento de portal) e interage apenas com o escopo da própria Quote via API — não enxerga as concorrentes, **sem necessidade de Apex managed sharing**; a beneficiária (dona da Opportunity) vê as Quotes recebidas conforme chegam. Recepção das propostas das facilitadoras e exposição do endpoint de consulta de demandas abertas via API (MuleSoft, E05). Adaptar objetos nativos sell-side ao padrão comprador→N-vendedores é o esforço principal (ADR 0004). `[decisions/0004-sales-cloud-objetos-nativos]` `[KB: salesforce-revenue-cloud-marketplace-arch.md:19-25]` — leilão reverso não é capability nativa; a equidade e a comparação são custom sobre os nativos. `[assumption: regras de seleção/desempate e conformidade com a Lei 14.133/2021 a definir — G0202/G0203/G0204]` `[assumption: termo de aceite (faixa salarial por CNPJ + matriz/filial → Novo PAT via INIS PJ) e regras PAT vs. não-PAT a detalhar]` `[assumption: contrato sem CLM no MVP — PDF imutável versionado]` **Enriquecimento/perfil por Data Cloud é adição Assumed e fica FORA do MVP** (buffer de cronograma — o leilão funciona sem ele; G0209).

### E04 — Credenciamento de Estabelecimentos

**Contexto de negócio.** Estabelecimentos (restaurantes, mercados) hoje se credenciam facilitadora a facilitadora, com duplicidade e fricção. O programa quer um cadastro unificado via gov.br, mantendo o papel legal das facilitadoras de aprovar e descredenciar.

**Abordagem de solução.** Objeto de estabelecimento com identidade gov.br PJ (CNPJ), workflow de aprovação e integração de deduplicação/validação de CNPJ contra as bases das facilitadoras. Inclui **vigilância sanitária** (5000+ padrões municipais de licença — a validade como parâmetro mínimo, extração por IA com transbordo humano, fluxo de renovação + alertas de expiração) e **consulta à adquirente via API** com monitoramento de transações.

**Arquitetura de suporte.** Aprovação declarativa + integração MuleSoft para dedup/reconciliação, validação de CNPJ, consulta à adquirente e monitoramento. `[assumption: G0401 — sistema-of-record do credenciamento (registro unificado vs. papel legal da facilitadora) é conflito de fonte a resolver]` `[assumption: 5000+ padrões municipais de vigilância sanitária tratados com validade como parâmetro mínimo + extração IA + transbordo humano; consulta à adquirente por API]`

### E03 — Motor de Regras de Split & Conciliação  *(XL)*

**Contexto de negócio.** A empresa faz upload da folha; o programa precisa validar o arquivo, ratear o pagamento (governo/facilitadora/estabelecimento) sob o teto de MDR de 3,6% e repasse em até 15 dias (Decreto 12.712/2025), emitir a cobrança já com o rateio aplicado, e conciliar o que efetivamente entrou. O dinheiro em si passa por conta custódia via gateway — **não pelo Salesforce**.

**Abordagem de solução (ADR 0003) — fluxo folha→pagamento→split detalhado.** O Salesforce é o **motor de regras de split** e orquestra o fluxo: (1) upload da folha por portal/API → a plataforma **valida layout + integridade** ("não quebrada"); (2) crítica pela melhor alternativa Salesforce (Einstein/agente) — não havendo, **disponibiliza o arquivo para download da facilitadora** (as linhas da folha **não são persistidas** em objeto no MVP — roadmap futuro); (3) a facilitadora baixa a folha por contrato/mês-ano de vigência e devolve status **"processado" + valor a pagar via API**; (4) a plataforma envia o valor ao **gateway** (intermedia conta custódia), recebe **boleto registrado** + metadados/link; (5) o boleto fica disponível à beneficiária no portal; (6) a plataforma recebe as movimentações bancárias do gateway e identifica o pagamento em **lotes incrementais via agendamento MuleSoft**; (7) consulta as regras de cálculo → **calcula o repasse** à facilitadora + demais; (8) registra toda a memória de cálculo/datas/rateio/ordens de transferência e entrega, via MuleSoft, ao **gateway (executor único das transações bancárias)**. A UI consolida ao status "crédito concedido". Revenue Cloud fora desta rodada.

**Arquitetura de suporte.** Integração via MuleSoft (on-premise, ADR 0005) com o **gateway** (que executa boleto/Pix/split bancário e custodia), com **idempotência** obrigatória e trilha de conciliação por lote incremental. A execução e a custódia são do gateway (contratado pelo cliente), não do CRM. `[decisions/0003-fronteira-crm-nao-transacional]` `[KB: salesforce-revenue-cloud-marketplace-arch.md:31-35]` — motor de split custom no CRM; execução externa. `[assumption: crítica da folha depende de qual alternativa Salesforce (Einstein/agente) se confirma viável; linhas da folha não persistidas no MVP]` `[assumption: regras de split/desempate, modelo de conta custódia + provedor do gateway e a mecânica de conciliação por lote incremental a confirmar — G0301/G0304/G0309]`

### E06 — Atendimento Inteligente (Agentforce)  *(fora do MVP — de-escopo/buffer)*

**Contexto de negócio.** Atender em escala os participantes (beneficiárias, facilitadoras, estabelecimentos) — dúvidas informacionais e operações transacionais — via WhatsApp/webchat.

**Abordagem de solução.** Agente Agentforce com camada informacional (FAQ grounded) e transacional (consultas ao marketplace). O agente transacional lê dados do participante, o que colide com a residência — o desenho evita CPF no prompt do LLM, resolvendo por referência tokenizada. **Não é pré-requisito do go-live regulatório de 15/nov — é o primeiro candidato a de-escopo e não entra no MVP.**

**Arquitetura de suporte.** Grounding por referência tokenizada; guardrails de agente público governamental; canal WhatsApp/BSP adiciona risco e prazo. `[assumption: G0603 — tensão residência × agente transacional; canais e casos de uso a confirmar — G0601/G0602]`

### E05 — Integração Corporativa (MuleSoft) *(transversal)*

**Contexto de negócio.** O marketplace só funciona conectado ao ecossistema: Novo PAT, GOV.BR/Geride, CTPS Digital, eSocial, SDC, Kinis PJ/Par, validação de CNPJ, o **gateway PCI/banco custódia** e as APIs das ~600-700 facilitadoras.

**Abordagem de solução.** Camada de integração API-led (System / Process / Experience) rodando **on-premise na infra soberana Dataprev** (ADR 0005 — não CloudHub; é o ponto de de-tokenização do CPF e o trilho de soberania). Abordagem **mock-first**, obrigatória porque o **Novo PAT não tem API hoje** e nenhum Swagger/contrato dos sistemas externos foi disponibilizado. O contrato de integração com o gateway (ADR 0003) e a origem do termo de aceite (INIS PJ / Kinis PJ) são alvos declarados já na Fundação. A conciliação financeira chega por **lotes incrementais via agendamento MuleSoft**; a consulta à adquirente + monitoramento alimentam E04. Além da recepção das Quotes e da devolução de processado+valor, a camada **expõe às facilitadoras um endpoint de consulta das demandas/leilões abertos na vigência** — pull no MVP (a facilitadora consulta, sem push ativo); a **notificação ativa/push é roadmap futuro, com o canal a definir** (o que decide se posicionamos ou não Marketing Cloud — G0209/G0211).

**Arquitetura de suporte.** Padrões event-driven onde couber (Platform Events/CDC), tratamento de erro/replay, e governança de virada dos mocks para APIs reais. `[decisions/0005-greenfield-mulesoft-onpremise]` `[KB: salesforce-revenue-cloud-marketplace-arch.md:36-40]` `[assumption: G0501 — ausência total de contratos de API (Novo PAT sem API) é o risco #1 e caminho crítico; G0309 — integração do gateway]` *(G0504 resolvido — MuleSoft on-premise, ADR 0005.)*

### E07 — Migração & Carga Inicial de Cadastros *(transversal)*

**Contexto de negócio.** Popular a plataforma com beneficiárias, facilitadoras e estabelecimentos a partir do Novo PAT/bases MTE.

**Abordagem de solução.** Carga inicial **mínima** (não migração massiva — o Novo PAT permanece system-of-record), com foco em qualidade, deduplicação e referências não-sensíveis (ADR 0001). Carga massiva fica pós-go-live (buffer).

**Arquitetura de suporte.** Extração/carga via MuleSoft com regras de dedup. `[assumption: volumes, fonte e qualidade da carga a confirmar; volume desconhecido é band-widener de sizing — G0701/G0703/G0704]`

### E08 — Segurança, Residência de Dados & Conformidade *(transversal)*

**Contexto de negócio.** Todo o programa lida com CPF e dados previdenciários sensíveis, sob LGPD Art. 11 e escrutínio de TCU/CGU/ANPD, numa instância dedicada (ADR 0002).

**Abordagem de solução.** Materializa a fundação de residência sobre **três eixos de isolamento/soberania**: (1) **tokenização** — CPF e sensíveis não persistem no Salesforce (ADR 0001); (2) **instância dedicada e apartada** — nenhum admin de outro ambiente enxerga estes dados (ADR 0002); (3) **greenfield + MuleSoft on-premise** — o trilho de integração roda dentro do perímetro soberano, a de-tokenização ocorre on-premise, e nenhuma org/metadado/administração é compartilhada (ADR 0005). Acompanham diagrama de fluxo de dados sob LGPD e trilha de auditoria para acesso a dados sensíveis que não estão na org.

**Arquitetura de suporte.** Tokenização + resolução runtime via MuleSoft on-premise; isolamento da org greenfield dedicada; overlay de conformidade regulada. `[decisions/0005-greenfield-mulesoft-onpremise]` `[assumption: G0801 — fronteira exata de campos a ratificar com arquitetura Dataprev; é a decisão que governa o data model de várias épicas]`

### E09 — Gestão de Mudança & Adoção *(transversal)*

**Contexto de negócio.** A escala do programa (~600-700 facilitadoras + ~800 mil estabelecimentos e ~450 mil beneficiárias, a ratificar) e a resistência esperada das facilitadoras (que perdem margem no modelo transparente) exigem comunicação, capacitação e acompanhamento de adoção deliberados.

**Abordagem de solução.** Plano de comunicação, materiais de apoio, capacitação e métricas de adoção. Entrega Salesforce PS. Sem arquitetura técnica bespoke. No MVP, adoção enxuta; programa completo pós-go-live (buffer).

**Arquitetura de suporte.** N/A — configuração/entrega, não construção técnica. `[assumption: escopo de change/adoção e a fronteira PS vs. Dataprev/MTE a confirmar — G0901/G0906]`

---

## Nota sobre fases

O programa opera em **modo data-fixa**, planejado de trás para frente a partir de datas comprometidas: **início 17/ago/2026 → homologação início nov → go-live PRODUÇÃO 15/nov/2026** (interoperabilidade total do Decreto 12.712/2025 + entrada do financeiro em produção). A data é imóvel, e o escopo é a variável de flexão. A estratégia de execução é **definir o modelo de dados fundacional (objetos nativos Opportunity/Quote + termo de aceite) com o time inteiro primeiro** e, sobre essa base, **paralelizar as frentes de baixa dependência** — é o que torna a data viável. O MVP entrega oito das nove épicas (E06/Agentforce fica de fora); o `roadmap` detalha as cinco fases (com marcos de projeto, de decreto e de entrega de jornadas para UAT e PROD), o caminho crítico e os candidatos a de-escopo que servem de buffer.

> ⚠ **Viabilidade da data fixa — sinalizada.** 13 semanas para um build XL regulado (financeiro com split, conciliação e emissão de boleto) sobre **três pré-requisitos externos de lead-time** — org greenfield, MuleSoft on-premise e gateway — é um cronograma **agressivo**, com margem mínima e apenas ~1 semana de estabilização. Se qualquer pré-requisito da Fase 0 atrasar ou a homologação achar defeito no financeiro, **15/nov não é alcançável só com esforço adicional**: o de-escopo (E03 financeiro primeiro, adiando parte do split/conciliação para pós-go-live) é o único trilho para preservar a data. A resolução dos três blockers restantes **mais** o provisionamento da org greenfield, a prontidão da infra MuleSoft on-premise e a contratação do gateway na Fase 0 são a recomendação que antecede tudo.
