# Solução — DATAPREV-PAT (Marketplace Digital do PAT)

> **Nível ROM, sobre premissas.** Este documento desenha a arquitetura da solução em nível de proposta, sobre três premissas de arquitetura já formalizadas — residência de dados híbrida (ADR 0001), **instância dedicada e apartada (ADR 0002)** e **fronteira CRM-não-transacional / motor de regras de split (ADR 0003)** — e quatro decisões ainda em aberto (fronteira campo-a-campo da residência, hospedagem MuleSoft, identidade Experience Cloud × CPF, contratos de API), além da seleção do provedor do gateway PCI. Essas decisões e o provisionamento da org dedicada se resolvem numa **Fase 0** antes do compromisso final de escopo. Cada decisão load-bearing carrega sua etiqueta de origem — `[KB: …]`, `[extends: …]` ou `[assumption: …]`.

---

## Fundações de Arquitetura (transversais)

Decisões horizontais que nenhuma épica individual possui — a base sobre a qual o mapa por processo, adiante, se apoia.

### Estratégia de org — instância dedicada e apartada (ADR 0002)

Os quatro domínios do programa (marketplace de cotação, credenciamento, financeiro/split e atendimento) vivem numa **única org**, mas essa org é **dedicada e apartada** das demais orgs de clientes da Dataprev. O isolamento não é preferência — é **forçado** por segurança e sensibilidade financeira, pela volumetria (~800 mil estabelecimentos, ~450 mil beneficiárias — a ratificar), pela auditabilidade perante TCU/CGU/ANPD e pela administração da instância pelo próprio MTE (que não pode enxergar "a cozinha" dos demais clientes). O provisionamento tem lead-time externo e é **pré-requisito de arranque (Fase 0)**. A separação entre domínios internos segue por objeto, perfil e modelo de compartilhamento. `[decisions/0002-instancia-dedicada-mte-pat]` — premissa ainda **verbal, a ratificar por escrito**.

### Seleção de produtos e licenciamento

| Produto | Papel |
|---|---|
| Experience Cloud (LWR) | Portal externo — beneficiárias, estabelecimentos, procuração digital |
| Core / Service Cloud | Motor de negócio: objetos custom (cotação, proposta, folha, contrato, **motor de split**), automação, atendimento |
| MuleSoft Anypoint | Camada de integração API-led para todos os sistemas externos, o **gateway PCI** e as ~600-700 facilitadoras |
| Agentforce | Atendimento inteligente (E06 — **fora do MVP**, candidato a de-escopo) |
| Gateway PCI / banco custódia | **Fora do escopo Salesforce** — contratado pelo cliente; executa transações bancárias e custodia (ver ADR 0003) |

`[KB: salesforce-revenue-cloud-marketplace-arch.md:41-45]` — arquitetura Experience Cloud + MuleSoft confirmada contra fonte primária Salesforce; Revenue Cloud fora desta rodada (é sell-side, sem RFQ/leilão reverso nativo).

**Licenciamento.** Licenças internas (Service/Platform) para a operação MTE; **Experience Cloud external** (Customer Community Plus) para as centenas de milhares de beneficiárias e estabelecimentos. O modelo (login-based vs. member-based) depende do volume de usuários ativos — variável de custo ainda não quantificada. `[assumption: modelo de licença external depende do volume de usuários ativos — G0103/G0108]`

### Modelo de compartilhamento (OWD / sharing)

OWD **Private** em todos os objetos transacionais (Cotacao__c, Proposta__c, folha, contrato, split): a beneficiária vê apenas seus próprios registros; a facilitadora vê apenas as propostas e contratos onde é parte. A visibilidade N-vendedores do leilão (uma cotação exposta a N facilitadoras) é habilitada por sharing por critério + Apex managed sharing. Perfis guest/external do portal ficam travados no mínimo necessário. `[extends: padrão Experience Cloud external-user OWD Private + sharing sets, aplicado ao modelo comprador→N-vendedores do marketplace]`

### DevOps e governança

Desenvolvimento source-driven (Salesforce CLI + Git) com pipeline Dev → QA → UAT → Produção; a equipe multi-perfil e a janela fixa comprimida justificam pipeline versionado em vez de Change Sets. Full sandbox para o UAT com dado representativo. `[assumption: padrão PS para equipe multi-perfil + go-live regulado; validar toolchain e política de deploy da Dataprev — G0809]`

### Segurança e residência de dados — a fundação (ADR 0001)

CPF e dados sensíveis **não persistem** na nuvem Salesforce. A org guarda **referências tokenizadas**, resolvidas em runtime via MuleSoft contra a infraestrutura Dataprev. É premissa transversal a E01, E02, E03 e E06, e o desenho concreto vive em E08. Combinada com o isolamento da instância dedicada (ADR 0002), forma a espinha de segurança/auditoria do programa. Diagrama de fluxo de dados sob LGPD Art. 11 e trilha de auditoria para TCU/CGU/ANPD acompanham.

**Quatro decisões de arquitetura em aberto que esta fundação carrega até a Fase 0:**
- `[assumption: G0801 — fronteira campo-a-campo exata da residência (o que é token vs. o que pode persistir) a ratificar com Jair Bogo; governa o data model de E01/E02/E03/E06]`
- `[assumption: G0504 — hospedagem MuleSoft (CloudHub vs. Runtime Fabric em gov cloud) × residência define ONDE ocorre a de-tokenização do CPF]`
- `[assumption: G0106 — Experience Cloud exige User/Contact com identidade; conciliar com "CPF não persiste" via Contact por referência tokenizada + resolução runtime]`
- `[assumption: G0501 — sem Swagger/contrato de API de nenhum sistema externo; integração é mock-first até os contratos existirem — risco #1, caminho crítico]`

### Fronteira CRM × financeiro — o Salesforce é o motor de regras, não o banco (ADR 0003)

O Salesforce **calcula e aplica as regras de split** (rateio governo/facilitadora/estabelecimento) sob o teto de administração (MDR) de 3,6% e o repasse em até 15 dias do Decreto 12.712/2025, **emite a boletagem já com o split aplicado**, orquestra e **concilia por casamento**, e **recebe** as movimentações bancárias. Ele **não transaciona nem custodia dinheiro**: a execução das transações bancárias e a custódia ficam no **gateway PCI**, contratado pelo cliente, que recebe as boletagens com split do Salesforce, executa e devolve as movimentações para o CRM conciliar. `[decisions/0003-fronteira-crm-nao-transacional]` — é o que dimensiona E03 como XL e coloca a seleção/contratação do gateway PCI como pré-requisito de Fase 0 (G0309).

---

## Solução por Processo de Negócio

Ordem por fluxo de criação de valor: identidade → cotação → credenciamento → financeiro/split → atendimento → (integração, migração, segurança, mudança — transversais ao final).

### E01 — Portal & Identidade gov.br

**Contexto de negócio.** A beneficiária precisa entrar no marketplace com a identidade gov.br já existente e agir em nome da empresa, sem um cadastro paralelo. É a porta de entrada de todo o programa.

**Abordagem de solução.** Experience Cloud (template LWR) com login gov.br via OpenID Connect, procuração digital e fluxo "representar empresa". É a base de identidade e navegação sobre a qual E02, E03 e E04 renderizam.

**Arquitetura de suporte.** Autenticação federada gov.br (OIDC) via Named Credentials/Auth Provider, com a resolução de identidade sensível intermediada por MuleSoft (ADR 0001 — o Contact carrega referência tokenizada, não o CPF). `[assumption: Experience Cloud + gov.br OIDC é padrão de produto, mas o conector nativo não cobre gov.br diretamente — validar o fluxo específico e a procuração digital — G0101/G0102]`

### E02 — Marketplace de Cotação e Contratação

**Contexto de negócio.** O coração da reforma: a beneficiária publica uma cotação (nº de funcionários, valor, vigência, distribuição por UF, recursos obrigatórios), N facilitadoras enviam propostas **ocultas até o fechamento**, há comparação lado a lado, e a seleção manual vira contrato **fora da plataforma**. É o "leilão reverso".

**Abordagem de solução.** Custom na Core Platform — não há suporte nativo Salesforce a RFQ/leilão reverso. Objetos `Cotacao__c` 1→N `Proposta__c`, Flow para publicação/prazo/SLA, e Apex para a comparação lado a lado, o ranking e a transição seleção→contrato.

**Arquitetura de suporte.** Modelo comprador→N-vendedores com Apex managed sharing (cada facilitadora vê só sua proposta; a beneficiária vê todas as recebidas ao fechamento). LWC custom para a tela "Comparar Propostas". Recepção de lances das facilitadoras via API (MuleSoft). `[KB: salesforce-revenue-cloud-marketplace-arch.md:19-25]` — leilão reverso não é capability nativa; modelo custom confirmado contra fonte primária. `[assumption: regras de seleção/desempate e conformidade com a Lei 14.133/2021 a definir — G0202/G0203/G0204]` **Enriquecimento/perfil por Data Cloud é adição Assumed e fica FORA do MVP** (buffer de cronograma — o leilão funciona sem ele; G0209).

### E04 — Credenciamento de Estabelecimentos

**Contexto de negócio.** Estabelecimentos (restaurantes, mercados) hoje se credenciam facilitadora a facilitadora, com duplicidade e fricção. O programa quer um cadastro unificado via gov.br, mantendo o papel legal das facilitadoras de aprovar e descredenciar.

**Abordagem de solução.** Objeto de estabelecimento com identidade gov.br PJ (CNPJ), workflow de aprovação e integração de deduplicação/validação de CNPJ contra as bases das facilitadoras.

**Arquitetura de suporte.** Aprovação declarativa + integração MuleSoft para dedup/reconciliação e validação de CNPJ. `[assumption: G0401 — sistema-of-record do credenciamento (registro unificado vs. papel legal da facilitadora) é conflito de fonte a resolver]`

### E03 — Motor de Regras de Split & Conciliação  *(XL)*

**Contexto de negócio.** A empresa faz upload da folha; o programa precisa ratear o pagamento (governo/facilitadora/estabelecimento) sob o teto de MDR de 3,6% e repasse em até 15 dias (Decreto 12.712/2025), emitir a cobrança já com o rateio aplicado, e conciliar o que efetivamente entrou. O dinheiro em si passa por conta custódia em banco público/gateway PCI — **não pelo Salesforce**.

**Abordagem de solução (ADR 0003).** O Salesforce é o **motor de regras de split**: objetos custom para folha, contrato e regras de rateio; upload em layout padronizado; o motor **calcula e aplica o split**, **emite a boletagem já com o split aplicado** para o gateway PCI, e **concilia por casamento** os lançamentos devolvidos com o boleto pago, monitorando a conta custódia. A UI consolida ao status "crédito concedido". Revenue Cloud fora desta rodada.

**Arquitetura de suporte.** Integração via MuleSoft com o **gateway PCI** (que executa boleto/Pix/split bancário e custodia), com **idempotência** obrigatória e trilha de conciliação. A execução e a custódia são do gateway PCI (contratado pelo cliente), não do CRM. `[decisions/0003-fronteira-crm-nao-transacional]` `[KB: salesforce-revenue-cloud-marketplace-arch.md:31-35]` — motor de split custom no CRM; execução externa. `[assumption: regras de split/desempate, modelo de conta custódia + provedor do gateway PCI e a mecânica de conciliação a confirmar — G0301/G0304/G0309]`

### E06 — Atendimento Inteligente (Agentforce)  *(fora do MVP — de-escopo/buffer)*

**Contexto de negócio.** Atender em escala os participantes (beneficiárias, facilitadoras, estabelecimentos) — dúvidas informacionais e operações transacionais — via WhatsApp/webchat.

**Abordagem de solução.** Agente Agentforce com camada informacional (FAQ grounded) e transacional (consultas ao marketplace). O agente transacional lê dados do participante, o que colide com a residência — o desenho evita CPF no prompt do LLM, resolvendo por referência tokenizada. **Não é pré-requisito do go-live regulatório de 15/nov — é o primeiro candidato a de-escopo e não entra no MVP.**

**Arquitetura de suporte.** Grounding por referência tokenizada; guardrails de agente público governamental; canal WhatsApp/BSP adiciona risco e prazo. `[assumption: G0603 — tensão residência × agente transacional; canais e casos de uso a confirmar — G0601/G0602]`

### E05 — Integração Corporativa (MuleSoft) *(transversal)*

**Contexto de negócio.** O marketplace só funciona conectado ao ecossistema: Novo PAT, GOV.BR/Geride, CTPS Digital, eSocial, SDC, Kinis PJ/Par, validação de CNPJ, o **gateway PCI/banco custódia** e as APIs das ~600-700 facilitadoras.

**Abordagem de solução.** Camada de integração API-led (System / Process / Experience), abordagem **mock-first** para desbloquear o desenvolvimento enquanto Swaggers/contratos não são disponibilizados. O contrato de integração com o gateway PCI (ADR 0003) é alvo declarado já na Fundação.

**Arquitetura de suporte.** Padrões event-driven onde couber (Platform Events/CDC), tratamento de erro/replay, e governança de virada dos mocks para APIs reais. `[KB: salesforce-revenue-cloud-marketplace-arch.md:36-40]` `[assumption: G0501 — ausência total de contratos de API é o risco #1 e caminho crítico; G0504 — hospedagem MuleSoft × residência define o ponto de de-tokenização; G0309 — integração do gateway PCI]`

### E07 — Migração & Carga Inicial de Cadastros *(transversal)*

**Contexto de negócio.** Popular a plataforma com beneficiárias, facilitadoras e estabelecimentos a partir do Novo PAT/bases MTE.

**Abordagem de solução.** Carga inicial **mínima** (não migração massiva — o Novo PAT permanece system-of-record), com foco em qualidade, deduplicação e referências não-sensíveis (ADR 0001). Carga massiva fica pós-go-live (buffer).

**Arquitetura de suporte.** Extração/carga via MuleSoft com regras de dedup. `[assumption: volumes, fonte e qualidade da carga a confirmar; volume desconhecido é band-widener de sizing — G0701/G0703/G0704]`

### E08 — Segurança, Residência de Dados & Conformidade *(transversal)*

**Contexto de negócio.** Todo o programa lida com CPF e dados previdenciários sensíveis, sob LGPD Art. 11 e escrutínio de TCU/CGU/ANPD, numa instância dedicada (ADR 0002).

**Abordagem de solução.** Materializa a fundação de residência: modelo de referências tokenizadas (CPF e sensíveis não persistem no Salesforce), diagrama de fluxo de dados sob LGPD, trilha de auditoria para acesso a dados sensíveis que não estão na org, e a justificativa explícita de isolamento/administração-pelo-cliente da instância dedicada.

**Arquitetura de suporte.** Tokenização + resolução runtime via MuleSoft; isolamento da org dedicada; overlay de conformidade regulada. `[assumption: G0801 — fronteira exata de campos a ratificar com arquitetura Dataprev; é a decisão que governa o data model de várias épicas]`

### E09 — Gestão de Mudança & Adoção *(transversal)*

**Contexto de negócio.** A escala do programa (~600-700 facilitadoras + ~800 mil estabelecimentos e ~450 mil beneficiárias, a ratificar) e a resistência esperada das facilitadoras (que perdem margem no modelo transparente) exigem comunicação, capacitação e acompanhamento de adoção deliberados.

**Abordagem de solução.** Plano de comunicação, materiais de apoio, capacitação e métricas de adoção. Entrega Salesforce PS. Sem arquitetura técnica bespoke. No MVP, adoção enxuta; programa completo pós-go-live (buffer).

**Arquitetura de suporte.** N/A — configuração/entrega, não construção técnica. `[assumption: escopo de change/adoção e a fronteira PS vs. Dataprev/MTE a confirmar — G0901/G0906]`

---

## Nota sobre fases

O programa opera em **modo data-fixa**: o go-live de **15/nov/2026** (interoperabilidade total do Decreto 12.712/2025 + entrada do financeiro em produção) é imóvel, e o escopo é a variável de flexão. O MVP entrega oito das nove épicas (E06/Agentforce fica de fora); o `roadmap` detalha as cinco fases, o caminho crítico e os candidatos a de-escopo que servem de buffer. A resolução dos quatro blockers **mais** o provisionamento da org dedicada e a contratação do gateway PCI na Fase 0 são a recomendação que antecede tudo — os lead-times externos aí são o maior risco à data fixa.
