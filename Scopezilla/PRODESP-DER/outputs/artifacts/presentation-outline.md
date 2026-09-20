# Outline de Apresentação — PRODESP · DER-SP
*Gerado em 2026-09-17 23:54 -03 · Revisado em 2026-09-18 (abertura de gaps/premissas, mapa de riscos, linha do tempo visual, roadmap de futuro, seção única de visão, change management aprofundado, investimento com entregáveis mapeados) · Revisado em 2026-09-20 (CTI entra no MVP — ADR 0003/0004 —, capacidades recontadas, arquitetura de telefonia detalhada, documento reclassificado de escopo/preço fechado para validação de visão de solução)*

## Fundações Socráticas

- **Objetivo real**: o cliente sai da apresentação com escopo alinhado (MVP, arquitetura, gaps/riscos, linha do tempo, capacidades/tecnologia, roadmap) e decide seguir com a Salesforce PS — a conclusão que buscamos é "eles entenderam o que a DER precisa."
- **Audiência**: DER-SP / PRODESP / Stefanini — lideranças de processo e operação. Fluentes no processo de negócio de socorro rodoviário, já viram valor concreto na PoC de Cubatão/Taubaté. Não são técnicos de TI/plataforma.
- **Fluência**: Parcialmente fluente — nomes de produto aparecem diretos (Field Service, Agentforce, Service Cloud, WhatsApp), mas todo padrão interno (Skills, Service Territory, trilha de auditoria, CTI) é explicado em uma frase na primeira menção.
- **Big Idea**: Este projeto leva o DER a uma nova fase de escalabilidade e inovação — coloca a tecnologia em prol dos processos e, no fim da linha, do cidadão na pista.
- **Natureza do ROM**: este é um documento de **validação da visão de solução, alcance, faseamento e esforço** — cada seção de escopo abaixo é a lista de entregáveis que sustenta essa validação, o preço final e o modelo comercial são confirmados no acordo comercial aplicável, não fixados por este documento.

**Nomes de produto travados para o deck**: Field Service, Agentforce, Service Cloud, WhatsApp.

## Cadeia Lógica e Tom

- **Arco**: Situação Atual + Visão + Resultados (uma única leitura) → Caminho (arquitetura, MVP, capacidades, gaps abertos, riscos administrados) → Linha do tempo e roadmap que escala → Change Management → Fechamento com o Ask.
- **Tom**: Autoritativo — direto, baseado em evidência, sem hedging — moderado por uma leitura de "parceria" na seção de change management (é uma jornada que a equipe de 1.152 operadores faz junto) e por transparência total nos gaps: abrimos o que assumimos, não só contamos.

---

## Slide 1 — Capa

**Action Title**: PRODESP-DER: da PoC de Cubatão/Taubaté para uma nova fase de escala estadual
**Motivo**: Ancora o Big Idea antes de qualquer dado.
**Conteúdo**: Nome do programa · DER-SP · Field Service + Agentforce · data
**Visual**: Capa limpa, wordmark + big idea como subtítulo
**Densidade**: sparse
**Fonte de dados**: `.project-metadata.json`

## Slide 2 — Situação Atual, Visão de Transformação e Resultados de Valor

**Action Title**: Do atendimento fragmentado a um protocolo único e rastreável — quatro resultados de valor já confirmados com o DER
**Motivo**: O usuário pediu explicitamente que as três seções antes separadas (Situação Atual, Visão de Transformação, Resultados de Valor Confirmados) se tornem uma única leitura contínua — GAPs, visão e prova de valor em uma única leitura.
**Conteúdo** (três blocos em uma página):
1. **Situação atual**: atendimento fragmentado em chamados distintos para pedido, despacho e encerramento; sem identificador único; sem rastreamento em tempo real para o cidadão na pista; único canal hoje é a voz (0800) — o WhatsApp existente pertence à ouvidoria, não ao socorro emergencial.
2. **Visão de transformação**: Protocolo único e rastreável do primeiro contato ao encerramento. Despacho automático apoiado pelo Field Service e múltiplos canais de entrada de uso cotidiano do cidadão — voz ou WhatsApp.
3. **Resultados de valor confirmados** (V1-V4): **V1** Protocolo único e rastreável do pedido ao encerramento · **V2** Canal digital complementar ao 0800 — remove a dependência exclusiva da voz, trazendo alternativas de contato quando a voz não está disponível · **V3** Despacho automatizado com governança de exceção — elimina a gestão manual da operação pelo C2C, sem regras sistemáticas de aderência/disponibilidade/proximidade, que sobrecarrega a mesa com atividades processuais que um sistema poderia executar · **V4** Auditabilidade do ciclo de atendimento — ganha-se uma trilha de auditoria obrigatória que facilita a prestação de contas a órgãos de controle do Estado.
**Visual**: Três faixas horizontais empilhadas (Hoje → Visão → Prova), a terceira com 4 linhas categoria-chip (chip = V#, conteúdo = outcome + dor removida) — a leitura visual é uma progressão, não três slides colados.
**Densidade**: dense
**Fonte de dados**: `strategy.json.business_outcomes[]` (V1-V4), `strategy.json.transformation_strategy.vision_statement`, `executive-summary.md` Visão Geral.

## Slide 3 — Arquitetura da Solução

**Action Title**: Uma única arquitetura: o Field Service comanda o despacho, o Agentforce atende WhatsApp e telefonia via CTI
**Motivo**: É a prova técnica (em linguagem de negócio) de que a solução é coerente, não uma colagem de produtos. `Experience Cloud` sai da lista de módulos independentes — não é um produto com licença própria neste desenho, é um template/capacidade que vive dentro da licença de Field Service (`[KA-6140]`), usado apenas onde o Field Service precisa de uma superfície externa (o link de rastreamento do cidadão, E05).
**Conteúdo**: Org única Salesforce · **Field Service** como motor central de despacho (Work Order/Service Appointment/Service Territory, motor de agendamento e otimização) e como origem do site de rastreamento do cidadão via seu template de Experience Cloud embutido e do **Appointment Assistant** nativo (E05) · **Agentforce (Contact Center Enterprise)** cobrindo os dois canais de entrada — WhatsApp e a integração CTI com a URA — com transbordo garantido para fila humana via **Omni-Channel** (`[KA-18817]`), preservando contexto e, no caso da CTI, o screen-pop da chamada · **Service Cloud** como a camada de atendimento que hospeda esse console/fila (Digital Engagement + Service Console) · duas integrações com os sistemas legados SIGOR/SIGEO. O **Visual Remote Assistant** (`[KA-6156]`) é outra extensão nativa do mesmo pacote de Field Service — não há caso de uso mapeado neste discovery para incluí-lo no MVP, citado aqui só para deixar o inventário de capacidades completo e nomeado.
**Visual**: Dois diagramas.
1. **Arquitetura em camadas / hub-and-spoke** (mantido, capacidades corrigidas) — Salesforce (org única) no centro, com Field Service/Agentforce/Service Cloud como módulos, o Experience Cloud representado como uma etiqueta *dentro* do módulo Field Service (não um módulo próprio), e SIGOR/SIGEO como sistemas externos alimentando/recebendo dados.
2. **Novo — Fluxo de telefonia e atendimento, do 0800 ao Service Console** (diagrama instrutivo, não técnico, para quem não conhece o fluxo de telefonia/atendimento): ver detalhamento abaixo.

### Diagrama 2 — Fluxo de telefonia e atendimento (0800 → PABX → URA → agente de IA → Service Console)

Sequência da esquerda para a direita, com dois ramos de derivação ao final:

1. **Cidadão liga para o 0800** — a operadora de telefonia (a mesma linha 0800 055 5510 hoje operada pela Instinct) recebe a chamada.
2. **PABX** (on-premise ou virtual, a depender do fornecedor de telefonia vigente na hora do build — `data/gaps.json` G0524) roteia a chamada para a URA.
3. **URA** atende e apresenta o menu/fluxo de voz.
4. **Agente de IA operando a URA** conduz a conversa com o cidadão (linguagem natural ou menu, a depender da capacidade da URA vigente) e tenta identificar a natureza do contato. A partir daqui, três desfechos:
   - **(a) Atendimento resolvido na própria URA** — o cidadão tem a resposta (ex.: informação, confirmação de protocolo já aberto) e desliga, sem transbordo.
   - **(b) Derivação para uma área interna do DER** — ex.: o cidadão liga sobre multas; a URA deriva a chamada para o departamento correto dentro do DER, fora do fluxo de socorro emergencial e fora deste programa.
   - **(c) Derivação para o fluxo emergencial** — a URA identifica uma emergência (pane/sinistro na pista) e deriva a chamada para um **agente especialista de emergência** (atendimento humano especializado, primeira linha do socorro rodoviário).
5. **Transbordo com contexto para o Service Console** — o agente especialista de emergência aciona a integração **CTI** (`decisions/0003`; padrão exato a confirmar — `data/gaps.json` G0524), que apresenta ao atendente no **Service Console do Salesforce** um **screen-pop**: contexto completo da chamada (número, transcrição/resumo da URA quando disponível, natureza identificada) já carregado — o atendente não repete perguntas que o cidadão já respondeu à URA.
6. A partir daqui, o fluxo entra no processo já coberto pela arquitetura em camadas acima: Service Cloud cria a ordem de serviço/protocolo, Field Service assume o despacho.

Grounding: o mecanismo de screen-pop com contexto de chamada é um padrão documentado (`[KA-0188]` "Integrate Open CTI with Lightning Flow for Service" — screen-pop a partir de dados de chamada); o padrão técnico exato de CTI usado no build (Open CTI remanescente vs. um caminho equivalente) não é fixado nesta fase, consistente com `decisions/0003`.
**Densidade**: dense
**Fonte de dados**: `outputs/01-solution.md`, `data/epics.json` (capabilities), `decisions/0003`, `data/gaps.json` (G0524), `[KA-6140]`, `[KA-6156]`, `[KA-18817]`, `[KA-0188]`

## Slide 4 — Alcance do MVP e Mapa de Capacidades

**Action Title**: O MVP cobre toda a produção estadual em 21 capacidades concretas, organizadas em 4 frentes tecnológicas
**Motivo**: Fecha "isso é só o piloto?" com escala real, e mostra o alcance da solução em capacidades nomeadas, não só em nomes de épico — visão real do que é entregue, não uma etiqueta genérica.
**Conteúdo**: 14 CGRs · 298 viaturas · 1.152 operadores de campo, — o MVP já é a escala real do DER. 4 frentes tecnológicas (Field Service, Agentforce, Service Cloud, WhatsApp) entregues integralmente pela Salesforce PS, em org única, totalizando 21 sub-capacidades nomeadas nos 5 épicos:
- **E01 — Canal Digital (M)**: abertura de chamado via WhatsApp (texto/áudio) e telefonia (CTI) · triagem automatizada pelo Agentforce · transbordo garantido para fila humana via Omni-Channel, com contexto completo (incluindo screen-pop de CTI) · criação automática de ordem de serviço e protocolo.
- **E02 — Registro e Classificação (L)**: registro do chamado multi-canal (WhatsApp/0800/CTI) · catálogo de classificação (100+ subtipos) · qualificação do chamado e da ordem de campo pelo Agentforce/Atendente · deduplicação por alerta ao C2C · integração de sincronização SIGOR/SIGEO.
- **E03 — Despacho Automatizado (L)**: motor de agendamento e otimização (Field Service) · reprocessamento automático em recusa · console do Dispatcher (Gantt/Mesa) · alarme e escalonamento ao supervisor da CGR · trilha de auditoria.
- **E04 — Execução em Campo (L)**: aplicativo único de Field Service Mobile · recebimento de despacho via push nativo · modo offline com fila de sincronização · encerramento com formulário, quando aplicável · travas de negócio (recusa com motivo, foto, check-in geolocalizado).
- **E05 — Rastreamento e Visibilidade (L)**: rastreamento do cidadão via Appointment Assistant (Field Service) · painel agregado para gestores (4 indicadores).
**Visual**: Linha de stat tiles (14 / 298 / 1.152 / 4 / 21) + grade capacidade×épico (5 colunas, uma por épico, cada célula lista suas sub-capacidades) — a mesma grade que alimenta o mapa de capacidades interno do projeto.
**Densidade**: dense
**Fonte de dados**: `.project-metadata.json.geographic_scope`, `data/epics.json` (campo `capabilities[]`, 21 itens nomeados no total), `executive-summary.md` Escopo.

## Slide 5 — Complexidade e Tecnologia por Capacidade

**Action Title**: Quatro das cinco capacidades concentram alta complexidade — despacho e mobilidade de campo puxam o esforço
**Motivo**: Mostra honestidade sobre onde está o esforço real, sem inflar nem esconder.
**Conteúdo**: Canal Digital (M) · Registro e Classificação (L) · Agendamento e Otimização Automatizados (L) · Execução em Campo (L) · Rastreamento em Tempo Real (L) — tecnologia por capacidade: Registro e Classificação = qualificação de caso e ordem de serviço, este último com um catálogo com mais de 100 subtipos de tipos de ocorrências; Agendamento e Otimização Automatizados = motor de inteligência do Field Service que leva em consideração as regras de trabalho e políticas estabelecidas pelo cliente; Execução em Campo = app único de Field Service Mobile; Rastreamento em Tempo Real = Appointment Assistant.
**Visual**: Distribuição de tamanhos (1 M, 4 L) + tabela capacidade→tecnologia
**Densidade**: dense
**Fonte de dados**: `data/estimates.json` (t_shirt_size), `outputs/01-solution.md`

## Slide 6 — Gaps Mapeados: Premissas, Perguntas Abertas e Fora do Escopo

**Action Title**: 80 gaps mapeados — 2 decisões de arquitetura ratificadas, 5 perguntas bloqueadoras ao DER, 7 premissas de entrega a confirmar, 6 itens deliberadamente fora do MVP
**Motivo**: O usuário pediu explicitamente para **abrir** os gaps mapeados, não só contá-los — cada categoria abaixo nomeia o item real, não uma estatística. Modelo estrutural: a seção "Premissas & Fora do Escopo" do ROM de referência (DATAPREV-PAT), adaptada às premissas e ADRs reais deste projeto.
**Conteúdo** (quatro blocos, nesta ordem):

**(A) Premissas de arquitetura — ratificadas (ADR)**
- **ADR 0003** (substitui a ADR 0001) — a integração **CTI com a URA ENTRA no MVP**: acionamento de chamada/caso a partir da URA (atual, vendor Instinct, ou uma futura substituta), com contexto/screen-pop ao atendente no Service Console. O padrão técnico exato não é fixado nesta ADR — a Open CTI clássica está em descontinuação pela Salesforce (retirada prevista fevereiro/2028), então o padrão a usar é uma premissa a validar (G0524), não um fato assumido. Fica **fora** do MVP o Salesforce Voice (telefonia nativa) e a substituição da própria URA/0800 — projeto de infraestrutura de telefonia separado, ainda em viabilização entre DER e PRODESP.
- **ADR 0004** (substitui a ADR 0002) — Service Cloud ENTRA no MVP para dois canais: WhatsApp (Agentforce Contact Center Enterprise, 1 fila humana única 24x7, sem skills-based routing — premissa a revalidar) e telefonia via CTI (per ADR 0003), com screen-pop no transbordo. Não inclui Salesforce Voice.

**(B) Perguntas abertas ao DER — bloqueiam decisão de design, não o início do build**
| Gap | Área | O que está em aberto |
|---|---|---|
| G0107 | E01 | Provisionamento de um número dedicado de WhatsApp (registro Meta Business API, homologação, dono do processo no DER/PRODESP) — o número atual da ouvidoria não pode ser reaproveitado. |
| G0305 | E03 | Overrides manuais de despacho pelo C2C sem trilha de auditoria definida — o padrão nativo (Field History Tracking) tem limite de 20 campos e retenção de 18-24 meses; não confirmado se atende à exigência de prestação de contas do Estado. |
| G0309 | E03 | Despacho por proximidade pode indicar viatura de CGR vizinha, mas cada UBA é contratada por CGR — não definido se o motor pode atribuir fora desse limite contratual. |
| G0415 | E02-E04 | Premissa de DevOps assume Salesforce CLI + desenvolvimento versionado em Git para o build (2 integrações + LWC customizado + Apex de escalonamento) — a confirmar formalmente com o cliente. |
| G0524 | E01-E03 | Padrão técnico exato da integração CTI com a URA — a Open CTI clássica está descontinuada pela Salesforce (indisponível para orgs Agentforce Service recém-criados, retirada fev/2028); depende de (i) a data de criação do org do DER frente a esse corte e (ii) qual API de CTI o fornecedor de telefonia expõe. |

**(C) Premissas de entrega — assumidas, com o que muda se caírem**
| Premissa | O que assumimos | Se cair… |
|---|---|---|
| Correção de localização (G0213) | C2C corrige manualmente km/local antes do despacho; ajuste dispara integração síncrona com SIGEO para corrigir lat/long. | Sem essa correção, o despacho por proximidade herda o erro de GPS de quem relata (ex.: "quilômetros atrás" do local real) — risco operacional direto. |
| Licenciamento do Console do Dispatcher (G0310) | 12 licenças individuais (não pool por turno) — preserva granularidade de autoria na trilha de auditoria. | Pool compartilhado quebraria a rastreabilidade individual de quem autorizou cada override. |
| Estratégia offline do app de campo (G0404) | Briefcase prima apenas Work Order, Service Appointment e Assigned Resource em aberto; conflitos resolvidos por last-write-wins (timestamp do servidor). | Sem esse recorte, o app tenta sincronizar histórico completo em trecho sem rede — risco de performance e de conflito de dados. |
| Sharing entre CGRs (G0412) | Território restringe visibilidade padrão à CGR de origem; reforço cross-CGR expõe só o chamado específico, não a CGR vizinha inteira. | Sem essa regra, operadores de empresas terceirizadas concorrentes veriam dados operacionais uns dos outros. |
| Token do link de rastreamento (G0506) | Token de uso único vinculado ao protocolo, expirando após encerramento do chamado + buffer — mesma base de governança do G0209/G0109. | Sem expiração, o link do cidadão continua expondo a posição GPS de uma equipe de campo do Estado indefinidamente. |
| Cobertura de sinal no aparelho do cidadão (G0507) | Sem fallback de canal alternativo (SMS) para o cidadão sem sinal — página leve, baixo consumo de dados. | Risco de falha em trecho sem rede fica aceito e registrado, não resolvido — o cidadão pode não conseguir abrir o link. |
| Última posição conhecida (G0511) | Mesa do C2C e link do cidadão exibem última posição conhecida com timestamp explícito quando o GPS perde sinal. | Sem esse flag, a mesa mostraria posição desatualizada como se fosse tempo real — risco de decisão operacional sobre dado errado. |

**(D) Fora do escopo do MVP — com destino nomeado no Roadmap** (ver Slide 9 para o desenvolvimento completo)
G0518 (Salesforce Voice / substituição nativa da URA do 0800 — projeto de infraestrutura separado, distinto da integração CTI que entra no MVP via ADR 0003) · G0519 (objeto Incidente nativo com merge automático) · G0520 (enforcement offline das travas) · G0521 (Portal de Parceiros para as 14 UBAs) · G0522 (Street-Level Routing/ESO) · G0523 (relatório por CGR + meta de SLA).

**Visual**: Quatro cartões coloridos empilhados — verde (A, ratificado), amarelo (B, a confirmar), tabela neutra (C, aceito com consequência), roxo (D, fora do escopo com destino) — mesmo código de cores do ROM de referência (DATAPREV-PAT).
**Densidade**: dense
**Fonte de dados**: `decisions/0003`, `decisions/0004`, `data/gaps.json` (80 linhas — 5 `Open*`, 7 `Premise Accepted*`, 6 `Out of Scope`, resto resolvido).

## Slide 7 — Mapa de Riscos

**Action Title**: Oito riscos monitorados, dois deles bloqueiam decisão do DER antes do build
**Motivo**: O usuário pediu explicitamente um mapa de risco — não existia um `risks.json` neste projeto, então este mapa é sintetizado das categorias `Potential Risk`/`Source Conflict` de `gaps.json`, da seção de Riscos já escrita em `executive-summary.md`, e do documento interno de governança agêntica (`knowledge/latam-agentic-governance-services.md`), que mapeia especificamente 6 riscos de governança de IA a estes gaps.
**Conteúdo**:
| Risco | Categoria | Probabilidade | Impacto | Mitigação | Gap relacionado |
|---|---|---|---|---|---|
| Trilha de auditoria de despacho sem desenho definido | Governança/Auditoria | Média | Alto | Resolver na Fase 0 — decidir entre padrão nativo e add-on Field Audit Trail antes do build do console | G0305 |
| Limite contratual da UBA por CGR não confirmado | Contratual | Média | Alto | Levar como pergunta bloqueadora ao DER antes de configurar o modelo de território | G0309 |
| Enforcement offline das travas de negócio retirado do MVP | Escopo/Operacional | Média | Médio | Validar formalmente a redução de escopo com o cliente antes do go-live — evidência ainda é capturada e sincroniza ao reconectar | G0413/G0520 |
| Governança de dados de geolocalização sem DPIA formal | LGPD/Compliance | Média | Alto | Nomear o DER-SP como steward (já assumido) e levar o mecanismo de token de uso único à próxima rodada formal de DPIA | G0211/G0506/G0209 |
| Classificação incorreta do Agentforce (pane vs. sinistro com vítimas) | Qualidade do Agente de IA | Baixa-Média | Alto (risco de vida) | Aceito como risco residual dadas as mitigações conservadoras já adotadas (transbordo obrigatório); QA contínuo do agente ainda sem dono nomeado no DER | G0112 |
| Known issue de licença Field Service Community para Service Appointment | Técnico/Licenciamento | Baixa | Médio | Testar esse fluxo especificamente em ambiente de build antes de escalar às 14 CGRs | — |
| Conectividade intermitente em rodovia (GPS e sincronização) | Infraestrutura/Física | Média-Alta | Médio | Correção manual de km/local + integração SIGEO; sincronização por last-write-wins | G0213/G0404 |
| Lane AI-native sem sponsor executivo nomeado | Governança do Programa | — | Baixo (não bloqueia o MVP) | Compressão de cronograma AI-native permanece condicional — revisitar quando um sponsor operacional for identificado | `decisions/0033` |
**Visual**: Matriz 2×2 (probabilidade × impacto) com os 8 riscos posicionados, os 2 riscos "Alto/Média" (auditoria, UBA) destacados em vermelho como bloqueadores de decisão.
**Densidade**: dense
**Fonte de dados**: `data/gaps.json` (categorias `Potential Risk` e `Source Conflict`), `executive-summary.md` Riscos e Mitigações, `knowledge/latam-agentic-governance-services.md`.

## Slide 8 — Roadmap: Cinco Fases e Linha do Tempo Visual

**Action Title**: Cinco fases levam a solução da fundação ao rastreamento em tempo real em 16 a 31 semanas — ilustradas semana a semana, não só nomeadas
**Motivo**: O usuário pediu um diagrama visual de fato representando as semanas, com as etapas baseadas na metodologia de entrega PS Salesforce e os marcos de entrega mais importantes — não uma tabela de fases.
**Conteúdo**: Diagrama estilo Gantt em grade de semanas (S1 a S31), com duas barras por fase — cenário compacto (16 semanas) e cenário estendido (31 semanas) — ilustrando a faixa derivada, nunca uma data-compromisso:

| Fase | Cenário compacto (16 sem.) | Cenário estendido (31 sem.) | Épicos | O que o marco de fim de fase entrega |
|---|---|---|---|---|
| Fase 0 — Resolução de Discovery | S1–S2 | S1–S3 | — | **M0**: gaps bloqueadores (G0305, G0309, G0524, G0415) respondidos; especificação SIGOR/SIGEO assinada; workstream de Change Management dimensionado. |
| Fase 1 — Fundação (Registro e Integrações) | S3–S5 | S4–S9 | E02 | **M1**: Work Order criável a partir de qualquer canal; catálogo completo de Work Type; sincronização SIGOR validada; callout SIGEO testado. |
| Fase 2 — Despacho e Canal Digital | S6–S8 | S10–S15 | E03, E01 | **M2**: despacho aciona a viatura correta nas 14 CGRs; console do Dispatcher operacional nos 4 turnos; triagem WhatsApp e telefonia via CTI criam Work Order de ponta a ponta. |
| Fase 3 — Execução em Campo | S9–S11 | S16–S20 | E04 | **M3**: app de campo em operação nas 14 UBAs, travas de negócio ativas, piloto concluído antes do rollout estadual. |
| Fase 4 — Rastreamento e Estabilização | S12–S16 | S21–S31 | E05 | **M4 (Go-live)**: rastreamento via Appointment Assistant e painel de gestores ativos; UAT estadual (298 viaturas, 1.152 operadores, 14 CGRs) assinado; hypercare concluído. |

**Caminho crítico**: E02 → E03 → E04 → E05, com E01 correndo em paralelo a partir da Fase 2 — atraso em qualquer ponto do caminho se propaga às fases seguintes.
**Metodologia**: as 5 fases seguem a sequência recomendada de setup do Field Service (Work Order Management → Workforce/Scheduling → execução em campo → visibilidade), citada em `[KA-6240]` — não uma estrutura genérica de projeto.
**Disclaimer no próprio diagrama**: a divisão semana-a-semana por fase é **ilustrativa e proporcional à complexidade relativa de cada fase** — não é uma data-compromisso. Só a faixa agregada (16-31 semanas) e os 3 range drivers nomeados (`.project-metadata.json.timeline.derived`) têm provenance direta; a alocação por fase distribui essa faixa de forma proporcional para visualização, e é sinalizada como tal no próprio gráfico (ex.: "ilustrativo — confirmar no planejamento detalhado da Fase 0").
**Visual**: Grade CSS de 31 colunas (uma por semana) × 5 faixas (uma por fase), cada faixa com duas barras semi-transparentes sobrepostas (compacto sólido, estendido tracejado/mais claro), marcos M0-M4 como bandeiras na semana de transição de fase; legenda de cores por fase; caixa de "Caminho crítico" em prosa abaixo da grade — modelo estrutural: seção "Linha do Tempo & Marcos" do ROM de referência (DATAPREV-PAT), adaptada de datas fixas para números de semana + duas barras de cenário (porque este projeto não tem data de início comprometida, só uma faixa de 16-31 semanas).
**Densidade**: dense
**Fonte de dados**: `data/roadmap.json` (fases, objetivos, success_criteria — grão real do projeto, sem `duration_weeks` fabricado), `.project-metadata.json.timeline.derived` (16-31 semanas, 3 range drivers), `[KA-6240]`.

## Slide 9 — Visão de Futuro: um Roadmap que Escala

**Action Title**: Seis capacidades já têm destino nomeado no Roadmap — o MVP não é um teto, é uma base que escala sem re-arquitetura
**Motivo**: O usuário pediu explicitamente que a visão de itens de roadmap fosse incluída de forma atraente ao cliente — mostrando que o plano escala para o futuro, não que faltou algo no MVP. Cada item abaixo tem uma razão deliberada de fasing e um destino nomeado, nunca um "gap" apresentado como falha.
**Conteúdo** (6 capacidades de futuro, cada uma com o motivo da decisão de fasing):
1. **Salesforce Voice / substituição da URA do 0800** (G0518, ADR 0003) — a integração CTI com a URA já entra no MVP (ver Slide 3/6); o que fica de fora é a telefonia nativa (Salesforce Voice) e a substituição da própria URA/0800 — projeto de infraestrutura de telefonia ainda em viabilização entre DER e PRODESP, distinto deste programa. Janela relevante: contrato atual de URA (Instinct) expira abril/2027; retirada da Open CTI legada prevista para fevereiro/2028.
2. **Objeto Incidente nativo com deduplicação automática** (G0519) — hoje a deduplicação é um alerta manual ao C2C (raio geográfico + janela de tempo + tipo); o objeto `Incident` nativo do Service Cloud (CSIM) automatiza esse merge quando o volume justificar o investimento.
3. **Enforcement offline (bloqueio duro)** (G0520) — a evidência de campo (foto, check-in, motivo de recusa) já é capturada offline e sincroniza ao reconectar; o bloqueio automático de avanço sem rede exige LWC offline especializado, upgrade natural quando esse roster estiver confirmado.
4. **Portal de Parceiros** (G0521) — hoje 6 superfícies de visibilidade (cidadão, C2C, gestores, app de campo, dispatcher, Agentforce); um portal dedicado para as 14 empresas terceirizadas (UBAs) é a 7ª superfície natural, candidato a nova épica de Roadmap.
5. **Street-Level Routing (ESO)** (G0522) — o MVP usa Aerial Routing nativo do Field Service para o mapa/Gantt do C2C, sem add-on; roteamento de precisão em nível de rua é um upgrade de Roadmap quando a operação pedir esse refinamento.
6. **Relatório por CGR + meta de SLA** (G0523) — o painel de gestores do MVP é um artefato único com 4 indicadores agregados; relatório segmentado por CGR e uma meta formal de SLA são decisão deliberada de fase, com dono a nomear no Roadmap.
**Visual**: Linha do tempo estendida à direita da linha do tempo do MVP (Slide 8) — um "trilho de futuro" com 6 cartões na mesma identidade visual das fases do MVP, mas em tom mais claro/aspiracional, cada um com ícone + título + "por que agora não, por que depois sim". Mensagem de fechamento do slide: "a arquitetura de hoje já suporta cada um destes itens sem re-trabalho — não são um roadmap de correções, são a próxima onda de valor."
**Densidade**: balanced
**Fonte de dados**: `data/gaps.json` (categoria `Out of Scope`, G0518-G0523), `decisions/0003`.

## Slide 10 — Adoção e Change Management

**Action Title**: 1.152 operadores em 14 empresas terceirizadas — por isso o DER pediu, por escrito, até dois meses de operação assistida e treinamento por persona
**Motivo**: O usuário pediu para explorar mais profundamente o change management — escopo, entregáveis e metodologia — e não tratá-lo como um parágrafo de encerramento. O workstream é um pedido nomeado do próprio DER (não uma adição do time de entrega), e a análise a seguir consolida conteúdo já presente em 9+ arquivos do projeto (epics, gaps, roadmap, estimate-comparison, resource-plan, delivery-plan, executive-summary) numa única leitura.
**Conteúdo**:

**Origem e escopo**: o gap `G0515` nasceu de uma necessidade de pesquisa de UX para a experiência de rastreamento do cidadão — dispensada porque a PoC (20/08) já validou essa experiência. Mas na mesma resolução, o DER trouxe um pedido mais amplo e explícito: até **2 meses de operação assistida (hypercare/Scale)** pós-go-live, mais **treinamento personalizado por persona**, com foco específico nos técnicos de campo das 14 UBAs — não uma adição do time de entrega, é uma linha de esforço nomeada pelo cliente, refletida no dimensionamento do programa inteiro, não apenas do épico de rastreamento (E05).

**Por que este escopo, e não outro**: o risco de adoção é estrutural, não incidental — 1.152 operadores terceirizados, de 14 empresas distintas, precisam adotar um único aplicativo e um único fluxo de trabalho no lugar de processos hoje fragmentados por empresa. O canal digital (WhatsApp) é complemento à voz, não substituto — reduz o risco de excluir o cidadão que só confia na ligação, mesma lógica aplicada à adoção interna: nenhuma mudança de processo é "só tecnologia".

**Entregáveis do workstream**:
- **Currículo de treinamento por persona** — trilhas distintas para o operador de campo (uso do app, travas de negócio, evidência), o programador/dispatcher (console, escalonamento N/N-10) e o gestor (painel de indicadores) — não um treinamento genérico único.
- **Plano de comunicação e leitura de prontidão para a mudança** — antecipando resistência nas 14 empresas terceirizadas antes do rollout estadual, não depois dele.
- **Modelo de hypercare/operação assistida** — canal de suporte dedicado, escalonamento definido, cadência diária nas primeiras semanas pós-go-live, por até 2 meses.
- **Acompanhamento de adoção** — usa o próprio painel de gestores (E05) como instrumento de leitura de adesão, não um relatório paralelo.

**Metodologia e dimensionamento**: o workstream é dimensionado na **Fase 0** (junto aos demais gaps bloqueadores) e sua execução atravessa as **Fases 3-4** — exatamente o período em que o app de campo entra em operação e o programa vai a produção estadual. No roster, aparece como a função **Change & Adoption** (lane traditional) / **Adoption Architect** (lane AI-native) — 1 pessoa, regular, onshore, ativa nas fases 3-4, com a justificativa citando `G0515` explicitamente: é headcount central *por causa* deste pedido nomeado, não um papel padrão que entraria de qualquer forma.

**O que já está resolvido, e não precisa de trabalho adicional**: a experiência do cidadão (link de rastreamento) já foi validada na PoC (20/08) — não é reaberta como pesquisa de UX formal.

**Visual**: Linha do tempo do workstream (dimensiona na Fase 0, executa nas Fases 3-4) + 4 cartões de entregável (treinamento por persona / comunicação / hypercare / adoção) + stat tile (1.152 operadores / 14 empresas / até 2 meses).
**Densidade**: dense
**Fonte de dados**: `data/gaps.json` (G0515), `data/epics.json` (E05, descrição), `data/roadmap.json` (Fase 0 objectives/success_criteria, Fase 3-4), `data/estimate-comparison.json` (linha AN-04, Change & Adoption/Adoption Architect), `outputs/02-delivery-plan.md`, `outputs/01-solution.md`, `executive-summary.md` Esforço e Disciplinas.

## Slide 11 — Investimento Indicativo e Entregáveis Mapeados

**Action Title**: A faixa de investimento indicativo cobre um conjunto de entregáveis mapeado e nomeado — cinco capacidades, uma fase de discovery e o workstream de change management
**Motivo**: Este ROM é um documento de validação da visão de solução, alcance, faseamento e esforço — o que está mapeado abaixo precisa estar claro na validação da proposta, não apenas a faixa de investimento. O preço final e o modelo comercial são confirmados no acordo comercial aplicável, não fixados por este documento. Ver a seção `## Approved Commercials` abaixo para as figuras completas (rates, faixas por lane) — esta seção nomeia os entregáveis que essas figuras cobrem.
**Conteúdo**: a faixa de investimento indicativo cobre a entrega de:
- **Fase 0** — resolução das 5 perguntas bloqueadoras (G0107, G0305, G0309, G0415, G0524) e dimensionamento do workstream de Change Management.
- **5 capacidades (épicos)** — Canal Digital (E01), Registro e Classificação (E02), Despacho Automatizado (E03), Execução em Campo (E04), Rastreamento e Visibilidade (E05) — as 21 sub-capacidades nomeadas na Slide 4, não uma lista aberta.
- **2 integrações** — SIGOR e SIGEO, ponto a ponto, especificadas e testadas.
- **Workstream de Change Management** — até 2 meses de operação assistida + treinamento por persona para os 1.152 operadores das 14 UBAs (Slide 10).
- **UAT estadual e hypercare** — validação nas 14 CGRs (298 viaturas, 1.152 operadores), não apenas no piloto.
**O que não está mapeado** (e por quê — ver Slide 9): os 6 itens de Roadmap futuro (Salesforce Voice/substituição da URA, Incidente nativo, enforcement offline, Portal de Parceiros, Street-Level Routing, relatório por CGR) ficam fora deste alcance, com destino nomeado — qualquer decisão de trazê-los para dentro é uma mudança de escopo a validar formalmente, não uma reinterpretação da faixa indicativa.
**Visual**: Lista de entregáveis em formato de checklist (o que está mapeado) ao lado da tabela de faixas por lane (ver `## Approved Commercials`).
**Densidade**: dense
**Fonte de dados**: `data/roadmap.json` (success_criteria por fase — a lista de entregáveis concretos), `data/gaps.json` (Out of Scope), `## Approved Commercials` abaixo (figuras).

## Slide 12 — Fechamento: o Ask

**Action Title**: Fechar agora leva o DER a uma nova fase de escalabilidade e inovação — a tecnologia em prol do processo e do cidadão
**Motivo**: Repete o Big Idea como último pensamento na sala e converte em três ações concretas.
**Conteúdo**: Ask em 3 passos: (1) validar a visão de solução, o alcance dos 5 épicos, a Fase 0 e o change management apresentados; (2) validar com Salesforce PS as 5 perguntas bloqueadoras (Slide 6-B) na sessão de Fase 0; (3) iniciar a Fase 0 com o roteiro já mapeado.
**Visual**: Big Idea repetida como hero + 3 bullets de ask numerados
**Densidade**: sparse
**Fonte de dados**: `executive-summary.md` Próximos Passos e Recomendações

---

## Notas de Palco (resumo por slide)

1. Abrir com confiança — este é o resultado da PoC, não uma nova venda.
2. Não passar rápido demais — esta é a leitura completa de dor, visão e prova em uma página; deixar cada bloco assentar antes de avançar ao próximo.
3. Reforçar: arquitetura é uma decisão, não uma colagem — cada produto tem um motivo de estar ali.
4. Âncora numérica — repetir "14, 298, 1.152, 21 capacidades" verbalmente, não só ler o slide.
5. Honestidade aqui gera confiança — "sim, é complexo, e sabemos exatamente onde".
6. Framear como "abrimos cada gap porque olhamos com profundidade" — mostrar os itens nomeados, não só o número 80. Se perguntarem por que duas ADRs e não mais, responder: são as duas decisões de arquitetura que realmente mudam o dimensionamento — o resto é premissa de entrega, documentada à parte.
7. Ser direto sobre os dois riscos vermelhos: "estes dois itens precisam de uma decisão do DER, não da Salesforce, antes do build."
8. Explicar a lógica do diagrama antes de mostrar os números: "as barras semana a semana são ilustrativas — a faixa real é 16 a 31 semanas, a divisão por fase é proporcional para visualização." Nomear a janela do contrato da URA em voz alta.
9. Este é o slide mais estratégico para o cliente sentir confiança de longo prazo — "nada aqui é um gap escondido, é uma decisão deliberada com destino."
10. Deixar claro: esse plano de change management já reflete o pedido do próprio DER, não é overhead nosso — é fruto de terem pedido por escrito.
11. Reforçar que este é um documento de validação — o que está na lista de entregáveis é o que sustenta a faixa de investimento indicativa; qualquer coisa fora dela é mudança de escopo a validar formalmente, não ambiguidade.
12. Terminar em silêncio após o ask — não preencher o espaço, deixar a decisão ser deles.

---

## Reclassificação: este artefato é o ROM

Confirmado com o usuário — o entregável final não é só um deck de venda, é o **ROM (Rough Order of Magnitude)** de PRODESP-DER: o documento único que leva escopo, arquitetura, gaps/riscos, linha do tempo, épicos/casos de uso e investimento ao cliente para decisão de fechamento. Estrutura de navegação adotada, seguindo o padrão de ROM já usado em `DATAPREV-PAT/outputs/artifacts/rom-cliente.html`:

1. **Visão Executiva** — Capa, Situação Atual + Visão + Resultados de Valor (Slides 1-2)
2. **Arquitetura & Solução** — Arquitetura, Alcance do MVP + Mapa de Capacidades, Complexidade por Capacidade (Slides 3-5)
3. **Escopo & Governança** — Gaps Mapeados (Premissas/Abertos/Fora do Escopo), Mapa de Riscos (Slides 6-7)
4. **Roadmap** — Linha do Tempo Visual, Visão de Futuro (Slides 8-9)
5. **Gestão da Mudança** — Adoção e Change Management (Slide 10)
6. **Estimativa & Entrega** — Investimento Indicativo e Entregáveis Mapeados, Épicos/Casos de Uso detalhado, Investimento com/sem impostos (Slide 11 + seções abaixo)
7. **Fechamento** — o Ask (Slide 12)

## Épicos e Casos de Uso (Escopo)

Cada épico segue o padrão "o que entrega / capacidade Salesforce / casos de uso habilitados" — mesmo formato usado no ROM de referência.

### E01 — Canal Digital de Atendimento ao Cidadão (WhatsApp + Telefonia via CTI + Agentforce) · Tamanho M
**O que entrega**: abertura de chamado de socorro via WhatsApp (texto/áudio) e via telefonia (integração CTI com a URA) com triagem automatizada, sempre com transbordo garantido para fila humana via Omni-Channel, com contexto completo (incluindo screen-pop de CTI) — a IA nunca decide a gravidade da vítima. Complementa, nunca substitui, o 0800.
**Capacidade Salesforce**: Service Cloud (Agentforce Contact Center Enterprise — número de licenças a revalidar per `decisions/0004`) + Digital Engagement + Omni-Channel + Service Console + integração CTI (padrão a confirmar, `data/gaps.json` G0524).
**Casos de uso habilitados**: abertura de chamado via WhatsApp (texto/áudio) e telefonia (CTI) · triagem automatizada pelo Agentforce · transbordo garantido para fila humana via Omni-Channel, com contexto completo (incluindo screen-pop de CTI) · criação automática de ordem de serviço e protocolo.

### E02 — Registro e Classificação da Ocorrência · Tamanho L
**O que entrega**: criação do chamado a partir de qualquer canal, classificação por catálogo de 100+ subtipos desde o dia 1, qualificação do chamado e da ordem de campo, e integração com os sistemas legados SIGOR/SIGEO.
**Capacidade Salesforce**: Field Service (Work Order, Work Type) + Service Console + integrações ponto a ponto.
**Casos de uso habilitados**: registro do chamado multi-canal (WhatsApp/0800/CTI) · catálogo de classificação (100+ subtipos) · qualificação do chamado e da ordem de campo pelo Agentforce/Atendente · deduplicação por alerta ao C2C · integração de sincronização SIGOR/SIGEO.

### E03 — Despacho Automatizado de Recursos de Campo · Tamanho L
**O que entrega**: motor de agendamento e otimização operando nas 14 CGRs, 100% reativo em tempo real, com reprocessamento automático em recusa e trilha de auditoria completa.
**Capacidade Salesforce**: Field Service (motor de agendamento e otimização, Service Territory, Console do Dispatcher).
**Casos de uso habilitados**: motor de agendamento e otimização (Field Service) · reprocessamento automático em recusa · console do Dispatcher (Gantt/Mesa) · alarme e escalonamento ao supervisor da CGR · trilha de auditoria.

### E04 — Execução em Campo (App Mobile) · Tamanho L
**O que entrega**: aplicativo único de Field Service Mobile para os 1.152 operadores de campo das 14 UBAs, com recebimento de despacho via push nativo e encerramento com formulário, quando aplicável.
**Capacidade Salesforce**: Field Service Mobile (licença Field Service Community).
**Casos de uso habilitados**: aplicativo único de Field Service Mobile · recebimento de despacho via push nativo · modo offline com fila de sincronização · encerramento com formulário, quando aplicável · travas de negócio (recusa com motivo, foto, check-in geolocalizado).

### E05 — Rastreamento e Visibilidade em Tempo Real · Tamanho L
**O que entrega**: protocolo único acompanhável do pedido ao encerramento — rastreamento do cidadão via Appointment Assistant e painel agregado para gestores.
**Capacidade Salesforce**: Field Service (template de Experience Cloud embutido + Appointment Assistant nativo, `[KA-6140]`) — sem build de site guest dedicado.
**Casos de uso habilitados**: rastreamento do cidadão via Appointment Assistant (Field Service) · painel agregado para gestores (4 indicadores).

**Fonte de dados**: `data/epics.json` (capabilities, description), `data/estimates.json` (t_shirt_size).

## Linha do Tempo — Detalhamento Visual (Estimativa & Entrega)

Ver Slide 8 para o conteúdo completo do diagrama de semanas (S1-S30, dois cenários, marcos M0-M4, caminho crítico) e Slide 9 para o trilho de futuro do Roadmap. Resumo tabular de apoio:

| Fase | Épicos incluídos | Objetivo | Marco de fim de fase |
|---|---|---|---|
| Fase 0 — Resolução de Discovery | — | Resolver as 5 perguntas bloqueadoras (G0107, G0305, G0309, G0415, G0524) e dimensionar o Change Management (G0515) antes do build | M0 |
| Fase 1 — Fundação | E02 | Registro da Ocorrência e Integrações (SIGOR/SIGEO) | M1 |
| Fase 2 — Despacho e Canal Digital | E03, E01 | Despacho Automatizado + Canal Digital (WhatsApp/Agentforce) | M2 |
| Fase 3 — Execução em Campo | E04 | App mobile único, travas de negócio | M3 |
| Fase 4 — Rastreamento e Estabilização | E05 | Link de rastreamento do cidadão, painel de gestores, UAT estadual, hypercare | M4 (Go-live) |

**Caminho crítico**: E02 → E03 → E04 → E05.

**Três lanes de duração** (não há `duration_weeks` por fase — `roadmap.json` não carrega essa granularidade; a faixa é derivada top-down por lane, não somada bottom-up):

| Lane | Duração | Basis |
|---|---|---|
| **Traditional** (âncora) | 16-31 semanas | Derivada do formato do engagement (benchmark top-down), sem compressão |
| **Augmented** | 14-25 semanas | Faixa traditional comprimida por `efficiency.json.realized_band` (~10-18%) |
| **AI-native** (condicional) | 10-19 semanas | Faixa traditional comprimida por `efficiency.json.native_band` (~35-40%) — gate de qualificação ainda não atendido |

**Urgência**: o contrato atual de URA (Instinct) expira abril/2027 — mesma janela da meta de produção do cliente (homologação jan/fev 2027, produção abril 2027). O contrato administrativo renova em 30/nov/2026, pressionando a decisão Open CTI vs. Salesforce Voice (ver Slide 9).

**Fonte de dados**: `data/roadmap.json` (fases/épicos/objetivos/success_criteria), `data/estimate-comparison.json.lanes` (durações por lane), `.project-metadata.json.timeline` (faixa derivada, driver de urgência), `[KA-6240]`.

## Approved Commercials — Investimento (ROM), valores com e sem impostos (Estimativa & Entrega)

Regra permanente de precificação PS LATAM: **valor COM imposto = valor SEM imposto ÷ 0,9345**. As rates abaixo já foram validadas pelo usuário em 2026-09-17 (com imposto); o valor sem imposto é obtido multiplicando por 0,9345 — mesma fonte, sem novo dado inventado.

**Rates aplicadas (R$/hora):**

| Bucket | Sem imposto | Com imposto |
|---|---|---|
| Architect-class sênior onshore (PM/SA/TA · Program Lead/Intent Architect/Agent Orchestrator) | R$ 884,68 | R$ 946,69 |
| Entrega sênior onshore ou qualquer offshore regular (FC/Developer/QA sênior onshore · qualquer papel offshore regular) | R$ 668,78 | R$ 715,66 |
| Change & Adoption regular onshore (Change & Adoption · Adoption Architect) | R$ 573,98 | R$ 614,21 |

**Faixa indicativa de investimento por lane (BRL, sem e com impostos):**

| Lane | Duração | Sem imposto | Com imposto |
|---|---|---|---|
| **Traditional** (âncora) | 16-31 semanas | R$ 5.918.133,18 – R$ 11.466.383,03 | R$ 6.332.940,80 – R$ 12.270.072,80 |
| **Augmented** | 14-25 semanas | R$ 5.178.366,53 – R$ 9.247.083,09 | R$ 5.541.323,20 – R$ 9.895.220,00 |
| **AI-native** (condicional) | 10-19 semanas | R$ 2.227.507,84 – R$ 4.231.264,90 | R$ 2.383.636,00 – R$ 4.528.908,40 |

> *Esta faixa é baseada nas rates de R$946,69/h (architect-class sênior onshore), R$715,66/h (entrega sênior onshore/qualquer offshore regular) e R$614,21/h (change & adoption regular onshore) que você forneceu e validou em 2026-09-17. Indicativo para planejamento apenas; a estrutura comercial final é confirmada através do acordo comercial aplicável.*

A faixa AI-native permanece condicional ao gate de qualificação (nenhum sponsor executivo nomeado, mandato AI-first ainda não assumido) — é um motivador, nunca uma entrega comprometida sem nomear o compromisso.

Este é um preço **indicativo**, não custo/margem, e não uma proposta de fixed fee — a estrutura comercial final (incluindo o modelo de precificação) é confirmada através do acordo comercial aplicável.

*Esta comparação é benchmark-based, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Faixas de duração e a faixa AI-native carregam a incerteza herdada de `confidence: Assumed` em todos os 5 épicos.*

### O que esta faixa indicativa mapeia — entregáveis do programa

As figuras acima validam a visão de solução, o alcance e o esforço de um conjunto de entregáveis mapeado e nomeado, não uma bolsa de horas a consumir — o modelo comercial final (time & material, preço fechado por escopo, ou outro) é confirmado no acordo comercial aplicável. A lista abaixo é a base de validação da proposta — o que está mapeado, fase a fase (fonte: `success_criteria` de cada fase em `data/roadmap.json`, sem número novo inventado):

- **Fase 0**: as 5 perguntas bloqueadoras (G0107, G0305, G0309, G0415, G0524) respondidas pelo DER/Stefanini; especificação de payload SIGOR/SIGEO assinada; workstream de Change Management dimensionado.
- **Fase 1**: Work Order criável a partir da tela nativa do Field Service e do Service Console; catálogo completo de Work Type; sincronização SIGOR validada em janela controlada; callout SIGEO testado; alerta de deduplicação manual funcionando.
- **Fase 2**: despacho aciona a viatura correta nas 14 CGRs em cenários de teste; escalonamento N/N-10 funciona; console do Dispatcher operacional nos 4 turnos; triagem WhatsApp cria Work Order de ponta a ponta; transbordo para fila humana preserva contexto.
- **Fase 3**: app recebe despacho e executa o ciclo completo até o encerramento com evidência; piloto com subconjunto de UBAs antes do rollout às 14 CGRs; travas de negócio bloqueiam encerramento sem os requisitos mínimos.
- **Fase 4**: link guest ativo e protegido por token com expiração; mapa/Gantt operacional para o C2C; painel de gestores exibindo os 4 indicadores; UAT estadual assinado pelo DER; hypercare concluído sem bloqueadores críticos.
- **Change Management** (atravessa Fases 3-4, dimensionado na Fase 0): até 2 meses de operação assistida + treinamento por persona para os 1.152 operadores das 14 UBAs.

**O que fica explicitamente fora deste alcance mapeado**: os 6 itens de Roadmap futuro nomeados na Slide 9 (Salesforce Voice/substituição da URA, Incidente nativo, enforcement offline, Portal de Parceiros, Street-Level Routing, relatório por CGR + SLA) — qualquer decisão de trazê-los para dentro do escopo é uma mudança de escopo formal a validar separadamente, não uma reinterpretação das figuras acima.

**Fonte de dados**: `data/estimate-comparison.json` (rates, lanes, indicative_price_range — Approved Commercials, validado pelo Solution Lead em 2026-09-17), `outputs/artifacts/estimate-comparison.md` (`## Approved Commercials`), `data/roadmap.json` (success_criteria por fase), regra de imposto ÷0,9345 (diretriz permanente do usuário).

---

## Renderização

Este outline (Fundações + Slides 1-12 + Linha do Tempo detalhada + Épicos/Casos de Uso + Investimento) é a fonte única de conteúdo para dois entregáveis:

1. **ROM HTML** — `outputs/artifacts/rom-cliente.html`, menu lateral esquerdo, modelado em `DATAPREV-PAT/outputs/artifacts/rom-cliente.html` (PT-BR apenas, sem toggle bilíngue). A seção de linha do tempo (Slide 8) usa o padrão visual de grade CSS "Linha do Tempo & Marcos" do ROM de referência (`s9`), adaptado de datas fixas para números de semana com dois cenários (compacto/estendido) e disclaimer de ilustratividade. A seção de gaps (Slide 6) usa o padrão visual de cartões coloridos "Premissas & Fora do Escopo" do ROM de referência (`s6b`), adaptado às 2 ADRs, 5 perguntas abertas e 6 itens fora de escopo reais deste projeto.
2. **Prompt para Gemini gerar o PPTX** — `outputs/artifacts/rom-gemini-prompt.md`, um prompt único cobrindo todo o conteúdo acima (incluindo investimento, linha do tempo visual, mapa de riscos, roadmap de futuro e change management aprofundado) para colar no Gemini e gerar a apresentação em PowerPoint/Google Slides.

Ambos carregam os mesmos disclaimers verbatim (benchmark, rate validada, faixa AI-native condicional, ilustratividade da linha do tempo) — nenhum dos dois some com a lente de risco/preço que o outro mostra. Toda adição futura pedida pelo usuário se aplica igualmente aos dois — regra permanente, sem necessidade de perguntar qual superfície.
