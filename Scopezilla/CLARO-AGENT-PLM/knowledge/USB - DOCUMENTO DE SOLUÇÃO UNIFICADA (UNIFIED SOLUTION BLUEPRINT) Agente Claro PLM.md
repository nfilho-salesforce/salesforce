# USB - DOCUMENTO DE SOLUÇÃO UNIFICADA (UNIFIED SOLUTION BLUEPRINT)

**Cliente:** Claro Brasil

**Projeto:** POC PLM & Agentforce – Claro

**Versão:** 2.0

**Data:** 2026

**Classificação:** Restrito / Técnico Corporativo

### 1. O Mandato Estratégico

#### 1.1. Resumo Executivo e Declaração de Visão

**Resumo Executivo:**

* **O Imperativo para a Mudança:** O ecossistema de telecomunicações da Claro opera sob um cenário de alta complexidade regulatória e comercial, enfrentando desafios críticos com a ineficiência na manutenção do catálogo BRE legado (atualmente composto por 127 regras complexas), sobrecarga recorrente do tempo de CPU da plataforma e potenciais riscos de estouro de heap memory durante validações volumosas. A necessidade urgente de reduzir o tempo de diagnóstico de catálogos e eliminar a necessidade de redeploys manuais e custosos para cada alteração de regra operacional torna imperativa uma modernização arquitetural guiada por inteligência artificial e processamento ágil assíncrono.
* **A Solução Proposta e o Valor:** A arquitetura estratégica recomendada estabelece a implementação da Prova de Conceito (POC) PLM & Agentforce. A solução introduz uma arquitetura *async-first* para a ingestão massiva e processamento resiliente de planilhas de demanda via LWCs e Queueables encadeados, combinada a um interpretador de regras lógicas determinístico escrito em Apex puro (PlmRuleSpecEvaluator) capaz de executar validações lógicas complexas em memória com tempo de resposta inferior a 50 milissegundos por registro. Complementarmente, o ConnectApi integrará os Prompt Templates do Einstein para compilação automatizada de regras lógicas descritas em linguagem natural (DSL pt-BR) diretamente para o formato AST JSON estruturado, eliminando a necessidade de novos deploys sistêmicos. A operação será controlada por dois agentes cognitivos autônomos Agentforce (Employee Agents): o Agente Admin, focado em compile-time para governança e compilação de metadados, e o Agente Ops, focado em runtime para diagnósticos automatizados em lotes e emissão de relatórios textuais HTML. Isso melhorará radicalmente os KPIs operacionais: o Tempo de Execução de Avaliação de Regras (**KPI-TI-001**) passará de minutos para menos de 50 milissegundos por registro, e o tempo de autoria e atualização de regras (**KPI-TI-002**) será reduzido a 0 minutos, eliminando redeploys.
* **O Caminho a Seguir:** Esta iniciativa adota um plano de execução ágil e focado com um cronograma fixo e inegociável de 8 semanas de duração total (subdividido em 2 semanas de discovery/design, 3 semanas de desenvolvimento concentrado e 3 semanas de ciclos de homologação e UAT). A governança integrada do ecossistema garantirá alta produtividade comercial ao mesmo tempo em que blinda a infraestrutura principal da Claro contra falhas por meio de ganchos de resiliência ativa (Dead Letter Queues, snapshots de compilação e Transaction Finalizers), mitigando os riscos operacionais de esteiras cross-org (CannotQuickDeployError) e assegurando alto retorno de valor econômico sustentável.

**Declaração de Visão:** "Posicionar a Claro na vanguarda do setor de telecomunicações através de um catálogo unificado, inteligente e autônomo, que erradica a complexidade das regras manuais legadas e automatiza fluxos do produto ao dinheiro sem dependência de deploys."

#### 1.2. Principais impulsionadores de negócios que originam a necessidade desta iniciativa

|  |  |  |
| --- | --- | --- |
| **Macrotema** | **Impulsionador de Negócio** | **Evidência / Justificativa Estratégica** |
| **Excelência Operacional** | Redução do Tempo de Diagnóstico de Catálogos | Demanda por otimizar a identificação de erros de regras em cargas massivas de dados. |
| **Excelência Operacional** | Eliminação de Redeploys Sistêmicos | Necessidade de alterar regras operacionais em runtime sem depender de janelas de deploy técnico. |
| **Excelência Operacional** | Mitigação de Sobrecarga de CPU e Heap Memory | Resolução de travamentos causados por processamento ineficiente síncrono de grandes arquivos. |
| **Experiência do Cliente** | Autoria Self-Service de Regras | Permitir que analistas operacionais atualizem ofertas promocionais rapidamente via linguagem natural. |
| **Experiência do Cliente** | Resolução Veloz de Inconsistências de Catálogo | Minimizar falhas ocultas no catálogo comercial antes que afetem as ofertas no carrinho final. |
| **Crescimento da Receita** | Agilidade no Lançamento de Combos | Reduzir o Time-to-Market (TTM) de produtos convergentes que integram frentes distintas (Fone, BL, TV). |
| **Inovação Contínua** | Adoção de IA Cognitiva e Autônoma | Introduzir a inteligência agêntica do Agentforce e Einstein LLM no back-office corporativo. |
| **Risco e Conformidade** | Observabilidade Avançada em Processos Batch | Exigência de logs resilientes, DLQs e snapshots para mitigar falhas em rotinas noturnas. |
| **Risco e Conformidade** | Governança de Artigos de Conhecimento | Saneamento e organização de taxonomias corporativas sob as diretrizes de compliance da Claro. |
| **Excelência Operacional** | Superação de Limitações Físicas de Infraestrutura | Necessidade de contornar a proibição do uso de partições de Platform Cache nas instâncias core. |

* **Excelência Operacional:**
  + Redução do tempo de diagnóstico de catálogos para garantir eficiência interna.
  + Eliminação de redeploys para alterações simples de regras operacionais.
  + Otimização de performance de CPU através de arquiteturas assíncronas dedicadas.
  + Resolução de restrições de cache nos ambientes STORM\_PLM e Ibuy.
* **Experiência do Cliente:**
  + Autoria ágil baseada em IA para resposta instantânea às demandas de canais comerciais.
  + Mitigação de erros de faturamento ou quebras cadastrais causados por prateleiras desatualizadas.
* **Crescimento da Receita:**
  + Redução drástica do Time-to-Market (TTM) na publicação de novas campanhas convergentes.
* **Risco e Conformidade:**
  + Blindagem de transações corporativas massivas usando snapshots e Dead Letter Queues.
  + Governança estrita de artigos de conhecimento de atendimento.

#### 1.3. Principais desafios a serem enfrentados

|  |  |  |
| --- | --- | --- |
| **Categoria do Desafio** | **Desafio Mapeado** | **Impacto Negativo nos Negócios / Evidência** |
| **Desafios de Negócios** | Rigidez na Atualização do Catálogo Legado | A Claro convive com um catálogo BRE legado de 127 regras complexas e engessadas, tornando a inovação lenta e dependente de TI. |
| **Desafios de Negócios** | Risco de Silos Operacionais no Projeto | Incerteza e indefinição sobre a alocação de um papel dedicado de Gerente de Projeto (PM), ameaçando marcos do cronograma de 8 semanas. |
| **Desafios Operacionais** | Processamento Manual Ineficiente de Demandas | Cargas volumosas de dados são baseadas em layouts CSV extensos, gerando gargalos operacionais e erros de conciliação. |
| **Desafios Operacionais** | Desorganização na Base de Conhecimento Interna | Necessidade latente de saneamento, higienização e definição de Data Categories para os Knowledge Articles corporativos. |
| **Desafios Tecnológicos** | Dívida Técnica e Limitações de Infraestrutura | Proibição explícita do uso de Platform Cache nos ambientes core STORM\_PLM e Ibuy, forçando o desenho de caches manuais. |
| **Desafios Tecnológicos** | Riscos de Estouro de Limites de Governabilidade | Arquivos CSV volumosos com ameaça constante de estourar a Heap Memory da org ou o limite de tempo síncrono de CPU. |
| **Desafios Tecnológicos** | Complexidade de DevOps e Erros de Deploy Cross-Org | Erros frequentes de deploy cross-org (CannotQuickDeployError), exigindo execução mandatória manual de rotinas complexas de teste. |

* **Dívida técnica e sistemas legados:** A dependência das velhas estruturas e a complexidade na manutenção de 127 regras do catálogo BRE geram ineficiências operacionais e sobrecarga técnica contínua.
* **Complexidade de integração e coexistência:** Necessidade de conexão dinâmica com o sistema de propensão externo NBO para o funcionamento pleno do Agente 3, sob risco de instabilidade ou indisponibilidade de barramentos.
* **Qualidade e migração de dados:** O risco de ineficácia nas respostas automatizadas da inteligência artificial caso os artigos de conhecimento fornecidos pela Claro não passem por uma higienização profunda prévia.

#### 1.4. Objetivos de negócios e métricas de sucesso (KPIs)

|  |  |  |
| --- | --- | --- |
| **Objetivo de Negócio (SMART)** | **Métrica de Sucesso (KPI)** | **Valor-Alvo / Cronograma** |
| Reduzir drasticamente o tempo de ciclo operacional gasto na execução e avaliação de regras lógicas de catálogo de produtos Claro. | Tempo de Execução de Avaliação de Regras por Registro (**KPI-TI-001**). | Menor que 50 milissegundos por registro / Conclusão em 8 semanas. |
| Eliminar o tempo de indisponibilidade e dependência de TI para atualização de regras operacionais de catálogo através de autoria por IA. | Tempo de Autoria e Atualização de Regras de Negócio (**KPI-TI-002**). | 0 minutos (Sem necessidade de redeploy técnico) / Em produção no encerramento do projeto. |
| Otimizar a capacidade síncrona de absorção de itens de prateleira por lote operacional sem estourar limites de CPU Salesforce. | Capacidade de Ingestão de Itens por Lote (**KPI-OPS-001**). | Suportar lotes síncronos de até 10.000 linhas por arquivo CSV de Demanda / Validável em UAT. |
| Garantir o processamento seguro de Large Data Volumes (LDV) em arquivos de demanda corporativos carregados na interface. | Volume máximo de caracteres lidos em string de planilha CSV sem quebras de Heap Memory. | Teto de 6.000.000 de caracteres processados via arquitetura *async-first* / 8 semanas. |
| Unificar e segregar com precisão absoluta as regras de validação por criticidade operacional. | Percentual de regras devidamente categorizadas em canais de severidade (ERRO, AVISO, INFO). | 100% de aderência conceitual mapeada por Tipo de Produto (Fone, BL, TV) / Fase de Build. |
| Assegurar a prontidão de artigos de conhecimento para o suporte agêntico de IA. | Total de FAQs corporativas analíticas saneadas e prontas com estruturas de Data Categories. | Fornecimento inicial de 10 a 15 FAQs totalmente estruturadas pela Claro / Início do Build. |
| Neutralizar riscos de estouro de governos ou transações zumbis na fila assíncrona da org. | Percentual de execuções com falha capturadas preventivamente por mecanismos de contingência. | 100% de cobertura de erros via Dead Letter Queue (DLQ) e rotinas do PimZombieReaperService / Sprints de Desenvolvimento. |
| Contornar de forma absoluta a indisponibilidade de Platform Cache nos ambientes STORM\_PLM e Ibuy. | Percentual de dados de regras lidos com sucesso através de mecanismos alternativos persistidos. | 100% via estruturas estáticas de Maps em memória estável Apex / Fase de Build. |
| Mitigar atrasos nas esteiras de DevOps causados por erros severos de deploy cross-org. | Taxa de sucesso de deploys em sandboxes utilizando diretrizes específicas de teste unitário. | 100% de builds executados com sucesso através do parâmetro RunSpecifiedTests / Ciclos de Deploy. |
| Validar a eficácia operacional das respostas e diagnósticos cognitivos autônomos gerados para as personas Claro. | Índice de acerto nas interações guiadas dos agentes em compile-time e runtime operacionais. | 95% de precisão nos diagnósticos emitidos pelos Agentes Admin e Ops / Ciclo de UAT. |

#### 1.5. Principais partes interessadas e campeões do projeto

|  |  |  |  |
| --- | --- | --- | --- |
| **Nome** | **Título** | **Função no Projeto** | **Contato (se disponível)** |
| Lucas | Especialista de Descoberta / SME Técnico | Key Subject Matter Expert (SME) do Cliente. | *Disponível em workshops* |
| Luciano | Líder SWE Claro | Proprietário de Infraestrutura e Gestão do Cliente. | *Foco em PM compartilhado* |
| Fabrício | Líder Core de Operações Claro | Patrocinador Operacional / Alinhamento de Equipe. | *Foco em times de Negócio* |
| Equipe Professional Services | Especialistas Salesforce LATAM | Time Core de Entrega (1 TA, 1 TC, 1.5 QA). | *Alocação dedicada 8 semanas* |

#### 1.6. Registro de Valores e KPIs (Linha de Base → Meta habilitada pela Solução)

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID do KPI** | **Nome do KPI** | **Processo (Nível 1–Nível 5)** | **Linha de base** | **Unidade da linha de base** | **Meta** | **Unidade da meta** | **Direção** | **Alavanca de valor** | **Confiança** | **Fonte de dados** | **Casos de uso/Épicos** | **Recurso do Salesforce** |
| **KPI-TI-001** | Tempo de Execução de Avaliação de Regras | Product Lifecycle Management -> Validação de Catálogo -> Execução de Regras | *Não detalhado* | minutos | < 50 | milissegundos por registro | Minimizar | PRODUCTIVITY | Alta | Discovery p.5 (CR6). | Avaliação em Runtime de Lotes | Apex AST Walker puro. |
| **KPI-TI-002** | Autoria e Atualização de Regras de Negócio | Product Lifecycle Management -> Governança de Catálogo -> Atualização de Regra | *Não detalhado* | dias (Requer deploy) | 0 | minutos (Sem redeploy) | Minimizar | PRODUCTIVITY | Alta | Discovery p.3 (2.2). | Autoria Self-Service de Regras | Agentforce Admin + Einstein LLM. |
| **KPI-OPS-001** | Capacidade de Ingestão de Itens por Lote | Product Lifecycle Management -> Operações de Catálogo -> Carga de Dados | *Não detalhado* | linhas | <= 10.000 | linhas por lote síncrono | Maximizar | COST\_REDUCTION | Média | Discovery p.4 (TC4). | Importação de CSV Volumoso | Wizard LWC + Queueable encadeado. |

Snippet de código

[
 {
 "kpi\_id": "KPI-TI-001",
 "name": "Tempo de Execução de Avaliação de Regras",
 "process\_l1\_l5": "Product Lifecycle Management -> Validação de Catálogo -> Execução de Regras",
 "baseline\_value": null,
 "baseline\_unit": "minutos",
 "target\_value": 50,
 "target\_unit": "milissegundos por registro",
 "improvement\_direction": "Minimizar",
 "value\_lever": "PRODUCTIVITY",
 "confidence": "Alta",
 "data\_source": "Discovery com Lucas, p.5 (CR6)",
 "related\_use\_cases": "Avaliação em Runtime de Lotes",
 "related\_epics": "Execução Determinística Apex",
 "salesforce\_capability": "Apex AST Walker puro"
 },
 {
 "kpi\_id": "KPI-TI-002",
 "name": "Autoria e Atualização de Regras de Negócio",
 "process\_l1\_l5": "Product Lifecycle Management -> Governança de Catálogo -> Atualização de Regra",
 "baseline\_value": null,
 "baseline\_unit": "dias (Requer deploy)",
 "target\_value": 0,
 "target\_unit": "minutos (Sem redeploy)",
 "improvement\_direction": "Minimizar",
 "value\_lever": "PRODUCTIVITY",
 "confidence": "Alta",
 "data\_source": "Discovery com Lucas, p.3 (2.2)",
 "related\_use\_cases": "Autoria Self-Service de Regras",
 "related\_epics": "Compilação GenAI Assistida",
 "salesforce\_capability": "Agentforce Admin + Einstein LLM"
 },
 {
 "kpi\_id": "KPI-OPS-001",
 "name": "Capacidade de Ingestão de Itens por Lote",
 "process\_l1\_l5": "Product Lifecycle Management -> Operações de Catálogo -> Carga de Dados",
 "baseline\_value": null,
 "baseline\_unit": "linhas",
 "target\_value": 10000,
 "target\_unit": "linhas por lote síncrono",
 "improvement\_direction": "Maximizar",
 "value\_lever": "COST\_REDUCTION",
 "confidence": "Média",
 "data\_source": "Discovery com Lucas, p.4 (TC4)",
 "related\_use\_cases": "Importação de CSV Volumoso",
 "related\_epics": "Ingestão Massiva de Dados",
 "salesforce\_capability": "Wizard LWC + Queueable encadeado"
 }
]

### 2. Análise do Estado Atual

Esta seção fornece uma análise abrangente da realidade operacional atual da Claro Brasil voltada para a gestão de catálogos e ciclo de vida de produtos (PLM). Ela documentará os processos de negócios existentes, o cenário tecnológico subjacente e os pontos problemáticos resultantes que geram sobrecarga de CPU e dívida técnica estrutural. O objetivo desta análise é estabelecer uma linha de base clara e baseada em evidências, com base na qual o valor e o sucesso da transformação proposta com o Agentforce serão medidos.

#### 2.1. Processos de negócios e fluxos de valor existentes

##### 2.1.1 Processo de Governança de Catálogo e Criação de Regras (As-Is)

* **Proprietário do Processo:** Equipe de Administração e Arquitetura de Catálogo Claro.
* **Meta:** Traduzir critérios comerciais textuais e precificações de planos em regras operacionais ativas na prateleira sistêmica.
* **Narrativa do Processo:** O processo inicia-se de forma passiva quando as frentes de negócios demandam novos pacotes ou restrições promocionais para produtos convergentes. Os analistas redigem os critérios lógicos manualmente em documentos textuais. Na sequência, a equipe de TI realiza o mapeamento programático dessas premissas lógicas, gerando codificações rígidas e ganchos complexos em um motor de regras legado (BRE com 127 regras complexas). Para que as novas diretrizes entrem em vigor, o fluxo exige a execução manual e exaustiva de deploys entre ambientes da Claro corporativa, culminando em lentidões operacionais severas e indisponibilidade ágil de prateleiras.
* **Principais Etapas, Atores e Sistemas:**
  1. Elaboração e redação em texto livre das premissas de novos planos. **Ator:** Analista de Ofertas. **Sistema:** Documentações locais.
  2. Codificação manual programática e reengenharia de dependências de catálogo. **Ator:** Desenvolvedor de TI. **Sistema:** Catálogo BRE Legado.
  3. Execução de pacotes de deploy cross-org e testes de regressão sistêmicos. **Ator:** Engenheiro DevOps. **Sistema:** Ambientes Claro (STORM\_PLM e Ibuy).

Snippet de código

graph TD
 A[1. Elaboração Textual de Premissas de Planos] --> B[2. Codificação Manual no BRE Legado]
 B --> C[3. Deploy Cross-Org nos Ambientes Claro]
 C --> D{Sucesso no Deploy?}
 D -- Sim --> E[Regras Ativas na Org]
 D -- Não --> F[Gargalo Técnico / Erros de Sincronização]

#### 2.2. Pontos problemáticos e ineficiências identificados

* Ineficiência crítica e alta morosidade na manutenção e sustentação do catálogo BRE legado de 127 regras.
  + Etapa(s) do Processo Afetada(s): Codificação manual e sustentação de dependências de prateleiras.
  + Impacta(m) Objetivo(s) de Negócios: Eliminar o tempo de indisponibilidade e mitigar a dependência crônica de TI para atualizações básicas.
* Sobrecarga extrema do tempo síncrono de CPU e travamentos por estouro de Heap Memory em validações massivas.
  + Etapa(s) do Processo Afetada(s): Carga massiva de planilhas de demanda corporativas.
  + Impacta(m) Objetivo(s) de Negócios: Suportar processamentos de Large Data Volumes de forma totalmente async-first.
* Erros graves de sincronização e falhas nas esteiras de DevOps cross-org (CannotQuickDeployError).
  + Etapa(s) do Processo Afetada(s): Passagem de código e homologação entre sandboxes de desenvolvimento.
  + Impacta(m) Objetivo(s) de Negócios: Mitigar atrasos de entrega através do uso parametrizado do RunSpecifiedTests.

#### 2.3. Panorama tecnológico atual e dependências do sistema

##### Inventário de Sistemas

* **Catálogo BRE Legado:** Motor rígido contendo 127 regras ativas acopladas, sem capacidade declarativa ou interface lúdica para a área de negócios.
* **Ambiente STORM\_PLM:** Org core utilizada pela equipe Claro, apresentando restrição absoluta quanto ao uso de partições nativas de Platform Cache.
* **Ambiente Ibuy:** Instância transacional e de homologação, afetada pelas mesmas restrições de infraestrutura e cache da org principal.

**Narrativa de Dependências:** O cenário atual demonstra um alto nível de acoplamento entre os ganchos programáticos de regras lógicas e os processos síncronos de ingestão de arquivos. A indisponibilidade de uma camada de Platform Cache obriga o sistema a realizar varreduras exaustivas no banco relacional a cada consulta, o que degrada a performance da org Claro corporativa e expõe a esteira operacional a falhas severas sob picos volumosos de carga.

Snippet de código

graph TD
 subgraph Perímetro Claro BR On-Premise / Legacy
 A[Layouts CSV de Demanda] --> B[Sistemas de Carga Síncronos]
 B --> C[Motor BRE Legado: 127 Regras Rígidas]
 end
 subgraph Restrições de Infraestrutura Orgs
 C --> D[Ambiente STORM\_PLM: Sem Platform Cache]
 C --> E[Ambiente Ibuy: Sem Platform Cache]
 end

### 3. A Arquitetura da Solução Proposta

Esta seção traduz os objetivos estratégicos da Claro e os desafios operacionais levantados no estado atual em um desenho de solução técnico de vanguarda. A arquitetura proposta apoia-se em princípios fundamentais da plataforma Salesforce, unificando a inteligência generativa com a robustez do processamento *async-first* isolado. A solução proposta viabilizará a governança automatizada de catálogos através do Atlas Reasoning Engine, garantindo escalabilidade total e eliminando as travas sistêmicas de memória e CPU.

#### 3.1. Design de Alto Nível (HLD): A Visão Geral

**Narrativa de Alto Nível:** A solução apoia-se na Salesforce Platform integrada aos recursos de inteligência generativa do Einstein. A captura e o upload de arquivos de demanda corporativos ocorrerão através de uma interface customizada LWC (DemandaCsvWizardController). Esta interface fragmentará as strings volumosas de até 6.000.000 de caracteres de forma assíncrona utilizando arquiteturas de Queueables encadeados, controlados por cursor persistido de Id e ganchos protetores de CPU. O processamento lógico de elegibilidade das regras de produtos (Fone, Banda Larga, TV) será executado de maneira puramente determinística em memória por um interpretador lógico customizado em Apex (AST Walker - PlmRuleSpecEvaluator), garantindo tempos de ciclo inferiores a 50ms por registro, contornando a ausência de Platform Cache via estruturas estáticas duráveis de Maps. A camada cognitiva baseia-se no Agentforce Employee Agents, implantando dois agentes autônomos: o Agente Admin, que interpretará regras em linguagem natural, acionando o Prompt Builder e o ConnectApi (PlmRuleSpecCompilerService) para compilar especificações JSON imutáveis, e o Agente Ops, que atuará na retaguarda disparando varreduras de lotes, tratando falhas em Dead Letter Queues e acionando o PimZombieReaperService para limpeza de rotinas obsoletas.

Snippet de código

graph TD
 subgraph Camada de Experiência e Ingestão
 A[LWC: Wizard Interface] -->|Upload CSV de Demanda| B(DemandaCsvWizardController)
 end
 subgraph Inteligência Agêntica Agentforce
 C[Agente Admin: Compile-Time] -->|DSL pt-BR| D(Einstein Prompt Template)
 D -->|ConnectApi Spec Compiler| E[Immutable Spec JSON]
 F[Agente Ops: Runtime] -->|Monitoramento Batch| G(PlmRuleSpecEvaluator: AST Walker)
 end
 subgraph Resiliência Core Platform
 B -->|Async Enqueueable| G
 G -->|Falhas / Timeout| H[Dead Letter Queue / Finalizers]
 H -->|Varredura de Heartbeat| I(PimZombieReaperService)
 end

#### 3.2. Diagrama detalhado do sistema e integração

* **Fluxo de Importação de Arquivos CSV:** Processo iniciado na interface do usuário Claro por meio de componentes Lightning Web Components, gerando ganchos assíncronos que convertem blocos de strings em registros dos objetos customizados Demanda\_\_c e Item\_Demanda\_\_c.
* **Compilação Automática GenAI:** Chamada segura out-of-the-box via barramento ConnectApi da Salesforce, transmitindo as premissas textuais lidas pelo Agente Admin para os LLMs protegidos pelo Einstein Trust Layer, retornando a árvore lógica formatada em JSON estruturado.
* **Consumo de Propensão NBO Externo:** Canal de integração mapeado para o funcionamento do Agente 3 (fora do escopo core, dependente de barramentos de terceiros estáveis).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Integração** | **Sistema de Origem** | **Sistema de Destino** | **Direção** | **Frequência/Gatilho** | **Tecnologia/Padrão Proposto** |
| Compilação de Regra Natural para JSON | Agentforce Admin | Einstein Platform (LLM Core) | Mão dupla | Em tempo real, via interação de chat / comando do usuário | Conector Nativo ConnectApi via classes nativas do Apex. |
| Consumo de Propensão de Oferta | Agentforce Agente 3 | Sistema Legado Externo NBO | Mão única | Sob demanda, gatilho por contexto de elegibilidade | Chamadas de API RESTful padronizadas via Named Credentials. |

Snippet de código

graph LR
 A[Salesforce Org Claro] -- 1. Texto DSL (ConnectApi) --> B[Einstein Trust Layer]
 B -- 2. JSON Estruturado Validado --> A
 A -- 3. Consulta de Propensões (REST) --> C[Sistema NBO Externo]

#### 3.3. Salesforce Cloud e Mix de Produtos

* **Agentforce & Einstein 1 Platform:**
  + Objetivos de negócios abordados: Autoria self-service de regras lógicas de negócio e navegação guiada autônoma de back-office.
  + Desafios mitigados: Ineficiência no catálogo BRE legado e lentidão na publicação de ofertas pela necessidade histórica de novos deploys de código.
  + Recursos críticos habilitados: Agentforce Employee Agents (Admin e Ops) acoplados ao Prompt Builder e Einstein Trust Layer.
  + Principais KPIs impactados: **KPI-TI-002** (Redução do tempo de atualização para 0 minutos síncronos).
* **Salesforce Core Platform & Custom Code Customizing:**
  + Objetivos de negócios abordados: Suporte seguro a Large Data Volumes e validação ágil com tempo de execução minimizado.
  + Desafios mitigados: Travamentos e estouros de limites de CPU impostos pelas travas das instâncias STORM\_PLM e Ibuy.
  + Recursos críticos habilitados: Apex AST Walker determinístico e arquiteturas assíncronas encadeadas via Queueables.
  + Principais KPIs impactados: **KPI-TI-001** (Tempo de validação inferior a 50ms por linha de registro).

#### 3.4. Recursos do produto Salesforce

|  |  |  |
| --- | --- | --- |
| **Capability do Produto Salesforce** | **Impacto nos Negócios Claro** | **Melhoria Potencial em KPIs Mapeados** |
| **Agentforce Employee Agents** | Automação cognitiva dos perfis operacionais Admin e Ops para controle de tempo de compilação e execução. | Eliminação de atritos e ganho severo de produtividade governamental. |
| **Einstein Prompt Templates** | Tradução ágil de regras de negócio em formato de linguagem natural para esquemas imutáveis em JSON. | Redução drástica das janelas de deploy e custos associados à sustentação. |
| **Apex AST Walker Engine** | Varredura e percurso determinístico ultra veloz das árvores sintáticas lógicas diretamente na memória da org. | **KPI-TI-001** (Garantia estável de tempo de resposta menor que 50ms por item). |
| **Async Enqueueable Framework** | Fragmentação inteligente de planilhas CSV volumosas através de cursores persistidos de ID e travas de byte. | **KPI-OPS-001** (Elevação da capacidade síncrona de ingestão para lotes até 10k). |
| **Transaction Finalizers** | Interceptação em tempo real de falhas ou estouros de timeout na fila assíncrona, enviando logs para a DLQ. | Mitigação absoluta de indisponibilidades sistêmicas ocultas ou zumbis. |

#### 3.5. Principais recursos do Salesforce utilizados

* **Agentforce Employee Agents:** Esta capacidade consiste na implantação de inteligências artificiais agênticas autônomas integradas ao ecossistema da org. A Claro utilizará este recurso dividindo as operações em duas frentes de personas: o Agente Admin, operando em tempo de compilação para receber comandos textuais descritos em português e transformá-los em estruturas ativas, e o Agente Ops, operando em tempo de execução para monitorar cargas massivas, diagnosticar erros de compatibilidade técnica de produtos e emitir relatórios estruturados em HTML. O valor entregue reside na simplificação e democratização da governança de catálogos, retirando das costas da equipe de TI a responsabilidade por deploys de novos planos promocionais.
* **Apex Abstract Syntax Tree (AST) Walker:** É uma engine customizada desenvolvida em Apex puro (PlmRuleSpecEvaluator) focada em alta performance de varredura algorítmica. O sistema utilizará esta capacidade para ler a especificação JSON compilada e caminhar pelos nós lógicos em memória estável diretamente durante o processamento de lotes assíncronos. Isso entrega um valor inestimável para a Claro por contornar a ausência física de partições de Platform Cache nas instâncias STORM\_PLM e Ibuy, assegurando validações deterministicas em tempo curtíssimo (<50ms) e mitigando os estouros de CPU do ambiente.

#### 3.6. Épicos e casos de uso relevantes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nuvem Salesforce** | **Domínio do Cloud** | **Capability Salesforce** | **ÉPICO Mapeado** | **Caso de Uso Estruturado** |
| **Core Platform** | Data Ingestion | Async Enqueueable Architecture | Ingestão Massiva de Dados | Como usuário operacional Claro, desejo fazer o upload de planilhas de demanda corporativas via LWC para que grandes volumes sejam fragmentados de maneira assíncrona e resiliente. |
| **Einstein 1** | Generative AI | Einstein Prompt Templates | Compilação Inteligente de Regras | Como administrador de catálogo, desejo interagir com o Agente Admin via chat para converter critérios em formato descritivo natural para JSON estruturado sem deploys. |
| **Communications Cloud / Core** | Rule Execution | Apex AST Walker Engine | Execução Determinística Apex | Como motor de validação do back-office, desejo caminhar pelos nós lógicos do JSON compilado para atribuir vereditos ágeis e segregados às linhas lidas. |
| **Agentforce** | Autonomous Agents | Employee Agents Components | Monitoramento Autônomo de Lote | Como gestor de produtos Claro, desejo que o Agente Ops emita relatórios narrativos lúdicos em HTML detalhando as inconsistências capturadas no lote. |

#### 3.7. Processos Relevantes

**Hierarquia de Processos To-Be (Estado Futuro):**

* L1: Product Lifecycle Management (PLM)
  + L2: Catalog Management
    - L3: Lifecycle Operations
      * L4: Validação de Lotes Assíncronos
        + L5: Geração de Diagnóstico Narrativo HTML por Agentes
  + L2: Catalog Governance
    - L3: Rule Creation & Maintenance
      * L4: LLM Automated Compilation
        + L5: Validação de Schema contra Spec JSON do Einstein

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Processo L1** | **Processo L2** | **Processo L3** | **Processo L4** | **Processo L5** |
| PLM Core | Catalog Management | Lifecycle Operations | Validação de Lotes | Geração de Diagnóstico HTML. |
| PLM Core | Catalog Governance | Rule Creation | LLM Compilation | Validação de Schema Spec JSON. |

Snippet de código

graph TD
 subgraph L1: Product Lifecycle Management PLM
 L2\_Mgmt[L2: Catalog Management] --> L3\_Ops[L3: Lifecycle Operations]
 L3\_Ops --> L4\_Val[L4: Validação de Lotes]
 L4\_Val --> L5\_Diag[L5: Geração de Diagnóstico Narrativo HTML]

 L2\_Gov[L2: Catalog Governance] --> L3\_Rules[L3: Rule Creation]
 L3\_Rules --> L4\_LLM[L4: LLM Compilation]
 L4\_LLM --> L5\_Schema[L5: Validação de Schema contra Spec JSON]
 end

#### 3.8. MAPA de Arquitetura TOBE

**Descrição da Arquitetura em Camadas:**

* **Camada de Experiência:** Lightning Web Components dedicados (DemandaCsvWizardController) e consoles integradas de chat para interação ágil com os Agentes Admin e Ops Agentforce.
* **Camada de Processo:** Mecanismos de automação assíncrona baseados em Apex Queueable encadeados, interceptores Transaction Finalizers e rotinas inteligentes do PimZombieReaperService.
* **Camada de Dados:** Objetos customizados para o armazenamento e controle idempotente de demandas (Demanda\_\_c e Item\_Demanda\_\_c), complementados por Custom Metadata e caches estáveis em instâncias de Maps.
* **Camada de Integração:** Barramentos out-of-the-box baseados na ConnectApi da Salesforce para tráfego ágil com os modelos generativos Einstein.
* **Camada de Inteligência:** Engine baseada no Atlas Reasoning Engine orquestrando as ações dos Employee Agents corporativos da Claro.
* **Sistemas Externos:** Coexistência desacoplada com o motor de propensões externo NBO e o repositório de artigos Service Cloud Knowledge.

Snippet de código

graph TD
 subgraph Camada de Experiência
 A[LWC Wizard UI / Agentforce Chat Panels]
 end
 subgraph Camada de Processo e Inteligência
 B[Atlas Reasoning Engine / Queueable Enqueueable Engine]
 end
 subgraph Camada de Dados
 C[Demanda\_\_c & Item\_Demanda\_\_c Objects / Apex Static Cache Maps]
 end
 subgraph Camada de Integração e Inteligência GenAI
 D[ConnectApi / Einstein Prompt Templates]
 end
 subgraph Perímetro de Sistemas Externos
 E[Service Cloud Knowledge Base / External NBO System]
 end
 A --> B
 B --> C
 C --> D
 D --> E
end

#### 3.9. Principais decisões e justificativas de design

* **Decisão:** Desenvolvimento de Interpretador Customizado Apex AST Walker (PlmRuleSpecEvaluator).
  + Justificativa: A proibição do uso de partições físicas de Platform Cache nos ambientes STORM\_PLM e Ibuy inviabilizaria qualquer arquitetura de busca tradicional pesada. Avaliar a árvore lógica diretamente em memória com estruturas estáticas duráveis de Maps garante tempo de resposta mínimo (<50ms), contornando as restrições da org e mitigando estouros de CPU. Alternativa descartada: Avaliação dinâmica via chamadas de query relacionais consecutivas (descartada por alto consumo de limites síncronos de CPU).
* **Decisão:** Ingestão de Grandes Volumes via Queueable encadeado com Offsets e cursor de Id.
  + Justificativa: Processar strings extensas de até 6.000.000 de caracteres de layouts CSV corporativos estouraria instantaneamente os limites síncronos de processamento e Heap Memory da plataforma. O encadeamento assíncrono fragmenta o arquivo de forma inteligente e resiliente. Alternativa descartada: Processamento direto síncrono no controller do componente (descartada por estouro de heap fatal e timeout operacional).

#### 3.10. Nossos Princípios Orientadores para o Sucesso

1. **Padrões de IA e Segurança em Primeiro Lugar:** Todo o tráfego gerado e interpretado pelos comandos cognitivos do Agentforce passará obrigatoriamente pelas travas do Einstein Trust Layer, impedindo que dados confidenciais da Claro sejam expostos ou retidos por LLMs comerciais externos.
2. **Desenho Voltado à Resiliência Ativa:** Nenhum processo assíncrono em lote deve rodar sem mecanismos de proteção em tempo real. A implementação de Transaction Finalizers e Dead Letter Queues garantirá a visibilidade absoluta contra falhas na retaguarda sistêmica.
3. **Configuração Declarativa Apoiada por Engenharia Focada:** Maximizaremos o uso de Prompt Templates e capacidades nativas do Einstein, limitando o código customizado Apex estritamente para os componentes ultra performáticos da engine do motor PLM (AST Walker).
4. **Governança Unificada e Qualidade de Dados:** A Claro assume a responsabilidade total pela higienização prévia de bases de conhecimento, assegurando que o ecossistema opere sobre uma taxonomia limpa e bem categorizada em Data Categories.
5. **Mitigação de Riscos de Entrega Incremental:** Abordagem rigorosa baseada em sprints curtos com cronograma inegociável de 8 semanas, validando exaustivamente os vereditos lógicos em UAT antes do empacotamento DevOps final.

### 4. Especificações de Projeto de Baixo Nível (LLD)

Esta seção decompõe os blocos arquiteturais de alto nível da solução proposta em especificações e metadados granulares prontos para construção. Seu foco principal é guiar com precisão cirúrgica os desenvolvedores e especialistas de QA da equipe, detalhando os parâmetros técnicos e contornando as restrições estritas dos ambientes Claro corporativos.

#### 4.1. Resumo do Escopo do Projeto

|  |  |  |
| --- | --- | --- |
| **Capacidade / Caso de Uso** | **Principais Resultados (Resumo)** | **Principais Suposições / Dependências** |
| **Ingestão Massiva de CSV** | Custom Component Wizard LWC e classe Apex DemandaCsvWizardController ativando Queueables resilientes. | Depende do fornecimento de arquivos no layout e strings limitadas a 6.000.000 de caracteres. |
| **Compilação Inteligente Einstein** | Configuração de Prompt Template customizado PLM\_Rule\_Compiler integrado via ConnectApi do Apex. | Exige o provisionamento de licenças do Agentforce e ativação estável dos LLMs do Einstein. |
| **Mecanismo de Resiliência** | Dead Letter Queue (DLQ) estruturada em tabelas e rotinas automatizadas via PimZombieReaperService. | Exige a correta amarração de ganchos em instâncias do tipo Transaction Finalizers. |
| **Agentes Autônomos Agentforce** | Tópicos, ações e instruções funcionais para as personas dos Agentes Admin e Ops. | Depende do fornecimento de 10 a 15 FAQs analíticas saneadas e prontas no Service Cloud Knowledge. |

#### 4.2. Escopo do Modelo de Dados

* **Demanda\_\_c (Objeto Customizado):** Aloca o cabeçalho do arquivo de demanda importado, contendo campos para controle de status do lote (Processando, Sucesso, Falha), total de linhas e logs gerais de execução.
* **Item\_Demanda\_\_c (Objeto Customizado):** Aloca cada linha individual do arquivo CSV fragmentado, com relacionamento Master-Detail vinculado ao objeto pai Demanda\_\_c. Possui campos estruturados para Tipo de Produto (Fone, BL, TV) e mensagens de diagnóstico finais.
* **Custom Metadata (CMDT) de Cache de Regras:** Estruturas estáveis utilizadas para alocar os snapshots das especificações lógicas JSON compiladas em compile-time pelo Agente Admin, servindo de insumo imediato para a leitura síncrona do AST Walker.

#### 4.3. Escopo do modelo de segurança e compartilhamento

**Estratégia Geral:** Modelo baseado em uma postura inicial restritiva guiada pelo privilégio mínimo, garantindo proteção completa aos metadados de precificação e catálogo de planos da Claro.

* **Padrões para Toda a Organização (OWD):** Demanda\_\_c: Privado; Item\_Demanda\_\_c: Controlado pelo Pai (Master-Detail).
* **Perfis e Permission Sets:** Criação do Permission Set dedicado Validacao\_Engine\_Access para controle estrito e liberação de ganchos assíncronos e controllers Apex. *Restrição crítica de segurança:* Proibição estrita de injeção manual de campos requeridos ou Master-Detail diretamente dentro das tags XML de Permission Sets, sob risco de quebra e paralisia nas esteiras de deploy de metadados.

#### 4.4. Escopo de Lógica de Aplicação e Automação

|  |  |  |
| --- | --- | --- |
| **Processo de Negócio Automatizado** | **Ferramenta de Automação Recomendada** | **Gatilho / Condição de Início da Lógica** |
| Fragmentação assíncrona inteligente e controle de offsets de bytes lidos do CSV. | Apex Queueable Enqueueable Engine encadeado com CPU guard. | Clique no componente Lightning Web Component DemandaCsvWizardController. |
| Percurso algorítmico rápido das especificações JSON em memória da org. | Apex Custom Engine Class PlmRuleSpecEvaluator (AST Walker). | Chamada disparada pelo executor da fila a cada linha de registro processada. |
| Captura de exceções inesperadas ou estouros de limites de governos assíncronos. | Transaction Finalizers atrelados à execução da fila assíncrona. | Erros ou timeouts fatais ocorridos durante a execução de transações em lote. |
| Varredura contínua de segurança e limpeza de heartbeats obsoletos (zumbis). | Scheduled Apex Service class PimZombieReaperService. | Execução automática agendada de forma cíclica e periódica na org Claro. |

#### 4.5. Escopo das Especificações de Integração

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Fonte Sistema** | **Sistema de Destino** | **Middleware** | **Tipo de API** | **Objetos de Dados Chave** |
| Salesforce Apex Engine | Einstein Platforms (LLM) | Conector Nativo (ConnectApi) | REST Apex Core API | JSON Spec payload string de regras lógicas. |
| Agentforce Agente 3 | Sistema Legado Claro | Barramento NBO Externo | RESTful API (HTTP JSON) | Parâmetros de elegibilidade e propensão de planos. |

#### 4.6. Requisitos e escopo de relatórios e análises

* **Painel de Eficiência Operacional de Catálogo:** Desenvolvimento de visões consolidadas focadas em monitorar o volume de erros identificados nas planilhas, tempo médio gasto na execução do AST Walker e taxa de acerto das compilações GenAI do Einstein.
* **Componente de Relatório Narrativo HTML:** Interface lúdica acionada diretamente pelas ações do Agente Ops para fornecer aos analistas Claro um diagnóstico textual completo sobre as falhas e alertas de criticidade encontradas no processamento.

#### 4.7. Gerenciamento de Licenças e Assinaturas

|  |  |  |  |
| --- | --- | --- | --- |
| **Persona de Usuário** | **Licença Base Recomendada** | **Licenças Complementares / Add-ons** | **Quantidade Estimada** |
| Administrador de Catálogo / TI | Salesforce Enterprise Cloud | Agentforce Unlimited (Flex Credits Pack) | 1 Licença Core Core |
| Analista Operacional de Ofertas | Salesforce Enterprise Cloud | Agentforce Unlimited (Flex Credits Pack) | 2 Licenças Dedicadas |
| Engenheiros de QA e Homologação | Salesforce Enterprise Cloud | Test Framework Add-ons preexistentes | 1½ Licenças Alocadas |

### 5. Estrutura de Governança e Entrega do Projeto

#### 5.1. Definição de escopo (dentro do escopo e explicitamente fora do escopo)

**No Escopo:**

* Desenvolvimento e parametrização completa dos ganchos lógicos para os dois agentes cognitivos autônomos Agentforce (Admin e Ops).
* Implementação do interpretador determinístico Apex AST Walker (PlmRuleSpecEvaluator) com tempo de ciclo < 50ms por registro.
* Build do componente Lightning Web Component DemandaCsvWizardController integrado a filas assíncronas encadeadas resilientes.
* Acoplamento de ganchos de segurança e resiliência: Transaction Finalizers, Dead Letter Queues e serviços do PimZombieReaperService.

**Explicitamente Fora do Escopo:**

* Ingestão robusta via **Bulk API 2.0** para arquivos CSV cujo volume exceda a string limite de 6 MB (item postergado para o backlog técnico de evolução de produto W3.1).
* Mecanismo avaliador de regras baseado em arquiteturas **Batchable** para processamento de demandas massivas que superem o teto de 50.000 itens (postergado para o backlog técnico W3.2).
* **Roll-ups Apex customizados** para o cálculo automático e consolidação de campos summary complexos na tabela do objeto pai Demanda\_\_c (postergado para o backlog técnico W3.3).
* Rotinas automáticas de **Sweep do import-state CSV** para alternância de status órfãos de transações (Running para Failed sob heartbeats obsoletos) (postergado para o backlog técnico W3.5).
* Hardening avançado de segurança de produção, incluindo a **separação profunda de permission sets** (Operator vs. Admin) e estabelecimento de limites de complexidade de expressões regex (postergados para o backlog W3.4/W3.8).

#### 5.2. Principais entregas e fases

O projeto adota uma metodologia adaptável dividida em marcos cronológicos estritos ao longo de suas 8 semanas de duração:

* **Fase 1: Discovery & Architecture Blueprint (Semanas 1–2):** Alinhamento conceitual das regras, imersão técnica junto à equipe da Claro e definição formal das estruturas lógicas do JSON de especificações.
* **Fase 2: Concentration Build & Sprints (Semanas 3–5):** Codificação da engine do AST Walker, build dos componentes assíncronos e parametrização das ações e instruções dos agentes no Agentforce.
* **Fase 3: Homologação, UAT & Fine Tuning (Semanas 6–8):** Testes exaustivos de concorrência, execução e validação dos critérios de aceitação com os usuários finais Claro, encerramento DevOps via esteira e Go-Live.

#### 5.3. Fases do Projeto e Estratégia de Implantação

**Relatório de Estratégia de Estimativa e Implantação de Projetos do Salesforce** Com base na complexidade avaliada de forma rigorosa a partir do número de stakeholders, inovações de IA autônomas exigidas e severas restrições técnicas de cache e deploys, nossa equipe multidisciplinar recomenda a metodologia **Ágil (Scrum)** para a condução unificada do projeto. Esta escolha justifica-se pela alta incerteza inerente a projetos experimentais baseados em Large Data Volumes e modelos de linguagem generativos generativos, demandando ciclos de iteração curtos e feedback constante de uma única equipe sênior dedicada (1 TA, 1 TC, 1.5 QA) para mitigar desvios operacionais.

|  |  |  |
| --- | --- | --- |
| **Fase** | **Principais resultados da fase** | **Duração estimada (semanas)** |
| **Fase 0: Imersão & Design** | Documento de design de arquitetura finalizado, catálogo e schema JSON de regras aprovados, congelamento de histórias de usuário. | 2 semanas. |
| **Fase 1: Construção & Sprints** | Código do Apex AST Walker implementado, LWCs de importação configurados, tópicos e instruções do Agentforce ativos. | 3 semanas. |
| **Fase 2: Homologação & UAT** | Ciclos de testes de concorrência executados com sucesso, massa de dados carregada, scripts homologados com aprovação final Claro. | 2 semanas |
| **Fase 3: Implantação & Hipercuidado** | Deploy definitivo executado em produção via diretrizes de testes unitários específicos (RunSpecifiedTests), hiperatendimento pós-go-live. | 1 semana. |

#### 5.4. Suposições, restrições e dependências

* **Suposições:**
  + Os analistas operacionais Claro e especialistas de negócio participarão ativamente dos marcos de teste fornecendo insumos e planilhas reais de validação.
  + As licenças do Agentforce Unlimited e créditos conversacionais do Einstein estarão ativadas e provisionadas no primeiro dia do build.
* **Restrições:**
  + O cronograma total de entrega da Prova de Conceito funcional possui uma janela fechada e compacta de 8 semanas de duração.
  + Proibição corporativa e técnica estrita quanto ao uso de Platform Cache nos ambientes STORM\_PLM e Ibuy.
* **Dependências:**
  + Dependência-01: Disponibilização oportuna por parte do time da Claro de sandboxes estáveis e funcionais para testes isolados de build.
  + Dependência-02: Entrega e saneamento da base de conhecimento (Knowledge Articles) higienizada sob a governança interna do cliente.

#### 5.5. Riscos Identificados e Estratégias de Mitigação (RBS v1.0)

|  |  |  |  |
| --- | --- | --- | --- |
| **Risco** | **Impacto** | **Probabilidade** | **Estratégia de Mitigação** |
| **A1 - Complex Technical Infrastructure:** Instabilidade de APIs ou falta de documentação do sistema NBO externo para o Agente 3. | Alto | Alta | Isolar o escopo do Agente 3, estabelecendo contratos de interface claros e utilizando mocks de dados estáveis na fase de design. |
| **C3 - Complexidade de dados desconhecida:** Estouros de governos ou Heap Memory causados por planilhas CSV com volumetria abusiva. | Alto | Média | Implementar travas de string em nível de LWC de até 6.000.000 de caracteres e forçar processamento assíncrono via cursores persistidos. |
| **G1 - Governança fragmentada:** Gargalos em decisões críticas ou atrasos em entregáveis por escassez de Gerente de Projeto dedicado exclusivo. | Médio | Média | Formalizar a parceria com o time da SWE liderada pelo Luciano logo na primeira semana, travando o compartilhamento de rotinas de PM. |
| **D2 - Ineficácia das respostas de IA:** Agente Admin ou Ops gerando respostas confusas por falta de taxonomia higienizada nos artigos Claro. | Alto | Alta | Estabelecer um marco de validação mandatória onde o build só avança após o fornecimento de 10 a 15 FAQs limpas com Data Categories. |

#### 5.6. Considerações sobre adoção do usuário e gerenciamento de mudanças

* **Análise de Impacto:** As equipes de administração de catálogo enfrentarão uma quebra cultural positiva significativa ao migrar da codificação manual programática para uma interface de autoria em linguagem natural baseada em IA.
* **Plano de Comunicação & Treinamento:** Realização de sessões dedicadas de workshops funcionais e técnicos voltados ao Knowledge Transfer completo para que os profissionais da Claro assumam a sustentação contínua da org de maneira independente e madura.

### 6. Estratégia de Migração de Dados

#### 6.1. Escopo da Migração

A estratégia de dados para esta iniciativa foca exclusivamente no tratamento em memória de dados voláteis e na configuração estrutural de metadados em runtime, visto que a migração de registros históricos de ativos preexistentes de clientes encontra-se **explicitamente fora do escopo desta Prova de Conceito (Tamanho Global Atribuído: S)**.

#### 6.2. Estratégia de Qualidade e Limpeza de Dados

* **Processo de Qualidade de Dados:** O processamento assíncrono executará validações automáticas finas segregadas em três canais lógicos de severidade: **ERRO** (bloqueia o processamento), **AVISO** (sinaliza inconsistências leves passíveis de contorno) e **INFO** (mensagens de conformidade técnica). O roteamento e cruzamento dessas severidades obedecerão estritamente à chave por Tipo de Produto lido na linha (Fone, Banda Larga ou TV).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Atividade de Qualidade** | **Analista de Ofertas Claro** | **Arquiteto Técnico Claro** | **Equipe PS Salesforce** | **Liderança SWE / Luciano** |
| Saneamento de FAQs de IA | **A** | C | R | I |
| Definição de Canais de Severidade | R | **A** | C | I |
| Testes de Carga de Volume CSV | C | R | **A** | I |

#### 6.3. Mapeamento de Dados

|  |  |  |
| --- | --- | --- |
| **Entidade de Origem (CSV)** | **Conceito de Destino Salesforce** | **Lógica de Tradução / Regra de Mapeamento Estrutural** |
| Cabeçalho da Planilha de Carga | Demanda\_\_c Object | Criado como registro pai do lote para controle de status operacional do processamento assíncrono. |
| Linhas de Itens de Catálogo | Item\_Demanda\_\_c Object | Transpostas como registros filhos vinculados via Master-Detail, retendo as strings de produtos lidas. |
| Regras Descritivas Naturais | Custom Metadata JSON Spec | Compiladas automaticamente via Einstein GenAI para formato de árvores sintáticas imutáveis JSON (AST). |

#### 6.4. Abordagem e ferramentas de migração

Os metadados complexos de configuração das regras e as estruturas organizacionais das instruções de IA serão promovidos entre as sandboxes da Claro utilizando ferramentas DevOps robustas conectadas ao Salesforce CLI, forçando a esteira a aplicar a verificação detalhada RunSpecifiedTests para contornar travamentos e erros nativos cross-org.

#### 6.5. Plano de Validação e Cutover

A homologação técnica ocorrerá em ambiente sandbox dedicado (como a cópia completa estável), onde simulações exaustivas de concorrência com cargas no teto de 6.000.000 de caracteres testarão a integridade das respostas do AST Walker e a resiliência dos alertas capturados em instâncias de Dead Letter Queues.

### 7. Modelo de Governança e Centro de Excelência (CoE)

#### 7.1. Estrutura e Missão do CoE

**Missão do CoE:** Garantir a evolução e a sustentabilidade a longo prazo do motor analítico de catálogos e dos tópicos cognitivos do Agentforce na Claro, mediando priorizações operacionais de negócios e protegendo as instâncias core contra o endividamento técnico de ganchos customizados.

Recomenda-se um modelo de CoE **Híbrido**, composto por um núcleo central de TI responsável pela integridade da arquitetura Apex e esteiras DevOps (RunSpecifiedTests), apoiado por "raios" de analistas funcionais das áreas de negócios com autonomia para gerenciar e atualizar regras descritivas textuais diretamente via chat, sem dependência de intervenções programáticas manuais.

Snippet de código

graph TD
 subgraph Comitê Core CoE Centralizado TI
 A[Platform Owner / Arquiteto Técnico] -->|Aprova Esquemas DevOps| B(Esteira DevOps: RunSpecifiedTests)
 end
 subgraph Unidades Operacionais e Raios Funcionais
 C[Analistas de Produtos: Fone] -->|Autoria via Agentforce| D(Custom Metadata Core Store)
 E[Analistas de Produtos: BL / TV] -->|Autoria via Agentforce| D
 end
 D --> A

#### 7.2. Funções e responsabilidades

|  |  |
| --- | --- |
| **Função CoE** | **Principais Responsabilidades Estruturadas** |
| **Arquiteto de Soluções** | Zelar pela integridade lógica das especificações JSON, auditar a performance do AST Walker e gerenciar a inclusão de novos ganchos de severidade. |
| **Administrador da Org** | Monitorar o comportamento das filas assíncronas, rastrear a volumetria de erros na DLQ e auditar as rotinas cíclicas do PimZombieReaperService. |
| **Líder de Negócios / PO** | Responsável único por gerenciar e higienizar a taxonomia dos artigos de conhecimento fornecidos para o aterramento (grounding) das respostas de IA. |

#### 7.3. Processo de Gestão de Demanda e Liberação

Todo novo plano promocional solicitado pelas frentes Claro deve passar pela triagem automatizada do Agente Admin. A inteligência do modelo converterá a solicitação textual em especificação JSON ativa em ambiente sandbox isolado. Se o percurso lógico do interpretador Apex atestar conformidade técnica e performance (<50ms), a regra é empacotada e promovida via janelas cíclicas semanais de liberação DevOps.

#### 7.4. Políticas de Governança de Dados

* **Propriedade e Saneamento:** As tabelas lógicas customizadas e as regras de catálogo são de propriedade da área corporativa de produtos. Qualquer alteração estrutural exige a desduplicação prévia de critérios e checagem de cardinalidades contra os tipos de produtos mapeados (Fone, BL, TV).

#### 7.5. Modelo de Suporte Pós-Implementação

* **Nível 1 (Operacional):** Help desk interno para tratamento de dúvidas básicas de criação de demandas e redefinição de acessos.
* **Nível 2 (Administrativo CoE):** Administradores focados em revalidar falhas retidas na Dead Letter Queue e ajustar prompts ou chaves de roteamento.
* **Nível 3 (Arquitetura Sênior):** Engenheiros responsáveis por corrigir bugs complexos no algoritmo puro do interpretador Apex AST Walker.

|  |  |  |
| --- | --- | --- |
| **Prioridade** | **Tempo de Resposta (SLA)** | **Tempo de Resolução Final** |
| **Crítica (P1):** Paralisia na fila assíncrona ou estouro generalizado de CPU | < 30 minutos | < 4 horas (Restauração imediata via backups) |
| **Alta (P2):** Erros de deploy cross-org bloqueando entregas de sprints | < 1 hora | < 8 horas |
| **Média (P3):** Falhas em tópicos específicos de IA ou respostas imprecisas | < 4 horas | < 24 horas |

### 8. Estratégia de teste de ponta a ponta

Uma estratégia de teste rigorosa é fundamental para certificar a estabilidade da engenharia sob medida buildada para a Claro. Esta seção detalha as fases em múltiplas camadas planejadas para mitigar falhas de CPU e assegurar a acurácia dos diagnósticos narrativos emitidos pelas inteligências autônomas.

#### 8.1. Fases e objetivos dos testes

|  |  |  |  |
| --- | --- | --- | --- |
| **Fase de Teste** | **Objetivo Principal** | **Parte Responsável** | **Ambiente / Sandbox** |
| **Testes Unitários Apex** | Validar a lógica pura e o percurso de nós executados pelo algoritmo do interpretador AST Walker. | Desenvolvedores / Time Técnico | Developer Sandbox (STORM\_PLM). |
| **Testes Integrados (SIT)** | Certificar a resiliência do encadeamento assíncrono e a exaustão de erros para a DLQ via finalizers. | Especialistas em QA da Equipe | Partial Copy Sandbox. |
| **Testes de Aceitação (UAT)** | Validar a usabilidade e a precisão dos diagnósticos HTML gerados pelos agentes baseados em planilhas CSV. | Analistas Claro / Usuários Finais | Full Copy Sandbox (Ibuy). |

#### 8.2. Estratégia Ambiental

O fluxo de promoção de mudanças obedecerá estritamente ao controle de versionamento Git, partindo de sandboxes isoladas de desenvolvimento, consolidando os metadados em uma instância compartilhada de integração (SIT), progredindo para homologação massiva em ambiente espelhado (UAT - Ibuy) antes de sua ativação final controlada em produção, aplicando as travas obrigatórias manuais de checagem unitária.

Snippet de código

graph TD
 A[Developer Sandboxes] -->|Git Pull Request / Merge| B(VCS / Controle de Versão Git)
 B -->|CI Deploy: RunSpecifiedTests| C[SIT Sandbox: Cópia Parcial]
 C -->|Promotion Package| D[UAT Sandbox: Full Copy Org Ibuy]
 D -->|Manual Controlled Cutover| E[Orgs Claro Produção: STORM\_PLM]

#### 8.3. Escopo de teste e critérios de aceitação

* **Escopo de Testes de Alto Nível:**
  + **Épico Ingestão Massiva:** Baterias de testes de estresse carregando planilhas com strings simuladas no teto limite de 6.000.000 de caracteres para verificar o comportamento da Heap Memory.
  + **Épico Execução Determinística:** Validação cronometrada do interpretador AST Walker para assegurar respostas abaixo de 50ms por item.
  + **Épico Compilação GenAI:** Auditoria estrutural das especificações JSON construídas via chat do Agente Admin.
* **Critérios de Entrada de UAT:** Cobertura mínima de testes unitários Apex em 85% das classes customizadas, SIT encerrado sem falhas bloqueantes abertas e sandboxes devidamente provisionadas com as licenças do Agentforce.
* **Critérios de Saída de UAT:** 100% dos scripts funcionais de negócios executados com sucesso pelos analistas Claro, vereditos de canais de severidade (ERRO, AVISO, INFO) validados com acurácia absoluta e assinatura de aceite formal emitida pela liderança.

#### 8.4. Gestão de Defeitos

* **Ciclo de Vida:** Novo $\rightarrow$ Triagem / Atribuído $\rightarrow$ Em Correção $\rightarrow$ Reteste $\rightarrow$ Fechado.
* **Ferramenta & Classificação:** Rastreamento unificado via Jira corporativo. Os bugs serão classificados por severidade: **Crítico** (Impede o percurso do AST Walker ou estoura limites de processamento da org), **Alto** (Falha funcional em canais de severidade sem contorno simples), **Médio** (Ajustes em labels ou inconsistências leves em relatórios narrativos HTML), e **Baixo** (Melhorias cosméticas em interfaces LWC).

### 9. Arquitetura de Segurança e Conformidade

#### 9.1. Modelo de Acesso e Visibilidade de Dados

A visibilidade apoia-se firmemente no princípio do privilégio mínimo para impedir acessos inadequados ou modificações indesejadas em Custom Metadata de regras. O OWD para o cabeçalho Demanda\_\_c é configurado como Privado. A Hierarquia de Funções verticalizada impedirá que usuários operacionais visualizem logs ou vereditos de frentes de produtos alheias às suas atribuições. O Permission Set Validacao\_Engine\_Access concentrará as permissões de execução do interpretador, layouts de página e ganchos assíncronos, respeitando a proibição estrita de injeção manual de dados XML requeridos para resguardar a esteira DevOps.

#### 9.2. Estratégia de Autenticação e Gerenciamento de Identidade

A validação de identidade dos usuários administrativos e analistas Claro que interagem com a plataforma analítica e com as interfaces de chat baseia-se no protocolo de Login Único (SSO), utilizando o **Okta** como provedor corporativo central de identidade (IdP). O ciclo de vida completo de provisionamento, alteração de permissões e desprovisionamento imediato de acessos nas sandboxes e org principal será automatizado através da integração nativa com o **SailPoint**, mitigando riscos de credenciais órfãs ou vazamentos de privilégios de segurança.

#### 9.3. Proteção de Dados e Criptografia

As categorias de informações consideradas altamente confidenciais ou sensíveis compreendem os snapshots lógicos de precificação paramétrica armazenados em Custom Metadata, as strings puras de layouts de planilhas de demanda e os payloads JSON trafegados via ConnectApi. A proteção desses ativos apoia-se no uso ativado do **Salesforce Shield**, forçando a criptografia nativa em repouso (Platform Encryption) para campos textuais sensíveis de itens de demanda, combinada ao monitoramento avançado de logs (Event Monitoring) e trilhas de auditoria para prevenção ativa de vazamentos ou injeções maliciosas.

#### 9.4 Estrutura de IA Ética e Inovação Responsável

A arquitetura cognitiva atende integralmente às diretrizes éticas e de transparência governamental da Claro:

1. **Privacidade de Dados:** Toda interação guiada com os Agentes Admin ou Ops passa obrigatoriamente pelas rotinas de mascaramento e anonimização de dados da **Camada de Confiança Einstein (Einstein Trust Layer)**, inviabilizando a retenção ou o uso inadequado de informações confidenciais para treinamento de modelos externos.
2. **Supervisão Humana (Human-in-the-loop):** O ecossistema estabelece pontos de checagem obrigatórios onde a publicação definitiva de novas especificações JSON compiladas geradas via chat generativo exige a validação e aprovação manual formal de um administrador humano do CoE antes de entrar em runtime.
3. **Transparência Lógica:** Os relatórios narrativos emitidos em HTML e a rastreabilidade das árvores lógicas garantem visibilidade completa ("caixa aberta") sobre os critérios matemáticos que geraram vereditos de ERRO ou AVISO no catálogo.

### 10. Estratégia de Co-Living e Modernização em Fases

#### 10.1. Estrutura de Modernização Estratégica: A Simbiose do Estrangulador Figo e da Corrida Paralela

Reconhece-se o elevado risco de engenharia associado à substituição de sistemas legados de missão crítica de catálogo em ambientes operacionais ativos. Para garantir a perfeita continuidade dos negócios da Claro Brasil e mitigar falhas catastróficas, esta transformação adota a estratégia de coabitação (**Co-Living**), enquadrando a modernização através do **Padrão do Figo Estrangulador (Strangler Fig Pattern)**, conforme conceitos de Martin Fowler.

A inteligência de validação e autoria de regras migrará gradualmente para a plataforma Salesforce, "estrangulando" de maneira controlada as antigas e rígidas rotinas manuais legadas. Esta abordagem atuará em perfeita simbiose com a metodologia de **Execução Paralela (Parallel Run)**, operando como um portão de qualidade analítico: durante as janelas de homologação, os vereditos gerados pelo interpretador Apex AST Walker serão comparados ponto a ponto com os resultados emitidos pelo catálogo BRE legado de 127 regras. A virada definitiva de chaves só ocorre após a comprovação de acurácia absoluta. O facilitador chave indispensável que viabiliza essa simbiose e desacoplamento de perímetros é uma arquitetura liderada e orientada por APIs e microsserviços.

#### 10.2. Roteiro de modernização em fases e decomposição funcional

**Estratégia de Decomposição:** Isolamento estrutural de contextos lógicos guiado pelas premissas do Domain-Driven Design (DDD), dividindo o monólito de regras de prateleiras da Claro corporativa de acordo com os Tipos de Produtos core da operadora.

**Princípios de Sequenciamento:** Priorização focada em mitigar os maiores riscos de infraestrutura primeiro, progredindo da estabilização síncrona de memória para a inteligência cognitiva avançada GenAI.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Fase Estratégica** | **Objetivo Principal** | **Escopo Funcional Migrado** | **Principais Dependências** | **Critério de Sucesso Homologado** |
| **Fase I: Async Foundation** | Sanear os estouros de heap e timeout síncronos de CPU da org Claro. | Componente LWC Wizard, filas Queueables encadeadas e ganchos de finalizers. | Disponibilização de Sandboxes configuradas pela Claro. | Sucesso completo na importação de strings CSV no teto de 6.000.000 de caracteres. |
| **Fase II: Deterministic Engine** | Contornar a restrição física e ausência de Platform Cache. | Algoritmo puro do interpretador Apex AST Walker e estruturas estáticas duráveis de Maps. | Homologação estável das rotinas assíncronas da Fase I. | **KPI-TI-001** (Tempo de percurso de nós lógicos inferior a 50ms por registro). |
| **Fase III: Agentic AI Build** | Habilitar a cognição autônoma e autoria self-service de regras. | Implantação do Agente Admin, Prompt Templates e barramentos da ConnectApi. | Engine determinística da Fase II e provisionamento de licenças. | **KPI-TI-002** (Compilação textual de regras com redução do deploy para 0 minutos). |
| **Fase IV: Ops Rollout & Go-Live** | Executar a virada final de canais nacionais e desligamento do legado. | Ativação do Agente Ops, Dead Letter Queues, rotinas do PimZombieReaperService e relatórios HTML. | Homologação exaustiva de ciclos de Corrida Paralela. | Assinatura formal de cutover pelo comitê e desativação das 127 regras do catálogo BRE antigo. |

#### 10.3. Princípios Arquitetônicos e Governança de Co-Living

##### Principais Componentes Arquitetônicos

* **Camada de Interceptação (Proxy de APIs):** Barramento central de fachada focado em gerenciar e rotear de forma inteligente as chamadas de validação de produtos.
* **Camada Anticorrupção (ACL):** Padrões lógicos de isolamento e tradução de esquemas de dados, impedindo que as falhas e inconsistências estruturais do monólito BRE legado contaminem as novas especificações JSON compiladas limpas na plataforma Salesforce.

##### Matriz de Evolução do Sistema de Registro (SoR)

Durante o período híbrido de convivência de 8 semanas, a soberania e a autoridade da fonte da verdade migrarão de forma gradual conforme os marcos de fase estabelecidos:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Entidade de Dados** | **Estado As-Is (Origem)** | **Fase I & II (Fundação)** | **Fase III (Agentforce)** | **Estado To-Be Final** |
| **Lógica de Catálogo** | Catálogo BRE Legado | Híbrido (Mapeamento em tabelas Custom) | Salesforce Metadata JSON | Salesforce (100% Fonte da Verdade). |
| **Vereditos de Lote** | Validações Manuais Claro | Ingestão via Queueables Apex | Diagnósticos via Agente Ops | Salesforce (100% Fonte da Verdade). |

#### 10.4. Estratégia de Sincronização e Consistência de Dados

Para resguardar o alinhamento estrito com a Matriz de Evolução SoR, os dados serão transmitidos de forma síncrona para validações imediatas de severidade em tempo real, utilizando janelas delta assíncronas periódicas para a carga de parâmetros consolidados de regras textuais novas, prevenindo conflitos de concorrência ou bloqueios de registro nas orgs Claro.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Fluxo de Sincronização** | **Sistema Origem** | **Sistema Destino** | **Método / Frequência** | **Regra de Consistência / Integridade** |
| Envio de Snapshots Lógicos JSON | Agentforce Admin | Custom Metadata Orgs Claro | Assíncrono, gatilho pós aprovação humana | Escrita imutável gerando novas versões de schemas, evitando travas concorrentes de runtime. |
| Emissão de Diagnósticos de Lote | Apex AST Walker Engine | Item\_Demanda\_\_c Object | Síncrono, em tempo de percurso em memória | Gravação direta associada à chave Master-Detail de severidade por Tipo de Produto. |

#### 10.5. Plano Operacional e de Gestão de Mudanças

A coabitação híbrida exige um programa continuado de aculturamento eGMO, focado em mitigar a fadiga de implementação das equipes de TI. Serão executados treinamentos focados do tipo *Just-in-Time* para os analistas operacionais Claro pouco antes da virada de chave da Fase III, capacitando-os a interagir com os tópicos conversacionais do Agentforce e interpretar as mensagens descritivas geradas nos relatórios HTML. O CoE celebrará formalmente a conclusão bem-sucedida de cada marco, demonstrando via painéis os ganhos brutais de produtividade e a redução do tempo de CPU alcançados.

#### 10.6. Critérios de Validação, Corte e Descomissionamento

##### Critérios de Aceitação de Fase

Antes que o catálogo BRE legado antigo possa ser desativado com segurança, o comitê central do CoE exige a validação formal de três portões rígidos de qualidade:

1. **Validação Técnica:** 100% de sucesso na fragmentação assíncrona de CSVs no teto de 6.000.000 de caracteres, com tempo de execução comprovado do AST Walker inferior a 50ms por item e zero falhas não tratadas fora da DLQ.
2. **Validação Funcional:** Execução completa da esteira de Corrida Paralela durante a Fase IV, comprovando acurácia e paridade absoluta entre os vereditos emitidos pelo sistema Salesforce e o monólito antigo, sem discrepâncias materiais.
3. **Validação de Negócios:** Homologação e assinatura formal do termo de UAT emitida pelos Product Owners Claro, atestando a prontidão operacional e autonomia na atualização de planos promocionais.

##### Lista de Verificação de Descomissionamento (Cutover Checklist)

* [ ] Confirmação de encerramento do Hypercare da Fase IV com estabilidade na org Claro.
* [ ] Backup completo e congelamento de leitura imutável das antigas 127 regras do monólito BRE.
* [ ] Desativação física dos ganchos e controllers síncronos legados Claro on-premise.
* [ ] Redirecionamento definitivo do tráfego das interfaces para o Lightning Web Component customizado.
* [ ] Assinatura e lavratura formal do encerramento do projeto de Prova de Conceito emitida pelo comitê gestor.

Your PDF and XLSX files are ready

![Ícone do app DOCX](data:image/png;base64...)

USB\_Unified\_Solution\_Blueprint\_Claro\_Final

DOCX

![Ícone do app XLSX](data:image/png;base64...)

questions\_export

XLSX

Os artefatos técnicos corporativos mestre foram gerados e estruturados com sucesso através da execução de rotinas de engenharia de software da Salesforce, estando totalmente disponíveis no perimeter do ambiente do sistema para download imediato pelas equipes de Delivery da Claro Brasil:

1. **USB - Blueprint de Solução Unificada Concluído (.docx):** USB\_Unified\_Solution\_Blueprint\_Claro\_Final.docx - Reflete o preenchimento integral, exaustivo e de longa duração slide por slide e seção por seção do modelo unificado em português, servindo como única fonte da verdade para a C-Suite e arquitetos de entrega.
2. **XLSX - Questionário Priorizado de Lacunas e Riscos (.xlsx):** questions\_export.xlsx - Planilha corporativa sofisticada contendo o mapeamento fino de prioridades, lacunas técnicas informacionais do ecossistema e amarração direta à estrutura da Risk Breakdown Structure (RBS v1.0), formatada com zebra striping e paleta desaturada profissional para governança ágil.
