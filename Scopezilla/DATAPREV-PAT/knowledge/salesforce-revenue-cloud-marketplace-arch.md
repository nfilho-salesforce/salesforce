<!-- Source: pesquisa web em docs oficiais Salesforce (salesforce.com, developer.salesforce.com, mulesoft.com) · Retrieved: 2026-07-28 · Via: Claude (researcher agent) -->

# Salesforce para Marketplace / Leilão Reverso B2G — Pesquisa de Arquitetura

Contexto: plataforma pública (Dataprev/MTE) de cotação competitiva multi-fornecedor (vale-alimentação). Beneficiária publica COTAÇÃO → N facilitadoras enviam PROPOSTAS → beneficiária COMPARA/SELECIONA → CONTRATO → FOLHA com conta custódia e SPLIT.

## 1. Componentes nativos do Revenue Cloud (Revenue Lifecycle Management)
Fonte: https://developer.salesforce.com/docs/atlas.en-us.rev_lifecycle_mgmt.meta (RLM Dev Guide) · https://www.salesforce.com/sales/revenue-lifecycle-management/ · 2026-07-28

- **Product Catalog Management** — portfólio de produtos, atributos, classificações, produtos simples/bundle, regras.
- **Pricing** — precificação baseada em atributos; integra com PIM/PLM/ERP.
- **Product Configurator** — Constraint Builder (configuração guiada por regras).
- **Transaction Management (Quoting/CPQ + Order + Contract)** — "subscription lifecycles from quotes and orders to contracts, assets, amendments, and renewals". Quote → Order → Contract → Asset.
- **Contract Lifecycle Management (CLM)** — criação/edição de contrato, redlining com IA, biblioteca de cláusulas, e-signature, gestão de obrigações/aprovações.
- **Order Management** — Order Automation, Dynamic Revenue Orchestrator para fulfillment.
- **Billing (Revenue Cloud Billing)** — "integrated and extensible subscription and usage-based billing solution", automatiza payment processing, invoice generation, credit memos, tax config. Doc home help.salesforce.com.
- **Revenue Analytics** — pricing/subscription/order/billing analytics.

## 2. Fit para leilão reverso / RFQ / sourcing — LACUNA CONFIRMADA
Fonte: RLM Dev Guide + página de produto RLM · 2026-07-28
- O modelo RLM é **sell-side / product-to-cash** (catálogo → preço → quote → order → billing). Referencia "customer assets" / "assets that belong to an account".
- **Nenhuma menção** a procurement, sourcing, RFQ, reverse auction ou multi-supplier bidding em nenhuma doc oficial consultada.
- Não existe produto "Salesforce Procurement" / sourcing buy-side no portfólio (Sales/Service/Revenue são todos sell-side).
- Conclusão: o padrão de leilão/matching/comparação de propostas de múltiplos fornecedores é **CUSTOM** na plataforma (objetos custom + Flow/Apex).

## 3. Quote seller→buyer vs buyer→seller
Fonte: RLM Dev Guide · 2026-07-28
- Objeto Quote é explicitamente **vendedor→comprador** (origina do catálogo do vendedor, para um Account/cliente).
- No marketplace o COMPRADOR publica demanda e N vendedores respondem → inverte o modelo. Quote nativo não modela isso; precisa de objetos custom (ex.: Cotacao__c, Proposta__c) com relação 1-cotação-para-N-propostas.

## 4. Billing + Split de pagamento
Fonte: RLM Dev Guide (Billing) · 2026-07-28
- Billing suporta invoice, payment processing, credit memos, tax, payment schedules e charge types.
- **NÃO** há menção nativa a split de pagamento entre múltiplas partes / escrow de marketplace / repasse a terceiros. Split → integração externa com banco/adquirente (via MuleSoft).

## 5. Experience Cloud + MuleSoft (portal + integração)
Fonte: https://www.mulesoft.com/platform/enterprise-integration · 2026-07-28
- **MuleSoft Anypoint Platform** — "#1 integration and API platform"; API-led connectivity; "connect to any system with pre-built connectors or build your own"; 1.500+ connectors; API Manager (secure/manage/insights); Anypoint Exchange. Padrão para integrar ~600-700 sistemas de facilitadoras via API.
- **Experience Cloud** — portal externo autenticado (parceiros/clientes/self-service), suporte a identidade externa/SSO (ex.: gov.br via OpenID Connect). Doc home: help.salesforce.com (páginas renderizam via JS, não capturáveis por fetch; produto amplamente documentado).

## 6. Recomendação de arquitetura
- **Core Platform (custom objects) + Experience Cloud + MuleSoft** para o núcleo de leilão/cotação/proposta/comparação/seleção — porque o leilão é custom de qualquer forma.
- Adicionar **Revenue Cloud apenas para CLM + Billing** do módulo financeiro (contrato pós-seleção, folha, faturamento) — evita forçar o modelo sell-side do Quote no padrão buyer-initiated.
- Split de pagamento/conta custódia = integração bancária/adquirente via MuleSoft, não nativo.

## URLs oficiais citáveis
- Revenue Cloud (produto): https://www.salesforce.com/sales/revenue-lifecycle-management/
- RLM Dev Guide: https://developer.salesforce.com/docs/atlas.en-us.rev_lifecycle_mgmt.meta
- MuleSoft Anypoint: https://www.mulesoft.com/platform/enterprise-integration
- Help Salesforce (home de docs Billing/Experience Cloud): https://help.salesforce.com/s/products
- Architect decision guides: https://architect.salesforce.com/decision-guides
