**USD - UNIFIED SCOPING DOCUMENT V2.0**

**Preâmbulo: Guia de Uso e Estrutura de Dimensionamento V2.0**

**Propósito do Documento**

Este compêndio serve como a ferramenta padrão e unificada para executar a fase de descoberta em todos os projetos da Salesforce.

Seu objetivo principal é padronizar a coleta de requisitos, facilitar estimativas de esforço precisas e servir como o artefato de entrada principal para os planos de negócios unificados (Unified Business Blueprints).

**Metodologia de Uso V2.0**

Paso 1: Descoberta (Entrada). Usar as Partes 2, 3 e 4 (o banco de perguntas da V1) como agenda principal para os workshops com o cliente.

Completar as respostas nas tabelas correspondentes utilizando o prompt de IA fornecido para cada seção, que inclui a instrução de consultar o arquivo Guided Scoping Questions e preencher a coluna Resposta / Observações do Cliente e Dimensionamento (S-XL-SC).

Paso 2: Análise (Saída). Utilizar uma IA generativa para processar as respostas do Passo 1 e qualquer documento do cliente (RFPs, análises estratégicas).

Paso 3: Geração (Saída). A IA utilizará os prompts da Parte 1 (Catálogo) e as Partes 5 a 9 para gerar o catálogo de requisitos, o mapeamento da solução, a análise de lacunas e a estimativa preliminar.

**Estrutura de Dimensionamento V2.0 (Sizing Framework)**

Adota-se a estrutura de dimensionamento completa para uma estimativa consistente.

**Tabela 0.1: Definições da Estrutura de Dimensionamento (Qualitativo)**

| **Nível** | **Descrição Geral** | **Impulsionadores Típicos** |
| --- | --- | --- |
| Small (S) | Configuração Out-of-the-Box (OOTB) com mínima personalização de layouts e campos. Aproveita as funcionalidades padrão sem necessidade de automação complexa. | 1-2 processos de negócios simples e lineares, < 3 roles de usuário distintos, sem integrações ou integrações plug-and-play da AppExchange , migração de dados de 1-2 fontes com limpeza mínima. |
| Medium (M) | Configuração avançada utilizando ferramentas declarativas como Flows para automatizar processos. Inclui personalização da experiência do usuário e relatórios complexos. | Múltiplos processos de negócios inter-relacionados, 3-5 roles de usuário com diferentes requisitos de visibilidade, 1-2 integrações point-to-point (baseadas em API), dashboards com múltiplas fontes de dados, uso de aplicativos da AppExchange que requerem configuração. |
| Large (L) | Implementação que envolve múltiplas nuvens da Salesforce, personalização complexa e um número significativo de integrações orquestradas. | Processos de negócios que abrangem múltiplos departamentos ou unidades de negócios, automação com lógica condicional complexa, 3-5 integrações que requerem middleware (como MuleSoft ou um ESB existente), migração de dados de múltiplos sistemas com transformações complexas. |
| Extra Large (XL) | Projetos de transformação de negócios em grande escala que envolvem a reengenharia de processos-chave e uma arquitetura de sistemas complexa. | Múltiplas nuvens e soluções de indústria, alto grau de personalização, mais de 5 integrações complexas (com ERP , sistemas legados, data warehouses ), grandes volumes de dados (>10M registros), governança de dados avançada e requisitos de segurança. |
| Super Custom (SC) | Requisitos de negócios únicos que excedem as capacidades padrão e declarativas da plataforma, exigindo um desenvolvimento personalizado extenso. | Lógica de negócios muito específica que requer desenvolvimento Apex ( Triggers , serviços complexos), componentes de interface de usuário personalizados ( LWC ), algoritmos complexos (ex., preços, comissões), integrações com sistemas proprietários ou não padrão. |

**Tabela 0.2: Métricas Quantitativas de Dimensionamento**

| **Métrica** | **Small (S)** | **Medium (M)** | **Large (L)** | **Extra Large (XL)** | **Super Custom (SC)** |
| --- | --- | --- | --- | --- | --- |
| # de Nuvens Salesforce | 1 | 2 | 3 | 4 | 5+ |
| # de Integrações | 0-10 | 10-20 | 20-30 | 30-50 | 50+ |
| Complexidade de Dados | Modelo padrão, <5 objetos custom, <100k registros a migrar. | Modelo estendido, 5-15 objetos custom, 100k-1M registros. | Modelo complexo, >15 objetos custom, >1M registros, requer limpeza. | Múltiplas fontes, > 30 objetos custom, requer MDM, >3M registros. | Múltiplas fontes, >50 objetos custom, requer MDM, >10M registros. |
| Nível de Personalização | Principalmente configuração, <5 flows complexos. | Flows complexos, <5 componentes LWC/Apex. | Lógica de negócios complexa em Apex, <10 componentes LWC/Apex. Integrações personalizadas. | Arquitetura personalizada, múltiplos componentes Apex complexos. <20 componentes LWC/Apex. | Arquitetura personalizada, múltiplos componentes Apex complexos. <30 componentes LWC/Apex. |
| # de Papéis de Usuário | <3 | 3-5 | 6-10 | 10 - 20 | <20 |
| Impacto Organizacional | 1 departamento, <50 usuários. | Múltiplos departamentos, 50-250 usuários. | Impacto em toda a unidade de negócios, 250-1000 usuários. | Transformação em 2 a 3 unidades de negócios empresariais, >1000 usuários. | Transformação em nível empresarial, >1000 usuários. |

# Parte 1: Catálogo de Requisitos do Cliente

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Analisar a fundo unicamente os documentos fornecidos pelo cliente (ex. RFP, Análise Estratégica, notas de workshop).

Seu objetivo é inferir, identificar, listar e categorizar TODOS os requisitos do cliente. Esta é a primeira etapa de geração;

não deve depender das Partes 2, 3 ou 4.

Instruções:

Extração e Nomeação: Identificar cada requisito e atribuir-lhe um ID único no formato REQ-[Category]-[###] (ex. REQ-BIZ-001).

Categorização: Classificar cada requisito em uma das seguintes categorias: Negócios (BIZ), Processo (PRO), Tecnologia (TEC), Integração (INT), Dados (DAT), Segurança (SEC), Governança (GOV), Implementação (IMP), Restrições (CON).

Descrição e Fonte: Fornecer uma descrição clara e concisa, e citar o documento e a seção fonte para manter a rastreabilidade (ex. "RFP p.3").

Formato de Saída: Apresentar os resultados exclusivamente em uma tabela Markdown.

| **Id do Requisito** | **Categoria** | **Descrição do Requisito** | **Origem** |
| --- | --- | --- | --- |
| REQ-XXX-001 | [Categoria] | ... | ... |
| ... | ... | ... | ... |

# Parte 2: Questionário Fundamental e Estratégico (Multi-Cloud)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Analisar em profundidade todos os documentos fornecidos pelo cliente (ex. RFPs, documentos de visão estratégica, análises "As-Is") e o banco de perguntas Guided Scoping Questions.pdf.

Instruções:

Análise de Requisitos (Fonte): Analisar os documentos do cliente para entender os requisitos fundamentais.

Análise do Banco de Perguntas: Analisar o arquivo Guided Scoping Questions.pdf para identificar perguntas fundamentais adicionais.

Preenchimento do Modelo: a. Para cada Question ID já presente nas tabelas da Parte 2, localizar a informação nos documentos fonte do cliente que responda à Discovery Question.

b. Se a análise do Guided Scoping Questions.pdf (Passo 2) revelou perguntas fundamentais relevantes que não estão no modelo, adicioná-las como novas linhas na subseção apropriada.

Localizar e Preencher: Para cada linha (original ou adicionada), preencher a coluna Resposta / Observações do Cliente com um resumo conciso dos achados, citando a fonte (ex. "RFP p.3").

Lacunas: Se a informação não for encontrada, marcar a resposta como "Não detalhado nos documentos".

(Esta marca é uma entrada crucial para a Parte 8).

Avaliação: Com base na resposta e no guia de dimensionamento, preencher Impacto / Prioridade (ex. Alta, Média, Baixa). 1

Dimensionamento: Usando a Tabela 0.1 (Sizing Framework) e a coluna Sizing Guidance and Complexity Drivers, atribuir um Dimensionamento (S-XL-SC) preliminar para a complexidade desse requisito específico.

Formato de Saída: Apresentar os resultados preenchendo (e adicionando linhas, se necessário) as tabelas Markdown desta seção.

A coluna Sizing Guidance and Complexity Drivers é fixa do modelo e não deve ser modificada pela IA.

## 2.1. Contexto de Negócios e Visão Estratégica

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| G-BIZ-001 | Descreva a estrutura da sua organização em alto nível (linhas de negócios, divisões, territórios, hierarquia organizacional, etc.). A operação abrange múltiplas regiões, moedas ou idiomas? 1 | S: Uma única linha de negócios, uma geografia, uma moeda, um idioma. M: Múltiplas equipes ou divisões dentro da mesma geografia e linha de negócios. L: Múltiplas linhas de negócios ou geografias com processos de negócios majoritariamente padronizados. XL: Estrutura matricial complexa, operações em múltiplas geografias com requisitos regulatórios e de negócios distintos, múltiplas moedas e idiomas. SC: Requisitos de consolidação financeira ou relatórios multimoeda que excedem as capacidades padrão do Salesforce. |  |  |  |
| G-BIZ-002 | Quais são as métricas mais importantes (KPIs) para sua organização (ex. Vendas, Atendimento, Marketing)? Quais dessas métricas vocês tentam melhorar com este projeto? 1 | S: O objetivo é melhorar 1-2 métricas operacionais básicas (ex. número de casos fechados). M: O objetivo é melhorar métricas de eficiência em um departamento (ex. reduzir o ciclo de vendas). L: O projeto busca impactar KPIs estratégicos que abrangem múltiplos departamentos (ex. Valor de Vida do Cliente). XL: O projeto é uma iniciativa de transformação com KPIs em nível executivo (ex. aumentar a participação de mercado, reduzir o churn em X%). SC: São necessários modelos preditivos e de medição personalizados para calcular KPIs complexos. |  |  |  |
| G-BIZ-003 | Quais são os três principais "pontos problemáticos" (pain points) que este projeto busca resolver? Qual é o impacto quantificável desses problemas hoje (em termos de receita perdida, custos operacionais, etc.)? | S: Pontos problemáticos operacionais e localizados (ex. "a entrada de dados é manual e lenta"). M: Problemas de eficiência que afetam uma equipe inteira (ex. "nossos agentes de vendas não têm uma visão 360 do cliente"). L: Pontos problemáticos sistêmicos que causam atrito entre departamentos (ex. "vendas vende coisas que operações não pode entregar"). XL: Problemas estratégicos que limitam o crescimento ou a competitividade da empresa (ex. "não conseguimos lançar novos produtos no mercado rápido o suficiente"). SC: O problema raiz é tão complexo ou desconhecido que é necessária uma fase de consultoria estratégica e análise de processos antes de definir a solução. |  |  |  |
| G-BIZ-004 | Descreva os principais tipos de usuários (personas) que trabalharão com o novo sistema. Para cada um, descreva um "dia na vida", suas motivações, tarefas principais e frustrações atuais. | S: 1-2 personas com papéis e tarefas bem definidas (ex. Representante de Vendas, Agente de Atendimento). M: 3-5 personas, incluindo papéis de gestão (ex. Gerente de Vendas). L: Múltiplas personas através de diferentes departamentos, incluindo papéis de operações e análise. XL: Inclui usuários externos (parceiros, clientes) e papéis executivos com necessidades de dashboards consolidados. SC: Os papéis de usuário são fluidos ou exigem uma experiência de usuário altamente personalizada e dinâmica que não pode ser alcançada com layouts padrão. |  |  |  |
| G-BIZ-005 | Como vocês avaliam sua maturidade digital e posição no mercado em comparação com seus concorrentes? | S: O cliente está começando sua transformação digital, buscando automatizar processos manuais básicos. M: O cliente possui sistemas digitais, mas estão isolados (em silos); buscam uma plataforma unificada. L: O cliente busca otimizar seus processos digitais existentes e começar a usar dados para a tomada de decisões. XL: O cliente aspira ser um líder digital em sua indústria, explorando capacidades avançadas como IA, personalização em tempo real e experiências omnichannel. SC: O cliente busca criar um modelo de negócios disruptivo ou uma plataforma digital que redefine sua indústria. |  |  |  |

## 2.2. Governança do Projeto e Metodologia

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| G-GOV-001 | Qual é a estrutura de governança do projeto? Quem é o Dono do Negócio (executive sponsor)? Quem assumirá o papel de Product Owner? Como são gerenciados o orçamento e a priorização? | S: Papéis claros e definidos, com um único Product Owner com poder de decisão. M: Um comitê diretivo toma decisões, mas há um Product Owner designado. L: Estrutura de governança de programa com múltiplos Product Owners por fluxo de trabalho que devem se alinhar. XL: Governança complexa envolvendo múltiplas unidades de negócios, geografias e stakeholders com prioridades potencialmente conflitantes. SC: Não existe uma estrutura de governança clara, ou o poder de decisão está altamente fragmentado. Isso representa um risco significativo e aumenta a complexidade da gestão do projeto. |  |  |  |
| G-GOV-002 | Que metodologia de gerenciamento de projetos vocês utilizam (ex. Agile, Scrum, SAFe, Waterfall)? Qual é o nível de maturidade da organização com essa metodologia? | S: O cliente está familiarizado e opera consistentemente com uma metodologia ágil padrão (Scrum). M: O cliente usa uma abordagem híbrida ou está em transição para o Ágil. L: O cliente opera dentro de um framework de Ágil escalado como SAFe, o que requer uma coorderação mais complexa de dependências e lançamentos. XL: Múltiplas equipes operam com metodologias diferentes, exigindo um esforço significativo de alinhamento e gerenciamento de integração. SC: Não há metodologia formal ou consistente, exigindo que a equipe de implementação estabeleça e guie o processo desde o início. |  |  |  |
| G-GOV-003 | Como vocês gerenciam seus ambientes Salesforce (sandboxes)? Qual é a sua estratégia de implantação (conjuntos de alterações / change sets, ferramentas DevOps)? Como são gerenciadas as dependências e conflitos entre diferentes equipes de desenvolvimento? | S: Um único fluxo de implantação de Desenvolvimento para Produção usando conjuntos de alterações (change sets). M: Múltiplas sandboxes de desenvolvimento e uma sandbox de UAT. Uso de conjuntos de alterações (change sets). L: Uma estratégia de ambientes definida (ex. Dev, QA, UAT, Staging), uso de ferramentas DevOps (ex. Copado, Gearset) para CI/CD. XL: Múltiplos projetos paralelos com equipes de desenvolvimento separadas, exigindo uma estratégia sofisticada de ramificação (branching) e versionamento de metadados. SC: Não há estratégia de gerenciamento de ambientes ou implantações, ou os ambientes estão dessincronizados e instáveis. |  |  |  |
| G-GOV-004 | Existem outros projetos de tecnologia importantes sendo executados em paralelo a esta iniciativa? Há dependências ou conflitos de recursos potenciais? | S: Este é o único projeto de tecnologia importante em andamento. M: Há 1-2 projetos adicionais com dependências mínimas. L: Há múltiplos projetos paralelos com dependências conhecidas que devem ser gerenciadas (ex. um projeto de ERP do qual dependemos para os dados de clientes). XL: O projeto faz parte de um programa de transformação massivo com múltiplas interdependências críticas e recursos compartilhados. SC: As dependências com outros projetos são críticas e estão em estado de alto risco ou incerteza. |  |  |  |

## 2.3. Gestão da Mudança e Adoção

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| G-CHG-001 | Foi realizada uma análise da capacidade e preparação da organização para a mudança? Quem liderará a iniciativa de gestão da mudança? | S: A organização tem experiência prévia com mudanças similares e mostra alta preparação. Um líder de mudança é designado. M: Focos de resistência são identificados, mas existe um plano para gerenciá-los. L: A cultura organizacional é resistente à mudança, ou a mudança impacta um grande número de usuários com rotinas muito arraigadas. XL: O projeto implica uma mudança cultural significativa (ex. passar de uma cultura reativa para uma proativa e impulsionada por dados). SC: A gestão da mudança não foi considerada, ou existe resistência ativa por parte de stakeholders-chave. |  |  |  |
| G-CHG-002 | Qual é a estratégia de comunicação para informar os stakeholders e usuários sobre o porquê, os benefícios e o progresso do projeto? | S: Plano de comunicação básico (ex. e-mails periódicos). M: Plano de comunicação estruturado com diferentes mensagens para diferentes públicos. L: Programa de comunicação multifacetado que inclui roadshows, demos, boletins informativos e a participação de um grupo de "campeões". XL: Estratégia de comunicação de transformação de negócios liderada pela equipe executiva. SC: Não existe um plano de comunicação. |  |  |  |
| G-CHG-003 | Como está planejado o treinamento e o suporte aos usuários durante a transição e após o lançamento? | S: Sessões de treinamento padrão e um guia do usuário. M: Treinamento adaptado por papel de usuário e criação de uma Base de Conhecimento (Knowledge Base). L: Programa de treinamento contínuo, com "horários de expediente", super-usuários designados e materiais de micro-aprendizagem (vídeos, Trailhead). XL: Criação de um centro de excelência ou uma equipe de suporte dedicada pós-lançamento. SC: A solução é tão complexa que requer um programa de certificação interna para os usuários. |  |  |  |

## 2.4. Arquitetura Técnica, Integração e Dados

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| G-TEC-001 | Que sistemas/ferramentas vocês utilizam atualmente para gerenciar seus processos (CRM, ERP, Faturamento, etc.)? Quais serão desativados e quais coexistirão com o Salesforce? Qual será o sistema de registro (fonte da verdade) para os dados-chave (Cliente, Produto, Pedido)? | S: O Salesforce substituirá um único sistema legado ou planilhas. O Salesforce será a fonte da verdade para a maioria dos dados. M: O Salesforce coexistirá com 1-2 sistemas-chave (ex. um ERP), com uma definição clara da fonte da verdade para cada entidade. L: Ecossistema complexo com múltiplos sistemas que devem ser integrados. Definir a fonte da verdade é um desafio e pode variar por campo. XL: Não há definição clara da fonte da verdade, o que requer um projeto de Gerenciamento de Dados Mestres (MDM) como parte da implementação. SC: Múltiplos sistemas afirmam ser a fonte da verdade para a mesma entidade, exigindo uma lógica complexa de reconciliação de dados. |  |  |  |
| G-TEC-002 | Vocês têm uma plataforma de integração (Middleware, ESB, ETL) como o MuleSoft? Seguem uma metodologia de integração específica como conectividade liderada por API (API-led)? | S: Não são necessárias integrações ou serão usados apenas conectores da AppExchange. M: São necessárias 1-2 integrações ponto a ponto (point-to-point) e serão construídas sob medida. L: O cliente possui middleware, mas as integrações são construídas ad-hoc. É necessário definir uma estratégia de integração. XL: O cliente adotou o MuleSoft e uma estratégia API-led. O projeto envolve criar ou consumir APIs de Sistema, Processo e Experiência. SC: O cliente não tem middleware e precisa integrar múltiplos sistemas complexos, o que significa que a implementação do MuleSoft é um pré-requisito ou um fluxo de trabalho principal do projeto. |  |  |  |
| G-TEC-003 | Quais são os requisitos de volume de dados (número de Contas, Contatos, Oportunidades, etc.)? Qual é o volume de transações esperado (ex. casos por dia, pedidos por hora)? | S: Volumes de dados baixos (< 1M de registros por objeto principal), baixo volume de transações. M: Volumes de dados moderados (1-5M de registros). L: Grandes volumes de dados (5-50M de registros), o que requer considerações de desempenho, indexação e estratégias de arquivamento. XL: Volumes de dados massivos (> 50M de registros), que podem exigir o uso de Big Objects e estratégias para gerenciar a distorção de dados (data skew). SC: Requisitos de processamento de transações em grande escala e em tempo real que podem levar ao limite os limites do governador (governor limits) da plataforma. |  |  |  |
| G-TEC-004 | Que padrões de segurança e conformidade regulatória devem ser atendidos (ex. GDPR, CCPA, HIPAA, WCAG)? Existem requisitos de criptografia de dados ou residência de dados? | S: Requisitos de segurança padrão da plataforma. M: Requisitos de conformidade como GDPR/CCPA que impactam o gerenciamento do consentimento e o direito ao esquecimento. L: Requisitos para indústrias reguladas como HIPAA (Saúde) ou PCI (Pagamentos), que exigem o Salesforce Shield e uma configuração de segurança mais rigorosa. XL: Múltiplas regulações globais com requisitos contraditórios, ou requisitos de residência de dados que podem implicar o uso do Hyperforce em uma região específica. SC: Requisitos de segurança personalizados que vão além das certificações padrão do Salesforce e exigem validações e auditorias complexas. |  |  |  |
| G-TEC-005 | Qual é a estratégia de migração de dados? Quem é responsável pela extração, limpeza e transformação de dados? Que objetos e que volume de dados históricos devem ser migrados? | S: Migração de 1-2 objetos a partir de arquivos CSV limpos, realizada pelo cliente com orientação da equipe de implementação. M: Migração de 3-5 objetos principais, com necessidades moderadas de limpeza e transformação de dados. L: Migração de um sistema legado que requer um mapeamento de dados complexo e migração de dados relacionais (ex. migrar Oportunidades com seus Produtos). XL: Migração de múltiplos sistemas de origem, com grandes volumes de dados históricos. Requer ferramentas ETL e uma equipe de migração dedicada. SC: A migração de dados é contínua (coexistência de sistemas) ou os dados de origem são de qualidade muito baixa, exigindo um projeto massivo de qualidade de dados. |  |  |  |

# Parte 3: Questionários por Plataforma e Nuvens Principais

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Analisar em profundidade todos os documentos fornecidos pelo cliente (ex. RFPs, análises estratégicas) 1 e o banco de perguntas Guided Scoping Questions.pdf.

Instruções:

Análise de Requisitos: Primeiro, analisar os documentos do cliente para entender os requisitos funcionais e técnicos (ex. "precisamos gerenciar vendas de publicidade no Media Cloud" 1).

Análise do Banco de Perguntas: Analisar o arquivo Guided Scoping Questions.pdf.

Identificar e coletar TODAS as perguntas desse arquivo que sejam relevantes para as nuvens, produtos e capacidades que atendem aos requisitos do cliente (ex. coletar todas as perguntas da seção "Media Cloud" e "Sales Cloud" se forem relevantes).

1

Preenchimento do Modelo: a. Para cada Question ID já presente nas tabelas da Parte 3, localizar a informação nos documentos fonte do cliente que responda à Discovery Question e preencher a coluna Resposta / Observações do Cliente com os achados, citando a fonte.

1 b. Se a análise do Guided Scoping Questions.pdf (Passo 2) revelou perguntas relevantes que não estão no modelo, adicioná-las como novas linhas na subseção apropriada.

Avaliação: Para cada linha (tanto originais quanto adicionadas), com base na resposta e no guia de dimensionamento, preencher Impacto / Prioridade (Alta, Média, Baixa) e Dimensionamento (S-XL-SC) preliminar.

1

Lacunas: Se a informação para uma pergunta não for encontrada, marcar a resposta como "Não detalhado nos documentos".

1

Formato de Saída: Apresentar os resultados preenchendo (e adicionando linhas, se necessário) as tabelas Markdown desta seção.

A coluna Sizing Guidance and Complexity Drivers é fixa do modelo e não deve ser modificada pela IA.

1

## 3.1. Sales Cloud

### 3.1.1. Gerenciamento de Contas e Contatos

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SC-ACC-001 | Que tipos de clientes vocês gerenciam (B2B, B2C, Parceiros, etc.)? Utilizam um modelo de Contas Pessoais (Person Accounts) ou o modelo padrão de Contas de Negócios e Contatos? | S: Um único tipo de cliente (B2B ou B2C) com o modelo padrão correspondente. M: Múltiplos tipos de clientes gerenciados com Tipos de Registro (Record Types). L: Modelo misto B2B e B2C, que pode exigir o uso tanto de Contas Pessoais quanto de Contas de Negócios na mesma organização. XL: Necessidade de representar relações complexas entre indivíduos e empresas, como em gestão de patrimônio ou seguros (requer FSC). SC: Modelo de dados não padrão que requer objetos personalizados para representar os clientes. |  |  |  |
| SC-ACC-002 | Existem relações hierárquicas ou de outro tipo entre Contas (ex. matriz-subsidiária, redes de influência)? Um Contato pode estar relacionado a mais de uma Conta? | S: Contas independentes sem relações hierárquicas. Contatos relacionados a uma única Conta. M: Uso da hierarquia de Contas padrão. A função "Contatos em múltiplas Contas" está habilitada. L: Necessidade de visualizar e gerenciar hierarquias complexas, possivelmente com ferramentas de terceiros ou componentes LWC personalizados. XL: Requisito de modelar redes de relações complexas (não apenas hierárquicas) entre múltiplas Contas e Contatos. SC: Lógica de negócios personalizada baseada em relações hierárquicas (ex. roll-ups de dados complexos, compartilhamento de registros personalizado). |  |  |  |
| SC-ACC-003 | Qual é o modelo de segurança e visibilidade para Contas e Contatos? Quem pode criar, ver, editar e excluir registros? Baseia-se na hierarquia de papéis, territórios ou equipes de contas? | S: Modelo simples público ou privado baseado na propriedade do registro e na hierarquia de papéis. M: Uso de Regras de Compartilhamento (Sharing Rules) baseadas em critérios para abrir o acesso. L: Uso intensivo de Equipes de Contas (Account Teams) para gerenciar o acesso em nível de registro de forma granular. XL: Modelo de segurança complexo que combina hierarquia de papéis, territórios, equipes de contas e compartilhamento manual. SC: Requisitos de compartilhamento dinâmico ou baseado em lógica que exigem o uso de Compartilhamento Gerenciado por Apex (Apex Managed Sharing). |  |  |  |

### 3.1.2. Gerenciamento de Leads

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SC-LEAD-001 | Quais são suas fontes de leads (web, eventos, inbound, etc.)? Como são capturados atualmente? | S: Criação manual de leads. M: Uso de Web-to-Lead e/ou importações manuais de arquivos. L: Integração com ferramentas de automação de marketing (ex. Account Engagement/Pardot, Marketing Cloud) para a captura e sincronização de leads. XL: Múltiplas fontes de leads em tempo real através de APIs, com necessidade de desduplicação e enriquecimento de dados no momento da criação. SC: Lógica de captura personalizada que requer um serviço web Apex personalizado. |  |  |  |
| SC-LEAD-002 | Descreva o processo de qualificação e atribuição de leads. Que equipe é responsável? Que critérios determinam se um lead está qualificado? Como ele é roteado para o representante de vendas correto? | S: Processo manual de qualificação e atribuição. M: Uso de Regras de Atribuição de Leads (Lead Assignment Rules) padrão baseadas em critérios simples como geografia. L: Regras de atribuição complexas com múltiplos critérios, roteamento round-robin e filas por especialização. Uso de Einstein Lead Scoring para priorização. XL: Processo de qualificação em etapas com diferentes equipes (ex. SDRs/BDRs qualificando para Account Executives). Integração com ferramentas de roteamento avançadas (ex. LeanData). SC: Algoritmos de roteamento e pontuação personalizados baseados em lógica de negócios proprietária. |  |  |  |
| SC-LEAD-003 | Que informação é obrigatória antes que um lead possa ser convertido? O que acontece durante a conversão (criação de Conta, Contato, Oportunidade)? | S: Conversão padrão OOTB sem campos obrigatórios adicionais. M: Uso de regras de validação para assegurar que certos campos sejam preenchidos antes da conversão. L: Mapeamento de campos personalizados de Lead para Conta/Contato/Oportunidade. A lógica de conversão pode variar dependendo do tipo de lead. XL: Processo de conversão automatizado ou que precisa prevenir a criação de duplicatas de forma avançada (além das regras padrão). SC: Requisitos de conversão complexos que necessitam de um trigger Apex para gerenciar a criação de registros adicionais ou atualizar outros sistemas. |  |  |  |

### 3.1.3. Gerenciamento de Oportunidades e Processo de Vendas

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SC-OPP-001 | Descreva o processo de vendas do início ao fim. Quais são as etapas do ciclo de vendas e o que cada uma significa? Quantos processos de vendas diferentes existem (por linha de negócios, produto, etc.)? | S: 1 processo de vendas linear, < 7 etapas, probabilidade padrão. M: 1-2 processos de vendas gerenciados com Tipos de Registro e Caminhos de Vendas (Sales Paths). Etapas com campos-chave e guia para o sucesso. L: 3-5 processos de vendas distintos, com etapas, campos e guias de sucesso específicos para cada um. Uso de regras de validação para controlar a progressão das etapas. XL: Múltiplos processos de vendas complexos que são atribuídos dinamicamente. Implementação de uma metodologia de vendas específica (ex. Miller Heiman) na plataforma. SC: O processo de vendas não é linear e requer um gerenciamento de estados complexo, possivelmente com um objeto personalizado ou desenvolvimento LWC. |  |  |  |
| SC-OPP-002 | Como são gerenciados os produtos e preços nas oportunidades? Usam Listas de Preços (Price Books)? Descontos são aplicados? | S: As oportunidades têm um campo de Valor (Amount) preenchido manualmente. Produtos não são utilizados. M: Uso de Produtos e Listas de Preços (Price Books) padrão. Os representantes de vendas adicionam produtos às oportunidades. L: Múltiplas listas de preços (por moeda, região, segmento de cliente). Os descontos são gerenciados em nível de linha de produto. XL: Necessidade de configuração de produtos, pacotes (bundles) ou preços de assinatura. Isso indica a necessidade do Salesforce CPQ. SC: Lógica de preços extremamente complexa, com preços dinâmicos baseados em fatores externos ou algoritmos personalizados, que excede as capacidades do CPQ. |  |  |  |
| SC-OPP-003 | Como as equipes colaboram em oportunidades complexas? Usam Equipes de Oportunidades (Opportunity Teams)? Que papéis estão envolvidos (ex. especialista de produto, engenheiro de soluções)? | S: O proprietário da oportunidade gerencia toda a venda. M: Uso informal do Chatter para colaboração. L: Uso formal de Equipes de Oportunidades (Opportunity Teams) com papéis predefinidos e divisões de receita/créditos. XL: Processos de colaboração estruturados com notificações automáticas e tarefas para os membros da equipe em diferentes etapas da venda. SC: Requisitos de colaboração que envolvem usuários externos (parceiros) na oportunidade, o que poderia exigir uma Experience Cloud. |  |  |  |

### 3.1.4. CPQ (Configure, Price, Quote) e Gestão de Contratos

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SC-CPQ-001 | Seus produtos são configuráveis? Vendem pacotes (bundles) de produtos? Existem regras de dependência ou exclusão entre produtos (ex. "se comprar A, não pode comprar B")? | S: Produtos simples e não configuráveis. Isso pode não exigir CPQ. M: Pacotes de produtos estáticos. L: Produtos configuráveis com opções e regras de produto (validação, alerta, seleção). XL: Configurações multinível, regras de produto complexas que dependem de atributos do cliente e necessidade de venda guiada (guided selling). SC: Lógica de configuração que requer plugins de configuração externos ou desenvolvimento Apex personalizado (não recomendado). |  |  |  |
| SC-CPQ-002 | Descreva seu modelo de preços. É baseado em assinatura, uso, por níveis ou por volume? Descontos multicamada são aplicados (ex. desconto por volume + desconto de parceiro + desconto discricionário)? | S: Preços de lista fixos. Descontos manuais simples. M: Descontos por volume ou baseados em contrato. L: Preços de assinatura (recorrentes) e únicos (one-time). Uso da Cascata de Preços (Price Waterfall) para aplicar descontos em sequência. XL: Múltiplos modelos de preços (assinatura, uso, etc.), preços baseados em atributos e regras de preços complexas. SC: Requisitos de preços que dependem de chamadas em tempo real a sistemas externos ou envolvem cálculos financeiros complexos. |  |  |  |
| SC-CPQ-003 | Qual é o processo para gerar e aprovar Cotações (Quotes)? Que informação deve constar no documento de cotação? O ciclo de vida do contrato deve ser gerenciado (criação, emendas, renovações)? | S: Geração manual de cotações. Aprovação por e-mail. M: Uso do objeto Cotação padrão com modelos de cotação simples. Processo de aprovação de uma única etapa. L: Uso do Salesforce CPQ para gerar cotações dinâmicas. Processos de aprovação multinível com Aprovações Avançadas (Advanced Approvals). XL: Gerenciamento completo do ciclo de vida do contrato com Salesforce Contracts: emendas e renovações que atualizam automaticamente os ativos e assinaturas. SC: Requisitos de geração de documentos altamente personalizados ou integração com sistemas de terceiros de Gerenciamento do Ciclo de Vida do Contrato (CLM). |  |  |  |

### 3.1.5. Previsões (Forecasting) e Gerenciamento de Territórios

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SC-FCAST-001 | Como vocês realizam a previsão de vendas atualmente? Baseia-se na hierarquia de papéis? Que categorias de previsão utilizam (ex. Pipeline, Best Case, Commit)? | S: Previsão informal baseada em relatórios de oportunidades. M: Uso de Previsões Colaborativas (Collaborative Forecasting) baseadas na hierarquia de papéis e categorias padrão. L: Múltiplos tipos de previsão (por produto, por território). Ajustes são feitos em nível de gerente. XL: Necessidade de prever por períodos personalizados (não mensais/trimestrais) ou roll-ups de previsão que não seguem a hierarquia de papéis. SC: Modelos de previsão preditivos personalizados ou que requerem a consolidação de dados de previsão de sistemas externos. |  |  |  |
| SC-FCAST-002 | Vocês utilizam gerenciamento de territórios? Como estão estruturados (geográficos, por indústria, por conta nomeada)? Como as contas e os representantes de vendas são atribuídos aos territórios? | S: Não se utiliza gerenciamento de territórios; a atribuição de contas é manual. M: Estrutura de territórios simples e estática, baseada em geografia. L: Uso do Gerenciamento de Territórios Enterprise (Enterprise Territory Management) com uma hierarquia de territórios e regras de atribuição que são executadas periodicamente. XL: Múltiplos modelos de territórios ativos simultaneamente. Necessidade de planejar e modelar mudanças de território antes de ativá-las. SC: Requisitos de atribuição de territórios em tempo real ou baseados em algoritmos complexos de balanceamento de carga. |  |  |  |

## 3.2. Service Cloud

### 3.2.1. Gerenciamento de Casos e Canais (Omni-Channel)

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SV-CASE-001 | Quais são os canais através dos quais os clientes solicitam suporte (e-mail, telefone, web, chat, redes sociais, etc.)? Desejam gerenciar todas as interações em um único console? | S: 1-2 canais básicos como Email-para-Caso (Email-to-Case) e Web-para-Caso (Web-to-Case). M: Múltiplos canais, mas gerenciados em filas separadas. L: Implementação do Omni-Channel para unificar o gerenciamento de múltiplos canais (ex. Email, Chat, Casos) em uma única interface de agente. XL: Omni-Channel com roteamento baseado em habilidades, capacidade do agente e presença. Integração de telefonia (CTI). SC: Roteamento omnichannel com lógica preditiva (ex. rotear para o agente com maior probabilidade de resolução na primeira chamada) ou integração com canais não padrão. |  |  |  |
| SV-CASE-002 | Descreva o ciclo de vida de um caso, desde a criação até o fechamento. Quantos processos de suporte diferentes existem? Que informação deve ser capturada para cada tipo de caso? | S: Um único processo de suporte com um layout de caso padrão. M: Múltiplos tipos de casos gerenciados com Tipos de Registro e Processos de Suporte. L: Processos de suporte dinâmicos que guiam o agente através de Fluxos de Tela (Screen Flows). Automação complexa para atualizações de status e notificações. XL: Processos de suporte que abrangem múltiplos objetos (ex. um caso que gera uma ordem de trabalho no Field Service) e exigem orquestração. SC: Lógica de gerenciamento de casos muito complexa que requer desenvolvimento Apex. |  |  |  |
| SV-CASE-003 | Como os casos são atribuídos e escalados? Baseia-se em filas, habilidades do agente, prioridade do caso ou SLAs? | S: Atribuição manual ou para uma única fila. Escalonamento manual. M: Uso de Regras de Atribuição de Casos (Case Assignment Rules) para rotear para filas específicas. L: Uso de Regras de Escalonamento de Casos (Case Escalation Rules) para notificar ou reatribuir casos que não cumprem os tempos de resposta. XL: Roteamento baseado em habilidades com Omni-Channel. Regras de escalonamento que disparam processos de negócios complexos. SC: Lógica de atribuição ou escalonamento preditiva, ou lógica que depende de fatores externos consultados em tempo real. |  |  |  |

### 3.2.2. SLAs, Conhecimento e Automação

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SV-SLA-001 | Vocês gerenciam Acordos de Nível de Serviço (SLAs) com seus clientes? Como são definidos (ex. tempo de primeira resposta, tempo de resolução)? Variam de acordo com o cliente ou o tipo de produto? | S: SLAs informais, não gerenciados no sistema. M: Uso de Gerenciamento de Direitos (Entitlement Management) para definir SLAs simples e padronizados para todos os clientes. L: Múltiplos processos de direitos que variam de acordo com o nível de serviço do cliente (ex. Ouro, Prata, Bronze). XL: SLAs dinâmicos baseados em múltiplos critérios (produto, severidade, tipo de cliente) e com marcos intermediários. SC: Cálculo de SLAs que requer lógica personalizada complexa ou está sujeito a pausas e retomadas baseadas em condições não padrão. |  |  |  |
| SV-KNOW-001 | Utilizam uma base de conhecimento para ajudar os agentes internos ou os clientes (FAQs)? Qual é o processo para criar, aprovar e publicar artigos? | S: Sem base de conhecimento formal. M: Implementação do Salesforce Knowledge com um tipo de artigo e um ciclo de publicação simples. L: Múltiplos tipos de artigos, processos de aprovação e gerenciamento de versões. Visibilidade de artigos baseada em categorias de dados. XL: Base de conhecimento multilíngue. Uso de Recomendações de Artigos Einstein (Einstein Article Recommendations) para sugerir artigos aos agentes. SC: Requisitos de formato ou conteúdo de artigos que exigem componentes LWC personalizados ou integração com Sistemas de Gerenciamento de Conteúdos (CMS) externos. |  |  |  |
| SV-AUTO-001 | Que processos de suporte vocês gostariam de automatizar? Estão interessados em usar chatbots para desviar casos ou para a captura inicial de informações? | S: Automação básica com regras de fluxo de trabalho ou flows simples (ex. enviar um e-mail de confirmação quando um caso é criado). M: Uso de macros e ações rápidas para que os agentes automatizem tarefas repetitivas. L: Implementação de um chatbot (Einstein Bots) para responder perguntas frequentes e desviar casos de nível 1. XL: Chatbot que pode realizar ações em nome do usuário (ex. verificar o status de um pedido) invocando flows ou Apex. SC: Chatbot com Processamento de Linguagem Natural (NLP) avançado, análise de sentimentos e integração profunda com sistemas backend. |  |  |  |

## 3.3. Field Service

### 3.3.1. Gerenciamento de Ordens de Trabalho e Ativos

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| FS-WO-001 | Descreva seu processo atual de serviço de campo (field service), desde a criação da solicitação até a finalização do trabalho. Que tipos de trabalhos realizam (instalação, manutenção preventiva, reparo)? | S: Um único tipo de trabalho de reparo (break-fix). M: Múltiplos tipos de trabalho (instalação, reparo) gerenciados com Tipos de Trabalho (Work Types). L: Gerenciamento de planos de manutenção preventiva que geram ordens de trabalho automaticamente. XL: Trabalhos complexos de vários dias ou que exigem múltiplos técnicos com diferentes habilidades. SC: Processos de serviço de campo que estão fortemente integrados com o gerenciamento de projetos ou têm uma lógica de negócios única. |  |  |  |
| FS-WO-002 | Como são criadas as Ordens de Trabalho (Work Orders)? São geradas a partir de Casos, Oportunidades ou diretamente? Que informação é crucial em uma ordem de trabalho? | S: Criação manual de ordens de trabalho. M: Criação de ordens de trabalho a partir de Casos. L: Geração automática de ordens de trabalho de múltiplas fontes (Casos, Ativos, Planos de Manutenção) com modelos predefinidos. XL: Lógica de negócios complexa na criação de ordens de trabalho, como a determinação automática de produtos, habilidades e duração necessários. SC: Criação de ordens de trabalho disparada por eventos de dispositivos IoT (requer integração). |  |  |  |
| FS-ASSET-001 | Vocês rastreiam os ativos dos clientes? É preciso conhecer o histórico de serviço de um ativo específico ao criar uma ordem de trabalho? | S: Sem rastreamento de ativos. M: Os ativos do cliente são registrados, mas sem histórico detalhado. L: Gerenciamento completo do ciclo de vida do ativo, incluindo histórico de ordens de trabalho, substituições e hierarquias de ativos. XL: Rastreamento em tempo real dos atributos do ativo através de telemetria, e criação proativa de ordens de trabalho baseada no desempenho do ativo. SC: Modelo de dados de ativos muito complexo ou que requer integração com sistemas de Gerenciamento do Ciclo de Vida do Produto (PLM). |  |  |  |

### 3.3.2. Programação, Despacho e Inventário

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| FS-SCHED-001 | Como são atribuídas e programadas as visitas de serviço? É um processo manual ou automático? Que critérios são utilizados (proximidade, habilidades, disponibilidade)? | S: Despacho e programação manual por um despachante a partir do console. M: Uso de políticas de programação padrão (ex. minimizar o tempo de viagem). L: Múltiplas políticas de programação, otimização de rotas para uma frota de técnicos e programação baseada em habilidades, níveis de habilidade e disponibilidade de inventário. XL: Otimização de recursos em tempo real, reprogramação automática para emergências e manejo de agendamentos complexos (multi-recursos, multi-dias). SC: Algoritmos de otimização personalizados ou integração com sistemas de logística de terceiros muito sofisticados. |  |  |  |
| FS-INV-001 | Como vocês gerenciam o inventário de peças de reposição? Os técnicos levam inventário em seus veículos? Como o estoque é solicitado e reposto? | S: Sem gerenciamento de inventário no sistema. M: Rastreamento de inventário em nível de armazém principal. L: Gerenciamento de inventário em múltiplas localizações, incluindo veículos de técnicos. Os produtos são consumidos nas ordens de trabalho. XL: Processos de solicitação e reposição de inventário, incluindo transferências entre localizações. Rastreamento de produtos serializados. SC: Integração em tempo real com um sistema ERP para o gerenciamento de inventário e logística da cadeia de suprimentos. |  |  |  |

### 3.3.3. Experiência Móvel e Faturamento

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| FS-MOB-001 | Que tarefas os técnicos devem realizar em seu dispositivo móvel? Precisam de acesso offline? | S: Ver sua agenda e detalhes básicos da visita. Requer conexão. M: Atualizar o status do trabalho, adicionar notas e ver ordens de trabalho. Capacidade offline básica é necessária. L: Capacidade offline completa, incluindo criação de registros, consumo de inventário e geração de relatórios de serviço. XL: Uso de Fluxos de Tela (Screen Flows) complexos no celular para guiar o técnico através de listas de verificação de segurança ou protocolos de reparo. SC: Requisitos de interface de usuário móvel altamente personalizados ou integração de aplicativos de terceiros dentro do app de Field Service. |  |  |  |
| FS-BILL-001 | Como é gerado o faturamento pelo serviço prestado? Baseia-se no tempo, nos materiais consumidos ou em tarifas fixas? Os técnicos capturam a assinatura do cliente ao finalizar? | S: O faturamento é realizado fora do Salesforce. M: Relatórios de serviço são gerados em PDF com um resumo do trabalho para a assinatura do cliente. L: O sistema calcula os custos baseados em tempo e materiais e os prepara para o faturamento. XL: Geração de faturas diretamente do Field Service ou integração direta com um sistema de faturamento para automatizar o processo de cobrança. SC: Modelos de faturamento complexos baseados em contratos de serviço, penalidades por descumprimento de SLA ou preços dinâmicos. |  |  |  |

## 3.4. Marketing Cloud (Engagement & Account Engagement)

### 3.4.1. Gerenciamento de Dados de Clientes e Segmentação

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| MC-DATA-001 | Que fontes de dados serão utilizadas para as atividades de marketing (Sales/Service Cloud, E-commerce, Data Warehouse, etc.)? Com que frequência precisam que esses dados sejam atualizados? | S: Uso de listas de assinantes importadas manualmente de arquivos CSV. M: Sincronização de dados do Sales/Service Cloud através do Marketing Cloud Connect. L: Ingestão de dados de 2-3 fontes adicionais (ex. E-commerce, fidelidade) via API ou transferências de arquivos automatizadas (SFTP). XL: Múltiplas fontes de dados em tempo real e em lote que exigem um modelo de dados unificado no Contact Builder. Isso sugere a necessidade do Data Cloud. SC: Requisitos de ingestão de dados de sistemas legados ou não padrão que exigem desenvolvimento de integração personalizado. |  |  |  |
| MC-DATA-002 | Descreva os 10-15 critérios de segmentação mais importantes que utiliza ou gostaria de utilizar (ex. demografia, histórico de compras, comportamento no site). | S: Segmentação básica baseada em campos de perfil (ex. país, gênero). M: Uso de filtros de dados e Queries SQL para segmentar com base em dados de múltiplas Data Extensions. L: Segmentação baseada no comportamento (interação com e-mails, visitas ao site) e dados de compra. XL: Segmentação avançada com Pontuação de Engajamento Einstein (Einstein Engagement Scoring) e criação de públicos de publicidade complexos. SC: Critérios de segmentação que requerem cálculos ou agregações complexas que devem ser realizadas fora do Marketing Cloud (ex. em um Data Warehouse ou Data Cloud). |  |  |  |

### 3.4.2. Automação de Jornadas e Personalização

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| MC-JNY-001 | Descreva as campanhas transacionais (ex. confirmação de pedido, boas-vindas) e comportamentais (ex. carrinho abandonado, reengajamento) que deseja implementar. | S: 1-3 jornadas (journeys) simples e lineares (ex. série de boas-vindas). M: Múltiplas jornadas com ramificação básica (divisões de decisão / decision splits) baseada em aberturas ou cliques de e-mail. L: Jornadas complexas que reagem ao comportamento do cliente em múltiplos canais (web, móvel) e atualizam dados no Sales/Service Cloud. XL: Orquestração de jornadas omnichannel que incluem e-mail, SMS, notificações push e públicos de publicidade. Uso de Einstein STO (Otimização do Horário de Envio). SC: Jornadas que exigem uma lógica de decisão em tempo real extremamente complexa baseada em chamadas a APIs externas. |  |  |  |
| MC-JNY-002 | Que nível de personalização de conteúdo vocês exigem? É personalização simples (ex. nome do cliente) ou conteúdo dinâmico baseado em atributos ou comportamento? | S: Personalização básica com campos de perfil (ex. %%FirstName%%). M: Uso de Conteúdo Dinâmico (Dynamic Content) baseado em 1-2 atributos (ex. mostrar uma imagem diferente por gênero ou país). L: Uso extensivo de AMPscript para personalizar conteúdo baseado em regras de negócios complexas e dados de múltiplas Data Extensions. XL: Personalização preditiva com Seleção de Conteúdo Einstein (Einstein Content Selection). Personalização web em tempo real com Personalization (Interaction Studio). SC: Geração de conteúdo personalizado em tempo real que requer um desenvolvimento backend significativo. |  |  |  |

## 3.5. Data Cloud

### 3.5.1. Fontes de Dados, Modelo e Unificação

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| DC-DATA-001 | Que sistemas e fontes de dados (Salesforce CRM, Marketing Cloud, sistemas externos, dados de site/móvel) serão conectados ao Data Cloud para criar o perfil de cliente unificado? | S: 1-2 fontes de dados, principalmente outras nuvens Salesforce (ex. Sales Cloud, Service Cloud) usando conectores padrão. M: Conexão a 3-5 fontes, incluindo Marketing Cloud e um sistema externo como um data warehouse através de conectores. L: Múltiplas fontes de dados, incluindo dados de comportamento em streaming de sites ou aplicativos móveis (requer o SDK Móvel/Web). XL: Ingestão de dados de sistemas legados ou data lakes através de conectores MuleSoft ou ingestão por API. SC: Requisitos de ingestão de dados não estruturados ou em formatos complexos que precisam de um pré-processamento significativo antes da ingestão. |  |  |  |
| DC-DATA-002 | Como os dados de origem serão mapeados para o modelo de dados padrão do Data Cloud (DMOs - Objetos do Modelo de Dados)? Será necessário normalizar ou transformar os dados antes de mapeá-los? | S: Mapeamento direto de objetos padrão do Salesforce (ex. Conta, Contato) para os DMOs correspondentes. M: Mapeamento de objetos padrão e alguns personalizados, com a necessidade de criar campos de fórmula simples para normalização. L: Mapeamento de dados de múltiplos sistemas com diferentes estruturas e formatos, exigindo o uso de Transformações de Dados (Data Transforms) para limpeza e normalização. XL: O modelo de dados de origem é muito diferente do modelo padrão do Data Cloud, exigindo a criação de DMOs personalizados e relações complexas. SC: Os dados de origem são de qualidade muito baixa ou inconsistentes, exigindo um esforço massivo de preparação de dados. |  |  |  |
| DC-ID-001 | Que regras de negócios definem um perfil de cliente unificado? Que identificadores (e-mail, telefone, ID de cliente) serão utilizados para a resolução de identidade? | S: Uma única regra de correspondência (match rule) baseada em um identificador exato, como o endereço de e-mail. M: Múltiplas regras de correspondência padrão (ex. e-mail exato E nome e sobrenome) com uma estratégia de consolidação simples. L: Uso de regras de correspondência difusa (fuzzy matching) para nomes ou endereços. Regras de reconciliação personalizadas para selecionar o "melhor" valor de campo (ex. o número de telefone mais recente). XL: Múltiplos perfis unificados (ex. unificar indivíduos e também unificar grupos familiares ou empresas) com regras de resolução complexas. SC: Requisitos de resolução de identidade que envolvem grafos de relações ou algoritmos de machine learning personalizados. |  |  |  |

### 3.5.2. Perspectivas (Insights), Segmentação e Ativação

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| DC-CI-001 | Que tipo de métricas agregadas ou KPIs (Insights Calculados) vocês precisam calcular sobre o perfil unificado (ex. valor de vida do cliente, gasto total nos últimos 12 meses, categoria de produto favorita)? | S: 1-3 Insights Calculados (Calculated Insights) simples baseados em uma única métrica (ex. SOMA(VendasTotais)). M: Insights Calculados que incluem filtros e dimensões (ex. SOMA(VendasTotais) agrupado por CategoriaProduto). L: Insights Calculados de múltiplos passos que se baseiam em outros Insights Calculados. Uso de funções de janela ou baseadas em tempo. XL: Criação de modelos de propensão ou pontuação (ex. risco de churn) usando as capacidades de IA do Data Cloud. SC: Cálculos que exigem lógica procedural ou iterativa não suportada pelo motor de Insights Calculados e devem ser realizados externamente. |  |  |  |
| DC-SEG-001 | Que tipo de públicos ou segmentos de clientes precisam criar? Serão estáticos ou dinâmicos? Serão baseados em atributos de perfil ou em comportamento em tempo real? | S: Segmentos simples baseados em atributos de perfil (ex. "todos os clientes na Espanha"). M: Segmentos que combinam atributos de perfil e dados de comportamento (ex. "clientes na Espanha que compraram nos últimos 30 dias"). L: Segmentos complexos com múltiplas condições aninhadas (E/OU) e que utilizam Insights Calculados como critérios. XL: Segmentação em cascata (waterfall) e uso de IA para encontrar públicos semelhantes (look-alike). SC: Critérios de segmentação que exigem consultar dados em tempo real de sistemas externos no momento da avaliação. |  |  |  |
| DC-ACT-001 | Para que sistemas ou plataformas (Alvos de Ativação / Activation Targets) precisam enviar esses segmentos (ex. Marketing Cloud, Google Ads, Facebook, SFTP)? | S: Ativação para um único destino, como o Marketing Cloud, usando o conector padrão. M: Ativação para 2-3 destinos, incluindo plataformas de publicidade como Google Ads ou Facebook. L: Ativação para múltiplos destinos, incluindo a necessidade de enriquecer perfis no Sales/Service Cloud com atributos do Data Cloud. XL: Ativação para destinos como data warehouses ou via SFTP, o que requer configuração do payload de dados. SC: Requisitos de ativação em tempo real para sistemas que não têm um conector OOTB, exigindo o uso da API do Data Cloud. |  |  |  |

## 3.6. Commerce Cloud (B2B & B2C)

### 3.6.1. Catálogo, Preços e Promoções

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| CC-CAT-001 | Descreva seu catálogo de produtos. São produtos simples, produtos com variações (tamanho/cor), pacotes (bundles) ou produtos configuráveis? Que sistema é a fonte da verdade para os dados de produto (PIM)? | S: Catálogo pequeno de produtos simples. Os dados de produto são gerenciados no Commerce Cloud. M: Produtos com variações. Utiliza-se um PIM externo de onde os dados são importados. L: Catálogo grande com pacotes de produtos e relações (cross-sell/up-sell). XL: Produtos complexos e configuráveis. Múltiplos catálogos atribuídos a diferentes grupos de clientes. SC: Requisitos de visualização de produtos personalizados (ex. visor 3D) ou lógica de catálogo extremamente dinâmica. |  |  |  |
| CC-PRICE-001 | Como funciona sua estratégia de preços? Têm preços diferentes por cliente ou segmento (B2B)? Com que frequência os preços mudam? Que tipos de promoções oferecem (ex. % de desconto, compre X leve Y)? | S: Uma única lista de preços. Promoções simples (ex. cupom de desconto). M: Múltiplas listas de preços (por país, por site). Promoções com condições (ex. "gaste mais de 100 €"). L: Preços específicos do cliente ou do contrato (B2B). Promoções empilháveis e complexas. XL: Preços que são obtidos em tempo real de um sistema ERP. Motor de promoções com lógica de negócios altamente personalizada. SC: Preços dinâmicos baseados em IA ou fatores de mercado em tempo real. |  |  |  |

### 3.6.2. Experiência de Compra e Gerenciamento de Pedidos

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| CC-SHOP-001 | Descreva o processo de checkout ideal. Que opções de pagamento (cartão de crédito, PayPal, etc.) e envio precisam? Permitem o checkout como convidado? | S: Checkout padrão de uma página com um gateway de pagamento e um método de envio. M: Múltiplas opções de pagamento e envio. Checkout como convidado e como usuário registrado. L: Checkout personalizado com etapas sob medida. Integração com sistemas de cálculo de impostos e prevenção de fraudes. XL: Checkout omnichannel (ex. comprar online, retirar na loja - BOPIS). Múltiplos endereços de envio por pedido. SC: Processo de checkout que requer lógica de negócios única ou integrações com sistemas de pagamento não padrão. |  |  |  |
| CC-OMS-001 | Como é gerenciado o ciclo de vida do pedido (processamento, envio, devoluções)? Que sistema atua como seu sistema de gerenciamento de pedidos (OMS)? Como o inventário e a disponibilidade (ATP) são gerenciados? | S: O gerenciamento de pedidos e inventário é feito manualmente ou em um sistema externo simple. M: Uso do Salesforce Order Management com um único armazém. L: Integração com um ERP que é a fonte da verdade para o inventário e o status do pedido. XL: Uso do Salesforce Order Management para orquestrar o cumprimento de pedidos de múltiplos armazéns ou lojas, com lógica de roteamento de pedidos. SC: Processos de devolução (RMA) e logística reversa muito complexos, ou requisitos de orquestração de pedidos em nível global. |  |  |  |

## 3.7. Experience Cloud

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| EX-USE-001 | Qual é o propósito principal da comunidade (portal)? É para clientes (autoatendimento), parceiros (gerenciamento de leads e oportunidades) ou funcionários (intranet)? Quantas comunidades diferentes precisam? | S: Uma única comunidade para um caso de uso simples, como um portal de ajuda com artigos do Knowledge. M: Uma comunidade de clientes que permite ver e criar casos, ou uma comunidade de parceiros para registro de negócios (deal registration). L: Múltiplas comunidades, ou uma única comunidade que atende a múltiplos públicos com perfis e páginas personalizadas para cada um. XL: Uma comunidade que é parte central do modelo de negócios, com funcionalidades transacionais complexas (ex. um portal de clientes para comprar produtos ou pagar faturas). SC: Uma comunidade que requer uma experiência de usuário completamente personalizada (pixel-perfect) e um grande número de componentes LWC personalizados. |  |  |  |
| EX-SEC-001 | Que método de autenticação os usuários utilizarão (login/senha, SSO, login social)? Que dados do Salesforce os usuários externos precisam ver e com que nível de acesso? | S: Autenticação com nome de usuário e senha. Os usuários veem apenas seus próprios registros. M: Configuração de Single Sign-On (SSO) com um provedor de identidade. Os usuários veem registros de sua conta. L: Múltiplos métodos de autenticação. Modelo de compartilhamento complexo para parceiros, com papéis e acesso delegado. XL: Requisitos de segurança avançados, como autenticação de dois fatores (2FA) ou o uso de fluxos de login para verificar a identidade do usuário. SC: Modelo de compartilhamento que não pode ser resolvido com configuração padrão e requer Compartilhamento Gerenciado por Apex (Apex Managed Sharing). |  |  |  |
| EX-BRAND-001 | Que nível de personalização de marca (branding) é necessário? Os modelos padrão são suficientes ou precisam de um design "pixel-perfect"? A comunidade deve ser responsiva para dispositivos móveis? | S: Uso de um modelo padrão com personalização de logo e cores. M: Modificações no modelo com CSS personalizado para alinhá-lo à marca. L: Criação de um tema de layout e componentes LWC personalizados para alcançar um look & feel específico. XL: A comunidade deve ser publicada como um aplicativo móvel de marca (Mobile Publisher). SC: Design completamente personalizado que requer um extenso desenvolvimento front-end. |  |  |  |

## 3.8. Slack

### 3.8.1. Casos de Uso e Colaboração

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SL-USE-001 | Quais são os principais casos de uso de colaboração que desejam implementar? (ex. "Swarming" em casos de atendimento, "Deal Rooms" para oportunidades de venda, notificações para campanhas de marketing). | S: Notificações unidirecionais do Salesforce para o Slack (ex. "Nova oportunidade atribuída"). M: Uso de ações padrão dos aplicativos Salesforce para Slack (ex. criar um caso, atualizar uma oportunidade do Slack). L: Implementação de um caso de uso estruturado como "Swarming" para o Service Cloud, que implica criar canais, adicionar especialistas e gerenciar o ciclo de vida do swarm. XL: Múltiplos casos de uso complexos que abrangem vários departamentos e que exigem flows do Salesforce invocados do Slack. SC: Desenvolvimento de um aplicativo Slack personalizado para um caso de uso proprietário. |  |  |  |
| SL-USE-002 | Como as equipes colaboram atualmente nesses cenários? Que ferramentas usam? Que informação do Salesforce seria mais valiosa ter diretamente no Slack? | S: A colaboração é realizada principalmente por e-mail. M: Canais do Slack são usados, mas a informação do Salesforce é copiada e colada manualmente. L: O objetivo é trazer visualizações de registros do Salesforce (expansão de links / unfurling) e a capacidade de realizar ações rápidas diretamente no Slack. XL: É necessária uma visão 360 do cliente ou da oportunidade diretamente no Slack, consolidando informações de múltiplos objetos. SC: É necessária a visualização de dados de sistemas de terceiros, além do Salesforce, dentro da mesma interface do Slack. |  |  |  |

### 3.8.2. Automação e Integrações

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| SL-AUTO-001 | Que processos de negócios vocês gostariam de automatizar usando Slack e Salesforce Flow? (ex. processos de aprovação, criação de canais de projeto, pesquisas com funcionários). | S: Aprovações simples que podem ser aceitas ou rejeitadas de uma notificação do Slack. M: Flows que são iniciados do Salesforce e enviam mensagens ou formulários para o Slack. L: Flows que são iniciados do Slack (ex. com um comando de barra / slash command ou um botão) e orquestram um processo de negócios no Salesforce. XL: Automações bidirecionais complexas que mantêm dados sincronizados entre uma conversa do Slack e um registro do Salesforce. SC: Flows que integram Slack, Salesforce e sistemas de terceiros (ex. criar um canal do Slack, um registro do Salesforce e um projeto do Jira, tudo a partir de uma única ação). |  |  |  |
| SL-INT-001 | Além do Salesforce, que outros aplicativos (ex. Jira, Google Drive, Workday) são críticos para seus fluxos de trabalho e precisam ser integrados em seus processos de colaboração no Slack? | S: Não são necessárias integrações de outros aplicativos. M: Uso de integrações padrão do Diretório de Aplicativos do Slack. L: Necessidade de que os flows de automação interajam com as APIs de outros aplicativos. XL: Criação de uma experiência unificada no Slack que consolida notificações e ações de múltiplos sistemas em um só lugar. SC: Desenvolvimento de um aplicativo Slack personalizado que atua como um hub central para múltiplos sistemas empresariais. |  |  |  |

## 3.9. MuleSoft

### 3.9.1. Estratégia de Integração e Conectividade API-led

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| MS-API-001 | Qual é a estratégia de integração da empresa? Buscam construir integrações ponto a ponto ou estabelecer uma rede de aplicativos reutilizável através de uma metodologia API-led? | S: Sem estratégia formal; são necessárias 1-2 integrações ponto a ponto. M: O cliente entende o valor da reutilização e está aberto a uma estratégia API-led, mas não tem experiência prévia. L: O cliente está comprometido com a estratégia API-led, e o projeto envolve criar um conjunto de APIs de Sistema, Processo e Experiência para um domínio de negócios. XL: O projeto é uma iniciativa de transformação em nível empresarial para estabelecer um C4E (Centro de Capacitação) e construir uma rede de aplicativos completa. SC: A organização é muito resistente a mudar de um modelo ponto a ponto para um modelo de plataforma, o que requer um esforço significativo de gestão da mudança e evangelização. |  |  |  |
| MS-API-002 | APIs de Sistema: Que sistemas de registro (ERPs, bancos de dados, sistemas legados) precisam ser desbloqueados para expor seus dados de maneira segura e controlada? | S: 1-2 sistemas modernos com APIs REST/SOAP bem documentadas. M: 3-5 sistemas, incluindo alguns bancos de dados que requerem conectores JDBC. L: Conexão a sistemas legados sem APIs modernas (ex. via arquivos planos, filas de mensagens). XL: Múltiplos sistemas de registro complexos (ex. SAP, Oracle EBS) que requerem conectores especializados e profundo conhecimento do domínio. SC: Sistemas mainframe ou proprietários que não têm conectividade padrão e requerem o desenvolvimento de conectores personalizados. |  |  |  |
| MS-API-003 | APIs de Processo: Que processos de negócios exigem a orquestração, composição ou agregação de dados de múltiplas APIs de Sistema? (ex. "Obter Visão 360 do Cliente", "Sincronizar Pedido de Venda"). | S: Não são necessárias APIs de Processo; a lógica de negócios reside na aplicação final. M: 1-2 APIs de Processo que realizam orquestração simples (ex. obter dados de dois sistemas e combiná-los). L: Múltiplas APIs de Processo que implementam lógica de negócios significativa, como a sincronização de entidades complexas entre sistemas. XL: APIs de Processo que gerenciam processos de longa duração ou exigem lógica complexa de compensação de erros. SC: Lógica de orquestração que requer um motor de BPM (Gerenciamento de Processos de Negócios) ou regras de negócios muito sofisticadas. |  |  |  |
| MS-API-004 | APIs de Experiência: Que canais ou aplicativos consumirão os dados (ex. Salesforce, um aplicativo móvel, um portal web, um parceiro externo)? Cada canal requer uma visão dos dados formatada ou filtrada de maneira diferente? | S: Uma única API de Experiência para um único consumidor (ex. Salesforce). M: Múltiplas APIs de Experiência, cada uma adaptada a um canal específico (ex. uma para o app móvel que retorna um payload leve, outra para o app web com mais detalhes). L: APIs de Experiência que precisam implementar políticas de segurança específicas por canal ou consumidor. XL: Criação de um portal de desenvolvedores para que terceiros descubram e consumam APIs de forma autoatendimento. SC: Requisitos de transformação de protocolos (ex. expor uma API REST a partir de um serviço SOAP ou GraphQL) ou segurança em nível de campo. |  |  |  |

### 3.9.2. Requisitos Não Funcionais

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| MS-NFR-001 | Quais são os requisitos de volume, desempenho e latência para as integrações? São síncronas (tempo real) ou assíncronas (lotes)? | S: Integrações em lote de baixo volume executadas durante a noite. M: Integrações em tempo real de baixo volume ou integrações em lote de alto volume. L: Requisitos de Alta Disponibilidade (HA) e Recuperação de Desastres (DR). Integrações síncronas de alto desempenho. XL: Processamento de eventos em streaming em grande escala (arquitetura orientada a eventos). SC: Requisitos de latência ultrabaixa (milissegundos) que podem exigir otimizações de desempenho em nível de rede e infraestrutura. |  |  |  |
| MS-NFR-002 | Como será gerenciada a segurança das APIs? Que políticas serão aplicadas (ex. limitação de taxa, ID/segredo de cliente, JWT, mTLS)? Como as APIs serão monitoradas e os erros gerenciados? | S: Segurança básica (ex. HTTPS, chave de API). Monitoramento e alertas manuais. M: Uso de políticas padrão do API Manager (ex. limitação de taxa, aplicação de ID de cliente). L: Implementação de um esquema de segurança mais robusto como OAuth 2.0. Estratégia de tratamento de erros consistente em todas as APIs. XL: Integração com um Provedor de Identidade (IdP) corporativo. Monitoramento e registro centralizado com ferramentas como Anypoint Monitoring ou Splunk. SC: Requisitos de segurança em nível de mensagem ou políticas de segurança personalizadas. |  |  |  |

# Parte 4: Questionários por Soluções de Indústria

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Analisar em profundidade todos os documentos fornecidos pelo cliente (ex. RFPs, análises estratégicas) 1 e o banco de perguntas Guided Scoping Questions.pdf.

Instruções:

Análise de requisitos: Primeiro, analisar os documentos do cliente para entender os requisitos de indústria (ex. "precisamos gerenciar vendas de publicidade no Media Cloud" 1).

Análise do Banco de Perguntas: Analisar o arquivo Guided Scoping Questions.pdf.

Identificar e coletar TODAS as perguntas desse arquivo que sejam relevantes para as soluções de indústria que atendem aos requisitos do cliente (ex. coletar todas as perguntas da seção "Media Cloud" ou "Financial Services Cloud").

1

Preenchimento do Modelo: a. Para cada Question ID já presente nas tabelas da Parte 4, localizar a informação nos documentos fonte do cliente que responda à Discovery Question e preencher a coluna Resposta / Observações do Cliente com os achados, citando a fonte.

1 b. Se a análise do Guided Scoping Questions.pdf (Passo 2) revelou perguntas de indústria relevantes que não estão no modelo, adicioná-las como novas linhas na subseção apropriada.

Avaliação: Para cada linha (tanto originais quanto adicionadas), com base na resposta e no guia de dimensionamento, preencher Impacto / Prioridade (Alta, Média, Baixa) e Dimensionamento (S-XL-SC) preliminar.

1

Lacunas: Se a informação para uma pergunta não for encontrada, marcar a resposta como "Não detalhado nos documentos".

1

Formato de Saída: Apresentar os resultados preenchendo (e adicionando linhas, se necessário) as tabelas Markdown desta seção.

A coluna Sizing Guidance and Complexity Drivers é fixa do modelo e não deve ser modificada pela IA.

1

## 4.1. Financial Services Cloud (FSC)

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| FSC-DM-001 | Qual é a sua subindústria principal (Banca de Varejo, Gestão de Patrimônio, Seguros)? Como modelam seus clientes? Qual é a definição de um "grupo familiar" (household) e como as relações financeiras são agrupadas? | S: Um único subsetor. Uso do modelo padrão de Grupos Familiares (Households) para agrupar clientes. M: Múltiplos subsetores. Necessidade de personalizar o modelo de relações para incluir papéis como "Advogado" ou "Contador". L: Requisitos complexos de agrupamento e roll-up de dados em nível de grupo familiar e entre grupos familiares. XL: O modelo de dados deve suportar tanto clientes individuais (B2C) quanto empresariais (B2B) com suas complexas estruturas de propriedade. SC: Necessidade de modelar relações financeiras não hierárquicas ou baseadas em grafos. |  |  |  |
| FSC-INS-001 | (Seguros) Descreva o ciclo de vida da apólice e da reclamação (sinistro). Que sistemas gerenciam η administração de apólices (PAS) e a adjudicação de reclamações? É necessária uma visão 360 das apólices e reclamações do cliente no Salesforce? | S: Os dados de apólices e reclamações são carregados manualmente no FSC. M: Integração somente leitura para ver apólices e reclamações de um sistema externo. L: Integração bidirecional para sincronizar dados básicos de apólices e reclamações. XL: Orquestração de partes do processo de reclamações (ex. Primeiro Aviso de Sinistro - FNOL) dentro do Salesforce, com integração a sistemas centrais. SC: Implementação de um sistema completo de administração de apólices ou reclamações sobre a plataforma Salesforce. |  |  |  |
| FSC-WM-001 | (Gestão de Patrimônio) Que tipos de Contas Financeiras precisam gerenciar (investimentos, depósitos, empréstimos)? Como são rastreados os Objetivos Financeiros e os ativos e passivos de um cliente? | S: Rastreamento de 1-2 tipos de contas financeiras com dados carregados manualmente. M: Integração para a carga periódica de saldos e transações de contas financeiras. L: Modelo financeiro completo do cliente, incluindo ativos e passivos não financeiros. Uso de Planos de Ação (Action Plans) para processos de onboarding. XL: Integração em tempo real com sistemas de custódia ou plataformas de trading para uma visão atualizada das carteiras de investimento. SC: Algoritmos personalizados de planejamento financeiro ou recomendação de investimentos implementados na plataforma. |  |  |  |

## 4.2. Health & Life Sciences (HLS)

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| HLS-PAT-001 | Como obtêm uma visão 360 do paciente? Que sistemas (Prontuário Eletrônico do Paciente - PEP / EHR/EMR, sistemas de farmácia, etc.) contêm dados do paciente? Têm uma estratégia de interoperabilidade baseada em padrões como FHIR? | S: Os dados do paciente são gerenciados principalmente dentro do Salesforce (dados demográficos e de interação). M: Integração somente leitura para ver dados clínicos básicos de um PEP (EHR). L: Uso do modelo de dados clínicos do Health Cloud (baseado em FHIR) para armazenar dados como condições, medicamentos e alergias. XL: Integração bidirecional com um PEP (EHR) através de APIs FHIR para sincronização de dados quase em tempo real. SC: O projeto requer η criação de uma plataforma de Intercâmbio de Informações de Saúde (HIE) ou a integração com múltiplos PEPs (EHRs) de diferentes fornecedores. |  |  |  |
| HLS-CARE-001 | Descreva o processo de gerenciamento de Planos de Cuidado (Care Plans). Como são criados, tarefas são atribuídas e o progresso do paciente é monitorado? São padronizados por condição ou personalizados? | S: Uso de modelos de planos de cuidado OOTB para condições comuns. M: Criação de modelos de planos de cuidado personalizados com problemas, metas e tarefas específicas da organização. L: Planos de cuidado dinâmicos que se adaptam conforme o progresso do paciente ou os dados recebidos de dispositivos de monitoramento remoto. XL: Coordenação de planos de cuidado entre uma equipe multidisciplinar (médicos, enfermeiros, assistentes sociais) com tarefas e visibilidade específicas por papel. SC: Planos de cuidado que requerem lógica de negócios ou protocolos clínicos muito complexos, implementados com flows ou Apex. |  |  |  |
| HLS-UM-001 | Como gerenciam o processo de Gerenciamento de Utilização (Utilization Management), como as autorizações prévias? Que regras de negócios são aplicadas para aprovar ou negar solicitações? | S: Registro manual de solicitações de autorização. M: Processo de revisão e aprovação de solicitações dentro do Salesforce. L: Uso do Motor de Regras de Negócio (Business Rules Engine) com modelos de conjuntos de expressões para automatizar a adjudicação de solicitações simples. XL: Integração com sistemas externos para verificar a elegibilidade do paciente e os benefícios do plano como parte do processo de autorização. SC: Algoritmos de IA para a detecção de fraude e abuso ou para recomendar alternativas de tratamento mais rentáveis. |  |  |  |

## 4.3. Manufacturing & Automotive Cloud

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| MFG-SA-001 | (Manufatura) Utilizam Acordos de Venda (Sales Agreements) de longo prazo? Como são negociados, gerenciados e acompanhados para conformidade (quantidades planejadas vs. reais)? | S: Gerenciamento de acordos em documentos fora do Salesforce. M: Uso de Acordos de Venda (Sales Agreements) para registrar termos. As quantidades reais são atualizadas manualmente ou via CSV. L: Integração com o ERP para atualizar automaticamente as quantidades reais baseadas nos pedidos processados. XL: Uso do Tableau CRM (CRM Analytics) para analisar o desempenho dos acordos, prever a conformidade e identificar oportunidades de upsell. SC: Modelos de preços ou participação nos lucros nos acordos que exigem lógica de cálculo personalizada. |  |  |  |
| MFG-FCAST-001 | (Manufatura) Como realizam a previsão de vendas? Baseia-se em contas (Previsão Baseada em Contas), produtos, territórios? Como as equipes de vendas, operações e finanças colaboram no processo S&OP (Planejamento de Vendas e Operações)? | S: Previsão baseada em oportunidades, gerenciada em planilhas. M: Uso da Previsão Baseada em Contas (Account-Based Forecasting) para agregar previsões por conta. L: Fórmulas de previsão avançadas que combinam dados de oportunidades, acordos de venda e dados históricos. XL: Processo S&OP colaborativo na plataforma, onde diferentes equipes podem ver e ajustar previsões, e analisar o impacto das mudanças. SC: Algoritmos de previsão de demanda personalizados que incorporam fatores externos (tendências de mercado, dados macroeconômicos). |  |  |  |
| AUTO-DLR-001 | (Automotivo) Como gerenciam sua rede de concessionárias (dealers)? Como os leads e as oportunidades são compartilhados? Como medem o desempenho das concessionárias? | S: O gerenciamento de concessionárias é feito fora do CRM. M: As concessionárias são modeladas como Contas de Parceiro (Partner Accounts). Um portal básico da Experience Cloud é usado para a distribuição de leads. L: Uso de capacidades de Gerenciamento de Desempenho de Concessionárias (Dealer Performance Management) para rastrear KPIs e dashboards por concessionária. XL: Processos de colaboração avançados com concessionárias, como o gerenciamento conjunto do inventário de veículos ou o planejamento de campanhas de marketing. SC: Integração profunda com Sistemas de Gerenciamento de Concessionárias (DMS) de terceiros. |  |  |  |
| AUTO-WAR-001 | (Automotivo) Descreva o ciclo de vida da reclamação de garantia, desde o envio pela concessionária até a adjudicação e o pagamento. Que sistemas estão envolvidos? | S: Registro manual de reclamações de garantia. M: Portal para que as concessionárias apresentem reclamações. Validação automática da cobertura de garantia do ativo. L: Uso do motor de regras de negócio para a adjudicação automática de reclamações simples. XL: Processo de adjudicação completo, incluindo gerenciamento de devolução de peças, integração com sistemas de inventário e liquidação financeira com a concessionária. SC: Detecção de reclamações fraudulentas através de IA ou análise de padrões complexos. |  |  |  |

## 4.4. Consumer Goods Cloud (Retail & CPG)

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| CG-RE-001 | Que atividades seus representantes de campo realizam durante uma visita à loja (Execução de Varejo)? (ex. auditoria de gôndolas, verificação de planograma, coleta de pedidos, pesquisas). | S: Uma lista de tarefas simples que o representante marca como concluída. M: Uso de Pesquisas (Surveys) para guiar as auditorias de loja. L: Tarefas de auditoria dinâmicas que mudam dependendo da loja ou da promoção ativa. Uso do Einstein Vision para reconhecimento de produtos nas gôndolas. XL: Correlação das atividades de execução em loja com os dados de ponto de venda (PDV) para medir o impacto direto. SC: Requisitos de auditoria que necessitam de lógica personalizada ou componentes móveis sob medida. |  |  |  |
| CG-RE-002 | Como as visitas às lojas são planejadas? As rotas dos representantes são otimizadas? Baseia-se na prioridade da loja, eventos especiais ou SLAs? | S: Planejamento manual de visitas pelos representantes ou seus gerentes. M: Uso do Salesforce Maps para visualização de lojas e planejamento manual de rotas. L: Geração automática de planos de visita baseada em regras (ex. "visitar todas as lojas de nível A uma vez por semana"). XL: Otimização avançada de rotas que considera janelas de visita, durações de tarefas e SLAs para maximizar a eficiência diária. SC: Algoritmos de planejamento e roteamento personalizados que consideram variáveis complexas como o tráfego em tempo real ou previsões de vendas. |  |  |  |
| CG-TPM-001 | Como gerenciam as Promoções Comerciais (Trade Promotions)? Como asseguram que as promoções sejam executadas corretamente nas lojas? Como medem o ROI dessas promoções? | S: Gerenciamento de promoções em planilhas. M: Registro de promoções no Salesforce. Tarefas de auditoria para verificar a conformidade. L: Gerenciamento do ciclo de vida da promoção, incluindo o planejamento de fundos (Trade Promotion Management - TPM). XL: Análise do desempenho da promoção (aumento de vendas / sales uplift) através da integração com dados de vendas. SC: Modelos de Otimização de Promoções Comerciais (TPO) que usam IA para recomendar o melhor investimento promocional. |  |  |  |

## 4.5. Communications, Media & Tech (CMT)

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| CMT-COM-001 | (Comunicações) Descreva seu catálogo de produtos e serviços. Como são configuradas, empacotadas e precificadas as ofertas complexas (ex. um pacote de Internet, TV e Celular)? Usam um Catálogo de Produtos Empresarial (EPC)? | S: Catálogo de produtos simples com preços fixos. M: Uso de CPQ para configurar pacotes de produtos com regras de validação básicas. L: Implementação de um EPC (Catálogo de Produtos Empresarial) para modelar produtos, serviços e recursos de forma desacoplada, permitindo maior agilidade na criação de novas ofertas. XL: Lógica de preços e elegibilidade complexa baseada em atributos técnicos (ex. disponibilidade de fibra em um endereço) e comerciais. SC: Catálogo de produtos extremamente grande e dinâmico que requer um gerenciamento sofisticado do ciclo de vida do produto (PLM). |  |  |  |
| CMT-COM-002 | (Comunicações) Descreva seus processos de Mover, Adicionar, Alterar, Desconectar (MACD) para os serviços do cliente. Como a provisão dessas mudanças é orquestrada através de seus sistemas de rede (OSS/BSS)? | S: Processos MACD gerenciados manualmente fora do sistema. M: Uso do Salesforce Order Management para orquestrar fluxos de trabalho com tarefas manuais para a provisão. L: Decomposição automática de um pedido comercial em pedidos técnicos e orquestração automatizada da provisão através de integrações (MuleSoft). XL: Gerenciamento de mudanças em pedidos em andamento (in-flight) e tratamento de dependências complexas entre serviços. SC: Orquestração que requer a coordenação de múltiplos sistemas de provisionamento de diferentes fornecedores com lógica de compensação de falhas. |  |  |  |
| CMT-MED-001 | (Mídia) Como gerenciam a venda de espaços publicitários? Descreva o processo desde a proposta (RFP) até a ordem de inserção (IO). Como as tabelas de preços (rate cards) são definidas? | S: Processo manual gerenciado com documentos e planilhas. M: Criação de Planos de Mídia (Media Plans) no Salesforce com produtos e preços de um catálogo. L: Uso de tabelas de preços (rate cards) com preços que variam por múltiplas dimensões (audiência, faixa horária, etc.). XL: Integração com um Servidor de Anúncios (Ad Server) como o Google Ad Manager para verificar a disponibilidade de inventário em tempo real e enviar ordens de inserção. SC: Venda de publicidade programática ou modelos de leilão em tempo real (real-time bidding). |  |  |  |
| CMT-TECH-001 | (Alta Tecnologia) Qual é o seu modelo de receita principal (licenças perpétuas, assinaturas, baseado em uso, híbrido)? Como gerenciam o faturamento, o reconhecimento de receita e as renovações? | S: Modelo de vendas únicas (one-time). M: Modelo de assinatura simples com faturamento recorrente. L: Uso do Salesforce CPQ e Billing para gerenciar assinaturas, emendas, co-terminação e renovações. XL: Modelo de receita baseado no uso que requer a ingestão e mediação de dados de uso antes do faturamento. Gerenciamento do Reconhecimento de Receita segundo padrões como ASC 606. SC: Modelos de faturamento e receita extremamente complexos que exigem lógica personalizada ou integração com sistemas ERP financeiros especializados. |  |  |  |

## 4.6. Public Sector Solutions

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| PS-LIC-001 | Descreva o processo de solicitação e aprovação para as licenças e permissões que gerenciam. Que informação e documentação são exigidas dos solicitantes? Como as validações e revisões são realizadas? | S: Um único tipo de solicitação com um formulário simples e um processo de aprovação linear. M: Portal da Experience Cloud para que os cidadãos apresentem solicitações e carreguem documentos. L: Uso de Omniscripts para criar fluxos de solicitação guiados e dinâmicos. Integração com um motor de regras de negócio (BRE) para validações automáticas. XL: Processo de aprovação multi-etapa que envolve diferentes agências ou departamentos. Integração com gateways de pagamento governamentais. SC: Requisitos de conformidade regulatória muito rigorosos que exigem uma trilha de auditoria completa de cada passo do processo. |  |  |  |
| PS-INS-001 | Realizam inspeções para verificar a conformidade regulatória (ex. segurança, saúde)? Descreva o processo de uma inspeção, desde η programação até o registro de achados e a emissão de possíveis sanções. | S: Listas de verificação (checklists) de inspeção em papel ou em planilhas. M: Uso do aplicativo móvel do Salesforce para que os inspetores sigam listas de verificação e capturem dados em campo. L: Uso de Avaliações Dinâmicas (Dynamic Assessments) para guiar os inspetores através de questionários complexos com lógica condicional. XL: Geração automática de violações e ações de acompanhamento baseadas nos resultados da inspeção. Programação otimizada de inspeções. SC: Integração com dispositivos de medição ou sensores durante a inspeção. |  |  |  |
| PS-GRT-001 | Como gerenciam o ciclo de vida do Gerenciamento de Subsídios (Grants Management), desde a publicação da oportunidade de financiamento até a solicitação, revisão, adjudicação e monitoramento dos fundos? | S: Processo manual de gerenciamento de subsídios. M: Portal para que as organizações solicitem subsídios e acompanhem seu status. L: Fluxos de trabalho para a revisão e pontuação de solicitações por um comitê avaliador. XL: Gerenciamento do desembolso de fundos e acompanhamento de relatórios de progresso e do impacto dos projetos financiados. SC: Requisitos de relatórios financeiros e de conformidade para agências governamentais federais ou internacionais. |  |  |  |

## 4.7. Energy & Utilities Cloud

| **Id. da Pergunta** | **Pergunta de Descoberta** | **Guia de Complexidade e Tamanho** | **Resposta / Observações do Cliente** | **Impacto / Prioridade** | **Dimensionamento (S-M-L-XL-SC)** |
| --- | --- | --- | --- | --- | --- |
| EU-CPQ-001 | Como estão estruturadas suas tarifas para clientes residenciais e comerciais (B2C/B2B)? Dependem da localização, tipo de serviço, níveis de consumo, hora do dia (tarifas pico/vale) ou contratos de longo prazo? | S: Tarifas simples e planas. M: Preços escalonados baseados em níveis de consumo. L: Uso de CPQ para modelar tarifas complexas baseadas em atributos (ex. geografia, tipo de indústria) e regras de elegibilidade. XL: Preços e ofertas para grandes clientes comerciais (B2B) que exigem cotações multi-site e negociação de contratos. SC: Integração em tempo real com mercados atacadistas de energia para oferecer preços dinâmicos ou indexados. |  |  |  |
| EU-SVC-001 | Descreva os processos mais comuns em seu contact center. Como lidam com solicitações de ativação de novos serviços, desconexões, transferências ou consultas de faturamento? | S: Processos manuais onde os agentes consultam múltiplos sistemas. M: Uso do Console do Contact Center para uma visão 360 do cliente. Scripts simples para guiar os agentes. L: Orquestração de processos de ativação/desconexão/transferência através de flows que se integram com o sistema de faturamento e gerenciamento de serviços (CIS/Billing). XL: Portal de autoatendimento na Experience Cloud onde os clientes podem gerenciar esses processos eles mesmos. SC: Integração complexa com medidores inteligentes (smart meters) para consultas de consumo em tempo real. |  |  |  |
| EU-BILL-001 | Que sistema utilizam para o faturamento e gerenciamento de clientes (CIS/Faturamento)? Que informação deste sistema os agentes precisam ver no Salesforce (ex. histórico de faturas, consumo, status de pagamentos)? | S: Não é necessária integração; os agentes alternam entre sistemas. M: Integração somente leitura para mostrar um resumo da última fatura e o saldo. L: Visão do histórico completo de faturas e consumo. Capacidade de iniciar ações no sistema de faturamento (ex. solicitar uma segunda via da fatura) a partir do Salesforce. XL: Integração bidirecional que permite aos agentes realizar ações complexas como criar planos de pagamento ou gerenciar disputas de faturas diretamente no Salesforce. SC: O projeto implica substituir um sistema de faturamento legado por uma solução baseada no Salesforce (ex. Salesforce Billing). |  |  |  |

# Parte 5: Mapeamento de Requisitos para Capacidades do Salesforce (Análise V2)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Tomar o "Catálogo de Requisitos do Cliente" (gerado na Parte 1) como entrada.

Seu objetivo é mapear cada requisito às nuvens, produtos, indústrias e capacidades específicas do Salesforce que o satisfazem.

Instruções:

Análise de Requisitos: Revisar cada Requirement ID da Parte 1.

Mapeamento de Capacidades: Usar os documentos Guided Scoping Questions.pdf e EPICASCASOSDEUSOPROCESOSESPAÑOL.pdf como catálogo de referências principal.

Para cada requisito, identificar a Salesforce Cloud / Industry, Salesforce Domain e Salesforce Capability específica (ex. Enterprise Product Catalog (EPC), Ad Server Integration) que é necessária.

Justificativa: Fornecer uma breve justificativa de por que a capacidade selecionada aborda o requisito.

Formato de Saída: Apresentar os resultados exclusivamente em uma tabela Markdown.

| **Id. Requisito** | **Descrição do Requisito** | **Salesforce Cloud / Indústria** | **Salesforce Domain** | **Salesforce Capability** | **Justificativa do Mapeamento** |
| --- | --- | --- | --- | --- | --- |
| REQ-XXX-001 | ... | (ex. Media Cloud) | (ex. Advertising Sales Management (ASM)) | (ex. Enterprise Product Catalog (EPC)) | (ex. O EPC do Media Cloud é projetado para modelar produtos de mídia multicanal complexos.) |
| ... | ... | ... | ... | ... | ... |

# Parte 6: Mapeamento de Requisitos para Épicos e Casos de Uso (Análise V2)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Estender o mapeamento da Parte 5. Para cada requisito, identificar TODOS os Épicos e Casos de Uso relevantes que detalham a implementação da capacidade do Salesforce.

Instruções:

Referência Cruzada: Usar o mapeamento de capacidades da Parte 5 como ponto de partida.

Identificação de Épicos e Casos de Uso: Consultar os documentos Guided Scoping Questions.pdf e EPICASCASOSDEUSOPROCESOSESPAÑOL.pdf.

Para cada capacidade do Salesforce identificada, extrair o Épico relevante e TODOS os Casos de Uso que se alinhem com o requisito do cliente.

Formato de Saída: Apresentar os resultados exclusivamente em uma tabela Markdown.

| **Id. do Requisito** | **Salesforce Capability** | **Épico** | **Caso de Uso** |
| --- | --- | --- | --- |
| REQ-XXX-001 | ... | (ex. Gestão Unificada do Catálogo de Inventário...) | - Como gerente de produto, quero definir e manter um catálogo mestre... |
| ... | ... | ... | ... |

# Parte 7: Mapeamento de Requisitos para Processos (Análise V2)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Estender o mapeamento da Parte 5. Para cada requisito, identificar TODOS os Processos de Negócio relevantes que detalham a implementação.

Instruções:

Referência Cruzada: Usar o mapeamento de capacidades da Parte 5 como ponto de partida.

Identificação de Processos: Se o documento de referência incluir mapas de processos (ex. Mapa "To-Be"), identificar TODOS os processos de negócio de Nível 1 (L1) a Nível 5 (L5) que são impactados pelo requisito.

Formato de Saída: Apresentar os resultados exclusivamente em uma tabela Markdown.

| **Id. do Requisito** | **Processo L1** | **Processo L2** | **Processo L3** | **Processo L4** | **Processo L5** |
| --- | --- | --- | --- | --- | --- |
| REQ-XXX-001 | (ex. Lead-to-Cash) | (ex. Quote-to-Order) | (ex. VENDER) 1 | ... | ... |
| ... | ... | ... | ... | ... | ... |

# Parte 8: Análise de Lacunas (Gaps) e Questionário ao Cliente (Análise V2)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Realizar uma análise de lacunas sistemática. A fonte principal de lacunas são todas as perguntas marcadas como "Não detalhado nos documentos" nas Partes 2, 3 e 4. Seu objetivo é converter essas lacunas de informação em um questionário priorizado para o cliente.

Instruções:

Identificação de Lacunas (Gap): Revisar as Partes 2, 3 e 4. Cada pergunta marcada como "Não detalhado" é uma lacuna (Gap).

Documentar esta lacuna (ex. "Detalhes sobre o processo de qualificação de Leads G-BIZ-002 não encontrados").

Análise Comparativa (USB): Avaliar se a informação coletada nas Partes 1-7 é suficiente para as seções-chave do USB - UNIFIED SOLUTION BLUEPRINT (ex. 3.2 Diagrama de Integração, 3.5 Modelo de Dados).

Se faltar informação, registrá-la como uma lacuna.

Mapeamento de Riscos: Para cada lacuna, consultar o documento Risk Breakdown Structure 1.0.xlsx e identificar o risco de projeto associado (ex. "A1 - Infraestrutura Técnica Complexa").

Geração de Perguntas: a. (Base) Formular uma pergunta direta para fechar a lacuna. b.

(Aumento) Consultar o Guided Scoping Questions.pdf e as perguntas originais das Partes 2, 3 e 4 para encontrar perguntas de acompanhamento detalhadas.

c. (Web Search) Realizar buscas web específicas para encontrar perguntas adicionais de melhores práticas da indústria que não estejam cobertas nos documentos de referência, para enriquecer o questionário.

d. (Formato) Assegurar UMA PERGUNTA POR LINHA.

Priorização: Atribuir uma prioridade (Alta, Média, Baixa) ao grupo de perguntas (todas as linhas relacionadas à mesma lacuna terão a mesma prioridade) com base na gravidade do risco.

Formato de Saída (Markdown): Apresentar os resultados exclusivamente em uma tabela Markdown (esta tabela é o entregável "exportável").

Repetir a informação de Prioridade, Seção Afetada, Lacuna e Risco para cada linha de pergunta relacionada à mesma lacuna.

Formato de Saída (XLS): (Instrução para a IA do Prompt Mestre) Gerar um arquivo questions\_export.xls com as colunas: Priority, Affected USB Section, Information Gap Identified, Associated Risk, Questions for the Client.

| **Prioridade** | **Solução USB Afetada** | **Lacuna de Informação Identificada** | **Risco Associado** | **Pergunta para o cliente** |
| --- | --- | --- | --- | --- |
| Alta | (ex. 3.2 Diagrama de sistema e integração) | (ex. Detalhes de Integração MDS: Especificações técnicas da API são desconhecidas.) | (ex. A1 - Infraestrutura técnica complexa; C3 - Complexidade de dados desconhecida) | Pode fornecer a documentação técnica completa da API (ex. OpenAPI/Swagger) para o sistema MDS? |
| Alta | (ex. 3.2 Diagrama de sistema e integração) | (ex. Detalhes de Integração MDS: Especificações técnicas da API são desconhecidas.) | (ex. A1 - Infraestrutura técnica complexa; C3 - Complexidade de dados desconhecida) | Que método de autenticação a API do MDS utiliza (ex. OAuth 2.0, API Key)? |
| Média | (ex. 3.4 Capacidades) | (ex. Geração de "Testemunhas": Requisito personalizado. Viabilidade técnica não definida.) | (ex. A2 - São necessárias personalizações significativas) | Poderia descrever o processo técnico atual para gerar "testemunhas"? |
| ... | ... | ... | ... | ... |

# Parte 9: Estimativa Preliminar de Complexidade e Tamanho (Análise V2)

## 9.1 Resumo da Estimativa

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer o resumo executivo final da estimativa.

Instruções:

Basear-se unicamente na linha 'Estimativa Geral' gerada na tabela da Seção 9.2 e apresentá-la aqui como um texto conciso.

Formato de Saída: Texto conciso indicando a estimativa geral (ex. "Estimativa Geral do Projeto: Extra Grande (XL)").

## 9.2 Estimativa de Alto Nível

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer a estimativa de alto Nível detalhada, sintetizando todos os achados do documento.

Instruções:

Avaliação Holística: Preencher cada linha da tabela Dimensão de Complexidade com base na informação coletada nas Partes 1 a 8.

Síntese de Estimativas: Para as linhas relevantes, incorporar e resumir as estimativas já geradas nas seções 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 9.10 e 9.11.

Classificação: Usar as definições da Seção 0 (Tabelas 0.1 e 0.2) para atribuir uma classificação (S, M, L, XL ou SC) a cada dimensão.

Estimativa Geral: Calcular a linha Estimativa Geral com base no peso de todas as dimensões anteriores.

Justificativa: Fornecer um resumo narrativo que justifique a Estimativa Geral (que será utilizada em 9.1), destacando os principais fatores de complexidade.

Formato de Saída: Apresentar a tabela de estimativa primeiro, seguida do resumo narrativo.

| **Dimensão de Complexidade** | **Estimativa (S, M, L, XL, SC)** | **Breve Justificativa (Fatores Chave)** |
| --- | --- | --- |
| **Dimensão 1: Escopo Funcional e de Negócios** |  |  |
| Complexidade Estratégica e de Negócios (Ref. 2.1) |  | (ex. KPIs estratégicos (XL), Múltiplas BUs (L)) |
| # de Nuvens Salesforce e Complexidade Funcional (Ref. 3.x) |  | (ex. 3 Nuvens (L), Processos complexos no Service Cloud (L)) |
| Complexidade de Indústria (Vertical) (Ref. 4.x) |  | (ex. Requer Health Cloud (L), Modelo de dados FHIR (XL)) |
| Nível de Personalização (OOTB vs. SC) (Ref. 0.1 / 9.5) |  | (ex. Lógica de negócios em Apex (L), Componente LWC (SC)) |
| **Dimensão 2: Arquitetura e Dados** |  |  |
| # de Integrações e Complexidade (Ref. 2.4 / 3.9) |  | (ex. 6 integrações (L), Requer Middleware (L)) |
| Complexidade de Dados e Migração (Ref. 2.4 / 9.7) |  | (ex. Múltiplas fontes (XL), >1M registros (L), Qualidade de dados (L)) |
| Complexidade de Arquitetura e Segurança (Ref. 2.4 / 9.11) |  | (ex. Requer Shield (L), Conformidade HIPAA (L)) |
| Estratégia de Coexistência (Ref. 9.8) |  | (ex. ERP é CoM, requer sincronização bidirecional (L)) |
| **Dimensão 3: Entrega e Organização** |  |  |
| Impacto Organizacional (Usuários) (Ref. 0.2 / 2.1) |  | (ex. >1000 usuários (XL), Transformação empresarial (XL)) |
| # de Papéis de Usuário e Personas (Ref. 2.1) |  | (ex. 8 papéis (L), Inclui usuários externos (XL)) |
| Maturidade de Governança e Metodologia (Ref. 2.2 / 9.6) |  | (ex. Governança fragmentada (SC), Sem PMO (L)) |
| Gestão da Mudança e Adoção (Ref. 2.3) |  | (ex. Cultura resistente (L), Sem plano de comunicação (L)) |
| Estratégia de Implantação (DevOps) (Ref. 2.2 / 9.9) |  | (ex. Múltiplos fluxos paralelos (XL), Requer DevOps (L)) |
| Estratégia de Testes (Ref. 9.10) |  | (ex. Testes E2E complexos (L), Testes de integração (L)) |
| **Dimensão 4: Risco do Projeto** |  |  |
| Nível de Lacunas (Gaps) e Riscos (Ref. 8) |  | (ex. Múltiplas lacunas "Altas" em integração e dados (L)) |
|  |  |  |
| **Estimativa Geral** | **...** |  |

(Justificativa Narrativa aqui...)

## 9.3 Estimativa por Capacidades

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade em nível de capacidades.

Instruções:

Avaliação: Considerar a dificuldade de configuração, desenvolvimento e integrações para cada capacidade identificada na Parte 5.

Classificação: Atribuir uma Complexity, Size (S, M, L, XL, SC) e uma Estimation (justificativa) para cada capacidade, usando o Sizing Framework (Seção 0).

Formato de Saída: Apresentar a tabela de estimativa.

| **Requirement ID** | **Salesforce Capability** | **Relevant Epic** | **Example Use Cases** | **Complexity** | **Size (S-XL-SC)** | **Estimation** |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-XXX-001 | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |

## 9.4 Estimativa por Processos

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade em nível de processo.

Instruções: Avaliar a dificuldade de configuração, desenvolvimento e integrações para cada processo de negócio identificado na Parte 7. Atribuir Complexity e Size (S, M, L, XL, SC) usando o Sizing Framework (Seção 0).

Formato de Saída: Tabela.

| **Requirement ID** | **L1 Process** | **L2 Process** | **L3 Process** | **L4 Process** | **L5 Process** | **Complexity** | **Size (S-XL-SC)** | **Estimation** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-XXX-001 | ... | ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## 9.5 Estimativa de Personalização de Dados (Data Customizing)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Personalização de Dados.

Instruções: Avaliar a dificuldade dos desenvolvimentos, extensões e configurações do modelo de dados com base nos requisitos das Partes 3 e 4.

Atribuir Complexity e Size (S, M, L, XL, SC) usando o Sizing Framework (Seção 0).

Formato de Saída: Tabela.

| **Requirement ID** | **Salesforce Object** | **Complexity** | **Size (S-XL-SC)** | **Estimation** |
| --- | --- | --- | --- | --- |
| REQ-XXX-001 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## 9.6 Estimativa de Governança e COE

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Governança e o Centro de Excelência (COE).

Instruções: Avaliar a dificuldade de estabelecer a governança necessária, com base no impacto organizacional, no número de papéis e na maturidade da metodologia (baseado nos achados das Partes 2.1, 2.2 e 2.3).

Não fazer referência à Tabela 9.2.

Atribuir um tamanho utilizando o Sizing Framework (S, M, L, XL, SC) e justificar.

Formato de Saída: Texto narrativo.

## 9.7 Estimativa de Migração de Dados

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Migração de Dados.

Instruções: Avaliar a dificuldade com base unicamente nos achados das Partes 2, 3 e 4 (ex. G-TEC-003, G-TEC-005), no número de fontes, na qualidade dos dados (identificada na Parte 8) e no volume de registros históricos.

Não fazer referência à Tabela 9.2.

Atribuir um tamanho utilizando o Sizing Framework (S, M, L, XL, SC) e justificar.

Formato de Saída: Texto narrativo.

## 9.8 Estimativa de Estratégia de Coexistência (Co-Living)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Estratégia de Coexistência.

Instruções: Avaliar a dificuldade de manter sistemas coexistindo (se aplicável), com base na complexidade das integrações (Parte 3.9) e na definição dos Sistemas de Registro (Parte 2.4, ex. G-TEC-001).

Não fazer referência à Tabela 9.2.

Atribuir um tamanho utilizando o Sizing Framework (S, M, L, XL, SC) e justificar.

Formato de Saída: Texto narrativo.

## 9.9 Estimativa de Estratégia de Implantação e Implementação

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Estratégia de Implantação e Implementação. 1

Instruções: Avaliar a dificuldade com base na governança (Parte 2.2), na metodologia (Agile/Waterfall) e no Nível de Personalização (determinado pelos achados das Partes 3 e 4).

Não fazer referência à Tabela 9.2.

Atribuir um tamanho utilizando o Sizing Framework (S, M, L, XL, SC) e justificar. 1

Formato de Saída: Texto narrativo.

## 9.10 Estimativa de Estratégia de Testes (Testing)

**Prompt de IA Generativa (para preencher esta seção):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Estratégia de Testes.

Instruções: Avaliar a dificuldade com base no número de integrações (Parte 2.4 / 3.9), no nível de personalização (SC), na quantidade de processos de ponta a ponta (Parte 7) e nos volumes de dados (Parte 2.4).

Não fazer referência à Tabela 9.2.

Atribuir um tamanho utilizando o Sizing Framework (S, M, L, XL, SC) e justificar.

Formato de Saída: Texto narrativo.

## 9.11 Estimativa de Estratégia de Segurança

**Prompt de IA Generativa (para preencher estacão):**

Persona: Atuar como uma equipe multidisciplinar da Salesforce (Arquiteto de Soluções Especialista, Arquiteto Técnico Especialista, Gerente de Engajamento Especialista, Analista de Negócios Principal, Gerente de Entrega, Arquiteto Corporativo, Engenheiro de Soluções, Arquitetos de Dados, Arquitetos de Integração, Arquitetos de Segurança, Especialistas em QA, Especialistas Funcionais e de Negócios e SMEs, e um Gerente de Programa).

Tarefa: Fornecer uma estimativa preliminar do tamanho e da complexidade para a Estratégia de Segurança.

Instruções:

Avaliação Holística: Revisar os requisitos de segurança identificados na Parte 1 (Requisitos Categoria SEC) e na Parte 2.4 (G-TEC-004).

Considerar os seguintes aspectos:

Conformidade Regulatória: Padrões específicos mencionados (GDPR, CCPA, HIPAA, etc.). 1

Criptografia: Necessidade de criptografia em trânsito e em repouso (ex. Salesforce Shield Platform Encryption). 1

Identidade e Acesso: Complexidade da integração com provedores de identidade (Okta, etc.), requisitos de SSO, gerenciamento de usuários (SailPoint) e modelo de papéis/perfis.

1

Residência de Dados: Requisitos geográficos específicos. 1

Monitoramento e Auditoria: Necessidade de rastreamento avançado (ex. Shield Event Monitoring, Field Audit Trail).

Segurança Personalizada: Requisitos que excedem as capacidades padrão. 1

Classificação: Utilizar as definições estabelecidas na Seção 0 (Sizing Framework Definition) para atribuir um tamanho global (S, M, L, XL, SC) para a estratégia de segurança.

Não fazer referência à Tabela 9.2.

Justificativa: Fornecer um resumo narrativo que justifique a estimativa, destacando os principais impulsionadores de complexidade (ex. "A necessidade de cumprir com a HIPAA 1 requer a implementação do Salesforce Shield (L), e a integração complexa com Okta e SailPoint 1 para SSO e provisionamento adiciona complexidade (L), resultando em uma estimativa geral de 'L'").

Formato de Saída: Texto narrativo.
