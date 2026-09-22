# Resumo Executivo — PRODESP · Poupatempo Balcão V2

*Gerado em 22/09/2026 · atualizado em 22/09/2026 com `data/strategy.json` · Scopezilla `narratives` · Audiência: executiva e técnica combinada*

## Visão Geral Rápida

- **Dor atual**: casos que fogem do script no balcão (biometria falha, documento divergente, sistema fora do ar) ainda dependem de coordenação informal entre postos por WhatsApp pessoal, fora da LGPD.
- **Visão de transformação**: em vez de o atendente recorrer a WhatsApp pessoal, ele trabalha num posto de trabalho institucional com o conhecimento do serviço à mão e um especialista a um huddle de distância, enquanto a cidadã recebe pré-atendimento antes da visita e, quando precisa, é atendida por um agente de IA 24 horas com humano por trás de qualquer decisão sobre seus documentos.
- **Principais direcionadores de valor**: substituir a coordenação informal por canais auditáveis; dar visibilidade de capacidade ociosa entre os 244 postos e 900 totens sem contratar gente nova; evitar expansão física de atendimento via canais digitais.
- **Maior risco/incerteza**: a camada de integração MuleSoft com 5 sistemas-alvo (gov.br, biometria estadual, Sistema Semântico, T7, legado Prodesp) ainda não tem identidades nem protocolos confirmados — é o épico de maior risco técnico do programa.
- **Primeiro passo recomendado**: uma Fase 0 de resolução de discovery, fechando as lacunas que travam o kick-off técnico antes de qualquer build começar.

---

## Visão do Programa

A Prodesp busca colocar o Slack como posto de trabalho do atendente do Poupatempo para os casos que a triagem digital (WhatsApp/Portal) não resolve, ao mesmo tempo em que expande o atendimento digital à cidadã com pré-atendimento, validação remota de documentos e um agente conversacional 24/7. As duas frentes — tática no balcão e plataforma completa de atendimento agêntico — entram no mesmo contrato, faseadas: a operação ganha uma base auditável de coordenação já na Fase 1, e a plataforma Headless completa segue em fases subsequentes, sem depender de uma segunda negociação.

Em vez de o atendente do Poupatempo recorrer a grupos pessoais de WhatsApp para resolver o que a triagem digital não consegue, ele passa a trabalhar dentro de um posto de trabalho institucional — com o conhecimento do serviço à mão e um especialista a um huddle de distância — enquanto a cidadã que hoje só ouve "volte depois" recebe pré-atendimento antes de chegar ao balcão e, quando precisar, é atendida por um agente de IA disponível 24 horas, sempre com um humano por trás de qualquer decisão sobre seus documentos. A coordenação hoje informal e sem histórico se torna auditável por desenho; a capacidade ociosa entre 244 postos e 900 totens, hoje invisível, se torna um dado que orienta o roteamento em tempo real.

**Por que agora**: a regulação sobre dado pessoal e decisão automatizada (LGPD Art. 20, PL 2338/2023 em tramitação) já eleva a régua para qualquer fluxo agêntico em atendimento ao cidadão, enquanto a coordenação informal por WhatsApp pessoal continua sem histórico auditável — cada mês de atraso é mais exposição a um achado de controle externo (TCE-SP) sobre um serviço de alto volume e alta visibilidade institucional. **Por que Salesforce**: a plataforma cobre as duas frentes com uma única base — Slack como posto de trabalho, Agentforce grounded em Data 360 para o atendimento à cidadã — apoiada num ambiente Anypoint já maduro na conta Prodesp, o que reduz o risco de construir a integração MuleSoft do zero, ainda que não resolva por si só as identidades dos sistemas-alvo.

### Prioridades estratégicas

1. **Formalizar a integração multissistema (E09)** para desbloquear o caminho crítico do programa — é o épico de maior risco técnico (XL/Unknown) e trava tanto a validação remota de documentos quanto o atendimento agêntico.
2. **Substituir a coordenação informal do balcão por um canal institucional auditável** — a dor mais concreta hoje e a base sobre a qual as demais frentes de valor se apoiam.
3. **Nomear a governança de agentes de IA** antes de qualquer fluxo agêntico entrar em produção — a Fase 4 já é escopo contratado, não visão futura.
4. **Instrumentar o sinal de capacidade ociosa** entre postos e totens — pré-condição de dado para o roteamento em tempo real e o modelo preditivo de E10.
5. **Estender o atendimento digital à cidadã** antes e além da visita física — depende das quatro prioridades anteriores estarem resolvidas.

## Resumo do Escopo

Dez épicos organizados em duas frentes. A frente tática (E01, E02, E04, E05) coloca o atendente no Slack, com huddle de escalonamento, workflow de contingência para sistema fora do ar e a governança de adoção que sustenta o rollout nos 244 postos e 900 totens. A frente de capacidade e plataforma (E03, E06, E07, E08, E09, E10) resolve o sinal de ocupação por posto, o pré-atendimento por WhatsApp, a validação remota de documentos, o atendimento agêntico 24/7 e a integração MuleSoft que liga tudo isso aos sistemas-alvo da Prodesp.

Distribuição de complexidade: 2 épicos S, 5 M, 2 L e 1 XL — o mix concentra a maior parte do esforço em complexidade média, com dois picos de risco em E08 (atendimento agêntico sem case de referência LATAM) e, sobretudo, E09 (a integração multi-sistema).

## Destaques da Solução

A arquitetura tem quatro camadas. No posto de trabalho, canais Slack por serviço com Canvas lastreado em Salesforce Knowledge e um agente Agentforce de tópico único, grounded em Data 360, resolvendo dúvidas de fluxo sem o atendente sair da cadeira (E01). Na operação, um sinal de ocupação/fila por posto — ainda sem fonte identificada, tratado como a maior incerteza técnica do programa junto com a integração — alimenta o roteamento entre postos e, mais adiante, um modelo preditivo de tempo de espera (E03, E10). Na experiência da cidadã, pré-atendimento por WhatsApp antes da visita e um agente multi-tópico 24/7 com escalonamento genuíno para atendente humano, nunca decisão automática de emissão de documento (E06, E08). E na integração, uma camada MuleSoft API-led ligando a plataforma Salesforce Headless a gov.br, biometria estadual, Sistema Semântico, T7 e o legado da Prodesp — apoiada num ambiente Anypoint já maduro na conta, o que reduz o risco de construir a camada do zero, mas não resolve as identidades e protocolos de cada sistema-alvo (E09).

Uma decisão de arquitetura importante: E03 é o dono designado da construção do sinal de capacidade por posto; E10 o consome, mas não compartilha o custo de build — isso evita que a mesma fundação de dados seja construída duas vezes.

## Abordagem de Implementação

O programa está sequenciado em 6 fases: uma Fase 0 de resolução de discovery (sem épicos, mas pré-requisito de todo o resto), Fase 1 de fundação do posto de trabalho e governança (E01, E05), Fase 2 de operação tática do balcão (E02, E03, E04), Fase 3 da plataforma de integração MuleSoft (E09, trilha paralela — não bloqueia as fases baseadas em Slack), Fase 4 de experiência agêntica da cidadã (E06, E07, E08) e Fase 5 de analítica e fechamento (E10).

O caminho crítico sequencial é E01 → E02 → E07, com E03 e E06 convergindo em E07 — atraso em qualquer uma das quatro fases atrasa a validação remota de documentos. A duração de referência do programa é 15–30 semanas, derivada da forma do engagement (classificação Multi-Cloud/Médio, com overlay regulatório de LGPD/setor público e a incerteza de E03/E06/E09 alargando o teto) — uma faixa de planejamento, não um compromisso de cronograma, e deve ser validada contra a disponibilidade real da equipe e a velocidade de decisão da Prodesp antes de qualquer citação ao cliente.

## Resumo de Esforço

A entrega é 100% Salesforce PS, sem redução de escopo por subtração — os papéis do lado cliente listados abaixo são cobertura necessária, não trabalho removido do time PS. O time nomeado combina arquitetura sênior onshore contínua (Program Manager, Solution Architect, Technical Architect) com um time de build e QA escalado ao volume do rollout, mantendo governança e change management ativos do início ao fim.

O programa carrega um item de governança que merece atenção antes do go-live: o owner de governança de agentes de IA do lado Prodesp ainda não foi nomeado. Sem esse papel definido, o atendimento agêntico 24/7 da Fase 4 entra em produção sem um dono claro de política de uso, guardrails e revisão de escalonamento — travar isso na Fase 0 evita retrabalho de governança depois que o agente já está no ar.

Uma ferramenta de IA aplicada durante a entrega comprime o cronograma dentro da mesma forma de time — não reduz headcount, não é insumo de precificação. No cenário atual de prontidão do cliente (Baixa, pela ausência de postura de ferramentas de IA e de governança nomeada), o ganho realizado projetado é modesto; ele sobe se a Prodesp nomear o owner de governança e formalizar as identidades dos 5 sistemas do MuleSoft antes do build.

## Riscos e Mitigações

| Risco | Fase | Mitigação |
|---|---|---|
| Licenciamento Slack dimensionado para a Sala de Situação, não para o headcount real de atendentes | 1 | Confirmar headcount por posto/totem na Fase 0 |
| Sinal de ocupação por posto sem fonte identificada | 2 | Resolver a fonte na Fase 0; E03 é o dono designado da construção |
| Owner de governança de agentes de IA não nomeado | 0/1 | Nomear antes do início da Fase 2 — item de maior exposição do programa |
| Identidades e protocolos dos 5 sistemas-alvo de E09 não confirmados | 0/3 | Formalizar no kick-off técnico; o ambiente Anypoint maduro na conta reduz só parte do risco |
| Evento de gatilho do agendamento que dispara o pré-atendimento (E06) não identificado | 4 | Confirmar o sistema de agendamento na Fase 0 |
| E08 é o primeiro fluxo agêntico 24/7 do setor público sem case de referência direto na América Latina | 4 | Aceito como nota qualitativa — sem case comparável, a calibração real só vem do piloto |

## Premissas e Nível de Confiança

A distribuição de confiança atual é 25% Confirmado, 55% Assumido e 20% Desconhecido, através de épicos e estimativas — um nível de confirmação baixo que recomenda uma sessão de validação com a Prodesp antes de fechar o escopo definitivo. O gap analysis identificou 136 lacunas, acima do limiar que recomenda a Fase 0 dedicada em vez de herdar a incerteza para dentro do build. Três épicos carregam confiança `Desconhecido` e alargam o teto das faixas de esforço e prazo até serem resolvidos: o sinal de ocupação por posto (E03), o evento de gatilho do pré-atendimento (E06) e as identidades dos sistemas-alvo do MuleSoft (E09) — este último o de maior risco técnico do programa inteiro.

Não há, publicamente, um caso de referência direto de "Slack + Agentforce num balcão de atendimento presencial de setor público na América Latina" — o posicionamento correto é first-mover/diferenciação, não padrão já provado na região.

## Próximos Passos e Recomendações

1. **Fechar a Fase 0 antes do kick-off técnico**: confirmar as 5 identidades de sistema de E09, a fonte do sinal de capacidade por posto, o sistema de agendamento que dispara o pré-atendimento, o owner de governança de agentes e o dimensionamento real de licenças Slack.
2. **Agendar uma sessão de validação de escopo com a Prodesp** antes de finalizar o compromisso de cronograma — a taxa de confirmação atual (25%) é baixa para travar um número final.
3. **Nomear o owner de governança de agentes de IA do lado Prodesp** com prioridade, dado que a Fase 4 (atendimento agêntico 24/7) já é escopo contratado, não visão futura.
4. **Tratar E09 como a trilha de maior lead time** e iniciar sua formalização de identidades em paralelo à Fase 1, para não ficar no caminho crítico do restante do programa.

---
*Este resumo consolida `data/epics.json`, `data/estimates.json`, `data/roadmap.json`, `data/resource-plan.json`, `data/efficiency.json`, `data/gaps.json`, `data/strategy.json` e os documentos-espinha (`00-discovery-brief.md`, `02-delivery-plan.md`). Não contém valores de investimento — o preço indicativo por trilha está em `outputs/artifacts/estimate-comparison.md`, disponível separadamente sob o gate de precificação validado.*

## Deliverables
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/artifacts/executive-summary.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/`
