# Estimativa PS — Migração para Financial Services Cloud
## ARI PRODESP / Desenvolve SP · Sales Cloud + Experience Cloud → FSC + Experience Cloud

*Estimativa em horas, perfis e linha do tempo · base AI-native (via aumentada) + 2 squads · sem valores financeiros*
*Gerado em 2026-08-24 · Fonte de escopo: Parecer de Viabilidade Desenvolve SP (19/08/2026) + atualizações do time de delivery*

---

## 1. Executive Summary

O portal de crédito fim-a-fim da Desenvolve SP está sendo implantado sobre **Sales Cloud + Experience Cloud** (6 pilares, 24 funcionalidades, 33 componentes, 30 integrações via MuleSoft). Esta estimativa cobre a **migração dessa solução para Financial Services Cloud (FSC) + Experience Cloud**, em modelo **in-place** (mesma org), adotando o **data model FinServ + recursos FSC** (Actionable Relationship Center, Financial Deals/Servicing, Interest Tags/Action Plans), com **migração de dados de produção** e **reapontamento** das 30 integrações MuleSoft para os objetos FSC (sem reconstrução das APIs no barramento).

- **Esforço total (AI-native):** **≈ 3.105 horas PS**
- **Âncora tradicional (referência):** ≈ 3.730 h (ganho AI-native ≈ 17%)
- **Duração:** **14 semanas** (dentro da faixa 12–22 sem do Parecer), 2 squads em paralelo
- **Pico de time:** ~9–10 perfis
- **Maior driver:** regressão da migração in-place + adoção de recursos FSC + migração de dados (Person Accounts é **irreversível** — exige ensaio em sandbox)
- **Fora de escopo:** reconstrução das APIs MuleSoft (só reapontamento), licenciamento/contagem de usuários, valores financeiros

---

## 2. Assumptions (premissas de sizing)

1. **Migração in-place** na org existente — não há build de org nova; foco em habilitar FSC e remapear a solução atual.
2. **Person Accounts** será habilitado (irreversível) — assume-se ensaio completo em sandbox full-copy antes do cutover.
3. **Recursos FSC em nível de configuração** (ARC, Financial Deals/Servicing, Interest Tags, Action Plans) — sem customização pesada além do data model.
4. **30 integrações MuleSoft reapontadas, não reconstruídas** — esforço concentrado no lado Salesforce (named credentials, mapeamento de campos para objetos FSC, refactor de callouts Apex, regressão por integração). Assume-se que os contratos das System APIs no barramento permanecem estáveis; ajustes de transformação no MuleSoft, se necessários, são tratados como risco (ver §6).
5. **Superfície de migração = os 6 pilares** (24 func / 33 componentes / páginas Experience Cloud) já construídos/estáveis em Sales Cloud.
6. **Migração de dados de produção** incluída (volume a confirmar) — estimativa assume volume moderado; volumes altos elevam horas de Data Engineer.
7. **Base AI-native / via aumentada** (aceleração ~15–20% em tarefas de build/refactor via ferramentas de IA) com **2 squads em paralelo**.
8. Sprints de 2 semanas; 40 h/semana por FTE; alocação distribuída por fase.
9. Licenciamento FSC/Experience Cloud e contagem de usuários **fora de escopo** desta estimativa.
10. Ambiente e acessos (sandboxes, DevOps/CI) disponíveis no arranque; SLA de 24h entre frentes (SF/DSP/Sinqia) mantido do Parecer.

---

## 3. Staffing Summary (perfis)

| Perfil (Role) | Horas | FTE (14 sem) | Papel na migração |
|---|---:|---:|---|
| Senior Project Manager | 560 | 1,00 | Gestão de projeto full-time (40h/sem × 14 sem): governança, planejamento, cutover, gestão multi-fornecedor, ceremonies |
| Solution Architect | 160 | 0,29 | Arquitetura FSC, data model FinServ, adoção de recursos |
| Technical Architect | 210 | 0,38 | Estratégia de migração/cutover, design do reapontamento e da migração de dados |
| FSC Functional Consultant / BA | 250 | 0,45 | Mapeamento funcional, config de recursos FSC, refino de backlog, UAT |
| Senior Developer (2 squad leads) | 490 | 0,88 | Habilitação FSC, refactor de Apex/LWC para objetos FSC |
| Developer (2 squads) | 500 | 0,89 | Reapontamento de componentes/flows/páginas Experience Cloud |
| Integration Developer | 280 | 0,50 | Reapontamento das 30 integrações (lado SF), regressão de integração |
| Data Engineer | 280 | 0,50 | ETL, conversão Person Accounts + objetos financeiros, reconciliação |
| QA Engineer | 375 | 0,67 | SIT, UAT, regressão in-place, validação de dados e integrações |
| **Total** | **3.105** | **~5,5 FTE médio** | Pico ~9–10 pessoas nas semanas 5–10 |

> **2 squads:** Squad 1 (Transacional) — pilares 1, 2, 3, 5 · Squad 2 (Cadastro/Contrato + backbone) — pilares 4, 6. Integração e dados atuam transversalmente aos dois squads.

---

## 4. Resource Allocation — Fase × Perfil (horas)

| Fase / Workstream | PM | SA | TA | BA/FSC | Sr Dev | Dev | Int Dev | Data Eng | QA | **Total** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **F1. Discovery & FSC Design** | — | 80 | 80 | 60 | — | — | 40 | 40 | — | **300** |
| **F2. FSC Platform Enablement** | — | 40 | 40 | 40 | 80 | 80 | — | — | 20 | **300** |
| **F3. Solution Migration (6 pilares)** | — | — | — | 90 | 300 | 340 | — | — | 45 | **775** |
| **F4. Integration Re-pointing (30 APIs)** | — | — | — | — | 40 | — | 220 | — | 60 | **320** |
| **F5. Data Migration** | — | — | 30 | 20 | — | — | — | 200 | 40 | **290** |
| **F6. Testing (SIT/UAT/Regressão)** | — | — | 20 | 40 | 40 | 80 | — | — | 180 | **360** |
| **F7. Cutover & Hypercare** | — | — | 40 | — | 30 | — | 20 | 40 | 30 | **160** |
| **F8. PM & Governança (full-time)** | 560 | 40 | — | — | — | — | — | — | — | **600** |
| **Total por perfil** | **560** | **160** | **210** | **250** | **490** | **500** | **280** | **280** | **375** | **3.105** |

### Detalhamento da F3 (Solution Migration por pilar)
| Pilar | Comp | Func | Sr Dev | Dev | BA | QA | Total |
|---|--:|--:|--:|--:|--:|--:|--:|
| P4 Estruturação (Grande) | 14 | 6 | 80 | 120 | 25 | 12 | 237 |
| P2 Pré-qualificação (Grande) | 6 | 5 | 65 | 75 | 20 | 10 | 170 |
| P1 Captação | 9 | 5 | 45 | 55 | 15 | 8 | 123 |
| P6 Formalização (Médio) | 3 | 4 | 45 | 45 | 12 | 6 | 108 |
| P3 Proposta (Médio) | — | 2 | 35 | 25 | 10 | 5 | 75 |
| P5 Aprovação (Médio) | 1 | 2 | 30 | 20 | 8 | 4 | 62 |
| **Total F3** | 33 | 24 | **300** | **340** | **90** | **45** | **775** |

---

## 5. Linha do Tempo (14 semanas · 2 squads)

```
Semana:            1  2  3  4  5  6  7  8  9 10 11 12 13 14
F1 Discovery/Design ██ ██
F2 FSC Enablement       ██ ██ ██
F3 Migration Sq1/Sq2       ██ ██ ██ ██ ██ ██ ██ ██
F4 Integration Re-point       ██ ██ ██ ██ ██ ██
F5 Data Migration                ██ ██ ██ ██ ██ ██ ██
F6 Testing SIT/UAT/Regr.                      ██ ██ ██ ██ ██
F7 Cutover & Hypercare                                    ██ ██
F8 PM full-time     ══════════════════════════════════════ (contínuo, 40h/sem)
```

**Marcos:**
- **Fim S2** — Arquitetura FSC + estratégia de migração/cutover aprovadas; backlog de migração refinado
- **Fim S4** — FSC habilitado (Person Accounts + data model FinServ) em sandbox; recursos FSC configurados
- **Fim S10** — 6 pilares reapontados para FSC; 30 integrações reapontadas
- **Fim S11** — Migração de dados validada em sandbox full-copy
- **Fim S13** — SIT/UAT/regressão concluídos
- **S14** — Cutover em produção (habilitação Person Accounts + migração de dados) + hypercare

> A migração in-place concentra risco na **regressão** (F6, 360h, maior fase de teste) e no **cutover irreversível de Person Accounts** (F7) — por isso o ensaio full-copy antecede a produção.

---

## 6. Riscos e drivers de esforço

| # | Risco / Driver | Impacto na estimativa | Mitigação |
|---|---|---|---|
| 1 | **Person Accounts irreversível** | Ensaio full-copy obrigatório; retrabalho se descoberto tarde | F1 dedica SA/TA ao impacto; sandbox full-copy antes do cutover |
| 2 | **Regressão in-place** | Maior fase de teste (F6) | QA 375h no total; regressão por pilar + integração |
| 3 | **Contratos das System APIs mudam com o data model FSC** | Se payloads mudarem, pode exigir transformação no MuleSoft (fora do escopo atual) | Confirmar na F1 que reapontamento é só lado SF; senão, escopo adicional |
| 4 | **Volume de migração de dados a confirmar** | Volumes altos elevam Data Engineer (F5) | Confirmar volumes/objetos; premissa = moderado |
| 5 | **Profundidade dos recursos FSC (ARC, Financial Deals/Servicing)** | Customização pesada elevaria F2/F3 | Premissa = nível de configuração; validar na F1 |
| 6 | **Aprovação multi-fornecedor (SF/DSP/Sinqia)** | Herdado do Parecer; atrasa fases | SLA 24h; governança em F8 |

---

## 7. Estimation Notes

- **Por que ~2.835h e não um build completo:** a superfície (6 pilares, 33 componentes) já existe em Sales Cloud; o esforço é **refactor/reapontamento** para o data model FSC, não construção do zero. Ainda assim é substancial por três motivos: adoção de recursos FSC net-new, migração de dados com conversão Person Accounts, e regressão in-place ampla.
- **MuleSoft:** 280h de Integration Developer cobrem **apenas o lado Salesforce** (mapeamento para objetos FSC, named credentials, refactor de callouts, regressão das 30 integrações). A construção das APIs no barramento **não** está estimada, conforme orientação.
- **AI-native:** a redução de ~18% vs. âncora tradicional aplica-se sobretudo às fases de build/refactor (F3) e migração de dados (F5), onde ferramentas de IA aceleram geração de código e scripts de ETL/testes. Fases de arquitetura e governança têm ganho menor.
- **Gestão de projeto:** a governança é feita por um **Senior Project Manager full-time** (560h = 40h/sem × 14 sem), dedicado ao longo de toda a migração — substitui o modelo de Engagement Manager em tempo parcial e reforça a coordenação multi-fornecedor (SF/DSP/Sinqia) num cutover in-place de alto risco.
- **Faixa de confiança:** ±20% dado que volume de dados, profundidade dos recursos FSC e estabilidade dos contratos de API ainda são premissas (ver §6). Confirmar na Fase 0 estreita a faixa.
- **CSV:** versão tabular (fase × workstream × perfil × horas × semanas × FTE) em `10-estimate-fsc-migration.csv`, compatível com a estrutura do Estimate Builder (colunas financeiras omitidas conforme solicitado).
