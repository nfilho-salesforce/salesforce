Catálogo estratégico de épicos e casos
de uso: Salesforce Automotive Cloud

Seção 1: Estrutura estratégica para a transformação
automotiva

O setor automotivo está em um ponto de inflexão, passando de um modelo de negócios
centrado no produto para um modelo focado na experiência do cliente e na mobilidade como
serviço. Nesse novo paradigma, a capacidade de uma organização de gerenciar de forma
abrangente o relacionamento com o cliente ao longo de todo o seu ciclo de vida torna-se o
principal diferencial competitivo. Este documento apresenta uma estrutura estratégica para a
implementação do Salesforce Automotive Cloud, estruturada em torno dos princípios da
metodologia Agile para garantir que a tecnologia não apenas otimize os processos, mas
também gere valor comercial tangível e mensurável.

Definindo épicos no contexto do Salesforce

No léxico da gestão ágil de projetos, umaÉpica representa uma grande iniciativa empresarial
ou um conjunto significativo de trabalho que não pode ser concluído em um único sprint de
desenvolvimento.1Ele serve como um contêiner de alto nível para um conjunto de
funcionalidades relacionadas que, juntas, alcançam um objetivo estratégico fundamental. No
contexto de uma implementação do Salesforce, um Épico traduz uma necessidade de negócio
em um resultado tangível dentro da plataforma. Por exemplo, em vez de um requisito vago
como "melhorar as vendas", um Épico bem definido seria "Implementar uma visão de 360° do
motorista e do veículo para personalizar as interações de vendas e serviços".

Os épicos são essenciais por vários motivos:

●Organização Hierárquica:Eles permitem que você estruture seu backlog de produtos,
dividindo grandes projetos em componentes gerenciáveis   que podem ser priorizados
e planejados ao longo de vários trimestres.1

●Alinhamento estratégico:Eles conectam o trabalho diário da equipe de desenvolvimento

aos objetivos mais amplos da organização, garantindo que cada recurso criado contribua
para um objetivo comercial maior.5

●Comunicação com as partes interessadas:Eles servem como a unidade de valor

comunicada aos líderes empresariais. Enquanto as equipes de desenvolvimento se
concentram em tarefas menores, a gerência pode acompanhar o progresso no nível Épico,
que representa marcos significativos do projeto.2

Definição de Casos de Uso (Histórias de Usuário)

Se um Épico é o "o quê" estratégico, oCasos de uso, comumente expressa comoHistórias
de usuáriosNo Agile, esses são os táticos "quem", "o quê" e "por quê". São descrições
curtas e simples de um recurso da perspectiva da pessoa que o deseja.6A estrutura padrão
para uma história de usuário é:

"Como um[tipo de usuário], quero [executar uma ação]para que [pode
atingir um objetivo]".

Essa estrutura é deliberadamente simples, mas poderosa. Ela força a equipe a se concentrar
no usuário final, seja um cliente, um vendedor de concessionária, um agente de serviço ou um
gerente de marketing. Ela divide a complexidade de um Épico em requisitos específicos e
acionáveis   que podem ser desenvolvidos, testados e entregues em um único sprint.8Por
exemplo, o épico "Implementar uma visão de 360° do motorista" pode ser dividido nos
seguintes casos de uso:

●"Como vendedorQuero ver o histórico de serviços do veículo de um cliente.para poder

recomendar proativamente um plano de manutenção durante uma conversa de vendas."

●"Como agente de serviço, Quero ver todos os veículos associados a uma famíliapara

poder oferecer um desconto em vários serviços."

A Hierarquia do Trabalho (Iniciativa > Épico > Caso de Uso)

Para um planejamento estratégico completo, é útil visualizar a hierarquia do
trabalho.Iniciativas São objetivos de negócios mais amplos, geralmente anuais ou
plurianuais, que agrupam vários Épicos. Por exemplo, uma Iniciativa pode ser "Aumentar a
Fidelidade do Cliente em 15%". Essa Iniciativa seria dividida em vários Épicos, como "Criar
uma Visão de 360   Graus da Fidelidade do Cliente".
Experiência do motorista", "Lançar um programa de manutenção preditiva" e "Otimizar a

experiência de serviço omnicanal". Cada um desses épicos, por sua vez, é dividido em
dezenas de casos de uso específicos que orientam o trabalho da equipe de
desenvolvimento.2Essa abordagem estruturada garante que cada linha de código escrita
esteja diretamente vinculada a um resultado comercial mensurável.

A análise da indústria automotiva revela uma transição crítica. As abordagens tradicionais,
frequentemente refletidas em questionários de escopo técnico, concentram-se na eficiência
dos processos internos, como a criação de ativos ou os fluxos de trabalho de aprovação.10No
entanto, pesquisas de mercado atuais e histórias de sucesso demonstram que o verdadeiro
diferencial competitivo não é mais apenas a eficiência operacional, mas sim a criação de uma
experiência do cliente (CX) omnicanal, personalizada e integrada.11

Essa mudança de perspectiva é fundamental para definir efetivamente os Épicos. Um
processo interno ineficiente, como o agendamento manual de consultas, não é apenas uma
questão de custo; é a causa raiz de uma experiência fragmentada do cliente. Portanto, um
Épico não deve ser simplesmente "Automatizar o Agendamento de Consultas". Um Épico
estratégico seria definido como "Elevar a Experiência do Cliente por meio do Agendamento de
Consultas Omnicanal e Sem Atrito". Essa reorientação altera a métrica de sucesso do projeto:
ela não é medida apenas pela redução dos tempos de ciclo interno, mas pelo impacto no Net
Promoter Score (NPS), na retenção de clientes e no Customer Lifetime Value. Isso alinha a
implementação da tecnologia diretamente com a geração de receita e a fidelidade a longo
prazo, que são os verdadeiros impulsionadores do crescimento sustentável na indústria
automotiva moderna.

Seção 2: O ecossistema do cliente automotivo:
uma jornada omnicanal

A jornada do cliente na indústria automotiva moderna é uma rede complexa de interações
digitais e físicas. Uma estratégia de CRM bem-sucedida deve orquestrar essa jornada de
forma integrada, eliminando o atrito entre canais e usando dados para personalizar cada
ponto de contato.

2.1. Aquisição e Compromisso Inicial

Esta fase inicial é fundamental para captar o interesse do cliente e orientá-lo para uma
interação.

tangível com a marca. A eficácia nesta fase depende da capacidade de gerenciar clientes
em potencial de forma centralizada e oferecer ferramentas intuitivas de autoatendimento.

Gestão de Leads e Oportunidades

A captura de leads ocorre por meio de uma infinidade de canais: formulários da web, mídias
sociais, eventos do setor e até mesmo visitas a concessionárias.11Um sistema de CRM
robusto deve consolidar esses leads em uma única plataforma para qualificação,
enriquecimento e roteamento inteligente. O Automotive Cloud aprimora o gerenciamento
padrão de leads do Salesforce, permitindo a captura de detalhes específicos do setor, como o
veículo de interesse, o tipo de transação (compra ou troca) e a concessionária preferida do
cliente.15Esse nível de detalhe, capturado desde o início, é transferido perfeitamente para o
estágio de oportunidade, fornecendo à equipe de vendas um contexto valioso para um
envolvimento mais personalizado.

Agendamento de test drive

O test drive continua sendo um marco crucial no processo de compra. Oferecer um sistema de
agendamento omnicanal é fundamental. Os clientes esperam poder agendar um test drive
online com a mesma facilidade com que reservam uma mesa em um restaurante.16Ao mesmo
tempo, os agentes do contact center e os vendedores das concessionárias precisam de uma
ferramenta unificada para gerenciar a disponibilidade de veículos de demonstração, coordenar
agendas e confirmar compromissos.10A implementação de um agendador de compromissos
integrado reduz o atrito, melhora a experiência do cliente e otimiza a utilização dos ativos da
concessionária.

Gestão de Formulários e Documentação Inicial

Antes que um cliente possa fazer um test drive, muitas vezes são necessárias documentações
como verificação da carteira de motorista, assinatura de formulários de consentimento e
isenções de responsabilidade. Gerenciar esses documentos manualmente é ineficiente e
propenso a erros. Digitalizar esse processo, permitindo que os clientes preencham e assinem
formulários eletronicamente antes da chegada, não só agiliza a experiência na concessionária,
como também garante a conformidade e reduz a sobrecarga.

administrativa.10

 Essa dualidade exige uma estratégia omnicanal que não apenas coexista em ambos os

A jornada do consumidor automotivo moderno é inerentemente híbrida. A pesquisa começa
online, onde os consumidores comparam modelos, configuram veículos e leem avaliações, mas
a grande maioria (85%) ainda encerra sua jornada com uma visita a uma concessionária
física.13
mundos, mas também os una em uma experiência única e coerente.14Ao definir este épico, é
crucial considerar os vários pontos de contato envolvidos na criação de um test drive, desde o
site do OEM até uma ligação para o contact center ou uma visita direta à
concessionária.10Implementar um agendador centralizado é essencial para gerenciar a
disponibilidade e evitar conflitos.10Além disso, o processo deve incluir a captura sistemática de
verificação de identidade e a geração de formulários de isenção de responsabilidade,
idealmente digitalmente, para agilizar a experiência da concessionária.10Quando um cliente
investe tempo configurando seu veículo ideal online, essas informações se tornam um ativo
valioso. Ao chegar à concessionária, ele espera que o vendedor esteja familiarizado com suas
preferências. Pedir que ele repita informações cria atritos desnecessários. Para evitar essa
desconexão, é fundamental estabelecer um "Tópico Digital Unificado de Clientes". Esse épico
fundamental requer uma integração robusta entre a plataforma de CRM e os sistemas de
gestão da concessionária (DMS). A execução dessa visão depende de uma arquitetura de
integração sólida, muitas vezes facilitada por plataformas como a MuleSoft, que conectam
sistemas distintos por meio de APIs.21

2.2. Transação e Venda de Veículos

A fase de transação é o momento da verdade, onde a confiança e a transparência são
primordiais. Um processo de cotação e contratação eficiente e sem erros é crucial para fechar
a venda e estabelecer as bases para um relacionamento de longo prazo.

Configuração, Preço e Cotação (CPQ)

As configurações de veículos modernos podem ser extraordinariamente complexas, com uma
infinidade de modelos, pacotes, opcionais e acessórios. Um sistema de Configuração, Preço e
Cotação (CPQ) orienta os fornecedores nessa complexidade, aplicando regras de negócios
para garantir que apenas configurações válidas sejam criadas. A integração com sistemas
ERP é vital.
para obter preços em tempo real e verificar a disponibilidade do estoque, garantindo que as
cotações sejam sempre precisas.23Configuradores visuais, que permitem aos usuários

Clientes e vendedores que veem uma representação 2D ou 3D do veículo personalizado
melhoram significativamente a experiência de compra e aumentam a confiança do cliente.

Comparação de cotações

Os compradores de hoje são altamente informados e usam ferramentas on-line para comparar
preços e ofertas de diversas concessionárias e marcas.24Em vez de ver isso como uma
ameaça, vendedores equipados com um CRM poderoso podem usar essas informações a seu
favor. A capacidade de gerar e apresentar comparações claras de diferentes modelos, opções
de financiamento ou até mesmo ofertas da concorrência posiciona o vendedor como um
consultor confiável, ajudando o cliente a tomar uma decisão informada e justificando a proposta
de valor da concessionária.

Contrato de Venda de Veículos (VSA)

O Contrato de Venda de Veículo (VSA) é o documento culminante do processo de compra. No
entanto, sua complexidade frequentemente o torna uma fonte de ansiedade e desconfiança
para o cliente, com preocupações sobre taxas ocultas, termos de empréstimo incorretos ou
complementos não solicitados.27Automatizar a geração de VSA diretamente do CRM mitiga
esses riscos. Ao utilizar a cotação finalizada como única fonte de verdade, o sistema pode
gerar automaticamente um contrato pré-preenchido com dados precisos do cliente e do veículo,
preços acordados e condições de financiamento. Isso minimiza drasticamente o erro humano.
Além disso, a implementação de fluxos de trabalho de aprovação digital para descontos ou
condições especiais garante a conformidade com as políticas da concessionária e cria uma
trilha de auditoria clara.10

O contrato de compra e venda não deve ser um obstáculo final, mas sim o culminar tranquilo
de uma relação de confiança. A fase de contratação costuma ser o ponto de maior atrito, onde
a falta de transparência pode corroer a reputação acumulada.27A solução está em posicionar o
CRM como a fonte incontestável da verdade. Ao projetar este Épico, é essencial analisar a
complexidade do processo atual: quantos tipos de contratos de venda existem? Eles são
gerados sistematicamente ou manualmente? Quais outros documentos são produzidos durante
esse processo (financiamento, seguro, registro)?10A estratégia deve abordar a gestão de
alterações e cancelamentos, bem como a necessidade de fluxos formais de aprovação para
descontos ou condições especiais.10Ao integrar um sistema CPQ com uma ferramenta de
geração de documentos, a Epic se transforma de uma simples
"Gerenciamento de Contratos de Vendas" para uma abordagem mais estratégica: "Garantir

uma transição transparente e sem erros da cotação para o contrato". Essa abordagem muda a
natureza dos casos de uso, que agora se concentram na validação e na confiança, como
implementar um fluxo de aprovação automatizado acionado para qualquer desconto que
exceda um limite predefinido ou permitir que o cliente receba uma versão digital do contrato
para pré-análise.

2.3. Ciclo de vida do proprietário e do veículo

O relacionamento com o cliente não termina com a venda; na verdade, é apenas o começo. A
fase de propriedade é onde a fidelidade é construída e fluxos de receita recorrentes são
gerados por meio de serviços, garantias e compras futuras.

Gestão de Ativos e Veículos

Cada veículo vendido se torna um ativo que deve ser gerenciado durante todo o seu ciclo de
vida.30É essencial manter um registro mestre (Asset Master) para cada veículo, contendo não
apenas suas especificações técnicas (VIN, modelo, recursos), mas também seu histórico
completo: proprietários anteriores, registros de serviço, reparos em garantia e dados de
telemetria.10Essa visão de 360   graus do ativo é a base para um serviço personalizado e
proativo.

Agendamento de serviços

O agendamento de serviços é uma interação recorrente e uma oportunidade fundamental
para fortalecer o relacionamento com os clientes. O processo é mais complexo do que
agendar um test drive, pois envolve a coordenação da disponibilidade de técnicos com
habilidades específicas, baias de serviço, ferramentas especializadas e estoque de
peças.32E
Um sistema de agendamento inteligente, integrado ao CRM, pode automatizar essa
complexidade, oferecendo aos clientes opções de autoatendimento on-line e, ao mesmo
tempo, otimizando a utilização dos recursos da loja.34
Gestão de Garantias e Reclamações

A gestão de garantias é um processo crítico que impacta diretamente a satisfação do cliente e
os resultados financeiros tanto da concessionária quanto da montadora. Um fluxo de trabalho
de gestão de sinistros bem definido dentro do CRM pode agilizar todo o processo, desde a
notificação inicial de sinistro (FNOL) até a autorização de reparo, pedido de peças, execução
do serviço e solicitação de reembolso ao fabricante.35A automação e a transparência nesse
processo reduzem atrasos, melhoram a comunicação com o cliente e garantem um controle de
custos eficaz.37

Gerenciamento de Dados de Telemetria e Veículos Conectados

A proliferação de veículos conectados está gerando um volume de dados sem precedentes. A
telemetria em tempo real sobre o desempenho do veículo, o comportamento do motorista e os
códigos de diagnóstico de problemas (DTCs) abre as portas para uma nova era de serviços
proativos.39O Automotive Cloud foi projetado para ingerir e orquestrar esses eventos
telemáticos, permitindo ações como manutenção preditiva, alertas de serviço automatizados e
até mesmo funções remotas, como travamento e destravamento de portas.39

 O processo começa quando um

A transição da manutenção reativa para a preditiva representa uma mudança de paradigma.
Não se trata mais de esperar que o cliente relate um problema, mas sim de antecipá-lo. Para
isso, é crucial definir onde o registro mestre do veículo ficará e qual nível de detalhe será
capturado, incluindo recursos, opções e uma possível hierarquia de ativos para componentes
principais e secundários.10O recurso "Orquestração de eventos acionáveis" do Salesforce
Automotive Cloud está impulsionando essa transformação.39
veículo conectado gera um evento telemático, como um código de diagnóstico. Em um modelo
proativo, esse evento aciona um épico de "Orquestração Proativa de Serviços". O sistema não
apenas registra os dados, mas também atua sobre eles: criando automaticamente um caso de
serviço, identificando o proprietário, verificando a garantia e localizando a concessionária mais
próxima com as peças necessárias e a disponibilidade. O resultado é um Caso de Uso que
redefine a experiência do cliente: "Como proprietário de um veículo, quero receber uma
notificação proativa no meu aplicativo móvel sobre um possível problema, juntamente com um
link para agendar um serviço com um clique." No nível estratégico, os dados agregados de
falhas podem ser repassados   aos departamentos de engenharia e qualidade, conectando o
CRM ao Gerenciamento do Ciclo de Vida do Produto (PLM) e criando um ciclo de melhoria
contínua.43
2.4. Gestão de Relacionamento e Fidelização

fidelidade  de

Construir
requer  uma  compreensão  profunda  dos
relacionamentos  com  os  clientes  e  a  capacidade  de  fornecer um serviço consistente e
contextual em todos os pontos de contato.

longo  prazo

Gestão de Partes Interessadas e Familiares

A propriedade e o uso de veículos raramente se limitam a um único indivíduo. As decisões de
compra e manutenção geralmente envolvem uma unidade familiar ou "família".44Um CRM
avançado deve ser capaz de modelar essas relações complexas: uma família pode ter vários
veículos, motoristas com necessidades diferentes (por exemplo, pais e um motorista
adolescente) e diferentes pessoas responsáveis   por decisões financeiras e de manutenção. A
gestão no nível familiar permite uma visão holística, abrindo oportunidades para campanhas
de marketing direcionadas (por exemplo, ofertas de seguro para novos motoristas) e
propostas de vendas personalizadas (por exemplo, um pacote de troca para vários
veículos).10

Console de serviço omnicanal

Para oferecer um serviço excepcional, os agentes precisam ter uma visão completa de
cada cliente. Um painel de atendimento omnicanal unifica todas as interações,
independentemente do canal — chamadas telefônicas, e-mails, chat ao vivo, mídias
sociais ou visitas presenciais — em uma única interface.14Isso fornece ao agente contexto
completo sobre o histórico do cliente, veículos, casos de serviço anteriores e preferências,
permitindo que ele resolva problemas de forma mais rápida e eficiente, sem exigir que o
cliente repita sua história.10

A unidade econômica fundamental na indústria automotiva nem sempre é o indivíduo, mas
sim a família. Reconhecer isso é fundamental para gerar valor significativo.44A capacidade do
Salesforce de modelar "famílias" é um recurso estratégico que nos permite passar de uma
visão transacional para uma relacional.10Ao projetar esta capacidade, é crucial definir os tipos
de relacionamentos existentes (por exemplo, cônjuge, filho, condutor principal) e estabelecer
processos claros sobre como essas famílias serão mantidas, fundidas ou divididas conforme
as circunstâncias familiares mudarem.10O épico que emerge dessa capacidade é "Maximizar o
Valor do Ciclo de Vida Doméstico". Essa perspectiva muda a forma como as vendas e o
marketing são abordados. Os casos de uso se tornam mais sofisticados: um gerente de

marketing pode criar um segmento de "domicílios com um motorista adolescente
recém-habilitado" para uma campanha conjunta de segurança e seguros. Um vendedor, ao
perceber que o aluguel de um sedã familiar está prestes a expirar, pode propor proativamente
um pacote de troca que inclui um SUV maior e um veículo elétrico menor. Essa gestão em
nível domiciliar transforma as interações de vendas de eventos únicos em uma gestão
contínua de portfólio de longo prazo.

Seção 3: Capacidades operacionais e
fundamentais

Para que os processos de atendimento ao cliente funcionem sem problemas, eles devem
ser sustentados por uma base operacional sólida. A gestão centralizada do catálogo de
produtos e das estruturas de preços é fundamental para a consistência e a eficiência em
toda a organização.

3.1. Catálogo de produtos e gerenciamento de preços

Produtos e preços precisos são a base da confiança do cliente e da lucratividade do
negócio.

Gestão de Produtos

O catálogo de produtos de uma empresa automotiva é vasto e complexo, abrangendo não
apenas veículos, mas também peças, acessórios, planos de serviço, garantias estendidas e
produtos financeiros. Um sistema centralizado de gestão de produtos é essencial para manter
a consistência das informações em toda a empresa. Isso inclui a definição de hierarquias e
categorias de produtos que facilitam a busca, a configuração e a análise de vendas.10A gestão
eficaz do catálogo garante que tanto os vendedores como os clientes
os clientes têm acesso a informações precisas e atualizadas sobre os produtos.

Gestão de Preços

A precificação no setor automotivo é dinâmica e multifacetada. Uma única lista de preços é
insuficiente para uma montadora global ou um grande grupo de concessionárias. Múltiplas
listas de preços (Price Books) são necessárias para gerenciar as variações por região
geográfica.
moeda,  tipo  de  cliente  (por  exemplo,  preços  de  varejo  vs.  preços  de  frota  corporativa)  e
campanhas  promocionais.10Um  sistema  de  CRM  deve permitir a criação e o gerenciamento
flexíveis dessas listas de preços, garantindo que o preço correto seja aplicado a cada cotação
automaticamente, reduzindo erros e garantindo a consistência.
os preços.52

A aparente simplicidade das perguntas em um questionário de escopo, como "Lista de preços
em uma única moeda ou em várias moedas?" ou "Uma única moeda ou em várias moedas?",
mascara uma profunda complexidade estratégica.10Para uma empresa automotiva que opera
em larga escala, uma única lista de preços é uma impossibilidade operacional. Flutuações
cambiais, impostos locais e pressões competitivas exigem uma estratégia de preços
localizada.10Dentro de uma única região, a segmentação de clientes exige maior granularidade.
Os preços para um cliente de frota corporativa serão diferentes dos preços de tabela para um
comprador individual. Além disso, o ciclo de vendas é impulsionado por promoções que exigem
estruturas de preços temporárias. Portanto, a capacidade de gerenciar múltiplas listas de
preços não é um mero recurso técnico; é o facilitador de uma estratégia comercial ágil. O épico
subjacente é "Habilitar uma Estratégia de Preços Dinâmica e Localizada". Essa visão dá origem
a casos de uso de alto valor. Um gerente de produto precisa ser capaz de criar uma lista de
preços específica para uma "Campanha de Vendas de Verão". Da mesma forma, um
administrador de vendas deve ser capaz de atribuir uma lista de preços de "Frota Corporativa"
a uma conta-chave, garantindo que qualquer vendedor utilize automaticamente os preços
pré-negociados, garantindo consistência e conformidade em toda a organização.10

Seção 4: Catálogo exaustivo de épicos e casos de
uso para nuvem automotiva

A tabela a seguir consolida a pesquisa e a análise estratégica em um catálogo
Uma estrutura abrangente de Épicos e Casos de Uso projetada para servir como um
acelerador para o planejamento, escopo e implementação do Salesforce Automotive Cloud.
A estrutura é baseada nos Domínios e Capacidades identificados, fornecendo uma ponte
direta entre as capacidades da plataforma e os resultados comerciais desejados.

Título da tabela:Catálogo de casos de uso e épicos do Salesforce Automotive Cloud

Nuvem

Nome de
domínio

Capacidade
Nome

Épica
(resumo)

Caso de uso
(resumo)

Automotivo
Nuvem

Automotivo
Nuvem

Vendas de
veículos
Acordo -
Automotivo
Nuvem

Garantindo
uma
transição
transparente
e sem erros
a cotação do
contrato
através do
automação,
padronizaçã
e
o
gerenciamen
to  do  ciclo
de vida
completo de
os acordos
à venda
veículos
(VSA).

Como
gerente de
vendas,
Quero  gerar
automaticam
ente
um
VSA
pré-preenchid
o
com os dados
a
validado
partir
da
cotação  final
para
minimizar
erros
manuais e
acelerar o
processo de
fechamento.10

Como cliente,
Eu quero
receber
uma versão
VSA digital
para revisão
diante de mim
nomeação no
revendedor,
para
garantir o
transparênc
ia e reduzir
a
tempo de

espere.27

Como
gerente
financeiro,
Quero um
fluxo de
aprovação
automatizad
o que seja
acionado
quando um
VSA inclui
um
desconto não
padrão, para
garantir a
conformidade
de políticas
de
margem.10

Como
especialista
em
conformidad
e, eu quero
gerenciar e
arquivo
digitalmente
todos os
documentos
associado a
um VSA
(financiame
nto,
seguros,
registro) em
um só lugar
para facilitar
o
auditorias.29

Como
vendedor,
Eu quero
começar
um
processo de
emenda em
um VSA

existente
para refletir
mudanças
solicitado
pelo cliente
(por
exemplo,
adicionar um
acessório) e
aquilo é
atualizar o
preço total
automática
me nte.10

Como
gerente de
operações,
Quero
analisar os
dados de
Cancelament
o do VSA
para
identificar
padrões ou
pescoços de
garrafa no
processo de
oferta.10

Automotivo
Nuvem

Automotivo
Nuvem

Veículo &
Ativo
Gestão -
Automotivo
Nuvem

Criar e
manter um
fonte única
realmente
para cada
veículo
e ativo,
rastreando seu

vida útil
completo,
do
fabricação
até o fim de
sua vida
útil,
para melhorar

o serviço
proativo e o
gestão de
relações.

Como gestor
de frota,
quero ver um
histórico
completo de
serviço e
manutenção
para cada
veículo na
minha frota
para
planejar o
manutenção
preventiva e
otimizar o
tempo de

atividade.31

Como agente
de plantão,
Quero
acessar os
detalhes
técnicos
completos de
um veículo
(recursos,
opções,
história de
garantia) para
de seu
VIN para
diagnosticar
problemas
com
precisão.10

Como
administrad
or de
sistemas,
Quero definir
e gerenciar o
diferentes
estágios do
vida útil
de um
veículo (em
trânsito, em
estoque,
vendido,
fora de
serviço)
para um
seguir
preciso do
estado do
ativos.30

Como analista

de dados,
quero
visualizar o
hierarquia de
ativos de um
veículo,
do
chassis até
o
componentes
individual,
para realizar
análise de
falhas e do
cadeia de
fornecer.10

Como
planejador
de serviços,
Quero
integrar a
gestão de
ativos com o
agendamen
to de
consultas
para
garantir que
as citações de
serviço é
link para o
registro
correto do
veículo.10

Como cliente,
quero
agendar um
teste
manuseio em
linha
selecionand
o um
veículo,
concessionári
a

Automotivo
Nuvem

Automotivo
Nuvem

Test Drive &
Serviço
Compromis
sos -
Automotivo
Nuvem

Levante o
experiência
do cliente e
eficiência
operacional
através do
unificação e
automação
do

agendamen
to de
consultas
para
testes de
manuseio e
serviços em
todos os
canais.

e cronograma
disponível
para um
experiência
de
autoatendim
ento
conveniente.16

um
em

Como agente
de um centro
contato,
quero
agendar  um
atendimento
para
cliente
seu nome,
vendo seu
história de
serviço e o
disponibilida
de de
oficina em
em tempo real,
para
através de um
console
unificada.34

Como
gerente de
serviço,
Eu quero
receber
um alerta
quando um
cotação alta
valor (por
exemplo, um
reparar
principal) é
cancela, para
pode
contato
proativamen
te e para o
cliente e
remarcar.11

Como cliente,
Eu quero
receber
lembretes
automáticos
por SMS e
correo
e-mail 24
horas antes
da minha
consulta
serviço para
evitar
esquecimento.
33

Como
recepcionista
do
revendedor,
eu quero
gerenciar um
processo de
check-in
digital para
testes
manuseio,
incluindo o
verificação
de licença
dirigir e o
a assinatura
de um
forma de
exención
digital.10

Automotivo
Nuvem

Automotivo
Nuvem

Parte
interessada
(Doméstico)
Gestão -
Automotivo
Nuvem

Como
vendedor,
Eu quero ver
todos os
veículos
propriedade
de
uma casa e
suas datas
de
expiração de

leasing  para
propor
proativament
e um pacote
de troca de
vários
veículos.10

Maximizar o
valor do ciclo
da vida do
cliente
através do
modelagem
e gestão do
unidade do
"lar",

entendimento
os complexos
relacionament
os
entre
indivíduos,
veículos e
roles para
impulsionar
vendas e
serviços
personalizad
os .

Como
gerente de
marketing,
Eu quero criar
um segmento
público
de "casas
com um novo
maestro
adolescente"
para um
campanha de
marketing
sobre
veículos
seguro e
opções de
seguro.11

Como agente
de plantão,
quero
identificar o
diretor
responsável
da tomada de
decisões
questões
financeiras
em
casa
para discutir

custos de
um reparo
importante.45

Como
gerente de
dados,
Eu quero ter
a
capacidade
de
fundir dois
registros de
casa quando
dois clientes
se casam ou
dividem uma
casa em
caso de
separação,
mantendo
integridade
do
história de
veículos e
serviços.10

Como
planejador
financeiro,
quero
ver o
relacionament
os
entre os
membros de
uma casa
(cônjuge,
crianças,
dependente
s) e seus
bens
(veículos,
políticas) para
oferecer um
aconselham

Automotivo
Nuvem

Automotivo
Nuvem

Serviço
Gestão -
Automotivo
Nuvem

Transformar
o centro de
serviço em
um motor
lealdade do
cliente
fornecer  aos
agentes  um
console
omnicanal
unificado e
ferramentas
de IA para
oferecer um
médio
rápido,
contextualiz
ado e
proativo.

ento
financeiro

integrante.56

Como agente
de plantão,
Eu quero um
console
único que
eu
mostrar o
história
completo do
cliente, seu
veículos,
casos
anteriores e
interações
em todos os
canais
(chamadas,
correos
eletrônica,
bate-papo)
não para
precisa
peça a ele
para
repita
Informação.10

Como cliente,
Eu quero
poder
começar um
conversa via
chat no site e
continuá-la
mais tarde
por SMS
sem perder o
contexto da
minha
consulta.12

Como
gerente do
centro
contato,
Eu quero usar

IA para
analisar o
transcrições
do
chamadas e
detectar
tendências
nos
problemas
dos clientes,
a fim de
poder
abordar o
causas
raízes de
uma forma
proativo.13

Como
agente,
quero
receber
sugestões
de
respostas e
artigos de
conhecimento
relevante em
tempo real
durante um
conversa
bate-papo
para
resolver o
problemas de
os clientes
avançar
rapidamente.58

Como
Administrad
or de TI, eu
quero
integrar
nosso
sistema de
telefonia
existente
(CTI) com
o console de
serviço para

Automotivo
Nuvem

Automotivo
Nuvem

Citar
Gestão -
Automotivo
Nuvem

habilitar o
funcionalidade
por "tela"
estouro",
mostrando
automaticam
ente  o  perfil
do
cliente
que
chamadas.10

Como
vendedor,
Eu quero usar
e
configurador
visual para
adicionar e
remover
opções
um veículo
junto com o
cliente,
vendo como
o
mudanças
afetam o
preço em
tempo real,
para
uma
experiência
de compra
interativo.23

criar

Acelere o
processo de
vendas e
melhorar o
precisão
através de um
sistema de
preço
(CPQ) que
permita
configurar
veículos
complexos,
aplicar
preços
precisos e
acionar
propostas
profissionais
rapidamente.

Como
gerente de
vendas,
Eu quero que
ele
sistema
aplique
automaticam
ente os
preços
corretos da
lista de
preços
regional e da
descontos em

a campanha
atual para
todos
citações
para
garantir o
coerência e
proteger o
margens.59

Como cliente,
Eu quero
receber
uma citação
clara e
detalhou que
permita-me
comparar
facilmente
diferentes
opções de
configuració
n o modelos
de
veículos
para levar
um
decisão
informada.24

Como
vendedor,
Quero gerar
rapidamente
uma citação
em formato
PDF com o
marca do
revendedor
e envie por
correo
eletrônico para
cliente
diretamente
do CRM

para um
seguir
eficiente.61

Como
administrad
or, quero
definir
regras de
validação
que impede
a
criação de
configuraçõe
s de veículos
incompatívei
s (por
exemplo,
um tipo de
motor
com
transmissão
incompatível
)
evitar
erros de
pedido.23

Como
gerente de
produto,
Quero definir
e gerenciar o
catálogo
completo de
modelos de
veículos,
incluindo
suas
especificaçõ
es, pacotes
de opções e
hierarquias
de
produtos,
em um
único

Estabelecer e
manter um
catálogo de
produtos
centralizado
e
estruturado
como a
única fonte
de
verdade para
todos os
veículos,
partes,
serviços e
acessórios,
habilitando
processos de
venda e

Automotivo
Nuvem

Automotivo
Nuvem

Produto
Gestão -
Automotivo
Nuvem

serviço
consistentes

sistema
central.43

ao longo do
organização.

Como
gerente de
preços,
Quero criar
e manter
várias listas
de preços
(Livros de
Preços)
para
diferentes
regiões,
moedas e
segmentos
de  clientes
(retail,  flota)
para
garantir uma
fixação de
preços
preciso e
estratégico.10

Como
analista de
estoque,
quero
classificar o
produtos em
categorías
lógicas (por
exemplo,
motor,
suspensão,
carroceria)
para facilitar
a busca, o
gestão de
inventário e o
análise de
vendas.50

Como gerente

o marketing,
Quero
associar
produtos
com
campanhas
promoções
específicas
para que o
descontos e
as ofertas são
aplicar
automatica
mente
durante o
processo de
preço.64

Como
especialista
em dados,
eu quero
garantir que
o sistema de
gestão de
produtos
sejam a
fonte
professor
(Produto
Master)  que
sincroniza
com  outros
sistemas,
como  o  ERP
e
a plataforma
de comércio
electrónico,
para
garantir o
consistência
de dados.10

Como cliente,
quero
registrar um
reclamación
da garantia
para

Automotivo
Nuvem

Automotivo
Nuvem

Garantia e
Reivindicaçõe
s
Gerenciament
o
(Extrapolado)

Otimizar o
gestão de
garantias e
afirma
melhorar a

satisfação
do cliente,
controlar o
custos e
obter
Informação
valioso sobre
a qualidade do
produto,
automatizan
todo  o
do
ciclo  de  vida
da
reivindicação
.

através de um
portal de
autoatendim
ento e poder
rastrear  seu
status em
tempo real
ter
visibilidade do
processo.35

Como agente
de plantão,
Quero
verificar
automaticam
ente o
cobertura de
a garantia de
um veículo
com base no
seu VIN ao
criar um
pedido
reparar
para informar
para o cliente
de
imediato
sobre o
custos
abordado.36

Como
gerente de
garantia,
Eu quero um
fluxo de
trabalho
automatiza
do para o
aprovação
de
reivindicaçõ
es
que
encaminha o

pedidos para
equipamento
correto de
acordo com o
tipo de
reivindicaçã
o e o valor,
para agilizar
o
decisões.37

Como
analista de
qualidade,
Quero  gerar
relatórios
sobre o
reivindicaçõ
es de
garantia
por  modelo
tipo  de
e
veículo
componente
para
identificar
problemas
qualidade
recorrente e
comunicá-los
para a equipe
de
engenharia.35

Como
gerente de
peças,
quero
gerenciar o
logística de
devolução
de peças
defeituoso
associado
com
reivindicaçõ
es de
garantia
para o seu
análise e

Automotivo
Nuvem

Automotivo
Nuvem

Conectado
Veículo &
Telemetria
Gerenciament
o
(Extrapolado)

garantir que
os períodos
de
retenção
contratual.35

Como
proprietário
do veículo,
Eu quero
receber
um alerta
proativo em
meu aplicativo
móvel quando
telemetria
do veículo
detectar um
falha
iminente
(por
exemplo,
bateria fraca),
junto com um
opção para
agendar o
serviço de
um clique.39

Aproveite os
dados de
veículos
conectados
para mover de
um modelo de
serviço
reativo para
um proativo
e
preditivo,
criando
novas fontes
de renda e
fortalecimento
a lealdade do
cliente
através de
experiências
personalizad
as .

Como
gerente de
serviço,
Eu quero usar
os dados de
telemetria
para prever o
precisa
de
manutenção
do
veículos de
meus clientes
e
envie-os
ofertas de
serviço

personalizad
o antes
ocorre uma
cair.40

Como agente
do centro de
contato,
Eu quero
poder
executar
ações
remoto no
veículo do
cliente (para
exemplo,
desbloquear
as portas)
depois
verifique seu
identidade,
para resolver
situações de
bloqueio.39

Como
analista de
frota,
quero
monitorar o
consumo de
combustível,
hábitos de
condução e
a localização
em tempo
real de todos
veículos de
frota para
otimizar rotas
e reduzir
custos
agentes.41

Como
desenvolvedor
,
Eu quero usar
a plataforma
de
orquestração
de eventos
para criar
fluxos de
trabalho
personalizad
os que são
acionados
por eventos
telemática
específicos,
como o
creación
caixa
automática
quando é
detecta um
código de
erro do
motor.39

Seção 5: Mapa de Processos de Negócios da
Indústria Automotiva

Para implementar com sucesso o Salesforce Automotive Cloud, é fundamental mapear os
recursos da plataforma para os processos de negócios de ponta a ponta do setor. Esta seção
detalha um modelo de processo multicamadas que serve como guia para a transformação
digital, desde a aquisição inicial de clientes até a fidelização a longo prazo.

5.1 Processo de aquisição e vendas (Lead-to-Cash)
Este macroprocesso abrange todas as atividades, desde a geração de um lead até a

conclusão da venda de um veículo.

●Nível 1: Gestão de Prospectos e Oportunidades

○Nível 2: Captura de leads omnicanal:Centralize a entrada de leads de todos os

pontos de contato, incluindo formulários da web, mídias sociais, eventos e visitas a
concessionárias.11

○Nível 2: Qualificação e Roteamento de Leads:Implemente regras automatizadas

para pontuar leads e atribuí-los ao vendedor ou revendedor certo.

○Nível 2: Agendamento de teste de direção:Ofereça um portal de autoatendimento

para os clientes agendarem compromissos, gerenciados por meio de um agendador
centralizado que controla a disponibilidade de veículos e funcionários.10
Verificação de identidade e consentimento:Digitalizar a captura de

 ■Nível 3:

carteiras de motorista e assinatura de termos de responsabilidade antes da
chegada do cliente para agilizar o processo.10

○Nível 2: Convertendo um cliente potencial em uma oportunidade:Formalize o

interesse do cliente em uma oportunidade de venda, transferindo todo o contexto
coletado.●Nível 1: Configuração, Cotação e Contratação

○Nível 2: Configuração de Veículo Guiado (CPQ):Use um configurador visual para

orientar o cliente e o vendedor sobre as opções de veículos, garantindo
configurações válidas.10

○Nível 2: Geração e comparação de cotações:Crie rapidamente orçamentos
precisos e permita comparações lado a lado de diferentes configurações ou
opções de financiamento.10

○Nível 2: Geração de Contrato de Venda de Veículos (VSA):Automatize a criação do

VSA a partir da cotação final para garantir precisão e reduzir erros manuais.10

■Nível 3: Processo de aprovação de contrato:Implemente fluxos de trabalho
para aprovar descontos, preços especiais ou termos de venda.

financiamento não padronizado.10

■Nível 3: Gestão de Emendas e Cancelamentos:Estabeleça um processo

estruturado para lidar com solicitações de alteração ou cancelamentos do VSA
antes da entrega.10

○Nível 2: Assinatura Eletrônica e Gestão de Documentos:Facilite a assinatura digital
de todos os documentos de vendas e arquive-os centralmente no registro do cliente.

5.2 Processo de Próprio para Serviço

Este macroprocesso abrange a gestão de veículos e o relacionamento com o cliente após
a compra, com foco em serviço e manutenção.

●Nível 1: Gestão do ciclo de vida de ativos e proprietários

○Nível 2: Criação de ativos de veículos:No momento da venda, crie um registro

mestre para o veículo, vinculando-o ao cliente e à família e definindo as etapas do
seu ciclo de vida.10

○Nível 2: Relacionamento e Gestão Doméstica:Modele a unidade familiar, identificando
todos os motoristas, veículos e funções dentro da casa para permitir uma visão de 360
  graus.10
■Nível  3:  Manutenção  da  casa:Estabeleça  procedimentos  para  unir  ou  dividir
domicílios  conforme  as circunstâncias familiares mudam, mantendo a integridade
dos dados.10

○Nível 2: Agendamento de compromissos de serviço:Permita que os clientes

agendem compromissos de serviço em vários canais (portal, aplicativo móvel, central
de atendimento) usando um agendador inteligente.10
■Nível 3: Alocação de Recursos de Serviço:Coordene automaticamente a
disponibilidade de técnicos qualificados, baias de serviço, ferramentas
especiais e peças necessárias para o agendamento.
●Nível 1: Execução de serviços e gerenciamento de garantia

○Nível 2: Recepção e Diagnóstico de Veículos:Gerenciar o processo de check-in do

veículo na oficina e registrar os resultados do diagnóstico.

○Nível 2: Gerenciamento de ordens de reparo:Crie e gerencie ordens de serviço
detalhadas, atribuindo tarefas aos técnicos e acompanhando o progresso.
○Nível 2: Gestão de Reclamações de Garantia:Iniciar e gerenciar o processo de
solicitação de garantia, desde a verificação da cobertura até a solicitação de
reembolso do fabricante.
■Nível  3:  Processo  de  aprovação  de  garantia:Automatize  os  fluxos  de
reparos  em  garantia,  garantindo  a

trabalho  de  aprovação  para
conformidade com as políticas.

○Nível 2: Faturamento e Pagamento de Serviço:Gere faturas detalhadas dos

serviços prestados e facilite o pagamento através de vários métodos.

5.3 Processo de Fidelização e Veículo Conectado
(Serviço à Lealdade)
Este macroprocesso se concentra em fortalecer a fidelidade do cliente por meio de serviços
proativos e experiências inovadoras impulsionadas pela tecnologia de veículos conectados.

●Nível 1: Suporte ao cliente omnicanal

○Nível  2:  Gerenciamento  de  Casos  Unificado:Forneça  aos  agentes  de  serviço  um
único console para gerenciar todas as interações com o cliente (chamadas, e-mails,
bate-papo, mídias sociais) com um histórico completo.10

○Nível 2: Portal de autoatendimento e base de conhecimento:Ofereça aos clientes

um portal onde eles podem encontrar respostas para perguntas frequentes, visualizar
seu histórico de serviços e gerenciar seus veículos.

●Nível 1: Orquestração de serviços proativos e conectados

○Nível 2: Ingestão e processamento de dados de telemetria:Capture dados em tempo
real de veículos conectados, como códigos de diagnóstico de problemas (DTCs) e

dados de desempenho.39

○Nível 2: Manutenção preditiva baseada em eventos:Configure fluxos de trabalho

que são acionados automaticamente por eventos telemáticos específicos.■Nível 3:
Criação automática de casos de serviço:Quando um DTC for detectado, crie um
caso de serviço proativo e atribua-o ao revendedor preferido do cliente.
■Nível 3: Notificação proativa ao cliente:Envie um alerta ao cliente por meio do

canal de sua preferência (aplicativo móvel, SMS) informando-o sobre o possível
problema e oferecendo o agendamento de uma consulta com um clique.39

○Nível 2: Execução de Ações Remotas:Permita que os agentes do contact center,
com a devida verificação, realizem ações remotas no veículo, como destravar as
portas ou buzinar, para auxiliar os clientes.39

Seção 6: Diagramas de Processos de Negócios
(Código da Sereia)

Abaixo está o código no formato Mermaid para gerar os fluxogramas de processos de
negócios detalhados na seção anterior. Este código pode ser usado em qualquer editor
compatível com Mermaid para visualizar a hierarquia e a sequência de processos.

6.1 Código para o Processo de Aquisição e Vendas (Lead-to-Cash)

Trecho de código

gráfico TD

subgráfico Processo L1: Lead-to-Cash

A[Aquisição e Venda]

fim

Processos L2 do subgrafo

B1[Gestão de Prospecção e Oportunidades]
B2[Configuração, Cotação e Contratação] fim

subgráfico L3 Processos - Gestão de
Prospectos C1 [Captura de leads omnicanal]
C2[Qualificação e Roteamento de Leads]

C3[Agendamento de Teste de Direção]

C4[Convertendo um Lead em uma Oportunidade]
fim

subgrafo L3 Processos - Contratação

D1[Configuração de Veículo Guiado (CPQ)]
D2[Geração e Comparação de Cotações] D3
D4

fim

subgrafo L4 Processos

E1[Verificação de Identidade e Consentimento]

F1[Processo de Aprovação de Contrato]
F2[Gestão de Alterações e Cancelamentos] fim

A --> B1
A --> B2

B1 --> C1
B1 --> C2
B1 --> C3
B1 --> C4
B2 --> D1
B2 --> D2
B2 --> D3
B2 --> D4

C3 --> E1
D3 --> F1
D3 --> F2

estilo A preenchimento:#00a1e0,traço:#333,largura do traço:2px,cor:#fff
estilo B1 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff
estilo B2 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff

6.2 Código para o Processo de Próprio para Serviço

Trecho de código

gráfico TD

subgrafo Processo L1: Próprio para Serviço

UM

fim

Processos L2 do subgrafo

B1 [Gestão do Ciclo de Vida de Ativos e Proprietários]
B2

fim

subgrafo L3 Processos - Ciclo de Vida
C1[Criação de Ativos de Veículos]
C2
C3

fim

subgrafo L3 Processos - Execução de Serviço

D1
D2
D3
D4

fim

subgrafo L4 Processos

E1[Manutenção Doméstica]
F1
G1[Processo de Aprovação de Garantia]

fim

A --> B1
A --> B2

B1 --> C1
B1 --> C2
B1 --> C3

B2 --> D1
B2 --> D2
B2 --> D3
B2 --> D4

C2 --> E1
C3 --> F1
D3 --> G1

estilo A preenchimento:#00a1e0,traço:#333,largura do traço:2px,cor:#fff
estilo B1 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff
estilo B2 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff

6.3 Código para o Processo de Fidelidade e Veículo Conectado
(Service-to-Loyalty)

Trecho de código

gráfico TD

subgrafo Processo L1: Serviço para Lealdade

A[Fidelidade e Veículo Conectado]

fim

Processos L2 do subgrafo

B1
B2

fim

Processos subgraph L3 - Suporte Omnicanal
C1[Gerenciamento Unificado de Casos]
C2

fim

subgrafo L3 Processos - Serviços Conectados

D1
D2
D3

fim

subgrafo L4 Processos

E1
E2[Notificação proativa ao cliente]

fim

A --> B1
A --> B2

B1 --> C1
B1 --> C2

B2 --> D1
B2 --> D2
B2 --> D3

D2 --> E1
D2 --> E2

estilo A preenchimento:#00a1e0,traço:#333,largura do
traço:2px,cor:#fff estilo B1
preenchimento:#00b5e2,traço:#333,largura do
traço:2px,cor:#fff estilo B2
preenchimento:#00b5e2,traço:#333,largura do
traço:2px,cor:#fff

Obras citadas

1.Épicos no desenvolvimento de software: benefícios e como criá-los. - 1 Rocket

Digital Labs, acessado em 25 de setembro de 2025,
https://1rocket.mx/epicas-en-desarrollo-de-software/

2.Epics, historias, temas e iniciativas - Atlassian, accessed September 25, 2025,
https://www.atlassian.com/es/agile/project-management/epics-stories-themes
3.Um guia para épicos ágeis (com exemplos) - Wrike, acessado em 25 de
setembro de 2025,https://www.wrike.com/agile-guide/agile-epics-guide/
4.Dominando épicos em gerenciamento ágil de projetos: uma abordagem estruturada
para entregar resultados de negócios - Dharma Consulting, acessado em 25 de
setembro de 2025,
https://dharmacon.net/2023/07/14/dominando-las-epicas-en-la-gestion-de-proy

Eletrônica ágil: uma abordagem estruturada para a entrega de resultados de
negócios 5.A Arte dos Épicos Ágeis: Criando, Rastreando e Medindo a Intenção
Correta, acessado em 25 de setembro de 2025,

https://clickup.com/es-ES/blog/25207/epics-agiles

6.Sobre Épicas e Historias de Usuarios | by Codeicus - Medium, accessed

September 25, 2025,
https://codeicussoftware.medium.com/sobre-%C3%A9picas-e-historias-de-usua
rios-9f8ff42a3e3d

7.Histórias de Usuário | Exemplos e Modelo - Atlassian, acessado em 25 de

setembro de 2025,https://www.atlassian.com/agile/project-management/user-stories
8.Épicos e histórias de usuários em projetos ágeis - QALovers, acessado em 25 de
setembro de 2025,

http://www.qalovers.com/2018/04/epicas-e-historias-de-usuario-en.html
9.Agile explicado: Parte 4 — Compreendendo épicos, recursos e histórias de
usuários - Medium, acessado em 25 de setembro de 2025,

https://medium.com/@mail2mhossain/explicado-agile-parte-4-entendendo-epi
recursos-cs-e-histórias-de-usuários-6696611af73c

10.Perguntas de Escopo Guiadas.pdf
11.CRM automotivo: o guia para escolher o melhor - HubSpot, acessado em 25 de

setembro de 2025,https://www.hubspot.es/products/crm/automotive

12.Transformando a experiência do cliente na indústria automotiva - T-Systems,

acessado em 25 de setembro de 2025,
https://www.t-systems.com/mx/es/industries/automotive/topics/automotive-cust
experiência ômer

13.Experiência do cliente automotivo (CX): chaves para transformar o setor de

concessionárias - cxgenies, acessado em 25 de setembro de 2025,
https://cxgenies.com/blog/experiencia-del-cliente-cx-automotriz-claves-para-tra
nsform-a-indústria-de-concessionárias/

14.Omnichannel, uma aposta segura para as concessionárias - Faconauto,

acessado em 25 de setembro de 2025,
https://www.faconauto.com/noticias-automocion/la-omnicanalidad-una-apuesta
-seguro-para-revendedores/

15.Gerencie candidatos e oportunidades com o Automotive Cloud - Ajuda do

Salesforce, acessado em 25 de setembro de 2025,
https://help.salesforce.com/s/articleView?id=sf.auto_manage_leads_and_opportu
nities.htm&language=es&type=5

16.Casos de uso automotivo - Impulse, acessado em 25 de setembro

de 2025,https://impulse.lat/casos-de-uso/automotriz

17.Software de agendamento de carro gratuito - Setmore, acessado em 25 de
setembro de 2025,https://www.setmore.com/es/industries/automotive
18.Clases en Espanol - Epic Driving School, acessado em 25 de setembro

de 2025,https://www.epicct.com/espanhol

19.Formularios - Departamento de Segurança Rodoviária e Veículos Motorizados
da Flórida, acessado em 25 de setembro de
2025,https://www.flhsmv.gov/resources/forms-es/ 20.Lista de verificação do teste
de direção - Coletor de impostos do Condado de Pinellas, acessado em 25 de
setembro de 2025,

https://pinellastaxcollector.gov/pdfs/Road_Test_Checklist_Spanish.pdf
21.Melhor CRM de nuvem automotiva da Salesforce, acessado em 25 de
setembro de 2025,https://www.salesforce.com/automotive/cloud/
22.Transforme as experiências com veículos com o Agentforce for Automotive. -
Salesforce, acessado em 25 de setembro de
2025.https://www.salesforce.com/automotive/ 23.Software CPQ para

Automotivo, acessado em 25 de setembro de
2025,https://cpq-integrations.com/cpq-software-automotive/
24.Orçamentos de carros - Quanto vale meu carro? - CarGurus, acessado em 25 de

setembro de 2025https://www.cargurus.com/es/car-valuation

25.Auto: Cote e compare todas as marcas e modelos., acessado em 25 de

setembro de 2025,https://www.auto.cl/

26.Compra e venda de carros: avaliações, preços e financiamento - CarGurus,

acessado em 25 de setembro de 2025,https://www.cargurus.com/es

27.Contrato de Compra e Venda de Carro | O que Considerar Antes de

Assiná-lo - Kavak, acessado em 25 de setembro de 2025
https://www.kavak.com/mx/blog/contrato-compra-venta-auto-cosas-a-consider
ar-antes-de-assinar

28.Como comprar um carro usado de uma concessionária - Comissão Federal

de Comércio, acessado em 25 de setembro de 2025,
https://consumidor.ftc.gov/como-comprar-un-carro-usado-un-concesionario

29.Modelo de contrato de venda de carro - Djaboo.com, acessado em 25 de
setembro de 2025,

https://djaboo.com/es/plantillas-de-contrato/modelo-de-contrato-de-venta-de-a
comando/

30.GESTAMP NO CICLO DE VIDA DO VEÍCULO, acessado em 25 de setembro de

2025,https://www.gestamp.com/Gestamp11/media/GestampFiles/Sustainability/En
viron mento/O-ciclo-de-vida-do-veículo.pdf

31.ERP para a indústria automotiva: recursos, integrações e plataformas - Innowise,

acessado em 25 de setembro de 2025,
https://innowise.com/es/blog/erp-para-indústria-automotiva/

32.Aplicativo de agendamento de compromissos para Dynamics 365 CRM - Maplytics,

acessado em 25 de setembro de 2025,
https://www.maplytics.com/es/mapa-cita-dynamics-crm/

33.Estes são os 10 melhores CRMs para o setor automotivo [México] -

ComparaSoftware, acessado em 25 de setembro de 2025,
https://www.comparasoftware.com/crm-para-automotrices

34.Configurar agendamento de compromissos no Automotive Cloud - Ajuda do

Salesforce, acessado em 25 de setembro de 2025,
https://help.salesforce.com/s/articleView?id=ind.auto_configure_scheduler_paren
t.htm&idioma=es&tipo=5

35.CQI 14 | GESTÃO DE GARANTIA NA INDÚSTRIA AUTOMOTIVA - YouTube,
acessado em 25 de setembro de
2025https://www.youtube.com/watch?v=4hgFPw058zs 36.Serviços de Gestão de
Reivindicações de Garantia de Automóveis - Formulário D, acessado em 25 de
setembro de 2025,

https://formeld.com/es/servicios/servicio-posventa/gestion-de-garantias/

37.Aplicação de Reivindicações de Garantia (Tr) - IBM, acessado em 25 de setembro
de
2025,https://www.ibm.com/docs/es/mft/cd?topic=overviews-warranty-claims-applicati

sobre
38.Garantias de automóveis e contratos de serviço - Comissão Federal de Comércio,

acessado em 25 de setembro de 2025,
https://consumidor.ftc.gov/garantias-y-contratos-de-servicio-para-carros
39.Automotive Cloud - Ajuda do Salesforce, acessado em 25 de setembro de
2025,https://help.salesforce.com/s/articleView?id=ind.auto_cloud.htm&language=es&t
y em=5
40.O que é telemetria: informações de veículos em tempo real - Pluxee, acessado em
25 de setembro de 2025,https://www.pluxee.co/blog/que-es-telemetria/ 41.O que é
telemetria veicular e suas aplicações - YPF Ruta, acessado em 25 de setembro de
2025,

https://ruta.ypf.com/que-es-la-telemetria-vehicular-y-sus-aplicaciones.html
42.6 Aplicações da Tecnologia no Setor Automotivo - Tractian, acessado em 25
de setembro de 2025,

https://tractian.com/es/blog/mantenimiento-en-la-industria-automotriz-con-tecn
ologia

43.Gestão do Ciclo de Vida do Produto (PLM) na Indústria Automotiva - Visure

Solutions, acessado em 25 de setembro de 2025,
https://visuresolutions.com/es/automotor/PLM/

44.Melhor CRM automotivo - Salesforce, acessado em 25 de setembro

de 2025,https://www.salesforce.com/mx/automotive/

45.O que é um CRM (gerenciamento de relacionamento com o cliente)?   - IBM,
acessado em 25 de setembro de
2025,https://www.ibm.com/mx-es/think/topics/crm 46.O melhor sistema telefônico
integrado para concessionárias de automóveis - GoTo, acessado em 25 de
setembro de 2025,

https://www.goto.com/es/solutions/automotive

47.O melhor CRM para concessionárias de automóveis - Salesforce,

acessado em 25 de setembro de 2025,
https://www.salesforce.com/es/automotive/car-dealership-software/

48.Plataforma de comunicação para concessionárias de veículos: Integração

com Auto.ru e Avito | Umnico for Automotive, acessado em 25 de setembro
de 2025https://umnico.com/es/solutions/automotive/

49.10 Chaves para um Inventário Automotivo Bem-Sucedido - Kavak, acessado

em 25 de setembro de 2025,
https://www.kavak.com/mx/blog/10-claves-del-inventario-automotriz-exitoso
50.Categorias de estoque para lojas de autopeças - Bind ERP, acessado em 25 de
setembro de
2025,https://bind.com.mx/blog/categorias-de-inventario-para-refaccionaria
51.Produtos, catálogos de preços e entradas do catálogo de preços do Salesforce -
YouTube, acessado em 25 de setembro de
2025,https://www.youtube.com/watch?v=b-Hg6dwtSDo 52.Produtos e catálogos de
preços - Ajuda do Salesforce, acessado em 25 de setembro de
2025,https://help.salesforce.com/s/articleView?id=sales.products_pricebooks.htm&lan

g uage=en_US&type=5
53.CRMAuto Sales | O CRM automotivo líder - Nextlane, acessado em 25 de
setembro de 2025,https://www.nextlane.com/es/product/crm-auto-sales-2/

54.Gestão do ciclo de vida do veículo - ARC-Refuellers, acessado em 25 de
setembro de
2025,https://arc-refuellers.be/es/services/vehicle-life-cycle-management/ 55.O CRM
especializado para o setor automotivo - Motorpath, acessado em 25 de setembro
de 2025,https://www.motorpath.pro/funcionalidades/crm 56.O que é um CRM para
concessionárias de veículos e como ele pode transformar sua concessionária? -
Dync Solutions, acessado em 25 de setembro de 2025,

https://dyncsolutions.com/que-es-un-auto-dealer-crm-y-como-puede-transfor
mar-sua-concessionária/

57.Os 10 melhores softwares de CRM para concessionárias automotivas em 2025 -

ClickUp, acessado em 25 de setembro de 2025,
https://clickup.com/es-ES/blog/420840/crm-automotriz

58.As 10 principais estratégias de atendimento ao revendedor que geram

resultados - Getac, acessado em 25 de setembro de 2025,
https://www.getac.com/latam/blog/servicios-al-concesionario/

59.O que é CPQ, ou Configurar, Preço, Cotação? - Salesforce, acessado em 25 de

setembro de 2025,https://www.salesforce.com/sales/cpq/what-is-cpq/
60.AutoUncle - Comparação de preços e verificação independente de preços,

acessado em 25 de setembro de 2025,https://www.autouncle.es/

61.Como criar um modelo de cotação interativo no Excel com impressão em PDF

(parte 1 de 2) - YouTube, acessado em 25 de setembro de 2025,
https://www.youtube.com/watch?v=yg2SkfT-B_E

62.Software de gerenciamento de concessionárias e oficinas de automóveis - Shift

Industry, acessado em 25 de setembro de 2025,
https://www.shiftindustry.com/es-es/auto-dealer-shop-software 63.O que é
Gerenciamento de Categorias? | Um Guia Completo - SAP, acessado em 25 de
setembro de 2025

https://www.sap.com/latinamerica/products/spend-management/category-mana
gerenciamento-software/o-que-e-gerenciamento-de-categorias.html
64.Gerenciamento de catálogo de produtos: definição e casos de uso -

Infoverity, acessado em 25 de setembro de 2025,
https://www.infoverity.com/es/blog/gestion-de-catalogos-de-productos-definici
casos de uso/

65.Garantindo a Qualidade na Indústria Automotiva: Importância e Estratégias

Eficazes, acessado em 25 de setembro de 2025,
https://www.bureauveritascertification.com/es/blog/calidad-de-productos/asegur e
qualidade na indústria automotiva - importância e

66.Quatro casos de uso de aprendizado de máquina na indústria automotiva -

Medium, acessado em 25 de setembro de 2025,
https://medium.com/@ejeraldo/cuatro-casos-de-uso-de-aprendizaje-autom%C3
Sótão na indústria automotiva 73b7b836b149

67.O que é telemetria e suas aplicações - SITRACK, acessado em 25 de setembro

de 2025,https://landing.sitrack.com/telemetria-y-sus-aplicaciones

68.Como funciona a telemetria? Tudo o que você precisa saber!, acessado em 25
de setembro de 2025.https://tl.trimble.com/es/blog/como-funciona-la-telemetria/
Catálogo estratégico de épicos e casos
de uso: Salesforce Commerce Cloud

Seção 1: Estrutura estratégica para a transformação
do comércio digital

O cenário do comércio evoluiu de transações isoladas para um ecossistema de experiências
interconectadas. Os clientes atuais, tanto B2C quanto B2B, não apenas compram produtos;
eles interagem com marcas por meio de uma infinidade de pontos de contato digitais e físicos.
Nesse novo paradigma, a capacidade de uma organização de oferecer uma jornada de compra
unificada, personalizada e inteligente torna-se o principal impulsionador do crescimento e da
fidelidade. Este documento apresenta uma estrutura estratégica para a implementação do
Salesforce Commerce Cloud, estruturada em torno dos princípios da metodologia Agile para
garantir que a tecnologia não apenas possibilite vendas, mas também gere valor comercial
tangível e mensurável.

Definindo épicos no contexto do Salesforce

No léxico da gestão ágil de projetos, umaÉpica Representa uma grande iniciativa
empresarial ou um conjunto significativo de trabalho que não pode ser concluído em um
único sprint de desenvolvimento. Funciona como um contêiner de alto nível para um conjunto
de funcionalidades relacionadas que, juntas, alcançam um objetivo estratégico fundamental.
No contexto de uma implementação do Commerce Cloud, um Epic traduz uma necessidade
empresarial em um resultado tangível dentro da plataforma. Por exemplo, em vez de um
requisito vago como "melhorar a loja online", um Epic bem definido seria "Implementar uma
experiência de compra B2B de autoatendimento para reduzir a carga da equipe de vendas e
otimizar pedidos recorrentes".

Os épicos são essenciais por vários motivos:

●Organização Hierárquica:Eles permitem que você estruture o backlog do produto, dividindo

projetos massivos em componentes gerenciáveis   que podem ser priorizados e
planejados ao longo de vários trimestres.

●Alinhamento estratégico:Eles conectam o trabalho diário da equipe de desenvolvimento

aos objetivos mais amplos da organização, garantindo que cada recurso criado contribua
para um objetivo comercial maior.

●Comunicação com as partes interessadas:Eles servem como a unidade de valor

comunicada aos líderes empresariais. Enquanto as equipes de desenvolvimento se
concentram em tarefas menores, a gerência pode acompanhar o progresso no nível Épico,
que representa marcos significativos do projeto.

Definição de Casos de Uso (Histórias de Usuário)

Se um Épico é o "o quê" estratégico, oCasos de uso, comumente expressa comoHistórias
de usuáriosNo Agile, estes são os táticos "quem", "o quê" e "por quê". São descrições
breves e simples de um recurso da perspectiva de quem o deseja. A estrutura padrão para
uma história de usuário é:

"Como um[tipo de usuário], quero [executar uma ação]para que [pode
atingir um objetivo]".

Essa estrutura é deliberadamente simples, mas poderosa. Ela força a equipe a se concentrar
no usuário final, seja um comprador B2C, um gerente de compras B2B, um comerciante ou um
agente de atendimento ao cliente. Ela divide a complexidade de um épico em requisitos
específicos e acionáveis   que podem ser desenvolvidos, testados e entregues em um único
sprint. Por exemplo, o épico "Implementar uma experiência de compra B2B de
autoatendimento" pode ser dividido nos seguintes casos de uso:

●"Como um comprador B2BQuero ver um catálogo com meus preços negociados
anteriormente.para poder faça pedidos sem precisar entrar em contato com um
vendedor."●"Como gerente de compras, Quero poder criar listas de compras
recorrentespara poder acelerar a reposição de produtos usados   com frequência."

A Hierarquia do Trabalho (Iniciativa > Épico > Caso de Uso)

Para um planejamento estratégico completo, é útil visualizar a hierarquia do
trabalho.Iniciativas Estes são objetivos de negócios mais amplos, geralmente anuais ou
plurianuais, que abrangem múltiplos Épicos. Por exemplo, uma Iniciativa pode ser "Expandir
as Operações de E-commerce para Mercados Internacionais". Essa Iniciativa seria dividida
em vários Épicos.
como "Lançar Vitrines Localizadas para Europa e Ásia", "Integrar Múltiplos Gateways de
Pagamento e Provedores de Impostos" e "Centralizar a Gestão de Catálogos Multi-Site".
Cada um desses Épicos é então dividido em dezenas de Casos de Uso específicos que
orientam o trabalho da equipe de desenvolvimento. Essa abordagem estruturada garante que
cada linha de código escrita esteja diretamente vinculada a um resultado comercial
mensurável.

A análise do setor de comércio digital revela uma transição crítica. As abordagens
tradicionais focavam na transação como o ponto final da jornada. No entanto, pesquisas de
mercado e histórias de sucesso atuais demonstram que o verdadeiro diferencial competitivo
é criar uma experiência do cliente (CX) que abrange todo o ciclo de vida do produto. A
compra é apenas um marco em um relacionamento contínuo que abrange marketing, serviço
pós-venda, gestão de devoluções e fidelidade.

Essa mudança de perspectiva é fundamental para definir efetivamente os Épicos. Um processo
de devoluções ineficiente não é apenas um problema logístico; é a causa raiz de uma
experiência frustrante do cliente que corrói a fidelidade. Portanto, um Épico não deve ser
simplesmente "Processar devoluções". Um Épico estratégico seria definido como "Construir a
confiança do cliente por meio de um processo omnicanal de devoluções e trocas de
autoatendimento". Essa mudança de foco muda a métrica de sucesso do projeto de
simplesmente medir a eficiência do processamento de reembolsos para impactar a retenção e
o valor da vida útil do cliente. Isso alinha a implementação da tecnologia diretamente com a
geração de receita recorrente e a fidelidade a longo prazo, que são os verdadeiros
impulsionadores do crescimento sustentável no comércio moderno.

Seção 2: O ecossistema do comprador digital: uma
jornada personalizada

A jornada de compra moderna é um fluxo contínuo entre descoberta, compra e atendimento.
Uma estratégia de comércio bem-sucedida deve orquestrar essa jornada de forma integrada,
usando dados e inteligência artificial para personalizar cada ponto de contato e eliminar atritos.

2.1. Descoberta e experiência na vitrine

Esta fase inicial é fundamental para captar o interesse do comprador e guiá-lo pelo catálogo de
produtos de forma intuitiva e relevante. A eficácia nesta fase depende de:
a capacidade de gerenciar catálogos complexos e personalizar a experiência de
navegação para cada usuário.

Gestão de Catálogo e Produtos

A base de qualquer experiência de comércio é o catálogo de produtos. Gerenciar esse catálogo
pode ser complexo, especialmente para empresas que operam várias marcas, vendem em
diferentes regiões ou lidam com tipos de produtos complexos, como pacotes e conjuntos.1O
Commerce Cloud permite o gerenciamento centralizado por meio de um catálogo mestre, a
partir do qual catálogos específicos para o site ou para a vitrine podem ser criados. Isso garante
a consistência das informações sobre os produtos, ao mesmo tempo em que permite a
flexibilidade de adaptar sortimentos, preços e conteúdo para diferentes públicos.3

Personalização e Pesquisa Inteligente

Depois que o catálogo estiver estruturado, o próximo desafio é ajudar os compradores a
encontrar o que procuram. Os consumidores modernos esperam experiências personalizadas
semelhantes às oferecidas pelos gigantes do varejo.5O Salesforce Commerce Cloud integra o
Einstein, seu mecanismo de inteligência artificial, para aprimorar a experiência na loja. O
Einstein Search permite que os usuários utilizem linguagem natural em suas pesquisas, indo
além da simples correspondência de palavras-chave para entender a intenção do comprador.7
Além disso, ferramentas como Einstein Product Recommendations e Predictive Sort
personalizam o conteúdo dinamicamente, exibindo os produtos mais relevantes para cada
visitante com base em seu comportamento de navegação e nas tendências de compra de
outros usuários.8

Para definir um épico de "Experiência de Compra Personalizada", é crucial entender a
diversidade do negócio. As principais questões de escopo giram em torno da complexidade:
Quantas marcas, regiões geográficas e moedas devem ser gerenciadas? O catálogo inclui

produtos únicos, pacotes, kits ou produtos com múltiplas opções? Essas variáveis   determinam
a estrutura dos catálogos e listas de preços (Price Books).1Uma empresa global precisará de
várias listas de preços para gerenciar variações regionais e campanhas promocionais,
enquanto uma empresa com produtos complexos precisará de um gerenciamento robusto de
tipos de produtos.1A estratégia deve se concentrar na criação de um "Gerenciamento Unificado
de Catálogos Multi-Site", onde um catálogo mestre atua como a única fonte de verdade, e os
catálogos de sites herdam e adaptam as informações. Essa abordagem não apenas garante a
consistência de dados, mas também permite personalização em escala, atribuindo conteúdo
e promoções específicas a segmentos de clientes definidos, criando uma experiência de
compra verdadeiramente relevante e direcionada.1

2.2. Transação e Pagamento

A fase de checkout é o momento da verdade, onde confiança, segurança e conveniência são
primordiais. Um processo de checkout sem atritos, com múltiplas opções e prevenção
robusta contra fraudes, é crucial para maximizar a conversão e proteger a receita.

Gestão de Pagamentos, Impostos e Fraudes

Um processo de checkout complexo é uma das principais causas de abandono de carrinho.
Para combater isso, o Commerce Cloud integra-se a diversos gateways de pagamento,
permitindo que os lojistas ofereçam diversas opções, desde cartões de crédito até carteiras
digitais como Apple Pay e PayPal.10A plataforma também se conecta com provedores de
serviços fiscais para calcular automaticamente os impostos sobre vendas aplicáveis   em tempo
real, um recurso essencial para empresas que vendem em diversas jurisdições.12A segurança
também é uma preocupação primordial. A integração com serviços de prevenção a fraudes
analisa transações em tempo real para identificar e bloquear pedidos suspeitos, minimizando o
risco de estornos e protegendo comerciantes e clientes.14

Ao projetar o épico "Otimização do Processo de Pagamento", a análise deve se concentrar na
diversidade de métodos de pagamento e na gestão de riscos. As perguntas de escopo são
simples: quais métodos de pagamento devem ser suportados (cartões de crédito, carteiras
digitais, vales-presente)?   Qual prestador de serviços tributários será utilizado? Existe um
prestador de serviços de prevenção a fraudes? O processo é manual ou automatizado? A
estratégia deve abordar não apenas a aceitação de pagamentos, mas também a gestão
pós-transação. O "Payments Workspace" da Salesforce permite que as equipes de operações
visualizem o histórico de transações, capturem pagamentos manualmente e processem

reembolsos centralmente.10Portanto, a Epic não se trata apenas de "Aceitar Pagamentos", mas
de "Oferecer uma Experiência de Pagamento Segura, Flexível e Sem Atrito". Isso se traduz em
casos de uso que beneficiam tanto o cliente, como a opção "Checkout Rápido" para
compradores registrados, quanto a empresa, com a capacidade de analisar transações e
gerenciar disputas.
eficientemente.10

2.3. Gestão de Pedidos e Serviço Pós-Venda

O  relacionamento com o cliente se aprofunda após a compra. A fase de pós-venda é onde a
fidelidade é construída por meio de uma gestão transparente de pedidos, atendimento eficiente
e um processo de devolução descomplicado.

Orquestração de conformidade e visibilidade de inventário

Após a realização do pedido, a promessa de entrega deve ser cumprida. O Salesforce Order
Management (OMS) orquestra esse processo do início ao fim. Um recurso essencial é a
visibilidade omnicanal do estoque, que centraliza o estoque de vários locais, como armazéns e
lojas físicas.17Isso não só proporciona uma visão precisa da disponibilidade, como também
permite estratégias de atendimento flexíveis, como "compre online e retire na loja" (BOPIS). O
sistema de roteamento de pedidos baseado em regras atribui automaticamente cada pedido ao
local de atendimento mais adequado, com base em critérios como proximidade do cliente,
disponibilidade de estoque ou custo de envio, otimizando a velocidade de entrega e a eficiência
de custos.18

Gestão de Devoluções, Trocas e Cancelamentos

Um processo de devolução complexo pode arruinar uma experiência positiva para o cliente. O
Salesforce Order Management oferece aos agentes de atendimento ao cliente uma visão
completa do histórico de pedidos do cliente, permitindo que eles gerenciem as solicitações de
serviço com eficiência.19A plataforma oferece suporte à criação de autorizações de devolução
de mercadorias (RMAs), permitindo que os clientes iniciem devoluções por meio de um portal
de autoatendimento.20Os agentes podem processar reembolsos, gerenciar trocas e cancelar
pedidos antes do envio, tudo em um único console. Essa capacidade de resolver problemas

pós-venda com rapidez e eficiência é fundamental para manter a confiança e promover a
fidelidade do cliente.21

A Epopeia da “Orquestração Inteligente da Ordem e do Cumprimento” é definida pela
A complexidade da rede de atendimento e das políticas de serviço. Questões de escopo são
cruciais: Quantos locais de atendimento existem (armazéns, lojas, dropshipping)? São
necessárias pré-encomendas ou pedidos em espera? Quais são as fontes de RMA? A
estratégia deve ir além da simples gestão de pedidos e focar na automação inteligente. Por
exemplo, a integração do OMS com o Service Cloud é vital para que um agente de
atendimento, ao receber uma consulta, tenha acesso imediato ao histórico de pedidos do
cliente sem precisar trocar de sistema.19Os casos de uso derivados deste Epic devem refletir
essa visão unificada. Um cliente deve poder iniciar uma devolução a partir de um portal de
autoatendimento, enquanto um agente de serviço deve poder cancelar um item de um pedido
que ainda não foi enviado e aplicar um desconto de conciliação para resolver uma reclamação,
tudo na mesma interface.21

Seção 3: Capacidades fundamentais para o
comércio B2B

O comércio B2B apresenta um conjunto único de complexidades que exigem capacidades
especializadas. Gerenciar relacionamentos comerciais de longo prazo, preços negociados e
processos de compra complexos são essenciais para o sucesso neste setor.

3.1. Gerenciamento de contas B2B e preços personalizados

Ao contrário do B2C, onde o preço geralmente é o mesmo para todos, o comércio B2B é
baseado em relacionamentos e acordos negociados.

Hierarquias de contas e cotações

Os compradores B2B geralmente não são indivíduos, mas sim equipes dentro de uma
organização. O Salesforce B2B Commerce permite modelar essas hierarquias de contas
complexas, onde uma empresa-mãe pode ter várias subsidiárias e compradores autorizados

podem fazer pedidos em nome de diferentes entidades.22Além disso, o processo de compra
B2B frequentemente envolve negociação. A plataforma oferece suporte ao fluxo de "Solicitação
de Orçamento", no qual o comprador pode preencher um carrinho e solicitar um orçamento.
cotação em vez de comprar diretamente, iniciando um processo de negociação com a
equipe de vendas.23

Catálogos e Preços Contratuais

Para refletir acordos comerciais, o B2B Commerce permite que você atribua catálogos de
produtos e listas de preços específicos a diferentes grupos de compradores.24Isso garante
que cada cliente veja apenas os produtos que está autorizado a comprar e pelos preços
pré-negociados. Essa capacidade de personalização em nível de conta é fundamental para o
modelo de negócios B2B, onde os preços e a variedade de produtos podem variar
drasticamente de cliente para cliente.

O Epic "Gerenciamento de Contas Corporativas e Precificação Complexa" é a base de
qualquer implementação de comércio B2B. Seu design depende da compreensão das
estruturas de contas e estratégias de precificação da empresa. Como as hierarquias de contas
são estruturadas? Os preços são baseados em contratos ou no volume de compras? É
necessário um processo formal de cotação e negociação? A solução deve permitir que um
gerente de vendas atribua um catálogo de produtos específico e uma lista de preços negociada
a um "Grupo de Compradores" que represente um cliente-chave.24Por sua vez, um comprador
dessa conta deve poder fazer login em um portal de autoatendimento, visualizar apenas seu
catálogo autorizado com seus preços e ter a opção de fazer um pedido grande enviando uma
lista de SKUs ou solicitar um orçamento formal para negociação.24Essa abordagem transforma
o site de comércio eletrônico de uma simples loja em um portal de autoatendimento para
gerenciamento de contas, liberando a equipe de vendas para se concentrar em
relacionamentos estratégicos em vez de fazer pedidos manualmente.

Seção 4: Catálogo exaustivo de épicos e casos de
uso para o Commerce Cloud

A tabela a seguir consolida a pesquisa e a análise estratégica em um catálogo
abrangente de épicos e casos de uso, projetado para servir como um acelerador para
planejamento, escopo e implementação do Salesforce Commerce Cloud.

Título da tabela:Catálogo de épicos e casos de uso do Salesforce Commerce Cloud

Nuvem

Comércio
Nuvem

Nome de
domínio

Capacidade
Nome

Épica
(resumo)

Caso de uso
(resumo)

Ordem
Gerenciament
o

Vendas
Canais e
Catálogo

Gerenciamen
to
Unificado de
Catálogos
Multi-Site:
Centralizar o
gestão de
produtos,
preços e
catálogos
para operar
múltiplo
marcas,
regiões e
moedas
de um
única
plataforma,
garantindo
consistência
e eficiência.

Como
comerciante
, eu quero
gerenciar um
catálogo
professor e
criar
catálogos de
lugar
específicos
que eles
herdam
produtos
para
diferentes
marcas o
regiões.3

Como
gerente de
preços,
quero
configurar
várias listas
de preços
(Livros de
Preços)
para
diferentes
geografias e
moedas, e
atribuí-los a
os sites

testes
corresponde
ntes.1

Como gestor

do catálogo,
Eu quero
poder
definir
produtos
complexos,
incluindo
variações
(tamanho,
cor),
pacotes
(pacotes) e
conjuntos de
produtos.1

Como
gerente de
comércio
eletrônico,
quero
localizar o
conteúdo do
produto,
como
descrições
e atributos,
para
diferentes
idiomas e
mercados.8

Comércio
Nuvem

Ordem
Gerenciament
o

Vendas
Canais e
Catálogo

Como cliente,
Eu quero usar
a busca
na linguagem
natural para
encontrar
produtos
relevantes,
mesmo que
não
Eu os uso
termos
exato do
produto
(Einstein
Procurar).7

Experiência
de Compra
Personaliza
da e
Inteligente:
Use IA e
dados do
cliente para
personalizar
a
experiência
da vitrine,
do
procurar
produtos
até o
recomendação

nes, em ordem

para
aumentar  a
conversão  e
o valor médio
do pedido
(AOV).

Como
comerciante
, eu quero
configurar
recomendaç
ões de
produtos
Na página
com base
em IA
desde o início,
desde
produto e
carrinho
para
promover o
descoberta
de
produtos.5

Como
estrategista de
comércio
eletrônico,
Eu quero as
páginas de
categoría
a ordem
automatica
mente o
produtos
para mostrar
primeiro o
que eles têm
prefeito
probabilidade
ser
comprados
por cada

Comércio
Nuvem

Ordem
Gerenciament
o

Pagamento/
Fraude/Impo
sto

visitante
(Einstein
Preditivo
Organizar).8

Como
especialista
em
marketing,
Eu quero criar
segmentos
de clientes
(ej.
compradores
VIP) e
mostre a eles
conteúdo e
promoções
personalizad
o no
vitrine.1

Como cliente,
Eu quero
poder
pagar meu
compras
utilizando
diversas
opções,
incluindo
cartas de
crédito e
carteiras
digital como
Apple Pay
ou
PayPal.10

Otimização
de
Processos
Pagamento e
Redução de
fraudes:
Oferecer um
experiência
de
pagamento
segura,
flexível e sem
atritos,
integrando
múltiplo
métodos de
pagamento e
um
sistema
robusto de

detecção de
fraude para
proteger o
renda.

Como gerente

de
operações,
Eu quero os
impostos de
venda é
calcular
automatica
mente
tempo
durante
finalização
da compra,
com base
na
localização
do cliente.12

em
real
a

Como
analista de
risco,
Quero
integrar um
serviço de
prevenção
de fraudes
que
analisar o
transações
e marcar o
pedidos
suspeitos
para revisão
manual ou o

Comércio
Nuvem

Ordem
Gerenciament
o

Integrações

rejeitar
automática
me nte.14

Como cliente
recorrente,
Eu quero
poder
salve meu
método de
pagamento
por
agilizar
futuras
compras
(Um clique
Confira).10

Como
arquiteto de
Quero você
estabelecer
uma
integração
bidirecional
com o ERP
para
sincronizar
pedidos,
clientes e
inventário em
tempo real,
usando um
middleware
como
MuleSoft.21

Ecossistema
do Comércio
Conectado:
Integrar
Comércio
Nuvem con
sistemas
principais
processos
de negócios
(ERP,
CRM, Dados
Armazém)
para garantir
um fluxo de
dados
coerente e
automatizar
processos de
negócios de
extremo para
extremo.

Como
gerente de
atendimento
ao cliente
cliente, eu
quero meu
agentes
tem um
Visão 360
graus do
cliente em
Service
Cloud,
incluindo
seu histórico
de
pedidos de
Comércio
Nuvem.19

Como
analista de
negócios,
quero
exportar o
dados de

pedidos de
Comércio
Nuvem a
nossos dados
armazém
para realizar
análise de
tendências
para
longo prazo.21

Comércio
Nuvem

Ordem
Gerenciament
o

Cliente
Serviço
(Devoluções
/Trocas/Can
celamentos)

Gestão de
Devoluções
e trocas
Omnicanal:
Oferecer um
processo de
devoluções
e trocas
flexível e sem
complicaçõe
s para o
cliente,
permitindo a
autogestão
e
fornecer aos
agentes de
serviço as
ferramentas
para resolver
casos
rapidamente.

Como cliente,
Eu quero
poder
começar um
solicitação de
retornar
(RMA) de
minha conta
no site e
receba um
rótulo de
envio para
retornar um
produto.21

Como agente
de serviço
para
Cliente,
quero poder
cancelar um
pedido ou
um item
específico de
uma ordem
do
console de

Ordem
Gerenciament
o
antes

Comércio
Nuvem

Ordem
Gerenciament
o

Alocação/Es
toque/Locali
zação
e
Atendimento

ser enviado.21

Como agente
de plantão,
quero
processar um
reembolso
para um
cliente e
aplicar um
desconto de
compensaçã
o
(apaziguame
nto)
para
resolver uma
reclamação.2
1

Como
gerente de
operações,
Eu quero ter
uma visão
unificado do
inventário para
através
todos os meus
armazéns e
lojas físicas
para
permitir
o "compre
online e
retire"
na loja"
(BOPIS).17

de

Orquestraç
ão
Ordem
Inteligente e
Conformida
de :
Automatizar
a tarefa
de ordens
para
centro de
conformidade
mais
eficiente e
fornecer
visibilidade do
inventário em
tempo real
para
através
todos os
canais.

Como
administrad
or de
sistemas,
quero
configurar
regras de

roteamento
queasign
automatica
mente o
pedidosal
armazém mais
cercanoal
cliente que
tem estoque
disponível.18

Como
gerente de
comércio
eletrônico,
Eu quero
permitir que
o
clientes
levar a cabo
pré-encomend
as
desprodutos
que ainda não
hansido
lançado,
gerenciando
o
expectativas
de entrega.21

Comércio
Nuvem

B2B
Comércio

Conta
Hierarquias&

Citando

Como cliente,
Eu quero
receber
notificações
por e-mail
electrónico
sobre o
estados-chave
demi pedido:
confirmação,
transporte e
entrega.21

Como
administrador

vendas,
Quero
modelar a
hierarquia de
uma conta
cliente, com
sua
empresa-mã
e e sua
subsidiarias,
para que o
compradores
autorizados
pode
realizar
pedidos em
nome de
diferentes
entidades.22

Gerenciamen
to
Contas

Corporativ
o e Preços
Complexos:
Facilitar o
Vendas B2B
através do
gestão de
hierarquias de
contas,
catálogos e
preços
personalizad
o e um
processo de
cotação e
pedido
simplificado
para
compradores
negócios.

Como
gerente de
contas,
Quero
atribuir um
catálogo de
produtos
específico e
uma lista de
preços
negociada a
um grupo de
compradores
(Grupo de
Compradores
) para refletir
um contrato
comercial.24

Como
comprador
B2B, eu quero
poder
adicionar
produtos ao
carrinho e

solicitar um
preço
formal para
começar um
processo de
negociación
preço com a
equipe
vendas.23

Como
comprador
B2B, eu quero
ser capaz de
executar

pedidos
grandes
rapidamente
carregando
um
arquivo CSV
com SKUs e
cantidades, o
repetindo um
pedido
anterior.24

Seção 5: Mapa de Processos de Negócios
de Comércio Eletrônico

Para implementar com sucesso o Salesforce Commerce Cloud, é essencial mapear os
recursos da plataforma para os processos de negócios de ponta a ponta do setor de comércio
eletrônico.

5.1 Experiência do comprador e processo de aquisição
Esse macroprocesso abrange todas as atividades desde o momento em que um cliente em
potencial descobre a marca até que ele esteja pronto para iniciar uma transação.

●Nível 1: Gestão de Vitrine Digital

○Nível 2: Gestão de Catálogo e Produtos:Gerencie a hierarquia de produtos,
categorias, atributos e tipos de produtos (simples, pacotes, conjuntos).○Nível 2:
Gerenciamento de conteúdo e página (CMS):Crie e gerencie conteúdo para páginas
do site, como página inicial, páginas de destino e banners promocionais.
○Nível 2: Configurações de pesquisa e navegação:Defina atributos de pesquisa, filtros

(facetas) e regras de classificação para facilitar a descoberta de produtos.

○Nível 2: Gestão de Preços:Gerencie várias listas de preços (Livros de Preços) por

região, moeda ou segmento de cliente.

●Nível 1: Marketing e Personalização

○Nível 2: Criação e Gestão de Promoções:Crie promoções com base em cupons,

descontos por volume ou campanhas sazonais.

○Nível 2: Personalização de IA:Implemente recomendações de produtos e

classificação preditiva de categorias com o Einstein para personalizar a experiência
de cada visitante.8

○Nível 2: Segmentação de clientes:Crie grupos dinâmicos de clientes com base em seu
comportamento de compra ou dados demográficos para oferecer a eles experiências
direcionadas.1

5.2 Processo de Compra e Transação

Este macroprocesso abrange todo o fluxo desde o momento em que um cliente adiciona um
produto ao carrinho até a confirmação do pagamento.

●Nível 1: Gerenciamento de carrinho e checkout

○Nível 2: Processo de adição ao carrinho:Permita que os usuários adicionem,

modifiquem e excluam produtos do carrinho de compras.

○Nível 2: Fluxo de checkout:Oriente o usuário nas etapas de envio, pagamento e

confirmação para usuários registrados e convidados.

○Nível 2: Aplicação de Promoções e Cupons:Valide e aplique descontos

promocionais ou cupons ao total do carrinho.

●Nível 1: Processamento de Pagamentos e Segurança

○Nível 2: Autorização de Pagamento:Integre e processe transações por meio de
vários gateways de pagamento (cartões de crédito, carteiras digitais).
○Nível 2: Verificação de fraude:Analise cada transação com um serviço de

detecção de fraudes para minimizar o risco de estornos.

○Nível 2: Cálculo de impostos:Calcule os impostos sobre vendas aplicáveis   em

tempo real com base no endereço de entrega do cliente.

○Nível 2: Confirmação do pedido:Finalize a transação e envie uma notificação de

confirmação do pedido ao cliente.

5.3 Processo de Gerenciamento e Atendimento de
Pedidos

Este macroprocesso abrange todas as operações que ocorrem após a realização de um

pedido, incluindo logística e serviço pós-venda.

●Nível 1: Ciclo de vida e orquestração de pedidos

○Nível 2: Criando o Resumo do Pedido:Centralize todas as informações do pedido

em um único registro (Resumo do Pedido).

○Nível 2: Roteamento de Pedidos (DOM):Atribua automaticamente o pedido ao local
de atendimento mais apropriado (armazém, loja, etc.) com base nas regras de
negócios.

○Nível 2: Atualizações de status e notificações:Mantenha o cliente informado sobre

alterações no status do pedido (enviado, entregue, etc.).

●Nível 1: Gestão de Estoque e Conformidade Física

○Nível 2: Atribuição de inventário:Reserve o estoque necessário para atender o

pedido.

○Nível 2: Processo de coleta e embalagem:Gerenciar a coleta e a embalagem de

produtos no centro de distribuição.
○Nível 2: Confirmação de despacho e envio:Gere a etiqueta de envio e
notifique o sistema (e o cliente) que o pedido foi enviado.

●Nível 1: Serviço pós-venda e devoluções

○Nível 2: Gestão de Cancelamento de Pedidos:Permita que os agentes de serviço

cancelem pedidos antes do atendimento.

○Nível 2: Iniciação de Devolução de Item (RMA):Gerencie o processo de autorização

de devolução de mercadorias, seja iniciado por um agente ou pelo cliente por meio
de um portal.
○Nível 2: Processamento de reembolsos ou trocas:Gerenciar o recebimento de
produtos devolvidos e processar o reembolso ou envio de um novo produto.

Seção 6: Diagramas de Processos de Negócios
(Código da Sereia)
Abaixo está o código no formato Mermaid para gerar os fluxogramas para os processos de
negócios detalhados na seção anterior.

6.1 Código para o Processo de Experiência e Aquisição do
Comprador

Trecho de código

gráfico TD

subgráfico Processo L1: Experiência do Comprador e Aquisição

A[Experiência e Aquisição]

fim

Processos L2 do subgrafo

B1
B2[Marketing e Personalização]

fim

subgrafo Processos L3 - Vitrine

C1[Gestão de Catálogo e Produtos]
C2
C3
C4[Gestão de Preços]

fim

subgrafo Processos L3 - Marketing

D1[Gestão de Promoção]
D2[Personalização de IA]
D3

fim

A --> B1
A --> B2
B1 --> C1
B1 --> C2
B1 --> C3
B1 --> C4

B2 --> D1
B2 --> D2
B2 --> D3

estilo A preenchimento:#00a1e0,traço:#333,largura do
traço:2px,cor:#fff estilo B1
preenchimento:#00b5e2,traço:#333,largura do
traço:2px,cor:#fff estilo B2
preenchimento:#00b5e2,traço:#333,largura do
traço:2px,cor:#fff

6.2 Código para o Processo de Compra e Transação

Trecho de código

gráfico TD

subgrafo Processo L1: Compra e Transação

UM

fim

Processos L2 do subgrafo

B1[Gerenciamento de carrinho e checkout]
B2

fim

subgrafo Processos L3 - Checkout
C1[Gerenciamento de carrinho]
C2[Fluxo de Caixa]
C3[Aplicação de Promoção]

fim

subgrafo L3 Processos - Pagamentos
D1[Autorização de Pagamento]
D2[Verificação de Fraude]
D3[Cálculo de Imposto]
D4[Confirmação do Pedido]

fim

A --> B1
A --> B2

B1 --> C1
B1 --> C2
B1 --> C3

B2 --> D1

B2 --> D2
B2 --> D3
B2 --> D4

estilo A preenchimento:#00a1e0,traço:#333,largura do traço:2px,cor:#fff
estilo B1 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff
estilo B2 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff

6.3 Código para o Processo de Gestão e Atendimento de Pedidos

Trecho de código

gráfico TD

subgráfico Processo L1: Gestão e Atendimento de Pedidos

A[Gestão e Atendimento de Pedidos]

fim

Processos L2 do subgrafo

B1[Ciclo de Vida e Orquestração do Pedido]
B2[Inventário e Conformidade Física]
B3

fim

subgrafo L3 Processos - Orquestração

C1
C2
C3[Atualização de status e notificações]

fim

subgráfico L3 Processos - Conformidade

D1[Atribuição de Inventário]
D2[Escolha e Embalagem]
D3

fim

subgrafo L3 Processos - Serviço

E1[Gestão de Cancelamento]
E2
E3

fim

A --> B1
A --> B2
A --> B3

B1 --> C1
B1 --> C2
B1 --> C3

B2 --> D1
B2 --> D2
B2 --> D3

B3 --> E1
B3 --> E2
B3 --> E3

estilo A preenchimento:#00a1e0,traço:#333,largura do traço:2px,cor:#fff
estilo B1 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff
estilo B2 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff
estilo B3 preenchimento:#00b5e2,traço:#333,largura do traço:2px,cor:#fff

Obras citadas

1.Sites e vitrines - Ajuda do Salesforce, acessado em 25 de setembro de

2025,https://help.salesforce.com/s/articleView?id=cc.b2c_sites_and_storefronts.ht
m&la idioma=en_US&type=5

2.Gerenciar pedidos no B2C Commerce - Ajuda do Salesforce, acessado em 25

de setembro de 2025,
https://help.salesforce.com/s/articleView?id=cc.b2c_managing_orders.htm&langu
idade=en_US&tipo=5

3.Configurando uma vitrine com o Salesforce Commerce Cloud | Astrea IT

Services, acessado em 25 de setembro de 2025,
https://astreait.com/Configurando-uma-vitrine-com-Salesforce-Commerce-Cloud/
4.Dominando catálogos de produtos e merchandising no Salesforce B2C Commerce
| Royal Cyber, acessado em 25 de setembro de 2025,
https://www.youtube.com/watch?v=fVanLj9CJhk
5.Ferramentas de IA para comércio eletrônico para recomendações de
produtos e muito mais..., acessado em 25 de setembro de

2025,https://www.salesforce.com/commerce/ai/
6.Recomendações de produtos do Einstein para Commerce Cloud - Trailhead -

Salesforce, acessado em 25 de setembro de 2025,
https://trailhead.salesforce.com/content/learn/modules/cc-einstein-product-reco
recomendações

7.Commerce Einstein - Ajuda do Salesforce, acessado em 25 de setembro de

2025,https://help.salesforce.com/s/articleView?id=commerce.comm_commerce_ei
nste em.htm&idioma=en_US&tipo=5

8.Salesforce B2C Commerce Cloud: O que é e por que as marcas o escolhem |

MOA - YouTube, acessado em 25 de setembro de 2025
https://www.youtube.com/watch?v=e6wK7bjP0NY

9.Preços e edições do Salesforce Commerce Cloud, acessado em 25 de setembro

de 2025,https://www.salesforce.com/commerce/pricing/
10.Salesforce Payments, acessado em 25 de setembro de 2025,

https://help.salesforce.com/s/articleView?id=commerce.payments_product_intro.
htm&idioma=en_US&tipo=5

11.Soluções de pagamento online para comércio eletrônico | Salesforce, acessado
em 25 de setembro de
2025,https://www.salesforce.com/commerce/online-payment-solution/ 12.Preços do
Salesforce Commerce Cloud: uma análise completa para 2025 - eesel AI,
acessado em 25 de setembro de 2025,

https://www.eesel.ai/blog/salesforce-commerce-cloud-pricing

13.Adicionar um serviço de cálculo de impostos para checkout personalizado -

Ajuda do Salesforce, acessado em 25 de setembro de 2025,
https://help.salesforce.com/s/articleView?id=commerce.comm_set_up_tax.htm&la
idioma=en_US&type=5

14.Prevenir fraudes no comércio eletrônico - Ajuda do Salesforce, acessado em 25

de setembro de
2025,https://help.salesforce.com/s/articleView?id=cc.b2c_prevent_ecommerce_fra
ud.h tm&idioma=en_US&tipo=5

15.Soluções de Pagamento Salesforce | Detecção de Fraudes | Agentforce

- Milestone Technologies, acessado em 25 de setembro de 2025,
https://milestone.tech/services/applications-and-digital-engineering-services/sale
sforce/pagamentos/

16.Riskified: Fraude e Gestão de Riscos | Salesforce AppExchange, acessado

em 25 de setembro de 2025,
https://appexchange.salesforce.com/appxListingDetail?listingId=d719d10c-198a-4
d46-9df8-c4a8920c023e

17.Sistema de gerenciamento de pedidos de comércio eletrônico - Salesforce,
acessado em 25 de setembro de
2025,https://www.salesforce.com/commerce/order-management/ 18.Atendimento de
pedidos - Ajuda do Salesforce, acessado em 25 de setembro de
2025,https://help.salesforce.com/s/articleView?id=commerce.om_order_fulfillment.ht
m &idioma=en_US&tipo=5

19.Gerenciamento de pedidos e Service Cloud - Ajuda do Salesforce, acessado

em 25 de setembro de 2025,
https://help.salesforce.com/s/articleView?id=commerce.om_order_management_
and_service_cloud.htm&idioma=en_US&tipo=5

20.Devolver um item do pedido - Ajuda do Salesforce, acessado em 25 de setembro

de
2025,https://help.salesforce.com/s/articleView?id=commerce.om_return_order_it
ems_ visão geral.htm&language=en_US&type=5

21.Perguntas de Escopo Guiadas.pdf
22.Configurar a estratégia de hierarquia pai-filho para contas eficazes - Ajuda do

Salesforce, acessado em 25 de setembro de 2025,
https://help.salesforce.com/s/articleView?id=sf.b2b_commerce_effective_account
_parent_hierarchy.htm&idioma=en_US&tipo=5

23.SALESFORCE B2B COMMERCE | CloudStreet, acessado em 25 de setembro de
2025,https://cloudstreet.ai/wp-content/uploads/2021/04/B2B-Commerce-on-Lightn
ing -Experiência-Recursos-Folha de dados.pdf

24.Salesforce B2B Commerce Cloud: Recursos, preços e casos de uso - Smart IT

Staff, acessado em 25 de setembro de 2025,
https://smartitstaff.com/blog/salesforce-b2b-commerce-cloud/

25.6 exemplos de e-commerce B2B para pequenas empresas (2025) - Shopify Brasil,

accessed September 25, 2025,
https://www.shopify.com/br/blog/exemplos-e-commerce-b2b
Análise estratégica do Salesforce
Communications Cloud: catálogo de
recursos para o provedor de
serviços digitais

Seção 1: Quadro estratégico para a transformação
do setor de telecomunicações

O setor de telecomunicações está em uma encruzilhada transformadora, impulsionado pela
convergência da tecnologia 5G, da Internet das Coisas (IoT) e pelas crescentes expectativas
dos clientes B2B e B2C.1O modelo de negócios tradicional, centrado na venda de conectividade

como uma commodity, tornou-se insustentável diante da comoditização dos serviços e da
intensa concorrência. Para prosperar, os Provedores de Serviços de Comunicação (CSPs)
precisam evoluir para Provedores de Serviços Digitais (DSPs), capazes de oferecer um
ecossistema de soluções inovadoras, experiências personalizadas para o cliente e agilidade
operacional sem precedentes.4

Essa mudança fundamental expõe a principal barreira à inovação no setor: a rigidez dos
sistemas de suporte a negócios (BSS) e sistemas de suporte a operações (OSS) legados.
Essas arquiteturas monolíticas e isoladas impedem o lançamento rápido de novos produtos,
criam experiências fragmentadas para o cliente e aumentam os custos operacionais.8A solução
para
Este desafio não é uma melhoria incremental, mas sim uma reinvenção arquitetônica. O
Salesforce Communications Cloud está posicionado como a plataforma para essa
transformação, atuando como um middle office unificado e ágil que orquestra todo o ciclo de
vida do cliente, do conceito do produto ao pagamento e do pedido à ativação.10

A chave para essa agilidade reside em sua arquitetura orientada por catálogo. Um Catálogo
de Produtos Corporativos (EPC) centralizado torna-se a única fonte de verdade, permitindo
que as equipes de negócios projetem, testem e lancem novas ofertas e pacotes de serviços a
uma velocidade antes inatingível. Essa abordagem dissocia a inovação empresarial da
complexidade técnica da rede, permitindo que os DSPs respondam às oportunidades de
negócios.
mercado em minutos, não em meses.11

Definindo épicos e casos de uso no contexto do Salesforce

Para traduzir essa visão estratégica em execução tangível, este documento adota os princípios
da metodologia Ágil, utilizando uma hierarquia de trabalho que alinha cada atividade de
desenvolvimento a um resultado comercial mensurável. Essa estrutura, espelhada nas
estruturas de implementação de outras nuvens Salesforce, garante que o investimento em
tecnologia gere valor claro e quantificável.14

Épica: No contexto de uma implementação de Nuvem de Comunicações, um Épico representa
uma iniciativa empresarial de alto nível que aborda um objetivo estratégico fundamental. Não se
trata de um recurso técnico, mas de um resultado comercial. Por exemplo, em vez de
"Implementar Orquestração de Pedidos", um Épico estratégico seria "Reduzir a Taxa de Perda
de Pedidos em 30% por meio da Automação Inteligente de Atendimento". Os épicos servem
como a unidade de valor comunicada às partes interessadas do negócio, permitindo a
priorização e o acompanhamento do progresso em termos de impacto nos negócios.

Caso de uso (história do usuário):Se um Épico é o "o quê" estratégico, os Casos de Uso são
o "quem", o "o quê" e o "por quê" táticos. Eles são expressos como Histórias de Usuário,
seguindo a estrutura: "Como [tipo de usuário], quero [executar uma ação] para [atingir um
objetivo]". Eles decompõem a complexidade de um Épico em requisitos funcionais granulares
que podem ser desenvolvidos, testados e entregues em um curto ciclo de desenvolvimento. Por
exemplo, o Épico de Redução de Fallout pode incluir o seguinte Caso de Uso: "Como gerente
de atendimento, quero receber um alerta automático no meu console para qualquer pedido que
falhe na fase de ativação, para que eu possa intervir imediatamente e cumprir o SLA do
cliente".

Essa abordagem estruturada (Iniciativa > Épico > Caso de Uso) garante que cada
componente da solução, desde uma regra de validação simples até um fluxo de orquestração
complexo, esteja diretamente vinculado à estratégia geral de transformação dos negócios.

Seção 2: O ecossistema do cliente
Telecomunicações: Uma jornada completa do
ciclo de vida
A jornada do cliente de telecomunicações é um ciclo contínuo que abrange desde a descoberta
de novas ofertas até o gerenciamento e a modificação de serviços existentes ao longo dos
anos. Uma implementação bem-sucedida da Nuvem de Comunicações deve orquestrar essa
jornada perfeitamente, unificando os processos de vendas, atendimento e serviços em uma
plataforma única e coerente.

2.1. Do conceito ao lançamento: catálogo de produtos e gestão de
ofertas (EPC)

A capacidade de inovar e lançar rapidamente novas ofertas é o motor do crescimento de uma
DSP. O Catálogo de Produtos Corporativos (EPC) é a base dessa agilidade, servindo como o
cérebro central que define tudo o que uma empresa pode vender e como deve ser entregue.11
arquitetura EPC é baseada em um princípio fundamental que é essencial para a agilidade nas
telecomunicações: a separação do catálogo comercial do catálogo técnico.16

 A

Ele Catálogo ComercialDefine produtos, serviços e pacotes como o cliente os vê. Isso inclui
ofertas como "Plano 5G Ilimitado com Assinatura de Streaming" ou "Pacote de Conectividade
para Pequenas Empresas". É aqui que as equipes de marketing e produto definem preços,

promoções, descontos e regras de elegibilidade, usando ferramentas visuais para criar ofertas
complexas a partir de componentes reutilizáveis.15

Ele Catálogo Técnico, por outro lado, define os serviços e recursos de rede necessários para
atender às ofertas comerciais. Seguindo os padrões do TM Forum, estes são modelados como
Serviços de Atendimento ao Cliente (CFS) e Serviços de Atendimento a Recursos (RFS). Por
exemplo, a oferta comercial "Plano Ilimitado 5G" é dividida em serviços técnicos, como
"Ativação de SIM 5G", "Provisionamento de Perfil de Dados" e "Configuração de Correio de
Voz".16

Essa separação é a chave para a velocidade. Ela permite que a equipe de marketing lance
uma nova promoção "Duplo de Dados pelo Mesmo Preço" (uma mudança no catálogo de
vendas) sem exigir nenhuma modificação nos sistemas de rede subjacentes (o catálogo técnico
permanece estável). Essa capacidade de gerenciar todo o ciclo de vida do produto, desde o
design e os testes até o lançamento e a descontinuação, torna o EPC a única fonte de verdade
para toda a organização, garantindo consistência em todos os canais de vendas e serviços.15
2.2. Da Aquisição à Cotação: Venda Guiada e Gestão de
Oportunidades (CPQ)

O processo de vendas de telecomunicações é notoriamente complexo, com um vasto portfólio
de produtos, regras de compatibilidade complexas e modelos de precificação multifacetados.
O Salesforce Industries CPQ (Configurar, Precificar, Cotar) foi projetado especificamente para
dominar essa complexidade, orientando vendedores e clientes por um processo de cotação
sem erros.11

Uma capacidade fundamental é aVenda Guiada, implementado por meio de OmniScripts.
Esses fluxos de tela passo a passo simplificam a experiência do usuário, fazendo perguntas
contextuais para ajudar a selecionar o produto certo. Por exemplo, um fluxo poderia
perguntar: "Quantos funcionários sua empresa tem?" e "Qual é o seu principal uso de
internet?" para recomendar o plano de fibra óptica B2B mais adequado, ocultando opções
irrelevantes e evitando a paralisia da análise.22

O Configuração complexaEle é gerenciado por um mecanismo de regras robusto que
analisa a elegibilidade (este cliente se qualifica para a oferta de fibra?), a compatibilidade
(este decodificador 4K funciona com este plano básico de TV?) e a disponibilidade (há
capacidade de fibra neste endereço?). Isso garante que apenas configurações válidas
possam ser criadas, eliminando erros dispendiosos posteriormente no processo.20

Ele Precificação baseada em atributosPermite precificação dinâmica. O custo de um serviço
pode variar com base em diversos atributos, como velocidade da banda larga, uso de dados
móveis, duração do contrato ou localização geográfica. O Industries CPQ utiliza matrizes de
precificação para calcular automaticamente o preço correto em tempo real, conforme a oferta é

configurada.15

Talvez a capacidade mais diferenciadora do mercado B2B seja aCotação Multi-SiteUm
agente de vendas pode criar um orçamento único para um cliente empresarial que necessita
de serviços em centenas de locais, cada um com seus próprios produtos, preços e
configurações, tudo em uma única interface. Isso transforma um processo que
tradicionalmente levava semanas de trabalho manual em planilhas em uma tarefa simplificada
e centralizada.20O sistema foi projetado para a realidade das telecomunicações, onde a
maioria das transações não são novas vendas, mas modificações de serviços existentes, um
conceito conhecido como

Ordenação baseada em ativos, que é essencial para os processos MACD (Mover, Adicionar,
Alterar, Excluir).
2.3. Da Ordem à Ativação: Decomposição e Orquestração de
Provisões (OM)

Assim que uma cotação se torna um pedido, o complexo processo de atendimento começa.
O Industries Order Management (OM) foi projetado para automatizar e orquestrar essa
jornada, garantindo que os serviços sejam ativados com rapidez e precisão.10

O primeiro passo crítico é oDetalhamento do pedidoO sistema recebe o pedido comercial (o
que o cliente comprou) e, usando as regras definidas no Contrato de Compra e Venda (EPC), o
divide em uma série de produtos técnicos que devem ser provisionados. Um único produto
comercial, como um "Pacote Triple Play", pode ser dividido em dezenas de tarefas técnicas:
verificar a viabilidade da linha, enviar um técnico, instalar um modem, ativar o serviço de
internet, provisionar canais de TV, portar o número de telefone e, por fim, atualizar o sistema de
faturamento.17

Uma vez dividido, o pedido entra na fase de processamento.Orquestração. Usando o
Fulfillment Designer, uma ferramenta gráfica de arrastar e soltar, os arquitetos de soluções
podem modelar fluxos de trabalho de atendimento comoPlanos de Orquestração. Esses
planos definem a sequência de tarefas, suas dependências (por exemplo, a linha não pode
ser ativada
até que o técnico confirme a instalação do modem), chamadas para sistemas externos
(chamadas para ativação de rede ou sistemas de cobrança) e tarefas manuais que exigem
intervenção humana.34

Inevitavelmente, em um ambiente tão complexo, algumas ordens falham. Gerenciar essas
exceções é onde o OM demonstra seu maior valor.Gestão de Riscosmonitora proativamente
os pedidos em andamento e alerta os supervisores caso um pedido corra o risco de não
cumprir a data de entrega prometida (SLA). Se uma tarefa falhar completamente,

umFalloutEm vez de o pedido se perder no limbo sistêmico, o OM o captura e o encaminha
para uma fila de tarefas manual, onde um agente especializado pode analisar o erro, corrigi-lo
e retomar o fluxo de orquestração. Essa capacidade de gerenciar as consequências de forma
inteligente é crucial para evitar a perda de receita e a insatisfação do cliente, os maiores custos
ocultos da má gestão de pedidos.36

2.4. Da Ativação ao Serviço Contínuo: Gestão do Ciclo de Vida do
Cliente (CLM)

Para uma DSP, o relacionamento com o cliente não termina na ativação; está apenas
começando. A grande maioria das interações e uma parcela significativa da receita vêm da
gestão.
dos serviços existentes de um cliente ao longo de seu ciclo de vida. Esse conjunto de
processos é comumente chamado de MACD: Mover, Adicionar, Alterar, Excluir.42

A Nuvem de Comunicações é fundamentalmente projetada em torno deOrdenação
Baseada em Ativos (ABO)Cada produto ou serviço que um cliente comprou e ativou é
representado como um registro de Ativo no Salesforce. Quando um cliente deseja fazer uma
alteração, o agente de vendas ou de atendimento não começa com o carrinho vazio. Em vez
disso, ele recupera os ativos existentes do cliente e os carrega no carrinho para
modificação.20

Essa abordagem ABO nativa permite o gerenciamento perfeito dos cenários MACD mais
comuns:

●Mover: Um cliente se muda para um novo endereço. O agente inicia uma solicitação de

"Mudança", que aciona um fluxo de orquestração para desativar os serviços no local antigo
e ativá-los no novo.

●Adicionar: Um cliente com um plano de celular deseja adicionar uma nova linha para um
membro da família. O agente inicia uma solicitação de "Adicionar", adicionando o novo
serviço ao contrato existente.

●Mudar: Um cliente deseja atualizar seu plano de internet de 100 Mbps para 500 Mbps. O
agente realiza uma "Alteração" no ativo existente, e o sistema calcula automaticamente o
rateio do preço e aciona comandos de rede para ajustar a velocidade.

●Excluir:Um cliente decide cancelar a assinatura de um pacote de canais de TV
premium. O agente processa uma solicitação de "Excluir" para aquele serviço
específico.

Esses processos MACD não são tratados como simples tickets de serviço, mas como
transações comerciais completas que fluem pelos mesmos mecanismos de CPQ e OM que as

novas vendas. Isso garante consistência, faturamento preciso e o provisionamento correto de
alterações, transformando o que muitas vezes são pontos de atrito em oportunidades para
fortalecer o relacionamento com os clientes e gerar receita adicional.49
 Além dos MACDs, a
plataforma gerencia outros

Processos "na vida", como atualizar um método de pagamento ou alterar a propriedade da
conta, geralmente por meio de fluxos guiados para garantir uma experiência consistente e
eficiente.14

2.5. Da Consulta à Resolução: Suporte Omnicanal e Autoatendimento

Oferecer um atendimento excepcional ao cliente é um diferencial fundamental no competitivo
mercado de telecomunicações. A estratégia para alcançar esse objetivo baseia-se em dois
pilares: capacitar
agentes com uma visão completa do cliente e oferecem aos clientes ferramentas de
autoatendimento poderosas e fáceis de usar.

O cerne da solução é oModelo de Datos Customer 360, que está alinhado aos padrões do
setor de SID do TM Forum. Isso fornece uma estrutura de dados predefinida para modelar
entidades complexas de telecomunicações, como contas, assinantes, assinaturas, ativos, uso
de dados, faturas e histórico de interações. Essa visão de 360   graus é a base para todas as
interações de serviço.10

Para os agentes, essa informação se materializa naConsolas de Agente
PreconstruidasEssas interfaces de usuário foram projetadas especificamente para as
necessidades dos agentes de telecomunicações, exibindo as informações mais relevantes
rapidamente. Quando um cliente liga, o agente pode ver instantaneamente quem ele é, quais
serviços possui, seu histórico de cobrança e quaisquer casos de serviço em aberto — tudo isso
sem precisar alternar entre telas. Isso reduz drasticamente o tempo médio de atendimento
(AHT) e melhora a resolução na primeira chamada.10Uma das dúvidas mais frequentes em
contact centers de telecomunicações é sobre faturamento; ferramentas como o Billing Inquiry
Manager são projetadas para orientar os agentes na resolução eficiente dessas disputas.10

Para os clientes, a plataforma permite a criação dePortais de autoatendimentoPortais
robustos usando a Experience Cloud. Por meio desses portais, os clientes podem realizar
uma ampla gama de tarefas de forma independente, 24 horas por dia, 7 dias por semana,
sem a necessidade de entrar em contato com um agente. Os recursos típicos incluem
visualização e pagamento de contas, monitoramento do uso de dados, alteração de planos,
compra de complementos, relato de problemas técnicos e acompanhamento do status de um
pedido ou incidente. Ao redirecionar consultas de rotina para canais de autoatendimento, os

CSPs podem reduzir significativamente os custos do contact center e liberar seus agentes
para se concentrarem em questões mais complexas e de maior valor.14

Seção 3: Catálogo exaustivo de épicos e casos de
uso para nuvem de comunicações

A tabela a seguir consolida a pesquisa e a análise estratégica em um catálogo abrangente
de Épicos e Casos de Uso. Este recurso foi desenvolvido para servir como um acelerador
para as fases de planejamento, escopo e estimativa de projetos de implementação do
Salesforce Communications Cloud, fornecendo uma ponte direta entre os recursos da
plataforma e os resultados comerciais desejados.

Nuvem

Nome de
domínio

Capacidade
Nome

Épica
(resumo)

Caso de uso
(resumo)

Comunicaçã
o em
Nuvem

Gestão do
Vida útil
do Produto

EPC
(Empresa
Produto
Catálogo)

Catálogo de
Produtos
Unificado e
Ágil:

Estabelecer um
catálogo de
produtos
centralizado
como a
única fonte
de
VERDADEIRO
,
separando
as ofertas
comerciais
do
especificaçõ
es técnicas
para acelerar
o tempo de
lançamento
no mercado
(Time-to-Mar
k
e
et)
garantir
consistência
omnicanal.

Como
gerente de
produto,
Quero
modelar um
novo plano
de dados 5G
como um
oferta
comercial,
reutilizando
especificaçõ
es técnicas
existentes
(SFC/RFS)
para lançá-lo
em menos de
uma semana.11

Como
designer de
catálogos,
Eu quero criar
um pacote
"Bem-vindo
ao Lar" que
combinar
serviços de
Internet de
fibra, TV por
streaming e

uma linha de
telefonia
móvel, com
regras de
compatibilida
de que
garante que
apenas
oferecer
decodificador
es
compatíveis.1
6

Como
gerente de
preços,
Eu quero
definir
uma
promoção de
"50% de
desconto por
3 meses"
para
novo
clientes de
fibra e
estabeleça
seu
período de
validade para
que se
aplica e
expira
automática
me nte.15

Como
arquiteto de
TI, quero
que o EPC
seja
sincronizar
com o
sistema
faturamento e
o portal de
Autoatendi
mento
via
APIs  do  TM
Forum
para


