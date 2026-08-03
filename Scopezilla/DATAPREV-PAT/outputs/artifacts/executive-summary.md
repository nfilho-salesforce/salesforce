# Sumário Executivo — Marketplace Digital do PAT (DATAPREV-PAT)

## Visão Geral (At a Glance)

- **Dor atual**: contratação de vale-alimentação fragmentada e opaca; MTE sem visibilidade sistêmica sobre a operação.
- **Visão de transformação**: PAT como mercado digital único, transparente e concorrencial, em jornada 100% gov.br, numa **org Salesforce 100% greenfield e apartada** do MTE/PAT, construída sobre **Sales Cloud** reusando objetos nativos para encurtar o tempo de implementação.
- **Principais motores de valor**: jornada única gov.br, leilão reverso entre facilitadoras sobre **objetos nativos Sales Cloud** (Opportunity = demanda; Quote = resposta via API), e o **Salesforce como motor de regras de split** sob o teto de MDR de 3,6% e repasse em 15 dias do Decreto 12.712/2025.
- **Maior risco**: a data de go-live é **fixa e externa (15/nov/2026)**, o escopo do financeiro é XL e regulado, e dois destravamentos externos (provisionamento da org 100% greenfield; seleção/contratação do gateway) somados a acessos/ambientes/capacidade na instalação MuleSoft on-premise **existente** (reuso, ADR 0006) precedem o build — se um escorregar, a data não é alcançável só com esforço e o de-escopo (E03) é o único trilho.
- **Primeiro passo recomendado**: **Fundação (17/ago – 13/set, Semanas 1-4)** — definir o modelo de dados fundacional com o time inteiro, provisionar a org 100% greenfield, selecionar o gateway e confirmar acessos/ambientes/capacidade na instalação MuleSoft on-premise já existente da Dataprev (a definição de arquitetura foi mesclada a esta fase — não há mais Etapa 0 isolada). Os dois destravamentos externos aqui são o maior risco à data fixa.

---

## Panorama

O Decreto nº 12.712/2025 promove a maior reforma do PAT em quase 50 anos: comprime a margem das operadoras (teto de administração — MDR — de 3,6%), exige **repasse ao estabelecimento em até 15 dias**, pré-pagamento obrigatório, fim do rebate e **interoperabilidade** (grandes operadoras a partir de mai/2026, total até nov/2026). Isso abre espaço para uma **plataforma pública neutra, operada pela Dataprev para o Ministério do Trabalho e Emprego (MTE)**, que substitui a negociação bilateral fragmentada de hoje por um leilão aberto entre facilitadoras — dando ao governo visibilidade sistêmica sobre um setor que movimenta centenas de bilhões de reais por ano.

**Por que agora:** o marco de **interoperabilidade total e a entrada do financeiro em produção estão fixados em 15/nov/2026**. A data não é uma preferência — é regulatória e externa. A janela de construção, com **início comprometido em 17/ago** e **homologação a partir da entrega do Marketplace**, é de **17 semanas (13 de build + 4 de Scale/Hypercare)**. Atrasar significa operar a nova regra sem plataforma que a suporte. *(A ADI 7962 tramita no STF sobre o decreto — premissas dependentes de data carregam a ressalva.)*

## Escopo

Nove épicas cobrem o fluxo completo. O **Fase 1 comprometido para 15/nov entrega oito delas**; a nona (Agentforce) é o primeiro candidato a de-escopo, tratado como buffer de cronograma.

- **Marketplace de cotação e contratação (E02, XL)** — o coração da reforma, sobre **Opportunity/Quote nativos**: a beneficiária registra a demanda de leilão reverso (**Opportunity**) → facilitadoras respondem **exclusivamente via API** (**Quote**) — sem acesso à plataforma, informando o ID da cotação aberta na vigência. Na Fase 1 elas **descobrem as demandas abertas por um endpoint de consulta (pull via API)** — a notificação ativa (push) é roadmap futuro, com o canal a definir (o que decide se posicionamos ou não Marketing Cloud). A **equidade é por construção** (a facilitadora não tem tela, logo não vê a proposta concorrente — sem regra de ocultamento custom). A beneficiária acompanha as cotações conforme chegam (comparação lado a lado), mas **só pode selecionar quando a janela de vigência fecha** (seleção manual travada, não cega) → **termo de aceite**. Contrato **sem CLM** (PDF imutável versionado).
- **Folha, Motor de Split & Conciliação (E03, XL)** — o Salesforce recebe a folha (CSV via portal/API), valida layout/integridade, disponibiliza à facilitadora, **calcula e aplica o rateio** sob o teto de MDR de 3,6% e o repasse de 15 dias, aciona o gateway para boletagem, **concilia por casamento** em lotes incrementais via MuleSoft e registra todo o racional. A execução bancária e a custódia ficam **fora** (gateway, selecionado pelo cliente); as linhas da folha **não persistem** em objeto (roadmap futuro).
- **Portal & Identidade gov.br (E01, L)** — portal **Experience Cloud** da beneficiária com login gov.br (versão de licença a requalificar — Partner Community expõe Opportunity/Quote, Customer Community Plus não) — e **Credenciamento (E04, M)** com cadastro via gov.br PJ/CNPJ + **vigilância sanitária** (triagem IA + alertas de vencimento de licença).
- **Integração Corporativa MuleSoft (E05, XL)** — camada API-led rodando sobre a instalação **on-premise já existente da Dataprev (reuso, ADR 0006)** para Novo PAT (sem API hoje — mock obrigatório), gov.br, eSocial, as facilitadoras e o **gateway**. Frente contínua liderada por um Arquiteto Técnico MuleSoft dedicado, do início da Fundação ao fim do build (Semanas 1-11).
- **Atendimento Inteligente Agentforce (E06, L — fora da Fase 1)**, **Migração & Carga (E07, M)**, **Segurança & Residência de Dados (E08, L)**, **Gestão de Mudança & Adoção (E09, M)**.

## Destaques da Solução

- **Sales Cloud reusando objetos nativos (ADR 0004)**: a plataforma é construída sobre **Sales Cloud**, reusando funcionalidade nativa para encurtar o tempo de implementação. O leilão reverso mapeia em objetos nativos — **Opportunity** = demanda registrada pela beneficiária; **Quote** = resposta da facilitadora recebida via API. Quem opera esses objetos no **portal Experience Cloud** é a **beneficiária** (o estabelecimento também acessa); a **facilitadora é API-only** e não consome licença de portal — as ~600–700 facilitadoras são integrações, não assentos. A versão de licença da beneficiária (Partner Community vs. Customer Community Plus) segue a requalificar contra o padrão de acesso real.
- **MuleSoft reusa a instalação on-premise existente (ADR 0006, supersede parcial da ADR 0005)**: a Dataprev já opera MuleSoft on-premise em produção — o programa **reusa** essa plataforma em vez de provisionar uma nova. Isso elimina o lead-time de aprovisionamento do MuleSoft (a antiga Etapa 0) e permite mesclar a definição de arquitetura ao Planning & Design da Fundação. Segue como o mecanismo de **soberania de dados** (a integração fica no perímetro Dataprev) e resolve o gap de hospedagem do MuleSoft (G0504) — agora como reuso, não instalação nova. Resta a dependência de acessos/ambientes/capacidade na instalação existente.
- **Instância Salesforce 100% greenfield e apartada (ADR 0002, inalterada)**: reforça o isolamento — forçada por segurança, volumetria, auditabilidade (TCU/CGU/ANPD) e administração pelo cliente. O provisionamento tem lead-time externo e é um dos dois destravamentos externos que precedem o build. O reuso do MuleSoft (ADR 0006) é exclusivo da camada de integração — a org Salesforce permanece greenfield.
- **Fronteira CRM × financeiro (ADR 0003)**: o Salesforce é o **motor de regras de split** e o orquestrador da conciliação — não transaciona nem custodia dinheiro. Ele aciona a boletagem com o split aplicado; o **gateway do cliente** intermedia a conta custódia, executa as transações bancárias e devolve as movimentações para o CRM conciliar. É o que dimensiona E03 como XL.
- **Residência de dados híbrida (ADR 0001)**: CPF e dados sensíveis **não persistem** na nuvem Salesforce — ficam na Dataprev e são resolvidos em runtime via referências tokenizadas por MuleSoft, aderente à LGPD (Art. 11) e à auditoria de TCU/CGU/ANPD. Isolamento (greenfield + on-premise) + tokenização são a espinha de segurança do programa.
- **Métodos que protegem a data fixa**: **definição fundacional de objetos + mapeamento de dados com o time inteiro primeiro**, depois paralelização das frentes de baixa dependência; mock-first nas integrações (Novo PAT sem API hoje) e configurar-antes-de-customizar (reforçado pelo reuso nativo do Sales Cloud).

## Abordagem de Implementação

**Modo data-fixa, planejado de trás pra frente. Datas comprometidas: início 17/ago/2026 → homologação (UAT) a partir da entrega do Marketplace → go-live PRODUÇÃO 15/nov/2026 → Scale/Hypercare 16/nov–13/dez/2026. Duração total: 17 semanas — 13 de build (Fase 1) + 4 de Scale/Hypercare. A data é o âncora; o escopo é a variável de flexão.** Seis fases sequenciadas por caminho crítico, com a **paralelização** como estratégia central de viabilidade:

- **Fundação — Modelo de Dados + Arquitetura + Identidade + Integração + Residência (17/ago – 13/set · 4 sem · S1-S4)**: inicia na **Semana 1** — a definição de arquitetura, antes isolada numa Etapa 0, foi **mesclada ao Planning & Design** (ADR 0006, MuleSoft reusa a instalação on-premise existente da Dataprev, eliminando o lead-time de aprovisionamento). Arranca com o **time inteiro definindo os objetos nativos fundacionais e o mapeamento de dados (ADR 0004)** — o marco que libera a paralelização. Em paralelo: provisionar a org **100% greenfield** (ADR 0002, inalterada), selecionar o gateway (ADR 0003) e confirmar acessos/ambientes/capacidade na instalação MuleSoft on-premise existente (ADR 0006). Épicas E05 (frente MuleSoft, agora contínua), E08 (residência), E01 (portal gov.br).
- **Marketplace & Credenciamento (14/set – 25/out · 6 sem · S5-S10, 2 sprints de 3 semanas)** — frente paralelizada (E02 sobre Opportunity/Quote nativos, sem Data Cloud; E04 com vigilância sanitária). Ancora o início da UAT.
- **Financeiro — Folha, Motor de Split & Conciliação (21/set – 1/nov · 6 sem · S6-S11)** (E03, XL) — paralela ao Marketplace, arrancando junto em S6; o fluxo folha→pagamento→split completo; a fase XL mais sensível à data fixa.
- **Homologação (UAT) — a partir da entrega do Marketplace (5/out – 14/nov · 6 sem · S8-S13)**: antecipada em relação ao plano anterior (+1 semana de UAT), corre em paralelo às frentes conforme cada uma entrega.
- **Carga Mínima, Adoção & Go-live PROD (2/nov – 15/nov · 2 sem · S12-S13)** (E07, E09) — carga inicial mínima nas duas últimas semanas; Novo PAT permanece system-of-record. **Marcos: projeto (go-live PROD 15/nov), decreto (interoperabilidade total), jornada (UAT→PROD).**
- **Scale / Hypercare (16/nov – 13/dez · 4 sem · S14-S17)** — pós-go-live, time enxuto reusando perfis do build; escopo restrito a **sustentar, manter e conduzir o cutover** para a Dataprev; sem novo desenvolvimento.

A frente **MuleSoft (E05)** corre continuamente por todo o Planning & Design e desenvolvimento (S1-S11), sob um Arquiteto Técnico MuleSoft dedicado.

**Caminho crítico**: Fundação (modelo de dados fundacional, S1-S4) → E05 frente MuleSoft contínua (S1-S11) → E03 (folha/split, frente Financeiro paralela S6-S11) → homologação (S8-S13) → carga mínima (S12-S13) → go-live 15/nov → Scale/Hypercare (S14-S17).

**Leitura honesta:** a janela de build continua agressiva para o escopo XL do financeiro regulado. Restam dois destravamentos externos — **provisionamento da org 100% greenfield** (ADR 0002) e **seleção/contratação do gateway** (ADR 0003) — mais **acessos, ambientes e capacidade** na instalação MuleSoft on-premise existente (ADR 0006); o antigo pré-requisito "instalação on-premise pronta a tempo" caiu com o reuso. É entregável **como Fase 1**, com de-escopo (Agentforce, Data Cloud, Marketing Cloud, carga massiva, adoção completa) como buffer real. **A trilha tradicional (18–38 semanas por benchmark) não alcança 15/nov** — por isso o modelo AI-native não é escolha de custo, e sim de viabilidade de cronograma. **Se um destravamento escorregar ou a homologação achar defeito no financeiro, 15/nov não é alcançável só com esforço — o de-escopo (E03 primeiro) é o único trilho.**

> *A duração por benchmark é baseada em benchmark, derivada dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Complexidade & Disciplinas

Dimensionamento por tamanho relativo de complexidade (T-shirt) — **não é esforço, não é conversível em horas nem multiplicável por uma taxa**: **3 XL** (E02 Marketplace, E03 Motor de Split, E05 Integração), **3 L** (E01, E06, E08), **3 M** (E04, E07, E09). E03 subiu de L para XL: o ADR 0003 confirmou que o motor de regras de split e a conciliação vivem no Salesforce — a premissa que o design havia sinalizado se realizou.

- **Especialista de arquitetura financeira/bancária**: E03 em XL exige um perfil sênior dedicado ao fluxo da folha, às regras de split, à conciliação e à integração com o gateway — adicionado ao roster de ambas as trilhas.
- **Gestão de mudança & adoção (E09)** entra como épica explícita: o alcance do programa — ~800 mil estabelecimentos e ~450 mil beneficiárias (a ratificar) — cria risco material de adoção e resistência (perda de margem no modelo transparente).
- **Governança & residência (E08)** precisa ser travada cedo: a fronteira campo-a-campo da tokenização e o isolamento greenfield/on-premise (agora on-premise reusado, ADR 0006) governam o data model — decidi-los tarde reescreve o modelo de dados. Reforça por que o **modelo de dados fundacional** (Fundação, S1-S4) precede toda paralelização.

**Aceleração por IA na entrega**: os ganhos mais confiáveis estão na documentação regulatória; o build custom (leilão, motor de split, de-tokenização) captura menos por causa do esforço de revisão. A faixa AI-native (~28–38%) que sustenta a janela de 13 semanas de build é **condicional e provisória** — depende de um modelo operacional AI-native que a prontidão medida hoje (Low, 2/8) não exibe. É o risco #1 do estimate.

## Riscos e Mitigações

| Risco | Onde pesa | Mitigação |
|---|---|---|
| Lead-time da org greenfield + seleção do gateway + acessos à instalação MuleSoft existente (risco #1 à data) | Fundação → Financeiro | Pedido no dia 1; escalonar com plataforma/cliente; contrato de integração mock na Fundação |
| Modelo de dados fundacional atrasa e bloqueia a paralelização | Fundação | Time inteiro no arranque; marco explícito antes de abrir frentes (ADR 0004) |
| Prontidão de IA baixa vs. modelo AI-native que a data exige | Programa | Nomear o gate AI-native; de-escopo como buffer; sign-off do Solution Lead |
| Ausência total de contratos de API (caminho crítico) | E05 / Fundação | Mock-first cedo; inventário na Fundação; governança da virada mock→real |
| Fronteira de residência não ratificada | E08 / Fundação | Ratificar com a arquitetura Dataprev (Jair Bogo) antes do data model |
| Regras de split/conciliação indefinidas | E03 / Financeiro | Definir na Fundação com o especialista financeiro; idempotência e trilha obrigatórias |
| Regras do leilão / Lei 14.133 indefinidas | E02 / Marketplace | Workshop de regras antes do build do motor |
| Incerteza jurídica (ADI 7962 no STF) | Cronograma | Premissas dependentes de data carregam a ressalva; monitorar decisão |

## Premissas & Nível de Confiança

Coerente com um pré-venda antes da resolução final dos blockers de arquitetura: todos os 9 tamanhos permanecem **Assumed** enquanto a fronteira de residência, Novo PAT sem API, identidade gov.br × CPF e o provedor do gateway não são resolvidos. Premissas load-bearing agora formalizadas como ADRs: **residência híbrida (ADR 0001)**, **instância dedicada e apartada (ADR 0002)**, **fronteira CRM-não-transacional / motor de split (ADR 0003)**, **Sales Cloud reusando objetos nativos — Opportunity/Quote; facilitadora API-only, licença de portal só da beneficiária, versão a requalificar (ADR 0004)**, **greenfield + MuleSoft on-premise = soberania/isolamento (ADR 0005, superseded parcialmente pela ADR 0006)** e **MuleSoft reusa a instalação on-premise existente da Dataprev — a org Salesforce permanece 100% greenfield (ADR 0006)**. Os seis ADRs são **scopezilla-recommended, Assumed, a ratificar com o cliente**; a instância dedicada segue **verbal, a ratificar por escrito**.

> **Dados a confirmar antes de uso client-facing**: a volumetria (~800 mil estabelecimentos, ~450 mil beneficiárias) foi falada em call e vem de imprensa citando o MTE, não de fonte primária — confirmar na origem antes de citar como fato.

## Próximos Passos e Recomendações

1. **Arrancar a Fundação imediatamente (17/ago)** — definir o modelo de dados fundacional com o time inteiro, provisionar a org 100% greenfield, iniciar a seleção do gateway e confirmar acessos/ambientes/capacidade na instalação MuleSoft on-premise existente (os dois destravamentos externos são o gargalo da data), e resolver os blockers.
2. **Ratificar com o cliente os seis ADRs** — em especial a instância greenfield/dedicada (ADR 0002), o reuso do MuleSoft on-premise (ADR 0006, que supersede parcialmente a ADR 0005), o modelo de objetos nativos Sales Cloud (ADR 0004) e a fronteira de residência (ADR 0001), todos ainda scopezilla-recommended/Assumed.
3. **Confirmar o modelo operacional AI-native** com o cliente — é o que torna a janela de 13 semanas de build viável; sem ele, o escopo da Fase 1 encolhe mais.
4. **Confirmar a volumetria** e o provedor do gateway antes de qualquer artefato client-facing.

---

*Proof points de referência: metodologia Salesforce Professional Services (229% de ROI ao cliente, entrega ~35% mais rápida, 10.000+ recursos de entrega). Observação: não há pacote vertical de Governo configurado neste projeto — recomenda-se defini-lo para incorporar proof points específicos do setor público.*
