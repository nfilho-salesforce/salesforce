# Prompts Gemini (Google Slides) — PRODESP · Poupatempo Balcão V3

Gerado a partir de `presentation-outline.md` (aprovado). Um prompt por slide, pronto para colar no painel do Gemini dentro do Google Slides ("help me create"), um de cada vez, em um slide de template em branco.

**Antes de rodar qualquer prompt:** mova a apresentação para uma pasta do Drive sem PDFs ou decks anteriores por perto (o Gemini usa arquivos vizinhos como contexto), desanexe qualquer arquivo-fonte da apresentação, e comece cada prompt num slide de template em branco — não numa cópia de um slide já estilizado.

**Regra fixa em todos os prompts:** a redação é final (usar cada linha exatamente como está); o layout é o Gemini quem constrói (caixas de texto, formas e tabelas); o fundo/logo/rodapé do template não muda — só o que for adicionado recebe o tema.

---

## Prompt 1 — Capa

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: PRODESP · Poupatempo Balcão V3
SUBTITLE: Aprovação de Fase 0 e Formato do Programa

LAYOUT: Slide de título, centralizado, sem elementos decorativos adicionais.

FOOTER (small, muted italic): Prodesp - Empresa de TI do Estado de São Paulo · 24 de setembro de 2026

Use the template's heading style for TITLE, subheading style for SUBTITLE.
```

---

## Prompt 2 — A resposta

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: Uma arquitetura Salesforce sustenta as duas jornadas do programa
SUBTITLE: Antecipação por WhatsApp, atendimento por Slack — mesma base por trás das duas.

LAYOUT: Hub-and-spoke — Salesforce ao centro, as duas jornadas como ramos que convergem na mesma base de dados e roteamento.

JORNADA 1 — Antecipação Digital
- Cidadão recebe oferta de atendimento antecipado por WhatsApp
- Gatilho: atendente fica disponível antes do agendamento

JORNADA 2 — Apoio Presencial
- Atendente resolve bloqueios no balcão apoiado por assistente no Slack
- Sem trocar de tela durante o atendimento

BASE COMPARTILHADA (caixa central do hub)
- Roteamento nativo de presença
- MuleSoft para os sistemas legados
- Agentforce e Data 360 para o conhecimento do atendente

Use the template's heading style for TITLE. Block headers bold. Body style for bullets.
```

---

## Prompt 3 — A dor

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: O atendente fica ocioso enquanto agendamentos futuros já teriam demanda para preencher esse tempo
SUBTITLE: A lacuna que a Jornada 1 resolve.

LAYOUT: Linha do tempo única, horizontal, mostrando "Atendente livre" e "Próximo agendamento" desalinhados no tempo, com o espaço vazio entre os dois pontos destacado visualmente (cor de alerta ou hachura). Três bullets abaixo da linha do tempo.

A LACUNA
- Agendamento futuro só é atendido na data marcada, mesmo com atendente disponível antes
- Fila de atendimento imediato às vezes está vazia enquanto atendentes ficam ociosos
- Capacidade de atendimento desperdiçada nos dois lados

Use the template's heading style for TITLE. Body style for bullets.
```

---

## Prompt 4 — O risco estrutural (tabela)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: Quatro dos sete blocos de escopo ainda têm dimensionamento Unknown sob um contrato Fixed Fee
SUBTITLE: 57 pontos em aberto no total — acima do limite de 15 que já justificaria uma Fase 0 formal.

LAYOUT: Render this as an actual table object — or a card/tile grid if that lays out more cleanly — not a text box with bolded headers and pipe characters. Each field below goes in its OWN cell (or its own tile); never concatenate a row's values into one cell.

The table has 8 rows and 3 columns.

ROW 1 — Headers
- Cell 1: Bloco de Escopo
- Cell 2: Tamanho
- Cell 3: Confiança

ROW 2 — Antecipação de Atendimento Agendado (WhatsApp)
- Cell 1: Antecipação de Atendimento Agendado (WhatsApp)
- Cell 2: L
- Cell 3: Confirmed

ROW 3 — Apoio ao Atendimento Presencial (Slack)
- Cell 1: Apoio ao Atendimento Presencial (Slack)
- Cell 2: M
- Cell 3: Confirmed

ROW 4 — Integração com Sistemas Legados
- Cell 1: Integração com Sistemas Legados
- Cell 2: L
- Cell 3: Unknown

ROW 5 — Serviço de Seleção de Antecipação
- Cell 1: Serviço de Seleção de Antecipação
- Cell 2: M
- Cell 3: Unknown

ROW 6 — Autoprovisionamento de Atendentes
- Cell 1: Autoprovisionamento de Atendentes
- Cell 2: XL
- Cell 3: Unknown

ROW 7 — Observabilidade e Analytics
- Cell 1: Observabilidade e Analytics
- Cell 2: L
- Cell 3: Assumed

ROW 8 — Base de Conhecimento e IA no Assistente do Slack
- Cell 1: Base de Conhecimento e IA no Assistente do Slack
- Cell 2: L
- Cell 3: Unknown

Style: header row uses the template's heading style with the accent color background and white text; body rows use body text. Column 1 left-aligned; columns 2 and 3 center-aligned. Give rows where Cell 3 = "Unknown" a light accent-color fill so they stand out visually.

FOOTER (small, muted italic): Cada um dos quatro pontos Unknown tem dono definido do lado do cliente — a Fase 0 fecha essas lacunas antes de travar cronograma.
```

---

## Prompt 5 — A decisão de arquitetura

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: O atendente passa a operar 100% dentro do Slack, apoiado por uma ponte já validada em PoC
SUBTITLE: Configuração nativa no lugar de automação customizada.

LAYOUT: Diagrama de arquitetura em camadas, três caixas empilhadas verticalmente (Status de Presença no topo, Ponte de Integração no meio, Canal do Slack na base), com um bloco de bullets "Decisão de Escopo" ao lado direito das três camadas.

CAMADA 1 — Status de Presença
- Mudança de status de disponibilidade do atendente no Omni-Channel
- Não é automação customizada monitorando fila

CAMADA 2 — Ponte de Integração
- Apex monitorando Platform Events
- PoC já validado com o cliente

CAMADA 3 — Canal do Slack
- Canal pessoal do atendente, thread por caso
- Atendente não alterna para a tela de atendimento padrão

DECISÃO DE ESCOPO
- Dois sistemas legados confirmados como plataformas distintas
- Autoprovisionamento de atendentes cresceu de M para XL — agora inclui criar o canal pessoal

Use the template's heading style for TITLE. Block headers bold. Body style for bullets.
```

---

## Prompt 6 — O plano de execução (timeline)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: A Fase 0 fecha os gaps que hoje bloqueiam o dimensionamento das quatro fases seguintes
SUBTITLE: Faixa indicativa de duração (lane Aumentada, sem cronograma comprometido): 15 a 34 semanas.

LAYOUT: Timeline horizontal de 5 fases em sequência, caixas de largura igual lado a lado. O caminho crítico (Fundação → Antecipação Digital → Observabilidade) usa uma cor de destaque diferente das fases em paralelo (Apoio Presencial).

FASE 0 — Resolução de Gaps
- Sem escopo de entrega
- Fecha os pontos em aberto do dimensionamento

FASE 1 — Fundação
- Integração com os dois sistemas legados
- Provisionamento de atendentes

FASE 2 — Jornada 1: Antecipação Digital
- WhatsApp + seleção de antecipação

FASE 3 — Jornada 2: Apoio Presencial
- Apoio via Slack + base de conhecimento

FASE 4 — Observabilidade e Analytics
- Relatórios executivos em Tableau Next

FOOTER (small, muted italic): A faixa de semanas é indicativa, não um compromisso de prazo.

Use the template's heading style for TITLE and for each phase name.
```

---

## Prompt 7 — O time

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: Dez papéis de Salesforce PS compõem o time, incluindo disciplinas dedicadas de Design de Experiência e de Change & Adoption
SUBTITLE: Duas disciplinas evitam retrabalho — sem expor contagem de pessoas.

LAYOUT: Fileira de três chips de categoria, empilhados verticalmente. Cada linha: chip de categoria à esquerda (~22% da largura, fundo de cor de destaque, texto branco em negrito) e conteúdo em bullets à direita (~78%).

DESIGN DE EXPERIÊNCIA
- Cobre a jornada do cidadão no WhatsApp
- Sem esse trabalho: retrabalho depois que o cidadão já estiver usando o canal em produção

CHANGE & ADOPTION
- Cobre a mudança de rotina dos atendentes
- Sem esse trabalho: risco de a solução não ser adotada como desenhada

LADO DO CLIENTE
- Responsável pela decisão do projeto ainda não foi nomeado
- Acesso a sistemas internos ainda não confirmado

FOOTER (small, muted italic): O formato do time está definido; a contagem exata acompanha a validação comercial.

Apply the template's accent color to the three category chips.
```

---

## Prompt 8 — A prova (PoC)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: O PoC da ponte entre a plataforma e o Slack já foi validado com o cliente
SUBTITLE: Falta confirmar qual mecanismo real de entrega ele usa.

LAYOUT: Estatística única em destaque, centralizada na parte superior do slide, sem gráfico — texto grande "PoC validado" em cor de destaque. Abaixo, uma nota de risco em dois blocos curtos.

STATUS
- PoC prova que a experiência 100%-Slack para o atendente funciona tecnicamente

PONTO ABERTO
- Mecanismo real: gatilho (limite mais alto) ou monitoramento contínuo (limite bem mais restritivo)
- A diferença muda o teto de quantas antecipações a solução aguenta por dia

Use the template's heading style for TITLE and for "PoC validado". Body style for bullets.
```

---

## Prompt 9 — Os riscos (tabela)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: Dos catorze riscos mapeados, o Fixed Fee sobre escopo incerto é o único sem mitigação de escopo disponível
SUBTITLE: Honestidade de risco antes do pedido de aprovação.

LAYOUT: Render this as an actual table object — or a card/tile grid if that lays out more cleanly — not a text box with bolded headers and pipe characters. Each field below goes in its OWN cell; never concatenate a row's values into one cell.

The table has 5 rows and 3 columns.

ROW 1 — Headers
- Cell 1: Risco
- Cell 2: Por que importa
- Cell 3: Quem resolve

ROW 2 — Fixed Fee sobre escopo incerto
- Cell 1: Fixed Fee sobre escopo incerto
- Cell 2: Preço fechado sobre escopo em que mais da metade dos blocos ainda é incerta
- Cell 3: Fechar os pontos abertos do dimensionamento (Fase 0)

ROW 3 — Regras de seleção de antecipação
- Cell 1: Regras de seleção de antecipação indefinidas
- Cell 2: Bloqueia sizing definitivo antes da Fase 1
- Cell 3: Cliente

ROW 4 — Sistema de RH não identificado
- Cell 1: Sistema de RH da PRODESP não identificado
- Cell 2: Bloqueia sizing do autoprovisionamento de atendentes
- Cell 3: Cliente

ROW 5 — Proteção de dados pessoais
- Cell 1: Proteção de dados pessoais (WhatsApp, gov.br, biometria)
- Cell 2: Sem decisão de arquitetura de dados tomada ainda
- Cell 3: Mesa comercial, antes do fechamento do MVP

Style: header row uses the template's heading style with the accent color background and white text; body rows use body text. Give Row 2 (Fixed Fee) an accent-color fill to signal it's the highest-weight risk.

FOOTER (small, muted italic): Riscos aceitos sem mitigação ativa: sponsor de observabilidade não nomeado, governança de dados de RH, governança de conteúdo da base de conhecimento.
```

---

## Prompt 10 — O pedido

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

TITLE: O primeiro passo é nomear o responsável do cliente pela decisão do projeto e aprovar a Fase 0
SUBTITLE: O pedido desta apresentação.

LAYOUT: Lista numerada, coluna única, centralizada, sem decoração.

PEDIDO
1. Nomear quem tem autoridade de decisão e disponibilidade definida para a Fase 0
2. Aprovar a Fase 0 antes de travar cronograma e time
3. Levar a decisão de proteção de dados pessoais à conversa comercial
4. Confirmar com o time que validou o PoC qual mecanismo real sustenta a ponte com o Slack

Use the template's heading style for TITLE. Body style, larger size, for the numbered list.
```
