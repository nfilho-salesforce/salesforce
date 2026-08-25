# ARI Vivo — Defesa da Nominação (PS Review for Approval)

> **O que é:** roteiro de perguntas-e-respostas do *PS Review* que aprova o ARI (Attrition Risk
> Investment) da Vivo BR. O ARI é um **investimento da Salesforce em Professional Services**
> concedido a um cliente **em risco de attrition (não-renovação)**, para blindar a renovação das
> licenças. Este documento **não dirige o escopo técnico** (isso é o ROM em `discovery-notes/`) —
> ele é o **business case** que justifica o investimento e fixa os critérios de sucesso.
> **Fonte:** `reference/ari-nomination-ps-review.png` (slide "Sample Questions to expect at PS Review for Approval — Latam ARI Nominations · Vivo BR").

## Números-âncora (o que decide a defesa)

| Fato | Valor |
|------|-------|
| **AOV em risco (Attrition Amount)** | **USD $10.281.553** — receita de licenças que o ARI protege |
| **Tipo de renovação** | Renovação **integral** (full renewal) |
| **Prazo de compromisso** | **3 anos** (upgrade de renovação de 1 ano → compromisso de 3) |
| **Vencimento dos contratos** | **Jan/2028** (todos, incluindo o contrato MCE adicional) |
| **Renovação antecipada** | Cliente **comprometido** a renovar antecipado |
| **Gatilho de início** | Cliente inicia o trabalho **após assinatura da renovação** (work-for-renewal) |
| **Co-investimento (50/50)** | **Não** |
| **Services Deal associado (accountability conjunta)** | **N/A** |
| **Attrition confirmada além desta** | Não · **primeira vez** que o cliente entra como risco de attrition |

## Account Plan

- **Clouds/produtos atuais:** Sales, Service, Comms B2B, Comms B2C, CRM Analytics (CRMA),
  Platform, MuleSoft, Marketing, Financial Services.
- **O que está em risco (attrited) e por quê:** Sales, Service, Comms B2B/B2C, CRMA, Platform e
  MuleSoft — o **backbone operacional** e pré-requisito da estratégia de atendimento AI-driven do
  cliente. **Alternativa viável do cliente se sair da Salesforce:** migrar para uma **aplicação
  homegrown com IA própria** (é essa a ameaça que o ARI neutraliza).
- **Decisor-chave:** **Alex Salgado** — postura **Neutra** (não é campeão nem detrator ⇒ risco de
  relacionamento a trabalhar).
- **Capacidade interna para tocar projeto com PS:** Sim.
- **Iniciativas concorrentes:** **Sim — plataforma homegrown + ServiceNow (SNOW).**
- **Impacto no engajamento de PS:** Não.

## Attrition

- **AOV em risco:** USD $10.281.553.
- **Outra attrition confirmada:** Não.
- **Já foi risco de attrition antes:** Não (primeira vez).
- **Este valor resolve o sucesso de longo prazo ou vamos precisar revisitar adoção depois?**
  **Resolve** — o investimento endereça os riscos imediatos e corrige a **percepção de valor**
  atual, eliminando necessidade de visitas de adoção subsequentes. **Além disso, pavimenta o
  caminho para o cliente virar uma *agentic enterprise*.**

## Renewal

- **Renovação parcial?** Não — é **full renewal**. Há outro contrato (**MCE**); **todos vencem em
  Jan/2028**.
- **Prazo:** **3 anos** (oportunidade de elevar de 1 ano para compromisso de 3 capturada).
- **Renovação antecipada:** Sim, comprometido.
- **Compromete a renovação em troca do início do trabalho** (começamos após assinatura): **Sim.**
- **Outras renovações previstas com o cliente no horizonte:** Não.
- **Oportunidades de PS existentes impactadas pelo investimento:** Não.
- **Está na release mais atual / há chance de modernizar com este investimento:** **Sim** — janela
  para trazer o cliente ao release corrente.

## ProServ & Commitment

- **Oferta de PS recomendada para garantir a renovação:** engajamento **"Hands-on-Keyboard"** que
  entrega uma **camada de atendimento Agentforce conversacional e nativa** para o segmento **B2C**
  da Vivo. Contra-ataca diretamente o risco de attrition (estratégia do cliente de construir
  alternativas de CRM internas) entregando um ambiente **production-ready** que substitui
  nativamente os front-ends legados fragmentados e as arquiteturas de iframe complexas.
  Estabelece capacidades de **cliente eTOM**, otimiza fluxos altamente regulados (ex.: contestação
  de fatura de **300+ passos**) via **motor determinístico**, e incorpora **federação Data 360**
  para proteger a arquitetura de *customer master* — provando **ROI direto ao COO**.
- **Critérios de sucesso mensuráveis** (amarram entrega ⇄ redução de risco de attrition):
  1. **Front-end agêntico único e unificado** — elimina o *multi-window switching* (Alt+Tab entre
     WDE/GPS/Next/Siebel).
  2. **Redução de 15% no TMA** (Tempo Médio de Atendimento / AHT).
  3. **Melhoria de FCR** (First Contact Resolution) para casos de suporte.
- **Services Deal associado ao investimento (accountability conjunta):** **N/A.**
- **Co-investimento com o cliente (50/50):** **Não.**
- **Cliente compromete a renovação em troca do início do trabalho:** **Sim.**

## Como isto conecta ao ROM e à estimativa

- **Justifica o teto de investimento:** o esforço de PS que estamos dimensionando (ROM build +
  fases PS completas) precisa caber na lógica de proteger **USD 10,28M** de receita de licenças por
  **3 anos** — a defesa de valor é *renewal insurance*, não margem de serviços.
- **A oferta é "Hands-on-Keyboard" B2C Agentforce** — coerente com o ROM (199 histórias, 10
  domínios, camada de atendimento nativa). O ROM é o *como*; este slide é o *porquê aprovar*.
- **Critérios de sucesso viram KPIs de entrega:** front-end único, **−15% TMA**, **+FCR**. Devem
  aparecer como *measurable outcomes* na estratégia/roadmap e como âncora dos KPIs propostos.
- **Ameaça competitiva (homegrown IA + ServiceNow)** é o *counterfactual* — reforça a narrativa de
  "substituir o legado fragmentado nativamente antes que o cliente construa a alternativa".
- **Relacionamento:** decisor **Neutro (Alex Salgado)** ⇒ a defesa precisa de prova de ROID ao COO;
  cuidar de *executive alignment* no roadmap.
