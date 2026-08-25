# Delivery Plan — ARI PRODESP / Desenvolve SP

*Roadmap faseado da migração Sales Cloud + Experience Cloud → Financial Services Cloud + Experience Cloud (in-place, mesmo org) · Gerado em 2026-08-25*

**Duração total do programa: por compromisso do usuário (a definir).** As fases abaixo mostram sequência e dependências apenas — sem números de semana.

**Caminho crítico:** E07 → E08 → E10 → E11 (Fundação FSC → Catálogo/Elegibilidade nativos → Migração de dados → Cutover) — essa cadeia governa o cronograma; atraso em qualquer elo cascateia. E04 (Estruturação) é o pilar mais pesado dentro da onda de build e o maior risco de cronograma isolado.

Este plano cobre **o quê** é entregue e **em que ordem**. **O time que entrega isto** — o roster nomeado com contagens defensáveis, por lane — vem do `estimate`.

---

## Fase 0 — Discovery & Foundation *(sem épicos)*

**Objetivo.** Ratificar o modelo-alvo e fechar os conflitos de fonte antes de comprometer o sizing.
**Resolve:** adoção do modelo de lending nativo do FSC (RLA/LoanApplicant/PCM/BRE/Person Accounts, hoje "REVISAR"); prontidão das 30 APIs (Swagger/contratos, write-back PUT/PATCH); volume de dados de produção; fronteira P3↔P5.
**Inclusão justificada:** 83 gaps (> 15) e 14 conflitos de fonte (> 5).
**Sucesso:** adoção FSC decidida e registrada; inventário de prontidão das 30 APIs; volume de produção confirmado; fronteira P3↔P5 reconciliada.
**Risco:** se a adoção FSC nativa não for ratificada, o escopo da migração muda (migração de modelo vs. reaponte leve). Baixa prontidão de API é o maior risco de cronograma.

## Fase 1 — Fundação FSC & Modelo de Dados · **E07, E08**

**Objetivo.** Base transversal da migração: habilitar Person Accounts (irreversível, config) e o modelo de lending nativo (E07); adotar PCM, BRE e DecisionTable no lugar das customizações de produto/enquadramento (E08).
**Sucesso:** Person Accounts habilitado em sandbox; objetos de lending nativos disponíveis; PCM/BRE/DecisionTable configurados e validados.
**Depende de:** Fase 0. E08 depende de E07.
**Risco:** habilitação de Person Accounts é irreversível (só em produção após ensaio full-copy, Fase 5); PCM/BRE são as frentes de maior esforço; permanência contratual das licenças Industries a confirmar.

## Fase 2 — Esteira de Entrada · **E01, E02**

**Objetivo.** Migrar a entrada da jornada: Captação (E01 — já em QA, menor risco) e Pré-qualificação (E02 — formulário adaptativo, validação facial, QRSA, Serpro, envio síncrono).
**Sucesso:** Lead→LoanApplicant operando; pré-qualificação sobre ResidentialLoanApplication; elegibilidade via BRE/PCM funcional.
**Depende de:** Fase 1. E01→E07; E02→E07, E08.
**Risco:** E02 é pilar Grande com 11 integrações — depende fortemente da prontidão de API (BioValid, Serpro); refatoração Serasa prevista.

## Fase 3 — Proposta, Estruturação & Aprovação · **E03, E04, E05**

**Objetivo.** Núcleo pesado: Proposta (E03), Estruturação (E04 — fichas PJ/PF, garantias, Central de Pendências; Garantia__c→LoanApplicantAsset) e Aprovação (E05 — aceite síncrono, efetivação via Platform Event).
**Sucesso:** E04 migrado com dados de tomador→LoanApplicant/Income/Employment e garantias→LoanApplicantAsset; efetivação síncrona via Platform Event validada.
**Depende de:** Fase 1. E03→E07; E04→E07, E08; E05→E07. Fronteira P3↔P5 reconciliada na Fase 0.
**Risco:** E04 é o maior pilar e o maior risco de cronograma da onda; sem Central de Pendências o backoffice Julgamental piora; repositório de documentos >12MB (Agro) diferido/indefinido.

## Fase 4 — Formalização · **E06**

**Objetivo.** Encerramento da jornada: download da CCB, upload da CCB assinada, Meus Contratos sobre objetos FSC.
**Sucesso:** fluxo de formalização da CCB operando; Meus Contratos disponível.
**Depende de:** Fase 1. E06→E07.
**Risco:** provedor de assinatura digital indefinido — MVP usa assinatura manual até definição.

## Fase 5 — Migração de Dados, Regressão & Cutover · **E10, E11**

**Objetivo.** Fechar a migração in-place: ETL/conversão (Account/Contact→Person Accounts, CreditApplication__c→RLA, Garantia__c→collateral), descomissionar objetos superados (Simulacao__c, Parcela__c), SIT/UAT, regressão in-place ampla e cutover irreversível com hypercare.
**Sucesso:** ensaio full-copy concluído; migração reconciliada; regressão aprovada; cutover sem perda; hypercare estável.
**Depende de:** Fases 1-4 e Fase 6 (reaponte). E10→E07, E08; E11→E10.
**Risco:** regressão in-place ampla é o maior risco da migração; cutover é irreversível (ensaio full-copy obrigatório); volume de produção a confirmar (contagens atuais são do sandbox HML); Lead 10.105 registros não endereçado (G1004).

## Fase 6 — Reapontamento de Integrações (30 APIs) · **E09** · *concorrente (parallel track com Fases 2-4)*

**Objetivo.** Reapontar o lado Salesforce das 30 integrações MuleSoft para objetos FSC — named credentials, mapeamento de campos, refactor de callouts Apex, regressão por integração. As APIs no barramento não são reconstruídas (premissa). Roda em paralelo às Fases 2-4, à medida que cada pilar migra.
**Sucesso:** 30 APIs reapontadas; regressão por integração aprovada; nenhuma quebra de contrato lado-Salesforce.
**Depende de:** Fase 1 (objetos FSC precisam existir). E09→E07.
**Risco:** só JUCESP em QA; 29/30 sem Swagger/contrato e write-back PUT/PATCH pendente (maior risco de cronograma, ~+42% no teto do Parecer). Se os contratos das System APIs mudarem, a transformação MuleSoft vira escopo adicional.

---

## Processos transversais (uma vez, não repetidos por fase)

- **Testes:** SIT/UAT concentrados na Fase 5; regressão por integração contínua na Fase 6.
- **Deployment:** pipeline e governança de metadados para a nova configuração declarativa (PCM/BRE/DecisionTable) — E11.
- **Cutover:** ensaio full-copy obrigatório antes do passo irreversível (habilitação de Person Accounts em produção); hypercare pós go-live.
- **Governança:** stewardship de PII/LGPD e CoE de metadados declarativos sem dono definido (gaps G0407/G0516/G0606/G0708/G1106) — levar ao cliente.

## Riscos consolidados

| # | Risco | Fase | Nota |
|---|-------|------|------|
| 1 | Adoção FSC nativa em "REVISAR" | 0/1 | Ratificar na Fase 0; muda o escopo da migração se negada. |
| 2 | Prontidão das 30 APIs (29/30 sem contrato) | 6 | Maior risco de cronograma (~+42% no teto do Parecer). |
| 3 | Regressão in-place ampla | 5 | Maior risco da migração; cutover irreversível. |
| 4 | E04 (Estruturação) — maior pilar | 3 | Maior risco de cronograma isolado na onda de build. |
| 5 | Volume de dados de produção não confirmado | 5 | Contagens são do sandbox HML; Lead 10.105 não endereçado. |
| 6 | Aprovação multi-fornecedor (SLA 24h) | todas | SF/DSP/Sinqia aprovam antes de cada pilar. |
| 7 | Repositório de documentos >12MB (Agro) e assinatura CCB | 3/4 | Diferidos/indefinidos. |

---

*Nota de sizing: sem `data/estimates.json` neste momento (o deck de estimativa foi produzido ad-hoc). O balanceamento entre fases é qualitativo, pela complexidade descrita nos épicos + fit/gap. Rode `estimate` para fechar o sizing formal e o roster nomeado.*
