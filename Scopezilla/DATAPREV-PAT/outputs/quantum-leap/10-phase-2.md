# Etapa 2 — Marketplace & Credenciamento — Frentes Paralelas (28/set – 18/out · Sem. 7-9) (DATAPREV-PAT)

> **Orquestração da fase — o que está dentro/fora da fase, dependências, estado inicial.** Leia isto primeiro para se orientar. As especificações construíveis por capacidade vivem em `11-intents-2.md` (quando presente) — é contra elas que você de fato constrói, um intent por vez.
> Duração da fase: **3 semanas (compromisso do usuário)**.

## Intenção

- **Para:** A beneficiária (publica a demanda, compara e seleciona), a facilitadora (responde via API), o estabelecimento (autocadastra e envia documentos) e o Analista MTE (analisa e emite parecer de credenciamento).
- **Resultado:** Construir o valor mais visível da reforma sobre os objetos nativos da Etapa 1: o leilão reverso (E02 — demanda como Opportunity → facilitadoras respondem com Quote via API, ocultas até o fechamento → comparação lado a lado → seleção manual → contrato sem CLM) e o credenciamento de estabelecimentos (E04 — autocadastro gov.br PJ, envio documental, validação com transbordo humano, licença sanitária). Duas frentes paralelas sobre o modelo de dados fundacional.
- **Medido por:** Marco de entrega de jornada (UAT): beneficiária publica a demanda (INT-019), facilitadoras enviam Quotes via API ocultas até o fechamento (INT-020, INT-021), tela 'Comparar Propostas' operante (INT-022), seleção manual registra o vencedor e firma contrato (INT-023, INT-024); estabelecimentos credenciam-se via gov.br PJ com aprovação da facilitadora e checagem de vigilância sanitária (INT-028..033).
- **Não deve:** Não expor a Quote concorrente antes do fechamento da vigência (equidade por construção — facilitadora é API-only, não vê a tela). Não introduzir CLM — contrato é PDF imutável versionado (INT-024). Não fazer seleção automática de vencedor — a seleção é manual da beneficiária (INT-023). Data Cloud para enriquecimento fica FORA da Fase 1 (buffer). Não persistir CPF (ADR 0001).

## Pré-decidido (não re-litigar)
- **Leilão reverso em objetos nativos (ADR 0004)**: Opportunity = demanda, Quote = resposta da facilitadora via API; Quotes ocultas até o fechamento por design (facilitadora API-only, sem tela — sem regra custom de ocultamento).
- **Seleção manual**: a beneficiária compara lado a lado e seleciona só quando a vigência fecha (decision_log, roadmap).
- **Contrato SEM CLM**: PDF imutável versionado (INT-024, decision_log).
- **Descoberta de demanda pela facilitadora**: Fase 1 entrega ENDPOINT DE CONSULTA (pull via API/MuleSoft, INT-006); notificação ativa (push) fica no roadmap futuro (decision_log).
- **Credenciamento via gov.br PJ (CNPJ)** com aprovação da facilitadora e checagem sanitária; Novo PAT permanece system-of-record onde aplicável.
- **Frentes paralelizáveis**: E02 e E04 dependem de E01+E05 (Etapa 1), baixa dependência entre si.

## Estado inicial (de Fundação — Modelo de Dados + Identidade + Integração + Residência (31/ago – 27/set · Sem. 3-6))

Você deve encontrar isto já deployado na sandbox:
- **Fundação — Modelo de Dados + Identidade + Integração + Residência (31/ago – 27/set · Sem. 3-6) — resultado:** MODELO DE DADOS FUNDACIONAL definido e ratificado com o time inteiro (objetos nativos Opportunity/Quote/Account + termo de aceite) — MARCO que libera a paralelização das demais frentes; camada API-led MuleSoft on-premise de pé com mocks (incluindo o contrato de integração com o gateway); modelo de referência tokenizada implementado e resolvendo em runtime na org greenfield dedicada; portal Partner Community com login gov.br funcional e Contact por referência tokenizada. Base pronta para o marketplace.

## Perguntas do modo Plan (resolver antes de passar ao modo Build)
- Regras de seleção/desempate e conformidade Lei 14.133/2021 indefinidas (G0202/G0203): como se decide o vencedor além do preço? Precisa fechar antes do build de INT-023.
- Conflito de system-of-record do credenciamento (G0401): quem é a fonte da verdade do estabelecimento — plataforma ou Novo PAT?
- 5000+ padrões municipais de vigilância sanitária: extração por IA (INT-033) + transbordo humano — qual o limiar de confiança para transbordo?
- A tela de comparação estava ausente no protótipo (G0201): validar o layout de 'Comparar Propostas' (INT-022) com a beneficiária.

## Perguntas do modo Build (perguntar só se a situação surgir)
- Campos da Quote expostos na tela de comparação (INT-022) e critérios de ordenação.
- Mecânica exata do versionamento do PDF de contrato (INT-024) — retenção e imutabilidade.
- Contrato de API da facilitadora para submissão de Quote e pull de demandas (herdado de INT-006).
- Formato dos documentos do estabelecimento e checklist guiado (INT-029); campos extraídos da licença sanitária (INT-033).

## Épicas no escopo desta fase

O brief de fase é autoritativo. As épicas abaixo estão listadas apenas para referência cruzada — quando uma automação cita `(E04)`, é a isto que ela se refere. Para a narrativa mais profunda da épica, veja `90-epics-context.md`.

- **E02: Marketplace de Cotação e Contratação** — Motor do 'leilão' reverso sobre SALES CLOUD com objetos NATIVOS (ADR 0004): a beneficiária cadastra a demanda como OPPORTUNITY nativa (nº funcionários, valor, vigência, distribuição por UF, recursos obrigatórios); N facilitadoras respondem com QUOTES nativas (prazo/SLA) EXCLUSIVAMENTE via API — a facilitadora NÃO tem acesso à plataforma (sem UI, sem licença de portal); submete a proposta informando o ID da cotação/oportunidade aberta dentro da vigência (G0210, confirmado grill 31/jul). COMO A FACILITADORA DESCOBRE UMA DEMANDA (decisão 31/jul): na Fase 1 a plataforma ENTREGA UM ENDPOINT DE CONSULTA (pull via API/MuleSoft, E05) das demandas abertas na vigência — a facilitadora CONSULTA, NÃO recebe push ativo; a NOTIFICAÇÃO ATIVA (push) fica no roadmap futuro, com o CANAL A DEFINIR — a escolha do canal é o que condiciona posicionar ou não Marketing Cloud (G0209/G0211). EQUIDADE POR CONSTRUÇÃO: como a facilitadora não tem UI, ela não enxerga as propostas concorrentes — não é necessário Apex managed sharing para ocultá-las. A beneficiária VÊ as cotações conforme chegam (comparação lado a lado, LWC), mas só PODE SELECIONAR quando a janela de vigência fecha — seleção manual TRAVADA até o fechamento, não seleção cega (confirmado grill 31/jul). Camada custom fina: tela Comparar Propostas + trava de seleção até o fechamento + máquina de estados da janela → contrato firmado. CONTRATO SEM CLM na Fase 1 (transcrição 31/jul): a facilitadora faz upload do PDF imutável do contrato + metadados + versões (aditivos/renovações como upload de nova versão); NÃO há ferramenta de contract lifecycle management nem validação automática de contrato nesta versão (roadmap futuro). PASSO NOVO — TERMO DE ACEITE (transcrição 31/jul, Fase 1-required): após o contrato firmado, a beneficiária dá o termo de aceite classificando nº de trabalhadores acima/abaixo de 5 salários mínimos por CNPJ e a distribuição matriz/filial — informação integrada ao Novo PAT via INIS PJ (E05). Matriz/filial: ao aderir, todas as filiais entram. BENEFICIÁRIAS PAT E NÃO-PAT (transcrição 31/jul): ambas contratam pelo marketplace, com regras de cálculo distintas (PAT sob teto 3,6%; não-PAT sem benefício fiscal → taxa diferente); contratos legados devem ser carregados. Camada custom reservada ao que o nativo não entrega (equidade, tela Comparar Propostas, seleção→contrato). Data Cloud para enriquecer histórico de facilitadoras — Assumed, candidato a de-escopo/buffer sob a janela fixa de 15/nov.
- **E04: Credenciamento de Estabelecimentos** — Cadastro unificado de estabelecimentos via gov.br PJ; facilitadoras mantêm o papel legal de aprovar e descredenciar. Duas faces (protótipos): a do estabelecimento que cadastra e sobe documentos, e a do Analista MTE que analisa documento a documento (Válido/Inválido + motivo), emite parecer (Deferido/Exigência complementar/Indeferido) e opera a trilha de auditoria. Fluxo automatizado de validação com TRANSBORDO humano para exceções. VIGILÂNCIA SANITÁRIA (transcrição 31/jul): 5000+ padrões municipais de licença, SEM base unificada — a data de validade é o parâmetro mínimo comum; IA pode extrair alguns campos. Inclui FLUXO DE RENOVAÇÃO e ALERTAS de expiração de documentos/licenças (rastreio de vencimento). Distinção de domínio: a ADQUIRENTE (Cielo, Rede, Getnet) consulta a base de estabelecimentos (via API, E05) antes de processar transações e envia todas as transações para monitoramento; a FACILITADORA é responsável pela custódia. Driver de negócio (Decreto 12.712/2025): o modelo antigo obrigava o estabelecimento a credenciar-se facilitadora a facilitadora (um contrato por operadora, MDR alto/variável, repasse caso a caso). A reforma inverte a economia — teto de MDR de 3,6%, repasse em até 15 dias, fim do rebate e interoperabilidade (um credenciamento/terminal aceita todas as bandeiras; mai/2026 grandes, nov/2026 total) — tornando o cadastro unificado a via de menor custo e menor fricção. É esse value driver que sustenta a adesão do estabelecimento.

## Alvos de construção — resumo de orquestração

Estas seções orientam o agente de construção sobre o formato da fase. O detalhe construível por capacidade (Resultado, Alvo de construção, Guardrails, Fora de escopo, Aceite, Perguntas em aberto) vive em `11-intents-2.md` por intent. Quando uma seção abaixo cita `INT-NNN`, consulte o intent lá.

### Modelo de dados
O leilão vive nos objetos nativos (Opportunity/Quote) já modelados na Etapa 1; esta fase adiciona o upload e versionamento do PDF de contrato sem CLM (INT-024), a carga de contratos legados (INT-027) e a estrutura do termo de aceite classificado por faixa salarial e matriz/filial que alimenta o Novo PAT (INT-025). O detalhe vive nesses intents.

### Automação
Recepção de Quotes das facilitadoras via API dentro da vigência (INT-020); máquina de estados da janela de vigência com trava de seleção até o fechamento (INT-021 — o mecanismo de equidade); ramificação de regras de cálculo PAT vs. não-PAT (INT-026). No credenciamento: validação documental automatizada com transbordo humano (INT-030), extração de campos da licença sanitária por IA (INT-033) e rastreio de vencimento/renovação com alertas (INT-034).

### UI & navegação
Portal (Experience Cloud) para publicar a demanda como Opportunity (INT-019), autocadastro do estabelecimento via gov.br PJ (INT-028) e envio de documentos com checklist guiado (INT-029). LWC 'Comparar Propostas' lado a lado (INT-022) e Screen Flow de seleção do vencedor → firmamento (INT-023) e de termo de aceite (INT-025). Console do Analista MTE para análise documento a documento e parecer (INT-031) e ação legal de aprovar/descredenciar com propagação de status (INT-032).

### Segurança & acesso
Herda a identidade gov.br e o acesso por papel da Etapa 1 (INT-014, INT-017). A facilitadora não tem seat de portal — responde só por API (ADR 0004), o que garante que não vê a proposta concorrente sem regra custom. Nenhum CPF persiste (ADR 0001).

### Relatórios & dashboards
Sem relatórios/dashboards dedicados na Fase 1 desta fase. A visibilidade sistêmica do governo sobre o leilão e o credenciamento é derivável dos objetos nativos (Opportunity/Quote e status de credenciamento), mas dashboards de gestão não estão no escopo comprometido de 15/nov — candidatos a onda futura.

### Dados de exemplo
_(opcional — carregar só a pedido do usuário)_

### Fontes de dados

gov.br PJ para autenticação/cadastro do estabelecimento (INT-028); contrato padrão da facilitadora via MuleSoft para Quote e pull de demandas (INT-006, Etapa 1); Novo PAT para o termo de aceite classificado (INT-025); fontes de vigilância sanitária municipal para checagem (INT-033). Enriquecimento via Data Cloud fica FORA da Fase 1.

## Aceite — verificações de resultado para o usuário (nível de fase)

Phase-level user-outcome claims a stakeholder would walk through to feel "Etapa 2 is done." Run them in conversation with the user; mark `- [x]` somente quando o usuário concordar. Os walkthroughs de aceite por intent vivem em `11-intents-2.md`.

Uma beneficiária publica a demanda no portal; duas facilitadoras enviam Quotes via API que permanecem ocultas até a vigência fechar; ao fechar, a beneficiária abre 'Comparar Propostas', vê as respostas lado a lado, seleciona manualmente o vencedor e o contrato é firmado como PDF versionado — sem CLM. Em paralelo, um estabelecimento autocadastra-se via gov.br PJ, envia documentos pelo checklist, a validação automática aprova o que pode e transborda o restante ao Analista MTE, que emite parecer.

## Aceite — verificações em forma de metadados (nível de fase)

Verificações em forma de metadados, no nível da fase — consultas que o agente de construção roda contra a org alvo sem ajuda humana. Rode via a skill Metadata (describe / tooling / SOQL). O aceite por intent está em `11-intents-2.md`.

Verifica-se: (a) Quotes submetidas via API ficam inacessíveis à leitura entre facilitadoras até o fechamento da vigência (INT-020, INT-021); (b) a seleção só é habilitada após o fechamento e registra o vencedor (INT-021, INT-023); (c) o contrato é gravado como PDF imutável versionado, sem objeto de CLM (INT-024); (d) o cálculo ramifica corretamente PAT vs. não-PAT (INT-026); (e) documentos do estabelecimento com baixa confiança de extração são roteados ao console humano (INT-030, INT-031); (f) campos da licença sanitária são extraídos e o vencimento rastreado com alerta (INT-033, INT-034); (g) nenhum CPF é persistido.

## Fora do escopo da Etapa 2

Se você perceber que precisa construir qualquer um destes, pare e sinalize — pertence a uma fase posterior ou está explicitamente excluído.

_(nenhum surgiu em gaps.json — confirme com o usuário na revisão do modo Plan)_

## Dependências e riscos

**Dependências:** Etapa 1 (modelo de dados fundacional ratificado — habilitador da paralelização; E01 portal/identidade Partner Community, E05 integração on-premise). E02 e E04 dependem de E01 + E05; entre si, baixa dependência (paralelizáveis).

**Riscos:** Regras de seleção/desempate e conformidade Lei 14.133/2021 indefinidas (G0202/G0203); tela de comparação ausente no protótipo (G0201); conflito de system-of-record do credenciamento (G0401); 5000+ padrões municipais de vigilância sanitária (extração IA + transbordo humano). Data Cloud para enriquecimento fica FORA da Fase 1 — buffer de cronograma.

## Citações de histórias cobertas nesta fase

- (US-0201) Como Beneficiária, quero autenticar via GOV.BR e selecionar a empresa (CNPJ) que represento por procuração digital, para operar o marketplace apenas nas empresas às quais tenho vínculo válido.
- (US-0202) Como Beneficiária, quero cadastrar uma demanda de benefício como Opportunity nativa informando nº de funcionários, valor por trabalhador, vigência em meses e periodicidade, para iniciar um leilão reverso entre as facilitadoras.
- (US-0203) Como Beneficiária, quero configurar a personalização do vale entre Alimentação e Refeição por percentual, para que as propostas cheguem já normalizadas à minha necessidade.
- (US-0204) Como Beneficiária, quero informar a distribuição de trabalhadores por UF na demanda, para que as facilitadoras precifiquem considerando a dispersão regional.
- (US-0205) Como Beneficiária, quero selecionar os recursos obrigatórios que exijo (app, NFC, geolocalização, histórico, segurança etc.), para padronizar a comparação entre propostas.
- (US-0206) Como Beneficiária, quero que minha demanda tenha um prazo (SLA) de recebimento de propostas com contagem regressiva, para saber quando a janela do leilão fecha.
- (US-0207) Como Facilitadora operando exclusivamente via API (sem UI, sem licença de portal), quero consultar as demandas abertas dentro da vigência através de um endpoint de consulta, para descobrir oportunidades de proposta no modelo pull.
- (US-0208) Como Facilitadora, quero submeter uma proposta como Quote nativa exclusivamente via API informando o ID da cotação/oportunidade aberta, para responder ao leilão sem acessar a plataforma.
- (US-0209) Como Facilitadora, quero que a plataforma me impeça de ver propostas concorrentes, para que a equidade do leilão seja garantida por construção.
- (US-0210) Como Beneficiária, quero uma tela Comparar Propostas (LWC) que exiba lado a lado as propostas recebidas conforme chegam, para avaliar taxas, cobertura e atendimento de recursos.
- (US-0211) Como Beneficiária, quero que o botão de seleção da proposta vencedora fique travado até o fechamento da janela de vigência, para garantir isonomia entre as facilitadoras.
- (US-0212) Como Beneficiária, quero selecionar manualmente a proposta vencedora após o fechamento da janela, para escolher a facilitadora que melhor atende minha demanda.
- (US-0213) Como Admin da plataforma, quero uma máquina de estados que governe a demanda de Nova até Contratada/Concluída sem contrato/Cancelada, para que o ciclo de vida do leilão seja consistente e auditável.
- (US-0214) Como Beneficiária, quero consultar a lista Minhas Cotações com filtros por número, status, data e prazo, para acompanhar o andamento das solicitações enviadas às facilitadoras.
- (US-0215) Como Beneficiária, quero cancelar uma demanda antes do fechamento da janela, para encerrar solicitações criadas por engano ou que não sejam mais necessárias.
- (US-0216) Como Facilitadora, após ser selecionada, quero fazer upload de um contrato em PDF imutável com metadados via API, para firmar a contratação sem um módulo de gestão de ciclo de vida de contrato (sem CLM na Fase 1).
- (US-0217) Como Facilitadora, quero registrar aditivos e renovações como novas versões do contrato, para manter o histórico contratual sem CLM.
- (US-0218) Como Beneficiária, após o contrato firmado, quero dar o termo de aceite classificando o nº de trabalhadores acima e abaixo de 5 salários mínimos por CNPJ, para atender à regra fiscal do PAT.
- (US-0219) Como Beneficiária, quero informar no termo de aceite a distribuição matriz/filial dos trabalhadores por CNPJ, para que a adesão reflita corretamente a estrutura societária.
- (US-0220) Como Admin da plataforma, quero que o termo de aceite finalizado seja integrado ao Novo PAT via INIS PJ, para registrar oficialmente a adesão da beneficiária.
- (US-0221) Como Admin da plataforma, quero validar a situação regular de beneficiária e facilitadora contra o Novo PAT antes de permitir cotação/proposta, para garantir que apenas participantes regulares operem no marketplace.
- (US-0222) Como Beneficiária PAT, quero que o cálculo do benefício respeite o teto de taxa de 3,6% e o benefício fiscal aplicável, para permanecer em conformidade com a reforma do PAT.
- (US-0223) Como Beneficiária NÃO-PAT, quero contratar pelo marketplace com regra de cálculo sem benefício fiscal, para poder usar a plataforma mesmo fora do enquadramento PAT.
- (US-0224) Como Admin da plataforma, quero carregar os contratos legados existentes entre beneficiárias e facilitadoras, para que o histórico contratual esteja disponível na plataforma desde o go-live.
- (US-0225) Como Beneficiária, quero consultar meus contratos firmados com filtros por facilitadora, status e vigência, para localizar rapidamente cada contrato e suas ações (visualizar, download, enviar folha).
- (US-0226) Como Admin da plataforma, quero configurar o catálogo de recursos obrigatórios e o SLA padrão da janela de propostas, para governar as regras do leilão sem depender de desenvolvimento.
- (US-0227) Como Facilitadora, quero consultar via API o status das minhas propostas e contratos, para acompanhar resultados sem acessar a plataforma.
- (US-0228) Como Admin da plataforma, quero uma trilha de auditoria das ações-chave do ciclo de cotação e contratação, para atender às exigências de auditabilidade (TCU/CGU/ANPD).
- (US-0229) Como Admin da plataforma, quero enriquecer o histórico das facilitadoras com dados do Data Cloud, para dar mais contexto na avaliação de propostas — reconhecendo que este item é candidato a de-escopo na Fase 1.
- (US-0230) Como Facilitadora, quero que a notificação ativa (push) de novas demandas seja reconhecida como roadmap futuro com canal a definir, para que a Fase 1 dependa apenas do modelo pull.
- (US-0401) Como Estabelecimento, quero iniciar meu credenciamento entrando com gov.br e selecionando a PJ que represento, para me cadastrar uma única vez e ser aceito por todas as bandeiras/facilitadoras.
- (US-0402) Como Estabelecimento, quero subir os documentos exigidos (incluindo licença de vigilância sanitária), para comprovar minha aptidão a vender alimentação/refeição.
- (US-0403) Como Estabelecimento, quero um assistente de credenciamento que me oriente sobre quais documentos preciso e por que meu cadastro está pendente, para concluir o credenciamento sem depender de suporte manual.
- (US-0404) Como Administrador da Plataforma, quero que cada submissão crie um registro do estabelecimento na base nacional unificada com status controlado, para centralizar a fiscalização e permitir consulta pelas adquirentes.
- (US-0405) Como Administrador da Plataforma, quero rotinas automáticas que validem CNPJ ativo e CNAE compatível com venda de alimentação, para aprovar automaticamente os casos simples e reduzir análise manual.
- (US-0406) Como Analista MTE, quero uma fila de análise onde avalio documento a documento marcando Válido ou Inválido com motivo, para instruir o parecer de credenciamento com rastreabilidade.
- (US-0407) Como Analista MTE, quero emitir um parecer de Deferido, Exigência complementar ou Indeferido, para concluir formalmente a análise do credenciamento.
- (US-0408) Como Analista MTE, quero que apenas as exceções da validação automática cheguem à minha fila (transbordo humano), para concentrar o esforço nos casos que realmente exigem análise.
- (US-0409) Como Administrador da Plataforma, quero registrar a data de validade da licença de vigilância sanitária como parâmetro mínimo comum, para controlar a vigência sem depender de uma base municipal unificada inexistente.
- (US-0410) Como Estabelecimento, quero que a IA extraia automaticamente alguns campos da minha licença sanitária (como a data de validade), para reduzir digitação e erros no cadastro.
- (US-0411) Como Estabelecimento, quero receber alertas antes do vencimento de documentos e licenças, para renovar a tempo e não perder o credenciamento.
- (US-0412) Como Estabelecimento, quero renovar minha licença/documentos pelo portal quando estiverem próximos do vencimento, para manter meu credenciamento ativo.
- (US-0413) Como Facilitadora, quero aprovar o credenciamento do estabelecimento (papel legal de custódia), para autorizar formalmente sua operação após a análise.
- (US-0414) Como Facilitadora, quero descredenciar um estabelecimento (ex.: por perda de licença ou irregularidade), para retirá-lo do programa de forma rastreável.
- (US-0415) Como Adquirente (via API), quero consultar por CNPJ se um estabelecimento está credenciado e apto, para só processar transações de vale alimentação/refeição de estabelecimentos válidos.
- (US-0416) Como Auditor MTE, quero uma trilha de auditoria completa de todo o ciclo de credenciamento, para atender exigências de LGPD, TCU e CGU e responder a fiscalizações.
- (US-0417) Como Estabelecimento, quero uma área no portal para ver o status do meu credenciamento e gerenciar meus dados e documentos, para acompanhar minha situação sem abrir chamados.
- (US-0418) Como Administrador da Plataforma, quero uma carga inicial dos estabelecimentos hoje mantidos pelas facilitadoras, marcando-os como 'migrado', para popular a base nacional unificada sem exigir recadastro imediato de ~800 mil estabelecimentos.
- (US-0419) Como Estabelecimento, quero atender a uma 'Exigência complementar' reenviando ou corrigindo o que foi apontado, para retomar a análise sem recomeçar o credenciamento do zero.

## Fronteira de recipe

Quando esta fase for aceita, pergunte ao usuário: *"Salvar esta execução como recipe para repetirmos na Etapa 3?"* A recipe deve capturar: as decisões de modelo de dados feitas acima, os padrões de nomenclatura confirmados em `03-glossary-and-naming.md`, e quaisquer resoluções de perguntas do modo Build que surgiram.
