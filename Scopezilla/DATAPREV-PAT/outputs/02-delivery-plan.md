# Plano de Entrega — DATAPREV-PAT (Reforma do PAT / MTE)

**Duração total do programa: 13 semanas (compromisso do usuário).** Modo **data-fixa, planejado de trás pra frente** a partir do go-live imóvel de **15/nov/2026** (marco de interoperabilidade total do Decreto 12.712/2025 + entrada do financeiro em produção). Proposta assinada ~15/ago/2026.

> **A data é o âncora; o escopo é a variável de flexão.** O programa não comprime 18–38 semanas de trabalho em 13 — ele entrega um **MVP** dimensionado para a janela e mantém um conjunto de **candidatos a de-escopo** como buffer de cronograma. Se um risco de caminho crítico se materializar (provisionamento, gateway PCI, contratos de API), o buffer é acionado antes da data.

**Leitura honesta do arquiteto:** esta é uma janela **agressiva** para o escopo em jogo — três épicas XL (E02, E03, E05), integração multi-sistema sem contratos e uma prontidão de IA baixa. É entregável **como MVP** com o de-escopo abaixo tratado como buffer real, disciplina de caminho crítico na Fase 0/1 e uma janela de estabilização mínima. Não é entregável como escopo completo. As alavancas de segurança do cronograma estão nomeadas — não escondidas.

---

## Caminho crítico

**Fase 0 (provisionamento da org dedicada + contratação do gateway PCI) → E05 (hub de integração) → E03 (motor de split & conciliação) → estabilização.**

Escorregões de terceiros na Fase 0 (lead-time de provisionamento e de contratação do gateway PCI) são o **maior risco** à data fixa — não estão sob controle da entrega. E01/E02/E04 dependem de E05; E03 depende de E05 + E08 + o gateway contratado. Qualquer atraso cascateia direto para o go-live.

---

## Sequência de fases

### Fase 0 — Arranque, Provisionamento & Arquitetura (2 semanas)
- **Épicas:** — (fase de destrave, sem build)
- Provisionar a **instância dedicada e apartada** (ADR 0002); **selecionar/contratar o provedor do gateway PCI** (G0309, ADR 0003); resolver os blockers de arquitetura (fronteira de residência G0801, contratos de API G0501, hospedagem MuleSoft G0504, identidade × CPF-não-persiste G0106).
- **Sai com:** org acessível, parceiro de gateway definido, ADR 0001 ratificado, inventário de contratos de API.

### Fase 1 — Fundação: Identidade + Integração + Residência (4 semanas) · *depende de: Fase 0*
- **Épicas:** E05 (hub MuleSoft mock-first, gateway PCI como alvo), E08 (residência/tokenização na org dedicada), E01 (portal Experience Cloud + login gov.br).
- Fase de maior carga; risco #1 (integração sem contratos) atacado primeiro. Comunicação de mudança (E09) arranca aqui.

### Fase 2 — Marketplace & Credenciamento (3 semanas) · *depende de: Fase 1 (E01, E05)*
- **Épicas:** E02 (leilão reverso — propostas ocultas até o fechamento, seleção manual, contrato fora da plataforma; **MVP sem Data Cloud**), E04 (credenciamento gov.br PJ/CNPJ).

### Fase 3 — Financeiro: Motor de Regras de Split & Conciliação (3 semanas) · *depende de: Fase 0 (gateway PCI), Fase 1 (E05, E08)*
- **Épicas:** E03 (**XL** — Salesforce calcula/aplica split com teto MDR 3,6% e repasse ≤15 dias, emite boletagem com split, concilia por casamento, recebe movimentações; execução/custódia FORA = gateway PCI do cliente).
- Fase XL mais sensível à data fixa; se algo escorrega, a pressão de de-escopo bate aqui.

### Fase 4 — Carga Mínima, Adoção & Estabilização/Go-live (1 semana) · *depende de: Fase 1 (E05)*
- **Épicas:** E07 (carga inicial **mínima**; Novo PAT permanece system-of-record), E09 (adoção enxuta, pico da comunicação).
- Janela de estabilização/hypercare mínima até 15/nov. Carga massiva e adoção completa ficam pós-go-live.

---

## Candidatos a de-escopo (buffer de cronograma)

Ordenados por primeiro-a-cair. Tratados como buffer — entram no MVP só se a janela permitir; saem primeiro se um risco de caminho crítico se materializar.

| # | Item | Épica | Justificativa |
|---|------|-------|---------------|
| 1 | **Agentforce — atendimento inteligente** | E06 (inteira) | Valor real, mas não é pré-requisito do go-live regulatório; canal WhatsApp/BSP + guardrails públicos somam risco e prazo. Fora do MVP. |
| 2 | **Data Cloud — enriquecimento/perfil** | E02 | Adição Assumed; o leilão reverso funciona sem ele. |
| 3 | **Marketing Cloud / alertas** | E02/E06 | Ambiguidade de escopo (G0209); não bloqueia o fluxo core. |
| 4 | **Carga massiva de dados** | E07 | MVP carrega o mínimo; volume completo pós-go-live. |
| 5 | **Adoção completa** | E09 | MVP entrega capacitação essencial; programa completo de adoção pós-go-live. |

---

## Processos padrão (transversais, não repetidos por fase)

- **Testes:** contínuos; QA amplifica-se e **surge** na janela de estabilização (financeiro regulado, data fixa) — não encolhe sob IA.
- **Deploy:** entregas incrementais na org dedicada; release management coordenado ao longo das fases.
- **Capacitação/adoção:** E09 transversal, comunicação desde a Fase 1, pico na Fase 4.

---

## Tabela de riscos consolidada

| Risco | Fase | Mitigação | Gap |
|-------|------|-----------|-----|
| Lead-time de provisionamento da org dedicada | 0 | Pedido no dia 1 da Fase 0; escalonar com a plataforma | ADR 0002 |
| Contratação/integração do gateway PCI atrasa | 0→3 | Selecionar cedo; contrato de integração mock na Fase 1 | G0309 |
| Contratos de API inexistentes (mock→real) | 1 | Mock-first; governança de virada; inventário na Fase 0 | G0501 |
| Fronteira de residência não ratificada | 0→1 | Ratificar com Jair Bogo antes do data model | G0801 |
| Regras de split/conciliação indefinidas | 3 | Definir na Fase 0/1; especialista de arquitetura financeira | G0304 |
| Janela de estabilização mínima | 4 | QA surge; hypercare desde o D-0; buffer de de-escopo | — |
| Volume de carga desconhecido | 4 | Carga mínima no MVP; massiva pós-go-live | G0701 |

---

## Equipe

As disciplinas e o roster nomeado para entregar isto — com contagens defensáveis, por lane — vêm do **`estimate`**. Este documento é funcionalidade ao longo do tempo; não nomeia time. Observação para o `estimate`: E03 agora XL exige um **especialista de arquitetura financeira/bancária (split)** no roster de ambas as lanes, e a janela fixa de ~13 semanas precisa ser reconciliada com as faixas de duração derivadas.
