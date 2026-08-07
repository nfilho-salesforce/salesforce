# 8. Perguntas em Aberto

> **Legenda:** 🔴 Bloqueadora (não inicia sem resposta) · 🟠 Alta prioridade (impacta timeline) · 🟡 Média prioridade

## Bloqueadoras — Pré-Kick-off

| ID | Pergunta | Impacto | Dono |
|----|----------|---------|------|
| **Q-01** | Volume de licenças Agentforce for Service para ambiente de testes? | ORG não pode ser ativada sem licenças 🔴 | Saulo, Milton (Dataprev) |
| **Q-02** | Volume de DSCs (Data Cloud) necessários? | Subdimensionamento exige ajuste contratual 🔴 | Saulo, Milton (Dataprev) |
| **Q-04** | Aprovação orçamentária para o ambiente produtivo adicional? | Sem aprovação, projeto não pode ser contratado 🔴 | Fernanda (AE) + gestão Dataprev |
| **Q-05** | Flex Credits aprovados? Sizing: 3.110 pacotes / R$ 3,11M (6 meses) | Sem créditos, ciclos CPQD paralisam 🔴 | Vinícius Machuca / Aline Sabino |

## Bloqueadoras — Por Fase

| ID | Pergunta | Impacto | Dono |
|----|----------|---------|------|
| **Q-06** | SLA de provisionamento da nova ORG — quanto tempo? | Pode atrasar S2; estratégia paralela absorve até 1 semana 🟠 | Salesforce Account Team / Renata |
| **Q-07** | O modelo de dias reservados do Scale Test atende cadência contínua do CPQD? | Se não, Scale Test perde valor estratégico 🟠 | CPQD (Thiago) |
| **Q-08** | Configuração Oracle OCI de 08/05/2026 está documentada e acessível? | Sem docs, esforço de F2/F5 pode dobrar (+30h) 🟠 | Renato / Dataprev DBA |
| **Q-10** | Número WhatsApp Business dedicado — Dataprev iniciou processo com Meta? | Registro na Meta leva 1–3 semanas; atrasa F4 🟠 | Dataprev (canal WhatsApp) |
| **Q-14** | Oracle OCI pode ser apontado para uma segunda ORG produtiva sem impacto no ambiente atual? | Pode inviabilizar arquitetura Zero Copy no novo ambiente 🟠 | Dataprev DBA / Oracle OCI team |

## Antes do Kick-off

| ID | Pergunta | Impacto | Dono |
|----|----------|---------|------|
| **Q-03** | Scale Test Add-On: o que já está habilitado? Qual o custo para a Dataprev? | Sem confirmação, F6 não pode iniciar 🔴 | Renata + Vrajesh (Scale Center) |
| **Q-09** | MuleSoft está no contrato? Qual o escopo? | +35h de esforço e possível +1 semana 🟠 | Jurídico / Comercial Dataprev |

## Média Prioridade

| ID | Pergunta | Impacto | Dono |
|----|----------|---------|------|
| **Q-11** | Validação dos 12k req/agente/ciclo — consumo real nos logs confirma? | Sizing de Flex Credits pode estar errado 🟡 | Renato (Dataprev) |
| **Q-12** | Sanity check: novo ambiente absorve 12 ciclos/mês sem se tornar gargalo? | Pode exigir revisão arquitetural pós go-live 🟡 | Vinícius Machuca / Aline Sabino |
| **Q-13** | Governança de acesso CPQD (restrições IP/geolocalização) definida? | Risco de uso indevido das licenças do ambiente de testes 🟡 | Dataprev (segurança) + CPQD |
