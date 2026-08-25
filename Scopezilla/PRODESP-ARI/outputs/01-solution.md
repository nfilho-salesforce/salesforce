# Solução — ARI PRODESP / Desenvolve SP

*Migração da esteira de crédito de Sales Cloud + Experience Cloud para Financial Services Cloud (FSC) + Experience Cloud, no mesmo org de produção (migração in-place). Gerado em 2026-08-25.*

Este documento descreve **o que** a plataforma passa a fazer e **a arquitetura que sustenta cada capacidade**. Ele parte de um fato decisivo: o org de produção da Desenvolve SP já tem o modelo de dados de lending do FSC provisionado e licenciado, mas ainda **não adotado** — a jornada atual roda sobre objetos padrão do core (Lead, Opportunity) e objetos customizados. Portanto isto é uma **adoção/migração**, não uma construção do zero. `[KB: fsc-fit-gap-report.md:1-60]`

O sequenciamento faseado (o que entrega em que ordem) está em `outputs/02-delivery-plan.md`; o dimensionamento de complexidade por épico está em `data/estimates.json`.

---

## Camada 1 — Fundações de Arquitetura (decisões transversais)

### F1. Estratégia de org — transformação brownfield in-place, um único org

A migração acontece dentro do org de produção existente (`00Das000005XO3tEAG`) — sem novo org, sem split. Os objetos de lending do FSC (ResidentialLoanApplication, LoanApplicant e correlatos) já existem no org, hoje com zero registros, enquanto a jornada viva roda sobre core padrão + objetos customizados. `[KB: fsc-fit-gap-report.md:1-60]` `[KB: knowledge/01-solution.md — org brownfield único, FSC em LEX interno + Experience Cloud LWR]` Manter um único org preserva visão única do tomador e evita sobrecusto de integração e governança de múltiplos orgs.

### F2. Modelo de dados alvo — lending nativo do FSC (ratificação na Fase 0)

O destino da migração re-hospeda a jornada nos objetos nativos: ResidentialLoanApplication, LoanApplicant (com Income, Employment, Liability, Asset), Person Accounts, Product Catalog Management (PCM) e Business Rules Engine (BRE). `[KB: fsc-fit-gap-report.md:1-90]` **Esta adoção está marcada como "REVISAR" no relatório de fit/gap — ainda não ratificada.** `[assumption: adoção do lending nativo do FSC ratificada na Fase 0 — se negada, o escopo recua de migração de modelo (ROM de fit/gap: 8-14 sprints) para reaponte leve; G0012]` O tamanho de cada pilar depende diretamente dessa decisão.

### F3. Person Accounts — habilitação irreversível

Person Accounts está **desabilitado hoje**; habilitá-lo é uma ação de mão única e precisa ser ensaiada em sandbox full-copy antes do cutover de produção. `[KB: fsc-fit-gap-report.md — Account/Contact FIT, Person Accounts DESABILITADO]` `[assumption: a arquitetura de baseline descreve conversão Lead→Person Account em produção, mas Person Accounts está desligado hoje — conflito de fonte, confirmar ao vivo; G0701]`

### F4. Substituição por recursos nativos — PCM e BRE no lugar de objetos customizados

Product2 + `EnquadramentoProduto__c` migram para Product Catalog Management (PCM); `Enquadramento__c` migra para DecisionTable / Business Rules Engine (BRE); `Instituicao__c` migra para Account (Record Type); `Metrica__c` é mantido. `[KB: fsc-fit-gap-report.md:90-180]` Estas são as frentes de maior esforço no fit/gap ("Produto→PCM Alto, 2-3 sprints; modelo de crédito nativo Alto, 3-5 sprints").

### F5. Modelo de compartilhamento e segurança — mantido, re-ancorado nos objetos FSC

Padrão de compartilhamento organizacional privado (Org-Wide Defaults privado) + Apex Managed Sharing para a visibilidade cooperativa; autenticação gerenciada pela plataforma (Named Credentials / External Credentials + External Client App com JWT). `[KB: knowledge/01-solution.md — OWD privado, Apex Managed Sharing, auth gerenciada pela plataforma]` O padrão não muda; o modelo de compartilhamento apenas se re-ancora nos objetos Person Account / FSC após a migração.

### F6. Razão config/código e governança

Pró-código como padrão (Lightning Web Components + Apex), Flow para o simples, OmniStudio como último recurso; a nova superfície declarativa (PCM/BRE/DecisionTable) exige pipeline de metadados e governança de um Centro de Excelência (Center of Excellence). `[KB: knowledge/01-solution.md — camada de serviço headless]` `[assumption: stewardship de dados pessoais / LGPD e o Centro de Excelência de metadados declarativos estão sem dono definido — G0407/G0516/G0606/G0708/G1106]`

### F7. Estratégia de sandbox e cutover

Ciclo de sandbox com Developer/Developer Pro para build e integração e **full-copy obrigatório** para o ensaio de migração e a habilitação irreversível de Person Accounts antes do passo de produção. `[extends: knowledge/01-solution.md — org brownfield; padrão Salesforce de ensaio full-copy antes de mudança irreversível]` `[assumption: volume de dados de produção não confirmado — as contagens atuais são do sandbox HML; G1004]`

### F8. Licenciamento — verificado ativo, permanência a confirmar

Todas as licenças Industries estão **ativas em produção** (BRE, PCM Admin/Viewer, Salesforce Pricing, Context Service, Decision Explainer, Digital Lending, FSC Standard/Extension, Unified Catalog). `[KB: fsc-fit-gap-report.md — seção de licenciamento]` `[assumption: permanência contratual das licenças Industries não confirmada; G0807/G0704]`

---

## Camada 2 — Solução por Processo de Negócio

A ordem abaixo segue o fluxo de criação de valor: primeiro a fundação que precisa existir (E07, E08), depois a jornada do tomador de crédito na ordem em que ele a percorre (Captação → Formalização), e por fim as frentes horizontais de integração, migração de dados e cutover.

### Habilitação FSC e Modelo de Dados (E07)

**Contexto de negócio.** O org já possui o modelo de lending do FSC, mas a jornada nunca o adotou — ela vive em Lead/Opportunity e objetos customizados. Sem essa fundação, nenhum pilar pode migrar.

**Abordagem de solução.** Habilitar Person Accounts (F3) e adotar os objetos nativos de lending (ResidentialLoanApplication, LoanApplicant e correlatos, hoje com zero registros), além de Action Plans e configuração de relacionamento no nível declarativo. É a base transversal aos seis pilares. `[KB: fsc-fit-gap-report.md:1-90]`

**Arquitetura de suporte.** Habilitação de Person Accounts é irreversível e ensaiada em full-copy (F3, F7). Sem dependência de outros épicos — é a cabeça do caminho crítico.

### Catálogo e Elegibilidade Nativos (E08)

**Contexto de negócio.** O produto de crédito e as regras de enquadramento hoje moram em objetos customizados (`Product2`+`EnquadramentoProduto__c`, `Enquadramento__c`, `Instituicao__c`), fora do modelo nativo.

**Abordagem de solução.** Adotar Product Catalog Management para o catálogo de produtos, Business Rules Engine / DecisionTable para as regras de elegibilidade e Account (Record Type) para instituições, mantendo `Metrica__c`. `[KB: fsc-fit-gap-report.md:90-180]`

**Arquitetura de suporte.** As duas frentes de maior esforço do fit/gap (F4). Depende de E07 (os objetos nativos precisam existir antes de o catálogo e as regras se ancorarem neles).

### Pilar 1 — Captação (E01)

**Contexto de negócio.** Porta de entrada da jornada: enriquecimento JUCESP, cadastro manual, simulador, Minhas Contas e cooperativas. Este pilar já está em QA no build atual, portanto tem o menor risco de retrabalho funcional.

**Abordagem de solução.** Migrar a captação para os objetos FSC — Lead→LoanApplicant, Person Account para tomadores pessoa física — com a simulação apoiada em OpportunityLineItem. `[KB: epics.json E01]` `[assumption: mapeamento Lead→LoanApplicant por pilar — validar na Fase 0]`

**Arquitetura de suporte.** Integração de enriquecimento (JUCESP) e a única chamada síncrona da jornada (simulação de captação, F9/E09). Fora isso, reaproveita o padrão de compartilhamento e auth das Fundações.

### Pilar 2 — Pré-qualificação (E02)

**Contexto de negócio.** Formulário adaptativo, validação facial (BioValid), consulta QRSA, integração Serpro e-CAC e envio síncrono ao core. É o pilar com a maior superfície de integração.

**Abordagem de solução.** Migrar o `CreditApplication__c` para ResidentialLoanApplication; a elegibilidade passa a rodar sobre BRE/PCM. `[KB: fsc-fit-gap-report.md:60-120]`

**Arquitetura de suporte.** Onze integrações, incluindo BioValid, Serpro e QRSA — o pilar mais dependente da prontidão de API. `[assumption: BioValid e Serpro como sistemas externos — confirmar contratos de API]` Refatoração Serasa prevista. A superfície de integração é reapontada, não reconstruída (F9).

### Pilar 3 — Proposta (E03)

**Contexto de negócio.** Lista de solicitações e detalhamento de status — essencialmente uma camada de leitura para o tomador acompanhar o andamento.

**Abordagem de solução.** Migrar a leitura para os objetos FSC, reaproveitando componentes de acompanhamento da Home. `[KB: fsc-fit-gap-report.md:1-60]` `[assumption: P3 reaproveita componentes da Home — validar inventário no build atual]`

**Arquitetura de suporte.** Quatro integrações QRSA. É o pilar mais leve — configuração padrão, sem arquitetura bespoke além das Fundações.

### Pilar 4 — Estruturação (E04)

**Contexto de negócio.** Fichas cadastrais PJ/PF, geração de PDF, bloqueio de edição, upload assíncrono, orquestração de status e Central de Pendências. É o maior pilar e a maior superfície de migração da onda de build.

**Abordagem de solução.** Migrar os dados de tomador para LoanApplicant/Income/Employment e as garantias de `Garantia__c` para LoanApplicantAsset; substituir o vaivém de e-mail pela Central de Pendências. `[KB: fsc-fit-gap-report.md:120-180]` `[assumption: Garantia__c→collateral (0 registros hoje) — confirmar destino nativo; G0404]`

**Arquitetura de suporte.** Oito integrações e quatorze componentes. Upload de documentos via Amazon S3 externo (limites de 6 MB síncrono / 12 MB assíncrono), com o MuleSoft guardando o binário no S3 e enviando referências/metadados ao Sinqia. `[KB: NOTELM Memory 24ago.md — arquitetura de upload S3]` `[assumption: repositório de documentos acima de 12 MB (Agro) diferido/indefinido; G0603]`

### Pilar 5 — Aprovação (E05)

**Contexto de negócio.** Aceite/recusa síncrono e orquestração de ocorrências, com a efetivação no core. A reanálise elevou este pilar ao absorver o aceite (F13).

**Abordagem de solução.** Migrar o aceite síncrono para os objetos FSC, com a efetivação disparada por Platform Event (`OpportunityInfo__e`) consumido pelo MuleSoft. `[KB: knowledge/01-solution.md — arquitetura event-first, uma chamada síncrona]` `[assumption: efetivação síncrona via Platform Event — confirmar padrão de evento no build atual]`

**Arquitetura de suporte.** Uma integração (API-09) e uma tela de decisão. Herda o padrão event-first das Fundações (F: integração). A fronteira P3↔P5 (aceite) precisa ser reconciliada na Fase 0 para evitar dupla contagem ou buraco de escopo. `[KB: memory.json — G0511]`

### Pilar 6 — Formalização (E06)

**Contexto de negócio.** Encerramento da jornada: download da Cédula de Crédito Bancário (CCB), upload da CCB assinada e Meus Contratos.

**Abordagem de solução.** Migrar o fluxo de formalização para os objetos FSC. `[KB: fsc-fit-gap-report.md:1-60]`

**Arquitetura de suporte.** Quatro integrações e três componentes. O provedor de assinatura digital da CCB ainda não está definido — o produto mínimo viável usa assinatura manual até a definição. `[assumption: provedor de assinatura digital da CCB não definido — thread aberta; G0601]`

### Reapontamento de Integrações — 30 APIs (E09) · frente horizontal, trilha paralela

**Contexto de negócio.** As 30 integrações MuleSoft hoje conversam com o modelo customizado; após a migração precisam falar com os objetos FSC.

**Abordagem de solução.** Reapontar **apenas o lado Salesforce** de cada integração: named credentials, mapeamento de campos para objetos FSC, refactor de callouts Apex e regressão por integração. As APIs no barramento **não são reconstruídas**. `[KB: fsc-fit-gap-report.md:1-40]` `[KB: NOTELM Memory 24ago.md — 19 APIs essenciais quantificadas]`

**Arquitetura de suporte.** Arquitetura event-first com uma única chamada síncrona (F: integração); fronteira de propriedade Salesforce-only (F6 / A6 — MuleSoft, Sinqia e Evertec são do cliente/parceiro). Apenas JUCESP está em QA; 29 das 30 APIs estão sem Swagger/contrato e com write-back PUT/PATCH pendente — o maior risco de cronograma. `[assumption: contratos das System APIs permanecem estáveis — se mudarem, a transformação MuleSoft vira escopo adicional; G0013]`

### Migração de Dados e Descomissionamento (E10)

**Contexto de negócio.** A migração in-place exige converter os dados vivos para o modelo nativo e aposentar os objetos superados.

**Abordagem de solução.** ETL e conversão: Account/Contact→Person Accounts, `CreditApplication__c` (68)→ResidentialLoanApplication, `Garantia__c`→collateral; desativar `Simulacao__c` (381) e `Parcela__c` (14.356), superados por OpportunityLineItem + evento; manter `Metrica__c` (262) e `AntiFraudAnalysis__c` (90); reconciliação. `[KB: fsc-fit-gap-report.md:180-260]`

**Arquitetura de suporte.** É a frente cujo esforço é dirigido pelo volume de produção — hoje não confirmado (as contagens são do sandbox HML), o que a mantém com confiança **Assumida**. `[assumption: volume de dados de produção não confirmado — driver de esforço do engenheiro de dados; G1004]` O registro Lead (10.105) ainda não está endereçado no plano de migração.

### Testes, Regressão e Cutover (E11)

**Contexto de negócio.** Fechar a migração com qualidade e virar a chave em produção.

**Abordagem de solução.** SIT/UAT, regressão in-place ampla (o maior risco da migração), governança de pipeline/metadados para a nova configuração declarativa (PCM/BRE/DecisionTable) e o cutover em produção (habilitação de Person Accounts + run de migração), seguido de hypercare. `[KB: fsc-fit-gap-report.md:180-260]`

**Arquitetura de suporte.** Ensaio full-copy obrigatório antes do passo irreversível (F3, F7). Depende de E10. A regressão in-place ampla e o cutover irreversível são os maiores riscos técnicos do programa.

---

## Resumo dos conflitos de fonte a ratificar na Fase 0

| # | Conflito / premissa | Onde impacta | Gap |
|---|---------------------|--------------|-----|
| 1 | Adoção do lending nativo do FSC marcada "REVISAR" | F2, E07, E08 e todos os pilares | G0012 |
| 2 | Person Accounts desabilitado hoje vs. conversão descrita em produção | F3, E07, E10 | G0701 |
| 3 | Estabilidade dos contratos das System APIs (29/30 sem contrato) | E09 | G0013 |
| 4 | Volume de dados de produção não confirmado | E10, E11 | G1004 |
| 5 | Fronteira P3↔P5 (aceite) não reconciliada | E03, E05 | G0511 |
| 6 | Provedor de assinatura digital da CCB indefinido | E06 | G0601 |
| 7 | Permanência contratual das licenças Industries | F8, E07, E08 | G0807/G0704 |

*As premissas load-bearing acima já estão registradas em `data/gaps.json`. Se a Fase 0 não ratificar a adoção do lending nativo (conflito 1), o escopo da migração recua de migração de modelo para reaponte leve, e o dimensionamento dos pilares muda.*
