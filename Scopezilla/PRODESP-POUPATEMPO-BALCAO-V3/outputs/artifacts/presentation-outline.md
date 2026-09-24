# Outline de Apresentação — PRODESP · Poupatempo Balcão V3

**Objetivo (True Goal):** aprovar a Fase 0 (fechamento de gaps) e o formato geral do programa.
**Audiência:** mista, executiva + técnica — mesma audiência do executive-summary.md.
**Fluência assumida:** parcialmente fluente — nomes de produto diretos, padrões internos explicados na primeira menção.
**Big Idea:** duas jornadas complementares rodam sobre a mesma arquitetura Salesforce — WhatsApp antecipa o atendimento do cidadão, Slack conduz o atendente.
**Arco:** Resposta → Por quê → Como → Prova. **Tom:** Autoritativo.

**Nomes de produto travados nesta apresentação:** Slack, Service Cloud, Agentforce, MuleSoft, Data 360, Tableau Next.

**Nota de sweep de jargão interno:** todo ID interno do Scopezilla (código de épico E0X, código de gap G0XXX, código de papel R0X/C0X) foi traduzido para linguagem simples no conteúdo voltado à audiência. Os IDs aparecem só na coluna "Fonte de Dados" abaixo, para rastreabilidade de produção — nunca no slide em si. Avise se preferir manter algum código visível (ex.: para uma sessão técnica de arquitetura que já conhece a nomenclatura do projeto).

Nenhum valor de investimento, hora ou headcount aparece em nenhum slide — apenas T-shirt sizes, contagem de fases/épicos/riscos/gaps e formato de time (papéis, não FTE).

---

## Slide 1 — Capa

**Reason for Existence:** contexto mínimo antes da audiência entrar no conteúdo.

**Content:**
- PRODESP · Poupatempo Balcão V3
- Aprovação de Fase 0 e Formato do Programa
- Data da apresentação · Conta: Prodesp - Empresa de TI do Estado de São Paulo

**Visual Concept:** slide de título, lockup co-brand PRODESP, sem elementos decorativos adicionais.
**Density:** sparse.
**Data Source:** `.project-metadata.json` (project_name, account_name).

**Speaker Notes:** Abrir nomeando o objetivo da reunião — decidir sobre a Fase 0 e o formato do programa, não apresentar um catálogo de funcionalidades. Transição: "vou começar já pela recomendação."

---

## Slide 2 — Uma arquitetura Salesforce sustenta as duas jornadas do programa: antecipação por WhatsApp, atendimento por Slack

**Reason for Existence:** Resposta do arco — a recomendação value-first, antes de qualquer detalhe, para uma audiência sênior que não precisa ser conduzida até a conclusão.

**Content:**
- Jornada 1 — antecipação digital: o cidadão recebe oferta de atendimento antecipado por WhatsApp quando um atendente fica disponível antes do agendamento.
- Jornada 2 — apoio presencial: o atendente resolve bloqueios no balcão apoiado por um assistente no Slack, sem trocar de tela.
- As duas jornadas compartilham a mesma base: roteamento nativo de presença, MuleSoft para os sistemas legados, Agentforce e Data 360 para o conhecimento que alimenta o atendente.

**Visual Concept:** diagrama hub-and-spoke — Salesforce no centro, as duas jornadas como ramos que convergem na mesma base de dados e roteamento.
**Density:** balanced.
**Data Source:** `outputs/01-solution.md`; executive-summary.md, seção "Visão Geral em 5 Pontos".

**Speaker Notes:** Esta é a resposta à pergunta que trouxe todos à sala. Não é um projeto de duas frentes separadas — é uma arquitetura, duas jornadas. Enfatizar que essa unificação é o que torna o programa mais barato de manter do que dois projetos isolados. Transição: "antes de entrar em como chegamos aqui, vale nomear a dor que isso resolve."

---

## Slide 3 — O atendente fica ocioso enquanto a fila de agendamentos futuros já teria demanda para preencher esse tempo

**Reason for Existence:** Por quê (1/2) — funda a audiência executiva na dor operacional antes de qualquer decisão de arquitetura.

**Content:**
- Hoje, um agendamento futuro só é atendido na data marcada, mesmo com atendente disponível antes disso.
- A fila de atendimento imediato às vezes está vazia enquanto atendentes ficam ociosos.
- Resultado: capacidade de atendimento desperdiçada nos dois lados, sem um mecanismo que os conecte.

**Visual Concept:** diagrama único mostrando a lacuna — uma linha do tempo com "atendente livre" e "próximo agendamento" desalinhados, com o espaço vazio entre eles destacado.
**Density:** sparse.
**Data Source:** executive-summary.md, seção "Visão Geral".

**Speaker Notes:** Manter curto — esta é a dor, não a solução. Se alguém perguntar "por que isso importa financeiramente", redirecionar para o resumo executivo (a apresentação não carrega números de investimento). Transição: "resolver essa lacuna com confiança total exige fechar quatro pontos em aberto primeiro."

---

## Slide 4 — Quatro dos sete blocos de escopo ainda têm dimensionamento Unknown sob um contrato Fixed Fee

**Reason for Existence:** Por quê (2/2) — nomeia o risco estrutural (Fixed Fee sobre escopo incerto) que torna a Fase 0 necessária, não opcional.

**Content:**
- Integração com os sistemas legados — depende de confirmar se são dois sistemas realmente separados ou um único produto com dois alvos.
- Serviço de seleção de antecipação — depende de regras de elegibilidade e prioridade que o cliente ainda não definiu.
- Autoprovisionamento de atendentes — depende de identificar o sistema de RH da PRODESP e se ele expõe API.
- Base de conhecimento e IA no assistente do Slack — depende de definir a relação com o agente do canal de atendimento existente (T7).
- 57 pontos em aberto no total, bem acima do limite de 15 que já justificaria uma fase de destravamento formal.

**Visual Concept:** tabela de 7 linhas (um bloco de escopo por linha), coluna de tamanho (T-shirt) e coluna de confiança — os 4 marcados como Unknown visualmente destacados.
**Density:** balanced.
**Data Source:** executive-summary.md, "Resumo do Escopo"; `data/gaps.json` (G0309, G0401, G0501/G0508, G0703 — não exibidos no slide).

**Speaker Notes:** Esse é o slide que justifica pedir a Fase 0 em vez de já travar cronograma. Nomear que cada um dos quatro pontos tem um dono claro do lado do cliente — não é vagueza nossa, é informação que só eles têm. Se a audiência perguntar "quanto isso muda o preço", a resposta correta é que ainda não sabemos — é exatamente por isso que a Fase 0 vem primeiro. Transição: "a arquitetura que já definimos para o resto do escopo é sólida — veja como."

---

## Slide 5 — O atendente passa a operar 100% dentro do Slack, apoiado por uma ponte já validada em prova de conceito com o cliente

**Reason for Existence:** Como (1/3) — leva a substância técnica para a metade arquitetural da sala; é a decisão mais visível desta rodada de revisão.

**Content:**
- O atendente conduz toda a interação — canal pessoal, thread por caso — sem alternar para a tela de atendimento padrão.
- O gatilho da antecipação é uma mudança de status de disponibilidade do atendente, não uma automação customizada monitorando a fila.
- Os dois sistemas legados (o do cidadão e o do atendente) são plataformas distintas — confirmado pelo responsável da conta.
- Consequência direta: o autoprovisionamento de atendentes cresceu de escopo médio para grande, porque agora inclui criar esse canal pessoal.

**Visual Concept:** diagrama de arquitetura em camadas — status de presença → ponte de integração → canal do Slack — com no máximo 6 caixas.
**Density:** dense.
**Data Source:** `outputs/01-solution.md`; executive-summary.md, "Destaques da Solução".

**Speaker Notes:** Este é o slide para a plateia técnica — ir no ritmo certo, sem pressa. A frase-chave é "configuração nativa em vez de automação customizada": menos código, menos risco de manutenção. Nomear o PoC como prova, não como promessa. Transição: "essas decisões técnicas se encaixam num plano de cinco fases."

---

## Slide 6 — A Fase 0 fecha os gaps que hoje bloqueiam o dimensionamento das quatro fases seguintes

**Reason for Existence:** Como (2/3) — mostra o plano de execução e situa a Fase 0 como o pedido imediato, não uma etapa qualquer entre outras.

**Content:**
- Fase 0 — sem escopo de entrega, só fechamento dos pontos em aberto do slide 4.
- Fase 1 — Fundação: integração com os dois legados + provisionamento de atendentes.
- Fase 2 — Jornada de antecipação digital.
- Fase 3 — Jornada de apoio presencial + base de conhecimento.
- Fase 4 — Observabilidade e relatórios executivos.
- Caminho crítico: Fundação → Antecipação Digital → Observabilidade. Faixa indicativa de duração (lane Aumentada, sem cronograma comprometido): 15 a 34 semanas.

**Visual Concept:** timeline horizontal de 5 fases, caminho crítico destacado com uma cor diferente das fases em paralelo.
**Density:** balanced.
**Data Source:** `outputs/02-delivery-plan.md`; `data/commercials.json` (`effort_basis.duration_weeks_range`).

**Speaker Notes:** Deixar claro que a faixa de semanas é indicativa, não um compromisso de prazo — isso é papel do resumo executivo, não desta apresentação. Se perguntarem por que a Fase 0 não tem semanas na faixa, explicar que o tamanho da Fase 0 depende de quão rápido o cliente resolve os quatro pontos do slide 4. Transição: "esse plano precisa de um time — sem entrar em números de pessoas."

---

## Slide 7 — Dez papéis de Salesforce PS compõem o time, incluindo disciplinas dedicadas de Design de Experiência e de Change & Adoption

**Reason for Existence:** Como (3/3) — nomeia o formato do time e os dois sinais de disciplina que evitam retrabalho, sem expor contagem de pessoas.

**Content:**
- Design de Experiência — cobre a jornada do cidadão no WhatsApp; sem esse trabalho, o risco é retrabalho depois que o cidadão já estiver usando o canal em produção.
- Change & Adoption — cobre a mudança de rotina dos atendentes (autodeclaração de disponibilidade + migração do atendimento para o Slack); sem esse trabalho, o risco é a solução funcionar tecnicamente e não ser adotada como desenhada.
- Do lado do cliente: um responsável pela decisão do projeto ainda não foi nomeado, e o acesso a sistemas internos ainda não foi confirmado.

**Visual Concept:** fileira de chips de categoria — um chip por disciplina do time, com a justificativa ao lado (padrão "category-chip row").
**Density:** balanced.
**Data Source:** executive-summary.md, "Resumo de Esforço"; `data/resource-plan.json` (papéis, sem contagem exibida).

**Speaker Notes:** Se perguntarem "quantas pessoas", a resposta é que o formato do time está definido, mas a contagem exata acompanha a validação comercial — não é o assunto desta reunião. O ponto que precisa aterrissar é que as duas disciplinas citadas não são custo extra, são prevenção de retrabalho. Transição: "antes de pedir aprovação, é justo mostrar onde a arquitetura já foi testada e onde ainda há risco aberto."

---

## Slide 8 — O PoC da ponte entre a plataforma e o Slack já foi validado com o cliente; falta confirmar qual mecanismo real de entrega ele usa

**Reason for Existence:** Prova (1/2) — evidência técnica que sustenta a aposta arquitetural do slide 5, com honestidade sobre o que falta confirmar.

**Content:**
- O PoC prova que a experiência 100%-Slack para o atendente funciona tecnicamente.
- Ponto ainda aberto: se o mecanismo real é baseado em gatilho (limite mais alto) ou em monitoramento contínuo (limite bem mais restritivo) — a diferença muda o teto de quantas antecipações a solução aguenta por dia.
- Confirmar isso com o time que já validou o PoC resolve o risco antes que ele apareça em produção.

**Visual Concept:** estatística única em destaque ("PoC validado") com uma nota de risco abaixo, sem gráfico.
**Density:** sparse.
**Data Source:** executive-summary.md, "Destaques da Solução" e "Riscos e Mitigações" (risco de limite de plataforma).

**Speaker Notes:** Esse é o slide mais tranquilizador da apresentação — usar como respiro entre o slide de arquitetura densa e o de riscos. Não minimizar o ponto aberto: é pequeno, mas real, e nomeá-lo aqui evita que pareça escondido depois. Transição: "esse é um risco entre catorze — vale ver o quadro completo antes do pedido final."

---

## Slide 9 — Dos catorze riscos mapeados, o Fixed Fee sobre escopo incerto é o único sem mitigação de escopo disponível

**Reason for Existence:** Prova (2/2) — honestidade de risco antes do pedido; constrói credibilidade com a audiência executiva.

**Content:**
- Risco de maior peso: preço fechado sobre um escopo em que mais da metade dos blocos ainda tem dimensionamento incerto — a única saída é fechar os pontos abertos do slide 4, não um ajuste de escopo.
- Dois pontos no caminho crítico só o cliente resolve: regras de seleção de antecipação, e identificação do sistema de RH.
- Proteção de dados pessoais (WhatsApp, identidade digital, biometria) ainda sem decisão de arquitetura — recomendação é levar à conversa comercial antes do fechamento, não deixar para o design detalhado.
- Riscos aceitos deliberadamente, sem mitigação ativa: ausência de responsável nomeado para a fase de observabilidade; governança de dados de RH; governança de conteúdo da base de conhecimento.

**Visual Concept:** tabela de risco — 4 a 5 linhas, colunas "risco" / "por que importa" / "quem resolve" — a linha do Fixed Fee em destaque.
**Density:** dense.
**Data Source:** executive-summary.md, "Riscos e Mitigações".

**Speaker Notes:** Não suavizar o risco do Fixed Fee — é o argumento mais forte a favor de aprovar a Fase 0 hoje em vez de travar tudo agora. A proteção de dados pessoais merece uma frase à parte: é uma decisão comercial, não um detalhe de design. Transição: "isso leva direto ao que estamos pedindo hoje."

---

## Slide 10 — O primeiro passo é nomear o responsável do cliente pela decisão do projeto e aprovar a Fase 0

**Reason for Existence:** O pedido — fecha o arco no objetivo verdadeiro da apresentação.

**Content:**
- Nomear, do lado do cliente, quem tem autoridade de decisão e disponibilidade definida para a Fase 0.
- Aprovar a Fase 0 antes de travar cronograma e time — ela revalida os quatro dimensionamentos incertos.
- Levar a decisão de proteção de dados pessoais à conversa comercial, não ao design detalhado.
- Confirmar com o time que validou o PoC qual mecanismo real sustenta a ponte com o Slack.

**Visual Concept:** lista numerada, coluna única, sem decoração.
**Density:** sparse.
**Data Source:** executive-summary.md, "Próximos Passos e Recomendações".

**Speaker Notes:** Terminar aqui, sem slide de "perguntas" — a pergunta natural já é a decisão pedida. Se a sala hesitar na aprovação da Fase 0, oferecer a alternativa concreta: T&M só para a Fase 0, escopo fechado só depois dela. Não empurrar para uma resposta na própria reunião se não vier naturalmente.

---

## Resumo dos sweeps da Fase 5

- **Jargão interno:** IDs de épico/gap/papel/cliente removidos do conteúdo voltado à audiência; mantidos só na coluna Fonte de Dados. "Change & Adoption" mantido como nome de disciplina (não é sigla interna, é nome de função reconhecível).
- **Alucinação:** todo número citado (10 papéis, 4 de 7 blocos Unknown, 57 gaps, 14 riscos, 5 fases, faixa de 15-34 semanas) rastreia a um arquivo `data/*.json` ou a `executive-summary.md`. Nenhum número novo foi introduzido nesta apresentação.
- **AI-tells / tom de vendas:** títulos revisados para uma afirmação só por slide, sem em-dash, sem paralelismo negativo, sem itens de jargão/tom de vendas da lista de `prose-style.md`.
- **Padrões visuais/estruturais:** nenhuma tríade forçada (a lista de 3 decisões no slide 5 é contagem real da fonte, não decorativa); nenhuma simetria de colunas forçada; nenhum ícone/gradiente decorativo especificado.
