# Discovery Brief — PRODESP · DER-SP (Socorro Emergencial em Rodovias)

**Data:** 2026-09-17 · **Conta:** PRODESP-Companhia de Processamento de Dados do Estado de São Paulo · **Cliente final:** DER-SP (Departamento de Estradas de Rodagem do Estado de São Paulo)
**Oportunidade Org62:** PRODESP DER FS Implementation CSG New · Stage 02-Scoping · Amount $8,000,000 · Close Date 2026-10-30 · Owner Juliana Brites · Type SOW

---

## 1. Resumo executivo

O DER-SP quer substituir o fluxo manual e fragmentado de atendimento a pane e sinistro nas rodovias estaduais (hoje via 0800 055 5510, despacho manual pelo C2C, sem protocolo nem rastreamento em tempo real) por um ciclo único e rastreável em Salesforce Field Service, com WhatsApp/WhatsApp voz e Agentforce como canal digital de entrada. O MVP está bem definido no nível de processo (7 etapas, 6 papéis, regras de despacho automático e alarme); o que falta fechar é ambiente/licenciamento Salesforce, o parâmetro de escalonamento N, e a arquitetura de longo prazo para voz/CTI — esta última, por decisão do usuário nesta sessão, vai para uma fase de Roadmap dedicada e detalhada, não para o MVP.

**Critério de sucesso, confirmado verbatim pelo cliente:** *"Controlar o atendimento emergencial desde a abertura até a conclusão, com visão única e rastreável, em tempo real."*

## 2. Extraction Audit (16 áreas)

| # | Área | Status | Evidência / Base |
|---|------|--------|-------------------|
| 1 | Identidade da empresa | Confirmed | DER-SP (agência estadual de rodovias), contratado via PRODESP (braço de TI do Estado de SP) |
| 2 | Estado atual Salesforce | Confirmed | Greenfield (Opportunity: "Fiel implementation - greenfield"); legado é o SIGOR (substituiu o SIGA ~1 ano) |
| 3 | Solução-alvo | Confirmed com conflito não resolvido | MVP = Field Service + Agentforce (WhatsApp/WhatsApp voz), org única. Service Cloud/Voice/Open CTI confirmados fora do MVP pelo usuário — mas o deck do BSA (v2) propõe objetos de mensageria sob Service Cloud para o mesmo canal WhatsApp. Não resolvido — ver Discrepancy Scan. |
| 4 | Usuários e personas | Confirmed | 298 viaturas, 1.152 operadores de campo (UBA terceirizada, uma empresa por CGR), 14 CGRs, 12 dispatchers C2C (DER, 6/turno), 4 turnos 12x36. 6 papéis no MVP: Cidadão, Agentforce, Atendente humano, C2C, Equipe de campo, Gestores. |
| 5 | Timeline e go-live | Confirmed (gravado em `.project-metadata.json`) | Homologação jan/fev 2027; produção abril 2027; contrato URA (Instinct) até abril/2027; contrato administrativo renova 30/nov/2026 |
| 6 | Objetivos de negócio | Confirmed | Visão única e rastreável do atendimento, do início ao fim, em tempo real (citação direta do cliente) |
| 7 | Processos de negócio core | Confirmed | Ciclo de 7 etapas (Solicita→Registra→Classifica→Despacha→Desloca→Atende→Encerra); despacho por aderência/disponibilidade/proximidade + regra N/N-10; alarme de 5 min no deslocamento; recusa só antes do deslocamento |
| 8 | Integrações | Confirmed (exclusões) | SIGOR e URA/CTI explicitamente fora do MVP. Integrações futuras (PM, Bombeiros, Defesa Civil, montadoras) citadas como "a verificar". SIPATI citado uma vez, sem substância — stub. |
| 9 | Migração de dados | Confirmed | Sem dupla convivência — chamados de emergência só nascem no Salesforce; SIGOR continua para outros fins |
| 10 | Compliance/regulatório | Unknown (gap real) | Nenhuma discussão de LGPD/DPIA registrada; RACI, retenção para auditoria, acessibilidade — gaps na aba Setor Público |
| 11 | Orçamento e funding | Confirmed no nível de deal | Amount $8M, Stage 02-Scoping, Close Date 30/10/2026. Instrumento contratual no nível DER (termo de referência vs. ata) — Unknown |
| 12 | Stakeholders | Confirmed | Nominal: Rafael Marques, Thiago Mantoanelli, Cristina Cândido, Renata Vendramini (BSA), Juliana Brites, Pedro Ganem Filho, Iran da Costa, Alex Gonzalez Veiga, Nelson Stebulaitis Filho + Stefanini (parceiro de telefonia). Sponsor executivo nominal: não identificado — gap. |
| 13 | Riscos e restrições | Confirmed | 10 riscos mapeados (aba Riscos): conectividade, salto POC→produção, LGPD/DPIA, dependência de terceiros, licenciamento indefinido, auditabilidade de override, canal de contingência, resistência a geolocalização, QA do agente sem dono, priorização em saturação |
| 14 | Sinais de handoff | Confirmed | Opportunity em Stage 02-Scoping pós-POC; a própria POC se declara exploratória, não arquitetura definitiva |
| 15 | Sinais de design de experiência | Assumed, raso | Jornada por persona esboçada; sem UX research formal nem acessibilidade (Setor Público Q7 — gap) |
| 16 | Sinais de governança | Unknown (maioria) | RACI, change control, QA do agente conversacional sem owner, consulta sindical sobre geolocalização — todos gaps |

## 3. Discrepancy & Stub Scan

- **Service Cloud para o canal WhatsApp** — o BSA v2 propõe objetos MessagingEndUser/MessagingSession/Case sob Service Cloud para viabilizar o canal WhatsApp/Agentforce; o usuário confirmou que Service Cloud está fora do MVP por falta de caso de uso de atendimento geral. **Não resolvido**: precisa esclarecer se a camada de Digital Engagement (mensageria) que sustenta o WhatsApp exige licenciamento de Service Cloud independentemente do caso de uso de atendimento geral com CTI.
- **Parâmetro N** (regra de despacho N/N-10) — mecanismo nomeado e obrigatório no MVP, valor nunca especificado em nenhum documento. Pergunta aberta confirmada pelo usuário.
- **SIPATI** — citado uma única vez como sistema que "precisa falar com o socorro", sem direção de integração, gatilho ou dado. Desconhecido tanto para o usuário quanto para o assistente — stub genuíno, levar à próxima reunião com o DER.
- **Login do app de campo (viatura ou pessoa)** — mecanismo de autenticação nomeado no BSA v2 como "ainda não fechado" — stub a resolver antes do design do aplicativo móvel.
- **Ambiente Salesforce e licenciamento (SKU/edição)** — bloqueador nomeado repetidamente nos documentos ("produto e licença ainda não estão fechados"); usuário decidiu conscientemente não bloquear a primeira versão de estimativa nisso, mas o gap segue real e deve ser resolvido antes do go-live.
- **Papel contratual da PRODESP vs. DER-SP** — nomeado como não descrito nos documentos (PREM-08 do BSA v2); a Opportunity Org62 mostra a PRODESP como Account contratante, mas o instrumento (repasse, gestão, etc.) não está documentado.
- Nenhum overlay de produto genuíno detectado no scan de palavras-chave — único hit ("Agentforce Operations" via "capa") é falso positivo (cabeçalho em PT "Capa e contexto" colidindo com a sigla CAPA de manufatura); descartado.

## 4. Decisão registrada nesta sessão (ADR)

**`decisions/0001-cti-voice-roadmap-deferral.md`** — Integração de voz/CTI e Agente de IA de voz ficam fora do MVP; tratadas como fase dedicada e detalhada do Roadmap, dado que a decisão Open CTI (retirado fev/2028) vs. Salesforce Voice depende de validação técnica pendente com a Stefanini sobre o vendor de URA "Instinct" (contrato até abril/2027).

## 5. Open Questions (para a próxima reunião com DER/Stefanini)

1. **URA/telefonia**: o vendor "Instinct" é PABX próprio do DER, solução em nuvem, ou serviço terceirizado da Stefanini? Expõe uma API CTI viável?
2. **Decisão formal Open CTI vs. Salesforce Voice** — a ser detalhada na fase de Roadmap (ver ADR 0001).
3. **Parâmetro N** da regra de despacho N/N-10 — qual o valor (em minutos) que o DER quer usar?
4. **SIPATI** — o que é esse sistema e por que precisaria integrar com o socorro emergencial?
5. **Ambiente Salesforce e licenciamento** — qual edição/SKU, quando será definido, e por quem (PRODESP + Salesforce, com o DER operacional, per o BSA)?
6. **Service Cloud vs. WhatsApp** — o canal WhatsApp/Agentforce do MVP exige licenciamento de Service Cloud subjacente, mesmo sem caso de uso de atendimento geral?
7. **Login do app de campo** — a autenticação é por viatura ou por pessoa?
8. **LGPD/DPIA** — quem no DER é o responsável por dados pessoais/geolocalização? Nenhuma discussão formal ocorreu até agora.
9. **Papel contratual PRODESP vs. DER-SP** — como se dá a relação contratual/de repasse entre as duas entidades para este projeto?

## 6. O que está fora do MVP (por decisão confirmada, não por omissão)

- URA/voz (fase de Roadmap dedicada — ADR 0001)
- Integração com SIGOR (sem convivência dupla; chamados de emergência só nascem no Salesforce)
- Guincho pesado, desobstrução, apoio com pick-up, apreensão de animais (demais serviços da UBA)
- Itens da Carta de Serviços (multa, AET, escolta, cartão-caminhão, ouvidoria, SIC, pátio, faixa de domínio, anúncios, ressarcimento)
- Pesquisa de satisfação ao cidadão (fase futura confirmada)
- Native GIS/ArcGIS (não fechado)
- Work Order Line Item (segunda viatura abre chamado vinculado, não usa este objeto)

## 7. Base de conhecimento

8 documentos indexados em `knowledge/`: `field_service_dev.md`, `service_cloud_3-27-2026.md`, `agentforce_contact_center_4-30-2026.md`, `voice_dev_guide.md` (biblioteca curada), `salesforce-architect-fundamentals.md` (WebFetch), `quantum-leap-methodology.md`, `latam-agentic-governance-services.md` (PS Methodology embutida), `POC versão 01 - 20.08.26.docx.md` (auto-convertido). ✓

## 8. Pesquisa web (achados externos, `discovery-notes/web-research-der-sp.md`)

Pesquisa limitada por ausência de WebSearch/browser automation neste ambiente (contornada via SERP estático); tratar tudo abaixo como apoio, não como fato client-facing sem confirmar a fonte primária.

- **14 divisões regionais do DER-SP (DR-01 a DR-14) confirmadas via fonte pública independente** — valida o número de "14 CGRs" usado no projeto (confiança média).
- **Precedente forte de proof point**: a PRODESP é parceira confirmada de implementação do "Infosiga 3.0" (painel de sinistros de trânsito do Detran-SP, relançado set/2025, com a Bloomberg Initiative for Road Safety) — SP registrou 135.545 sinistros de trânsito em 2024 (dado estadual agregado). Referência direta e citável para o business case de segurança viária.
- **Portal CCM da ARTESP** (rodovias concedidas) tem taxonomia pública de ocorrências (inclui "pane elétrica/mecânica/seca") — útil como referência de categorização para o catálogo operacional.
- **Não confirmado publicamente** (não fabricar, tratar como gap): quilometragem/orçamento específico do DER-SP; o termo "SIGOR" colide integralmente com um sistema não relacionado da CETESB — não há confirmação pública de um SIGOR de ocorrências rodoviárias do DER-SP, é termo interno a validar; o vendor de URA "Instinct" e o contrato Stefanini–PRODESP não têm evidência pública específica; TMA de socorro mecânico em concessões (CCR/ARTESP); nome do atual Presidente do DER-SP (baixa confiança, não usar sem confirmar).
- **Nota**: a extinção da Dersa (empresa estadual de desenvolvimento rodoviário) por lei em 2019 é confirmada — não usá-la como comparável ativo caso apareça em algum benchmark.
