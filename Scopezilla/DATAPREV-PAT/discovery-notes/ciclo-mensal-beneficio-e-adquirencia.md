<!-- Source: DuckDuckGo + ticket.com.br + confiancadigital.com.br + g1.globo.com · Retrieved: 2026-07-29 · Via: Claude (WebFetch) -->

# Ciclo mensal do benefício + relação com bandeiras/maquininhas (nota de pesquisa)

Nota de grounding para o domínio do projeto DATAPREV-PAT. Responde: **depois que uma empresa (beneficiária) contrata uma facilitadora, como é o ciclo mensal de solicitação de créditos, envio da folha, cobrança e repasse — e qual a relação com as empresas de bandeiras/maquininhas?**

Relevante para **E03 (Folha & Financeiro)**, **E02 (Marketplace de Cotação)**, **E04 (Credenciamento)** e **E05 (Integração MuleSoft)**.

## Fontes

- **Ciclo mensal / recarga:** blog Ticket — `https://www.ticket.com.br/blog/beneficios-ticket/como-oferecer-vale-alimentacao-para-funcionarios/` (define valor mensal, cadastra colaboradores, recarga na plataforma, crédito automático no cartão).
- **Arranjo aberto / bandeira / adquirente / rebate:** guia de portabilidade — `https://confiancadigital.com.br/novas-regras-do-vale-refeicao-e-alimentao-o-guia-completo-sobre-portabilidade-e-seus-direitos/` (circuito fechado → arranjo aberto; rebate 6–8% proibido; pré-pagamento obrigatório; MCC).
- **Reforma / prazos / limites de taxa:** G1 — `https://g1.globo.com/trabalho-e-carreira/noticia/2026/02/25/vale-refeicao-e-alimentacao-regras.ghtml`.
- Complementa e depende de: `discovery-notes/reforma-pat-decreto-12712-2025.md` (Decreto 12.712/2025, teto de MDR 3,6%, repasse 15 dias, sub judice ADI 7962/STF).

## O ciclo mensal (empresa beneficiária → facilitadora), passo a passo

1. **Setup (uma vez):** a empresa define o valor mensal por colaborador e cadastra os funcionários (CPF); a facilitadora emite e distribui os cartões.
2. **Pedido de recarga (mensal):** o RH envia o arquivo de recarga na plataforma da facilitadora — por CPF, o valor do mês (ajustado por admissões, desligamentos, dias trabalhados, férias). É, na prática, uma folha.
3. **Cobrança / pré-pagamento:** a facilitadora consolida o total e cobra a empresa. Modelo agora é **pré-pagamento obrigatório** (a reforma vedou o pós-pagamento). Cobrança por boleto/Pix pelo valor da folha **+ taxa de administração** da empresa contratante.
4. **Crédito nos cartões:** confirmado o pagamento, o saldo entra **automaticamente** no cartão de cada colaborador na data de recarga.
5. **Uso pelo trabalhador:** gasto no estabelecimento credenciado (vale-refeição = refeições prontas; vale-alimentação = gêneros), controlado por **MCC** (Merchant Category Code).
6. **Repasse ao estabelecimento:** a facilitadora (via adquirente) liquida a venda ao estabelecimento, **descontado o MDR** — teto de 3,6% e prazo de até 15 dias nas vendas PAT.

## Os dois fluxos financeiros (não confundir)

| Fluxo | Sentido | Gatilho | Taxa |
|---|---|---|---|
| **1 · Recarga (pré-pago)** | Empresa beneficiária → facilitadora | Pedido mensal de recarga (folha por CPF) | **Taxa de administração** paga pela empresa (sem rebate/deságio após a reforma) |
| **2 · Liquidação da venda** | Facilitadora/adquirente → estabelecimento | Compra do trabalhador na maquininha | **MDR** pago pelo estabelecimento — teto 3,6%, repasse ≤15 dias |

No modelo antigo o **rebate** cruzava os dois fluxos: a facilitadora dava desconto à empresa (fluxo 1) e recuperava com MDR alto (6–8%) no estabelecimento (fluxo 2). A reforma **proibiu** esse cruzamento (vedado qualquer deságio sobre o valor contratado).

## Relação com bandeiras e maquininhas (adquirência)

- **Modelo antigo — rede fechada:** cada operadora rodava seu próprio arranjo; o cartão da operadora Y só passava na maquininha credenciada por Y. Se o restaurante tinha a bandeira X e o trabalhador o cartão Y, a transação não ocorria. Por isso o credenciamento era **facilitadora a facilitadora**.
- **Reforma — arranjo aberto:** interoperabilidade — qualquer maquininha habilitada no PAT aceita qualquer bandeira, referenciada ao arranjo de pagamento (Banco Central como referência). Portabilidade gratuita entre operadoras. Fim do "não aceitamos a bandeira X".
- **Papéis:** **facilitadora/operadora** emite o benefício e faz a recarga; **adquirente** (maquininha) captura e processa a transação; **bandeira/arranjo** conecta os dois lados. O estabelecimento paga o MDR à adquirência; o teto de 3,6% incide sobre essa relação.
- **Cronograma da interoperabilidade:** mai/2026 (sistemas com +500 mil trabalhadores) → nov/2026 (total).

## Ligação com o projeto

- **E03 (Folha & Financeiro)** — coração do ciclo no marketplace: upload de folha, boleto/Pix, conta custódia em banco público, split governo/facilitadora, repasse 15 dias. O **fluxo 1** é o que E03 orquestra. Desenho de conta custódia / adquirente-PSP / split ainda é **assunção** (Open Question do discovery).
- **E02 (Marketplace)** — taxa de administração e condições de repasse são variáveis da cotação; o ciclo mensal é o que a beneficiária "compra" no leilão reverso.
- **E04 (Credenciamento)** — MDR/repasse (fluxo 2) é o value driver que torna o cadastro unificado racional para o estabelecimento; interoperabilidade dispensa o credenciamento por operadora.
- **E05 (Integração)** — os dois fluxos batem em sistemas externos (banco público; APIs de adquirência/facilitadoras). Reforça o mock-first.

## Caveats

- **Pré-pagamento obrigatório** e **teto de MDR** vêm do Decreto 12.712/2025 — **sub judice** (ADI 7962/STF). Mesma premissa regulatória da nota da reforma.
- Se o marketplace opera **só o fluxo 1 (recarga)** ou **também o fluxo 2 (liquidação ao estabelecimento)** é uma pergunta aberta de escopo — muda E03 e E05.
