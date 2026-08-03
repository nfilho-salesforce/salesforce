## INTENT FOR
A beneficiária (publica a demanda, compara e seleciona), a facilitadora (responde via API), o estabelecimento (autocadastra e envia documentos) e o Analista MTE (analisa e emite parecer de credenciamento).

## INTENT OUTCOME
Construir o valor mais visível da reforma sobre os objetos nativos da Fase 1: o leilão reverso (E02 — demanda como Opportunity → facilitadoras respondem com Quote via API, ocultas até o fechamento → comparação lado a lado → seleção manual → contrato sem CLM) e o credenciamento de estabelecimentos (E04 — autocadastro gov.br PJ, envio documental, validação com transbordo humano, licença sanitária). Duas frentes paralelas sobre o modelo de dados fundacional.

## INTENT MEASURED BY
Marco de entrega de jornada (UAT): beneficiária publica a demanda (INT-019), facilitadoras enviam Quotes via API ocultas até o fechamento (INT-020, INT-021), tela 'Comparar Propostas' operante (INT-022), seleção manual registra o vencedor e firma contrato (INT-023, INT-024); estabelecimentos credenciam-se via gov.br PJ com aprovação da facilitadora e checagem de vigilância sanitária (INT-028..033).

## INTENT MUST NOT
Não expor a Quote concorrente antes do fechamento da vigência (equidade por construção — facilitadora é API-only, não vê a tela). Não introduzir CLM — contrato é PDF imutável versionado (INT-024). Não fazer seleção automática de vencedor — a seleção é manual da beneficiária (INT-023). Data Cloud para enriquecimento fica FORA do MVP (buffer). Não persistir CPF (ADR 0001).

## PRE-DECIDED
- **Leilão reverso em objetos nativos (ADR 0004)**: Opportunity = demanda, Quote = resposta da facilitadora via API; Quotes ocultas até o fechamento por design (facilitadora API-only, sem tela — sem regra custom de ocultamento).
- **Seleção manual**: a beneficiária compara lado a lado e seleciona só quando a vigência fecha (decision_log, roadmap).
- **Contrato SEM CLM**: PDF imutável versionado (INT-024, decision_log).
- **Descoberta de demanda pela facilitadora**: MVP entrega ENDPOINT DE CONSULTA (pull via API/MuleSoft, INT-006); notificação ativa (push) fica no roadmap futuro (decision_log).
- **Credenciamento via gov.br PJ (CNPJ)** com aprovação da facilitadora e checagem sanitária; Novo PAT permanece system-of-record onde aplicável.
- **Frentes paralelizáveis**: E02 e E04 dependem de E01+E05 (Fase 1), baixa dependência entre si.

## PLAN-MODE QUESTIONS
- Regras de seleção/desempate e conformidade Lei 14.133/2021 indefinidas (G0202/G0203): como se decide o vencedor além do preço? Precisa fechar antes do build de INT-023.
- Conflito de system-of-record do credenciamento (G0401): quem é a fonte da verdade do estabelecimento — plataforma ou Novo PAT?
- 5000+ padrões municipais de vigilância sanitária: extração por IA (INT-033) + transbordo humano — qual o limiar de confiança para transbordo?
- A tela de comparação estava ausente no protótipo (G0201): validar o layout de 'Comparar Propostas' (INT-022) com a beneficiária.

## BUILD-MODE QUESTIONS
- Campos da Quote expostos na tela de comparação (INT-022) e critérios de ordenação.
- Mecânica exata do versionamento do PDF de contrato (INT-024) — retenção e imutabilidade.
- Contrato de API da facilitadora para submissão de Quote e pull de demandas (herdado de INT-006).
- Formato dos documentos do estabelecimento e checklist guiado (INT-029); campos extraídos da licença sanitária (INT-033).

## DATA MODEL
O leilão vive nos objetos nativos (Opportunity/Quote) já modelados na Fase 1; esta fase adiciona o upload e versionamento do PDF de contrato sem CLM (INT-024), a carga de contratos legados (INT-027) e a estrutura do termo de aceite classificado por faixa salarial e matriz/filial que alimenta o Novo PAT (INT-025). O detalhe vive nesses intents.

## AUTOMATION
Recepção de Quotes das facilitadoras via API dentro da vigência (INT-020); máquina de estados da janela de vigência com trava de seleção até o fechamento (INT-021 — o mecanismo de equidade); ramificação de regras de cálculo PAT vs. não-PAT (INT-026). No credenciamento: validação documental automatizada com transbordo humano (INT-030), extração de campos da licença sanitária por IA (INT-033) e rastreio de vencimento/renovação com alertas (INT-034).

## UI
Portal (Experience Cloud) para publicar a demanda como Opportunity (INT-019), autocadastro do estabelecimento via gov.br PJ (INT-028) e envio de documentos com checklist guiado (INT-029). LWC 'Comparar Propostas' lado a lado (INT-022) e Screen Flow de seleção do vencedor → firmamento (INT-023) e de termo de aceite (INT-025). Console do Analista MTE para análise documento a documento e parecer (INT-031) e ação legal de aprovar/descredenciar com propagação de status (INT-032).

## SECURITY
Herda a identidade gov.br e o acesso por papel da Fase 1 (INT-014, INT-017). A facilitadora não tem seat de portal — responde só por API (ADR 0004), o que garante que não vê a proposta concorrente sem regra custom. Nenhum CPF persiste (ADR 0001).

## DATA SOURCES
gov.br PJ para autenticação/cadastro do estabelecimento (INT-028); contrato padrão da facilitadora via MuleSoft para Quote e pull de demandas (INT-006, Fase 1); Novo PAT para o termo de aceite classificado (INT-025); fontes de vigilância sanitária municipal para checagem (INT-033). Enriquecimento via Data Cloud fica FORA do MVP.

## ACCEPTANCE USER
Uma beneficiária publica a demanda no portal; duas facilitadoras enviam Quotes via API que permanecem ocultas até a vigência fechar; ao fechar, a beneficiária abre 'Comparar Propostas', vê as respostas lado a lado, seleciona manualmente o vencedor e o contrato é firmado como PDF versionado — sem CLM. Em paralelo, um estabelecimento autocadastra-se via gov.br PJ, envia documentos pelo checklist, a validação automática aprova o que pode e transborda o restante ao Analista MTE, que emite parecer.

## ACCEPTANCE METADATA
Verifica-se: (a) Quotes submetidas via API ficam inacessíveis à leitura entre facilitadoras até o fechamento da vigência (INT-020, INT-021); (b) a seleção só é habilitada após o fechamento e registra o vencedor (INT-021, INT-023); (c) o contrato é gravado como PDF imutável versionado, sem objeto de CLM (INT-024); (d) o cálculo ramifica corretamente PAT vs. não-PAT (INT-026); (e) documentos do estabelecimento com baixa confiança de extração são roteados ao console humano (INT-030, INT-031); (f) campos da licença sanitária são extraídos e o vencimento rastreado com alerta (INT-033, INT-034); (g) nenhum CPF é persistido.

## REPORTS
Sem relatórios/dashboards dedicados no MVP desta fase. A visibilidade sistêmica do governo sobre o leilão e o credenciamento é derivável dos objetos nativos (Opportunity/Quote e status de credenciamento), mas dashboards de gestão não estão no escopo comprometido de 15/nov — candidatos a onda futura.
