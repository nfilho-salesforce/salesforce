# 6. Timelines

## 6.1 Visão por Fases (Gantt)

```
         S1          S2          S3          S4
         ────────────────────────────────────────
F1 Prep  ████████
         ────────────────────────────────────────
F2 ORG   ████████
         ────────────────────────────────────────
F3 Agts              ████████
         ────────────────────────────────────────
F4 WApp              ████████
         ────────────────────────────────────────
F5 Endpt             ████████
         ────────────────────────────────────────
F6 Scale             ████████  ████████
         ────────────────────────────────────────
F7 Tests                       ████████  ████████
         ────────────────────────────────────────
F8 Docs                                  ████████
         ────────────────────────────────────────
```

> S1–S2 = execução técnica intensa (70h/sem) · S3 = testes + CPQD · S4 = go-live + documentação (35h)

---

## 6.2 Visão por Entregáveis Macro

```
    Semana 1          Semana 2          Semana 3          Semana 4
       │                 │                 │                 │
      [M1]             [M2]             [M3]           [M4][M5][M6]
       │                 │                 │                 │
       ▼                 ▼                 ▼                 ▼
  Arquitetura        6 Agentes +       1º Ciclo          Go-live +
  aprovada +         WhatsApp +        CPQD +            Runbook +
  Nova ORG ativa     11 Endpoints      Homologação       Encerramento
                     validados         Dataprev
```

---

## Milestones

| Marco | Semana | Entregável |
|-------|:------:|-----------|
| **M1** | Fim S1 | Arquitetura aprovada · nova ORG ativa com Data Cloud · RACI assinado |
| **M2** | Fim S2 | 6 agentes Wave 2 operacionais · WhatsApp configurado · 11 endpoints validados |
| **M3** | Fim S3 | 1º ciclo CPQD executado · homologação Dataprev concluída · testes de volume OK |
| **M4** | Fim S4 | Go-live em janela protegida · hypercare ativo |
| **M5** | Fim S4 | Runbook entregue · dashboards Splunk ativos |
| **M6** | Fim S4 | Encerramento formal e aceite do cliente |

---

## Lógica de Compressão (v3.0)

| Movimento | Impacto |
|-----------|---------|
| F2 consolidada: Full Copy + Data Cloud Setup em tarefas únicas | 96h → 20h |
| F3 consolidada: todos os 6 agentes + orquestrador em ciclo único | 104h → 16h |
| F4 consolidada: WhatsApp end-to-end em tarefa única | 28h → 12h |
| F5 consolidada: todos os endpoints em tarefa única, MuleSoft removido | 78h → 16h |
| F1+F2 paralelas na S1; F3+F4+F5 paralelas na S2 | 7 sem → 4 sem |
