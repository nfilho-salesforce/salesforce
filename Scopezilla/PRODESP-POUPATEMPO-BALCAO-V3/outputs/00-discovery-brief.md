# Discovery Brief — PRODESP · Poupatempo Balcão (V3)

**Projeto:** PRODESP - Poupatempo Balcão V3 · **Data:** 2026-09-23 · **Conta:** Prodesp - Empresa de TI do Estado de São Paulo

---

## Resumo executivo

O Poupatempo — rede estadual de atendimento ao cidadão de São Paulo, com mais de 4.000 serviços no catálogo — quer reduzir a sobrecarga dos guichês físicos usando o Slack como estação de trabalho do atendente, com Service Cloud como motor de filas/casos por trás e MuleSoft integrando os sistemas legados. O MVP confirmado cobre duas jornadas BPMN (antecipar atendimento agendado por WhatsApp/gov.br, e apoiar o atendente de guichê via Slackbot e escalonamento a especialistas), mais dois itens de escopo que o usuário adicionou nesta sessão: autoprovisionamento de atendentes no Service Cloud/Omni-Channel e observabilidade via Tableau do canal WhatsApp e da ociosidade nas filas.

**Alerta de proveniência que governa este brief inteiro:** a maior parte do desenho detalhado (as duas jornadas BPMN, trinta premissas de arquitetura) foi produzida por Nelson Stebulaitis Filho em 23/09/2026, como *nossa* proposta de solução coerente — não como fato confirmado pelo cliente. Só dois materiais são do cliente: o deck "Prodesp — Atendimento Poupatempo" (Vinicius Ferraz) e a ata da reunião de 23/09/2026. Nenhuma das trinta premissas foi validada com a PRODESP. Tratar o desenho como ponto de partida sólido para a proposta, não como escopo fechado.

---

## Contexto da empresa e do setor

**PRODESP** — Companhia de Processamento de Dados do Estado de São Paulo — é a empresa de TI do governo estadual, responsável pelo programa **Poupatempo**, a rede de atendimento presencial e digital ao cidadão mais reconhecida do país. O catálogo atual soma mais de 4.000 serviços (emissão de documentos, CNH, licenciamento, etc.), com agendamento hoje distribuído entre app (60%), totem físico (38%) e WhatsApp (apenas 2%) — uma disparidade que a iniciativa busca corrigir.

Hoje, quando um atendente de guichê enfrenta dificuldade, não existe processo formal de escalonamento: ele precisa se levantar, procurar o supervisor pessoalmente e, se não resolver, pede ao cidadão que retorne outro dia. Há também desbalanceamento de carga entre unidades — algumas sobrecarregadas, outras com capacidade ociosa, sem mecanismo de balanceamento entre postos.

Este é um engajamento de setor público de alta visibilidade e pressão comercial — a equipe de vendas descreveu a oportunidade internamente como estratégica e disputada por outros fabricantes. Existe uma iniciativa-irmã na mesma conta (Poupatempo Balcão V2), cobrindo o mesmo material de discovery, mas modelada de forma independente nesta versão (V3) — sem compartilhar dados de escopo, apenas os documentos-fonte e a base de conhecimento.

---

## Panorama Salesforce: atual vs. alvo

**Estado atual — desconhecido.** Nenhuma fonte descreve o que já existe de Salesforce no Poupatempo hoje. O agente do T7 (IA interna da PRODESP para FAQ) já está em adoção, mas é ativo próprio da PRODESP, não Salesforce.

**Estado alvo — confirmado pelo usuário nesta sessão (Q1):**

| Produto | Papel proposto |
|---|---|
| **Slack** | Interface única de trabalho do atendente — todo o atendimento passa por aqui, mesmo quando o Service Cloud gerencia filas e agendas por trás |
| **Service Cloud** | Motor de backend: gestão de filas, casos, Omni-Channel |
| **Agentforce** | Resumo de histórico de atendimento e apoio à dúvida do atendente via Slackbot |
| **MuleSoft** | Camada de integração e espelhamento de eventos entre Service Cloud, Slack e sistemas legados |
| **Data 360** | Uso restrito — apenas em suporte ao Agentforce, não como plataforma de dados própria |
| **Tableau** | Novo escopo (Q2): observabilidade do canal WhatsApp e da ociosidade/disponibilidade de atendentes nas filas do Omni-Channel |

**Importante:** nenhum documento do cliente nomeia produto Salesforce por etapa do processo — o deck do cliente traz apenas uma caixa genérica "Plataforma Salesforce". A associação de produtos específicos a cada passo do fluxo é proposta nossa, construída na sessão de desenho de 23/09.

---

## Escopo e objetivos do projeto

### Objetivo

Reduzir a sobrecarga física dos postos Poupatempo antecipando atendimentos digitalmente e dando ao atendente de guichê um caminho formal de apoio remoto — sem interromper o atendimento presencial em curso. Nenhuma meta numérica, KPI ou percentual de redução foi declarado pelo cliente; o objetivo é qualitativo até que o cliente valide indicadores.

### Escopo confirmado do MVP

**Duas jornadas especificadas** (nível analítico, com fluxo BPMN e exceções mapeadas):

1. **Jornada 1 — Antecipar atendimento agendado.** Um robô detecta atendente ocioso, consulta a fila viva e, só com ela vazia, busca um agendamento futuro para antecipar. Oferece ao cidadão por WhatsApp, autentica via gov.br, roteia para a fila, e o atendente conduz pelo Slack. 53 elementos de fluxo mapeados.
2. **Jornada 2 — Apoiar o atendimento presencial via Slack.** O atendente de guichê consulta um Slackbot sem sair do lugar e, se necessário, escala para um canal de especialidade. 18 elementos de fluxo mapeados.

**Mais dois itens de escopo que o cliente/usuário adicionou nesta sessão (Q2), sem precedente em nenhuma das quatro fontes de discovery originais:**

3. **Autoprovisionamento de usuários** — integração com o sistema de dados de funcionários da PRODESP (ainda não identificado; premissa de API exposta) para criar, habilitar/inativar, atribuir perfil, permission set, licença, Service Resource, habilidade e capacidade de atendimento, e vincular o atendente à fila/papel correto — todo o setup base para habilitar um atendente no Service Cloud/Omni-Channel.
4. **Tableau — observabilidade** do canal WhatsApp e da ociosidade/disponibilidade de atendentes nas filas do Omni-Channel.

### Explicitamente fora de escopo

- O agendamento em si — feito por totem do Detran, entregue em fase anterior.
- O atendimento presencial que ocorre depois da antecipação (fora da Jornada 1).
- Atendentes fora do guichê (o escopo se restringe a atendentes de mesa).
- **Três das cinco jornadas do deck do cliente não foram especificadas** e não fazem parte deste MVP: pré-atendimento digital (atendentes ociosos disparando mensagens via WhatsApp), atendimento totalmente digital, e atendimento agêntico com validação humana obrigatória. Elas existem no material do cliente mas não foram analisadas nesta rodada — se entrarem em escopo depois, este brief não as cobre.
- Migração de dados históricos — a carga do sistema de CRM/ServiceDesk legado inicia do zero, sem migração.
- Transformação/estruturação complexa de dados (ETL) nesta fase (Q3) — apenas réplica direta via Platform Events, sem ferramenta como Informatica.

### Stubs — nomeados mas sem nada atrás (gap, não escopo)

- **"Plataforma Salesforce"** — nomeada no deck do cliente como caixa única, sem produto, processo ou usuário atrás.
- **Serviço de biometria** — nomeado na arquitetura do próprio cliente; não se sabe contra qual base consulta, se a integração existe ou precisa ser construída, nem o que o resultado decide (ver Perguntas Abertas, L-35).
- **Agente do T7** — tem papel definido (responder FAQ) e nenhum contrato de integração formal com o Slackbot.
- **Subprocessos colapsados** — o passo 14 da Jornada 1 e o passo 9 da Jornada 2 são caixas sem conteúdo serviço a serviço / especialidade a especialidade.

### Usuários e personas

Personas nomeadas no deck do cliente: **Ana** (cidadã), **Felipe** (atendente de mesa Poupatempo), **Anderson** (atendente em Santo Amaro). **Contagem de usuários é desconhecida** — nenhuma fonte informa quantos atendentes de mesa, atendentes de posto, especialistas ou postos existem hoje.

### Cronograma e restrições

**Não há prazo ou data de go-live para este engajamento.** Qualquer `client_target` eventualmente presente em metadados de outro projeto da mesma conta (DER-SP, rodovia) pertence a um engajamento completamente distinto e não deve ser reaproveitado aqui.

O modelo comercial discutido internamente é de **capacidade fixa de serviço**, com remuneração atrelada a entregas e escopo validados progressivamente — não time & materials nem escopo 100% fixo de uma vez. A entrega deve ser faseada em quick wins, não em um pacote único de meses, para que o cliente perceba valor progressivamente.

---

## Considerações de dados e conformidade

- **Sistema de CRM legado / Sistema de ServiceDesk legado** (plataforma real anonimizada por instrução do cliente — ver `decisions/0001-servicenow-anonymization.md`): fornece o protocolo de atendimento no início da interação e recebe transcrição, anexos e histórico no fim. Carga histórica inicia do zero, sem migração.
- **WhatsApp** carrega dado pessoal do cidadão (número, conteúdo de conversa). Mensagem ativa (outbound) tem custo por disparo e não garante resposta; existe janela de sessão que expira.
- **Autenticação gov.br** e **biometria** envolvem verificação de identidade — zona de LGPD ainda não explorada pelo cliente.
- **Opt-out do cidadão** (L-12): como é capturado, onde é armazenado e quem o respeita nos ciclos seguintes — apontado como provável exigência jurídica, ainda sem resposta.
- Nenhum requisito de conformidade, residência de dados ou certificação foi declarado pelo cliente nesta rodada — área de risco a levantar formalmente em discovery com o cliente, não apenas assumida.
- **Sem ETL / sem migração complexa nesta fase** — decisão confirmada (Q3): réplica direta de eventos, sem transformação.

---

## Achados de pesquisa e contexto de mercado

- Existe uma iniciativa-irmã na mesma conta (**Poupatempo Balcão V2**) que trabalhou os mesmos quatro materiais de discovery e, em sessão direta com o usuário, decidiu tratar **os dois recortes do material do cliente em conjunto e faseados dentro do mesmo SOW** — um recorte tático (Slack no balcão, quick wins) seguido de um recorte de plataforma completa (WhatsApp pré-atendimento, validação remota, atendimento agêntico 24/7, integração MuleSoft com gov.br/biometria/sistemas legados). O MVP confirmado neste projeto (V3) é mais estreito que essa decisão-irmã — cobre as duas jornadas do BPMN mais os dois itens novos (autoprovisionamento, Tableau) — e ainda não inclui as três jornadas de deck não especificadas. Vale checar com o usuário, ao avançar para `requirements`, se o MVP de V3 deve permanecer nesse recorte mais estreito ou se deve absorver o faseamento mais amplo já decidido em V2.
- Um material tático interno (deck "Poupatempo Balcão V2", Jackson Ulisses) descreve os mesmos quick wins nativos ao Slack — escalonamento em tempo real via huddle/canal, roteamento de ociosidade entre postos, base de conhecimento viva via Canvas, canais oficiais substituindo grupos de WhatsApp pessoais (risco de LGPD) — e cita casos de benchmark **externos**, não do Poupatempo: Nubank, Nutanix, suporte interno da própria Salesforce e Sammons Financial Group. Esses números são prova de conceito de mercado, não dados confirmados da PRODESP, e não devem ser confundidos com fato do cliente em nenhuma peça de proposta.
- A reunião de 22/09/2026 (Sync Poupatempo) registrou duas soluções técnicas paralelas em desenvolvimento para mitigar o risco de estabilidade do canal WhatsApp↔Slack — preocupação levantada diretamente por Nelson Stebulaitis Filho sobre risco de mensagens pararem de chegar.

---

## Perguntas abertas — a levar ao cliente

Estas são lacunas que **só a PRODESP pode responder**. Não devem ser respondidas por quem conduz o discovery interno — são pauta de validação com o cliente antes ou durante `requirements`.

### Bloqueiam desenho de arquitetura

1. **Validação de biometria (L-35)** — o que ela decide? Biometria validada remotamente dispensa o atendimento presencial, ou o presencial é mantido de todo modo? Não validada interrompe a antecipação? Contra qual base se valida — gov.br, IIRGD, Detran ou base própria da PRODESP? (A mais cara das pendências — reabre o gateway central da Jornada 1.)
2. **Autenticação gov.br (L-33)** — antes de detalhar: o Poupatempo de fato autentica no gov.br para atendimento remoto? Se sim, qual nível de confiança (bronze/prata/ouro) cada serviço exige, qual o prazo para o cidadão se autenticar, e o que fazer com quem não tem conta gov.br?
3. **T7 vs. Slackbot (L-13/J2)** — são o mesmo componente, um substitui o outro, ou coexistem? Se coexistem, quem é consultado primeiro e as bases de conhecimento são a mesma?
4. **Elegibilidade de serviços (L-03/J1)** — quais dos 4.000+ serviços do catálogo permitem transbordo para atendimento virtual? Define o tamanho real do benefício da Jornada 1.
5. **Critério de especialidade (L-02/J1, L-01/J2)** — as especialidades (para roteamento de filas e canais) são organizadas por departamento ou por tipo de problema?
6. **Conteúdo dos subprocessos colapsados (L-32/J1, L-14/J2)** — o que existe dentro do subprocesso 14 (Jornada 1) e do subprocesso 9 (Jornada 2), serviço a serviço / especialidade a especialidade?
7. **Roteiro de caso vindo da fila espontânea (L-31/J1)** — percorre o mesmo caminho da antecipação, incluindo cancelamento do agendamento presencial? Vale para toda demanda espontânea ou só para quem também tem agendamento?
8. **Órgão parceiro no gateway (L-27/J1)** — confirmar que um caso dependente de IIRGD/Detran é a saída "não" do gateway 17, e não um ramo próprio.

### Bloqueiam configuração (prazos), não arquitetura

9. Prazo de tolerância para resposta do cidadão e para disponibilidade de atendente (L-01/J1).
10. Prazo para o cidadão responder ao atendente após aceitar — reinicia a cada pedido de complemento desde a versão 2.0 do desenho (L-28/J1).
11. Tempo de inatividade que dispara encerramento automático (L-29/J1).
12. Prazo para um especialista assumir antes do encaminhamento automático (L-02/J2).
13. Limite de duração do apoio especializado — hoje sem temporizador, com o cidadão sentado no guichê aguardando (L-15/J2).

### Técnicas e de conformidade

14. Contrato da integração Slackbot ↔ agente do T7 — interface, dono da base de conhecimento, critério de FAQ, comportamento quando o T7 está indisponível (L-34).
15. Opt-out do cidadão — como é capturado, onde armazenado, quem o respeita nos ciclos seguintes; provável exigência jurídica (L-12).
16. Quem provisiona/desprovisiona o canal de Slack do atendente, e o que ocorre com casos abertos no desligamento (L-13/J1).
17. Como funciona a integração nativa do Slack com o objeto de caso e o acesso ao histórico (L-06/J1).
18. O que ocorre se a consulta à fila viva falhar ou expirar — caminho de erro ainda sem destino (L-30/J1).
19. Quem executa as tarefas de serviço nos passos 18, 25 e 53 — hoje numa raia humana mas descritas como chamada de sistema; decisão de arquitetura levantada e não fechada (L-36/J1).
20. Revisão humana em fluxos automatizados fica ou sai do MVP (L-05/J1).

---

## Deliverables

- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V3/outputs/00-discovery-brief.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V3/outputs/`
