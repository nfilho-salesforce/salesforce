Como este notebook está configurado em modo de apenas leitura (read-only), eu não tenho
permissão para criar novos arquivos persistentes ou salvar documentos diretamente no seu
painel do Studio. Para gerar arquivos de forma definitiva ou salvar novos entregáveis no
sistema, você deve criar uma cópia pessoal deste notebook.

No entanto, para garantir que você tenha acesso imediato a esses dados e possa utilizá-los de
forma prática, compilei a memória técnica e funcional completa do projeto diretamente aqui
no nosso chat. Você pode simplesmente copiar o conteúdo em Markdown abaixo e colá-lo na
sua outra base de dados ou ferramenta de estimativas.

MEMÓRIA TÉCNICA E FUNCIONAL
COMPILADA – PORTAL DE CRÉDITO
DESENVOLVE SP

1. VISÃO GERAL E MODELO ARQUITETURAL

O projeto consiste na migração e unificação do Portal de Crédito da Desenvolve SP para a
plataforma Salesforce (Experience Cloud), adotando um modelo de arquitetura híbrida:

●  Salesforce: Atua estritamente como a camada de Front-end, orquestração leve de
experiência do usuário (LWC e Flows) e retenção temporária de rascunhos.

●  MuleSoft: Funciona como o middleware de integração de APIs responsável por

padronizar as chamadas e a comunicação de dados.

●  Sinqia e Workflow Legado: Permanecem centralizando toda a lógica complexa de

negócios, análise de crédito, controle de taxas, processamento de contratos e
regras de motor de decisão.

2. DIRETRIZES DE PRAZO, SIZING E
DESENVOLVIMENTO

Para subsidiar a estimativa de esforço na outra base, devem ser considerados os seguintes
parâmetros quantitativos e metodológicos oficiais:

●  Volumetria de APIs: Escopo quantificado em 19 APIs essenciais que conectam o

Salesforce ao core bancário (Sinqia) e sistemas satélites via MuleSoft.

●  Estrutura de Squads: 2 squads de desenvolvimento paralelos atuando em modelo

de metodologia leapfrog.

●  Cronograma Macro: Roadmap estruturado em 14 semanas de desenvolvimento,

com entrega focada em viabilizar um fluxo end-to-end funcional.

3. DETALHAMENTO DOS 6 PILARES OFICIAIS DE
CRÉDITO

PILAR 1: CAPTAÇÃO

Foco: Autenticação, Onboarding, Enriquecimento Cadastral Síncrono e Simulação Sem
Geração de Leads no Legado.

●  Autenticação e Seleção de Contexto: O usuário realiza login no portal utilizando CPF.
Se o CPF possuir múltiplos vínculos empresariais ativos mapeados, o portal exibe um
modal para que ele selecione o CNPJ de contexto sob o qual deseja navegar.

●  Enriquecimento Cadastral Síncrono (JUCESP): No momento do login e seleção da
empresa, o Salesforce consome a API da JUCESP síncronamente via MuleSoft para
capturar a Razão Social, CNAE, faturamento oficial e endereço geográfico completo.
Esses campos são persistidos no objeto Account do Salesforce e configurados como
"Apenas Leitura" (Read-Only) no portal para blindar o cadastro contra fraudes e
digitações erradas.

●  Fallback de Cadastro Manual (Julgamental & Agro): Ativado em caso de erro/timeout
na API JUCESP ou para produtores rurais PF que não constam nas bases de dados
padrão. Permite digitação manual, mas o Salesforce armazena em registro de rascunho
temporário (Draft Account) para impedir que dados manuais sobrescrevam registros
já homologados sem validação do backoffice. Gera logs de auditoria indestrutíveis
(Log_Auditoria__c).

●  Simulador de Crédito Unificado: Executa simulações parametrizadas localmente no

Salesforce sem registrar leads ou propostas no Sinqia nesta fase.

○  Retenção de Contexto: A simulação salva possui validade rígida de 2 dias
corridos (48 horas) comunicada de forma visual por cronômetro regressivo.
Após o prazo, o portal expira o rascunho de simulação e força o reinício do fluxo.

●  Momento de Criação de Registros no Core: A criação síncrona do cliente PJ e da
proposta de crédito no Sinqia só ocorre quando o usuário clica em "Solicitar" no
formulário de pedido, evitando "lixo" ou registros abandonados no legado na fase de
simulação.

●  Compartilhamento e Hierarquia Cooperativas (Agro): Configuração de regras rígidas
de compartilhamento de dados (Sharing Rules e Role Hierarchy) para garantir
que os consultores de uma cooperativa visualizem e operem exclusivamente os dados e
propostas de seus próprios cooperados parceiros.

PILAR 2: PRÉ-QUALIFICAÇÃO

Foco: Formulário Adaptativo, Validação Facial, Conformidade Socioambiental (QRSA) e Serpro.

●  Formulário Unificado Adaptativo: Adapta dinamicamente os campos de solicitação

com base no produto escolhido (ex: Giro Digital vs. Investimento Julgamental),
ocultando as regras de roteamento interno do usuário.

●  Validação Facial (Biovalid): Utiliza a API homologada do Biovalid (Serpro) para

autenticar o sócio proponente que possui CNH ativa.

○  Fluxo de Contingência: Se houver falha de biometria ou ausência de CNH, o
sistema desvia automaticamente para um fluxo de validação manual por
videochamada conduzida pela equipe de backoffice.

●  Filtros de Exclusão Socioambiental: Funciona sob lógica de corte direto ("Tudo ou
Nada"). Se o tomador assinalar desconformidade em qualquer item obrigatório das
listas de restrição (CNAEs/CNPJs vetados), a proposta é cancelada de forma
preventiva diretamente no portal, sem avançar para cálculos de score.
Isenção Parametrizada de QRSA: Operações dos segmentos de setor público,
crédito rural/agro e capital de giro digital estão isentas do preenchimento do
questionário socioambiental completo (Sarasque).

●

●  Motor de Cálculo do Rating QRSA: Processado por procedure no back-end:

Quantidade de respostas positivas / total de questões aplicáveis
(desconsiderando opções "não se aplica"). Classifica em três faixas de rating:

○  Bom: Nota \(\ge\) 0.7
○  Regular: Nota de 0.4 a 0.69
○  Ruim: Nota < 0.4

●  Matriz Combinada de Decisão (Rating vs. Sensibilidade): A sensibilidade é avaliada
de forma combinada por CNAE, Empreendimento e Município (deve ser tudo baixo para
classificar como "Baixa Sensibilidade").

○  Cancelamento Automático: Rating Ruim (< 0.4) em qualquer cenário; OU Rating

Regular (0.4 a 0.69) em operações de Alta Sensibilidade.

○  Prosseguimento: Rating Regular ou Bom em Baixa Sensibilidade; OU Rating

Bom em Alta Sensibilidade.

●  Compartilhamento de Faturamento via Serpro (e-CAC): O cliente PJ indica no portal

o CPF do responsável por autorizar o compartilhamento das informações fiscais
registradas no site do e-CAC da Receita Federal.

●  Triagem Obrigatória (Julgamental): Passagem humana obrigatória pela equipe de

backoffice antes da liberação da ficha cadastral detalhada, analisando o relato do cliente
e a finalidade do crédito.

PILAR 3: PROPOSTA

Foco: Acompanhamento de Status e Tomada de Decisão Comercial.

●  Visualização Híbrida em 3 Estados: A tela de detalhamento das solicitações

adapta-se para otimizar performance e consistência:

○  Estado 1 - Simulação: Visualização básica dos dados de simulação locais.
○  Estado 2 - Em Análise: Carregamento reduzido utilizando estritamente as

informações gravadas no Salesforce (garantindo performance).

○  Estado 3 - Proposta Final: Consulta síncrona em tempo real à API do Sinqia para
carregar os encargos detalhados (IOF, CET, Tarifas, Cronograma de Parcelas).

●  Aceite Síncrono (Digital): O aceite na Jornada Digital formaliza e liquida
instantaneamente a proposta no core bancário de forma automatizada.

●  Validade de Aceite (Julgamental): O Certificado de Aprovação emitido pelo comitê de
crédito possui validade improrrogável de 15 dias corridos para que o cliente realize o
aceite dentro do portal.

PILAR 4: ESTRUTURAÇÃO

Foco: Ficha Cadastral PJ/PF, Bloqueio de Edição e Gestão de Anexos.

●  Fichas Cadastrais de PF e PJ: Formulários detalhados parametrizados para herdar

todos os dados de faturamento e endereço capturados no Pilar 1, evitando redigitação.
Na Jornada Digital, esse preenchimento é exigido pós-aceite da proposta comercial; na
Julgamental, é pré-requisito antes do Comitê de Crédito.

●  Bloqueio Rígido de Edição de Dados: Assim que as fichas cadastrais são

submetidas, o status muda para "Em Análise" e o Salesforce realiza o bloqueio total de
digitação em todos os campos do portal.

●  Ferramenta de Reabertura (Backoffice): O analista interno do Salesforce conta com

um botão de ação rápida para reabrir e desbloquear campos específicos que
apresentem inconsistências, notificando o cliente e ativando pendências visíveis no
portal.

●  Geração de Ficha Cadastral em PDF: Disponibiliza a geração e impressão do PDF

consolidado da ficha cadastral montada com regras de design estáticas (hardcoded) no
Salesforce para agilizar o MVP.

●  Arquitetura e Limitações de Upload de Anexos: O projeto deve contornar os limites
técnicos síncronos de arquivos do Salesforce (6MB para transações síncronas e 12MB
para assíncronas).

○  Solução: Separação em duas APIs (GET para listar categorias; POST de
chunking binário via MuleSoft). A equipe de arquitetura deve validar a
hospedagem física de binários no repositório Amazon S3, mantendo apenas
referências e metadados no CRM.

●  Documentação Agro: Coleta obrigatória de comprovantes de posse ou arrendamento

de terra durante a fase de estruturação.

PILAR 5: APROVAÇÃO

Foco: Sincronização de Status Finais de Crédito.

●  Orquestração de Status via Ocorrências: As transições das fases físicas do workflow

no portal do cliente são controladas estritamente pelo disparo de ocorrências
customizadas geradas no core (Sinqia) e consumidas no Salesforce. O Salesforce
atua de forma reativa, sem criar lógica paralela de esteira de decisão.

●  Adiantamento de Funcionalidades Financeiras (Postergado): Decidido formalmente
que a exibição de dados pós-liberação de crédito no portal (pagamento de parcelas,
quitações, renegociações e variação de taxas pós-fixadas) será postergada para fases
futuras, concentrando o MVP estritamente na originação e formalização.

PILAR 6: FORMALIZAÇÃO

Foco: Emissão de Contratos, Assinaturas Externas e Garantias Complexas.

●  Modelagem Estática da CCB e Termos: O contrato da CCB e os termos de
formalização de garantia são gerados de forma estática pelo backoffice e
disponibilizados ao portal como arquivos em PDF fixos para download, evitando
montagens complexas de HTML ou listagens dinâmicas de cláusulas.

●  Assinatura Digital Externa (Fallback): O portal não implementa assinatura digital
nativa nem biometria de contrato nesta fase. A formalização é tratada como uma
pendência de upload: o cliente baixa o PDF da CCB, realiza a assinatura (física com
firma reconhecida ou por fora do portal via plataforma parceira, como o Glob) e faz o
upload do documento assinado de volta no portal.

●  Codificação Técnica Visual de Cores (Backoffice): Para controle do analista interno
do Salesforce ao conferir as certidões e garantias, os documentos são divididos por
categorias visuais de cores:

○  Azul Escuro: Documentos cadastrais padrão e obrigatórios para todas as

propostas.

○  Azul Claro: Documentos específicos atrelados à atividade econômica declarada.
○  Amarelo: Documentos específicos exigidos para crédito rural e cooperativas

(Agro).

●  Garantias Complexas Agro: O envio de certidões e garantias reais rurais complexas

(penhor de safra, seguros, etc.) é tratado como pendência de anexo de arquivo comum
no portal, sem necessidade de parsing ou processamento complexo de conteúdo pelo
frontend.

4. MATRIZ DE ALINHAMENTO DAS ETAPAS DAS
JORNADAS

Pilar de
Crédito Oficial

Etapa na Jornada Digital

Etapa na Jornada Julgamental /
Agro

Pilar 1:
Captação

• Simulação comercial baseada em
faturamento

• Simulação comercial baseada em
faturamento

Pilar 2:
Pré-qualificaç
ão

• Preenchimento simplificado do
pedido• Acompanhamento inicial do
pedido• Validação facial
automatizada (Biovalid)•
Questionário de conformidade
socioambiental (Desacoplado / Isento
para Giro)

• Preenchimento simplificado do
pedido• Acompanhamento inicial do
pedido• Triagem Humana
Obrigatória (Backoffice)•
Questionário socioambiental
completo (Sarasque - se elegível)

Pilar 3:
Proposta

• Emissão e Aceite Síncrono da
proposta digital (gravação e
consolidação imediata no Sinqia)

Pilar 4:
Estruturação

• Cadastro profundo PF e PJ
(Pós-aceite da proposta comercial)

• Montagem manual da proposta•
Validade de 15 dias corridos do
Certificado de Aprovação para
aceite no portal

• Cadastro profundo PF e PJ
(Pré-envio ao comitê de crédito)•
Envio de documentação
complementar

Pilar 5:
Aprovação

• Orquestração de status de
aprovação via ocorrências

• Orquestração de status de
aprovação via ocorrências

Pilar 6:
Formalização

• Assinatura de Fichas e CCB (via
download e upload de arquivo
assinado de forma externa)

• Documentação e comprovação de
garantias reais complexas
(Pós-Comitê)• Assinatura de
Fichas, CCB e Garantias (via
download e upload de arquivo
assinado externamente)

5. DIRETRIZES DE ENGENHARIA PARA APOIO À
ESTIMATIVA

Ao cadastrar a estimativa na outra base de dados, a equipe técnica deve considerar as
seguintes complexidades de desenvolvimento (volumetria estimada):

1.  Componentes LWC customizados no Experience Cloud:

○  LWC Simulador: Cálculo de encargos locais com regras de expiração de 48h.
○  LWC Formulário de Pedido: Fluxo dinâmico de etapas que oculta o roteamento.
○  LWC de Propostas: Exibição em 3 estados de dados e renderização de parcelas

síncronas.

○  LWCs de Fichas PF/PJ: Formulários repletos de herança, máscaras de dados e

validações.

2.  Lógica de Negócios e Controle de Segurança no Salesforce:

○  Configuração do modelo de objetos temporários para contingência e prevenção

de sobrescrita.

○  Desenvolvimento de gatilhos (Triggers) de bloqueio de edição rígido no

○

Salesforce para status "Em Análise".
Implementação de rotinas de log indestrutíveis para auditoria de criação manual
de contas.

○  Mapeamento de papéis e regras de compartilhamento para restrição de

cooperados.

3.  Middleware de Integração (MuleSoft):

○  Desenvolvimento, mapeamento e testes de 19 barramentos/APIs de integração.
○  Desenvolvimento de conectores para consulta síncrona à JUCESP.
○  Lógica de tratamento de limites de payload de upload de arquivos (GET e POST

separados) e envio de chunks para o Amazon S3.

Se precisar de qualquer refinamento em alguma regra específica ou que eu aprofunde algum
pilar em detalhes antes de você carregar essas informações na outra base, é só me avisar!

💡 Dica de Próximo Passo: Se você desejar, posso ajudar a rascunhar um modelo detalhado
do escopo específico de uma das 19 APIs com os campos mais críticos (como JUCESP ou
Biovalid) para refinar ainda mais a sua base de estimativas.

Para apoiar o planejamento do seu time de desenvolvimento, consolidando o que discutimos
sobre as decisões de escopo e arquitetura, segue o detalhamento técnico e funcional
completo das 19 APIs essenciais mapeadas para a integração entre o Salesforce e o core
bancário (Sinqia/MuleSoft):

PILAR 1: CAPTAÇÃO

1. API-01 – Consulta de Solicitações do Cliente

●  Fase da Jornada: Captação
●  Sistema de Origem: Sinqia
●  Operação: Leitura (GET)
●  Objetivo: Retornar todas as solicitações de crédito do cliente vinculadas a todos os
CNPJs associados ao CPF do usuário autenticado no portal, incluindo as propostas
migradas do portal anterior.

●  Onde é Consumido no Salesforce: Componente de Lista de Solicitações na Home do

Cliente (Experience Cloud). Adota uma solução híbrida: faz a consulta no legado sob

demanda a cada carregamento para atualizar status e armazena os dados no
Salesforce para cache.
●  Middleware: MuleSoft
●  Status / Comentário: Pendente de envio pela equipe da Sinqia. Necessário confirmar

com o cliente a exibição de dados legados do portal anterior.

2. API-20 – Lista "Parceiro que Indicou" (Entidade Empresarial)

●  Fase da Jornada: Captação / Proposta
●  Sistema de Origem: Sinqia (ou outro a definir)
●  Operação: Leitura (GET)
●  Objetivo: Fornecer a listagem de valores válidos e parametrizados de parceiros e
entidades empresariais indicadoras. Centraliza também o campo de Entidade
Empresarial.

●  Onde é Consumido no Salesforce: No subcomponente de "Dados Gerais" dentro do

assistente (wizard) de Criação de Solicitação de Crédito.

●  Middleware: MuleSoft
●  Status / Comentário: A confirmar se o cadastro é uma lista estática pré-definida no

Salesforce ou se virá por integração síncrona.

PILAR 2: PRÉ-QUALIFICAÇÃO

3. API-02 – Detalhamento da Solicitação

●  Fase da Jornada: Pré-Qualificação / Acompanhamento
●  Sistema de Origem: Sinqia
●  Operação: Leitura (GET)
●  Objetivo: Retornar as informações detalhadas de uma proposta comercial de crédito

específica registrada no core bancário.

●  Onde é Consumido no Salesforce: Na aba "Proposta" da Tela de Detalhamento da
Solicitação (as abas de "Simulação" e "Em Análise" utilizam dados residentes no
Salesforce para garantir melhor performance de tela).

●  Middleware: MuleSoft
●  Status / Comentário: Pendente de envio pela Sinqia. Pode haver necessidade de

refatorar o componente de visualização dependendo do formato do payload retornado.

4. API-06 – Gravação/Criação de Declarações

●  Fase da Jornada: Pré-Qualificação
●  Sistema de Origem: Sinqia
●  Operação: Gravação (POST)

●  Objetivo: Persistir na base de dados do Sinqia os aceites formais dados pelo cliente
para as declarações jurídicas obrigatórias (ex: termos de autorização e consulta a
órgãos externos).

●  Onde é Consumido no Salesforce: No subcomponente "Declarações" no fluxo de

criação de proposta de crédito.

●  Middleware: MuleSoft
●  Status / Comentário: A chamada poderá ser efetuada via POST em Ocorrência ou

diretamente no serviço de criação da proposta. Depende de confirmação técnica sobre
se existe uma tabela isolada no banco Sinqia para esses termos.

5. API-11 – Leitura, Criação e Edição de Contas e Contatos (CRUD)

●  Fase da Jornada: Pré-Qualificação / Estruturação
●  Sistema de Origem: Sinqia
●  Operação: Leitura e Escrita (GET/POST/PUT)
●  Objetivo: Centralizar as operações de sincronização cadastral para ler, criar ou

atualizar dados cadastrais de Pessoas Físicas e Jurídicas no Sinqia.

●  Onde é Consumido no Salesforce: No preenchimento da Ficha Cadastral (PJ / PF),

permitindo o reaproveitamento de dados existentes.

●  Middleware: MuleSoft
●  Status / Comentário: Agrupa as necessidades de leitura (API-11), criação (API-12) e

edição (API-13) em uma única interface padronizada de barramento.

6. API-14 – Geração / Impressão de Ficha Cadastral

●  Fase da Jornada: Pré-Qualificação / Estruturação
●  Sistema de Origem: Sinqia
●  Operação: Comando / Geração (GET)
●  Objetivo: Solicitar ao core bancário a geração da ficha cadastral em formato estático

PDF para apoiar coletas de assinaturas físicas, se necessário.

●  Onde é Consumido no Salesforce: Na tela de Ficha Cadastral do Cliente.
●  Middleware: MuleSoft
●  Status / Comentário: O time alinhou que, para fins de MVP e agilidade, as regras de

design visual da ficha serão renderizadas e mantidas hardcoded estáticas no
Salesforce, eliminando processamentos densos de layouts dinâmicos vindos via API do
core bancário.

7. API-17 – Endpoints de Listas de Valores (Picklists)

●  Fase da Jornada: Pré-Qualificação / Estruturação
●  Sistema de Origem: Sinqia
●  Operação: Leitura (GET)
●  Objetivo: Retornar dinamicamente os valores padronizados de tabelas acessórias (ex:

CNAE Principal, CNAE Secundário, Forma de Constituição, Origem de Capital, Controle
Acionário, Setores de Atuação e Bancos homologados).

●  Onde é Consumido no Salesforce: Em todos os formulários da Ficha Cadastral e de

pedidos do portal que demandem seleção padronizada em combos.

●  Middleware: MuleSoft
●  Status / Comentário: Pendente de desenvolvimento técnico para expor os endpoints

das tabelas do Sinqia.

8. API-27 – Validação Facial Antifraude (BioValid)

●  Fase da Jornada: Pré-Qualificação
●  Sistema de Origem: BioValid (Serpro / SENATRAN)
●  Operação: Comando / Integração síncrona
●  Objetivo: Realizar a checagem biométrica facial do sócio PJ proponente cruzando os

dados de imagem com a base oficial do DETRAN/SENATRAN.

●  Onde é Consumido no Salesforce: No fluxo de Onboarding e Validação do Pedido

Digital.

●  Middleware: MuleSoft
●  Status / Comentário: Ficou formalmente decidido que o BioValid será tratado como
opcional nesta primeira entrega. Caso o usuário não possua CNH ativa ou a API
biométrica falhe, o Salesforce tratará isso como uma exceção guiada, desviando o fluxo
para um processo de validação manual (videochamada) com o analista.

PILAR 3: PROPOSTA

9. API-16 – Gravação e Criação de Solicitação ("Conta-Proposta")

●  Fase da Jornada: Proposta
●  Sistema de Origem: Sinqia
●  Operação: Criação / Gravação (POST)
●  Objetivo: Consolidar e gravar síncronamente a relação definitiva entre a Conta e a

Prospecção/Proposta no core bancário Sinqia.

●  Onde é Consumido no Salesforce: No momento exato em que o cliente finaliza o

preenchimento de todas as informações básicas da proposta e clica no botão "Solicitar
Financiamento".
●  Middleware: MuleSoft
●  Status / Comentário: Pendente de envio pela Sinqia. É a chamada integradora que
sinaliza ao core que uma nova intenção de crédito foi consolidada (evitando dados
fantasmas nas simulações anteriores).

PILAR 4: ESTRUTURAÇÃO

10. API-10 – Consulta de Categorização de Arquivo

●  Fase da Jornada: Estruturação
●  Sistema de Origem: Sinqia
●  Operação: Leitura (GET)
●  Objetivo: Buscar os tipos de arquivos e as categorias de anexos permitidas e

obrigatórias com base no produto financeiro de interesse do cliente.

●  Onde é Consumido no Salesforce: No componente de upload de anexos da Ficha

Cadastral e de Pendências.

●  Middleware: MuleSoft
●  Status / Comentário: Funciona como um mapeamento em par de chave-valor. Auxilia a

validar regras de negócio dinâmicas no front-end.

11. API-19 – Armazenamento e Upload de Anexos

●  Fase da Jornada: Estruturação
●  Sistema de Origem: Sinqia / Repositório de Arquivos Externo (Amazon S3)
●  Operação: Gravação / Upload (POST)
●  Objetivo: Persistir os binários dos documentos enviados pelo cliente de forma

assíncrona para contornar as limitações físicas de tamanho de arquivo do Salesforce.
●  Onde é Consumido no Salesforce: No assistente de uploads de documentos da Ficha

PJ/PF e do painel de Pendências.

●  Middleware: MuleSoft
●  Status / Comentário: A equipe de arquitetura está avaliando o desenho de tráfego

síncrono/assíncrono integrando o Salesforce via MuleSoft diretamente ao Amazon S3
para hospedagem definitiva, mantendo no Salesforce somente os metadados.

12. API-22 – QRSA (Leitura de Questionário Socioambiental)

●  Fase da Jornada: Estruturação / Pré-Qualificação
●  Sistema de Origem: Sinqia / Sistema Officer
●  Operação: Leitura (GET)
●  Objetivo: Retornar dinamicamente a estrutura de perguntas vigentes do Questionário
de Responsabilidade Socioambiental (QRSA) cadastrado e mantido no back-end.
●  Onde é Consumido no Salesforce: Na seção dedicada de Declaração/QRSA do

pedido, permitindo que o Salesforce avalie as isenções (Giro Digital, Crédito Agro e
Setor Público).

●  Middleware: MuleSoft
●  Status / Comentário: Permite que as perguntas do questionário de sensibilidade

permaneçam parametrizadas no Sinqia, eliminando a manutenção manual no CRM.

13. API-23 – QRSA (Gravação de Respostas do Questionário)

●  Fase da Jornada: Estruturação
●  Sistema de Origem: Sinqia / Sistema Officer
●  Operação: Gravação (POST)

●  Objetivo: Enviar os dados e as respostas preenchidas pelo tomador para persistência

direta no back-end.

●  Onde é Consumido no Salesforce: Ao salvar o step do formulário QRSA do cliente.
●  Middleware: MuleSoft
●  Status / Comentário: Esta submissão síncrona aciona e alimenta os serviços internos

de análise de risco e o motor de cálculo.

14. API-25 – QRSA (Cálculo e Processamento de Rating)

●  Fase da Jornada: Estruturação
●  Sistema de Origem: Sinqia (via Stored Procedure ou serviço dedicado)
●  Operação: Cálculo / Processamento de regras
●  Objetivo: Executar de forma automatizada o cálculo de nota socioambiental (Rating =

respostas positivas / total de perguntas aplicáveis) e cruzar com os dados de
Sensibilidade (CNAE de atividade, tipo de empreendimento e município) para retornar
se o cliente está elegível (Bom / Regular) ou descartado (Ruim).

●  Onde é Consumido no Salesforce: Integrado à esteira interna do motor de decisão

para tomada de ação síncrona.

●  Middleware: MuleSoft
●  Status / Comentário: Permite blindar a lógica complexa de rating socioambiental de
forma centralizada em uma procedure interna do back-end legado, poupando código
customizado no Salesforce.

PILAR 5: APROVAÇÃO

15. API-09 – Aceite / Recusa Comercial no Workflow

●  Fase da Jornada: Aprovação / Proposta
●  Sistema de Origem: Sinqia
●  Operação: Gravação / Envio de comando (POST)
●  Objetivo: Notificar de forma síncrona ao Sinqia o comando formalizado pelo tomador no

portal de aceitação das taxas vigentes ou recusa definitiva do crédito liberado pelo
comitê.

●  Onde é Consumido no Salesforce: Na tela de Acompanhamento / Detalhes de

Proposta comercial aprovada.

●  Middleware: MuleSoft
●  Status / Comentário: Será mapeado utilizando POST em registro de Ocorrência

customizada para sinalizar ao workflow legado que o processo pode avançar para a
fase de emissão de CCB e formalização.

PILAR 6: FORMALIZAÇÃO

16. API-03 – Consulta de Lista de Contratos do Cliente

●  Fase da Jornada: Formalização
●  Sistema de Origem: Sinqia
●  Operação: Leitura (GET)
●  Objetivo: Retornar uma listagem dos contratos e termos comerciais do cliente.
●  Onde é Consumido no Salesforce: No painel/seção "Meus Contratos" do cliente

cadastrado para permitir navegação e consulta de detalhes financeiros.

●  Middleware: MuleSoft
●  Status / Comentário: Pendente de confirmação com a equipe Sinqia sobre a existência

da API de GET de Lista de Contratos.

17. API-04 – Download de Arquivo de Contrato (CCB)

●  Fase da Jornada: Formalização
●  Sistema de Origem: Sinqia
●  Operação: Leitura / Download (GET)
●  Objetivo: Fornecer e retornar de forma direta para download o documento binário

correspondente à Cédula de Crédito Bancário (CCB) gerada para que o proponente a
assine externamente. Centraliza também a lógica da API-30 de geração.

●  Onde é Consumido no Salesforce: No subcomponente de Contratação e no painel de

Detalhes de Contrato.
●  Middleware: MuleSoft
●  Status / Comentário: Depende de definição técnica sobre o formato e a entrega do

binário.

18. API-24 – Assinatura Digital do Termo QRSA

●  Fase da Jornada: Formalização
●  Sistema de Origem: Sinqia / Sistema de Assinatura Digital homologado
●  Operação: Gravação / Comando
●  Objetivo: Registrar síncronamente no Sinqia que o Termo do QRSA gerado foi

devidamente assinado e vinculá-lo como anexo associado à oportunidade de negócio
de crédito.

●  Onde é Consumido no Salesforce: Na conclusão do passo de formalização do

questionário socioambiental.

●  Middleware: MuleSoft
●  Status / Comentário: Necessário obter definições acordadas com a equipe sobre o

fluxo integrado de geração do documento e mecanismos de segurança de assinatura
digital.

19. API-29 – Assinatura e Validação da CCB

●  Fase da Jornada: Formalização
●  Sistema de Origem: Sinqia / CCB / Sistema de Assinatura parceiro

●  Operação: Gravação / Comando síncrono
●  Objetivo: Processar o comando de verificação e validação da CCB assinada de forma

externa, aplicando as chaves de segurança e liberando o status de contrato formalizado
no back-end.

●  Onde é Consumido no Salesforce: No subcomponente de finalização da contratação

da CCB.

●  Middleware: MuleSoft
●  Status / Comentário: Escopo técnico a ser integrado e parametrizado com suporte de
barramentos do MuleSoft para lidar com plataformas de terceiros de assinaturas.

💡 Próximo Passo Recomendado

Como sua equipe de engenharia do MuleSoft e Salesforce está em fase de refinamento e
consolidação das planilhas de Swagger, eu posso rascunhar um modelo representativo em
formato JSON (Payload Mockup) de entrada e saída para a API-25 (Processamento e
Rating da matriz de risco socioambiental) ou para a API-16 (Conta-Proposta) para que eles
possam acelerar os contratos de desenvolvimento. Qual delas seria mais útil estruturar agora?

O fluxo da API de Anexos no novo portal foi desenhado com foco em alta performance e
eliminação definitiva do uso de e-mails para envio de documentos, resolvendo gargalos
históricos de descentralização de arquivos.

Abaixo está o detalhamento de como a arquitetura do Salesforce, MuleSoft e o core bancário
(Sinqia) interagem para processar e armazenar os arquivos:

1. Separação de Responsabilidades (API-10 e API-19)

Para otimizar o tráfego de dados e permitir que o portal saiba dinamicamente quais
documentos exigir do cliente (sem precisar de manutenção manual no front-end), o fluxo foi
dividido em duas APIs distintas:

●  API-10 – Consulta de Categorização (GET): Quando o cliente acessa uma etapa de
upload (seja na Ficha Cadastral ou na resolução de uma pendência), o Salesforce
consome a API-10. Ela retorna do back-end a lista de tipos de documentos obrigatórios
e permitidos com base no perfil do cliente e no produto financeiro (tratados como pares
de chave-valor).

●  API-19 – Armazenamento de Anexos (POST): É a API responsável pelo envio físico e

gravação do binário do arquivo submetido pelo portal.

2. Tratamento dos Limites de Arquivos e Armazenamento (Amazon S3)

O Salesforce possui limitações nativas rígidas de tamanho para tráfego síncrono de dados de
arquivos:

●  6 MB para transações síncronas.
●  12 MB para transações assíncronas.

O Fluxo de Contorno Técnico:

1.  Para contornar esse limite e evitar lentidão ou falhas de envio no portal, a equipe de
arquitetura definiu o uso de um repositório Amazon S3 externo para guardar
fisicamente os arquivos.

2.  Quando o cliente faz o upload de um arquivo pesado no portal, o componente de

front-end (LWC) processa o arquivo de forma assíncrona.

3.  O MuleSoft atua como o middleware orquestrador: ele recebe o binário, salva o arquivo
com segurança no Amazon S3 e envia ao legado (Sinqia) apenas as referências físicas
e metadados de vinculação do arquivo àquela proposta/conta específica.

4.  O Salesforce não armazena os binários pesados, guardando internamente apenas os

registros de metadados das pendências e o status do arquivo (ex: "Em Análise"),
economizando espaço e garantindo alta performance de tela.

3. Integração com o Fluxo de Saneamento de Pendências (Fim dos E-mails)

O envio de documentos está diretamente atrelado à Central de Pendências do portal, que
funciona de forma integrada com o backoffice:

1.  Geração da Pendência: Se um analista de backoffice identificar um documento inválido
ou vencido, ele registra uma ocorrência no Salesforce. Isso cria automaticamente uma
pendência ativa na página inicial do portal do cliente, bloqueando o avanço do fluxo de
crédito.

2.  Upload de Resolução: O cliente visualiza o alerta em sua Home, clica na pendência e

faz o upload do novo documento.

3.  Processamento Automático: O upload dispara a API-19 (salvando o binário no S3) e
gera uma ocorrência automática de retorno para o sistema da Sinqia/Workflow.

4.  Visualização no Backoffice: O analista interno visualiza todos os arquivos enviados de

forma centralizada e diretamente associados à proposta, ordenados
cronologicamente por data, sem precisar caçar e-mails ou abrir pastas externas na
rede.

Se você precisar de apoio para desenhar o contrato Swagger detalhado (payloads de entrada e
saída) desta API de upload assíncrono para os seus times técnicos, ou se quiser detalhar o
fluxo específico das pendências de garantias rurais (Agro), é só me avisar!


