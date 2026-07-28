# Plano de Entrega — DATAPREV-PAT (Marketplace Digital do PAT)

> **Roadmap por fases — funcionalidade ao longo do tempo.** Este documento sequencia *o quê* é entregue e *em que ordem*. Não nomeia equipe: as disciplinas e o quadro nominal para entregar isto — com contagens defensáveis, por trilha — vêm do `estimate`.

## Duração do programa

**Faixa por benchmark: 18–38 semanas** (derivada top-down da forma do engajamento — Multi-Cloud + integração de dados, shape entre Medium e High: 9 épicas, 2 XL + 4 L + 3 M, hub de integração multi-sistema + ~600-700 facilitadoras, 4 clouds; baseline de 16-26 semanas alargado por adders de risco — regulada, integração sem contratos de API, UI custom do leilão, todos os sizes ainda Assumed — teto limitado a +50%).

> *This figure is benchmark-based, derived from the AI model's training data and general delivery patterns (not Salesforce-validated) — not a commitment. Final figures are confirmed through the applicable commercial agreement.*

**A janela do cliente está abaixo do piso do benchmark.** O alvo em pauta (homologação set/2026, produção 15/nov/2026) equivale a ~15-16 semanas de calendário a partir de 28/jul — **abaixo do piso de 18 semanas, antes mesmo de qualquer compressão por IA**. Isso não é um "não dá"; é o argumento para (a) a **Fase 0** resolver os blockers que hoje seguram todos os sizes em Assumed, e (b) tratar o **escopo como variável de flexão** contra a data — decidir com o cliente o que entra em cada marco (homologação vs. produção). A faixa aperta quando os range-drivers abaixo são resolvidos.

**O que fixa o teto (range-drivers):**
- **E05 — Integração:** hub multi-sistema + ~600-700 APIs de facilitadoras, mock-first, sem nenhum contrato/Swagger. *Aperta com:* quantos sistemas têm contrato hoje e qual o modelo de onboarding das facilitadoras (API única padronizada vs. N integrações).
- **E03 — Financeiro:** boleto/Pix/split multi-parte com idempotência e conciliação; sobe a XL se exigir motor financeiro dedicado. *Aperta com:* qual banco custódia/PSP e se a mecânica de split/conciliação está definida.
- **E08 — Residência:** fronteira campo-a-campo não ratificada; governa o data model de E01/E02/E03/E06. *Aperta com:* ratificar com Jair Bogo o que é token vs. o que pode persistir (G0801).

**Reconciliação de analog:** SGP/MGI (Dataprev, MuleSoft + Agentforce, ~2.085h) é uma forma **menor** que o PAT — sem o hub de centenas de facilitadoras nem o leilão custom. Ancora o **piso** da faixa (um build Dataprev multi-produto aterrissa na casa das ~15-18 semanas); não puxa o teto para baixo.

## Caminho crítico

**E05/E08 (fundação) → E01 → E02/E03.** A residência (E08) e a integração (E05) destravam a identidade (E01), que destrava o marketplace (E02) e o financeiro (E03). Escorregão em qualquer elo da fundação cascateia por todo o cronograma.

## Sequência de fases

As fases mostram **posição na sequência e dependências** — sem semanas por fase (a faixa vive no nível do programa, acima; não há commitment de duração).

### Fase 0 — Discovery & Arquitetura *(posição 1 de 5)*
- **Épicas:** nenhuma (fase de resolução).
- **Objetivo:** resolver os quatro blockers antes do compromisso final — fronteira da residência (G0801, ratificar com Jair Bogo), contratos de API (G0501), hospedagem MuleSoft × residência (G0504), identidade Experience Cloud × CPF (G0106). Iniciar CTID/ANPD e o inventário das APIs das facilitadoras.
- **Saída:** os 9 sizes Assumed podem ser reconfirmados e a faixa apertada.
- **Disparada por:** 63 gaps > 15 (regra do produto).

### Fase 1 — Fundação (Identidade + Integração + Residência) *(posição 2 de 5)*
- **Épicas:** E05 (integração, mock-first), E08 (residência/segurança), E01 (portal + gov.br). *depende de: Fase 0.*
- **Objetivo:** erguer a base sobre a qual tudo renderiza. O risco #1 (E05, sem contratos) começa cedo, de propósito. A comunicação de mudança (E09) arranca aqui.
- **É front-loaded de propósito** — fundação + a integração de maior risco primeiro, para não descobrir o problema dos contratos no fim.

### Fase 2 — Marketplace (o coração) *(posição 3 de 5)*
- **Épicas:** E02 (cotação/leilão reverso), E04 (credenciamento). *depende de: E01, E05.*
- **Objetivo:** o valor mais visível da reforma — publicar cotação, receber propostas de N facilitadoras, comparar lado a lado, selecionar → contrato; credenciar estabelecimentos via gov.br.

### Fase 3 — Financeiro & Atendimento *(posição 4 de 5)*
- **Épicas:** E03 (folha/split/boleto/Pix), E06 (Agentforce). *depende de: E01, E05, E08 (E03); E05, E08 (E06).*
- **Objetivo:** fechar o fluxo — financeiro sob repasse ≤15 dias (a integração externa de maior risco) e atendimento inteligente informacional + transacional sem CPF em prompt.

### Fase 4 — Carga, Adoção & Estabilização *(posição 5 de 5)*
- **Épicas:** E07 (carga inicial), E09 (adoção — pico aqui; comms desde a Fase 1). *depende de: E05 (E07).*
- **Objetivo:** popular a plataforma com dedup/qualidade, conduzir o pico da capacitação/adoção, estabilizar/hypercare.

## Processos padrão (transversais, não repetidos por fase)

- **Testes:** unitário + integração contínuos; UAT em full sandbox com dado representativo antes de cada marco de go-live; hardening/QA concentrado na Fase 4 (go-live regulado com emissão financeira).
- **Deployment:** pipeline source-driven (Salesforce CLI + Git) Dev → QA → UAT → Produção.
- **Capacitação:** materiais e treinamento sob E09, com comunicação iniciada na Fase 1 pela escala das facilitadoras.
- **Virada mock→real (E05):** governança explícita de substituição dos mocks pelas APIs reais conforme os contratos surgem.

## Riscos consolidados

| Risco | Onde pesa | Mitigação |
|---|---|---|
| Ausência total de contratos de API (G0501) — risco #1, caminho crítico | E05 / Fase 1 | Mock-first cedo; inventário na Fase 0; governança de virada |
| Fronteira de residência não ratificada (G0801) | E08 / Fase 1 | Ratificar com Jair Bogo na Fase 0 antes do data model |
| Janela do cliente < piso do benchmark | Programa | Fase 0 + escopo como variável de flexão contra a data |
| Banco custódia/PSP e conciliação indefinidos (G0301/G0304) | E03 / Fase 3 | Definir na Fase 0/1; idempotência e trilha obrigatórias |
| Regras de leilão/Lei 14.133 indefinidas (G0202/G0203) | E02 / Fase 2 | Workshop de regras antes do build do motor |
| Resistência das facilitadoras (perda de margem) | E09 / Fases 1→4 | Comunicação antecipada; adoção medida |
| Volume de carga desconhecido (G0701) | E07 / Fase 4 | Band-widener; confirmar volume/fonte na Fase 0 |

## Próximo passo

As disciplinas e o quadro nominal para entregar isto — com contagens defensáveis, por trilha — vêm do `estimate`. A faixa de duração aperta à medida que os range-drivers (E05/E03/E08) são resolvidos, idealmente na Fase 0.
