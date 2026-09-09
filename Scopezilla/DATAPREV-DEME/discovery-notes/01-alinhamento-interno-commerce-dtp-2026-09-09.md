<!-- Source: /Users/nfilho/Downloads/Alinhamento interno - Commerce - DTP - 2026_09_09 09_28 GMT-03_00 - Notes by Gemini.pdf · Retrieved: 2026-09-09 · Via: Claude (Read tool, PDF, 71 páginas em lotes de leitura) -->

# Alinhamento interno — Commerce - DTP (2026-09-09)

Ata gerada por Gemini Notes (transcrição editável por IA, pode conter erros — nomes próprios em especial saíram com ruído de OCR/transcrição; ver seção "Ambiguidades de nomes" abaixo). Reunião **interna Salesforce** (não é reunião com o cliente Dataprev), sobre a arquitetura de Commerce/Revenue Cloud + Experience Cloud para a Loja Dataprev (DEME).

**Participantes**: Rogerio Meira, Rene Soares, Fernanda de O Pacheco Rodrigues, Luis Gabriel Fernandes, Juliane Lopes, Nelson Stebulaitis Filho, Guilherme Mattei.

Transcrição encerrada após 01:07:34.

## Resumo executivo

Reunião discutiu a arquitetura do marketplace da Dataprev adotando Revenue Cloud + Experience Cloud; integração GOV.BR + Mulesoft para autenticação/validação documental por IA; próximo passo é uma demo prática para validar templates necessários e alinhamento com o cliente.

## Decisões (alinhadas nesta reunião)

1. **Adotar Revenue Cloud como motor central** + **Experience Cloud como vitrine (storefront)**, focado em celebração contratual B2B — **descartando Commerce Cloud** como base inicial. Racional: a complexidade do sistema não está no checkout transacional, está na celebração contratual (configurar modelos de negócio complexos, componentes obrigatórios/opcionais, faixas de recorrência e valores únicos, gerar minuta+assinatura, aplicar cláusulas, anexos condicionais por natureza do cliente, conduzir aditivos e distratos) — domínio nativo do Revenue Cloud (quote-to-contract, price rules, documentation, amendments). DataPrev não vende B2C hoje; não há pagamento online no fluxo atual; faturamento ocorre depois, no ERP (TOTVS). Um carrinho de commerce sem transação financeira agregaria pouco valor.
2. **Usar exclusivamente Screen Flows + LWCs**, descartando Omni Studio (considerado deprecated pelo time).
3. **Commerce Cloud não é descartado permanentemente** — fica como opção de camada de storefront caso no futuro haja abertura massiva para pessoa física (B2C real, com checkout transacional). Arquitetura deve ficar preparada para isso, mas não construída agora (abordagem "Lego", nas palavras de Juliane Lopes: comece pelo caminho mais simples — Revenue + Experience Cloud, inclusive versão headless — e agregue checkout/funcionalidades depois se a evolução vier).
4. Diferença de risco de customização: customização de **frontend** (LWC no Experience Cloud) não quebra em atualizações de release ("você não vai quebrar componente"). Já customização de fluxo transacional dentro do **Commerce** (celebração contratual inteira customizada em cima do app de Commerce) seria um risco real em major updates — foi um dos motivos centrais para descartar Commerce como base.
5. Solicitar ao vendor atual do cliente (ver ambiguidade de nome abaixo) uma demo da solução atual dele, para identificar pontos de dor reais antes de supor requisitos.
6. Limite de escopo do marketplace: vai até a assinatura do contrato. Após assinado, a gestão do contrato (aditivo, renovação, reajuste, distrato) fica dentro do processo que o cliente já tem hoje — TOTVS é tanto CRM quanto RP/ERP do cliente ("Qual é o RP deles? É o Totvs também"). Faturamento/bilhetagem ocorre no ERP.
7. Revenue Cloud requer Sales Cloud como pré-requisito de licenciamento ("é uma questão de licenciamento, de coaching") — Sales Cloud já vem incluído na compra do Revenue Cloud, independentemente de o cliente optar por integrar ou não com o CRM dele (TOTVS).
8. Posicionamento de integração com o CRM do cliente (TOTVS): objetivo primário é **integrar** com o CRM existente do cliente, mantendo TOTVS como fonte da verdade (a gente consome GET/POST sempre a partir da fonte da verdade). Objetivo secundário/opcional (não é o plano, é uma possibilidade a abrir com o cliente depois): eventualmente questionar se ele quer substituir o CRM. Motivo do cuidado: apresentar a solução como dependente de "outro CRM duplicado" gera percepção negativa e complica a entrada — a proposta é mostrar possibilidades e deixar a escolha com o cliente, sem assumir nada por ele.
9. Para evitar duplicidade de dados entre TOTVS e Salesforce, avaliar **Data Cloud (Zero Copy)** como forma de consumir dados do TOTVS sem duplicá-los — ainda uma pergunta aberta sobre viabilidade prática (não confirmada nesta reunião como solução fechada).

## Próximos passos (com donos)

- **[Grupo/Luis Gabriel Fernandes]** Preparar demo do template "Revenon" (nome interno do template de commerce/Revenue Cloud usado como base) — configurar catálogo, navegação de portal **sem login obrigatório**, deixar assinatura/aprovação para etapa posterior. Dúvida em aberto: configurar produtos reais do cliente vs. mock mais próximo da realidade — Luis Gabriel vai revisar documentos que tem para ajudar a parametrizar.
- **[Luis Gabriel Fernandes]** Contatar "Thiago" (líder da loja/marketplace do vendor atual do cliente) via WhatsApp para agendar uma demo da solução atual deles — meta: esta semana, se possível. Mensagem sugerida por Fernanda: pedir para o vendor mostrar tanto os pontos boas quanto os que não atendem bem, "pra gente ver como que a gente endereça dentro de casa".
- **[Fernanda de O Pacheco Rodrigues]** Compartilhar o contato do "Wild" com Luis Gabriel Fernandes (feito durante a própria reunião).
- **[Rogerio Meira]** Compartilhar no grupo do Slack a transcrição da reunião + o PDF de requisitos original enviado pelo vendor do cliente.
- **[Guilherme Mattei + Wagner]** Dono da construção técnica do "Revenon"/Revenue Cloud; Guilherme confirma disponibilidade do Wagner (baixa, mas "eu cuido dele" se precisar para o dia seguinte — sem urgência).
- **[Luis Gabriel Fernandes]** Parte de Experience Cloud considerada de baixo risco/"tranquila" para o time — ele mesmo pode puxar a configuração de catálogo no portal.
- **[Luis Gabriel Fernandes]** Já teve reunião com Hamilton no mesmo dia sobre Document AI/Data Cloud (pesquisa da parte de validação documental por IA).
- **[Guilherme Mattei]** Verificar agenda do Wagner para começar discussão técnica — meta inicial era esta semana, mas Guilherme já via a agenda dele mais livre só na segunda-feira que vem.
- Rogerio Meira reforçou que antes de uma nova rodada de discussão com o time, ele vai enviar o material que compilou + as duas fontes que usou, para cada um poder fazer sua própria análise.
- Combinado: próximos marcos de entrega devem nascer de perguntar ao cliente "o que mais dói hoje" — criar marcos de entrega junto com a jornada, não assumir do lado de dentro.

## Temas detalhados (síntese distilada + pontos adicionais capturados na transcrição verbatim)

### Contexto do Marketplace da Dataprev
"Loja"/marketplace vende produtos de prateleira e APIs para outros órgãos governamentais. Sistema atual construído sobre **ServiceNow** (2ª versão), com falhas estruturais. Responsável pela loja no lado do cliente Dataprev é referido como "Degard"/"Hild" (ver ambiguidade de nomes). Luis Gabriel Fernandes trabalhou na construção do sistema anterior (ServiceNow) enquanto estava em outra empresa (referida como "CR Sinal"), o que dá a ele conhecimento prático direto das dores herdadas.

### Dores atuais do sistema do cliente
- Customização excessiva causando quebras a cada atualização semestral (6 meses).
- Manutenção cara e arriscada.
- Processo de contratação lento e manual.
- Suporte reativo.
- Catálogo de produtos só é visível **logado** — não existe navegação/visualização de vitrine sem login hoje (dor confirmada como "muito grande" e motivo de discussão interna grande no projeto anterior também).
- Produto atualmente usado pelo cliente é relativamente novo (lançado há ~6 meses a 1 ano quando começaram a usá-lo), ainda passando por muita modificação — ponto de argumentação a favor do Salesforce (produto mais sólido/consolidado, menor risco de quebra).
- Assinatura eletrônica: formato de assinatura era uma dor no sistema anterior — cliente queria um "formato X" específico; sistema antigo só permitia organizar assinaturas de forma limitada.

### Validação documental por IA / OCR
- Cliente quer validação inicial por IA/OCR de documentos de identidade (confirmar que o documento realmente é um documento de identidade e que se refere àquela pessoa) — ideia que já existia desde a época do "CR Sinal".
- Solução hoje é baseada em Einstein (legado) — time já sabe que existe um "replacement" (substituto) — proposto: **Data 360/Document AI**.
- Requisito do cliente (conforme documento de requisitos que enviaram): "IA vai tentar ler o documento e fazer o match três vezes; se não der, cai no fallback" — pelo que Luis Gabriel leu, hoje **sempre cai no fallback** (processo manual) — ou seja, a automação atual não funciona bem na prática.
- Ponto levantado por Guilherme Mattei: Oracle (empresa de origem de Rogerio Meira) tem uma solução nativa para esse tipo de validação de identidade/notarização — mencionado como contexto competitivo, não como fato de plataforma Salesforce.
- Ainda não está claro se buscar isso com terceiros foi avaliado na época do fornecedor anterior.

### Navegação sem login na vitrine
Requisito confirmado do cliente: poder abrir o portal, navegar, visualizar produtos sem estar logado; login só seria necessário para efetivamente contratar. Ponto identificado como importante para demonstrar na demo.

### Checkout / transacionalidade — decisão de descartar Commerce Cloud
Debate extenso (Juliane Lopes, Fernanda, Rogerio, Luis Gabriel): confirmado que não há checkout com cartão hoje — "é um contrato", o final do fluxo é um contrato, não uma transação de pagamento. B2B sem pagamento online; faturamento/bilhetagem ocorre depois no ERP. Juliane: "então eu já descartaria de cara o commerce" — trabalhar em versão headless, front pode ser Experience Cloud ou qualquer coisa, os metadados usados não são de e-commerce, são do revenue (celebração contratual) — vai entrar no fluxo do Revenue Cloud. A única coisa a construir do zero é o "experienceal" (parte de Experience Cloud), onde já existe ferramental que acelera bastante.

Cenário futuro considerado (não é decisão para agora): se o cliente quiser abrir venda para pessoa física/pessoa jurídica menor/cartório com pagamento por cartão, a arquitetura precisa estar preparada — pode virar até um "site" diferente/marca separada, com autopreenchimento via lookup de CPF ("quinispo", garble de transcrição) para pessoa física. Essa possibilidade **já aparece no próprio documento de requisitos do cliente**: cadastro de cliente pessoa física, "futuro volume massivo, alto preenchimento" — ou seja, o cliente já pensa em pessoa física em algum momento futuro, não é hipótese só do time interno.

### Meios de pagamento (Salesforce Payment Cloud)
Juliane Lopes (ex-Commerce): payments hoje é "Salesforce Payment Cloud", PCI compliant, permite transação tokenizada, atende segurança exigida pelo Banco Central incluindo aceitar Pix — parte transnacional é "bem potente", começou muito americanizada mas hoje já tem Pix. Nativamente tinha 2 tipos de pagamento (ela não acompanha há ~4 anos, pode ter mais hoje): PayPal (caro para o comércio brasileiro, ~13% de taxa, "ninguém usa") e outro meio comprado pela Salesforce (marca internacional, logo azulada, ela não lembrou o nome — descrito como "bring your own payment white-label card"). Rogerio: não há apelo forte hoje para meios de pagamento tipicamente usados no Brasil pela galera. Não é bloqueador para a decisão atual (não há checkout hoje), mas relevante se/quando evoluir para B2C.

### Experience Cloud — templates nativos e diferença de esforço vs. Commerce
- Confirmado: existem templates nativos de portal Experience Cloud reaproveitáveis já com catálogo, select picker, etc. — chamado internamente de "template do Reven"/"digital commerce" — segundo Nelson, "tem bastante coisa" pronta nesse template.
- Guilherme Mattei confirma: **esse template é LWC** — nativo, "nativão de componentes nativos que eles criam" (Juliane). Nelson: template técnico LW do Commerce (B2B/B2C antigo) já vem com componentes prontos: mini carrinho, checkout, histórico de pedidos, venda guiada.
- Diferença de esforço: Guilherme nota que o Commerce já vem com a parte de seleção de produto pronta, com catálogo sincronizado nativamente com o catálogo do Revenue Cloud/CPQ — dentro do Experience, essa sincronização/parte de seleção de produto teria que ser construída do zero pelo time.
- Contexto histórico dado por Juliane (ela veio da equipe de Commerce): quando a Salesforce absorveu Commerce (comprou CloudCraze → tornou-se B2B, e Demandware → tornou-se B2C), a ideia era absorver as funcionalidades dessas ferramentas externas e agregar ao core. Criaram o app de Commerce (B2B2C) — "deu certo e deu errado" ao longo dos 7 anos dela na Salesforce. Mas todos esses templates/objetos/fluxos nativos já existem e são usados por clientes grandes (ela citou Petrobras, Ipiranga, Vibra) com Field Service, Service Cloud — ou seja, dá para aproveitar bastante do B2B2C mesmo indo pelo caminho "nativo de sales/revenue/CPQ" sem comprar o app de Commerce.
- Nenhuma demo desse template ainda foi feita pelo time internamente até a data desta reunião — era um dos objetivos da própria reunião avaliar isso, mas não deu tempo/não foi feito ainda. Motivo prático citado por Luis Gabriel: o cliente (vendor/lld) "não quer nada" ainda — só conversaram uma vez, foi tipo "next, next, finish" (baixo engajamento até agora).

### Autenticação, GOV.BR e perfis/procurações
- Autenticação e gestão de identidades hoje já é feita via GOV.BR + Mulesoft (confirmado pelo time como algo que já existe/fazem hoje, "eles já têm hoje, né?").
- Hoje o contrato é firmado no CPF de um funcionário do órgão que está contratando — é uma contratação B2B, mas o processo é feito em cima do CPF (representando o órgão).
- **Ponto de atenção levantado por Juliane Lopes — cruzamento verbal com outro projeto interno, não deve ser usado para misturar os dois projetos**: ela mencionou que a questão de "procuração" (uma pessoa que representa uma empresa/órgão precisar ter, dentro da autenticação, uma autorização para representar aquele órgão) é literalmente o mesmo fluxo que o time está passando/implementando "lá no fluxo do PAT" — citação direta da transcrição, preservada aqui por fidelidade à fonte. **Isto é uma referência feita pelos próprios participantes da reunião, não uma inferência minha — não usei isso para buscar, comparar ou alterar nada no projeto DATAPREV-PAT, conforme instrução permanente de manter os dois projetos isolados.** Se for útil no futuro perguntar diretamente à Juliane sobre esse paralelo, é uma opção — mas não tratei isso como fonte de conhecimento técnico aqui.

### Integração com CRM do cliente (TOTVS) e risco de duplicidade de dados
Ver decisões 7-9 acima para o essencial. Detalhes adicionais da discussão:
- Rogerio recordou um precedente de projeto anterior — um cliente citado na transcrição como "Sony"/"Sinal" (nome provavelmente distorcido por OCR/transcrição, não confirmado) — onde trabalharam três pilares: (1) construção de novos projetos/marketplace, (2) CRM propriamente dito (gestão de vendas), (3) medição/analytics. Esse trabalho de marketplace fica ao lado das vendas, faz parte do mesmo ecossistema, mas é um caminho adicional além do "SEOS" (Sales/Service Cloud).
- Preocupação real de Rogerio não é técnica, é de **posicionamento comercial**: soar como se a solução exigisse "mais um CRM" para o cliente se preocupar gera percepção negativa. Consenso final do time: apresentar como integração com o CRM existente (TOTVS), sem assumir nada pelo cliente, deixando a decisão de integrar vs. substituir com ele.
- Debate técnico sobre Zero Copy (Data Cloud): ideia é consumir dados do TOTVS sem duplicá-los para completar transações (cruzamento de dados contratuais etc.), e no final do ato, postar a conclusão de volta para o TOTVS — evitando duplicidade. Ainda uma pergunta aberta ("não sei se é possível ou não" — Juliane). Ponto técnico levantado por Guilherme: se o dado mudar dentro do Salesforce (ex.: cliente muda telefone via Experience Cloud), esse delta precisa propagar de volta para o TOTVS via post/webhook — mecanismo de sincronização de "delta", não duplicação plena.
- Escala mencionada no documento de requisitos do cliente: **reenquadramento anual de mais de 2.100 clientes** com PR/RP, conforme faixas de competência — detalhe concreto de volume não capturado na nota anterior (00-loja-dtp-...).

### Fluxos contratuais, faturamento e limite de escopo
- Marketplace vai até a assinatura do contrato. Gestão pós-assinatura fica no processo já existente do cliente. RP (ERP) do cliente = TOTVS (mesmo sistema do CRM).
- Requisito do cliente conforme documento fornecido: integração com CRM — prospecção, oportunidade, ganha/perda, assinado/encerrado precisam ser sinalizados e propagados para o CRM atual (TOTVS). Integração com RP: envio do contrato assinado como fonte oficial.
- Automação: entrega e liberação de acesso ao produto após assinatura via Flow + Platform Events. Cancelamento, extrato, avaliação interna, suspensão, termo de distrato, assinatura e encerramento via Flow + Digital Signature. Aditivo contratual, renovação, reajuste, mudança de razão social via equipe (revenue cloud, templates de termo aditivo chancelados, roteados à equipe por exceção).
- Geração de minuta: hoje o cliente faz via integração com Office 365 (constrói o template, com place-holders substituídos automaticamente) — confirmado como "funciona" pelo time (Guilherme). Alternativa: gerador interno do Salesforce, mais complicado/trabalhoso, mas possível. Contrato do cliente é direto com a Microsoft (não é uma solução gov-específica) — não há problema de licenciamento para usar essa integração.
- Assinatura eletrônica hoje é via flow, certificado padrão **A3** (padrão brasileiro de certificado digital).

### Visão de arquitetura consolidada (lida por Rogerio Meira de um documento de posicionamento)
Experience Cloud integrado com GOV.BR, AgentForce, Data 360/Document AI, analytics; motor de contratação = Revenue Cloud; Sales Cloud CRM + assinatura digital; orquestração via Flows (Screen Flows) e LWCs; eventos de plataforma (Platform Events); Shield para dados e governança; modelo de dados; integração de APIs com sistemas externos.

### Agentes de IA
Proposta (Rogerio Meira): agente de IA com base na documentação do marketplace, fazendo papel de assistente de compras/atendimento; validação documental por IA (Document AI); agente de apoio à gestão interna como copiloto para analistas de gestão do marketplace — resume pendências, sugere próximos passos, red de comunicações, analítico de previsão de funil (não existe hoje) — evolução de funil sobre a data prévia de contratação, painéis de conversão, prospecção, gargalos e previsão de volume.

### Posicionamento competitivo e argumento de venda
- Argumento central: solução atual do cliente é relativamente nova (lançada há pouco tempo no fornecedor atual), ainda passando por muita modificação — vs. produto Salesforce mais consolidado, menor risco de quebra.
- Vender o pacote (Revenue Cloud, que já inclui capacidades adjacentes de commerce) em vez de vender Commerce Cloud como produto isolado — custo é o mesmo de qualquer forma (Fernanda confirma: "o produto é um só e vai tá disponível" independente de integrar ou não; "o custo é o mesmo").
- **Nota de contexto interno (não é fato de arquitetura, é dinâmica interna Salesforce)**: Rogerio e Fernanda alertaram sobre outro time interno ("galera do Saulo", de Vendas) que pode tentar se adiantar e comunicar a outro stakeholder interno ("Pelitoni"/nome não confirmado) que "já fez" o projeto — risco de sobreposição/território interno, não subestimar. Relevante para Nelson como consciência de dinâmica interna, não para o corpo técnico da proposta.

## Ambiguidades de nomes (não resolvidas — flag para o usuário)

A transcrição (gerada por IA a partir de áudio) tem ruído consistente em nomes próprios. Aparecem, muito provavelmente referindo-se à **mesma entidade** (o fornecedor/vendor atual do cliente e/ou seu representante), as grafias: **"Hild"**, **"lld"**, **"Yild"**, **"Wild"**, **"RioD"**. Também aparece **"Thiago"** como o líder da loja/marketplace desse vendor, e **"Degard"** como o responsável pela loja no lado Dataprev — não está claro se "Degard" é a mesma pessoa que "Hild/lld/Yild/Wild" ou uma pessoa diferente do lado do cliente. Recomendo confirmar a grafia correta antes de usar esses nomes em qualquer material formal (proposta, e-mail). Também aparecem "CR Sinal" (empresa anterior onde Luis Gabriel trabalhou) e um cliente citado como "Sony"/"Sinal" em um precedente de projeto (pilares CRM) — nomes possivelmente distorcidos pela transcrição automática, não confirmados.
