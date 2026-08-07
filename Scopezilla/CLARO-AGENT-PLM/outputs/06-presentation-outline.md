# Presentation Outline — Win Themes & Talking Points
## CLARO Agente PLM — POC PLM & Agentforce

**Audience:** Claro Brasil — Lucas, Luciano, Fabrício, steering committee  
**Format:** 10–12 slides · 30 min presentation + 15 min Q&A  
**Version:** 1.0 · 2026-06-17

---

## Win Themes

Three messages that must land, in order of priority:

1. **"This is a proven pattern, not an experiment."**  
   Salesforce PS LATAM has built this exact architecture before. The AST Walker, DLQ-first resilience, and Agentforce PLM Admin/Ops design are production-tested patterns — not exploratory work. Claro gets an accelerated delivery of something already proven, not a team figuring it out on the job.

2. **"The PLM POC is the investment that unlocks the platform."**  
   This 8-week engagement is not a one-off fix. It is the architectural beachhead for Agents 1, 3, and 4. Every design decision in PLM is made with replicability in mind. Approving this POC is approving the reference architecture for the full Agentforce platform.

3. **"You become the catalog authority — not IT."**  
   The most tangible outcome for the business: a catalog analyst writes a rule in Portuguese, and it is live in production in minutes. No developer. No deployment window. No sprint cycle. Claro's business teams regain control of their own product offering.

---

## Slide Structure

### Slide 1 — Title
**CLARO Agente PLM: Autoria Inteligente de Catálogo com Agentforce**  
Salesforce Professional Services LATAM · POC · June 2026

---

### Slide 2 — O Problema: O Catálogo Que Não Acompanha o Negócio
*"127 regras. Cada mudança exige um deploy. O mercado não espera."*

- **Pain 1:** Cada nova oferta, bundle ou ajuste de preço exige um sprint de engenharia e um deploy cross-org — processo de dias a semanas
- **Pain 2:** Validações volumosas fazem overflow de CPU e heap — o pipeline falha silenciosamente; erros chegam ao downstream sem ser detectados
- **Pain 3:** Enquanto Vivo e TIM lançam combos em semanas, Claro aguarda aprovação de TI para alterar uma regra

*Talking point para Fabrício:* "O catálogo é o coração da oferta comercial da Claro. Se o coração bate devagar, o negócio inteiro desacelera."

---

### Slide 3 — O Diagnóstico: Onde o Sistema Falha
*Three-column: Processo / Impacto / Causa raiz*

| Processo | Impacto | Causa raiz |
|---|---|---|
| Alteração de regra | Dias (sprint + deploy) | BRE acoplado ao pipeline de engenharia |
| Validação em lote | Falhas silenciosas | Processamento síncrono — overflow de heap |
| Diagnóstico de erros | Horas de investigação manual | Sem observabilidade nativa; sem DLQ |
| Auditoria LGPD / ANATEL | Sem rastreabilidade | BRE sem lineage de regras |

---

### Slide 4 — A Solução em Uma Frase
*"Compilação por IA. Execução determinística. Zero redeploy."*

**Visual:** Two-lane diagram  
- Lane 1 (Admin Agent → Einstein LLM → AST JSON → Plm_Rule_Spec__c): Rule authored in Portuguese → Compiled to JSON → Live in seconds  
- Lane 2 (Ops Agent → Async CSV Ingest → AST Walker → Diagnostic): Batch uploaded → Evaluated at <50ms/record → HTML report generated

*No redeploy. No developer. No silent failures.*

---

### Slide 5 — Arquitetura de Alto Nível
*"Três camadas: experiência, inteligência, motor."*

```
EXPERIENCE   │ LWC Upload Wizard  ·  Agentforce Chat Console
             │
INTELLIGENCE │ Admin Agent (compile-time)  ·  Ops Agent (runtime)
             │ Atlas Reasoning Engine  ·  Einstein Trust Layer
             │
ENGINE       │ AST Walker (Apex puro, <50ms)  ·  DLQ + Finalizers
             │ Platform Events  ·  Compile Snapshots (LGPD lineage)
```

*Key message:* LLM only at authoring time. At runtime, it's pure Apex — deterministic, fast, auditable. No AI in the critical path.

---

### Slide 6 — Os KPIs: O Que Muda
*Before / After table — make it visual*

| KPI | Hoje | Com Agentforce PLM |
|---|---|---|
| Tempo para alterar uma regra | Dias (sprint + deploy) | **0 minutos — sem redeploy** |
| Tempo de avaliação por registro | Minutos (lote síncrono) | **< 50ms por registro** |
| Capacidade por lote | Instável em volumes altos | **≤ 10.000 linhas — estável** |
| Falhas silenciosas | Sim — não rastreadas | **Zero — 100% capturado em DLQ** |
| Investigação de erros | Horas (manual) | **Segundos — relatório HTML gerado por IA** |
| Auditoria LGPD | Sem rastreabilidade | **Lineage completo — Spec_Key + Snapshots** |

---

### Slide 7 — Por Que Agora: O POC Como Beachhead
*"O PLM é o primeiro de quatro agentes."*

**Timeline visual:** PLM POC (Week 8) → Agents 1/3/4 (post-POC roadmap)

- Agent 1: Knowledge Base — atendimento ao cliente via base de conhecimento
- **Agent 2: PLM — este POC → referência arquitetural para todos os outros**
- Agent 3: Next Best Offer — propensão de oferta via sistema NBO
- Agent 4: Lead Qualification — qualificação de leads

*Talking point:* "Cada decisão de design deste POC é tomada pensando nos três agentes seguintes. Aprovando este POC, a Claro aprova a arquitetura da plataforma completa."

---

### Slide 8 — Plano de Entrega: 8 Semanas
*Gantt visual simplificado*

| Semana | Fase | O Que Acontece |
|---|---|---|
| 1–2 | Descoberta & Arquitetura | Alinhamento técnico, dependências confirmadas, registro de testes acordado |
| 3 | Sprint 1 — Fundação | Motor de ingestão CSV + segurança e configuração de plataforma |
| 4 | Sprint 2 — Motor Core | AST Walker + compilador LLM + observabilidade e DLQ |
| 5 | Sprint 3 — Inteligência & UX | Agentes Admin + Ops + narrativa diagnóstica + componentes LWC |
| 6–7 | UAT & Fine-tuning | Testes de carga, run paralelo vs. BRE legado, revisão legal LGPD |
| 8 | Go-Live & Hipercuidado | Deploy em produção, transferência de conhecimento, encerramento formal |

**Critical dependencies box:** 6 pré-requisitos que a Claro precisa confirmar nas primeiras 2 semanas (sandbox, licenças Agentforce, artigos de conhecimento, LGPD)

---

### Slide 9 — O Time Salesforce PS
*"A equipe que construiu este padrão."*

| Papel | Dedicação |
|---|---|
| Arquiteto Técnico | 8 semanas — integral |
| Consultor Técnico | 8 semanas — integral |
| Especialista em QA | 8 semanas — 1.5x |
| Gerente de Projeto | 8 semanas — dedicado, faturável (pago pela Claro) |

*Talking point:* "Este não é um time que está aprendendo este padrão no seu projeto. É o time que o definiu."

---

### Slide 10 — Riscos e Mitigações
*Honest risk table — builds trust*

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Artigos de Conhecimento não prontos na semana 1 | Alta | Gate formal: Sprint 3 não começa sem KB confirmada. PM escalona imediatamente. |
| Licença Agentforce não ativa no sandbox | Média | PS valida via chamada ConnectApi no fim da semana 2. Blocker escalado ao CSM Salesforce. |
| Overflow em lotes >10k linhas | Média | Arquitetura assíncrona mitiga até 10k. Acima de 50k está no backlog (W3.2). |
| LGPD — sign-off jurídico atrasado | Média | Janela da semana 6 agendada na semana 2. Sem sign-off = sem go-live. Não há exceção. |
| Deploy cross-org bloqueado (CannotQuickDeployError) | Confirmado | Registro RunSpecifiedTests acordado com DevOps Claro nas semanas 1–2. |

---

### Slide 11 — O Que Precisamos da Claro (Pré-Requisitos)
*Make it a checklist — clear ownership*

| # | Pré-requisito | Responsável Claro | Prazo |
|---|---|---|---|
| 1 | Cadeia de sandboxes provisionada (Dev + SIT + Ibuy UAT) | Luciano | Fim da semana 1 |
| 2 | 3–5 CSVs de produção para profiling de volume | Lucas | Fim da semana 1 |
| 3 | Licença Agentforce Unlimited + créditos Einstein ativos | Luciano | Fim da semana 2 |
| 4 | 10–15 FAQs com Data Categories no sandbox | Fabrício / Analistas | Fim da semana 2 |
| 5 | Registro RunSpecifiedTests acordado com PS | Luciano / DevOps | Semanas 1–2 |
| 6 | Janela de revisão jurídica LGPD agendada na semana 6 | Jurídico Claro | Agendada na semana 2 |

*Talking point:* "Seis dependências. Todas resolvíveis em duas semanas. O maior risco deste projeto não é técnico — é operacional. O PM Salesforce rastreia tudo isso desde o primeiro dia."

---

### Slide 12 — Próximos Passos
*"Three actions to start the clock."*

1. **Confirmar pré-requisitos de ambiente** — Luciano provisiona sandbox chain na semana 1
2. **Agendar kickoff técnico** — TA + Lucas + Luciano para alinhar schema JSON e registro RunSpecifiedTests
3. **Aprovar engajamento** — confirmar modelo T&M e equipe PS LATAM alocada

*Cierre:* "Em 8 semanas, a Claro terá o catálogo que o negócio merece — governado por analistas, validado em milissegundos, auditável para o LGPD. E a arquitetura que torna os próximos três agentes possíveis."

---

## Objection Handling

**"8 semanas é muito apertado para isso."**  
> A janela foi definida pela própria Claro e é viável com a equipe dedicada que estamos trazendo. Não é exploratório — é entrega acelerada de um padrão comprovado. O que comprime a janela não é complexidade técnica, são as dependências de ambiente. Se resolvermos as seis dependências nas primeiras duas semanas, 8 semanas é confortável.

**"Por que não usar o BRE legado e apenas adicionar o Agentforce por cima?"**  
> O BRE é o problema, não a fundação. Ele não tem API de integração limpa, não tem rastreabilidade de lineage, e não resolve o overflow de CPU. Colocar Agentforce por cima do BRE seria construir inteligência sobre instabilidade. O AST Walker é mais rápido, mais auditável, e foi desenhado especificamente para as restrições dos ambientes da Claro (sem Platform Cache, cross-org deploy).

**"Posso usar Platform Cache para simplificar o cache de regras?"**  
> Não — Platform Cache está explicitamente proibido nos ambientes STORM_PLM e Ibuy. Esta é uma restrição de infraestrutura Claro, não uma escolha de design. O static Map cache é a única alternativa suportada — e é exatamente o que a arquitetura usa.

**"E a conformidade LGPD — o Einstein Trust Layer é suficiente?"**  
> Para este POC, sim — com a validação jurídica da Claro. Zero-Data Retention Policy garante que nenhum dado da Claro é usado para treinar modelos externos. O lineage de regras (Spec_Key + Source_Hash + Compile Snapshots) satisfaz os requisitos de rastreabilidade do ANATEL. O sign-off jurídico na semana 6 é o gate formal que confirma isso antes do go-live.

**"Por que PS LATAM? Não posso usar um parceiro local?"**  
> Este padrão específico — AST Walker, DLQ-first, Agentforce PLM Admin/Ops, integração ConnectApi com Prompt Templates — foi desenvolvido e documentado pelo time PS LATAM. Um parceiro local estaria aprendendo esta arquitetura no seu projeto, com o seu prazo de 8 semanas. PS LATAM já passou pela curva de aprendizado.
