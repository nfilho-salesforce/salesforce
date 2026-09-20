# PRODESP — DER-SP · Plano de Entrega

**Duração de programa (benchmark-based): 16–31 semanas** — derivada top-down a partir da forma do engagement (5 épicos, mix 4L + 1S — E01 M→L nesta revisão pelo canal de telefonia via CTI, E05 L→S pelo Appointment Assistant nativo substituindo o site guest customizado —, Field Service + Service Cloud/Agentforce Contact Center Enterprise, dois canais WhatsApp+CTI, 2 integrações ponto-a-ponto), classificada como Multi-Cloud/Medium — baseline mantido em 16–24 semanas, ajustada +10% por UI/UX customizada sem padrão nativo (E04) + 10% por sobrecarga de governança/auditoria (G0305, G0211) + 10% por risco de padrão de integração CTI ainda não fixado (E01/E02, G0524) → 24×1,30 = 31,2, arredondado para 31. Não é um compromisso.

> *Esta figura é baseada em benchmark, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Números finais são confirmados através do acordo comercial aplicável.*

**Contra o alvo do cliente**: Homologação jan/fev 2027 (~19–23 semanas a partir de 17/set/2026) cai dentro da faixa; Produção abril 2027 (~30 semanas) cai perto da ponta alta — pouca folga se os fatores de risco abaixo se confirmarem no lado mais pesado.

**O que mais amplia a faixa** (resolver estes primeiro para estreitá-la):
- **E01** — padrão técnico da integração CTI com a URA ainda não fixado, Open CTI clássica em retirada (fev/2028) → resolver G0524, validar API exposta pelo fornecedor de telefonia (Instinct).
- **E03** — console + escalonamento N/N-10 sobre trilha de auditoria aberta → resolver G0305 antes do build detalhado.
- **E04** — as 3 travas de negócio são hoje só online; enforcement offline é premissa de corte de escopo → confirmar G0413.

**Critical path: E02 → E03 → E04 → E05** — a fundação de registro/integrações (E02) gate todo o resto; o canal digital (E01) só depende de E02 e pode avançar em paralelo à Fase 2. Atraso em qualquer épico do caminho crítico se propaga para os seguintes.

---

## Fase 0 — Resolução de Discovery *(sequência 1 de 5)*

80 gaps registrados no levantamento de requisitos (>15, dispara Fase 0 por regra; 5 permanecem abertos, 7 são conflitos de fonte). Fecha as questões bloqueadoras antes do build: especificação de payload/API do SIGOR e SIGEO com o DER/Stefanini; trilha de auditoria de overrides manuais (G0305); limite contratual da UBA por CGR para escalonamento cross-CGR (G0309); padrão técnico da integração CTI com a URA (G0524); premissa de DevOps/pipeline versionado (G0415); dimensionamento do workstream de Change Management/Operação Assistida (G0515).

**Critério de sucesso**: G0305, G0309, G0524, G0415 respondidos; especificação SIGOR/SIGEO assinada; Change Management dimensionado.
**Risco**: sem resolução, E03 entra em build com trilha de auditoria não confirmada e E01/E02 avançam sem padrão técnico de CTI fixado — retrabalho no console e na integração de telefonia.

## Fase 1 — Fundação: Registro da Ocorrência e Integrações *(sequência 2 de 5)*

**Épicos**: E02.

Modelo núcleo (Work Order, Work Type de 100+ subtipos, 2 slots de Assigned Resource) e as duas integrações legadas: SIGOR (dupla convivência, Platform Events/CDC assíncrono) e SIGEO (correção de lat/long, callout síncrono). Fundação sobre a qual o canal digital e o motor de despacho escrevem `[KA-6240: Work Order Management precede Workforce/Dispatch na sequência recomendada de setup do Field Service]`.

**Critério de sucesso**: Work Order criável por qualquer canal; sincronização SIGOR validada; callout SIGEO testado.
**Risco**: divergência de dados na dupla convivência SIGOR — monitorar volume de conflitos nas primeiras semanas.

## Fase 2 — Despacho Automatizado e Canal Digital *(sequência 3 de 5, depends on: E02)*

**Épicos**: E03, E01 (concorrentes — nenhum depende do outro, ambos só de E02).

Motor de agendamento e otimização do Field Service com escalonamento N/N-10 customizado e console do Dispatcher (12 licenças); em paralelo, canal digital — WhatsApp com triagem Agentforce e telefonia via integração CTI com a URA (screen-pop no Service Console) — com fila humana única 24x7.

**Critério de sucesso**: despacho aciona a viatura correta nas 14 CGRs; console operacional nos 4 turnos; triagem WhatsApp e telefonia via CTI criam Work Order de ponta a ponta.
**Risco**: G0305/G0309/G0524, se não resolvidos na Fase 0, forçam retrabalho no console, no modelo de território e na integração de telefonia durante esta fase.

## Fase 3 — Execução em Campo *(sequência 4 de 5, depends on: E03)*

**Épicos**: E04.

App único de Field Service Mobile para os 1.152 operadores das 14 UBAs, com push nativo, retry ao reconectar, briefcase offline restrito à ocorrência em andamento, e as 3 travas de negócio (recusa com motivo, foto obrigatória, check-in geolocalizado) em modo online.

**Critério de sucesso**: app executa o ciclo completo até o encerramento com evidência; piloto com subconjunto de UBAs antes do rollout estadual.
**Risco**: known issue de Service Appointment com licença Field Service Community; enforcement offline das travas fora do MVP.

## Fase 4 — Rastreamento, Visibilidade e Estabilização *(sequência 5 de 5, depends on: E03, E04)*

**Épicos**: E05.

Rastreamento do cidadão via Appointment Assistant nativo do Field Service (sem build de site guest dedicado) e painel de gestores com 4 indicadores agregados — o mapa/Gantt do C2C com Aerial Routing nativo já é entregue na Fase 2 como parte do Console do Dispatcher. Fecha com UAT em escala estadual (298 viaturas, 1.152 operadores, 14 CGRs) e hypercare antes do go-live pleno.

**Critério de sucesso**: Appointment Assistant validado contra o comportamento com 2ª viatura vinculada e o canal de entrega por SMS ([KA-6140]/[KA-6156]); UAT estadual assinado pelo DER; hypercare concluído sem bloqueadores críticos.
**Risco**: Appointment Assistant ainda não validado em detalhe contra os requisitos específicos do DER — risco de gap de comportamento descoberto tarde no template nativo.

---

## Processos Padrão (consolidados, não repetidos por fase)

- **Testes**: por fase, mais UAT em escala estadual antes do go-live pleno (Fase 4).
- **Implantação**: sandbox Developer para squads, Full/Partial para UAT com volume representativo das 14 CGRs.
- **Treinamento**: personalizado por persona, foco nos técnicos de campo das UBAs — parte do workstream de Change Management (Fase 0 dimensiona, execução atravessa as Fases 3–4).

## Riscos Consolidados

| Risco | Fase mais exposta | Mitigação |
|---|---|---|
| G0305/G0309/G0524 não resolvidos a tempo | Fase 0 → 2 | Levar como perguntas bloqueadoras formais ao DER/Stefanini antes do fim da Fase 0 |
| Divergência SIGOR (dupla convivência) | Fase 1 | Log de erro + alerta ao C2C; monitorar volume nas primeiras semanas |
| Known issue de licença Field Service Community | Fase 3 | Monitorar releases; plano de contingência = migrar para licença padrão se crítico |
| Appointment Assistant não validado em detalhe contra requisitos do DER | Fase 4 | Revalidar `[KA-6140]`/`[KA-6156]` antes do build detalhado |
| Enforcement offline das 3 travas fora do MVP | Fase 3 | Documentar como premissa de redução de escopo (G0413) para validação formal com o cliente |

---

Grounding: 5 fases com 3 decisões marcadas — 1 grounded ([KA-6240]), 2 inferred (agrupamento E01+E03 na Fase 2 por dependência compartilhada não-bloqueante; E05 unido à estabilização/hypercare), 0 flagged assumptions.

O disciplinar e o roster nomeado (papéis, senioridade, localização, contagem defensável por fase) para entregar este plano vêm da skill `estimate`.
