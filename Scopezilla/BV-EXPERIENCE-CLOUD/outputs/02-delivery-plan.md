# BV — Plano de Entrega (Experience Cloud + MuleSoft)

**Cliente:** BV Financeira (Banco BV) · Financial Services · Brasil
**Natureza:** engajamento *brownfield* — remediação de débito técnico e ativação de recursos prioritários sobre três portais Experience Cloud em produção e uma camada de integração MuleSoft/Apigee viva.

**Duração total do programa: conforme compromisso do cliente (a definir).** As fases abaixo mostram apenas sequência e dependências — nenhum número de semana foi comprometido (decisão do usuário: sem compromisso de prazo). Para uma faixa de prazo derivada da forma do engajamento, rode `roadmap` no modo *benchmark*; para dimensionar o time e uma faixa indicativa de preço, rode `estimate`.

**Caminho crítico:** E04 + E06 → **E01** — as duas fundações (base transversal e camada MuleSoft) alimentam o Portal Governança, o núcleo de valor; escorregar em qualquer uma cascateia no cronograma. Em paralelo corre a trilha de parceiros: E04 + E06 → E02 → E03.

---

## Fase 0 — Resolução de Pré-requisitos *(posição 1 de 5)*

Sem épicas de build. Fecha os bloqueadores antes do build: licença Experience Cloud externa (R1) e interna (G0307); provedores de identidade externo e interno (G0202/G0301); topologia single-org (G0403); limitação do Anypoint contratado (R2/G0602); fronteira de catálogos entre carga one-off e ETL recorrente (G0509); toolchain de DevOps/versionamento (G0404); fonte, volume e qualidade dos dados legados (G0503/G0504).

**Concluída quando:** licenças contratadas ou com pedido em curso; IdP externo e interno nomeados e federáveis; topologia de org e sandboxes confirmada; limitação do Anypoint documentada; fronteira E05/E06 delimitada; toolchain escolhido; fonte legada conhecida.
**Risco:** bloqueadores de licença e de IdP são externos ao time de build e podem represar o início das fases seguintes.

## Fase 1 — Fundações & Integração *(posição 2 de 5)* · E04, E06

Base técnica transversal aos três portais (E04) e camada de integração MuleSoft API-led (E06). E06 publica os contratos de XAPI/SAPI que os portais consomem — é a interface que sequencia toda a trilha.

**Concluída quando:** org e ambientes operacionais; perfis/permission sets core, connected apps e usuário de integração provisionados; frameworks de trigger/logging/mocking em pé; contratos de XAPI/SAPI acordados e SAPIs/XAPIs prontas para consumo; TLS context de borda com Apigee estabelecido.
**Depende de:** insumos da Fase 0. **Risco:** é o caminho crítico; a limitação do Anypoint (R2) pode onerar geração de OAS/render de contrato; overhead de arquitetura de integração (G0610) pode estar fora da base e subdimensionar a entrega.

## Fase 2 — Governança & Dados *(posição 3 de 5)* · E01, E05

Portal Governança (E01) — cadastro de API, Wizard de geração de API Técnica, validação de contrato via OPA renderizada em HTML, aprovação por Flow + Approval Process — e carga dos catálogos (E05) que alimentam o modelo de dados do portal. Dentro da fase: modelo de dados primeiro (E01), migração em seguida (E05), depois os recursos do E01 consomem os dados carregados.

**Concluída quando:** ciclo de vida de API operável ponta a ponta; catálogos das dez entidades carregados com integridade referencial e reconciliação; integrações de saída do E01 consumindo as XAPIs do E06.
**Depende de:** E04, E06 (Fase 1). **Risco:** fronteira de catálogos E05/E06 (G0509) e cutover/rollback em produção viva (G0506) precisam estar resolvidos antes da carga.

## Fase 3 — Portal de Parceiros Externo *(posição 4 de 5)* · E02

Portal externo (E02): autorregistro, login diferenciado via Login Discovery, catálogo público/privado, criação de apps e gestão de credenciais, contratos por versão de produto e páginas de conteúdo/enablement.

**Concluída quando:** parceiros externos se registram, descobrem APIs, criam apps e gerem credenciais em autoatendimento; sharing público/privado ativo; SAPIs do E06 consumidas; licença EC externa (R1) ativa.
**Depende de:** E04, E06 (Fase 1). **Risco:** relação com o portal Apigee incumbente (G0204) e consentimento LGPD/OneTrust (G0203) abertos; sem licença EC externa contratada, não há go-live externo.

## Fase 4 — Portal de Parceiros Interno *(posição 5 de 5)* · E03

Portal interno para funcionários do BV — build distinto, com público, personas, licença, visibilidade e segurança próprios, reaproveitando a base do E02 onde couber.

**Concluída quando:** portal interno operacional com personas e sharing próprios; tipo e contagem de licença interna definidos e provisionados.
**Depende de:** E02 (Fase 3) — sequenciada após o *freeze* da configuração do E02. **Risco:** licença interna indefinida (G0307/G0303); sem o freeze do E02, mudanças no externo forçam retrabalho.

---

## Processos transversais (todas as fases)

- **Teste de não-regressão dos três portais em produção viva** — contínuo a cada release; alterar fundações transversais pode quebrar comportamento existente (E04).
- **Deploy versionado** — esteira de deploy com janelas de release e caminho de rollback (toolchain definido na Fase 0).
- **QA/testes e hardening de serviços financeiros** — QA funcional dos portais + teste do fluxo de aprovação OPA; segurança/carga antes do go-live externo.
- **Release e UAT** — conduzidos pelo BV. **Gestão de mudança e treinamento** — do BV; a PS entrega o enablement embutido nas páginas de conteúdo do E02 (G0408).

## Riscos consolidados

| # | Risco | Fase(s) | Mitigação |
|---|---|---|---|
| R1 | Licença Experience Cloud externa não contratada | 0 → 3 | Contratar antes do go-live externo; rastrear na Fase 0. |
| R2 | Limitação do Anypoint contratado pode onerar OAS/contrato | 0 → 1 | Caracterizar na Fase 0; pode redimensionar E06. |
| G0509 | Dupla contagem/lacuna de catálogos entre E05 e E06 | 0 → 2 | Delimitar fronteira one-off vs. ETL na Fase 0. |
| G0307/G0303 | Tipo e contagem de licença interna indefinidos | 0 → 4 | Definir na Fase 0; bloqueia sizing de licença do E03. |
| G0202/G0301 | IdP externo e interno não nomeados | 0 → 1,3 | Nomear e confirmar federação na Fase 0. |
| G0610 | Arquitetura de integração pode estar fora da base do E06 | 1 | Confirmar escopo do Technical Architect na Fase 1. |
| — | Freeze do E02 antes de derivar o E03 | 3 → 4 | Congelar config do E02 antes de iniciar a Fase 4. |

---

*O time e o roster nomeado para entregar este plano — com contagens defensáveis, por trilha — vêm do `estimate`. Este documento é sequência e dependências, não equipe nem preço.*

*Fontes: `data/epics.json`, `data/estimates.json`, `data/gaps.json`, `data/roadmap.json`, decisões do grill 2026-08-04 (`data/memory.json`).*
