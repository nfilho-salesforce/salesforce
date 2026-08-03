## INTENT FOR
A beneficiária (envia a folha, recebe o boleto), a facilitadora (baixa a folha por API e devolve 'processado' + valor), o MTE/governo (recebe a taxa via split), o gateway/banco custódia (executa e custodia — fora do CRM) e a área de conformidade (TCU/CGU/ANPD, consulta a trilha).

## INTENT OUTCOME
Fechar o núcleo regulatório da reforma (E03, XL — ADR 0003), seguindo o fluxo folha→pagamento→split: upload assíncrono da folha → validação de layout/integridade → crítica → download pela facilitadora → 'processado' + valor → gateway emite boleto → beneficiária vê o boleto no portal → conciliação por lotes incrementais via MuleSoft → motor calcula o split (teto MDR 3,6%, repasse ≤15 dias) → ordens de transferência ao gateway com trilha auditável e idempotência.

## INTENT MEASURED BY
Marco de entrega de jornada (UAT/homologação): o fluxo completo folha→boleto→conciliação→split→transferência opera ponta a ponta (INT-035..045), com trilha auditável, idempotência e status consolidado 'crédito concedido' — sem persistir linhas da folha e sem o Salesforce mover ou custodiar dinheiro.

## INTENT MUST NOT
Não persistir as linhas do trabalhador — só cabeçalho/competência (todos os intents E03). Não executar nem custodiar dinheiro — o gateway executa; o Salesforce é motor de regras (ADR 0003). Não processar a crítica de forma síncrona no clique do upload (pico ~28/s excede o teto de 25 Apex longos concorrentes — INT-035). Não emitir boleto duplicado nem aplicar efeito financeiro duplicado (idempotência — INT-040, INT-042). Não adotar Revenue Cloud/Billing — split não é nativo (motor custom, ADR 0004). Não enviar CPF a LLM nem logar dado sensível (ADR 0001).

## PRE-DECIDED
- **Fronteira CRM-não-transacional (ADR 0003)**: Salesforce = motor de regras de split, boletagem, conciliação por casamento; o gateway PCI (cliente) executa e custodia. O Salesforce entrega ordens de transferência; não move dinheiro.
- **Split não é nativo**: motor de regras custom sobre baseline Core-only (ADR 0004; KB confirma que Billing não cobre split multipartes).
- **Assíncrono por capacidade**: o upload da folha é desacoplado (fila), forçado pelo pico ~28/s vs. teto de 25 Apex longos concorrentes (INT-035).
- **Sem persistência de linhas**: só cabeçalho/competência da folha (ADR 0001, premissa de discovery G0310).
- **Facilitadora API-only**: baixa a folha por contrato/vigência e devolve 'processado'+valor por API, sem UI (ADR 0004).
- **Teto MDR 3,6% e repasse ≤15 dias** (Decreto 12.712/2025) parametrizados no motor de split (INT-043).

## PLAN-MODE QUESTIONS
- Provedor do gateway/banco custódia não definido (G0309) — **risco #1 da fase**: sem parceiro contratado e integrado, o financeiro não vai a produção em 15/nov. Contrato de API (boleto/Pix, webhook de retorno) a definir (INT-040, INT-042, INT-044).
- Regras de conciliação e tratamento de divergência por lote incremental indefinidas (G0304): pagamento parcial, valor a maior/menor, estorno, não-casado (INT-042).
- Layout exato do CSV da folha (colunas, encoding, volume) e se é único da plataforma ou por facilitadora (G0306, INT-035, INT-036).
- Qual a melhor alternativa Salesforce para a crítica (Einstein, Agentforce, Apex determinístico) e o que ela deve criticar (INT-037 — confiança Unknown).
- A partir de qual evento conta o prazo ≤15 dias e há enforcement ou só registro? Como a taxa MTE se distingue do teto de 3,6% (INT-043).
- Notificação via CTPS Digital é escopo Salesforce (via MuleSoft) ou do MTE, e existe contrato de API (INT-045)?

## BUILD-MODE QUESTIONS
- Mecanismo assíncrono concreto (Platform Events / Queueable / Batch) para a recepção e a crítica (INT-035, INT-037).
- Onde reside o log auditável imutável e sua retenção (Shield/Event Monitoring vs. MuleSoft/Dataprev) — INT-044.
- Chave de idempotência do retorno 'processado' e do casamento de conciliação (INT-039, INT-042).

## DATA MODEL
Modelo de dados financeiro custom sobre a base nativa (INT-038): folha por competência (só cabeçalho — sem linhas do trabalhador), contrato/vigência que a facilitadora usa para baixar por competência, e regras de split parametrizáveis (percentuais por parte, teto MDR, prazo de repasse, distinção PAT vs. não-PAT). Sem Revenue Cloud/Billing. O detalhe vive em INT-038.

## AUTOMATION
O coração regulado da solução, todo assíncrono. Validação de layout/integridade (INT-036) e crítica por IA a definir (INT-037); conciliação agendada por lotes incrementais com casamento e tratamento de divergência (INT-042); motor de regras de split com teto MDR 3,6%, repasse ≤15 dias e ramificação PAT/não-PAT (INT-043); registro do racional auditável + entrega das ordens de transferência ao gateway com idempotência (INT-044); status consolidado 'crédito concedido' (uma linha por folha) e gatilho de notificação à empresa e via CTPS Digital (INT-045). O detalhe vive nesses intents.

## UI
Superfície mínima no portal (Experience Cloud): a beneficiária envia a folha e encontra o boleto registrado disponível, vinculado à competência (INT-041), com status consolidado do ciclo — sem lista por trabalhador. UI simplificada; a facilitadora não tem tela (API-only).

## SECURITY
Herda a residência híbrida e a trilha de auditoria da Fase 1 (ADR 0001, INT-011, INT-012). A trilha do racional de split é imutável e consultável por conformidade (TCU/CGU/ANPD) sem persistir CPF (INT-044). Nenhuma linha de folha nem dado sensível do trabalhador persiste; a crítica por IA não recebe CPF em prompt/log (INT-037).

## DATA SOURCES
MuleSoft on-premise (Fase 1) como hub. Fontes: portal/API para recepção assíncrona da folha (INT-035); facilitadora para download da folha e retorno 'processado'+valor (INT-039, contrato INT-006); gateway/banco custódia para solicitação e retorno do boleto registrado (INT-040), feed agendado de movimentações bancárias para conciliação (INT-008, INT-042) e recepção das ordens de transferência (INT-044); CTPS Digital para a notificação de 'expectativa de crédito' (INT-045, fronteira a confirmar).

## ACCEPTANCE USER
Uma beneficiária envia o CSV da folha da competência e recebe confirmação de recebimento em segundos; o arquivo é validado e criticado de forma assíncrona; a facilitadora baixa a folha por contrato/vigência via API e devolve 'processado' + valor; o gateway emite o boleto registrado, que a beneficiária encontra no portal; ao pagar, a conciliação por lote casa o pagamento, o motor calcula o split sob o teto de 3,6% e prazo ≤15 dias, as ordens de transferência vão ao gateway com trilha auditável, e a folha exibe 'crédito concedido' em uma linha — sem que nenhuma linha de trabalhador tenha sido persistida.

## ACCEPTANCE METADATA
Verifica-se: (a) o upload retorna confirmação e enfileira sem processar a crítica síncrona (INT-035); (b) só o cabeçalho/competência persiste — nenhuma linha de trabalhador (INT-038, todos E03); (c) folha inconsistente é sinalizada e não liberada ao download (INT-036); (d) o retorno 'processado' e o casamento de conciliação são idempotentes (INT-039, INT-042); (e) o boleto não é duplicado em retentativa (INT-040); (f) o split respeita o teto MDR 3,6% e sinaliza risco de estouro do prazo ≤15 dias, ramificando PAT/não-PAT (INT-043); (g) o racional é registrado de forma imutável sem CPF e as ordens de transferência são entregues ao gateway — sem o Salesforce mover dinheiro (INT-044); (h) divergências de conciliação vão a um caminho de exceção, sem falha silenciosa (INT-042).

## REPORTS
Sem dashboards financeiros dedicados no MVP. A trilha auditável do racional de split (INT-044) e o status consolidado 'crédito concedido' (INT-045) são os artefatos de dados desta fase, voltados à conformidade (TCU/CGU/ANPD) e à consulta no portal — não a relatórios de gestão, que ficam para onda futura.
