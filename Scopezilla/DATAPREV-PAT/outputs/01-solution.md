# Solução — DATAPREV-PAT (Marketplace Digital do PAT)

> **Nível ROM, sobre premissas.** Este documento desenha a arquitetura da solução em nível de proposta, sobre a premissa de residência de dados híbrida (ADR 0001) e quatro decisões de arquitetura ainda em aberto (fronteira de residência, hospedagem MuleSoft, identidade Experience Cloud × CPF, contratos de API). Essas decisões idealmente se resolvem numa **Fase 0** antes do compromisso final de escopo e prazo. Cada decisão load-bearing carrega sua etiqueta de origem — `[KB: …]` (base de conhecimento do projeto), `[extends: …]` (padrão fundamentado estendido) ou `[assumption: …]` (conhecimento geral Salesforce; o que a validaria).

---

## Fundações de Arquitetura (transversais)

Decisões horizontais que nenhuma épica individual possui — a base sobre a qual o mapa por processo, adiante, se apoia.

### Estratégia de org — org única

Uma única org Salesforce (Enterprise Edition ou superior) hospeda os quatro domínios do programa: marketplace de cotação, credenciamento, folha/financeiro e atendimento. A separação entre domínios é feita por objeto, perfil e modelo de compartilhamento — não por múltiplas orgs. Não há requisito de isolamento regulatório que force multi-org; a residência de dados sensíveis é resolvida por tokenização (ver Segurança), não por separação física de org. `[assumption: org única é o default do produto; validar que nenhum requisito de isolamento (ex.: segregação ministerial) force multi-org — G0808]`

### Seleção de produtos e licenciamento

| Produto | Papel |
|---|---|
| Experience Cloud (LWR) | Portal externo — beneficiárias, estabelecimentos, procuração digital |
| Core / Service Cloud | Motor de negócio: objetos custom (cotação, proposta, folha, contrato), automação, atendimento |
| MuleSoft Anypoint | Camada de integração API-led para todos os sistemas externos e as ~600-700 facilitadoras |
| Agentforce | Atendimento inteligente informacional + transacional |

`[KB: salesforce-revenue-cloud-marketplace-arch.md:41-45]` — arquitetura Experience Cloud + MuleSoft confirmada contra fonte primária Salesforce; Revenue Cloud fora desta rodada (é sell-side, sem RFQ/leilão reverso nativo).

**Licenciamento.** Licenças internas (Service/Platform) para a operação Dataprev/MTE; **Experience Cloud external** (Customer Community Plus) para as centenas de milhares de beneficiárias e estabelecimentos. O modelo (login-based vs. member-based) depende do volume de usuários ativos — variável de custo ainda não quantificada. `[assumption: modelo de licença external depende do volume de usuários ativos — G0103/G0108]`

### Modelo de compartilhamento (OWD / sharing)

OWD **Private** em todos os objetos transacionais (Cotacao__c, Proposta__c, folha, contrato): a beneficiária vê apenas seus próprios registros; a facilitadora vê apenas as propostas e contratos onde é parte. A visibilidade N-vendedores do leilão (uma cotação exposta a N facilitadoras) é habilitada por sharing por critério + Apex managed sharing. Perfis guest/external do portal ficam travados no mínimo necessário. `[extends: padrão Experience Cloud external-user OWD Private + sharing sets, aplicado ao modelo comprador→N-vendedores do marketplace]`

### DevOps e governança

Desenvolvimento source-driven (Salesforce CLI + Git) com pipeline Dev → QA → UAT → Produção; a equipe multi-perfil e a timeline comprimida justificam pipeline versionado em vez de Change Sets. Full sandbox para o UAT com dado representativo. `[assumption: padrão PS para equipe multi-perfil + go-live regulado; validar toolchain e política de deploy da Dataprev — G0809]`

### Segurança e residência de dados — a fundação (ADR 0001)

CPF e dados sensíveis **não persistem** na nuvem Salesforce. A org guarda **referências tokenizadas**, resolvidas em runtime via MuleSoft contra a infraestrutura Dataprev. É premissa transversal a E01, E02, E03 e E06, e o desenho concreto vive em E08. Diagrama de fluxo de dados sob LGPD Art. 11 e trilha de auditoria para TCU/CGU/ANPD acompanham.

**Quatro decisões de arquitetura em aberto que esta fundação carrega até a Fase 0:**
- `[assumption: G0801 — fronteira campo-a-campo exata da residência (o que é token vs. o que pode persistir) a ratificar com Jair Bogo; governa o data model de E01/E02/E03/E06]`
- `[assumption: G0504 — hospedagem MuleSoft (CloudHub vs. Runtime Fabric em gov cloud) × residência define ONDE ocorre a de-tokenização do CPF]`
- `[assumption: G0106 — Experience Cloud exige User/Contact com identidade; conciliar com "CPF não persiste" via Contact por referência tokenizada + resolução runtime]`
- `[assumption: G0501 — sem Swagger/contrato de API de nenhum sistema externo; integração é mock-first até os contratos existirem — risco #1, caminho crítico]`

---

## Solução por Processo de Negócio

Ordem por fluxo de criação de valor: identidade → cotação → credenciamento → financeiro → atendimento → (integração, migração, segurança, mudança — transversais ao final).

### E01 — Portal & Identidade gov.br

**Contexto de negócio.** A beneficiária precisa entrar no marketplace com a identidade gov.br já existente e agir em nome da empresa, sem um cadastro paralelo. É a porta de entrada de todo o programa.

**Abordagem de solução.** Experience Cloud (template LWR) com login gov.br via OpenID Connect, procuração digital e fluxo "representar empresa". É a base de identidade e navegação sobre a qual E02, E03 e E04 renderizam.

**Arquitetura de suporte.** Autenticação federada gov.br (OIDC) via Named Credentials/Auth Provider, com a resolução de identidade sensível intermediada por MuleSoft (ADR 0001 — o Contact carrega referência tokenizada, não o CPF). `[assumption: Experience Cloud + gov.br OIDC é padrão de produto, mas o conector nativo não cobre gov.br diretamente — validar o fluxo específico e a procuração digital — G0101/G0102]`

### E02 — Marketplace de Cotação e Contratação

**Contexto de negócio.** O coração da reforma: a beneficiária publica uma cotação (nº de funcionários, valor, vigência, distribuição por UF, recursos obrigatórios), N facilitadoras enviam propostas com prazo/SLA, há comparação lado a lado, e a seleção vira contrato. É o "leilão reverso".

**Abordagem de solução.** Custom na Core Platform — não há suporte nativo Salesforce a RFQ/leilão reverso. Objetos `Cotacao__c` 1→N `Proposta__c`, Flow para publicação/prazo/SLA, e Apex para a comparação lado a lado, o ranking e a transição seleção→contrato.

**Arquitetura de suporte.** Modelo comprador→N-vendedores com Apex managed sharing (cada facilitadora vê só sua proposta; a beneficiária vê todas as recebidas). LWC custom para a tela "Comparar Propostas". Recepção de lances das facilitadoras via API (MuleSoft). `[KB: salesforce-revenue-cloud-marketplace-arch.md:19-25]` — leilão reverso não é capability nativa; modelo custom confirmado contra fonte primária. `[assumption: regras de seleção/desempate e conformidade com a Lei 14.133/2021 a definir — G0202/G0203/G0204]`

### E04 — Credenciamento de Estabelecimentos

**Contexto de negócio.** Estabelecimentos (restaurantes, mercados) hoje se credenciam facilitadora a facilitadora, com duplicidade e fricção. O programa quer um cadastro unificado via gov.br, mantendo o papel legal das facilitadoras de aprovar e descredenciar.

**Abordagem de solução.** Objeto de estabelecimento com identidade gov.br PJ (CNPJ), workflow de aprovação e integração de deduplicação contra as bases das facilitadoras.

**Arquitetura de suporte.** Aprovação declarativa + integração MuleSoft para dedup/reconciliação. `[assumption: G0401 — sistema-of-record do credenciamento (registro unificado vs. papel legal da facilitadora) é conflito de fonte a resolver]`

### E03 — Folha & Financeiro

**Contexto de negócio.** A empresa faz upload da folha, a facilitadora processa, gera boleto/Pix, o dinheiro passa por conta custódia em banco público e é dividido (split) governo/facilitadora, sob a regra de repasse em até 15 dias (Decreto 12.712/2025).

**Abordagem de solução.** Baseline Core-only: objetos custom para folha e contrato; upload em layout padronizado; o **split é integração externa via MuleSoft** (não é nativo do Billing). Revenue Cloud fora desta rodada — reavaliar em fase futura se o financeiro crescer.

**Arquitetura de suporte.** Integração transacional com banco público/PSP (boleto, Pix, split), com **idempotência** obrigatória e trilha de conciliação. `[KB: salesforce-revenue-cloud-marketplace-arch.md:31-35]` — split multi-parte não é nativo de Billing; integração externa via MuleSoft. `[assumption: modelo de conta custódia + adquirente/PSP, e a mecânica de conciliação, a confirmar — G0301/G0304]`

### E06 — Atendimento Inteligente (Agentforce)

**Contexto de negócio.** Atender em escala os participantes (beneficiárias, facilitadoras, estabelecimentos) — dúvidas informacionais e operações transacionais — via WhatsApp/webchat.

**Abordagem de solução.** Agente Agentforce com camada informacional (FAQ grounded) e transacional (consultas ao marketplace). O agente transacional lê dados do participante, o que colide com a residência — o desenho evita CPF no prompt do LLM, resolvendo por referência tokenizada.

**Arquitetura de suporte.** Grounding por referência tokenizada; guardrails de agente público governamental. `[assumption: G0603 — tensão residência × agente transacional: desenhar sem CPF em prompt; canais e casos de uso a confirmar — G0601/G0602]`

### E05 — Integração Corporativa (MuleSoft) *(transversal)*

**Contexto de negócio.** O marketplace só funciona conectado ao ecossistema: Novo PAT, GOV.BR/Geride, CTPS Digital, eSocial, SDC, Kinis PJ/Par, banco público, e as APIs das ~600-700 facilitadoras.

**Abordagem de solução.** Camada de integração API-led (System / Process / Experience), abordagem **mock-first** para desbloquear o desenvolvimento enquanto Swaggers/contratos não são disponibilizados.

**Arquitetura de suporte.** Padrões event-driven onde couber (Platform Events/CDC), tratamento de erro/replay, e governança de virada dos mocks para APIs reais. `[KB: salesforce-revenue-cloud-marketplace-arch.md:36-40]` `[assumption: G0501 — ausência total de contratos de API é o risco #1 e caminho crítico; G0504 — hospedagem MuleSoft × residência define o ponto de de-tokenização]`

### E07 — Migração & Carga Inicial de Cadastros *(transversal)*

**Contexto de negócio.** Popular a plataforma com beneficiárias, facilitadoras e estabelecimentos a partir do Novo PAT/bases MTE.

**Abordagem de solução.** Carga inicial (não migração massiva — o Novo PAT permanece system-of-record), com foco em qualidade, deduplicação e referências não-sensíveis (ADR 0001).

**Arquitetura de suporte.** Extração/carga via MuleSoft com regras de dedup. `[assumption: volumes, fonte e qualidade da carga a confirmar; volume desconhecido é band-widener de sizing — G0701/G0703/G0704]`

### E08 — Segurança, Residência de Dados & Conformidade *(transversal)*

**Contexto de negócio.** Todo o programa lida com CPF e dados previdenciários sensíveis, sob LGPD Art. 11 e escrutínio de TCU/CGU/ANPD.

**Abordagem de solução.** Materializa a fundação de residência: modelo de referências tokenizadas (CPF e sensíveis não persistem no Salesforce), diagrama de fluxo de dados sob LGPD, trilha de auditoria para acesso a dados sensíveis que não estão na org.

**Arquitetura de suporte.** Tokenização + resolução runtime via MuleSoft; overlay de conformidade regulada. `[assumption: G0801 — fronteira exata de campos a ratificar com arquitetura Dataprev; é a decisão que governa o data model de várias épicas]`

### E09 — Gestão de Mudança & Adoção *(transversal)*

**Contexto de negócio.** A escala do programa (600-700 facilitadoras + centenas de milhares de beneficiárias) e a resistência esperada das facilitadoras (que perdem margem no modelo transparente) exigem comunicação, capacitação e acompanhamento de adoção deliberados.

**Abordagem de solução.** Plano de comunicação, materiais de apoio, capacitação e métricas de adoção. Entrega Salesforce PS. Sem arquitetura técnica bespoke.

**Arquitetura de suporte.** N/A — configuração/entrega, não construção técnica. `[assumption: escopo de change/adoção e a fronteira PS vs. Dataprev/MTE a confirmar — G0901/G0906]`

---

## Nota sobre fases

O split por fases (o que vai para homologação set/2026 vs. produção 15/nov/2026) é **decisão do cliente** — não pré-decidida aqui. O `roadmap` trabalha a sequência e a janela; a timeline agressiva é uma consequência a sinalizar, e a resolução dos quatro blockers na Fase 0 é a recomendação que a antecede.
