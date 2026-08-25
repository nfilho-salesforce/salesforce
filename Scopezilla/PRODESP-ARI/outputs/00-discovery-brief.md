# Discovery Brief — ARI PRODESP / Desenvolve SP

*Portal de crédito fim-a-fim no Salesforce · Experience Cloud + MuleSoft · Base para ROM Salesforce PS*
*Gerado em 2026-08-24 · Fonte primária: Parecer de Viabilidade Desenvolve SP (19/08/2026) + canvas de discovery Slack*

## Resumo executivo

A Desenvolve SP (agência de fomento de São Paulo) vai construir um portal de crédito digital fim-a-fim sobre Salesforce Experience Cloud (LWR), com a lógica de crédito mantida no core Sinqia/Officer e toda a integração orquestrada por MuleSoft. Um Parecer de Viabilidade já foi produzido por um time Salesforce (Giselle Hamano/SA, Pedro Martire/TA, Felipe Guerra/Mule) mapeando 6 pilares — 24 funcionalidades, 30 integrações, 33 componentes — com marco de entrega em **30/11/2026**. **Este projeto (ARI) produz a ROM / estimativa Salesforce PS para o build**, com o **PS entregando a implementação** (Orange sai ou é subcontratada) e o **MuleSoft dentro do escopo PS**.

## Contexto de empresa e indústria

- **Cliente:** Desenvolve SP — agência de fomento (banco de desenvolvimento) do estado de São Paulo. Domínio: serviços financeiros / crédito.
- **Programa:** Portal "Desenvolve SP" para jornada de crédito digital, cobrindo 3 esteiras: **Digital, Julgamental e Agro** (esta última nova — antes atendida pelo Banco do Brasil).
- **RACI atual:** Prodesp (infraestrutura, gestão técnica) · Orange (implementação Salesforce) · DSP (negócio, validação, decisão). *Decisão deste projeto: PS assume o build.*

## Estado atual vs. alvo Salesforce

**Estado atual:** Pilar 1 (Captação) já está em QA — 17 user stories concluídas + 12 US de integração. Base reaproveitável.

**Arquitetura alvo:**
- **Experience Cloud (LWR)** — portal do cliente (simulador, wizard de solicitação, fichas cadastrais, acompanhamento, formalização)
- **Salesforce Platform** — backoffice leve (analista/comitê)
- **MuleSoft Anypoint** — orquestração, transformação, retry/DLQ, seleção de birôs (**no escopo PS**)
- **Sinqia / Officer** — sistema de registro (esteira, regras, cálculo, aprovação, CCB); núcleo passivo, event-first
- **Externos:** JUCESP (vínculo societário), Serasa R6 (antifraude), Serpro (faturamento e-CAC), BioValid (validação facial / SENATRAN / CNH)

**API-Led (MuleSoft):** 1 Experience API · 5 Process APIs · 28 System APIs = **30 integrações** (só JUCESP em QA hoje). Volume: 10k–100k req/dia, síncrono REST.

## Escopo e objetivos do projeto

**Objetivo:** ROM Salesforce PS para o build do portal, escopo integral do Parecer, estimativa em base **AI-native / via aumentada** com 2 squads em paralelo.

**6 pilares (épicas candidatas):**

| # | Pilar | Tamanho | Func | Integr | Comp |
|---|-------|---------|------|--------|------|
| 1 | Captação | QA/Pequeno | 5 | 2 | 9 |
| 2 | Pré-qualificação | Grande | 5 | 11 | 6 |
| 3 | Proposta | Médio | 2 | 4 | — |
| 4 | Estruturação | Grande | 6 | 8 | 14 |
| 5 | Aprovação | Médio | 2 | 1 | 1 |
| 6 | Formalização | Médio | 4 | 4 | 3 |

**Totais:** 24 funcionalidades · 30 integrações · 33 componentes · 3 jornadas.

**Base de estimativa (do Parecer):** via aumentada + 2 squads = **~12–22 semanas** (piso ~12 / teto ~22). Tradicional seria ~14–26 sem. Drivers do teto: prontidão das 30 APIs (+42%), aprovação multi-fornecedor (+17%), requisitos macro (+25%).

**MVP (Cenário 2):** 19 de 24 funcionalidades. Diferido p/ Fase 2: Central de Pendências, retorno síncrono bidirecional Sinqia, "Meus Contratos", biometria BioValid plena, assinatura digital CCB, repositório externo de anexos (>12 MB), cadastro manual sem-JUCESP (produtor rural PF), cooperativas Agro (hierarquia).

## Timeline e restrições

- **Marco alvo:** 30/11/2026 (mudou de 30/09) — 5 pilares; Pilar 6 finaliza em dezembro.
- **Início esperado:** 24/08/2026. **Fase 0 (Discovery & Foundation):** 07–14/set/2026.
- **Set:** Fundação + Captação · **Out:** Pré-qual + Proposta + Aprovação · **Nov:** Estruturação + Formalização + SIT/UAT (2 sem).
- **Restrição-chave:** viabilidade técnica é positiva; **a restrição é de prazo, não de viabilidade**. Meta original (~7 sem) não é realista; faixa realista 12–22 sem.

## Dados e compliance

- **Compliance/regulatório (assumido, não detalhado):** QRSA, antifraude Serasa R6, validação facial BioValid, faturamento e-CAC via Serpro.
- **Migração de dados:** não mencionada no material — **gap**.
- **Anexos:** Salesforce Files (limite 12 MB) insuficiente para documentos Agro (penhor, escrituras) — requer repositório externo.

## Premissas críticas (do Parecer — herdadas na ROM)

1. Escopo integral fixo (24 func · 30 integr · 33 comp)
2. Captação reaproveitada em QA
3. Integrações prontas 1 semana antes de cada pilar
4. Ajustes de API em até 24h
5. Comunicação entre 3 frentes (SF/DSP/Sinqia) com SLA 24h
6. Aprovação de User Stories em 24h

## Riscos

1. **APIs não prontas** (maior risco) — só JUCESP em QA; 29 de 30 a confirmar; Swagger e write-back PUT/PATCH pendentes → bloqueia builds.
2. **Aprovação multi-fornecedor** — SF, DSP, Sinqia/Evertec aprovam antes de cada pilar.
3. **Requisitos em nível macro** — detalhamento pode revelar complexidade não prevista.
4. **Refatoração Serasa** — prevista no escopo.
5. **Backoffice Julgamental** — sem Central de Pendências fica pior que hoje.
6. **Repositório de anexos** — Files (12 MB) insuficiente para docs Agro.
7. **Assinatura digital** — provedor não definido; MVP usa assinatura manual.

## Esteira Agro (nova)

Maioria dos tomadores é PF; produtor rural não está na JUCESP; sem QRSA; 2 produtos; motor de crédito Agro externo, volume baixo. Cooperativas: acesso via login consultor ou cliente direto; hierarquia de contas. **Decisões abertas:** portal único vs. dois; enquadramento manual; conta corrente; cadastro de produto duplicado.

## Open Questions (levar ao cliente / resolver antes da ROM final)

1. **Escopo MuleSoft PS** — confirmado que as 30 APIs (1 Exp + 5 Process + 28 System) entram no esforço PS. Confirmar disponibilidade de Swagger/contratos e write-back PUT/PATCH do Sinqia por API (define esforço real de integração).
2. **Papel Orange** — PS assume o build; confirmar se Orange sai totalmente ou permanece como subcontratada em alguma frente (afeta composição de time e handoff).
3. **Volume de usuários / licenças** — fora de escopo desta ROM, mas necessário para proposta comercial completa (Experience Cloud member-based vs. login-based).
4. **Budget / modelo comercial** — sem sinal de orçamento; definir Fixed Fee vs. T&M para a proposta.
5. **Migração de dados** — há dados legados a migrar? Não mencionado.
6. **KPIs quantificados** — objetivos de negócio ainda qualitativos; capturar metas mensuráveis.
7. **Fornecedor de build + data de início** — gate crítica do Parecer (Fase 0); confirma o ponto de partida da timeline.
8. **Decisões Agro** — portal único vs. dois; tratamento de cooperativas e produtor rural PF sem JUCESP.
9. **Governança/adoção** — sem CoE, gestão de mudança, treinamento ou comms plan definidos.
10. **Assinatura digital da CCB** — provedor a definir (MVP assume manual).
