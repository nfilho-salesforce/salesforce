# Apresentação — PRODESP · Poupatempo Balcão V2

*Gerado em 22/09/2026 · Scopezilla `slides` (Creation Mode) · Nomes travados: Slack, Agentforce, MuleSoft, Data 360*

## Fundamentos

- **Objetivo real**: validar o entendimento da necessidade com a audiência de negócio/executiva, obter validação técnica da arquitetura, e então apresentar linha de tempo e investimento — três decisões em uma sessão.
- **Audiência**: executivos, responsáveis por negócio e técnicos da Prodesp, na mesma sala.
- **Fluência em Salesforce**: parcial — produtos citados pelo nome; nenhum ID de épico ou termo interno Scopezilla aparece nos slides.
- **Grande Ideia**: a cidadã já fala com o Estado no WhatsApp; o que falta é o posto de trabalho de quem está atrás do guichê — quando o caso foge do script, o atendente hoje levanta, usa o celular pessoal ou pede para a pessoa voltar.
- **Arco lógico**: Problema → Consequência → Solução → Prova → Pedido — constrói a dor com a sala antes de pedir validação, depois valida a arquitetura e o maior risco técnico, encerra com sequenciamento, prazo e investimento.
- **Tom**: colaborativo nos slides de validação (3, 5, 6, 7 — convida confirmação, não afirma), mais direto e assertivo nos slides de fechamento (9, 10, 12 — a sala precisa decidir, não debater).

---

## Slide 1 — Poupatempo Balcão V2: do WhatsApp pessoal ao posto de trabalho institucional

**Razão de existir**: capa — ancora o programa no ativo específico (o posto de trabalho), não em "transformação digital" genérica.

**Conteúdo**: PRODESP · Poupatempo Balcão V2 · data da sessão.

**Visual**: capa com co-branding PRODESP + Salesforce.

**Densidade**: sparse

**Fonte de dados**: `.project-metadata.json`

**Notas do apresentador**: Abrir nomeando as três coisas que a sala precisa decidir hoje — entendimento validado, leitura técnica confirmada, prazo e investimento na mesa. Transição: "antes de qualquer dado, uma frase resume por que estamos aqui."

---

## Slide 2 — O posto de trabalho do atendente ainda falta no balcão do Poupatempo

**Razão de existir**: fixa a Grande Ideia antes de qualquer dado — arco dedutivo para audiência sênior.

**Conteúdo**: A cidadã já fala com o Estado no WhatsApp. Quando o caso foge do script — uma digital que não entra, um documento divergente, um sistema fora do ar — o atendente hoje levanta, usa o celular pessoal ou pede para a pessoa voltar.

**Visual**: painel dividido — hoje (celular pessoal, "volte depois") vs. proposto (posto de trabalho institucional).

**Densidade**: sparse

**Fonte de dados**: enquadramento do usuário nesta sessão + `strategy.json` (vision_statement)

**Notas do apresentador**: Deixar a frase pousar — não explicar demais. Transição: "isso é o que ouvimos no discovery; queremos confirmar com vocês antes de seguir."

---

## Slide 3 — Casos fora do script ainda são resolvidos por WhatsApp pessoal, fora do alcance da LGPD

**Razão de existir**: checkpoint de validação — pede à audiência de negócio/executiva que confirme que entendemos a dor corretamente.

**Conteúdo**: Biometria que falha, documento divergente, sistema fora do ar. Coordenação hoje informal, sem histórico auditável. Exposição crescente a um achado de controle externo em um serviço de alto volume.

**Visual**: linhas de categoria — chip "Hoje" à esquerda, evidências à direita.

**Densidade**: balanced

**Fonte de dados**: `outputs/artifacts/executive-summary.md` (Dor atual, Por que agora)

**Notas do apresentador**: Perguntar diretamente: "isso reflete o que vocês vivem no balcão?" Pausar para reação antes de seguir — é o primeiro dos dois momentos de validação da sessão. Transição: "essa dor tem um tamanho concreto — vamos ao número."

---

## Slide 4 — 244 postos e 900 totens operam hoje sem visibilidade de capacidade ociosa entre si

**Razão de existir**: converte a dor abstrata em um número verificável — eleva a consequência.

**Conteúdo**: Capacidade ociosa entre postos hoje é invisível. O objetivo é redirecionar atendimento sem contratar. O sinal de ocupação por posto ainda não tem fonte identificada.

**Visual**: estatística única + diagrama simples de rede (postos e totens).

**Densidade**: balanced

**Fonte de dados**: `outputs/artifacts/executive-summary.md`; `data/roadmap.json` (Fase 0)

**Notas do apresentador**: Nomear que a fonte do sinal de ocupação é uma pergunta aberta para a Prodesp responder na Fase 0 — não um problema técnico do lado Salesforce. Transição: "com a dor e a escala confirmadas, é hora de mostrar a solução para a leitura técnica de vocês."

---

## Slide 5 — Quatro camadas cobrem o posto de trabalho, a operação, a cidadã e a integração multissistema

**Razão de existir**: slide principal de validação técnica — pede a arquitetos e líderes técnicos que confirmem a forma da solução.

**Conteúdo**: Camada 1 — posto de trabalho (canais por serviço, Canvas, agente de tópico único). Camada 2 — operação (sinal de ocupação, escalonamento por huddle, contingência de sistema fora do ar). Camada 3 — cidadã (pré-atendimento, validação remota de documentos, agente disponível 24 horas com humano por trás de qualquer decisão sobre documentos). Camada 4 — integração multissistema. Decisão de arquitetura: quem constrói o sinal de ocupação não é quem só o consome — evita duplicar a mesma base de dados.

**Visual**: diagrama de arquitetura em camadas, 4 faixas horizontais.

**Densidade**: dense

**Fonte de dados**: `outputs/artifacts/executive-summary.md` (Destaques da Solução); `data/epics.json`

**Notas do apresentador**: Pausar após cada camada para perguntas técnicas — este é o slide mais denso da sessão e o principal pedido de validação. Transição: "antes de seguir, o escopo completo por trás dessas quatro camadas."

---

## Slide 6 — Dez frentes de trabalho, com dois picos de risco: o atendimento por agente de IA e a integração de cinco sistemas

**Razão de existir**: inventário completo do escopo — nada fica de fora da validação.

**Conteúdo**: Dez frentes agrupadas em tática (posto de trabalho, escalonamento, contingência, governança) e capacidade/plataforma (sinal de ocupação, pré-atendimento, validação de documentos, atendimento por agente, integração, analytics). Mix de complexidade: 2 pequenas, 5 médias, 2 grandes, 1 muito grande.

**Visual**: grade de escopo com chips de tamanho por frente.

**Densidade**: dense

**Fonte de dados**: `data/epics.json`, `data/estimates.json`

**Notas do apresentador**: Se a sala questionar algum item do escopo, é o momento — antes de comprometer prazo e investimento. Transição: "dos dois picos de risco, um precisa de confirmação da Prodesp hoje."

---

## Slide 7 — A integração com cinco sistemas ainda não tem identidade nem protocolo confirmados

**Razão de existir**: o item de maior risco técnico do programa — pedido concreto e específico de validação técnica.

**Conteúdo**: Gov.br, biometria estadual, Sistema Semântico, T7 e o sistema legado da Prodesp — identidades e protocolos ainda pendentes. O ambiente de integração já maduro na conta reduz parte do risco de construir do zero, não todo.

**Visual**: diagrama hub-and-spoke — integração ao centro, cinco sistemas ao redor, conexões pendentes marcadas.

**Densidade**: balanced

**Fonte de dados**: `.project-metadata.json` (range_drivers); `outputs/artifacts/executive-summary.md`

**Notas do apresentador**: Pedir explicitamente: quem do lado técnico da Prodesp assume formalizar essas cinco identidades na Fase 0? Transição: "com escopo e maior risco confirmados, como isso se sequencia no tempo."

---

## Slide 8 — Quatro fases formam o caminho crítico: atraso em qualquer uma atrasa a validação remota de documentos

**Razão de existir**: mostra como o escopo validado se transforma em sequência — prepara o slide de prazo.

**Conteúdo**: Fase 0 (fechar lacunas) → Fase 1 (fundação do posto de trabalho) → Fase 2 (operação tática do balcão) → Fase 3 (integração, trilha paralela) → Fase 4 (experiência da cidadã) → Fase 5 (analytics). Caminho crítico: fundação → escalonamento → validação de documentos.

**Visual**: linha do tempo horizontal com o caminho crítico destacado.

**Densidade**: balanced

**Fonte de dados**: `data/roadmap.json`

**Notas do apresentador**: Nomear que a Fase 3 (integração) corre em paralelo — não bloqueia as fases baseadas em Slack. Transição: "isso se traduz em uma faixa de prazo."

---

## Slide 9 — 15 a 30 semanas de referência: a Fase 0 fecha as lacunas antes de travar qualquer prazo

**Razão de existir**: entrega a linha de tempo pedida pela sessão, enquadrada como faixa, não compromisso.

**Conteúdo**: Faixa derivada da forma do programa — classificação multi-cloud de porte médio — com acréscimo por overlay regulatório de LGPD/setor público. O teto é alargado por três frentes ainda com confiança baixa (integração, sinal de ocupação, gatilho de pré-atendimento).

**Visual**: barra de faixa com marcadores das Fases 0–5.

**Densidade**: balanced

**Fonte de dados**: `.project-metadata.json` (timeline.derived) — inclui o disclaimer de benchmark

**Notas do apresentador**: Ler o disclaimer de benchmark verbatim antes de qualquer pergunta sobre prazo fechado. Transição: "essa faixa de prazo sustenta a faixa de investimento a seguir."

---

## Slide 10 — Faixa indicativa de R$ 4,39 a R$ 9,42 milhões, ancorada na trilha com o mesmo time acelerado por IA

**Razão de existir**: entrega o investimento pedido pela sessão, ancorado na trilha validada.

**Conteúdo**: Tradicional (15–30 semanas, R$ 4,71–9,42 milhões) · Augmented — âncora (14–25 semanas, R$ 4,39–7,85 milhões, mesmo time acelerado por ferramenta de IA) · AI-native condicional (10–18 semanas, R$ 1,78–3,21 milhões, depende de a Prodesp nomear o owner de governança de agentes).

**Visual**: tabela comparativa de três colunas.

**Densidade**: dense

**Fonte de dados**: `outputs/artifacts/estimate-comparison.md` (## Approved Commercials) — inclui o disclaimer de taxa validada

**Notas do apresentador**: Ler o disclaimer de taxa validada verbatim. Deixar claro que a trilha AI-native é um motivador condicional, não uma oferta em aberto. Transição: "o que precisa fechar antes do kick-off técnico para essa faixa se manter válida."

---

## Slide 11 — Cinco lacunas fecham na Fase 0, antes do kick-off técnico

**Razão de existir**: converte o registro de risco em uma lista de ações que a sala pode assumir hoje — fecha o ciclo de validação.

**Conteúdo**: Identidades dos cinco sistemas da integração · fonte do sinal de ocupação por posto · sistema que dispara o pré-atendimento · owner de governança de agentes de IA do lado Prodesp · dimensionamento real de licenças para 244 postos e 900 totens.

**Visual**: checklist em linhas de categoria.

**Densidade**: balanced

**Fonte de dados**: `outputs/artifacts/executive-summary.md` (Riscos e Mitigações, Próximos Passos)

**Notas do apresentador**: Perguntar, item a item, quem assume cada lacuna do lado Prodesp — não deixar a lista sem dono. Transição: "com isso claro, três decisões encerram a sessão."

---

## Slide 12 — Aprovar a Fase 0 hoje mantém a faixa de 15–30 semanas em pé

**Razão de existir**: fecha com as decisões específicas necessárias — atende aos três objetivos da sessão.

**Conteúdo**: 1) Validar o entendimento da dor e do desenho apresentados. 2) Confirmar a leitura técnica da arquitetura e do risco de integração. 3) Aprovar a Fase 0 e a faixa indicativa de prazo e investimento.

**Visual**: lista numerada de três ações.

**Densidade**: sparse

**Fonte de dados**: `outputs/artifacts/executive-summary.md` (Próximos Passos)

**Notas do apresentador**: Pedir a confirmação das três decisões em voz alta, uma a uma, antes de encerrar — não deixar a sessão terminar sem um "sim" ou um "ainda não" explícito em cada uma.

---

## Varreduras aplicadas (Fase 5)

- **Jargão interno**: nenhum ID de épico (E01–E10) ou nome de arquivo `data/*.json` aparece em título ou conteúdo de slide — só nos campos de Fonte de Dados, que são internos.
- **Nomenclatura de produto**: Slack, Agentforce, MuleSoft e Data 360 usados por extenso e de forma consistente.
- **Alucinação**: todo número (244 postos, 900 totens, 15–30 semanas, faixas de R$, mix 2S/5M/2L/1XL, cinco sistemas, cinco lacunas) rastreado a `executive-summary.md`, `estimate-comparison.md`, `.project-metadata.json`, `epics.json`/`estimates.json` ou `roadmap.json`. Nenhum item marcado `[verify]`.
- **AI-tells**: removido paralelismo negativo do título do Slide 2 (era "não é X — é Y", reescrito como afirmação direta) e do Slide 5 (clausula "sem duplicar" movida do título para o conteúdo). Reduzido uso de travessão nos títulos dos Slides 8, 9 e 11 em favor de dois-pontos ou reestruturação direta.
- **Visual/estrutural**: nenhuma tríade reflexiva — os grupos de 3 (trilhas comerciais no Slide 10, ações finais no Slide 12) são pares genuínos, não preenchimento. O painel antes/depois (Slide 2) é a única ocorrência de simetria forçada, reservada para o único contraste real da sessão.

## Deliverables
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/artifacts/presentation-outline.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/`
