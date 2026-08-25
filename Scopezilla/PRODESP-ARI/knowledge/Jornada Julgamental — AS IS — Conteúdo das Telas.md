## Jornada Julgamental — AS IS — Conteúdo das Telas

### Tela 1 — LOGIN

Login via CPF. Após o login, o sistema consulta a JUCESP e retorna as empresas vinculadas ao usuário.

### Tela 2 — TELA DE DECISÃO DE LOGIN — JUCESP

Seleção do CNPJ/empresa em que o usuário vai trabalhar nessa sessão. Dados pré-preenchidos da JUCESP, não editáveis.

Decisão (sessão 10/08): Essa tela foi descontinuada — o novo protótipo já unifica o login por CPF com a visualização dos vínculos de CNPJ.

### Tela 3 — TERMO DE COMPARTILHAMENTO DE DADOS — PARCEIROS

Exibição de termo de consentimento para compartilhamento de dados com parceiros (ex: Sebrae). Aceite registrado.

Decisão: Texto fixo no front-end (sem API dinâmica). O termo do Sebrae tem endpoint próprio (compartilhamento customizado).

### Tela 4 e 5 — TELA INICIAL — ACOMPANHAMENTO DE PEDIDO (sem/com filtro)

Lista de solicitações do cliente. Campos exibidos por pedido:

* Status atual (abstração para o cliente: "Em Análise", "Proposta", etc.)
* Botão contextual para ação pendente (ex: "Concluir Simulação")
* Filtro de lista (na tela 5)

Arquitetura: Estratégia híbrida — dados mantidos no Salesforce, consulta ao legado (Sinqia) por demanda para sincronizar status. Visualização de etapas (path) somente na tela de detalhes, não na lista.

### Tela 6 — FORMULÁRIO — PASSO 1: FINANCIAMENTO DE INTERESSE

Campos:

* Linha de crédito / Produto (seleção — sem filtro automático pelo perfil, nesta versão)
* Finalidade do financiamento
* CNPJ (pré-preenchido pela conta selecionada)
* Razão Social (pré-preenchido via JUCESP)
* Nome do Parceiro indicador (picklist pré-definida)
* Valor pretendido
* Periodicidade da amortização (vem da Simulação, se aplicável)
* Prazo Total / Prazo de Carência (da Simulação)

Nota: O formulário deve ser "enxugado" — CNAE e Faturamento podem ser eliminados ou pré-preenchidos.

### Tela 7 — FORMULÁRIO — PASSO 2: TERMOS DE AUTORIZAÇÃO

Apresentação dos termos de autorização de acesso a órgãos externos (ex: Receita Federal, SCR, SERPRO). Texto fixo, igual para Digital e Julgamental.

* Checkbox de aceite por termo
* Registros gravados no Salesforce

### Tela 8 — FORMULÁRIO — PASSO 3: DECLARAÇÃO DE EXCLUSÃO

Declaração de responsabilidade socioambiental (lista de exclusão QRSA).

* Checklist de afirmações ("não realizo X atividade")
* Lógica "tudo ou nada": se o cliente não concordar com qualquer item → operação cancelada automaticamente
* Sem API complexa; lógica no front-end

### Telas 9 e 10 — FORMULÁRIO — PASSO 4 (1 e 2): QRSA

Questionário de Responsabilidade Socioambiental (QRSA / Sarasque):

Parte 1 (tela 9): Perguntas do questionário — respostas: Sim / Não / Não se aplica

Parte 2 (tela 10): Resultado e assinatura

* Rating calculado automaticamente: respostas positivas ÷ total aplicáveis
  + Bom ≥ 0,7 → prossegue
  + Regular 0,4–0,69 → depende da Sensibilidade DSP
  + Ruim < 0,4 → cancelamento automático
* Apuração de Sensibilidade DSP (automática, baseada em CNAE + tipo de empreendimento + município):
  + Baixa exposição: todos os fatores são baixos
  + Alta exposição: qualquer fator de alto risco
* Matriz de decisão:

| Rating | Sensibilidade | Resultado |
| --- | --- | --- |
| Ruim | Qualquer | ❌ Cancelado |
| Regular | Alta | ❌ Cancelado |
| Regular | Baixa | ✅ Prossegue |
| Bom | Alta | ✅ Prossegue |
| Bom | Baixa | ✅ Prossegue |

* Assinatura digital do termo QRSA + upload para a oportunidade

Implementação: APIs existentes no Sinqia (procedures) fazem o cálculo; o Salesforce consome via API. Telas construídas estaticamente no SF.

### Tela 11 — FORMULÁRIO — PASSO 5: CPF AUTORIZADOR

* Campo: CPF do Autorizador
* Integração com SERPRO para validação
* Registro gravado vinculado à proposta (junto com o CPF, para auditoria)

### Telas 12 e 13 — FICHA CADASTRAL PJ / PF

Preenchimento estruturado do cadastro, solicitado após triagem.

PJ — abas:

| Aba | Campos |
| --- | --- |
| Identificação | CNPJ, Razão Social, Nome Fantasia, Atividade Principal (CNAE), Atividade Secundária (CNAE), Forma de Constituição, Origem do Capital, Controle Acionário, Setor, Banco |
| Dados Complementares | Dados financeiros, faturamento, etc. |
| Sócios Acionistas / Admin | Inclusão e gestão de sócios/administradores |
| Participação em PJs | Empresas que a PJ participa |
| Participação em PJs — Inclusão | Formulário de inclusão de nova participação |
| Participação em PJs — Anexos | Upload de documentos (cartão CNPJ obrigatório; hardcoded) |

PF — abas:

| Aba | Campos |
| --- | --- |
| PF's Relacionadas | Garantes / sócios PF vinculados |
| Identificação | CPF, Nome, RG, data de nascimento |
| Cônjuge ou Companheiro | Dados do cônjuge |
| Endereço Residencial | Endereço completo |
| Dados Profissionais | Cargo, renda |
| Empresa que Participa | Vínculo com PJs |
| Anexos | Upload de documentos (hardcoded, tipo definido pelo cartão CNPJ / doc padrão) |

Comportamento após salvar: Status muda para "Em Análise" → cadastro travado para o cliente. Backoffice tem permissão para reabrir.

Dados de picklists (CNAE, Forma de Constituição, etc.): endpoint específico no Sinqia, se lista for extensa.

Armazenamento de anexos: limite 6MB síncrono / 12MB assíncrono no SF; Amazon S3 em avaliação para grandes arquivos.

### Tela 14 — TELA DE CONSULTOR — MANUTENÇÃO DE ACESSO DE USUÁRIO

Perfil interno (consultor). Gestão de acessos de usuário vinculados a propostas.

### Tela 15 — TELA DE CONSULTOR — ALTERAÇÃO DE STATUS CADASTRAL

Perfil interno (consultor/backoffice). Permite alterar status cadastral do cliente manualmente durante a análise — funcionalidade que precisa ser desenhada no Salesforce para evitar o bloqueio rígido atual do processo.

# Comparativo de Jornada — Digital vs. Julgamental

Cobre o fluxo completo: login → solicitação de crédito → acompanhamento do pedido. Base: prints das telas, notas das sessões de discovery (Sessões 1–3) e levantamento DSP.

## Legenda

| **Símbolo** | **Significado** |
| --- | --- |
| ✓ | Presente e equivalente em ambas |
| D | Exclusivo da jornada Digital |
| J | Exclusivo da jornada Julgamental |
| ≈ | Presente em ambas, mas com diferença relevante |

## Comparativo por etapa

| **Etapa** | **Digital** | **Julgamental** | **Observações** |
| --- | --- | --- | --- |
| **Login e autenticação** | ✓ | ✓ | CPF/CNPJ; seleção de empresa via JUCESP; dados pré-preenchidos e não editáveis |
| **Menu "Minhas solicitações" e "Ficha cadastral"** | D | — | Julgamental acessa via backoffice (Officer/Sinqia) |
| **Tela introdutória com jornada macro** | D | — | Digital apresenta as 4 etapas: Solicitação → Cad.PJ → Cad.PF → Contratação |
| **Simulação de crédito** | — | J | Pré-solicitação; dados da simulação não são trazidos para o formulário (dor conhecida) |
| **Estrutura do formulário de solicitação** | D | J | Digital: wizard de 10 passos com progress bar; Julgamental: formulário único longo |
| **Termos de autorização** | ≈ | ≈ | Mesmo conteúdo (2 termos); Digital tem passo dedicado antes dos dados; Julgamental exibe em modal ao avançar |
| **Dados gerais da solicitação** | ✓ | ✓ | Identificação da empresa e endereço |
| **Contato** | ✓ | ✓ | Digital tem passo dedicado; Julgamental inline no formulário |
| **Dados da empresa** | ≈ | ≈ | Base idêntica; Julgamental tem campos adicionais (Setor, grupo econômico, nº empregados) |
| **Empréstimo pretendido** | ≈ | ≈ | Mesmos dados; labels divergem ("Financiamento de interesse" vs. "Linha de crédito") |
| **Sócios** | D | J | Digital coleta no Cadastro PJ (etapa separada); Julgamental coleta no próprio formulário do pedido |
| **Declaração de exclusão** | ✓ | ✓ | Mesmo conteúdo; pequena diferença no mecanismo de aceite |
| **QRSA — Responsabilidade Socioambiental** | ≈ | ≈ | Mesmo questionário; Julgamental exibe resultados calculados (Sensibilidade/Rating/Classificação); Digital não exibe |
| **Autorizador Receita Federal (eCAC/SERPRO)** | ✓ | ✓ | Digital tem passo dedicado; Julgamental exibe em modal |
| **Validação facial (BioValid)** | D | — | Via app BioValid (CNH); alternativa: análise manual ou videoconferência |
| **Tela "Em análise" / confirmação** | D | — | Julgamental não tem tela de confirmação no fluxo do cliente |
| **Cadastro Pessoa Jurídica** | D | — | Digital: 5 passos (endereço, dados complementares, sócios, participação em empresa, anexos) |
| **Cadastro Pessoa Física** | D | — | Digital: etapa 3 da jornada macro (conteúdo a confirmar) |
| **Proposta** | ≈ | ≈ | Digital: gerada por motor automático (fundo garantidor); Julgamental: montada manualmente pela SUCI |
| **Certificado de aprovação** | — | J | Cliente tem 15 dias para aceitar |
| **Aceite/recusa da proposta pelo cliente** | ✓ | ✓ | Com geração de PDF |
| **Acompanhamento do pedido** | ✓ | ✓ | Status em tempo real via Sinqia; detalhe, anexos, despachos, exigências, procuradores |
| **Notificações** | ✓ | ✓ | Ambas notificam em cancelamento; sem notificação intermediária durante análise |
| **Controle visual de SLA / prazo** | — | — | Não implementado em nenhuma jornada; controle manual por e-mail |
| **Formalização / Contratação** | ≈ | ≈ | Download e upload de documentos; sem assinatura digital nativa (ferramenta externa); Julgamental tem garantias fortes + documentação socioambiental por cores |

## Resumo executivo

### Exclusivo Digital

* Tela introdutória com jornada macro em 4 etapas
* Wizard de 10 passos com progress bar
* Termos de autorização em passo dedicado (antes dos dados)
* Passo dedicado para Autorizador SERPRO
* Validação facial (BioValid / CNH) com fallback para análise manual
* Tela "Em análise" com confirmação pós-envio
* Cadastro PJ estruturado em 5 passos (etapa separada)
* Cadastro PF como etapa separada
* Proposta gerada por motor automático (fundo garantidor)

### Exclusivo Julgamental

* Simulação de crédito antes da solicitação
* Formulário único longo (sem wizard)
* Termos e autorizações exibidos em modais sobrepostos
* Sócios + cônjuge coletados no próprio formulário do pedido
* Campos adicionais de dados da empresa (Setor, grupo econômico, nº empregados)
* Resultados calculados do QRSA visíveis para o usuário
* Proposta montada manualmente pela área de crédito (SUCI)
* Certificado de aprovação com prazo de 15 dias
* Garantias fortes + documentação socioambiental por cores na formalização

## Pontos em aberto para a discussão de unificação

1. **Sócios:** consolidar coleta no Cadastro PJ ou manter no formulário do pedido?
2. **Simulação:** trazer pré-preenchimento para o Digital ou universalizar para as duas jornadas?
3. **Termos:** passo dedicado (Digital) ou modal inline (Julgamental)? UX de menor atrito a definir.
4. **QRSA:** exibir resultados calculados também no Digital ou ocultar dos dois?
5. **Validação de identidade:** BioValid é exclusivo Digital — avaliar se Julgamental precisará em algum cenário.
6. **Nomenclatura:** unificar "Financiamento de interesse" vs. "Linha de crédito".
7. **SLA / prazo:** nenhuma jornada tem controle visual — oportunidade de melhoria compartilhada.
8. **Passo 10 "Proposta" no Digital:** sem print disponível — conteúdo a confirmar.
9. **Cadastro PF:** sem prints — mapear conteúdo antes de discutir unificação.
