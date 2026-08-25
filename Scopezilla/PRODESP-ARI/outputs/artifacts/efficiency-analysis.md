# Análise de Eficiência de Entrega com IA — ARI PRODESP / Desenvolve SP

*Migração da esteira de crédito de Sales Cloud + Experience Cloud para Financial Services Cloud (FSC) + Experience Cloud, no mesmo org de produção. Análise em fidelidade category-only (sem roster nomeado ainda). Gerada em 2026-08-25.*

## So What

**~12–16% de eficiência de entrega realizada, com prontidão Mid (score 3/8).** É um ganho de ritmo e qualidade dentro da mesma forma de time — não é redução de headcount, nem entrada de precificação.

Onde os ganhos aparecem neste projeto:
- **Documentação & Gestão de Conhecimento** (~13–19%): a mais confiável — E11, E07, E08; contexto regulado doc-pesado, sem imposto de verificação de código.
- **Análise & Design** (~11–17%): rascunho de user stories e modelos nos pilares E01/E02/E04/E05; refinamento com stakeholder segue humano.
- **Engenharia Técnica & QA** (~9–15%): maior ganho bruto (E04-XL, integração/migração) mas maior imposto de IA no brownfield/legado.

**Onde a IA não ajuda**: aprovação multi-fornecedor antes de cada pilar (SF/DSP/Sinqia/Evertec), ratificação dos conflitos de fonte na Fase 0 (G0012), sign-off regulatório (LGPD/antifraude), decisão de cutover irreversível (Person Accounts) — mais o trabalho de maior imposto de IA: reaponte das 30 integrações legadas sem contrato e regressão in-place ampla.

**Para subir a High readiness (~16–22%)**: publicar política de dados IA compatível com LGPD, comprimir o loop de aprovação multi-fornecedor, contratar/Swagger as 29/30 APIs.

## Headline

**Realizado: ~12–16%** (Mid readiness) · **Task-level blend: ~30–45%** · **Fator de realização: 0.30–0.40** — straddle entre a linha regulado+legado e config-misto+custom; FS regulado e 30 integrações legadas puxam para baixo, time misto de 2 squads e config nativa FSC seguram o piso · **Confiança: Assumed** (volume de produção não confirmado — G1004; adoção FSC nativo não ratificada — G0012).

> A banda **AI-native** condicional é **~30–38%** (native_qualification = conditional): só atrás do portão de operação conjunta (decisor empoderado, cadência diária, mandato AI-first), que não está atendido hoje. Diagnóstico ancorado (DORA/METR: o gargalo é coordenação, não ferramenta); magnitude provisória, vendor-reported. Overlap ~25–35% com o realizado augmented — o portão, não o número, distingue as trilhas.

## Cenários de Prontidão do Cliente

| Cenário | Banda Realizada | Notas |
|---|---|---|
| Low readiness | ~9–13% | Enquanto tooling de IA/política de dados não alcançam e os gates multi-fornecedor não comprimem, os ganhos ficam no piso. Score atual está a um sinal do Low. |
| Mid readiness (atual ✓) | ~12–16% | Vies de velocidade e higiene de ambiente sustentam ganho moderado; compliance multi-fornecedor e legado sem contrato limitam a captura. |
| High readiness | ~16–22% | Com política de IA publicada, tooling aprovado, ambiente contratado e aprovação comprimida, a captura sobe para o topo. |

**Cenário atual**: Mid readiness (score 3/8, no piso do Mid).

### Sinais por trás do score
- **Postura de tooling IA**: 1/2 — sem evidência de política de ferramentas de IA do cliente na discovery. Entrega é AI-augmentada do lado Salesforce, mas a postura do cliente é Unknown → vira pergunta de clarificação.
- **Velocidade de entrega / vies de velocidade**: 1/2 — data fixa agressiva (30/11/2026) e 2 squads indicam vies de velocidade, mas aprovação multi-fornecedor antes de cada pilar e dependência de SLA 24h são arrastos de cadência. Cadência enterprise padrão.
- **Higiene de dados & ambiente**: 1/2 — org único brownfield com sandbox full-copy disponível (F7); porém 29/30 APIs sem Swagger (G0013) e volume de produção não confirmado (G1004).
- **Postura legal / segurança / compliance**: 0/2 — FS regulado + setor público (LGPD, antifraude/biometria, Serpro/Serasa), gates de sign-off multi-fornecedor antes de cada pilar, sem política de tratamento de dados por IA.

### O que é preciso para subir
- **Low → Mid**: publicar política de dados IA compatível com LGPD; aprovar ferramentas de codificação IA para o time de entrega.
- **Mid → High**: comprimir o loop de aprovação multi-fornecedor (decisor empoderado, SLA 24h efetivamente cumprido); contratar/Swagger as 29/30 APIs.

## Por Categoria

### Documentação & Gestão de Conhecimento — realizado ~13–19% (task-level ~35–55%)
- **Épicos dirigentes**: E11 (L), E07 (L), E08 (L)
- **Como aparece aqui**: num contexto regulado doc-pesado (matriz de rastreabilidade, evidência de teste, runbooks de cutover em E11, documentação de habilitação FSC em E07/E08) a IA acelera geração e sumarização de forma consistente. O ganho é capturado quase todo porque não há imposto de verificação de código aqui. `[7]`

### Análise & Design — realizado ~11–17% (task-level ~30–50%)
- **Épicos dirigentes**: E01 (M), E02 (L), E04 (XL), E05 (L)
- **Como aparece aqui**: rascunho de user stories, mapeamento Lead→LoanApplicant e modelos de análise ganham na primeira versão gerada por IA nos pilares funcionais. O refinamento com stakeholder e a ratificação de conflitos de fonte na Fase 0 seguem humanos, o que cap o ganho líquido. `[4]`

### Engenharia Técnica & QA — realizado ~9–15% (task-level ~25–45%)
- **Épicos dirigentes**: E04 (XL), E02 (L), E09 (L), E10 (L, Assumed), E11 (L)
- **Como aparece aqui**: maior ganho bruto do programa, mas também o maior imposto de IA — refactor de callouts Apex e reaponte das 30 integrações legadas sem contrato (E09) e regressão in-place ampla (E11) são código fora da fronteira, onde revisão e verificação consomem parte do ganho. Por isso o realizado fica abaixo de Documentação apesar do task-level alto. `[1]`

### Gestão de Projeto & Operações — realizado ~6–11% (task-level ~15–30%)
- **Épicos dirigentes**: E11 (L), E10 (L)
- **Como aparece aqui**: a categoria mais baixa — a coordenação multi-fornecedor (SF/DSP/Sinqia/Evertec) e o alinhamento de gates de aprovação são trabalho humano-a-humano que a IA sumariza mas não conduz. O ganho fica em relatórios e artefatos de status. `[7]`

## Trabalho Só-Humano (onde a IA não move o número)

| Atividade | Por que não há ganho |
|---|---|
| Project Pulse / relatórios de saúde do programa | Construção de confiança que a IA sumariza mas não facilita. |
| Alinhamento de stakeholders | Negociação humano-a-humano; a IA rascunha posições, as pessoas decidem. |
| Resolução de conflitos | Julgamento humano. |
| Aprovação multi-fornecedor antes de cada pilar (SF/DSP/Sinqia/Evertec) | Sign-off contratual e de governança entre partes. |
| Ratificação dos conflitos de fonte na Fase 0 (G0012, adoção FSC nativo) | Decisão de escopo load-bearing do cliente. |
| Sign-off regulatório (LGPD, antifraude/biometria) | Responsabilidade de compliance humana e auditável. |
| Decisão de cutover irreversível (habilitação de Person Accounts) | Ação de mão única que exige autorização humana após ensaio full-copy. |

## Premissas

- Benchmarks de dados publicados 2022–2026 (Peng et al./GitHub 2022, Paradis et al./Google 2024, METR 2025, DORA 2024–2025, GitClear 2025, Stanford HAI AI Index 2026) mais observações internas.
- Bandas task-level convertidas para projeto-nível via fator de realização que considera a lei de Amdahl + overhead de revisão / imposto de IA.
- A banda AI-native é condicional e provisória: o portão de operação conjunta não está atendido hoje — aprovação multi-fornecedor e dependência de SLA 24h são exatamente o risco.
- Confiança Assumed no projeto-nível: G1004 (volume) e G0012 (adoção FSC) alargam as bandas.

## Ressalvas

- Bandas qualitativas e específicas do projeto, não garantias.
- Nenhuma hora, FTE ou custo é calculado ou implicado — este artefato é band-only.
- O realizado (~12–16%) é o número **augmented** honesto (tooling + operação inalterados). A banda AI-native (~30–38%) é condicional ao portão e provisória.
- Gap de percepção é real — times frequentemente sentem-se mais rápidos do que os ganhos medidos confirmam (METR 2025).

---

### Fontes
- `[1]` METR 2025 — impacto medido em OSS maduro (imposto de revisão em código complexo).
- `[2]` Peng et al./GitHub 2022 — ganho em tarefas de codificação greenfield.
- `[4]` Paradis et al./Google 2024 — ganho em contexto enterprise (~21%).
- `[5]` DORA 2024 — efeito de time / AI tax em nível de equipe.
- `[7]` GitClear / benchmarks de documentação e operações.
- `[8]` GitClear 2025 — churn e retrabalho em código gerado por IA.
