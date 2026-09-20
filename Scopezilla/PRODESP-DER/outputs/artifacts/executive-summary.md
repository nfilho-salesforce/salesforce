# Resumo Executivo — PRODESP · DER-SP
## Atendimento de Socorro na Malha Rodoviária Estadual

## Visão Rápida

- **Dor atual**: atendimento de socorro fragmentado em chamados distintos para pedido, despacho e encerramento, sem protocolo único nem rastreamento em tempo real para o cidadão na pista.
- **Visão de transformação**: protocolo único e rastreável do primeiro contato ao encerramento, com despacho automático apoiado pelo Field Service e múltiplos canais de entrada de uso cotidiano do cidadão — voz ou WhatsApp.
- **Principais drivers de valor**: despacho automático por aderência/disponibilidade/proximidade, protocolo único rastreável, trilha de auditoria de overrides e canal digital complementar ao 0800.
- **Maior risco/incerteza**: 80 gaps registrados (7 conflitos de fonte, 5 ainda abertos) — dois bloqueiam decisão do DER antes do build: trilha de auditoria de despacho (G0305) e limite contratual das UBAs por CGR (G0309); um terceiro (G0524, padrão técnico da integração CTI) é premissa de design a validar antes do build de E01/E02/E03.
- **Primeiro passo recomendado**: Fase 0 de resolução de discovery, fechando as perguntas bloqueadoras ao DER/Stefanini antes de iniciar o build do motor de despacho.

---

## Visão Geral

O DER-SP registra hoje o atendimento de socorro em rodovia por canais e chamados separados, sem um identificador único que acompanhe o pedido do primeiro contato ao encerramento — o próprio critério de sucesso que o cliente definiu para o projeto. A janela de decisão é real: o contrato da URA atual (Instinct) expira em abril de 2027, mesma data-alvo de produção do programa, e o Open CTI legado do Salesforce sai de linha em fevereiro de 2028. O modelo de dados nativo do Field Service (Work Order, Service Appointment, Service Territory) mapeia diretamente ao ciclo de sete etapas já mapeado na discovery — solicita, registra, classifica, despacha, desloca, atende, encerra — sem exigir um motor de despacho customizado do zero, e o Agentforce abre o canal WhatsApp e, via integração CTI com a URA, também qualifica o canal de telefonia — ambos complementares, sem substituir a voz do 0800 que o cidadão já conhece.

## Escopo

O programa está estruturado em 5 épicos, todos entregues integralmente pela Salesforce PS, em org única:

1. **Canal Digital de Atendimento ao Cidadão** (E01, tamanho L) — abertura de chamado por WhatsApp e por telefonia via integração CTI com a URA, com triagem pelo Agentforce (Agentforce Contact Center Enterprise, número de licenças a revalidar à luz do canal de telefonia) e transbordo garantido para fila humana via Omni-Channel em suspeita de vítima, com screen-pop de CTI no canal de voz.
2. **Registro e Classificação da Ocorrência** (E02, tamanho L) — criação e classificação do chamado a partir de qualquer canal (WhatsApp, telefonia via CTI ou 0800), com catálogo de mais de 100 subtipos e sincronização com os sistemas legados SIGOR e SIGEO.
3. **Despacho Automatizado de Recursos de Campo** (E03, tamanho L) — motor de agendamento e otimização do Field Service operando nas 14 CGRs, com escalonamento por tempo de espera (regra N/N-10), Console do Dispatcher (mapa/Gantt) e reprocessamento automático em caso de recusa.
4. **Execução em Campo** (E04, tamanho L) — aplicativo único de Field Service Mobile para os 1.152 operadores das 14 empresas terceirizadas, com recebimento de despacho, encerramento com formulário quando aplicável e as três travas de negócio confirmadas (motivo de recusa, foto obrigatória, check-in geolocalizado).
5. **Rastreamento e Visibilidade em Tempo Real** (E05, tamanho S) — rastreamento do cidadão via Appointment Assistant nativo do Field Service e painel agregado para gestores, sobre a mesma base de dados de E02/E03.

O escopo cobre a produção estadual completa — 14 CGRs, 298 viaturas e 1.152 operadores de campo — não apenas o piloto de Cubatão/Taubaté testado na PoC.

## Destaques da Solução

A arquitetura assenta-se em org única do Salesforce, com Field Service como motor central de despacho e Agentforce Contact Center Enterprise cobrindo dois canais de entrada — WhatsApp e telefonia via integração CTI com a URA — ambos transbordando para a mesma fila humana única via Omni-Channel; Service Cloud entra no MVP escopado a esses dois canais, não como plataforma de atendimento ampla (número de licenças a revalidar à luz do canal de telefonia adicional). O modelo de dados reaproveita os objetos nativos do Field Service (Work Order, Service Appointment, Service Territory) e usa o modelo padrão de Skills para o critério de aderência do despacho, evitando um motor customizado do zero. Dois pontos de integração externa compõem o escopo: sincronização com o sistema legado SIGOR (convivência dupla durante a transição) e um retorno síncrono ao SIGEO para correção de coordenadas geográficas após ajuste manual de endereço. O acesso do cidadão ao rastreamento em tempo real é resolvido pelo Appointment Assistant nativo do Field Service — um template de Experience Cloud já embutido na licença de Field Service, sem build de site guest dedicado. O modelo de sharing segmenta a visibilidade por CGR de origem, com exposição pontual em reforços entre regiões, e o login individual por operador (campo e mesa) sustenta a trilha de auditoria exigida pela governança pública.

## Abordagem de Implementação

O programa está sequenciado em 5 fases, com uma Fase 0 dedicada à resolução de discovery — recomendada porque o volume de gaps registrados (80, sendo 7 conflitos de fonte e 5 ainda abertos) excede os limiares que justificam essa fase dedicada antes do build:

- **Fase 0 — Resolução de Discovery**: fecha as perguntas bloqueadoras ao DER/Stefanini antes de iniciar o build, sem épicos associados.
- **Fase 1 — Fundação**: Registro da Ocorrência e Integrações (E02), a base sobre a qual despacho, campo e rastreamento se apoiam.
- **Fase 2 — Despacho e Canal Digital**: Despacho Automatizado (E03) e Canal Digital de Atendimento (E01), em paralelo.
- **Fase 3 — Execução em Campo**: aplicativo mobile para os operadores das 14 UBAs (E04).
- **Fase 4 — Rastreamento e Estabilização**: visibilidade em tempo real (E05) e estabilização em escala estadual.

O caminho crítico segue E02 → E03 → E04 → E05, com E01 correndo em paralelo a partir da Fase 2 — atraso em qualquer ponto desse caminho se propaga para as fases seguintes.

A duração do programa é uma **faixa derivada do formato do engagement, não um compromisso**: **16 a 31 semanas**, classificada como multi-cloud de complexidade média, com a ponta alta ampliada por três fatores específicos deste projeto — a experiência mobile combina múltiplas travas de negócio customizadas sem padrão declarativo nativo equivalente (E04), há uma sobreposição de governança/auditoria ainda em aberto (trilha de auditoria de despacho, tratamento de dados de geolocalização sob LGPD), e o padrão técnico da integração CTI com a URA ainda não está fixado (G0524).

> *Esta figura é benchmark-based, derivada dos dados de treinamento do modelo e padrões gerais de entrega (não validado pela Salesforce) — não é um compromisso. Os números finais são confirmados através do acordo comercial aplicável.*

## Esforço e Disciplinas

O programa concentra 4 dos 5 épicos em tamanho L — o rastreamento e visibilidade (E05) caiu para S nesta revisão, ao trocar o site de rastreamento customizado por Appointment Assistant nativo — o que empurra o esforço para engenharia de integração e desenvolvimento customizado (motor de agendamento, integração CTI, app mobile) mais do que para configuração declarativa pura. As disciplinas necessárias cobrem arquitetura de solução e técnica, consultoria funcional, desenvolvimento (caminho crítico de integração e um pod de build escalando com o volume dos épicos L), garantia de qualidade com surge na fase final de estabilização em escala estadual, e change management.

O workstream de Change Management existe porque o próprio DER solicitou explicitamente até 2 meses de operação assistida e treinamento personalizado por persona, com foco nos técnicos de campo das 14 UBAs — não é uma adição do time de entrega, é uma linha de esforço nomeada pelo cliente para reduzir o risco de adoção numa mudança de processo que afeta 1.152 operadores terceirizados. A experiência do cidadão em si (o link de rastreamento) já foi validada na PoC e não exige pesquisa de UX formal adicional.

## Riscos e Mitigações

- **Trilha de auditoria do despacho ainda sem desenho definido.** Overrides manuais do C2C não têm campos ou retenção definidos, e o padrão nativo (Field History Tracking) tem limite de 20 campos e retenção de 18 a 24 meses — pode não atender à exigência de prestação de contas. *Mitigação*: resolver na Fase 0, decidindo entre o padrão nativo e o add-on Field Audit Trail antes do build do console do dispatcher.
- **Limite contratual das UBAs por CGR não confirmado.** O despacho por proximidade pode indicar uma viatura de CGR vizinha, mas cada empresa terceirizada é contratada por CGR — não está definido se o motor pode atribuir fora desse limite. *Mitigação*: levar ao DER como pergunta bloqueadora antes de configurar o modelo de território.
- **Enforcement das travas de negócio quando o app está offline foi retirado do MVP.** As três travas (recusa com motivo, foto obrigatória, check-in geolocalizado) permanecem como regra de negócio, mas o bloqueio automático de avanço sem rede exige desenvolvimento LWC offline especializado, fora do escopo desta fase. *Mitigação*: validar formalmente essa redução de escopo com o cliente antes do go-live — a evidência ainda é capturada e sincroniza ao reconectar, apenas sem o bloqueio automático.
- **Governança de dados de geolocalização (LGPD/DPIA) sem discussão formal registrada.** O link de rastreamento expõe posição em tempo real, incluindo casos com vítimas de acidente. *Mitigação*: nomear o DER-SP como steward de dados (já assumido) e levar o fluxo de acesso do cidadão à próxima rodada formal de DPIA.
- **Padrão técnico da integração CTI com a URA ainda não fixado (G0524).** A Open CTI clássica está em retirada (fev/2028), o que conflita com a exclusão deliberada de Salesforce Voice do MVP. *Mitigação*: validar com o fornecedor de telefonia (Instinct) a API de CTI exposta antes do build detalhado de E01/E02/E03.
- **Appointment Assistant (E05) ainda não validado em detalhe contra os requisitos específicos do DER.** O comportamento de exibição com 2ª viatura vinculada e o canal de entrega por SMS precisam de confirmação no template nativo. *Mitigação*: revalidar `[KA-6140]`/`[KA-6156]` antes do build detalhado.
- **Licença Field Service Community para os 1.152 operadores terceirizados carrega um known issue documentado** (erro de registro ausente ao abrir Service Appointment). *Mitigação*: testar esse fluxo especificamente em ambiente de build antes de escalar para as 14 CGRs.
- **Lane AI-native ainda não qualificada.** Nenhum sponsor executivo nomeado foi identificado na discovery, e a cadeia de decisão atravessa três organizações (DER, PRODESP, Stefanini) — sem esse compromisso operacional, a compressão de cronograma do modelo AI-native permanece um motivador condicional, não uma entrega planejável.

## Premissas e Nível de Confiança

O escopo dos 5 épicos está com confiança **Confirmed** — validado com o cliente. Os tamanhos T-shirt (M/L) que dimensionam o esforço de cada épico estão com confiança **Assumed** em todos os cinco, o que amplia o risco realizado da faixa de duração para a ponta alta na prática, mesmo sem mover o piso mecanicamente.

O programa carrega **80 gaps identificados** na discovery, dos quais a maioria já tem uma premissa fixada e documentada (a base deste resumo) — mas 7 são conflitos de fonte e 5 permanecem abertos, principalmente em torno da trilha de auditoria de despacho, do modelo contratual das UBAs e do padrão técnico da integração CTI. Esse volume de gaps é o que justifica a Fase 0 dedicada, e recomenda uma sessão de validação com o cliente antes de finalizar o escopo para o build.

## Próximos Passos e Recomendações

1. **Agendar sessão de validação com DER/PRODESP/Stefanini** para fechar as perguntas bloqueadoras (trilha de auditoria de despacho, limite contratual das UBAs) antes do início da Fase 0.
2. **Fixar o padrão técnico da integração CTI com a URA** (G0524) — confirmar se o org do DER está anterior ao corte de disponibilidade da Open CTI (fev/2028) e validar com o fornecedor de telefonia (Instinct) a API exposta, com antecedência ao vencimento do contrato da URA em abril de 2027.
3. **Validar formalmente com o cliente** a redução de escopo do enforcement offline das travas de negócio (E04) antes de comprometer o desenho do app mobile.
4. **Revalidar o Appointment Assistant nativo (E05)** contra os requisitos específicos do DER — comportamento de exibição com 2ª viatura vinculada e canal de entrega por SMS — e levar o fluxo de acesso do cidadão à próxima rodada formal de LGPD/DPIA.
5. Uma vez o escopo validado, seguir para a fase de resolução de discovery com o roteiro já mapeado nos 5 épicos e no plano de 5 fases.

---
*Este resumo é derivado dos dados de scoping do projeto (epics, gaps, estimativas, roadmap e estratégia) — não substitui a validação formal com o DER-SP nos pontos ainda marcados como pergunta bloqueadora ou premissa a confirmar.*
