# Fase 0 — Kit de Fechamento de Pendências

**ARI PRODESP / Desenvolve SP** · Migração Sales Cloud + Experience Cloud → Financial Services Cloud + Experience Cloud (in-place)
*Gerado em 2026-08-27 · Janela Fase 0: 07–14/set/2026 · Base: `10-estimate-fsc-migration.md` (§6 riscos) + `02-delivery-plan.md` (Fase 0)*

---

## Propósito

A estimativa (≈3.105h AI-native, 14 sem, faixa **±20%**) apoia-se em 4 premissas de sizing ainda abertas. Este kit converte cada pendência em **perguntas fechadas, com dono e decisão requerida**, para que a Fase 0 as ratifique e **estreite a faixa de ±20%**. Cada bloco traz: *o que decidir · impacto se não resolver · evidência a coletar · dono*.

**Legenda de donos:** DSP (negócio) · Prodesp (infra) · Orange/Sinqia (integração/barramento) · SF (Salesforce PS).

---

## P1 — Adoção do modelo de lending nativo do FSC  🔴 *gate de escopo*

**Status hoje:** "REVISAR" (RLA/LoanApplicant/PCM/BRE/Person Accounts). É a **decisão-mãe**: se negada, o programa deixa de ser "migração de modelo FSC" e vira "reaponte leve" — muda o sizing inteiro.

**Decidir:**
1. Confirma-se a adoção de **Person Accounts** (irreversível em produção)? PF é maioria dos tomadores — encaixa. Há bloqueio jurídico/LGPD ou de integração que impeça?
2. Adota-se **ResidentialLoanApplication (RLA) + LoanApplicant + LoanApplicantAsset** como objetos-alvo (substituindo `CreditApplication__c` / `Garantia__c`)?
3. Adota-se **PCM (Product Catalog Management) + BRE (Business Rules Engine) + DecisionTable** no lugar das customizações de produto/enquadramento?
4. As **licenças Industries/FSC** permanecem contratadas pelo horizonte do programa? (permanência contratual a confirmar)

**Impacto se não resolver:** todo o caminho crítico E07→E08 fica sem fundação; sizing de F1/F2/F3 indefinido.
**Evidência a coletar:** ata de decisão assinada (SF+DSP); confirmação de licenças ativas; parecer LGPD sobre Person Accounts.
**Dono:** DSP + SF (arquitetura: Giselle Hamano / Pedro Martire).

---

## P2 — Prontidão das 30 integrações (29/30 sem contrato)  🔴 *maior risco de cronograma (~+42% no teto do Parecer)*

**Status hoje:** só **JUCESP** em QA. Para as outras 29 faltam Swagger/contratos e o write-back **PUT/PATCH** (Sinqia) está pendente.

**Decidir/coletar — por API (planilha 1 linha/API):**
| Campo | O que confirmar |
|---|---|
| Swagger/OpenAPI | Existe? Versão? Ambiente (QA/PRD)? |
| Direção | Read-only (GET) ou write-back (PUT/PATCH)? |
| Write-back Sinqia | Confirmado e testável em QA? |
| Estabilidade do contrato | Payload muda com o data model FSC? *(→ ver P4)* |
| Named credential | Já provisionada no org? |
| Owner técnico | Orange/Sinqia/Prodesp? |

**Impacto se não resolver:** bloqueia builds (F2–F4) e o reaponte (F6); é o driver do +42% no teto do Parecer.
**Evidência a coletar:** inventário das 30 APIs preenchido; ao menos as 5 Process APIs + top System APIs (BioValid, Serpro, Serasa, JUCESP) com Swagger em mãos.
**Dono:** Orange/Sinqia + Felipe Guerra (Mule) / Prodesp.

---

## P3 — Volume de dados de produção  🟠 *driver de Data Engineer (F5)*

**Status hoje:** as contagens conhecidas são do **sandbox HML**, não de produção. Premissa de sizing = volume **moderado**.

**Decidir/coletar (contagens de PRODUÇÃO):**
- `Account` / `Contact` a converter em **Person Accounts** (nº de PF vs PJ).
- `CreditApplication__c` → **RLA** (nº de aplicações históricas a migrar; corte por status/data?).
- `Garantia__c` → **LoanApplicantAsset** (volume + anexos).
- Objetos a **descomissionar**: `Simulacao__c`, `Parcela__c` (migrar ou arquivar?).
- **G1004 — Lead: 10.105 registros** ainda não endereçados: migram, arquivam ou descartam?
- Anexos/documentos e o **repositório >12MB (Agro)** — volume e destino.

**Impacto se não resolver:** volumes altos elevam horas de Data Engineer (hoje 280h / 0,50 FTE) e o esforço de reconciliação/ensaio full-copy.
**Evidência a coletar:** relatório de contagens de produção por objeto; política de retenção/corte histórico.
**Dono:** DSP (negócio, política de retenção) + Prodesp (extração).

---

## P4 — Estabilidade dos contratos das System APIs  🔴 *gate do escopo MuleSoft*

**Status hoje:** premissa = **reaponte só no lado Salesforce** (named credentials, mapeamento de campos, refactor de callouts Apex). Se os **payloads** mudarem ao adotar o data model FSC, a transformação no barramento MuleSoft entra como **escopo adicional** (fora da estimativa atual).

**Decidir:**
1. Ao migrar para objetos FSC, os payloads que as System APIs consomem/produzem **mudam de estrutura**? (mapear campo-a-campo por API — cruza com P2)
2. Se mudam: o ajuste fica no **lado Salesforce** (mapeamento/transformação Apex) ou exige **transformação no MuleSoft**?
3. Confirmar por escrito que **reconstruir APIs no barramento está fora de escopo** (premissa nº 4 da estimativa).

**Impacto se não resolver:** risco nº 3 da §6 — pode adicionar frente MuleSoft não orçada.
**Evidência a coletar:** matriz de impacto de contrato por API (estável / muda-lado-SF / muda-MuleSoft); aceite formal da fronteira de escopo.
**Dono:** SF (arquitetura) + Orange/Sinqia (barramento).

---

## P5 — Fronteira funcional P3 ↔ P5 (Proposta ↔ Aprovação)  🟠

**Status hoje:** conflito de fonte a reconciliar (14 conflitos totais no discovery). Afeta onde termina "Proposta" (E03) e começa "Estruturação/Aprovação" (E04/E05), incl. efetivação síncrona via Platform Event.

**Decidir:** onde fica a fronteira de responsabilidade e o handoff de dados entre os pilares 3 e 5; quem dispara/consome o Platform Event de efetivação.
**Impacto se não resolver:** rebalanceia esforço entre E03/E04/E05 (E04 já é o maior pilar e o maior risco isolado de cronograma).
**Evidência a coletar:** fluxo P3→P5 reconciliado e assinado.
**Dono:** DSP + SF.

---

## P6 — Itens diferidos com definição pendente (MVP Cenário 2)  🟡

Não bloqueiam o sizing base, mas precisam de **dono e data de decisão** para não virarem escopo-surpresa:

| Item | Decisão pendente | Dono |
|---|---|---|
| **Assinatura digital da CCB** | Fornecedor indefinido — MVP usa assinatura manual até definir | DSP |
| **Repositório de anexos >12MB (Agro)** | Destino/serviço externo indefinido | DSP + Prodesp |
| **Central de Pendências** | Diferida p/ Fase 2 — sem ela o backoffice Julgamental piora | DSP |
| **Retorno síncrono bidirecional Sinqia / "Meus Contratos" / BioValid plena** | Diferidos p/ Fase 2 — confirmar sequência | DSP + Sinqia |
| **Governança sem dono** (G0407/G0516/G0606/G0708/G1106 — PII/LGPD + CoE de metadados declarativos) | Definir stewardship | DSP + SF |

---

## P7 — Materiais de discovery não incorporados  ⚪ *housekeeping*

Pendências de coleta que ficaram da última sessão (sem tools Google Workspace disponíveis):
- **URL do LUCID** (diagrama de arquitetura/fluxo) — obter e anexar a `discovery-notes/`.
- **Google Docs / NotebookLM / Drive** do cliente — não puxados; validar se contêm requisitos além do Parecer de Viabilidade (19/08/2026).

**Dono:** SF (Nelson) — obter acessos/links.

---

## Saída esperada da Fase 0 (critérios de sucesso)

1. ✅ **P1 ratificada** — adoção FSC nativa decidida e registrada em ata.
2. ✅ **P2** — inventário das 30 APIs preenchido (Swagger/direção/write-back por API).
3. ✅ **P3** — volume de produção confirmado por objeto + política de retenção.
4. ✅ **P4** — matriz de impacto de contrato por API + fronteira MuleSoft aceita por escrito.
5. ✅ **P5** — fronteira P3↔P5 reconciliada.
6. ✅ **P6** — cada item diferido com dono e data de decisão.

**Resultado:** com P1–P4 fechadas, a faixa de confiança da estimativa estreita de **±20%** para a faixa firme, e o roster/cronograma nomeados podem ser comprometidos.

---

*Rastreabilidade: P1↔Risco 1 · P2↔Risco 2 · P4↔Risco 3 · P3↔Risco 5 (§6 da estimativa). Gera insumo direto para `estimate` (fechar sizing) e para a proposta comercial.*
