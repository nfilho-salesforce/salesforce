# Fase 1 — Fundação — Modelo de Dados + Identidade + Integração + Residência (31/ago – 27/set · Sem. 3-6) (DATAPREV-PAT)

> **Orquestração da fase — o que está dentro/fora da fase, dependências, estado inicial.** Leia isto primeiro para se orientar. As especificações construíveis por capacidade vivem em `11-intents-1.md` (quando presente) — é contra elas que você de fato constrói, um intent por vez.
> Duração da fase: **4 semanas (compromisso do usuário)**.

## Intenção

- **Para:** A equipe de implementação inteira (arquitetura + dev + MuleSoft), arrancando junta sobre a org greenfield dedicada — mais a beneficiária/estabelecimento como usuários finais do portal gov.br.
- **Resultado:** Estabelecer a base compartilhada de que todas as frentes dependem: o modelo de dados Sales Cloud nativo (Account = beneficiária/CNPJ; Opportunity = demanda; Quote = resposta da facilitadora), a camada de integração API-led do MuleSoft on-premise (com mocks contract-first), a residência híbrida com CPF tokenizado resolvido em runtime, e a identidade gov.br no Experience Cloud. Ratificar o modelo de dados fundacional é o marco que libera a paralelização das Fases 2 e 3.
- **Medido por:** Modelo de dados fundacional ratificado com o time inteiro (INT-009, INT-010, INT-014); camada MuleSoft on-premise de pé com mocks incluindo o contrato do gateway (INT-001..008); referência tokenizada resolvendo em runtime na org dedicada (INT-002, INT-009, INT-010); login gov.br OIDC operante no portal Partner Community (INT-014, INT-018).
- **Não deve:** Não persistir CPF nem dado sensível do trabalhador na org (ADR 0001 — só referências tokenizadas). Não construir capacidade de leilão/financeiro nesta fase (Fases 2/3). Não abrir a paralelização antes de o modelo de dados fundacional fechar. Não introduzir Revenue Cloud/CLM (baseline Core-only, ADR 0004).

## Pré-decidido (não re-litigar)
- **Objetos nativos Sales Cloud, sem custom sell-side inventado**: Account = beneficiária (CNPJ), Opportunity = demanda do leilão reverso, Quote = resposta da facilitadora via API (ADR 0004, decision_log).
- **Residência híbrida (ADR 0001)**: CPF e dados sensíveis nunca persistem na org; ficam na Dataprev e são resolvidos em runtime via MuleSoft on-premise. Só referências tokenizadas na org (INT-009, INT-010).
- **Org 100% greenfield e apartada + MuleSoft ON-PREMISE (ADR 0002/0005)**: nova, isolada de qualquer ambiente/admins Dataprev; integração na infra soberana.
- **Facilitadoras (~600–700) são integrações API MuleSoft, não seats de portal**; a beneficiária é o driver de licença do Experience Cloud (decision_log).
- **Baseline Core-only**: sem Revenue Cloud, sem CLM, sem Billing (ADR 0004).
- **Integração contract-first**: mocks primeiro, virada mock→real governada (INT-001).

## Perguntas do modo Plan (resolver antes de passar ao modo Build)
- Fronteira de residência campo-a-campo (G0801): quais campos são tokenizados vs. persistidos? A ratificação re-molda o data model — precisa fechar antes do build.
- Não existe conector gov.br OIDC nativo (G0101): confirmar a abordagem de federação OIDC no Experience Cloud (INT-014).
- Contratos de API dos sistemas externos existem? (G0501 — Novo PAT possivelmente sem API): o inventário existe/não-existe governa a estratégia de mock (INT-001, INT-004).
- Geride expõe a validação CPF↔CNPJ por API? (INT-016) — se não, definir a alternativa.

## Perguntas do modo Build (perguntar só se a situação surgir)
- Nomes de API dos objetos e campos do termo de aceite (faixa salarial, matriz/filial) — a definir no workshop de modelagem.
- Formato e claims do token OIDC gov.br (mapeamento para o usuário do portal).
- Contrato exato do serviço de de-tokenização MuleSoft (payload, latência aceitável em runtime).

## Épicas no escopo desta fase

O brief de fase é autoritativo. As épicas abaixo estão listadas apenas para referência cruzada — quando uma automação cita `(E04)`, é a isto que ela se refere. Para a narrativa mais profunda da épica, veja `90-epics-context.md`.

- **E05: Integração Corporativa (MuleSoft)** — Camada de integração API-led MuleSoft ON-PREMISE (ADR 0005 — instalado na infra Dataprev/gov, dentro do perímetro soberano; resolve G0504; ponto de de-tokenização do CPF). Conecta Novo PAT (que HOJE NÃO TEM API — transcrição 31/jul, MT/DTI: mock-first obrigatório), GOV.BR/Geride, CTPS Digital ('expectativa de crédito' ao trabalhador no processamento da folha — só monitoramento no MVP), eSocial, SDC, INIS PJ/Kinis PJ (origem do termo de aceite — nº trabalhadores por faixa salarial e matriz/filial, E02), o gateway/banco custódia (recebe a boletagem com split e o valor a pagar; devolve o boleto registrado e as MOVIMENTAÇÕES BANCÁRIAS em BATCH INCREMENTAL via AGENDAMENTO no MuleSoft — ADR 0003) e as APIs das ~600-700 facilitadoras (recepção de Quotes/propostas e devolução de processado+valor, MAIS a EXPOSIÇÃO DE UM ENDPOINT DE CONSULTA das demandas/leilões abertos na vigência — pull no MVP: a facilitadora consulta e descobre as demandas publicadas pelas beneficiárias, sem push ativo; a notificação ativa/push é roadmap futuro, com o canal a definir — E02/G0211, decisão 31/jul). ADQUIRENTE (transcrição 31/jul): API para a adquirente CONSULTAR o status de credenciamento do estabelecimento antes de processar transações; a adquirente envia TODAS as transações para monitoramento/analytics interno (antifraude/desvio) — feed de monitoramento é near-term para a consulta e V2/futuro para o analytics completo. Validação de estabelecimento por CNPJ: client credentials flow, connected app com escopo restrito, validação de token com rate limit e cache. Mock-first para desbloquear o desenvolvimento enquanto Swaggers/contratos não são disponibilizados.
- **E08: Segurança, Residência de Dados & Conformidade** — Três eixos de isolamento que coexistem. (1) RESIDÊNCIA (ADR 0001): modelo de dados com referências tokenizadas — CPF e dados sensíveis não persistem na nuvem Salesforce, resolvidos em runtime via API. (2) TOPOLOGIA (ADR 0002): instância Salesforce dedicada e apartada para o MTE/PAT, isolada das demais orgs de clientes da Dataprev — isolamento forçado (não opção) por segurança/sensibilidade financeira (conta custódia, split), volumetria (~800k estabelecimentos, ~450k beneficiárias), auditabilidade (TCU/CGU/ANPD) e administração pelo próprio MTE. (3) SOBERANIA/GREENFIELD (ADR 0005): ambiente 100% greenfield — nenhuma org/admin compartilhada com outros ambientes Dataprev — e MuleSoft ON-PREMISE na infra soberana, de modo que o dado sensível não sai do perímetro e nenhum administrador de outro ambiente o enxerga; o MuleSoft on-premise cumpre as exigências de soberania de dados. Segurança/auditoria são requisito explícito escrito na proposta com justificativa: observabilidade, trilha de auditoria imutável do acesso a dado sensível, mascaramento de CPF nos logs. Diagrama de fluxo de dados sob LGPD (Art. 11). Requisito transversal a todas as épicas.
- **E01: Portal & Identidade gov.br** — Fundação Experience Cloud do marketplace: login gov.br (OpenID Connect), procuração digital, fluxo 'representar empresa', navegação e controle de acesso do portal da BENEFICIÁRIA (e do estabelecimento). Base de identidade e experiência sobre a qual os processos de negócio (E02/E03/E04) são renderizados. Licenciamento (corrigido no grill 31/jul): o driver de licença de portal é a BENEFICIÁRIA — que opera Opportunity (demanda) e Quote (comparação/seleção) no portal. A FACILITADORA é API-only (E05), NÃO consome licença de portal — as ~600–700 facilitadoras são integrações MuleSoft, não assentos. A versão da licença da beneficiária (Partner Community vs. Customer Community Plus) segue a requalificar (G0103/G0108): Customer Community Plus não expõe Opportunity/Quote nativamente; se a beneficiária precisar operá-los no portal, Partner Community é a candidata, a confirmar.

## Alvos de construção — resumo de orquestração

Estas seções orientam o agente de construção sobre o formato da fase. O detalhe construível por capacidade (Resultado, Alvo de construção, Guardrails, Fora de escopo, Aceite, Perguntas em aberto) vive em `11-intents-1.md` por intent. Quando uma seção abaixo cita `INT-NNN`, consulte o intent lá.

### Modelo de dados
Base fundacional nativa Sales Cloud e a espinha de residência. O modelo de referências tokenizadas (INT-009) garante que CPF/dado sensível nunca resida na org, com de-tokenização em runtime via MuleSoft (INT-010). Sobre a base nativa (Account/Opportunity/Quote — ADR 0004) modela-se o termo de aceite e a estrutura matriz/filial e faixa salarial que as fases seguintes consomem. A detalhe carregado vive nos intents INT-009 e INT-010; a ratificação deste modelo é o marco que libera a paralelização.

### Automação
A validação de vínculo CPF↔CNPJ via Geride (INT-016) é a automação fundacional que habilita a representação de empresa no portal. A resolução de identidade e de-tokenização em runtime é acionada pela camada de integração, não por gravação de dado sensível.

### UI & navegação
Portal Experience Cloud (Partner Community) com login gov.br OIDC (INT-014), seleção 'representar empresa' dirigida por procuração (INT-015), controle de navegação por papel (INT-017) e sessão/logout federado gov.br (INT-018). O portal é a superfície onde beneficiária e estabelecimento entram — as jornadas de negócio (leilão, credenciamento, financeiro) chegam nas fases seguintes.

### Segurança & acesso
Espinha de segurança formalizada nos ADRs 0001/0002. Autenticação federada gov.br (INT-014), acesso de menor privilégio na org dedicada (INT-013), trilha de auditoria imutável de acesso a dado sensível (INT-011), mascaramento de CPF em logs/erros (INT-012) e autenticação + rate-limit dos chamadores externos no gateway de API (INT-003). Nenhum CPF persiste; todo acesso sensível é auditável (TCU/CGU/ANPD).

### Relatórios & dashboards
Sem relatórios/dashboards de negócio no escopo desta fase — é fundação (dados, identidade, integração, residência). O único artefato de dados relevante é a trilha de auditoria de acesso a dado sensível (INT-011), consumida por conformidade, não por dashboard operacional.

### Dados de exemplo
_(opcional — carregar só a pedido do usuário)_

### Fontes de dados

Camada API-led MuleSoft on-premise, contract-first com mocks (INT-001). Fontes: serviço de de-tokenização/resolução de identidade na Dataprev (INT-002), System APIs de leitura/validação de fontes federais mock-first (INT-004), ingest do termo de aceite INIS/Kinis PJ (INT-005), contrato padrão da facilitadora — hand-off de Quote, retorno 'processado', endpoint de consulta de demandas em aberto (INT-006), API de checagem de credenciamento + monitoramento transacional do adquirente (INT-007), feed agendado de conciliação de movimentação bancária gateway→CRM (INT-008), e o contrato de integração com o gateway (mockado nesta fase).

## Aceite — verificações de resultado para o usuário (nível de fase)

Afirmações de resultado para o usuário, no nível da fase, que um stakeholder percorreria para sentir que "a Fase 1 está pronta". Rode-as em conversa com o usuário; marque `- [x]` somente quando o usuário concordar. Os walkthroughs de aceite por intent vivem em `11-intents-1.md`.

Uma beneficiária acessa o portal, autentica-se via gov.br, escolhe representar a empresa cujo vínculo CPF↔CNPJ é validado, e navega apenas às áreas do seu papel — sem que nenhum CPF tenha sido gravado na org. O time confirma que a org greenfield está de pé, o MuleSoft on-premise responde aos mocks contract-first (incluindo o gateway), e o modelo de dados fundacional foi ratificado.

## Aceite — verificações em forma de metadados (nível de fase)

Verificações em forma de metadados, no nível da fase — consultas que o agente de construção roda contra a org alvo sem ajuda humana. Rode via a skill Metadata (describe / tooling / SOQL). O aceite por intent está em `11-intents-1.md`.

Verifica-se na org: (a) nenhum objeto persiste CPF — apenas referências tokenizadas (INT-009); (b) a chamada de de-tokenização resolve em runtime via MuleSoft on-premise (INT-010); (c) a trilha de auditoria registra cada acesso a dado sensível de forma imutável (INT-011) e logs mascaram CPF (INT-012); (d) o login OIDC gov.br cria/associa o usuário do portal com o papel correto (INT-014, INT-017); (e) o modelo de acesso é de menor privilégio na org dedicada (INT-013); (f) as System APIs MuleSoft respondem contract-first com mocks versionados (INT-001..008).

## Fora do escopo da Fase 1

Se você perceber que precisa construir qualquer um destes, pare e sinalize — pertence a uma fase posterior ou está explicitamente excluído.

_(nenhum surgiu em gaps.json — confirme com o usuário na revisão do modo Plan)_

## Dependências e riscos

**Dependências:** Fase 0 (org greenfield provisionada, MuleSoft on-premise instalado, blockers resolvidos, gateway selecionado). A definição fundacional do modelo de dados É o pré-requisito interno que precede a paralelização de E02/E04 na Fase 2. E01 depende de E05 (resolução de identidade) e E08 (Contact tokenizado).

**Riscos:** Se o modelo de dados fundacional não fechar cedo, a paralelização não arranca e a data fixa fica em risco — é o gargalo de sequenciamento interno. Ausência de contratos de API (G0501, Novo PAT sem API) trava a virada mock→real; fronteira de residência (G0801) não ratificada re-molda o data model; conector gov.br OIDC nativo inexistente (G0101); adaptar objetos nativos sell-side (Opportunity/Quote) ao padrão comprador→N-vendedores adiciona esforço (ADR 0004). Fase de maior carga dentro da janela mais apertada da história do projeto.

## Citações de histórias cobertas nesta fase

- (US-0501) Como desenvolvedor/integrador, quero estruturar a camada de integração em API-led connectivity (System, Process e Experience APIs) no Anypoint Platform, para que cada sistema externo seja desacoplado da lógica de orquestração e do consumo pelos portais.
- (US-0502) Como desenvolvedor/integrador, quero gerir e monitorar as APIs pelo API Manager, para aplicar políticas de segurança e observar tráfego de forma centralizada.
- (US-0503) Como desenvolvedor/integrador, quero um framework mock-first (mocking service / MUnit) para cada sistema ainda sem Swagger, para que o desenvolvimento e os testes do marketplace não fiquem bloqueados pela ausência de contratos reais.
- (US-0504) Como desenvolvedor/integrador, quero uma estratégia contract-first que permita trocar o mock pela integração real assim que o Swagger chegar, para minimizar retrabalho quando os contratos forem disponibilizados.
- (US-0505) Como plataforma, quero autenticar consumidores externos (facilitadoras, adquirente) via client credentials flow com connected app de escopo restrito, para que cada integrador acesse apenas os recursos autorizados.
- (US-0506) Como plataforma, quero validar o token de acesso em cada chamada aplicando rate limit por consumidor, para proteger os backends soberanos contra abuso e picos (ex.: fechamento de mês).
- (US-0507) Como plataforma, quero cachear resultados de validação de token e consultas idempotentes de baixa volatilidade, para reduzir latência e carga sobre os sistemas de origem.
- (US-0508) Como plataforma, quero realizar a de-tokenização do CPF em runtime dentro do perímetro soberano (MuleSoft on-premise, ADR 0005), para que o CPF em claro nunca transite nem seja persistido fora da infraestrutura Dataprev/gov.
- (US-0509) Como desenvolvedor/integrador, quero implantar os runtimes MuleSoft on-premise na infra Dataprev/gov (ADR 0005), para que a camada de integração opere dentro do perímetro soberano e conecte a nuvem aos sistemas internos.
- (US-0510) Como plataforma, quero uma System API para o Novo PAT operando em modo mock-first (o Novo PAT hoje não tem API), para desbloquear o desenvolvimento das validações de situação cadastral desde já.
- (US-0511) Como plataforma, quero validar via Novo PAT a situação regular (cadastro obrigatório) de beneficiárias e facilitadoras, para que apenas participantes em situação regular operem no marketplace.
- (US-0512) Como plataforma, quero obter do INIS PJ / Kinis PJ os dados de origem do termo de aceite (nº de trabalhadores por faixa salarial e estrutura matriz/filial), para alimentar a base de contratação e cotação (E02).
- (US-0513) Como plataforma, quero integrar identidade e autenticação via GOV.BR/Geride, para suportar login das beneficiárias com procuração digital no portal (E01).
- (US-0514) Como plataforma, quero enviar à CTPS Digital a 'expectativa de crédito' ao trabalhador (apenas monitoramento no MVP), para notificar o trabalhador de forma análoga ao aviso de crédito do FGTS.
- (US-0515) Como plataforma, quero uma System API para o eSocial em modo mock-first, para preparar o consumo de dados trabalhistas/vínculos assim que o contrato real for disponibilizado.
- (US-0516) Como plataforma, quero uma System API para o SDC em modo mock-first, para desbloquear a integração dependente do SDC sem esperar o contrato real.
- (US-0517) Como gateway/banco custódia, quero receber da plataforma a boletagem com split e o valor a pagar, para gerar o boleto registrado da folha em conta custódia de banco público.
- (US-0518) Como gateway/banco custódia, quero devolver à plataforma o boleto registrado, para que a beneficiária possa efetuar o pagamento e a plataforma acompanhe o status.
- (US-0519) Como plataforma, quero consumir as movimentações bancárias do gateway em batch incremental via agendamento (ADR 0003), para conciliar pagamentos e split sem depender de webhooks em tempo real.
- (US-0520) Como plataforma, quero garantir idempotência e controle de checkpoint no batch incremental de movimentações, para que reprocessamentos não dupliquem lançamentos na conciliação financeira.
- (US-0521) Como facilitadora, quero consultar via endpoint um pull das demandas/leilões (cotações) abertos na vigência, para captar oportunidades e decidir sobre o envio de propostas.
- (US-0522) Como facilitadora, quero enviar minhas propostas (Quotes) via API para uma cotação aberta, para participar do leilão reverso sem operar por portal manual.
- (US-0523) Como facilitadora, quero receber a folha e devolver o processado + o valor apurado via API, para fechar o ciclo financeiro da folha contratada.
- (US-0524) Como facilitadora, quero (roadmap futuro) receber push de notificação de novas demandas, para reagir mais rápido do que no modelo pull do MVP.
- (US-0525) Como adquirente, quero consultar via API o status de credenciamento de um estabelecimento por CNPJ antes de processar transações, para só autorizar transações de estabelecimentos ativos no marketplace.
- (US-0526) Como adquirente, quero enviar transações à plataforma para monitoramento (near-term, para consulta), para dar visibilidade das operações ao MTE mesmo antes do analytics completo.
- (US-0527) Como MTE/plataforma, quero (V2 roadmap) o analytics completo das transações da adquirente, para identificar padrões anômalos e irregularidades além da simples consulta.
- (US-0528) Como plataforma, quero trilha de auditoria e observabilidade em todas as integrações, para atender aos requisitos de auditoria ANPD/TCU/CGU sobre operações financeiras e de dados sensíveis.
- (US-0529) Como desenvolvedor/integrador, quero tratamento padronizado de erros com retry e dead-letter nas integrações assíncronas, para que falhas transitórias dos sistemas de origem não percam mensagens nem travem o fluxo.
- (US-0530) Como desenvolvedor/integrador, quero um modelo canônico de dados (canonical data model) nas Process APIs para as entidades-chave (beneficiária, facilitadora, estabelecimento, cotação, proposta, folha, transação), para desacoplar os formatos dos sistemas de origem do núcleo do marketplace.
- (US-0801) Como Arquiteto de dados, quero um modelo de dados baseado em referências tokenizadas em que CPF e dados sensíveis não persistam na org Salesforce, para que a nuvem nunca armazene dado pessoal sensível e o programa cumpra a decisão de residência de dados.
- (US-0802) Como Arquiteto, quero que o CPF e demais dados sensíveis sejam resolvidos (de-tokenizados) em runtime via MuleSoft contra a infra Dataprev, para que a plataforma exiba/utilize o dado apenas no momento do uso sem nunca persisti-lo.
- (US-0803) Como Admin de plataforma, quero uma instância Salesforce dedicada e apartada exclusiva do MTE/PAT, isolada das demais orgs Dataprev, para que a sensibilidade financeira, a volumetria e a auditabilidade do programa fiquem contidas em um perímetro próprio.
- (US-0804) Como Admin de plataforma, quero que o ambiente seja 100% greenfield, provisionado do zero sem reaproveitar org, metadado ou administração de outros ambientes Dataprev, para que o isolamento de segurança seja garantido por construção.
- (US-0805) Como Arquiteto, quero que o MuleSoft rode on-premise na infraestrutura soberana Dataprev (não em CloudHub), para que o dado sensível não saia do perímetro soberano em nenhum momento do trânsito.
- (US-0806) Como Auditor/DPO, quero uma trilha de auditoria imutável de todo acesso a dado sensível, para que qualquer resolução ou visualização de CPF possa ser comprovada e não possa ser adulterada.
- (US-0807) Como Admin de segurança, quero que o CPF e dados sensíveis apareçam mascarados em todos os logs (aplicação, integração, depuração), para que nenhum dado pessoal sensível vaze por telemetria ou troubleshooting.
- (US-0808) Como Admin de segurança, quero um modelo de controle de acesso baseado em menor privilégio com perfis/permission sets por papel (beneficiária, facilitadora API-only, MTE, admin, auditor), para que cada ator acesse apenas o que sua função exige.
- (US-0809) Como Admin de plataforma, quero observabilidade e monitoramento de segurança (eventos de login, acessos a dado sensível, chamadas de integração, anomalias), para que incidentes sejam detectados e respondidos rapidamente.
- (US-0810) Como DPO, quero que o tratamento de dado pessoal sensível esteja documentado e amarrado a uma base legal sob o Art. 11 da LGPD, para que o programa comprove conformidade no tratamento de dados sensíveis dos trabalhadores.
- (US-0811) Como Auditor, quero relatórios e evidências de auditoria prontos para TCU, CGU e ANPD (acessos, transações, split, trilha imutável), para que os órgãos de controle obtenham comprovação sem intervenção manual demorada.
- (US-0812) Como Arquiteto, quero um diagrama de fluxo de dados sob LGPD como artefato versionado e mantido, para que a fronteira do dado sensível (o que persiste, o que só transita, onde é resolvido) seja explícita e revisável.
- (US-0813) Como Admin de segurança, quero gestão segura de credenciais e segredos das integrações (Named Credentials/secret store) para os callouts ao MuleSoft e à infra soberana, para que credenciais nunca fiquem expostas em código ou configuração legível.
- (US-0814) Como Admin de segurança, quero políticas de sessão e autenticação forte (MFA, timeout, restrição de IP para admins) na org dedicada, para que o acesso administrativo e privilegiado a um ambiente que orquestra dado sensível seja protegido.
- (US-0815) Como DPO, quero políticas de retenção e expurgo dos tokens/referências e artefatos de auditoria conforme LGPD, para que dados não sejam mantidos além do necessário e o expurgo seja comprovável.
- (US-0816) Como Sistema, quero controle de acesso a nível de campo (FLS) e criptografia em repouso dos campos de referência/token, para que mesmo os identificadores tokenizados só sejam legíveis por quem tem permissão e estejam protegidos em armazenamento.
- (US-0101) Como beneficiária (RH de uma empresa), quero acessar o portal do marketplace autenticando-me pelo gov.br, para entrar com minha identidade digital sem criar novo usuário e senha.
- (US-0102) Como beneficiária, quero selecionar qual empresa desejo representar após o login, para operar o portal em nome do CNPJ correto usando minha procuração digital.
- (US-0103) Como beneficiária que representa muitas empresas, quero buscar a empresa por Razão Social ou CNPJ na tela de seleção, para localizar rapidamente o CNPJ que preciso operar.
- (US-0104) Como beneficiária, quero que o portal exiba apenas as empresas para as quais tenho vínculo válido, para não operar indevidamente em nome de CNPJs que não represento.
- (US-0105) Como beneficiária que representa mais de uma empresa, quero trocar a empresa representada pelo menu superior sem deslogar, para operar em nome de outro CNPJ na mesma sessão.
- (US-0106) Como beneficiária de um grupo com matriz e filiais, quero que o portal distinga Matriz de Filial no contexto de representação, para operar cotações e folhas no CNPJ correto da estrutura.
- (US-0107) Como beneficiária, quero navegar pelo portal por um menu lateral com as áreas do marketplace, para acessar cotação, folha, empresas credenciadas e demais funções a partir de um único ponto.
- (US-0108) Como estabelecimento (restaurante/mercado), quero acessar o portal autenticando-me pelo gov.br, para iniciar meu credenciamento e acompanhar meu cadastro sem criar novas credenciais.
- (US-0109) Como estabelecimento já credenciado, quero uma área no portal para visualizar e gerenciar meu cadastro, para consultar meu status de credenciamento e dados sem depender de uma facilitadora.
- (US-0110) Como administrador da plataforma, quero que beneficiárias e estabelecimentos vejam experiências e permissões distintas conforme seu papel, para que cada ator acesse apenas as funções e dados que lhe competem.
- (US-0111) Como administrador da plataforma, quero definir o modelo de licenciamento de portal por perfil de acesso, para dimensionar corretamente licenças nomeadas (beneficiária, acesso recorrente) e por login (estabelecimento, acesso esporádico).
- (US-0112) Como analista do MTE, quero acesso administrativo e de governança à plataforma com o nível de privilégio adequado, para acompanhar a operação e administrar o que me compete sem acessar dados indevidos.
- (US-0113) Como beneficiária, quero encerrar minha sessão com segurança e ter a sessão expirada por inatividade, para proteger o acesso em nome da empresa que represento.

## Fronteira de recipe

Quando esta fase for aceita, pergunte ao usuário: *"Salvar esta execução como recipe para repetirmos na Fase 2?"* A recipe deve capturar: as decisões de modelo de dados feitas acima, os padrões de nomenclatura confirmados em `03-glossary-and-naming.md`, e quaisquer resoluções de perguntas do modo Build que surgiram.
