Plataforma de Originação de Crédito · Salesforce

Relatório Fit / Gap
Financial Services Cloud

Capacidades nativas do FSC × uso real no org

Projeto: Desenvolve SP (Agentic Delivery Platform)

Orgs analisados: desenvolvesp-hml (Sandbox · 00DHZ000007P1mn2AC) + desenvolvesp-prod (Produção · Unlimited
· 00Das000005XO3tEAG, veriﬁcação de licença)

Fonte: Org ao vivo (sf CLI) + metadados versionados + governança arquitetural do projeto

Data: 25/06/2026  ·  Classiﬁcação: Interno — sensível

Sumário Executivo

Para liderança técnica e de negócio

Este relatório compara as capacidades nativas do Financial Services Cloud (FSC) com o que a Desenvolve SP de fato utiliza. O achado
central é uma divergência clara: o org tem o modelo de dados de lending do FSC totalmente provisionado, mas a jornada de crédito foi

construída sobre objetos standard do core + objetos customizados, deixando as capacidades de lending do FSC sem adoção.

Matriz Fit / Gap por capacidade FSC

Capacidade FSC

Status

Adoção

Implicação

Modelo de dados de Lending

GAP

ResidentialLoanApplication,

LoanApplicant +

Income/Employment/Liability/Asset

Não adotado. Jornada roda em
Lead → Opportunity + customs.

Capacidade paga, não adotada. Custom

( CreditApplication__c ,  Simulacao__c )

cobre o mesmo domínio.

Account/Contact + Relationships

FIT

Adotado.

Núcleo de partes adotado. Person Accounts
desabilitado.

Financial Goals

GAP

Não adotado.

Fora de escopo da jornada atual — gap esperado,

baixa prioridade.

Product / Pricing (Product2,
PricebookEntry)

PARCIAL

Standard adotado, fortemente
estendido com campos

Forte extensão custom sobre standard — funciona,
mas diverge de produtos FSC.

custom.

Business Milestones

GAP

Não adotado; telemetria de

Capacidade de marcos substituída por solução

etapa via  Metrica__c .

custom (alinhada ao modelo de integração do

projeto).

Actionable Relationship Center /

GAP

Não adotado.

Oportunidade futura para estruturação de

Action Plans

documentos/garantias.

Risco-chave: a jornada de crédito (núcleo do produto) está modelada fora do modelo de lending do FSC. Isso signiﬁca licença

FSC paga com baixo aproveitamento das capacidades de originação e débito técnico de divergência frente ao princípio de
priorizar o padrão da plataforma.

Nuance importante: parte dessa divergência é decisão arquitetural deliberada e registrada, não acidente. O princípio de priorizar
o padrão convive com objetos custom legítimos (catálogo de crédito, enquadramento, instituições), e a simulação atual já está

marcada como débito técnico a desativar. O gap real está em não ter migrado para o modelo de crédito nativo do FSC onde ele
se aplicaria.

Product Catalog Management (PCM / EPC)

Modelagem de produto e elegibilidade declarativa nativas

As capacidades nativas de catálogo de produtos (EPC/PCM) e de regras de negócio (Business Rules Engine) estão disponíveis e
licenciadas, porém não adotadas — o domínio de produto e elegibilidade é hoje modelado em objetos custom sobre  Product2  e

Enquadramento__c . Há um encaixe forte para migrar para o modelo nativo, e a decisão já está formalmente registrada (em proposta)
na governança do projeto: produto → PCM; elegibilidade → DecisionTable;  Instituicao__c  → Account.

PCM

✓

DISPONÍVEL E NÃO ADOTADO

LICENCIADO (PRODUÇÃO)

✓

DECISÃO REGISTRADA (EM
PROPOSTA)

Mapeamento custom → destino nativo (escopo reﬁnado)

Objeto / conceito atual

Destino nativo

Veredito

Nota

Product2 (estendido) +

PCM:  ProductClassification  +

FIT FORTE

Caso de uso canônico do PCM. Os campos

EnquadramentoProduto__c

AttributeDefinition  +

custom viram atributos classiﬁcados.

AttributeCategory  +

ProductSellingModel

Enquadramento__c  (framing de
elegibilidade c/ janela de validade)

BRE:  DecisionTable  (matriz
faturamento × porte) —

FIT

ExpressionSet  evitado por ora

Elegibilidade declarativa nativa.
DecisionTable escolhida sobre

ExpressionSet para preservar a

rastreabilidade do código em revisão. A

matriz de faturamento já existente é o caso
de manual para DecisionTable.

Instituicao__c  (instituição

Account — Record Type "Instituição

FIT

Hoje duplica a semântica de Account.

ﬁnanceira interna, chave Sinqia)

Financeira" (Business Account). NÃO

Household modela núcleo de pessoas, não

household.

instituição. Migração leve.

Metrica__c  (telemetria de

— (custom mantido)

KEEP

Observabilidade do processo. Sem

etapa)

equivalente standard — decisão conﬁrmada.

Simulação / cronograma de

amortização

OpportunityLineItem + payload de
evento → Sinqia via MuleSoft

JÁ DECIDIDO

PCM não calcula amortização. Cálculo

permanece na integração com o core
bancário (via MuleSoft).

O que o PCM cobre e o que não cobre: PCM/EPC é nativo para modelagem de produto + elegibilidade declarativa (linhas 1–2).
NÃO é catálogo: instituição é parte/conta (→ Account), métrica é observabilidade (→ custom), e amortização é cálculo de
integração (→ Sinqia). Tratar esses três "via PCM" seria erro de categoria.

Existe ferramenta de projeto que cobriria a implementação caso a adoção seja aprovada. A decisão está formalmente registrada (em proposta) na governança do

projeto.

Estimativa de Esforço — Adoção do FSC Nativo

Esforço adicional para migrar do modelo custom para as capacidades nativas — ordem de magnitude (ROM) para

planejamento, não compromisso de cronograma.

Esforço por frente de adoção

Frente

Esforço

Sprints (ROM)

Risco

Drivers de esforço

Modelo de produto → PCM

Alto

2–3 sprints

Alto

Catálogo de produtos e campos custom de Product2 re-

modelados como ProductClassiﬁcation + AttributeDeﬁnition;

migração de dados + re-vínculo de referências (LWC do

simulador, controllers).

Elegibilidade →
DecisionTable

Médio

1–2 sprints

Médio

Matriz faturamento×porte + enquadramento viram

DecisionTable. Esforço dominado por aprendizado do motor de

regras, não por volume.

Instituição → Account

Baixo

0,5–1 sprint

Baixo

Record Type + migração da chave do core bancário; refatorar

referências. Volume baixo, padrão conhecido.

Modelo de crédito nativo do

Alto

3–5 sprints

Alto

Adotar o modelo de originação nativo (hoje não adotado) na

FSC

jornada; decisão arquitetural ampla, possivelmente ligada ao

Digital Lending. Maior incerteza.

Pipeline / governança de

Médio

1–2 sprints

Médio

Pipeline atual é centrado em código; as novas conﬁgurações

metadados novos

exigem passos próprios de build, teste e revisão (gap já

identiﬁcado).

Regressão (sem regressão)

Médio

1 sprint (+

contínuo)

Médio

Ambiente em produção — simulador atual deve seguir

funcionando até o corte. Caderno de testes automatizados

cobre isso.

Total (ROM)

—

≈ 8–14 sprints

—

Faixa consolidada, com sobreposição parcial entre frentes.

Inclui o modelo de crédito nativo; sem essa frente, ≈ 5–9
sprints.

Premissas: sprint de 2 semanas, squad dedicado (3–5 pessoas) já com domínio de FSC/Industries; as faixas pressupõem
sobreposição parcial entre frentes e excluem ramp-up — sem experiência prévia, aplicar multiplicador de 1,3–1,8.

Sequência recomendada (menor risco primeiro): (1) Instituição → Account; (2) Elegibilidade → DecisionTable; (3) veriﬁcar Digital
Lending; (4) Produto → PCM; (5) modelo de crédito nativo do FSC.

Pré-requisitos para comprometer cronograma: fechar as ações abertas da decisão registrada (conﬁrmação contratual da
licença e veriﬁcação do Digital Lending) e rodar a estimativa formal sobre o backlog para converter estas faixas em Story Points

e horas-equipe.

Licenciamento

Veriﬁcação ao vivo — Permission Set Licenses no org de produção

Esta seção consolida a veriﬁcação de licenciamento que fundamentou a decisão de adoção. A pergunta original era se as capacidades
nativas (FSC lending, EPC/PCM, Business Rules Engine) exigiriam add-on — o que o "No Add-on Policy" do projeto excluiria. A

veriﬁcação foi feita ao vivo no org de produção ( Desenvolve SP ,  00Das000005XO3tEAG , BRA36, Unlimited Edition) via  sf data
query  sobre  PermissionSetLicense .

Conclusão: o caminho nativo de catálogo + elegibilidade já está licenciado na baseline — não requer compra de add-on. Isso
reconcilia o "No Add-on Policy" do HIGH-LEVEL-E2E, que foi atualizado para refletir as licenças Industries ativas.

Licenças relevantes — Active em produção

Permission Set License

Seats (prod)

Status

Habilita

Business Rules Engine Designer / Runtime

100 / 100

BRE Runtime for Communities

52.000

Product Catalog Management Admin / Viewer

2.150 / 4.100

Context Service Admin / Runtime

2.100 / 4.100

Salesforce Pricing Design Time / Run Time

50 / 50

Decision Explainer

Digital Lending

50

50

Active

Active

Active

Active

Active

Active

Active

DecisionTable, ExpressionSet — motor de elegibilidade

Regras no contexto guest/Community (simulador

público)

EPC/PCM — modelagem de produto e atributos

Base de dados de entrada da BRE

Preciﬁcação nativa de produto

Explicabilidade/auditoria de decisões de regra

Produto FSC de originação de crédito (capacidades não

veriﬁcadas)

Financial Services Cloud Standard / Extension

50 / 50

Active

Modelo de dados FSC, lending

FSC for Customer Community / Login

2.000 / 50.000

Active

Acesso FSC na Experience Cloud

Uniﬁed Catalog Admin / Agent / Community

2.050 / 2.050 /

Active

Catálogo uniﬁcado

2.000

Ação aberta: seats  Active  num org conﬁrmam disponibilidade técnica, mas não substituem a conﬁrmação contratual com o
time de licenciamento de que essas licenças Industries são permanentes na baseline — não um provisionamento transitório.

Recomenda-se validar antes de comprometer roadmap.

Anexo Técnico

Inventário objeto a objeto — fonte: org desenvolvesp-hml ao vivo

A. Modelo de dados de Lending do FSC (provisionado × usado)

Objeto FSC standard

Registros

Status

Equivalente custom em uso

ResidentialLoanApplication

LoanApplicant

LoanApplicantIncome

LoanApplicantEmployment

LoanApplicantLiability

LoanApplicantAsset

FinancialGoal

BusinessMilestone

0

0

0

0

0

0

0

0

GAP

GAP

GAP

GAP

GAP

GAP

GAP

GAP

CreditApplication__c  (68)

Lead (10.105) + Contact

Campos em Lead/custom

Campos em Lead/custom

—

Garantia__c  (0)

Fora de escopo

Metrica__c  (262)

Nota: o pacote gerenciado legado  FinServ__  NÃO está instalado (0 objetos / 0 classes Apex no namespace). O org usa o modelo de dados FSC nativo (sem

namespace) da plataforma, o que é o padrão atual.

B. Objetos do core standard que carregam a jornada (FIT, estendidos)

Objeto

Lead

Account

Contact

Opportunity

OpportunityLineItem

Product2

Registros

10.105

311

205

157

69

134

Campos

custom

56

150

4

12

0

117

Record Types

Papel na jornada

3

3

0

1

0

2

Captação — entrada (HIGH-LEVEL-CORE)

Tomadores PF/PJ e cooperativas

Pessoas / cooperados

Operação de crédito pós-captura

Linhas da operação (futuro lar da simulação)

Produtos de crédito

Observação de extensão: 150 campos custom em Account e 117 em Product2 indicam forte modelagem própria sobre objetos
standard. É funcional e legítimo num brownﬁeld, mas aumenta o custo de eventual adoção do modelo FSC e merece revisão de

equivalência.

Anexo Técnico (continuação)

C. Custom objects do domínio de crédito (uso atual)

Objeto custom

Registros

Veredito governança

Observação

Simulacao__c

381

DESATIVAR

Superseded por OpportunityLineItem + evento (HIGH-LEVEL-

CORE)

Parcela__c

14.356

DESATIVAR

Cronograma viaja no payload do evento de avanço

CreditApplication__c

Enquadramento__c

EnquadramentoProduto__c

Instituicao__c

Metrica__c

AntiFraudAnalysis__c

Garantia__c

68

3

32

25

262

90

0

REVISAR

Candidato a ResidentialLoanApplication FSC

→ DecisionTable

Elegibilidade migra para Business Rules Engine

→ PCM

Vínculo produto ↔ elegibilidade migra para catálogo nativo

→ Account

Chaveado ao Sinqia; vira Account Record Type

MANTER

MANTER

REVISAR

Telemetria de etapa do processo

Resultado antifraude (fora do escopo FSC)

Candidato a LoanApplicantAsset / collateral FSC

Custom objects de pacotes gerenciados ( et4ae5__  Marketing Cloud,  omnistudio__ ,  sf_devops__ ,  usf3__ ) foram excluídos deste recorte — não
fazem parte do domínio de crédito.


