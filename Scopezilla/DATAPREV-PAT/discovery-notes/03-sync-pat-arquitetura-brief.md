<!-- Source: "sync PAT" — reunião interna Salesforce × Dataprev (Nelson Stebulaitis Filho, Juliane Lopes, Renata Vendramini) · Registrado: 2026-07-30 · Anotações + Transcrição do Gemini · Retrieved: 2026-07-31 · Via: Nelson (upload PDF) -->

# Brief — sync PAT: arquitetura macro e fluxo ponta a ponta (30/jul/2026)

Síntese estruturada da reunião **interna** de alinhamento técnico (não é call com o cliente). Fonte bruta: `sync PAT - 2026_07_30 15_05 GMT-03_00 - Anotações do Gemini.pdf`. Complementa o `02-call-esclarecimento-brief.md` (call do cliente, mesma data): aquele trouxe **premissas de arquitetura/prazo/volumetria**; este trava o **desenho do fluxo e os produtos Salesforce da solução**. Material **pós-escopo** → entra como **revisão** (revise), não como discovery.

## O que este documento trava (fluxo ponta a ponta acordado)

1. **Login e abertura de cotação (E01/E02)** — login gov.br PF/PJ; PF lista as empresas que representa (procuração) e escolhe a beneficiária que assume. Abertura de cotação guiada por **script**, **Flow** valida campos obrigatórios, cria objeto Cotação status "aberto", **MuleSoft dispara webhooks para todas as facilitadoras cadastradas**. Regra: cotação fica aberta por prazo mínimo configurado pelo MTE.
2. **Processamento e comparação de propostas (E02)** — propostas chegam após o prazo, gravadas em **objetos customizados**, exibidas via **FlexCards** (comparativo = layout). **Data Cloud** decidido para **enriquecer o histórico das facilitadoras** (knowledge/graph). Regra de negócio: **propostas ocultas até o fechamento da janela** (equidade — ninguém vê antes). **Sem algoritmo de decisão** — a **beneficiária** seleciona a melhor proposta manualmente (leilão reverso, escolha humana).
3. **Seleção e formalização de contrato (E02→E03)** — beneficiária seleciona; **contrato firmado FORA da plataforma**, registrado via post da facilitadora. O clique de seleção gera evento no **Flow** → notifica facilitadora via MuleSoft → após recepção do **PDF de metadados**, o CRM atualiza o contrato para **"ativo"**; Salesforce **sugere resumo dos termos em linguagem acessível** (candidato a Agentforce/IA generativa).
4. **Gestão de dados de trabalhadores / folha (E03)** — mensalmente a **beneficiária** sobe **CSV** com trabalhadores + valores de VA/VR. Validação via **OmniScript (client-side) + Apex (linha a linha)**, erros retornados linha a linha. Arquivo encaminhado à facilitadora via MuleSoft. **CPF/dados sensíveis mascarados nos logs de auditoria** (requisito regulatório MTE/LGPD).
5. **Fluxo de pagamento e custódia (E03 — passo NOVO)** — identificada a necessidade de **passo de solicitação de boletos** após o processamento da folha pelas facilitadoras. Envolve: **monitoramento da conta custódia**, **casamento** dos lançamentos com o boleto pago, e **processamento dos repasses/split** — exige **ajustes na comunicação com o banco**. Boleto gerado com valor retornado pela facilitadora; empresa paga por canal bancário normal; confirmação de pagamento via webhook.
6. **Acompanhamento e dashboard (E02/E03)** — empresas veem status de benefícios/contratos **em tempo real** via **dashboard no Experience Cloud** com **FlexCards** por trabalhador. **Marketing Cloud** discutido para **alertas automáticos** (vencimento de contrato, atualização de folha).
7. **Papel das adquirentes (domínio — E04/E03)** — distinção travada: **adquirente (Cielo, Rede, Getnet)** = responsável pelo **crédito no cartão** e pela relação com o estabelecimento credenciado; **facilitadora** = responsável pela **custódia do dinheiro**. A adquirente consulta a base de estabelecimentos antes de processar transações de alto volume.
8. **Integração técnica e validação de estabelecimentos (E05)** — **client credentials flow** para obter token de acesso à API do marketplace; **connected app com escopo restrito**; MuleSoft valida token antes de cada chamada, com **controle de rate limit**. Consulta de estabelecimentos por **CNPJ** para validar credenciamento antes de aprovar transação, com **cache** para otimizar consultas frequentes.
9. **Exibição de status ao beneficiário (E03 — simplificação)** — decisão de **simplificar**: o portal mostra um **status consolidado** ("crédito concedido") em vez de lista detalhada por trabalhador (**uma linha, não 10 mil**). Essa marca de status é o **gatilho** para notificar a empresa da ativação do crédito — e para a notificação via **CTPS** (Carteira de Trabalho Digital).

## Sinal de maior peso — fronteira de escopo (PCI gateway / banco custódia)

**Decisão travada (00:14:40–00:16:43):** como a solução é **CRM sem regulação do Banco Central**, o Salesforce/Dataprev **NÃO executa transações financeiras diretamente** nem movimenta dinheiro. A solução definida: **contratar um gateway de pagamento (PCI gateway) que atue como banco custódia** — responsável pelo **motor de regras** e pela **execução das transações financeiras/split**. O Salesforce **calcula e explica** (BOE/racional), **mas não transaciona**.

- **Fronteira de escopo out-of-scope**: execução de transação financeira + custódia + split bancário = **componente externo (PCI gateway), contratado pelo cliente** — não é entrega Salesforce PS.
- **Quem provê o PCI gateway está em aberto** — Nelson sinalizou que precisa envolver especialista (Camargo, Renata/mundo financeiro); ninguém confirmou o nome ainda. Sinal a **grillar** + candidato a **gap/risco** (dependência de terceiro na entrega).
- Isto é uma **premissa de arquitetura load-bearing** → candidata a **ADR** (fronteira CRM-vs-financeiro). Reforça a separação já registrada e casa com a regra "pré-pagamento obrigatório / repasse 15 dias / split" do Decreto 12.712/2025 (o *cálculo* do split é nosso; a *execução* é do gateway).

## Novos produtos Salesforce sinalizados (afetam épicas + estimativa)

| Produto | Uso | Onde bate | Confiança |
|---|---|---|---|
| **Data Cloud** | Enriquecer histórico das facilitadoras p/ comparação de propostas | E02 | Decidido na sync (Assumed até ratificar) |
| **Experience Cloud** | Portal + dashboard tempo real por trabalhador (FlexCards) | E01/E02/E03 | Confirma direção |
| **OmniStudio (OmniScript + FlexCards)** | Validação de folha client-side; render de comparativo/dashboard | E02/E03 | Confirma direção |
| **MuleSoft** | Orquestração, webhooks facilitadoras, validação de token, rate limit | E05 | Confirma (já em escopo) |
| **Marketing Cloud** | Alertas automáticos (vencimento contrato, folha) | E02/E03 | **Discutido, não travado** — grillar (é escopo ou "plus"?) |
| **Agentforce / IA generativa** | Resumo de termos do contrato em linguagem acessível | E02/E03 | Sinal fraco — "sugere resumo"; grillar |

## Roteiro de revisão (candidatos a mudança confirmada — grillar um a um)
1. **Fronteira PCI gateway / banco custódia** — premissa de arquitetura → **ADR** (Salesforce = CRM, não financeiro; execução financeira é externa). Gera **out-of-scope explícito** + **gap/risco de dependência de terceiro**.
2. **Data Cloud em escopo (E02)** — novo produto → afeta épica E02, sizing, estimativa dual-track.
3. **Passo novo de pagamento/custódia (E03)** — solicitação de boleto + casamento + repasse/split + comunicação bancária → expande E03; parte executória sai (item 1).
4. **Simplificação do status consolidado ("crédito concedido")** — reduz complexidade de UI de E03 (uma linha vs. lista); **gatilho de notificação + CTPS**.
5. **Integração de validação de estabelecimento por CNPJ (E05)** — client credentials flow + connected app + rate limit + cache → detalhe técnico que dá corpo a E05.
6. **Notificação via CTPS** — novo touchpoint de integração (Carteira de Trabalho Digital) — grillar se está em escopo Salesforce ou é do MTE.
7. **Marketing Cloud / Agentforce** — grillar: escopo real vs. "plus"/nice-to-have.
8. **Modelo de domínio adquirente × facilitadora** — clareza de domínio; ajustar descrições de E03/E04, não necessariamente novo trabalho.

## Caveats
- **Transcrição automática (Gemini)** — muitos erros de ASR ("Murisoft/Missoft/Unissoft" = MuleSoft; "força/force" = Salesforce; "EOCO/EPEX/IS" = ruído). Validar termos sensíveis contra a memória da reunião.
- Reunião **interna** — as decisões são **do time Salesforce/Dataprev**, ainda a **validar com o cliente** (sexta 9h). Tratar produtos "decididos" como **forte recomendação (Assumed)**, não confirmação do cliente.
- **Provedor do PCI gateway não definido** — dependência aberta e material para a entrega e para o prazo fixo de 15/nov.
- A arquitetura macro está sendo mantida por Juliane em **Git + Heroku**; Nelson revisa. Este brief é a leitura da transcrição, não a arquitetura oficial — cruzar quando a versão do Git for compartilhada.
