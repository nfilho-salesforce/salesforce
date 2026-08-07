# 7. Sizing de Flex Credits (CPQD)

Baseado nas informações pós-reunião CPQD em 19/06 (Thiago).

## Parâmetros

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

## Cenários

| Cenário | Ciclos/mês | Meses | Total pacotes | Total R$ |
|---------|:----------:|:-----:|:-------------:|:--------:|
| Mínimo | 4 | 6 | ~1.037 | ~R$ 1,04M |
| Médio | 8 | 6 | ~2.074 | ~R$ 2,07M |
| **Máximo (escolhido)** | **12** | **6** | **~3.110** | **R$ 3,11M** |

---

## Composição por Ciclo (1 agente)

| Tipo de teste | Requisições |
|---------------|:-----------:|
| Qualidade de resposta | 8.000 |
| Guardrails | 3.000 |
| Pentest | 500 |
| Exploratório | 500 |
| **Total** | **12.000** |
