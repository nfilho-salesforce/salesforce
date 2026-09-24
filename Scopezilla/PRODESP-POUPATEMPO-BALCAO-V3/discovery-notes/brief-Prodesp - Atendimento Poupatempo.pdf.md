# Brief visual — Prodesp - Atendimento Poupatempo.pdf (69 páginas)

> Extração literal do conteúdo visual (diagramas, wireframes, mockups, personas, texto em cards) via leitura página a página. Nada foi inferido além do que está visível na imagem. Deck é majoritariamente visual — texto corrido é escasso, a informação está em cards, diagramas de jornada e mockups de WhatsApp/Slack.

---

## Página 1 — Capa
Fundo azul Salesforce. Logo "poupatempo" (com sublinhado vermelho) + brasão "GOVERNO DO ESTADO DE SÃO PAULO". Mascote Astro (Salesforce) vestido de lobo/urso segurando a nuvem "salesforce", ao lado de um "blueberry" (mascote Slack) e estrelas decorativas. Título: **"Ninguém Espera, Ninguém Fica Ocioso"**.

## Página 2 — "Obrigado"
Slide de encerramento (idêntico ao da página 69) aparecendo logo após a capa — provavelmente um slide de template reaproveitado/fora de ordem no arquivo fonte. Texto "Obrigado" + mascotes Salesforce/Slack + bandeira do Brasil.

## Página 3 — Agenda
Lista as 5 jornadas do deck, nesta ordem exata:
- **01** Primeira Jornada: Atendimento Presencial com Slack
- **02** Segunda Jornada: Pré-Atendimento Digital
- **03** Terceira Jornada: Atendimento Digital
- **04** Quarta Jornada: Atendimento Agêntico
- **05** Quinta Jornada: Gestão Comunicação

> Nota: a ordem/nome real das jornadas no deck difere do que constava no brief textual prévio — aqui J1 é "Atendimento Presencial com Slack" (apoio ao atendente via Slack) e J2 é "Pré-Atendimento Digital" (antecipação do atendimento agendado).

## Página 4 — Resumo Executivo
Card "Contexto Atual":
- Gargalo no Atendimento Presencial: filas extensas e alto Tempo Médio de Atendimento (TMA) nos postos centrais, causados em grande parte pela checagem e triagem manual de documentos no guichê
- Capacidade Ociosa Dispersa: unidades centrais no limite de capacidade enquanto atendentes de outros postos têm ociosidade sem integração entre redes
- Dependência de Atendimento Físico: serviços elegíveis para a esfera digital continuam exigindo atendimento presencial
- Escala Limitada ao Headcount e Horário Comercial

Card "Benefícios Solução Salesforce":
- Eficiência e Redução da Ociosidade: diminui filas redistribuindo a checagem documental para atendentes ociosos da rede (Balanceamento Virtual de Carga) e adiantando a burocracia antes do atendimento presencial
- Jornada Digital e Ininterrupta (24/7): resolução 100% remota via WhatsApp, combinando validação jurídica com Agentes de IA autônomos
- Escalabilidade: automatiza demandas, libera força de trabalho humana para atuar como supervisora (Human-in-the-Loop) e em casos mais complexos
- Governança e Conformidade: centraliza a operação no Slack e Salesforce, garantindo auditabilidade, proteção de dados (LGPD) e padronização do atendimento

---

## JORNADA 1 — Atendimento Presencial com Slack

### Página 5 — Título de seção
"01. Atendimento Presencial com Slack"

### Página 6 — Contexto/Solução/Benefícios
**Contexto Atual:**
- Gargalo operacional: em casos complexos/exceções o operador trava e não resolve sozinho; abre chamados lentos, chama supervisão ou pede ao cidadão "voltar outro dia"
- Comunicação Descentralizada: coordenação ocorre em grupos pessoais de WhatsApp, sem governança, sem histórico, sem conformidade LGPD

**Solução Salesforce:**
- Slack como Sistema Único e Hub de Operação — interface principal de trabalho e apoio do atendente
- Suporte Inteligente: Slackbot e/ou Agentes de IA integrados consultam base de conhecimento
- Transbordo em Tempo Real: especialistas acionados em canais dedicados sem o operador se ausentar do posto

**Benefícios:**
- Redução do Tempo Médio de Atendimento e Resolução
- Resolução Assistida por IA (consulta em linguagem natural)
- Apoio Instantâneo sem Parar o Atendimento (inclusive indisponibilidade de sistema)
- Governança, Auditabilidade e LGPD (canais oficiais e auditáveis)

### Página 7 — Diagrama de jornada (mapa de fluxo com "trilha" colorida)
Personas na lateral: **Cidadã** (Ana), **Atendente** (Anderson). Sequência de balões ao longo da trilha:
1. Realiza agendamento para CIN
2. Comparece ao Posto de Atendimento Presencial
3. [Anderson] Inicia o atendimento
4. Tem dificuldades para coletar uma das digitais
5. Interage com Slackbot para saber o que ele deve fazer nessa situação
6. Slackbot sugere algumas ações e pergunta se conseguiu resolver ou se gostaria de ajuda de um especialista
7. Anderson diz que quer ajuda de um especialista
8. Slackbot abre um ticket para um especialista e apresenta o link do canal para Anderson ser atendido
9. Especialista identifica o problema no sistema e auxilia na correção
10. Anderson finaliza a coleta das digitais e o atendimento da Ana
11. Ana fica satisfeita com o tempo reduzido de atendimento

### Página 8 — Persona card
**Ana** — Cidadã (foto: mulher jovem, fundo amarelo)

### Páginas 9–11 — Mockups WhatsApp (jornada de agendamento da Ana)
- **Pág. 9**: Chat WhatsApp "Poupatempo" (verificado): "Olá! ✨ Sou o assistente virtual do Poupatempo SP.GOV.BR" → cidadã: "Gostaria de tirar minha CIN" → bot envia card com logo **gov.br**: "Realize sua autenticação. GOV.BR"
- **Pág. 10**: Mockup da tela de login **gov.br**: "Identifique-se no gov.br com: Número de CPF" + campo CPF + botão "Continuar" + opções alternativas: "Login com seu banco" (badge "SUA CONTA GRÁTIS"), "Seu aplicativo gov.br", "Seu certificado digital em nuvem"
- **Pág. 11**: WhatsApp continua: bot — "O posto de atendimento mais próximo a sua residência é o de Santo Amaro. Temos disponíveis os horários das 14:30 e 16h para o dia 13/05. Algum desses horários é interessante?" → cidadã: "Sim, as 14h está ótimo" → bot: "Agendamento foi realizado com sucesso! 😊 - Serviço: Emissão de CIN - Data: 13/05/2026 - Horário: 14:30 - Local: Poupatempo Santo Amaro" → cidadã: "Ok, muito obrigado!"

### Página 12 — Persona card
**Anderson** — Atendente em Santo Amaro (foto: homem careca, barba, óculos)

### Página 13 — Foto de ambiente físico
Foto real de um posto Poupatempo: atendente (camisa azul "poupatempo") auxiliando cidadã em guichê, monitor com sistema aberto, sinalização ao fundo: "ATENDIMENTO 1-20", "RETIRADA DE DOCUMENTOS", "SAÍDA", "SENHA".

### Página 14 — Mockup Slack (Home)
Tela inicial do Slack ("Hoje", data "setembro 5") mostrando painel "IA do Slackbot", seção "No que se concentrar hoje" (sem itens — "Hoje você está tendo um dia tranquilo"), "Pauta" (com sugestão de acessar pesquisas/contextos via agente Slackbot), "Tarefas" (Criar uma tarefa), "Destaques".

### Página 15 — Mockups Slack (thread de suporte)
Dois painéis lado a lado: Anderson pergunta ao Slackbot "não estou conseguindo realizar a leitura de digital, o que devo fazer?" → Slackbot responde com checklist (confirmar leitor funcionando/higienizado; orientar posicionamento do dedo; tentar outros dedos; evitar pressão excessiva/repetição/produtos não previstos no manual) → Anderson: "ainda estou com dificuldades" → Slackbot: "recomendo falar com um especialista... Quer que eu já abra um chamado no #atendimentos-cin registrando o caso?" → Anderson: "por favor" → Slackbot posta no canal **#atendimentos-cin**, protocolo **CIN-20260905-0121**, menciona @Anderson Santos, resume o problema e as tentativas já feitas, pergunta "Você quer aprovar as alterações?" com botões **Sim/Não**.

### Páginas 16–17 — Continuação Slack (canal de transbordo)
- **Pág. 16**: Três painéis mostrando a criação do canal #atendimentos-cin (opções "Adicionar pessoas ao canal / Adicionar descrição do canal / Envie e-mails para o canal / Escolha um modelo") e a thread anterior com "Agente" entrando na conversa.
- **Pág. 17**: Canal #atendimentos-cin com painel lateral "Conversa" — mensagem do Anderson com protocolo CIN-20260905-0121; **Agente** responde: "Olá, identifiquei um problema no sistema, você poderia desconectar e conectar novamente o leitor da digital e tentar novamente?" → Anderson: "Ótimo, agora deu certo, muito obrigado".

---

## JORNADA 2 — Pré-Atendimento Digital

### Página 18 — Título de seção
"02. Pré-atendimento Digital"

### Página 19 — Contexto/Solução/Benefícios
**Contexto Atual:**
- Filas e Longo Tempo de Atendimento Presencial devido à triagem/conferência manual de documentos no guichê
- Capacidade Crítica dos Postos (postos centrais no limite)
- Ociosidade Dispersa na Rede (atendentes de outras unidades com momentos de baixa demanda)

**Solução Salesforce:**
- Antecipação da Etapa Burocrática via WhatsApp & Slack: cidadão abordado antes do dia agendado; atendente ocioso usa Slack para analisar/conferir/validar documentação previamente
- Presencial Reduzido ao Essencial (coleta de biometria e/ou atividades essenciais)

**Benefícios:**
- Redução Drástica do Tempo Médio de Atendimento
- Balanceamento Virtual de Carga de Trabalho (aproveita ociosidade de atendentes de qualquer posto)
- Aumento na Vazão de Atendimentos (mais cidadãos/hora com mesma infraestrutura e quadro)

### Página 20 — Diagrama de jornada
Personas: **Cidadã** (Ana), **Atendente** (Felipe), **Atendente** (Anderson). Sequência:
1. Identifica-se
2. Diz que quer fazer tirar CIN
3. Recebe sugestões de postos de atendimento
4. Confirma o dia e hora e local do agendamento
5. [Felipe] Sabe que terá um tempo ocioso pela frente
6. Acessa o Slack
7. Inicia o fluxo de atendimento
8. Aguarda o sistema encontrar alguém
9. [Ana] Recebe mensagem no whats
10. Demonstra interesse no pré-atendimento
11. Solicita documentação para análise
12. Acessa o canal específico para efetuar o atendimento
13. Utiliza agente do **T7** algumas dúvidas
14. Utiliza slackbot para dúvidas/validações
15. Finaliza o atendimento
16. [Ana] Vai pessoalmente no posto de atendimento de Santo Amaro
17. [Anderson] Inicia atendimento
18. Utiliza o Slack
19. Finaliza o atendimento presencial

> Nota: primeira aparição explícita do **"agente do T7"** dentro de um fluxo desenhado — é acionado pelo atendente durante o pré-atendimento remoto para "algumas dúvidas".

### Páginas 21–26 — Mockups (repetem o padrão WhatsApp/gov.br já visto, com novo conteúdo)
- **Pág. 21**: Persona card Ana (repetição)
- **Pág. 22**: WhatsApp — intro do assistente + pedido de CIN + card gov.br (repetição do fluxo de auth)
- **Pág. 23**: Mockup tela de login gov.br (repetição)
- **Pág. 24**: WhatsApp — fluxo de **reagendamento**: bot pede confirmação de CEP "15.200-000", avisa "ao confirmar o reagendamento, o agendamento atual será cancelado. Posso prosseguir?" → cidadã "Sim" → bot: "O reagendamento foi realizado com sucesso! 😊 Novo agendamento: - Serviço: CIN - Carteira de Identidade Nacional - Data: 13/05/2026 - Horário: 14:30 - Local: Poupatempo **Santo Amaro**"
- **Pág. 25**: Mockup laptop + celular — notificação de lockscreen (Sábado, 29 de Junho, 11:30): **"Agendamento próximo — Ana, que tal fazermos um pré-atendimento agora e agilizar a emissão da sua CIN?"**
- **Pág. 26**: WhatsApp — confirmação com **Protocolo: 7403459773**; bot pede documentos: "1. Certidão de nascimento 2. CPF"; anexos enviados na conversa: `certidao.pdf` (1 página, 262 KB) e imagem de CPF; bot: "Muito obrigada Ana, lembre de levar amanhã seus documentos originais."

### Página 27 — Transição
"Como isso foi possível?" (slide de transição, fundo azul)

### Página 28 — Persona card
**Felipe** — Atendente Poupatempo (foto: homem, suéter escuro)

### Página 29 — Foto de ambiente físico
Sala tipo call center dentro do Poupatempo: várias estações de trabalho lado a lado, atendentes de uniforme amarelo em cada uma, monitor de painel ao fundo exibindo "F2412 1" (painel de senha/fila).

### Página 30 — Mockup Slack (Workflows)
Canal **#pre-atendimentos**, aba "Workflows": workflow destacado **"Busca Pre Atendimento"** — descrição: "Busca cidadãos que gostariam de ter um atendimento agilizado", com botão de iniciar ("Start workflow").

### Página 31 — Mockup Slack (modal de workflow)
Modal **"Serviço"** aberto sobre o canal #pre-atendimentos: campo "Tipo de serviço" com opções em rádio: **Renovação de CNH** / **Emissão de CIN** (selecionado) / **Emissão de atestado de antecedentes criminais**. Botões "Close" / "Submit".

> Nota: primeira evidência visual de que o workflow de pré-atendimento cobre pelo menos 3 tipos de serviço nomeados: CNH (renovação), CIN (emissão) e atestado de antecedentes criminais (emissão) — não apenas CIN, como o texto extraído sugeria.

### Página 32 — Mockup Slack (mensagem do workflow no canal)
Canal #pre-atendimentos: Felipe entrou no canal; o workflow bot posta: "Tipo de serviço: Emissão de CIN. Buscando interessados em realizar o pré atendimento" (com 1 resposta em thread).

### Página 33 — Thread do workflow
Resposta do workflow bot na thread: **"Cidadão encontrado, canal criado: #protocolo-1234556"**.

### Página 34 — Canal de protocolo
Canal **#protocolo-1234556**: Felipe: "Olá, para emissão de CNI preciso que me envie uma cópia da sua certidão e do seu CPF"; Ana Motta entra no canal e envia 2 arquivos: imagem de CPF + `certidao.pdf`.

### Página 35 — Benefícios (cards numerados)
- **01** Cadastro prévio da documentação — "Ana já chegou no atendimento com a documentação pré cadastrada"
- **02** Ganho de agilidade no atendimento para o cidadão — "O atendimento presencial resumiu-se a cadastro de biometria (foto e digitais)"
- **03** Otimização no tempo do atendente — "Felipe aproveitou o tempo ocioso na unidade para antecipar o atendimento da Ana"

---

## JORNADA 3 — Atendimento Digital

### Página 36 — Título de seção
"03. Atendimento Digital"

### Página 37 — Contexto/Solução/Benefícios
**Contexto Atual:**
- Capacidade crítica em postos centrais e ociosidade em outros postos da rede
- Dependência do Deslocamento Presencial mesmo quando cidadão possui documentos válidos digitalmente
- Limitação de Horário Comercial: atendimentos digitais assistidos ocorrem exclusivamente na janela de trabalho humana dos atendentes

**Solução Salesforce:**
- Atendimento Humano 100% Remoto e Assíncrono para serviços elegíveis
- Validação via Slack: cidadão envia documentos com validade jurídica pelo WhatsApp
- Atendente processa/valida a solicitação via Slack com auxílio de Slackbot para acelerar checagem
- Documento entregue na casa do cidadão

**Benefícios:**
- Despressurização Físico-Operacional dos Postos
- Experiência e Conveniência ao Cidadão (sem deslocamento/espera)
- Governança, Rastreabilidade e LGPD

### Página 38 — Diagrama de jornada
Igual estrutura da Jornada 2, mas culminando em: "[Ana] Recebe a CIN em casa depois de **5 dias úteis**" (sem etapa presencial — atendimento 100% remoto).

### Páginas 39–42 — Mockups repetidos
Persona Ana, WhatsApp intro + gov.br, tela de login gov.br, fluxo de reagendamento — idênticos aos das páginas 21–24 (mesmos textos/telas reaproveitados).

### Página 43 — Mockup lockscreen
Notificação: **"Atendimento disponível — Ana, disponibilizamos um atendimento 100% digital hoje às 14:30, você teria disponibilidade?"**

### Página 44 — WhatsApp (documentos + foto)
Repete pedido de certidão/CPF (protocolo 7403459773) e adiciona: **"Precisamos de uma foto sua. Procure um ambiente iluminado e fundo de cor única"**.

### Página 45 — WhatsApp (selfie + assinatura)
Cidadã envia foto (selfie) → bot: "Ótimo. O último passo é assinar utilizando nosso serviço digital" com botão **[Assinar]** → captura de assinatura manuscrita digital "Ana Motta" → bot: "Muito obrigado, o prazo para análise e recebimento da sua CIN é de **5 dias úteis**".

---

## JORNADA 3 (continuação) / material reaproveitado

### Página 46 — Persona card
Felipe — Atendente Poupatempo (repetição)

### Páginas 47–50 — Mockups Slack repetidos
Repetem exatamente as páginas 30, 31, 32, 34 (workflow "Busca Pre Atendimento", modal "Serviço", canal #pre-atendimentos, canal #protocolo-1234556) — mesmos prints reaproveitados nesta seção do deck.

### Página 51 — Benefícios adicionais
- **01** Antecipação de atendimento — "Ana conseguiu emitir a CIN antes do prazo inicial"
- **02** Produtividade — "Nos momentos de ociosidade Felipe vai conseguir finalizar mais atendimentos"
- **03** Governança — "Todas as mensagens trocadas no atendimento ficam registradas e são auditáveis"

---

## JORNADA 4 — Atendimento Agêntico

### Página 52 — Título de seção
"04. Atendimento Agêntico"

### Página 53 — Contexto/Solução/Benefícios
**Contexto Atual:**
- Escala Limitada pela Capacidade Humana: por mais eficiente que seja o atendimento humano/digital, fica limitado ao headcount disponível
- Atendimento Comercial: atualmente ocorre apenas em horário comercial

**Solução Salesforce:**
- **Força de Trabalho Sintética**: Agentes de IA Salesforce e/ou Terceiros integrados a Salesforce assumem o atendimento ao cidadão via WhatsApp
- Atendimento Conectado e Ininterrupto (24/7): o Agente de IA identifica o cidadão e a demanda, solicita documentos, valida regras de negócio e conclui a solicitação a qualquer hora
- Supervisão Humana Estratégica (**Human-in-the-loop**): o atendente atua no Slack apenas como validador final

**Benefícios:**
- Disponibilidade 24 horas, 7 dias por semana (elimina filas de espera virtuais)
- Escalabilidade (absorção de picos de demanda — ex.: mutirões, novas emissões de RG/CIN)
- Humanização do Trabalho do Atendente: operador humano deixa validações repetitivas e passa a atuar como supervisor/especialista de casos complexos

### Página 54 — Diagrama de jornada
Introduz um terceiro tipo de ator visual: **"Agente"** (avatar de IA, ícone azul), além de Cidadã e Atendente. Sequência:
1. Identifica-se
2. Diz que quer fazer tirar CIN
3. Recebe sugestões de postos de atendimento
4. Confirma o dia e hora e local do agendamento
5. [**Agente**] Busca cidadãos que podem ser atendidos
6. Envia WhatsApp
7. [Ana] Demonstra interesse no Atendimento
8. Recebe mensagem no whats
9. [**Agente**] Entende o processo de atendimento
10. Solicita documentação
11. Valida documentação
12. Solicita Foto e assinatura
13. Finaliza o atendimento
14. [Atendente — avatar azul, sem nome atribuído nesta jornada] Acessa Slack e consulta atendimentos realizados
15. Valida o atendimento realizado pelo agente
16. [Ana] Recebe a CIN em casa depois de 5 dias úteis

> Nota: nesta jornada o atendente humano que faz a validação final aparece com avatar genérico (sem nome de persona atribuído no diagrama), diferente das jornadas anteriores que nomeiam Anderson/Felipe.

### Página 55 — Persona card
Ana — Cidadã (repetição)

### Página 56 — Mockup lockscreen
Notificação: **"Você sabia — Ana, que tal utilizar nossa nova plataforma e efetuar seu atendimento de modo digital a qualquer hora do dia?"**

### Página 57 — Persona card
Felipe — Atendente Poupatempo (repetição, ainda que o diagrama da pág. 54 não o nomeie)

### Página 58 — Mockup Slack (artefato de validação gerado por IA)
Painel "Files" do Slack exibindo um documento estruturado: **"Protocolo 1234556 – Emissão de CIN – Ana Motta"**, com seções:
- **Resumo da Solicitação**: Ana Motta, horário local, "Solicitante: Ana Motta. Tipo de solicitação: Emissão de CIN (Carteira de Identidade Nacional). Canal: #protocolo-1234556. Ana Motta solicitou a emissão da CIN e enviou os documentos pedidos (certidão e CPF) em resposta ao pedido inicial."
- **Documentos Enviados**: tabela com `certidao.pdf` e `im_cpf.jpg`, cada um com link "Visualizar"
- **Avaliação da IA**: "✅ Tudo correto — os documentos enviados foram analisados e estão de acordo com o exigido para a emissão da CIN."
- **Validação**: botão **[VALIDAR]**

> Este é o artefato visual mais concreto de "Human-in-the-Loop" no deck: um resumo de caso gerado por IA, dentro do Slack, com um único botão de validação humana.

### Página 59 — Benefícios adicionais
- **01** Atendimento 24h — "Ana conseguiu emitir a CIN no horário que ela estava disponível"
- **02** Felipe continua importante — "A validação humana ainda é essencial para finalizar o processo e em casos que o agente não consiga finalizar o atendimento"

---

## JORNADA 5 — Gestão de Comunicação (seção incompleta no deck)

### Página 60 — Título de seção
"05. Gestão de Comunicação"

### Página 61 — Cards vazios
Slide **"Gestão Comunicação"** com dois cards numerados **01** e **02** — **ambos sem qualquer texto de corpo** (apenas o número em círculo, nenhum título nem descrição preenchidos). Diferente de todas as outras jornadas, esta seção não tem: contexto atual, solução Salesforce, benefícios, diagrama de jornada, personas ou mockups. É essencialmente um placeholder de template não preenchido.

> **Achado relevante para escopo**: a 5ª jornada mencionada na Agenda (pág. 3) não tem nenhum conteúdo desenvolvido no deck além do título. Se "Gestão de Comunicação" é escopo real, precisa ser detalhado — hoje é um stub.

---

## Seção final — Solução Proposta / Cronograma / Investimentos

### Página 62 — Título de seção
"Solução Proposta"

### Página 63 — **Diagrama de Arquitetura Salesforce** (slide mais importante para arquitetura)
Layout esquerda→direita:
- **Cidadã** → ícone **WhatsApp** (rótulo: "Comunicação e envio de documentação")
- **Atendente** → ícone **Slack** (rótulo: "Comunicação com o cidadão")
- Ambos os canais apontam para uma caixa central grande: **"Plataforma Salesforce Headless"**
- À direita da plataforma: uma barra vertical rotulada **"API/MCP"** sobre **"Plataforma de integração"** (ícone azul circular, estilo logo de plataforma de integração/MuleSoft) — os fluxos de dados atravessam essa barra
- Setas bidirecionais rotuladas (de cima a baixo): *Dados de atendimentos*, *Cadastro e consulta*, *Autenticação*, *IA*, *Employee Data*, *Dados analíticos*
- À direita, coluna vertical **"Sistemas Integrados"** contendo caixas escuras nomeadas: **Atendimento**, **Biometria**, **Gov.br**, **T7**, **Agentes de IA**, **API de terceiros**, **Sistema Semântico**

> **Achados novos vs. texto extraído**:
> - Não há qualquer menção ou logo de **ServiceNow** neste diagrama de arquitetura nem em nenhuma outra página do deck — apesar de citado no contexto do briefing, não aparece visualmente nesta versão.
> - **"Sistema Semântico"** aparece como um sistema integrado nomeado, distinto de "Agentes de IA" e de "T7" — é a primeira vez que esse componente é citado; sugere uma camada de busca semântica/RAG separada do agente T7.
> - **"Employee Data"** e **"Dados analíticos"** aparecem como fluxos de dados distintos atravessando a "Plataforma de integração" — indicando integração com dados de RH/força de trabalho e uma camada analítica, não apenas dados de atendimento ao cidadão.
> - A camada de integração é rotulada genericamente "Plataforma de integração" com ícone que se assemelha ao logo do MuleSoft, mas o nome do produto não é escrito explicitamente.
> - "Biometria" e "Gov.br" e "T7" aparecem como **sistemas de destino/integração** (caixas do lado direito), não apenas como conceitos de jornada.

### Página 64 — Benefícios da solução (cards numerados)
- **01** Flexibilidade e Escalabilidade — "Uma plataforma flexível possibilita adaptar-se aos diferentes serviços e jornadas de atendimento do Poupatempo"
- **02** Integração Ecossistêmica — "A plataforma se integra com sistemas existentes para viabilizar a digitalização do atendimento"
- **03** Slack como Hub Unificado de Trabalho — "O Slack atua como a interface unificada onde o atendente trabalha, colabora, acessa manuais, interage com assistentes digitais e Agentes de IA"
- **04** Inteligência Contextual & Retroalimentação Analítica — "Os dados analíticos da plataforma Salesforce geram conhecimento e contexto que retroalimentam Agentes de IA, melhorando continuamente o atendimento"

### Página 65 — Título de seção
"Cronograma Macro"

### Página 66 — Cards vazios
Slide **"Cronograma: Entrega por Jornadas"** com dois cards numerados **01** e **02**, **ambos sem texto de corpo** — mesmo padrão de placeholder vazio da página 61. Nenhuma data, fase, duração ou sequenciamento visível.

> **Achado relevante para escopo**: não há cronograma real no deck — apesar do título "Cronograma Macro" e do slide "Entrega por Jornadas", nenhuma data/fase foi preenchida. Nada a extrair aqui além da existência da intenção de estruturar entrega por jornada.

### Página 67 — Título de seção
"Investimentos"

### Página 68 — Cards vazios
Slide **"Investimentos: Produtos e Serviços"** com dois cards numerados **01** e **02**, **ambos sem texto de corpo** — mesmo padrão de placeholder vazio das páginas 61 e 66. Nenhum valor, produto ou serviço nomeado.

> **Achado relevante para escopo**: não há nenhuma cifra, produto/SKU ou proposta comercial visível neste deck — a seção "Investimentos" está vazia. Não há vazamento de preço para tratar; mas também não há nenhum insumo comercial aproveitável.

### Página 69 — Encerramento
"Obrigado" (idêntico à página 2) — mascotes Salesforce/Slack + bandeira do Brasil.

---

## Resumo de achados novos (não presentes na extração textual de 1768 palavras)

1. **Arquitetura concreta com 7 sistemas integrados nomeados**: Atendimento, Biometria, Gov.br, T7, Agentes de IA, API de terceiros, **Sistema Semântico** (este último é novo/não documentado antes).
2. **Nenhuma menção a ServiceNow** em nenhuma página, incluindo o diagrama de arquitetura — contradiz a expectativa de que haveria integração ServiceNow visível.
3. Fluxos de dados na "Plataforma de integração" incluem **Employee Data** e **Dados analíticos**, além de Autenticação, Cadastro/consulta, Dados de atendimentos e IA.
4. O workflow de pré-atendimento no Slack cobre pelo menos **3 tipos de serviço**: Renovação de CNH, Emissão de CIN, Emissão de atestado de antecedentes criminais (modal "Serviço", págs. 31/48) — não só CIN.
5. Existe um **artefato concreto de Human-in-the-Loop**: um resumo de caso gerado por IA no Slack (protocolo, documentos, avaliação da IA, botão VALIDAR) — pág. 58.
6. Na Jornada 4 (Agêntica), o atendente humano validador aparece **sem persona nomeada** no diagrama (avatar genérico), diferente das outras jornadas que usam Anderson/Felipe.
7. **Três seções inteiras estão vazias no deck-fonte**: "Gestão de Comunicação" (Jornada 5), "Cronograma: Entrega por Jornadas" e "Investimentos: Produtos e Serviços" — todas têm apenas títulos de card (01/02) sem qualquer texto preenchido. Isso é lacuna de discovery, não informação a ser extraída.
8. Personas cidadã/atendente reaproveitam as mesmas fotos e falas em várias jornadas (Ana, Felipe, Anderson) — reforçando que o deck é construído sobre um roteiro narrativo único replicado por jornada, e não 5 cenários totalmente distintos de personas.
