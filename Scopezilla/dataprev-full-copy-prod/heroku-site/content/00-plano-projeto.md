# Plano de Projeto PS — Dataprev | Nova ORG Produtiva Dedicada
**Versão:** 2.0 (Estratégia Paralela) | **Data:** 2026-06-23 | **Responsável PS:** Nelson Stebulaitis Filho (Salesforce PS LATAM)

---

## 1. Contexto e Objetivo

A Dataprev opera hoje uma ORG de produção (`00Das00000Cz7qb` / prod11) com Agentforce (6 agentes Wave 2), Service Cloud, Data Cloud e Digital Engagement (WhatsApp), gerando **~40k mensagens/dia** com pico de **15k conversation entries/min**.

O **CPQD** realiza certificação independente com testes automatizados massivos (JMeter), mas as sandboxes atuais limitam o throughput a **~120 RPS / ~200 req/hora de LLM** — causando falsos negativos, atrasos e dependência crítica de Renato + Melyssa para replicação manual de bases (1 dia por instância).

**Decisão estratégica** (Vinícius Machuca + Aline Sabino, 11/06/2026): provisionar uma **nova ORG de produção dedicada** exclusivamente para testes de estresse e homologação massiva. O **Scale Test Add-On** é camada complementar (não alternativa) — cobre slots de burst controlado na Full Copy Sandbox existente.

### Objetivos do Projeto

| # | Objetivo | Indicador de Sucesso |
|---|----------|----------------------|
| O-1 | Provisionar nova ORG produtiva na mesma região (Brasil / prod11), Summer '26 | ORG ativa, mesma versão, mesmo datacenter |
| O-2 | Replicar arquitetura completa: Data Cloud (Zero Copy OCI), Agentforce + orquestrador, Digital Engagement | 6 agentes + orquestrador respondendo no novo ambiente |
| O-3 | Reconfigurar todos os endpoints e integrações críticas (11 no total) | Todos os endpoints validados ponta a ponta |
| O-4 | Configurar Scale Test Add-On para ciclos CPQD (JMeter via GitHub) | 1º ciclo CPQD executado com sucesso no novo ambiente |
| O-5 | Implantar Proactive Monitoring (Splunk) + runbook operacional | Dashboards ativos; dependência Renato/Melyssa eliminada |
| O-6 | Habilitar número WhatsApp Business dedicado para testes | Canal ativo sem interferência no número produtivo |

---

## 2. Premissas

### Técnicas
- **P-01:** Nova ORG provisionada na instância prod11 (Brasil) — mesmo datacenter da ORG atual para evitar latência
- **P-02:** Versão: Summer '26 (mesma da ORG atual, atualizada em jun/2026)
- **P-03:** Conectividade Oracle OCI utilizará a configuração validada em 08/05/2026 (Zero Copy cacheado) — documentação deve estar disponível antes do início da F2
- **P-04:** Marketing Cloud **NÃO está no escopo** — confirmado por Vinícius Machuca em 11/06/2026. Escopo: Core + Agentforce + Service Cloud + Data Cloud + Digital Engagement
- **P-05:** MuleSoft no escopo somente se confirmado contratualmente (+35h contingenciadas)
- **P-06:** Full Copy Sandbox existente será usada como base de replicação para a nova ORG
- **P-07:** Número WhatsApp Business dedicado para testes é responsabilidade da Dataprev junto à Meta (PS configura o Digital Engagement, não cria o número)
- **P-08:** Infraestrutura Oracle OCI para o novo ambiente é responsabilidade da Dataprev
- **P-09:** Capacidade de GPU/LLM da nova ORG deve ser equivalente à produção (~15k conversation entries/min) — ponto crítico de infraestrutura Salesforce
- **P-10:** TC1 e TC2 disponíveis a partir da Semana 1 com dedicação mínima de 70% nas semanas S3–S5

### Comerciais / Contratuais
- **P-11:** Licenças Agentforce for Service, Service Cloud, Data Cloud (DSCs), Digital Engagement e Einstein estarão aprovadas antes do kick-off
- **P-12:** Signature Success ativo para o novo ambiente (recomendado dado volume e criticidade)
- **P-13:** Flex Credits aprovados: sizing CPQD = ~3.110 pacotes / R$ 3,11M (6 meses, cenário máximo 12 ciclos/mês)
- **P-14:** Contrato-mãe BRL 35,5M como referência; novo ambiente é complementar

### Operacionais
- **P-15:** Janelas de deploy protegidas: sem atualizações em horário comercial BR (08h–20h)
- **P-16:** Times Dataprev responsáveis por cada integração estarão disponíveis nas janelas de reconfiguração (semanas 3–5)
- **P-17:** Renato e Melyssa disponíveis para apoio na carga de bases de conhecimento (semanas 2–4)
- **P-18:** Governança de acesso CPQD (restrições IP/geolocalização) definida antes do início dos testes

### Uso de IA para Aceleração de Entrega
- **P-19:** **Documentação assistida por IA** (Claude/Copilot): geração de documentação técnica, runbook e RACI — redução estimada de ~35% no esforço de documentação (~12–16h de economia)
- **P-20:** **Scale Agent (Pilot — Sprint 260):** monitoramento em tempo real dos ciclos CPQD com diagnóstico automático de root cause — reduz tempo de análise de falhas
- **P-21:** **Trial Accuracy Checker:** valida configuração com carga reduzida antes de escalar — reduz retrabalho no ciclo de homologação
- **P-22:** **Script Recorder Chrome Plugin:** grava fluxos de UI e gera scripts Playwright automaticamente — redução de ~30% no esforço de criação de scripts de teste
- **P-23:** **Agentforce Vibes (Pilot — Summer '26):** geração automatizada de scripts de teste de qualidade de resposta para os 6 agentes Wave 2
- **P-24:** **Ganho total estimado com IA:** ~70–90h de redução versus abordagem 100% manual (≈12–14% do esforço total)

---

## 3. Escopo

### Dentro do Escopo

| Componente | O que será feito |
|------------|-----------------|
| **Nova ORG Produtiva** | Provisionamento (prod11, Summer '26), Full Copy Sandbox, perfis, permissões, usuários |
| **Data Cloud** | Data Streams, Data Lake Objects (DLOs), Identity Resolution, Zero Copy Oracle OCI |
| **Agentforce** | 6 agentes Wave 2 (MEC, MDS, MS, Primeira Infância, MTE, IBAMA) + orquestrador; bases de conhecimento + RAG |
| **Digital Engagement** | Canal WhatsApp com número dedicado para testes |
| **Endpoints (11)** | CPQD, Oracle OCI, IBAMA, MTE, PCI Infra, GovBR, MEC, MDS, MS, Primeira Infância, WhatsApp Business API |
| **Scale Test Add-On** | JMeter via GitHub, Trial Accuracy Checker, Scale Agent (monitoring em tempo real) |
| **Proactive Monitoring** | Dashboards Splunk ativos desde o início + alertas automatizados |
| **Runbook Operacional** | Documentação completa que elimina dependência exclusiva de Renato + Melyssa |
| **Documentação Técnica** | Arquitetura, endpoints, acessos, credenciais |

### Fora do Escopo

- Marketing Cloud (BU, conectores, journeys, campanhas) — decisão confirmada 11/06/2026
- Desenvolvimento de novos agentes ou fluxos não existentes na ORG atual
- Configuração inicial do CPQD — apenas reconfiguração do endpoint Salesforce
- Suporte e manutenção pós-hypercare (5 dias úteis)
- Configuração de integrações novas não existentes na ORG atual
- Migração de dados de produção (replicação via Full Copy Sandbox)
- Alterações de arquitetura em relação ao ambiente atual
- Criação do número WhatsApp Business (responsabilidade Meta/Dataprev)
- Configuração da infraestrutura Oracle OCI (responsabilidade Dataprev)
- Change management ou treinamento de usuários finais
- Testes de performance do CPQD em si (apenas lado Salesforce)
- MuleSoft — somente se confirmação contratual (+35h se incluído)

---

## 4. Fases, Atividades e Esforço

### Fase 1 — Preparação e Planejamento (Semana 1) · 40h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 1.1 | Kick-off com stakeholders (Dataprev + Salesforce PS) | 4h | TA + PM |
| 1.2 | Levantamento e documentação do ambiente atual (ORG, integrações, endpoints) — assistido por IA | 10h | TA + TC1 |
| 1.3 | Mapeamento detalhado dos 11 endpoints (configs, credenciais, certificados) | 6h | TC1 |
| 1.4 | Revisão de licenças: Agentforce, DSCs, Scale Test Add-On, Digital Engagement | 4h | PM + TA |
| 1.5 | Definição da arquitetura do novo ambiente e aprovação | 8h | TA |
| 1.6 | Plano detalhado, cronograma e RACI (gerado com IA) | 4h | PM |
| 1.7 | Governança: acesso CPQD (IP/geo), janelas de deploy | 4h | PM + TA |
| 1.8 | **Envio do request de provisionamento da nova ORG** (disparar SLA Salesforce) | 0h | TA + AE |

> **Nota:** A solicitação de provisionamento é enviada no fim da S1. O SLA de resposta Salesforce (~1 semana) cobre exatamente a S2, que é aproveitada para F4 e preparativos de F3.

### Fase 2 — Nova ORG + Data Cloud (Semanas 2–3) · 96h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 2.1 | Replicação via Full Copy Sandbox para nova ORG (assim que provisionada) | 12h | TC1 |
| 2.2 | Configuração de perfis, permissões e usuários | 8h | TC1 |
| 2.3 | Data Cloud: Data Streams e Data Lake Objects (DLOs) | 20h | TA + TC2 |
| 2.4 | Data Cloud: Identity Resolution (regras, reconciliação) | 12h | TA |
| 2.5 | Reconfiguração Zero Copy Oracle OCI ↔ Data Cloud | 12h | TA + TC1 |
| 2.6 | Validação de capacidade de LLM (~15k conversation entries/min) | 8h | TA |
| 2.7 | Named Credentials e Connected Apps | 8h | TC2 |
| 2.8 | Configuração do orquestrador Agentforce | 16h | TA |

### Fase 3 — Agentes Wave 2 + Bases de Conhecimento (Semanas 3–4) · 104h

> TC1 e TC2 trabalham em paralelo — cada um fica responsável por 3 agentes.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 3.1 | Agente MEC (Topics, Actions, guardrails, base de conhecimento) | 14h | TC1 |
| 3.2 | Agente MDS | 14h | TC1 |
| 3.3 | Agente MS | 14h | TC1 |
| 3.4 | Agente Primeira Infância | 14h | TC2 |
| 3.5 | Agente MTE | 14h | TC2 |
| 3.6 | Agente IBAMA | 14h | TC2 |
| 3.7 | Carga de bases de conhecimento em todos os agentes — apoio Renato/Melyssa | 8h | TC1 + TC2 |
| 3.8 | Validação de RAG e qualidade de resposta por agente | 12h | TA + TC1 + TC2 |

### Fase 4 — Digital Engagement / WhatsApp (Semanas 2–3) · 28h

> Antecipada para a janela de espera do SLA de provisionamento (S2).

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 4.1 | Configuração do canal Digital Engagement na nova ORG | 8h | TC2 |
| 4.2 | Conexão do número dedicado de testes (número provido pela Dataprev) | 4h | TC2 |
| 4.3 | Testes de envio/recebimento WhatsApp | 8h | TC2 |
| 4.4 | Validação integração WhatsApp ↔ Agentforce + orquestrador | 8h | TA + TC2 |

### Fase 5 — Reconfiguração de Endpoints e Integrações (Semanas 3–5) · 78h (+35h MuleSoft)

> Iniciada em S3 em paralelo com F3 — TC1 e TC2 revezam entre agentes e endpoints.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 5.1 | Reconfiguração endpoint CPQD (IA externa) | 8h | TC1 |
| 5.2 | Reconfiguração integração Oracle OCI (Named Credentials + certificados) | 10h | TA + TC1 |
| 5.3 | Reconfiguração endpoint IBAMA | 6h | TC2 |
| 5.4 | Reconfiguração endpoint MTE | 6h | TC2 |
| 5.5 | Reconfiguração integração PCI Infra | 8h | TC1 |
| 5.6 | Reconfiguração integrações GovBR, MEC, MDS, MS, Primeira Infância | 16h | TC1 + TC2 |
| 5.7 | Atualização de webhooks e callbacks | 8h | TC2 |
| 5.8 | Validação de conectividade de todos os endpoints (11 integrações) | 16h | TA + TC1 + TC2 |
| 5.9 | *(Contingência)* MuleSoft — somente se Q-09 confirmado | +35h | TA |

### Fase 6 — Scale Test Add-On + Validação CPQD (Semanas 4–6) · 60h

> Inicia S4 assim que endpoint CPQD (5.1) estiver pronto — não aguarda todos os 11 endpoints.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 6.1 | Configuração do Scale Test Add-On no novo ambiente | 8h | TA |
| 6.2 | Integração scripts JMeter CPQD via GitHub | 8h | TC1 |
| 6.3 | Trial Accuracy Checker: validação com carga reduzida | 8h | TA + TC1 |
| 6.4 | Scale Agent: configuração de monitoramento em tempo real | 8h | TA |
| 6.5 | Execução dos primeiros ciclos CPQD (qualidade + guardrails) | 16h | TA + TC1 |
| 6.6 | Análise de resultados e ajustes | 12h | TA + TC1 |

### Fase 7 — Testes, Homologação e Go-Live (Semanas 5–7) · 96h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 7.1 | Scripts de testes funcionais Agentforce (Script Recorder + Agentforce Vibes) | 16h | TC2 |
| 7.2 | Testes de integração ponta a ponta (11 endpoints) | 24h | TA + TC1 + TC2 |
| 7.3 | Testes de volume/performance (meta: 100k RPS) | 16h | TA + TC1 |
| 7.4 | Homologação com time técnico Dataprev | 12h | TA + PM |
| 7.5 | Plano de rollback documentado e validado | 8h | TA + PM |
| 7.6 | Go-live em janela protegida (fora de horário comercial BR) | 8h | TA + TC1 |
| 7.7 | Hypercare pós go-live (monitoramento ativo — 5 dias úteis) | 12h | TC2 |

### Fase 8 — Documentação, Runbook e Handover (Semanas 1–7, entrega S7) · 54h

> Produção de documentação distribuída ao longo do projeto com IA; consolidação na S7.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 8.1 | Documentação técnica contínua (arquitetura, endpoints, acessos) — gerado com IA | 12h | TA |
| 8.2 | Runbook operacional completo (elimina dependência Renato + Melyssa) — gerado com IA | 12h | TC1 + TA |
| 8.3 | Ativação de dashboards Splunk + alertas proativos | 8h | TA |
| 8.4 | Consolidação e revisão final de toda a documentação | 8h | TA + TC1 |
| 8.5 | Sessão de handover e treinamento time Dataprev | 4h | TA + PM |
| 8.6 | Registro de decisões, lessons learned e encerramento | 6h | PM |
| 8.7 | Encerramento formal e aceite do cliente | 4h | PM |

---

## 5. Resumo de Esforço

| Fase | Descrição | Esforço |
|------|-----------|---------|
| F1 | Preparação e Planejamento | 40h |
| F2 | Nova ORG + Data Cloud | 96h |
| F3 | Agentes Wave 2 + Bases de Conhecimento | 104h |
| F4 | Digital Engagement (WhatsApp) | 28h |
| F5 | Endpoints e Integrações | 78h |
| F6 | Scale Test Add-On + Validação CPQD | 60h |
| F7 | Testes, Homologação e Go-Live | 96h |
| F8 | Documentação, Runbook e Handover | 54h |
| **TOTAL BASE** | | **556h** |
| Contingência MuleSoft (Q-09) | | +35h |
| **TOTAL COM MULESOFT** | | **591h** |

> **Impacto da IA:** estimativa sem as ferramentas de IA listadas em P-19 a P-23 seria ~630–650h. O uso de IA representa economia de **70–90h** (≈12–14% do total).

---

## 6. Carga por Semana e por Papel

| Semana | Fases Ativas | TA | TC1 | TC2 | PM | **Total** |
|--------|-------------|:--:|:---:|:---:|:--:|:---------:|
| S1 | F1 · F8 início | 24h | 14h | 4h | 8h | **50h** |
| S2 | F2 (SLA wait) · F4 · F8 | 26h | 22h | 22h | 6h | **76h** |
| S3 | F2 · F3 · F4 · F5 início · F8 | 32h | 30h | 30h | 6h | **98h** |
| S4 | F3 · F5 · F6 início · F8 | 34h | 30h | 30h | 8h | **102h** |
| S5 | F5 fim · F6 · F7 início · F8 | 30h | 26h | 26h | 8h | **90h** |
| S6 | F6 fim · F7 · F8 | 26h | 22h | 22h | 8h | **78h** |
| S7 | F7 go-live · F8 handover | 22h | 16h | 14h | 10h | **62h** |
| **TOTAL** | | **194h** | **160h** | **148h** | **54h** | **556h** |

### Perfis e Dedicação

| Papel | Sigla | Carga Total | Média/Semana | Pico | Perfil |
|-------|-------|:-----------:|:------------:|:----:|--------|
| Technical Architect | TA | 194h | 28h/sem | 34h (S4) | Sênior — Agentforce, Data Cloud, integrações |
| Technical Consultant 1 | TC1 | 160h | 23h/sem | 30h (S3–S4) | Pleno/Sênior — agentes MEC/MDS/MS, endpoints críticos |
| Technical Consultant 2 | TC2 | 148h | 21h/sem | 30h (S3–S4) | Pleno/Sênior — agentes PI/MTE/IBAMA, WhatsApp, testes |
| Project Manager | PM | 54h | 8h/sem | 10h (S7) | Part-time (25–30% de alocação) |

> **Trade-off:** pico de **102h na S4** com TA + TC1 + TC2 em dedicação ~70–80%. Compensado por 3 semanas a menos de projeto (7 vs. 10).

---

## 7. Timelines

### 7.1 Visão por Fases (Gantt)

```
         S1    S2    S3    S4    S5    S6    S7
         ──────────────────────────────────────
F1 Prep  ████
         ──────────────────────────────────────
F2 ORG         SLA░  ████  █
         ──────────────────────────────────────
F3 Agts               ████  ████
         ──────────────────────────────────────
F4 WApp        ████  ██
         ──────────────────────────────────────
F5 Endpt             ████  ████  ██
         ──────────────────────────────────────
F6 Scale              ░░░░  ████  ████  ██
         ──────────────────────────────────────
F7 Testes                         ████  ████  ██
         ──────────────────────────────────────
F8 Docs  ─────────────────────────────── ████
         ──────────────────────────────────────
```

> `████` ativo · `░░░░` preparação/pré-requisito · `SLA░` wait provisionamento Salesforce · `─────` documentação contínua via IA

### 7.2 Visão por Entregáveis Macro

```
         S1         S2         S3         S4         S5         S6         S7
         ─────────────────────────────────────────────────────────────────────────
         [M1]       ────────────[M2]       [M3]       ───────────[M4]       [M5][M6]
         │                      │          │                      │          │   │
         ▼                      ▼          ▼                      ▼          ▼   ▼
   Arquitetura           Nova ORG      6 Agentes +          Homolog.      Go-live
   aprovada +            ativa +       11 Endpoints         CPQD          +
   ORG request           WhatsApp      validados +          concluída     Runbook
   enviado               configurado   1º ciclo CPQD                      entregue
```

| Marco | Semana | Entregável |
|-------|:------:|-----------|
| **M1** | Fim S1 | Arquitetura aprovada · request de provisionamento enviado · RACI assinado |
| **M2** | Fim S3 | Nova ORG ativa com Data Cloud · WhatsApp configurado · orquestrador ativo |
| **M3** | Fim S4 | 6 agentes Wave 2 operacionais · todos os 11 endpoints validados · 1º ciclo CPQD executado |
| **M4** | Fim S6 | Homologação Dataprev concluída · testes de volume OK · rollback documentado |
| **M5** | Fim S7 | Go-live em janela protegida · hypercare ativo |
| **M6** | Fim S7 | Runbook entregue · dashboards Splunk ativos · encerramento formal |

---

## 8. Sizing de Flex Credits (CPQD) — Referência

Baseado nas informações pós-reunião CPQD em 19/06 (Thiago):

| Parâmetro | Valor |
|-----------|-------|
| Requisições por agente / ciclo CPQD | ~12.000 (qualidade 8k + guardrails 3k + pentest 500 + exploratório 500) |
| Actions por requisição | 3 (dado de produção) |
| Créditos por action | 20 |
| Custo por pacote Flex | R$ 1.000 (100k créditos) |
| **Custo por agente / ciclo** | **R$ 7.200** |
| **Custo Wave 2 completo (6 agentes) / ciclo** | **R$ 43.200** |
| Cadência escolhida | 12 ciclos/mês (~3x/semana) |
| **Custo total Flex Credits (6 meses)** | **R$ 3,11 milhões (~3.110 pacotes)** |

> O gargalo atual de 30h para 2.000 req é limite da sandbox (~120 RPS throttled), não apetite do CPQD. No novo ambiente o throughput deixa de ser restrição.

---

## 9. Perguntas em Aberto (Impacto no Prazo)

| ID | Pergunta | Impacto | Prioridade | Dono |
|----|----------|---------|-----------|------|
| **Q-01** | Volume de licenças Agentforce for Service para ambiente de testes? | ORG não pode ser ativada sem licenças | 🔴 Bloqueadora kick-off | Saulo, Milton (Dataprev) |
| **Q-02** | Volume de DSCs (Data Cloud) necessários? | Subdimensionamento exige ajuste contratual | 🔴 Bloqueadora kick-off | Saulo, Milton (Dataprev) |
| **Q-03** | Scale Test Add-On: o que já está habilitado? Qual o custo para a Dataprev? | Sem confirmação, F6 não pode iniciar | 🔴 Bloqueadora F6 | Renata + Vrajesh (Scale Center) |
| **Q-04** | Aprovação orçamentária para o ambiente produtivo adicional? | Sem aprovação, projeto não pode ser contratado | 🔴 Bloqueadora assinatura | Fernanda (AE) + gestão Dataprev |
| **Q-05** | Flex Credits aprovados? Sizing: 3.110 pacotes / R$ 3,11M (6 meses) | Sem créditos, ciclos CPQD paralisam | 🔴 Bloqueadora kick-off | Vinícius Machuca / Aline Sabino |
| **Q-06** | SLA de provisionamento da nova ORG produtiva — quanto tempo? | Pode atrasar S2; estratégia paralela absorve até 1 semana | 🟠 Bloqueadora F2 | Salesforce Account Team / Renata |
| **Q-07** | O modelo de dias reservados do Scale Test (mín. 1 dia, 2 sem. antecedência) atende cadência contínua do CPQD? | Se não, Scale Test perde valor estratégico | 🟠 Bloqueadora F6 | CPQD (Thiago) |
| **Q-08** | Configuração Oracle OCI de 08/05/2026 está documentada e acessível? | Sem docs, esforço de F2/F5 pode dobrar (+30h) | 🟠 Bloqueadora F2 | Renato / Dataprev DBA |
| **Q-09** | MuleSoft está no contrato? Qual o escopo? | +35h de esforço e possível +1 semana | 🟠 Antes do kick-off | Jurídico / Comercial Dataprev |
| **Q-10** | Número WhatsApp Business dedicado — Dataprev iniciou processo com Meta? | Registro na Meta leva 1–3 semanas; atrasa F4 | 🟠 Bloqueadora F4 | Dataprev (canal WhatsApp) |
| **Q-11** | Validação dos 12k req/agente/ciclo — consumo real nos logs do Primeira Infância confirma? | Sizing de Flex Credits pode estar errado | 🟡 Semana 1 | Renato (Dataprev) |
| **Q-12** | Sanity check técnico: novo ambiente absorve 12 ciclos/mês sem se tornar gargalo? | Pode exigir revisão arquitetural pós go-live | 🟡 Antes do go-live | Vinícius Machuca / Aline Sabino |
| **Q-13** | Governança de acesso CPQD (restrições IP/geolocalização) definida? | Risco de uso indevido das licenças do ambiente de testes | 🟡 Semana 2 | Dataprev (segurança) + CPQD |
| **Q-14** | Oracle OCI pode ser apontado para uma segunda ORG produtiva sem impacto no ambiente atual? | Pode inviabilizar arquitetura Zero Copy no novo ambiente | 🟠 Bloqueadora F2 | Dataprev DBA / Oracle OCI team |

> **Legenda:** 🔴 Bloqueadora (não inicia sem resposta) · 🟠 Alta prioridade (impacta timeline) · 🟡 Média prioridade

---

## 10. Riscos

| ID | Risco | Probabilidade | Impacto | Mitigação |
|----|-------|:---:|:---:|-----------|
| R-01 | SLA de provisionamento da ORG maior que 1 semana | Média | Médio (+1 sem absorvido; +2 sem crítico) | Acionar Account Team na semana 1; estratégia paralela absorve 1 semana de espera |
| R-02 | Reconfiguração Oracle OCI sem documentação adequada | Alta | Alto (+30h, +1 sem) | Garantir Q-08 e Q-14 antes do kick-off; buffer em F2 |
| R-03 | Times de integração Dataprev indisponíveis nas janelas planejadas | Alta | Alto (+1–2 sem) | Agendar janelas com 2 semanas de antecedência; incluir no RACI desde S1 |
| R-04 | Pico S3–S4 (98–102h) — risco de burnout ou conflito de agenda TC1/TC2 | Média | Médio | Confirmar dedicação mínima 70% antes de assinar; dividir claramente as responsabilidades por agente |
| R-05 | Bases de conhecimento não replicadas a tempo (dep. Renato/Melyssa) | Alta | Alto (atrasa F3 e M3) | Iniciar S2; runbook endereça dependência pós-projeto |
| R-06 | LLM capacity da nova ORG inferior à produção | Baixa | Muito Alto | Validar na atividade 2.6 antes de avançar para F3 |
| R-07 | Número WhatsApp não aprovado pela Meta a tempo | Média | Médio (atrasa F4) | Iniciar processo Meta antes do kick-off (Q-10) |
| R-08 | Flex Credits insuficientes para ciclos CPQD | Baixa | Alto | Validar sizing com Renato (Q-11) + sanity check Vinícius/Aline (Q-12) |

---

## 11. Stakeholders e Responsabilidades

| Papel | Nome | Fase(s) Críticas |
|-------|------|-----------------|
| Sponsor técnico Dataprev | Vinícius Machuca | F1, F6, F7 |
| Responsável técnica Dataprev | Aline Sabino | F1, F2, F7 |
| Account Executive Salesforce | Fernanda | F1 (aprovação orçamentária) |
| Scale Center | Renata + Vrajesh | F1, F6 |
| Replicação de bases | Renato + Melyssa | F3, F8 |
| Certificação independente | Thiago (CPQD) | F6, F7 |
| Licenças / comercial Dataprev | Saulo, Milton | Pré-kick-off |
| **PS Lead** | **Nelson Stebulaitis Filho** | **Todas** |

---

*Documento v2.0 — Estratégia paralela (7 semanas, TC1 + TC2). Gerado em 2026-06-23 com base no PDF "Dataprev | Novo Ambiente de Testes — Proposta de Licenças e Infraestrutura" (Juliane Lopes, 11/06/2026) e revisão de 23/06/2026. Premissas e estimativas sujeitas a revisão após resolução das questões em aberto (Seção 9).*
