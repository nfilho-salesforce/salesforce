# Prompts Gemini — ROM PRODESP-DER (geração de deck PPTX/Google Slides)

*Gerado em 2026-09-18. Fonte única de conteúdo: `outputs/artifacts/presentation-outline.md`. Todo número (R$, semanas, contagens) foi copiado verbatim dessa fonte — nenhum valor foi recalculado ou arredondado.*

## Como usar

1. Abra o Gemini web (gemini.google.com), não a barra lateral do Gemini dentro de um Slides existente — este é um deck **novo**, gerado do zero.
2. Trabalhe em uma pasta do Drive limpa, sem outros decks ou PDFs de referência por perto — o Gemini usa arquivos vizinhos como contexto.
3. Cole os prompts **um por vez, na ordem abaixo**, cada um em um slide de template em branco (não duplique um slide já estilizado — o estilo "vaza" para o próximo).
4. Cada prompt é autocontido: não depende do Gemini lembrar o conteúdo do slide anterior. Aceite o resultado, inspecione o slide antes de colar o próximo prompt.
5. Todo o conteúdo é PT-BR. Não peça tradução para inglês ou espanhol em nenhum momento.
6. Esta versão cobre os 12 slides originais do outline mais 3 slides novos exigidos por este ROM: "Épicos e Casos de Uso" (após o Alcance do MVP), a divisão do Roadmap em duas telas (linha do tempo + comparação de lanes), e "Investimento (ROM)". Total: 15 blocos de prompt.
7. Se o Gemini parafrasear, expandir ou colapsar itens, use as frases de recuperação do guia `gemini-delivery.md` (ex.: "Restaure minha formulação exata, verbatim: [colar]. Não parafraseie.").

---

### Slide 1 — Capa

Nota de palco: abrir com confiança — este é o resultado da PoC, não uma nova venda.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: PRODESP-DER: da PoC de Cubatão/Taubaté para uma nova fase de escala estadual

LAYOUT: Capa centralizada, densidade sparse. Título grande centralizado no terço superior do slide. Uma linha de subtítulo abaixo do título. Espaço em branco generoso — não adicionar gráficos, ícones ou caixas extras.

SUBTÍTULO (menor, cor discreta, abaixo do título)
- DER-SP · Field Service + Agentforce

RODAPÉ (pequeno, discreto): [inserir data da apresentação]

Use o estilo de capa do template (wordmark/logo mantidos como estão). Título em estilo de heading grande; subtítulo em estilo de corpo menor e com cor mais discreta (muted).
```

---

### Slide 2 — Situação Atual

Nota de palco: não passar rápido demais aqui — é a única vez que a dor aparece explicitamente antes da solução.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Hoje, o socorro na rodovia não tem um protocolo único do pedido ao encerramento

LAYOUT: Estatística dominante centralizada na metade superior do slide, com 4 marcadores de apoio abaixo, em uma única coluna.

ESTATÍSTICA CENTRAL (número grande + legenda abaixo, destaque visual máximo do slide)
- 0
- protocolo único

MARCADORES DE APOIO (abaixo da estatística, alinhados à esquerda)
- Atendimento fragmentado em chamados distintos: pedido, despacho e encerramento
- Sem identificador único do início ao fim do atendimento
- Sem rastreamento em tempo real para o cidadão na pista
- Único canal hoje é a voz (0800) — o WhatsApp existente pertence à ouvidoria, não ao socorro emergencial

Style: número "0" em fonte muito grande na cor de destaque do template; "protocolo único" como legenda diretamente abaixo, em fonte menor. Marcadores de apoio em estilo de corpo padrão.
```

---

### Slide 3 — Visão de Transformação

Nota de palco: pausa de 2-3 segundos após ler a frase central — deixar a Big Idea assentar.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: A tecnologia a serviço do processo — e, no fim da linha, do cidadão na pista

LAYOUT: Texto hero central, sem tabelas nem gráficos competindo. Uma frase de destaque no centro do slide e, abaixo, 3 marcadores curtos.

TEXTO HERO (centralizado, fonte grande)
- Protocolo único e rastreável do primeiro contato ao encerramento

MARCADORES DE APOIO (abaixo do texto hero, fonte menor)
- Despacho automático apoiado pelo Field Service
- Entrada pelo canal que o motorista já usa: voz ou WhatsApp
- Escala real: 14 CGRs, não apenas o piloto

Style: nenhum gráfico competindo com o texto hero. Espaço em branco generoso nas laterais e acima/abaixo do bloco central.
```

---

### Slide 4 — Resultados de Valor Confirmados

Nota de palco: se perguntarem "por que só 4 outcomes", responder que são os que o DER confirmou — o resto é tático, não estratégico.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Quatro resultados de valor confirmados com o DER orientam todo o desenho da solução

LAYOUT: 4 linhas horizontais no estilo "chip de categoria" — um chip colorido à esquerda (~22% da largura) com o identificador do resultado, e o conteúdo à direita (~78%) com o nome do resultado e a dor que ele remove.

LINHA 1
- Chip: V1
- Conteúdo: Protocolo único e rastreável — remove o atendimento fragmentado em chamados distintos para pedido, despacho e encerramento, sem identificador único nem rastreamento em tempo real para o cidadão na pista

LINHA 2
- Chip: V2
- Conteúdo: Canal digital complementar ao 0800 — remove a dependência exclusiva da voz; o WhatsApp existente pertence à ouvidoria, não ao socorro emergencial, deixando o motorista sem alternativa quando a voz não é viável

LINHA 3
- Chip: V3
- Conteúdo: Despacho automatizado com governança de exceção — remove o despacho manual pelo C2C sem regra sistemática de aderência/disponibilidade/proximidade, que sobrecarrega a mesa em picos de demanda

LINHA 4
- Chip: V4
- Conteúdo: Auditabilidade do ciclo de atendimento — remove overrides manuais de despacho e execução em campo sem trilha de auditoria obrigatória, que dificultam a prestação de contas a órgãos de controle do Estado

Style: aplicar a cor de destaque do template ao chip (V1-V4). Conteúdo em estilo de corpo à direita, alinhado verticalmente ao centro de cada linha.
```

---

### Slide 5 — Arquitetura da Solução

Nota de palco: se perguntarem sobre outras nuvens Salesforce fora de escopo, reforçar que o Service Cloud está deliberadamente limitado ao canal WhatsApp — não é atendimento amplo.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Uma única arquitetura: o Field Service comanda o despacho, o Agentforce abre a porta do WhatsApp

LAYOUT: Hub-and-spoke. Salesforce (org única) no centro do slide, em um círculo ou hexágono de destaque. Ao redor, 4 módulos conectados por linhas ao centro: Field Service, Agentforce (Contact Center Enterprise), Service Cloud (escopado ao canal WhatsApp), Experience Cloud. Fora do hub, dois sistemas externos conectados por linhas de integração: SIGOR e SIGEO.

CENTRO DO HUB
- Salesforce — org única

MÓDULO 1 — Field Service
- Motor central de despacho
- Work Order, Service Appointment, Service Territory
- Modelo de Skills para aderência

MÓDULO 2 — Agentforce (Contact Center Enterprise)
- Cobre o canal WhatsApp

MÓDULO 3 — Service Cloud (escopado ao canal WhatsApp)
- Não é atendimento amplo — escopo limitado a esse canal

MÓDULO 4 — Experience Cloud
- Link de rastreamento do cidadão

SISTEMAS EXTERNOS (fora do hub, conectados por linhas de integração)
- SIGOR
- SIGEO

Style: aplicar a cor de destaque do template ao círculo/hexágono central "Salesforce". Módulos em caixas de mesmo tamanho ao redor do hub. Sistemas externos (SIGOR, SIGEO) em caixas de estilo visualmente diferente (ex.: contorno pontilhado ou cor neutra), indicando que são sistemas legados fora da org Salesforce, conectados por linhas rotuladas "integração".
```

---

### Slide 6 — Alcance do MVP

Nota de palco: âncora numérica — repetir "14, 298, 1.152" verbalmente, não só ler o slide.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: O MVP cobre toda a produção estadual — 14 CGRs, 298 viaturas, 1.152 operadores

LAYOUT: Linha de 4 blocos de estatística (stat tiles) na parte superior, e uma tabela (ou grid de cartões) de 5 linhas de conteúdo na parte inferior, com 2 colunas: nome do épico e tamanho. Each field below goes in its OWN cell (or its own tile); never concatenate a row's values into one cell.

LINHA DE ESTATÍSTICAS (4 blocos, cada um número grande + legenda abaixo)
- 14 / CGRs
- 298 / viaturas
- 1.152 / operadores de campo
- 5 / capacidades entregues em org única

TABELA — 6 linhas (1 de cabeçalho + 5 de conteúdo) e 2 colunas.

LINHA 1 — Cabeçalho
- Célula 1: Épico
- Célula 2: Tamanho

LINHA 2
- Célula 1: Canal Digital de Atendimento ao Cidadão
- Célula 2: M

LINHA 3
- Célula 1: Registro e Classificação da Ocorrência
- Célula 2: L

LINHA 4
- Célula 1: Despacho Automatizado de Recursos de Campo
- Célula 2: L

LINHA 5
- Célula 1: Execução em Campo (App Mobile)
- Célula 2: L

LINHA 6
- Célula 1: Rastreamento e Visibilidade em Tempo Real
- Célula 2: L

Style: linha de estatísticas com números grandes na cor de destaque do template, legendas em fonte menor abaixo de cada número. Tabela abaixo com linha de cabeçalho em estilo heading com fundo na cor de destaque; linhas de corpo em estilo de texto padrão. Se ficar mais limpo, renderize como grid de 5 cartões (um por épico) em vez de tabela — desde que cada campo permaneça em sua própria célula ou cartão.
```

---

### Slide 7 — Épicos e Casos de Uso (novo)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Cinco épicos entregam o MVP completo — do canal digital ao rastreamento em tempo real

LAYOUT: Render this as an actual table object — or a card/tile grid if that lays out more cleanly — not a text box with bolded headers and pipe characters. Each field below goes in its OWN cell (or its own tile); never concatenate a row's values into one cell. A tabela tem 6 linhas (1 de cabeçalho + 5 de conteúdo) e 4 colunas.

LINHA 1 — Cabeçalho
- Célula 1: Épico
- Célula 2: Tamanho
- Célula 3: O que entrega
- Célula 4: Casos de uso principais

LINHA 2 — Canal Digital de Atendimento ao Cidadão
- Célula 1: Canal Digital de Atendimento ao Cidadão (WhatsApp + Agentforce)
- Célula 2: M
- Célula 3: Abertura de chamado de socorro via WhatsApp com triagem automatizada e transbordo garantido para fila humana — a IA nunca decide a gravidade da vítima
- Célula 4: Abertura de chamado via WhatsApp · Triagem automatizada pelo Agentforce · Transbordo garantido para fila humana

LINHA 3 — Registro e Classificação da Ocorrência
- Célula 1: Registro e Classificação da Ocorrência
- Célula 2: L
- Célula 3: Criação do chamado a partir de qualquer canal, classificado por catálogo de 100+ subtipos desde o dia 1, com trilha de auditoria e integração aos sistemas legados SIGOR/SIGEO
- Célula 4: Registro multi-canal (WhatsApp/0800) · Catálogo de classificação com 100+ subtipos · Sincronização SIGOR/SIGEO

LINHA 4 — Despacho Automatizado de Recursos de Campo
- Célula 1: Despacho Automatizado de Recursos de Campo
- Célula 2: L
- Célula 3: Motor de despacho por aderência operando nas 14 CGRs, 100% reativo em tempo real, com escalonamento de espera e reprocessamento automático em recusa
- Célula 4: Motor de despacho por aderência (Skills) · Escalonamento de espera por tempo (regra N/N-10) · Console do Dispatcher

LINHA 5 — Execução em Campo (App Mobile)
- Célula 1: Execução em Campo (App Mobile)
- Célula 2: L
- Célula 3: Aplicativo único de Field Service Mobile para os 1.152 operadores de campo das 14 UBAs, com despacho via push nativo e encerramento por checklist condicional
- Célula 4: App único de Field Service Mobile · Recebimento de despacho via push nativo · Travas de negócio (recusa com motivo, foto, check-in geolocalizado)

LINHA 6 — Rastreamento e Visibilidade em Tempo Real
- Célula 1: Rastreamento e Visibilidade em Tempo Real
- Célula 2: L
- Célula 3: Protocolo único acompanhável do pedido ao encerramento — link de rastreamento para o cidadão, mapa/Gantt para o C2C, painel agregado para gestores
- Célula 4: Link de rastreamento para o cidadão (Experience Cloud guest) · Mapa/Gantt do C2C com Aerial Routing · Painel agregado para gestores (4 indicadores)

Style: header row com fundo na cor de destaque do template; linhas de corpo em texto padrão. Coluna 1 (Épico) e coluna 2 (Tamanho) mais estreitas; colunas 3 e 4 mais largas para acomodar o texto. Se a tabela ficar muito densa para 5 linhas de conteúdo, renderize como grid de 5 cartões (um por épico) com os 4 campos dentro de cada cartão, nunca concatenados.
```

---

### Slide 8 — Complexidade e Tecnologia por Capacidade

Nota de palco: honestidade aqui gera confiança — "sim, é complexo, e sabemos exatamente onde".

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Quatro das cinco capacidades concentram alta complexidade — despacho e mobilidade de campo puxam o esforço

LAYOUT: Duas seções verticais. Seção superior: distribuição de tamanhos das 5 capacidades (1 M, 4 L) como uma linha de 5 blocos, um por capacidade, com o tamanho como rótulo em cada bloco. Seção inferior: tabela de 6 linhas (1 de cabeçalho + 5 de conteúdo) e 2 colunas — capacidade e tecnologia associada. Each field below goes in its OWN cell; never concatenate a row's values into one cell.

DISTRIBUIÇÃO DE TAMANHOS (5 blocos em linha)
- Canal Digital — M
- Registro e Classificação — L
- Despacho Automatizado — L
- Execução em Campo — L
- Rastreamento em Tempo Real — L

TABELA CAPACIDADE → TECNOLOGIA

LINHA 1 — Cabeçalho
- Célula 1: Capacidade
- Célula 2: Tecnologia

LINHA 2
- Célula 1: Canal Digital
- Célula 2: Agentforce (Contact Center Enterprise) + Digital Engagement, no canal WhatsApp

LINHA 3
- Célula 1: Registro e Classificação
- Célula 2: Catálogo de mais de 100 subtipos

LINHA 4
- Célula 1: Despacho Automatizado
- Célula 2: Motor de aderência com Skills

LINHA 5
- Célula 1: Execução em Campo
- Célula 2: App único de Field Service Mobile

LINHA 6
- Célula 1: Rastreamento em Tempo Real
- Célula 2: Site de convidado no Experience Cloud

Style: blocos de tamanho na seção superior usando cores diferentes para M e L (M em cor neutra, L na cor de destaque do template, indicando maior complexidade). Tabela na seção inferior com cabeçalho destacado.
```

---

### Slide 9 — Gaps Mapeados e a Fase 0

Nota de palco: framear como "encontramos isso porque olhamos com profundidade" — não como uma falha da PoC.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: 79 gaps mapeados na discovery, sete deles conflitos de fonte — por isso a Fase 0 é necessária antes do build

LAYOUT: Gráfico de barras horizontais com as 8 categorias de gap e sua contagem, ordenado do maior para o menor. A barra "Conflito de Fonte" destacada em cor diferente das demais. Abaixo do gráfico, um bloco de texto com a nota de limite.

CATEGORIAS E CONTAGENS (barras, maior para menor)
- Requisito Faltante: 26
- Gap Lógico: 14
- Ambiguidade: 10
- Risco Potencial: 8
- Conflito de Fonte: 7
- Fora de Escopo: 6
- Gap de Capacidade: 6
- Premissa: 2

NOTA DE LIMITE (abaixo do gráfico)
- Limite que aciona recomendação de Fase 0: mais de 15 gaps ou mais de 5 conflitos de fonte — ambos excedidos neste projeto

Style: todas as barras na cor neutra do template, exceto "Conflito de Fonte", que usa a cor de destaque para chamar atenção. Contagem numérica ao final de cada barra.
```

---

### Slide 10 — Riscos Críticos e Mitigações

Nota de palco: ser direto — "estes dois itens precisam de uma decisão do DER, não da Salesforce, antes do build."

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Dois riscos bloqueiam decisão do DER antes do build — trilha de auditoria e limite contratual das UBAs por CGR

LAYOUT: Duas seções. Seção superior, título "Bloqueadores": 2 callouts vermelhos lado a lado. Seção inferior, título "Riscos Monitorados": 3 callouts amarelos lado a lado.

CALLOUT VERMELHO 1 — G0305
- Trilha de auditoria do despacho sem desenho definido
- Padrão nativo tem limite de 20 campos e 18-24 meses de retenção
- Mitigação: resolver na Fase 0, antes de configurar console e território

CALLOUT VERMELHO 2 — G0309
- Limite contratual das UBAs por CGR não confirmado
- Despacho por proximidade pode indicar viatura de CGR vizinha
- Mitigação: resolver na Fase 0, antes de configurar console e território

CALLOUT AMARELO 1
- Enforcement offline

CALLOUT AMARELO 2
- LGPD / DPIA

CALLOUT AMARELO 3
- Licença Field Service Community

FOOTER (pequeno, discreto, itálico): Estes dois itens precisam de uma decisão do DER, não da Salesforce, antes do build.

Style: callouts vermelhos com fundo vermelho/cor de alerta forte; callouts amarelos com fundo amarelo/cor de atenção mais leve. Títulos de seção ("Bloqueadores", "Riscos Monitorados") em estilo heading acima de cada linha de callouts.
```

---

### Slide 11 — Roadmap: Cinco Fases (Linha do Tempo)

Nota de palco: nomear a janela do contrato da URA em voz alta — é o argumento de urgência mais forte que existe.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Cinco fases levam a solução da fundação ao rastreamento em tempo real em 16 a 30 semanas

LAYOUT: Timeline horizontal com 5 blocos de fase em sequência (Fase 0 a Fase 4), cada bloco com o nome da fase e o objetivo abaixo. Abaixo da timeline, uma linha indicando o caminho crítico com setas conectando os épicos correspondentes. Abaixo disso, um callout de urgência.

TIMELINE (5 blocos em sequência horizontal)
- Bloco 1: Fase 0 — Resolução de Discovery / Resolver G0305 (trilha de auditoria) e G0309 (limite de UBAs por CGR) antes do build
- Bloco 2: Fase 1 — Fundação / Registro da Ocorrência e Integrações (SIGOR/SIGEO)
- Bloco 3: Fase 2 — Despacho e Canal Digital / Despacho Automatizado + Canal Digital (WhatsApp/Agentforce)
- Bloco 4: Fase 3 — Execução em Campo / App mobile único, travas de negócio
- Bloco 5: Fase 4 — Rastreamento e Estabilização / Link de rastreamento do cidadão, painel de gestores

CAMINHO CRÍTICO (linha abaixo da timeline, com setas conectando os blocos correspondentes)
- E02 → E03 → E04 → E05

CALLOUT DE URGÊNCIA (abaixo da timeline, cor de destaque)
- O contrato atual de URA (Instinct) expira em abril de 2027 — mesma janela da meta de produção do cliente (homologação jan/fev 2027, produção abril 2027)
- O contrato administrativo renova em 30 de novembro de 2026, pressionando a decisão entre Open CTI e Salesforce Voice

FOOTER (pequeno, discreto, itálico): Faixa derivada do formato do engagement (benchmark) — ponta alta ampliada por mobile e site 100% customizados e por overlay de governança/auditoria em aberto.

Style: blocos da timeline em sequência conectada por uma linha ou seta; cada bloco com o nome da fase em destaque e o objetivo em fonte menor abaixo. Callout de urgência com fundo na cor de destaque do template para se diferenciar dos blocos da timeline.
```

---

### Slide 12 — Comparação de Duração por Modelo de Entrega (novo)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: A duração varia por modelo de entrega — do modelo tradicional ao AI-native condicional

LAYOUT: Render this as an actual table object — or a card/tile grid if that lays out more cleanly — not a text box with bolded headers and pipe characters. Each field below goes in its OWN cell (or its own tile); never concatenate a row's values into one cell. A tabela tem 4 linhas (1 de cabeçalho + 3 de conteúdo) e 3 colunas. A linha (ou cartão) "AI-native (condicional)" deve ter borda tracejada e uma etiqueta "CONDICIONAL" visível, para diferenciá-la visualmente das outras duas — nunca apresentada como equivalente ou igualmente alcançável.

LINHA 1 — Cabeçalho
- Célula 1: Modelo de Entrega
- Célula 2: Duração
- Célula 3: Base de Cálculo

LINHA 2 — Traditional (âncora)
- Célula 1: Traditional (âncora)
- Célula 2: 16-30 semanas
- Célula 3: Derivada do formato do engagement (benchmark top-down), sem compressão

LINHA 3 — Augmented
- Célula 1: Augmented
- Célula 2: 14-25 semanas
- Célula 3: Faixa Traditional comprimida pela banda de eficiência realizada (aproximadamente 10-18%)

LINHA 4 — AI-native (condicional)
- Célula 1: AI-native (condicional)
- Célula 2: 10-18 semanas
- Célula 3: Faixa Traditional comprimida pela banda de eficiência nativa (aproximadamente 35-40%) — gate de qualificação ainda não atendido

FOOTER (pequeno, discreto, itálico): A faixa AI-native permanece condicional ao gate de qualificação (nenhum sponsor executivo nomeado, mandato AI-first ainda não assumido) — é um motivador, nunca uma entrega comprometida sem nomear o compromisso.

Style: header row com fundo na cor de destaque do template. Linhas/cartões "Traditional" e "Augmented" com bordas sólidas normais. Linha/cartão "AI-native (condicional)" com borda tracejada e uma etiqueta pequena "CONDICIONAL" em destaque (ex.: fundo laranja ou cinza, texto em caixa alta) — visualmente distinto dos outros dois, nunca no mesmo estilo visual.
```

---

### Approved Commercials — Slide 13 — Investimento (ROM) (novo)

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Investimento indicativo por modelo de entrega, com e sem impostos

LAYOUT: Duas tabelas empilhadas verticalmente, ambas como table objects reais (Insert > Table), nunca texto com pipes. Each field below goes in its OWN cell; never concatenate a row's values into one cell. Tabela 1 (superior): rates aplicadas, 4 linhas (1 cabeçalho + 3 conteúdo) e 3 colunas. Tabela 2 (inferior): faixa de investimento por modelo de entrega, 4 linhas (1 cabeçalho + 3 conteúdo) e 4 colunas. Na Tabela 2, a linha "AI-native (condicional)" deve ter borda tracejada e etiqueta "CONDICIONAL", no mesmo padrão visual do slide de comparação de duração. Abaixo das duas tabelas, um bloco de texto pequeno e discreto com os três avisos abaixo, na ordem dada, sem alterar uma palavra.

TABELA 1 — Rates aplicadas (R$/hora)

LINHA 1 — Cabeçalho
- Célula 1: Bucket
- Célula 2: Sem imposto
- Célula 3: Com imposto

LINHA 2
- Célula 1: Architect-class sênior onshore (PM/SA/TA · Program Lead/Intent Architect/Agent Orchestrator)
- Célula 2: R$ 884,68
- Célula 3: R$ 946,69

LINHA 3
- Célula 1: Entrega sênior onshore ou qualquer offshore regular (FC/Developer/QA sênior onshore · qualquer papel offshore regular)
- Célula 2: R$ 668,78
- Célula 3: R$ 715,66

LINHA 4
- Célula 1: Change & Adoption regular onshore (Change & Adoption · Adoption Architect)
- Célula 2: R$ 573,98
- Célula 3: R$ 614,21

TABELA 2 — Faixa indicativa de investimento por modelo de entrega (BRL)

LINHA 1 — Cabeçalho
- Célula 1: Modelo de Entrega
- Célula 2: Duração
- Célula 3: Sem imposto
- Célula 4: Com imposto

LINHA 2 — Traditional (âncora)
- Célula 1: Traditional (âncora)
- Célula 2: 16-30 semanas
- Célula 3: R$ 5.918.133,18 – R$ 11.096.499,71
- Célula 4: R$ 6.332.940,80 – R$ 11.874.264,00

LINHA 3 — Augmented
- Célula 1: Augmented
- Célula 2: 14-25 semanas
- Célula 3: R$ 5.178.366,53 – R$ 9.247.083,09
- Célula 4: R$ 5.541.323,20 – R$ 9.895.220,00

LINHA 4 — AI-native (condicional)
- Célula 1: AI-native (condicional)
- Célula 2: 10-18 semanas
- Célula 3: R$ 2.227.507,84 – R$ 4.009.514,12
- Célula 4: R$ 2.383.636,00 – R$ 4.290.544,80

RODAPÉ (pequeno, discreto, itálico) — usar exatamente os três avisos abaixo, nesta ordem, sem alterar uma palavra:

Aviso 1: "Esta faixa é baseada nas rates de R$946,69/h (architect-class sênior onshore), R$715,66/h (entrega sênior onshore/qualquer offshore regular) e R$614,21/h (change & adoption regular onshore) que você forneceu e validou em 2026-09-17. Indicativo para planejamento apenas; a estrutura comercial final é confirmada através do acordo comercial aplicável."

Aviso 2: "A faixa AI-native permanece condicional ao gate de qualificação (nenhum sponsor executivo nomeado, mandato AI-first ainda não assumido) — é um motivador, nunca uma entrega comprometida sem nomear o compromisso. Este é um preço indicativo, não custo/margem, e não uma proposta de fixed fee."

Aviso 3: "Esta comparação é benchmark-based, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Faixas de duração e a faixa AI-native carregam a incerteza herdada de confidence: Assumed em todos os 5 épicos."

Style: Tabela 1 com cabeçalho destacado na cor de destaque do template. Tabela 2 igual, exceto a linha "AI-native (condicional)", que usa borda tracejada e uma etiqueta pequena "CONDICIONAL" em destaque — nunca no mesmo estilo visual das outras duas linhas. Os três avisos no rodapé em fonte pequena, itálica, cor discreta (muted), claramente separados das tabelas por um espaço ou linha fina.
```

---

### Slide 14 — Adoção e Change Management

Nota de palco: deixar claro que esse plano já reflete o pedido do próprio DER, não é overhead nosso.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: 1.152 operadores em 14 empresas terceirizadas — por isso o DER pediu até dois meses de operação assistida

LAYOUT: Bloco de 3 estatísticas em linha no topo, com uma narrativa curta abaixo em uma única coluna.

BLOCO DE ESTATÍSTICAS (3 números grandes em linha, cada um com legenda abaixo)
- 1.152 / operadores de campo
- 14 / empresas terceirizadas (UBAs)
- até 2 meses / de operação assistida

NARRATIVA (abaixo do bloco de estatísticas)
- O change management não é uma adição do time de entrega — foi pedido explícito do DER
- Operação assistida e treinamento personalizado por persona, com foco nos técnicos de campo das 14 UBAs
- A experiência do cidadão no link de rastreamento já foi validada na PoC, sem necessidade de pesquisa de UX adicional

Style: bloco de estatísticas com números grandes na cor de destaque do template; narrativa em estilo de corpo, alinhada à esquerda, abaixo do bloco.
```

---

### Slide 15 — Fechamento: o Ask

Nota de palco: terminar em silêncio após o ask — não preencher o espaço, deixar a decisão ser deles.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Fechar agora leva o DER a uma nova fase de escalabilidade e inovação — a tecnologia em prol do processo e do cidadão

LAYOUT: Texto hero repetindo a Big Idea no topo, e abaixo 3 marcadores numerados com o ask.

TEXTO HERO (centralizado, fonte grande)
- Este projeto leva o DER a uma nova fase de escalabilidade e inovação — coloca a tecnologia em prol dos processos e, no fim da linha, do cidadão na pista

ASK EM 3 PASSOS (numerados, abaixo do texto hero)
- 1. Aprovar o escopo dos 5 épicos e a faixa de roadmap apresentada
- 2. Validar com a Salesforce PS os dois riscos bloqueadores (auditoria, limite de UBAs) na sessão de Fase 0
- 3. Iniciar a Fase 0 com o roteiro já mapeado

Style: texto hero em fonte grande, sem gráficos competindo. Os 3 passos numerados em fonte grande o suficiente para leitura à distância, com o número em destaque na cor do template.
```
