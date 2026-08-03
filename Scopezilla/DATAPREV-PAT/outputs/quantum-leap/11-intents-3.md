# Intent Statements — Phase 3 (DATAPREV-PAT)

> Reference role: the **load-bearing build target** for Phase 3. Each intent below is one capability — one firing trigger or user action, one outcome, one walkthrough. Build one at a time. The phase brief (`10-phase-3.md`) is orchestration; this file is what to build.
>
> **For architects:** walk these with the customer to assign priority and answer open questions. Edit `data/intents.json` (canonical) or this file directly — the next quantum-leap run re-renders from JSON.

## INT-035 — Recepção assíncrona de folha (upload CSV via portal/API, desacoplado)

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

A beneficiária envia o CSV da folha da competência pelo portal ou por API e recebe confirmação de recebimento em segundos; o arquivo entra numa fila de processamento sem travar a sessão nem consumir um slot de processamento longo.

### 2. Build target

- Aceitar upload do CSV da folha por dois canais: portal (beneficiária autenticada) e API (integração)
- Persistir o arquivo recebido como anexo/conteúdo e registrar o cabeçalho da folha (competência mês-ano, contrato, beneficiária) — sem gravar as linhas do trabalhador
- Devolver confirmação imediata de recebimento e enfileirar o processamento (validação + crítica) para execução assíncrona
- Suportar o pico de ~28 uploads/s numa janela de 5 dias sem enfileiramento síncrono nem estouro do teto de processos longos concorrentes

### 3. Guardrails

- Must not process payroll critique synchronously on upload click (peak ~28/s exceeds the 25 concurrent long-Apex ceiling)
- Must not persist payroll line items in MVP (header/competência only)
- Must not block the user session waiting for validation or critique to finish

### 4. Out of scope

- Must not persist or expose per-worker payroll rows (roadmap futuro)
- Must not normalize N formatos proprietários de facilitadora no MVP — assume layout único da plataforma até definição contrária
- Must not execute or custody funds

### 5. Acceptance

Cenário de verificação — A beneficiária envia o CSV da folha da competência pelo portal ou por API e recebe confirmação de recebimento em segundos; o arquivo entra numa fila de processamento sem travar a sessão nem consumir um slot de processamento longo.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not process payroll critique synchronously on upload click (peak ~28/s exceeds the 25 concurrent long-Apex ceiling)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014

### 7. Grounding

- **Source artifact:** gap: G0310 fluxo de 8 passos (premissa confirmada, linhas não persistem) _(data/gaps.json)_
- **Source artifact:** gap: G0306 layout padronizado de folha (formato/validação/volume em aberto) _(data/gaps.json)_

### Open questions

- [ ] Qual o layout exato do CSV da folha (colunas, formato, encoding) e a contagem média/máxima de linhas por arquivo? (Resolver: MTE/Dataprev (workshop de regras E03))
- [ ] O layout é único imposto pela plataforma ou cada facilitadora usa o próprio, exigindo normalização? (Resolver: MTE/Dataprev)

---

## INT-036 — Validação de layout e integridade da folha (não quebrada)

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

Toda folha enfileirada passa por uma checagem automática de layout e integridade estrutural; folhas íntegras seguem para disponibilização à facilitadora e as inconsistentes são sinalizadas à beneficiária com o motivo, sem persistir as linhas.

### 2. Build target

- Validar estrutura do arquivo (colunas esperadas, tipos, encoding, arquivo não corrompido/truncado) de forma assíncrona a partir da fila
- Marcar a folha como íntegra (apto a download) ou inconsistente, registrando o resultado no cabeçalho da folha
- Devolver à beneficiária o resultado da validação (aceita / rejeitada com motivo) sem gravar as linhas do trabalhador
- Emitir evento de conclusão que habilita o próximo passo (download pela facilitadora) apenas para folhas íntegras

### 3. Guardrails

- Must not process payroll critique synchronously on upload click (peak ~28/s exceeds the 25 concurrent long-Apex ceiling)
- Must not persist payroll line items in MVP (header/competência only)
- Must not release a payroll to facilitadora download before validation passes

### 4. Out of scope

- Must not attempt fraud detection or business-rule scoring here — this is structural integrity only
- Must not persist rejected line content for reprocessing in MVP

### 5. Acceptance

Cenário de verificação — Toda folha enfileirada passa por uma checagem automática de layout e integridade estrutural; folhas íntegras seguem para disponibilização à facilitadora e as inconsistentes são sinalizadas à beneficiária com o motivo, sem persistir as linhas.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not process payroll critique synchronously on upload click (peak ~28/s exceeds the 25 concurrent long-Apex ceiling)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014

### 7. Grounding

- **Source artifact:** gap: G0310 validação de layout + integridade ('não quebrada') _(data/gaps.json)_
- **Source artifact:** gap: G0306 regras de validação de arquivo em aberto _(data/gaps.json)_

### Open questions

- [ ] Qual a regra concreta de integridade ('não quebrada') — só estrutura/parse, ou inclui somatórios/consistência de totais? (Resolver: MTE/Dataprev)

---

## INT-037 — Crítica da folha por IA (assíncrona; melhor alternativa Salesforce a definir)

epic `E03` · priority _(unassigned)_ · confidence _Unknown_ · surface `automation`

### 1. Outcome

Folhas que passam na validação estrutural recebem uma crítica automática mais rica (consistência dos dados da competência) executada de forma assíncrona; o resultado alimenta a liberação para download sem que a crítica rode no clique do upload.

### 2. Build target

- Executar uma camada de crítica automática da folha após a validação estrutural, de forma 100% assíncrona (fila/batch/evento)
- Registrar o veredito da crítica no cabeçalho da folha (aprovada / apontamentos) sem persistir linhas
- Descrever o comportamento esperado (detectar inconsistências da competência) e deixar o agente de build escolher o mecanismo Salesforce — a melhor alternativa (Einstein, agente, Apex) ainda não está travada

### 3. Guardrails

- Must not process payroll critique synchronously on upload click (peak ~28/s exceeds the 25 concurrent long-Apex ceiling)
- Must not persist payroll line items in MVP (header/competência only)
- Must not send worker-level sensitive data (CPF) into an LLM prompt or log it (residência ADR 0001)

### 4. Out of scope

- Must not commit to a specific AI product before the critique-mechanism decision is made
- Must not gate go-live on a heavy AI capability if a lighter deterministic critique meets the need

### 5. Acceptance

Cenário de verificação — Folhas que passam na validação estrutural recebem uma crítica automática mais rica (consistência dos dados da competência) executada de forma assíncrona; o resultado alimenta a liberação para download sem que a crítica rode no clique do upload.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not process payroll critique synchronously on upload click (peak ~28/s exceeds the 25 concurrent long-Apex ceiling)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014

### 7. Grounding

- **Source artifact:** gap: G0310 crítica via melhor alternativa Salesforce (Einstein/agente) a definir _(data/gaps.json)_
- **Source artifact:** decision: ADR 0001 residência híbrida — CPF não persiste/transita para o LLM _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] Qual a melhor alternativa Salesforce para a crítica (Einstein, agente Agentforce, Apex determinístico) e o que exatamente ela deve criticar? (Resolver: Arquitetura Salesforce + MTE/Dataprev)

---

## INT-038 — Modelo de dados financeiro (folha cabeçalho/competência, contrato, regras de split)

epic `E03` · priority _(unassigned)_ · confidence _Confirmed_ · surface `data-model`

### 1. Outcome

A plataforma tem os objetos custom que sustentam o ciclo financeiro — folha por competência (só cabeçalho), contrato/vigência e regras de split parametrizáveis — sobre a base Sales Cloud, sem Revenue Cloud e sem persistir linhas de folha.

### 2. Build target

- Objeto custom de folha: cabeçalho por competência (mês-ano), vínculo a contrato e beneficiária, resultado de validação/crítica e status do ciclo — SEM linhas do trabalhador
- Objeto custom de contrato/vigência que a facilitadora usa para baixar a folha por contrato e competência
- Objeto custom de regras de split parametrizáveis (percentuais por parte, teto MDR, prazo de repasse, distinção PAT vs não-PAT)
- Modelar sobre os objetos nativos já assumidos (ADR 0004: Opportunity/Quote para o leilão) sem introduzir Revenue Cloud/Billing

### 3. Guardrails

- Must not persist payroll line items in MVP (header/competência only)
- Must not adopt Revenue Cloud / Billing — split não é nativo; motor de regras é custom (baseline Core-only)
- Must not execute or custody funds

### 4. Out of scope

- Must not model per-worker payroll tables or line-item reporting (roadmap futuro)
- Must not persist CPF or worker sensitive data in the core org (residência ADR 0001)

### 5. Acceptance

Cenário de verificação — A plataforma tem os objetos custom que sustentam o ciclo financeiro — folha por competência (só cabeçalho), contrato/vigência e regras de split parametrizáveis — sobre a base Sales Cloud, sem Revenue Cloud e sem persistir linhas de folha.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not persist payroll line items in MVP (header/competência only)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0003 Salesforce é o motor de regras de split _(decisions/0003-fronteira-crm-nao-transacional.md)_
- **Source artifact:** knowledge: Split não nativo no Billing → custom + integração externa _(knowledge/salesforce-revenue-cloud-marketplace-arch.md:31-34)_
- **Source artifact:** gap: G0308 baseline Core-only (Billing fora) — E03 Assumed _(data/gaps.json)_

### Open questions

- [ ] O baseline Core-only aguenta a evolução do financeiro (faturamento, notas, credit memos, múltiplos ciclos) ou há gatilho de migração para Revenue Cloud? (Resolver: Arquitetura Salesforce + MTE/Dataprev)

---

## INT-039 — Disponibilização da folha à facilitadora e retorno de 'processado + valor'

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

A facilitadora baixa a folha íntegra por contrato e vigência (mês-ano) via API e devolve à plataforma o status 'processado' com o valor a pagar, que passa a alimentar a emissão de boleto.

### 2. Build target

- Expor endpoint (via MuleSoft, E05) para a facilitadora baixar a folha por contrato + competência — facilitadora é API-only, sem UI/licença de portal (ADR 0004)
- Receber o retorno 'processado' + valor a pagar e registrá-lo no cabeçalho da folha, avançando o status do ciclo
- Garantir idempotência do retorno (evitar reprocessamento/duplicidade de valor) e rastrear a data do processamento (âncora do prazo de repasse)

### 3. Guardrails

- Must not persist payroll line items in MVP (header/competência only)
- Must not expose a UI/portal seat to facilitadoras — integração é API-only (ADR 0004)
- Must not accept a processed-value return without idempotency guarding against duplicate financial effect

### 4. Out of scope

- Must not build per-facilitadora bespoke connectors — assume a single standard API contract
- Must not execute or custody funds

### 5. Acceptance

Cenário de verificação — A facilitadora baixa a folha íntegra por contrato e vigência (mês-ano) via API e devolve à plataforma o status 'processado' com o valor a pagar, que passa a alimentar a emissão de boleto.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not persist payroll line items in MVP (header/competência only)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014
- **External:** Facilitadora (integração API) — Contrato de API (payload/auth/idempotência) para baixar folha por contrato/vigência e devolver 'processado' + valor _(owner: cliente)_

### 7. Grounding

- **Source artifact:** gap: G0310 facilitadora baixa por contrato/vigência, retorna processado + valor _(data/gaps.json)_
- **Source artifact:** decision: ADR 0004 facilitadora API-only (sem UI) _(decisions/0004-facilitadora-api-only.md)_

### Open questions

- [ ] Qual o contrato de API facilitadora↔plataforma (payload, auth, idempotência) para download e retorno de valor? (Resolver: MTE/Dataprev + facilitadoras (E05))

---

## INT-040 — Solicitação e recebimento de boleto registrado junto ao gateway

epic `E03` · priority _(unassigned)_ · confidence _Unknown_ · surface `integration`

### 1. Outcome

Com o valor da folha processado, a plataforma envia a instrução de cobrança ao gateway (que intermedia a conta custódia) e recebe de volta o boleto registrado com metadados e link, sem movimentar dinheiro.

### 2. Build target

- Enviar ao gateway (via MuleSoft, E05) a solicitação de boletagem com o valor processado da folha
- Receber e registrar o boleto retornado (identificador, metadados, link) vinculado à folha/competência
- Tratar erro/retentativa na emissão (boleto não gerado, timeout do gateway) com idempotência para não duplicar cobrança

### 3. Guardrails

- Must not execute or custody funds — the gateway does (ADR 0003); Salesforce only requests and records
- Must not persist payroll line items in MVP (header/competência only)
- Must not issue duplicate boletos on retry — enforce idempotency

### 4. Out of scope

- Must not implement bank settlement rails or escrow logic inside Salesforce
- Must not assume Pix vs boleto mechanics until the gateway contract is defined

### 5. Acceptance

Cenário de verificação — Com o valor da folha processado, a plataforma envia a instrução de cobrança ao gateway (que intermedia a conta custódia) e recebe de volta o boleto registrado com metadados e link, sem movimentar dinheiro.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not execute or custody funds — the gateway does (ADR 0003); Salesforce only requests and records).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014
- **External:** Gateway/banco custódia (PCI) — Contrato de API (Swagger) para receber boletagem e devolver boleto registrado + metadados; provedor ainda não definido _(owner: cliente)_

### 7. Grounding

- **Source artifact:** decision: ADR 0003 gateway executa/custodia; Salesforce emite boletagem _(decisions/0003-fronteira-crm-nao-transacional.md)_
- **Source artifact:** gap: G0302 mecanismo de geração de boleto/Pix indefinido; G0309 provedor não definido _(data/gaps.json)_

### Open questions

- [ ] Qual o provedor do gateway/banco custódia e o contrato de API (boleto e/ou Pix, formato do webhook de retorno)? (Resolver: cliente (MTE/Dataprev) + especialista arquitetura bancária)

---

## INT-041 — Disponibilização do boleto à beneficiária no portal

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `experience-cloud`

### 1. Outcome

Assim que o boleto registrado retorna do gateway, a beneficiária o encontra disponível no portal (link/metadados) vinculado à folha da competência.

### 2. Build target

- Exibir à beneficiária autenticada o boleto da competência (link e metadados) no portal, vinculado à folha/contrato
- Refletir o status do boleto/ciclo de forma consolidada, sem lista por trabalhador
- Atualizar a disponibilização conforme o retorno do gateway (emitido, pago) via os eventos do ciclo

### 3. Guardrails

- Must not persist payroll line items in MVP (header/competência only)
- Must not execute or custody funds
- Must not surface per-worker CPF or sensitive data in the portal (residência ADR 0001)

### 4. Out of scope

- Must not display a per-worker breakdown — consolidated status only in MVP
- Must not host payment execution in the portal — the boleto links to the gateway rails

### 5. Acceptance

Cenário de verificação — Assim que o boleto registrado retorna do gateway, a beneficiária o encontra disponível no portal (link/metadados) vinculado à folha da competência.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not persist payroll line items in MVP (header/competência only)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014

### 7. Grounding

- **Source artifact:** gap: G0310 boleto disponível à beneficiária no portal _(data/gaps.json)_

### Open questions

_(no open questions captured)_

---

## INT-042 — Conciliação agendada de movimentações bancárias (casamento incremental) e identificação de pagamento

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

A plataforma recebe do gateway as movimentações bancárias em lotes incrementais por agendamento e faz o casamento com os boletos emitidos, identificando o pagamento e avançando o status da folha automaticamente.

### 2. Build target

- Consumir as movimentações bancárias devolvidas pelo gateway em batch incremental, disparado por agendamento no MuleSoft (E05)
- Casar cada lançamento com o boleto/folha correspondente (matching por identificador do boleto e valor)
- Ao identificar o pagamento, avançar o status do ciclo e disparar o cálculo de split
- Tratar divergência (pagamento parcial, valor a maior/menor, não casado) como exceção registrada, sem falha silenciosa

### 3. Guardrails

- Must not execute or custody funds — reconciliation is matching/record-keeping only (ADR 0003)
- Must not persist payroll line items in MVP (header/competência only)
- Must not silently drop unmatched or divergent movements — route them to an exception path

### 4. Out of scope

- Must not initiate refunds/estornos or bank reversals — those are gateway actions
- Must not reconcile against per-worker rows (competência-level only)

### 5. Acceptance

Cenário de verificação — A plataforma recebe do gateway as movimentações bancárias em lotes incrementais por agendamento e faz o casamento com os boletos emitidos, identificando o pagamento e avançando o status da folha automaticamente.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not execute or custody funds — reconciliation is matching/record-keeping only (ADR 0003)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014
- **External:** Gateway/banco custódia (PCI) — Feed de movimentações bancárias (webhook/batch) com formato e cadência definidos _(owner: cliente)_

### 7. Grounding

- **Source artifact:** decision: ADR 0003 conciliação = casamento no CRM _(decisions/0003-fronteira-crm-nao-transacional.md)_
- **Source artifact:** gap: G0304 regras concretas de conciliação/divergência em aberto; G0305 tratamento de erros do fluxo de pagamento _(data/gaps.json)_

### Open questions

- [ ] Quais as regras de conciliação e o tratamento de divergência (pagamento parcial, valor a maior/menor, estorno, não casado)? (Resolver: MTE/Dataprev + especialista arquitetura bancária)

---

## INT-043 — Motor de regras de split (teto MDR 3,6%, repasse ≤15 dias, ramificação PAT vs não-PAT)

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

Identificado o pagamento, a plataforma consulta as regras de split e calcula o rateio entre facilitadora, governo/MTE e demais partes, aplicando o teto de MDR de 3,6%, a distinção entre beneficiária PAT e não-PAT e o prazo de repasse de até 15 dias.

### 2. Build target

- Consultar as regras de split parametrizadas e calcular o rateio do pagamento identificado por competência/contrato
- Aplicar o teto de MDR de 3,6% (Decreto 12.712/2025) e a taxa distinta de beneficiárias não-PAT
- Ramificar o cálculo por tipo de beneficiária (PAT com benefício/teto vs não-PAT)
- Medir o prazo de repasse (≤15 dias) a partir do evento-gatilho definido e sinalizar risco de descumprimento

### 3. Guardrails

- Must not execute or custody funds — the engine computes and applies the split; the gateway settles (ADR 0003)
- Must not exceed the 3,6% MDR cap or breach the ≤15-day repasse window without flagging
- Must not persist payroll line items in MVP (header/competência only)

### 4. Out of scope

- Must not perform the bank transfers implied by the split — it emits transfer orders only
- Must not adopt Revenue Cloud Billing for the split — it is not native (custom engine)

### 5. Acceptance

Cenário de verificação — Identificado o pagamento, a plataforma consulta as regras de split e calcula o rateio entre facilitadora, governo/MTE e demais partes, aplicando o teto de MDR de 3,6%, a distinção entre beneficiária PAT e não-PAT e o prazo de repasse de até 15 dias.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not execute or custody funds — the engine computes and applies the split; the gateway settles (ADR 0003)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0003 Salesforce calcula e aplica as regras de split _(decisions/0003-fronteira-crm-nao-transacional.md)_
- **Source artifact:** knowledge: Billing não cobre split multipartes — custom _(knowledge/salesforce-revenue-cloud-marketplace-arch.md:31-34)_
- **Source artifact:** gap: G0303 gatilho/enforcement do prazo de 15 dias; G0307 cálculo da taxa MTE no split _(data/gaps.json)_

### Open questions

- [ ] Como a taxa ao MTE/Dataprev é parametrizada no split e como se distingue do teto de 3,6% a estabelecimentos? (Resolver: MTE/Dataprev)
- [ ] A partir de qual evento conta o prazo de ≤15 dias e há enforcement (alerta/bloqueio) ou só registro? (Resolver: MTE/Dataprev (jurídico))

---

## INT-044 — Registro do racional de cálculo (trilha auditável) e entrega das ordens de transferência ao gateway

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

A plataforma registra todo o racional do repasse — datas, split aplicado, ordens de transferência — como trilha auditável e entrega as ordens de transferência ao gateway via MuleSoft, que executa a movimentação.

### 2. Build target

- Registrar de forma imutável/auditável o racional completo: datas, regras de split aplicadas, valores por parte, ordens de transferência geradas
- Entregar as ordens de transferência ao gateway (via MuleSoft, E05) para execução — sem mover dinheiro na plataforma
- Expor a trilha para consulta de conformidade (TCU/CGU/ANPD), sem persistir CPF/dado sensível do trabalhador

### 3. Guardrails

- Must not execute or custody funds — the platform hands transfer orders to the gateway (ADR 0003)
- Must not persist payroll line items in MVP (header/competência only)
- Must not log CPF/worker sensitive data in the audit trail (residência ADR 0001)

### 4. Out of scope

- Must not perform the actual bank transfers or settlement
- Must not build per-worker rationale — competência/split-level record only in MVP

### 5. Acceptance

Cenário de verificação — A plataforma registra todo o racional do repasse — datas, split aplicado, ordens de transferência — como trilha auditável e entrega as ordens de transferência ao gateway via MuleSoft, que executa a movimentação.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not execute or custody funds — the platform hands transfer orders to the gateway (ADR 0003)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014
- **External:** Gateway/banco custódia (PCI) — Contrato de API para receber ordens de transferência e executar a movimentação _(owner: cliente)_

### 7. Grounding

- **Source artifact:** decision: ADR 0003 registra racional; gateway é o executor único _(decisions/0003-fronteira-crm-nao-transacional.md)_
- **Source artifact:** gap: G0803 trilha de auditoria sob residência híbrida _(data/gaps.json)_

### Open questions

- [ ] Onde reside e como se garante a imutabilidade do log auditável (Shield/Event Monitoring vs log MuleSoft/Dataprev) e sua retenção? (Resolver: Arquitetura Salesforce + Dataprev (Jair Bogo))

---

## INT-045 — Status consolidado 'crédito concedido' e gatilho de notificação (empresa + CTPS Digital)

epic `E03` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

Concluído o repasse, a folha exibe um status consolidado 'crédito concedido' em uma única linha (não por trabalhador) e dispara a notificação à empresa e, via CTPS Digital, a 'expectativa de crédito' ao trabalhador — monitoramento apenas no MVP.

### 2. Build target

- Consolidar o status da competência em 'crédito concedido' (uma linha por folha, não lista por trabalhador)
- Disparar notificação à empresa beneficiária quando o status é atingido
- Disparar a notificação de 'expectativa de crédito' via CTPS Digital (via MuleSoft, E05), tratada como monitoramento no MVP
- Não persistir dado sensível do trabalhador ao acionar a notificação (residência ADR 0001)

### 3. Guardrails

- Must not persist payroll line items in MVP (header/competência only)
- Must not display a per-worker status list — consolidated 'crédito concedido' line only
- Must not persist or log the worker's CPF when triggering the CTPS notification (residência ADR 0001)

### 4. Out of scope

- Must not build active worker-level credit tracking beyond monitoring in MVP
- Must not execute or custody funds

### 5. Acceptance

Cenário de verificação — Concluído o repasse, a folha exibe um status consolidado 'crédito concedido' em uma única linha (não por trabalhador) e dispara a notificação à empresa e, via CTPS Digital, a 'expectativa de crédito' ao trabalhador — monitoramento apenas no MVP.; O comportamento é aceito quando um revisor percorre o fluxo ponta a ponta e observa exatamente esse resultado, com os guardrails respeitados (notadamente: Must not persist payroll line items in MVP (header/competência only)).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-009, INT-014
- **External:** CTPS Digital (Carteira de Trabalho Digital) — Contrato de API para receber a notificação de 'expectativa de crédito'; fronteira de responsabilidade (SF via MuleSoft vs MTE) a confirmar _(owner: cliente)_

### 7. Grounding

- **Source artifact:** gap: G0509 notificação via CTPS Digital — fronteira de escopo a confirmar; G0807 trabalhador é titular mas não usuário _(data/gaps.json)_
- **Source artifact:** decision: ADR 0001 residência híbrida (CPF do trabalhador) _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] A entrega da notificação via CTPS Digital é escopo Salesforce (via MuleSoft) ou responsabilidade do MTE/Novo PAT, e existe contrato de API? (Resolver: MTE/Dataprev)

