# Sumário Executivo — Marketplace Digital do PAT (DATAPREV-PAT)

## Visão Geral (At a Glance)

- **Dor atual**: contratação de vale-alimentação fragmentada e opaca; MTE sem visibilidade sistêmica sobre a operação.
- **Visão de transformação**: PAT como mercado digital único, transparente e concorrencial, em jornada 100% gov.br, numa **instância Salesforce dedicada e apartada** do MTE/PAT.
- **Principais motores de valor**: jornada única gov.br, leilão automatizado entre facilitadoras, e o **Salesforce como motor de regras de split** sob o teto de MDR de 3,6% e repasse em 15 dias do Decreto 12.712/2025.
- **Maior risco**: a data de go-live é **fixa e externa (15/nov/2026)** e a trilha tradicional não a alcança — só o modelo AI-native com escopo de MVP fecha a janela, num programa cuja prontidão de IA medida hoje é baixa.
- **Primeiro passo recomendado**: **Fase 0** (provisionamento da org dedicada + contratação do gateway PCI + destrave dos blockers de arquitetura) — os lead-times externos aqui são o maior risco à data fixa.

---

## Panorama

O Decreto nº 12.712/2025 promove a maior reforma do PAT em quase 50 anos: comprime a margem das operadoras (teto de administração — MDR — de 3,6%), exige **repasse ao estabelecimento em até 15 dias**, pré-pagamento obrigatório, fim do rebate e **interoperabilidade** (grandes operadoras a partir de mai/2026, total até nov/2026). Isso abre espaço para uma **plataforma pública neutra, operada pela Dataprev para o Ministério do Trabalho e Emprego (MTE)**, que substitui a negociação bilateral fragmentada de hoje por um leilão aberto entre facilitadoras — dando ao governo visibilidade sistêmica sobre um setor que movimenta centenas de bilhões de reais por ano.

**Por que agora:** o marco de **interoperabilidade total e a entrada do financeiro em produção estão fixados em 15/nov/2026**. A data não é uma preferência — é regulatória e externa. A janela de construção, a partir de uma proposta assinada por volta de 15/ago, é de **~13 semanas**. Atrasar significa operar a nova regra sem plataforma que a suporte. *(A ADI 7962 tramita no STF sobre o decreto — premissas dependentes de data carregam a ressalva.)*

## Escopo

Nove épicas cobrem o fluxo completo. O **MVP comprometido para 15/nov entrega oito delas**; a nona (Agentforce) é o primeiro candidato a de-escopo, tratado como buffer de cronograma.

- **Marketplace de cotação e contratação (E02, XL)** — o coração da reforma: cotação → propostas **ocultas** de N facilitadoras até o fechamento → comparação lado a lado → seleção manual da beneficiária → contrato fora da plataforma.
- **Motor de Regras de Split & Conciliação (E03, XL)** — o Salesforce **calcula e aplica o rateio** (governo/facilitadora/estabelecimento) sob o teto de MDR de 3,6% e o repasse de 15 dias, **emite a boletagem já com o split aplicado**, orquestra e **concilia por casamento**. A execução bancária e a custódia ficam **fora** (gateway PCI, contratado pelo cliente).
- **Portal & Identidade gov.br (E01, L)** e **Credenciamento (E04, M)** — jornada autenticada única e cadastro unificado de estabelecimentos via gov.br PJ/CNPJ.
- **Integração Corporativa MuleSoft (E05, XL)** — camada API-led para Novo PAT, gov.br, eSocial, as facilitadoras e o **gateway PCI**.
- **Atendimento Inteligente Agentforce (E06, L — fora do MVP)**, **Migração & Carga (E07, M)**, **Segurança & Residência de Dados (E08, L)**, **Gestão de Mudança & Adoção (E09, M)**.

## Destaques da Solução

- **Instância dedicada e apartada (ADR 0002)**: o MTE/PAT roda numa instância Salesforce isolada — forçada por segurança, volumetria, auditabilidade (TCU/CGU/ANPD) e administração pelo cliente. O provisionamento tem lead-time externo e é um pré-requisito de Fase 0.
- **Fronteira CRM × financeiro (ADR 0003)**: o Salesforce é o **motor de regras de split** e o orquestrador da conciliação — não transaciona nem custodia dinheiro. Ele emite a boletagem com o split aplicado; o **gateway PCI do cliente** executa as transações bancárias, custodia e devolve as movimentações para o CRM conciliar. É o que dimensiona E03 como XL.
- **Residência de dados híbrida (ADR 0001)**: CPF e dados sensíveis **não persistem** na nuvem Salesforce — ficam na Dataprev e são resolvidos em runtime via referências tokenizadas por MuleSoft, aderente à LGPD (Art. 11) e à auditoria de TCU/CGU/ANPD. Isolamento + tokenização são a espinha de segurança do programa.
- **Leilão reverso é build custom na Core Platform** (objetos Cotacao__c 1→N Proposta__c + automação): não há capability nativa Salesforce para leilão reverso, o que dimensiona E02 como uma das épicas de maior complexidade.
- **Métodos que protegem a data fixa**: mock-first nas integrações (desbloqueia o desenvolvimento antes dos contratos de API) e configurar-antes-de-customizar.

## Abordagem de Implementação

**Modo data-fixa, planejado de trás pra frente a partir de 15/nov/2026. Duração total: 13 semanas (compromisso do usuário). A data é o âncora; o escopo é a variável de flexão.** Cinco fases sequenciadas por caminho crítico:

- **Fase 0 — Arranque, Provisionamento & Arquitetura (2 sem)**: provisionar a instância dedicada (ADR 0002), selecionar/contratar o gateway PCI (ADR 0003) e resolver os blockers (fronteira de residência, contratos de API, hospedagem MuleSoft, identidade gov.br × CPF). **Os lead-times externos aqui são o maior risco à data.**
- **Fase 1 — Fundação (4 sem)** (E05, E08, E01): integração mock-first, modelo de residência na org dedicada e portal gov.br — o risco #1 atacado cedo.
- **Fase 2 — Marketplace & Credenciamento (3 sem)** (E02 sem Data Cloud, E04).
- **Fase 3 — Motor de Split & Conciliação (3 sem)** (E03) — a fase XL mais sensível à data fixa.
- **Fase 4 — Carga Mínima, Adoção & Estabilização (1 sem)** (E07, E09) — hypercare mínimo até o go-live.

**Caminho crítico**: Fase 0 (provisionamento + gateway PCI) → E05 (integração) → E03 (motor de split) → estabilização.

**Leitura honesta:** a janela é agressiva para três épicas XL e integração sem contratos. É entregável **como MVP**, com de-escopo (Agentforce, Data Cloud, Marketing Cloud, carga massiva, adoção completa) como buffer real. **A trilha tradicional (18–38 semanas por benchmark) não alcança 15/nov** — por isso o modelo AI-native não é escolha de custo, e sim de viabilidade de cronograma.

> *A duração por benchmark é baseada em benchmark, derivada dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

## Complexidade & Disciplinas

Dimensionamento por tamanho relativo de complexidade (T-shirt) — **não é esforço, não é conversível em horas nem multiplicável por uma taxa**: **3 XL** (E02 Marketplace, E03 Motor de Split, E05 Integração), **3 L** (E01, E06, E08), **3 M** (E04, E07, E09). E03 subiu de L para XL: o ADR 0003 confirmou que o motor de regras de split e a conciliação vivem no Salesforce — a premissa que o design havia sinalizado se realizou.

- **Especialista de arquitetura financeira/bancária**: E03 em XL exige um perfil sênior dedicado às regras de split, à conciliação e à integração com o gateway PCI — adicionado ao roster de ambas as trilhas.
- **Gestão de mudança & adoção (E09)** entra como épica explícita: o alcance do programa — ~800 mil estabelecimentos e ~450 mil beneficiárias (a ratificar) — cria risco material de adoção e resistência (perda de margem no modelo transparente).
- **Governança & residência (E08)** precisa ser travada cedo: a fronteira campo-a-campo da tokenização e o isolamento da instância dedicada governam o data model — decidi-los tarde reescreve o modelo de dados.

**Aceleração por IA na entrega**: os ganhos mais confiáveis estão na documentação regulatória; o build custom (leilão, motor de split, de-tokenização) captura menos por causa do esforço de revisão. A faixa AI-native (~28–38%) que sustenta a janela de 13 semanas é **condicional e provisória** — depende de um modelo operacional AI-native que a prontidão medida hoje (Low, 2/8) não exibe. É o risco #1 do estimate.

## Riscos e Mitigações

| Risco | Onde pesa | Mitigação |
|---|---|---|
| Lead-time de provisionamento da org dedicada + contratação do gateway PCI (risco #1 à data) | Fase 0 → 3 | Pedido no dia 1; escalonar com plataforma/cliente; contrato de integração mock na Fase 1 |
| Prontidão de IA baixa vs. modelo AI-native que a data exige | Programa | Nomear o gate AI-native; de-escopo como buffer; sign-off do Solution Lead |
| Ausência total de contratos de API (caminho crítico) | E05 / Fase 1 | Mock-first cedo; inventário na Fase 0; governança da virada mock→real |
| Fronteira de residência não ratificada | E08 / Fase 0-1 | Ratificar com a arquitetura Dataprev (Jair Bogo) antes do data model |
| Regras de split/conciliação indefinidas | E03 / Fase 3 | Definir na Fase 0/1 com o especialista financeiro; idempotência e trilha obrigatórias |
| Regras do leilão / Lei 14.133 indefinidas | E02 / Fase 2 | Workshop de regras antes do build do motor |
| Incerteza jurídica (ADI 7962 no STF) | Cronograma | Premissas dependentes de data carregam a ressalva; monitorar decisão |

## Premissas & Nível de Confiança

Coerente com um pré-venda antes da Fase 0: todos os 9 tamanhos permanecem **Assumed** enquanto os blockers de arquitetura (fronteira de residência, contratos de API, hospedagem MuleSoft, identidade gov.br × CPF, provedor do gateway PCI) não são resolvidos. Premissas load-bearing agora formalizadas como ADRs: **residência híbrida (ADR 0001)**, **instância dedicada e apartada (ADR 0002)** e **fronteira CRM-não-transacional / motor de split (ADR 0003)**. A instância dedicada segue **verbal, a ratificar por escrito**.

> **Dados a confirmar antes de uso client-facing**: a volumetria (~800 mil estabelecimentos, ~450 mil beneficiárias) foi falada em call e vem de imprensa citando o MTE, não de fonte primária — confirmar na origem antes de citar como fato.

## Próximos Passos e Recomendações

1. **Executar a Fase 0 imediatamente** — provisionar a org dedicada e iniciar a contratação do gateway PCI (lead-times externos são o gargalo da data), e resolver os blockers.
2. **Ratificar por escrito a instância dedicada (ADR 0002)** e a fronteira de residência (ADR 0001) com a arquitetura Dataprev.
3. **Confirmar o modelo operacional AI-native** com o cliente — é o que torna a janela de 13 semanas viável; sem ele, o escopo do MVP encolhe mais.
4. **Confirmar a volumetria** e o provedor do gateway PCI antes de qualquer artefato client-facing.

---

*Proof points de referência: metodologia Salesforce Professional Services (229% de ROI ao cliente, entrega ~35% mais rápida, 10.000+ recursos de entrega). Observação: não há pacote vertical de Governo configurado neste projeto — recomenda-se defini-lo para incorporar proof points específicos do setor público.*
