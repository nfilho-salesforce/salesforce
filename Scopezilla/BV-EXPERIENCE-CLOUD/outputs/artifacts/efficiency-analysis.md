# Análise de Eficiência de Entrega com IA — BV (Experience Cloud + MuleSoft)

**Cliente:** BV Financeira (Banco BV) · Financial Services · Brasil
**Natureza:** engajamento *brownfield* — remediação de débito técnico e ativação de recursos prioritários sobre três portais Experience Cloud em produção e uma camada de integração MuleSoft/Apigee viva.

## So What
**~10–18% de eficiência de entrega realizada em prontidão Baixa.** Um ganho de ritmo e qualidade dentro da mesma forma de time — não redução de headcount, não um insumo de preço.

Onde os ganhos aparecem neste projeto:
- **Engenharia Técnica & QA** (~10–18%): E06, E01, E02 — integração API-led e builds customizados; é também onde vive o maior imposto de IA.
- **Documentação & Gestão de Conhecimento** (~13–20%): E06, E01 — contratos de XAPI/SAPI e OAS, o terreno de maior alavanca.
- **Análise & Design** (~9–15%): E01, E06, E04 — modelo de dados de catálogos e desenho de contratos.

**Onde a IA não ajuda**: pulso de programa, alinhamento de stakeholders, sign-off regulatório (LGPD/BACEN), decisão de IdP e licenciamento, negociação da limitação do Anypoint — mais os builds customizados do E01 (render OPA/Wizard) e os fluxos MuleSoft do E06, o trabalho de maior imposto de IA aqui.

**Para subir a prontidão Alta (~16–22%)**: aprovar IA em IDE para o time, publicar política de manuseio de dados por IA, adotar mandato AI-first com compliance pré-liberado.

## Headline
**Realizada: ~10–18%** (prontidão Baixa) · **Blend nível-tarefa: ~30–45%** · **Fator de realização: 0,30–0,40** — banco regulado, brownfield em produção viva, integração legada pesada · **Confiança: Assumed**

**Trilha AI-native (condicional/provisória): ~30–38%.** O diagnóstico — que um modelo operacional AI-first comprime o overhead de coordenação — é sustentado por DORA/METR; a magnitude é majoritariamente reportada por fornecedor e não calibrada neste engajamento. Temperada abaixo do teto canônico (~35–40%) pelo imposto regulatório + de integração legada do BV. **Só é real se** o BV se comprometer com o modelo operacional conjunto: decisor disponível diariamente, business owners empoderados, mandato AI-first. A banda aumentada (~10–18%) e a AI-native (~30–38%) se sobrepõem em ~30–35% — é o status de qualificação, não o número, que distingue as trilhas.

## Cenários de Prontidão do Cliente
| Cenário | Banda Realizada | Notas |
|---|---|---|
| Baixa (atual: ✓) | ~8–12% | Ganhos modestos enquanto tooling e política de IA não avançarem — é o estado de hoje. |
| Média | ~12–16% | IA em IDE aprovada e higiene de ambiente resolvida elevam o meio da faixa. |
| Alta | ~16–22% | Postura AI-first e compliance pré-liberado capturam o topo; cliente mais rápido captura mais. |

**Cenário atual**: Baixa (score 2/8)

### Sinais por trás do score
- **Postura de tooling de IA**: 0/2 — sem evidência no discovery de ferramentas de IA de codificação aprovadas; banco regulado tende a postura restritiva por padrão. *Unknown/Assumed — pergunta de esclarecimento.*
- **Velocidade de entrega / viés de rapidez**: 1/2 — remediação brownfield em produção viva; sem mandato explícito de velocidade no discovery.
- **Higiene de dados & ambiente**: 1/2 — plataforma, DevOps e versionamento já existem (E04); fonte/volume/qualidade dos dados legados da migração (E05) seguem em aberto (G0503/G0504).
- **Postura legal/segurança/compliance**: 0/2 — instituição financeira regulada; LGPD, consentimento OneTrust, fluxo de aprovação por OPA — arrasto real sobre a velocidade realizada.

### O que leva a subir
- **Baixa → Média**: aprovar IA em IDE (Copilot/Claude) para o time de entrega; publicar política de manuseio de dados por IA.
- **Média → Alta**: mandato AI-first na entrega; pré-liberação de compliance para os fluxos de aprovação regulados.

## Por Categoria

### Engenharia Técnica & QA — realizada ~10–18% (nível-tarefa ~30–45%)
- **Épicos que puxam**: E06 (XL), E01 (XL), E02 (L)
- **Como aparece aqui**: É onde os ganhos concentram e onde vive o maior imposto de IA — os builds customizados do E01 (render OPA em HTML, Wizard de geração de API) e os fluxos MuleSoft do E06 rendem menos que o boilerplate de config do E04. A banda é ampla justamente por essa mistura [5].

### Análise & Design — realizada ~9–15% (nível-tarefa ~25–40%)
- **Épicos que puxam**: E01 (XL), E06 (XL), E04 (M)
- **Como aparece aqui**: A IA acelera o rascunho do modelo de dados de catálogos (E01) e o desenho dos contratos de XAPI/SAPI (E06), mas a decisão de arquitetura de integração permanece trabalho humano de julgamento [3].

### Documentação & Gestão de Conhecimento — realizada ~13–20% (nível-tarefa ~40–55%)
- **Épicos que puxam**: E06 (XL), E01 (XL)
- **Como aparece aqui**: Contratos de XAPI/SAPI, OAS e documentação técnica dos portais são o terreno de maior alavanca — geração e manutenção de spec é onde a IA mais rende neste projeto [2].

### Gestão de Projeto & Operações — realizada ~8–13% (nível-tarefa ~20–35%)
- **Épicos que puxam**: E01 (XL), E06 (XL)
- **Como aparece aqui**: Cinco fases e coordenação transversal em produção viva geram reporte que a IA resume bem, mas o pulso de programa e o alinhamento entre BV e PS seguem humanos [6].

## Trabalho Humano-Só
- **Pulso de programa** — construção de confiança que a IA resume mas não conduz.
- **Alinhamento de stakeholders** — negociação humano-a-humano; a IA rascunha posições, as pessoas decidem.
- **Resolução de conflito** — julgamento humano.
- **Sign-off regulatório (LGPD/BACEN)** — aprovação de compliance de banco; a IA não assume o risco regulatório.
- **Decisão de IdP e licenciamento (bloqueadores da Fase 0)** — decisões de contratação e identidade externas ao time de build.
- **Negociação da limitação do Anypoint (R2)** — negociação de fornecedor/contrato.

## Premissas
- Benchmarks de dados publicados 2022–2026 (Peng et al./GitHub 2022, Paradis et al./Google 2024, METR 2025, BCG×Harvard, DORA 2024–2025, McKinsey 2025, GitClear 2025, Stanford HAI AI Index 2026) mais observações internas.
- Bandas de nível-tarefa convertidas em nível-projeto por um fator de realização que reflete a lei de Amdahl + overhead de revisão/imposto de IA.
- Fidelidade *category-only*: sem `resource-plan.json` ainda (o roster é autorado no `estimate`). Re-rodar após o roster existir eleva para *category+role*.

## Ressalvas
- Bandas são qualitativas e específicas do projeto, não garantias.
- Nenhuma implicação de horas, FTE ou custo é computada ou insinuada.
- A banda AI-native (~30–38%) é **condicional** e **provisória** (ver Headline).
- Gap de percepção é real — times frequentemente sentem-se mais rápidos do que os ganhos medidos confirmam (METR 2025).

---

*Fontes: `data/efficiency.json`, `data/epics.json`, `data/estimates.json`, `data/roadmap.json`, `.discovery-context.md`. Benchmark: model-training-data (ver Premissas).*
