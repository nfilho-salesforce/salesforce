# Prompts Gemini — ROM PRODESP-DER (geração de deck PPTX/Google Slides)

*Gerado em 2026-09-18. Revisado em 2026-09-18 (sincronizado com a reescrita do outline: seção única de Situação Atual/Visão/Resultados, gaps abertos em 4 blocos, mapa de riscos, linha do tempo visual em Gantt, roadmap de futuro, change management aprofundado, investimento com entregáveis de escopo fechado). Fonte única de conteúdo: `outputs/artifacts/presentation-outline.md`. Todo número (R$, semanas, contagens) foi copiado verbatim dessa fonte — nenhum valor foi recalculado ou arredondado.*

## Como usar

1. Abra o Gemini web (gemini.google.com), não a barra lateral do Gemini dentro de um Slides existente — este é um deck **novo**, gerado do zero.
2. Trabalhe em uma pasta do Drive limpa, sem outros decks ou PDFs de referência por perto — o Gemini usa arquivos vizinhos como contexto.
3. Cole os prompts **um por vez, na ordem abaixo**, cada um em um slide de template em branco (não duplique um slide já estilizado — o estilo "vaza" para o próximo).
4. Cada prompt é autocontido: não depende do Gemini lembrar o conteúdo do slide anterior. Aceite o resultado, inspecione o slide antes de colar o próximo prompt.
5. Todo o conteúdo é PT-BR. Não peça tradução para inglês ou espanhol em nenhum momento.
6. Esta versão cobre os 12 slides do outline (Capa → Fechamento) mais 2 blocos adicionais: "Épicos e Casos de Uso" (detalhamento completo por épico, após o Alcance do MVP) e a divisão do slide de Investimento em duas telas (entregáveis do escopo fechado, sem valores, e as figuras de investimento com/sem impostos do `## Approved Commercials`). Total: 14 blocos de prompt.
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

### Slide 2 — Situação Atual, Visão de Transformação e Resultados de Valor

Nota de palco: não passar rápido demais — esta é a leitura completa de dor, visão e prova em uma página; deixar cada bloco assentar antes de avançar ao próximo.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Do atendimento fragmentado a um protocolo único e rastreável — quatro resultados de valor já confirmados com o DER

LAYOUT: Três faixas horizontais empilhadas ocupando toda a altura útil do slide, cada uma com um pequeno rótulo lateral (Hoje / Visão / Prova de valor confirmada) e uma cor de filete diferente por faixa. A leitura é uma progressão de cima para baixo — dor, depois visão, depois prova — não três slides colados.

FAIXA 1 — rótulo lateral "Hoje". Estatística dominante à esquerda (número grande + legenda) e 4 marcadores de apoio à direita, alinhados à esquerda.

ESTATÍSTICA CENTRAL
- 0
- protocolo único

MARCADORES DE APOIO (Faixa 1)
- Atendimento fragmentado em chamados distintos: pedido, despacho e encerramento
- Sem identificador único do início ao fim do atendimento
- Sem rastreamento em tempo real para o cidadão na pista
- Único canal hoje é a voz (0800) — o WhatsApp existente pertence à ouvidoria, não ao socorro emergencial

FAIXA 2 — rótulo lateral "Visão". Texto hero centralizado, sem gráficos competindo, e 3 marcadores de apoio abaixo em fonte menor.

TEXTO HERO
- Protocolo único e rastreável do primeiro contato ao encerramento

MARCADORES DE APOIO (Faixa 2)
- Despacho automático apoiado pelo Field Service
- Entrada pelo canal que o motorista já usa: voz ou WhatsApp
- Escala real: 14 CGRs, não apenas o piloto

FAIXA 3 — rótulo lateral "Prova de valor confirmada". 4 linhas no estilo "chip de categoria" — um chip colorido à esquerda (~22% da largura) com o identificador do resultado, e o conteúdo à direita (~78%) com o nome do resultado e a dor que ele remove.

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

Style: aplicar a cor de destaque do template ao rótulo lateral de cada faixa e aos chips V1-V4. Separar as 3 faixas com uma linha fina ou leve variação de fundo entre elas. Conteúdo em estilo de corpo, alinhado verticalmente ao centro de cada linha/bloco.
```

---

### Slide 3 — Arquitetura da Solução

Nota de palco: reforçar que arquitetura é uma decisão, não uma colagem — cada produto tem um motivo de estar ali.

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

### Slide 4 — Alcance do MVP e Mapa de Capacidades

Nota de palco: âncora numérica — repetir "14, 298, 1.152, 26 capacidades" verbalmente, não só ler o slide.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: O MVP cobre toda a produção estadual — 14 CGRs, 298 viaturas, 1.152 operadores — em 26 capacidades concretas

LAYOUT: Linha de 5 stat tiles no topo (número grande + legenda abaixo de cada um), seguida de uma grade de 5 cartões (um por épico) ocupando o restante do slide. Cada cartão tem o nome do épico + tamanho como badge no topo, e a lista de sub-capacidades nomeadas como marcadores dentro do cartão. Each sub-capability goes on its own line inside its card; never concatenate them into one paragraph.

STAT TILES (5 blocos em linha)
- 14 / CGRs
- 298 / viaturas
- 1.152 / operadores de campo
- 5 / capacidades entregues em org única
- 26 / sub-capacidades nomeadas

CARTÃO 1 — E01 · Canal Digital (M)
- Abertura via WhatsApp (texto/áudio)
- Triagem automatizada pelo Agentforce
- Transbordo garantido para fila humana com contexto completo
- Criação automática de ordem de serviço e protocolo

CARTÃO 2 — E02 · Registro e Classificação (L)
- Registro multi-canal (WhatsApp/0800)
- Catálogo de 100+ subtipos
- Segunda viatura no mesmo chamado
- Reclassificação com trilha de auditoria
- Deduplicação por alerta ao C2C
- Sincronização SIGOR/SIGEO

CARTÃO 3 — E03 · Despacho Automatizado (L)
- Motor de despacho por aderência (Skills)
- Escalonamento N/N-10
- Reprocessamento automático em recusa
- Console do Dispatcher
- Alarme/escalonamento ao supervisor
- Trilha de auditoria de overrides

CARTÃO 4 — E04 · Execução em Campo (L)
- App único de Field Service Mobile
- Push nativo
- Modo offline com fila de sincronização
- Encerramento por checklist condicional
- Travas de negócio (recusa com motivo, foto, check-in geolocalizado)
- Sharing restrito à CGR de origem

CARTÃO 5 — E05 · Rastreamento e Visibilidade (L)
- Link de rastreamento para o cidadão (Experience Cloud guest)
- Mapa/Gantt do C2C com Aerial Routing
- Painel agregado para gestores (4 indicadores)
- Governança de dados de geolocalização

Style: stat tiles com números grandes na cor de destaque do template, legendas em fonte menor abaixo de cada número. Cartões com título do épico em destaque e o tamanho (M/L) como badge colorido no canto; sub-capacidades em lista com marcadores dentro do cartão.
```

---

### Slide 5 — Épicos e Casos de Uso

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

### Slide 6 — Complexidade e Tecnologia por Capacidade

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

### Slide 7 — Gaps Mapeados: Premissas, Perguntas Abertas e Fora do Escopo

Nota de palco: framear como "abrimos cada gap porque olhamos com profundidade" — mostrar os itens nomeados, não só o número 79. Se perguntarem por que duas ADRs e não mais, responder: são as duas decisões de arquitetura que realmente mudam o dimensionamento — o resto é premissa de entrega, documentada à parte.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: 79 gaps mapeados — 2 decisões de arquitetura ratificadas, 5 perguntas bloqueadoras ao DER, 7 premissas de entrega a confirmar, 6 itens deliberadamente fora do MVP

LAYOUT: Quatro blocos horizontais empilhados, cada um ocupando toda a largura do slide, com uma cor de fundo/faixa lateral distinta por categoria: Bloco A (verde), Bloco B (amarelo, contém uma tabela), Bloco C (neutro, contém uma tabela), Bloco D (roxo). Each table field below goes in its OWN cell; never concatenate a row's values into one cell. Se os quatro blocos não couberem com boa legibilidade em um único slide, divida em dois slides (7a: Blocos A+B; 7b: Blocos C+D), mantendo os mesmos títulos de bloco e o mesmo código de cores.

BLOCO A — fundo verde — "Premissas de arquitetura — ratificadas (ADR)"
- ADR 0001 — CTI/voz (Salesforce Voice/Native Telephony) fica fora do MVP; vira fase dedicada de Roadmap, no maior nível de detalhe possível, antes do vencimento do contrato de URA (Instinct) em abril/2027 e da retirada do Open CTI legado em fevereiro/2028.
- ADR 0002 — Service Cloud ENTRA no MVP, mas só para o canal WhatsApp: Agentforce Contact Center Enterprise (50 licenças), 1 fila humana única 24x7, sem skills-based routing (premissa a revalidar). Não inclui Salesforce Voice — a ADR 0001 permanece intacta.

BLOCO B — fundo amarelo — "Perguntas abertas ao DER — bloqueiam decisão de design, não o início do build" — TABELA (6 linhas: 1 cabeçalho + 5 conteúdo, 3 colunas: Gap / Área / O que está em aberto)

LINHA 1 — Cabeçalho
- Célula 1: Gap
- Célula 2: Área
- Célula 3: O que está em aberto

LINHA 2
- Célula 1: G0107
- Célula 2: E01
- Célula 3: Provisionamento de um número dedicado de WhatsApp (registro Meta Business API, homologação, dono do processo no DER/PRODESP) — o número atual da ouvidoria não pode ser reaproveitado.

LINHA 3
- Célula 1: G0305
- Célula 2: E03
- Célula 3: Overrides manuais de despacho pelo C2C sem trilha de auditoria definida — o padrão nativo (Field History Tracking) tem limite de 20 campos e retenção de 18-24 meses; não confirmado se atende à exigência de prestação de contas do Estado.

LINHA 4
- Célula 1: G0309
- Célula 2: E03
- Célula 3: Despacho por proximidade pode indicar viatura de CGR vizinha, mas cada UBA é contratada por CGR — não definido se o motor pode atribuir fora desse limite contratual.

LINHA 5
- Célula 1: G0415
- Célula 2: E02-E04
- Célula 3: Premissa de DevOps assume Salesforce CLI + desenvolvimento versionado em Git para o build (2 integrações + LWC customizado + Apex de escalonamento) — a confirmar formalmente com o cliente.

LINHA 6
- Célula 1: G0517
- Célula 2: E05
- Célula 3: Mecanismo técnico do token de uso único/expirável do link de rastreamento do cidadão assume um token Apex assinado com TTL, expirando após encerramento do chamado + buffer — a confirmar na próxima rodada de DPIA.

BLOCO C — fundo neutro — "Premissas de entrega — assumidas, com o que muda se caírem" — TABELA (8 linhas: 1 cabeçalho + 7 conteúdo, 3 colunas: Premissa / O que assumimos / Se cair…)

LINHA 1 — Cabeçalho
- Célula 1: Premissa
- Célula 2: O que assumimos
- Célula 3: Se cair…

LINHA 2
- Célula 1: Correção de localização (G0213)
- Célula 2: C2C corrige manualmente km/local antes do despacho; ajuste dispara integração síncrona com SIGEO para corrigir lat/long.
- Célula 3: Sem essa correção, o despacho por proximidade herda o erro de GPS de quem relata (ex.: "quilômetros atrás" do local real) — risco operacional direto.

LINHA 3
- Célula 1: Licenciamento do Console do Dispatcher (G0310)
- Célula 2: 12 licenças individuais (não pool por turno) — preserva granularidade de autoria na trilha de auditoria.
- Célula 3: Pool compartilhado quebraria a rastreabilidade individual de quem autorizou cada override.

LINHA 4
- Célula 1: Estratégia offline do app de campo (G0404)
- Célula 2: Briefcase prima apenas Work Order, Service Appointment e Assigned Resource em aberto; conflitos resolvidos por last-write-wins (timestamp do servidor).
- Célula 3: Sem esse recorte, o app tenta sincronizar histórico completo em trecho sem rede — risco de performance e de conflito de dados.

LINHA 5
- Célula 1: Sharing entre CGRs (G0412)
- Célula 2: Território restringe visibilidade padrão à CGR de origem; reforço cross-CGR expõe só o chamado específico, não a CGR vizinha inteira.
- Célula 3: Sem essa regra, operadores de empresas terceirizadas concorrentes veriam dados operacionais uns dos outros.

LINHA 6
- Célula 1: Token do link de rastreamento (G0506)
- Célula 2: Token de uso único vinculado ao protocolo, expirando após encerramento do chamado + buffer — mesma base de governança do G0209/G0109.
- Célula 3: Sem expiração, o link do cidadão continua expondo a posição GPS de uma equipe de campo do Estado indefinidamente.

LINHA 7
- Célula 1: Cobertura de sinal no aparelho do cidadão (G0507)
- Célula 2: Sem fallback de canal alternativo (SMS) para o cidadão sem sinal — página leve, baixo consumo de dados.
- Célula 3: Risco de falha em trecho sem rede fica aceito e registrado, não resolvido — o cidadão pode não conseguir abrir o link.

LINHA 8
- Célula 1: Última posição conhecida (G0511)
- Célula 2: Mesa do C2C e link do cidadão exibem última posição conhecida com timestamp explícito quando o GPS perde sinal.
- Célula 3: Sem esse flag, a mesa mostraria posição desatualizada como se fosse tempo real — risco de decisão operacional sobre dado errado.

BLOCO D — fundo roxo — "Fora do escopo do MVP — com destino nomeado no Roadmap"
- G0518 (Voice/CTI unificado) · G0519 (objeto Incidente nativo com merge automático) · G0520 (enforcement offline das travas) · G0521 (Portal de Parceiros para as 14 UBAs) · G0522 (Street-Level Routing/ESO) · G0523 (relatório por CGR + meta de SLA).

Style: Bloco A com fundo verde claro. Bloco B com fundo amarelo claro e a tabela contida dentro do bloco, cabeçalho da tabela destacado. Bloco C como tabela de aparência neutra com cabeçalho cinza. Bloco D com fundo roxo claro. Os quatro blocos mantêm a mesma largura e alinhamento vertical entre si.
```

---

### Slide 8 — Mapa de Riscos

Nota de palco: ser direto sobre os dois riscos vermelhos: "estes dois itens precisam de uma decisão do DER, não da Salesforce, antes do build."

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Oito riscos monitorados, dois deles bloqueiam decisão do DER antes do build

LAYOUT: Render the table below as an actual table object (Insert > Table), not text with pipe characters — each field in its own cell. Below the table, build a 2×2 quadrant matrix (Probabilidade no eixo horizontal, Impacto no eixo vertical) with the 8 risks plotted as small labeled markers; the 2 risks in the "Média/Alta probabilidade × Alto impacto" quadrant are highlighted in red with an alert icon, since they block the DER's decision before build.

TABELA DE RISCOS — 9 linhas (1 cabeçalho + 8 conteúdo), 6 colunas

LINHA 1 — Cabeçalho
- Célula 1: Risco
- Célula 2: Categoria
- Célula 3: Probabilidade
- Célula 4: Impacto
- Célula 5: Mitigação
- Célula 6: Gap relacionado

LINHA 2
- Célula 1: Trilha de auditoria de despacho sem desenho definido
- Célula 2: Governança/Auditoria
- Célula 3: Média
- Célula 4: Alto
- Célula 5: Resolver na Fase 0 — decidir entre padrão nativo e add-on Field Audit Trail antes do build do console
- Célula 6: G0305

LINHA 3
- Célula 1: Limite contratual da UBA por CGR não confirmado
- Célula 2: Contratual
- Célula 3: Média
- Célula 4: Alto
- Célula 5: Levar como pergunta bloqueadora ao DER antes de configurar o modelo de território
- Célula 6: G0309

LINHA 4
- Célula 1: Enforcement offline das travas de negócio retirado do MVP
- Célula 2: Escopo/Operacional
- Célula 3: Média
- Célula 4: Médio
- Célula 5: Validar formalmente a redução de escopo com o cliente antes do go-live — evidência ainda é capturada e sincroniza ao reconectar
- Célula 6: G0413/G0520

LINHA 5
- Célula 1: Governança de dados de geolocalização sem DPIA formal
- Célula 2: LGPD/Compliance
- Célula 3: Média
- Célula 4: Alto
- Célula 5: Nomear o DER-SP como steward (já assumido) e levar o mecanismo de token de uso único à próxima rodada formal de DPIA
- Célula 6: G0211/G0506/G0209

LINHA 6
- Célula 1: Classificação incorreta do Agentforce (pane vs. sinistro com vítimas)
- Célula 2: Qualidade do Agente de IA
- Célula 3: Baixa-Média
- Célula 4: Alto (risco de vida)
- Célula 5: Aceito como risco residual dadas as mitigações conservadoras já adotadas (transbordo obrigatório); QA contínuo do agente ainda sem dono nomeado no DER
- Célula 6: G0112

LINHA 7
- Célula 1: Known issue de licença Field Service Community para Service Appointment
- Célula 2: Técnico/Licenciamento
- Célula 3: Baixa
- Célula 4: Médio
- Célula 5: Testar esse fluxo especificamente em ambiente de build antes de escalar às 14 CGRs
- Célula 6: —

LINHA 8
- Célula 1: Conectividade intermitente em rodovia (GPS e sincronização)
- Célula 2: Infraestrutura/Física
- Célula 3: Média-Alta
- Célula 4: Médio
- Célula 5: Correção manual de km/local + integração SIGEO; sincronização por last-write-wins
- Célula 6: G0213/G0404

LINHA 9
- Célula 1: Lane AI-native sem sponsor executivo nomeado
- Célula 2: Governança do Programa
- Célula 3: —
- Célula 4: Baixo (não bloqueia o MVP)
- Célula 5: Compressão de cronograma AI-native permanece condicional — revisitar quando um sponsor operacional for identificado
- Célula 6: decisions/0033

MATRIZ 2×2 (abaixo da tabela)
- Eixo horizontal: Probabilidade (Baixa → Alta) · Eixo vertical: Impacto (Baixo → Alto)
- Quadrante superior direito (Média-Alta probabilidade / Alto impacto): destacar em vermelho, com ícone de alerta, os 2 riscos bloqueadores — trilha de auditoria de despacho (G0305) e limite contratual da UBA por CGR (G0309)
- Os demais 6 riscos posicionados no quadrante correspondente à sua combinação de probabilidade/impacto, em cor neutra

Style: tabela com cabeçalho destacado na cor de destaque do template. Matriz 2×2 com fundo sutilmente gradiente do verde (canto inferior esquerdo, baixo risco) ao vermelho (canto superior direito, alto risco); os 2 riscos bloqueadores com contorno vermelho e rótulo curto; os demais riscos como marcadores neutros com rótulo curto.
```

---

### Slide 9 — Roadmap: Cinco Fases e Linha do Tempo Visual

Nota de palco: explicar a lógica do diagrama antes de mostrar os números: "as barras semana a semana são ilustrativas — a faixa real é 16 a 30 semanas, a divisão por fase é proporcional para visualização." Nomear a janela do contrato da URA em voz alta.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Cinco fases levam a solução da fundação ao rastreamento em tempo real em 16 a 30 semanas — ilustradas semana a semana, não só nomeadas

LAYOUT: Build this as an actual visual Gantt-style diagram — not a table with pipe characters and not a bullet list. Construct a horizontal week axis from S1 to S30 (label at least S1, S5, S10, S15, S20, S25, S30) and 5 horizontal lanes stacked top to bottom, one per phase, in this order: Fase 0, Fase 1, Fase 2, Fase 3, Fase 4. Inside each lane, draw TWO overlapping horizontal bars for that phase's two scenarios:
- "Cenário compacto (16 semanas)": solid fill, positioned at that phase's compact-scenario week range.
- "Cenário estendido (30 semanas)": lighter fill or dashed outline, positioned at that phase's extended-scenario week range — it always starts at or after the compact bar's start and extends further right, since it represents the SAME phase taking longer, never a different phase.
Give each phase lane its own distinct accent color (5 colors total); within a lane, the two bars share that same hue at different styles (compact = solid/full opacity, extended = lighter/dashed border) so the two scenarios read as paired, not as different phases. Place a small flag/marker at each phase boundary, labeled with its milestone code (M0, M1, M2, M3, M4). Below the grid, add a callout box with the "Caminho crítico" text. Below that, add a small italic disclaimer box with the illustrativeness note, verbatim. Never collapse two phases into one bar, and never render the week grid as a markdown-style table.

FAIXAS (fase | cenário compacto | cenário estendido | marco de transição)
- Fase 0 — Resolução de Discovery | S1–S2 | S1–S3 | M0
- Fase 1 — Fundação (Registro e Integrações) | S3–S5 | S4–S9 | M1
- Fase 2 — Despacho e Canal Digital | S6–S8 | S10–S15 | M2
- Fase 3 — Execução em Campo | S9–S11 | S16–S20 | M3
- Fase 4 — Rastreamento e Estabilização | S12–S16 | S21–S30 | M4 (Go-live)

CONTEÚDO DOS MARCOS (texto de apoio abaixo do grid — uma linha por marco, o que cada um entrega)
- M0: gaps bloqueadores (G0305, G0309, G0517, G0415) respondidos; especificação SIGOR/SIGEO assinada; workstream de Change Management dimensionado.
- M1: Work Order criável a partir de qualquer canal; catálogo completo de Work Type; sincronização SIGOR validada; callout SIGEO testado.
- M2: despacho aciona a viatura correta nas 14 CGRs; console do Dispatcher operacional nos 4 turnos; triagem WhatsApp cria Work Order de ponta a ponta.
- M3: app de campo em operação nas 14 UBAs, travas de negócio ativas, piloto concluído antes do rollout estadual.
- M4 (Go-live): link de rastreamento e painel de gestores ativos; UAT estadual (298 viaturas, 1.152 operadores, 14 CGRs) assinado; hypercare concluído.

CAMINHO CRÍTICO (callout abaixo do grid)
- E02 → E03 → E04 → E05, com E01 correndo em paralelo a partir da Fase 2 — atraso em qualquer ponto do caminho se propaga às fases seguintes.

DISCLAIMER (caixa pequena, itálica, no rodapé — usar exatamente este texto, sem alterar uma palavra):
"A divisão semana-a-semana por fase é ilustrativa e proporcional à complexidade relativa de cada fase — não é uma data-compromisso. Só a faixa agregada (16-30 semanas) tem provenance direta; a alocação por fase distribui essa faixa de forma proporcional para visualização."

Style: 5 cores de fase distintas, consistentes com as cores usadas para os épicos nos demais slides. Barra "compacto" sólida; barra "estendido" com opacidade menor ou borda tracejada. Marcos M0-M4 como pequenas bandeiras/triângulos na fronteira entre fases, com o código do marco visível. Legenda de cores por fase em um canto do slide.
```

---

### Slide 10 — Visão de Futuro: um Roadmap que Escala

Nota de palco: este é o slide mais estratégico para o cliente sentir confiança de longo prazo — "nada aqui é um gap escondido, é uma decisão deliberada com destino."

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Seis capacidades já têm destino nomeado no Roadmap — o MVP não é um teto, é uma base que escala sem re-arquitetura

LAYOUT: Trilho horizontal de 6 cartões em sequência, na mesma identidade visual das fases do MVP (slide anterior) mas em tom mais claro/aspiracional — sinalizando que é a continuação da linha do tempo, não um problema. Cada cartão tem: título com código do gap entre parênteses, e o "por que agora não, por que depois sim" resumido. Um bloco de destaque no rodapé com a mensagem de fechamento.

CARTÃO 1 — Voz/CTI unificado (G0518, ADR 0001)
- Salesforce Voice/Native Telephony como canal de voz unificado ao WhatsApp e ao 0800. Decisão explícita do DER: preparar a decisão Open CTI vs. Salesforce Voice antes do vencimento do contrato de URA (abril/2027) e da retirada do Open CTI legado (fevereiro/2028) — no maior nível de detalhe possível, como fase própria do Roadmap.

CARTÃO 2 — Objeto Incidente nativo com deduplicação automática (G0519)
- Hoje a deduplicação é um alerta manual ao C2C (raio geográfico + janela de tempo + tipo); o objeto Incident nativo do Service Cloud (CSIM) automatiza esse merge quando o volume justificar o investimento.

CARTÃO 3 — Enforcement offline (bloqueio duro) (G0520)
- A evidência de campo (foto, check-in, motivo de recusa) já é capturada offline e sincroniza ao reconectar; o bloqueio automático de avanço sem rede exige LWC offline especializado, upgrade natural quando esse roster estiver confirmado.

CARTÃO 4 — Portal de Parceiros (G0521)
- Hoje 6 superfícies de visibilidade (cidadão, C2C, gestores, app de campo, dispatcher, Agentforce); um portal dedicado para as 14 empresas terceirizadas (UBAs) é a 7ª superfície natural, candidato a nova épica de Roadmap.

CARTÃO 5 — Street-Level Routing (ESO) (G0522)
- O MVP usa Aerial Routing nativo do Field Service para o mapa/Gantt do C2C, sem add-on; roteamento de precisão em nível de rua é um upgrade de Roadmap quando a operação pedir esse refinamento.

CARTÃO 6 — Relatório por CGR + meta de SLA (G0523)
- O painel de gestores do MVP é um artefato único com 4 indicadores agregados; relatório segmentado por CGR e uma meta formal de SLA são decisão deliberada de fase, com dono a nomear no Roadmap.

MENSAGEM DE FECHAMENTO (bloco de destaque no rodapé)
- A arquitetura de hoje já suporta cada um destes itens sem re-trabalho — não são um roadmap de correções, são a próxima onda de valor.

Style: 6 cartões em tom aspiracional (mais claro que as cores de fase usadas no slide da linha do tempo do MVP), cada um com um ícone. Mensagem de fechamento em destaque visual (fundo na cor de acento do template, texto maior) no rodapé do slide.
```

---

### Slide 11 — Adoção e Change Management

Nota de palco: deixar claro que esse plano de change management já reflete o pedido do próprio DER, não é overhead nosso — é fruto de terem pedido por escrito.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: 1.152 operadores em 14 empresas terceirizadas — por isso o DER pediu, por escrito, até dois meses de operação assistida e treinamento por persona

LAYOUT: Bloco de 3 estatísticas em linha no topo. Abaixo, duas colunas: coluna esquerda "Origem e escopo" (texto narrativo curto em marcadores), coluna direita com uma grade 2×2 de 4 cartões de entregável. Abaixo das duas colunas, uma faixa fina de linha do tempo com dois marcos conectados por uma seta ("Fase 0" → "Fases 3-4").

BLOCO DE ESTATÍSTICAS (3 números grandes em linha, cada um com legenda abaixo)
- 1.152 / operadores de campo
- 14 / empresas terceirizadas (UBAs)
- até 2 meses / de operação assistida

ORIGEM E ESCOPO (coluna esquerda, marcadores)
- O gap G0515 nasceu de uma necessidade de pesquisa de UX para a experiência de rastreamento do cidadão — dispensada porque a PoC (20/08) já validou essa experiência.
- Na mesma resolução, o DER trouxe um pedido mais amplo e explícito: até 2 meses de operação assistida (hypercare/Scale) pós-go-live, mais treinamento personalizado por persona, com foco específico nos técnicos de campo das 14 UBAs.
- Não é uma adição do time de entrega — é uma linha de esforço nomeada pelo cliente, refletida no dimensionamento do programa inteiro, não apenas do épico de rastreamento (E05).
- O risco de adoção é estrutural: 1.152 operadores terceirizados, de 14 empresas distintas, precisam adotar um único aplicativo e um único fluxo de trabalho no lugar de processos hoje fragmentados por empresa.

ENTREGÁVEIS DO WORKSTREAM (grade 2×2, coluna direita, 4 cartões)
- Cartão 1 — Currículo de treinamento por persona: trilhas distintas para o operador de campo (uso do app, travas de negócio, evidência), o programador/dispatcher (console, escalonamento N/N-10) e o gestor (painel de indicadores) — não um treinamento genérico único.
- Cartão 2 — Plano de comunicação e leitura de prontidão para a mudança: antecipando resistência nas 14 empresas terceirizadas antes do rollout estadual, não depois dele.
- Cartão 3 — Modelo de hypercare/operação assistida: canal de suporte dedicado, escalonamento definido, cadência diária nas primeiras semanas pós-go-live, por até 2 meses.
- Cartão 4 — Acompanhamento de adoção: usa o próprio painel de gestores (E05) como instrumento de leitura de adesão, não um relatório paralelo.

LINHA DO TEMPO DO WORKSTREAM (faixa fina abaixo das colunas)
- Marco 1: "Dimensionado na Fase 0" (junto aos demais gaps bloqueadores)
- Marco 2: "Executado nas Fases 3-4" — exatamente o período em que o app de campo entra em operação e o programa vai a produção estadual. Roster: função Change & Adoption (lane traditional) / Adoption Architect (lane AI-native) — 1 pessoa, regular, onshore, ativa nas fases 3-4, headcount central por causa deste pedido nomeado (G0515).

Style: bloco de estatísticas com números grandes na cor de destaque do template. 4 cartões de entregável em grade 2×2 na coluna direita. Linha do tempo do workstream como faixa fina com os dois marcos conectados por uma seta, na cor de destaque.
```

---

### Slide 12 — Investimento: Escopo Fechado e Entregáveis

Nota de palco: reforçar a palavra "fechado" — o que está na lista de entregáveis é o que está no preço; qualquer coisa fora dela é mudança de escopo, não ambiguidade.

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Este é um preço fechado por escopo — cinco capacidades, uma fase de discovery e o workstream de change management, todos entregues integralmente

LAYOUT: Checklist de entregáveis ("O que está incluído") ocupando a maior parte do slide, com um ícone de check por item, organizado por fase. Abaixo, um bloco menor e visualmente neutro, "O que não está incluído", listando os 6 itens de Roadmap futuro com seus destinos. Nenhum valor em R$ aparece neste slide — os valores completos estão no próximo slide (Investimento — ROM).

O QUE ESTÁ INCLUÍDO (checklist)
- Fase 0: resolução das 5 perguntas bloqueadoras (G0107, G0305, G0309, G0415, G0517) e dimensionamento do workstream de Change Management.
- 5 capacidades (épicos): Canal Digital (E01), Registro e Classificação (E02), Despacho Automatizado (E03), Execução em Campo (E04), Rastreamento e Visibilidade (E05) — as 26 sub-capacidades nomeadas, não uma lista aberta.
- 2 integrações: SIGOR e SIGEO, ponto a ponto, especificadas e testadas.
- Workstream de Change Management: até 2 meses de operação assistida + treinamento por persona para os 1.152 operadores das 14 UBAs.
- UAT estadual e hypercare: validação nas 14 CGRs (298 viaturas, 1.152 operadores), não apenas no piloto.

O QUE NÃO ESTÁ INCLUÍDO (bloco menor, tom neutro — decisão deliberada, não uma falha)
- Os 6 itens de Roadmap futuro (Voice/CTI, Incidente nativo, enforcement offline, Portal de Parceiros, Street-Level Routing, relatório por CGR) são explicitamente fora deste escopo fechado, com destino nomeado — qualquer expansão para esses itens é uma mudança de escopo formal, não uma reinterpretação do preço fechado.

Style: checklist com ícones de check verdes, um por linha. Bloco "não incluído" com fundo neutro/cinza claro, tom informativo, sem conotação negativa. Nenhuma tabela de valores neste slide.
```

---

### Slide 13 — Investimento (ROM): Faixas com e sem Impostos

Os valores abaixo replicam, sem alteração, as figuras da seção `## Approved Commercials` de `outputs/artifacts/presentation-outline.md` — nenhum número novo, nenhum recálculo.

#### Approved Commercials — figuras usadas neste prompt

```
Format this slide using my current template — build the layout described below.

The WORDING is final: use every line exactly as written, verbatim. Do not add, remove, rephrase, expand, or editorialize the text.

The LAYOUT is yours to build: create the text boxes, shapes, and tables needed to lay the slide out as described. Building visual structure is the job — do not just recolor existing text.

Keep the slide's existing background, color fills, logos, and footer untouched. Match the template theme only for what you ADD (fonts, accent color, spacing) — do not recolor or restyle the slide itself.

Do not reference or reproduce any attached file, PDF, or other slide. Use only the content in this prompt.

Todo o texto deve estar em português do Brasil (PT-BR). Não traduza para inglês nem para espanhol.

TITLE: Investimento indicativo por modelo de entrega, com e sem impostos

LAYOUT: Duas tabelas empilhadas verticalmente, ambas como table objects reais (Insert > Table), nunca texto com pipes. Each field below goes in its OWN cell; never concatenate a row's values into one cell. Tabela 1 (superior): rates aplicadas, 4 linhas (1 cabeçalho + 3 conteúdo) e 3 colunas. Tabela 2 (inferior): faixa de investimento por modelo de entrega, 4 linhas (1 cabeçalho + 3 conteúdo) e 4 colunas. Na Tabela 2, a linha "AI-native (condicional)" deve ter borda tracejada e etiqueta "CONDICIONAL" visível. Abaixo das duas tabelas, um bloco de texto pequeno e discreto com os três avisos abaixo, na ordem dada, sem alterar uma palavra. Um pequeno texto de referência acima das tabelas remete ao slide anterior para os entregáveis cobertos por estas figuras.

REFERÊNCIA (linha pequena acima das tabelas)
- Ver slide anterior ("Investimento: Escopo Fechado e Entregáveis") para o que estas figuras cobrem.

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

### Slide 14 — Fechamento: o Ask

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
- 1. Aprovar o escopo fechado dos 5 épicos, Fase 0 e change management, e a faixa de roadmap apresentada
- 2. Validar com a Salesforce PS as 5 perguntas bloqueadoras (Slide 7-B) na sessão de Fase 0
- 3. Iniciar a Fase 0 com o roteiro já mapeado

Style: texto hero em fonte grande, sem gráficos competindo. Os 3 passos numerados em fonte grande o suficiente para leitura à distância, com o número em destaque na cor do template.
```
