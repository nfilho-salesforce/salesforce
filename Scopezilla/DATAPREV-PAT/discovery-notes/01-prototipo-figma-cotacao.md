# Protótipo Figma — "PAT – Cotação" (do cliente)

Fonte: protótipo Figma público do cliente. Screenshots em `discovery-notes/figma/`.
Persona demonstrada: **Beneficiária** (empresa que contrata o vale). Fluxo publicado cobre cotação → contrato → folha; visões de Facilitadora (API) e MTE (monitoramento) não estão no protótipo.

## Telas capturadas

| # | Tela | Persona | Conteúdo-chave |
|---|------|---------|----------------|
| 1 | **Landing / Login** | Pública | Portal gov.br "Programa de Alimentação do Trabalhador – MTE". Botão único **"Entrar com gov.br"**. Links: Política de privacidade, Precisa de ajuda? |
| 2 | **Selecionar empresa que deseja representar** | Beneficiária | Procuração digital: "Seu CPF possui autorização para operar as empresas abaixo." Cards com Razão Social + CNPJ + tipo (Matriz/Filial) + chip **Ativa** + **Selecionar**. Busca por Razão Social/CNPJ. Botões **Cancelar / Continuar**. Aviso: acesso via gov.br, apenas empresas com vínculos válidos, troca de empresa pelo menu superior. |
| 3 | **Empresa selecionada** | Beneficiária | Mesmo layout, card destacado "✓ Empresa selecionada", Continuar habilitado. |
| 4 | **Minhas Cotações (lista)** | Beneficiária | "Consulte o andamento das solicitações enviadas às facilitadoras." Filtros: Número · Status · Data · **Consultar** · **+ Nova Cotação**. Colunas: Número / Data / Empresa / **Status** / Prazo / Ações. Chips de status: 🟢 Contratada · 🟣 Concluída sem contrato · 🟠 Aguardando Propostas · 🔴 Cancelada. Prazo com countdown (4 dias / 1 dia). Ações: 👁 visualizar · 📄 contrato · **Comparar Propostas**. Paginação "1-10 de 100 itens". |
| 5 | **Nova Cotação (formulário)** | Beneficiária | Campos: Quantidade de funcionários (350) · Valor do benefício por trabalhador (R$ 750,00) · Vigência contratual em meses (24) · Periodicidade (Mensal/Quinzenal) · Envio de cartões/talão (Comercial/Residencial) · **Personalização**: Alimentação 70% / Refeição 30% · **Distribuição por UF** (dropdown UF + qtd + adicionar; tabela SP 200 / SC 150) · **Recursos Obrigatórios** (fileira de ícones: cartão, segurança, app, NFC, mobile, carteira, geolocalização, histórico). |
| 6 | **Cotação criada com sucesso** | Beneficiária | Nº 000124 · Status "Em análise pelas facilitadoras" · Data de envio · painel **Acompanhamento**: "Prazo restante **5 dias** para recebimento das propostas" · Próxima etapa. |
| 7 | **Folha de Pagamento → Consultar Contratos** | Beneficiária | Submenu: **Folha de Beneficiários** + **Histórico de Folhas**. Filtros: nº contrato · Facilitadora · Status · Vigência inicial/final · Limpar filtros · Consultar. Tabela: Contrato (CT-000458…) · **Facilitadora** (CAJU, Alelo, Ticket, Sodexo) · Beneficiária · Vigência · **Valor Mensal** (R$ 262.500 / R$ 350.500) · Status (Ativo/Inativo) · Ações (visualizar, **Enviar Folha**, download). |

## Menu lateral (navegação da Beneficiária)
Início · Registros · Empresas Credenciadas · Cotação · Folha de Pagamento (Folha de Beneficiários / Histórico de Folhas) · Facilitadores · Sair.
(Variação vista: "Beneficiários" e "Meus Contratos" em telas de contexto de credenciamento.)

## Máquina de estados da Cotação (inferida)
`Nova → Em análise/Aguardando Propostas (com prazo) → [Comparar Propostas] → Contratada | Concluída sem contrato | Cancelada`

## Regras de negócio visíveis
- Vale dividido em **Alimentação / Refeição** com percentuais configuráveis (ex: 70/30).
- Distribuição de beneficiários **por UF** (impacta precificação regional das facilitadoras).
- **Recursos obrigatórios** padronizados que a beneficiária exige → normaliza a comparação de propostas.
- Cotação tem **prazo/SLA** de recebimento de propostas (dinâmica de leilão, confirmada na reunião).
- Contrato liga Facilitadora ↔ Beneficiária com Vigência e Valor Mensal; folha é enviada por contrato ativo.

## Lacunas do protótipo (validar com cliente)
- Tela de **Comparar/Selecionar Propostas** não capturável (hotspot inativo no proto publicado).
- Telas de **fechar contrato** (URL/telefone com a facilitadora) — citadas no BPMN, não no proto.
- **Credenciamento de estabelecimentos** (BPMN existe; proto não demonstra).
- Visão **Facilitadora** (opera via API, não portal) e visão **MTE/monitoramento**.
- Fluxo financeiro (boleto, conta custódia, split) — está nos BPMN, não no proto.

## Mapeamento preliminar → Salesforce
| Elemento do protótipo | Produto/objeto SF |
|---|---|
| Login gov.br + representar empresa (procuração) | Experience Cloud + integração GOV.BR/Geride via MuleSoft |
| Minhas Cotações (lista + status + prazo) | Objeto **Cotação** com lifecycle/SLA (Core Platform + Flows) |
| Nova Cotação (funcionários, valor, UF, recursos) | Objetos **Cotação / Distribuição-UF / Requisitos** |
| Comparar Propostas + countdown | Motor de **leilão/RFQ**: **Proposta** (N por cotação), comparação, seleção |
| Consultar Contratos + Enviar Folha | Objetos **Contrato** e **Folha**; integração financeira via MuleSoft |
| Facilitadoras via API | MuleSoft (consulta de cotações, envio de propostas, processamento de folha) |
