# USD - DOCUMENTO DE ESCOPO UNIFICADO (UNIFIED SCOPING DOCUMENT)

**Projeto: POC PLM & Agentforce – Claro** **Versão:** 2.0

**Data:** 2026

## 1. Catálogo de Requisitos do Cliente

Com base na análise dos insumos de descoberta e alinhamentos técnicos estruturados para a Prova de Conceito (POC) da Claro, foram extraídos e formalizados os seguintes requisitos fundamentais:

| **Id do Requisito** | **Categoria** | **Descrição do Requisito** | **Origem** |
| --- | --- | --- | --- |
| **REQ-TEC-001** | Tecnologia (TEC) | Implementação de arquitetura *async-first* para importação assíncrona de arquivos CSV corporativos via componentes especializados (DemandaCsvWizardController, Queueable, cursor resumível e CPU guard). | Discovery com Lucas, p. 2 |
| **REQ-PRO-001** | Processo (PRO) | Avaliação determinística de regras de catálogo nativas do Salesforce por meio de um interpretador de árvore de sintaxe abstrata (AST Walker) codificado em Apex puro (PlmRuleSpecEvaluator), com tempo de execução inferior a 50 ms por registro. | Discovery com Lucas, p. 2, 5 |
| **REQ-TEC-002** | Tecnologia (TEC) | Compilação automática de regras em linguagem natural (DSL pt-BR) para formato AST JSON utilizando o modelo de linguagem (LLM) do Einstein via ConnectApi (PlmRuleSpecCompilerService). | Discovery com Lucas, p. 2, 4 |
| **REQ-TEC-003** | Tecnologia (TEC) | Mecanismo de observabilidade, resiliência e tratamento de falhas em execuções assíncronas utilizando Dead Letter Queue (DLQ), Snapshots de compilação, Transaction Finalizers e rotinas de limpeza agendadas (PimZombieReaperService). | Discovery com Lucas, p. 2, 3 |
| **REQ-BIZ-001** | Negócios (BIZ) | Implantação de dois agentes autônomos Agentforce (Employee Agents) para conduzir os fluxos operacionais da plataforma: Agente Admin (tempo de compilação) e Agente Ops (tempo de execução). | Discovery com Lucas, p. 1, 2, 3 |
| **REQ-DAT-001** | Dados (DAT) | Validação segregada de regras de catálogo estruturadas em 3 canais de severidade (ERRO, AVISO, INFO) com base na chave de roteamento por Tipo de Produto: Fone, Banda Larga (BL) e TV. | Discovery com Lucas, p. 2, 3, 4, 5 |
| **REQ-GOV-001** | Governança (GOV) | Governança, higienização e preparação dos artigos de conhecimento (Knowledge Articles) com configurações adequadas de Data Categories, sob estrita responsabilidade do cliente. | Discovery com Lucas, p. 1, 2 |
| **REQ-CON-001** | Restrições (CON) | Proibição do uso de partições de *Platform Cache* nos ambientes STORM\_PLM e Ibuy, exigindo estratégia alternativa de cache estático persistido via Maps e instâncias duráveis. | Discovery com Lucas, p. 3, 5 |

## 1.2 Registro de Valor e KPIs

O sucesso estratégico desta implementação está diretamente associado à mitigação de atritos operacionais e ao ganho substancial de produtividade na gestão de regras de catálogo.

| **ID do KPI** | **Nome do KPI** | **Processo (Nível 1–Nível 5)** | **Linha de base** | **Unidade da linha de base** | **Meta** | **Unidade da meta** | **Direção** | **Alavanca de valor** | **Confiança** | **Fonte de dados** | **Requisitos relacionados** | **Casos de uso/Épicos** | **Capacidade do Salesforce** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **KPI-TI-001** | Tempo de Execução de Avaliação de Regras | PLM -> Validação de Catálogo -> Execução de Regras | *Não detalhado* | minutos | < 50 | milissegundos por registro | Minimizar | PRODUTIVIDADE | Alta | Discovery p.5 (CR6) | REQ-PRO-001 | Avaliação em Runtime de Lotes | Apex AST Walker puro |
| **KPI-TI-002** | Autoria e Atualização de Regras de Negócio | PLM -> Governança de Catálogo -> Atualização de Regra | *Não detalhado* | dias (Requer deploy) | 0 | minutos (Sem redeploy) | Minimizar | PRODUTIVIDADE | Alta | Discovery p.3 (2.2) | REQ-TEC-002, REQ-BIZ-001 | Autoria Self-Service de Regras | Agentforce Admin + Einstein LLM |
| **KPI-OPS-001** | Capacidade de Ingestão de Itens por Lote | PLM -> Operações de Catálogo -> Carga de Dados | *Não detalhado* | linhas | <= 10.000 | linhas por lote síncrono | Maximizar | REDUÇÃO\_DE\_CUSTOS | Média | Discovery p.4 (TC4) | REQ-TEC-001 | Importação de CSV Volumoso | Wizard LWC + Queueable encadeado |

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
 "value\_lever": "PRODUTIVIDADE",
 "confidence": "Alta",
 "data\_source": "Discovery com Lucas, p.5 (CR6)",
 "related\_requirements": "REQ-PRO-001",
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
 "value\_lever": "PRODUTIVIDADE",
 "confidence": "Alta",
 "data\_source": "Discovery com Lucas, p.3 (2.2)",
 "related\_requirements": "REQ-TEC-002, REQ-BIZ-001",
 "related\_use\_cases": "Autoria Self-Service de Regras",
 "related\_epics": "Compilação GenAI Assistida",
 "salesforce\_capability": "Agentforce Admin + Einstein LLM"
 }
]

## 2. Questionário Fundamental e Estratégico (Multi-Cloud)

### 2.1 Contexto de Negócios e Visão Estratégica

* **G-BIZ-001 (Estrutura Organizacional):** *Não detalhado nos documentos.* A análise foca estritamente no ecossistema da operadora Claro para validação nativa de catálogos.
* **G-BIZ-002 (Métricas Importantes):** Redução do tempo de diagnóstico de catálogos e eliminação da necessidade de redeploys para alteração de regras operacionais. **Impacto: Alto | Dimensionamento: L**.
* **G-BIZ-003 (Pain Points):** Ineficiência na manutenção do catálogo BRE legado (127 regras) e sobrecarga do tempo de CPU em validações volumosas. **Impacto: Alto | Dimensionamento: SC**.
* **G-BIZ-004 (Personas):** Admin (atua em compile-time gerenciando e compilando regras) e Ops (atua em runtime executando cargas e diagnosticando erros). **Impacto: Médio | Dimensionamento: M**.

### 2.2 Governança do Projeto e Metodologia

* **G-GOV-001 (Estrutura de Governança):** Alinhamento direto com o time corporativo. Equipe alocada de 1 Arquiteto Técnico, 1 Consultor Técnico e 1½ Consultor de QA. Definição sobre papel de PM pendente com liderança. **Impacto: Médio | Dimensionamento: M**.
* **G-GOV-002 (Metodologia):** Cronograma fixo de 8 semanas, subdividido em: 2 semanas de discovery/design, 3 semanas de desenvolvimento e 3 semanas de UAT/Ajustes finos. **Impacto: Alto | Dimensionamento: S**.
* **G-GOV-003 (Ambientes e DevOps):** Ambientes ativos (Sales, Service ou Data Cloud) com licenças Agentforce provisionadas. *Restrição crítica:* Quick-deploy rejeitado cross-org (CannotQuickDeployError), exigindo execução mandatória de testes especificados (RunSpecifiedTests). **Impacto: Alto | Dimensionamento: L**.

### 2.4 Arquitetura Técnica, Integração e Dados

* **G-TEC-001 (Sistemas de Registro):** Coexistência com sistema legados de catálogo. Salesforce atua na validação por meio de objetos customizados (Demanda\_\_c e Item\_Demanda\_\_c) baseados em layouts CSV. **Impacto: Alto | Dimensionamento: M**.
* **G-TEC-002 (Plataforma de Integração):** Integrações sistêmicas amplas fora de escopo no momento. Consumo de dados do sistema NBO externo para o Agente 3 condicionado à estabilidade e documentação de endpoints. **Impacto: Médio | Dimensionamento: L**.
* **G-TEC-003 (Volume de Dados):** Arquitetura desenhada para suportar Large Data Volumes (LDV) no CSV limitados a 6.000.000 de caracteres para evitar estouros de heap de memória e limites síncronos de CPU. **Impacto: Alto | Dimensionamento: SC**.

## 3. Questionários por Plataforma e Nuvens Principais

### 3.2 Service Cloud & SLAs

* **SV-KNOW-001 (Base de Conhecimento):** Utilização de Base de Conhecimento existente para o Agente 1. A Claro assume responsabilidade total pela governança, taxonomia, artigos e fornecimento inicial de 10 a 15 FAQs analíticas. Criação de conteúdo do zero está explicitamente fora de escopo. **Impacto: Alto | Dimensionamento: M**.

### 3.4. Marketing Cloud & Outras Nuvens

* *Nota metodológica:* As seções referentes a Sales Cloud, Field Service, Marketing Cloud, Commerce Cloud, Slack e MuleSoft encontram-se marcadas como **Não detalhado nos documentos**, visto que a fronteira desta iniciativa delimita-se exclusivamente à validação técnica do motor de regras PLM e agentes Agentforce correlatos.

## 4. Questionários por Soluções de Indústria

### 4.5 Communications, Media & Tech (CMT)

* **CMT-COM-001 (Catálogo de Telecomunicações):** A validação foca no catálogo de produtos focado no modelo Claro (combos ou planos envolvendo Fone, Banda Larga e TV). O projeto mitiga a complexidade do catálogo BRE substituindo-o por especificações compiladas via LLM. **Impacto: Alto | Dimensionamento: SC**.
* **CMT-COM-002 (Processos MACD / Orquestração OSS/BSS):** Transações de execução, ativação, fulfillment de ofertas ou integrações complexas de rede encontram-se explicitamente fora do escopo desta POC. **Impacto: Baixo | Dimensionamento: S**.

## 5. Mapeamento de Requisitos para Capacidades do Salesforce

Baseado nas definições técnicas e nos componentes mapeados para a engine do PLM.

| **Id. Requisito** | **Descrição do Requisito** | **Salesforce Cloud / Indústria** | **Salesforce Domain** | **Salesforce Capability** | **Justificativa do Mapeamento** |
| --- | --- | --- | --- | --- | --- |
| **REQ-TEC-001** | Ingestão e processamento de arquivos CSV robustos sem estourar governos de CPU. | Core Platform | Data Ingestion | Async Enqueueable Architecture | A combinação de Queueable encadeado, offsets de bytes e cursores persistidos contorna as travas nativas de timeout síncrono e limites de heap. |
| **REQ-PRO-001** | Processamento rápido e performático de regras complexas de produtos. | Communications Cloud / Core | Rule Execution | Apex Abstract Syntax Tree (AST) Walker | O motor PlmRuleSpecEvaluator executa a árvore lógica diretamente em memória Apex, garantindo tempo de resposta mínimo (<50ms) sem latência de chamadas GenAI. |
| **REQ-TEC-002** | Tradução e transformação de regras de texto humano para especificações estruturadas JSON. | Einstein 1 Platform | Generative AI | Einstein Prompt Templates & ConnectApi | O Prompt Template PLM\_Rule\_Compiler utiliza os LLMs nativos do Einstein para receber regras em formato textual e produzir o JSON correspondente validado contra esquemas formais. |
| **REQ-BIZ-001** | Automação e navegação guiada por voz/chat para operações e administração do catálogo. | Agentforce | Autonomous Agents | Agentforce Employee Agents (Admin & Ops) | Os tópicos e ações configuradas nos agentes permitem gerenciar fluxos operacionais de compilação de metadados e diagnósticos de lote sem intervenção manual em código. |

## 6. Mapeamento de Requisitos para Épicos e Casos de Uso

| **Id. do Requisito** | **Salesforce Capability** | **Épico** | **Caso de Uso** |
| --- | --- | --- | --- |
| **REQ-TEC-001** | Async Enqueueable Architecture | Ingestão Massiva de Dados | Como usuário operacional, desejo fazer o upload de planilhas de demanda corporativas via LWC, processando assincronamente grandes volumes de dados de maneira resiliente. |
| **REQ-TEC-002** | Einstein Prompt Templates | Compilação Inteligente de Regras | Como administrador do catálogo, desejo interagir com o Agente de IA para converter critérios de governança textuais em especificações JSON ativas, eliminando a necessidade de novos deploys. |
| **REQ-PRO-001** | Apex AST Walker | Mecanismo de Validação Determinística | Como motor de validação, desejo ler e caminhar pela árvore lógica do JSON compilado para atribuir vereditos rápidos (PASS, FAIL, AVISO) às linhas processadas. |

## 7. Mapeamento de Requisitos para Processos

| **Id. do Requisito** | **Processo L1** | **Processo L2** | **Processo L3** | **Processo L4** | **Processo L5** |
| --- | --- | --- | --- | --- | --- |
| **REQ-BIZ-001** | Product Lifecycle Management | Catalog Management | Lifecycle Operations | Validação de Lotes | Geração de Diagnóstico Narrativo HTML |
| **REQ-TEC-002** | Product Lifecycle Management | Catalog Governance | Rule Creation | LLM Compilation | Validação de Schema contra Spec JSON |

## 8. Análise de Lacunas (Gaps) e Questionário ao Cliente

Com base na ausência de detalhamento explícito e premissas técnicas levantadas no material preliminar, consolidamos o questionário crítico voltado à mitigação de riscos:

| **Prioridade** | **Solução USB Afetada** | **Lacuna de Informação Identificada** | **Risco Associado** | **Pergunta para o cliente** |
| --- | --- | --- | --- | --- |
| **Alta** | 3.2 Diagrama de Sistema e Integração | Especificações técnicas da API e estabilidade do sistema de ofertas externas NBO para o Agente 3. | A1 - Infraestrutura técnica complexa / Atraso na conectividade do agente. | O sistema NBO externo possui documentação formal OpenAPI/Swagger ativa e ambiente de homologação estável disponível para testes imediatos? |
| **Alta** | 3.5 Modelo de Dados & Governança | Volumetria média esperada para o processamento de itens de demanda e impacto na quebra de limites assíncronos. | C3 - Estouro de Heap Memory ou limites operacionais de governos em cenários extremos. | Qual o volume médio e máximo de linhas esperado por arquivo CSV de Demanda? Existe algum plano imediato para cargas que excedam o limite de 50k itens? |
| **Média** | 2.2 Governança do Projeto | Definição da alocação e liderança do papel de Gerente de Projetos (PM). | G1 - Desalinhamento em marcos de entrega por escassez de liderança dedicada. | Fica acordado que o papel de PM será compartilhado com a estrutura existente da SWE liderada pelo Luciano, ou teremos alocação exclusiva Claro? |
| **Média** | 3.4 Recursos e Plataforma | Detalhamento dos artigos de conhecimento e sua categorização correta no Salesforce Service Cloud. | D2 - Ineficiência nas respostas do Agente 1 por falta de taxonomia estruturada. | A lista de 10-15 FAQs lógicas e a estrutura de Data Categories já estão configuradas e saneadas no ambiente sandbox fornecido? |

### Exportação do Questionário Corporativo

Para facilitar o controle das equipes de Delivery, o código estruturado abaixo permite a exportação automatizada da planilha de gestão de riscos:

Python

import pandas as pd

# Criação do DataFrame com as lacunas priorizadas
data = {
 "Priority": ["Alta", "Alta", "Média", "Média"],
 "Affected USB Section": [
 "3.2 Diagrama de sistema e integração",
 "3.5 Modelo de Dados & Governança",
 "2.2 Governança do Projeto",
 "3.4 Recursos e Plataforma"
 ],
 "Information Gap Identified": [
 "Especificações técnicas e estabilidade da API do sistema externo NBO.",
 "Volumetria real de linhas por arquivo CSV de Demanda e risco de concorrência.",
 "Definição final sobre alocação do papel de Project Manager (PM).",
 "Status do saneamento e categorias de dados nos Knowledge Articles da Claro."
 ],
 "Associated Risk": [
 "A1 - Infraestrutura técnica complexa / Falha de integração com Agente 3.",
 "C3 - Limitações de Heap e processamento Apex em cenários massivos (>50k).",
 "G1 - Gargalos em tomadas de decisão e marcos de entrega do cronograma.",
 "D2 - Ineficácia nas respostas do modelo de IA por dados não higienizados."
 ],
 "Questions for the Client": [
 "O sistema NBO externo possui documentação formal OpenAPI/Swagger e ambiente disponível para testes imediatos?",
 "Qual o volume médio e máximo de linhas esperado por arquivo CSV? Há demandas que superam 50k itens?",
 "Fica acordado o reuso da estrutura de PM do SWE com Luciano, ou haverá alocação dedicada?",
 "A lista de 10-15 FAQs prioritárias e a estrutura de Data Categories já estão prontas no Salesforce?"
 ]
}

df = pd.DataFrame(data)
# Salvando o arquivo de exportação em formato compatível com Excel/Planilhas
df.to\_csv("questions\_export.csv", index=False, encoding="utf-8-sig")
print("Arquivo corporativo 'questions\_export.csv' estruturado com sucesso.")

## 9. Estimativa Preliminar de Complexidade e Tamanho (Análise V2)

### 9.3 Estimativa por Capacidades

* **Capacidade Custom Apex AST Walker & Caching Estático:** **Complexidade: Alta | Tamanho: SC**. Exige codificação de algoritmo puro de percurso lógico e contorno de travas de infraestrutura sem auxílio de cache nativo da plataforma.
* **Integração Prompt Templates Einstein via ConnectApi:** **Complexidade: Média | Tamanho: L**. Requer configuração cirúrgica de parâmetros obrigatórios (applicationName) e tratamento robusto contra INTERNAL\_ERROR globais.
* **Implantação de Agentes Autônomos Agentforce:** **Complexidade: Média | Tamanho: L**. Envolve desenho lógico de tópicos separados para tempo de compilação e execução.

### 9.4 Estimativa por Processos

* **Processo de Ingestão Assíncrona de Carga:** **Complexidade: Alta | Tamanho: L**. Encadeamento complexo de transações Queueable controladas por offsets e estados persistidos.

### 9.5 Estimativa de Personalização de Dados (Data Customizing)

* **Modelagem de Objetos Shadow e Custom Metadata:** **Complexidade: Baixa | Tamanho: M**. Criação de campos estruturados no modelo Demanda\_\_c, logs idempotentes e tabelas de decisão CMDT flexíveis em runtime.

### 9.6 Estimativa de Governança e COE

* **Tamanho: M**. O time técnico é reduzido (1 TA, 1 TC, 1.5 QA). A maior parte da governança de dados estruturais e taxonomia de conhecimento fica centralizada e sob responsabilidade do próprio cliente.

### 9.7 Estimativa de Migração de Dados

* **Tamanho: S**. Não há projeto de migração de dados históricos para fins de carga inicial. O escopo restringe-se estritamente à ingestão recorrente e processamento dinâmico dos arquivos em formato CSV anexados no fluxo operacional.

### 9.8 Estimativa de Estratégia de Coexistência (Co-Living)

* **Tamanho: M**. O Salesforce atuará de forma desacoplada como motor de validação isolado. O consumo do sistema de propensão externo NBO será feito via leitura de parâmetros expostos, sem persistência profunda ou reengenharia interna do legado.

### 9.9 Estimativa de Estratégia de Implantação e Implementação

* **Tamanho: L**. A restrição cross-org que impede os mecanismos de Quick Deploy adiciona passos rigorosos e manuais nas esteiras de entrega. Todo deploy exigirá validação unitária explícita e mapeamento criterioso de metadados (RunSpecifiedTests).

### 9.10 Estimativa de Estratégia de Testes (Testing)

* **Tamanho: L**. A validação exige testes extensivos de concorrência, cenários assíncronos encadeados, interceptação de falhas via Transaction Finalizers e simulação de cargas volumosas no limite de CPU orçado por lane.

### 9.11 Estimativa de Estratégia de Segurança

* **Tamanho: M**. Controle baseado em restrições explícitas de Permission Sets (Validacao\_Engine\_Access), com proibição estrita de injeção manual de campos requeridos ou Master-Detail em tags de segurança xml para evitar quebras de deploy.

### 9.2 Estimativa de Alto Nível

A tabela abaixo consolida as dimensões analíticas do projeto:

| **Dimensão de Complexidade** | **Estimativa (S, M, L, XL, SC)** | **Breve Justificativa (Fatores Chave)** |
| --- | --- | --- |
| **Dimensão 1: Escopo Funcional e de Negócios** | **SC** | Substituição do BRE legado através de um interpretador AST customizado e agentes inteligentes de controle. |
| **Dimensão 2: Arquitetura e Dados** | **L** | Processamento *async-first* rigoroso para grandes volumes de dados (LDV) e restrições severas de Cache de plataforma. |
| **Dimensão 3: Entrega e Organização** | **M** | Janela de tempo de desenvolvimento extremamente curta (3 semanas) compensada por um time core enxuto e sênior. |
| **Dimensão 4: Risco do Projeto** | **L** | Bloqueios potenciais relacionados à esteira de DevOps (Quick-deploy ausente) e dependência de APIs de terceiros. |
| **Estimativa Geral** | **Super Custom (SC)** |  |

#### Justificativa Narrativa

Embora o projeto possua uma duração de cronograma enxuta e envolva um número controlado de objetos e usuários operacionais, a **Estimativa Geral é definida como Super Custom (SC)**. Esse cenário é impulsionado por imperativos de engenharia de software complexos dentro da plataforma Salesforce: o desenvolvimento de um interpretador lógico próprio em Apex (AST Walker) , a criação de mecanismos resilientes baseados em Dead Letter Queues e Transaction Finalizers para blindagem contra estouros de CPU , as fortes restrições de arquitetura que proíbem o uso de Platform Cache , e os desafios nas esteiras de deploy impostos pelas regras das instâncias STORM\_PLM e Ibuy.

### 9.1 Resumo da Estimativa

**Estimativa Geral do Projeto: Super Custom (SC)** O projeto caracteriza-se pelo desenvolvimento de arquitetura avançada sobre a plataforma Salesforce, combinando inteligência artificial autônoma via Agentforce e engenharia de código sob medida altamente performática.

## [SYSTEM: AUDIT PROTOCOL - MANDATORY] COMPLETED :: VALIDATION KEY: E-6KARS5X8
