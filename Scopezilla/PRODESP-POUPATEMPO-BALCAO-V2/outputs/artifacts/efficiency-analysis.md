# AI Delivery Efficiency Analysis — PRODESP · Poupatempo Balcão V2

## So What
**~10-18% de eficiência de entrega realizada com IA, em readiness Baixa.** Um ganho de ritmo e qualidade dentro da mesma forma de time — não redução de headcount, não um insumo de preço.

Onde os ganhos aparecem neste projeto:
- **Documentação & Gestão do Conhecimento** (~12-20%): E05 concentra currículo de treinamento e política de canal — o trabalho de documentação mais denso do programa.
- **Análise & Design** (~10-18%): design de tópicos/ações do Agentforce em E01, E06 e E08.
- **Engenharia Técnica & QA** (~7-13%): integração MuleSoft de E09 (XL) e os workflows de E03/E06, tratados pela linha enterprise/legado — sistemas-alvo são legados, não greenfield.

**Papéis que capturam mais** *(role-type ainda não disponível — sem `resource-plan.json` nesta rodada)*.

**Onde a IA não ajuda**: coordenação com os 5 donos de sistema externos de E09 (T7, Sistema Semântico, Atendimento, Biometria, Legado), revisão jurídica/compliance de LGPD sobre biometria e identidade federada gov.br — mais o trabalho de maior AI-tax do programa, a integração MuleSoft de confiança Unknown.

**Para subir a readiness Alta (~20-24%)**: nomear o owner de governança de agentes de IA do lado Prodesp, confirmar identidades/protocolos dos 5 sistemas-alvo do MuleSoft (G0901-G0905), publicar uma postura/política de uso de ferramentas de IA.

## Headline
**Realizado: ~10-18%** (readiness Baixa) · **Blend task-level: ~30-45%** · **Fator de realização: 0.30-0.40** — puxado para a linha de indústria regulada por overlay LGPD/setor público + risco de integração XL/Unknown em E09 · **Confiança: Assumed**

## Cenários de Readiness do Cliente
| Cenário | Banda Realizada | Notas |
|---|---|---|
| Readiness Baixa (atual: ✓) | ~8-12% | Estado atual — governança de IA não nomeada, ritmo de decisão de setor público e integrações não confirmadas mantêm o ganho modesto. |
| Readiness Média | ~12-16% | Com governança nomeada e integrações formalizadas na Fase 0, o programa capta o meio da faixa de forma defensável. |
| Readiness Alta | ~20-24% | Favorece o topo da faixa apenas se o setor público remover as travas regulatórias e de governança de IA — cenário não observado hoje. |

**Cenário atual**: Baixa (score 1/8)

### Sinais por trás do score
- **Postura de ferramentas de IA**: 0/2 — nenhuma evidência de discovery sobre postura de ferramentas de IA aprovadas para uso interno da Prodesp; owner de governança de agentes de IA ainda não identificado (gap consolidado em 9 gaps espalhados por 7 épicos).
- **Velocidade de entrega / viés de ritmo**: 0/2 — agência de setor público, coordenação entre 5 sistemas-alvo e overlay regulatório que já adiciona +15% ao teto do benchmark.
- **Higiene de dados & ambiente**: 1/2 — fundação Salesforce bem especificada em E01 (Slack + Canvas + Knowledge), mas identidades/protocolos dos 5 sistemas-alvo do MuleSoft (G0901-G0905) e a fonte do sinal de capacidade por posto (G0315) permanecem não confirmados.
- **Postura jurídica / segurança / compliance**: 0/2 — overlay regulatório LGPD/setor público explícito (biometria estadual, identidade federada gov.br, PII de cidadã); nenhuma política de tratamento de dados por IA registrada.

### O que é preciso para subir
- **Baixa → Média**: publicar política de tratamento de dados por IA cobrindo LGPD/biometria; confirmar fonte do sinal de capacidade por posto (G0315).
- **Média → Alta**: nomear o owner de governança de agentes de IA; confirmar identidades/protocolos dos 5 sistemas-alvo do MuleSoft.

## Por Categoria

### Engenharia Técnica & QA — realizado ~7-13% (task-level ~20-35%)
- **Épicos condutores**: E09 (XL), E03 (M), E06 (M), E08 (L)
- **Como aparece aqui**: a integração MuleSoft de E09 (5 sistemas-alvo) e os workflows de E03/E06 dominam o esforço técnico. Tratado pela linha enterprise/legado — os sistemas de destino são legados, não greenfield [1].

### Análise & Design — realizado ~10-18% (task-level ~30-50%)
- **Épicos condutores**: E01 (M), E06 (M), E08 (L)
- **Como aparece aqui**: o desenho de tópicos/ações do Agentforce em E01/E06/E08 é o trabalho de design mais repetido do programa. Puxa esta categoria para o meio-alto da faixa [2].

### Documentação & Gestão do Conhecimento — realizado ~12-20% (task-level ~35-55%)
- **Épicos condutores**: E05 (M)
- **Como aparece aqui**: currículo de treinamento e política de canal em E05 é trabalho de documentação denso, historicamente o ganho mais alto de qualquer categoria [7]. Mesmo sob o overlay regulatório, este teto se mantém.

### Gestão de Projeto & Operações — realizado ~7-13% (task-level ~20-35%)
- **Épicos condutores**: E09 (XL), E05 (M)
- **Como aparece aqui**: coordenação entre Prodesp/Slack/MuleSoft/Data 360 e os potenciais donos externos dos 5 sistemas-alvo mantém esta categoria no meio da faixa [7]. Alinhamento multi-organização resiste mais à automação.

## Trabalho com Barreira Humana
- **Project Pulse Reports** — trabalho de construção de confiança que a IA pode resumir, mas não facilitar.
- **Alinhamento de Stakeholders** — negociação humano-a-humano; a IA rascunha posições, pessoas decidem.
- **Resolução de Conflitos** — julgamento humano.
- **Coordenação com os 5 donos de sistema externos de E09** (T7, Sistema Semântico, Atendimento, Biometria, Legado) — negociação de identidade/protocolo entre organizações depende de relacionamento e autoridade, não de ferramenta.
- **Revisão jurídica/compliance LGPD** sobre biometria e identidade federada gov.br — sign-off regulatório em dado sensível de cidadã permanece humano por desenho.

## Banda AI-Native (condicional, provisória)
**~35-40%** — condicionada a: a Prodesp nomear um owner de governança de agentes de IA e comprometer-se com o modelo operacional AI-native (decisor de negócio disponível diariamente, product owner empoderado, mandato AI-first). **Qualificação: condicional** — o gate ainda não foi atendido; apresentada como motivador ("se a Prodesp se comprometer com esse modelo operacional, é isto que custaria"), nunca como alcançável sem nomear esse compromisso. A banda realizada augmented (~10-18%) e a banda nativa se sobrepõem em ~10-18 pontos — o status de qualificação, não o número, distingue as trilhas.

## Premissas
- Benchmarks extraídos de dados publicados 2022-2026 (Peng et al./GitHub 2022, Paradis et al./Google 2024, METR 2025, BCG×Harvard, DORA 2024-2025, McKinsey 2025, GitClear 2025, Stanford HAI AI Index 2026) mais observações internas.
- Bandas task-level convertidas a project-level via fator de realização que contabiliza a lei de Amdahl + overhead de revisão/AI-tax.
- Fidelidade category-only — `data/resource-plan.json` ainda não existe; a leitura por role-type virá quando o roster for autorado no skill `estimate`.

## Ressalvas
- Bandas são qualitativas e específicas do projeto, não garantias.
- Nenhuma hora, FTE ou implicação de custo é computada ou implícita.
- O gap de percepção é real — equipes costumam se sentir mais rápidas do que os ganhos medidos confirmam (METR 2025).
- A banda AI-native (~35-40%) é condicional e provisória — não é um número a citar sem a qualificação nomeada acima.

## Deliverables
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/efficiency.json`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/artifacts/efficiency-analysis.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/csv/08-efficiency.csv`
