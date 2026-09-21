# PRODESP · DER-SP — Pacote de Escopo para SOW

**Client-Ready Check:** pendente — revisão humana de legal/comercial obrigatória antes de qualquer envio ao cliente.
**Gerado em:** 2026-09-21 · **Fonte:** dados de escopo do projeto (`data/strategy.json`, `data/epics.json`, `data/gaps.json`, `data/roadmap.json`, `data/resource-plan.json`, `data/estimates.json`)

> *Scope package generated from scoping data — paste into the SOW template (Ironclad), which owns parties, commercial terms, standard terms, and signature. For internal and legal/commercial review only; not an offer.*

---

## Background & Objectives

O atendimento emergencial na malha rodoviária do DER-SP hoje não tem protocolo único: o registro do pedido, o despacho de recursos de campo e o encerramento do atendimento ocorrem em sistemas e etapas distintas, sem um identificador rastreável do início ao fim. Este programa estabelece um protocolo único e rastreável do primeiro contato ao encerramento, com despacho automatizado apoiado pelo Field Service e canais de entrada adicionais ao 0800 — voz via integração de telefonia e WhatsApp — sem substituir o 0800 como porta de entrada.

Objetivos do programa:

- Eliminar a fragmentação de registro do atendimento emergencial, atribuindo a cada chamado um identificador único rastreável do pedido ao encerramento.
- Oferecer um canal digital de entrada (WhatsApp) complementar à voz, com triagem automatizada e transbordo para atendimento humano nos casos que envolvam risco à vítima.
- Automatizar o despacho de recursos de campo por aderência, disponibilidade e proximidade nas 14 Coordenadorias de Circunscrição Regional (CGRs) do DER-SP, com intervenção humana limitada a exceções auditáveis.
- Preparar a decisão de arquitetura de voz de longo prazo (unificação de canais de telefonia) sem que essa decisão condicione a entrada em operação do MVP.

Princípios que orientam o desenho da solução:

- O 0800 permanece o canal oficial de entrada; nenhum canal novo o substitui.
- Os processos usam os objetos nativos do Field Service (Work Order, Service Appointment, Service Territory) antes de qualquer extensão do modelo de dados.
- A triagem automatizada por IA nunca conclui, por si só, o atendimento a uma vítima — o transbordo humano é obrigatório nesses casos.

## Scope of Services

O programa entrega cinco componentes de solução (épicos), sequenciados conforme a seção Project Approach & Phases:

1. **Canal Digital de Atendimento ao Cidadão.** Abertura de chamado de socorro via WhatsApp (texto e áudio) e via telefonia por integração de CTI com a Unidade de Resposta Audível (URA) em uso, com triagem automatizada por Agentforce e criação automática de ordem de serviço e protocolo. Transbordo para uma fila humana única, com contexto completo do canal de origem, em três condições: falha de identificação automatizada, preferência do cidadão, ou suspeita de vítima.
2. **Registro e Classificação da Ocorrência.** Criação do chamado a partir de qualquer canal de entrada (WhatsApp, telefonia via CTI, ou 0800 registrado manualmente), classificação por um catálogo de subtipos de ocorrência, qualificação do chamado e da ordem de campo pelo Agentforce ou pelo atendente, alerta de possível duplicidade ao operador do Centro de Controle e Comunicação (C2C), e sincronização de dados com os sistemas legados SIGOR e SIGEO.
3. **Despacho Automatizado de Recursos de Campo.** Motor de agendamento e otimização do Field Service operando nas 14 CGRs, com escalonamento de espera baseado em parâmetro de tempo configurável, reprocessamento automático após recusa de despacho, console do dispatcher com visão de mapa e agenda, e trilha de auditoria do ciclo de despacho.
4. **Execução em Campo.** Aplicativo único de Field Service Mobile para os operadores de campo do recorte do MVP, com recebimento de despacho por notificação nativa, modo offline com fila de sincronização, encerramento de atendimento por formulário quando aplicável ao tipo de ocorrência, e as travas de negócio de recusa com motivo, foto obrigatória e confirmação de localização.
5. **Rastreamento e Visibilidade em Tempo Real.** Acompanhamento do atendimento pelo cidadão via o recurso nativo de acompanhamento de agendamento do Field Service, e painel agregado de indicadores operacionais para gestores.

## Out of Scope

Os seguintes itens ficam fora do escopo deste programa:

- **Substituição da URA/0800 por telefonia nativa (Salesforce Voice).** A integração de CTI com a URA em uso está em escopo (item 1); a substituição da própria URA por telefonia nativa Salesforce é um projeto de infraestrutura de telefonia separado, com viabilidade ainda em definição entre DER-SP e PRODESP.
- **Fusão automática de chamados duplicados.** O escopo cobre alerta manual de possível duplicidade ao operador do C2C (item 2); a fusão automática de registros duplicados não está incluída.
- **Bloqueio automático de avanço no aplicativo de campo quando sem conexão.** O escopo cobre a captura de evidências (foto, confirmação de localização, motivo de recusa) em modo offline com sincronização ao reconectar (item 4); o bloqueio automático de avanço sem rede não está incluído.
- **Portal dedicado para as empresas terceirizadas de operação de campo.** O escopo cobre visibilidade para cidadão, C2C, gestores, operador de campo, dispatcher e Agentforce (itens 1 a 5); uma superfície de visibilidade dedicada para as empresas terceirizadas não está incluída.
- **Roteamento de precisão em nível de rua para o mapa do dispatcher.** O escopo cobre o recurso de roteamento aéreo nativo do Field Service no console do dispatcher (item 3); um recurso de roteamento de precisão em nível de rua não está incluído.
- **Relatório segmentado por CGR e meta formal de nível de serviço no painel de gestores.** O escopo cobre um painel único com indicadores agregados (item 5); relatórios segmentados por CGR e uma meta formal de nível de serviço não estão incluídos.

## Assumptions & Dependencies

Este escopo parte das seguintes premissas e dependências:

- **Padrão técnico de integração de telefonia.** O padrão de integração de CTI entre o Salesforce e a URA em uso (atualmente fornecida pela Instinct) depende de confirmação técnica com o fornecedor de telefonia antes do início do desenvolvimento do canal de atendimento (item 1).
- **Especificação de integração com sistemas legados.** As especificações de integração com os sistemas SIGOR e SIGEO (item 2) dependem de confirmação da PRODESP antes do desenvolvimento dessas integrações.
- **Parâmetro de escalonamento de despacho.** O valor do parâmetro de tempo que aciona o escalonamento de despacho (item 3) é uma premissa inicial de referência, sujeita a validação e ajuste com o DER-SP antes da entrada em operação.
- **Trilha de auditoria do ciclo de despacho.** O desenho detalhado da trilha de auditoria (campos capturados e período de retenção) do ciclo de despacho (item 3) depende de definição conjunta com o DER-SP.
- **Consentimento e responsabilidade sobre dados da ocorrência.** O tratamento de dados pessoais e de geolocalização coletados no canal digital (item 1) e no registro da ocorrência (item 2) segue premissas de consentimento e de responsabilidade sobre os dados que permanecem sujeitas a validação formal de privacidade de dados pelo DER-SP e pela PRODESP.
- **Ferramental de desenvolvimento e implantação.** O desenvolvimento assume o uso do Salesforce CLI e de práticas de desenvolvimento orientado a repositório de código-fonte, sujeito a confirmação da PRODESP sobre ferramental de integração e implantação contínua já em uso.
- **Licenciamento do canal de atendimento.** A quantidade de licenças necessárias para o canal de atendimento (item 1) está sujeita a revalidação em função da adição do canal de telefonia.

## Project Approach & Phases

O programa está sequenciado em cinco fases, definidas pela dependência entre os componentes de solução:

1. **Resolução de Discovery.** Fase de resolução das questões abertas que condicionam o desenho dos componentes seguintes, sem componente de solução associado.
2. **Fundação — Registro da Ocorrência e Integrações.** Entrega o componente de Registro e Classificação da Ocorrência (item 2), incluindo as integrações com SIGOR e SIGEO. Depende da resolução da Fase 1.
3. **Despacho Automatizado e Canal Digital.** Entrega os componentes de Despacho Automatizado de Recursos de Campo (item 3) e Canal Digital de Atendimento ao Cidadão (item 1), em paralelo. Depende da Fase 2 — o modelo de ordem de serviço e de recursos de campo precisa existir antes do motor de despacho e da criação automatizada de chamados.
4. **Execução em Campo.** Entrega o componente de Execução em Campo (item 4). Depende da Fase 3 — o aplicativo de campo recebe as atribuições geradas pelo motor de despacho.
5. **Rastreamento, Visibilidade e Estabilização.** Entrega o componente de Rastreamento e Visibilidade em Tempo Real (item 5). Depende das Fases 3 e 4 — o rastreamento consome o ciclo de vida da ordem de serviço e do agendamento gerado pelo despacho e pela execução em campo.

## Roles & Responsibilities

**Disciplinas fornecidas pela Salesforce Professional Services:**

- Gerenciamento de Projeto/Programa
- Arquitetura de Solução
- Arquitetura Técnica
- Consultoria Funcional
- Desenvolvimento
- Garantia de Qualidade
- Gestão de Mudança e Adoção

**Disciplinas fornecidas pelo cliente (DER-SP/PRODESP):**

- Product Owner / tomador de decisão do lado do cliente
- Consultoria Funcional (especialistas de negócio do DER-SP)
- Arquitetura Técnica (contraparte técnica da PRODESP/Stefanini)
- Garantia de Qualidade (validação de aceite do lado do cliente)
- Gestão de Mudança e Adoção (contraparte do lado do cliente)
