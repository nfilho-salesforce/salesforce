# Sumário Executivo — Marketplace Digital do PAT (DATAPREV-PAT)

## Visão Geral (At a Glance)

- **Dor atual**: contratação de vale-alimentação fragmentada e opaca; MTE sem visibilidade sistêmica sobre a operação.
- **Visão de transformação**: PAT como mercado digital único, transparente e concorrencial, em jornada 100% gov.br, numa **org Salesforce 100% greenfield e apartada** do MTE/PAT, construída sobre **Sales Cloud** reusando objetos nativos para encurtar o tempo de implementação.
- **Principais motores de valor**: jornada única gov.br, leilão reverso entre facilitadoras sobre **objetos nativos Sales Cloud** (Opportunity = demanda; Quote = resposta via API), e o **Salesforce como motor de regras de split** sob o teto de MDR de 3,6% e repasse em 15 dias do Decreto 12.712/2025.
- **Maior risco**: a data de go-live é **fixa e externa (15/nov/2026)**, o escopo do financeiro é XL e regulado, e três pré-requisitos externos de lead-time (org greenfield, MuleSoft on-premise, gateway) precedem o build — se um escorregar, a data não é alcançável só com esforço e o de-escopo (E03) é o único trilho.
- **Primeiro passo recomendado**: **Fase 0 (17/ago – 30/ago)** — provisionar a org 100% greenfield + a infra do MuleSoft on-premise + selecionar o gateway + destravar os blockers de arquitetura. Os lead-times externos aqui são o maior risco à data fixa.

---

## Panorama

O Decreto nº 12.712/2025 promove a maior reforma do PAT em quase 50 anos: comprime a margem das operadoras (teto de administração — MDR — de 3,6%), exige **repasse ao estabelecimento em até 15 dias**, pré-pagamento obrigatório, fim do rebate e **interoperabilidade** (grandes operadoras a partir de mai/2026, total até nov/2026). Isso abre espaço para uma **plataforma pública neutra, operada pela Dataprev para o Ministério do Trabalho e Emprego (MTE)**, que substitui a negociação bilateral fragmentada de hoje por um leilão aberto entre facilitadoras — dando ao governo visibilidade sistêmica sobre um setor que movimenta centenas de bilhões de reais por ano.

**Por que agora:** o marco de **interoperabilidade total e a entrada do financeiro em produção estão fixados em 15/nov/2026**. A data não é uma preferência — é regulatória e externa. A janela de construção, com **início comprometido em 17/ago** e **homologação início nov**, é de **~13 semanas**. Atrasar significa operar a nova regra sem plataforma que a suporte. *(A ADI 7962 tramita no STF sobre o decreto — premissas dependentes de data carregam a ressalva.)*

## Escopo

Nove épicas cobrem o fluxo completo. O **MVP comprometido para 15/nov entrega oito delas**; a nona (Agentforce) é o primeiro candidato a de-escopo, tratado como buffer de cronograma.

- **Marketplace de cotação e contratação (E02, XL)** — o coração da reforma, sobre **Opportunity/Quote nativos**: a beneficiária registra a demanda de leilão reverso (**Opportunity**) → facilitadoras respondem **exclusivamente via API** (**Quote**) — sem acesso à plataforma, informando o ID da cotação aberta na vigência. No MVP elas **descobrem as demandas abertas por um endpoint de consulta (pull via API)** — a notificação ativa (push) é roadmap futuro, com o canal a definir (o que decide se posicionamos ou não Marketing Cloud). A **equidade é por construção** (a facilitadora não tem tela, logo não vê a proposta concorrente — sem regra de ocultamento custom). A beneficiária acompanha as cotações conforme chegam (comparação lado a lado), mas **só pode selecionar quando a janela de vigência fecha** (seleção manual travada, não cega) → **termo de aceite**. Contrato **sem CLM** (PDF imutável versionado).
- **Folha, Motor de Split & Conciliação (E03, XL)** — o Salesforce recebe a folha (CSV via portal/API), valida layout/integridade, disponibiliza à facilitadora, **calcula e aplica o rateio** sob o teto de MDR de 3,6% e o repasse de 15 dias, aciona o gateway para boletagem, **concilia por casamento** em lotes incrementais via MuleSoft e registra todo o racional. A execução bancária e a custódia ficam **fora** (gateway, selecionado pelo cliente); as linhas da folha **não persistem** em objeto (roadmap futuro).
- **Portal & Identidade gov.br (E01, L)** — portal **Experience Cloud** da beneficiária com login gov.br (versão de licença a requalificar — Partner Community expõe Opportunity/Quote, Customer Community Plus não) — e **Credenciamento (E04, M)** com cadastro via gov.br PJ/CNPJ + **vigilância sanitária** (triagem IA + alertas de vencimento de licença).
- **Integração Corporativa MuleSoft (E05, XL)** — camada API-led **on-premise** para Novo PAT (sem API hoje — mock obrigatório), gov.br, eSocial, as facilitadoras e o **gateway**.
- **Atendimento Inteligente Agentforce (E06, L — fora do MVP)**, **Migração & Carga (E07, M)**, **Segurança & Residência de Dados (E08, L)**, **Gestão de Mudança & Adoção (E09, M)**.

## Destaques da Solução

- **Sales Cloud reusando objetos nativos (ADR 0004)**: a plataforma é construída sobre **Sales Cloud**, reusando funcionalidade nativa para encurtar o tempo de implementação. O leilão reverso mapeia em objetos nativos — **Opportunity** = demanda registrada pela beneficiária; **Quote** = resposta da facilitadora recebida via API. Quem opera esses objetos no **portal Experience Cloud** é a **beneficiária** (o estabelecimento também acessa); a **facilitadora é API-only** e não consome licença de portal — as ~600–700 facilitadoras são integrações, não assentos. A versão de licença da beneficiária (Partner Community vs. Customer Community Plus) segue a requalificar contra o padrão de acesso real.
- **Greenfield + MuleSoft on-premise (ADR 0005)**: a org é **100% greenfield** — instância nova, sem ORG existente, isolada de qualquer ambiente/admins Dataprev. O **MuleSoft on-premise** é o mecanismo de **soberania de dados** (a integração fica no perímetro Dataprev) e um pré-requisito de marco da Fase 0. Resolve o gap de hospedagem do MuleSoft (G0504).
- **Instância dedicada e apartada (ADR 0002)**: reforça o isolamento — forçada por segurança, volumetria, auditabilidade (TCU/CGU/ANPD) e administração pelo cliente. O provisionamento tem lead-time externo e é um pré-requisito de Fase 0.
- **Fronteira CRM × financeiro (ADR 0003)**: o Salesforce é o **motor de regras de split** e o orquestrador da conciliação — não transaciona nem custodia dinheiro. Ele aciona a boletagem com o split aplicado; o **gateway do cliente** intermedia a conta custódia, executa as transações bancárias e devolve as movimentações para o CRM conciliar. É o que dimensiona E03 como XL.
- **Residência de dados híbrida (ADR 0001)**: CPF e dados sensíveis **não persistem** na nuvem Salesforce — ficam na Dataprev e são resolvidos em runtime via referências tokenizadas por MuleSoft, aderente à LGPD (Art. 11) e à auditoria de TCU/CGU/ANPD. Isolamento (greenfield + on-premise) + tokenização são a espinha de segurança do programa.
- **Métodos que protegem a data fixa**: **definição fundacional de objetos + mapeamento de dados com o time inteiro primeiro**, depois paralelização das frentes de baixa dependência; mock-first nas integrações (Novo PAT sem API hoje) e configurar-antes-de-customizar (reforçado pelo reuso nativo do Sales Cloud).

## Abordagem de Implementação

**Modo data-fixa, planejado de trás pra frente. Datas comprometidas: início 17/ago/2026 → homologação (UAT) início nov → go-live PRODUÇÃO 15/nov/2026. Duração total: 13 semanas (compromisso do usuário). A data é o âncora; o escopo é a variável de flexão.** Cinco fases sequenciadas por caminho crítico, com a **paralelização** como estratégia central de viabilidade:

- **Fase 0 — Arranque, Provisionamento & Arquitetura (17/ago – 30/ago · 2 sem)**: provisionar a org **100% greenfield** (ADR 0002/0005) + a infra do **MuleSoft on-premise** (ADR 0005), selecionar o gateway (ADR 0003) e resolver os blockers (fronteira de residência, Novo PAT sem API, identidade gov.br × CPF). **Os três lead-times externos aqui são o maior risco à data.**
- **Fase 1 — Fundação: Modelo de Dados + Identidade + Integração + Residência (31/ago – 27/set · 4 sem)** (E05, E08, E01): arranca com o **time inteiro definindo os objetos nativos fundacionais e o mapeamento de dados (ADR 0004)** — o marco que libera a paralelização; depois integração mock-first (on-premise), residência e portal Partner Community gov.br.
- **Fase 2 — Marketplace & Credenciamento (28/set – 18/out · 3 sem)** — frente paralelizada (E02 sobre Opportunity/Quote nativos, sem Data Cloud; E04 com vigilância sanitária). **Marco de jornada (UAT).**
- **Fase 3 — Folha, Motor de Split & Conciliação (19/out – 8/nov · 3 sem)** (E03) — o fluxo folha→pagamento→split completo; a fase XL mais sensível à data fixa. **A homologação início nov abre ao fim desta fase.**
- **Fase 4 — Homologação, Carga Mínima, Adoção & Go-live PROD (9/nov – 15/nov · 1 sem)** (E07, E09) — hypercare mínimo. **Marcos: projeto (go-live PROD 15/nov), decreto (interoperabilidade total), jornada (UAT→PROD).**

**Caminho crítico**: Fase 0 (org greenfield + MuleSoft on-premise + gateway) → modelo de dados fundacional (Fase 1) → E05 (integração) → E03 (folha/split) → homologação → estabilização.

**Leitura honesta:** a janela é agressiva para o escopo XL do financeiro regulado sobre três pré-requisitos externos de lead-time. É entregável **como MVP**, com de-escopo (Agentforce, Data Cloud, Marketing Cloud, carga massiva, adoção completa) como buffer real. **A trilha tradicional (18–38 semanas por benchmark) não alcança 15/nov** — por isso o modelo AI-native não é escolha de custo, e sim de viabilidade de cronograma. **Se um pré-requisito da Fase 0 escorregar ou a homologação achar defeito no financeiro, 15/nov não é alcançável só com esforço — o de-escopo (E03 primeiro) é o único trilho.**

> *A duração por benchmark é baseada em benchmark, derivada dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Complexidade & Disciplinas

Dimensionamento por tamanho relativo de complexidade (T-shirt) — **não é esforço, não é conversível em horas nem multiplicável por uma taxa**: **3 XL** (E02 Marketplace, E03 Motor de Split, E05 Integração), **3 L** (E01, E06, E08), **3 M** (E04, E07, E09). E03 subiu de L para XL: o ADR 0003 confirmou que o motor de regras de split e a conciliação vivem no Salesforce — a premissa que o design havia sinalizado se realizou.

- **Especialista de arquitetura financeira/bancária**: E03 em XL exige um perfil sênior dedicado ao fluxo da folha, às regras de split, à conciliação e à integração com o gateway — adicionado ao roster de ambas as trilhas.
- **Gestão de mudança & adoção (E09)** entra como épica explícita: o alcance do programa — ~800 mil estabelecimentos e ~450 mil beneficiárias (a ratificar) — cria risco material de adoção e resistência (perda de margem no modelo transparente).
- **Governança & residência (E08)** precisa ser travada cedo: a fronteira campo-a-campo da tokenização e o isolamento greenfield/on-premise governam o data model — decidi-los tarde reescreve o modelo de dados. Reforça por que o **modelo de dados fundacional** (Fase 1) precede toda paralelização.

**Aceleração por IA na entrega**: os ganhos mais confiáveis estão na documentação regulatória; o build custom (leilão, motor de split, de-tokenização) captura menos por causa do esforço de revisão. A faixa AI-native (~28–38%) que sustenta a janela de 13 semanas é **condicional e provisória** — depende de um modelo operacional AI-native que a prontidão medida hoje (Low, 2/8) não exibe. É o risco #1 do estimate.

## Riscos e Mitigações

| Risco | Onde pesa | Mitigação |
|---|---|---|
| Lead-time da org greenfield + infra MuleSoft on-premise + seleção do gateway (risco #1 à data) | Fase 0 → 3 | Pedido no dia 1; escalonar com plataforma/cliente; contrato de integração mock na Fase 1 |
| Modelo de dados fundacional atrasa e bloqueia a paralelização | Fase 1 | Time inteiro no arranque; marco explícito antes de abrir frentes (ADR 0004) |
| Prontidão de IA baixa vs. modelo AI-native que a data exige | Programa | Nomear o gate AI-native; de-escopo como buffer; sign-off do Solution Lead |
| Ausência total de contratos de API (caminho crítico) | E05 / Fase 1 | Mock-first cedo; inventário na Fase 0; governança da virada mock→real |
| Fronteira de residência não ratificada | E08 / Fase 0-1 | Ratificar com a arquitetura Dataprev (Jair Bogo) antes do data model |
| Regras de split/conciliação indefinidas | E03 / Fase 3 | Definir na Fase 0/1 com o especialista financeiro; idempotência e trilha obrigatórias |
| Regras do leilão / Lei 14.133 indefinidas | E02 / Fase 2 | Workshop de regras antes do build do motor |
| Incerteza jurídica (ADI 7962 no STF) | Cronograma | Premissas dependentes de data carregam a ressalva; monitorar decisão |

## Premissas & Nível de Confiança

Coerente com um pré-venda antes da Fase 0: todos os 9 tamanhos permanecem **Assumed** enquanto os blockers de arquitetura (fronteira de residência, Novo PAT sem API, identidade gov.br × CPF, provedor do gateway) não são resolvidos. Premissas load-bearing agora formalizadas como ADRs: **residência híbrida (ADR 0001)**, **instância dedicada e apartada (ADR 0002)**, **fronteira CRM-não-transacional / motor de split (ADR 0003)**, **Sales Cloud reusando objetos nativos — Opportunity/Quote; facilitadora API-only, licença de portal só da beneficiária, versão a requalificar (ADR 0004)** e **greenfield + MuleSoft on-premise = soberania/isolamento (ADR 0005, resolve G0504)**. Os cinco ADRs são **scopezilla-recommended, Assumed, a ratificar com o cliente**; a instância dedicada segue **verbal, a ratificar por escrito**.

> **Dados a confirmar antes de uso client-facing**: a volumetria (~800 mil estabelecimentos, ~450 mil beneficiárias) foi falada em call e vem de imprensa citando o MTE, não de fonte primária — confirmar na origem antes de citar como fato.

## Próximos Passos e Recomendações

1. **Executar a Fase 0 imediatamente (17/ago)** — provisionar a org 100% greenfield + a infra do MuleSoft on-premise e iniciar a seleção do gateway (os três lead-times externos são o gargalo da data), e resolver os blockers.
2. **Ratificar com o cliente os cinco ADRs** — em especial a instância greenfield/dedicada (ADR 0002/0005), o modelo de objetos nativos Sales Cloud (ADR 0004) e a fronteira de residência (ADR 0001), todos ainda scopezilla-recommended/Assumed.
3. **Confirmar o modelo operacional AI-native** com o cliente — é o que torna a janela de 13 semanas viável; sem ele, o escopo do MVP encolhe mais.
4. **Confirmar a volumetria** e o provedor do gateway antes de qualquer artefato client-facing.

---

*Proof points de referência: metodologia Salesforce Professional Services (229% de ROI ao cliente, entrega ~35% mais rápida, 10.000+ recursos de entrega). Observação: não há pacote vertical de Governo configurado neste projeto — recomenda-se defini-lo para incorporar proof points específicos do setor público.*
