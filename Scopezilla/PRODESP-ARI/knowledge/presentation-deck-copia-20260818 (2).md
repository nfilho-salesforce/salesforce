salesforce

Parecer da Análise Técnica · 19 de agosto de 2026

# Portal Desenvolve SP Análise Técnica da Solução Salesforce

Portal de crédito fim-a-fim para entrega de valor em 2026.

Cliente

Desenvolve SP

Autores

Giselle Hamano · Pedro Martire · Adriana Cardoso · Felipe Guerra

Objetivo

## Apresentar o plano de entrega do portal de crédito fim-a-fim no Salesforce — com a lógica de crédito mantida na Sinqia — para a Desenvolve SP entregar valor em 2026.

Catálogo de funcionalidades

## A jornada em 6 pilares (épicos) — funcionalidades, integrações e componentes

| Pilar (épico) | Tam. | Func. | Integr. | Comp. | Foco |
| --- | --- | --- | --- | --- | --- |
| 1 · Captação QA | P | 5 | 2 | 9 | Login CPF/CNPJ, enriquecimento JUCESP, simulador de crédito público, cadastro manual de contas, visibilidade de cooperativas |
| 2 · Pré-qualificação | G | 5 | 11 | 6 | Formulário de pedido adaptativo, validação facial BioValid, exclusão/isenção QRSA, faturamento via Serpro, envio síncrono ao core |
| 3 · Proposta | M | 2 | 4 | — | Lista e detalhamento das solicitações com status sincronizado do Sinqia (leitura); o aceite/recusa migrou para o Pilar 5 |
| 4 · Estruturação | G | 6 | 8 | 14 | Fichas cadastrais PF e PJ (sócios/garantidores), geração de PDF, upload assíncrono de anexos, pendências de documentação |
| 5 · Aprovação | M | 2 | 1 | 1 | Decisão do cliente: tela de proposta (detalhes financeiros) + aceite/recusa que grava/liquida/consolida no core; orquestração via ocorrências como mecanismo |
| 6 · Formalização | M | 4 | 4 | 3 | Download e upload da CCB (assinatura manual), pendências de garantias pós-comitê, sessão de contratos com detalhes da operação |
| Total da jornada | 2G·3M·1P | 24 | 30 | 33 | 6 épicos · 3 jornadas |

Plano de entrega · Cronograma

## Plano de entrega

Marco · 30/11

Discovery / Foundation

Fase 0

Pilar 1 · Captação

Squad 1

Pilar 2 · Pré-qualificação

Squad 2

Pilar 3 · Proposta

Squad 1

Pilar 4 · Estruturação

Squad 1

Pilar 5 · Aprovação

Squad 2

Pilar 6 · Formalização

Squad 2

Ago/26Set/26Out/26Nov/26Dez/26Jan/27

Squad 1
 Squad 2

**⚠ Atenção:** o cronograma cobre **do Discovery (Fase 0) até a finalização do QA**. **Início esperado em 24/08/2026** — o cronograma apresentado só se sustenta a partir dessa data de arranque.

Plano de entrega · Marcos mensais

## O que o cliente ganha a cada mês

Cada marco entrega uma capacidade de negócio pronta para uso — as funcionalidades que a compõem estão listadas abaixo.

SET2026

Fundação pronta para construir

Discovery concluído: contratos de API, write-back Sinqia, cálculo QRSA, ambiente e fornecedor definidos.

OUT2026

Captação — cadastro e visibilidade · P1 Captação

Cadastro manual de conta (Jornada Agro) · sessão de contas (Jornada Agro) · visibilidade de cooperativas (Jornada Agro) · refatoração da API Serasa.

NOV2026

Solicita e acompanha a proposta · P2 Pré-qualificação + P3 Proposta

Formulário adaptativo · BioValid · exclusão/isenção QRSA · Serpro · envio ao core · lista e detalhamento das solicitações com status.

DEZ2026

Cliente aprova a proposta · P5 Aprovação

Tela de proposta com detalhes financeiros + aceite/recusa do cliente, com efetivação síncrona no core (Sinqia).

JAN2027

🏁 Jornada de crédito completa · P4 Estruturação + P6 Formalização

Fichas PF/PJ com reaproveitamento · geração de PDF · bloqueio de edição · upload assíncrono · pendências de documentação · CCB (download/upload) · garantias · sessão de contratos.

Riscos e premissas dos prazos

## Riscos e premissas do cronograma

O cronograma vale **sobre um conjunto de premissas** (à esquerda). Os **riscos ainda em aberto** (à direita) ameaçam o prazo se não forem resolvidos — cada um endereçado na **Fase 0** protege o cronograma.

Premissas — a base dos prazos

| Premissa | Se não valer |
| --- | --- |
| **Escopo integral fixo** 24 func · 30 integr · 33 comp | Mudança de escopo desloca o prazo nas duas pontas. |
| **Captação reaproveitada** já em QA | Retrabalho na Captação soma esforço não previsto. |
| **Integrações do Sinqia prontas na hora certa** cada API do Sinqia entregue **ao menos 1 semana antes** de a frente começar o pilar que a consome | Se a API não chegar com essa antecedência, a frente para no início do pilar e o prazo desloca. |

Riscos — o que ameaça o prazo

| Risco | Efeito no prazo |
| --- | --- |
| **Contratos das 30 APIs em aberto** | Documentação/contratos das APIs em finalização (30 de 30 a confirmar, só JUCESP em QA) — bloqueiam o backbone e o caminho crítico, a maior fonte de retrabalho tardio. |
| **Aprovação das 3 frentes antes de iniciar** | Cada pilar/funcionalidade exige alinhamento das três frentes (Salesforce · DSP · Sinqia/Evertec) antes de começar — o gate de entrada atrasa o início e reduz o ganho do paralelismo. |
| **Requisitos ainda em nível macro** | Escopo detalhado só na refinação — pode revelar complexidade não prevista (regras, exceções, telas), pressionando o prazo. |

salesforce

# Obrigado

Portal Desenvolve SP · Análise Técnica da Solução Salesforce

Cliente

Desenvolve SP

Autores

Giselle Hamano · Pedro Martire · Adriana Cardoso · Felipe Guerra

salesforce

Portal Desenvolve SP · Cenário de escopo

# Proposta de MVP

MVP Funcional — corte por complexidade, preservando as 3 esteiras da jornada de crédito.

Cliente

Desenvolve SP

Autores

Giselle Hamano · Pedro Martire · Adriana Cardoso · Felipe Guerra

Escopo proposto

## MVP Funcional — o que entra, o que difere para a Fase 2

19/24

funcionalidades

15/19

integrações

31/33

componentes

3

esteiras no baseline

Entra — a jornada de crédito fim-a-fim

* **Captação** — login/JUCESP, contas, simulador, lista de solicitações
* **Pré-qualificação** — wizard de solicitação, **QRSA completo**, SERPRO, envio síncrono ao core
* **Proposta** — lista e detalhes das solicitações com status
* **Aprovação** — tela de proposta + aceite/recusa do cliente (efetivação síncrona no core)
* **Estruturação** — Fichas Cadastrais PF e PJ (14 componentes), upload via Salesforce Files
* **Acompanhamento** — status em leitura (Sinqia → Salesforce)
* **Formalização** — download da CCB + upload da CCB assinada por fora

Todas as 3 esteiras recebem o mesmo baseline — a diferença Digital/Julgamental (cadastro manual, cooperativas) é preservada, não é o fundamento do corte.

Não entra

* **Central de Pendências** + **retorno síncrono ao Sinqia** — dependem do contrato de ocorrências
* **Meus Contratos** (consulta histórica de contratos vigentes)
* **Biometria BioValid** → contingência manual por padrão
* **Assinatura digital da CCB** → assina por fora e devolve o arquivo

A maioria já está **bloqueada por contratos de API não fechados** — diferir alinha o escopo às dependências reais.

Sugestão de cronograma · MVP Funcional

## Comparativo das vias de entrega — escopo do MVP Funcional

Meta Proposta DSP 30.09

~7 sem

Tradicional

Entrega manual, sem IA — a âncora de referência

15 sem

24 sem

Aumentada

Time humano acelerado por ferramentas de IA

12 sem

22 sem

Agosto/2026Setembro/2026Outubro/2026Novembro/2026Dezembro/2026Janeiro/2027Fevereiro/2027Março/2027Abril/2027Maio/2027

melhor caso (mín.)
 pior caso (máx.)

**⚠ Atenção:** os prazos estão associados aos **riscos e premissas apresentados adiante**. As datas consideram do **refinamento até QA** e **não incluem** o período de **homologação por parte do cliente**. Faixas benchmark, não compromisso; tempo de calendário.

salesforce

# Obrigado

Portal Desenvolve SP · Análise Técnica da Solução Salesforce

Cliente

Desenvolve SP

Autores

Giselle Hamano · Pedro Martire · Adriana Cardoso · Felipe Guerra

Anexo

# Material de Referência

Detalhamento por pilar · APIs e componentes · 6 pilares (E01–E06)

Material de referência · Mapa da jornada

## Os 6 pilares e as 24 funcionalidades da jornada única

1 · Captação

* **F01** Enriquecimento cadastral via JUCESP
* **F02** Cadastro manual de conta (Julg./Agro)
* **F03** Simulador de crédito unificado
* **F04** Sessão "Minhas Contas"
* **F05** Visibilidade e hierarquia de cooperativas (Agro)

2 · Pré-qualificação

* **F06** Formulário de pedido adaptativo
* **F07** Validação facial (Digital)
* **F08** Exclusão socioambiental / QRSA
* **F09** Autorização de faturamento (Serpro e-CAC)
* **F10** Envio síncrono ao core

3 · Proposta

* **F11** Lista de solicitações do tomador
* **F12** Detalhamento das solicitações (status)

4 · Estruturação

* **F14** Ficha Cadastral PJ (reaproveitamento)
* **F15** Ficha Cadastral PF (sócios, garantidores)
* **F16** Geração de PDF da ficha
* **F17** Bloqueio de edição em análise
* **F18** Upload assíncrono de arquivos
* **F19** Orquestração de status
* **F20** Central de Pendências

5 · Aprovação (decisão do cliente)

* **F13** Aceite/recusa da proposta — tela + efetivação síncrona no core
* **F21** Orquestração via ocorrências (mecanismo)

6 · Formalização

* **F22** Download da Ficha CCB
* **F23** Upload da CCB assinada
* **F24** Sessão "Meus Contratos"

Material de referência · Ponto de partida

## Pilar 1 · Captação — desenvolvido e em QA

5

funcionalidades entregues

17

user stories concluídas

12

user stories de integração

Funcionalidades desenvolvidas

* Simulador de crédito público (área guest, sem login)
* Login + MFA, redefinição/alteração de senha, logout
* Conversão Lead → Person Account (OTP)
* Home logada e inicio de Nova Solicitação
* Lista de Solicitações

Integrações e regras já operando

* **JUCESP** — vínculo societário CNPJ×CPF (em QA)
* **Serasa R6** — antifraude com classificação de risco
* Matriz de decisão (**BRE**) — roteamento por risco/produto
* Auditoria imutável das análises (AnalisysResult)

**Status de qualidade:** em SIT/UAT (10–21/08).

**Observação de escopo:** a integração da API Serasa exigirá refatoração — este esforço entra neste escopo.

**Nota:** parte da solução já entregue exigirá refatoração parcial para integrar-se à jornada completa (a integração da API Serasa é o caso já identificado) — esse esforço está previsto neste escopo.

Material de referência · Formas de entregar

## De onde vêm os prazos: a complexidade dos 6 pilares define a faixa

A base — mix de complexidade dos épicos

| Pilar | Tam. | Func·Integr·Comp |
| --- | --- | --- |
| 1 · Captação | S | 5·2·9 |
| 2 · Pré-qualificação | L | 5·11·6 |
| 3 · Proposta | M | 2·4·— |
| 4 · Estruturação | L | 6·8·14 |
| 5 · Aprovação | M | 2·1·1 |
| 6 · Formalização | M | 4·4·3 |

As vias comprimem a MESMA base — em tempo de calendário

| Via | Duração (2 times) | Compressão do tempo |
| --- | --- | --- |
| **Tradicional** (âncora) | ~14–26 sem | base sem compressão |
| **Aumentada** | ~12–22 sem | −10 a 25% do tempo (ferramentas IA) |

**Prazos com 2 times em paralelo** — as duas frentes pesadas (P2 e P4) correm ao mesmo tempo, derrubando o piso; com 1 time as faixas seriam ~18–28 (Tradicional) e ~14–26 (Aumentada). A compressão reduz o **tempo de calendário**, não o escopo.

**⚠ Atenção:** os prazos estão associados aos **riscos e premissas apresentados adiante**. As datas consideram do **refinamento até QA** e **não incluem** o período de **homologação por parte do cliente**.

Material de referência · Parecer de viabilidade

## Parecer: Análise Técnica da Solução Salesforce

A solução alternativa — portal fim-a-fim no Salesforce com a lógica de crédito na Sinqia — é **tecnicamente viável** para o escopo integral (3 esteiras · 24 funcionalidades · 30 integrações · 33 componentes). A restrição é de **prazo**.

Estimativas por via de entrega — escopo integral (cronograma paralelo)

| Via | 1 time | 2 times (paralelo) | vs. ~7 sem |
| --- | --- | --- | --- |
| **Tradicional** (âncora) | ~18–28 sem | **~14–26 sem** | 2,0× a 3,7× |
| **Aumentada** | ~14–26 sem | **~12–22 sem** | 1,7× a 3,1× |

Duas frentes em paralelo (P2 e P4 concorrentes) derrubam o piso; a via Aumentada comprime cada faixa mais −10 a 25% (ferramentas de IA). Faixas benchmark top-down, tempo de calendário (refinamento até QA, sem homologação do cliente) — não compromisso. Mesmo o melhor piso (~12 sem) supera a meta de ~7 sem.

Recomendação

Seguir com o escopo integral no Salesforce

A arquitetura fecha: núcleo passivo event-first, MuleSoft orquestrando a Sinqia, Captação já em QA. O risco é de **cronograma**, não de viabilidade. A decisão honesta é **ajustar a data de go-live** à faixa realista de entrega.

Antes de fixar prazo — abrir a Fase 0

Definir o **fornecedor de build** e a **data de início**, fechar os **contratos das APIs** e dimensionar o **time**. Cada premissa resolvida encolhe a faixa e converte a estimativa benchmark em compromisso defensável.

Material de referência · Arquitetura

## System Landscape — Salesforce, MuleSoft e o ecossistema Desenvolve SP

USUÁRIOS & CANAIS

Visitante (guest)

Tomador PF/PJ

Cooperativa

Analista / Comitê

▼ HTTPS / SSO (MFA)

SALESFORCE

Experience Cloud (LWR) — Portal do Cliente
simulador guest · wizard · fichas · acompanhamento · formalização

Salesforce Platform — Backoffice leve
Analista · Comitê · triagem · pendências

Dados: Lead · Person Account · Opportunity/OLI · Product2 (EPC) · Case

Serviços headless (Apex) · **BRE** (matriz de decisão)

**Platform Event** OpportunityInfo · ocorrências · auditoria imutável

▲▼   evento Pub/Sub (avanço + birôs)  ·  write-back via API padrão

INTEGRAÇÃO

MuleSoft Anypoint — orquestração · transformação · retry/DLQ · seleção de birôs

▼

SISTEMAS EXTERNOS

**Sinqia / Officer**
sistema de registro — esteira, regras, cálculo, aprovação, CCB

**JUCESP**
vínculo societário

**Serasa R6**
antifraude

**Serpro**
faturamento e-CAC

**BioValid**
facial · SENATRAN/CNH

**Núcleo passivo, event-first:** o Salesforce publica no barramento e o MuleSoft orquestra Sinqia + birôs, gravando o retorno via API padrão.

Material de referência · Perspectiva de integração

## Arquitetura de integração — API-Led Connectivity em 3 camadas via MuleSoft

34

**pontos de integração** no build
28 System · 5 Process · 1 Experience

10k–100k

**requisições/dia**
operação síncrona REST · sem batch/bulk

Por que API-Led

O gateway **agrega** Cliente + Crédito + Contratos em uma chamada, com **caching** e **rate-limiting** — desempenho sob o volume acima. Salesforce nunca chama Sinqia diretamente.

Arquitetura — API-Led Connectivity em 3 camadas

Salesforce · Portal de Crédito — consome uma única porta de entrada, nunca chama os sistemas externos diretamente

▼

Experience Layer · gateway

**1 Experience API** — porta única para o Salesforce: **agrega** Cliente + Crédito + Contratos em uma chamada, faz **caching** e **rate-limiting**, com versionamento e compatibilidade. Extensível a canais futuros (mobile, parceiros).

↕

Process Layer · orquestração

**5 Process APIs** — orquestram a lógica de negócio: geração de CCB, workflow de aceite/recusa, validação facial (BioValid), impressão de documentos e compliance (QRSA).

↕

System Layer · backend

**28 System APIs** — integram o legado **SINQIA** (mainframe BJ21M05 / BJ04M06 / BJ33M10) e os sistemas externos: **JUCESP** (em QA) e **Serpro**.

**⚠ A confirmar:** refinamento dos pontos de integração enviados (a confirmar; só JUCESP em QA) · SLAs por API, DR/HA e estratégia de erro/DLQ. **30 → 34:** as 30 APIs do slide anterior são o grão da planilha do cliente; o build MuleSoft acrescenta a **Experience API** (gateway, não estava na planilha) e conta **sub-serviços** como APIs distintas.

Material de referência · Lista de integrações

## As 30 APIs da jornada — planilha Discovery v3.1

| ID | Pilar | API / Serviço |
| --- | --- | --- |
| **API-01** | Captação/Solic. | Consulta de Solicitações do Cliente |
| **API-02** | Pré-qualificação | Detalhamento de Solicitação |
| **API-03** | Formalização | Lista de Contratos |
| **API-04** | Formalização | Arquivo de Contrato (dados + arquivo) |
| **API-05** | Pré-qualificação | Consulta de Declarações |
| **API-06** | Pré-qualificação | Criação de Declarações |
| **API-07** | Captação | Integração JUCESP (vínculos + cadastro) QA |
| **API-08** | Pré-qualificação | Imprimir Solicitação |
| **API-09** | Aprovação | Comando de Aceite / Recusa (Workflow) |
| **API-10** | Estruturação | Categorização de Tipo de Arquivo |
| **API-11** | Estruturação | Leitura de Conta e Contato |
| **API-12** | Estruturação | Criação de Conta e Contato |
| **API-13** | Estruturação | Edição de Conta e Contato |
| **API-14** | Estruturação | Imprimir Ficha Cadastral |
| **API-15** | Estruturação | Sincronização de Contas |

| ID | Pilar | API / Serviço |
| --- | --- | --- |
| **API-16** | Pré-qualificação | Fim de Solicitação Sinqia "Conta-Proposta" |
| **API-17** | Pré-qualificação | Endpoints de Listas de Valor (múltiplas) |
| **API-18** | Captação | Dados de Simulação (empréstimo pretendido) |
| **API-19** | Estruturação | Armazenamento de Anexos |
| **API-20** | Pré-qualificação | Lista "Parceiro que indicou" |
| **API-21** | Captação | Sensibilização ao Sinqia no Login |
| **API-22** | Proposta | Declaração (QRSA) — leitura |
| **API-23** | Proposta | Declaração (QRSA) — gravação |
| **API-24** | Proposta | Declaração (QRSA) — comando |
| **API-25** | Proposta | Declaração (QRSA) — cálculo/rating |
| **API-26** | Estruturação | Ficha Cadastral PJ |
| **API-27** | Pré-qualificação | Validação Facial (BioValid, 3 steps) |
| **API-28** | Pré-qualificação | Entidade Empresarial |
| **API-29** | Formalização | Assinatura da CCB (a prever) |
| **API-30** | Formalização | Geração da CCB |

Fonte: Lista de APIs Discovery da Jornada Digital + Julgamental v3.1 · 30 APIs distintas (41 endpoints com sub-serviços) · todas via MuleSoft · status a confirmar (só JUCESP em QA). O build MuleSoft acrescenta a Experience API (gateway) → 34.

Material de referência · Pilar 1

## Pilar 1 · Captação — 2 APIs · 9 componentes

APIs a desenvolver (2)

* **API-07** — Integração JUCESP (vínculos + cadastro) em QA
* **API-21** — Sensibilização ao Sinqia no login

Antifraude Serasa R6 já opera (via BRE). Simulador reaproveitado da Captação (QA).

Componentes a desenvolver (9)

* **CMP-01/02** — Header + carousel por onboarding
* **CMP-03/04** — Navegação (remover "Escolher Conta")
* **CMP-05/06** — Lista de solicitações + filtros
* **CMP-07** — Painel de pendências
* **CMP-08** — Lista de contratos (download CCB)
* **CMP-09** — Lista de contas vinculadas

Fonte: user-stories.json · Apresentação Final p.6 · Lista de APIs Discovery · Lista de Componentes Discovery (Tela Home). APIs = endpoints da planilha Discovery (grão distinto das 30 integrações da jornada).

Material de referência · Pilar 2

## Pilar 2 · Pré-qualificação — 8 APIs · 6 componentes

APIs a desenvolver (8)

* **API-05/06** — Declarações (consulta / criação)
* **API-22/23/25** — QRSA (perguntas, respostas, cálculo)
* **API-18** — Dados de simulação
* **API-16** — Conta-Proposta (submissão síncrona)
* **API-27** — Validação facial BioValid opcional

Faturamento Serpro sem endpoint na planilha — a confirmar.

Componentes a desenvolver (6)

* **CMP-10** — Orquestrador do wizard (multi-step)
* **CMP-11** — Dados gerais (parceiro, canal, operação)
* **CMP-12** — Dados da solicitação (simulação)
* **CMP-13** — Declarações (QRSA parametrizável)
* **CMP-14** — Anexos (upload categorizado)
* **CMP-15** — Tela de confirmação e envio

Fonte: user-stories.json · Apresentação Final p.7 · Lista de APIs Discovery · Lista de Componentes Discovery (Tela de Solicitação de Crédito). APIs = endpoints da planilha (grão distinto das 30 integrações).

Material de referência · Pilar 3

## Pilar 3 · Proposta — 4 APIs · 1 componente

APIs a desenvolver (4)

* **API-01** — Consulta de solicitações do cliente
* **API-02** — Detalhamento de solicitação
* **API-08** — Imprimir solicitação
* **API-09** — Comando de aceite / recusa (workflow)

Componentes a desenvolver (1)

* **CMP-30** — Acompanhamento de pedido (timeline de status + histórico)

Lista e detalhamento reaproveitam os componentes da Home (Pilar 1).

Fonte: user-stories.json · Apresentação Final p.8 · Lista de APIs Discovery · Lista de Componentes Discovery (Tela de Acompanhamento). APIs = endpoints da planilha (grão distinto das 30 integrações).

Material de referência · Pilar 4

## Pilar 4 · Estruturação — 9 APIs · 14 componentes

APIs a desenvolver (9)

* **API-11** — Leitura de conta e contato
* **API-12/13** — Criação / edição de conta e contato write a confirmar
* **API-15** — Sincronização de contas
* **API-17** — Endpoints de listas de valor
* **API-26/28** — Ficha PJ / entidade empresarial
* **API-14** — Imprimir ficha cadastral
* **API-10 / API-19** — Categorização e anexos

Componentes a desenvolver (14)

* **CMP-16→23** — Ficha PF: orquestrador, identificação, cônjuge, endereço, dados profissionais, participações, PEP, anexos
* **CMP-24→29** — Ficha PJ: orquestrador, identificação, dados complementares, sócios, participações, anexos

Fonte: user-stories.json · Apresentação Final p.9 · Lista de APIs Discovery · Lista de Componentes Discovery (Fichas Cadastrais PF/PJ). APIs = endpoints da planilha (grão distinto das 30 integrações).

Material de referência · Reanálise do Pilar 5

## Reanálise · Pilar 5 · Aprovação — é a decisão do cliente sobre a proposta

O pilar vinha mapeado como orquestração de ocorrências (sincronização de status, sem tela). Revisando a esteira com o cliente, o **propósito do Pilar 5 é a etapa em que o tomador aprova ou recusa a proposta enviada pela Desenvolve SP** — o aceite/recusa comercial, com tela e decisão do usuário. A orquestração de ocorrências continua, mas como **mecanismo**, não como o propósito do pilar.

Como estava mapeado (a corrigir)

* **"Sincronização de status finais de crédito"** — F21, orquestração de ocorrências customizadas do Sinqia
* Tratado como **backbone sem tela** — mecanismo técnico, sem componente de decisão do cliente
* O aceite/recusa da proposta ficava em **F13 · Aceite Síncrono**, dentro do Pilar 3 · Proposta

O que o Pilar 5 realmente é

* Etapa em que o **cliente aprova ou recusa** a proposta que a DSP enviou
* **Tela de proposta** com detalhes financeiros (parcelas, taxas) + comando aceitar/recusar
* O aceite **grava, liquida e consolida** a decisão no core (Sinqia) e libera a esteira → Estruturação
* **Absorve o aceite** antes mapeado como F13 no Pilar 3

Impacto a propagar

**Pilar 3 · Proposta** perde o aceite (F13) — passa a lista, detalhe e acompanhamento de status. · **Pilar 5** deixa de ser "sem tela": ganha componente de decisão → **o sizing sobe** (M pode virar L). · A **orquestração de ocorrências** permanece como o mecanismo que sinaliza "proposta pronta" e grava a resposta no legado.

Fonte: correção do scoper (participante das sessões de entendimento) · Apresentação Final p.7,10 · transcrições 07/08 e 10/08 (aceite/recusa da proposta). **Confiança: Assumed** — contradiz o mapa v21 (F21) e Cenários de Entrega; a propagar via *revise* para P3/P5, estimates e roadmap.

Material de referência · Pilar 5

## Pilar 5 · Aprovação — a decisão do cliente sobre a proposta

Componente de decisão (1 tela)

* **Tela de proposta** com detalhes financeiros — parcelas (line items), taxas, condições
* Comando **aprovar / recusar** — o aceite grava, liquida e consolida a operação síncronamente no core (Sinqia)
* Absorve o antigo **F13 · Aceite Síncrono** (antes mapeado no Pilar 3)

Consistência transacional do aceite (rollback/idempotência em falha) é o ponto de maior cuidado.

Mecanismo — orquestração via ocorrências (1 integração)

* Ocorrências do Sinqia via MuleSoft (Pub/Sub) sinalizam **"proposta pronta"** e gravam a resposta do cliente no legado
* Platform Event **OpportunityInfo** + consumidor Apex; matriz **BRE** versionável
* Máquina de estados para etapas bloqueantes

A orquestração é o mecanismo que serve a decisão — não o propósito do pilar. Estratégia de erro/retry (DLQ) a definir.

Fonte: Apresentação Final p.7,10 · transcrições 07/08 e 10/08 · ADR-011/015/016. **Confiança: Assumed** — reanálise do scoper (participante das sessões) que realoca o aceite do Pilar 3 para cá; contradiz o mapa v21 (F21).

Material de referência · Sizing do Pilar 5

## Por que o Pilar 5 · Aprovação é tamanho L

Reclassificado de M para **L** com a reanálise: o pilar deixou de ser "backbone sem tela" e passou a conter a **decisão do cliente sobre a proposta** — ganhou uma tela de proposta e, sobretudo, a **efetivação síncrona no core** que grava/liquida/consolida a operação (antes em F13/Pilar 3). O driver dominante é a integração de efetivação, não mais a orquestração.

O que puxa para L

* **Efetivação síncrona no core** (integration = L) — o aceite grava/liquida/consolida a operação no Sinqia; consistência transacional (rollback/idempotência) é o maior cuidado da jornada
* **Tela de proposta** (UI = M) — detalhes financeiros (parcelas como line items, taxas) + comando aprovar/recusar em LWC com controlador Apex; o pilar antes não tinha tela
* **Orquestração via ocorrências** (automation = M) — agora o mecanismo que sinaliza "proposta pronta" e grava a decisão no legado; Platform Event + matriz BRE
* **Absorve o esforço** que sustentava o M do antigo Pilar 3

O que segura em L (não é XL)

* Uma única tela de decisão + uma integração de efetivação — escopo focado, não uma suíte
* Modelo de ocorrências **confirmado 13/08** — o mecanismo de sinalização já está definido e mais simples
* Cancelamento só por status — sem ocorrência/pendência dedicada

**Sobe para XL se** a efetivação síncrona exigir orquestração transacional ampla (compensação/rollback) ou a estratégia de erro/DLQ do write-back (PUT/PATCH) se mostrar extensa na refinação (gap G0704).

Fonte: estimates.json (E05) · reanálise do scoper · ADR-011/015. Tamanho = complexidade relativa, não esforço nem preço. Confiança: **Assumed** — reanálise que realoca o aceite (F13) do Pilar 3 para cá; contradiz o mapa v21 (F21).

Material de referência · Pilar 6

## Pilar 6 · Formalização — 5 APIs · 3 componentes

APIs a desenvolver (5)

* **API-30** — Geração da CCB (BBP a avaliar)
* **API-04** — Arquivo de contrato (CCB)
* **API-29** — Assinatura da CCB (provedor a definir)
* **API-24** — Declaração QRSA / assinatura
* **API-03** — Lista de contratos

Assinatura manual no MVP (sem provedor digital nativo).

Componentes a desenvolver (3)

* **CMP-31** — Orquestrador de contratação
* **CMP-32** — Declaração / aceite final
* **CMP-33** — Anexos finais (garantias)

"Meus Contratos" reaproveita o componente de contratos da Home (Pilar 1).

Fonte: user-stories.json · Apresentação Final p.11 · Lista de APIs Discovery · Lista de Componentes Discovery (Tela de Contratação). APIs = endpoints da planilha (grão distinto das 30 integrações).

Material de referência · Esteira Agro

## Esteira Agro — insumos da sessão de 11/08

Como o Agro difere da esteira PJ

* Toda a esteira da DSP foi desenhada para **PJ**; o Agro é a exceção (novo na DSP desde 2025, antes era Banco do Brasil)
* Maioria dos tomadores é **pessoa física**; produtor rural PF **não está na JUCESP** (PJ rural está)
* Eric: **não é preciso replicar** a validação JUCESP para o PF rural
* No formulário, muda essencialmente **CPF ↔ CNPJ**
* Ficha Cadastral PF e PJ é **a mesma**
* **Sem QRSA** no Agro · apenas **2 produtos**
* Motor de crédito Agro é **externo** e de **volume muito baixo**

Cooperativa — entrada e acesso

* Duas formas de entrada de pedidos: via **parceiro/cooperativa** (login do consultor) ou **direto pelo cliente**
* Cooperativa **não passa** pela verificação JUCESP; hoje conta como usuário comum da DSP
* Precisa **criar as contas da Cooperativa no Salesforce** e um tipo de usuário distinto (permissões como funcionário)
* Acessa: **visualiza pedidos** · simulador opcional · Fichas PF/PJ · JUCESP opcional
* Acompanhamento do CNPJ/solicitante é feito pela Cooperativa · exige **Hierarquia de Contas**
* Ideal: poder **enviar todos os dados de uma vez**; a cooperativa já tem o motor de crédito

Decisões em aberto

* **Modelo de portal:** foram pedidos 2 portais (Cooperativa / Cliente); a linha vinha indo para o **unificado** — decisão pode ser revista
* **Enquadramento manual:** avaliar se continua sendo feito no Sinqia
* **Conta corrente** é pedida para PJ; para o Agro precisa ser repensada
* Cadastro de produto duplicado (Core Bancário + Officer): avaliar se o SF precisa cadastrar tudo ou só produtos padrão
* Nada específico de Agro foi fechado — **retomar na sessão de quinta (13/08)**

Fonte: discovery-notes/ultimasessao11-08.md (notas da sessão com o cliente, 11/08). Insumos de descoberta — pontos de trabalho e decisões em aberto, não escopo confirmado.

Material de referência · MVP Funcional

## MVP Funcional — escopo completo por pilar (Cenário 2)

| Pilar | Incluídas no MVP | Cortadas / simplificadas → Fase 2 | Comp. | Integr. |
| --- | --- | --- | --- | --- |
| **1 · Captação** | Login/JUCESP, simulador, contas, lista de solicitações | Cadastro manual sem-JUCESP e Cooperativas cortadas · Central de Pendências e Meus Contratos diferidos | 7 | 2 |
| **2 · Pré-qualificação** | Formulário adaptativo, SERPRO, envio síncrono · **QRSA completo** · biometria em contingência | BioValid API | 6 | 7 |
| **3 · Proposta** | Lista e detalhes das solicitações com status (leitura via backbone do P5) | — | — | — |
| **4 · Estruturação** | Fichas PF e PJ, upload via Salesforce Files, status em leitura | PDF estático e reabertura de campos cortadas · retorno síncrono e repositório externo diferidos | 14 | 3 |
| **5 · Aprovação** | Tela de proposta + aceite/recusa (efetivação síncrona no core) · orquestração via ocorrências como mecanismo | Retorno síncrono ao Sinqia → Fase 2 (contrato de ocorrências) | 1 | 1 |
| **6 · Formalização** | Download da CCB + upload da CCB assinada por fora | Meus Contratos cortado · assinatura digital da CCB diferida | 3 | 2 |
| Total | 19 de 24 funcionalidades | 5 não entram | 31 | 15 |

15 integrações incluídas

Consulta de solicitações · parceiro indicador · leitura/criação de conta e contato · declarações · Lista de Valores dos Formulários · SERPRO e-CAC · Conta-Proposta · detalhamento · QRSA perguntas · QRSA respostas · QRSA cálculo de rating · categorização de arquivo · anexos (SF Files) · status (leitura) · download da CCB

4 integrações não entram

BioValid · QRSA assinatura · assinatura da CCB · lista/arquivo de contratos (Meus Contratos)

Fonte: Cenários de Entrega (Cenário 2 · MVP Funcional). Corte por complexidade — mantém as 3 esteiras no baseline. Escopo indicativo pela complexidade relativa, não compromisso.

Material de referência · Cortado do MVP

## O que sai do MVP — itens diferidos para a Fase 2

Cada item tem alternativa operacional hoje ou depende de algo ainda em aberto. A maioria está travada por **contratos de API não fechados** — diferir alinha o escopo às dependências reais, sem restringir jornada.

| Item | Complexidade | Dependência para a Fase 2 |
| --- | --- | --- |
| **Central de Pendências** (CMP-07) | Muito Alta | Contrato de ocorrências customizadas do Sinqia |
| **Retorno síncrono ao Sinqia** (status bidirecional) | Alta | Contrato de ocorrências customizadas do Sinqia |
| **Meus Contratos** (CMP-08) | Alta | Definir cache + APIs de lista/arquivo de contratos |
| **Biometria BioValid** (integração plena) | Alta | Certificação com o BioValid |
| **Assinatura digital da CCB** (CMP-32) | Alta | Contratação de provedor de assinatura |
| **Repositório externo de anexos** (>12 MB) | Média | Definição de arquitetura (S3 vs alternativa) |
| **Cadastro manual sem-JUCESP** (produtor rural PF) | Média | Desenho do fluxo Julgamental/Agro |
| **Cooperativas Agro** (hierarquia de contas) | Média | Decisão arquitetural de hierarquia + modelo de portal |
| **PDF estático da ficha** · **Reabertura de campos** | Baixa | Nenhuma — menor esforço e menor criticidade |

**Riscos residuais a aceitar:** sem a Central de Pendências, o backoffice Julgamental fica pior que hoje · Salesforce Files (12 MB) é insuficiente para documentos Agro (penhor de safra, escrituras).

Fonte: Cenários de Entrega (Cenário 2 · o que vai para a Fase 2). Complexidade relativa, não esforço/preço.

Material de referência · Esforço e paralelismo

## Dois times em paralelo — efeito nos dois cenários

Como o trabalho se divide em duas frentes

| Frente | Pilares | Carga (tam.) |
| --- | --- | --- |
| **Time A** Transacional / wizard | 1 · Captação · 2 · Pré-qualificação · 3 · Proposta · 5 · Aprovação | S L M L |
| **Time B** Cadastro profundo / contrato | 4 · Estruturação · 6 · Formalização | L M |
| **Espinha compartilhada** Não paraleliza | Backbone de ocorrências (plumbing) · infra · contratos das APIs · SIT/UAT | M |

As duas frentes pesadas — **P2 e P4 (ambas L)** — que hoje correm em sequência passam a correr **ao mesmo tempo**. O backbone de ocorrências (plumbing) gate o status de todos os pilares e é o piso compartilhado das duas frentes.

Efeito no prazo (via Tradicional, âncora)

| Cenário | 1 time | 2 times |
| --- | --- | --- |
| **Escopo completo** 24 func · 30 integr · 33 comp | ~18–28 sem | **~14–26 sem** |
| **MVP Funcional** 19 func · 15 integr · 31 comp | ~15–24 sem | **~12–22 sem** |

A via **Aumentada** comprime cada faixa acima em mais **−10 a 25%** (ferramentas de IA), sobre a mesma divisão de frentes.

**⚠ Dois times compram o melhor caso, não o pior.** A frente concorrente derruba o piso (mínimo); o teto (máximo) segue travado pelos **contratos das 30 APIs** e pelo **backbone de ocorrências** — que não paralelizam. Exige a **interface entre as frentes definida cedo** e adiciona custo de coordenação.

Prazos derivados top-down pela forma do engajamento, comprimidos pela concorrência das frentes P2/P4; tempo de calendário. Faixas baseadas em referências, não compromisso. Não convertíveis em horas nem em preço.

Material de referência · Plano de implementação

## Plano de implementação — do discovery ao QA (via Aumentada)

Fases da via **Aumentada** (time humano acelerado por ferramentas de IA), do **refinamento até QA**, com **início em 24/08/2026**. Envelope total **~14–26 semanas** — conclusão do QA entre **30/11/2026** (melhor caso) e **22/02/2027** (pior caso), sem incluir a homologação do cliente. Datas indicativas, não compromisso.

Fase 0

07/09–14/09/26

Fase 1

28/09–19/10/26

Fase 2

26/10–07/12/26

Fase 3

16/11/26–18/01/27

Fase 4

30/11/26–22/02/27

| Fase | Foco | Saída / gate | Conclusão melhor · pior |
| --- | --- | --- | --- |
| **0 · Discovery & Foundation** refinamento | Trava as decisões que gatilham o build: write-back Sinqia (PUT/PATCH), sync do catálogo SF↔Officer, contrato BioValid, cálculo QRSA no Sinqia, e — trava nº 1 — fornecedor de build + data de início. | Premissas confirmadas ou assumidas com donos; fornecedor e início nomeados. É o gate de viabilidade. | 07/09/26 14/09/26 |
| **1 · Backbone + Captação** Pilares 5 & 1 | Sobe a orquestração event-first (ocorrências, matriz BRE, mapa ocorrências↔pendências) e endurece a Captação já em QA (JUCESP, simulador, contas/cooperativas). | Orquestração operacional via MuleSoft; Captação com defeitos de SIT/UAT triados. | 28/09/26 19/10/26 |
| **2 · Pré-qualificação + Proposta** Pilares 2 & 3 · mais pesada | Formulário de crédito adaptativo, QRSA, Serpro, entrada síncrona no core; lista, detalhamento e aceite síncrono da proposta digital. | Cliente completa um pedido fim-a-fim e aceita a proposta com efetivação síncrona no Sinqia. | 26/10/26 07/12/26 |
| **3 · Estruturação + Formalização** Pilares 4 & 6 | Fichas PF/PJ com reaproveitamento, upload assíncrono, pendências de documentação; download/upload da CCB e sessão de contratos (assinatura manual). | Fichas sincronizadas; documentação e garantias tramitam no portal; CCB assinada por fora e re-anexada. | 16/11/26 18/01/27 |
| **4 · SIT / UAT / QA** estabilização | Teste de integração, UAT com dados representativos e endurecimento full-journey nas 3 esteiras (Digital, Julgamental, Agro). | Regressão full-journey verde; pronto para o sign-off de UAT do cliente (homologação fora deste envelope). | 30/11/26 22/02/27 |

Fonte: roadmap.json (Fases 0–4) · faixa Aumentada de estimate-comparison.json (~14–26 sem, comprimida da âncora Tradicional pela banda de eficiência). Datas contadas a partir de 24/08/2026, alocadas por complexidade — cada fase mostra a conclusão no melhor e no pior caso; tempo de calendário, refinamento até QA, sem homologação do cliente. Indicativas, não compromisso; não convertíveis em horas nem preço.

Sugestão de cronograma

## Comparativo das vias de entrega frente à meta de ~7 semanas

Meta Proposta DSP 30.09

~7 sem

Tradicional

Entrega manual, sem IA — 2 times em paralelo

14 sem

26 sem

Aumentada

IA + 2 times em paralelo

12 sem

22 sem

Agosto/2026Setembro/2026Outubro/2026Novembro/2026Dezembro/2026Janeiro/2027Fevereiro/2027Março/2027Abril/2027Maio/2027

melhor caso (mín.)
 pior caso (máx.)

**⚠ Atenção:** faixas com **2 times em paralelo** (frentes P2 e P4 concorrentes). Os prazos estão associados aos **riscos e premissas apresentados adiante**. As datas consideram do **refinamento até QA** e **não incluem** o período de **homologação por parte do cliente**.

Material de referência · Plano de entrega até 30/11

## Faseamento por squad — plano completo até 30/11

Após a Fase 0 (compartilhada), as duas squads fluem em paralelo em ondas encadeadas — cada onda emenda a seguinte, sem ociosidade. Até **30/11**: **5 dos 6 pilares**.

🔍 Fase 0 · Discovery
compartilhada — refinamento, contratos de API, write-back Sinqia, cálculo QRSA, fornecedor + data de início

▼      ▼

Squad 1transacional / decisão

ONDA 1

P1 · Captação

JUCESP · cadastro manual · simulador · contas · cooperativas

→

ONDA 2

P3 · Proposta

Lista · detalhamento com status · orquestração via ocorrências

→

ONDA 3

P4 · Estruturação

Fichas PF/PJ · PDF · bloqueio de edição · upload · pendências

Squad 2cadastro / contrato

ONDA 1

P2 · Pré-qualificação

Formulário adaptativo · BioValid · QRSA · Serpro · envio ao core

→

ONDA 2

P5 · Aprovação

Tela de proposta + aceite/recusa · efetivação síncrona no core

⇢

APÓS 30/11

P6 · Formalização

CCB (download/upload) · garantias · contratos — até o fim do QA

🏁 Marco 30/11 — Pilares 1 a 5 concluídos

Ondas derivadas do cronograma (melhor caso, início 24/08). Faseamento indicativo, não compromisso.

Material de referência · Responsabilidades

## Matriz RACI — responsabilidades por atividade

Três partes: **Prodesp** (infraestrutura e gestão técnica) · **Orange** (implementação Salesforce) · **DSP** (negócio, validação e decisão).

| Atividade | Prodesp infra & gestão técnica | Orange implementação Salesforce | DSP negócio & decisão |
| --- | --- | --- | --- |
| **Refinamento funcional** | I | R | **A** |
| **Refinamento técnico** | C | **A** · R | I |
| **Construção** | C | **A** · R | I |
| **Homologação / UAT** | I | R | **A** |
| **Deploy e go-live** | **A** · R | R | C |
| **Gestão de mudança** | I | C | **A** · R |

**R** Responsible (executa) · **A** Accountable (responde/aprova) · **C** Consulted (consultado) · **I** Informed (informado).

Atribuições propostas a partir dos papéis das três partes — a validar com os patrocinadores antes de assinatura. Não substitui o contrato/SOW.

Material de referência · Visão de 12 semanas

## Visão de 12 semanas — entregas por bloco (melhor caso)

Blocos de semanas alinhados às janelas do cronograma (melhor caso, início 24/08). As duas squads correm em paralelo; cada bloco lista as entregas concretas por pilar.

| Semanas | Squad 1 · transacional / decisão | Squad 2 · cadastro / contrato |
| --- | --- | --- |
| **S1–2** Discovery | **Fase 0 (compartilhada):** refinamento funcional e técnico, contratos das APIs, write-back Sinqia, cálculo QRSA, provedor de assinatura (P6) e ambiente confirmados. | |
| **S3–4** | **P1 · Captação** — JUCESP, cadastro manual, simulador, sessão de contas, cooperativas (endurecimento/finalização). | **P2 · Pré-qualificação (início)** — formulário adaptativo, exclusão/isenção QRSA. |
| **S5–6** | **P3 · Proposta** — lista de solicitações, detalhamento com status, orquestração via ocorrências (mecanismo). | **P2 · Pré-qualificação (conclui)** — BioValid, Serpro/e-CAC, envio síncrono ao core. |
| **S7–9** | **P4 · Estruturação** — fichas PF/PJ, geração de PDF, bloqueio de edição, upload assíncrono, pendências de documentação. | **P5 · Aprovação** — tela de proposta (detalhes financeiros) + aceite/recusa, efetivação síncrona no core. |
| **S10–12** → 30/11 | **P6 · Formalização** — download/upload da CCB, pendências de garantias, sessão de contratos. | **SIT / UAT / estabilização** — regressão full-journey e hardening nas 3 jornadas. |

Premissas que sustentam as 12 semanas

* **Ambiente Salesforce provisionado** (org, sandboxes, acessos) **antes do início** (S1).
* **APIs Sinqia com escopo confirmado** (Swagger/contratos, write-back PUT/PATCH, erro/DLQ) **até a S2**, no fim da Fase 0.
* **Disponibilidade da área de crédito da DSP** para refinamento e **UAT nas S10–12**.
* **P1 · Captação entregue ou em finalização** no início do período (reaproveitamento do que já está em QA).
* **Provedor de assinatura digital (P6) definido antes da S10**, quando a Formalização entra em construção.
* **Início em 24/08** e as duas squads dedicadas em paralelo, sem realocação.

Blocos e janelas derivados do cronograma (melhor caso). Indicativo, não compromisso; se uma premissa não valer, a faixa desloca em direção ao teto (22 semanas).

Material de referência · Escopo por marco

## O que é entregue até 30/09 — Pilar 1 (Captação)

No melhor caso, o marco de **30/09** (≈5 semanas após o arranque) conclui a **Fase 0 + o Pilar 1 (Captação)**. Os demais pilares ainda estão em desenvolvimento nesta data.

Concluído até 30/09

**Fase 0 · Discovery / Foundation** — refinamento e trava das premissas.

Pilar 1 · Captação

* Enriquecimento cadastral automático via JUCESP
* Cadastro manual de conta e proteção de dados
* Simulador de crédito unificado
* Sessão de contas e visualização de detalhes
* Regras de visibilidade e hierarquia para cooperativas

Ainda em desenvolvimento em 30/09

* **Pilar 2 · Pré-qualificação** — em andamento (a mais pesada)
* **Pilar 3 · Proposta** — não iniciado
* **Pilar 4 · Estruturação** — não iniciado
* **Pilar 5 · Aprovação** — não iniciado
* **Pilar 6 · Formalização** — não iniciado

A meta de 30/09 entrega apenas a Captação — muito aquém da jornada completa. Ver o marco 30/11 (5 pilares) para o contraste.

Material de referência · Composição das squads

## Composição das squads — funções por frente

As duas squads correm em paralelo por fase (slide anterior). Abaixo, as **funções** que cada uma exige, derivadas do escopo dos pilares que entrega. **Funções, não quantitativo** — o número de pessoas é dimensionado com o Solution Lead e não é apresentado aqui.

Squad 1 · Transacional / wizard

Captação · Pré-qualificação · Proposta (Pilares 1, 2, 3)

* **Desenvolvedor Salesforce** (LWC + Apex) — formulários adaptativos, wizard, telas de proposta
* **Especialista em integração** — entrada síncrona no core, Serpro, status
* **Business Analyst** — jornada única, regras por linha de crédito
* **SME de risco** — QRSA (perguntas, rating, isenção)
* **QA** — regressão da esteira transacional

Squad 2 · Cadastro / contrato + backbone

Estruturação · Formalização · Aprovação + backbone de ocorrências (Pilares 4, 6, 5)

* **Desenvolvedor Salesforce** (LWC + Apex) — fichas PF/PJ, CCB, contratos
* **Arquiteto de integração** — backbone event-first, orquestração de ocorrências
* **Desenvolvedor de Platform Events** — publicação/consumo do barramento
* **Modelador de dados** — sócios/garantidores/participações
* **Business Analyst** — mapa ocorrências↔pendências↔fases
* **QA** — regressão de cadastro/contrato

Compartilhado entre as squads

**Solution Architect** (governança técnica e coerência entre frentes) · **coordenação/gestão de entrega** (interface entre squads, definida cedo) · a **lane de integração MuleSoft** (API-Led) é conduzida pelo parceiro/Evertec, fora das squads Salesforce.

Funções derivadas de estimates.json (skills\_needed por pilar) e da divisão de frentes do slide "Dois times em paralelo". Sem quantitativo de pessoas — a contagem é dimensionada e validada com o Solution Lead.

Material de referência · Justificativa dos prazos

## Por que a faixa é 12–22 semanas no melhor cenário

Melhor cenário = via **Aumentada** (IA) com **2 squads em paralelo**. O **piso (12 sem)** assume as premissas resolvidas e as frentes correndo juntas; o **teto (22 sem)** reflete os riscos ainda em aberto. A amplitude de **10 semanas** é o custo da incerteza — cada premissa fechada na Fase 0 encolhe a faixa.

O que fixa o piso (~12 sem)

* **2 squads concorrentes** — as frentes pesadas (transacional e cadastro/contrato) correm ao mesmo tempo, derrubando o mínimo
* **Aceleração por IA** (via Aumentada) — compressão de −10 a 25% do tempo de calendário sobre a âncora Tradicional
* **Captação reaproveitada** (já em QA) e **backbone de ocorrências** como plumbing comum
* Escopo integral fixo e crédito permanecendo no Sinqia (Salesforce só front-end)

O que empurra ao teto (~22 sem) — os fatores em detalhe

**① Prontidão das APIs e o tempo de DSP/Sinqia** — incerteza sobre se as integrações estão **totalmente prontas** (30 de 30 a confirmar, só JUCESP em QA; Swagger/documentação e write-back PUT/PATCH pendentes) *e* sobre o **tempo que DSP/Sinqia levará para desenvolvê-las/disponibilizá-las**. É uma dependência externa fora do nosso controle: se as APIs atrasam, o build espera ou corre sobre mocks e refaz — o maior risco de deslocamento do teto.

**② Aprovação das 3 frentes antes de iniciar cada item** — cada novo pilar/funcionalidade exige **alinhamento e aprovação das três frentes** (Salesforce, DSP e Sinqia/Evertec) antes de começar. Esse gate de entrada, somado à coordenação multi-fornecedor, pode **atrasar o início** de cada frente de trabalho e reduzir o ganho do paralelismo entre as squads.

**③ Requisitos ainda em nível macro** — o trabalho até aqui foi de **escopo macro**, sem refinamento detalhado por funcionalidade. Requisitos que só se detalham na refinação podem **revelar complexidade não prevista** (regras, exceções, telas) — quanto menor o detalhamento hoje, mais larga a faixa. Fechar o refinamento na Fase 0 é o que mais a estreita.

**⚠ Faixa benchmark, não compromisso** · tempo de calendário (refinamento até QA, sem homologação do cliente). Derivada top-down pela forma do engajamento e comprimida pela via Aumentada + paralelismo. Fechar as premissas da Fase 0 é o que mais estreita a faixa.

Material de referência · Justificativa dos prazos

## Justificativa da faixa por fase — o que ancora cada janela

| Fase | Janela (melhor · pior) | O que sustenta o prazo — e o que alarga |
| --- | --- | --- |
| **0 · Discovery / Foundation** | 07/09 · 14/09 | Curta e fixa: refinamento e trava das premissas. É o gate de viabilidade — fechar contratos de API, write-back Sinqia, cálculo QRSA e fornecedor/início **encolhe todas as fases seguintes**. |
| **1 · Captação + Backbone** | 28/09 · 19/10 | Piso apoiado no **reaproveitamento** da Captação (QA). Alarga se o backbone de ocorrências (event-first) exigir mais orquestração/BA ou se a estratégia de erro/DLQ crescer. |
| **2 · Pré-qual + Proposta + Aprovação** | 26/10 · 07/12 | **A fase mais pesada** (52% do peso): jornada adaptativa, QRSA completo, Serpro, entrada síncrona no core e a efetivação síncrona da aprovação. Maior amplitude — puxada por **QRSA (local de cálculo)** e pelos contratos de API. |
| **3 · Estruturação + Formalização** | 16/11 · 18/01 | Fichas PF/PJ profundas, upload assíncrono, CCB. Alarga com a **escrita (PUT/PATCH) ao Sinqia** não confirmada e o reuso da geração de CCB. |
| **4 · SIT / UAT / QA** | 30/11 · 22/02 | Estabilização full-journey nas 3 jornadas. O pior caso reflete o **cutover da dupla operação** Salesforce+Sinqia e a regressão sobre brownfield + trabalho novo. Homologação do cliente fica fora do envelope. |

Datas: via Aumentada, início 24/08/2026, refinamento até QA (slide "Plano de implementação"). Fases 2–4 se sobrepõem pelas 2 squads em paralelo. Faixas benchmark, não compromisso; tempo de calendário, sem homologação do cliente.

Material de referência · Incertezas e impacto

## Do piso ao teto — as incertezas que alargam a faixa (12 → 22 semanas)

Base · 12 sempiso (melhor cenário)

① +5 sem+42%

② +2+17%

③ +3 sem+25%

012 sem (base)22 sem (teto)

| Incerteza | Impacto s/ base | Por que alarga |
| --- | --- | --- |
| **① Prontidão das APIs + tempo DSP/Sinqia** | +42% ~+5 sem | Dependência externa fora do nosso controle: se as 30 APIs (só JUCESP em QA) não estiverem prontas, o build espera ou corre sobre mocks e refaz. **Incerteza adicional: a complexidade real de cada API** — sem Swagger/contrato, o esforço verdadeiro (transformação, write-back PUT/PATCH, erro/retry/DLQ) só se revela na integração e pode ser maior que o assumido. O maior fator. |
| **② Aprovação das 3 frentes antes de iniciar** | +17% ~+2 sem | Cada pilar/funcionalidade exige alinhamento das três frentes (Salesforce · DSP · Sinqia/Evertec) antes de começar — o gate de entrada atrasa o início e reduz o ganho do paralelismo. |
| **③ Requisitos ainda em nível macro** | +25% ~+3 sem | Escopo macro, sem refinamento por funcionalidade — a refinação pode revelar complexidade não prevista (regras, exceções, telas). |
| Total das incertezas | ~+83% | +10 semanas sobre a base → teto de 22 semanas. Fechar cada incerteza na Fase 0 encolhe a faixa. |

**Alocação indicativa** dos percentuais por incerteza — o total (+83% / +10 sem) é a amplitude derivada da faixa; a repartição entre as três é uma leitura para validação, não uma medição fina. Faixas benchmark, não compromisso; tempo de calendário.

← Anterior

Próximo →
