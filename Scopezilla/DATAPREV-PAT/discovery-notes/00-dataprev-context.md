# Contexto Dataprev — PAT (Marketplace do Programa de Alimentação do Trabalhador)

## Identificação
- Projeto: **PAT — Marketplace do Programa de Alimentação do Trabalhador**
- Área Dataprev: **DPS / SUTF / DEBT** (Divisão de Benefício Trabalho — mesma que opera Seguro-Desemprego, Abono Salarial, CAGED)
- Cliente final / dono do programa: **Ministério do Trabalho e Emprego (MTE)**
- Executor da solução: **Dataprev** (fábrica pública de software do governo federal)
- Tipo: Governo Federal Brasileiro

## Produtos Salesforce in-scope
Confirmado por Nelson (27/jul/2026) — 4 produtos:
- **MuleSoft** — integração via API com Novo PAT, CTPS Digital, GOV.BR, Geride (auth), eSocial, SDC, Kinis PJ/Par, banco público (boleto/split). Ordem de grandeza: 600–700 facilitadoras + centenas de milhares de beneficiárias.
- **Experience Cloud** — portal marketplace para beneficiárias/facilitadoras (cotação/contratação/credenciamento) autenticado via GOV.BR / procuração digital.
- **Core Platform / Service Cloud** — motor de cotação, credenciamento, gestão de folha, orquestração de status.
- **Agentforce** — agente informacional e transacional via WhatsApp/webchat (citado explícito nas próximas etapas da reunião).

_Fora do escopo confirmado nesta rodada:_ Data Cloud / Tableau (monitoramento do MTE) — reavaliar em DISCOVER/DESIGN se o bloco de monitoramento entrar no contrato.

## Objetivo do Projeto
Construir uma **plataforma-marketplace** que centralize e dê transparência ao PAT, com quatro blocos:
1. **Cotação e Contratação** — beneficiárias publicam necessidades (nº funcionários, valor do benefício); facilitadoras (Visa Vale, Sodexo/Pluxee, Caju etc.) enviam propostas com taxas padronizadas. Dinâmica de "leilão" (não é produto de prateleira — flexibilidade por porte/região).
2. **Módulo Financeiro / Folha de Pagamento** — beneficiária faz upload de folha em layout padronizado (relação de empregados + valores VA/VR); facilitadora processa e agenda crédito; plataforma gera boleto (Bolex/Pix), recebe em **conta custódia** em banco público e faz **split** (repasse à facilitadora + taxa ao MTE/Dataprev).
3. **Credenciamento de Estabelecimentos** — cadastro unificado de restaurantes/mercados via GOV.BR; facilitadoras mantêm papel legal de aprovar/descredenciar.
4. **Monitoramento e Visibilidade (MTE)** — acompanhamento *a posteriori* das operações; identificação de irregularidades, padrões anômalos, transações fora do padrão; dados: estabelecimento, valor, data/hora, CPF do comprador (futuro: categoria do produto). Notificação ao trabalhador via **CTPS Digital** (modelo similar ao FGTS — aviso de crédito, não gestão de saldo).

## Fase Atual
- **Discovery / Avaliação de aderência (pré-proposta).**
- Reunião de apresentação de demanda: **21/jul/2026**.
- Fechamento contratual será com **Antônio Jaime e Flávio Ronerson** (diretores) — equipe técnica apresenta, diretoria decide.

## Contexto Regulatório do PAT (pré-carregado)
- PAT instituído pela **Lei nº 6.321/1976**; consolidado no Decreto 10.854/2021.
- **Reforma de nov/2025**: taxa máxima cobrada de estabelecimentos reduzida de ~8–8,5% para **3,6%**; prazo de repasse às redes credenciadas fixado em **até 15 dias** (antes média de mercado de ~45 dias, sem lei); interoperabilidade/aceitação de qualquer bandeira de alimentação.
- **"Novo PAT"** = sistema oficial do MTE (novopat.trabalho.gov.br), login GOV.BR, com prazo de atualização cadastral obrigatória de participantes em jul/2026. O marketplace integra-se a ele para validar situação regular de beneficiárias e facilitadoras.
- Dados sensíveis (CPF do trabalhador) → **LGPD** + discussão de **residência nacional dos dados** (nuvem vs. Oracle on-premise — decisão de arquitetura em aberto).

## Volumetria (estimada, reunião)
- ~**22 milhões** de trabalhadores beneficiados
- ~**450 mil** empresas beneficiárias
- ~**800 mil** estabelecimentos credenciados (projeção +300 mil até 2030)
- **600–700** facilitadoras no Brasil (justifica arquitetura via API, não portal manual)

## Cronograma-alvo (agressivo)
- **Fim de setembro/2026**: homologação do marketplace (cotação + contratação) e integração com o Novo PAT.
- **15 de novembro/2026**: produção do fluxo completo, incluindo módulo financeiro.
- Uso de **mocks/simulações** das APIs enquanto integração real é construída (conhecimento detalhado das APIs em tempo de projeto — hoje sem Swagger/definição arquitetural).

## Stakeholders
- **Dataprev (negócio/técnico):** Fabricio Paiva, Lucas Pinheiro (Divisão Benefício Trabalho), Ramon Pontes (requisitos), Jair Bogo (técnico/baixo nível).
- **Dataprev (decisão contratual):** Antônio Jaime, Flávio Ronerson (diretores).
- **Salesforce PS:** Rafael Roquette (PM), Tony Tonete (AE Market Cloud/gov), Juliana Brites (líder PS/consultoria), Juliane Lopes (estratégia/roadmap), Nelson Stebulaitis (Engagement Manager), Rudi Mayer (CSM).
- **Serviço na ponta (sem dependência técnica imediata):** Fernanda, Milton, Márcia Bezerra.

## Termos-chave
- **Facilitadora** = emissora do cartão VA/VR (Visa Vale, Sodexo/Pluxee, Caju).
- **Beneficiária** = empresa que contrata o benefício para seus funcionários.
- **Estabelecimento** = rede credenciada (supermercado/restaurante) que aceita o cartão.

## Riscos iniciais mapeados
- **Integração Novo PAT = alto risco** — sem Swagger/definição arquitetural hoje; mocks necessários.
- **Timeline agressiva** (set + nov/2026) com escopo amplo (4 módulos) e integrações múltiplas.
- **Decisão de residência de dados** (nuvem vs. on-premise) em aberto — impacta arquitetura e segurança.
- **Lógica financeira sensível** (conta custódia + split governo/facilitadora) — regra de negócio reside na plataforma do Ministério.
- **Decisão contratual concentrada em diretoria** (Antônio Jaime/Flávio Ronerson) — pressão por definições rápidas.
- Governança pública: LGPD (dados sensíveis), auditoria TCU/CGU, licitação Lei 14.133/2021.

## Artefatos recebidos (discovery-notes/)
- PDF Notes by Gemini (resumo + transcrição da reunião de 21/jul/2026)
- Gravação MP4 (~883 MB — não processada)
- BPMN 1 — Cotação e Contratação (raias Beneficiária / Marketplace / Facilitadoras)
- BPMN 2 — Folha de Pagamento (upload CSV → processamento → boleto, com polling da facilitadora)
- BPMN 3 — Split Financeiro (Beneficiária / Marketplace / Facilitadora / Banco Público / MTE; split paralelo)
- Slides "Marketplace – Financeiro" (o que é, como funciona, comparativo atual vs. nova plataforma)
