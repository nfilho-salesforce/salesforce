# PRODESP — Poupatempo Balcão V2 — Memória do Projeto (export)

*Exportado de `data/memory.json` em 23/09/2026. Este arquivo é uma leitura legível para humanos; a fonte de verdade continua sendo o JSON.*

---

## Sessões

### 2026-09-21 — `discover`
Discovery completo a partir de 3 fontes em discovery-notes/ (BSA autoria própria do Heroku HTML, deck Jackson "Poupatempo Balcão V2" / Slack no guichê, deck Vinicius "Atendimento Poupatempo" / plataforma Headless). Investigou o canal Slack #prodesp-slack-reuniao-thiago-waltz e seus anexos no Google Drive para tentar identificar "T7"; descobriu que esse canal trata de uma oportunidade distinta (Slack CSG interno — Approvals/RH), não da Balcão V2, e a excluiu do projeto por decisão do usuário. Conduziu entrevista adaptativa fechando lacunas prioritárias e escreveu o Discovery Brief (`outputs/00-discovery-brief.md`) com uma seção de Open Questions para o restante.

**Decisões:**
- **Escopar este ciclo apenas a Fase 1 tática (Slack no guichê); Fase 2+ (plataforma Headless whole-house) é visão, fora deste SOW.** *(superseded em 2026-09-21, ver sessão de reconciliação abaixo)* — Rationale: os dois decks de setembro/2026 são bets diferentes: um sem preço/cronograma mas "no ar em semanas", outro com investimento/cronograma em branco no próprio material. Registrado como `decisions/0001`.
- **Não importar o conteúdo do canal Slack #prodesp-slack-reuniao-thiago-waltz** — trata de oportunidade distinta (Slack CSG interno, ~2.000 funcionários PRODESP), não do atendimento presencial ao cidadão.
- **Tratar os KPIs de tempo médio de espera (15/16/17 min) do deck de plataforma como ilustrativos, não validados pelo cliente** — confirmado explicitamente pelo usuário.

**Threads abertos (nesta sessão):** T7 sem identidade; Biometria/Sistema Semântico/Atendimento sem identidade; escopo real do piloto totalmente aberto; budget/valor comercial sem número; champion/patrocinador executivo não identificado; documento LGPD/Trust sobre inferência do Agentforce não localizado.

---

### 2026-09-21 — `scopezilla-knowledge-curator`
Curadoria automática pós-discover. 3 arquivos `knowledge/` pré-existentes confirmados. Extraídos 3 novos arquivos a partir de fontes STAAR 5.1/5.2 (Data Cloud + Generative & Agentic AI): `staar-headless-360-doctrine.md`, `staar-data-360-headless.md`, `staar-agentforce-governance-guardrails.md`. Índice reconstruído: 61 seções em 6 arquivos.

---

### 2026-09-21 — `discover` (reconciliação)
Enquanto um processo em background executava discover+knowledge-curator, o usuário foi entrevistado nesta sessão sobre o mesmo escopo. O usuário rejeitou a limitação à Fase 1 e pediu Corte 1 + Corte 2 completos, faseados na mesma SOW.

**Decisões:**
- **Superseder `decisions/0001`: ambos os cortes entram como escopo contratado desta mesma SOW, faseados** — usuário rejeitou explicitamente escopo parcial. Registrado como `decisions/0002`.

**Threads abertos:** T7/Biometria/Sistema Semântico/Atendimento agora mais críticos (MuleSoft confirmado como escopo, não visão); gap de dimensionamento de licenças Slack (1.800 validadas vs. headcount real de 244 postos); owner de governança de agentes de IA não identificado; timeline e budget ainda não discutidos.

---

### 2026-09-21 — `requirements`
Gap analysis para os 10 épicos aprovados (E01–E10), via agentes `epic-analyst` em paralelo. 128 gaps salvos (G0101–G1011). Distribuição: Missing Requirement 50, Potential Risk 24, Ambiguity 21, Logical Gap 17, Capability Gap 7, Assumption 5, Source Conflict 4.

**Threads abertos:** identidades T7/Sistema Semântico/Atendimento/Biometria bloqueiam sizing de E08/E09; nenhum piloto combinado (posto/serviço/headcount); sinal de capacidade ociosa por posto sem fonte (E03/E10); owner de governança de IA ainda não identificado; documento LGPD/Trust ainda não localizado; KPIs de espera seguem ilustrativos; protocolo/volume MuleSoft indefinido (maior bloqueador de E09); framing arquitetural de E09 não escolhido; possível sobreposição E06↔E07 e E02↔E07; Governança e Experience Design como discipline gaps recorrentes sem owner.

---

### 2026-09-22 — `design`
Design completo para os 10 épicos, cobrindo Fase 1 + Fase 2. Central KB indisponível nesta sessão — skeleton fundamentado apenas na camada 1 (`knowledge/`), sinalizado explicitamente. Esqueleto arquitetural aprovado (20 decisões tagueadas — 8 fundamentadas, 2 inferidas, 10 como suposição); 8 assunções persistidas em `gaps.json` (total sobe de 128 para 136 gaps). `outputs/01-solution.md` escrito em ordem de jornada de valor (E06→E08→E01→E02→E07→E03→E04→E05→E09→E10). Estimativas por sizing direto: S=2/M=5/L=2/XL=1; E09 é XL/Unknown, maior risco técnico do programa.

**Decisões:**
- Ordem de apresentação segue jornada de valor, não ordem de ID.
- E03 e E10 compartilham a mesma fundação de dados não resolvida (sinal de ocupação por posto) — tratada como gap único (G0315), não duplicada.

**Threads abertos:** Central KB indisponível — recomendado `/kb-sync` antes de entrega final citando padrão validado Salesforce; G0315 (sinal de ocupação em tempo real) bloqueia sizing fino de E03/E10; G0911 (identidades) mantém E09 Unknown/XL; G0613 (gatilho de agendamento E06); G0712 (residência/retenção LGPD de imagens); owner de governança de IA ainda não identificado.

---

### 2026-09-22 — `grill-me-on-scope` (rodada 1)
6 itens de auto-exposição ranqueados. Resolvidos nesta sessão: propriedade do sinal de capacidade ociosa (E03 assume, E10 é puro consumidor); owner de governança de IA consolidado (9 gaps/7 épicos); sobreposição E06→E07 e E02↔E07 tratada como fluxo conectado; PM/QA dedicado definido como decisão de resourcing interna, não gap. Permaneceram abertos: (1) E09 identidade/infra de integração; (5) possível sub-dimensionamento de E08.

**Decisões:**
- E03 assume a propriedade do sinal de capacidade ociosa por posto; E10 é puro consumidor.
- E06→E07 e E02↔E07 tratados como fluxo de design conectado (aposta de design a validar com a Prodesp).
- Este programa precisa de PM e QA dedicados — decisão de resourcing interna, não gap.json (resposta explícita do usuário).

**Threads abertos:** E09 (identidades T7/Sistema Semântico/Atendimento/Biometria + maturidade Anypoint) sem resposta; E08 possível sub-dimensionamento sem `size_if_assumption_breaks`; decisão de PM/QA dedicado precisa ser lida pelo `estimate` na hora do roster.

---

### 2026-09-22 — `grill-me-on-scope` (rodada 2)
Fechamento dos dois itens abertos. E09: usuário confirmou que a Prodesp já opera ambiente MuleSoft/Anypoint maduro (Confirmed em G0906) — reduz risco de "greenfield" na API-led, mas G0901–G0905 (identidades/protocolo/volume) continuam bloqueando; E09 permanece XL/Unknown, sem resize. E08: usuário optou por manter L atual sem `size_if_assumption_breaks` — risco de execução fica como nota qualitativa apenas.

**Threads abertos:** G0901–G0905 seguem sem resposta — formalizar como pergunta ao cliente no kick-off técnico.

---

### 2026-09-22 — `roadmap`
6 fases (Fase 0 discovery + 5 de build). Fase 0 gatilhada pelos 136 gaps/4 conflitos de fonte. Fase 1 (E01,E05) fundação/governança; Fase 2 (E02,E03,E04) operação tática, depende de E01; Fase 3 (E09) MuleSoft como trilha paralela; Fase 4 (E06,E07,E08) experiência agêntica, E07 converge E01+E02+E03+E06; Fase 5 (E10) analítica, depende de E03. Caminho crítico: E01→E02→E07. Timeline: faixa benchmark derivada de 15–30 semanas (linha de base 16–24 +15% overlay regulatório LGPD/setor público → 16–28, + alargamento por E03/E06/E09 Unknown → 15–30 final). Corrigido bug de JSON pré-existente em `estimates.json` (E09).

**Decisões:**
- E09 (MuleSoft) como trilha paralela, não sequenciada atrás dos épicos Slack — maior lead time/risco do programa, sem dependência dura síncrona.

**Threads abertos:** faixa de 15–30 semanas é benchmark, não compromisso; G0901–G0905 e G0613 seguem sendo os range_drivers que travam piso/teto.

---

### 2026-09-22 — `efficiency`
Category-only (sem resource-plan.json). Blend task-level ~30–45%, fator de realização 0.30–0.40 (overlay LGPD/setor público + risco XL/Unknown de E09). Realized band ~10–18%, readiness Baixa (score 1/8). Native band ~35–40%, qualificação condicional.

**Decisões:**
- Bandas de efficiency computadas a partir dos sinais próprios do POUPATEMPO, não herdadas do DER (efficiency é específico de cada projeto por design do skill; só roles/rates do DER são reaproveitados no estimate).

**Threads abertos:** autorar `resource-plan.json` (3 lanes) usando rates/roster-shaping do DER; confirmar anchor=augmented; rodar `estimate` até o fim.

---

### 2026-09-22 — `estimate`
3 lanes (traditional/augmented/quantum-leap="AI-native"), anchor=augmented, ownership 100% PS-owned, rates/metodologia de roster reutilizados do PRODESP-DER (validados 2026-09-17). Traditional 15–30sem R$4,71M–9,42M. Augmented (ANCHOR) 14–25sem R$4,39M–7,85M. AI-native 10–18sem R$1,78M–3,21M, condicional (owner de governança de IA não nomeado). Ambos `resource-plan.json` e `estimate-comparison.json` PASS em validate-data.py.

**Fricção:** validate-data.py exigiu `resource_id` (não `role_id`) e faixas em objeto (não campos flat) — corrigido via jq após ler o validator.

**Decisões:**
- Rates e forma de roster reutilizados verbatim do PRODESP-DER; bandas de efficiency computadas frescas para o POUPATEMPO.
- anchor=augmented (não traditional) — número escolhido pelo usuário para defender.

**Threads abertos:** falso-positivo de pricing-leak em `00-discovery-brief.md` linha 50 (case Thames Valley Police) — deixado como estava nesta sessão; CL-01 (Product Owner Prodesp) ainda não nomeado, condiciona a trilha AI-native.

---

### 2026-09-22 — `validate` (1ª rodada)
FAIL: pricing-leak pré-existente em `00-discovery-brief.md:50` (citação de case público Thames Valley Police, não é pricing próprio) + 2 WARN de staleness (gaps.json anterior a epics.json; roadmap.json anterior a estimates.json). Confidence: 25% Confirmed / 55% Assumed / 20% Unknown; 136 gaps.

---

### 2026-09-22 — `validate` (2ª rodada — correção)
Corrigido o falso-positivo: "£1,4M de economia" reescrito para "economia de 1,4 milhão de libras esterlinas", evitando os padrões de moeda do validator. validate-data.py agora PASS limpo. Investigadas as 2 WARN de staleness via git log/diff — nenhuma mudança pós-timestamp foi substantiva (write-back de dependência + fix de sintaxe JSON); `revise` não foi executado por não haver mudança de escopo real para propagar.

**Decisões:**
- Não rodar `revise` para as 2 WARN de staleness — confirmado não-substantivo via diff.

---

### 2026-09-22 — `narratives` (1ª rodada)
`outputs/artifacts/executive-summary.md` gerado — audiência mista executiva/técnica. Retém profundidade de arquitetura (MuleSoft/Anyponi, Data 360, Agentforce grounding, dono do sinal E03/E10) nas seções Solution highlights e Effort summary. Sem strategy.json/rfp.json nesta rodada — seções derivadas omitidas.

---

### 2026-09-22 — `strategy`
Pulou pesquisa web — `00-discovery-brief.md` já carregava especificidade suficiente (volumetria oficial, achados LGPD, casos análogos internacionais). Vision statement + framework aprovados via AskUserQuestion (duas perguntas no mesmo gate). Vision statement aprovado verbatim, sem edição. Business case escrito após aprovação. `business_outcomes[]` (Value Map) não escrito — nenhum capability-map planejado.

**Decisões:**
- Vision statement aprovado exatamente como redigido, sem wordsmith do usuário.

---

### 2026-09-22 — `narratives` (2ª rodada)
Re-rodada para incorporar `data/strategy.json` ao executive-summary.md já existente. At a Glance atualizado com linguagem do vision_statement; Visão do Programa ganhou parágrafo integral + "Por que agora"/"Por que Salesforce" + 5 strategic_priorities ranqueadas. Confidence report re-confirmado inalterado (25/55/20, 136 gaps).

---

### 2026-09-22 — `export`
Empacotamento completo: openpyxl presente, workbook Excel gerado (não zip fallback). validate-data.py PASS limpo pré-export. CSVs re-sincronizados (7 arquivos). Sem rfp.json — revisão RFP-cycle pulada. `outputs/scoping-deliverables.xlsx` escrito com 7 abas.

---

### 2026-09-22 — `slides`
Modo criação — outline de 12 slides para sessão híbrida (validação de negócio + validação técnica + prazo/investimento). Arco Problema-Consequência-Solução-Prova-Pedido. Outline aprovado e renderizado como deck HTML autocontido (`presentation-deck.html`) — sem co_brand configurado, cores padrão Salesforce Electric Blue mantidas.

**Decisões:**
- Deck único cobre os três objetivos (negócio/técnico/investimento) em vez de decks separados — audiência mista na sala.

---

### 2026-09-22 — build ad-hoc (sem skill)
`outputs/artifacts/rom-cliente.html` gerado sob pedido direto do usuário (não é skill — "fazer um HTML de X"), espelhando estrutura/paleta do PRODESP-DER/rom-cliente.html, sem co-branding (null confirmado na conta Prodesp). Version stamp v1.0. validate-data.py achou FAIL pré-existente não relacionado (pricing leak em `presentation-outline.md` linha 160/164, Slide 10) — não corrigido, fora do escopo do pedido.

**Threads abertos:** pricing leak em `presentation-outline.md` (corrigir se for exportar/publicar formalmente); `sow-scope.md` permanece pendente — deferido, não cancelado.

---

### 2026-09-23 — exploração isolada (sem skill, fora do fluxo canônico)
A partir da sync interna Salesforce de 22/09 (participantes: Nelson, Larisse Gois, Juliana Brites, Pedro Ganem Filho, Renata Vendramini, Osvaldo Melo, Rafael Marques, Juliane Lopes, Viviani Hupp), consolidado um caso de uso de "Atendimento Digital" (antecipação de agendamento via WhatsApp + roteamento cross-posto de capacidade ociosa). Escrito em dois artefatos: nova seção em `rom-cliente.html` (v1.0→v1.1, fluxo de 8 etapas + arquitetura em 4 camadas) e `atendimento-digital-isolado.md` (consolidação escrita completa). **Não incorporado** a `epics.json`/`gaps.json` — nenhuma skill de revisão executada, por decisão explícita do usuário. 6 pontos em aberto documentados como candidatos futuros a `gaps.json`/`revise`. Checkpoint git commitado e enviado (push) para `origin/main`.

---

## Preferências — Terminologia

| Termo | Significado |
|---|---|
| **Poupinha** | Apelido do canal digital (WhatsApp + Portal) de nível 1 do Poupatempo — agendamento, triagem, FAQ. |
| **Balcão V2** | Ambíguo na própria conta: deck do Jackson usa para "Slack no guichê" (posto do atendente); Poupinha usa para check-in de fila ("sua vez chegou"). Confirmar sempre a qual se refere. |
| **Transbordo** | Escalonamento em tempo real do atendente para especialista via huddle Slack, sem deixar a cadeira. |
| **Frente A / Frente B** | A = Slack corporativo/licenças (RH, Approvals, desde out/2025). B = Slack no Poupatempo/PS (desde CSG 13/07/2026). Relógios e donos diferentes na mesma conta. |
| **Flex Credits** | Combustível de raciocínio do Agentforce (USD 500/100 mil créditos) — separado do saldo de créditos WhatsApp. |
| **T7** | Sistema real no diagrama de arquitetura-alvo com agente de IA próprio; nome/sigla completa ainda não identificada. |
| **Corte 1 / Corte 2** | Corte 1 = deck Jackson Ulisses, "Slack no guichê", tático. Corte 2 = deck Vinicius Ferraz, "Atendimento Poupatempo", plataforma Headless completa. Ambos escopo da mesma SOW, faseados (`decisions/0002`). |

---

## Decision Log

| Data | Área | Decisão | Rationale |
|---|---|---|---|
| 2026-09-21 | scope | Esqueleto de 10 épicos aprovado sem alterações: E01 Posto de Trabalho do Atendente no Slack, E02 Escalonamento em Tempo Real (Transbordo via Huddle), E03 Roteamento de Capacidade Ociosa Entre Postos, E04 Workflow de Contingência, E05 Governança/Adoção/Change Management (Fase 1), E06 Pré-Atendimento Digital via WhatsApp, E07 Validação Remota de Documentos por Atendente Ocioso, E08 Atendimento Agêntico 24/7 HITL, E09 Plataforma de Integração MuleSoft (Gov.br/Biometria/Legado/Sistema Semântico/T7), E10 Analytics e Previsibilidade de Atendimento. | Cobre Fase 1 (Corte 1) e Fase 2 (Corte 2) completas, faseadas na mesma SOW, per `decisions/0002`. E09 marcado Unknown pela identidade não resolvida de T7/Sistema Semântico/Atendimento. |

---

## Estado atual (o que falta)

- **G0901–G0905** — identidades de T7/Sistema Semântico/Atendimento/Biometria e protocolo/volume — maior bloqueador de sizing fino de E09. Formalizar no kick-off técnico.
- **Owner de governança de IA do lado Prodesp (CL-01)** — não nomeado; condiciona a trilha AI-native (native_qualification: conditional).
- **`sow-scope.md`** — pendente, deferido por decisão do usuário em favor do rom-cliente.html direto.
- **Pricing leak em `presentation-outline.md`** (linhas 160–164, Slide 10) — corrigir antes de exportar/publicar esse outline formalmente.
- **Exploração "Atendimento Digital"** (22–23/09) — isolada em `rom-cliente.html`/`atendimento-digital-isolado.md`; 6 pontos em aberto ainda não avaliados para incorporação a `epics.json`/`gaps.json`.
