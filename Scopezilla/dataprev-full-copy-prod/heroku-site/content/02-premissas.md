# 2. Premissas

## Técnicas

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

## Comerciais / Contratuais

- **P-11:** Licenças Agentforce for Service, Service Cloud, Data Cloud (DSCs), Digital Engagement e Einstein estarão aprovadas antes do kick-off
- **P-12:** Signature Success ativo para o novo ambiente (recomendado dado volume e criticidade)
- **P-13:** Flex Credits aprovados: sizing CPQD = ~3.110 pacotes / R$ 3,11M (6 meses, cenário máximo 12 ciclos/mês)
- **P-14:** Contrato-mãe BRL 35,5M como referência; novo ambiente é complementar

## Operacionais

- **P-15:** Janelas de deploy protegidas: sem atualizações em horário comercial BR (08h–20h)
- **P-16:** Times Dataprev responsáveis por cada integração estarão disponíveis nas janelas de reconfiguração (semanas 3–5)
- **P-17:** Renato e Melyssa disponíveis para apoio na carga de bases de conhecimento (semanas 2–4)
- **P-18:** Governança de acesso CPQD (restrições IP/geolocalização) definida antes do início dos testes

## Uso de IA para Aceleração de Entrega

- **P-19:** **Documentação assistida por IA** (Claude/Copilot): geração de documentação técnica, runbook e RACI — redução estimada de ~35% no esforço de documentação (~12–16h de economia)
- **P-20:** **Scale Agent (Pilot — Sprint 260):** monitoramento em tempo real dos ciclos CPQD com diagnóstico automático de root cause — reduz tempo de análise de falhas
- **P-21:** **Trial Accuracy Checker:** valida configuração com carga reduzida antes de escalar — reduz retrabalho no ciclo de homologação
- **P-22:** **Script Recorder Chrome Plugin:** grava fluxos de UI e gera scripts Playwright automaticamente — redução de ~30% no esforço de criação de scripts de teste
- **P-23:** **Agentforce Vibes (Pilot — Summer '26):** geração automatizada de scripts de teste de qualidade de resposta para os 6 agentes Wave 2
- **P-24:** **Ganho total estimado com IA:** ~70–90h de redução versus abordagem 100% manual (≈12–14% do esforço total)
