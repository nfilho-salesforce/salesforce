# Solução — PRODESP · Poupatempo Balcão V2

*Gerado em 21/09/2026 · Scopezilla `design` · Escopo completo `decisions/0002` (Fase 1 tática + Fase 2 plataforma Headless, faseadas em uma única SOW)*

Este documento é a espinha dorsal da solução: as decisões arquiteturais horizontais primeiro, depois os 10 épicos aprovados percorridos na ordem da jornada de valor (do pré-atendimento da cidadã até a analítica), com a arquitetura de suporte tecida dentro de cada épico — não anexada como um capítulo técnico separado.

**Nota de fundamentação (para o time interno, não para o cliente):** o KB central da Salesforce (`doc_search` MCP) não está conectado nesta sessão de design. As decisões marcadas `[KB: ...]` abaixo vêm da camada 1 (`knowledge/` deste projeto) — fundamentadas, mas não confirmadas contra o KB central de camada 2. Recomendo rodar `/kb-sync` ou conectar via DevBar antes de qualquer entrega final ao cliente que cite essas decisões como padrão validado pela Salesforce como um todo, além deste corpus.

---

## Fundações de Arquitetura

Decisões horizontais que não pertencem a um único épico — valem para todo o programa, Fase 1 e Fase 2.

### Estratégia de Org

Uma única org Salesforce existente já hospeda a capacidade contratada na conta — Slack Enterprise Plus (1.800 licenças validadas para a Sala de Situação), Agentforce/Flex Credits (~125,8 milhões de créditos a cada 90 dias), WhatsApp/e-mail/push Message Credits, MuleSoft e Data 360. O programa reutiliza essa org e essa capacidade em vez de provisionar um ambiente novo. `[assumption: confirmar a topologia exata da org — qual orgId hospeda cada produto — com o time de conta/Org62 antes do design detalhado; nenhuma fonte de discovery cita o orgId explicitamente]`

### Modelo de Compartilhamento e Segurança

Três camadas de sensibilidade de dados, cada uma com um controle diferente:
- **Coordenação entre atendentes (huddle, canais de serviço)** — texto institucional auditável, migrando da coordenação hoje feita em WhatsApp pessoal (fora da LGPD, sem histórico) para canais Slack da Prodesp. Este é o ganho central de compliance da Fase 1.
- **Dados de biometria** — nunca devem transitar em texto nos canais Slack; apenas o relato textual do problema (ex.: "digital não capturou") é permitido no canal. `[assumption: confirmar com o time de conta o documento de posicionamento LGPD/Trust sobre onde ocorre a inferência do Agentforce — existência confirmada pelo usuário, documento ainda não localizado]`
- **Imagens de documento (E07, Fase 2)** — dado sensível, mas de natureza diferente da biometria; tratamento de residência/retenção ainda a validar (ver G0712).

### Governança de Agentes

Todo agente Agentforce do programa (o agente de Slack do atendente na Fase 1, o agente de WhatsApp 24/7 na Fase 2) é definido pelos 5 atributos — Role, Data, Actions, Channel, Guardrails. `[KB: staar-agentforce-governance-guardrails.md:14-29]` Os dois guardrails nominais mais relevantes para este programa: nunca informar incorretamente status de emissão de documento/CIN, e nunca revelar dados pessoais a um remetente não autenticado. O porte do programa (1-2 agentes nomeados, um departamento) está mais próximo do tier "Governance Foundations" do framework LATAM de governança agêntica. `[KB: latam-agentic-governance-services.md:39-43]` A análise de LGPD do Discovery Brief já estabelece que, por o desenho ser assistivo (humano no loop, nunca decisão 100% automática), o programa tende a ficar fora do gatilho estrito do Art. 20 da LGPD — mas isso reforça, não elimina, a necessidade de revisão humana genuína no ponto de escalonamento e capacidade de explicar a lógica de roteamento se questionado. `[extends: análise LGPD Art. 20 do Discovery Brief, aplicada ao design de governança de agentes]`

### DevOps e Configuração

Abordagem declarativa-primeiro (Flow/configuração antes de Apex) para toda automação do programa — especialmente o workflow de contingência (E04), que é um caso clássico de broadcast automatizável via Flow sem código customizado. `[KB: salesforce-architect-fundamentals.md:30-38]` Nenhum épico do programa, pela leitura atual do discovery, exige desenvolvimento customizado pesado (Apex) — a maior incerteza técnica está na integração (E09), não na camada de configuração Salesforce.

### Owner de Governança (gap aberto, não resolvido aqui)

O owner de governança de agentes de IA do lado Prodesp ainda não foi identificado — item já registrado no Discovery Brief como mais crítico agora que a Fase 2 (atendimento agêntico 24/7) é escopo confirmado, não visão. Este documento assume que esse papel será nomeado antes do início da Fase 2; não resolve a lacuna.

---

## Solução por Processo de Negócio

Ordem: jornada da cidadã e do atendente, do pré-atendimento até a analítica — não por ID de épico. Fases (1 tática / 2 plataforma completa) indicadas em cada título, per `decisions/0002` (ambas comprometidas na mesma SOW).

### Pré-Atendimento Digital via WhatsApp (Fase 2)

**Contexto de negócio**: Hoje a cidadã chega ao balcão sem triagem prévia; muitos casos que chegam ao guichê físico poderiam ter sido resolvidos ou preparados antes da visita. A Jornada 02 do deck de plataforma propõe um convite de pré-atendimento pelo WhatsApp antes do dia marcado.

**Abordagem de solução**: Um agente Agentforce conversa com a cidadã pelo WhatsApp Business API — já contratado e quase ocioso na conta (4,9 bilhões de créditos WhatsApp válidos até maio/2027) — para triagem e preparação antes da visita presencial.

**Arquitetura de suporte**: O mesmo padrão "Agent Persona" documentado para Data 360 sobre Slack se aplica ao WhatsApp — ambos são superfícies conversacionais sobre o mesmo núcleo Data 360 headless. `[extends: padrão Agent Persona documentado para Slack em staar-data-360-headless.md:16-22, estendido para WhatsApp]` A dependência real de gating não é o canal WhatsApp (já disponível) — é ter um evento de gatilho confiável ("cidadã tem visita agendada") vindo de um sistema de agendamento. `[assumption: G0613 — identificar qual sistema agenda hoje as visitas ao Poupatempo e se ele pode emitir esse evento]`

### Atendimento Agêntico 24/7 — Human-in-the-Loop (Fase 2)

**Contexto de negócio**: Fora do horário de atendimento presencial, a cidadã não tem canal digital assistido por IA — hoje o WhatsApp/Portal ("Poupinha") já resolve o caso simples, mas sem um agente que escale para humano quando o caso exige.

**Abordagem de solução**: Um agente Agentforce atende pelo WhatsApp 24 horas por dia, com supervisão humana — escalando para atendente humano quando o caso sai do escopo do agente (Jornada 04 do deck de plataforma).

**Arquitetura de suporte**: Segue ponto a ponto a doutrina "humanos direcionam, agentes executam, a plataforma governa". `[KB: staar-headless-360-doctrine.md:17-19]` Desenho no padrão do exemplo "Order Status Agent" do framework de referência: Role (responder dúvidas comuns de atendimento Poupatempo), Data (Data 360 — cadastro/histórico da cidadã + base de conhecimento do serviço), Actions (confirmar identidade → responder/triar → escalar), Channel (WhatsApp), Guardrails (nunca afirmar status de emissão de documento sem confirmação humana; nunca revelar dados pessoais a remetente não autenticado). `[KB: staar-agentforce-governance-guardrails.md:22-29]` A revisão humana no ponto de escalonamento precisa ser genuína, não pro forma — consistente com a análise de LGPD Art. 20 do Discovery Brief. `[extends: análise LGPD Art. 20]`

### Posto de Trabalho do Atendente no Slack (Fase 1)

**Contexto de negócio**: O atendente do guichê hoje trabalha com conhecimento disperso entre atendentes, sem uma referência única e auditável de regra/processo vigente. Quando o caso foge do script, a coordenação com especialistas acontece hoje em grupos pessoais de WhatsApp — fora da governança institucional e da LGPD.

**Abordagem de solução**: O atendente passa a trabalhar dentro do Slack: canais dedicados por serviço, Canvas fixado com a regra/conhecimento vigente, e Agentforce disponível em contexto para dúvidas do próprio fluxo de atendimento.

**Arquitetura de suporte**: Agentforce embutido no canal de serviço segue o pilar de roadmap que a própria Salesforce já declara — "Slack-first, MCP-powered conversations." `[KB: staar-data-360-headless.md:24-26]` Recomendo que o conteúdo do Canvas seja lastreado em artigos de Salesforce Knowledge, não autoria nativa solta no Canvas — mantém versionamento e trilha de auditoria, consistente com a tese de migrar coordenação informal para canal governado. `[extends: princípio de canal auditável já estabelecido no Discovery Brief para a coordenação por huddle, estendido aqui para a autoria de conteúdo]` `[assumption: G0116 — mecanismo exato de sincronização Canvas↔Knowledge a validar]` **Risco carregado, não resolvido aqui**: as 1.800 licenças Slack já validadas cobrem a Sala de Situação (monitoramento de canais digitais), não o headcount real de atendentes nos 244 postos + 900 totens — dimensionamento de licenças pendente com o cliente.

### Escalonamento em Tempo Real — Transbordo via Huddle (Fase 1)

**Contexto de negócio**: Quando o caso foge do script (digital que não captura, documento divergente, dúvida fora do Canvas), o atendente hoje não tem um canal institucional para pedir ajuda a um especialista sem deixar a cadeira.

**Abordagem de solução**: O atendente aciona um huddle Slack com um especialista diretamente do canal de serviço, sem sair do fluxo de atendimento.

**Arquitetura de suporte**: Recomendo Slack User Groups estáticos por especialidade para a Fase 1 — build simples, alinhado ao ritmo tático do piloto. Roteamento decidido por Agentforce (o agente identifica a especialidade certa e sugere/inicia o huddle) fica como caminho de evolução para Fase 2+, apoiado no mesmo padrão de decisão de agente usado em E08. `[assumption: G0214 — User Group estático é suficiente na escala do piloto; validar cobertura real de especialistas por tema/turno]`

### Validação Remota de Documentos por Atendente Ocioso (Fase 2)

**Contexto de negócio**: Um atendente ocioso em outro posto poderia acelerar o atendimento presencial em curso em outro balcão validando documentos à distância — hoje essa capacidade ociosa entre postos não é aproveitada (extensão das Jornadas 01/03 do deck de plataforma).

**Abordagem de solução**: O atendente ocioso valida documentos à distância via Slack, usando o mesmo posto de trabalho de E01 como superfície.

**Arquitetura de suporte**: Reutiliza o mesmo sinal de capacidade ociosa por posto que E03 precisa (ver E03, abaixo) — é o terceiro consumidor dessa mesma fundação de dados junto com E10. O transporte da imagem do documento via Slack carrega um risco de LGPD mais alto do que a coordenação em texto do huddle (E02), porque a imagem em si é dado sensível, distinto do caso já resolvido de "sem biometria bruta em texto". `[assumption: G0712 — validar tratamento de residência/retenção de dados especificamente para imagens de documento em thread do Slack]`

### Roteamento de Capacidade Ociosa Entre Postos (Fase 1)

**Contexto de negócio**: Visibilidade e roteamento de casos entre os 244 postos físicos + 900 totens, direcionando demanda para onde há capacidade ociosa — sem precisar contratar mais atendentes.

**Abordagem de solução**: Um sinal de ocupação/fila em tempo real por posto alimenta o roteamento de casos entre postos.

**Arquitetura de suporte**: Nenhum sistema de registro de ocupação em tempo real por posto foi identificado no discovery — esta é a fundação de dados mais carregada do programa. **Achado do cruzamento com E10 (reflexo de consumo posterior)**: o modelo preditivo de espera de E10 precisa exatamente do mesmo sinal — não é um dado exclusivo de E03, é uma fundação compartilhada por dois épicos, e deve ser desenhada uma única vez. `[assumption: G0315 — provável objeto Data 360 alimentado por check-in/check-out do atendente ou estado de sessão dos totens; validar com a Prodesp se já existe qualquer sinal de fila/ocupação hoje, mesmo fora do Salesforce, antes de desenhar do zero]`

### Workflow de Contingência — Sistema Fora do Ar (Fase 1)

**Contexto de negócio**: Quando um sistema crítico cai (ex.: sistema do Detran), hoje o atendimento continua sem visibilidade do problema até que o boca a boca informal alcance todos os postos.

**Abordagem de solução**: Workflow Builder dispara aviso automático aos atendentes/postos quando um sistema crítico cai.

**Arquitetura de suporte**: Flow declarativo de broadcast — sem necessidade de código customizado. `[KB: salesforce-architect-fundamentals.md:30-38]` O gatilho manual (atendente/operação aciona o Flow) é o caminho de menor complexidade para o MVP da Fase 1; um gatilho automático depende de o stack de monitoramento da Prodesp expor um webhook/API para o Salesforce consumir — carrega a ambiguidade já registrada em G0401 sobre se o disparo é automático ou manual. `[assumption: G0413 — default gatilho manual na Fase 1; automático é evolução Fase 2+ condicionada à integração de monitoramento]`

### Governança, Adoção e Change Management (Fase 1)

**Contexto de negócio**: Confirmado explicitamente em escopo pelo usuário na sessão de discovery — papéis e responsabilidades, treinamento dos atendentes, política de canais e critérios de adoção do Slack como posto de trabalho.

**Abordagem de solução**: Aplica diretamente o checklist de 5 atributos e o framework de governança agêntica LATAM já descritos nas Fundações de Arquitetura — sem decisão técnica nova específica deste épico.

**Arquitetura de suporte**: Não aplicável — este épico é horizontal por natureza (papéis, treinamento, política), não uma capacidade técnica própria. Ver Fundações de Arquitetura, seção Governança de Agentes.

### Plataforma de Integração MuleSoft — Gov.br, Biometria, Legado, Sistema Semântico, T7 (Fase 2)

**Contexto de negócio**: A plataforma Headless completa depende de uma camada de integração ligando o Salesforce a gov.br, biometria estadual, sistemas legados da Prodesp, "Sistema Semântico" e "T7" — confirmada visualmente no diagrama de arquitetura do deck de plataforma, mas com identidades exatas de vários desses sistemas ainda em aberto.

**Abordagem de solução**: MuleSoft como camada de integração horizontal — já contratado na conta, hoje quase não usado por este recorte específico.

**Arquitetura de suporte**: MuleSoft é citado explicitamente na doutrina Headless 360 como uma das infraestruturas horizontais que um agente atravessa junto com Slack, Data 360 e outros sistemas — não é uma peça isolada de integração, é parte da mesma camada de governança de agente. `[KB: staar-headless-360-doctrine.md:21-23]` As identidades de Sistema Semântico, "Atendimento", T7 e Biometria continuam abertas (G0901-G0910, não resolvidas neste documento) — mas o *formato* da camada de integração (API-led connectivity: camadas de API de Sistema, Processo e Experiência) pode ser desenhado independentemente dessas identidades específicas. `[assumption: G0911 — padrão API-led connectivity da MuleSoft se aplica; protocolos e mecanismos de autenticação por sistema específico ficam pendentes até as identidades serem confirmadas]` **Confiança permanece "Unknown" — este é o épico de maior risco técnico do programa.**

### Analytics e Previsibilidade de Atendimento (Fase 2)

**Contexto de negócio**: Cruzamento de dados em tempo real, algoritmo preditivo de tempo de espera, e retroalimentação analítica dos agentes de IA para melhoria contínua do atendimento. Os KPIs de exemplo (15/16/17 minutos) citados no deck de plataforma são ilustrativos e não validados pelo cliente — não uma métrica existente a ser exposta.

**Abordagem de solução**: Data 360 como camada de dados cruzados em tempo real, alimentando um modelo preditivo de tempo de espera.

**Arquitetura de suporte**: Segue o mesmo padrão "Agent Persona" sobre Data 360 documentado para E01/E06. `[KB: staar-data-360-headless.md:16-22]` **Reflexo "já têm isso?"**: os KPIs ilustrativos confirmam que este é um build novo, não uma exposição de métrica já existente — o cliente ainda não validou nenhum baseline real. **Reflexo de consumo posterior**: este épico compartilha a mesma fundação de sinal de capacidade por posto que E03 precisa (ver E03, acima) — resolver uma vez, consumir duas vezes. `[assumption: G1012 — direção de integração do modelo preditivo ainda não confirmada: nativo Salesforce/Data Cloud (Einstein) vs. alimentar uma ferramenta de BI já existente da Prodesp; depende também da resolução de G0315]`

---

## Deliverables

- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/01-solution.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/`
