# Proposta de Jornada Unificada — Portal de Crédito Desenvolve SP

**Papel:** Arquiteto de Solução
**Base:** Comparativos Digital vs. Julgamental (pedido + ficha cadastral PJ + PF), notas das sessões de discovery 1–3, reuniões de entendimento técnico de 10 e 11/08/2026.

## Problema central

As jornadas atuais Digital e Julgamental foram construídas de forma independente, resultando em:

| **Problema** | **Onde ocorre hoje** |
| --- | --- |
| Dados da empresa coletados 2× | Na solicitação (Pedido) e novamente na Ficha Cadastral PJ |
| Sócios coletados 2× no Julgamental | No formulário do pedido e na Ficha Cadastral PJ |
| Endereço coletado 3× | Login/JUCESP → Pedido → Cadastro PJ |
| Garantias, docs complementares e CCB fora do portal | Julgamental: tudo por e-mail, sem rastreabilidade |
| Duas estruturas de formulário incompatíveis | Digital = wizard; Julgamental = formulário único |
| Termos e QRSA com UX diferente por jornada | Digital = passo dedicado; Julgamental = modais |
| Jornada Agro sem fluxo digital estruturado | Produtor rural PF sem vínculo JUCESP → enquadramento manual no Salesforce |
| Cooperativas sem visibilidade dos próprios indicados | Acesso similar ao de funcionários internos — regras de visibilidade inadequadas para o papel |
| Roteamento Digital/Julgamental opaco | O cliente não sabe por que recebeu um tratamento diferente do esperado |
| Consultor acessado por WhatsApp pessoal | Canal não rastreável, sem registro no portal |
| Simulação sem validade visível | Prazo de 2 dias não comunicado — cliente retorna e perde contexto |

## Princípios da proposta

1. **Coletar dado uma vez, reutilizar em todo o fluxo** — pré-preenchimento via JUCESP e dados já existentes no Salesforce. Dados informados na Solicitação não sobrescrevem o cadastro vigente antes da aprovação do backoffice.
2. **Jornada única adaptativa** — mesma estrutura para Digital, Julgamental e Agro; o sistema oculta ou exibe etapas com base na linha de crédito e no perfil do tomador.
3. **Portal-first** — eliminar o uso de e-mail para documentação de garantias, complementar e CCB; tudo dentro do portal como pendências rastreáveis.
4. **Progresso salvo e retomável** — o cliente pode interromper e retomar sem perder dados; simulação tem validade de 2 dias comunicada de forma clara.
5. **Visibilidade de status em tempo real** — o cliente sempre sabe em que etapa está, o que falta e qual o prazo de cada pendência.
6. **Roteamento transparente pelo produto** — a linha de crédito escolhida define internamente o fluxo (Digital/Julgamental/Agro); o cliente não precisa conhecer essa distinção.
7. **Separação de papéis: cliente, cooperativa e consultor** — regras de visibilidade e acesso distintas para cada papel, sem expor dados de terceiros indevidamente.

# Proposta de Jornada Unificada — Portal de Crédito Desenvolve SP

**Papel:** Arquiteto de Solução
**Base:** Comparativos Digital vs. Julgamental (pedido + ficha cadastral PJ + PF), notas das sessões de discovery 1–3, reuniões de entendimento técnico de 10 e 11/08/2026.

## Problema central

As jornadas atuais Digital e Julgamental foram construídas de forma independente, resultando em:

| **Problema** | **Onde ocorre hoje** |
| --- | --- |
| Dados da empresa coletados 2× | Na solicitação (Pedido) e novamente na Ficha Cadastral PJ |
| Sócios coletados 2× no Julgamental | No formulário do pedido e na Ficha Cadastral PJ |
| Endereço coletado 3× | Login/JUCESP → Pedido → Cadastro PJ |
| Garantias, docs complementares e CCB fora do portal | Julgamental: tudo por e-mail, sem rastreabilidade |
| Duas estruturas de formulário incompatíveis | Digital = wizard; Julgamental = formulário único |
| Termos e QRSA com UX diferente por jornada | Digital = passo dedicado; Julgamental = modais |
| Jornada Agro sem fluxo digital estruturado | Produtor rural PF sem vínculo JUCESP → enquadramento manual no backoffice (Officer) |
| Cooperativas sem visibilidade dos próprios indicados | Acesso similar ao de funcionários internos — regras de visibilidade inadequadas para o papel |
| Roteamento Digital/Julgamental opaco | O cliente não sabe por que recebeu um tratamento diferente do esperado |
| Consultor acessado por WhatsApp pessoal | Canal não rastreável, sem registro no portal |
| Simulação sem validade visível | Prazo de 2 dias não comunicado — cliente retorna e perde contexto |

## Princípios da proposta

1. **Coletar dado uma vez, reutilizar em todo o fluxo** — pré-preenchimento via JUCESP e dados já existentes no Salesforce. Dados informados na Solicitação não sobrescrevem o cadastro vigente antes da aprovação do backoffice.
2. **Jornada única adaptativa** — mesma estrutura para Digital, Julgamental e Agro; o sistema oculta ou exibe etapas com base na linha de crédito e no perfil do tomador.
3. **Portal-first** — eliminar o uso de e-mail para documentação de garantias, complementar e CCB; tudo dentro do portal como pendências rastreáveis.
4. **Progresso salvo e retomável** — o cliente pode interromper e retomar sem perder dados; simulação tem validade de 2 dias comunicada de forma clara.
5. **Visibilidade de status em tempo real** — o cliente sempre sabe em que etapa está, o que falta e qual o prazo de cada pendência.
6. **Roteamento transparente pelo produto** — a linha de crédito escolhida define internamente o fluxo (Digital/Julgamental/Agro); o cliente não precisa conhecer essa distinção.
7. **Separação de papéis: cliente, cooperativa e consultor** — regras de visibilidade e acesso distintas para cada papel, sem expor dados de terceiros indevidamente.

## Visão macro da jornada unificada

O cliente percorre sempre as mesmas fases. O sistema adapta internamente o que exibe em cada fase com base na linha de crédito escolhida — sem que o cliente precise conhecer a distinção Digital / Julgamental / Agro.

┌─────────────────────────────────────────────────────────────────────┐

│ 1. ENTRADA [todas as jornadas] │

│ │

│ Login (CPF) │

│ ├── PJ / PF com CNPJ → Seleção de empresa via JUCESP │

│ └── Produtor rural PF (Agro) → Criação manual de conta │

│ │

│ Dashboard: solicitações ativas + próxima ação esperada │

└──────────────────────────────────┬──────────────────────────────────┘

↓

┌─────────────────────────────────────────────────────────────────────┐

│ 2. SOLICITAÇÃO [todas as jornadas] │

│ │

│ Passo 1 · Termos de autorização (texto fixo, aceite gravado) │

│ Passo 2 · Dados da empresa + Contato (pré-preenchido do JUCESP) │

│ Passo 3 · Linha de crédito ◄── ROTEADOR INTERNO │

│ ├── Capital de giro → trilha Digital │

│ ├── Máquinas / Equipamentos → trilha Julgamental │

│ └── Irriga Mais / Agro Máq. → trilha Agro │

│ Passo 4 · Declaração de exclusão + QRSA (condicional) │

│ Passo 5 · Autorizador SERPRO (eCAC) │

│ Passo 6 · Validação facial Biovalídia (apenas Digital) │

└──────────────────────────────────┬──────────────────────────────────┘

↓

┌─────────────────────────────────────────────────────────────────────┐

│ 3. CADASTRO [todas as jornadas] │

│ │

│ Dados da Solicitação pré-preenchidos; cliente só completa o delta │

│ │

│ Cadastro PJ ·· endereço · constituição · faturamento │

│ sócios · conta bancária · EPR · anexos │

│ └── por sócio → Cadastro PF ·· identificação · cônjuge │

│ endereço · renda · PEP · anexos │

│ │

│ Agro PF: Cadastro PF é o cadastro principal (sem PJ) │

└──────────────────────────────────┬──────────────────────────────────┘

↓

┌──────────────────┬──────────────────────┬───────────────────────────┐

│ 4a. ANÁLISE │ 4b. ANÁLISE │ 4c. ANÁLISE │

│ Digital │ Julgamental │ Agro │

│ │ │ │

│ Motor │ SUCI monta │ Enquadramento │

│ automático │ proposta │ manual │

│ (instantâneo) │ (alguns dias) │ (prazo a calibrar) │

└──────────────────┴──────────────────────┴───────────────────────────┘

↓

┌─────────────────────────────────────────────────────────────────────┐

│ 5. PROPOSTA [todas as jornadas] │

│ │

│ Detalhes financeiros → Aceite ou Recusa → PDF │

│ Julgamental / Agro: prazo de aceite com contador visível │

└──────────────────────────────────┬──────────────────────────────────┘

↓

┌────────────────────┴──────────────────────┐

│ Digital │ Julgamental + Agro

↓ ↓

┌──────────────────────┐ ┌──────────────────────────────────┐

│ Contratação │ │ 6. FORMALIZAÇÃO │

│ simplificada │ │ │

│ (sem garantias) │ │ Pendências no portal: │

└──────────┬───────────┘ │ garantias · docs complementares │

│ │ geração de CCB · assinatura │

└─────────────┬───────────┘

↓

┌─────────────────────────────────────────────────────────────────────┐

│ 7. ACOMPANHAMENTO [todas as jornadas] │

│ │

│ Status em tempo real (Officer) · Pendências abertas · Despachos │

│ Notificação quando cliente precisa agir · Prazo visível por etapa │

└─────────────────────────────────────────────────────────────────────┘



## Detalhamento por fase

### Fase 1 — Entrada

* Login único via CPF; o sistema exibe os CNPJs vinculados ao usuário via JUCESP.
* Seleção de empresa na tela de vínculos — protótipo Helena (sprint atual). Tela de seleção manual de CNPJ descartada.
* Tela de termos pré-login descartada do escopo atual.
* **Agro PF:** produtor rural pessoa física não consta na JUCESP → criação manual de conta centralizada no Salesforce (rastreabilidade auditável). Exibir vínculos JUCESP validados antes de permitir adição manual para evitar CNPJs aleatórios.
* Dashboard inicial: solicitações ativas com status e próxima ação esperada. Tela "Minhas Solicitações" substituída pela nova camada unificada.
* Visualização de etapas (path) reservada para a tela de detalhe — não exibida na lista principal.

### Fase 2 — Solicitação

Wizard de **5 passos fixos**, com condicionais por linha e perfil:

| **Passo** | **Nome** | **Condicional** |
| --- | --- | --- |
| 1 | Termos de autorização | Sempre; texto fixo no front-end, sem API dinâmica. Aceites gravados para auditoria (tabela SC2018) |
| 2 | Dados da empresa + Contato | Sempre; pré-preenchido do JUCESP/Salesforce. Elegibilidade validada pelo simulador — bloqueia produtos fora do porte do cliente |
| 3 | Empréstimo pretendido | Sempre; a linha escolhida é o roteador: aciona/desativa etapas e define Digital/Julgamental/Agro internamente |
| 4 | Declaração de exclusão + QRSA | Declaração: "tudo ou nada", sem lógica complexa. QRSA: desativado para linhas isentas. Exibição dos resultados socioambientais ao cliente: pendente validação com área de riscos |
| 5 | Autorizador SERPRO (eCAC) | Sempre |
| 5+ | Validação facial (Biovalídia) | Apenas linhas Digital; via CNH ou validação manual por backoffice; integração Serasa antifraude futura |

**Roteamento por produto (confirmado em reunião 11/08):**

* Capital de giro → Digital (motor automático)
* Máquinas, equipamentos, projetos → Julgamental (análise SUCI)
* Irriga Mais → Agro com cooperativa obrigatória
* Agro Máquinas → Agro aberto a produtores rurais PF e PJ

**Dados reaproveitados:**

* Razão Social, CNPJ, endereço → JUCESP.
* CNAE, faturamento, elegibilidade de porte → simulador/Salesforce.
* Contato → perfil do usuário logado.
* Dados inseridos aqui **não sobrescrevem** o cadastro existente antes da aprovação do backoffice.

**Agro — mensagem de orientação:** se a linha selecionada for "Irriga Mais" e o cliente não possuir cooperativa, exibir mensagem informativa antes da submissão para evitar pedidos impróprios direcionados a enquadramento manual.

### Fase 3 — Cadastro

**Princípio: coletar uma vez.** Dados da Solicitação pré-preenchidos; cliente só completa o que falta.

#### 3a. Cadastro PJ

Formulário em **seções expansíveis** com indicador de progresso por seção:

| **Seção** | **Origem dos dados** |
| --- | --- |
| Identificação (endereço) | JUCESP + Solicitação |
| Constituição (NIRE, forma, capital, controle, beneficiário final) | Pré-preenchido parcialmente |
| Atividades (CNAE, faturamento) | Solicitação |
| Sócios / Administradores | Solicitação; completa ou adiciona aqui |
| Participação em outras empresas | Novo dado |
| Conta bancária | Novo dado |
| EPR (Partes Relacionadas) | Pré-preenchido se já declarado |
| Anexos (validação por tipo) | Documentos padronizados (hardcoded); Cartão CNPJ, Contrato Social, Termo EPR. Armazenamento: Salesforce (até 12MB async) ou S3 para volumes maiores — decisão pendente com suporte técnico |

Campo "grupo econômico" removido do escopo da v1 (decisão reunião 11/08).

Botão "Preencher cadastro" no card do sócio (modelo Julgamental) → padrão unificado para iniciar Cadastro PF sem sair da PJ.

#### 3b. Cadastro PF (por sócio / produtor rural)

Wizard de **6 passos**:

| **Passo** | **Seção** | **Nota** |
| --- | --- | --- |
| 1 | Identificação pessoal | CPF, doc, nascimento, filiação, estado civil, grau instrução, raça, emancipado |
| 2 | Cônjuge / Companheiro(a) | Condicional: estado civil = casado/união estável |
| 3 | Endereço residencial + Contato | Telefone, celular, email |
| 4 | Dados profissionais | Renda líquida mensal |
| 5 | Empresas em que participa | País, CNPJ, Razão social, Participação% |
| 6 | Declaração PEP + Anexos | PEP próprio + parente (com grau de parentesco); upload de documentos |

**Campos regulatórios a incluir na unificação:** Regime de casamento, Número de dependentes, Valor do imóvel, Grau de parentesco no PEP — exibição condicional onde possível.

**Agro PF:** quando o tomador é produtor rural pessoa física, o Cadastro PF é o cadastro principal (não há PJ). O sistema deve tratar CPF como identificador primário nesse perfil, sem exigir CNPJ JUCESP.

### Fase 4 — Análise

Tela unificada "Em análise" com 3 estados (decisão reunião 10/08):

| **Estado** | **Descrição** | **Fonte de dados** |
| --- | --- | --- |
| Simulação | Pedido criado; aguarda envio formal | Salesforce |
| Em análise | Proposta em avaliação | Salesforce (visualização reduzida) |
| Proposta final | Pronta para aceite | API Sinqia/Officer |

* Prazo estimado visível por tipo: Digital (instantâneo), Julgamental (alguns dias), Agro (manual — prazo a ser calibrado).
* Consultor designado exibido no portal (nome + canal) — eliminando WhatsApp pessoal como canal oficial.
* Simulação com validade de **2 dias**: prazo exibido com contador regressivo.

### Fase 5 — Proposta

* Detalhes financeiros: valor, prazo, carência, taxas; parcelas tratadas como line items.
* Aceite ou recusa com confirmação.
* Geração de PDF.
* **Julgamental:** certificado de aprovação com prazo de 15 dias para aceite, com contador visível no portal.
* **Agro:** mesma experiência; prazo de aceite a ser definido pela área de crédito.

### Fase 6 — Formalização *(portal-first: substituição do fluxo por e-mail)*

Garantias e CCB tratados como **pendências** no portal — modelo de troca de arquivos, sem validação complexa de conteúdo pelo front-end na v1:

| **Etapa** | **Hoje** | **Proposta** |
| --- | --- | --- |
| Documentação de garantias | E-mail | Pendência no portal: upload de arquivos com checklist por tipo |
| Documentação complementar | E-mail | Pendência no portal com tipos definidos |
| Geração de CCB | E-mail / automático no sistema | Geração acionada via API (ocorrência no Officer) → disponível para download no portal |
| Assinatura de CCB | E-mail (Glob) | API de assinatura CCB (BPP/DCP); rastreada como pendência até conclusão |
| Validação pelo consultor | Manual | Ocorrência no Officer sinaliza conclusão; status atualizado no portal |

**Modelo de integração (reunião 11/08):** Salesforce gerencia as pendências do cliente (upload, comunicação, aprovação); ocorrências customizadas no Officer sinalizam início e fim de cada etapa para o sistema de crédito. Salesforce não modifica a estrutura de configuração do Officer — apenas cria ocorrências específicas.

**Regra:** dados enviados pelo cliente atualizam o Salesforce em staging — só aplicados ao cadastro definitivo após aprovação do backoffice.

### Fase 7 — Acompanhamento

Já unificado em ambas as jornadas atuais — sem alteração estrutural necessária:

* Status do pedido em tempo real (fonte: Sinqia/Officer).
* Detalhe do pedido: histórico de eventos, anexos, despachos, exigências, procuradores.
* Notificação: hoje ativa apenas em cancelamento; sem notificação intermediária durante análise.
* Controle de SLA/prazo: **não implementado** em nenhuma jornada hoje.

**Proposta de melhoria:** notificação ativa quando o cliente precisa agir (exigência aberta, proposta disponível, pendência de garantia) e contador de prazo para etapas com SLA (aceite da proposta, validade da simulação).

## Jornada Agro — especificidades

### Perfis do tomador Agro

| **Perfil** | **Identificador** | **Validação JUCESP** | **Fluxo** |
| --- | --- | --- | --- |
| Produtor rural PJ | CNPJ | Sim (se registrado) | Padrão PJ; pode ter bugs em homologação — monitorar |
| Produtor rural PF | CPF | Não | Conta criada manualmente no Salesforce |
| Cooperativa (indicadora) | CNPJ | Não | Acesso diferenciado — ver abaixo |

### Produtos Agro

| **Produto** | **Quem pode solicitar** | **Análise** |
| --- | --- | --- |
| Irriga Mais | Produtor + cooperativa obrigatória | Manual (SUCI) |
| Agro Máquinas | Todos os produtores rurais | Manual (SUCI) |

### Motor de crédito Agro

* Opera fora do sistema principal (web), baixo volume — não é gargalo crítico no momento.
* Limitação atual: não consulta CADIN nem dados bancários para CPF.
* Necessidade futura: integrar motor de crédito já contratado; resolver consultas para pessoa física.

### Cooperativas — papel e acesso

Cooperativas **não são tomadoras de crédito** — são indicadoras de produtores rurais. Operam hoje com acesso similar ao de funcionários da Desenvolve, o que não é adequado.

**Proposta de acesso para cooperativas:**

| **Capacidade** | **Hoje** | **Proposta** |
| --- | --- | --- |
| Ver propostas dos próprios indicados | Sim (via acesso interno) | Sim, restrito aos indicados pela cooperativa |
| Ver propostas de outras cooperativas | Potencialmente sim | Não |
| Criar solicitações para produtores | Sim | Sim, com vínculo explícito ao cooperado |
| Volume histórico | ˜200 pedidos desde 2025 | — |

**Questão em aberto (reunião 11/08):** portal unificado com regras de visibilidade por papel vs. portal separado para cooperativas. Decisão pendente — a questão central é a hierarquia de contas (cooperativa → cooperados) no Salesforce.

### Fluxo Agro simplificado

Login (CPF ou CNPJ da cooperativa)

│

├── Produtor PJ → Vincular JUCESP → Jornada padrão com linha Agro

│

├── Produtor PF → Criação manual de conta → Jornada PF com linha Agro

│ ↓

│ Mensagem de orientação: Irriga Mais exige cooperativa

│

└── Cooperativa → Dashboard de indicados → Selecionar produtor → Iniciar solicitação

↓

Linha Agro → Análise manual (enquadramento SUCI)

↓

Proposta → Aceite → Formalização (mesma Fase 6)



## Mapa de reaproveitamento de dados

| **Dado** | **Coletado em** | **Reutilizado em** |
| --- | --- | --- |
| CNPJ, Razão Social, Endereço | JUCESP (login) | Solicitação, Cadastro PJ |
| CNAE, Faturamento, Porte | Simulador/Salesforce | Solicitação (elegibilidade) |
| Contato (CPF, nome, tel, email) | Solicitação passo 2 | Cadastro PF do sócio |
| Sócios (CPF, nome, participação) | Solicitação passo 2 | Cadastro PJ + Cadastro PF |
| Empréstimo (linha, valor, prazo) | Solicitação passo 3 | Análise + Proposta |
| EPR (enquadramento) | Cadastro PJ | Formalização |
| Aceites de termos | Solicitação passo 1 | Auditoria (SC2018) |

## Delta mínimo por tipo de jornada

| **Dimensão** | **Digital** | **Julgamental** | **Agro** |
| --- | --- | --- | --- |
| Perfil do tomador | PJ (qualquer porte) | PJ (máquinas, equipamentos, projetos) | PF (produtor rural) ou PJ agro |
| Validação de identidade | Biovalídia (CNH) | Não exige | Não exige (v1) |
| QRSA | Isento | Obrigatório | Isento |
| Motor de análise | Automático | SUCI manual | Manual (motor web externo, baixo volume) |
| Validação JUCESP | Sim | Sim | PJ: sim / PF: não (manual) |
| Formalização | Simplificada | Garantias + docs + CCB | Igual ao Julgamental |
| Cooperativa como intermediária | Não | Não | Sim (Irriga Mais obrigatório) |

## Pontos de decisão antes de implementar

1. **Roteamento por produto:** confirmar com Sinqia/Officer se a regra Digital/Julgamental/Agro está disponível via API ou precisa ser replicada no Salesforce.
2. **Portal cooperativas:** portal unificado com roles vs. portal separado — decisão de arquitetura com impacto na hierarquia de contas do Salesforce.
3. **Agro PF — fluxo de conta manual:** definir SLA para criação manual e critério de revalidação para produtores que já possuem histórico na Cínquia.
4. **QRSA — exibição de resultados ao cliente:** validar com área de riscos (Renata) se Sensibilidade/Rating/Classificação podem ser exibidos ao tomador.
5. **CCB e assinatura:** APIs a incluir: geração de CCB, assinatura CCB (BPP/DCP). Confirmar configuração necessária para a DCP.
6. **Armazenamento de anexos:** Salesforce (6MB síncrono / 12MB assíncrono) vs. S3 — definir estratégia com suporte técnico.
7. **Biovalídia:** incluída na lista de APIs; confirmar escopo de integração (v1 = usar processo existente; integração Serasa antifraude = futura).
8. **Beneficiário final na PJ:** ausente no Digital — incluir na jornada unificada por exigência regulatória.
9. **Campos PF regulatórios:** Regime de casamento, número de dependentes, valor do imóvel — alinhar com área de crédito se obrigatórios para todas as linhas ou só Julgamental.
10. **Validade da simulação (2 dias):** comunicar claramente na interface; definir comportamento quando expirada com pedido em andamento.

| **Jornada** | **1. Captação** | **2. Pré-qualificação** | **3. Proposta** | **4. Estruturação** | **5. Aprovação** | **6. Formalização** |
| --- | --- | --- | --- | --- | --- | --- |
| **Digital** | • Simulação  • Preenchimento do pedido | • Acompanhamento do pedido  • Validação facial (Biovalid) | • Aceite da proposta digital | • Cadastro PF e PJ (Pós-aceite)  • Questionário QRSA (Desacoplado) | • Aprovação automatizada | • Assinatura de Fichas e CCB (via ferramenta externa) |
| **Julgamental** | • Simulação  • Preenchimento do pedido | • Acompanhamento do pedido  • Triagem obrigatória | • Montagem da proposta (Manual) | • Cadastro PF e PJ (Pré-comitê)  • Questionário QRSA (Sarasque)  • Documentação complementar | • Parecer do Comitê (Matéria)  • Aceite do Certificado (Prazo de 15 dias) | • Documentação de garantias  • Assinatura de Fichas e CCB (via ferramenta externa) |

**Esta lista consolida as principais regras de negócio, limitações técnicas e fluxos operacionais que devem ser minuciosamente detalhados durante a etapa de refinamento técnico de cada pilar de crédito da Desenvolve SP.**

##### 1. Pilar: Captação

* Regra de Herança e Não Redundância de Dados:
  + No momento da criação do Pedido de Crédito (Solicitação), os parâmetros originalmente simulados (Linha de fomento, Valor do giro, Periodicidade, Amortização, Prazo total e Carência) devem ser herdados e pré-preenchidos automaticamente na tela [76].
  + A captação inicial da Jornada Julgamental deve ser mantida de forma simplificada e enxuta, coletando apenas dados mínimos de identificação e crédito, sem exigir uploads de anexos imediatos [76].
* Integração JUCESP Automática no Login:
  + A identificação do cliente e o acesso ao portal devem seguir estritamente o protótipo unificado: o usuário loga utilizando o seu CPF e visualiza de forma dinâmica as empresas (CNPJs) vinculadas mapeadas pela API JUCESP, selecionando o contexto de trabalho desejado [76].
  + Uma vez selecionada a empresa, os dados geográficos e de faturamento retornados pela JUCESP devem ser exibidos de forma pré-preenchida e bloqueada para edição manual para evitar erros de consistência [76].
* Controle de Retenção de Contexto da Simulação:
  + As simulações operadas no portal devem possuir uma validade rígida de 2 dias corridos [76]. O tempo de expiração deve ser comunicado visualmente e de forma explícita na tela para orientar o cliente sobre a necessidade de reiniciar o fluxo se o prazo for ultrapassado [76].
* Momento de Criação de Registros no Core Bancário:
  + A etapa de simulação e a criação preliminar de leads no Salesforce não devem gravar nenhum registro no core bancário (Sinqia) [76]. A chamada integrada para a criação síncrona do cliente PJ e da Prospecção/Proposta só será disparada quando o proponente clicar em "Solicitar" no formulário, reduzindo o volume de registros abandonados no legado [76].
* Fluxo de Cadastro Manual Fallback (Criação de Conta):
  + Para usuários/empresas que não possuem vínculo ativo ou retornado pela consulta da JUCESP (como produtores rurais PF), o portal habilitará o fluxo de cadastro manual, o qual será processado e centralizado diretamente no Salesforce para fins de controle de auditoria, rastreabilidade e segurança dos dados [52, 61].
  + Proteção Contra Sobrescrita: Os dados preenchidos durante esse fluxo manual no portal não devem de forma alguma sobrescrever informações já existentes e homologadas em contas do Salesforce antes da validação e aprovação do backoffice, evitando a corrupção de registros [61-62].

##### 2. Pilar: Pré-qualificação

* Regras Excludentes de Exclusão Socioambientais ("Tudo ou Nada"):
  + A declaração de restrições socioambientais no preenchimento do pedido funciona sob uma lógica de filtro eliminatório imediato [77]. Se o tomador declarar desconformidade com qualquer um dos itens das listas de restrição (CNPJs vetados), o fluxo é cancelado preventivamente de forma direta no portal, dispensando a aplicação de lógicas complexas de cálculo de score nesta fase [77].
* Isenção Parametrizada do QRSA (Sarasque):
  + O preenchimento do questionário socioambiental completo (QRSA) deve contar com uma regra de isenção automatizada com base no enquadramento do produto ou perfil: as operações dos segmentos de setor público, crédito agro e capital de giro digital estão isentas de preencher o questionário [77].
* Motor de Cálculo e Faixas de Rating do QRSA: Não estará no Salesforce
  + Para os clientes elegíveis ao Sarasque, o rating socioambiental final deve ser gerado por uma fórmula de cálculo matemática fixa processada por procedure no back-end: quantidade de respostas positivas / total de questões aplicáveis (desconsiderando opções assinaladas como "não se aplica") [77].
  + O resultado deve classificar o cliente de forma estrita em três níveis de rating: Bom (nota $\ge$ 0.7), Regular (nota de 0.4 a 0.69) ou Ruim (nota < 0.4) [77].
* Apuração da Sensibilidade DSP por CNAE, Empreendimento e Município:
  + O portal deve validar automaticamente se a empresa possui alta ou baixa exposição a riscos ambientais [77]. Para que uma proposta seja classificada como de "Baixa Sensibilidade", a combinação dos três quesitos (CNAE de atividade, tipo de empreendimento e município de atuação) deve ser simultaneamente identificada como baixa [77]. A presença de qualquer fator em lista de restrição classifica a operação como de Alta Sensibilidade [77].
* Matriz Combinada de Decisão (Tratamento de Risco):
  + A combinação dos dois indicadores dita se a proposta segue na esteira ou é descartada automaticamente [77]:
    - Cancelamento Automático: Proposta com Rating Ruim (< 0.4) ou com Rating Regular (0.4 a 0.69) em operações de Alta Sensibilidade [77].
    - Prosseguimento na Esteira: Proposta com Rating Regular ou Bom em Baixa Sensibilidade, ou com Rating Bom em Alta Sensibilidade [77].
* Autenticação Facial com CNH (Biovalid):
  + A validação biométrica utiliza a API do Biovalid (Serpro) e deve ser realizada exclusivamente por um sócio da empresa proponente que possua Carteira Nacional de Habilitação (CNH) cadastrada na base de dados nacional [77].
  + Fluxo de Contingência: Na impossibilidade de validar por biometria automatizada (como quando o sócio não possui CNH ou o aplicativo falha), o sistema deve desviar automaticamente para um fluxo de validação manual por videochamada conduzida por um analista interno [77].
* Triagem Obrigatória para Esteiras Julgamentais:
  + Independentemente do enquadramento, todos os pedidos submetidos na Jornada Julgamental passam pela etapa de triagem humana obrigatória [77]. Essa regra garante que a área de negócio analise e valide fisicamente o relato da empresa e a finalidade do empréstimo antes de disponibilizar o formulário de cadastro estruturado [77].
* Hierarquia e Compartilhamento de Dados para Cooperativas (Agro):
  + As cooperativas parceiras gerenciam propostas de múltiplos cooperados e requerem regras de visibilidade estritas [62-63]. Deve ser configurada uma hierarquia de contas dedicada no Salesforce para que cada cooperativa acesse e opere exclusivamente as informações e propostas de seus próprios cooperados, sem expor dados de terceiros [50, 62-63].
* Mitigação Visual de Enquadramento no Agro:
  + Devido à ausência de dados do produtor rural (CPF) no banco da JUCESP, o enquadramento inicial requer atenção [84]. O portal deve implementar avisos, mensagens e instruções visuais explícitas em tela para orientar o cliente antes de submeter a proposta à análise manual do backoffice, evitando submissões inadequadas [51, 84].

##### 3. Pilar: Proposta

* Abordagem Híbrida e Estados da Tela de Detalhes:
  + A tela de acompanhamento e detalhe da proposta deve ser configurada em três estados dinâmicos de visualização para o usuário final [78]:
    - Estado 1 - Simulação: Visualização básica de simulação salva [78].
    - Estado 2 - Em Análise: Visualização reduzida de informações utilizando dados extraídos diretamente do Salesforce para garantir melhor performance da tela [78].
    - Estado 3 - Proposta Final: Carregamento dinâmico via API consultando os dados em tempo real no core bancário (Sinqia) [78].
* Apresentação Estruturada de Encargos:
  + A tela de visualização de Proposta Final deve carregar os dados financeiros com itens de linha (line items) para as parcelas, exibindo claramente o valor aprovado, o CET, IOF, TCC aplicados e a periodicidade [78]. O cliente terá os botões interativos para Aceitar ou Recusar o crédito e exportar o PDF [78].
* Aceite Síncrono Automatizado (Digital):
  + Diferente da esteira julgamental, o aceite do cliente na proposta da Jornada Digital grava e formaliza instantaneamente a criação da proposta diretamente no core bancário (Sinqia) de forma síncrona [78].
* Validade Limite de Aceite de Proposta (Julgamental):
  + Para propostas que passam pela análise técnica e aprovação pelo comitê, o Certificado de Aprovação emitido pelo core bancário possui um prazo improrrogável de 15 dias de validade para que o cliente realize o aceite dentro do portal [78].

##### 4. Pilar: Estruturação

* Regra de Bloqueio Rígido de Edição de Cadastro:
  + Assim que o cliente preencher as fichas cadastrais (PJ/PF) e clicar no botão de salvar, o sistema Salesforce deve mudar imediatamente o status para "Em Análise" e bloquear toda e qualquer edição dos campos por parte do cliente [79]. Isso garante que a equipe interna revise os dados sem sofrer alterações concorrentes.
* Ferramenta de Desbloqueio e Reabertura de Cadastro (Backoffice):
  + Caso a equipe interna de análise cadastral detecte inconsistências ou exija correções de dados, o backoffice do Salesforce deve dispor de um botão de ação rápida para reabrir e liberar o cadastro novamente para edição direta do cliente, enviando notificações automáticas detalhando os campos pendentes [79].
* Proteção de Sobrescrita de Dados:
  + Os dados novos digitados ou alterados pelo tomador durante o preenchimento de uma nova solicitação não devem sobrescrever dados pré-existentes e homologados do cliente no Salesforce antes de passarem pela aprovação final do backoffice [79]. Caso o CPF de um sócio ou garantidor já conste na base, o formulário de cadastro do portal deve carregar os dados cadastrais prévios de forma blindada [79].
* Geração Estática de Ficha Cadastral em PDF:
  + O portal deve disponibilizar a funcionalidade de geração automática e impressão da ficha cadastral consolidada em formato PDF [79]. Para garantir agilidade na entrega do MVP, o formato da ficha será implementado de forma estática (hardcoded) diretamente no Salesforce [79].
* Limitações Técnicas e Arquitetura de Anexos:
  + O refinamento técnico deve considerar as limitações nativas de tráfego de arquivos do Salesforce (6MB para transações síncronas e 12MB para assíncronas) [79]. Os anexos devem ser tratados como par de chave-valor (utilizando APIs distintas de Get para categorias e Post para binários) [79] e a equipe de arquitetura deve validar a viabilidade de hospedar e sincronizar esses binários diretamente em um repositório Amazon S3 [79].
* Saneamento de Pendências via Salesforce:
  + Caso haja documentação complementar pendente ou vencida (como licença ambiental suspensa), a equipe de backoffice do Salesforce registrará uma ocorrência que criará uma pendência ativa visível na página inicial do portal, bloqueando o avanço do fluxo até que o anexo corretivo seja submetido pelo portal [79].
* Documentação de Posse e Terra (Agro):
  + O preenchimento da ficha cadastral de produtores rurais na fase de estruturação exige a coleta e upload obrigatório de comprovantes de posse ou arrendamento de terra [12, 59].

##### 5. Pilar: Aprovação

* Orquestração de Workflow via Ocorrências:
  + As transições de status da proposta no core bancário (Sinqia) e no Salesforce serão orquestradas e sincronizadas utilizando o disparo e consumo de códigos de ocorrências customizadas no Salesforce [80]. Essa abordagem mapeia os estados físicos das "casinhas" do workflow interno do Sinqia e protege as regras de negócio consolidadas no legado [80].
* Postergação Operacional de Dados Financeiros de Longo Prazo:
  + Ficou formalmente decidido adiar para fases futures a exibição de dados pós-liberação de crédito no portal (como controle de parcelas a vencer, status de pagamento, quitação parcial via fundos garantidores ou variação diária de taxas pós-fixadas) [80]. O portal se concentrará na esteira de originação e formalização fim a fim [80].

##### 6. Pilar: Formalização

* Modelagem de CCB e Termos Estáticos:
  + Para fins de redução de complexidade no portal, o contrato da Cédula de Crédito Bancário (CCB) e o termo do QRSA gerados pelo backoffice serão disponibilizados ao portal como arquivos em PDF fixos para download, descartando a necessidade de listagens dinâmicas ou montagem de contratos na interface via API [81].
* Fluxo de Assinatura Externa Obrigatória:
  + Como o portal não contará com ferramenta nativa de assinatura digital e biometria de contrato nesta fase [81], a formalização será tratada como uma pendência de upload de arquivos no portal [81]: o cliente faz o download da CCB, assina fisicamente com reconhecimento de firma ou por meio de plataformas externas parceiras (como o Glob) e realiza o upload do binário assinado de volta no portal [81].
* Codificação Técnica Socioambiental por Cores:
  + A documentação e garantias acessórias exigidas para a formalização socioambiental devem respeitar uma codificação técnica visual de cores para facilitar o monitoramento do analista no Salesforce [81]:
    - Azul Escuro: Documentação obrigatória para todas as operações [81].
    - Azul Claro: Documentação específica correlacionada ao tipo de atividade desempenhada pelo tomador [81].
    - Amarelo: Documentos específicos exigidos para crédito rural / agro [81].
* Garantias Específicas do Agro (Safras/Maquinários):
  + A estruturação e envio de garantias específicas para o crédito rural (como penhor de safra ou alienação de maquinários) serão tratadas de forma simplificada como pendências de envio de arquivos no portal, sem necessidade de processamento complexo de conteúdo pelo frontend [52, 59].
