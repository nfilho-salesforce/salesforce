# Loja Dataprev · Celebração Contratual · BSA

**gov.br** — Empresa de Tecnologia e Informações da Previdência · Dataprev
Material interno · PS Brasil · duas visões

Fonte: https://ps-latam-bsa-9eba136812c1.holly-virginia.herokuapp.com/LATAM-Agentforce-BSA/dataprev-assets/dataprev-marketplace-deme-bsa.html
Convertido para Markdown em 2026-09-09.

## DATAPREV SALESFORCE BSA

### Loja Dataprev, celebração contratual

DEME · quote-to-sign · não é o PAT Marketplace

Owner: Juliane Lopes · Agentforce Business Strategy

---

## Navegação

**Entrada**
- 🗂️ Capa e as duas visões

**Visão Estratégia**
- 🎯 Tese e recorte
- 🏭 Duas fábricas
- 🔓 Decisões em aberto (5)
- ⚠️ O que ainda não fecha
- 👥 Conta, ondas, próximo passo

**Visão Técnica**
- 🏗️ Arquitetura de módulos
- 📋 Necessidades × Salesforce
- 🔄 Fluxo do dossiê
- 📦 Inventário e gaps
- ⚙️ Integrações, RNF, riscos

**Apoio**
- 📚 Fontes

---

## Capa e as duas visões

*Atualizado 02/09/2026 · reunião Loja DTP 31/08*

Dataprev · DEME · Loja DTP

### Celebração contratual. Duas visões, uma tese ainda em aberto.

Este material separa o que é estratégia de conta (o que vender, para quem, em que onda, o que ainda não se pode afirmar) do que é aderência técnica Salesforce (módulos, NEs, gaps). A reunião de 31/08 já pediu nativo na plataforma, para sair do ServiceNow. O Documento de Visão v1.1 descreve o rito. A arquitetura de módulos é do Luis Gabriel Fernandes, SE, quem implementou esse ServiceNow. As fontes não coincidem em tudo. Onde há conflito, está marcado como decisão, não como fato.

**Key facts:**
- Reunião Loja DTP · 31/08/2026
- DV Marketplace v1.1 · mai/2026
- Incumbente: ServiceNow
- Arquitetura: Luis Gabriel Fernandes, SE
- Área: DEME, não previdência/agentes
- Não confundir com PAT Marketplace

**Stats:**
- **2** — Modelos de contratação na reunião (prateleira e exclusivo)
- **9** — Produtos no portfólio hoje, com expansão planejada (reunião 31/08)
- **B2B** — Clientes só órgão público ou privado. Nunca B2C, na fala da reunião
- **ERP** — Pós-vigência fora. Handoff do contrato assinado é o encontro

#### E Visão Estratégia
Para AE, liderança de conta e BSA. Tese, recorte da reunião, as duas fábricas, decisões que travam o deal, o que o DV e a reunião contradizem, ondas e mapa de gente.

Comece aqui se a pergunta for: o que estamos vendendo, e o que ainda não podemos prometer.

#### T Visão Técnica
Para SE, arquitetura e diligência. Hipótese do Luis Gabriel Fernandes (quem implementou o ServiceNow): camadas Salesforce, mapeamento NE × módulo, fluxo do dossiê, inventário nativo versus integração, RNF e riscos.

Comece aqui se a pergunta for: o que cabe nativo, o que pede parceiro, o que depende de API da Dataprev.

📌 **Como ler.** A visão Estratégia não fecha stack. A visão Técnica não fecha envelope comercial. As cinco decisões da seção correspondente precisam ser resolvidas antes de proposta de preço, SKU ou SOW. Volumetria pedida por Rogerio Meira na reunião (produtos, transações, clientes, contratos, usuários) ainda não chegou.

---

## Visão Estratégia · 1 de 5

### A tese: loja de celebração, nativa, no Salesforce

Na reunião Loja DTP de 31/08/2026 a Dataprev não pediu um CRM. Pediu uma solução de celebração contratual, o mais nativa possível na plataforma Salesforce, para substituir o ServiceNow atual. Quem implementou esse ServiceNow foi o Luis Gabriel Fernandes, hoje SE na Salesforce, no time do Rogerio Meira. A cada cerca de seis meses as customizações quebram nas atualizações de plataforma.

#### O que a reunião fechou 31/08

Fonte: notas da reunião Loja DTP, 31/08/2026, 14h. Presentes pelo cliente: Hildegard Barbosa (DEME). Pela Salesforce, entre outros: Juliane Lopes, Rogerio Meira, Juliana Brites, Nelson Filho, Rene Soares e Luis Gabriel Fernandes (SE, autor da arquitetura de módulos deste caso).

**Recorte de produto**
Foco exclusivo em celebração contratual. Gestão pós-contrato já coberta por outras ferramentas e encontra este caso via ERP. Atos que geram novo termo (cancelamento, reajuste, mudança de razão social) a Dataprev quer automatizados na loja, com exceção manual quando a regra não cobrir.

**Dor nº 1, nas palavras deles**
A solução atual é ServiceNow, com alto grau de customização. A cada cerca de seis meses, atualização de plataforma quebra funcionalidade. Retrabalho recorrente e risco operacional. Requisito central: configuração vale; custom só quando não houver jeito nativo. O Luis Gabriel implementou esse ServiceNow. Hoje ele está neste lado da mesa e escreveu o mapeamento de módulos Salesforce.

**Quem compra e quem usa**
Clientes exclusivamente B2B: órgãos públicos e privados. Nunca B2C, na fala da reunião. Autenticação Gov.BR e bases de pessoa jurídica. Administração direta exige dotação orçamentária. Dataprev é custodiante do dado, não controladora: alguns produtos pedem autorização do órgão dono.

**Validade jurídica**
Contrato público só tem validade jurídica depois da publicação no PNCP. O sistema deve controlar e registrar a confirmação de publicação pelo cliente. Isso não é anexo administrativo. É condição de existência do contrato.

> "Requisito central: solução o mais nativa possível na plataforma Salesforce. Configurações são aceitáveis; customizações apenas quando estritamente necessárias." — Notas da reunião Loja DTP, 31/08/2026.

#### O que isso implica para o posicionamento BSA

A reunião já era "Loja DTP, Salesforce". A pergunta não é se eles consideram a plataforma. A pergunta é se esta loja entra no Org do programa de previdência e agentes, ou se é envelope e Org novos, com o DEME como sponsor.

- **Não vender como CRM.** NE9 (feed de pipeline) é desejável no DV. O eixo é catálogo, simulação, minuta, assinatura, autorizador, PNCP e handoff.
- **Displacement, não reforma de Org Salesforce.** Sai ServiceNow. Entra Salesforce. O Luis Gabriel é o asset: conhece o rito, o que foi customizado, o que quebra, e o que precisa nascer nativo para não repetir a história.
- **O argumento de venda que eles verbalizaram** é upgrade-safe, não "temos Agentforce". Custom que quebra a cada semestre é a ferida. Qualquer desenho que empurre LWC e OmniStudio no dia 1 trabalha contra a fala deles e contra a leitura do Luis.
- **Outra área, outro orçamento.** DEME não é a área de previdência/agentes. Relacionamento e envelope são independentes, mesmo que a marca Salesforce seja a mesma na conta.
- **Este material não é o PAT Marketplace.** PAT é outro deal, outro sponsor, outro ministério. O nome "marketplace" colide. Internamente: Loja DTP / celebração DEME.

#### Síntese desta parte

Eles querem nativo no Salesforce para celebrar contrato de produto de prateleira (e, na mesma reunião, também contrato exclusivo). Pós-vigência (NF, RAS, consumo) não é este caso. O que ainda não está fechado: de quem é o contrato depois da assinatura, se a loja faz as duas fábricas, e qual volumetria real. Isso vai na próxima seção e nas decisões.

---

## Visão Estratégia · 2 de 5

### Duas fábricas de contrato, três jeitos de precificar

A reunião descreveu dois modelos de contratação na Dataprev. O Documento de Visão e a arquitetura do Luis Gabriel (quem implementou o ServiceNow) desenharam a prateleira com carrinho. Contrato exclusivo por cliente não tem catálogo nem simulação de volume. São teses de produto diferentes, no mesmo pedido de "loja". O desenho do Luis vale para a fábrica 1. A fábrica 2 ainda não está nesse HTML.

#### Os dois modelos da reunião 31/08

**1. Produto de prateleira**
Vendido a múltiplos clientes, com configuração e parametrização. É o que o DV chama de Marketplace: vitrine, modelo de negócio, carrinho, simulação. COMPREV é o carro-chefe citado no DV (obrigatório para INSS e RPPS, Decreto 10.188/2019). A reunião falou em 9 produtos no portfólio, com expansão planejada.

Fit técnico natural: Revenue Cloud (catálogo, preço, CPQ, Doc Gen) + Experience Cloud.

**2. Contrato exclusivo por cliente**
Sistemas não reutilizáveis, um cliente, um desenho. Não tem "selecionar 5 mil consultas/mês". Tem minuta, cláusulas, autorizador se o dado tiver dono, assinatura, PNCP se for ente público, handoff ao ERP. Carrinho e catálogo aqui são teatro.

Fit técnico: CLM + Document Generation + Approval + portal. CPQ de prateleira não é o eixo.

🚧 **Buraco de tese.** Se a loja precisa dos dois, Revenue Cloud CPQ não é o eixo do caso inteiro. É o eixo da fábrica 1. A fábrica 2 é documento e rito. Misturar os dois num único "~90% nativo com CPQ" infla SKU e desvia o discovery.

#### Três modelos de comercialização na prateleira reunião

Hildegard descreveu a complexidade de preço. Qualquer catálogo Salesforce precisa nascer cabendo estes três, não um price book genérico.

**1. Consumo bilhetado**
Cobrança em tempo de execução. Cliente não escolhe volume antecipado. O "carrinho" aqui é adesão a um modelo, não seleção de faixa.

**2. Volume mensal**
Seleção de faixa (exemplo citado: 5 mil ou 10 mil consultas/mês). É o caso clássico de CPQ com atributos e preço por faixa.

**3. Volume + opcional único**
Volume mensal mais componentes de execução única: instalação, configuração, consultoria. Bundle com obrigatório e opcional, vigências diferentes.

#### O que entra e o que sai, sem maquiar a conta

Não usar "14 NEs + 2 fora". São 16 necessidades no DV. Fora está a NE14 inteira e o FN10.02 (um FN dentro da NE10). NE10 continua no rito pelo handoff (FN10.01). NE15 (PF) está em conflito com a reunião (só B2B).

**Em celebração (rito da loja)**
- Catálogo, vitrine, carrinho, simulação (NE1, NE3), para a fábrica prateleira
- Gov.BR, cadastro PJ e papéis (NE2, NE4, NE5)
- Minuta, autorizador do órgão dono do dado, assinatura, PNCP (NE6, NE7, NE8)
- Handoff do contrato assinado ao ERP (FN10.01)
- Provisionamento de acesso (NE11)
- Atos com novo termo: distrato, reajuste, razão social (NE12, NE13), pedidos como automação na reunião
- Chatbot (NE16) no DV como crítico; na estratégia, candidato a onda posterior

**Fora, ou em conflito**
- FN10.02: portal de NF, RAS, fiscais, consumo. Já riscado no DV. Confirmado fora em 31/08.
- NE14: reenquadramento anual COMPREV. Pós-vigência, outra ferramenta + ERP.
- NE15 PF: crítica no DV e "futura" no mesmo card. Reunião: nunca B2C. Tratar como estacionada até o DEME desdizer a fala de 31/08.
- NE9 feed CRM: desejável no DV. Se Salesforce for a loja, não é integração: a oportunidade já nasce aqui.

#### Síntese desta parte

Pergunte ao DEME, cedo: a loja celebra só prateleira, ou também o contrato exclusivo? Sem isso, o desenho de Revenue Cloud Advanced é um chute de SKU. Os três modelos de preço da prateleira, esses sim, precisam estar no discovery de catálogo.

---

## Visão Estratégia · 3 de 5

### Cinco decisões que travam proposta, SKU e SOW

Enquanto estas cinco não tiverem dono e prazo, o material técnico é briefing interno. Não é oferta. Hildegard ficou de mandar o DV com cerca de 8 telas de regras e a volumetria que Rogerio pediu. Até isso entrar, número de tamanho de deal é invenção.

#### 1. Sistema de registro depois da assinatura — *Em aberto*

**Por que trava**: O DV chama o ERP de fonte oficial do contrato após o handoff. A arquitetura de módulos põe CLM no Salesforce para aditivo, reajuste e distrato. Os dois juntos criam dois donos do mesmo termo.

**Se A**: Salesforce continua dono de preço e termo. ERP só fatura. Aí Revenue Cloud é o eixo da fábrica prateleira. Precisa estar escrito no handoff.

**Se B · recomendação a testar**: ERP assume o contrato no dia 1. Salesforce só cerimonia PDF + assinatura + autorizador. Aí CLM Advanced pode ser oversell. Doc Gen + Approval bastam para o ato.

#### 2. A loja faz prateleira, exclusivo, ou os dois? — *Em aberto*

**Por que trava**: A reunião citou os dois modelos. O DV e a arquitetura do Luis só desenharam prateleira com carrinho. O HTML dele é a leitura Salesforce da fábrica 1, feita por quem implementou o ServiceNow. A fábrica 2 (exclusivo) ainda não está nesse desenho.

**Se só prateleira**: Eixo: Experience + Revenue Cloud. Contrato exclusivo fica em outro rito, outro sistema, ou fase 2.

**Se os dois**: Duas jornadas no mesmo portal, dois desenhos de objeto. Não forçar CPQ no exclusivo. Discovery separado por fábrica.

#### 3. PF e chatbot entram em que onda? — *Conflito DV × reunião*

**Reunião 31/08**: Clientes exclusivamente B2B. Nunca B2C. Chatbot não foi a dor nº 1. A dor foi custom que quebra.

**DV v1.1**: NE15 PF marcada crítica e, no mesmo texto, funcionalidade futura. NE16 chatbot crítica, resposta em 30s, sem alucinação.

**Leitura BSA**: Estacionar PF até o DEME desdizer o "nunca B2C". Agentforce como onda, não como go-live da loja, salvo o DEME insistir que atendimento na vitrine bloqueia lançamento.

#### 4. Assinatura: registrar o ato, ou validade ICP-Brasil / A3? — *Em aberto*

**Por que trava**: Muda arquitetura no dia zero. Sem ICP, Approval Process + captura + Doc Gen + Gov.BR. Com token A3, entra parceiro (Gov.BR, DocuSign, Adobe, Clicksign), custo e homologação.

**O que o DV diz**: A3 é desejável. Crítico só se Gov.BR indisponível. PNCP é que dá validade ao contrato público, não o token, na lógica da reunião.

**Leitura BSA**: O Luis lembra que ICP não era necessário no rito atual. Ainda assim: confirmar com jurídica Dataprev, não só de memória. Não vender parceiro de assinatura até essa frase existir por escrito.

#### 5. Volumetria, users Experience e Org — *Aguardando Hildegard*

**Pedido na reunião**: Rogerio pediu quantidade de produtos, transações, clientes, contratos e usuários. Hildegard ficou de incluir no documento ou enviar à parte. Ainda não está neste material.

**O que o RNF do DV traz**: ≥ 50 contratações/mês e até 10 acessos internos simultâneos. Isso não descreve a loja: a loja é externa (guest, signatário de RPPS, autorizador do órgão dono do dado).

**Org**: Mesmo Org do programa de agentes/previdência, ou Org do DEME? Isso muda licença, sharing, e se NE9/NE16 são nativos ou integração a um CSM que já existe.

⏳ **Dado que falta de propósito.** Sem a volumetria do Hildegard não há hipótese honesta de Experience Cloud (guest versus named), nem de MuleSoft (chamadas), nem de Agentforce (conversas). Qualquer ROM agora seria número inventado.

---

## Visão Estratégia · 4 de 5

### O que neste dossiê ainda não tem lógica

Crítica de strategy sobre o cruzamento DV + arquitetura do Luis. Serve para o time interno não repetir o overlap como se fosse tese fechada. Não é lista para o cliente, até virar pergunta de discovery.

#### Fraturas para não levar como fato BSA

**"Só celebração" e, no mesmo fôlego, reajuste IPCA e distrato**
Renovação, reajuste e cancelamento de contrato vigente são pós-vigência. A reunião pediu esses atos automatizados na loja. Isso só fecha se a loja permanecer dona do termo depois do handoff, ou se o ato for só cerimônia de PDF cuja conta o ERP recalcula. Escolher. Ver decisão 1.

**COMPREV 2.100+ no hero, reenquadramento fora**
Os 2.100+ RPPS (Decreto 10.188/2019, citado no DV) são base instalada. O trabalho anual que mexe nela (NE14) está fora. Este deal vende celebração de contrato novo de prateleira. Usar 2.100 como prova de escala deste envelope é métrica de palco.

**"Enviar ao CRM" se o Salesforce for a loja**
O DV foi escrito como portal custom que alimenta "o CRM em uso". A proposta inverte: Salesforce é a loja. Aí NE9 não é integração, a oportunidade já nasce no objeto. NE16 não é "abrir no CSM da Dataprev", o Service Cloud seria o CSM. O texto técnico ainda oscila entre os dois.

**"~90% nativo" versus "é construção"**
O ~90% é leitura do Luis Gabriel sobre a fábrica prateleira (nativo + add-on Salesforce), com um gap duro: ICP-Brasil, que ele lembra não ser necessário. Vale internamente, porque quem estimou implementou o ServiceNow. Não usar como garantia comercial até diligência de SKU. Carrinho CPQ em portal, cláusulas condicionais e autorizador externo ainda são construção, não só Setup.

**22 estados como se fossem o processo**
A máquina de estados do DV inclui vários terminais de falha. Happy path de celebração é bem menor (vitrine → cadastro → minuta → assinatura → PNCP se público → handoff). Mostrar 22 de cara trabalha contra "nativo e simples".

**Self-service não é "sem o comercial Dataprev"**
Continua havendo autorizador externo, dois signatários Dataprev por tabela de competência, validação de PNCP (às vezes manual) e cancelamento administrativo. Self-service do contratante, sim. Fábrica sem gente Dataprev, não.

**Incumbente: ServiceNow. Displacement, não reforma**
A loja atual é ServiceNow, com custom que quebra nas atualizações. Quem implementou foi o Luis Gabriel, hoje SE neste time. A história comercial é sair do ServiceNow para nativo Salesforce, com quem conhece o rito do nosso lado. O que ainda falta nome é a ferramenta de pós-vigência (vizinha do FN10.01), não a de celebração.

**PNCP tratado como anexo**
Na reunião: contrato público só vale depois da publicação. Flow rescindindo ente público por prazo é risco jurídico alto. Jurídica Dataprev na sala, não só automação de Flow.

#### O que ainda não está no material e precisa entrar no discovery

- Nome e dono da ferramenta de pós-vigência (vizinha obrigatória do FN10.01).
- Persona do secretário de RPPS, do autorizador do órgão dono do dado (ex.: INSS no COMPREV), do signatário Dataprev, do jurídico e do dono do ERP. Hoje só há e-mail do DEME.
- Make/buy: Dataprev tem fábrica. Por que não reconstruir a loja internamente e só pedir CRM/CSM. O antídoto é a fala deles sobre o ServiceNow custom que quebra, com o Luis como quem já viveu esse ciclo.
- Caminho de contratação pública (TED, ata, inexigibilidade, licitação) e se este envelope compete politicamente com o programa de agentes.
- Hyperforce Brasil, LGPD (custodiante versus controladora), guest user em vitrine pública. Para esta conta isso é mesa.
- Se Public Sector Solutions entra na conversa, ou se vamos de Revenue Cloud com regra pesada de governo (Lei 14.133, dotação, PNCP).

---

## Visão Estratégia · 5 de 5

### Conta, gente, ondas, o que fazer na próxima conversa

DEME é sponsor novo. A reunião já deixou dever de casa dos dois lados: Hildegard manda regras e volumetria; a Salesforce devolve aderência nativa. Este material é essa devolutiva, ainda sem preço.

#### Quem estava na sala e quem falta — Conta

Reunião Loja DTP, 31/08/2026. Pelo cliente, Hildegard Barbosa. Pela Salesforce: Juliane Lopes, Rogerio Meira, Juliana Brites, Nelson Filho, Rene Soares, Luis Gabriel Fernandes, entre outros. O DV v1.1 ainda lista Thiago Cunha, Fábio Gasparotto, Rodrigo Lobo e Liliane Frez no DEME. Não estavam nesta ata.

**Hildegard Paulino Barbosa**
DEME, Gerente-Executivo. Sponsor visível. Ficou de enviar o DV (~8 telas de regras) e volumetria. Pediu a transcrição.
hildegard.barbosa@dataprev.gov.br

**Luis Gabriel Fernandes**
SE Salesforce, time do Rogerio Meira. Implementou o ServiceNow da loja atual. Autor da arquitetura de módulos deste caso. Asset de detalhamento: rito, custom que quebra, o que precisa nascer nativo.

**Rogerio Meira**
Salesforce. Pediu volumetria explícita: produtos, transações, clientes, contratos, usuários. Sem isso não há licenciamento Experience.

**Ainda fora do mapa**
Jurídica Dataprev (PNCP, ICP, rescisão automática). Dono do ERP. Dono da ferramenta de pós-vigência. Autorizador típico (INSS no COMPREV). TI de identidade Gov.BR. Sem esses, FN10.01 e NE7 são desenho no vazio.

🔗 Área diferente do programa de agentes/previdência. Ponte política com a conta principal é decisão nossa, não fato do DEME. Não assumir mesmo Org.

#### Ondas sugeridas (internas, até o DEME discordar)

Hipótese de BSA para não colocar chatbot, PF, OCR 80% e ICP no mesmo go-live. Ajuste quando a volumetria e as cinco decisões chegarem.

**Onda 1 · rito mínimo de prateleira**
Vitrine + cadastro PJ + papéis + minuta + assinatura (sem ICP, se a jurídica confirmar) + handoff ERP. Um produto piloto, não os nove. Configuração, não custom. Mede: tempo de celebração versus o processo manual atual (ainda sem baseline: pedir na volumetria).

**Onda 2 · governo de verdade**
Autorizador do órgão dono do dado (NE7), PNCP como condição de validade, dotação orçamentária, tabela de competência dos dois signatários Dataprev. Provisionamento (NE11) se o produto piloto tiver API.

**Onda 3 · atos com novo termo**
Distrato, reajuste, razão social. Só depois da decisão 1 (quem é SoR). Se o ERP for o dono, esta onda é cerimônia. Se o Salesforce for o dono, entra CLM de verdade.

**Onda 4 · atendimento e o que estiver estacionado**
Agentforce + Service Cloud se o DEME confirmar que a vitrine precisa de triagem. PF só se a fala "nunca B2C" cair. Contrato exclusivo como jornada paralela, se a decisão 2 disser que a loja faz as duas fábricas.

#### Próxima conversa com o DEME, roteiro curto

1. Confirmar: a loja é só prateleira, ou também contrato exclusivo?
2. Confirmar: depois de assinado, quem é dono de preço e termo, Salesforce ou ERP?
3. Cobrar a volumetria (produtos, transações, clientes, contratos, usuários) e o DV de ~8 telas.
4. Pedir o nome da ferramenta de pós-vigência (a de celebração já é ServiceNow). Quem opera, quem é dono.
5. Jurídica na sala para PNCP (validade) e para ICP-Brasil / A3.
6. PF: a reunião disse nunca B2C. O DV diz o contrário. Qual vale?

#### Fecho da visão Estratégia

Serve para o time interno e para preparar discovery. Não serve ainda como proposta. A reunião pediu nativo. O DV descreveu um portal quase ponta a ponta. O Luis mapeou a prateleira em Salesforce a partir de quem já construiu o ServiceNow. Este material escolhe o recorte da reunião e deixa o resto como decisão, não como stack vendida. A visão Técnica, a seguir, é a hipótese do Luis, cruzada com as falas de 31/08.

---

## Visão Técnica · 1 de 5

### Arquitetura de módulos, hipótese de prateleira

Hipótese de Luis Gabriel Fernandes, SE: ele implementou o ServiceNow da loja e mapeou a aderência nativa Salesforce (Experience Cloud + Revenue Cloud). Vale se a decisão 2 for "fábrica prateleira" e a decisão 1 permitir que catálogo e termo morem no Salesforce até o handoff. Contrato exclusivo não usa a camada de carrinho. PF não entra neste desenho de go-live.

#### Camadas hipótese

Eixo: Experience Cloud (portal de celebração) + Revenue Cloud (catálogo, preço, CPQ, Doc Gen, CLM se SoR for Salesforce) + Identity Gov.BR + MuleSoft nas APIs da Dataprev. Agentforce não é eixo de go-live nesta hipótese.

**Portal**
- Experience Cloud · vitrine — Logados e não logados. Modelo de negócio só logado (NE1, NE2)
- Experience Cloud · cadastros — Papéis, entidade PJ, documentos (NE4, NE5)
- Experience Cloud · autorizador — Órgão dono do dado, parecer, PDF (NE7)

**Revenue**
- Catalog + Pricing — Faixa, bilhetagem, opcional único. 3 modelos da reunião (NE1)
- Cart + simulação — Só fábrica prateleira (NE3)
- Document Generation — Minuta, cláusulas, dotação se administração direta (NE6)
- CLM amend / distrato — Condicionado à decisão 1 de SoR (NE12, NE13)

**Rito**
- Approval + Flow — Signatários, prazos, tabela de competência (NE8)
- Captura + Gov.BR — Sem ICP: nativo. Com A3: parceiro
- Parceiro ICP / A3 — Só se jurídica exigir (FN8.04)

**Plataforma**
- Identity · Gov.BR — OIDC/SAML, Prata/Ouro no claim (NE2)
- Platform Events — Provisionar / suspender acesso (NE11, NE12)
- Agentforce + Service — Onda 4. NE16 crítica no DV, não na reunião
- Sales Cloud — Nativo se SF é a loja. Integração se CRM for outro (NE9)

**MuleSoft**
- CNISPJ — PJ Dataprev (NE5)
- ERP handoff — Contrato assinado (FN10.01)
- PNCP — Registro da publicação. Validade jurídica (NE8)
- OCR / docs — Ressalva. Fallback manual após 3 tentativas (FN4.03)

**Externo**
- Gov.BR — Auth e, se for o caso, assinatura
- ERP Dataprev — Fonte oficial após handoff, no texto do DV
- PNCP — Lei 14.133
- Produtos contratados — 9 no portfólio (reunião). APIs de acesso ainda sem inventário
- Órgão controladora — Autoriza. Dataprev custodiante

**Ponto de decisão, assinatura.** Sem validade ICP-Brasil: Approval + captura + Doc Gen + Gov.BR. Com token A3: parceiro. O DV trata A3 como desejável. A reunião pôs a validade do contrato público no PNCP, não no token. O Luis lembra que ICP não era necessário no rito atual. Confirmar com jurídica, não assumir de memória.

**Contrato exclusivo.** Se a decisão 2 incluir a fábrica 2, esta camada de Cart + Pricing não se aplica. A jornada entra por Doc Gen + Approval + portal, sem simulação de faixa.

---

## Visão Técnica · 2 de 5

### Necessidades do DV × módulo, com o recorte da reunião

16 NEs no Documento de Visão. Não são 14+2. Fora: NE14 e FN10.02. Em conflito com a reunião: NE15. Condicionado a SoR: NE12 e NE13. Desejável: NE9. Crítica no DV e onda na estratégia: NE16.

#### Mapa DV v1.1

| NE | O quê | DV | Reunião 31/08 | Módulo (hipótese prateleira) |
|---|---|---|---|---|
| **NE1** | Catálogo, vitrine, modelos de negócio | Crítico | 9 produtos, 3 jeitos de preço | Revenue Catalog + Experience |
| **NE2** | Auth Gov.BR, e-mail, Prata/Ouro para assinar | Crítico | Gov.BR + bases PJ | Identity (OIDC/SAML) |
| **NE3** | Carrinho e simulação | Crítico | Só fábrica prateleira | Revenue CPQ |
| **NE4** | Papéis, docs, fiscais, OCR 80% | Crítico | Verificação documental dos signatários, automatizar a regra | Experience + OCR (ressalva) + Flow |
| **NE5** | Cadastro PJ via CNISPJ | Crítico | Integração bases PJ | Experience + MuleSoft |
| **NE6** | Minuta, cláusulas, dotação se público | Crítico | Dotação para administração direta | Document Generation |
| **NE7** | Autorizador externo | Crítico | Órgão controladora; Dataprev custodiante | Experience + Approval |
| **NE8** | Assinatura, 30 dias, PNCP, 2 signatários Dataprev | Crítico | PNCP = validade jurídica. Registrar publicação | Approval + Flow. Parceiro se ICP |
| **NE9** | Feed CRM ganho/perdido | Desejável | Não foi a dor | Nativo se SF é a loja. Senão, integração |
| **NE10** | ERP + portal cliente | FN10.01 crítico; FN10.02 riscado | Pós-vigência fora; encontro via ERP | MuleSoft FN10.01. FN10.02 fora |
| **NE11** | Provisionar acesso | Muito importante | Implícito na entrega do produto | Platform Events. Falta inventário das 9 APIs |
| **NE12** | Distrato | Crítico | Automatizar atos; exceção manual | CLM se SoR = SF. Senão, cerimônia + ERP |
| **NE13** | Aditivo, reajuste, razão social | Crítico | Idem | Idem NE12 |
| **NE14** | Reenquadramento COMPREV | Crítico no DV | Pós-vigência fora | Fora deste caso |
| **NE15** | Cadastro PF / CNISPF | Crítico e "futuro" | Nunca B2C | Estacionada. Conflito explícito |
| **NE16** | Chatbot, Case, CSAT | Crítico | Não foi a dor nº 1 | Agentforce + Service. Onda 4 nesta hipótese |

---

## Visão Técnica · 3 de 5

### Happy path primeiro. Os 22 estados são a máquina de exceção.

O DV lista 22 estados do dossiê, vários de encerramento. Para desenho e para conversa com o cliente, o rito feliz cabe em oito passos. Autorizador e PNCP só entram quando o produto e o tipo de ente exigirem.

#### Celebração, caminho feliz — 8 passos

1. **Vitrine** — NE1, guest ou logado
2. **Gov.BR + PJ** — NE2, NE5, CNISPJ
3. **Carrinho / modelo** — NE3, 3 preços
4. **Papéis e docs** — NE4, OCR com fallback
5. **Autorizador, se houver dono do dado** — NE7, não é todo produto
6. **Minuta + assinaturas** — NE6, NE8, cliente + 2 Dataprev
7. **PNCP, se ente público** — NE8, validade jurídica
8. **Handoff ERP + acesso** — FN10.01, NE11, fim da celebração

Estados 2, 6, 7, 8, 13 e 22 do DV são encerramentos (desistência, rejeição, ausência de assinatura, ausência de PNCP, cancelamento administrativo). Úteis na máquina. Ruins como slide de processo.

#### Os 22 estados, para quem for implementar Flow DV

| # | Estado | Tipo |
|---|---|---|
| 1 | Prospecção | Início |
| 2 | Desistência do cliente | Terminal |
| 3 a 7 | Autorizador: espera, aceite, ajuste, cancelado, rejeitado | NE7, se aplicável |
| 8 a 11 | Assinatura: prazo estourado, espera cliente, espera Dataprev, assinado pelo cliente | NE8 |
| 12 a 17 | PNCP: espera, cancelado, rejeitado, anexado, em validação, validado | Só ente público |
| 18 a 21 | Acesso: espera, erro, liberado, Produção | NE11 + handoff |
| 22 | Cancelamento administrativo | Terminal interno |

---

## Visão Técnica · 4 de 5

### Nativo, integração, ressalva, parceiro, fora

Inventário para diligência, a partir do mapeamento do Luis. Não usar "~90% nativo" como garantia comercial. O número é a leitura dele sobre a fábrica prateleira (nativo + add-on Salesforce), com ICP como único gap duro, que ele lembra não ser necessário.

#### Inventário diligência

| Módulo | Papel | Situação | NEs |
|---|---|---|---|
| **Revenue Cloud** Catalog, Pricing, CPQ, Doc Gen | Prateleira: catálogo, os 3 preços, minuta | Nativo — SKU Advanced a confirmar | NE1, NE3, NE6 |
| **Revenue Cloud CLM** | Aditivo / distrato | Condicionado a SoR | NE12, NE13 |
| **Experience Cloud** | Vitrine, cadastros, autorizador. Celebração, não portal de NF | Nativo — licença guest/named sem volumetria | NE1, NE4, NE5, NE7 |
| **Approval + Flow** | Assinatura sem ICP, prazos, PNCP, competência | Nativo | NE7, NE8 |
| **Identity** | Gov.BR OIDC/SAML | Integração — habilitação Gov.BR | NE2 |
| **MuleSoft** | CNISPJ, ERP, PNCP, produtos, OCR externo | Integração — RNF ≤ 5s | NE5, FN10.01, NE8, NE11 |
| **Sales Cloud** | Pipeline | Desejável nativo se SF é a loja | NE9 |
| **Agentforce + Service + Surveys** | Chat e Case | Onda 4 nesta hipótese | NE16 |
| **Einstein OCR / parceiro** | Docs e comprovante PNCP, 80% em 5 min | Ressalva — fallback manual já no DV | FN4.03, FN8.09 |
| **Parceiro de assinatura** | A3 / ICP-Brasil | Parceiro, se jurídica exigir | FN8.04 |
| **Fora** | Portal NF/RAS/fiscais; reenquadramento COMPREV; PF até o DEME mudar a fala | Fora / estacionado | FN10.02, NE14, NE15 |

#### Gaps reais desta hipótese

| Item | Situação | Tratamento |
|---|---|---|
| ICP-Brasil / A3 | Gap só se validade jurídica exigir token | Parceiro. Sem ICP = nativo. Confirmar jurídica. |
| OCR 80% | Ressalva de produto | Serviço externo via MuleSoft. Tarefa humana após 3 tentativas (já no DV). |
| Gov.BR Auth Provider | Integração | OIDC/SAML nativo. Depende de habilitação. |
| CNISPJ, ERP, PNCP, 9 produtos | Integração | MuleSoft. Inventário de API dos 9 ainda não existe neste material. |

**O gap que não é da Salesforce:** payload e dono do FN10.01. Sem a ferramenta de pós-vigência nomeada, o handoff não tem contrato de integração.

---

## Visão Técnica · 5 de 5

### Integrações, RNF, riscos de implementação

MuleSoft é o tecido. ERP só no handoff. RNF de 10 usuários internos não descreve a loja externa. O risco que o cliente verbalizou (custom que quebra) é o critério para aceitar ou recusar cada LWC.

#### Sistemas externos

**Gov.BR**: Auth. Prata/Ouro para assinar. Pode entrar como canal de assinatura se não houver ICP de parceiro.

**CNISPJ**: API Dataprev. Preenche PJ. Tipos: público, estatal dependente/não, privado.

**ERP**: FN10.01, contrato assinado. Não NF, não RAS, não reenquadramento.

**PNCP**: Lei 14.133. Publicação é validade, não anexo. Registrar confirmação do cliente (fala da reunião).

**Produtos (9)**: Provisionamento. Inventário de API ainda não veio na volumetria.

**Órgão controladora**: Autoriza produtos cujo dado não é da Dataprev. NE7. Ex.: INSS no COMPREV, no DV.

#### RNF do DV, com nota BSA

| Dimensão | Requisito | Nota |
|---|---|---|
| Página / clique / integração | ≤ 5 segundos | Integração ≤ 5s depende das APIs Dataprev, não do Salesforce. |
| E-mail | ≤ 30 s | Assinatura, PNCP, autorizador. |
| Chatbot | ≤ 30 s | RNF do DV. Fora da Onda 1 nesta hipótese. Streaming se um dia entrar. |
| OCR | ≤ 5 min, ≥ 80% | Não nativo robusto. Fallback já especificado. |
| Internos | Até 10 simultâneos | Analista DEME. Não é a carga da loja. |
| Volume | ≥ 50 contratações/mês | RNF do DV, não a volumetria pedida por Rogerio. Tratar como piso, não como tamanho do deal. |
| Visual | Identidade Dataprev | Gov.br DS em Experience. Esforço, não produto. |

#### Riscos de implementação (critério: a fala deles)

Qualquer item que empurre custom de plataforma para o dia 1 precisa de justificativa escrita. Eles disseram que isso quebra a cada semestre.

| Nível | Risco | Como tratar |
|---|---|---|
| Alto | Recair em LWC/OmniStudio no portal e na captura, repetindo a dor atual | Maximizar Experience padrão + Flow + Approval. Cada LWC vira exceção nomeada. |
| Alto | SoR duplo Salesforce × ERP depois do handoff | Decisão 1 antes de comprar CLM. |
| Alto | Rescisão automática por PNCP em ente público | Jurídica Dataprev. Trilha de auditoria. Não é "só um Flow". |
| Médio | SKU Revenue Cloud Advanced (cláusulas condicionais, amend) | Diligência de licença depois da decisão 1 e 2. |
| Médio | OCR 80% e APIs ≤ 5s | Risco de terceiro. Fallback manual já previsto. |
| Médio | Guest user + LGPD em vitrine pública | Sharing, Shield, Hyperforce Brasil. Dataprev é custodiante, não controladora, na fala da reunião. |
| Médio | Nove produtos, N APIs de acesso, sem inventário | Piloto de um produto na Onda 1. Não prometer os nove. |
| Baixo | Carga de 10 gestores e ≥ 50/mês | Escala trivial se a volumetria real não explodir. O desafio é rito, não CPU. |

#### Fecho da visão Técnica

A aderência de prateleira no Salesforce é a leitura do Luis, e é crível: portal, catálogo, minuta, rito, Gov.BR, MuleSoft. O que não é crível ainda é um único desenho que resolve exclusivo, PF, chatbot crítico, CLM pós-handoff e 90% nativo ao mesmo tempo. A Técnica devolve a Estratégia com um recado: dá para nascer nativo na Onda 1, se o time recusar custom (a lição do ServiceNow) e se as cinco decisões forem respondidas antes do SKU.

---

## Fontes

### Primárias

- Reunião **Loja DTP - Salesforce**, 31/08/2026, 14h (notas Granola, Juliane Lopes). Hildegard Barbosa pelo DEME. Pedidos: DV de ~8 telas, volumetria (Rogerio Meira), aderência nativa, envio da transcrição para o Hildegard.
- Documento de Visão DV_Marketplace v1.1, 20/05/2026, DEME. Necessidades NE1 a NE16, fluxo de 22 estados, RNF.
- Arquitetura de módulos Salesforce × requisitos, HTML de **Luis Gabriel Fernandes** (SE Salesforce, time do Rogerio Meira; implementou o ServiceNow atual da loja). Eixo Experience Cloud + Revenue Cloud. Estimativa ~90% nativo + add-on. Gap duro: ICP-Brasil, com a ressalva dele de memória ("do que me lembro não precisava"), a confirmar com jurídica.

### Normativos citados no DV ou na reunião

- Decreto nº 10.188/2019 (COMPREV, RPPS). Base "2.100+" vem do DV, não de censo novo neste material.
- Lei nº 14.133 (PNCP, contratações públicas). Validade jurídica após publicação: fala da reunião 31/08.

### O que este material não é

- Não é o BSA do PAT Marketplace (MTE / Decreto 12.712/2025).
- Não é o programa de agentes/previdência da conta Dataprev.
- Não é proposta comercial. Não há ROM. Volumetria de licença ainda não chegou.

📝 Onde DV e reunião divergem (PF/B2C, papel do chatbot, SoR após assinatura, se a loja faz contrato exclusivo), o texto marca decisão em aberto em vez de escolher em silêncio.

---

*Loja Dataprev · celebração contratual · DEME × Salesforce PS Brasil.
Duas visões (Estratégia e Técnica). Owner: Juliane Lopes. Uso interno para discovery e desenho de aderência. Atualizado em 02/09/2026.*
