# Outline de Apresentação — Marketplace Digital do PAT (DATAPREV-PAT)

**Público:** executivo (DATAPREV / MTE — patrocinadores e decisores).
**Objetivo (o que muda depois):** alinhamento e sinal de avanço — ratificar os cinco ADRs e autorizar a Fase 0 no dia 17/ago.
**Fluência:** parcial em Salesforce → nomes de produto usados, padrões internos explicados em linguagem simples; sem códigos de épica em tela.
**Big idea:** a reforma do PAT tem data fixa e externa (15/nov/2026); construímos a plataforma pública neutra em 13 semanas sobre Sales Cloud nativo — **a data é o âncora, o escopo é a variável de flexão.**
**Arco:** Situação → Complicação → Resolução. **Tom:** autoritativo (confiante, breve, fatos antes de entusiasmo).
**Nomes travados:** Sales Cloud (Opportunity/Quote nativos) · Experience Cloud (portal da beneficiária) · MuleSoft (integração on-premise) · Agentforce (fora do MVP) · gov.br (identidade).

---

## Logic chain (a frase que cada slide precisa aterrissar)

1. Capa — abre o assunto.
2. **Situação:** o Decreto 12.712/2025 é a maior reforma do PAT em ~50 anos e reescreve as regras econômicas do setor.
3. **Situação:** isso abre espaço para uma plataforma pública neutra — o que o MTE não tem hoje.
4. **Complicação:** a data de go-live é fixa, externa e regulatória — 15/nov/2026 — e a janela de construção é de ~13 semanas.
5. **Resolução:** a solução cabe em uma arquitetura — Sales Cloud nativo + MuleSoft on-premise + gateway do cliente.
6. **Resolução:** o leilão reverso mapeia em objetos nativos e a equidade é por construção (não por customização).
7. **Resolução:** o motor de split é o coração regulado — e o que dimensiona o financeiro como XL.
8. **Prova:** nove épicas cobrem o fluxo; o MVP entrega oito, com Agentforce como buffer.
9. **Prova:** cinco fases, planejadas de trás pra frente a partir da data fixa.
10. **Prova:** a espinha de segurança (isolamento + tokenização) está formalizada em cinco ADRs.
11. **Prova:** os riscos são conhecidos e mitigados — o maior é o lead-time da Fase 0.
12. **Ask (contexto):** o investimento indicativo, com a base transparente e o disclaimer.
13. **Ask:** executar a Fase 0 agora e ratificar os ADRs.

---

## Slide-a-slide

### Slide 1 — Capa
- **Título de ação:** Marketplace Digital do PAT — a plataforma pública da reforma
- **Existe porque:** abre o contexto e o patrocínio (DATAPREV para o MTE).
- **Conteúdo:** subtítulo "Do bilateral fragmentado ao leilão aberto — em jornada 100% gov.br". Data.
- **Visual:** capa (hero claro). **Densidade:** sparse.
- **Fonte:** executive-summary.md.

### Slide 2 — A reforma muda o jogo
- **Título de ação:** O Decreto 12.712/2025 reescreve as regras econômicas do vale-alimentação
- **Existe porque:** estabelece o "porquê agora" regulatório.
- **Conteúdo (stats):** teto de administração (MDR) **3,6%** · repasse ao estabelecimento em **15 dias** · **fim do rebate** + pré-pagamento obrigatório · **interoperabilidade** total até nov/2026.
- **Visual:** 4 stat tiles. **Densidade:** sparse.
- **Fonte:** executive-summary.md (Panorama).

### Slide 3 — A oportunidade
- **Título de ação:** A reforma abre espaço para uma plataforma pública neutra que o MTE não tem hoje
- **Existe porque:** transição da regra para a visão de transformação.
- **Conteúdo:** hoje = negociação bilateral fragmentada e opaca; amanhã = leilão aberto entre facilitadoras, visibilidade sistêmica do governo, org Salesforce 100% greenfield e apartada.
- **Visual:** card "hoje → amanhã". **Densidade:** balanced.
- **Fonte:** strategy.json (prioridades), executive-summary.md.

### Slide 4 — A data é fixa (a tensão)
- **Título de ação:** A data de go-live não é preferência — é regulatória, externa e fixa: 15/nov/2026
- **Existe porque:** é a complicação que governa todo o resto do deck.
- **Conteúdo:** início comprometido **17/ago** → homologação **início nov** → go-live PRODUÇÃO **15/nov**. Janela: **~13 semanas**. A trilha tradicional (18–38 semanas por benchmark) **não alcança** a data. *(ADI 7962 no STF — premissas dependentes de data carregam ressalva.)*
- **Visual:** stat tiles (13 semanas) + faixa de datas. **Densidade:** balanced.
- **Fonte:** executive-summary.md, roadmap, estimate-comparison.json.

### Slide 5 — A solução em uma imagem
- **Título de ação:** Uma plataforma sobre Sales Cloud nativo, com a integração no perímetro da DATAPREV
- **Existe porque:** dá a visão arquitetural única antes dos detalhes.
- **Conteúdo (camadas):** beneficiária/estabelecimento no **Experience Cloud** (gov.br) → **Sales Cloud** (Opportunity=demanda, Quote=resposta) → **MuleSoft on-premise** (Novo PAT, gov.br, eSocial, facilitadoras, gateway) → **gateway do cliente** (custódia/execução bancária, fora do CRM).
- **Visual:** diagrama de camadas (CSS). **Densidade:** balanced.
- **Fonte:** 01-solution.md, executive-summary.md (ADR 0003/0004/0005).

### Slide 6 — Leilão reverso, equidade por construção
- **Título de ação:** As facilitadoras respondem só por API — logo não veem a proposta concorrente, sem regra custom de ocultamento
- **Existe porque:** é o diferencial de design mais elegante da solução.
- **Conteúdo:** beneficiária registra a demanda (Opportunity) no portal → ~600–700 facilitadoras respondem exclusivamente via API (Quote), sem tela → no MVP descobrem as demandas por **endpoint de consulta (pull)**; notificação ativa (push) é roadmap futuro, canal a definir → beneficiária compara lado a lado, **seleciona só quando a vigência fecha** → termo de aceite. Contrato sem CLM (PDF imutável versionado).
- **Visual:** fluxo de 4 passos (chips/setas). **Densidade:** balanced.
- **Fonte:** executive-summary.md (E02), 01-solution.md.

### Slide 7 — O motor financeiro
- **Título de ação:** O Salesforce é o motor de regras de split — não transaciona nem custodia dinheiro
- **Existe porque:** explica a fronteira CRM×financeiro e por que o financeiro é XL.
- **Conteúdo:** recebe a folha (CSV) → valida → calcula e aplica o rateio sob o teto MDR 3,6% e repasse de 15 dias → aciona o gateway para boletagem → concilia por casamento via MuleSoft → registra o racional. Execução bancária e custódia ficam no gateway do cliente.
- **Visual:** card + tag XL. **Densidade:** balanced.
- **Fonte:** executive-summary.md (E03, ADR 0003).

### Slide 8 — Escopo
- **Título de ação:** Nove épicas cobrem o fluxo completo; o MVP comprometido entrega oito
- **Existe porque:** mostra o escopo e o buffer honesto (Agentforce fora).
- **Conteúdo (tabela):** as 9 épicas com tamanho relativo (T-shirt) — 3 XL (Marketplace, Motor de Split, Integração), 3 L, 3 M. Agentforce (L) marcado "fora do MVP — buffer".
- **Visual:** tabela com tags de tamanho. **Densidade:** dense.
- **Fonte:** estimates.json, executive-summary.md.
- *Nota:* tamanho = complexidade relativa, **não** esforço/horas/preço (dito em nota de rodapé do slide).

### Slide 9 — Roadmap
- **Título de ação:** Cinco fases, planejadas de trás pra frente a partir da data fixa
- **Existe porque:** mostra a viabilidade de cronograma e o caminho crítico.
- **Conteúdo (timeline):** Fase 0 Arranque/Provisionamento (2 sem) · Fase 1 Fundação (4 sem) · Fase 2 Marketplace & Credenciamento (3 sem) · Fase 3 Financeiro/Split (3 sem) · Fase 4 Homologação & Go-live (1 sem). Marco: modelo de dados fundacional libera a paralelização.
- **Visual:** timeline de fases. **Densidade:** balanced.
- **Fonte:** roadmap, executive-summary.md (Abordagem).

### Slide 10 — Segurança & residência
- **Título de ação:** Isolamento + tokenização são a espinha de segurança — formalizados em cinco decisões de arquitetura
- **Existe porque:** cobre a preocupação de compliance (LGPD, TCU/CGU/ANPD) de um público de governo.
- **Conteúdo:** CPF e dados sensíveis **não persistem** na nuvem — ficam na DATAPREV, resolvidos em runtime por MuleSoft (LGPD Art. 11); org 100% greenfield e apartada; MuleSoft on-premise = soberania de dados. Cinco ADRs (residência híbrida, instância dedicada, fronteira não-transacional, objetos nativos, greenfield/on-premise).
- **Visual:** cards dos 5 ADRs. **Densidade:** balanced.
- **Fonte:** executive-summary.md (Destaques, Premissas), decisions/.

### Slide 11 — Riscos & mitigações
- **Título de ação:** Os riscos são conhecidos — o maior é o lead-time externo da Fase 0
- **Existe porque:** honestidade executiva; antecipa a objeção de viabilidade.
- **Conteúdo (tabela):** lead-time org greenfield + MuleSoft on-premise + gateway (risco #1) → pedir no dia 1; modelo de dados atrasa → time inteiro no arranque; prontidão de IA vs. modelo AI-native → nomear o gate + de-escopo como buffer; ausência de contratos de API → mock-first; incerteza jurídica ADI 7962 → ressalva + monitorar.
- **Visual:** tabela risco/mitigação com tags de severidade. **Densidade:** dense.
- **Fonte:** executive-summary.md (Riscos).

## Approved Commercials

### Slide 12 — Investimento indicativo
- **Título de ação:** Investimento indicativo do MVP na janela fixa: R$ 3,74M (com imposto)
- **Existe porque:** o público pediu a cifra; entra com base transparente e disclaimer.
- **Conteúdo (stats):** R$ 3.740.984 com imposto (R$ 3.495.950 sem) · trilha AI-native · janela fixa de 13 semanas · roster de 11 funções PS. **Ponto indicativo, não faixa; escopo é a variável de flexão.**
- **Visual:** stat tiles + disclaimer box. **Densidade:** balanced.
- **Fonte:** commercials.md / commercials.json.
- **Disclaimer (verbatim, Validated-Rate):** "*This range is based on the rate of the official Salesforce PS LATAM rate table (per-role, R$ 573,98–R$ 884,68/h sem imposto, mapeado por função no roster) you supplied and validated on 2026-07-31. Indicative for planning only; final commercial structure is confirmed through the applicable commercial agreement.*"

## Slide-a-slide (continuação)

### Slide 13 — O pedido
- **Título de ação:** Executar a Fase 0 agora e ratificar os cinco ADRs — a data não espera
- **Existe porque:** fecha com a ação concreta (o objetivo do deck).
- **Conteúdo:** 1) Fase 0 em 17/ago — provisionar org greenfield + MuleSoft on-premise + selecionar gateway. 2) Ratificar os cinco ADRs. 3) Confirmar o modelo operacional AI-native. 4) Confirmar volumetria + provedor do gateway.
- **Visual:** panorama de fechamento (navy) com a frase-âncora. **Densidade:** sparse.
- **Fonte:** executive-summary.md (Próximos Passos).

---

## Speaker notes (resumo)
- **S4 é o pivô** — pare aqui. A data fixa é o que torna todo o resto não-negociável; se a plateia aceitar a data, aceita o de-escopo como mecânica de segurança.
- **S6** — é o slide que impressiona um arquiteto: equidade sem custom é design, não sorte. Esteja pronto para "e se a facilitadora tiver tela?" (resposta: não tem — é API-only por ADR 0004).
- **S8** — sempre diga que T-shirt é complexidade relativa, não horas nem preço, antes que alguém multiplique.
- **S12** — leia o disclaimer. É preço indicativo derivado de rate validado, não custo, não margem, não fixed-fee. O número se move com o escopo.
- **S13** — a transição é "a data não espera": o único risco real à data é o lead-time da Fase 0, e ele começa a correr no dia 1.
