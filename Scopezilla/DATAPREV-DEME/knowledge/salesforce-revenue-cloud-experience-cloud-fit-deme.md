<!-- Source: pesquisa web em docs oficiais Salesforce (developer.salesforce.com, salesforce.com) · Retrieved: 2026-09-09 · Via: Claude (WebFetch, sessão sem MCP docsearch — plugin:search:search com ENDPOINT_NOT_FOUND) -->

# Revenue Cloud + Experience Cloud — Aderência para Loja Dataprev (DEME)

Contexto: DEME quer celebração contratual de produto de prateleira (catálogo, 3 modelos de preço, carrinho, minuta, assinatura, PNCP, handoff ERP) o mais nativo possível no Salesforce, saindo do ServiceNow. Ver `discovery-notes/00-loja-dtp-celebracao-contratual-bsa.md` para o contexto completo. Esta nota valida (ou marca como não confirmado) as afirmações técnicas da hipótese de arquitetura do Luis Gabriel Fernandes antes de uso em proposta.

## 1. Catálogo, Preço, CPQ — CONFIRMADO em doc oficial
Fonte: https://www.salesforce.com/sales/revenue-lifecycle-management/ · 2026-09-09

- **Catálogo único, multi-canal**: "Reduce SKU proliferation and expose products across all channels with a single, attribute-based catalog."
- **Pricing configurável**: motor de preço invocável em qualquer ponto do processo de venda, com "full control and visibility into the calculation process." A doc não nomeia explicitamente "faixa de volume" ou "bilhetagem/usage-based" como features — só descreve lógica de precificação configurável. **Os 3 modelos de comercialização do DEME (bilhetado, faixa mensal, faixa+opcional único) são plausíveis via Pricing configurável + bundling, mas não há confirmação textual explícita de "usage-based" ou "tiered pricing" nesta página.** Tratar como 🟡 até confirmar em doc mais profunda (RLM Dev Guide, help.salesforce.com) ou em diligência de SKU.
- **Bundling**: "Protect revenue with intelligent product bundling and rules that ensure correct pricing."
- **CPQ/Quoting**: geração de quote (inclusive com Agentforce) + Product Configurator com "Constraint Builder" para regras de produtos complexos.

## 2. CLM (aditivo, renovação, distrato) — CONFIRMADO em doc oficial
Fonte: https://www.salesforce.com/sales/revenue-lifecycle-management/ · 2026-09-09

- **Nativo, a nível de asset**: "Provide sellers the flexibility to amend, renew, or cancel customer contracts anytime."
- **CLM completo**: "Manage every contracting touchpoint — from initial sale to ongoing changes — straight from CRM." Inclui biblioteca de cláusulas, redlining assistido por IA, workflows de aprovação, integração de e-signature.
- **Implicação para a Decisão 1 do DEME (quem é o SoR depois da assinatura)**: a doc confirma que CLM nativo é real (não é oversell técnico) — a pergunta em aberto é comercial/de rito (quem opera o termo pós-handoff: Salesforce ou ERP), não uma limitação de plataforma. Reforça a leitura do Luis Gabriel: se a Decisão 1 for "Salesforce continua dono", CLM Advanced é uma escolha de SKU deliberada, não um gap.

## 3. Experience Cloud + portal de catálogo/carrinho (self-service B2B) — NÃO CONFIRMADO nesta sessão
Fonte: tentativa de busca em salesforce.com/service/experience-cloud/overview/ (404) e developer.salesforce.com/docs/atlas.en-us.rev_lifecycle_mgmt.meta (página-índice, sem conteúdo substantivo) · 2026-09-09

- Não encontrei, nesta sessão, doc oficial que confirme explicitamente que **componentes nativos de Revenue Cloud/CPQ (catálogo + carrinho + configurador) podem ser embutidos diretamente em um site Experience Cloud** sem depender de Digital Commerce / B2B Commerce / templates LWR de storefront.
- Este é exatamente o ponto que o handoff da sessão anterior já havia marcado como pendente de confirmação antes de proposta — **continua pendente**. O MCP de busca (`plugin:search:search`, docsearch) segue com falha de conexão (`ENDPOINT_NOT_FOUND` em `127.0.0.1:29051`), o que impediu a via mais direta (KB central Scopezilla + Salesforce Docs MCP).
- 🔴 **Não usar como fato em proposta** até confirmar via um dos caminhos abaixo. Isso não invalida a hipótese do Luis Gabriel (ele mapeou como quem construiu o ServiceNow desta loja, o que é um forte sinal prático), mas a afirmação "~90% nativo" no material BSA já é tratada como leitura interna, não garantia comercial — esta lacuna é o motivo.

### Como fechar essa lacuna
1. Reiniciar o Claude Code (restart completo, não `/reload-plugins`) para religar `search@aisuite`/docsearch e reconsultar a KB central Scopezilla (`kb-search.py`, atoms `[KA-XXXX]`) e o Salesforce Docs MCP.
2. Alternativa manual: baixar PDFs de Implementation/Developer Guide em https://help.salesforce.com/s/products (Revenue Cloud + Experience Cloud) e colocar em `knowledge/` deste projeto para indexação local.
3. Perguntar a um SE/Architect com experiência recente em Revenue Cloud Advanced + Experience Cloud (o próprio Luis Gabriel Fernandes é candidato natural, já que ele é o autor da hipótese).

### Corroboração interna (não é confirmação oficial — item 3 continua 🔴)
Fonte: `discovery-notes/01-alinhamento-interno-commerce-dtp-2026-09-09.md` (ata de reunião interna Salesforce, 2026-09-09).

Nessa reunião interna, o time (Juliane Lopes — ex-Commerce, Guilherme Mattei, Rogerio Meira, Luis Gabriel Fernandes, Nelson Stebulaitis Filho) **decidiu deliberadamente** ir de Revenue Cloud + Experience Cloud (templates LWC nativos de portal B2B/B2B2C: catálogo, mini carrinho, checkout, histórico de pedidos), descartando Commerce Cloud como base — não porque confirmaram documentalmente que componentes de Revenue Cloud/CPQ podem ser embutidos nativamente num site Experience Cloud sem Digital Commerce/LWR, mas porque (a) o núcleo de complexidade do DEME é celebração contratual, não checkout transacional, e (b) customização de frontend (LWC) não quebra em upgrades, enquanto customizar o fluxo contratual inteiro dentro do app de Commerce seria um risco real de quebra em major updates. Guilherme Mattei nota explicitamente que o Commerce já vem com sincronização de catálogo com CPQ pronta, e que fazer isso em Experience Cloud puro **exige construir essa sincronização do zero** — ou seja, o time reconhece que não é "nativo out-of-the-box" nesse ponto específico, é trabalho de construção sobre templates LWC.

**Efeito nesta nota**: isso é opinião de arquitetos internos experientes (inclusive alguém que veio da própria equipe de Commerce), e mudou a decisão de produto do projeto — mas não é uma confirmação em doc oficial Salesforce de que Revenue Cloud/CPQ embute nativamente em Experience Cloud sem Digital Commerce. Trato como sinal forte de viabilidade prática (upgrade de 🔴 para "🔴 com corroboração interna forte"), **não** como 🟢. Não usar a frase "~90% nativo" em proposta com base só nisso — a decisão do time foi ir por Experience Cloud + construção customizada de LWC sobre templates existentes, o que é uma aposta de esforço/risco calculada, não uma garantia de nativo pronto.

## 4. Modelo de dados Quote — fit para o modelo sell-side do DEME

Fonte: RLM Dev Guide (`developer.salesforce.com/docs/atlas.en-us.rev_lifecycle_mgmt.meta`) · 2026-09-09

- O objeto Quote é nativamente **vendedor→comprador**: origina do catálogo do vendedor para um Account/cliente.
- A Loja Dataprev é exatamente esse modelo sell-side padrão (Dataprev vende produto de prateleira a órgãos/empresas) — o fit nativo do Quote é direto para a fábrica de prateleira do DEME (catálogo → preço → quote → assinatura). Isso reforça a leitura do Luis Gabriel de que essa fábrica é candidata forte a "nativo".
- Billing nativo (invoice, payment processing, credit memos, tax) não tem split de pagamento entre múltiplas partes — não parece relevante para o DEME, já que não há repasse a terceiros na celebração contratual descrita no material (a confirmar em discovery se aparecer algum caso de intermediação financeira).

## URLs oficiais citáveis (validadas nesta sessão)

- Revenue Cloud (produto, página consultada e citada acima): https://www.salesforce.com/sales/revenue-lifecycle-management/
- RLM Dev Guide (página-índice, sem conteúdo substantivo capturado): https://developer.salesforce.com/docs/atlas.en-us.rev_lifecycle_mgmt.meta
- Help Salesforce (home de docs por produto, para PDFs de Implementation/Developer Guide): https://help.salesforce.com/s/products
- Architect decision guides: https://architect.salesforce.com/decision-guides
- ⚠️ https://www.salesforce.com/service/experience-cloud/overview/ retornou 404 nesta sessão — não usar; buscar URL correta via help.salesforce.com/s/products ou Docs MCP quando disponível.

## Síntese para o BSA

Duas das três camadas centrais da hipótese do Luis Gabriel (Catálogo+Pricing+CPQ e CLM) têm confirmação textual direta em doc oficial pública, hoje. A terceira — Experience Cloud como camada de vitrine/carrinho self-service embutindo componentes nativos de Revenue Cloud, sem precisar de Digital Commerce/LWR storefront — **não foi confirmada nesta sessão** por falha do MCP de busca interno; é a lacuna a fechar antes de qualquer garantia comercial do "~90% nativo" na proposta.
