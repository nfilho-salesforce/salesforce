[Externa] Proposta Sales Force - PAT-20260813_100550-Gravação de Reunião
13 de agosto de 2026, 01:05PM
1h 12m 33s
Georges Leitao dos Santos começou a transcrição
Georges Leitao dos Santos   0:03
Está gravando já. Bom dia, bom dia, pessoal. A gente provocou que a reunião aqui, já tinha conversado aqui, estamos dando andamento na reunião de ontem. O objetivo aqui hoje, como eu coloquei lá no grupo, é a gente apresentar essa parte da arquitetura de vocês aí, dessa parte técnica do projeto e da parte data prev.
Nelson (Salesforce)   0:04
Okay.
Georges Leitao dos Santos   0:24
Alinhar o entendimento em que todos estão envolvidos, esclarecer eventuais dúvidas, acho que é importante pra gente seguir bem alinhado. Acho que o Nelson colocou algumas dúvidas ontem, acho que é hoje que o objetivo aqui é esse, para garantir que todo mundo esteja
Na mesma página aí e seguir na mesma direção. Então, a expectativa é que a gente saia daqui da reunião hoje com o entendimento único da solução. Aí eu vou depois passar para vocês aí todas as responsabilidades. Também acho que cada um da equipe, o que é a responsabilidade da Dataprev?
O que é responsabilidade da sales, o que é responsabilidade da do MTS, que é importante a gente ter essa divisão.
E para a gente poder seguir com os próximos passos necessários para a evolução do projeto. Então, por isso que foi provocado aqui até a reunião Danielson, até por sugestão aí da própria Nina, da equipe, para a gente poder seguir aí, acho que tem alguns entendimentos.
Tem novos membros aqui também da equipe aqui também. O Rigan já acompanhou, mas aí ficou de fora daquela reunião de ontem. Então é a parte de analítico, monitoramento, onde vai rodar a solução. Então é isso que a gente tem que alinhar aqui hoje é o objetivo da reunião.
É alguém aqui da Dataprev antes de passar aí palavra para Passagens?
Daniel Santos de Jesus   1:41
Oh Jorge, e peço já desculpas, eu estou chegando em 5 minutos e estou dirigindo, mas eu gostaria de colocar, acho que inicialmente um ponto importante aqui. Primeiro, para Seios, está claro quais foram os requisitos passados aí sobre do ponto de vista da Assunção.
Georges Leitao dos Santos   1:46
Tranquilo.
Daniel Santos de Jesus   1:58
Faltou algo, esse ponto de partida aí daquela proposta arquitetural, já contempla o que chegou até.
de requisito. É importante a gente dar esse ponto de partida, Jorge, que às vezes a gente está com uma visão aqui Fabricio sobre tudo, de quais são os requisitos. E a gente fazer esse depara com o Time 6 Force era importante, né? Porque a gente viu algumas situações ali na parte analítica.
que acredito que sejam as principais dúvidas. E esse seria um ponto de partida razoável pra gente começar aqui.
Georges Leitao dos Santos   2:30
Bacana, bacana. Jesus, é Fabricio, quer complementar aí?
Fabricio Gustavo de Paiva Vicente   2:35
Foram gerados alguns documentos, como Jesus disse, de recomendações da arquitetura, de pontos críticos pela área de analytics, inclusive sobre os dados, a totalidade dos dados estão aqui, o Rigan e o Paulo Paulo pode até falar melhor.
e também dos requisitos do Sistema. Os requisitos a gente teve um momento de apresentar e detalhar e ali a gente conversou e teve até uma devolutiva da Sales. Aí só para a gente deixar claro também desses pontos da arquitetura e da área de analytics, para a gente deixar tudo muito.
Todo mundo aliado.
Nelson (Salesforce)   3:13
Okay.
Daniel Santos de Jesus   3:13
Desculpa, Fabricio, isso envolve inclusive, aí eu acho que entra mais o Rigan, aquela estratégia de aonde é o processo, onde é o repouso. Estou falando mais na questão do ciclo de vida de dado, dado compilate da empresa. Isso vai ser processado e repousado em nuvem.
Tá claro a estratégia? Enfim, eu acho que esse é o ponto crucial, tá? Fazendo uma comparação das primeiras discussões, havia essa restrição escancarada lá, tá? O dado precisa ser processado e repousado na estrutura da dataprev e se não tiver errado.
É o que a Sergio apresentou ontem rodava e processava na estrutura deles, se não tiver equivocado da Mota.
Nelson (Salesforce)   3:58
é o deixa eu só primeiro apresentar aqui só o Eric e o Pedro né então eu Renato vocês já participaram já passamos de outras reuniões entrou se não entrou mais ninguém não por enquanto somos nós só apresentar o Eric
Pedro, então eles são arquitetos, é principalmente arquitetos técnicos da Costa Force. É ontem a Nina procurou dentro dos nossos recursos. Até agradeço ao Eric e ao Pedro pela disponibilidade, porque.
Como eu disse, a gente está ainda em processo de contratação e existe todo uma processos e compliance a respeito de alocação das pessoas. Então, reforçando, então a gente não está ainda com o time do projeto completamente definido, engajado, então é uma
Talvez algumas expectativas, você só fica um pouco preocupado, algumas expectativas de resposta, ou talvez ainda não tenham, a gente vai ter que construir junto, mas principalmente entender que o Pedro e o Eric estão começando esse.
esse projeto com a gente, esse trabalho com a gente para refinar a arquitetura, mas também para responder acho que pontos de dúvidas que vocês poderiam ter, principalmente sobre a plataforma, sobre como funciona. Não sei ainda, não é uma certeza se eles continuam e vão ser os arquitetos que vão realmente efetivamente trabalhar no projeto
Rigan Andre Campos Gonzalez   5:13
Call.
Nelson (Salesforce)   5:22
Ou se vai ser alguém até mesmo da própria estrutura do Eric, que ele também é. Tem uma estrutura de arquitetos embaixo dele. Então, mas de qualquer forma, não precisa se preocupar que toda essa transição, essa passagem de conhecimento para vocês vai ser transparente. Mas.
Foi uma forma de a gente poder começar, já responder as perguntas e já começar a ter as definições iniciais. Alguns dos pontos que colocaram, assim, se estão esperando uma resposta, eu acho que a gente precisa alinhar as perguntas porque eu não tenho. Por exemplo, sobre analytics, é uma delas. Não existe uma resposta, existe uma que a gente vai construir.
Porque não foi mapeado em pré-venda, até porque não tinha esses requisitos ou se tinha eu não ou eu comi bola ou eu não vi. Mas não algumas definições, elas simplesmente não existem. A gente precisa fechar. Tableau foi uma.
Uma delas, assim, muito, muito claro, a parte de analytics, como tinha todo um, como tinha uma premissa, vamos dizer assim, que seria feito dentro da estrutura Oracle, ela nunca foi aprofundada. Então não sei como é.
Como vai ser a transferência descida de informação? Como eu disse na reunião, eu não tenho essa resposta. É uma coisa que a gente realmente vai ter que desenhar juntos, esclarecer juntos. Rigan.
Rigan Andre Campos Gonzalez   6:42
Então, Nelson, assim, só pra dar uma dica, como Daniel Jesus falou, a gente construiu previamente a escolha do fornecedor, uma série de requisitos.
Que eram necessários pra gente. Uma série de decisões foram previamente tomadas, que embasaram uma nota técnica. Essa nota técnica, junto com alguns desenhos de arquitetura, estavam já desde o início pronto, o início de.
Nelson (Salesforce)   7:09
Mhm.
Mm-hmm.
Rigan Andre Campos Gonzalez   7:17
Não início zero, mas assim antes efetivamente da conversa com vocês. Então existe sim, várias requisitos, várias decisões que já foram tomadas pela Equipe da Dataprev e que eu acho que vocês precisam tomar consciência disso.
Nelson (Salesforce)   7:31
Mm-hmm.
Rigan Andre Campos Gonzalez   7:34
Porque a expectativa nossa é que aquilo seja atendido, principal.
Nelson (Salesforce)   7:35
Yeah.
Claro, mas esse ponto é bom, se permitir, então qual é a definição sobre o repositório de dados para alimentar o analytics da Oracle? Porque realmente eu não conheço e eu não documentei isso, então, e nenhum documento da Silva Soares tem este.
Este ponto está muito especificamente deste ponto. Não tem isso porque realmente não tinha definição. Então, se existe, é legal. A gente pode até começar por ele, porque eu não sei nem como apresentar qual que é. Eu realmente desconheço.
Rigan Andre Campos Gonzalez   8:08
Existia um requisito que os dados que são, na verdade, cadastrados, no caso, quando eu cadastro um contrato, quando eu faço uma cotação, num primeiro momento que esse dado ele tem que estar disponível dentro.
Da Dataprev tá aí tem que ver, deixa o pessoal da arquitetura Silva falar, você tá falando em Oracle, e eu não sei se a decisão que a Dataprev tomou é armazenar isso em Oracle, tá? A gente tem CDP claudera.
Nelson (Salesforce)   8:39
Yeah.
Rigan Andre Campos Gonzalez   8:40
A gente tem vários outros ambientes que isso pode ser armazenado, tá? Então aí teria que deixar o pessoal da arquitetura. Giovana já levantou a mão, mas assim, a nota técnica, ela fala isso das nossas necessidades para poder construir soluções.
Nelson (Salesforce)   8:45
Mhm.
There go.
Rigan Andre Campos Gonzalez   8:57
Que o cliente precisa, porque, na verdade, ele tem uma expectativa muito grande. Essa parte é uma parte mais tranquila que eu dei o exemplo. Mas depois, quando envolveu financeiro, ele tem uma expectativa que as transações que são feitas.
pelos beneficiários, eles sejam repassados e analisados em cima de uma lógica de análise de risco. E isso tem uma periodicidade, uma temporalidade muito mais curta.
Do que efetivamente um Painel é aonde eu mostro para ele quantos contratos aconteceram, quantas cotações foram feitas, tudo isso que vai começar a acontecer no momento que a gente lançar, eles já vão querer ver no dia seguinte.
Nelson (Salesforce)   9:36
Mm-hmm.
Rigan Andre Campos Gonzalez   9:44
Assim, lançou, apertou o botãozinho. A pergunta no minuto seguinte é, quantos contratos vocês já internalizaram? Quantos cotações você já fizeram? Mas isso é bem basicão, né? Assim, eu estou mais preocupado com a parte em que a gente lida com o monitoramento, que é o nome mais.
Nelson (Salesforce)   9:44
Mhm.
Mm-hmm.
Rigan Andre Campos Gonzalez   10:06
Todo uma análise de risco em cima do que está entrando de uso do programa, entendeu? Então, isso tem que estar dentro da plataforma da Dataprev para a gente poder efetivamente trabalhar.
Nelson (Salesforce)   10:12
Yeah.
Rigan Andre Campos Gonzalez   10:21
Como é que a gente trabalha hoje? A gente tem várias ferramentas internas que a gente trabalha isso, fortemente em cima do ambiente cloud dera, que a gente consegue fazer de dados em cima dele. Mas a gente tem muitas outras ferramentas. Aí eu vou deixar a Juliana falar, porque aí ela vai conseguir.
Eu sou um cara de negócio. Eu sou, na verdade, hoje, embora estatístico e etc, hoje eu estou numa função mais de gestão. Eu trabalho na superintendência diretamente de análise de produtos de analytics e dados.
Nelson (Salesforce)   10:40
Mm-hmm.
Mhm. No, they don't.
Rigan Andre Campos Gonzalez   10:57
Jovan Juliana Juliana.
Giuliana Silva Bezerra   11:00
Juliana, mais conhecida como Giovanna, né? Brincadeiras à parte, pessoal. Bom dia, todo mundo. Eu trabalho aqui na DIAD, só para deixar um contexto assim, não sei se vocês sabem como é que a gente trabalha aqui com arquitetura, mas a gente da DIAD trabalha muito em definir cenários.
Focados no analítico, né? A gente divide as aplicações entre transacionais e analíticas, tudo que tem uso analítico, seja B A, B A, Big Data, tudo isso a gente acaba elaborando esses cenários e há dias aqui representado até pelo Wallace, trabalha em cima desses cenários para definir qual
Nelson (Salesforce)   11:26
Yes.
Giuliana Silva Bezerra   11:36
o produto recebendo um requisito de produto, qual cenário ele se encaixa, e a gente trabalha muito junto aqui nesse sentido. Então, só para vocês terem conhecimento sobre a nossa estratégia, essa demanda, e aí eu não sei se vocês tiveram essa percepção,
mas o uso do dado é muito
eu vou até dizer exclusivamente analítico é esses dados que estão sendo gerados Claro pelos Sistema né pelas pelos pelos processos ali que podem considerar podem ser considerados uma aplicação transacional o uso que o cliente vai fazer é muito analítico para tomada de decisão
então o que que a gente faz aqui dentro da Dataprev no contexto analítico, Rigan já trouxe até alguns usos de dado analítico que a gente faz dentro das nossas plataformas, a gente usa esse dado ouro que a gente chama dentro da Dataprev, o dado ouro precisa ser da Dataprev
porque com esse dado aqui dentro a gente consegue usar as nossas diferentes plataformas sem perder autonomia em relação ao que pode ser feito em cima do dado, sem perder a proximidade do dado das plataformas de processamento, porque são grandes volumes, a gente não pode ficar transferindo de um lado para o outro, por exemplo, e aí
de vender tanto em questões de latência como até em questões de Banda mesmo né permitido nessas transferências questões de soberania segurança enfim interoperabilidade entre plataformas né então consumir um dado que seja legível por pelas diferentes plataformas que não tenha nenhum formato proprietário
Isso são requisitos que a gente entende como não funcionais, que vão ser adequar, vão ser necessário ser atendidos por qualquer produto que venha a ser criado aqui, provisionado dentro da Dataprev. Então, a gente tem realmente algumas plataformas, o Hidan colocou, né, plataforma para análise de risco, plataforma para batimento
informação, plataforma para construção de painéis, plataformas para permitir um multi self-service pela empresa, então os engenheiros de dados vem fazem análises, os cientistas de dados vem fazem análises, a gente tem essa necessidade de ter um dado ouro aqui dentro da dataprev
o dado que vai ser usado para o consumo analítico. Isso é um requisito importante que a gente precisa alinhar para ver se dentro da proposta de arbitras que vocês estão fornecendo o dado vai ficar aqui dentro. E se tiver algum nível de transferência de dados como é que vai ser lidado essa questão da latência?
E da temporalidade do dado, o tempo que ele vai chegar, que vai sair, questões de banda, tudo isso que a gente vai iria precisar considerar.
Nelson (Salesforce)   14:11
Tá legal, eu acho que tem na sequência. Eu acho que o Eric vai ser melhor para responder. É um ponto só que eu tinha colocado, gente, e é isso. Só que eu quero é dizer, porque, como eu disse, eu acho que a nossa arquitetura não responde essa pergunta.
Georges Leitao dos Santos   14:15
Wallace.
Wallace Roque de Figueiredo   14:17
Bastos in
Nelson (Salesforce)   14:27
Porque é não tinha exatamente a exploração dessa parte do analytics da Dataprev. Vocês veem na nossa proposta, ela não aparece. Então, assim, isso não é um problema se a gente precisar realmente persistir o dado para algum lugar.
De novo, zero problema, gente, não é isso. É que é só o fato de que eu não tenho a resposta, porque não está no nosso desenho de arquitetura exatamente esta, vamos dizer, esse requisito de que o dado tem que estar exposto, replicado numa base local.
Não existe nenhum momento da proposta, vocês vão encontrar isso porque não tem, porque também não tinha definição. Mas de novo, não é que a gente não tenha e não vai resolver. Eu só quero dizer que eu não tenho a resposta dentro do desenho de arquitetura porque realmente ela não foi dada.
A solução, tá, gente? É só isso. Então, só pra alinhar a expectativa mesmo, assim, de que eu não tenho a resposta pronta, mas a gente vai encontrar uma.
O próximo, desculpa.
Wallace Roque de Figueiredo   15:28
não não só complementar aqui rapidamente né a Ju e o Rigan já falaram bastante coisas aí que que tava aqui no meu radar para falar mas a gente também não vai chegar aqui já te dar uma solução ao cara
Georges Leitao dos Santos   15:28
No.
Wallace Roque de Figueiredo   15:44
Porto que você tiver aqui, vamos começar a fazer a transferência de dados. É o que você falou desde ontem, não é? A gente pode fazer essa construção juntos, não é? Então é, eu acho que essa fase agora é realmente de alinhar essas expectativas.
Nelson (Salesforce)   15:59
Mm-hmm.
Wallace Roque de Figueiredo   16:00
e chegar juntos aí na melhor solução possível, tá? Então, eu acho que agora tá bastante claro aí qual é a necessidade da Dataprev de do recebimento desses dados e a gente senta e vocês apresentam um pouco do
O que é possível ser feito com a plataforma de vocês, não é? Eu já tinha tido um contato prévio aí com uma outra demanda. É, e aí eu acho que ficou um pouco mais claro para mim. Eu tenho certa tranquilidade até com relação a isso.
Mas aí apresentar para o restante aí para Juliana e outros times, outros arquitetos que estão aqui também, para a gente ver qual a melhor estratégia para recebimento desses dados.
Nelson (Salesforce)   16:49
Perfeito.
Eric (Salesforce)   16:51
Pessoal, só comentando, eu participei do início do projeto da UNA, também no Dataprev, e assim, a gente tinha uma série de requisitos também de não persistir o dado aqui, persistir lá, isso tinha que ficar na infra e.
E isso dentro do projeto, a gente já sabia de cara da maioria dos requisitos. Alguns surgiram durante o projeto. É natural, né? Como todo projeto, quando você entra no detalhe ali, ele realmente aparecem coisas que a gente precisa se adaptar.
e a gente conseguiu atender plenamente. Então, assim, eu acredito que o projeto ainda não estar todo do nosso lado, acho que não teve alocação ainda, como o Nelson comentou, mas isso são detalhes que vão ser discutidos nos requisitos de vocês, quando a gente
Quando tiver que escrever as user stories, com certeza a gente vai ter que entrar em muito mais detalhe de homologação. Como que a gente faz durante a homologação? Como que faz transferência? É cadeia do que já está pronto de vocês de APIs? O que não estaria?
Qual a melhor maneira de se integrar? Então assim, eu estou caindo de paraquedas, o Nelson me chamou ontem, então não participei nem da definição de pré-venda, então assim, não quero falar nenhuma besteira aqui, mas queria dar essa tranquilidade de que é normal assim que a gente começar o projeto, a gente entrar realmente nos detalhes, o arquiteto que for.
vai conseguir entrar nesse nível de detalhes e fazer isso. Lá no Projeto Uno, por exemplo, a persistência dentro dos seus forces é mínima e de campos que não são críticos para vocês. Então, cada um dos itens foi negociado com a estrutura que estava ali de projeto com a gente.
Nelson (Salesforce)   18:17
Okay.
Eric (Salesforce)   18:32
o que a gente poderia gravar ou não, algumas dificultou bastante o nosso projeto, mas faz parte, então a gente entendia as necessidades ali, por ser governo, por ter toda uma parte ali de segurança importante para vocês, e a gente foi adaptando as histórias, foi adaptando as
entregas e entregou com sucesso. Então, eu acho que é importante a gente ter essa relação de quais são os requisitos que já estavam quando o contrato foi fechado, perfeito, e se tem coisas novas, a gente ter conhecimento disso, mas
Passa essa tranquilidade que durante o projeto, mesmo durante os refinos, isso vai ser muito mais mais tranquilo e transparente.
Nelson (Salesforce)   19:21
Valeu Eric. É OK, até para a gente ditar aqui, acho que qual é o melhor formato aqui para a gente trabalhar não só nessa, mas nas próximas reuniões.
É melhor a gente já pegar esse tema e vamos aprofundar, ou a gente vai fazer um Panorama geral da arquitetura? Como vocês acham melhor a gente mais produtivo aqui?
Georges Leitao dos Santos   19:47
Acho que poderia, acho que a gente poderia fazer um acho que eles poderiam fazer um panorama geral aí o não assim debatendo ponto a ponto aí acho que fica mais interessante. Não sei se os demais aí pode seguir nessa linha aí Fabricio, Jesus, entendeu?
Nelson (Salesforce)   19:53
Ótimo, a legal, está bem.
Fabricio Gustavo de Paiva Vicente   19:57
Eu acho que talvez fosse até interessante, Jesus e Rigan, talvez abrir o documento, falar dos pontos críticos do documento.
Nelson (Salesforce)   20:06
But
Pode ser também, porque o que eu tenho é o meu, o meu documento, então não sei se ele é o melhor pano de fundo, sabe? Ou se vocês querem colocar, por exemplo, exatamente esse documento com os termos da nota técnica, senão eu abro aquele meu desenho, que é aquele que eu já abri na outra reunião, já compartilhei também com.
com Eric e com o Pedro. Com Eric e o Pedro, até desse pouco tempo que eu tive de dar um banho de loja neles, eu foquei bastante nas jornadas para eles entenderem o processo como um todo, porque fica muito mais fácil de entrar no projeto e entender alguns pontos que a gente vai comentar e como que eles se conectam.
do Connect, né? Então eu foquei bastante em dar um banho de loja neles, do que se trata a solução, né? O contexto do PAT, a solução, principalmente direção ali as jornadas, do que entrar em pontos específicos sobre como é que vai ser a integração com o novo PAT, etc e tal.
Só pra é também esclarecer o nível de profundidade que o Eric e o Pedro estão do projeto. Mas como eu entendi que um dos focos hoje muito importante era exatamente esclarecer sobre.
Plataforma, dúvida sexy de plataforma, por exemplo, como residência de dados, a exemplo, eles, independente do contexto, conseguem contribuir, responder muito bem, então.
Só para que seja mais produtivo e te alcance maior expectativa possível. Por isso que eu fiz essa parada aqui, só para a gente entender como.
como a gente se orienta daqui para frente né se colocamos a a plataforma e se vocês quiserem já trazer essas dúvidas esses Pontes a gente vai respondendo aí vocês me ajudam aqui só para como
da forma mais produtiva possível.
Rafael Roquette (Salesforce)   22:08
Uma sugestão Nelson, e pessoal deixa eu me apresentar, eu sou Rafael Roquete, gerente de projetos aqui da Salesforce, mas como uma sugestão, tanto o Eric quanto o Pedro, por mais Nelson que você tenha feito aquela passagem que você fez ontem, eles tenham ali o conhecimento por conta do que fizeram no UNA,
Nelson (Salesforce)   22:08
Yeah, what?
Oh, half.
Rafael Roquette (Salesforce)   22:26
A gente ainda vai precisar de uma descoberta mais profunda de tudo que está sendo proposto, tudo que é pedido e tudo mais. Eu entendi até ontem do que o Georges até propôs essa reunião para que a gente pudesse adiantar e dar mais segurança para vocês em termos gerais, as dúvidas que vocês têm em termos gerais. Vocês estão
Com certeza, quando vocês olham toda a programação que foi feita, surgem esses questionamentos como esse que acabamos de discutir com Eric. Talvez hoje aqui a gente não saia já com um plano, já com a definição da arquitetura, até porque isso vai ser construído logo nos primeiros dias, quando a gente começar a locação.
Então, a minha sugestão, Georges Wallace, é que a gente time aqui todo, que a gente foque no que vocês entendem que poderia ser o ponto crítico, que vocês não entenderam como é que seria feito, ou pontos de atenção que vocês têm internos, que vocês sabem que.
Que vale a pena a nossa arquitetura saber e discorrer e a gente tentar aqui no máximo só para vocês, é.
Só para botar todo mundo na mesma página, Nelson, de que a integração do Eric e do Pedro, ela é ainda pequena, para que a gente aprofunde, por exemplo, a arquitetura completa de como vai ser o trabalho.
Nelson (Salesforce)   23:27
Go on.
Rafael Roquette (Salesforce)   23:39
Só uma sugestão, tá pessoal?
Nelson (Salesforce)   23:41
Eu gosto de A Ricardo de contribuição. Eu gosto se tiverem de acordo.
Georges Leitao dos Santos   23:43
So, the
Daniel levantou a mão eu Jesus
Daniel Santos de Jesus   23:47
Não, tranquilo, eu ia pedir exatamente o que está na tela aí como antifatina.
Nelson (Salesforce)   23:51
É um plano de fundo, né? É.
É, então coloquei exatamente aquele desenho que nós tínhamos ali, que é o que a gente trouxe na proposta para apresentar, montar, apresentar a proposta e validar. Ela fica como plano de fundo e a gente consegue ir discorrendo em cima dela. Como eu disse, existem alguns elementos aqui que preveem funcionalidades que estão em Rodrigo, por exemplo, a parte de agente.
De data cloud, como eu já tinha mencionado, então esse aqui a gente montou essa arquitetura quando a gente estava olhando a foto muito, talvez olhando também mais para o futuro, recursos que a gente acha que vai trazer benefício, mas como?
A gente fez muito o planejamento orientado a um prazo, uma parede de data muito rígida, muito séria a ser seguida. Então, algumas funcionalidades elas não consideram nessa fase, igual os agentes. Então, vou mencionando aqui os itens, só que a gente não tem que.
A princípio, não, mas eu acho que é basicamente a parte de agentes de data cloud que não estão realmente dentro do escopo dessa primeira fase. Um ponto, acho que talvez falar sobre a questão de plataforma e de residência de dados, talvez acho que seja o primeiro ponto.
É que pode trazer dúvida, entender se é muito claro, então nós temos dentro dessa o core, na verdade, de todos os dados, todos os objetos, de tudo que a gente vai receber de dados de integração.
E os transacionais que a gente vai ali quando fala de cadastro de estabelecimento, o cadastro de das oportunidades, respostas às cotações, elas acontecem dentro do Sales Cloud, dentro do core. Então a gente exatamente é.
Personaliza esses objetos, a gente está numa pegada muito de utilizar alguns objetos que já são nativos da plataforma, porque eles já trazem algumas features, vamos dizer, até mesmo a questão de compartilhamento de dados, mas.
Esses dados, eles ficam, eles são, é, vamos dizer assim, eles são armazenados e controlados, esses metadados pelo core, essa camada aqui intermediária, Rafa.
Rafael Roquette (Salesforce)   26:10
É Nelson, quando a gente começou a fazer o serviço na ponta, a discussão e eu estou vendo CDP Oracle aqui do lado e aí queria fazer uma provocação aqui, porque a discussão que passou muito sobre os dados sensíveis dos cidadãos.
Nelson (Salesforce)   26:26
Okay.
Rafael Roquette (Salesforce)   26:26
Que não poderiam estar armazenados em nuvens que eles chamam de nuvem pública, mas seriam as nossas nuvens. Por mais que a gente tenha ali todas as comprovações de segurança e tudo mais. Bem, por uma questão também de estratégia de governo e por aí vai. Eu estou entendendo que.
Nelson (Salesforce)   26:33
Is.
Rafael Roquette (Salesforce)   26:42
Tudo que a gente for fazer aqui vai trabalhar dados sensíveis. A gente está falando de dados das empresas, tamanhos de contratos e tudo mais. A solução que foi feita do lado do Serviço na Ponta foi inicialmente a gente só trabalhou com agentes informacionais, ou seja, trabalhando dados públicos.
E vamos começar agora a trabalhar com transacionais, mas usando a base do CDP Oracle que nos passa dados por zero copy. Aí zero copy é uma nomenclatura Eric Pedro aqui nossa, né? O ponto é, eu estou entendendo que essa mesma arquitetura que foi construída lá vai ser refletida aqui.
Certo? Ou seja, os dados não vão ficar armazenados dentro da nossa estrutura ou não.
Nelson (Salesforce)   27:21
Okay.
Não, não, não é o Core. Então a gente tem o objeto e a residência dos dados do transacional no Core. Por isso que eu achei legal exatamente a gente colocar esse ponto, porque eu acho que ele é o primeiro a ser muito bem esclarecido e entendido. Então.
Acho que a gente tem toda uma questão de classificar o dado sensível, então quando a gente fala, por exemplo, dado de cidadão perfeito, não está aqui, não tem residência de cidade aqui, mas, por exemplo, o credenciamento do estabelecimento.
Rafael Roquette (Salesforce)   27:52
Mhm.
Nelson (Salesforce)   27:57
A gente utiliza a estrutura de objetos de conta do Core. Então, por mais que eu possa persistir, a gente tem o shield para mascarar, a gente pode persistir esse dado e, sei lá, fazer algum tratamento depois que essa informação é, sei lá, enviada para o PAT, ou desce para o CDP, a exemplo.
OCDP do Amaral a gente colocou aqui, inclusive dentro da arquitetura, porque ele faz parte. Mas como eu disse, se o que não existe é, eu tenho um requisito que depois que, sei lá, a cotação foi ganha, eu tenho que pegar esse dado, mandar para o CDP e apagar. Esse requisito não tem. É isso que eu estou querendo dizer, que não, por mais que.
Rafael Roquette (Salesforce)   28:32
Yeah.
Nelson (Salesforce)   28:33
Que possa, ele faz parte da arquitetura, são componentes que a gente já está acostumado a trabalhar na dataprev, mas eu não tenho dentro desse projeto este requisito definido. E não só discutido, mas também muito francamente, eu não vi isso. Até por isso que eu falei para o Rigan que que era esse requisito, porque.
Rafael Roquette (Salesforce)   28:42
Boa.
Nelson (Salesforce)   28:52
Realmente desconheço, é, mas a gente sabe mais ou menos já como funciona a.
Os requisitos de sobre a linha de dados e o que a gente tem aqui de ferramentas na mão. Quando eu falo do processo, vamos focar aqui na primeira jornada, que é a de registro da oportunidade pela beneficiária. Então, ela tem a necessidade de comprar um produto, ela vai registro.
Essa intenção dentro do portal, aí só fechando aqui um pouco da arquitetura. Essa primeira camada, vamos dizer assim, ela é a camada de interface de front-end. Então todos os objetos, os dados, eles estão dentro dessa segunda camada do core.
E Pedro, Eric, por favor, fiquem à vontade para me trampar e me corrigir a qualquer momento. Mas essa primeira camada, ele faz exatamente a interface, o front-end. Então a gente expõe esses objetos a partir do portal, tanto do perfil beneficiário quanto do estabelecimento. A gente expõe esses objetos para que seja a interface.
Para eles poderem cadastrar, mas esses dados estão sim residindo no Core. O Core, ele fica, ele é um dado em nuvem, sim, da plataforma de seus Force. Só que vocês têm esse dado no Brasil, né?
Então, ele fica hospedado no na astrologia da WS, que fica aqui em São Paulo. Segundo barulho. Segundo.
Eric (Salesforce)   30:10
O.
O Nelson, mas esse é um ponto bem importante, então acho que é importante validar com o Dataprev. Ok, quanto a isso, pessoal? Assim, a gente vai persistir alguns dados, pelo que eu entendi, de empresas, de quem está solicitando ali dentro dos seus forces.
Nelson (Salesforce)   30:19
Sim.
Isso.
Eric (Salesforce)   30:29
Isso na visão de vocês também, tá ok?
He.
Giuliana Silva Bezerra   30:35
Já pode abertura para dúvida sobre o desenho?
Nelson (Salesforce)   30:38
Acho que sim. Acho que pode ser conversa mesmo, né? É.
Eric (Salesforce)   30:39
Sim.
Giuliana Silva Bezerra   30:43
uma pergunta eu não tô entendendo o papel do CDT nessa solução eu sei que ele foi usado por serviço na ponta porque tinha um objetivo ali realmente de marketing né de enviar promoções ali para os clientes enfim notificações eu não tô entendendo qual é o papel dele aqui dentro do contexto do Pass vocês poderiam explicar
Nelson (Salesforce)   31:00
Boa.
Ele, na verdade, não tem um papel. É isso que eu estava comentando no começo. Não existe um papel definido para o CDP ou para qualquer outra forma de persistência do dado em qualquer ambiente on-premise do DataprevRJ, porque, como eu disse no começo, eu não tinha este requisito, então.
Eu coloquei o CDP aqui dentro da arquitetura, porque ele já é um recurso conhecido que nós temos para poder fazer residência de dados dentro da dataprevvoeturcombr dentro da dataprevvoeturcombr.
vamos dizer assim, repository on-premise, conhecido por nós, e por isso ele aponta, eu coloco ele dentro da arquitetura, mas, como eu disse, eu não tenho nenhum requisito que no final eu falo, muito bem, pegue esse dado e replique para cá. Eu não tenho, é exatamente o que a gente precisa desenhar. Eu nem sei se ele é a melhor opção também.
Rafael Roquette (Salesforce)   31:51
Então, a princípio ele nem entraria, porque quando eu vi eu também estranho porque que está aqui. Então ele nem casa muito com até a ideia total. Mas essa pergunta do Eric, pessoal, acho muito importante da gente ter ela muito clara. Ou seja, todos os dados que a gente trabalhava vão ser persistidos dentro das nuvens da Salesforce.
Nelson (Salesforce)   31:57
These.
Rafael Roquette (Salesforce)   32:10
Com todas as camadas de segurança e por aí vai. Eric e Pedro podem falar com mais categoria técnica, mas essa validação acho que é muito importante, porque ele é um ponto de partida muito significativo para definição de arquitetura. Eric?
Eric (Salesforce)   32:24
Perfect.
Giuliana Silva Bezerra   32:25
Ao meu ver, então, acho que a gente tem que fazer um próximo papo para alinhar essas Fontes de dados, porque o CDP como Fontes de dados, ele não se sustenta dentro da arquitetura, ele é muito mais do que isso. Então a gente pode combinar um alinhamento para entender.
Porque a gente tem outras formas de disponibilizar dados, a gente trabalha com nuvens públicas também e nesses cenários a gente tem uma estratégia de consumo de dados arquitetural que a gente pode apresentar para vocês e adaptar para funcionar nessa solução ponta a ponta, para a gente poder adaptar a arquitetura.
Nelson (Salesforce)   32:46
All right.
Rigan Andre Campos Gonzalez   32:51
As in.
Giuliana Silva Bezerra   32:58
Não sei se nesse momento seria agora ou se seria num outro momento, até porque essa agenda está com, talvez está com a previsão de tempo, de duração, enfim, eu não sei como é que vocês estão aí e o que vocês acham.
Rafael Roquette (Salesforce)   33:09
Boa, não, perfeito. A gente pode deixar, Juliana, esse ponto como um ponto de esclarecimento logo de início para a gente fazer o desenho definitivo, entender se realmente é necessário, de onde vai vir os dados. Eu estou entendendo que o CDP vai ser um grande.
A proposta estratégica, pelo que eu vi aí dentro com vocês, a ideia é que ele seja um grande repositório de todas as bases que vocês têm de várias Fontes, inclusive as internas que vocês têm.
É, e também não sei o que a gente usaria disso, se isso já está pronto, como é que seria esse ponto?
Nelson (Salesforce)   33:44
E um pouco de Pessoas de Pessoas de Pessoas, não necessariamente também precisa ser persistido o dado para uma estrutura on-premise e para ele poder ser consumido pelo Analytics, que eu comentei até ontem. Essa informação, desde que, vamos dizer, ela é entendida, que pode ficar nessa plataforma.
Giuliana Silva Bezerra   33:44
Então, essa visão é.
Rigan Andre Campos Gonzalez   33:45
Okay.
Nelson (Salesforce)   34:00
No vida se esforce, que ela não tem um dado, é.
Sigiloso que não pode estar aqui. Ele simplesmente tem um token que aponta para algum lugar onde tem a informação completa e que faz residência dentro do data center de vocês. Mas, por exemplo, a informação do analista ele pode consultar, inclusive dentro da cloud, nem precisaria persistir.
E acho que é exatamente esse um dos pontos. O que a gente entende de informação transacional que a gente está correndo dentro do marketplace, vamos chamar assim, a solução dentro do marketplace, que não pode ficar residida na cloud, que precisa ser persistida, e que a própria analítica não pode consumir aqui.
Rigan Andre Campos Gonzalez   34:40
Então, Nelson. Tá, desculpe, Juliana.
Giuliana Silva Bezerra   34:40
Só para essa, só deixa. Eu só queria alinhar antes de passar a palavra um ponto sobre o CDP, essa estratégia dele ser um repositório de dados global, ela não existe em termos de arquitetura. A gente não alinhou isso aí, tá? Eu acho que é importante a gente.
Nelson (Salesforce)   34:53
Okay.
Giuliana Silva Bezerra   34:55
Alinhar aqui o CDP, ele foi usado para a demanda do serviço na ponta. Beleza, atendeu aquela necessidade, mas a gente não estruturou nada em termos de arquitetura mestre para esse cara ser usado como repositório. Até por isso que eu propus um outro papo de alinhamento.
para a gente apresentar para vocês qual é de fato a nossa estratégia para ser bidados para ambientes de nuvem.
Rafael Roquette (Salesforce)   35:19
Perfeito Junior, perfeito.
Rigan Andre Campos Gonzalez   35:21
Beleza, Nelson, então é só pra marcar a posição. Você tem sim esse requisito que o dado tem que estar dentro do ambiente DataprevRJ, porque agora a gente falou pra você que esse requisito existe, tá? Então assim.
Nelson (Salesforce)   35:34
Mhm.
Rigan Andre Campos Gonzalez   35:35
É efetivamente, pra gente ter celeridade e desempenho em cima da analytics que o cliente quer, a gente precisa estar com esse dado dentro da infraestrutura dataprev. Então, assim, eu fui na primeira reunião com vocês, eu falei isso, eu me lembro claramente.
Nelson (Salesforce)   35:45
Okay.
Tá bom.
Rigan Andre Campos Gonzalez   35:51
Pode ser que eu tenha perdido algumas outras reuniões no meio do caminho, porque, afinal de contas, são muitas reuniões e como eu tô representando superintendência, eu tenho minha agenda, por exemplo, essa hora hoje eu tinha 3 reuniões simultâneas, tá? Então desculpe realmente se em alguma eu não fui.
Mas eu lembro que inicialmente eu tive lá o com certeza Daniel Jesus também foi algumas vezes e eu tenho bastante confiança de que esse requisito tenha sido colocado internamente. Mas tá ok, né? Agora ele existe, tá? A gente tá falando claramente.
Nelson (Salesforce)   36:20
Yeah.
Okay.
Rigan Andre Campos Gonzalez   36:24
Que eu posso consumir dentro da nuvem, cara, isso traz um uma complexidade e uma latência que teoricamente não atende o que a gente tem, o que a gente está esperando. Então, na verdade, esse requisito está posto.
Nelson (Salesforce)   36:38
Mhm.
Rigan Andre Campos Gonzalez   36:40
Pra ti, tá? Então a gente realmente precisa desse dado dentro da infraestrutura DataprevRJ. Como vai ser feito isso? Aí a Juliana ajuda a gente, diz o que a gente, na verdade, normalmente usa, mas a gente tem expectativa que vocês gravem esse.
Nelson (Salesforce)   36:41
Couple.
Rigan Andre Campos Gonzalez   36:57
Esse dado lá e tem um itemzinho que eu não estou vendo aqui, que é muito mais crítico do que essa base de estabelecimento, essa questão de cotações de contratos, que é o monitoramento em si. Não sei se isso.
Eu me lembro também de ter sido falado, mas assim, a expectativa do cliente é que.
Depois de efetivamente o contrato ser feito, tem toda a parte do financeiro que efetivamente o dinheiro vai ser repassado, mas quando a pessoa física for usar lá o consumo daquele benefício que é o
Para a FAT, este dado vai ser enviado sobre esta transação para a plataforma. Em cima disso é que vai ser, que isso é que se chama monitoramento, né? O monitoramento que está aqui é exatamente este acompanhamento do uso do programa.
E isso é violentamente grande, é uma quantidade de processamentos muito grandes e que eles precisam para fazer algum tipo de análise, eles precisam estar dentro do nosso ambiente. Então, isso me preocupa um pouco, porque eu não vi muito isso citado aqui, embora
Agora, dentro das reuniões que eu participei antes, aparentemente tinha falado claro.
Mais um ponto que eu acho importante, aí eu vou provocar um pouquinho o nosso pessoal interno do transacional. A definição, se aquele dado pode persistir ou não, ele precisa de uma análise da nossa área de segurança.
Eles é que na verdade tipificam isso. Então, assim, eu como dados, não consigo responder se esse dado pode ficar ou não na nuvem da Salesforce. A gente vai ter que ter aí. Não sei se isso foi feito, mas a gente vai ter que ter uma passagem aí.
Para perguntar a efetivamente se esse dado pode ficar ou não do ponto de vista de analytics, como a gente tem a expectativa do dado tá aqui dentro, na verdade, a gente precisa de uma autorização.
Só para a gente poder efetivamente usar o dado, e isso o cliente, na verdade, vai buscar essas autorizações. Então, assim, do ponto de vista de segurança, eu acho que a gente tem um passo aí para fazer, gente, que é avaliar.
Se existe restrições, porque assim, um pedaço disso é o financeiro, a gente vai transitar dados que são dados de dinheiro das pessoas, ou pelo menos.
Quanto ela vai cada um, o Joãozinho, ele vai receber tanto de auxílio alimentação, de auxílio refeição. Então esse é um dado pra mim já bem sensível. O contrato em si, aí eu não sei te dizer, porque aí tem uma questão.
Então, entre 2 partes, que é o contratante e a.
E aí eu não sei se efetivamente esse dado existe, não é só pra pontuar isso, mas o mais importante pra mim é assim, o requisito agora existe, tá Nelson? É só pra você saber. Na verdade, agora ele tá posto. Se não tava antes compreendido, agora ele tá posto, tá bom?
Nelson (Salesforce)   40:09
Mm-hmm.
Não, claro.
É e não é negando o requisito também não tá aí eu falei o único problema que eu não sabia explicar porque não definimos só isso então eu entendo que tinha assim sempre foi mesmo dito né que tinha a a questão do Analytics a gente sempre pontou muito bem o papel do aqui dentro né que não era de substituir o Analytics algumas a gente já falou que
Seria talvez uma estrutura de analistas do Oracle, por isso o CDP já venceu na cabeça, e também porque a estrutura que a gente conhece é exatamente por causa do serviço na ponta. Mas não é nem negando o requisito, é só que eu não tinha uma resposta porque não concluímos como seria só.
Nesse ponto, mas está claro, eu sei que existe um ponto, só que você mencionou que não está, não está sendo sedado muito aqui, quando você falou da das movimentações, você está se referindo exatamente ao crédito por bens de competência.
Para o Trabalhador, é disso que eu estou falando, certo? É dizer que o João, o mês tal, vai receber tanto. O que é?
Rigan Andre Campos Gonzalez   41:14
Não.
Não me ajuda aí, Jorge. É o uso do programa pela isso, a compra.
Nelson (Salesforce)   41:19
Okay.
A conta?
a compra o pagamento a refeição com o cartão
Rigan Andre Campos Gonzalez   41:28
Isso, Jorge, me ajuda aí, não é isso ou isso está fora deste escopo aqui inicial?
Nelson (Salesforce)   41:33
E isso a gente falou sobre isso. Está no a gente. Isso foi mencionado sim na nas apresentações que fizeram, mas não como um requisito do 15 de novembro. Aí me corrige se eu estiver errado. Eu entendi assim, é.
Georges Leitao dos Santos   41:40
Team.
Não é do 15 é não é o olha só do 15 de novembro é o item da compra ainda não tá no 15 de novembro o item da compra mas aonde foi comprado o horário é e outros pontos que servem para fiscalização
Rigan Andre Campos Gonzalez   41:53
Victoria.
da tabela.
Right.
Georges Leitao dos Santos   42:01
Esse tem que ter uma API que seja da facilitadora para informar para a plataforma, para a gente montar esse painel, para saber então o uso desse vale alimentação ou refeição. Então beleza.
Rigan Andre Campos Gonzalez   42:04
Anderson.
Nelson (Salesforce)   42:09
Okay.
Rigan Andre Campos Gonzalez   42:10
então então eu tô certo Jorge é nada na verdade assim o item da compra não vou ter mas a movimentação da compra já vai ter nesse nesse escopo
Georges Leitao dos Santos   42:17
Isso.
Sim, já, sim.
Nelson (Salesforce)   42:24
Vai? Não, eu entendi que não, tá gente? Então já é bom a gente alinhar aqui. Porque quem processa, quem tem esse registro da compra é a facilitadora ou a adquirente, por exemplo.
Georges Leitao dos Santos   42:28
Oh, sim.
Uh, uh.
Adquirência, no caso.
Nelson (Salesforce)   42:43
Adquirente, né? Então, e a gente não tem a integração adquirente de mandar a movimentação, né? E até um outro ponto, até falando em arquitetura, se a gente tem uma, por exemplo, de novo, né?
Georges Leitao dos Santos   42:52
Mas foi isso foi isso foi bem debatido nas reuniões, cara. Isso foi bem debatido nas reuniões que a gente colocou.
Nelson (Salesforce)   42:56
Não foi. Eu conheci, não é? A gente conversou. Só que o que também eu entendi é que não era como a gente tinha um 15 de novembro e a gente focou o escopo dentro do 15 de novembro.
Esse ponto eu entendi que ele não era, não fazia parte dessa, desse escopo, vamos dizer, essa entrega.
Eric (Salesforce)   43:13
Pell
Só, só um ponto.
Georges Leitao dos Santos   43:19
Oi, Eric.
Eric (Salesforce)   43:19
Só um ponto, porque assim, já fiz muitos sistemas relacionados a ao setor bancário aqui e esse é o tipo de informação que.
Raras vezes faz sentido estar dentro dos seus esforços, mas muitas vezes ela precisa ser visualizada de dentro dos seus esforços. São coisas diferentes. Então, se eu tiver uma API do banco, de um sistema interno, seja lá o que for, onde vocês já tenham essas transações.
Nelson (Salesforce)   43:32
East.
Perfect.
Eric (Salesforce)   43:44
Que quando o usuário ali precisar ver, ele vai clicar, ele vai visualizar ela, beleza, não sei se está no escopo ou não, isso não importa, mas assim, em termos técnicos, isso é muito fácil de fazer, o que me assustaria se a gente tivesse que importar para a plataforma, porque o volume deve ser gigantesco.
Nelson (Salesforce)   43:53
Perfeito.
These.
Eric (Salesforce)   44:01
Então, eu evitaria isso ao máximo, até por segurança de vocês, tudo, mas a visualização tende a ser normal, desde que a gente tenha um lugar tranquilo de, ah, eu tenho o ID do cliente, seja lá quem for, me dá as transações dos últimos 30 dias e a gente apresenta para o usuário.
Nelson (Salesforce)   44:20
É perfeito. É porque é um ponto que eu ia falar, porque eu entendo que isso é muita informação analytics. Então eu imagino que não faz sentido ficar na plataforma, obviamente, eSIM exatamente nesse repositório que vai ser o repositório analytics. Acho que ele tem que receber essa movimentação, porque no final.
Esse dado, ele é analítico. Um ponto que a gente fala, eu posso ser a camada de apresentação dessa informação. Só que a gente não tem no marketplace a visão, por exemplo, a quem este consumo vai interessar. Vamos falar assim.
Entendo que OMTL, ele quer exatamente monitorar o consumo disso. Então eu não vou apresentar isso. Primeiro que eu não tenho, obviamente, um portal é do cidadão para dizer, deixa eu ver o que eu comprei. É a beneficiária.
Talvez poderia apresentar essa informação do consumo, mas.
Essa informação, que destino ela vai ter dentro da plataforma? Se não, eu acho exatamente como o Eric falou, ele tem que existir, registrar. O Marioft pode ser a camada de API entre adquirente e o repositório final.
com toda certeza é
Mas talvez a residência dessa informação, desse volume dentro do marketplace, sendo que ele não é OA capa Analytics, fica.
Talvez não seja o modelo de arquitetura correto.
Rafael.
Georges Leitao dos Santos   45:45
Antes de passar a palavra aí pro pro Rafael Rafael só para deixar bem claro, Nelson, que uma das expectativas lá do do MTE é justamente esse monitoramento, cara, a gente tem que ter, tem que ter isso em mente, tá? É porque pensa assim, eu tô falando hoje com.
Rafael Roquette (Salesforce)   45:45
Yeah, ah, pode falar.
Georges Leitao dos Santos   46:00
com a cabeça do auditor, do auditor de trabalho. Ele quer lá ter o conhecimento, se está passando lá no estabelecimento, está passando numa borracharia ou se está passando no supermercado. Essa informação, aonde a gente vai buscar, a gente pode depois alinhar junto com o MTS, se vai ser na própria adquirente, se vai ser via, obrigar lá eles
Portinho, um decreto para poder ser feita essa informação, mas que a informação tem que estar de forma aí deles, consumir esses dados aí, isso aí é primordial, viu? Só para deixar claro aí no radar.
Nelson (Salesforce)   46:33
Não, sim. A questão é, tem que estar disponível onde? Esse acho que essa eu acho que é esse o que a gente vai discutir.
Eric (Salesforce)   46:39
E mais que isso, Nelson, uma parte ali me preocupou. O que você chama de monitoramento? É uma questão mais de auditoria, por exemplo, eu quero ver o Eric, eu vou abrir o cadastro do Eric, quero ver onde ele comprou.
Georges Leitao dos Santos   46:40
Sure.
Portella Man.
Nelson (Salesforce)   47:00
I mean.
Georges Leitao dos Santos   47:04
Sim.
Eu acho que tem a vai ter. Acho que vai ter tantas 2 coisas que eu até um exemplo que o auditor colocou. Por exemplo, eu tenho um restaurante que ele só funciona lá de geralmente de 11 até as 3. De repente passou uma transação 4 da manhã com um cartão. OPA, algo estranho. Então um alerta ali para o auditor.
Ter isso no radar dele, poder fiscalizar. Então são esses tipos de alertas que o analytics pode oferecer aí para uma fiscalização mais efetiva.
Rafael Roquette (Salesforce)   47:35
Pessoal, de todo o material que a gente até já está tendo contato, tudo que foi falado, todas as gravações de reuniões, toda a proposta mesmo que foi super detalhado o material, acho que o time de arquitetura já tem condição de fazer um trabalho inicial, Eric, pelo que eu
Consigo perceber aqui, aí queria ouvir a tua opinião do Pedro também, de fazer um detalhamento e aí transformar isso aqui que está de um jeito mais esquemático, realmente num painel de arquitetura ali mais bem detalhado. E logo após esse trabalho, acho que vão surgir uma série de perguntas como essa.
Retenção do dado, da onde vai, como vai ser essa API exatamente aqui e sem essa construção inicial, por mais Nelson, que esse sistema aqui já dê a visão completa do que se quer o Eric, Pedro e a arquiteta funcional de solução, assim que entrarem.
vão conseguir construir essa primeira visão que vai nos capacitar nessa primeira fase que a gente faz, George, que é uma fase que a gente chama de descoberta, em que a gente bota no papel exatamente, todos os requisitos são esses, a arquitetura então vai ser assim, a gente tem ainda essas dúvidas, e aí situações como essa que a gente levou
Se levantou que o Rigan até disse muito bem, acho que vai ter que ter para em paralelo uma série de confirmações aí abrindo frente com vocês, elas vão surgir. E eu estou falando tudo isso porque Jorge? Porque a intenção eu entendi dessa reunião aqui era a gente poder entrar para tirar essas dúvidas iniciais. E aí a gente está vendo agora aqui que eu acho
Realmente a gente precisa logo da descoberta para começar logo os trabalhos com os arquitetos para poder sentar com vocês nesse fórum aqui, que então pode ser até essas mesmas pessoas, mas já com um conhecimento técnico exatamente de quais respostas precisam ser dadas.
Quais informações precisam realmente ser validadas? Qual vai ser a estratégia geral para que a gente possa fechar o plano de trabalho, considerando que o tempo é curto, a gente precisa fazer isso para ontem. Então, o Nelson, eu estou falando tudo isso por conta do tempo, tá cara? O que eu sugiro é realmente que.
Nelson (Salesforce)   49:36
Para.
Rafael Roquette (Salesforce)   49:37
Assim, eu não sei como é que está o trâmite aí de pré-venda, assinatura, mas assim que a gente fechar, nos dê aí para o time Eric, um tempo de 1, 2 dias para o time. O time precisa se debruçar, o time alocado que eu estou dizendo, se debruçar sobre tudo isso para vir aqui de forma mais assertiva. A dúvida é essa.
O ponto é esse e eu tenho certeza que essas dúvidas vão virar outras dúvidas ou outras frentes de trabalho durante essa descoberta.
Nelson (Salesforce)   50:02
Yeah.
Pedro Martire - Salesforce   50:05
Perfeito, Rafa, se você se eu puder complementar primeiro, bom dia pessoal, Pedro aqui, eu sou arquiteto técnico aqui da Silva Esforce. Só para dar um pouco de contexto, entendendo a celeridade que o projeto pede, eu vou dar o exemplo aqui do projeto Uno, que o Eric estava desde o começo. Em algum momento ele passou bastão.
Nelson (Salesforce)   50:06
Or.
Pedro Martire - Salesforce   50:21
Pra mim era do projeto que a gente concluiu. Foi tomada a decisão de quase zero persistência de dados dentro da Silva Esforços. Isso impactou em arquitetura num ponto que a gente precisava de uma série de API, na verdade de uma volumetria muito alta de API, a gente inclusive fez um mapeamento recente
Foram cerca de 30 APIs que a gente utilizou para a construção do portal. A gente só conseguiu terminar o projeto no tempo esperado, também porque o time da Dataprev entendeu essa necessidade e conseguiu fazer o mapeamento, senão das 30, mas pelo menos de 20 e poucas APIs.
E isso acelerou o nosso trabalho de uma forma considerável. Isso reforça que o ponto do Rafa da gente já conseguir ter esse primeiro desenho pra gente conseguir ter pelo menos essa resposta porque a gente entende aqui do trabalho que precisa ser feito e da construção do nosso lado que precisa ser feito, só que a gente vai levantar uma série de dependências a tomada decisão.
precisão de zero persistência ou não E essas dependências normalmente aqui por experiência do projeto são que podem causar algum pedágio aqui que a gente possa pagar de tempo e enfim possa causar algum atraso ou do tipo tá Brasil
Rafael Roquette (Salesforce)   51:32
E isso, Georges, não é para dar um passo para trás não, é para ganhar força para a gente conseguir entregar aquilo que está posto, porque a gente já está compromissado a fazer aquilo acontecer como está definido com vocês em relação ao tempo e em relação ao escopo. Então pode dar essa sensação, mas a gente vai ter que abrir as caixinhas de pandora inteira, discutir tudo,
Georges Leitao dos Santos   51:46
Okay.
Rafael Roquette (Salesforce)   51:51
de que está todo mundo super bem alinhado para que a gente não tenha surpresa no futuro e consiga fazer exatamente aquilo que é esperado, tá gente?
Nelson (Salesforce)   51:56
Okay.
e nesse projeto ainda um ponto que difere em um ponto da Una né É porque a Una já já é um legado que já tem todo o modelo de dados pode expor APIs e tudo mais para a gente ser vamos ver uma nova
um Segundo front-end, né? E por trás ele é UNA. Nesse caso do Marketplace, diferente da UNA, não existe, né? Essa estrutura de cotações, e esse leilão reverso que a gente inicialmente chamou aí, não é bem o termo leilão, ele não existe, é uma UNA.
Para a gente poder ser só um front-change expor o crude ali de outra plataforma, ele é a plataforma, então é oficial, vamos dizer assim, de frente da Mota. Então acho que esse.
ponto que acho que talvez seja o primeiro e o mais importante de todos né é olhando para este bloco entendendo que ocorre ele é posicionado como o repositório do metadado destas transações é entender se
Issa, se esse modelo.
Pode ou não pode? Acho que isso é o Marco zero. Agora para mim, não é? Eric concorda, mas para mim é o Marco zero de tudo.
Georges Leitao dos Santos   53:12
Singer.
Well, uh
O Nelson, diante da proposição aí do Rafael, é e também onde já está da hora aqui, né? Que a gente tinha marcado só 1 hora. A gente poderia então, quem sabe amanhã, nesse mesmo horário aí, o Rafael, será que você consegue apresentar pra gente então a sua sugestão aí então?
Nelson (Salesforce)   53:23
Uh-huh.
Rafael Roquette (Salesforce)   53:31
É, a gente pode apresentar um plano inicial de trabalho, tá pessoal, mas Nelson, eu preciso da sua orientação porque o time ainda não está alocado, eu não sei exatamente aí eu estou falando aqui, pisando em ovos por conta do time de pré-vendas, mas nós somos o time de professional service que é onde vão ter os recursos
O Eric e o Pedro são pessoas que provavelmente a gente quer elencar para esse trabalho inicial, mas para isso a gente só precisa da confirmação. Então o que eu te peço Georges, uma vez que o time esteja alocado, e aí Nelson, esse start você vai saber dizer quando é que vai ser feito,
Nelson (Salesforce)   54:00
Mhm.
Rafael Roquette (Salesforce)   54:08
Que a gente tenha pelo menos aí uns 2 dias úteis, certo Pedro e Eric? Para uma visão inicial assim profunda, a gente vai trazer um plano mais profundo para vocês, já com uma série de apontamentos e já com um plano de trabalho num nível mais detalhado do que aquele que o Nelson botou na proposta para vocês. Então a gente vai pegar
Nelson (Salesforce)   54:08
Okay.
Okay.
Rafael Roquette (Salesforce)   54:27
Cada caixinha daquela vai revisar, vai entender se realmente é aquele tempo, se precisa de um ajuste para cá, para lá, botar isso no calendário, porque se você olha ali, está em semanas. Vamos botar aquilo num calendário próprio. A gente está falando da primeira semana de setembro do dia tal.
Que tem um feriado, então tudo isso é feito logo nesse primeiro encontro, até antes da reunião de kick-off, porque o ideal é que a gente faça a reunião de kick-off depois desse pelo menos dois dias ali de aprofundamento do time, tá George?
Nelson dando start, contem dois dias para nós e aí nós podemos já fazer uma reunião de kick-off já apresentando o plano inicial, as dúvidas iniciais e aí começar os trabalhos mais técnicos e mais profundos, tá Jorge? Agora Nelson, time de pré-vendas, por favor, amiguinha, que se eu falei besteira, mas eu acho que essa é a sequência, né?
Nelson (Salesforce)   55:17
Não é isso, é fora da questão Contratos já sabido para a gente poder ter, é claro, o time completo. Mas eu acho que assim, a gente tem dois pontos aqui que a gente pode separar desse pré-trabalho, vamos chamar assim. O contrato, ele vai marcar, ele é uma divisória boa ali de como
O projeto acontece, de como a alocação de todo o time acontece. Vamos falar sobre esse pré-trabalho. Para mim, a gente tem que dividir 2 expectativas bem claras. Uma coisa é, eu preciso, a gente precisa detalhar e refinar mais o escopo. Acho que isso tem que ser com o time completo. Tem que estar a solução exatamente se não.
Qual isso de qualquer coisa que a gente faça? Por mais que a gente grave, por mais que a gente transfira o melhor possível todo o conhecimento para alguém, pode ser que depois ele faça outra visão, outras perguntas. Então é legal o refinamento do escopo, o detalhamento das histórias, exatamente a gente fazer isso com o time completo. O que a gente entende que a gente precisa fazer nesse pré trabalho é exatamente.
Esses Marcos importantes e que ele muda o desenho da solução, sabe? Igual, por exemplo, se eu não posso fazer guarda da informação da cotação lançada pela beneficiária no seus cloud, muda a solução.
Muda o desenho da solução, assim, acho que esse acho que é o trabalho que a gente tem que direcionar agora nesse pré-projeto, que exatamente alinhando com esses requisitos arquiteturais da Dataprev.
entender exatamente quais são essas opções, por exemplo, temos que fazer, guarda a persistência do dado local, fechou. Entendeu o que é, já é sabido, já é conhecido, para onde vai. Para a gente, puxa, legal essa ferramenta, eu consigo conectar com o primeiro software, eu já vejo uma saída.
O que eu quero é fazer assim, fechar aqui a solução, ainda que alto nível, ainda que eu não estou falando, é o campo tal que eu vou precisar ter no contato, e esse campo tal eu não posso ter guarda dele ou ele tem que estar criptografado, sabe?
Não é nem nesse nível ainda que eu estou preocupado. Eu estou preocupado é a solução se baseia que eu guardo a cotação nos seus cloud. E a gente está falando que já não sabe se isso pode. Então acho que isso para mim é o alvo desse pré-trabalho. Eric, você concorda?
Acho que eu preciso ter certeza de que a solução que a gente montou está fechando, sabe? Está fechando com todos os requisitos e políticas de segurança e arquitetura.
Porque são muda a solução.
Eric (Salesforce)   57:47
Dos pontos que a gente conversou de novo, estou recente aqui no projeto, não tive tempo de me aprofundar, mas 2 me chamou atenção, um é esse realmente, o que é, o que, quando, como que a gente pode guardar aqui?
Então, se vocês precisam validar lá com o time de segurança, eu acho que é importante tocar isso em paralelo, porque realmente muda o desenho aqui. O ideal é que a gente tenha uma certa flexibilidade. Se eu não posso guardar um campo, mas ok, eu posso anonimizar, eu posso, sei lá.
Então, o detalhe a gente vai conversar depois, mas a gente tem uma visão geral, porque isso, por exemplo, é um requisito muito forte do Uno lá, que travou a gente desde o início, mas já era previsto. Então, aqui a gente precisa ter essa visibilidade também do impacto que isso daria no desenho da solução.
Nelson (Salesforce)   58:29
Mhm.
Eric (Salesforce)   58:36
E essa questão do monitoramento também. Então, assim, a gente precisa ter exemplo do que vocês querem receber, o que é esse monitoramento, porque também impacta no desenho, porque a gente está falando de volumes, imagino, gigantescos. Então.
Nelson (Salesforce)   58:37
Yeah.
É, impacta até na proposta de licença, se a gente for ouvir bem, né?
Eric (Salesforce)   58:54
Porque assim, só um exemplo, uma coisa é eu entrar no dash e ter no dash ali que eu estou consultando em algum lugar, seja no banco, seja em algum lugar, eu estou mostrando ali para vocês tudo que aparentemente sai do padrão ali fora do comum que vocês definiram. Outra coisa seria eu receber todas as transações
E eu ter que disparar um alerta para alguém. Sei lá, a solução é diferente. Uma eu vou consumir os dados e vou apresentar a outra. Eu estou recebendo todos os dados. Então, assim, a gente precisa entender.
Não sei o que está escrito na SOW, realmente ali, ou o que vocês realmente precisam para a gente ver o melhor desenho para essa solução, principalmente quando a gente está falando de grande volume de dados. Isso me preocupa e a gente tem que dar a melhor solução em termos de performance e assim por diante.
Nelson (Salesforce)   59:43
Eu não retocaria nada, acho que exatamente os 2 pontos para mim era o alvo da próxima reunião.
Yeah, Juliana.
Georges Leitao dos Santos   59:52
Yeah.
Giuliana Silva Bezerra   59:53
Então, pessoal, acho que essa falta de insumos acabou até prejudicando talvez as nossas discussões nessa primeira pauta, porque a gente poderia até ter discutido mais algumas questões e vocês já teriam até mais insumo para isso. A gente tem uma nota técnica, inclusive que.
que seria enviada para vocês com esses requisitos, insumos, esclarecimentos também de várias questões, mas um ponto que eu queria colocar aqui em relação à arquitetura é que assim, vocês falaram de concordância e tudo a gente precisa realmente conversar tá, em termos de arquitetura também.
antes de pensar assim, pensando em próximos passos, como vocês sugeriram, principalmente essa questão de qual é o ciclo do dado, por onde ele passa, como é que esse dado que está sendo operado dentro da plataforma vai ser disponibilizado pelo Analytics.
Isso é um requisito, nós precisamos do dado disponível para a gente colocar na nossa esteira analítica. Então isso também precisa ser pensado novamente para questões de alinhamento em relação a como hoje a gente arquiteta aqui os projetos, as soluções analíticas, a gente pode conversar sobre questões
de conectividade de disponibilização dos dados porque o CDP não seria utilizado nessa solução e aí a gente pode fazer esse alinhamento com vocês também para que a gente consiga evoluir esse desenho colocar termos mais concretos a respeito dessas integrações né é
Como seria o dado, a origem do dado, todo o ciclo de vida do dado fica claro para a gente, para a gente poder fazer, avaliar de fato, arquiteturalmente, a viabilidade da solução como um todo, aqui em termos de arquitetura. Tá bom?
Nelson (Salesforce)   1:01:34
Legal. Podemos então, Jorge, seguir então a próxima a nossa próxima agenda é focar nisso, então a gente entender o dado e a proposta, a princípio, que ele faz residência na plataforma e eu entendo que parte dessa decisão
Depende do tipo do dado em si para tomar essa decisão. Então a gente pode ir para mim, acho que essa tem que ser a próxima. A próxima agenda é se este, se a se AO fato dos metadados e os dados estarem no core.
Da da Seus Force na plataforma, isso É Ou Não É um problema, porque, de novo, o desenho da solução muda.
Aí, só não sei para essa próxima, não que a gente precisa pensar em sumo, gente, porque, por exemplo, o que eu tenho de informação do dado em si? O protótipo, o Prota no Figma é o melhor modelo que eu tenho para saber qual é o dado que a gente coleta, logo qual é o dado que a gente guarda.
Uh
Então a gente pode
Com esse, com esse filme para a próxima, então vamos olhar OA jornada e o dado e decidir para a gente poder decidir um se.
Está aderente ou não está aderente manter o dado na plataforma ou não?
So you shot it there, yeah?
Georges Leitao dos Santos   1:02:52
É, eu acho que sim. Eu acho que também eu estou vendo aqui internamente o Nelson, a questão de disponibilizar também esses dados aí da nota técnica pra você já ter o conhecimento. Aí que aí com essa informação da nota técnica.
Nelson (Salesforce)   1:03:01
Ohh, this is a seria I want to do my.
Rafael Roquette (Salesforce)   1:03:06
City Dell.
Georges Leitao dos Santos   1:03:08
É, eu tô vendo aqui só com o com o jurídico aqui, como é que pode ser feita essa prévia aqui, o envio dela, porque aí com ela, como tem todos esses dados aí que o Rio de Janeiro já levantou, como ele bem colocou, a equipe de Jesus, ele fez um levantamento bom em cima dele, um detalhamento.
Nelson (Salesforce)   1:03:13
Turn
Georges Leitao dos Santos   1:03:24
Aí dá dá para vocês ter um dever de casa bom final de semana, uma leitura, uma leitura boa e a gente marcar já na sequência para tirar essas dúvidas aí.
Rafael Roquette (Salesforce)   1:03:26
Perfect.
Nelson (Salesforce)   1:03:34
É, talvez seja uma, se a nota técnica responder esses principais pontos que eu falei para mim, o principal ponto agora é a solução, como ela foi feita, ela para de Bell ou não? Essa é a resposta importante. Se a nota técnica dá essa resposta,
Se vocês acharem que é melhor do que a gente explorar isso numa próxima agenda, como vocês acharem?
Georges Leitao dos Santos   1:03:56
Não, mas eu acho que eu acho que pode ter, pode ter a próxima agenda, mas ele te encaminha, independente da nota técnica ou não, ela servia de insumo para vocês, entendeu? Acho que não invalida, né? Tá? É o Jesus, pode falar, ele é Jesus.
Rafael Roquette (Salesforce)   1:04:01
Okay.
Nelson (Salesforce)   1:04:07
Good feed.
Perfect.
Daniel Santos de Jesus   1:04:11
Não é perfeito, Nelson. Acho que no nosso primeiro encontro ali eu frisei da importância da gente trabalhar em conjunto e usei ainda a referência que seria normal esse momento. Não temos. Nós não temos todos os requisitos.
E às vezes vai chegar lá na primeira solução e não terá. Então acho que o mais importante aqui é a gente trabalhar sincronizado. E aí a composição que foi colocada aqui dos times nos dará esse amparo. Do meu lado aqui da arquitetura, a Gil aí é a nossa mestre.
Nelson (Salesforce)   1:04:39
No.
Daniel Santos de Jesus   1:04:43
É com relação a à discussão analítica de dados voltado para arquitetura. Tem um time aqui bem robusto, time do Rigan. E essa construção dessa solução, ela vai ter que ter esse viés, tá? Trabalhar com múltiplas áreas e acho que a resposta ali à tua pergunta, se para de pé ou não.
É tá dentro dessa construção coletiva, porque não se enganem, a gente tá aqui apertado com o cronograma, a gente vai ter que trabalhar em parceria e, enfim, o trabalho vai ter que ser desenvolvido assim, gente, dentro dessas condições, tá? Não vai chegar nada refinado não, porque o.
Nelson (Salesforce)   1:05:03
There you go.
Daniel Santos de Jesus   1:05:16
Tempo do negócio é que dá o tom. Então só queria reforçar que meu time está aqui à disposição. É meu amigo George Fabricio, sabem que eu dediquei aqui um exército que é prioridade zero, estratégica. E cara, não me incomodo de repente a gente se reunir 2 vezes por dia, se for o caso.
Fabricio Gustavo de Paiva Vicente   1:05:27
Exatamente.
Daniel Santos de Jesus   1:05:34
Utilize a arquitetura como seu braço de apoio. Não vamos falhar por conta de delay de comunicação. Não chegou esse artefato. Eu vou perturbar meus amigos George e Fabricio aqui e vou correr atrás de tudo, tá? Mas só queria reforçar essa parceria, meu irmão. A gente vai sair do outro lado, tá? Mas trabalhando em conjunto.
Nelson (Salesforce)   1:05:51
Oh, perfect.
Georges Leitao dos Santos   1:05:52
Pois é, pois é, Nelson, aí diante da fala do Jesus, cara, eu não queria deixar isso pra semana que vem, cara. Se a gente pudesse ter alguma coisa amanhã, uma agenda amanhã, mas o que puder adiantar, a gente pode definir já aqui o que você acha que é nesse mesmo horário aí.
Nelson (Salesforce)   1:06:03
Wow.
Vocês acham que é isso é proposto? Você acha que esse amanhã, esse mesmo horário da Eric e Pedro, tudo bem?
Georges Leitao dos Santos   1:06:12
Aqui do time da Dataprev aqui com certeza.
Rafael Roquette (Salesforce)   1:06:14
Do time de arquitetura, Nelson, vamos discutir aqui internamente por conta desse trabalho que a gente precisa fazer de deep dive. É claro, entrar aqui e discutir, acho que é viável, mas a gente precisa para ser produtivo, entendeu, pessoal?
Porque até o direcionamento das questões ele vai se dar muito a partir dessa análise mais profunda da arquitetura. Então eu ia sugerir, pelo menos, Nelson, primeiro que a gente conversa aqui da Silva acabar com uma proposta de agenda aqui pra gente, mas que a gente converse depois desses dois dias de alocação ali do time, entendendo e aprofundando.
Nelson (Salesforce)   1:06:44
Tá bom.
Rafael Roquette (Salesforce)   1:06:50
Para que a gente vá direto no ponto, sabe pessoal? Não fique. A gente pode estar esquecendo de falar coisas importantes aqui que a gente não está falando pelo pela falta de profundidade.
Daniel Santos de Jesus   1:06:53
Isso it.
Perfect, Rafael.
Nelson (Salesforce)   1:06:57
Francisco.
What's up?
Daniel Santos de Jesus   1:07:00
E aí, Rafael e Nelson, desculpa, é Jorge. A gente entende aí toda a questão do compilar, se toda aquela parte burocrática do artefato, etc. Sei, cara, vamos fazer uma ressonância do que a gente pode extrair dessa nota técnica. Estou falando de tecniquês, que isso vai ajudar como insumo para os meninos.
Nelson (Salesforce)   1:07:00
A gente conversa aqui.
Georges Leitao dos Santos   1:07:07
Sim.
Yeah.
Daniel Santos de Jesus   1:07:17
Não estou dizendo que a gente vai pegar antes da aprovação processual e entregar, mas eu acho que a gente faz uma ressonância ali e traz as questões técnicas e isso vai dar celeridade para eles, tá? Deixa o fluxo do CEI rolar e o jurídico aprovar. Mas eu acho, Fabricio, que a gente consegue fazer um apanhado bem legal ali.
Georges Leitao dos Santos   1:07:23
Four.
Daniel Santos de Jesus   1:07:33
De muita coisa que a gente discutiu tecnicamente e isso eu não vejo problema algum em colocar a mesa.
Georges Leitao dos Santos   1:07:38
Jesus, então assim é.
Nelson (Salesforce)   1:07:38
Então, mesmo que vá como disclaimer, Justino, que não é um documento oficial, não é draft, Sei lá o que for, só para a gente poder já mergulhar, beber um pouquinho dessas desses requisitos.
Georges Leitao dos Santos   1:07:43
Yes.
**** her.
Então, como o Fabricio, como você consolidou essa informação lá na data técnica, você pode fazer, você pode fazer esse compilado aí que essa sugestão do Jesus para a gente poder encaminhar para o parceiros e eles poderem já trabalhar em cima dela. Aí fica beleza, aí o Nelson a gente.
Fabricio Gustavo de Paiva Vicente   1:07:53
Okay.
Posso sim, posso sim. Ainda hoje eu vou estar fazendo isso, porque na nota técnica ela tem as recomendações tanto da arquitetura como também da área de dados, da área de analíticos. Então eu vou estar fazendo esse apanhado e estou passando. Eu passo para qual e-mail?
Georges Leitao dos Santos   1:08:05
Michel.
Isso.
Frank.
Fabricio Gustavo de Paiva Vicente   1:08:14
Eu poderia passar para 1,5 da Sales e ele replicar para os demais.
Rafael Roquette (Salesforce)   1:08:18
Pode ser por Nelson mesmo, para Georges e Georges Pass
Georges Leitao dos Santos   1:08:18
No, pode, é para o Neves.
Nelson (Salesforce)   1:08:20
Ortiz.
Fabricio Gustavo de Paiva Vicente   1:08:20
Tá, vou mandar pro nos.
Georges Leitao dos Santos   1:08:21
É, Paulo, vamos centralizar o canal comigo aqui. Aí você manda e eu despacho para a equipe. Aí eu copio vocês. Depois pode ficar tranquilo.
Fabricio Gustavo de Paiva Vicente   1:08:25
Tá bom?
Daniel Santos de Jesus   1:08:31
É uma última recomendação, tô igual um papagaio aqui, mas desculpa, a gente é projeto prioritário, é meu amigo Georges, considera com os colegas da Costa, depois que a gente acentuar aqui essa discussão de requisito.
Georges Leitao dos Santos   1:08:36
É isso aí, cara, tem que ser assim mesmo.
Rafael Roquette (Salesforce)   1:08:37
Mm-hmm.
É só o começo.
Nelson (Salesforce)   1:08:39
Okay.
Daniel Santos de Jesus   1:08:47
É, e aí tem todo um cronograma para a gente trabalhar em conjunto. Ponto de controle frequente. Eu acho que vai nos ajudar sobretudo a organizar as agendas aqui. E a gente fica tentando encaixar o pobre do Rigan ali com 300 agendas. Ele é importante. Acho que a gente pode considerar.
Georges Leitao dos Santos   1:08:55
R.
Daniel Santos de Jesus   1:09:03
Diariamente uma horinha ali de ponto de controle e acho que isso vai organizar aqui a questão das agendas.
Rafael Roquette (Salesforce)   1:09:09
Daniel, e até falo direcionando para o Georges que eu sei que Georges você vai ser o gerente do projeto pelo lado da DataprevRJ pelo que eu entendi da estrutura, a gente já tem todo um modelo de governança que eu primeiro vou propor para você Georges, que inclui reuniões diárias, reunião de comitê semanal ou quinzenal, as nossas próprias internas da seus forces
Georges Leitao dos Santos   1:09:09
Good food.
Yes.
Rafael Roquette (Salesforce)   1:09:28
vão ter visibilidade quando a gente está fazendo o quê? Então essa governança toda ela vem com o pacote da própria gestão do projeto aqui pelo nosso lado, mas alinhado, claro George, com você, tá?
Georges Leitao dos Santos   1:09:38
Ate a fase seguinte, hoje à tarde, se quiser marcar 1 hora aí pra você apresentar, pode ser. E aí eu.
Rafael Roquette (Salesforce)   1:09:43
Tá bom, a gente pode falar, com certeza.
Georges Leitao dos Santos   1:09:44
O Nelson, eu fico em disposição aí, eu me adaptei na agenda aí pra poder.
Nelson (Salesforce)   1:09:47
Mm.
É, acho que mais se dizer o modelo que a gente usa, né, Rafa? Talvez propor como o modelo que a gente usa como modelo e aí e aí a gente ajusta isso.
Rafael Roquette (Salesforce)   1:09:53
Uhum, com certeza.
Sim, canais de comunicação que a gente vai falar.
Exact.
Georges Leitao dos Santos   1:09:59
Perfeito, então tá bom. Pessoal, então dá, eu acho que dá.
Nelson (Salesforce)   1:10:02
Está bem, eu vou então eu vou conversar então com o Eric Pedro e o Rafa Jorge, e aí eu te eu vou, eu vou falando ali contigo para com relação a venda de amanhã.
Georges Leitao dos Santos   1:10:11
Okay.
Oh, legal, beleza.
Nelson (Salesforce)   1:10:15
Obedecendo aqui o que o pessoal propôs, aí eu já converso com eles e te confirmo se a gente tem consistência de um material, de novo, para que a hora do pessoal aqui seja bem produtiva e não tenha que desmarcar outros compromissos por uma agenda que às vezes, ah, puxa, não foi tão produtiva assim.
é eu já respondo eu já te mando sim
Georges Leitao dos Santos   1:10:33
Tá bom?
Tá, então só para a gente ficar fechar aqui hoje então aqui de A gente ficou combinado então do nosso time aqui a gente fazer esse copilato aí do que tem na nota técnica né da parte de arquitetura, de analytics, né da parte de produto que a gente vai fazer esse consolidado aí não seguindo o modelo da nota técnica pegando a sugestão aí do
Nelson (Salesforce)   1:10:44
Okay.
Georges Leitao dos Santos   1:10:55
de Jesus te encaminha para vocês ainda hoje. E aí vocês dá um dever de casa e dá uma lida lá e vê se tem fundamento a gente ter essa reunião amanhã. E diante disso também, aí eu aguardo vocês pra gente ter uma reunião hoje à tarde pra gente definir essa questão de ponte de controle, né? Diário.
Quais são os horários sugeridos? A gente já faz esse alinhamento também hoje à tarde aí vocês apresentam esse modelo aí pra mim aí a gente já dá sequência, tudo bom?
Nelson (Salesforce)   1:11:23
Combinados.
Georges Leitao dos Santos   1:11:25
É isso pessoal, mais alguma coisa aí?
Jesus, Fabricio.
Rigan Andre Campos Gonzalez   1:11:31
Então, beleza, Jorge, só lembrando, eu tenho aqui, a equipe tá aqui também, tá? Então, se na eventualidade eu não poder participar da reunião, tem o Paulo Ohno, que é, na verdade, o substituto do gerente de departamento que lidera essa.
Fabricio Gustavo de Paiva Vicente   1:11:34
Hello.
Rigan Andre Campos Gonzalez   1:11:47
Parte aí de analytics, não é que a gente tem mais 22 pessoas aqui também, então assim, não deixe de chamá-los, está na minha.
Georges Leitao dos Santos   1:11:54
Wallace Sharp.
Thank you.
Rigan Andre Campos Gonzalez   1:11:57
Oh, this.
Nelson (Salesforce)   1:11:58
Wait out. Bruno, do I go?
Georges Leitao dos Santos   1:11:59
de Jesus aí Fabricio
Rigan Andre Campos Gonzalez   1:11:59
Bell is.
Daniel Santos de Jesus   1:12:02
Tranquilo para mim está está bem coberto aqui.
Fabricio Gustavo de Paiva Vicente   1:12:04
Okay.
Rafael Roquette (Salesforce)   1:12:06
O pessoal, parabéns pelo projeto. A gente está muito feliz aqui de poder fazê-lo. O caso de uso, ele é fantástico assim. O que vai ser proposto? A gente vê todas as potencialidades e capacidades da Silvaforce sendo aplicadas aqui. Acho que, bem, vai ser um projetão.
Georges Leitao dos Santos   1:12:07
Alan. So, but.
Rafael Roquette (Salesforce)   1:12:21
Contem com a gente, tá?
Daniel Santos de Jesus   1:12:23
Eu só diria o seguinte, seus falsos, faz seu nome.
Nelson (Salesforce)   1:12:23
Okay.
Georges Leitao dos Santos   1:12:26
They see.
Rafael Roquette (Salesforce)   1:12:26
Pode deixar. Boa. Valeu, gente. Tchau, tchau.
Daniel Santos de Jesus   1:12:27
Meu case é bonito.
Georges Leitao dos Santos parou a transcrição