# Discovery Brief — DATAPREV / PAT (Marketplace do Programa de Alimentação do Trabalhador)

*Fase: Discovery / avaliação de aderência (pré-proposta). Data: 2026-07-27.*
*Insumos: reunião de 21/jul/2026 (Notes by Gemini), 3 BPMN, slides "Marketplace–Financeiro", protótipo Figma "PAT–Cotação". Pesquisa complementar: reforma do PAT (nov/2025), Novo PAT, GOV.BR.*

---

## 1. Executive summary
A Dataprev vai construir, para o Ministério do Trabalho e Emprego (MTE), uma **plataforma-marketplace do PAT** que dá transparência e concorrência à contratação de vale-alimentação/refeição — conectando empresas beneficiárias, facilitadoras (emissoras de cartão) e estabelecimentos credenciados, sob as novas regras da reforma de nov/2025 (taxa máxima 3,6%, repasse em até 15 dias). Salesforce PS propõe um ROM cobrindo os **quatro módulos** (Cotação/Contratação, Folha/Financeiro, Credenciamento e Agentforce) sobre **MuleSoft + Experience Cloud + Core/Service Cloud + Agentforce**, com homologação-alvo em set/2026 e produção em 15/nov/2026.

## 2. Contexto do cliente e da indústria
- **Executor:** Dataprev (DPS / SUTF / DEBT — Divisão de Benefício Trabalho, mesma que opera Seguro-Desemprego, Abono Salarial, CAGED). **Dono do programa:** MTE.
- **Programa:** PAT (Lei 6.321/1976; Decreto 10.854/2021). **Reforma nov/2025** reduziu a taxa a estabelecimentos de ~8% para **3,6%**, fixou repasse em **até 15 dias** e exige interoperabilidade/aceitação de qualquer bandeira.
- **"Novo PAT"** (novopat.trabalho.gov.br, login GOV.BR) é o sistema oficial do MTE; o marketplace integra-se a ele para validar situação regular de participantes.
- **Volumetria:** ~22 mi trabalhadores · ~450 mil empresas beneficiárias · ~800 mil estabelecimentos (proj. +300 mil até 2030) · **600–700 facilitadoras** (justifica integração via API, não portal manual).

## 3. Landscape Salesforce: atual → alvo
- **Atual (as-is):** greenfield para o PAT — sem org/asset SF reaproveitável citado para este programa.
- **Alvo (to-be), 4 produtos confirmados (Nelson, 27/jul):**
  | Produto | Papel na solução |
  |---|---|
  | **MuleSoft** | Integração com Novo PAT, CTPS Digital, GOV.BR, Geride (auth), eSocial, SDC, Kinis PJ/Par, banco público (boleto/split). Orquestra dados sensíveis *na origem* (ver ADR 0001). |
  | **Experience Cloud** | Portal marketplace (beneficiárias/facilitadoras) autenticado via GOV.BR + procuração digital. |
  | **Core Platform / Service Cloud** | Motor de cotação (leilão), credenciamento, gestão de folha, orquestração de status. |
  | **Agentforce** | Agente informacional/transacional (WhatsApp/webchat) — próximas etapas. |
- **Fora desta rodada:** Data Cloud / Tableau (bloco de monitoramento MTE) — reavaliar em fase futura.

## 4. Escopo e objetivos
**Escopo do ROM (confirmado): fluxo completo — 4 módulos.**
1. **Cotação e Contratação** — beneficiárias publicam necessidade (nº funcionários, valor, vigência, distribuição por UF, recursos obrigatórios); facilitadoras enviam propostas com prazo/SLA; dinâmica de "leilão"; seleção → contrato.
2. **Folha / Financeiro** — upload de folha em layout padronizado; facilitadora processa e agenda crédito; geração de boleto (Bolex/Pix), **conta custódia** em banco público e **split** (repasse à facilitadora + taxa ao MTE/Dataprev).
3. **Credenciamento de Estabelecimentos** — cadastro unificado via GOV.BR; facilitadoras mantêm papel legal de aprovar/descredenciar.
4. **Agentforce** — atendimento/consulta informacional e transacional aos participantes.

**Objetivos:** transparência e concorrência (comparabilidade de propostas), conformidade com a reforma (3,6% / 15 dias), centralização da operação hoje fragmentada entre facilitadoras.

**Jornadas confirmadas pelo protótipo (persona Beneficiária):** login GOV.BR → representar empresa (procuração digital) → Minhas Cotações → Nova Cotação → acompanhamento com prazo → Comparar Propostas → Contrato → Folha de Pagamento (Enviar Folha). Detalhe em `discovery-notes/01-prototipo-figma-cotacao.md`.

## 5. Dados, compliance e arquitetura
- **Residência de dados: híbrida (ADR 0001)** — CPF/dados sensíveis permanecem em infra Dataprev; Salesforce orquestra via MuleSoft sem persistir dado sensível no core. Fronteira exata a ratificar com arquitetura Dataprev.
- **LGPD** (Art. 11 — dado sensível), auditoria **TCU/CGU**, **ANPD**.
- **Licitação:** contratação sob Lei 14.133/2021 — modelo comercial **PS Services + Licenças SF** (Experience Cloud, Agentforce, MuleSoft, Platform).
- **Migração:** carga inicial de cadastros (beneficiárias/facilitadoras/estabelecimentos) a partir do Novo PAT / bases MTE; Novo PAT permanece system-of-record (sem migração massiva).

## 6. Personas / usuários
- **Beneficiária** (empresa contratante) — usuária primária do portal Experience Cloud.
- **Facilitadora** (Visa Vale, Sodexo/Pluxee, Caju, Alelo, Ticket…) — opera via **API** (não portal manual).
- **Estabelecimento** (mercado/restaurante) — credenciamento via GOV.BR.
- **Trabalhador** — notificação de crédito via CTPS Digital (modelo FGTS-like).
- **MTE** — monitoramento a posteriori (fora desta rodada).
- **Dataprev** — operação/sustentação da plataforma.
- *Dimensionamento de usuários nomeados/licenças Experience Cloud a definir (ver Open Questions).*

## 7. Stakeholders
- **Dataprev (negócio/técnico):** Fabricio Paiva, Lucas Pinheiro, Ramon Pontes (requisitos), Jair Bogo (arquitetura/baixo nível).
- **Dataprev (decisão contratual):** Antônio Jaime, Flávio Ronerson (diretores).
- **Salesforce PS:** Rafael Roquette (PM), Tony Tonete (AE), Juliana Brites (líder PS), Juliane Lopes (estratégia/roadmap), Nelson Stebulaitis (EM), Rudi Mayer (CSM).

## 8. Riscos e restrições
1. **Integração Novo PAT/APIs = alto risco** — sem Swagger/definição arquitetural hoje; exigirá **mocks/simulações** enquanto a integração real é construída.
2. **Timeline agressiva** — 4 módulos + múltiplas integrações entre set e nov/2026.
3. **Residência de dados** — decisão híbrida assumida, mas fronteira de campos a ratificar (impacta arquitetura/segurança).
4. **Lógica financeira sensível** — conta custódia + split governo/facilitadora; regra de negócio crítica.
5. **Decisão contratual concentrada na diretoria** — pressão por definições rápidas.
6. **Governança pós go-live** (CoE, change mgmt, adoção) ainda não endereçada.

## 9. Pesquisa / contexto de mercado
- Reforma do PAT (MTE, nov/2025): teto de taxa 3,6% e repasse ≤15 dias mudam o modelo econômico das facilitadoras e criam demanda por comparabilidade → tese do marketplace.
- Mercado concentrado em poucas facilitadoras grandes; interoperabilidade obrigatória favorece plataforma neutra operada pelo governo.

## Open Questions (levar ao cliente)
**Integrações (crítico — bloqueiam DESIGN/estimativa):**
1. Existe Swagger/contrato de API do **Novo PAT**, GOV.BR/Geride, CTPS Digital, eSocial, SDC, Kinis? Prazo para disponibilização? (define quanto será mock vs. real na Etapa 1)
2. Qual **banco público** operará a conta custódia e qual o mecanismo de boleto/Pix e split (Bolex? API própria)?

**Arquitetura / dados:**
3. Fronteira exata da **residência híbrida**: quais campos podem transitar/persistir no SF e quais ficam only-on-Dataprev? (ratificar com Jair Bogo)
4. Escopo real da **carga inicial de cadastros** — volumes, fonte (Novo PAT?), qualidade/deduplicação.

**Escopo / negócio:**
5. Regras do **"leilão"**: critérios de comparação/seleção de propostas, quebra de empate, SLA de resposta das facilitadoras (a tela de Comparar Propostas não está no protótipo).
6. **KPIs de sucesso** quantificados (ex.: % contratações via plataforma, redução de tempo de cotação, taxa média negociada).
7. **Volume de usuários** do portal (beneficiárias ativas simultâneas) para dimensionar licenças Experience Cloud.
8. Escopo do **Agentforce** nesta fase — canais (WhatsApp/webchat), casos de uso (informacional vs. transacional), integração com o marketplace.

**Comercial / governança:**
9. Modelo de licitação/contratação (dispensa via Dataprev vs. edital) e timing de fechamento com a diretoria.
10. Necessidade de **CoE / change management / plano de adoção** no escopo (600–700 facilitadoras + 450k beneficiárias).

---
*Decisões registradas: ADR 0001 (residência de dados híbrida).*
*Próxima fase sugerida: REQUIREMENTS (definir épicas) — via `/dataprev`.*
