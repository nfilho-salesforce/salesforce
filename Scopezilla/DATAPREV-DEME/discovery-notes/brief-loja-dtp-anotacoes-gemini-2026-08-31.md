# Scoping Brief: Loja DTP (Marketplace Dataprev) — Reunião de Alinhamento de Escopo

**Source**: Loja DTP - salesforce - 2026_08_31 14_00 GMT-03_00 - Anotações do Gemini.pdf
**Date**: 2026-08-31
**Participants**: Hildegard Paulino Barbosa (Dataprev, Florianópolis), Rogerio Meira (Salesforce/consultoria — conduziu a reunião), Luis Gabriel Fernandes (Salesforce/consultoria — já teve histórico prévio com o projeto), Juliane Lopes, Juliana Brites, Rene Soares — todos aparentemente do lado consultoria/Salesforce, tomando notas e conduzindo perguntas. Convidados que não aparecem falando na transcrição: Fernanda de O Pacheco Rodrigues, Nelson Stebulaitis Filho [Unknown — presença não confirmada pela fala]. Ausente: Thiago (motivo médico).
**Original length**: ~28 minutos de reunião, transcrição ≈ 4.000–4.500 palavras (23 páginas do PDF, incluindo timestamps).

---

## Business Context
- Dataprev está migrando de um modelo de contratos exclusivos/sob-medida por cliente para um modelo de produtos "de prateleira" — o mesmo sistema é vendido a diferentes clientes variando apenas configurações específicas. [00:04:08]
- Objetivo central do projeto: automatizar o rito de contratação adotando um padrão semelhante a e-commerce (analogia usada: Netflix — processo padronizado para todos que assinam). [00:05:19]
- Motivação: crescimento do volume de clientes tornou inviável manter o modelo artesanal de elaboração de contrato por cliente. [00:05:19]
- Estratégia adotada internamente: "termo de adesão" — o contrato deve ser o mesmo para todos os clientes de um determinado produto. [00:05:19]

## Current State
- Já existe uma solução/ferramenta em produção hoje que cobre parte desse fluxo de contratação ("hoje já existe uma solução... que faz hoje esse marketplace"). [00:22:22–00:23:58]
- Dor atual principal: excesso de customização na ferramenta existente compromete a sustentabilidade do produto no longo prazo — atualizações de versão da plataforma que sustenta o produto causam quebras de funcionamento recorrentes, aproximadamente a cada seis meses. [00:23:58] [Confirmed — dita explicitamente por Hildegard]
- Portfólio atual: 9 produtos, com plano de expandir esse portfólio e permitir que as equipes atuem em contratações mais complexas. [00:20:58]
- Modelo de venda é estritamente B2B (não B2C). [00:07:03]

## Desired State
- Priorizar o máximo de soluções nativas da plataforma Salesforce, minimizando customizações — critério explícito de sucesso/diferencial da nova solução. [00:23:58, 00:11:59]
- Sistema deve resolver automaticamente o máximo possível das situações rotineiras (contratação, cancelamento, aditivo), deixando intervenção manual apenas para casos de exceção. [00:16:58]
- Suportar múltiplos modelos de precificação/comercialização de produto:
  - Produtos faturados por consumo (bilhetagem), sem seleção prévia de unidades — geração de contrato com faturamento no momento da execução. [00:18:29–00:19:45]
  - Produtos tipo API com seleção de capacidade mensal (ex.: 5.000 ou 10.000 consultas/mês), com exibição de preço no momento da seleção. [00:19:45]
  - Produtos complexos com componentes opcionais de execução única (instalação, configuração, consultoria) somados a valores mensais recorrentes. [00:19:45]
- Automatizar a verificação documental de representantes legais (signatários) — validar se a pessoa física que assina pela pessoa jurídica possui a devida autorização, substituindo validação manual que não escala com o volume de contratos assinados por semana/mês. [00:13:18–00:14:27]
- Suportar aditivos (reajuste de valor, mudança de razão social) e cancelamentos (distratos) dentro do próprio fluxo automatizado. [00:16:58]

## Integrations
- Autenticação via Gov.br para identificação do representante/signatário. [00:07:03]
- Integração com bases de pessoas físicas e jurídicas para determinar a natureza do órgão cliente (administração direta ou estatal dependente/não dependente) e assim confeccionar o contrato de acordo com essa natureza. [00:07:03]
- Controle/monitoramento da publicação obrigatória do contrato no Portal Nacional de Contratações Públicas (PNCP) — a validade jurídica do contrato depende dessa publicação. [00:08:45]
- Ao final da celebração contratual, o contrato é "jogado" para o ERP da empresa, e a gestão contratual contínua passa a ser feita por outra(s) ferramenta(s) já em curso, fora do escopo desta solução. [00:15:44]

## Data Migration
- Não foi discutido volume ou plano de migração de dados legados nesta reunião. [Unknown]

## Users & Roles
- Cliente é sempre B2B — nunca venda diretamente a pessoa física (B2C). [00:07:03]
- Representantes legais (signatários) — pessoas físicas que assinam pela pessoa jurídica cliente, sujeitos a validação documental automatizada. [00:13:18]
- Equipe interna Dataprev vai avaliar o documento de visão junto a um especialista interno em soluções de marketplace Salesforce para determinar viabilidade e nível de customização necessário. [00:10:21]

## Timeline & Constraints
- Nenhuma data de go-live, prazo contratual ou faseamento foi discutido nesta reunião. [Unknown]

## Budget Signals
- Discussão de orçamento ocorreu apenas no sentido de regras de negócio (classificação orçamentária do cliente público — administração direta vs. estatal dependente/não dependente para fins de empenho), não de investimento no projeto Salesforce. [00:07:03] Nenhuma sinalização de faixa de investimento para o próprio projeto foi feita. [Assumed — nenhuma menção a modelo de funding ou processo de aprovação]

## Compliance & Security
- Autenticação obrigatória via Gov.br. [00:07:03]
- Validade jurídica do contrato condicionada à publicação no PNCP — exigência legal, reforçada por parecer jurídico interno; auditoria do TCU também verifica esse controle. [00:08:45]
- Muitos produtos da Dataprev envolvem dados dos quais a empresa é mera custodiante, não proprietária — é necessária autorização do órgão controlador para poder comercializar esse serviço a outro ente público. [00:07:03–00:08:45]
- Sistema precisa diferenciar entes públicos (administração direta vs. estatal dependente/não dependente) para fins de origem orçamentária do contrato. [00:07:03]

## Decisions Made
- **Definição do escopo na celebração contratual** — Escopo da nova solução definido para focar exclusivamente na "celebração contratual" (rito inicial de contratação, incluindo aditivos e cancelamentos), excluindo a gestão contratual contínua pós-vigência, que já é tratada por outra ferramenta existente integrada ao ERP. [Confirmed — marcado como "Alinhada" nas anotações do Gemini] [00:15:44–00:16:58]
- **Priorização de soluções nativas** — Estratégia de desenvolvimento definida para priorizar funcionalidades nativas da plataforma Salesforce, minimizando customizações para garantir sustentabilidade e facilidade de atualização do produto a longo prazo. [Confirmed — marcado como "Alinhada"] [00:11:59, 00:23:58]

## Action Items
- **[Hildegard Paulino]** Compartilhar o documento de visão detalhando regras de negócio, requisitos e particularidades do sistema de contratação. — sem data definida
- **[Hildegard Paulino]** Informar volumetria: números detalhados de utilização e escala do projeto atual (quantidade de produtos, transações, clientes, contratos, pessoas que interagem com a solução). — sem data definida
- **[Equipe interna Salesforce/consultoria]** Avaliar internamente o documento de visão, com apoio de especialista em marketplace, para determinar viabilidade da solução Salesforce e o nível de customização necessário.
- **[Rogerio Meira]** Enviar a transcrição da reunião para Hildegard Paulino.
- Possibilidade mencionada (não formalmente comprometida) de realizar uma demonstração (demo) da solução de marketplace já existente da consultoria para a equipe Dataprev. [00:25:33] [Unknown — tratado como sugestão, não como compromisso firme]

## Open Questions & Ambiguity
- Números de volumetria (quantidade de clientes, transações, contratos) ainda não foram compartilhados — dependem do documento a ser enviado por Hildegard. [Unknown]
- Nível exato de customização necessário só será determinado após a análise interna do documento de visão pelo especialista em marketplace. [Unknown]
- Mecânica de captura/registro do "consentimento legal" dos signatários foi levantada por Rene Soares mas não detalhada na reunião. [Unknown] [00:13:18]
- Não ficou claro se Fernanda de O Pacheco Rodrigues e Nelson Stebulaitis Filho, listados como convidados, efetivamente participaram — não aparecem falas atribuídas a eles na transcrição. [Unknown]
- Confirmação formal de agendamento de demo ainda pendente. [Unknown]

## Key Quotes
> "Em algum momento a empresa decidiu investir cada vez mais em produtos de chamadas de prateleira, que a gente pode vender o mesmo produto para diferentes clientes... a gente decidiu adotar a estratégia de termo de adesão... o contrato deve ser o mesmo para todos os produtos, para todos os clientes daquele produto... tal como a gente faz em outras soluções de e-commerce quando contrata, sei lá, a Netflix da vida." — Hildegard Paulino [00:05:19]

> "Tô falando cliente como B2B, a gente não vende B2C." — Hildegard Paulino [00:07:03]

> "Todos precisam colocar o contrato na Portal Nacional de Contratações Públicas, PNCP... O contrato só tem a validade se for publicado lá... já ouvi dizer até que a auditoria do TCU também, a gente precisa ter esse controle." — Hildegard Paulino [00:08:45]

> "Eu acho que o principal ponto aqui... é ter uma solução mais nativa possível e que atenda os requisitos que vocês precisam sem tanta customização... Eu acho que o objetivo principal é isso." — Luis Gabriel Fernandes [00:11:59]

> "Seria muito ruim a gente ficar alocando alguém para ficar validando se aquele documento da pessoa tá correto, se a pessoa realmente representa aquele órgão." — Hildegard Paulino [00:14:27]

> "Eu queria focar que essa solução... focasse na parte de celebração contratual... se for privado... tá em produção, joga esse contrato no nosso ERP e daí em diante vai ser gerido por outras soluções." — Hildegard Paulino [00:15:44]

> "A gente ter verificou muita customização, então isso compromete a sustentabilidade do produto no longo prazo, porque versões da plataforma... trocam [a versão] rotineiramente... a cada seis meses [a gente fica] com produto com algum tipo de quebra." — Hildegard Paulino [00:23:58]

> "Existem ainda outros produtos com uma característica um pouco mais complexa... que além de possibilitar essa capacidade mensal, também tem alguns componentes opcionais de execução única, por exemplo, instalação, configuração, consultoria." — Hildegard Paulino [00:19:45]
