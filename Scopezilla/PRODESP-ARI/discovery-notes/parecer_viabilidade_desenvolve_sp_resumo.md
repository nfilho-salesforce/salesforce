# Parecer de Viabilidade — Portal Desenvolve SP (resumo estruturado)

> Fonte: arquivo Slack `F0BRV3WGG4X` — "visao-executiva-copia-20260820 (1).html"
> HTML íntegro salvo em `timeline_parecer_viabilidade_desenvolve_sp.html`
> Data do parecer: **19 de agosto de 2026** · Capturado em 2026-08-24 · parte da descoberta do ARI PRODESP

**Projeto:** Portal de crédito fim-a-fim Desenvolve SP no Salesforce
**Cliente:** Desenvolve SP (DSP)
**Objetivo:** Viabilidade técnica do portal, com a lógica de crédito mantida na Sinqia.
**Marco alvo:** **30/11/2026** · Início esperado: **24/08/2026**

## RACI
- **Prodesp:** Infraestrutura, gestão técnica
- **Orange:** Implementação Salesforce
- **DSP:** Negócio, validação, decisão

## Arquitetura
- **Salesforce Experience Cloud (LWR)** — Portal do cliente (simulador, wizard, fichas, acompanhamento, formalização)
- **Salesforce Platform** — Backoffice leve (analista/comitê)
- **MuleSoft Anypoint** — Orquestração, transformação, retry/DLQ, seleção de birôs
- **Sinqia / Officer** — Sistema de registro: esteira, regras, cálculo, aprovação, CCB (núcleo passivo, event-first)
- **Integrações externas:** JUCESP (vínculo societário), Serasa R6 (antifraude), Serpro (faturamento e-CAC), BioValid (facial/SENATRAN/CNH)

**API-Led (MuleSoft, 3 camadas):** 1 Experience API · 5 Process APIs (CCB, workflow aceite/recusa, BioValid, impressão, compliance QRSA) · 28 System APIs.
**Volume:** 10k–100k requisições/dia (síncrono REST, sem batch/bulk).

## Pilares / Épicos (jornada)
Total: **24 funcionalidades · 30 integrações · 33 componentes** · 6 épicos · 3 jornadas (Digital, Julgamental, Agro).

| # | Pilar | Tamanho | Func | Integr | Comp | Conteúdo |
|---|-------|---------|------|--------|------|----------|
| 1 | **Captação** | QA/Pequeno | 5 | 2 | 9 | Login CPF/CNPJ, enriquecimento JUCESP, simulador de crédito, cadastro manual de contas, visibilidade de cooperativas |
| 2 | **Pré-qualificação** | Grande | 5 | 11 | 6 | Formulário adaptativo, validação facial BioValid, exclusão/isenção QRSA, faturamento Serpro, envio síncrono ao core |
| 3 | **Proposta** | Médio | 2 | 4 | — | Lista e detalhamento com status sincronizado do Sinqia (aceite/recusa migrado p/ Pilar 5) |
| 4 | **Estruturação** | Grande | 6 | 8 | 14 | Fichas cadastrais PF/PJ, geração PDF, upload assíncrono, pendências de documentação |
| 5 | **Aprovação** | Médio | 2 | 1 | 1 | Tela de proposta + detalhes financeiros + aceite/recusa; efetivação síncrona no core via orquestração de ocorrências |
| 6 | **Formalização** | Médio | 4 | 4 | 3 | Download/upload CCB (assinatura manual), pendências de garantias, sessão de contratos |

**Pilar 1 já em QA:** 17 US concluídas + 12 US de integração.

## Cronograma (marco 30/11/2026)
- **Set/2026** — Fundação (Fase 0) + Captação (P1): discovery, contratos de API, critérios de aceite, equipe alinhada; cadastro manual, sessão de contas, cooperativas, refatoração API Serasa.
- **Out/2026** — Solicita/acompanha/aprova (P2 + P3 + P5): formulário adaptativo, BioValid, QRSA, Serpro, envio ao core; lista/detalhamento com status; tela de proposta + aceite/recusa com efetivação síncrona.
- **Nov/2026** — Jornada completa + testes (P4 + P6 + SIT/UAT 2 sem): fichas PF/PJ, PDF, upload, pendências; CCB, garantias, contratos.
- **30/11/2026** — 5 pilares concluídos; **Pilar 6 finaliza em dezembro**.

### Fase 0 — Discovery & Foundation
**07–14/set/2026** (1 sem, melhor caso). Trava decisões que gatilham build: write-back Sinqia (PUT/PATCH), sincronização catálogo SF ↔ Officer, contrato BioValid, cálculo QRSA local, **fornecedor de build + data de início (gate crítica)**.

## Estrutura de times — 2 squads em paralelo
- **Squad 1 (Transacional/Wizard):** Pilares 1, 2, 3, 5 — Devs LWC/Apex, especialista integração, BA, SME risco, QA.
- **Squad 2 (Cadastro/Contrato):** Pilares 4, 6, 5 + backbone — Devs LWC/Apex, arquiteto integração, dev Platform Events, modelador de dados, BA, QA.
- Quantitativo final dimensionado com o Solution Lead (não fixado no documento).

## Estimativas de prazo (refinamento até QA, sem homologação cliente)
| Via | 1 Time | 2 Times (paralelo) |
|-----|--------|--------------------|
| Tradicional (âncora) | ~18–28 sem | ~14–26 sem |
| Aumentada (IA) | ~14–26 sem | **~12–22 sem** |

**Recomendação:** Via Aumentada + 2 squads = **~12–22 semanas** (melhor ~12 / pior ~22).
- **Piso (~12 sem):** 2 squads concorrentes, aceleração IA (−10 a 25%), Captação reaproveitada, backbone de ocorrências pronto, escopo fixo.
- **Teto (~22 sem):** ① prontidão das 30 APIs + tempo DSP/Sinqia +42% (+5 sem, maior risco); ② aprovação das 3 frentes +17% (+2 sem); ③ requisitos macro +25% (+3 sem).

**Visão 12 sem (melhor caso):** S1–2 Discovery · S3–4 P1 + início P2 · S5–6 P3 + conclui P2 · S7–9 P4 + P5 · S10–12 P6 + SIT/UAT → 30/11.

## Premissas críticas (se não valerem, prazo desloca)
1. Escopo integral fixo (24 func · 30 integr · 33 comp)
2. Captação reaproveitada em QA
3. Integrações prontas **1 semana antes** de cada pilar (sucesso/falha, arquitetura)
4. Ajustes de API em até **24h**
5. Comunicação entre 3 frentes (SF/DSP/Sinqia) com **SLA 24h**
6. Aprovação de User Stories em **24h**

## Escopo MVP (Cenário 2): 19 de 24 funcionalidades
**Diferido para Fase 2:** Central de Pendências (alta complexidade), retorno síncrono bidirecional ao Sinqia, "Meus Contratos", biometria BioValid plena, assinatura digital da CCB, repositório externo de anexos (>12 MB), cadastro manual sem-JUCESP (produtor rural PF), cooperativas Agro (hierarquia).

## Riscos principais
1. **APIs não prontas** — só JUCESP em QA; 29 de 30 a confirmar; Swagger e write-back PUT/PATCH pendentes → bloqueia builds (maior risco).
2. **Aprovação multi-fornecedor** — SF, DSP, Sinqia/Evertec aprovam antes de cada pilar.
3. **Requisitos em nível macro** — detalhamento pode revelar complexidade não prevista.
4. **Refatoração Serasa** — prevista no escopo.
5. **Backoffice Julgamental** — sem Central de Pendências fica pior que hoje.
6. **Repositório de anexos** — Salesforce Files (12 MB) insuficiente para docs Agro (penhor, escrituras).
7. **Assinatura digital** — provedor não definido; MVP usa assinatura manual.

## Esteira Agro (nova — antes era Banco do Brasil)
Maioria dos tomadores é PF; produtor rural não está na JUCESP; sem QRSA; apenas 2 produtos; motor de crédito Agro externo, volume baixo. Cooperativa: acesso via login consultor ou cliente direto; sem JUCESP; hierarquia de contas. **Decisões abertas:** portal único vs. dois; enquadramento manual; conta corrente; cadastro de produto duplicado.

## Mapa de integrações (30, todas via MuleSoft; só JUCESP em QA)
- **P1 (arranque 24/08):** API-07 JUCESP, API-18 Simulação
- **P2 (arranque 24/08):** API-01/02 solicitações, API-05/06 declarações, API-08 impressão, API-16 conta-proposta, API-17 listas, API-20 parceiro, API-21 sensibilização, API-27 BioValid, API-28 entidade
- **P3 (11/09):** API-22/23/24/25 QRSA (leitura, gravação, comando, cálculo)
- **P5 (27/09):** API-09 comando aceite/recusa
- **P4 (27/09):** API-10 tipos arquivo, API-11/12/13 CRUD conta/contato, API-14 ficha, API-15 sync, API-19 anexos, API-26 ficha PJ
- **P6 (18/10):** API-03 contratos, API-04 arquivo, API-29 assinatura CCB, API-30 geração CCB

## Parecer
Solução **tecnicamente viável** para o escopo integral. **A restrição é de prazo, não de viabilidade.** Meta original (~7 sem) não bate; faixa realista 12–22 sem. Antes de fixar prazo: abrir Fase 0, definir fornecedor de build e data de início, fechar contratos de APIs, dimensionar time. Todas as datas/tamanhos/estimativas são indicativas, não compromisso.
