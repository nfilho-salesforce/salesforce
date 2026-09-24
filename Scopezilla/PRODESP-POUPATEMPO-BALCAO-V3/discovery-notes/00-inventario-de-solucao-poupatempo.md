# Inventário de solução — Poupatempo (PRODESP)

> **Destino:** entrada de discovery para o Scopezilla.
> **Origem:** derivado das duas especificações de processo em `clients/prodesp/processos/`, versão **2.0** de 23/09/2026, e do quadro FigJam `nnU7s7eXiIfOnoA9xwg9Ww`. A especificação é a fonte da verdade; o quadro é renderização dela. Este inventário é uma terceira renderização — se divergir das specs, as specs mandam.
> **Gerado em:** 23/09/2026.

> ## ⚠ Leia isto antes de escopar a partir deste documento
>
> **A maior parte do que está aqui é proposta nossa, não fato do cliente.** Só duas fontes são do cliente: o deck "Prodesp — Atendimento Poupatempo" (**F2.2**) e a ata da reunião de 23/09/2026 (**F2.3**). Todo o resto — trinta premissas de solução — foi decidido por nós em 23/09/2026 para fechar caminhos que o desenho deixava abertos, e **nenhuma foi validada com o cliente**.
>
> Cada item abaixo está marcado com a sua origem. Na linguagem do Scopezilla: o que vem de F2.2 ou F2.3 é **Confirmed**; o que vem de F2.4 em diante é **Assumed**, e vira pergunta antes de virar escopo.
>
> **Não há volumetria, não há contagem de usuários e não há data de go-live para o Poupatempo.** O `client_target` de jan/fev 2027 que está no `.project-metadata.json` é do engajamento **DER-SP rodovia**, outro escopo — não reaproveitar aqui.

---

## 1. Identidade e enquadramento

| Campo | Valor | Origem |
|---|---|---|
| Conta | PRODESP — Companhia de Processamento de Dados do Estado de São Paulo | Confirmed |
| Programa | **Poupatempo** — rede de atendimento ao cidadão do Estado de São Paulo | Confirmed (F2.2) |
| Iniciativa | Atendimento remoto e apoio ao atendimento presencial | Confirmed (F2.2) |
| Relação com o engajamento DER-SP | **Iniciativa distinta, mesma conta.** Não compartilha processo, sistema nem persona com o socorro em rodovia | Confirmed |
| Estado modelado | TO BE. Não existe AS IS documentado | Confirmed |
| Profundidade | Analítico, nível de delivery | — |
| Recorte | **MVP** — Minimum Viable Product | Confirmed (F2.3) |

---

## 2. Escopo: o que entra e o que fica de fora

**Duas jornadas foram especificadas.**

**Jornada 1 — Antecipar atendimento agendado.** Um robô detecta atendente de mesa ocioso, consulta a fila viva, e só com ela vazia procura um agendamento futuro para antecipar. Oferece ao cidadão por WhatsApp, autentica no gov.br, roteia para a fila, e o atendente conduz o atendimento pelo Slack. Cinquenta e três elementos de fluxo.

**Jornada 2 — Apoiar o atendimento presencial pelo Slack.** O atendente do guichê trava num procedimento, consulta um Slackbot sem sair do lugar, e se preciso escala para um canal de especialidade. Dezoito elementos de fluxo.

**Fora de escopo, declarado:**

- O agendamento em si — feito por totem do Detran, entregue em fase anterior. `Confirmed (F2.2)`
- O atendimento presencial subsequente à antecipação.
- **O escopo se restringe aos atendentes de mesa** (RN-09). `Confirmed (F2.3)`
- **Três das cinco jornadas do deck do cliente não foram especificadas:** pré-atendimento digital, atendimento agêntico e gestão de comunicação. Elas existem no material do cliente e **não** foram analisadas. Se entrarem no escopo, este inventário não as cobre.

---

## 3. Participantes e personas

| Participante | Tipo BPMN | Papel | Persona no deck |
|---|---|---|---|
| Cidadão | pool fechado | Recebe a oferta, aceita ou recusa, autentica-se, responde | **Ana** — cidadã (F2.2, pág. 8) |
| Atendente de mesa | raia | Trabalha pelo Slack. Declara ociosidade, atende, encerra | **Felipe** — atendente Poupatempo (F2.2, pág. 28) |
| Atendente do posto | raia | Atende no guichê e pede apoio sem sair do lugar | **Anderson** — atendente em Santo Amaro (F2.2, pág. 12) |
| Especialista | raia | Atua remotamente a partir do canal da especialidade | — |
| Robô de antecipação | raia (executor automatizado) | Consulta a API, dispara a mensagem ativa, controla prazos | — |
| Roteamento Omni-Channel | raia (executor automatizado) | Dono da fila. Enfileira, busca atendente ocioso, entrega | — |
| Slackbot | raia (executor automatizado) | Consulta base de conhecimento, abre chamado, aciona canal | — |
| Coordenação | não é raia | Compartilha com o atendente o gesto de declarar ociosidade | — |

**Contagem de usuários: desconhecida.** Nenhuma fonte diz quantos atendentes de mesa, quantos atendentes de posto, quantos especialistas, nem quantos postos. `Unknown`

---

## 4. Sistemas e integrações

| Sistema | Tipo BPMN | Usado em | O que sabemos | Estado |
|---|---|---|---|---|
| **ServiceNow** | depósito de dados | J1 passos 4, 12, 25 · J2 passo 6 | CRM master e service desk. Fornece o protocolo no início da interação e recebe transcrição, anexos e histórico no fim. **Carga histórica inicia do zero, sem migração** | Confirmed (F2.3) |
| **Sistema de agendamento** | pool fechado | J1 passos 2, 18, 21 | API externa **com lógica de seleção própria** — a inteligência que escolhe qual agendamento antecipar é dela, não nossa. Agendamento do cidadão é feito por totem do Detran | Confirmed (F2.3) |
| **Slack** | canal de trabalho | J1 passos 1, 11, 16, 20, 44 · J2 passos 2, 5, 7, 8, 9 | Um canal por usuário, uma thread exclusiva por chamado. Canais por especialidade na jornada 2 | Confirmed (F2.3) |
| **WhatsApp** | canal do cidadão | J1 passos 5, 6, 15, 47 | Mensagem ativa (outbound) **tem custo por disparo e não garante resposta**. Há janela de sessão que expira | Confirmed (F2.3) |
| **gov.br** | pool fechado | J1 passos 47, 48, 49 | Provedor de identidade federal. Caixa-preta | **Assumed (F2.7)** — a autenticação foi decisão nossa |
| **Serviço de biometria** | integração de consulta | J1 passo 53 | É a caixa "Biometria" que a arquitetura do próprio cliente lista como sistema integrado. **Contra qual base consulta não foi definido** — gov.br, IIRGD, Detran ou base própria | Nome Confirmed (F2.2); uso Assumed (F2.9) |
| **Agente do T7** | pool fechado | J1 passo 16 | IA interna da PRODESP que responde FAQ, **já em adoção no Poupatempo**. Consultado pelo Slackbot, não pelo atendente | Existência Confirmed (F2.5); integração Assumed (F2.8) |
| **Base de conhecimento** | depósito de dados | J2 passo 3 | Precisa estar estruturada por especialidade | Confirmed (F2.3) |
| **Fila de atendimento** | depósito de dados | J1 passos 1a, 9, 44 | Controlada pelo Omni-Channel. O robô apenas consulta | Confirmed (F2.3) |

**Catorze fluxos de mensagem entre pools** estão inventariados como M-01 a M-14 na especificação da jornada 1.

### Produtos Salesforce

**Nenhuma fonte do cliente nomeia produto Salesforce por passo.** O deck traz apenas uma caixa genérica "Plataforma Salesforce". A associação abaixo é **proposta nossa** e está marcada como tal na legenda do quadro.

| Produto | Onde propomos | Estado |
|---|---|---|
| Slack | Canal de trabalho do atendente nas duas jornadas | **Assumed** |
| Omni-Channel | Enfileiramento e entrega automática do caso ao atendente ocioso | **Assumed** |
| Agentforce | Resumo do histórico (J1 passo 12) e apoio à dúvida do atendente (J1 passo 16) | **Assumed** |

---

## 5. Premissas de solução — trinta, nenhuma validada

Organizadas pelo que assumem. A coluna **Se o cliente disser não** é o que o Scopezilla precisa para dimensionar risco de retrabalho.

### 5.1 Premissas que vieram do cliente — `Confirmed`

Estas **não** são premissas nossas. Estão aqui porque restringem o desenho.

| ID | Regra | Fonte |
|---|---|---|
| RN-01 | Ociosidade é declarada **manualmente** pelo atendente ou pelo coordenador, via Slackbot. Não há detecção automática | Ata |
| RN-02 | As filas são organizadas por **departamento**, não por agência territorial | Ata |
| RN-03 | O protocolo de atendimento vem do ServiceNow no início da interação | Ata |
| RN-04 | Um canal de Slack por usuário e uma thread exclusiva por chamado | Ata |
| RN-05 | O agente de IA entrega **resumo** do histórico, nunca a transcrição completa | Ata |
| RN-06 | O agente validador de documentos **não entra no MVP** | Ata |
| RN-07 | Todo não atendimento é registrado no sistema de agendamento para impedir disparo duplicado | Ata |
| RN-08 | O encerramento pelo Slack fecha o caso, encerra a sessão e remove o status de ocioso, num comando só | Ata |
| RN-09 | O escopo se restringe aos **atendentes de mesa** | Ata |
| J2 RN-01 | O acionamento é por canal ou thread, nunca por menção a especialista nominal | Ata |
| J2 RN-02 | Todo pedido de apoio vira chamado no ServiceNow — **de service desk apenas** | Ata |
| J2 RN-03 | O atendente não se ausenta do guichê em nenhum ponto do fluxo | Deck |

### 5.2 Premissas de arquitetura — decisão nossa, alto impacto se recusada

| ID | Premissa | Se o cliente disser não |
|---|---|---|
| **RN-21** (F2.7) | A identidade do cidadão é **verificada no gov.br antes de o caso entrar na fila**. Nenhuma ação de atendimento acontece sem autenticação concluída | **Cinco elementos saem do fluxo** (47 a 51) e o desfecho 55 deixa de existir. O risco R-08 desaparece junto |
| **RN-22** (F2.8) | O **Slackbot é a porta única** das dúvidas do atendente; dúvida de FAQ é encaminhada ao agente do T7 por integração. O atendente não escolhe a quem perguntar | Se o cliente quiser o T7 como canal direto, o passo 16 muda e L-34 vira desenho de integração diferente |
| **RN-23** (F2.9) | A validação de biometria é **consulta, não decisão**. O resultado é registrado e não altera o caminho | Se biometria validada dispensar o presencial, **o gateway 17 deixa de ser a única porta de saída** e o passo 18 ganha gatilho novo. É a premissa que mais mexe no desenho |
| **RN-17** (F2.4) | **A fila viva tem precedência sobre a antecipação proativa.** Só com a fila vazia o robô procura agendamento | Se o cliente quiser antecipação paralela à fila, o gateway 1b some e o risco R-07 muda de natureza |
| **RN-18** (F2.4) | A entrega ao atendente é **automática e automaticamente aceita**. Não existe gesto de aceitar nem recusar | Volta o passo de aceite e o de devolução à fila, que foram removidos, e E-05 volta a ser decisão de aceite |
| **RN-20** (F2.4) | A fila é controlada pelo Omni-Channel; o robô só consulta, nunca administra | Muda o dono do enfileiramento e o desenho das duas raias automatizadas |

### 5.3 Premissas de tratamento de exceção — decisão nossa

| ID | Premissa | Se o cliente disser não |
|---|---|---|
| RN-10 (F2.4) | Atendimento por canais digitais só é **iniciado até uma hora antes do fim do expediente** | Volta a existir atendimento atravessando o fim do expediente, sem destino desenhado |
| RN-11 (F2.4) | Falha de entrega no WhatsApp é tratada como **contato inválido** e sinalizada ao ServiceNow, impedindo nova tentativa | Precisa de política de retentativa, que não existe |
| RN-12 (F2.4) | A ausência do resumo do histórico **não bloqueia** o atendimento | O resumo vira dependência dura e a indisponibilidade do agente de IA para o processo |
| RN-13 (F2.4) | O protocolo do ServiceNow é **bloqueante**: sem ele não existe interação | Precisa de modo degradado sem protocolo |
| RN-14 (F2.4) | Falha de integração **depois** do atendimento prestado não reverte o atendimento; o atendente fecha manualmente | Precisa de compensação automática, que é ordem de grandeza diferente |
| RN-15 (F2.4) | O atendente pode devolver à fila um atendimento **em curso**, sem descartar o que já foi feito | Some o passo 44 e o limite de três transferências |
| RN-16 (F2.4) | Cancelamento do agendamento por outro canal permanece com **gestão manual** no MVP | Entra integração de cancelamento bidirecional |
| RN-19 (F2.4) | Na transferência, o próximo atendente recebe o resumo **atualizado com o atendimento em curso** | Muda o contrato do agente de resumo |
| RN-24 (F2.10) | **O Slackbot pode não saber, e dizer que não sabe.** A decisão de como seguir é do atendente | Exige cobertura de base de conhecimento que ninguém dimensionou |
| E-06 (F2.4) | Falha da API de agendamento: **uma única retentativa**, sem espera crescente nem fila de reprocessamento | Entra política de resiliência |
| E-08 (F2.4) | Falha de entrega no WhatsApp é lida como telefone incorreto ou número sem WhatsApp | — |
| E-09 (F2.4) | Resposta que não é aceite nem recusa gera **uma única repergunta**; a segunda fora do esperado é tratada como silêncio | — |
| E-13 (F2.4) | Máximo de **três** transferências, depois encerra por indisponibilidade | O laço volta a poder circular sem limite |
| E-16 (F2.4) | O ciclo de complemento **não tem limite numérico**: o atendente decide quando parar | — |
| E-22 (F2.4) | Cidadão que cancela por outro canal: **nenhum caminho automático**, deliberadamente | — |
| E-24 (F2.7) | Indisponibilidade do gov.br, falha de autenticação, desistência e prazo esgotado têm **o mesmo destino** | Abre braço novo no fluxo para cada caso distinto |
| J2 RN-04 (F2.4) | Especialidade sem canal próprio cai num **canal geral de plantão** | Precisa de roteamento alternativo |
| J2 RN-05 (F2.4) | Haverá **plantão de especialistas cobrindo todo o horário** de atendimento | É compromisso operacional, não de software. Se não houver, E-07 volta a ser caminho de processo |
| J2 RN-06 (F2.4) | O registro no ServiceNow **não é bloqueante** para o apoio acontecer | — |
| J2 RN-07 (F2.4) | **Não há segundo nível automático** de escalonamento; o especialista escala manualmente | Entra hierarquia de escalonamento |
| J2 RN-08 (F2.10) | O "não sei" do Slackbot é desfecho legítimo e não decide nada por si | — |

---

## 6. Riscos

### Jornada 1

| ID | Risco | Onde | Mitigação discutida |
|---|---|---|---|
| **R-07** | **A antecipação pode nunca acontecer.** Se a fila raramente esvazia, o passo 2 nunca é alcançado e o investimento em antecipação proativa não se realiza | gateway 1b | Medir com que frequência a fila está vazia no momento da declaração de ociosidade, **antes** de dimensionar o ganho |
| **R-08** | **A autenticação gov.br é ponto de abandono.** Cidadão sem conta, com senha esquecida ou que não completa o segundo fator perde a antecipação mesmo tendo aceitado — e o disparo de WhatsApp já foi pago | passos 47, 48 | Medir taxa de conclusão da autenticação no piloto. Possível, não decidido: aceitar nível de confiança mais baixo para serviços que não exigem identidade forte |
| R-01 | **Ociosidade manual não é confiável.** O atendente pode estar ocupado e não sinalizar; o coordenador pode marcar alguém incorretamente | passo 1 | Painéis de tempo offline. Expõe, não resolve |
| R-02 | Custo de mensagem ativa no WhatsApp sem garantia de resposta | passo 5 | Timeout curto e registro de não atendimento |
| R-03 | Disparo duplicado do mesmo agendamento se o não atendimento não for registrado | passo 21 | RN-07 |
| R-04 | Vaga de agendamento presencial fica ocupada se o cancelamento não acontecer | passo 18 | Integração que cancela junto com o encerramento. Fase inicial pode ser manual |
| R-05 | Gestão dos canais de Slack por usuário em admissão e desligamento | passo 11 | ServiceNow como histórico definitivo reduz o impacto; a gestão de canal permanece |
| R-06 | Pessoa deixa de estar ociosa no exato momento da resposta do cidadão | passo 11 | A entrega é automática, então o caso chega de qualquer modo. A saída é transferir, e isso custa tempo do cidadão |

### Jornada 2

| ID | Risco | Onde | Mitigação discutida |
|---|---|---|---|
| R-01 | **Base de conhecimento mal estruturada torna o Slackbot inútil** e o fluxo vira só abertura de chamado | passo 3 | Depende de L-01 |
| R-02 | Canal de especialidade sem ninguém de plantão deixa o cidadão esperando no guichê | passo 8 | Timeout e encaminhamento. Prazo não definido |

### Riscos de engajamento, não do processo

- **Nenhuma das trinta premissas foi validada.** O desenho inteiro é uma proposta coerente construída sobre suposições nossas. Uma reunião de validação pode derrubar várias de uma vez.
- **Não existe roteiro de serviço.** O passo 14 da jornada 1 e o passo 9 da jornada 2 são subprocessos colapsados: a caixa é honesta quanto ao que não sabemos, mas o conteúdo precisa existir antes do build (L-32 e L-14).
- **Sem volumetria**, não dá para dizer quais exceções são frequentes e quais são raras. A priorização é por gravidade estrutural, não por incidência.

---

## 7. Pendente de definição

### 7.1 Só o cliente responde — bloqueia escopo

| ID | Pergunta | Bloqueia |
|---|---|---|
| **L-35** | **O que a validação de biometria decide?** Biometria validada remotamente dispensa o presencial, ou o presencial é mantido de todo modo? Não validada interrompe a antecipação? E contra qual base se valida — gov.br, IIRGD, Detran ou base própria da PRODESP? | Passo 53 e muito provavelmente o gateway 17. **A mais cara da rodada** |
| **L-33** | **Autenticação gov.br:** qual nível de confiança cada serviço exige — bronze, prata ou ouro? Qual o prazo para o cidadão se autenticar? Como o resultado volta para o robô? O que fazer com quem não tem conta gov.br? | Passos 47 a 51 e o risco R-08. Antes disso, confirmar a própria premissa: o Poupatempo autentica no gov.br para atendimento remoto? |
| **L-13 (J2)** | **O agente do T7 e o Slackbot fazem a mesma coisa.** São o mesmo componente, um substitui o outro, ou coexistem? Se coexistem, quem se consulta primeiro e as bases de conhecimento são a mesma? | Passo 3 da jornada 2 e o desenho da base de conhecimento. Nosso posicionamento é RN-22, mas é posicionamento, não resposta |
| **L-03 (J1)** | **Quais serviços permitem transbordo para atendimento virtual?** | Critério de elegibilidade do passo 2. Define o tamanho real do benefício |
| **L-02 (J1)** / **L-01 (J2)** | As especialidades são por **departamento** ou por **tipo de problema**? | Configuração da fila, estrutura dos canais e da base de conhecimento |
| **L-32 (J1)** | O que existe dentro do subprocesso 14, **serviço a serviço**? | Conteúdo do passo 14. Relacionada a L-03 |
| **L-14 (J2)** | O que existe dentro do subprocesso 9, **especialidade a especialidade**? | Conteúdo do passo 9. Relacionada a L-01 |
| **L-31 (J1)** | Um caso vindo da fila percorre o mesmo roteiro da antecipação, incluindo cancelar o agendamento presencial. Isso vale para toda demanda espontânea, ou só para quem também tem agendamento? | Passos 14 e 18 no braço "sim" de 1b |
| **L-27 (J1)** | Confirmar que caso dependente de órgão parceiro (IIRGD, Detran) é a saída "não" do gateway 17, e não um ramo próprio | E-18 |

### 7.2 Prazos que não existem — bloqueiam configuração, não arquitetura

| ID | O que falta |
|---|---|
| **L-01 (J1)** | Prazo de tolerância para a resposta do cidadão (braço 7c) e para a disponibilidade de atendente (braço 10b) |
| **L-28 (J1)** | Prazo para o cidadão responder ao atendente depois de aceitar (temporizador 15t). **Atenção: desde a v2.0 esse prazo reinicia a cada pedido de complemento** |
| **L-29 (J1)** | Tempo de inatividade que dispara o encerramento automático (passo 43) |
| **L-02 (J2)** | Prazo para um especialista assumir antes do encaminhamento |
| **L-15 (J2)** | **Quanto tempo o apoio especializado pode durar?** O laço não tem limite numérico nem temporizador, e há um cidadão sentado no guichê |

### 7.3 Técnicas e de conformidade

| ID | O que falta |
|---|---|
| **L-34 (J1)** | **Contrato da integração Slackbot ↔ agente do T7:** qual interface, quem mantém a base de conhecimento, como se decide o que é FAQ, e o que o atendente vê quando o T7 está indisponível. A decisão foi integrar; o como não existe |
| **L-12 (J1)** | **Opt-out do cidadão:** como é capturado, onde é armazenado, quem o respeita nos ciclos seguintes. É obrigação de canal e **provavelmente tem exigência jurídica** |
| **L-13 (J1)** | Quem provisiona e desprovisiona o canal de Slack, e o que ocorre com casos em aberto no desligamento. Materializa R-05 |
| **L-06 (J1)** | Como funciona a integração nativa do Slack com o objeto de caso e o acesso ao histórico |
| **L-30 (J1)** | O que acontece se a consulta à fila (passo 1a) falhar ou expirar. O caminho feliz foi decidido; a falha não tem destino |
| **L-36 (J1)** | **Quem executa as tarefas de serviço 18, 25 e 53?** Estão numa raia humana e são chamada de sistema. Decisão de arquitetura, levantada e não fechada |
| **L-05 (J1)** | A revisão humana em fluxos automatizados fica ou sai do MVP? |

---

## 8. Matriz de extração pré-preenchida

Para o `discover` do Scopezilla. As dezesseis áreas, com o estado real.

| # | Área | Estado | Evidência ou motivo |
|---|---|---|---|
| 1 | Identidade da empresa | **Confirmed** | PRODESP, programa Poupatempo, setor público estadual de São Paulo |
| 2 | Estado atual Salesforce | **Unknown** | Nenhuma fonte descreve o que já existe de Salesforce no Poupatempo. O T7 é IA da PRODESP, não Salesforce |
| 3 | Solução alvo | **Assumed** | Slack, Omni-Channel e Agentforce são **proposta nossa**. O deck traz só "Plataforma Salesforce" |
| 4 | Usuários e personas | Personas **Confirmed**, contagem **Unknown** | Ana, Felipe e Anderson vêm do deck. Nenhum número de atendentes, postos ou especialistas |
| 5 | Prazo e go-live | **Unknown** | Nada para o Poupatempo. O `client_target` do metadata é do DER-SP — **não reaproveitar** |
| 6 | Objetivos de negócio | **Assumed** | O objetivo implícito é reduzir presencial antecipando atendimento e encurtar o tempo de resolução no guichê. **Nenhum KPI, meta ou percentual foi declarado** |
| 7 | Processos de negócio | **Confirmed** | Duas jornadas especificadas em nível analítico, 53 e 18 elementos, com exceções inventariadas |
| 8 | Integrações | **Confirmed** para ServiceNow, agendamento, Slack, WhatsApp, base de conhecimento; **Assumed** para gov.br, biometria e T7 | Ver seção 4. Catorze fluxos de mensagem inventariados |
| 9 | Migração de dados | **Confirmed** | **Carga histórica do ServiceNow inicia do zero, sem migração** |
| 10 | Conformidade | **Unknown, com alerta** | Nada declarado. Mas há **dado pessoal de cidadão em WhatsApp**, autenticação de identidade e **biometria** — e o opt-out (L-12) é apontado como provável exigência jurídica. Zona de LGPD não explorada |
| 11 | Orçamento | **Unknown** | Nenhum sinal |
| 12 | Stakeholders | Parcial | Nelson Stebulaitis Filho e Rafael Marques aparecem nas fontes. Patrocinador, decisor e área dona não identificados |
| 13 | Riscos e restrições | **Confirmed** | Dez riscos inventariados. Ver seção 6 |
| 14 | Sinais de handoff | Pré-venda / definição de escopo de MVP | As specs já estão em formato que aguenta virar backlog |
| 15 | Design de experiência | Parcial | Três personas do cliente e duas jornadas desenhadas. **Nenhuma pesquisa com usuário, teste de usabilidade ou requisito de acessibilidade** |
| 16 | Governança | **Unknown** | Nada sobre CoE, gestão de mudança, treinamento ou plano de adoção — apesar de o desenho mudar a rotina de duas populações de atendentes |

---

## 9. Stubs — nomeados mas sem nada atrás

Na linguagem da persona do Scopezilla: *stub é lacuna, não escopo*. Estes aparecem citados e não sustentam build.

- **"Plataforma Salesforce"** — nomeada no deck do cliente como caixa única, sem produto, processo ou usuário atrás.
- **Serviço de biometria** — nomeado na arquitetura do cliente, mas não se sabe contra qual base consulta, se a integração existe ou precisa ser construída, nem o que o resultado decide.
- **Agente do T7** — tem definição de papel (responde FAQ) e nenhum contrato de integração.
- **Subprocesso 14 (J1) e subprocesso 9 (J2)** — caixas colapsadas, conteúdo inexistente serviço a serviço.
- **Três jornadas do deck** — pré-atendimento digital, atendimento agêntico e gestão de comunicação: nomeadas, nunca especificadas.

---

## 10. Rastreabilidade

| Artefato | Caminho |
|---|---|
| Especificação jornada 1 (v2.0) | `clients/prodesp/processos/01-antecipacao-proativa.process.md` |
| Especificação jornada 2 (v2.0) | `clients/prodesp/processos/02-apoio-presencial-slack.process.md` |
| Gaps e exceções consolidados | `clients/prodesp/processos/00-gaps-e-excecoes.md` |
| Controle de alterações C-01 a C-12 | `clients/prodesp/processos/CHANGELOG.md` |
| Snapshot congelado da v1.9 | `clients/prodesp/processos/versoes/v1.9/` |
| Registro de fontes F2.1 a F2.12 | `clients/prodesp/01-fontes/registro-de-fontes.md` |
| Registro da sessão de desenho | `clients/prodesp/99-log/2026-09-23-bpmn-poupatempo-registro-da-sessao.md` |
| Quadro FigJam | `nnU7s7eXiIfOnoA9xwg9Ww` — v1.9 congelada à esquerda, v2.0 vigente à direita |
| Lucidchart | `73781e03-e981-44c5-bc9e-997617cc3bc8` — **doze versões defasado, não usar** |
