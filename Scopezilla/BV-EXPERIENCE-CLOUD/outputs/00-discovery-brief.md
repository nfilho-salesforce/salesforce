# Discovery Brief — BV · Experience Cloud & MuleSoft

**Cliente:** Banco BV (BV Financeira) · **Projeto:** Resolução de débito técnico e ativação de recursos prioritários nos portais Experience Cloud + camada MuleSoft
**Fase:** ROM (Rough Order of Magnitude) → próximo: Discussion Document → SOW → Staff & Engage
**Base:** Tech Assessment Salesforce Professional Services (jun/2025, FY26) + planilha de alcance + pesquisa de mercado
**Data do brief:** 2026-08-04

> Sigla e termos: **EC** = Experience Cloud; **XAPI/SAPI** = Experience/System API (padrão API-led do MuleSoft); **OPA** = Open Policy Agent (validação de políticas); **BaaS** = Banking-as-a-Service; **APD** = Account Partner Director; **EM** = Engagement Manager. Os valores de esforço citados são os **do assessment do cliente** — não são estimativa nova da Salesforce PS.

---

## 1. Resumo executivo

O Banco BV opera três portais sobre Salesforce Experience Cloud — **Portal Governança** (ciclo de vida de APIs), **Portal Parceiros** (portal externo de desenvolvedores/parceiros) e **Portal Parceiros Interno** — integrados a uma camada MuleSoft e ao gateway Apigee. A Salesforce Professional Services conduziu um Tech Assessment que mapeou as ações prioritárias, técnicas e funcionais, para **corrigir débito técnico e ativar recursos prioritários**, visando estabilidade, performance e evolução contínua. O engajamento é **brownfield** (portais já em produção — [ADR 0001](../decisions/0001-brownfield-remediacao-debito-tecnico.md)). O assessment dimensionou o esforço em **~2.222 horas (≈13 semanas)** para a trilha Experience Cloud e **319 horas** no detalhamento MuleSoft. Um gap de licenciamento (Experience Cloud fora do contrato Experience Hub) está em aberto e é bloqueador de go-live ([ADR 0002](../decisions/0002-gap-licenca-experience-cloud.md)).

## 2. Contexto do cliente e mercado

- **Banco BV** — banco múltiplo brasileiro, controle 50% Votorantim S.A. + 50% Banco do Brasil. Líder histórico em financiamento de veículos; também crédito, atacado e banco digital. Lucro líquido 2024 recorde de R$ 1,7 bi; carteira ampliada ~R$ 102 bi (1T25).
- **BV Open (BaaS)** — plataforma de Banking-as-a-Service via API, aberta a fintechs, marketplaces e parceiros. Ecossistema maduro (70+ APIs, 100+ parceiros em referências públicas).
- **Stack de APIs incumbente:** portais de desenvolvedores já existentes rodando em **Apigee (Google Cloud)** (developers.bvopen.com.br e sandbox). Isso confirma o cenário brownfield: o valor do projeto está na **camada de experiência/onboarding (Experience Cloud)** e na **orquestração (MuleSoft)**, não em expor APIs do zero.
- **Regulatório:** Open Finance Brasil (BCB, faseado desde 2021, APIs padronizadas) e LGPD moldam requisitos de segurança e consentimento. OneTrust já aparece no fluxo de governança.

*(Detalhe completo e fontes em `discovery-notes/research-banco-bv-contexto-mercado.md`.)*

## 3. Landscape Salesforce: atual vs. alvo

**Atual (brownfield):** Três portais Experience Cloud em produção + camada MuleSoft (XAPIs segregadas) + Apigee no edge. Débito técnico acumulado e recursos prioritários ainda não ativados.

**Alvo:** Portais estabilizados e evoluídos, com débito técnico remediado e recursos prioritários ativos, cobrindo:

| Bloco | O que é | Destaques de escopo |
|-------|---------|---------------------|
| **Portal Governança** | Ciclo de vida de APIs: API de Negócio → API Técnica → validação OPA → aprovação → publicação de versões | Renderização do resultado OPA em HTML; wizard (desejável); validações de versão; processo de aprovação (Flow); fechamento após 3 rejeições |
| **Portal Parceiros** | Portal externo de desenvolvedores/parceiros: catálogo de APIs (público/privado), autorregistro, gestão de apps e credenciais, contratos por versão de produto | Login diferenciado (senha p/ básico, IdP p/ parceiro); páginas LWC aprimoradas (desejável); "Seja um Parceiro" |
| **Portal Parceiros Interno** | Versão interna do Portal Parceiros (config derivada) | Reaproveita configuração do Portal Parceiros; SSO com IdP |
| **Transversal** | Fundações: perfis/permissões core, DevOps, logging, trigger framework, mocking, **migração de catálogos e APIs** | Migração: Torre, Sigla, Tribu, Squad, Domínio, Subdomínio, API Negócio/Técnica, Produto, Versão |
| **MuleSoft** | Camada de integração API-led (319h): TLS/Apigee, XAPIs segregadas, SAPIs, batch ETL | XAPIs: OneTrust, ServiceNow, OPA, PortalTech, Jira; SAPIs Jira/Apigee/Anypoint; testes E2E; acompanhamento de gestão |

**Integrações mapeadas:** Apigee (gateway), Jira (CASP — criação de API de Negócio/issues), OneTrust (privacidade/consentimento), ServiceNow (tickets), PortalTech (aprovação de componentes/bypass), Anypoint (contratos/YAML→HTML), OPA (validação de contrato), catálogos Torre/Sigla/Tribu/Squad.

## 4. Escopo e objetivos

- **Objetivo:** corrigir débito técnico e ativar recursos prioritários nos portais EC + MuleSoft, garantindo estabilidade, performance e evolução contínua.
- **Escopo confirmado:** backlog completo do assessment — todos os itens MVP dos 3 portais + Transversal + MuleSoft. Itens marcados "desejável/No" (ex.: Wizard de geração de API ~160h, páginas LWC aprimoradas) ficam como candidatos de fase 2.
- **Estado:** brownfield (preservar produção; testes de não-regressão, gestão de release e migração de dados vivos entram no esforço — [ADR 0001](../decisions/0001-brownfield-remediacao-debito-tecnico.md)).
- **Esforço do assessment (referência do cliente, não estimativa nova):** ~2.222h (≈13 semanas) EC + 319h no detalhamento MuleSoft. Perfis previstos: EM, PM, Senior PM, Senior Technical Architect, Solution Architect, MuleSoft Technical Architect, MuleSoft Technical Consultant, Technical Consultant, Developer, QA Associate.

## 5. Dados e considerações de compliance

- **Migração de dados:** catálogos e APIs existentes (10 entidades). Esforço ~80h; **status MVP divergente entre abas** (Si em "Detail3", No em "Salesforce Portales") — a resolver.
- **Privacidade/consentimento:** OneTrust integrado ao fluxo de governança; conformidade LGPD.
- **Regulatório setorial:** Open Finance Brasil (APIs padronizadas BCB) — validar impacto nos requisitos não-funcionais.
- **Segurança:** SSO/IdP, TLS/mTLS via Apigee, credenciais nomeadas, permission sets por persona.

## 6. Riscos e constraints

| # | Risco / Constraint | Impacto | Origem |
|---|--------------------|---------|--------|
| R1 | **Licença Experience Cloud não contemplada no Experience Hub** (em aberto) | **Bloqueador de go-live** — portais não publicáveis sem licenças | Highlights do assessment + [ADR 0002](../decisions/0002-gap-licenca-experience-cloud.md) |
| R2 | **Limitação do Anypoint da MuleSoft** | Pode restringir padrões de integração / render de contratos | Highlights do assessment |
| R3 | Topologia MuleSoft ↔ Apigee incumbente | Precisa estar clara (coexistência confirmada no assessment; validar governança/ownership) | Pesquisa + assessment |
| R4 | Brownfield: preservar produção | Regressão, gestão de release, coexistência de dados | ADR 0001 |
| R5 | Divergências internas de esforço/MVP no material | Base de estimativa inconsistente até reconciliar | Planilha (2 abas) |
| R6 | Dimensionamento de licenças depende de contagem de usuários (desconhecida) | Bloqueia R1 e o roadmap de go-live | Extração |

## 7. Stakeholders

- **Salesforce:** Amanda Basílio (Engagement Manager), Ricardo de Oliveira (Account Partner Director), Antonio Torres e David Pendeza (Technical Architects — conduziram o assessment).
- **BV:** contrapartes de negócio/TI **ainda não nominadas** no material — a mapear.

---

## Open Questions

Perguntas de discovery a levar ao cliente (ou resolver internamente):

1. **Licenciamento EC (R1):** qual o plano e prazo para contratar as licenças Experience Cloud? Member-based ou login-based? Quem é o owner (account team / BV)?
2. **Contagem de usuários por persona:** quantos usuários externos (parceiros/desenvolvedores), gestores de governança e usuários internos? — dimensiona licenças e performance.
3. **Estado exato de cada portal:** o que já está 100% em produção vs. parcialmente construído? Quais débitos técnicos são os mais críticos hoje (bugs, performance, segurança)?
4. **MuleSoft vs. Apigee:** confirmar a topologia alvo — MuleSoft como camada XAPI/SAPI coexistindo com Apigee no edge? Há intenção de migrar algo do Apigee/BV Open para MuleSoft?
5. **Ownership do MuleSoft:** a entrega MuleSoft (319h) é Salesforce PS, BV, ou misto? (Material marca alguns itens "Salesforce o Banco BV".)
6. **Divergências do material (R5):** reconciliar o status MVP da migração (80h) e o esforço do render OPA (60h vs 40h); reconciliar o total MuleSoft (319h no detalhamento vs. ~660h de perfis MuleSoft na tabela do PDF).
7. **Timeline:** há data de go-live ou marco regulatório (Open Finance) forçando prazo? Quando o BV pretende iniciar?
8. **Open Finance:** os portais têm relação com obrigações de Open Finance Brasil, ou são de APIs proprietárias do BV Open? — muda requisitos regulatórios.
9. **Design de experiência:** há necessidade de UX research / design system para as páginas de parceiros, ou reaproveitar o padrão atual?
10. **Change & adoção:** há plano para onboarding de parceiros e capacitação de gestores internos no novo fluxo?
