# Discovery Brief — PRODESP · Poupatempo Balcão V2 (Slack no guichê)

*Gerado em 21/09/2026 · Scopezilla `discover`*

## Executive summary

PRODESP quer que o Professional Services da Salesforce formalize uma proposta de serviço para colocar o Slack como posto de trabalho do atendente no balcão do Poupatempo — não para a cidadã, que já usa WhatsApp e o Portal (Poupinha) para o atendimento simples, mas para o atendente, quando o caso foge do script (uma digital que não captura, um documento divergente, um sistema fora do ar). O pedido interno de proposta veio da AE Juliana Brites em 09/09/2026 e foi reforçado em 17/09; ainda não existe SOW, registro comercial, cronograma nem preço. Duas visões de design chegaram na mesma semana de setembro: um recorte tático ("Slack no guichê", semanas, sem integração pesada) e uma visão de plataforma inteira (Headless, cronograma e preço em branco). Este discovery escopa apenas o primeiro (ver `decisions/0001`).

## Company and industry context

PRODESP é a empresa de TI do Governo do Estado de São Paulo, operadora do Poupatempo — a rede de atendimento presencial e digital ao cidadão paulista (244–246 unidades físicas, "totens" incluídos). Em 2024 a rede registrou ~45 milhões de atendimentos presenciais e ~76 milhões de interações digitais; de janeiro a setembro de 2025, ~13 milhões de presenciais e ~54,8 milhões de digitais (fonte pública: Agência SP). É um caso clássico de setor público digitalizado: o canal digital (WhatsApp/Portal, apelidado "Poupinha") já absorve a maior parte da demanda simples — no recorte medido de 1 a 7 de julho de 2026, ~20 mil conversas/dia, 15,1% de autoatendimento completo, NPS 82,24%. O que sobra no balcão físico é o caso que a triagem digital não resolve: falha biométrica, documento divergente, sistema do Detran fora do ar.

## Current vs. target Salesforce landscape

**Já na casa hoje:**
- **Slack Enterprise Plus** — 1.800 usuários já validados (15–16/07/2026) para monitoramento de canais digitais (Sala de Situação). Este número dimensiona aquela frente, não a folha de atendentes do guichê.
- **Agentforce / Flex Credits** — já em consumo na conta: ~125,8 milhões de créditos Flex a cada 90 dias (Digital Wallet, 17/07/2026), pago conforme o uso. Uma fala não confirmada no comitê interno (09/09) descreveu o Flex da conta como "ilimitado" — tratada aqui como hipótese, não fato da Wallet.
- **WhatsApp / e-mail / push (Message Credits)** — já pré-pagos: 4,9 bilhões de créditos WhatsApp, 150 milhões de e-mail, 10 milhões de push, todos válidos até 13/05/2027 (contrato 05608946). Consumo hoje é quase ocioso.
- **MuleSoft e Data 360** — já contratados na conta, hoje quase não usados por este recorte específico.

**Alvo — Fase 1 (tático, este SOW, decisions/0001):** o atendente passa a trabalhar dentro do Slack — canais por serviço, Canvas fixado com a regra vigente, huddle com especialista sem sair da cadeira, roteamento de casos para postos com capacidade ociosa, workflow de aviso quando um sistema cai. Nenhuma integração pesada nova; roda sobre a capacidade Slack/Agentforce já validada.

**Alvo — Fase 2+ (visão, fora deste SOW):** plataforma "Headless 360" — a cidadã recebe convite de pré-atendimento pelo WhatsApp antes do dia marcado, um atendente ocioso valida documentos à distância pelo Slack, um agente de IA atende 24/7 pelo WhatsApp com supervisão humana (human-in-the-loop), e o MuleSoft liga tudo isso a gov.br, biometria estadual e o legado da Prodesp. Cronograma e investimento continuam em branco no próprio deck que descreve essa visão — não é escopo contratável hoje.

## Project scope and objectives

Escopo deste ciclo de discovery: a Fase 1 tática — desenho de um piloto num posto ainda não escolhido, cobrindo canais Slack por serviço, Canvas de atendimento, escalonamento por huddle, balanceamento de capacidade entre postos e workflow de contingência quando um sistema cai. Governança e adoção (papéis, treinamento, política de canais) foram explicitamente confirmadas como dentro do escopo pelo usuário nesta sessão.

Objetivos de negócio citados pela fonte: reduzir o tempo do "preciso de ajuda" até a cidadã saída atendida (hoje: horas ou "volte depois"); acabar com a coordenação entre postos por grupos de WhatsApp pessoal (sem histórico, fora da LGPD); dar visibilidade de capacidade ociosa entre postos sem contratar gente nova.

Explicitamente fora deste ciclo: a Fase 2+ (integração MuleSoft a gov.br/biometria, jornadas de pré-atendimento no WhatsApp da cidadã, atendimento agêntico 24/7) — ver `decisions/0001`.

## Data and compliance considerations

A LGPD é um driver de design de primeira ordem, não um item de rodapé: a própria fonte descreve a coordenação atual entre postos, feita em grupos pessoais de WhatsApp, como "fora da LGPD" — sem histórico institucional, sem auditoria. A proposta de valor central da Fase 1 é justamente migrar essa coordenação para canais Slack institucionais, auditáveis e dentro do ambiente da Prodesp. O material também registra a intenção de que nenhum dado biométrico bruto trafegue nos canais de texto do Slack (apenas o relato textual do problema) — uma premissa de design a validar, não um controle já implementado.

O usuário confirmou nesta sessão que já existe um posicionamento externo do time de conta sobre onde o processamento/inferência do Agentforce ocorre (relevante para uma eventual pergunta de residência de dados). Nenhum documento ou URL específico foi indicado até o momento — este item permanece uma referência a obter, não uma citação verificável, e não deve ser tratado como fonte 🟢 até que o documento real seja localizado. Ver Open Questions.

## Research findings and market context

Não há, publicamente, um caso de referência direto de "Slack + Agentforce num balcão de atendimento presencial de setor público na América Latina" — esta seria, na prática, uma referência pioneira (first-of-kind), o que pesa tanto no risco de execução quanto na conversa de precificação (menos ancoragem comparável, mais trabalho de calibração no piloto).

Os casos citados no próprio material de venda (Nubank, Nutanix, Salesforce Support, Sammons Financial Group) são histórias de cliente já publicadas pela Salesforce — evidência direcional de que "Slack como hub único + IA no canal" reduz MTTR e tempo de rampa de novato, mas nenhuma é do setor público nem de atendimento presencial com fila física; servem como analogia de mecanismo, não como prova para este caso.

Para a estimativa de consumo, a linha recomendada é bottom-up por Flex Credits (rate card oficial: quinhentos dólares por cada cem mil créditos), não o alvo comercial de um milhão de dólares citado pela Ju Brites em 10/09 — esse valor é meta de licenciamento Slack-Prodesp como um todo, desvinculado deste SOW de serviço (ver `decisions/0001`).

Os KPIs de tempo médio de espera (15/16/17 minutos, para CNH/CIN/biometria/exame médico) que aparecem no deck de plataforma são, conforme confirmado pelo usuário nesta sessão, **ilustrativos e não validados pelo cliente** — não devem ser apresentados como baseline real em nenhum entregável derivado deste discovery sem essa ressalva explícita.

## Open Questions

- **T7 (sistema no diagrama de arquitetura-alvo).** Referenciado como sistema real com agente de IA próprio ("Utiliza agente do T7 algumas dúvidas"), mas sem nome ou sigla expandida em nenhuma fonte acessível. Decisão do usuário nesta sessão: **deprioritizar** — não bloqueia o discovery, mas seria bom fechar antes do desenho técnico da Fase 1.
- **Biometria, Sistema Semântico e "Atendimento"** (caixas do mesmo diagrama de arquitetura-alvo). Confirmadas como sistemas reais, porém sem identidade/produto conhecido. → **pergunta ao cliente**.
- **Escopo real do piloto** — qual posto, quantos atendentes, qual(is) serviço(s). Totalmente aberto; Ana, Anderson, Felipe, Santo Amaro e a CIN são explicitamente storyboard, não um piloto já combinado com a Prodesp.
- **Budget / valor comercial** — sem SOW, sem registro comercial, sem preço. O alvo comercial de um milhão de dólares é de licenciamento Slack, não deste serviço. Gate de precificação: nenhum número deve ser produzido até o cliente fornecer uma rate a validar.
- **Champion / patrocinador executivo da Balcão V2** no lado PRODESP — ainda não identificado claramente (diferente da Frente A de licenças, que tem Thiago Waltz como ponto de entrada).
- **Documento de posicionamento LGPD/Trust sobre localização de inferência do Agentforce** — existência confirmada pelo usuário, mas sem documento/URL específico ainda localizado ou citável.

## Deliverables

- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/decisions/0001-phase1-tactical-vs-phase2-whole-house.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/00-discovery-brief.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/`
