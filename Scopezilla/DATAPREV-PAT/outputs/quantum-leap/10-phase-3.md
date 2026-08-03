# Etapa 3 — Financeiro — Folha, Motor de Split & Conciliação (19/out – 8/nov · Sem. 10-12) (DATAPREV-PAT)

> **Orquestração da fase — o que está dentro/fora da fase, dependências, estado inicial.** Leia isto primeiro para se orientar. As especificações construíveis por capacidade vivem em `11-intents-3.md` (quando presente) — é contra elas que você de fato constrói, um intent por vez.
> Duração da fase: **3 semanas (compromisso do usuário)**.

## Intenção

- **Para:** A beneficiária (envia a folha, recebe o boleto), a facilitadora (baixa a folha por API e devolve 'processado' + valor), o MTE/governo (recebe a taxa via split), o gateway/banco custódia (executa e custodia — fora do CRM) e a área de conformidade (TCU/CGU/ANPD, consulta a trilha).
- **Resultado:** Fechar o núcleo regulatório da reforma (E03, XL — ADR 0003), seguindo o fluxo folha→pagamento→split: upload assíncrono da folha → validação de layout/integridade → crítica → download pela facilitadora → 'processado' + valor → gateway emite boleto → beneficiária vê o boleto no portal → conciliação por lotes incrementais via MuleSoft → motor calcula o split (teto MDR 3,6%, repasse ≤15 dias) → ordens de transferência ao gateway com trilha auditável e idempotência.
- **Medido por:** Marco de entrega de jornada (UAT/homologação): o fluxo completo folha→boleto→conciliação→split→transferência opera ponta a ponta (INT-035..045), com trilha auditável, idempotência e status consolidado 'crédito concedido' — sem persistir linhas da folha e sem o Salesforce mover ou custodiar dinheiro.
- **Não deve:** Não persistir as linhas do trabalhador — só cabeçalho/competência (todos os intents E03). Não executar nem custodiar dinheiro — o gateway executa; o Salesforce é motor de regras (ADR 0003). Não processar a crítica de forma síncrona no clique do upload (pico ~28/s excede o teto de 25 Apex longos concorrentes — INT-035). Não emitir boleto duplicado nem aplicar efeito financeiro duplicado (idempotência — INT-040, INT-042). Não adotar Revenue Cloud/Billing — split não é nativo (motor custom, ADR 0004). Não enviar CPF a LLM nem logar dado sensível (ADR 0001).

## Pré-decidido (não re-litigar)
- **Fronteira CRM-não-transacional (ADR 0003)**: Salesforce = motor de regras de split, boletagem, conciliação por casamento; o gateway PCI (cliente) executa e custodia. O Salesforce entrega ordens de transferência; não move dinheiro.
- **Split não é nativo**: motor de regras custom sobre baseline Core-only (ADR 0004; KB confirma que Billing não cobre split multipartes).
- **Assíncrono por capacidade**: o upload da folha é desacoplado (fila), forçado pelo pico ~28/s vs. teto de 25 Apex longos concorrentes (INT-035).
- **Sem persistência de linhas**: só cabeçalho/competência da folha (ADR 0001, premissa de discovery G0310).
- **Facilitadora API-only**: baixa a folha por contrato/vigência e devolve 'processado'+valor por API, sem UI (ADR 0004).
- **Teto MDR 3,6% e repasse ≤15 dias** (Decreto 12.712/2025) parametrizados no motor de split (INT-043).

## Estado inicial (de Marketplace & Credenciamento — Frentes Paralelas (28/set – 18/out · Sem. 7-9))

Você deve encontrar isto já deployado na sandbox:
- **Marketplace & Credenciamento — Frentes Paralelas (28/set – 18/out · Sem. 7-9) — resultado:** MARCO DE ENTREGA DE JORNADA (UAT): beneficiária publica a demanda (Opportunity), facilitadoras enviam Quotes via API (ocultas até o fechamento), tela 'Comparar Propostas' operante, seleção manual registra o vencedor; estabelecimentos se credenciam via gov.br PJ (CNPJ) com aprovação da facilitadora e checagem de vigilância sanitária. Capacidades principais: leilão reverso + credenciamento.

## Perguntas do modo Plan (resolver antes de passar ao modo Build)
- Provedor do gateway/banco custódia não definido (G0309) — **risco #1 da fase**: sem parceiro contratado e integrado, o financeiro não vai a produção em 15/nov. Contrato de API (boleto/Pix, webhook de retorno) a definir (INT-040, INT-042, INT-044).
- Regras de conciliação e tratamento de divergência por lote incremental indefinidas (G0304): pagamento parcial, valor a maior/menor, estorno, não-casado (INT-042).
- Layout exato do CSV da folha (colunas, encoding, volume) e se é único da plataforma ou por facilitadora (G0306, INT-035, INT-036).
- Qual a melhor alternativa Salesforce para a crítica (Einstein, Agentforce, Apex determinístico) e o que ela deve criticar (INT-037 — confiança Unknown).
- A partir de qual evento conta o prazo ≤15 dias e há enforcement ou só registro? Como a taxa MTE se distingue do teto de 3,6% (INT-043).
- Notificação via CTPS Digital é escopo Salesforce (via MuleSoft) ou do MTE, e existe contrato de API (INT-045)?

## Perguntas do modo Build (perguntar só se a situação surgir)
- Mecanismo assíncrono concreto (Platform Events / Queueable / Batch) para a recepção e a crítica (INT-035, INT-037).
- Onde reside o log auditável imutável e sua retenção (Shield/Event Monitoring vs. MuleSoft/Dataprev) — INT-044.
- Chave de idempotência do retorno 'processado' e do casamento de conciliação (INT-039, INT-042).

## Épicas no escopo desta fase

O brief de fase é autoritativo. As épicas abaixo estão listadas apenas para referência cruzada — quando uma automação cita `(E04)`, é a isto que ela se refere. Para a narrativa mais profunda da épica, veja `90-epics-context.md`.

- **E03: Folha & Financeiro** — Ciclo folha→pagamento→split sob a regra de repasse em até 15 dias (Decreto 12.712/2025). FLUXO (premissa 31/jul): (1) a beneficiária faz UPLOAD do CSV de folha da competência via PORTAL ou API; (2) a plataforma VALIDA o layout do arquivo e a integridade ('não quebrado') — avaliar a melhor alternativa Salesforce para as críticas (Einstein / agente / outro); (3) SEM crítica, habilita o arquivo para DOWNLOAD da facilitadora — as LINHAS DA FOLHA NÃO SÃO CARREGADAS em objeto da plataforma (necessidade futura de roadmap, não agora); (4) a facilitadora baixa a folha associada ao contrato do beneficiário na vigência mês/ano específica e DEVOLVE via API o status 'processado' + o valor a pagar; (5) a plataforma envia o valor ao GATEWAY (que intermedia a conta custódia) e recebe de volta o BOLETO REGISTRADO + metadados/link; (6) o boleto é disponibilizado à beneficiária no portal para download e pagamento; (7) a plataforma recebe do gateway as MOVIMENTAÇÕES BANCÁRIAS de forma BATCH INCREMENTAL via AGENDAMENTO no MuleSoft (E05) para identificar o pagamento e avançar status; (8) identificado o pagamento, o sistema consulta as REGRAS DE CÁLCULO DE SPLIT, calcula o repasse à facilitadora e demais empresas, e REGISTRA todo o racional (datas, split, ordens/boletagens de transferência), entregando via MuleSoft ao gateway. FRONTEIRA (ADR 0003): o Salesforce é o MOTOR DE REGRAS DE SPLIT (calcula, aplica, emite boletagem, orquestra, concilia por casamento, registra racional); o GATEWAY é o ÚNICO responsável pela EXECUÇÃO das transações bancárias e pela custódia — FORA do escopo Salesforce. UI simplificada: status consolidado 'crédito concedido' (uma linha, não lista por trabalhador); marca é o gatilho de notificação à empresa e via CTPS Digital ('expectativa de crédito', só monitoramento na Fase 1). Objetos custom para folha (cabeçalho/competência, sem linhas), contrato e regras de split; Revenue Cloud fora desta rodada. Lógica financeira real → XL.

## Alvos de construção — resumo de orquestração

Estas seções orientam o agente de construção sobre o formato da fase. O detalhe construível por capacidade (Resultado, Alvo de construção, Guardrails, Fora de escopo, Aceite, Perguntas em aberto) vive em `11-intents-3.md` por intent. Quando uma seção abaixo cita `INT-NNN`, consulte o intent lá.

### Modelo de dados
Modelo de dados financeiro custom sobre a base nativa (INT-038): folha por competência (só cabeçalho — sem linhas do trabalhador), contrato/vigência que a facilitadora usa para baixar por competência, e regras de split parametrizáveis (percentuais por parte, teto MDR, prazo de repasse, distinção PAT vs. não-PAT). Sem Revenue Cloud/Billing. O detalhe vive em INT-038.

### Automação
O coração regulado da solução, todo assíncrono. Validação de layout/integridade (INT-036) e crítica por IA a definir (INT-037); conciliação agendada por lotes incrementais com casamento e tratamento de divergência (INT-042); motor de regras de split com teto MDR 3,6%, repasse ≤15 dias e ramificação PAT/não-PAT (INT-043); registro do racional auditável + entrega das ordens de transferência ao gateway com idempotência (INT-044); status consolidado 'crédito concedido' (uma linha por folha) e gatilho de notificação à empresa e via CTPS Digital (INT-045). O detalhe vive nesses intents.

### UI & navegação
Superfície mínima no portal (Experience Cloud): a beneficiária envia a folha e encontra o boleto registrado disponível, vinculado à competência (INT-041), com status consolidado do ciclo — sem lista por trabalhador. UI simplificada; a facilitadora não tem tela (API-only).

### Segurança & acesso
Herda a residência híbrida e a trilha de auditoria da Etapa 1 (ADR 0001, INT-011, INT-012). A trilha do racional de split é imutável e consultável por conformidade (TCU/CGU/ANPD) sem persistir CPF (INT-044). Nenhuma linha de folha nem dado sensível do trabalhador persiste; a crítica por IA não recebe CPF em prompt/log (INT-037).

### Relatórios & dashboards
Sem dashboards financeiros dedicados na Fase 1. A trilha auditável do racional de split (INT-044) e o status consolidado 'crédito concedido' (INT-045) são os artefatos de dados desta fase, voltados à conformidade (TCU/CGU/ANPD) e à consulta no portal — não a relatórios de gestão, que ficam para onda futura.

### Dados de exemplo
_(opcional — carregar só a pedido do usuário)_

### Fontes de dados

MuleSoft on-premise (Etapa 1) como hub. Fontes: portal/API para recepção assíncrona da folha (INT-035); facilitadora para download da folha e retorno 'processado'+valor (INT-039, contrato INT-006); gateway/banco custódia para solicitação e retorno do boleto registrado (INT-040), feed agendado de movimentações bancárias para conciliação (INT-008, INT-042) e recepção das ordens de transferência (INT-044); CTPS Digital para a notificação de 'expectativa de crédito' (INT-045, fronteira a confirmar).

## Aceite — verificações de resultado para o usuário (nível de fase)

Phase-level user-outcome claims a stakeholder would walk through to feel "Etapa 3 is done." Run them in conversation with the user; mark `- [x]` somente quando o usuário concordar. Os walkthroughs de aceite por intent vivem em `11-intents-3.md`.

Uma beneficiária envia o CSV da folha da competência e recebe confirmação de recebimento em segundos; o arquivo é validado e criticado de forma assíncrona; a facilitadora baixa a folha por contrato/vigência via API e devolve 'processado' + valor; o gateway emite o boleto registrado, que a beneficiária encontra no portal; ao pagar, a conciliação por lote casa o pagamento, o motor calcula o split sob o teto de 3,6% e prazo ≤15 dias, as ordens de transferência vão ao gateway com trilha auditável, e a folha exibe 'crédito concedido' em uma linha — sem que nenhuma linha de trabalhador tenha sido persistida.

## Aceite — verificações em forma de metadados (nível de fase)

Verificações em forma de metadados, no nível da fase — consultas que o agente de construção roda contra a org alvo sem ajuda humana. Rode via a skill Metadata (describe / tooling / SOQL). O aceite por intent está em `11-intents-3.md`.

Verifica-se: (a) o upload retorna confirmação e enfileira sem processar a crítica síncrona (INT-035); (b) só o cabeçalho/competência persiste — nenhuma linha de trabalhador (INT-038, todos E03); (c) folha inconsistente é sinalizada e não liberada ao download (INT-036); (d) o retorno 'processado' e o casamento de conciliação são idempotentes (INT-039, INT-042); (e) o boleto não é duplicado em retentativa (INT-040); (f) o split respeita o teto MDR 3,6% e sinaliza risco de estouro do prazo ≤15 dias, ramificando PAT/não-PAT (INT-043); (g) o racional é registrado de forma imutável sem CPF e as ordens de transferência são entregues ao gateway — sem o Salesforce mover dinheiro (INT-044); (h) divergências de conciliação vão a um caminho de exceção, sem falha silenciosa (INT-042).

## Fora do escopo da Etapa 3

Se você perceber que precisa construir qualquer um destes, pare e sinalize — pertence a uma fase posterior ou está explicitamente excluído.

_(nenhum surgiu em gaps.json — confirme com o usuário na revisão do modo Plan)_

## Dependências e riscos

**Dependências:** Etapa 0 (gateway selecionado — dependência dura), Etapa 1 (E05 integração on-premise com o gateway, E08 residência/soberania). E03 depende de E01 + E05 + E08 + o gateway contratado.

**Riscos:** Provedor do gateway não definido a tempo (G0309) é o risco #1 desta fase — sem o parceiro contratado e integrado, o financeiro não vai a produção em 15/nov; regras de conciliação/divergência por lote incremental ainda indefinidas (G0304); mecânica boleto/Pix e settlement (G0302/G0301); a crítica da folha depende de qual alternativa Salesforce (Einstein/agente) se confirma viável. É a fase XL mais sensível à data fixa; se algo escorregar, é aqui que a pressão de de-escopo bate.

## Citações de histórias cobertas nesta fase

- (US-0301) Como beneficiária, quero fazer upload do arquivo CSV da folha da competência pelo portal, para iniciar o ciclo de pagamento do vale do mês/ano vigente.
- (US-0302) Como beneficiária integrada, quero submeter a folha da competência via API, para automatizar o envio a partir do meu sistema de RH sem uso do portal.
- (US-0303) Como plataforma, quero validar o layout do arquivo de folha recebido, para rejeitar arquivos fora do padrão antes de qualquer processamento.
- (US-0304) Como plataforma, quero validar a integridade e as críticas de negócio do arquivo de folha, para garantir consistência dos dados antes de liberá-lo à facilitadora.
- (US-0305) Como plataforma, quero avaliar o uso de Einstein/agente para apoiar as críticas do arquivo, para acelerar a detecção de anomalias sem depender só de regras fixas.
- (US-0306) Como beneficiária, quero visualizar as críticas do meu arquivo e reenviá-lo corrigido, para desbloquear o processamento da folha.
- (US-0307) Como plataforma, quero habilitar o arquivo validado para download da facilitadora, para que ela obtenha a folha vinculada ao contrato na vigência mês/ano.
- (US-0308) Como facilitadora, quero baixar via API a folha associada ao meu contrato na vigência da competência, para processá-la no meu sistema de crédito.
- (US-0309) Como facilitadora, quero devolver via API o status 'processado' e o valor a pagar da folha, para que a plataforma inicie a emissão do boleto.
- (US-0310) Como plataforma, quero modelar um objeto custom de cabeçalho/competência da folha (sem linhas), para rastrear o ciclo sem carregar os itens da folha na Fase 1.
- (US-0311) Como administrador financeiro do MTE, quero cadastrar e versionar as regras de cálculo de split, para que o motor aplique os percentuais corretos de repasse.
- (US-0312) Como plataforma, quero enviar o valor a pagar ao gateway (conta custódia), para solicitar a emissão do boleto registrado.
- (US-0313) Como gateway, quero devolver à plataforma o boleto registrado com seus metadados e link, para que a plataforma o disponibilize à beneficiária.
- (US-0314) Como beneficiária, quero acessar o boleto registrado no portal, para efetuar o pagamento da folha da competência.
- (US-0315) Como plataforma, quero receber do gateway as movimentações bancárias em batch incremental por agendamento no MuleSoft, para identificar os pagamentos realizados.
- (US-0316) Como plataforma, quero conciliar cada movimentação bancária ao boleto por casamento, para confirmar o pagamento da folha correspondente.
- (US-0317) Como plataforma, quero garantir idempotência em todo o processamento financeiro, para evitar boletagem, conciliação ou repasse em duplicidade.
- (US-0318) Como plataforma, quero, ao identificar o pagamento, consultar as regras de cálculo de split vigentes, para determinar os repasses às partes.
- (US-0319) Como plataforma, quero aplicar o teto de taxa (MDR) de 3,6% no cálculo do split, para respeitar o limite regulatório da reforma de nov/2025.
- (US-0320) Como plataforma, quero distinguir transações PAT de não-PAT no cálculo do split, para aplicar a regra correta a cada tipo de operação.
- (US-0321) Como plataforma, quero calcular o repasse à facilitadora e às demais empresas, para gerar as boletagens de repasse do ciclo.
- (US-0322) Como plataforma, quero controlar o prazo de repasse em até 15 dias, para cumprir o prazo regulatório de repasse às redes credenciadas.
- (US-0323) Como plataforma, quero emitir as boletagens de repasse e entregá-las ao gateway via MuleSoft, para que o gateway execute as transações bancárias das partes.
- (US-0324) Como administrador financeiro do MTE, quero que o sistema registre o racional completo do ciclo (datas, split, boletagens), para dispor de trilha de auditoria do repasse.
- (US-0325) Como beneficiária, quero ver um status consolidado 'crédito concedido' no portal, para acompanhar de forma simples o resultado do ciclo sem detalhes financeiros internos.
- (US-0326) Como plataforma, quero disparar notificação à empresa quando o crédito é concedido, para informar a beneficiária sobre a conclusão do ciclo.
- (US-0327) Como plataforma, quero enviar à CTPS Digital a 'expectativa de crédito' do trabalhador, para monitoramento na Fase 1, sem gestão de saldo.
- (US-0328) Como administrador financeiro do MTE, quero tratar as movimentações não casadas e as exceções do ciclo, para resolver pagamentos que não conciliaram automaticamente.
- (US-0329) Como administrador financeiro do MTE, quero relatórios de conciliação e repasses por competência, para acompanhar volumes, prazos e taxas aplicadas.
- (US-0330) Como plataforma, quero orquestrar as transições de status da folha ao longo do ciclo, para dar rastreabilidade fim-a-fim de recebido a crédito concedido.
- (US-0331) Como facilitadora, quero consultar via API o status corrente de uma folha e seus boletos de repasse, para reconciliar no meu sistema sem depender do portal.

## Fronteira de recipe

Quando esta fase for aceita, pergunte ao usuário: *"Salvar esta execução como recipe para repetirmos na Etapa 4?"* A recipe deve capturar: as decisões de modelo de dados feitas acima, os padrões de nomenclatura confirmados em `03-glossary-and-naming.md`, e quaisquer resoluções de perguntas do modo Build que surgiram.
