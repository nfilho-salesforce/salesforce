# Scoping Brief: DER-SP — Reunião de Preparação para PoC (Sistema de Gestão de Atendimento de Ocorrências em Rodovia)

**Source**: [DER SP REUNIÃO HÍBRIDA] Reunião de Preparação para PoC  - 2026_09_04 08_53 GMT-03_00 - Notes by Gemini.pdf
**Date**: 2026-09-04
**Participantes**: Rafael Marques (Salesforce, condutor da demo Field Service), Thiago Mantoanelli, Cristina Cândido, Renata Vendramini, Juliana Brites, Pedro Ganem Filho, Iran da Costa, Juliane Lopes, Alex Gonzalez Veiga, Nelson Stebulaitis Filho, Fernanda Aparecida da Silva, Felipe Bernardo do Nascimento, e representantes DER-SP/Apoio DER/Diefra (e-mails: saftim@sp.gov.br, raplima@der.sp.gov.br, asoleite@der.sp.gov.br, mllemes@apoioder.sp.gov.br, fbarboza@sp.gov.br, rccavalcanti@apoioder.sp.gov.br, csc5-der@der.sp.gov.br, operacoes.sp.cubatao.eng{jr02,senior}@diefra.com.br)
**Original length**: ~62 páginas PDF (resumo estruturado do Gemini + transcrição integral de ~2h08min; transcrição bruta é verbosa e repetitiva, com ruído de reconhecimento de voz)

---

## Business Context
- Objetivo da reunião: preparar o teste de campo (PoC) do "Sistema de Gestão de Atendimento de Ocorrências em Rodovia" do DER-SP, usando Salesforce Field Service.
- Escopo do atendimento: ocorrências do tipo PAN (pane) e sinistro (acidente) nas rodovias sob gestão do DER-SP, com despacho de viaturas de guincho e inspeção.
- Recurso principal do modelo operacional: viatura (guincho leve / inspeção), não o operador — decisão explícita para gerenciar manutenção e alocação corretamente.

## Current State
- Operação hoje descrita como fragmentada — múltiplas aplicações e processos manuais de atendimento ao cidadão. [Assumed — inferido do comentário de Rafael Marques sobre "aplicações fragmentadas" e sobre a curva de aprendizado da equipe]
- Escala de recursos no estado: 298 recursos (viaturas) simultâneos possíveis frente a 1.292 operadores terceirizados cadastrados no estado.
- Sede administrativa da Regional 5 (Cubatão) fica a 150–200 km da primeira rodovia de atendimento — exige ponto de encontro alternativo para o teste.

## Desired State
- Plataforma Salesforce Field Service com interface 100% traduzida para português, organizada em abas/painéis para ordens de serviço e compromissos.
- Modelagem por viatura (não operador) como recurso principal, com operadores vinculados à viatura.
- Roteirização por rota mais rápida (não menor distância) para acionamento de recursos, com localização em tempo real da viatura (não endereço-base) priorizada em atendimentos emergenciais.
- Ciclo de vida de status parametrizado (aberto → acionado → em fila → aceito → iniciado → encerrado/cancelado), com bloqueio de status regressivo após início de deslocamento/serviço para evitar cancelamentos indevidos e perda de rastreabilidade.
- Aglutinação de múltiplos chamados referentes a um mesmo evento usando a funcionalidade nativa de "Incidente", evitando despacho duplicado.
- Tratamento de ocorrências fora do polígono geográfico: encaminhadas para avaliação/triagem do supervisor em vez de despacho automático.
- Canal de atendimento ao cidadão via WhatsApp, iniciando 100% por inteligência artificial, com handoff para atendimento humano a qualquer momento (limite de até 3 chats simultâneos por operador; canal de voz tem prioridade na fila).
- Assistente Visual Remoto (RVA/VRA): chamadas de vídeo via link (WhatsApp, SMS ou e-mail) para reduzir deslocamentos desnecessários e retrabalho, com gravação e transcrição automática para auditoria.
- Assistente de IA interno (base de conhecimento) para suporte a supervisores/operadores, reduzindo tempo de atendimento (TNA) e a curva de aprendizado de novos contratados (hoje estimada em 2–3 semanas). [Assumed — número de semanas citado informalmente por Rafael Marques, sem confirmação formal do DER]
- Formulário estruturado na etapa de checkout (técnico em campo), com foto obrigatória no check-in, assinatura digital opcional do cidadão, e geração de relatório em PDF vinculado à ordem de serviço.
- Gestão de territórios primários/secundários e realocação temporária de recursos (datas de início/fim), para picos sazonais de demanda (ex.: aumento de fluxo para o litoral no fim de ano).
- Habilidades (skills) obrigatórias/opcionais com pesos, para impedir roteamento de chamados a técnicos sem qualificação (com possibilidade de sobrescrita manual mediante alerta).
- Painéis/dashboards padrão e customizáveis por persona para métricas operacionais (SLA, tempos de atendimento, despacho, encerramento).

## Integrations
- Canal de entrada via WhatsApp com IA (fluxo automatizado de triagem e classificação de ocorrência).
- Redirecionamento nativo para apps de mapas, ligação telefônica e WhatsApp no aplicativo móvel do técnico.
- Possibilidade discutida (não decidida) de integrar APIs de tráfego em tempo real (ex.: Google Maps) para roteirização, em comparação ao uso de dados estatísticos históricos. [Unknown — mencionado como algo a avaliar, sem decisão]
- Uso de número de teste americano para WhatsApp durante a PoC (risco de bloqueio por disparo excessivo de SMS) — ponto operacional a resolver antes do go-live. [Unknown]

## Data Migration
- Sem menção de migração de dados legados nesta reunião — o foco foi massa de dados de teste (mais de 20 atendimentos simulados) e cadastro inicial de endereços/recursos para as regionais 5 (Cubatão) e 6 (Taubaté).
- Delimitação geográfica por polígonos (não por faixas de CEP, prática mais comum no mercado) ainda não configurada — Salesforce optou por não assumir a definição dos limites por falta de informação do escopo real de atendimento. [Unknown — pendente de definição pelo DER/parceiros]

## Users & Roles
- Regional 5 (Cubatão) — teste em campo dia 10/09: supervisores Ivan e Carlos, engenheira Karen Aparecida Santana de Lima, Thiago Mantoanelli (veículo leve/guincho), 4 viaturas na rua.
- Regional 6 (Taubaté/UBA) — teste em campo dia 11/09: Alan Delon (técnico de inspeção), Isabela (auxiliar de inspeção), Cristina Cândido e Hélio (engenheiros da UBA), 2 veículos leves + 2 de operação.
- Equipe C2C (Centro a Centro / central de atendimento): supervisor Marcelo, operadores Santiago, Renata e Alessandro — divididos entre suporte à operação e suporte prático em campo.
- Equipe Salesforce em campo: 4 pessoas acompanhando técnicos, 3 pessoas dando suporte na base.
- Escala referência do estado: 1.292 operadores terceirizados para até 298 recursos (viaturas) simultâneos.

## Timeline & Constraints
- Teste piloto em campo agendado para os dias 10 e 11 de setembro de 2026.
- Dia 10/09, 9h: encontro Regional 5 na rodovia SP-55, na altura da portaria da Riviera de São Lourenço (ajuste necessário pela distância da sede administrativa).
- Dia 11/09, 9h: encontro Regional 6 na Rua Armando de Moura, nº 41.
- Formato inicial de teste: proporção 1 para 1 (uma viatura por evento) antes de expandir para fluxos com múltiplos chamados simultâneos.
- Simulação prevista de até 8 eventos por dia, com deslocamento real das equipes.

## Budget Signals
- Nenhuma discussão de preço, taxa horária ou modelo de investimento ocorreu nesta reunião — o foco foi 100% técnico/operacional de preparação do teste de campo.

## Compliance & Security
- Auditoria de atendimentos: gravação e transcrição automática das chamadas de vídeo/RVA ficam registradas na plataforma para fins de auditoria.
- Login/autenticação dos dispositivos móveis de campo configurada previamente pela equipe Salesforce (não é aberto a qualquer contato externo).
- Nenhum requisito formal de residência de dados, LGPD ou compliance regulatório específico foi mencionado nesta reunião. [Unknown — não abordado; possível gap a levantar em discovery futuro]

## Decisions Made
**Alinhadas:**
- Modelagem de recurso por viatura (não operador) para gerenciar manutenção e alocação.
- Parâmetro de roteirização por maior rapidez (não menor distância) para acionamento.
- Ocorrências fora do polígono são encaminhadas para triagem do supervisor, sem despacho automático.
- Inclusão de formulário estruturado na etapa de checkout pelo técnico em campo.
- Aglutinação de chamados de um mesmo incidente via funcionalidade nativa "Incidente".
- Estrutura do teste prático em campo: 4 viaturas na rua, equipes divididas entre suporte na base e acompanhamento em campo, iniciando em formato individual antes da expansão.

**Precisa de mais conversa:**
- Parâmetros do fluxo de ordens de serviço — adoção de múltiplos compromissos por ordem de serviço para rastreamento histórico foi debatida, mas ficou pendente de validação definitiva da equipe. [Unknown]

## Action Items
- [O grupo] Confirmar endereços cadastrados para as regionais Cubatão e Taubaté.
- [O grupo] Definir papéis e responsabilidades de cada participante para o dia do teste de campo.
- [O grupo] Decidir a configuração preferida para o fluxo e ciclo de vida dos status de atendimento.
- [O grupo] Planejar procedimentos e logística detalhada para o teste prático do dia 11.
- [Thiago Mantoanelli] Comprar chip para os dispositivos móveis usados nos testes.
- [Rafael Marques] Desenhar a jornada detalhada do usuário e compartilhar com a equipe.
- [Rafael Marques] Incluir Alessandro no time e avisá-lo sobre sua participação nos testes do dia 10.
- [O grupo] Enviar os endereços específicos para os testes nas regionais.
- [Raul] Encaminhar informações completas sobre o encontro na Riviera para Thiago Mantoanelli.
- [AI] Confirmar data e horário da reunião na Riviera via WhatsApp para Thiago Mantoanelli.
- [Rafael Marques] Finalizar configuração dos dispositivos móveis para os testes de campo.
- [O grupo] Desenhar a área geográfica (polígono) necessária para o escopo dos incidentes.

## Key Quotes
> "A gente estruturou ali, como vocês pediram, quatro recursos em cada regional, tá? Então a gente tem dois guinchos leves e duas inspeções." — Rafael Marques

> "A grande questão aqui desse ciclo de vida dos status é garantir que uma vez que o técnico começou a rodar, ninguém, nem o programador, possa mudar, porque isso é muito ruim pra experiência dele." — Rafael Marques

> "Aqui vai ser sempre emergência, né? [...] o Field nativamente olha onde você está e para onde você está indo. Por quê? Porque precisa que você chegue o mais rápido possível." — Rafael Marques

> "A gente pegou um local de pedido [...] imagina lá que vocês falaram do caso onde o técnico informou que o veículo apresentou defeito e aí ele vai entrar em contato com os supervisores." — Rafael Marques

> "O envio de links de vídeo via WhatsApp, SMS ou e-mail permite coletar evidências visuais exatas [...] o foco de uma solução de VRA é a métrica de sucesso dela é o não retrabalho." — Rafael Marques

> "Esse atendimento inicialmente vai ser realizado 100% por inteligência artificial [...] mas em qualquer momento que você falar 'Quero falar com humano', eu vou te transferir para um atendente." — Rafael Marques

> "A gente até pensou em fazer [os polígonos] para cá, mas a gente não quis assumir porque a gente não sabia até onde ia o atendimento." — Rafael Marques

> "A sede da regional 5 está distante entre 150 e 200 quilômetros da primeira rodovia de atendimento, exigindo um ajuste no local de encontro." — Thiago Mantoanelli (via resumo Gemini)

## Open Questions & Ambiguity
- Adoção de múltiplos compromissos por ordem de serviço para rastreamento histórico — decisão de fluxo ainda não validada pela equipe. [Unknown]
- Delimitação exata dos polígonos geográficos de atuação (vs. uso de faixas de CEP) — Salesforce não quis assumir os limites sem confirmação do DER. [Unknown]
- Viabilidade e decisão sobre integrar APIs de tráfego em tempo real (ex.: Google Maps) versus manter dados estatísticos históricos para roteirização. [Unknown]
- Risco de bloqueio do número de WhatsApp de teste (número americano) por volume de disparo de SMS durante a PoC — mitigação não definida. [Unknown]
- Papéis e responsabilidades definitivas de cada participante no dia do teste ainda pendentes de fechamento (listado como action item, não decisão fechada).
- Nenhum requisito de compliance/segurança/LGPD explicitamente discutido — possível gap a explorar em rodada futura de discovery. [Unknown]
