# Sumário Executivo — Marketplace Digital do PAT (DATAPREV-PAT)

## Visão Geral (At a Glance)

- **Dor atual**: contratação de vale-alimentação fragmentada e opaca; MTE sem visibilidade sistêmica sobre a operação.
- **Visão de transformação**: PAT como mercado digital único, transparente e concorrencial, em jornada 100% gov.br.
- **Principais motores de valor**: jornada única gov.br, leilão automatizado entre facilitadoras, fluxo financeiro digital sob repasse de 15 dias.
- **Maior risco**: timeline agressiva (set→nov/2026) abaixo do piso de benchmark, com integrações sem contratos de API.
- **Primeiro passo recomendado**: Fase 0 (Discovery & Arquitetura) para resolver os quatro blockers antes do compromisso final de escopo e prazo.

---

## Panorama

O Decreto nº 12.712/2025 promove a maior reforma do PAT em quase 50 anos: comprime a margem das operadoras (teto de administração — MDR — de 3,6%, tarifa de intercâmbio de 2%) e exige repasse ao estabelecimento em até 15 dias e interoperabilidade. Isso abre espaço para uma **plataforma pública neutra, operada pela Dataprev para o Ministério do Trabalho e Emprego (MTE)**, que substitui a negociação bilateral fragmentada de hoje por um leilão aberto entre facilitadoras — dando ao governo visibilidade sistêmica sobre um setor que movimenta R$ 150–200 bilhões/ano e atende mais de 22 milhões de trabalhadores.

**Por que agora:** o decreto entra em vigor a partir de 10/02/2026 e o Novo PAT exige recadastramento obrigatório sob pena de perda do benefício fiscal. A janela para instrumentalizar a fiscalização e a transparência da reforma é imediata — atrasar significa operar a nova regra sem plataforma que a suporte e sem visibilidade para o MTE.

## Escopo

Nove épicas cobrem o fluxo completo em quatro módulos, mais os habilitadores transversais:

- **Marketplace de cotação e contratação (E02)** — o coração da reforma: cotação → propostas de N facilitadoras → comparação lado a lado → seleção → contrato.
- **Folha & Financeiro (E03)** — folha, boleto/Pix, conta custódia e split governo/facilitadora sob a regra de 15 dias.
- **Portal & Identidade gov.br (E01)** e **Credenciamento (E04)** — jornada autenticada única e cadastro unificado de estabelecimentos.
- **Integração Corporativa MuleSoft (E05)** — camada API-led para Novo PAT, gov.br, eSocial e as ~600–700 facilitadoras.
- **Atendimento Inteligente Agentforce (E06)**, **Migração & Carga (E07)**, **Segurança & Residência de Dados (E08)**, **Gestão de Mudança & Adoção (E09)**.

## Destaques da Solução

- **Uma plataforma, quatro capacidades nativas**: portal externo autenticado (Experience Cloud sobre gov.br), motor de processos e estados de negócio (Core/Service Cloud), integração corporativa (MuleSoft) e atendimento em escala (Agentforce) — encurtando o caminho para a timeline do programa.
- **Leilão reverso é build custom na Core Platform** (objetos Cotacao__c 1→N Proposta__c + automação): não há capability nativa Salesforce para leilão reverso, o que dimensiona E02 como a épica de maior complexidade de construção.
- **Residência de dados híbrida (ADR 0001)**: CPF e dados sensíveis **não persistem** na nuvem Salesforce — ficam na Dataprev e são resolvidos em runtime via referências tokenizadas por MuleSoft, aderente à LGPD (Art. 11) e à auditoria de TCU/CGU/ANPD.
- **Métodos que protegem o prazo**: mock-first nas integrações (desbloqueia o desenvolvimento antes dos contratos de API) e configurar-antes-de-customizar.

## Abordagem de Implementação

Cinco fases sequenciadas por caminho crítico — **E05/E08 (fundação) → E01 → E02/E03**:

- **Fase 0 — Discovery & Arquitetura**: resolve os quatro blockers (fronteira da residência, contratos de API, hospedagem MuleSoft × residência, identidade gov.br × CPF).
- **Fase 1 — Fundação** (E05, E08, E01): integração mock-first e modelo de residência primeiro, de propósito — o risco #1 é atacado cedo.
- **Fase 2 — Marketplace** (E02, E04) · **Fase 3 — Financeiro & Atendimento** (E03, E06) · **Fase 4 — Carga, Adoção & Estabilização** (E07, E09).

**Duração por benchmark: 18–38 semanas**, derivada top-down da forma do engajamento (Multi-Cloud + integração de dados, entre Medium e High; alargada por adders de risco — regulada, integração sem contratos de API, interface custom do leilão).

> *Este número é baseado em benchmark, derivado dos dados de treinamento do modelo de IA e de padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados por meio do acordo comercial aplicável.*

**A janela do cliente (set→nov/2026, ~15–16 semanas) está abaixo do piso de 18 semanas**, antes mesmo de qualquer compressão por IA. A recomendação é tratar a **Fase 0** como destravadora e o **escopo como variável de flexão** contra a data — decidir com o cliente o que entra em cada marco (homologação vs. produção).

## Complexidade & Disciplinas

Dimensionamento por tamanho relativo de complexidade (T-shirt) — **não é esforço, não é conversível em horas nem multiplicável por uma taxa**: 2 XL (E02 Marketplace, E05 Integração), 4 L (E01, E03, E06, E08), 3 M (E04, E07, E09). Para faixa de prazo, veja a duração por benchmark acima; para preço indicativo, é necessário rodar `commercials` com uma taxa validada.

- **Gestão de mudança & adoção (E09)** entra como épica explícita porque o alcance do programa — 600–700 facilitadoras e centenas de milhares de beneficiárias — cria risco material de adoção e resistência (perda de margem no modelo transparente); deixá-la implícita é o caminho para retrabalho e baixa adoção pós go-live.
- **Governança & residência (E08)** precisa ser travada cedo: a fronteira campo-a-campo da tokenização governa o data model de E01/E02/E03/E06 — decidi-la tarde reescreve o modelo de dados.

**Aceleração por IA na entrega**: uma faixa realizada de **~10–18%** (prontidão atual Low) em ritmo e qualidade, dentro da mesma forma de time — não é redução de equipe nem insumo de preço. Os ganhos mais confiáveis estão na documentação regulatória; o build custom (leilão, de-tokenização) captura menos por causa do esforço de revisão. Uma faixa maior (~28–38%) é possível apenas sob um modelo operacional AI-native — condicional e provisória, exigindo um compromisso de forma de trabalho que um programa gov com gates de conformidade não exibe hoje.

## Riscos e Mitigações

| Risco | Onde pesa | Mitigação |
|---|---|---|
| Ausência total de contratos de API (risco #1, caminho crítico) | E05 / Fase 1 | Mock-first cedo; inventário na Fase 0; governança da virada mock→real |
| Fronteira de residência não ratificada | E08 / Fase 1 | Ratificar com a arquitetura Dataprev na Fase 0, antes do data model |
| Janela do cliente abaixo do piso do benchmark | Programa | Fase 0 destravadora + escopo como variável de flexão contra a data |
| Banco custódia/PSP e conciliação indefinidos | E03 / Fase 3 | Definir na Fase 0/1; idempotência e trilha obrigatórias |
| Regras do leilão / Lei 14.133 indefinidas | E02 / Fase 2 | Workshop de regras antes do build do motor |
| Incerteza jurídica (ADI no STF sobre o decreto) | Cronograma | Premissas dependentes de datas carregam a ressalva; monitorar decisão |

## Premissas & Nível de Confiança

**Confiança atual: 28% Confirmed / 72% Assumed** — coerente com um pré-venda antes da Fase 0. Todos os 9 tamanhos permanecem **Assumed** enquanto os quatro blockers de arquitetura não são resolvidos; 65 gaps mapeados (acima do limiar de 15) sustentam a recomendação de **Fase 0 antes do compromisso final**. Premissas load-bearing incluem: org única com residência resolvida por tokenização, DevOps source-driven, e o escopo de E09 (fronteira PS vs. Dataprev) a confirmar.

> **Dados a confirmar antes de uso client-facing**: o número de empresas beneficiárias diverge entre fontes (~450 mil citado em discovery vs. ~300–327,7 mil em fontes oficiais/imprensa); os números de 22 mi trabalhadores e ~800 mil estabelecimentos vêm de imprensa citando o MTE, não de fonte primária. Confirmar na origem antes de citar como fato.

## Próximos Passos e Recomendações

1. **Executar a Fase 0** — resolver os quatro blockers e reconfirmar os tamanhos, apertando a faixa de 18–38 semanas.
2. **Decidir a estratégia de marco contra a data** — o que entra em homologação (set) vs. produção (15/nov), com escopo como variável de flexão.
3. **Ratificar a fronteira de residência** (ADR 0001) com a arquitetura Dataprev antes de fixar o data model.
4. **Confirmar os dados divergentes** de volume antes de qualquer artefato client-facing.

---

*Proof points de referência: metodologia Salesforce Professional Services (229% de ROI ao cliente, entrega ~35% mais rápida, 10.000+ recursos de entrega). Observação: não há pacote vertical de Governo configurado neste projeto — recomenda-se defini-lo para incorporar proof points específicos do setor público. Os proof points aqui são os padrão de Salesforce PS.*
