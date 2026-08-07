# 4. Fases, Atividades e Esforço

## Fase 1 — Preparação e Planejamento (Semana 1) · 40h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 1.1 | Kick-off com stakeholders (Dataprev + Salesforce PS) | 4h | TA + PM |
| 1.2 | Levantamento e documentação do ambiente atual (ORG, integrações, endpoints) — assistido por IA | 10h | TA + TC |
| 1.3 | Mapeamento detalhado dos 11 endpoints (configs, credenciais, certificados) | 6h | TC |
| 1.4 | Revisão de licenças: Agentforce, DSCs, Scale Test Add-On, Digital Engagement | 4h | PM + TA |
| 1.5 | Definição da arquitetura do novo ambiente e aprovação | 8h | TA |
| 1.6 | Plano detalhado, cronograma e RACI (gerado com IA) | 4h | PM |
| 1.7 | Governança: acesso CPQD (IP/geo), janelas de deploy | 4h | PM + TA |
| 1.8 | **Envio do request de provisionamento da nova ORG** (disparar SLA Salesforce) | 0h | TA + AE |

> **Nota:** Provisionamento solicitado no fim da S1. O SLA de resposta Salesforce (~1 semana) é coberto pela S2, aproveitada para F3–F5.

---

## Fase 2 — Nova ORG + Data Cloud (Semana 1) · 20h

> Revisado pelo arquiteto técnico: escopo focado nos testes CPQD — sem provisionamento direto de acesso ao CPQD na ORG, sem orquestrador, Data Cloud em setup básico.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 2.1 | Full Copy Sandbox para nova ORG + configuração de perfis, permissões e usuários | 8h | TC |
| 2.3 | Data Cloud Setup: Data Streams, DLOs, Identity Resolution e Zero Copy Oracle OCI | 8h | TA + TC |
| 2.6 | Validação de capacidade de LLM + Named Credentials e Connected Apps | 4h | TA |

> **Consolidações:** 2.2 incorporada em 2.1 · 2.4 e 2.5 incorporadas em 2.3 · 2.7 incorporada em 2.6 · 2.8 (orquestrador) removida do escopo.

---

## Fase 3 — Agentes Wave 2 + Bases de Conhecimento (Semana 2) · 16h

> Baseado na experiência com ambientes de homologação equivalentes: todos os agentes + orquestrador instalados no mesmo ciclo.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 3.1 | Configuração de todos os agentes Wave 2 + bases de conhecimento + orquestrador (MEC, MDS, MS, Primeira Infância, MTE, IBAMA) | 16h | TA + TC |

> **Consolidação:** atividades 3.2 a 3.8 incorporadas em 3.1.

---

## Fase 4 — Digital Engagement / WhatsApp (Semana 2) · 12h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 4.1 | Configuração e validação completa do canal Digital Engagement + WhatsApp (número dedicado, envio/recebimento, integração com Agentforce) | 12h | TA + TC |

> **Consolidação:** atividades 4.2 a 4.4 incorporadas em 4.1.

---

## Fase 5 — Reconfiguração de Endpoints e Integrações (Semana 2) · 16h

> Escopo focado nas integrações necessárias para os ciclos CPQD. MuleSoft removido do escopo.

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 5.1 | Reconfiguração de todos os endpoints e integrações: CPQD, Oracle OCI, IBAMA, MTE, PCI Infra, GovBR, MEC, MDS, MS, Primeira Infância | 16h | TA + TC |

> **Consolidação:** atividades 5.2 a 5.8 incorporadas em 5.1. MuleSoft (5.9) removido.

---

## Fase 6 — Scale Test Add-On + Validação CPQD (Semanas 2–3) · 60h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 6.1 | Configuração do Scale Test Add-On no novo ambiente | 8h | TA |
| 6.2 | Integração scripts JMeter CPQD via GitHub | 8h | TC |
| 6.3 | Trial Accuracy Checker: validação com carga reduzida | 8h | TA + TC |
| 6.4 | Scale Agent: configuração de monitoramento em tempo real | 8h | TA |
| 6.5 | Execução dos primeiros ciclos CPQD (qualidade + guardrails) | 16h | TA + TC |
| 6.6 | Análise de resultados e ajustes | 12h | TA + TC |

---

## Fase 7 — Testes, Homologação e Go-Live (Semanas 3–4) · 96h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 7.1 | Scripts de testes funcionais Agentforce (Script Recorder + Agentforce Vibes) | 16h | TC |
| 7.2 | Testes de integração ponta a ponta (11 endpoints) | 24h | TA + TC |
| 7.3 | Testes de volume/performance (meta: 100k RPS) | 16h | TA + TC |
| 7.4 | Homologação com time técnico Dataprev | 12h | TA + PM |
| 7.5 | Plano de rollback documentado e validado | 8h | TA + PM |
| 7.6 | Go-live em janela protegida (fora de horário comercial BR) | 8h | TA + TC |
| 7.7 | Hypercare pós go-live (monitoramento ativo — 5 dias úteis) | 12h | TC |

---

## Fase 8 — Documentação, Runbook e Handover (Semana 4) · 54h

| ID | Atividade | Esforço | Papel |
|----|-----------|---------|-------|
| 8.1 | Documentação técnica contínua (arquitetura, endpoints, acessos) — gerado com IA | 12h | TA |
| 8.2 | Runbook operacional completo (elimina dependência Renato + Melyssa) — gerado com IA | 12h | TC + TA |
| 8.3 | Ativação de dashboards Splunk + alertas proativos | 8h | TA |
| 8.4 | Consolidação e revisão final de toda a documentação | 8h | TA + TC |
| 8.5 | Sessão de handover e treinamento time Dataprev | 4h | TA + PM |
| 8.6 | Registro de decisões, lessons learned e encerramento | 6h | PM |
| 8.7 | Encerramento formal e aceite do cliente | 4h | PM |
