# Discovery Brief — PRODESP · Poupatempo Balcão V2 (Slack no guichê + Plataforma Headless)

*Gerado em 21/09/2026 · Scopezilla `discover` · Revisado em 21/09/2026 após reconciliação de escopo (ver `decisions/0002`)*

## Executive summary

PRODESP quer que o Professional Services da Salesforce formalize uma proposta de serviço para colocar o Slack como posto de trabalho do atendente no balcão do Poupatempo — não para a cidadã, que já usa WhatsApp e o Portal (Poupinha) para o atendimento simples, mas para o atendente, quando o caso foge do script (uma digital que não captura, um documento divergente, um sistema fora do ar). O pedido interno de proposta veio da AE Juliana Brites em 09/09/2026 e foi reforçado em 17/09; ainda não existe SOW, registro comercial, cronograma nem preço. Duas visões de design chegaram na mesma semana de setembro: um recorte tático ("Slack no guichê", semanas, sem integração pesada) e uma visão de plataforma inteira (Headless, cronograma e preço em branco). **Decisão de escopo (revisada, `decisions/0002`): os dois cortes entram, completos, nesta mesma SOW, faseados** — Fase 1 é o recorte tático (Corte 1/Jackson); Fase 2 é a plataforma Headless completa (Corte 2/Vinicius: pré-atendimento WhatsApp, validação remota de documentos, atendimento agentic 24/7 com human-in-the-loop, integração MuleSoft a gov.br/biometria/legado). Nenhum dos dois cortes tem cronograma ou preço definidos ainda — isso permanece aberto.

## Company and industry context

PRODESP é a empresa de TI do Governo do Estado de São Paulo, operadora do Poupatempo — a rede de atendimento presencial e digital ao cidadão paulista (244–246 unidades físicas, "totens" incluídos). Em 2024 a rede registrou ~45 milhões de atendimentos presenciais e ~76 milhões de interações digitais; de janeiro a setembro de 2025, ~13 milhões de presenciais e ~54,8 milhões de digitais (fonte pública: Agência SP). É um caso clássico de setor público digitalizado: o canal digital (WhatsApp/Portal, apelidado "Poupinha") já absorve a maior parte da demanda simples — no recorte medido de 1 a 7 de julho de 2026, ~20 mil conversas/dia, 15,1% de autoatendimento completo, NPS 82,24%. O que sobra no balcão físico é o caso que a triagem digital não resolve: falha biométrica, documento divergente, sistema do Detran fora do ar.

## Current vs. target Salesforce landscape

**Já na casa hoje:**
- **Slack Enterprise Plus** — 1.800 usuários já validados (15–16/07/2026) para monitoramento de canais digitais (Sala de Situação). Este número dimensiona aquela frente, não a folha de atendentes do guichê.
- **Agentforce / Flex Credits** — já em consumo na conta: ~125,8 milhões de créditos Flex a cada 90 dias (Digital Wallet, 17/07/2026), pago conforme o uso. Uma fala não confirmada no comitê interno (09/09) descreveu o Flex da conta como "ilimitado" — tratada aqui como hipótese, não fato da Wallet.
- **WhatsApp / e-mail / push (Message Credits)** — já pré-pagos: 4,9 bilhões de créditos WhatsApp, 150 milhões de e-mail, 10 milhões de push, todos válidos até 13/05/2027 (contrato 05608946). Consumo hoje é quase ocioso.
- **MuleSoft e Data 360** — já contratados na conta, hoje quase não usados por este recorte específico.

**Alvo — Fase 1 (tático, Corte 1/Jackson, `decisions/0002`):** o atendente passa a trabalhar dentro do Slack — canais por serviço, Canvas fixado com a regra vigente, huddle com especialista sem sair da cadeira, roteamento de casos para postos com capacidade ociosa, workflow de aviso quando um sistema cai. Nenhuma integração pesada nova; roda sobre a capacidade Slack/Agentforce já validada.

**Alvo — Fase 2 (plataforma completa, Corte 2/Vinicius, `decisions/0002` — escopo contratado desta mesma SOW, não visão solta):** a cidadã recebe convite de pré-atendimento pelo WhatsApp antes do dia marcado, um atendente ocioso valida documentos à distância pelo Slack, um agente de IA atende 24/7 pelo WhatsApp com supervisão humana (human-in-the-loop), e o MuleSoft liga tudo isso a gov.br, biometria estadual e o legado da Prodesp (Sistema Semântico, "Atendimento", T7 — identidades ainda abertas, ver Open Questions). Cronograma e investimento continuam em branco no próprio deck que descreve essa visão — a sequência dentro do contrato (Fase 1 → Fase 2) e o preço permanecem abertos, mas o **escopo** de Fase 2 está confirmado como parte desta SOW, não como pitch futuro separado.

## Project scope and objectives

Escopo desta SOW (revisado, `decisions/0002`): **os dois cortes, completos, faseados no mesmo contrato.**

- **Fase 1 (tática):** desenho de um piloto num posto ainda não escolhido, cobrindo canais Slack por serviço, Canvas de atendimento, escalonamento por huddle, balanceamento de capacidade entre postos e workflow de contingência quando um sistema cai. Governança e adoção (papéis, treinamento, política de canais) foram explicitamente confirmadas como dentro do escopo pelo usuário nesta sessão.
- **Fase 2 (plataforma completa):** pré-atendimento da cidadã pelo WhatsApp antes do dia marcado, validação remota de documentos por atendente ocioso via Slack, atendimento agentic 24/7 com human-in-the-loop, e integração MuleSoft a gov.br, biometria estadual e legado Prodesp.

Objetivos de negócio citados pela fonte: reduzir o tempo do "preciso de ajuda" até a cidadã saída atendida (hoje: horas ou "volte depois"); acabar com a coordenação entre postos por grupos de WhatsApp pessoal (sem histórico, fora da LGPD); dar visibilidade de capacidade ociosa entre postos sem contratar gente nova; e, na Fase 2, resolver o caso simples inteiramente antes do cidadão chegar ao balcão.

**Não mais fora de escopo:** a Fase 2 deixou de ser vision-only (posição anterior em `decisions/0001`, superseded) e passou a ser escopo contratado desta mesma SOW, por decisão direta do usuário nesta sessão — ver `decisions/0002`.

## Data and compliance considerations

A LGPD é um driver de design de primeira ordem, não um item de rodapé: a própria fonte descreve a coordenação atual entre postos, feita em grupos pessoais de WhatsApp, como "fora da LGPD" — sem histórico institucional, sem auditoria. A proposta de valor central da Fase 1 é justamente migrar essa coordenação para canais Slack institucionais, auditáveis e dentro do ambiente da Prodesp. O material também registra a intenção de que nenhum dado biométrico bruto trafegue nos canais de texto do Slack (apenas o relato textual do problema) — uma premissa de design a validar, não um controle já implementado.

O usuário confirmou nesta sessão que já existe um posicionamento externo do time de conta sobre onde o processamento/inferência do Agentforce ocorre (relevante para uma eventual pergunta de residência de dados). Nenhum documento ou URL específico foi indicado até o momento — este item permanece uma referência a obter, não uma citação verificável, e não deve ser tratado como fonte 🟢 até que o documento real seja localizado. Ver Open Questions.

## Research findings and market context

Não há, publicamente, um caso de referência direto de "Slack + Agentforce num balcão de atendimento presencial de setor público na América Latina" — esta seria, na prática, uma referência pioneira (first-of-kind), o que pesa tanto no risco de execução quanto na conversa de precificação (menos ancoragem comparável, mais trabalho de calibração no piloto). Pesquisa web dedicada (21/09/2026) não encontrou nenhum caso Agentforce/Salesforce específico do Brasil ou LATAM em governo, nem relatório de analista (Gartner/Forrester/McKinsey) — a perna regional e a perna de validação por analista do business case seguem finas. Posicionar como **first-mover/diferenciação**, não como "padrão já provado na região".

Os casos citados no próprio material de venda (Nubank, Nutanix, Salesforce Support, Sammons Financial Group) são histórias de cliente já publicadas pela Salesforce — evidência direcional de que "Slack como hub único + IA no canal" reduz MTTR e tempo de rampa de novato, mas nenhuma é do setor público nem de atendimento presencial com fila física; servem como analogia de mecanismo, não como prova para este caso.

**Casos análogos mais fortes (achados na pesquisa web, mais próximos do use case real deste projeto):**
- **Texas Department of Public Safety** — agente Agentforce ("Agent Sheri") para dúvidas de CNH/ID por chat e voz, grounded em Service Cloud/Data 360, com handoff para atendente humano: +105% de cidadãos atendidos ano a ano, 5.000 chats na primeira semana, implementado em 90 dias (vs. 25.000 ligações/dia e esperas de até 35 min antes). **Analogia direta de use case** (CNH/documento de identidade). Fonte: salesforce.com/customer-stories/texas-dps.
- **Thames Valley Police & Hampshire/IoW Constabulary** — agente Agentforce ("Bobbi") resolve autonomamente 75% de 200+ conversas não-emergenciais/dia, triando casos de risco para humanos, com portal do cidadão via MuleSoft: £1,4M de economia, 97% menor custo por interação, -10% no volume de chamadas. **Analogia direta de arquitetura** (Agentforce + MuleSoft + triagem IA com escalonamento humano — o padrão da Fase 2). Fonte: salesforce.com/customer-stories/tvp-and-hiowc.
- **Defense Digital Service** usa Slack Connect (FedRAMP Moderate) para coordenação auditável com parceiros externos, substituindo threads de e-mail — analogia para a substituição da coordenação por WhatsApp pessoal por canais Slack institucionais (Fase 1). Fonte: slack.com/customer-stories/defense-digital-service-government-teamwork.
- **FIFA** escalona operações de rewards encaminhando conversas Slack com contexto completo para um canal de gestor, com Slack Enterprise Search puxando registros Salesforce vinculados — analogia funcional direta do "transbordo" da Fase 1. Fonte: salesforce.com/customer-stories/fifa/rewards-recognition-collaboration.

Para a estimativa de consumo, a linha recomendada é bottom-up por Flex Credits (rate card oficial: quinhentos dólares por cada cem mil créditos), não o alvo comercial de um milhão de dólares citado pela Ju Brites em 10/09 — esse valor é meta de licenciamento Slack-Prodesp como um todo, desvinculado deste SOW de serviço.

Os KPIs de tempo médio de espera (15/16/17 minutos, para CNH/CIN/biometria/exame médico) que aparecem no deck de plataforma são, conforme confirmado pelo usuário nesta sessão, **ilustrativos e não validados pelo cliente** — não devem ser apresentados como baseline real em nenhum entregável derivado deste discovery sem essa ressalva explícita.

**Correção de volumetria:** o site oficial do Poupatempo lista **244 unidades físicas + 900 totens de autoatendimento** (não "244–246") — usar esse número; os ~45M presenciais/~76M digitais de 2024 não puderam ser verificados externamente (só achados agregados multi-ano por unidade) — tratar como "a verificar no relatório de transparência interno da Prodesp", não citar externamente sem essa ressalva.

**LGPD e IA — achados de pesquisa (21/09/2026):**
- O Art. 20 da LGPD (direito a revisão de decisão automatizada) se aplica estritamente a decisões tomadas **unicamente** com base em tratamento automatizado. Como o desenho de Agentforce em ambas as fases é assistivo (humano no loop, nunca decisão 100% automática de emissão de CIN/CNH), o projeto tende a ficar fora do gatilho estrito do Art. 20 — mas isso reforça a necessidade de preservar revisão humana genuína (não pro forma) e capacidade de explicar a lógica de roteamento/triagem se questionado. Recomendação: tratar isso como **princípio de arquitetura explícito** da Fase 2 (agentic 24/7), não como nota de rodapé de compliance.
- O PL 2338/2023 (Marco Legal da IA) já passou no Senado e está na Câmara desde 17/03/2025 — ainda não é lei (21/09/2026). É um item para **monitorar**, não um gate ativo hoje; trará exigências de transparência/rotulagem de IA que podem afetar a Fase 2 (atendimento agentic) quando/se virar lei.
- Não foi encontrada orientação pública da ANPD específica sobre biometria, nem diretriz federal (SGD/MGI) ou decreto estadual de SP sobre governança de IA. **Gap de pesquisa, não evidência de ausência** — recomenda-se checagem manual do site da ANPD e puxar a documentação de compliance LGPD/Brasil do time de conta Salesforce antes de qualquer entregável afirmar postura de compliance. Isso reforça (não substitui) o item já aberto sobre o documento de posicionamento LGPD/Trust do Agentforce, abaixo.

**Sinal de cautela institucional (achado de pesquisa, risco de stakeholder/procurement):** a Prodesp está sob escrutínio do TCE-SP (Tribunal de Contas do Estado) num contrato não relacionado (câmeras de vigilância "Muralha Paulista"), tendo rescindido parceria com um fornecedor em junho/2026 em meio a esse escrutínio. Não afeta o mérito deste projeto, mas sinaliza cautela institucional elevada para novos contratos de tecnologia na conta agora — vale monitorar no relacionamento comercial. (Nota: não confundir com o "Poupatempo RJ", operação privada do Rio de Janeiro em disputa judicial por sobre-reporte de volumes — é outro estado, outro operador; útil só como comparação rotulada sobre governança de métricas de SLA, nunca como achado de São Paulo.)

## Open Questions

- **T7 (sistema no diagrama de arquitetura-alvo).** Referenciado como sistema real com agente de IA próprio ("Utiliza agente do T7 algumas dúvidas"), mas sem nome ou sigla expandida em nenhuma fonte acessível. Decisão do usuário nesta sessão: **deprioritizar** — não bloqueia o discovery, mas seria bom fechar antes do desenho técnico da Fase 1.
- **Biometria, Sistema Semântico e "Atendimento"** (caixas do mesmo diagrama de arquitetura-alvo). Confirmadas como sistemas reais, porém sem identidade/produto conhecido. → **pergunta ao cliente**.
- **Escopo real do piloto** — qual posto, quantos atendentes, qual(is) serviço(s). Totalmente aberto; Ana, Anderson, Felipe, Santo Amaro e a CIN são explicitamente storyboard, não um piloto já combinado com a Prodesp.
- **Budget / valor comercial** — sem SOW, sem registro comercial, sem preço. O alvo comercial de um milhão de dólares é de licenciamento Slack, não deste serviço. Gate de precificação: nenhum número deve ser produzido até o cliente fornecer uma rate a validar.
- **Champion / patrocinador executivo da Balcão V2** no lado PRODESP — ainda não identificado claramente (diferente da Frente A de licenças, que tem Thiago Waltz como ponto de entrada).
- **Documento de posicionamento LGPD/Trust sobre localização de inferência do Agentforce** — existência confirmada pelo usuário, mas sem documento/URL específico ainda localizado ou citável. Pesquisa web (21/09/2026) não encontrou orientação pública ANPD/SGD/MGI específica que substitua essa necessidade — recomenda-se puxar do time de conta antes de qualquer afirmação de compliance em entregável.
- **Gap de dimensionamento de licenças Slack** — 1.800 licenças Slack Enterprise Plus já validadas cobrem a Sala de Situação (monitoramento de canais digitais), não o headcount real de atendentes nos 244 postos + 900 totens. Confirmado pelo usuário nesta sessão: esse número ainda não foi dimensionado com o cliente. Relevante para `requirements`/`estimate` de ambas as fases, mas principalmente Fase 1 (adoção no guichê).
- **Owner de governança de agentes de IA do lado Prodesp** — confirmado pelo usuário nesta sessão como ainda não identificado. Mais crítico agora que a Fase 2 (atendimento agentic 24/7) é escopo confirmado, não visão — ver `knowledge/latam-agentic-governance-services.md` para a pauta de discovery de governança a usar quando esse owner for identificado.

## Deliverables

- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/decisions/0001-phase1-tactical-vs-phase2-whole-house.md` (superseded)
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/decisions/0002-both-cuts-in-scope-phased.md` (current)
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/00-discovery-brief.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/`
