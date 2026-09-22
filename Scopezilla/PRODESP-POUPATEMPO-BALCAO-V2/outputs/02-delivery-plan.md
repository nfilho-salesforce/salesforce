# Plano de Entrega — PRODESP · Poupatempo Balcão V2

*Gerado em 22/09/2026 · Scopezilla `roadmap` · 6 fases (0 discovery + 5 de build) sobre os 10 épicos aprovados (`decisions/0002`)*

**Duração benchmark do programa: 15–30 semanas** (faixa top-down a partir da forma do engagement; não é compromisso). Classificado como Multi-Cloud/Médio — 10 épicos, mix predominante M (5) com dois L (E08, E10) e um XL (E09), Slack + Agentforce + MuleSoft + Data 360 em escopo — linha de base 16–24 semanas. +15% no limite superior por overlay regulatório LGPD/setor público (biometria estadual, identidade federada gov.br, PII de cidadã cruzando E07/E08/E09) → 16–28. Alargamento modesto adicional porque E03, E06 e E09 seguem com confiança `Unknown` em dimensões de sizing que travam o piso/teto do programa — E09 é o épico de maior risco técnico do programa inteiro → **15–30 semanas finais**. Nenhum análogo do usuário disponível para calibrar contra um caso real entregue.

> **Disclaimer de Benchmark**: esta faixa é derivada de padrões de engagements comparáveis (fonte: `model-training-data`) — direcional, não um compromisso de cronograma. Valide contra a disponibilidade real da equipe e a velocidade de decisão do cliente antes de citar a um cliente.

O time nomeado que entrega este plano — funções e headcount, com justificativa — vem do skill `estimate`, não deste documento.

---

## Fase 0 — Resolução de Discovery e Pré-Kickoff
*(sem épicos — sequência 1 de 6)*

Fecha as lacunas que travam o kick-off técnico antes de qualquer build: identidades e protocolos dos 5 sistemas-alvo de E09 (T7, Sistema Semântico, Atendimento, Biometria, Legado — G0901-G0905); fonte do sinal de ocupação/fila por posto que E03/E07/E10 consomem (G0315); sistema de agendamento que dispara E06 (G0613); owner de governança de agentes do lado Prodesp (lacuna consolidada em 9 gaps espalhados por 7 épicos, ver `01-solution.md`); dimensionamento real de licenças Slack para 244 postos + 900 totens.

**Critério de sucesso**: as 5 identidades de sistema de E09 confirmadas; fonte do sinal de capacidade identificada; owner de governança nomeado; licenciamento Slack dimensionado.
**Risco**: gatilho — 136 gaps / 4 conflitos de fonte no gap analysis, acima do limiar de >15 gaps que recomenda esta fase em vez de herdar a incerteza para o build.

---

## Fase 1 — Fundação do Posto de Trabalho e Governança
*(E01, E05 · sequência 2 de 6 · Fase 1 tática do cliente)*

O atendente passa a trabalhar dentro do Slack — canais por serviço, Canvas fixado, Agentforce em contexto — com papéis, treinamento e política de canal definidos desde o dia um, não retrofitados depois do rollout.

**Critério de sucesso**: atendente resolve dúvidas de fluxo sem saltar para conhecimento disperso; Canvas lastreado em Salesforce Knowledge; papéis e critérios de adoção publicados antes do go-live.
**Depende de**: Fase 0 (owner de governança nomeado, licenciamento dimensionado).
**Risco**: as 1.800 licenças Slack já validadas cobrem a Sala de Situação, não o headcount real dos 244 postos + 900 totens — dimensionamento pendente com o cliente.
`[KB: staar-data-360-headless.md:24-26]` `[KB: staar-agentforce-governance-guardrails.md:42-45]`

---

## Fase 2 — Operação Tática do Balcão
*(E02, E03, E04 · sequência 3 de 6 · Fase 1 tática do cliente)*

Escalonamento em tempo real por huddle a partir do posto de trabalho de E01; sinal de ocupação/fila por posto entre 244 postos + 900 totens — a maior incerteza técnica da Fase 1, endereçada com antecedência porque E07 e E10 dependem dela; workflow de contingência para sistema fora do ar.

**Critério de sucesso**: atendente aciona huddle sem sair da cadeira; sinal de capacidade por posto disponível e confiável; aviso automático de sistema fora do ar chega antes do boca a boca informal.
**Depende de**: E01 (posto de trabalho onde o huddle é acionado).
**Risco**: E03 dimensionado com confiança `Unknown` — pode subir de M para L se exigir instrumentação nova (integração com totens/check-in); resolver isso aqui evita propagar o risco para E07/E10.

---

## Fase 3 — Plataforma de Integração MuleSoft
*(E09 · sequência 4 de 6 · trilha paralela · Fase 2 plataforma do cliente)*

Camada de integração API-led ligando a Plataforma Salesforce Headless a gov.br, biometria estadual, legado Prodesp, Sistema Semântico e T7 — o épico de maior risco técnico do programa (XL, confiança `Unknown`).

**Critério de sucesso**: camadas de API de Sistema/Processo/Experiência entregues para os 5 sistemas-alvo, com protocolos e autenticação confirmados por sistema.
**Depende de**: nenhum épico — corre em paralelo às Fases 2–4 por ter o maior lead time do programa; não bloqueia os épicos baseados em Slack. *(Trilha paralela — suas semanas não entram na soma do caminho crítico sequencial.)*
**Risco**: ambiente MuleSoft/Anypoint já maduro na conta (confirmado em grill 2026-09-22) reduz o risco de construção da camada do zero, mas as identidades e protocolo/volume por sistema continuam sendo o bloqueador dominante até formalizados na Fase 0.
`[KB: staar-headless-360-doctrine.md:21-23]`

---

## Fase 4 — Experiência Agêntica Cidadã
*(E06, E07, E08 · sequência 5 de 6 · Fase 2 plataforma do cliente)*

Pré-atendimento digital por WhatsApp antes da visita (E06); validação remota de documentos por atendente ocioso, reutilizando o posto de trabalho de E01, o padrão de huddle de E02, o sinal de capacidade de E03 e o intake de documento de E06 como um único fluxo conectado (E07); atendimento agêntico 24/7 com escalonamento human-in-the-loop (E08).

**Critério de sucesso**: cidadã recebe triagem antes do dia marcado; atendente ocioso valida documento sem duplicar intake; agente de WhatsApp atende fora do horário e escala genuinamente quando o caso exige.
**Depende de**: E01, E02, E03, E06 — E07 converge as quatro; atraso em qualquer uma atrasa E07.
**Risco**: E06 depende de um evento de gatilho de agendamento ainda não confirmado (Fase 0); E07 carrega risco de LGPD mais alto que o huddle em texto por transportar imagem de documento; E08 é o primeiro fluxo agêntico 24/7 do setor público sem case de referência LATAM — mantido em L sem sensibilidade formal de sizing, por decisão explícita do usuário (grill 2026-09-22).
`[extends: staar-data-360-headless.md:16-22]`

---

## Fase 5 — Analítica e Fechamento
*(E10 · sequência 6 de 6 · Fase 2 plataforma do cliente)*

Cruzamento de dados em tempo real via Data 360, modelo preditivo de tempo de espera e retroalimentação analítica dos agentes de IA para melhoria contínua.

**Critério de sucesso**: modelo preditivo treinado com dado real do sinal de capacidade da Fase 2; retroalimentação dos agentes operando.
**Depende de**: E03 (dependência de dado, não de esforço de build compartilhado).
**Risco**: sem o sinal de E03 resolvido a tempo, o modelo preditivo não tem dado de entrada confiável — por isso sequenciado por último, não em paralelo.
`[extends: staar-data-360-headless.md:16-22]`

---

## Caminho Crítico

**E01 → E02 → E07** é a cadeia mais longa de dependência do programa — E03 e E06 também convergem em E07, então um atraso em qualquer um dos quatro (E01, E02, E03, E06) atrasa E07. E10 depende só de E03. E09 corre paralelo e não faz parte do caminho crítico sequencial.

## Processos Padrão (consolidados, não repetidos por fase)

- **Teste/QA**: validação de cada épico antes de promover ao próximo posto/canal piloto; atenção redobrada em E07 (LGPD/imagem de documento) e E08 (guardrails de escalonamento humano genuíno).
- **Implantação**: rollout por onda entre os 244 postos + 900 totens — não big-bang; ordem sugerida acompanha a sequência de fases acima.
- **Treinamento**: currículo de E05 cobre Fases 1 e 2; atualização incremental a cada fase de plataforma (E06/E07/E08) conforme o atendente ganha novos canais.

## Tabela de Riscos Consolidada

| Risco | Fase | Mitigação |
|---|---|---|
| Licenciamento Slack dimensionado para Sala de Situação, não para o headcount real | 1 | Confirmar headcount de atendentes por posto/totem na Fase 0 |
| Sinal de ocupação por posto sem fonte identificada (G0315) | 2 | Resolver a fonte na Fase 0; E03 é o dono designado da construção |
| Owner de governança de agentes não nomeado | 0/1 | Nomear antes do início da Fase 2 (item de maior exposição do programa) |
| Identidades/protocolos dos 5 sistemas de E09 não confirmados (G0901-G0905) | 0/3 | Formalizar no kick-off técnico; ambiente Anypoint já maduro reduz só parte do risco |
| Evento de gatilho de agendamento de E06 não identificado (G0613) | 4 | Confirmar sistema de agendamento na Fase 0 |
| E08 é primeiro fluxo agêntico 24/7 do setor público sem referência LATAM | 4 | Aceito como nota qualitativa, sem sensibilidade formal de sizing (decisão do usuário) |

## Deliverables

- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/02-delivery-plan.md`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/data/roadmap.json`
- `/Users/nfilho/claude/Scopezilla/PRODESP-POUPATEMPO-BALCAO-V2/outputs/`
