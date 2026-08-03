# Análise de Eficiência de Entrega com IA — DATAPREV-PAT (Marketplace Digital do PAT)

## So What

**~8-12% de eficiência de entrega realizada com prontidão Low (estado atual).** É ganho de ritmo e qualidade dentro da mesma forma de time — não redução de headcount, não insumo de preço.

Onde os ganhos aparecem neste projeto:
- **Documentação & Gestão de Conhecimento** (~12-20%): onde o ganho mais confiável vive — E08, E09, E01; programa regulado gera muito documento estruturado que a IA rascunha bem.
- **Engenharia Técnica & QA** (~8-16%): E05, E02, E03; mock-first de E05 favorece a IA, mas o leilão custom (E02) e a de-tokenização em runtime (E08) ficam "fora da fronteira" e o review come o ganho.
- **Análise & Design** (~10-18%): E08, E02, E01; IA acelera minutas, o refinamento com Jair Bogo e a Lei 14.133 é humano.

**Onde a IA não ajuda**: alinhamento MTE × Dataprev × 600-700 facilitadoras, ratificação da fronteira de residência (G0801), regras do leilão/Lei 14.133 (G0202/G0203), incerteza jurídica (ADI/STF) — mais o build de maior imposto de IA: o leilão reverso custom (E02) e a lógica de de-tokenização em runtime (E08).

**Para subir a High readiness (~16-22%)**: aprovar Copilot/Claude em IDE dentro da fronteira de segurança, publicar política de manuseio de dados por IA sob LGPD, resolver contratos de API na Fundação.

> **⚠ Sobre o alvo de ≥25% do programa:** a banda augmented honesta (~10-18%) **não** alcança 25% para este engajamento regulado, integração-pesada e de baixa prontidão. Os 25% só aparecem na banda **AI-native condicional (~28-38%)** — gated e provisória (ver Nota de Honestidade), e que exige o cliente adotar um modelo operacional native. Não inflamos a banda augmented para atingir o alvo.

## Headline

**Realizada: ~10-18%** (Low readiness) · **Blend task-level: ~30-45%** · **Fator de realização: 0.30-0.40** — governo regulado + zero contratos de API puxam ao piso; org greenfield + mock-first + configurar-antes-de-customizar nudge para cima · **Confiança: Assumed** (todos os 9 sizes seguem Assumed atrás dos destravamentos externos da Fundação)

## Cenários de Prontidão do Cliente

| Cenário | Banda Realizada | Notas |
|---|---|---|
| Low readiness (atual: ✓) | ~8-12% | Sem ferramental de IA aprovado e com gates de compliance pesados, o ganho fica no piso |
| Mid readiness | ~12-16% | Com ferramental aprovado e política de dados clara, ganho documental e de testes captura-se de forma consistente |
| High readiness | ~16-22% | Ferramental aprovado, dados limpos, ciclos rápidos — topo da banda augmented |

**Cenário atual**: Low (score 2/8)

### Sinais por trás do score
- **AI tooling posture**: 0/2 — Dataprev é empresa pública federal de TI; nenhuma evidência de ferramentas de IA aprovadas ou postura de adoção (Assumed — pergunta de esclarecimento).
- **Delivery velocity / speed bias**: 1/2 — data-alvo agressiva (~13 sem de build, bem abaixo do piso de 18) sinaliza velocidade, mas camadas de aprovação gov + ADI/STF + destravamentos externos temperam.
- **Data & environment hygiene**: 1/2 — org Salesforce greenfield limpa, mas integração externa fragmentada (sem contratos/Swaggers, ~600-700 facilitadoras em silos, volume de carga desconhecido G0701).
- **Legal / security / compliance posture**: 0/2 — LGPD Art. 11, TCU/CGU/ANPD, residência híbrida (CPF não persiste), ADI no STF; máximo de restrição para código/dado em prompts.

### O que leva a subir
- **Low → Mid**: aprovar Copilot/Claude em IDE dentro da fronteira de segurança; publicar política de manuseio de dados por IA sob LGPD.
- **Mid → High**: ambientes/dados de teste representativos cedo; contratos de API resolvidos na Fundação (reduz o mock-then-rework).

## Por Categoria

### Engenharia Técnica & QA — realizada ~8-16% (task-level ~25-40%)
- **Épicas motoras**: E05 (XL), E02 (XL), E03 (L)
- **Como aparece aqui**: O mock-first de E05 é favorável à IA — gerar stubs/mocks aproxima-se de greenfield, onde o ganho é maior. Mas o leilão reverso custom (E02) e a de-tokenização em runtime (E08) são exatamente "fora da fronteira irregular": código bespoke complexo onde o esforço de review consome o ganho bruto [13].

### Análise & Design — realizada ~10-18% (task-level ~30-50%)
- **Épicas motoras**: E08 (L), E02 (XL), E01 (L)
- **Como aparece aqui**: A IA acelera o rascunho de modelos de análise e histórias (fronteira de residência de E08, regras do leilão de E02, jornada do portal E01). O refinamento é humano-dependente: ratificar a fronteira campo-a-campo com Jair Bogo e alinhar as regras do leilão à Lei 14.133 não é trabalho que o modelo fecha [2].

### Documentação & Gestão de Conhecimento — realizada ~12-20% (task-level ~35-50%)
- **Épicas motoras**: E08 (L), E09 (M), E01 (L)
- **Como aparece aqui**: É onde os ganhos mais defensáveis vivem — um programa regulado gera documentação pesada (documentos de fluxo de dados sob LGPD, docs de trilha de auditoria TCU/CGU, ADR, materiais de capacitação de E09) que a IA rascunha bem. O ganho é real porque o volume é alto e a estrutura é repetível [7].

### Gestão de Projeto & Operações — realizada ~8-12% (task-level ~20-30%)
- **Épicas motoras**: E09 (M), E05 (XL)
- **Como aparece aqui**: A categoria de menor ganho. A IA sumariza status e recupera informação, mas o núcleo — alinhamento entre MTE × Dataprev × 600-700 facilitadoras, resolução dos blockers da Fundação, coordenação da virada mock→real de E05 — é trabalho humano que não se move [5].

## Trabalho Só-Humano
- **Project Pulse Reports** — construção de confiança que a IA sumariza mas não facilita.
- **Alinhamento de stakeholders** — enorme aqui: MTE (governo) × Dataprev × 600-700 facilitadoras. A IA rascunha posições; as pessoas decidem.
- **Resolução de conflitos** — julgamento humano.
- **Ratificação da fronteira de residência (G0801)** — decisão de arquitetura humana com Jair Bogo; governa o data model.
- **Definição das regras do leilão / Lei 14.133 (G0202/G0203)** — sign-off legal/regulatório humano.
- **Resolução da incerteza jurídica (ADI no STF)** — fora do controle de qualquer equipe de entrega.

## Banda AI-Native (condicional, provisória)

**~28-38%, qualificação: condicional.** Esta banda usa o fator de realização AI-native (0.55-0.75), cujo denominador maior é ganho pelo *modelo operacional* native encolhendo o overhead de coordenação — não por um ganho de ferramenta maior. Está temperada abaixo da faixa genérica de 35-40% porque um programa gov com gates TCU/CGU/ANPD e incerteza jurídica tem um piso de coordenação irredutível estruturalmente grande, mesmo num modelo native.

**É esta — e só esta — a trilha que cruza o alvo de ≥25% do programa.** Mas ela é condicional: exige o cliente comprometer-se com um modelo operacional native (build/demo/decide diário, decisores empoderados no momento, mandato AI-first). Um programa gov com destravamentos externos pendentes, camadas de aprovação e ADI no STF mostra hoje a postura *oposta*. Apresentamos a banda como motivador — o "*se* vocês adotarem esse jeito de trabalhar…" — não como compromisso.

> **Nota de honestidade (dois lados):** o *diagnóstico* de que um modelo operacional native encolhe o overhead de coordenação é fundamentado (DORA 2024-2025; METR 2025). A *magnitude* (~28-38%) é reportada por fornecedores e ainda não calibrada de forma independente para este contexto — por isso a banda é provisória e não é aplicada por padrão (decisions/0033).

## Premissas
- Benchmarks extraídos de dados publicados 2022-2026 (Peng et al./GitHub 2022, Paradis et al./Google 2024, METR 2025, DORA 2024-2025, McKinsey 2025, GitClear 2025, Stanford HAI AI Index 2026) mais observações internas.
- Bandas task-level convertidas para project-level via fator de realização que contabiliza a lei de Amdahl + overhead de review/imposto de IA.
- Todos os 9 sizes permanecem Assumed atrás dos blockers da Fundação — a banda realizada herda essa confiança.

## Ressalvas
- Bandas são qualitativas e específicas do projeto, não garantias.
- Nenhuma implicação de horas, FTE ou custo é computada ou implícita.
- **Faixa honesta para código**: os estudos divergem — METR 2025 mediu −19% em devs experientes em codebases maduros (o imposto de review é real), enquanto Peng/GitHub 2022 viu +55% em greenfield e Paradis/Google 2024 viu +21%. A verdade deste projeto está no meio-baixo: muito código custom em contexto regulado, com uma fatia greenfield (mock-first) que puxa levemente para cima.
- O gap de percepção é real — times frequentemente sentem-se mais rápidos que os ganhos medidos confirmam (METR 2025).
