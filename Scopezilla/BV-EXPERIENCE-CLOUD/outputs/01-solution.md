# BV — Solução Experience Cloud + MuleSoft

**Cliente:** BV Financeira (Banco BV) · Financial Services · Brasil
**Natureza:** engajamento *brownfield* — três portais Experience Cloud já em produção e uma camada de integração MuleSoft/Apigee viva. O escopo é remediação de débito técnico e ativação de recursos prioritários, preservando produção (ADR 0001). Não é um build do zero.
**Bloqueador comercial paralelo:** as licenças Experience Cloud não fazem parte do contrato do Experience Hub; o BV precisa contratá-las antes do go-live (ADR 0002 / R1).

Este documento tem duas camadas. Primeiro as **Fundações de Arquitetura** — as decisões horizontais que nenhuma épica isolada carrega. Depois a **Solução por Processo de Negócio** — a jornada épica a épica, na ordem do fluxo de valor do ciclo de vida de API, com a arquitetura específica de cada capacidade embutida no seu lugar.

---

## Fundações de Arquitetura

Decisões transversais aos três portais. Cada épica adiante herda estas escolhas sem repeti-las.

### Estratégia de org

Assumimos **org única** (single-org): os três portais coexistem numa org de produção Experience Cloud já viva, com ambientes de desenvolvimento derivados dela. É a topologia mais provável num brownfield de portais que já compartilham catálogos e identidade, e simplifica governança e modelo de dados. `[assumption: topologia single-org e número/tipo de sandboxes não confirmados — validar se os 3 portais compartilham a org e se há refresh de Full Sandbox com dados de produção — G0403]`

### Modelo de compartilhamento (público vs. privado)

O catálogo de APIs é exposto em duas visibilidades — público e privado. Governamos isso por **Org-Wide Defaults externo restritivo** nos objetos Produto e Versão de Produto, abrindo visibilidade privada por *sharing sets* / grupos disparados na criação do registro de acesso de parceiro à versão. A visibilidade de usuário externo é controlada pela configuração *Site User Visibility* do Experience Cloud. `[KA-10297]` `[KA-10398]` `[KA-10395]` A regra de **revogação/expiração** de acesso (o que acontece ao fim de um contrato/parceria) ainda não está definida e é risco de vazamento de visibilidade se ficar em aberto. `[assumption: critério público-vs-privado e comportamento de revogação a detalhar — G0205]`

### Identidade e login diferenciado

Usamos **Login Discovery** com um único FederationId por usuário, roteando o acesso básico por senha e o acesso de parceiro/interno por provedor de identidade (IdP). `[KB: experience_cloud_4-2-2026.md:52751-53002]` `[KB: experience_cloud_4-2-2026.md:4088-4410]` A dependência real que dimensiona esse fluxo não é o mecanismo — é a **existência de um IdP nomeado e federável** para os parceiros externos e para os usuários internos. Nenhum dos dois está nomeado hoje. `[assumption: IdP de parceiros e IdP interno não nomeados/confirmados — G0202/G0301]`

### DevOps, release e não-regressão (brownfield)

Sobre produção viva, toda mudança passa por uma **esteira de deploy versionada** com teste de não-regressão dos três portais, janelas de release e caminho de rollback. A cadeia de ferramentas ainda não foi nomeada — a decisão está entre *change sets*, Salesforce DevOps Center (Git-backed, point-and-click) e uma esteira CI/CD completa (SFDX + Gearset/Copado). Com produção viva e mais de um desenvolvedor, recomendamos no mínimo o DevOps Center. `[assumption: toolchain de deploy/versionamento a nomear — change sets vs. DevOps Center vs. SFDX/Gearset/Copado — G0404/G0409]` (ancorado na ADR 0001)

### Governança de configuração multi-time

O ciclo de vida de API é operado por múltiplos times (Governance, times donos das APIs, integração MuleSoft) e cruza vários sistemas. Falta um dono claro das regras do ciclo de vida (estados, critérios de validação OPA, política de exceção) e da configuração transversal aos três portais. Sem esse árbitro, decisões conflitantes entre times travam a evolução e arriscam a estabilidade em produção. `[assumption: autoridade de decisão e dono da config transversal — PS vs. BV; necessidade de Centro de Excelência/gestão de mudança — G0107/G0306/G0405]`

### Camada de integração — API-led com Apigee no edge

A integração segue o padrão **API-led connectivity** de três camadas: SAPIs (conectam sistemas — Jira, Apigee Apps Management, Anypoint OAS), XAPIs de processo/orquestração, e XAPIs de consumo segregadas por sistema de destino. `[KA-0441 — recomendação da prática MuleSoft, opinião de arquitetura]` `[KA-0042 — arquitetura de referência que evita integração ponto-a-ponto]` `[KB: MuleSoft — Catálogo Estratégico Consolidado (EN) (Claude).md:17-52]` O **Apigee permanece no gateway de borda** (TLS context de entrada/saída) e o MuleSoft opera como a camada XAPI/SAPI atrás dele — coexistência, não substituição. O ownership das políticas de borda do Apigee está em aberto, assim como a caracterização exata da limitação do Anypoint contratado pelo BV. `[assumption: ownership da borda Apigee — G0603]` `[assumption: limitação do Anypoint a caracterizar; pode onerar geração de OAS e render de contrato — R2/G0602]`

### Requisitos não-funcionais de serviços financeiros

Como banco com operação Open Finance, o desenho precisa de padrões que ainda não estão especificados: mascaramento de PII e retenção no logging de callouts (LGPD), mTLS entre camadas, rotação de certificados, e um esforço de hardening/QA para portais externos (teste de segurança, carga, UAT) antes do go-live. Estes moldam o desenho das apps Mule e do framework de logging. `[assumption: logging com mascaramento PII/retenção nível FS — G0406]` `[assumption: NFRs de throughput/latência/mTLS Open Finance a definir — G0605]` `[assumption: QA/hardening/pentest/carga do go-live não escopado como build — vive como linha PS de QA no roster — G0407/G0611]`

---

## Solução por Processo de Negócio

A ordem segue o fluxo de valor do ciclo de vida de API: os catálogos são carregados, o ciclo de vida governa a API, os parceiros externos consomem, os usuários internos consomem. As épicas horizontais (Fundações, MuleSoft) fecham o documento.

### Migração de Catálogos e APIs (E05)

**Contexto de negócio:** os portais não têm valor no go-live sem os catálogos e as APIs carregados — um Portal Governança ou Parceiros vazio não opera. O grill de 2026-08-04 fixou a migração na Fase 1, entregue pela Salesforce PS.

**Abordagem de solução:** carga inicial *one-off* das dez entidades — Torre, Sigla, Tribu, Squad, Domínio, Subdomínio, API de Negócio, API Técnica, Produto e Versão de Produto — para o modelo de dados que o Portal Governança consome, com de-para de campos e reconciliação pós-carga.

**Arquitetura de suporte:** a ordem de carga preserva a integridade referencial entre as dez entidades (organizacionais primeiro, depois ciclo de vida, com a junção API Técnica × Versão de Produto por último). A fonte legada não está nomeada e volumes/qualidade são desconhecidos, o que mantém esta épica *Assumed*. `[assumption: sistema de origem, volumes e qualidade dos dados legados desconhecidos — G0503/G0504]` `[assumption: estratégia de cutover/rollback em produção viva a definir — G0506]` A fronteira entre esta carga one-off e a batch de ETL recorrente do E06 precisa ser delimitada para não contar o mesmo trabalho duas vezes. `[assumption: migração one-off (E05) vs. sincronização recorrente (E06) — evitar dupla contagem — G0509/G0505/G0608]`

### Portal Governança (E01)

**Contexto de negócio:** o BV precisa de um ciclo de vida de API governado — cadastrar uma API de Negócio, gerar e anexar a API Técnica, validar o contrato, aprovar, versionar e publicar — hoje disperso entre planilhas, Jira e o Apigee.

**Abordagem de solução:** portal Experience Cloud com cadastro de API de Negócio, geração da API Técnica por **Wizard** (guia o usuário pelas etapas de geração, anexo de contrato, validação e envio — incluído na Fase 1 por decisão do grill, ~160h), **validação de contrato via OPA com o resultado renderizado em HTML** (a tela de decisão do gestor — 60h, Fase 1), e **aprovação por Flow + Approval Process** com fechamento automático após três rejeições.

**Arquitetura de suporte:** o mecanismo de aprovação combina um Flow que orquestra o envio, histórico e notificação com o Approval Process nativo para aprovar/rejeitar/reatribuir. `[extends: KA-13258 — padrão de Flow + Approval Process coordenados em portal self-service; aplicado aqui ao fluxo de aprovação de API Técnica]` `[KB: experience_cloud_4-2-2026.md:27155-27318]` O modelo de dados são os catálogos das dez entidades com relações hierárquicas (versões Major/Minor) e uma junção API Técnica × Versão de Produto — o objeto "Revisão de API" pode ser substituído pelo próprio Approval Process, decisão de modelo ainda aberta. `[KB: experience_cloud_4-2-2026.md:27656-27752]` As integrações de saída (validar OPA, YAML→HTML do Anypoint, OneTrust, ServiceNow, PortalTech, Jira/CASP) **consomem as XAPIs segregadas do E06**, o que impõe sequenciamento E06→E01 e contratos de API acordados. `[assumption: contratos de XAPI e sequência E06→E01 a acordar; horas Salesforce do E01 pressupõem XAPIs prontas — G0103]`

### Portal Parceiros (E02)

**Contexto de negócio:** desenvolvedores e parceiros externos precisam descobrir APIs, registrar-se, criar aplicações e gerir credenciais em autoatendimento — hoje no portal Apigee incumbente (developers.bvopen.com.br).

**Abordagem de solução:** portal externo Experience Cloud com autorregistro de visitante, **login diferenciado** (senha para acesso básico, IdP para parceiro via Login Discovery), catálogo de APIs público/privado, criação de apps e gestão de credenciais, contratos por versão de produto e **páginas LWC aprimoradas** (Soluções, Como começar, Ajuda, Seja Um Parceiro — incluídas na Fase 1 por decisão do grill, ~32h). As páginas de conteúdo carregam o enablement de parceiros que o BV usará em vez de um programa de treinamento externo separado (grill G0408).

**Arquitetura de suporte:** o modelo de dados adiciona Produto, Versão de Produto e a junção de acesso de parceiro; a automação de compartilhamento dispara na criação do acesso (herda o modelo público/privado das Fundações). `[KB: experience_cloud_4-2-2026.md:63605-63737]` `[KB: experience_cloud_4-2-2026.md:31202-31329]` Criação de app, geração/renovação de credenciais e navegação do esquema OAS **consomem SAPIs do E06** (Apigee Apps Management, Jira, Anypoint OAS). `[assumption: SAPIs do E06 confirmadas e contratadas; limitação do Anypoint pode restringir OAS/credenciais — G0206]` Esta épica ativa o bloqueador de licença EC externa (R1/ADR 0002) e a relação com o portal Apigee incumbente — substituição, coexistência ou migração de parceiros/apps — está em aberto. `[assumption: relação com o portal Apigee incumbente e migração de credenciais — G0204]` `[assumption: consentimento LGPD no autorregistro e integração OneTrust — G0203]`

### Portal Parceiros Interno (E03)

**Contexto de negócio:** funcionários internos do BV precisam de um portal equivalente ao de parceiros, mas com público, personas, tipo de licença, visibilidade e segurança próprios.

**Abordagem de solução:** **build distinto** (decisão do grill 2026-08-04), não uma configuração derivada leve do E02. Reaproveita a base de componentes e o modelo de dados onde faz sentido, mas tem desenho próprio de acesso, sharing e personas internas.

**Arquitetura de suporte:** o tipo de licença dos usuários internos (Employee/usuário interno Salesforce vs. Partner Community do E02) e a contagem não estão definidos, o que bloqueia o sizing de licença e abre um segundo caminho de licenciamento distinto do R1 externo. `[assumption: tipo e contagem de licença interna — Employee Community/usuário interno/outro — G0307/G0303]` `[KB: experience_cloud_4-2-2026.md:2249-2352]` A épica é sequenciada **após o congelamento (freeze) da configuração do E02** para não cascatear retrabalho. `[assumption: freeze de E02 antes de derivar E03; itens exclusivos do interno vs. cópia real — G0302/G0304]`

### Fundações & Segurança Transversal (E04)

**Contexto de negócio:** base técnica compartilhada pelos três portais — sem ela, nenhuma capacidade adiante se sustenta.

**Abordagem de solução:** org de produção e ambientes de desenvolvimento, perfis e permission sets core, connected apps e usuário de integração para DevOps, integrações de entrada ao Salesforce, e frameworks de trigger, logging e mocking, além da parametrização de configuração administrativa. `[KB: experience_cloud_4-2-2026.md:30835-30862]` `[KB: experience_cloud_4-2-2026.md:63739-63834]`

**Arquitetura de suporte:** o framework de logging captura request/response de callouts e, em contexto de banco, precisa de mascaramento de PII e política de retenção — mais do que um logging básico. `[assumption: logging nível FS com mascaramento/retenção — G0406]` O teste de **não-regressão dos três portais em produção** vive nesta épica como atividade contínua; alterar fundações transversais (permission sets core, trigger framework) pode quebrar comportamento existente. `[assumption: cobertura, ambientes e critérios de não-regressão a definir — G0401]`

### Camada de Integração MuleSoft (E06)

**Contexto de negócio:** toda a comunicação entre os portais Salesforce e os sistemas de destino (OPA, OneTrust, ServiceNow, PortalTech, Jira, Anypoint) passa por esta camada; sem ela, os fluxos de governança e de parceiros não fecham ponta a ponta.

**Abordagem de solução:** camada API-led com TLS context de entrada/saída no Apigee, **XAPIs segregadas** por sistema de destino mais uma XAPI de retorno, **SAPIs** (Jira CRUD/login, Apigee Apps Management, Anypoint OAS), uma app batch de ETL e testes E2E. Base de estimativa fixada em **319h** pelo grill; entregue pela prática MuleSoft da Salesforce PS. `[KB: MuleSoft — Catálogo Estratégico Consolidado (EN) (Claude).md:53-88]`

**Arquitetura de suporte:** esta é a épica horizontal que o E01 e o E02 consomem — os contratos de XAPI/SAPI são a interface que sequencia toda a trilha. `[extends: KA-0441 — as XAPIs de consumo e SAPIs seguem a segregação de camadas]` A arquitetura de integração (papel de Technical Architect, ~220h na tabela de perfis do ROM) pode estar dentro ou fora das 319h de base — resíduo aberto que, se não estiver em nenhuma épica, subdimensiona a entrega. `[assumption: arquitetura de integração dentro das 319h ou separada — G0610]` NFRs de Open Finance (mTLS, throughput, idempotência, retry/dead-letter) e a caracterização da limitação do Anypoint permanecem em aberto e mantêm a épica *Assumed*. `[assumption: NFRs FS/Open Finance e resiliência da camada — G0605/G0606]` `[assumption: limitação do Anypoint — R2/G0602]`

---

## Atividades transversais PS (roster, não build)

Duas atividades implícitas não são épicas de build e serão autoradas como linhas do roster no `estimate` (G0611):

- **Gestão de entrega/programa** — coordena as três trilhas (EC, MuleSoft, migração) de um programa multi-trilha em serviços financeiros.
- **QA/testes dedicado** — QA funcional dos três portais + teste de aceitação do fluxo de aprovação OPA.

O BV conduz **release e UAT** (não entra no roster PS). A gestão de mudança e o treinamento são do BV; a PS entrega o enablement embutido nas páginas de conteúdo do E02 (grill G0408) — risco de adoção fraca se o BV não conduzir a mudança.

---

*Fontes: `data/epics.json`, `data/gaps.json`, ADRs 0001/0002, decisões do grill 2026-08-04 (`data/memory.json`), knowledge/ (Experience Cloud, MuleSoft Catálogo), central Salesforce KB (KA-10297/10398/10395 sharing, KA-13258 aprovação, KA-0441/0042 API-led).*
