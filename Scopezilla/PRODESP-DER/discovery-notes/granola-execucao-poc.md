<!-- Source: Transcrição Granola (resumida) · Retrieved: 2026-09-17 · Via: colado pelo usuário no chat -->

# Execução PoC — DER-SP (Granola, resumo)

## Contexto da Reunião
POC de execução do sistema de atendimento emergencial viário (DER-SP)

Foco principal: atendimento de pane e sinistro nas rodovias estaduais

Participantes do DER discutiram o SIGOR (sistema legado) e suas limitações

Equipe Salesforce demonstrou Service Cloud, Field Service e agente de triagem com IA

## SIGOR: Limitações e Contexto Operacional
- Sistema relativamente novo (1 ano), substituiu o SIGA
- 28 processos mapeados internamente, com gaps identificados
- ~120 tipos de ocorrência (TOs) cadastrados, mas muitos desatualizados ou redundantes
- 5 macros: pane, sinistro, teóscio, diversos, solicitação de informação
- Subdividem-se em mais de 100 tipos específicos
- Dados do SIGOR usados para decisões estratégicas (posicionamento de radares, curvas, passagens de fauna)
- Confiabilidade dos dados comprometida por registro manual e falta de rastreabilidade
- Ligações recebidas não vinculadas automaticamente ao evento correspondente
- Controle de ligação vs. ocorrência feito manualmente, sem de-para preciso
- URA atual (Instinct) migrada recentemente, sem integração via API com o SIGOR
- Migração ocorreu esta semana, causou queda parcial do sistema emergencial

## Operação de Campo: Recursos e Estrutura
- 298 viaturas VTE (veículo técnico de emergência), base de dimensionamento
- 4 turnos de 12x36, totalizando ~1.200 pessoas (4 por viatura)
- Controle feito por viatura, não por pessoa; operador loga no app da viatura
- Pico simultâneo: 298 viaturas ativas
- Tipos de veículo: VTE, guincho leve/pesado, moto, brigadista, veículo de fauna (gaiola)
- 14 CGRs (regionais), cada lote atendido por uma única empresa terceirizada
- Empresas não veem os trabalhos umas das outras
- Operadores do CCO (~6 por turno por CGR) fazem o despacho manualmente, por feeling
- Sem regras padronizadas de priorização ou composição de equipes
- Gap mapeado: ausência de matriz de habilidades e checklist de insumos por viatura
- Exemplo citado: pane de veículo elétrico sem patins disponíveis no guincho

## Gaps de Processo Identificados
- Sem fluxo estruturado de pós-operação ou auditoria de serviço prestado
- Sem pesquisa de satisfação ativa (encerrada em 2 de março de 2026)
- Pesquisa anterior era manual, enviada no dia seguinte, sem identidade visual do DER
- Sem rastreabilidade de qual ligação gerou qual ocorrência
- Sem autodispacho: toda decisão é humana e intuitiva
- Serviços emergenciais podem ser multi-day (ex.: interdição de rodovia entre estados)
- Waze foi usado como fonte de alertas, mas taxa de localização ficou em ~20%
- Abandonado em favor do projeto de câmeras (cobertura a cada 5 km, financiado pelo BID)
- 38 câmeras fixas ativas hoje, monitoramento ainda dependente de ação humana

## Funcionalidades Demonstradas (Salesforce)
- Field Service: despacho por arrastar e soltar, alertas de conflito de agenda sem bloqueio
- Agente de triagem com IA generativa: classifica sinistro, pane ou outros antes de transbordar para atendente
- Configurável: transfere para humano se solicitado explicitamente ou em caso de sinistro
- Incidente geográfico (Service Cloud): agrupa atendimentos de uma mesma ocorrência por zona
- Evita múltiplas ordens de serviço para o mesmo evento; permite desvincular se necessário
- Envio de link por SMS para coleta de geolocalização (lat/long) do usuário em ligação
- Pontos de referência cadastrados no mapa para triangular localização sem GPS preciso
- Supervisor Command Center: visão em tempo real de todos os operadores e fila
- URA: CTI conversacional substituindo menu DTMF, com possibilidade de consulta de protocolo por voz

## Escopo do MVP Definido
- Canal principal: WhatsApp (já demonstrado na POC)
- Ligações telefônicas: abertura manual de caso no Service Cloud pelo atendente
- URA não incluída no escopo emergencial inicial; decisão de infraestrutura de voz ainda pendente
- Jornadas a escopar: habilitação do canal WhatsApp, triagem, abertura de ordem e execução de campo
- Meta de homologação: janeiro/fevereiro; produção: abril
- Infraestrutura de telefonia (itens 1 a 5 do termo de referência): validar com Stefanini (parceira da Prodesp)
- Itens 6 a 10: escopo Salesforce, a ser detalhado em proposta

## Termo de Referência e Próximos Passos Contratuais
- Contrato atual de URA ativo até abril; contrato administrativo renova em 30 de novembro
- Números do termo de referência desatualizados (ex.: 50 licenças simultâneas) — precisam ser revisados
- Licença por posição única vs. simultânea a ser definida; impacta personalização de sessão por agente
- DER quer centralizar todos os canais externos em uma única plataforma (circular enviada a todas as diretorias)
- Inclui diretoria de operações viárias, planejamento (faixa de domínio, AET), obras, APC
- Proposta financeira solicitada separada por diretoria (disponibilidade orçamentária distinta)
- Stefanini: validar se atende itens 1 a 5 via convênio Prodesp (processo mais ágil que nova licitação)

## Próximos Passos (registrados na reunião)
- Enviar questionário de dúvidas técnicas ao DER (Renata) — consolidar perguntas sobre topologia, volumetria, tipos de trabalho emergencial e integrações necessárias para escopo da proposta
- Atualizar termo de referência com quantitativos revisados — separar itens 1-5 (Stefanini) dos itens 6-10 (Salesforce) e corrigir número de licenças simultâneas
- Validar com Stefanini cobertura dos itens 1 a 5 — confirmar se atende via convênio Prodesp a parte de infraestrutura física e telefonia
- Elaborar proposta financeira separada por diretoria — diretoria de operações viárias tem orçamento distinto das demais
- Definir decisão sobre infraestrutura de voz antes de conectar canal telefônico — MVP segue com WhatsApp; voz entra como segundo canal somente após consolidação da decisão de telefonia

## Problema Atual: Visibilidade e Dados
- Veículos em áreas de sombra: sem clareza se estão alocados ou não
- Atualizações de painel feitas via BI com gateway limitado a 30 em 30 minutos — equipe só vê retrato de 30 minutos atrás, sem dados em tempo real
- Hoje não há dados suficientes para análise comparativa de desempenho entre equipes

## Objetivo da PoC
- Centralizar atividades e treinamentos em uma única ferramenta
- Ter domínio sobre o que cada recurso está fazendo para priorização
- Subsidiar tomada de decisão com dados (incluindo análise de risco futura)

## Dashboard e Capacidades Demonstradas
- Métricas disponíveis no painel padrão: número de ordens, tempo médio de deslocamento, tempo desde o acionamento até check-in e finalização, prioridade por recurso e por território, zona de serviço, tipo de serviço, documentos por território
- Comparação entre recursos: mesmos números, mas um se desloca mais, outro resolve mais rápido
- Possibilidade de ver tempo de aceitação por equipe (ex: uma equipe demora 10 min para aceitar, outra aceita imediatamente)
- Download de snapshots e colaboração disponíveis na plataforma
- Personalização avançada de gráficos possível via tab/framework adicional

## Demonstração: Ordem Não Completada (Caso Rute)
- Ordem aberta pela Rute fechada como "não foi possível completar" — motivo registrado: cliente recusou/não aceitou
- Visualização no Command Center (gancho): ícone com bolinha e quadradinho indica ordem não aceita
- Fluxo demonstrado ao vivo: abertura da ordem, troca de status, visualização do resultado
