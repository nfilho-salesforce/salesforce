# PRODESP — DER-SP · Solução Salesforce para Atendimento Emergencial nas Rodovias

**Escopo do MVP**: Field Service + Agentforce + Service Cloud (Digital Engagement + Omni-Channel — canais WhatsApp e telefonia via integração CTI), produção estadual nas 14 CGRs desde o dia 1 (298 viaturas, 1.152 operadores de campo, 14 UBAs terceirizadas).

**Homologação**: jan/fev 2027 · **Produção**: abril 2027.

T-shirt sizes neste documento expressam **complexidade relativa, não esforço** — não são convertíveis em horas e não devem ser multiplicados por uma taxa para gerar preço. Para prazo, ver a skill `roadmap`; para preço indicativo, `commercials` (com taxa validada pelo cliente).

---

## 1. Arquitetura — Fundamentos

### 1.1 Estratégia de Org

**Org única.** Governança unificada, modelo de dados compartilhado entre os canais digitais (Agentforce/WhatsApp e telefonia via CTI), o motor de despacho (Field Service) e o app de campo — todos operam sobre o mesmo Work Order/Service Appointment. *(decisions/0004, que substitui decisions/0002, ratificada pelo usuário em 2026-09-20.)*

### 1.2 Seleção de Produtos

- **Field Service** — motor de agendamento e otimização (considerando regras de trabalho, Skills, território e disponibilidade), Work Order/Service Appointment, app mobile de execução em campo, Console do Dispatcher com mapa/Gantt (Aerial Routing nativo), Appointment Assistant para rastreamento do cidadão.
- **Service Cloud — Agentforce Contact Center Enterprise + Digital Engagement + Omni-Channel** — dois canais de entrada: WhatsApp (abertura de chamado, triagem por IA) e telefonia via integração CTI com a URA (screen-pop no Service Console), ambos transbordando para a mesma fila humana única 24x7. Número de licenças a revalidar à luz do canal de telefonia adicional. Escopado *apenas* ao canal de socorro emergencial; exclusão geral de Service Cloud para atendimento amplo permanece válida. *(decisions/0004.)*
- **Fora do MVP**: Salesforce Voice (telefonia nativa) e a substituição da própria URA/0800 — projeto de infraestrutura de telefonia separado, ainda em viabilização entre DER e PRODESP (decisions/0003); objeto nativo Incident/CSIM (dedup fica em alerta manual); Enhanced Scheduling and Optimization — ESO (roteamento usa Aerial Routing nativo); Partner Community Portal (7ª superfície de visibilidade, candidato a nova epic no Roadmap). Nota: Experience Cloud não é um produto/capacidade separada deste MVP — o rastreamento do cidadão (E05) usa o Appointment Assistant, um template de Experience Cloud já embutido na licença de Field Service, sem build de site guest dedicado.

### 1.3 Licenciamento

- Agentforce Contact Center Enterprise: número de licenças a revalidar (dois canais — WhatsApp + telefonia via CTI).
- Dispatcher Console: 12 licenças individuais (6/turno × 4 turnos 12x36).
- Field Service Mobile: 1.152 operadores de campo, licença **Field Service Community (Partner License)** — risco monitorado: known issue de erro em Service Appointment com licença Community `[KB:field_service_dev.md:27272-27273]`.
- Nenhum hardware AVL — rastreamento tier P (GPS do próprio app de campo).

### 1.4 Modelo de Dados

Objetos padrão do Field Service — sem objetos customizados de negócio no núcleo do fluxo:
- **Work Order** — a ocorrência. 2 slots de **Assigned Resource** (não Work Order Line Item) para acomodar uma 2ª viatura no mesmo chamado `[extends: padrão multi-recurso do Field Service — um WO, múltiplos Assigned Resource]`.
- **Work Type** — catálogo completo de 100+ subtipos, disponível desde o dia 1; macro-tipo (pane/sinistro/inspeção) como picklist informativo, sem Record Type.
- **Contact** — o relator (não anônimo, não Person Account).
- **Service Appointment** — status lifecycle padrão; briefcase offline prima apenas a ocorrência em andamento (sem Task, sem histórico encerrado) `[KB:field_service_dev.md:27274-27275]`.
- **Service Resource / Service Resource Skill / Skill Requirement** — motor de aderência (E03).

Sem migração de dados — é um build greenfield; SIGOR/SIGEO entram por integração, não por carga inicial.

### 1.5 Arquitetura de Integração

Dois sistemas legados do DER-SP em escopo — abaixo do limiar de 3 integrações que justificaria middleware dedicado. **Point-to-point**, sem MuleSoft `[KA-0012]`:

- **SIGOR** (dupla convivência): sincronização quase-real-time bidirecional via Platform Events/Change Data Capture — Data Integration assíncrona `[KA-0012]`. Justifica-se pela natureza operacional (chamado de emergência em andamento nos dois sistemas simultaneamente).
- **SIGEO** (correção de lat/long): callout síncrono (request/reply) disparado no ajuste manual de endereço pelo C2C — Process Integration síncrona `[KA-0012]`.
- Autenticação: Named Credentials para ambos os callouts server-to-server.
- Erro/retry: Platform Event de erro + log customizado para falhas de sincronização SIGOR; alertas ao C2C em caso de falha persistente.

### 1.6 Arquitetura de Segurança e Sharing

- **OWD**: Private no Work Order (dados operacionais sensíveis de despacho).
- **Sharing model**: role hierarchy padrão + sharing rules baseadas em Service Territory (CGR = território). Visibilidade restrita à CGR de origem, com override automático quando o recurso é acionado cross-CGR `[extends: Service Territory + criteria-based sharing — padrão para modelos regionais de Field Service]`. O limite exato de fronteira entre CGRs e o limite contratual da UBA permanecem **gaps abertos** (G0307 confirmado só para áreas de intersecção geográfica; G0309 aberto — limite contratual da UBA).
- **Perfis/Permission Sets**: um único app de Field Service Mobile, visões gated por Permission Set (não apps distintos por perfil). Console do Dispatcher com 12 licenças individuais.
- **Acesso externo**: Appointment Assistant nativo do Field Service para o link de rastreamento do cidadão — acesso controlado pelo número de telefone que abriu a ocorrência (SMS exclusivo a esse número); sem token/link customizado a manter (E05).
- **LGPD/Governança de dados**: DER-SP como steward dos dados de geolocalização (G0211).

### 1.7 DevOps

Salesforce CLI + desenvolvimento orientado a source (Git) — volume de customização (LWC no app de campo, Apex de escalonamento N/N-10, 2 integrações) justifica um pipeline versionado desde o início `[assumption: prática padrão de PS para builds multi-integração; validar contra tooling de DevOps já existente na PRODESP — G0415]`. Sandbox mínimo: Developer (squads), Full/Partial para UAT com volume representativo das 14 CGRs.

### 1.8 Governança e Auditoria

Trilha de auditoria de overrides manuais de despacho — piso é Field History Tracking padrão, mas **G0305 permanece aberto** (pergunta bloqueadora ao DER/Stefanini: campos a rastrear, retenção exigida — pode escalar para Field Audit Trail add-on). Change Management: workstream dedicado solicitado pelo DER, incluindo até 2 meses de Scale/Operação Assistida pós-go-live e treinamento personalizado por persona, com foco nos técnicos de campo das UBAs — a refletir no dimensionamento de esforço do programa (G0515).

---

## 2. Solução por Processo de Negócio

### Canal Digital de Atendimento ao Cidadão

**Contexto de negócio**: O cidadão precisa reportar pane ou sinistro na rodovia da forma mais rápida possível — hoje, só pelo 0800. O DER quer um canal digital que reduza o tempo de abertura sem perder o 0800 como porta de entrada de voz.

**Abordagem de solução**: WhatsApp (texto e áudio) e telefonia via integração CTI com a URA, com triagem automatizada pelo Agentforce no canal digital — identifica tipo de emergência e local; se não conseguir, ou por preferência do cidadão, ou em suspeita de vítima, transborda via Omni-Channel para fila humana única 24x7, sempre com contexto completo — incluindo, no canal de telefonia, o screen-pop de CTI com o contexto da chamada. O Agentforce cria a ordem de serviço e devolve o protocolo ao cidadão; a partir daí, o Field Service assume o Work Order.

**Arquitetura de suporte**:
- Triagem via Agentforce Contact Center — reconhecimento de tipo/local como topic/actions do agente `[KB:agentforce_contact_center_4-30-2026.md:26814-26939]`.
- Mensageria outbound no WhatsApp requer add-on (WhatsApp Outbound Messages ou Message Credits) `[KB:agentforce_contact_center_4-30-2026.md:19416-19458]`.
- Integração CTI com a URA do 0800: acionamento de chamada/caso a partir da URA (atual ou futura substituta), com screen-pop no Service Console no momento do transbordo. Padrão técnico exato ainda não fixado — **G0524 aberto** (Open CTI clássica em retirada, fev/2028; conflita com a exclusão deliberada de Salesforce Voice do MVP).
- Transbordo humano via Omni-Channel: **fila única, roteamento baseado em queue** (não skills-based) — adequado porque o modelo é de uma fila sem combinação de habilidades a avaliar `[KA-4393]`. Premissa de setup a revalidar formalmente com o cliente.
- A IA nunca decide a gravidade da vítima — toda suspeita de vítima transborda automaticamente para o humano.
- "WhatsApp voz" é só áudio dentro do canal de mensageria — não usa Salesforce Voice/Native Telephony. Salesforce Voice e a substituição da própria URA/0800 ficam fora do MVP como projeto de infraestrutura de telefonia separado (decisions/0003).

### Registro e Classificação da Ocorrência

**Contexto de negócio**: A ocorrência pode chegar pelo WhatsApp (automatizado), por telefonia via CTI (automatizado, com qualificação pelo Agentforce), ou pelo 0800 (registro manual pelo C2C). Precisa de um registro único, completo e auditável, com espaço para 2ª viatura e reclassificação em campo.

**Abordagem de solução**: Work Order criado a partir de qualquer canal, indistintamente pela tela nativa do Field Service ou pelo Service Console. Classificação pelo catálogo completo de subtipos desde o dia 1, com qualificação do chamado e da ordem de campo pelo Agentforce (canais digitais/CTI) ou pelo atendente (canal manual). Deduplicação por alerta manual ao C2C (raio geográfico + janela de tempo + tipo) — sem fusão automática.

**Arquitetura de suporte**:
- Work Order + 2 Assigned Resource slots para a 2ª viatura, sem Work Order Line Item `[extends: padrão multi-recurso do Field Service]`.
- Work Type como catálogo (100+ subtipos); macro-tipo é picklist informativo, sem Record Type.
- Relator como Contact — login individual por operador para trilha de auditoria de reclassificação (mesma decisão de E04/G0212).
- Objeto nativo Incident (CSIM) fora do MVP — vai para o Roadmap.
- Integrações SIGOR (dupla convivência, Platform Events) e SIGEO (correção de lat/long, callout síncrono) — ver Fundamentos §1.5.

### Despacho Automatizado de Recursos de Campo

**Contexto de negócio**: Uma vez aberta a ocorrência, o DER precisa acionar a viatura certa, na CGR certa, o mais rápido possível — 100% reativo, sem pré-agendamento, operando nas 14 CGRs simultaneamente.

**Abordagem de solução**: Motor de agendamento e otimização do Field Service — considera regras de trabalho, Skills (Work Type → Skill Requirement × Service Resource Skill), território e disponibilidade, não apenas aderência por Skills. Regra N/N-10 (N = 30min, valor de referência a validar) como escalonamento de espera — se o tempo estimado exceder N, amplia o pool para recursos não-aderentes com teto N-10. Recusa exige motivo estruturado; reprocessamento automático imediato, sem intervenção do C2C.

**Arquitetura de suporte**:
- Modelo padrão de Skills do Field Service — Skill Requirement × Service Resource Skill `[KB:field_service_dev.md:23338-23832]`.
- Escalonamento N/N-10 exige Apex/Flow customizado sobre a scheduling policy padrão — a lógica de teto/ampliação de pool excede automação declarativa pura `[extends: field_service_dev.md:25488-25602]`.
- Escalonamento cross-CGR restrito a áreas de intersecção/fronteira geográfica — flag customizado no território `[assumption: extends Service Territory com indicador de zona de fronteira; G0309 aberto — limite contratual da UBA]`.
- Console do Dispatcher: 12 licenças individuais (6/turno × 4 turnos 12x36); despacho e cronômetros continuam sem interrupção na troca de turno.
- Alarme de 5 minutos ao programador responsável, com escalonamento ao supervisor da CGR se não reconhecido.
- **G0305 aberto**: trilha de auditoria de overrides manuais (campos, retenção) — pergunta bloqueadora ao DER antes do build do console.

### Execução em Campo (App Mobile)

**Contexto de negócio**: O operador de campo (das 14 UBAs terceirizadas) precisa receber o despacho, executar o atendimento e encerrar com evidência — muitas vezes em trechos de rodovia sem cobertura de rede.

**Abordagem de solução**: Aplicativo único de Field Service Mobile (visões por Permission Set, não apps distintos) para os 1.152 operadores. Recebimento via push nativo, com retry automático ao reconectar. Encerramento com formulário por macro-tipo e 3 travas de negócio (recusa com motivo, foto obrigatória, check-in geolocalizado em 200m).

**Arquitetura de suporte**:
- Licença Field Service Community (Partner License) — risco monitorado de known issue `[KB:field_service_dev.md:27272-27273]`, aceito pelo cliente apesar da recomendação original de licença padrão.
- Push nativo configurável: on assignment + on dispatch, com retry ao reconectar `[KA-6541]`. Sem fallback SMS no MVP.
- Alarme cíclico de 5 minutos visível na mesa (C2C); confirmação local no app excede capacidade declarativa nativa — fora do MVP.
- Offline: briefcase prima apenas Work Order/Service Appointment/Assigned Resource abertos, sem Task, sem histórico encerrado `[KB:field_service_dev.md:27274-27275]`.
- As 3 travas são regras de negócio ativas (validation rule/Flow + LWC de captura de foto e check-in geolocalizado), mas o **enforcement offline fica fora do MVP** — exige LWC offline "seasoned", vai para o Roadmap `[extends: field_service_dev.md:27512-27655]`. Premissa de redução de escopo a validar formalmente com o cliente.
- 1 formulário base por macro-tipo (pane/sinistro/inspeção) com campos condicionais por subtipo.
- Sharing restrito à CGR de origem, exceto quando o operador é acionado por reforço cross-CGR.

### Rastreamento e Visibilidade em Tempo Real

**Contexto de negócio**: O cidadão quer acompanhar o atendimento; o C2C precisa de um mapa operacional; os gestores precisam de indicadores agregados — um único protocolo acompanhável do pedido ao encerramento, em três públicos diferentes.

**Abordagem de solução**: Cidadão recebe link por SMS (exclusivo ao número que abriu a ocorrência); C2C opera mapa/Gantt com roteamento nativo; gestores veem painel único com 4 indicadores agregados, sem meta de SLA nesta fase.

**Arquitetura de suporte**:
- Mapa/Gantt do C2C: **Aerial Routing nativo do Field Service** (sem ESO/add-on) `[KA-6746]` — entregue como parte do Console do Dispatcher (E03), não deste épico.
- Link do cidadão: **Appointment Assistant nativo do Field Service** — extensão do mesmo template de Experience Cloud já embutido na licença de Field Service, sem build de site guest dedicado `[KA-6140]`/`[KA-6156]` (G0517, gap de token/segurança customizado fechado por mudança de arquitetura — o Appointment Assistant não exige token/link assinado próprio). Mostra apenas a 1ª viatura quando há segunda vinculada — comportamento a confirmar no template nativo.
- Tier P de rastreamento — GPS do app de campo, zero hardware AVL; última posição conhecida com flag/timestamp quando o GPS perde sinal; sem fallback de canal quando o cidadão está sem sinal (risco aceito).
- Painel de gestores: artefato único (mesmo do console C2C), gated por Permission Set — sem relatório à medida por CGR no MVP `[extends: padrão Report/Dashboard folder + sharing]`. 4 indicadores agregados (ocorrências, tempo de resposta, TMA, recusas), sem meta de SLA (decisão deliberada de fase) e sem drill-down por protocolo.
- Canal WhatsApp de entrega do link usa a mesma base de licenciamento de Service Cloud já decidida (decisions/0004).
- UX da experiência do cidadão já validada na PoC. Portal Partner Community para terceiros fica fora do MVP (candidato a nova epic no Roadmap). Governança dos dados de geolocalização (DER-SP steward, G0211) e sharing entre CGRs (G0412) permanecem premissas de entrega documentadas em `gaps.json`, não capacidades nomeadas deste épico.

---

## 3. Riscos Técnicos Principais

| Risco | Mitigação |
|---|---|
| Known issue de Service Appointment com licença Field Service Community | Monitorar releases; escalar para Support se o issue impactar volume real; plano de contingência = migrar para licença padrão se crítico |
| G0305/G0309 abertos podem exigir retrabalho no console do Dispatcher e no modelo de território | Levar como perguntas bloqueadoras formais ao DER antes do build detalhado de E03 |
| Padrão técnico da integração CTI com a URA não fixado (G0524) — Open CTI clássica em retirada (fev/2028), conflita com a exclusão de Salesforce Voice do MVP | Confirmar se o org do DER é anterior ao corte de disponibilidade da Open CTI; validar com o fornecedor de telefonia (Instinct) a API de CTI exposta antes do build de E01/E02/E03 |
| Appointment Assistant (E05) ainda não validado em detalhe contra os requisitos específicos do DER (comportamento com 2ª viatura, canal de entrega SMS) | Revalidar `[KA-6140]`/`[KA-6156]` e o comportamento de exibição de 1ª viatura no template nativo antes do build detalhado |
| Offline enforcement das travas fora do MVP — risco de evidência incompleta em campo sem rede | Documentar como premissa de redução de escopo para validação formal com o cliente (G0413); reavaliar prioridade no Roadmap |
| Sincronização SIGOR em dupla convivência — risco de divergência entre sistemas | Log de erro + alerta ao C2C em falha persistente; monitorar volume de divergências nas primeiras semanas de produção |

---

## Próximos Passos

- `roadmap` — fasear os épicos e derivar uma faixa de prazo top-down.
- `estimate` — dimensionar o roster nomeado (papéis, senioridade, localização).
- Levar G0305 e G0309 como perguntas bloqueadoras formais ao DER/Stefanini.
- Refletir o workstream de Change Management (G0515) no dimensionamento de esforço do programa.
