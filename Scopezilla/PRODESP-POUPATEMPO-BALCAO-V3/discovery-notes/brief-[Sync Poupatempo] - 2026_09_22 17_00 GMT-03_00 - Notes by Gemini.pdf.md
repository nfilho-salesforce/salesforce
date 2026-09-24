# Scoping Brief: Sync Poupatempo — Arquitetura Omnichannel (Slack + Service Cloud + Agentforce + MuleSoft)

**Source**: `[Sync Poupatempo] - 2026_09_22 17_00 GMT-03_00 - Notes by Gemini.pdf`
**Date**: 22 de setembro de 2026
**Participantes**: Rafael Marques, Osvaldo Melo, Juliana Brites, Larisse Gois, Vinicius Ferraz, Pedro Ganem Filho, Juliane Lopes, Nelson Stebulaitis Filho, Viviani Hupp, Renata Vendramini
**Duração**: ~1h18min (sessão encerrada em 01:18:26)
**Original length**: 63 páginas (resumo estruturado do Gemini + transcrição completa com marcação de tempo); ~14–16k palavras na fonte

---

## Business Context
- Reunião estratégica interna (Salesforce/PRODESP-side) para revisar a arquitetura omnichannel do programa Poupatempo antes de consolidar a proposta comercial.
- Pedro Ganem Filho e Juliana Brites enquadraram a oportunidade como crítica: **"a aplicação mais importante da América Latina", disputada por fabricantes globais** — pressão comercial para September (mês da própria reunião).
- Motivação central: reduzir sobrecarga física dos postos presenciais, digitalizar parte do atendimento e aproveitar tempo ocioso de atendentes, usando Slack como camada de trabalho e Service Cloud como motor.
- Estratégia de entrega enfatizada por Larisse Gois e Juliane Lopes: **quick wins** faseados em vez de uma entrega única de 6 meses (o cronograma originalmente vendido), para que o cliente sinta valor progressivamente.

## Current State
- Poupatempo tem **mais de 4.000 serviços** no catálogo atual (fonte: Larisse Gois, 00:10:53 / 00:54:09).
- Disparidade de canais de agendamento hoje: **60% via app, 38% via totem físico, apenas 2% via WhatsApp** (Pedro Ganem Filho, 00:22:30–00:23:34).
- Hoje, quando um atendente presencial tem dificuldade, não existe processo formal de escalonamento: ele precisa se levantar, buscar o supervisor pessoalmente e, se não resolver, interrompe o atendimento e pede para o cidadão retornar outro dia (Larisse Gois, 00:05:54).
- Existe desbalanceamento de carga entre unidades — unidades como **Santo Amaro** ficam sobrecarregadas enquanto outras, como **Limeira**, ficam com capacidade ociosa (Pedro Ganem Filho / Larisse Gois, 00:23:34–01:03:59).
- Agendamentos hoje são geridos por sistemas externos/legados, acessados via API (não nativos ao Salesforce) — ex.: agendamento de CNH passa por "sistema de arrendamento" externo, não pelo Service Cloud (Rafael Marques, 00:15:27).
- Já existe uso de Agentforce para agendamento em pelo menos um fluxo mencionado como já operacional (referência incidental de Larisse Gois em 00:05:54). [Assumed — mencionado de forma incidental, não detalhado]
- Dados de atendimento hoje estão pulverizados entre sistemas (WhatsApp/Meta, plataforma interna, sessões de mensagem), o que já gerou dor em projetos anteriores — Juliane Lopes citou experiência similar no **DataPrev**, com alta granularidade de dados e limitações de extração na Meta exigindo arquitetura complexa (00:46:08).

## Desired State
- **Decisão-chave alinhada**: Service Cloud atua como motor/backend; **Slack é a interface única (frontend) de trabalho para os atendentes** — todo o trabalho do atendente passa por um único hub (Larisse Gois, 00:13:39: *"por mais que você pode ter o service gerindo filas, gerindo agendas e afins, isso vai ter que aparecer no Slack pros atendentes"*).
- Quatro jornadas de atendimento foram desenhadas como possibilidades (não fechadas, para orientar discovery):
  1. **Apoio ao atendimento presencial via Slack** — base de conhecimento, canais de especialistas, Slackbot que abre "ticket" para especialista humano quando não resolve.
  2. **Pré-atendimento digital via atendentes ociosos** — Slack aciona um agente que identifica filas no WhatsApp e dispara mensagens antecipando etapas do atendimento.
  3. **Atendimento totalmente digital** — dos 4.000+ serviços, os que puderem ser 100% digitais, sem necessidade de ida ao posto.
  4. **Atendimento agêntico** — mediado por Agentforce de ponta a ponta, com **validação humana final obrigatória** antes do fechamento do caso.
- Balanceamento de carga entre unidades físicas e virtuais: uma unidade sobrecarregada pode redirecionar atendimento para atendentes ociosos de outras unidades, independentemente da região (Rafael Marques, Juliane Lopes, 00:26:08–00:27:04).
- Objetivo de reduzir a "sobrecarga física" migrando parte crescente do volume para canais digitais, corrigindo a disparidade atual de 2% no WhatsApp.
- Painéis analíticos via Tableau (incluindo dados de Marketing Cloud para campanhas de engajamento) — mas posicionados com cautela, sem prometer granularidade antes do detalhamento (ver Open Questions).

## Integrations
- **MuleSoft + Platform Events (Eventos de Plataforma)** definidos como camada de integração para gerenciar fluxo e espelhamento de mensagens entre Service Cloud e Slack (decisão alinhada).
- A conexão **WhatsApp ↔ Slack não é nativa** — exige integração via Digital Engagement + uma camada intermediária adicional ("MID") para fazer a ponte de comunicação que falta nativamente entre as duas plataformas (Rafael Marques / Osvaldo Melo, 00:14:31–00:16:29).
- Arquitetura decidida: **Service Cloud conectado a sistemas legados de agendamento** via API — o Service Cloud consome eventos desses sistemas externos para habilitar o atendimento via Slack (Rafael Marques, 00:15:27–00:16:29).
- **Risco técnico identificado e mitigado com dupla abordagem**: por preocupação de Nelson Stebulaitis Filho quanto à estabilidade do motor de conversa via WhatsApp (*"minha maior dúvida é só essa solução, assim, ela é realmente estável, tranquila, não tem risco de... a mensagem parar de chegar"*, 01:14:27), a equipe confirmou que **duas soluções técnicas paralelas** foram adotadas para mitigar o risco: a solução apresentada por Osvaldo Melo e uma segunda, trabalhada por **Vinicius Ferraz** em paralelo, envolvendo um recurso adicional de "bring" + uma camada MID complementar (Osvaldo Melo, 01:15:43).
- Demonstração técnica (protótipo funcional) apresentada por Osvaldo Melo: recepção do cidadão pelo Agentforce → criação de eventos de plataforma → geração de tópicos no Slack, tudo via MuleSoft como intermediário (00:29:10–00:31:15). Réplica de dados sem transformação complexa **nesta fase** — sem uso de ferramenta de ETL como Informatica (00:31:15–00:34:17).
- Salesforce **MCP** (Model Context Protocol) mencionado como possibilidade futura para levar dados analíticos à IA da Salesforce (Viviani Hupp, 00:46:08).

## Data Migration
- Não há migração de dados legados discutida como tal — o modelo é de **replicação/espelhamento em tempo real** (via Platform Events) entre sistemas, não uma migração pontual.
- Osvaldo Melo confirmou que, nesta fase, não há transformação de dados complexa nem uso de ferramenta de ETL — apenas réplica direta dos eventos de plataforma.
- **Ponto de atrito não resolvido**: Juliane Lopes discordou parcialmente, apontando que vê "uma certa necessidade de estruturação de dados" e precisa "mastigar melhor esse fluxo" com Nelson antes de descartar transformação (00:34:17). [Unknown — contradição entre Osvaldo/Larisse ("sem transformação") e Juliane Lopes ("precisa de estruturação")]

## Users & Roles
- **Atendentes presenciais** dos postos Poupatempo — usuários primários do Slack, tanto durante atendimento presencial (apoio) quanto durante ociosidade (pré-atendimento digital).
- **Cidadãos** (ex.: persona "Ana", "Anderson", "Felipe", "Renata" usados como exemplos nas jornadas) — interagem via WhatsApp ou presencialmente.
- **Especialistas** acionáveis via canais no Slack para apoio a atendentes em dificuldade.
- **Time de administração/sistemas central** (não a unidade local) seria responsável por cadastro, perfil e alocação de fila dos atendentes no Service Cloud — Rafael Marques descartou a necessidade de um workflow customizado só para isso, tratando como administração padrão (00:56:40–00:57:26). [Assumed — papel ainda não nomeado formalmente]
- Não foram mencionados números de headcount de atendentes, licenças ou volumetria de usuários nesta reunião. [Unknown]

## Timeline & Constraints
- Cronograma originalmente vendido ao cliente era de **6 meses** de entrega única — time decidiu evitar essa abordagem e estruturar entregas faseadas com quick wins (Larisse Gois / Juliane Lopes, 00:18:49–00:20:01).
- **Prazo comercial crítico**: proposta precisa ser consolidada para **setembro** (mês corrente) — Pedro Ganem Filho e Juliana Brites enfatizaram a criticidade competitiva.
- Nelson Stebulaitis Filho **bloqueou a própria agenda no dia seguinte (23/set)** para materializar o desenho técnico da solução e mapear casos de uso/detalhes operacionais (01:10:32–01:11:35).
- Muitos detalhes de arquitetura e regras de negócio foram explicitamente **empurrados para a fase de projeto (discovery)** — não são gaps a resolver antes da proposta, mas cláusulas de discovery a prever no escopo (recorrente ao longo da reunião, ex.: 00:22:30, 00:42:33, 00:58:16).

## Budget Signals
- Discussão comercial ocorreu, mas sem números de preço no conteúdo revisado. [Assumed — nenhuma cifra específica foi mencionada na reunião]
- **Modelo comercial alinhado**: capacidade fixa de serviço (não time & materials, não escopo 100% fixo), com **remuneração atrelada a entregas e escopo validados progressivamente** — Juliana Brites: *"a gente pensa numa capacidade fixa de serviço e a cada detalhamento que a gente vai fazendo, refinando, a gente vai validando com o cliente escopo e os esforços realmente feitos... eles vão fazendo pagamento pra gente por entregas"* (01:09:35).
- Proposta deve conter: mapa de arquitetura inicial, cronograma de casos de uso entregues em etapas progressivas, e uma **estimativa de capacidade mínima por nuvem** (Service Cloud, Slack/Unito(?), Tableau) — Juliana Brites, 01:08:18.
- Pedro Ganem Filho é o responsável por alinhar esse modelo (capacidade fixa + pagamento por entrega) diretamente com a PRODESP (01:08:18–01:09:35).

## Compliance & Security
- Único ponto tangencial: um cenário hipotético levantado por Larisse Gois onde a coleta de biometria seria substituída por consumo de dados do **TSE** para validação de identidade em um fluxo 100% digital — tratado explicitamente como exercício de raciocínio, não como decisão ("eu vou dar uma viajada que eu não acho que eles vão chegar nessa linha", 00:38:44). [Unknown — hipótese não confirmada, não é requisito]
- Nenhuma outra menção a LGPD, residência de dados, ou requisitos regulatórios específicos nesta reunião. [Unknown — gap a explorar em discovery]

## Decisões Made
### Alinhadas
1. **Arquitetura de atendimento**: Service Cloud = motor/backend; Slack = interface única de trabalho para os atendentes.
2. **Uso de MuleSoft + Platform Events** para gerenciar integração, fluxo e espelhamento de mensagens entre Service Cloud e Slack.
3. **Escopo de serviços e regras de ociosidade**: detalhamento da carta de serviços a digitalizar e regras de negócio do pré-atendimento ficam para a fase de projeto (discovery).
4. **Modelo comercial**: capacidade fixa de serviço, remuneração atrelada a entregas e escopo validados progressivamente.
5. **Balanceamento de carga** entre unidades físicas e virtuais, usando ociosidade de outras unidades para atender demanda excedente.
6. **Arquitetura de integração**: Service Cloud conectado a sistemas legados de agendamento via API (não há integração nativa WhatsApp↔Slack).
7. **Duas soluções técnicas paralelas** adotadas para mitigar risco de estabilidade do motor de conversa via WhatsApp/Slack.

### Precisa de mais conversa (gaps / perguntas ao cliente)
- **Mecanismo de alocação/disponibilidade de atendentes ociosos**: acionamento manual pelo próprio atendente no Slack **vs.** modelo preditivo automatizado de alocação de filas alinhado ao motor Omnichannel do Service Cloud. Decisão explicitamente deixada para definição em tempo de projeto (Renata Vendramini / Rafael Marques, 00:59:53–01:03:02).
- **Fonte da verdade dos indicadores de atendimento**: Service Cloud vs. sistema legado maduro do cliente — não definida; Renata Vendramini alertou que indicadores podem não ser factíveis dado o esforço de desenvolvimento (BEC) necessário para unificar dados pulverizados (01:05:12–01:07:25).
- **Uso do Salesforce Scheduler**: Renata Vendramini propôs internalizar agendamentos externos no Scheduler para melhor gestão de tempos/SLA — não decidido, tratado como possibilidade a avaliar em projeto (00:39:40–00:42:33).
- **Necessidade de transformação/estruturação de dados (ETL)**: Osvaldo/Larisse dizem que não há necessidade nesta fase; Juliane Lopes discorda parcialmente e quer revisar o fluxo com Nelson antes de fechar.
- **Granularidade dos dados analíticos (Tableau)**: Juliane Lopes trouxe experiência de projeto anterior (DataPrev/Meta) com limitações de extração — decisão é posicionar recursos analíticos com cautela, sem promessas de indicadores antes do detalhamento (00:48:30).
- **Regras de antecipação de atendimento**: quantos dias de antecedência, e quais dos 4.000 serviços permitem antecipação digital — depende de validação de escopo com o cliente (00:52:17–00:55:04).
- **Filtro/critério de roteamento** para pré-atendimento (por tipo de serviço vs. por unidade vs. por prioridade de fila) ainda em aberto (00:57:26).

## Action Items
- **[O grupo]** Validar serviços: mapear quais dos 4.000 serviços atuais podem ser digitalizados ou atendidos remotamente durante a fase de projeto.
- **[Juliane Lopes, Nelson Stebulaitis Filho]** Revisar fluxo técnico: analisar o fluxo de dados entre Slack, Service Cloud e sistemas externos.
- **[O grupo]** Planejar cronograma com foco em entregas rápidas (quick wins) para viabilizar percepção de valor da plataforma.
- **[Juliana Brites]** Revisar proposta: criar mapa de arquitetura inicial + cronograma de entregas; definir casos de uso da proposta de solução.
- **[Nelson Stebulaitis Filho]** Desenhar solução: materializar o desenho técnico, mapear detalhes operacionais e casos de uso — agenda do dia seguinte (23/set) bloqueada para isso.
- **[Larisse Gois]** Documentar validações: registrar possibilidades avaliadas e decisões técnicas internas; compartilhar documento com a equipe.
- **[Pedro Ganem Filho]** Compartilhar licenciamento: disponibilizar documentos de licenciamento para composição da proposta final.
- **[O grupo]** Criar cronograma de prestação de serviços referente à proposta enviada.
- **[O grupo]** Definir estratégia / estruturar plano de serviços para a entrega da solução.
- **[O grupo]** Apresentar overview da solução proposta e dos casos de uso definidos.
- **[Viviani Hupp, Pedro Ganem Filho, Larisse Gois]** Produzir materiais visuais (slides comerciais sobre Tableau) e alinhar entrega do cronograma/estratégia de serviços.

## Key Quotes
> "O Slack é o único fronte. Então assim, o surfice fica por trás pra nos dar as ferramentas para fazer toda a gestão que a gente precisa de atendimento... por mais que você pode ter o service gerindo filas, gerindo agendas e afins, isso vai ter que aparecer no Slack pros atendentes." — Larisse Gois (00:13:39)

> "Isso é um dial para setembro... é a aplicação mais importante da América Latina. Todo mundo, todos os fabricantes do mundo querem ela e a jornada do atendente tá na nossa mão." — Pedro Ganem Filho (00:50:28)

> "os agendamentos são feitos [60%] no app, 38% no tótem físico e 2% só no WhatsApp. Então, realmente tem uma disparidade muito grande." — Pedro Ganem Filho (00:23:34)

> "minha maior dúvida é só essa solução, assim, ela é realmente estável, tranquila, não tem risco de... a mensagem parar de chegar." — Nelson Stebulaitis Filho (01:14:27)

> "a gente adotamos duas soluções para a mesma coisa... porque a gente estava com medo disso, do mesmo [risco] que você [comentou]." — Osvaldo Melo (01:15:43)

> "a gente pensa numa capacidade fixa de serviço e a cada detalhamento que a gente vai fazendo, refinando, a gente vai validando com o cliente escopo e os esforços realmente feitos... eles vão fazendo pagamento pra gente por entregas." — Juliana Brites (01:09:35)

> "eu não tô nem me atentando tanto ao micro mesmo. É só um teste de mesa da solução macro ainda." — Nelson Stebulaitis Filho (00:59:05)

> "A gente vendeu sonho, todo mundo fala legal, mas eles conseguirem começar a ter de forma palpável o que que eles podem fazer com essas ferramentas... fazendo uma boa entrega muda o jogo completamente pra gente." — Larisse Gois (01:16:43)

> "mas é uma oportunidade única para a gente trazer algo que é o desejo de todo mundo... o mercado inteiro tá atrás disso." — Pedro Ganem Filho (01:16:43)

> "Pro bem ou pro mal. Não esqueça disso." — Pedro Ganem Filho (01:16:43, sobre a responsabilidade da equipe após a venda)

## Open Questions & Ambiguity
- Alocação de disponibilidade de atendentes ociosos: manual (Slack) vs. preditivo automatizado (Omnichannel) — **[Unknown]**, decisão explicitamente adiada.
- Fonte da verdade dos indicadores de atendimento: Service Cloud vs. sistema legado do cliente — **[Unknown]**.
- Viabilidade/factibilidade dos indicadores solicitados pelo cliente dado o esforço de desenvolvimento (BEC) necessário para unificar dados pulverizados entre WhatsApp/Meta, Slack e Service Cloud — **[Unknown]**, risco levantado por Renata Vendramini sem resposta fechada.
- Necessidade de transformação/estruturação de dados (ETL): posição de Osvaldo/Larisse ("não precisa nesta fase") contradiz preocupação de Juliane Lopes ("vejo necessidade de estruturação") — **[Unknown]**, contradição não resolvida em reunião, a ser destravada entre Juliane Lopes e Nelson Stebulaitis Filho.
- Uso do Salesforce Scheduler para internalizar agendamentos externos — proposto, não decidido — **[Unknown]**.
- Quais dos 4.000+ serviços atuais serão elegíveis para digitalização, pré-atendimento ou atendimento totalmente digital — depende de mapeamento a ser feito em discovery — **[Unknown]**, ação pendente formalizada como next step.
- Regras de antecedência para antecipação de atendimento (quantos dias, quais serviços) — **[Unknown]**.
- Papel/responsável formal pela administração de cadastro e alocação de fila dos atendentes no Service Cloud — mencionado como "time central de sistemas", mas não nomeado como função de projeto — **[Assumed]**.
- Requisitos de compliance/segurança/LGPD/residência de dados — não abordados nesta reunião — **[Unknown]**, gap a levantar em discovery.
- Cifra de investimento/preço da proposta — não mencionada nesta reunião; modelo comercial (capacidade fixa + pagamento por entrega) foi discutido, mas nenhum valor foi dito — **[Assumed]** que a negociação de valores ocorre em outro fórum (Pedro Ganem Filho ↔ PRODESP).
