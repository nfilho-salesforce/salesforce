# 1. Contexto e Objetivo

A Dataprev opera hoje uma ORG de produção (`00Das00000Cz7qb` / prod11) com Agentforce (6 agentes Wave 2), Service Cloud, Data Cloud e Digital Engagement (WhatsApp), gerando **~40k mensagens/dia** com pico de **15k conversation entries/min**.

O **CPQD** realiza certificação independente com testes automatizados massivos (JMeter), mas as sandboxes atuais limitam o throughput a **~120 RPS / ~200 req/hora de LLM** — causando falsos negativos, atrasos e dependência crítica de Renato + Melyssa para replicação manual de bases (1 dia por instância).

**Decisão estratégica** (Vinícius Machuca + Aline Sabino, 11/06/2026): provisionar uma **nova ORG de produção dedicada** exclusivamente para testes de estresse e homologação massiva. O **Scale Test Add-On** é camada complementar (não alternativa) — cobre slots de burst controlado na Full Copy Sandbox existente.

## Objetivos do Projeto

| # | Objetivo | Indicador de Sucesso |
|---|----------|----------------------|
| O-1 | Provisionar nova ORG produtiva na mesma região (Brasil / prod11), Summer '26 | ORG ativa, mesma versão, mesmo datacenter |
| O-2 | Replicar arquitetura completa: Data Cloud (Zero Copy OCI), Agentforce + orquestrador, Digital Engagement | 6 agentes + orquestrador respondendo no novo ambiente |
| O-3 | Reconfigurar todos os endpoints e integrações críticas (11 no total) | Todos os endpoints validados ponta a ponta |
| O-4 | Configurar Scale Test Add-On para ciclos CPQD (JMeter via GitHub) | 1º ciclo CPQD executado com sucesso no novo ambiente |
| O-5 | Implantar Proactive Monitoring (Splunk) + runbook operacional | Dashboards ativos; dependência Renato/Melyssa eliminada |
| O-6 | Habilitar número WhatsApp Business dedicado para testes | Canal ativo sem interferência no número produtivo |
