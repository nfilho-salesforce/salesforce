## INTENT FOR
A equipe de go-live e hypercare, as beneficiárias e facilitadoras (adoção/capacitação), e o Novo PAT/MTE como system-of-record das cargas iniciais.

## INTENT OUTCOME
Fechar a homologação (UAT) aberta no início de novembro e virar para PRODUÇÃO em 15/nov/2026. Popular a plataforma com a carga inicial MÍNIMA necessária ao go-live (E07 — beneficiárias, facilitadoras, estabelecimentos a partir do Novo PAT, que permanece system-of-record) e conduzir a adoção enxuta (E09 — capacitação e materiais essenciais, com o pico da comunicação já iniciado na Fase 1).

## INTENT MEASURED BY
Homologação (UAT) concluída sobre as jornadas entregues (portal, marketplace, credenciamento, financeiro); cadastros mínimos carregados com dedup e reconciliação (INT-046, INT-047, INT-048); facilitadoras e beneficiárias com capacitação essencial (INT-049); GO-LIVE PROD 15/nov estabilizado com hypercare ativo.

## INTENT MUST NOT
Não carregar dado sensível/CPF na org — só referências não-sensíveis (ADR 0001, INT-046). Não recriar registros em recarga — a carga é idempotente por external ID (INT-046). Não fazer batimento pesado de dedup no MVP — entrar marcado, sem batimento profundo (INT-047, temperado pelo discovery). Não expandir E09 além de adoção enxuta (change management, não build pesado).

## PRE-DECIDED
- **Novo PAT permanece system-of-record** dos cadastros; a plataforma recebe a carga mínima ao go-live (roadmap, decision_log).
- **Carga idempotente**: Bulk API 2.0 + upsert por external ID (INT-046 — dimensionado para o pico ~28/s / 1M registros analisado em 2026-07-31).
- **Dedup leve no MVP**: entrar marcado por chave não-sensível, sem batimento profundo (INT-047).
- **E09 é transversal e enxuto**: a comunicação começou na Fase 1 e culmina aqui; capacitação e materiais essenciais, não uma frente de build.
- **Data fixa imóvel**: go-live PROD 15/nov/2026 (ADR de modo data-fixa; decision_log).

## PLAN-MODE QUESTIONS
- ⚠ **VIABILIDADE DA DATA FIXA — SINALIZAR**: 13 semanas para um build XL regulado sobre 3 pré-requisitos externos de lead-time (org greenfield, MuleSoft on-premise, gateway) é cronograma agressivo; a janela de 1 semana entre o fim do build (8/nov), a homologação e o PROD (15/nov) é o ponto mais frágil. Se algo escorregar, o de-escopo (E03 primeiro) é o trilho.
- Qual o conjunto mínimo de cadastros para o go-live e sua fonte exata no Novo PAT (INT-046)?
- Chave de dedup não-sensível acordada (INT-047) — qual campo, dado que CPF não persiste?
- Critérios de aceite da reconciliação pós-carga (INT-048): tolerância de divergência aceitável.

## BUILD-MODE QUESTIONS
- Jobs Bulk API 2.0: tamanho de lote, janela de execução, ordem de carga entre objetos (INT-046).
- Relatório de reconciliação pós-carga: formato e destinatário (INT-048).
- Conteúdo e canal dos materiais de adoção essenciais (INT-049).

## DATA MODEL
Deduplicação na carga por chave não-sensível (INT-047) — dado que CPF não persiste, a chave de unicidade é um external ID não-sensível vindo do Novo PAT. Sem novos objetos de negócio nesta fase; a carga popula os objetos fundacionais das Fases 1–3.

## AUTOMATION
Carga inicial idempotente de referências não-sensíveis via Bulk API 2.0 com upsert por external ID (INT-046 — a arquitetura assíncrona que evita o teto de Apex concorrente) e validação de qualidade + reconciliação pós-carga (INT-048). O detalhe vive nesses intents.

## UI
Painel de adoção do portal da beneficiária (INT-049) — Lightning Record Page/monitoramento leve para a adoção enxuta. Sem novas jornadas de negócio nesta fase.

## SECURITY
Herda a residência híbrida (ADR 0001): a carga traz apenas referências não-sensíveis; nenhum CPF entra na org. Acesso por papel e trilha de auditoria já estabelecidos na Fase 1.

## DATA SOURCES
Novo PAT/MTE como origem da carga inicial via MuleSoft (INT-046, camada E05 da Fase 1). Novo PAT permanece system-of-record.

## ACCEPTANCE USER
A homologação percorre as jornadas entregues (portal gov.br, leilão reverso, credenciamento, financeiro) e é aprovada; a carga mínima do Novo PAT popula a plataforma sem duplicar registros nem trazer CPF; beneficiárias e facilitadoras recebem a capacitação essencial; em 15/nov a plataforma entra em PRODUÇÃO com hypercare ativo e um painel de adoção acompanhando os primeiros acessos.

## ACCEPTANCE METADATA
Verifica-se: (a) a carga é idempotente — recarregar não cria duplicatas (upsert por external ID, INT-046); (b) registros duplicados entram marcados por chave não-sensível, sem batimento pesado (INT-047); (c) a reconciliação pós-carga confere contagens e sinaliza divergências dentro da tolerância acordada (INT-048); (d) nenhum CPF/dado sensível foi carregado na org (ADR 0001); (e) o painel de adoção reflete os acessos ao portal (INT-049); (f) o go-live PROD 15/nov está estável com hypercare.

## REPORTS
O relatório de reconciliação pós-carga (INT-048) confere contagens e sinaliza divergências da carga inicial. Para adoção, o painel do portal da beneficiária (INT-049) acompanha os primeiros acessos. Dashboards operacionais mais amplos ficam para pós-go-live/onda futura.
