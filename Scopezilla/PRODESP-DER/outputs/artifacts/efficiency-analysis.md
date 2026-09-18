# AI Delivery Efficiency Analysis — PRODESP · DER-SP

## So What
**~10-18% de eficiência de entrega realizada em readiness Low.** Um ganho de ritmo e qualidade dentro da mesma forma de equipe — não redução de headcount, não é insumo de precificação.

Onde os ganhos aparecem neste projeto:
- **Documentation & Knowledge Management** (~11-20%): especificações de payload SIGOR/SIGEO (E02) e a documentação de segurança do token de guest (E05) — o rascunho comprime bem, mas o sign-off multi-organizacional mantém a revisão em ritmo humano.
- **Technical Engineering & QA** (~8-16%): integração dupla SIGOR/SIGEO (E02) e motor de despacho/escalonamento (E03) — geração de código e dados de teste acelera, mas a revisão sobre specs legadas não confirmadas limita o ganho.
- **Analysis & Design** (~8-16%): fluxos de triagem do Agentforce (E01) e lógica de escalonamento N/N-10 (E03) — rascunho rápido, refinamento com stakeholders permanece humano.

**Onde a IA não ajuda**: resolução de gaps bloqueadores com DER/Stefanini (G0305, G0309, G0517) — decisão formal entre três organizações — mais o trabalho de alinhamento de stakeholders e conflito, que seguem 100% humanos.

**Para subir para readiness High (~18-22%)**: resolver LGPD/DPIA e a trilha de auditoria de overrides (G0305), definir política de uso de IA para dados sensíveis do canal de emergência, reduzir camadas de aprovação entre DER/PRODESP/Stefanini.

## Headline
**Realizado: ~10-18%** (readiness Low) · **Blend em nível de tarefa: ~30-45%** · **Fator de realização: 0,30-0,40** — perfil misto entre "config+dev customizado" e "setor regulado/legado pesado", puxado para baixo pela auditoria em aberto e pelas integrações SIGOR/SIGEO sem spec confirmado · **Confiança: Assumed**

**Faixa AI-native (condicional, não qualificada): ~35-40%** — motivador, não um número alcançável hoje. Depende de um compromisso operacional (decisão diária, donos de negócio empoderados, mandato AI-first) que o DER/PRODESP ainda não assumiu — a cadeia de decisão DER→PRODESP→Stefanini e a ausência de um sponsor executivo nomeado são os sinais que mantêm este gate fechado.

## Cenários de Client-Readiness
| Cenário | Faixa Realizada | Notas |
|---|---|---|
| Low readiness (atual: ✓) | ~7-11% | Estado atual — ganhos modestos até a cadeia DER→PRODESP→Stefanini amadurecer e a postura de dados ser resolvida. |
| Mid readiness | ~10-16% | Faixa base se a cadência de decisão e a postura de dados melhorarem moderadamente. |
| High readiness | ~18-22% | Favorece a ponta alta com cadência ágil e ambiente de integração maduro — improvável no perfil atual de contratação pública. |

**Cenário atual**: Low (score 2/8)

### Sinais por trás do score
- **Postura de ferramentas de IA**: 1/2 — nenhuma menção a política de uso de IA/ferramentas aprovadas na discovery do DER/PRODESP.
- **Velocidade de entrega**: 0/2 — cadeia de decisão DER→PRODESP→Stefanini, Opportunity em Stage 02-Scoping, ciclo formal de contratação pública.
- **Higiene de dados e ambiente**: 1/2 — org Salesforce greenfield, mas duas integrações legadas (SIGOR, SIGEO) com payload/API ainda não confirmado.
- **Postura legal/segurança/compliance**: 0/2 — nenhuma discussão formal de LGPD/DPIA registrada; trilha de auditoria de overrides (G0305) permanece gap aberto.

### O que é preciso para subir
- **Low → Mid**: resolver LGPD/DPIA e G0305; definir política de uso de IA para dados sensíveis; reduzir camadas de aprovação DER/PRODESP/Stefanini.
- **Mid → High**: aprovar ferramentas de IA para uso em IDE/documentação; fechar a spec SIGOR/SIGEO.

## Por Categoria

### Technical Engineering & QA — realizado ~8-16% (nível de tarefa ~25-40%)
- **Épicos que impulsionam**: E02 (L), E03 (L), E04 (L)
- **Como aparece aqui**: Na integração dupla SIGOR/SIGEO (E02) e no motor de despacho/escalonamento (E03), a IA acelera geração de código e dados de teste, mas a revisão sobre duas specs de payload legado ainda não confirmadas limita o ganho realizado [1].

### Analysis & Design — realizado ~8-16% (nível de tarefa ~25-40%)
- **Épicos que impulsionam**: E01 (M), E03 (L)
- **Como aparece aqui**: Rascunhar os fluxos de triagem do Agentforce (E01) e a lógica de escalonamento N/N-10 (E03) comprime bem, mas o refinamento com stakeholders sobre o valor de N e a trilha de auditoria (G0305) permanece 100% humano [2].

### Documentation & Knowledge Management — realizado ~11-20% (nível de tarefa ~35-50%)
- **Épicos que impulsionam**: E02 (L), E05 (L)
- **Como aparece aqui**: As especificações de payload de integração (E02) e a documentação de segurança do token de guest (E05) compressam bem no rascunho, mas a cadeia de aprovação DER/PRODESP/Stefanini mantém a revisão final em ritmo humano [7].

### Project Management & Operations — realizado ~8-14% (nível de tarefa ~25-35%)
- **Épicos que impulsionam**: E02 (L), E03 (L)
- **Como aparece aqui**: Um programa de 5 fases cobrindo 14 CGRs e três organizações gera carga alta de coordenação; a IA rascunha status e notas de reunião, mas o alinhamento real sobre G0305/G0309 continua humano.

## Onde a IA não ajuda
- **Project Pulse Reports** — trabalho de construção de confiança que a IA pode resumir, mas não conduzir.
- **Stakeholder Alignment** — negociação humano-a-humano; a IA rascunha posições, pessoas decidem.
- **Conflict Resolution** — julgamento humano.
- **Resolução de gaps bloqueadores com DER/Stefanini (G0305, G0309, G0517)** — exige decisão formal entre três organizações; a IA prepara a pauta, não decide.

## Assumptions & Caveats
- Benchmarks extraídos de dados publicados 2022-2026 (Peng et al./GitHub 2022, Paradis et al./Google 2024, METR 2025, DORA 2024-2025, McKinsey 2025, GitClear 2025, Stanford HAI AI Index 2026) mais observações internas da Salesforce [1][2][7].
- Todos os 5 épicos carregam `confidence: Assumed` em `estimates.json` — amplia a incerteza em ambas as direções.
- Bandas são qualitativas e específicas do projeto, não garantias. Nenhuma implicação de horas, FTE ou custo é computada ou implícita.
- O gap de percepção é real — equipes frequentemente se sentem mais rápidas do que os ganhos medidos confirmam (METR 2025).
- A faixa AI-native (~35-40%) é condicional e provisória — depende de um compromisso operacional que o DER/PRODESP ainda não assumiu.

---
*Esta análise é baseada em benchmark, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso.*
