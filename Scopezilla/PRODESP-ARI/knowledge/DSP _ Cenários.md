# Cenários de Entrega — Portal de Crédito Desenvolve SP

**Arquitetura de referência:** Salesforce (front-end) · Sinqia/Workflow (back-end)
**Base:** mapa-funcionalidades-v19 · Lista de APIs · Lista de Componentes (33 mapeados)
**Data:** Agosto de 2026

Estes cenários não fixam prazo — comparam escopo e viabilidade de corte. Estimativas de prazo dependem de composição de time, data de início e velocidade de sprint.

## Por que cortar por esteira não é o argumento certo

O argumento "só Digital" poupa **2 funcionalidades** (F02 e F05) e **zero componentes**. Eis por quê:

### Distribuição por cobertura de jornada

| **Funcionalidade** | **Jornada** | **Componentes dedicados** |
| --- | --- | --- |
| F02 · Cadastro Manual de Conta | Julgamental / Agro | 0 |
| F05 · Cooperativas | Agro | 0 |
| F07 · Biometria Biovalid | Digital | 1 sub (CMP-17, CMP-27) |
| F13 · Aceite Síncrono | Digital | 1 sub (CMP-15) |
| **F01, F03, F04, F06, F08–F12, F14–F22, F23–F24** | **Todas (Geral)** | **31 componentes** |

Cortar Julgamental e Agro elimina F02 + F05 — funcionalidades sem componente dedicado no spreadsheet. Os 31 componentes restantes são os mesmos independente de qual esteira está no escopo.

### O peso está nas telas compartilhadas

A planilha de componentes mapeia 33 itens distribuídos em 5 telas. Nenhuma tela é exclusiva de uma jornada:

| **Tela (spreadsheet)** | **v19 Pilar** | **Comp** | **Integ** | **Itens de maior complexidade** |
| --- | --- | --- | --- | --- |
| Home do Portal | P1 Captação | 9 | 2 | CMP-07 Pendências (F21) · CMP-08 Contratos (F24) |
| Wizard de Solicitação | P2 Pré-qualificação | 6 | 6 | CMP-13 QRSA · CMP-14 Anexos wizard |
| Ficha Cadastral PF | P4 Estruturação | 8 | — | CMP-16 orquestrador · CMP-27 Sócios+Biovalid |
| Ficha Cadastral PJ | P4 Estruturação | 6 | — | CMP-24 orquestrador · CMP-26 listas dinâmicas |
| Acompanhamento | P5/F20 | 1 | — | CMP-30 polling/Platform Events |
| Contratação (CCB) | P6 Formalização | 3 | 4 | CMP-31 orquestrador + assinatura digital |
| **Total** |  | **33** | **19** |  |

**Nota:** a planilha de componentes usa nomenclatura anterior à v19. "Pré-Qualificação" na planilha = Fichas PJ+PF = P4 Estruturação na v19. "Proposta" na planilha = wizard de solicitação = P2 Pré-qualificação na v19. Os 33 componentes mapeados não cobrem F20, F21, F22, F23 integralmente — estão pendentes de mapeamento.

### Ranking de complexidade dos componentes

| **Componente** | **Tela** | **Complexidade** | **Por quê** |
| --- | --- | --- | --- |
| CMP-07 · Pendências | Home | Muito Alta | Agrega múltiplas entidades + Sinqia bidirecional + criação manual backoffice (= F21) |
| CMP-10 · Wizard Solicitação | Solicitação | Muito Alta | Flow/LWC multi-step + persistência incremental + callout Sinqia ao final |
| CMP-30 · Acompanhamento | Aprovação | Alta | Platform Events / polling Sinqia + histórico de status (= F20) |
| CMP-13 · Declarações | Solicitação | Alta | API dinâmica QRSA + radio groups parametrizados + POST rating |
| CMP-16 · Cadastro PF | Ficha PF | Alta | Flow orquestrador + 7 subcomponentes + sync Sinqia |
| CMP-24 · Cadastro PJ | Ficha PJ | Alta | Flow orquestrador + 5 subcomponentes + JUCESP prefill |
| CMP-31 · Contratação | CCB | Alta | CCB API + provedor de assinatura digital (a contratar) |
| CMP-08 · Contratos | Home | Média-Alta | API lista contratos + download CCB + Platform Cache (= F24) |
| CMP-05 · Lista Solicitações | Home | Média-Alta | Apex híbrido + cache + Sinqia por carregamento |
| CMP-27 · Sócios | Ficha PJ | Média | lightning-datatable + regra 100% + Biovalid |

**Conclusão:** os componentes mais pesados (CMP-07, CMP-10, CMP-30) são compartilhados por todas as jornadas. Cortar esteiras não os remove — só remove a lógica condicional dentro deles (que é uma fração do esforço de construção).

## Comparativo Rápido

| **Dimensão** | **Cenário 1 · Completo** | **Cenário 2 · MVP Funcional** |
| --- | --- | --- |
| Funcionalidades | 24 | 18 |
| Integrações | 19 | 12 |
| Componentes mapeados | 33 | 31 |
| Jornadas cobertas | Digital · Julgamental · Agro | Digital · Julgamental (baseline) |
| F21 · Central de Pendências | Incluída | **Excluída** · 1 componente deferido |
| F24 · Meus Contratos | Incluído | **Excluído** · 1 componente deferido |
| F08 · QRSA completo | Incluído | **Simplificado** · só exclusão |
| F07 · Biometria Biovalid | Incluída | **Contingência** · sem API |
| F02, F05 | Incluídas | **Excluídas** |
| F16, F18 | Incluídas | **Excluídas** |
| F19 · Upload | Repositório externo | Salesforce Files (12 MB) |
| F20 · Status | Bidirecional | Leitura only |

## Cenário 1 · Escopo Completo

**Objetivo:** entregar a jornada unificada completa — Digital, Julgamental e Agro — com todas as funcionalidades mapeadas na v19.

### Escopo por Pilar

| **Pilar** | **Funcionalidades** | **Integrações** | **Componentes** | **Observação** |
| --- | --- | --- | --- | --- |
| 1 · Captação | 5 (F01–F05) | 2 | 9 | Inclui F21 (CMP-07) e F24 (CMP-08) na Home |
| 2 · Pré-qualificação | 5 (F06–F10) | 6 | 6 | QRSA completo + Biovalid + SERPRO |
| 3 · Proposta | 3 (F11–F13) | 1 | — | Aceite síncrono Digital |
| 4 · Estruturação | 8 (F14–F21) | 5 | 14+ | 14 componentes fichas + F20 + F21 pendentes |
| 5 · Aprovação | — | — | 1 | CMP-30 (= F20 Acompanhamento) |
| 6 · Formalização | 3 (F22–F24) | 4 | 3 | CCB + assinatura digital (provedor a definir) |
| **Total** | **24** | **19** | **33+** |  |

### Pré-condições para Início

1. Contrato de ocorrências customizadas (F20 + F21) formalizado com Sinqia
2. Estratégia de repositório externo para arquivos > 12 MB (F19)
3. SLA de resposta Sinqia para integração síncrona (F10, F13)
4. Validação regulatória da exibição de resultados QRSA ao tomador
5. Arquitetura do portal de cooperativas decidida (F05)

## Cenário 2 · MVP Funcional

**Lógica de corte:** cortar os 6 itens de maior complexidade que têm workaround operacional disponível, sem restringir jornada. Todas as jornadas recebem o mesmo baseline — a diferença entre Digital e Julgamental (F02, F05 inexistentes) é preservada, mas não é o fundamento do corte.

**Resultado:** 24 → 18 funcionalidades · 19 → 12 integrações · 33 → 31 componentes mapeados

### Escopo por Pilar

| **Pilar** | **Incluídas** | **Cortadas / Simplificadas** | **Comp** | **Integ** |
| --- | --- | --- | --- | --- |
| 1 · Captação | F01, F03, F04 | F02, F05 cortadas · F21/CMP-07 diferido · F24/CMP-08 diferido | 7 | 2 |
| 2 · Pré-qualificação | F06, F09, F10 + F08 parcial + F07 contingência | QRSA completo · Biovalid API | 6 | 4 |
| 3 · Proposta | F11, F12, F13 | — | — | 1 |
| 4 · Estruturação | F14, F15, F17, F19, F20 | F16, F18 cortadas · F21 cortada · F20 read-only · F19 SF Files | 14+1 | 3 |
| 5 · Aprovação | Via F20 | — | — | — |
| 6 · Formalização | F22, F23 | F24 cortada · assinatura CCB diferida | 2 | 2 |
| **Total** | **18** | **6 cortadas** | **31** | **12** |

### Justificativas por Corte (baseadas em componente e integração)

**F21 · Central de Pendências → CMP-07 diferido**
O componente CMP-07 é o mais complexo da Home: agrega entidades de múltiplas solicitações, integra com Sinqia de forma bidirecional e precisa do contrato de ocorrências customizadas — que ainda não está formalizado. Sem F21, o backoffice gerencia pendências por e-mail/Salesforce interno como hoje. Impacto operacional real, mas workaround existe e é o estado atual.

**F24 · Meus Contratos → CMP-08 diferido**
CMP-08 na Home exige API de lista de contratos + download de CCB + Platform Cache. Toda a Formalização (F22, F23) cobre o que o cliente precisa fazer — CCB download e upload. O que F24 acrescenta é consulta histórica de contratos vigentes. Diferir esse componente não bloqueia o ciclo de crédito atual.

**F08 · QRSA Completo → simplificado a exclusão/filtro**
O wizard de solicitação (CMP-13) tem a lógica de declarações parametrizáveis. Para o MVP, manter apenas o filtro de exclusão (setor público, Agro, giro digital) e a declaração de compliance básica — corta 3 das 6 integrações do Pilar 2 e remove a dependência de validação regulatória sobre exibição de resultados ao tomador.

**F07 · Biometria Biovalid → contingência por padrão**
A v19 já documenta a contingência: usuário prossegue sem biometria, proposta vai para análise manual. CMP-17 e CMP-27 mencionam Biovalid mas a lógica de coleta facial é um subfluxo isolado. Para o MVP, todos os clientes usam a contingência — elimina 1 integração externa e o tempo de certificação com o Biovalid.

**F02 · Cadastro Manual + F05 · Cooperativas**
F02 não tem componente dedicado; é um formulário de contingência para PF sem JUCESP. F05 requer decisão arquitetural sobre hierarquia de contas para cooperativas — pendente de design. Ambos são Julgamental/Agro-only. Corte sem impacto em Digital.

**F16 · PDF Estático + F18 · Reabertura de Campos**
Nenhum dos dois exige componente novo: F16 é geração de PDF (workaround via Salesforce relatorio); F18 é um botão de ação rápida no console do backoffice. São os dois itens de menor esforço do P4, mas também de menor criticidade — analista opera sem eles durante o MVP.

**F20 · Orquestração de Status → read-only**
CMP-30 (Acompanhamento) é incluído, mas só na direção Sinqia → Salesforce (leitura de ocorrências para exibir status). A parte de retorno síncrono ao Sinqia — que libera o processo no legado quando o cliente resolve uma pendência — entra junto com F21 na Fase 2, quando o contrato de ocorrências for fechado.

### Integrações Incluídas (12 de 19)

| **API / Serviço** | **Pilar** | **Observação** |
| --- | --- | --- |
| Consulta de Solicitações do Cliente | P1 |  |
| Lista "Parceiro que Indicou" | P1 |  |
| Leitura/Criação de Conta e Contato | P2 |  |
| Criação de Declarações | P2 |  |
| Listas de Valor (múltiplos endpoints) | P2 |  |
| Autorização SERPRO e-CAC | P2 |  |
| API Conta-Proposta (envio ao Sinqia) | P3 |  |
| Detalhamento de Solicitação | P3 |  |
| Categorização de Tipo de Arquivo | P4 |  |
| Armazenamento de Anexos (SF Files) | P4 | Simplificado — sem repositório externo |
| Orquestração de Status (leitura) | P4 | Sem retorno síncrono |
| Download de Ficha CCB | P6 |  |

**Cortadas (7):** Biovalid · QRSA perguntas · QRSA respostas · QRSA cálculo de rating · QRSA assinatura · Assinatura CCB · Lista/Arquivo de Contratos (F24)

### Componentes em Escopo (31 de 33)

| **Tela** | **Comp no MVP** | **Diferidos** | **Observação** |
| --- | --- | --- | --- |
| Home (Captação) | 7 | 2 | CMP-07 (Pendências/F21) e CMP-08 (Contratos/F24) diferidos |
| Wizard Solicitação | 6 | — | CMP-13 simplificado (QRSA só exclusão) |
| Ficha Cadastral PF | 8 | — | CMP-17 sem Biovalid API |
| Ficha Cadastral PJ | 6 | — | CMP-27 sem Biovalid API |
| Acompanhamento (F20) | 1 | — | Read-only, sem Platform Events bidirecional |
| CCB (Formalização) | 3 | — | CMP-32 sem assinatura digital externa; CMP-33 incluso |
| **Total** | **31** | **2** |  |

### Riscos Residuais

* **Sem F21 + F20 bidirecional:** backoffice não tem canal único de pendências no MVP. Pior que hoje para Julgamental — esse custo operacional precisa ser aceito explicitamente antes da decisão de corte.
* **QRSA simplificado:** se a área de crédito exigir o questionário completo como pré-requisito regulatório de qualquer esteira, o corte não é viável. Confirmar antes do início da construção.
* **SF Files 12 MB:** cobre a maioria dos documentos PJ urbanos. Penhor de safra, escrituras de imóvel e outros documentos Agro frequentemente excedem esse limite — o MVP é tecnicamente insuficiente para Agro.
* **Assinatura CCB:** F23 inclui upload de CCB assinada por fora do portal (papel ou plataforma externa). A integração de assinatura digital dentro do portal (CMP-32) fica para Fase 2 — o cliente assina fora e devolve o arquivo.

### O que vai para a Fase 2

| **Item** | **Complexidade** | **Dependência** |
| --- | --- | --- |
| F21 · Central de Pendências + CMP-07 | Muito Alta | Contrato de ocorrências Sinqia |
| F20 · Retorno síncrono ao Sinqia | Alta | Contrato de ocorrências Sinqia |
| F24 · Meus Contratos + CMP-08 | Alta | Definir cache + APIs Sinqia |
| F07 · Biometria Biovalid (integração plena) | Alta | Certificação com Biovalid |
| F08 · QRSA completo (3 endpoints) | Alta | Validação regulatória QRSA |
| CMP-32 · Assinatura digital CCB | Alta | Contratação de provedor de assinatura |
| F19 · Repositório externo de arquivos | Média | Definição de arquitetura |
| F16 · PDF Ficha Cadastral | Baixa | Nenhuma |
| F18 · Reabertura de Campos | Baixa | Nenhuma |
| F02 · Cadastro Manual | Média | Design do fluxo Julgamental/Agro |
| F05 · Cooperativas Agro | Média | Decisão arquitetural hierarquia |

## Sugestão de Sequência de Construção (Cenário 2)

Semana 1 Infra: Experience Cloud · autenticação · named credentials · logs

(Bloqueio: ambiente não provisionado = tudo para)

Semana 2 P1 Home (7 CMP): CMP-01/02/03/04 (alterações) · CMP-05/06 (lista solicitações) · CMP-09 (contas)

F01 (JUCESP) · F04 (Contas) · F03 (Simulador standalone)

Semana 3 P2 Wizard passo 1-3 (CMP-10/11/12): dados gerais + simulação

F06 parcial · F08 (exclusão QRSA) · F09 (SERPRO)

Semana 4 P2 Wizard passo 4-5 (CMP-13/14/15): declarações + anexos + confirmação

F10 (envio síncrono Sinqia) · P3: F11 (lista) · F12 (detalhes)

Semana 5 P3: F13 (aceite Digital) · P4: F14 (Ficha PJ — CMP-24 a 29, 6 CMP)

Semana 6 P4: F15 (Ficha PF — CMP-16 a 23, 8 CMP) · F17 (bloqueio) · F19 (upload SF Files)

Semana 7 P4: F20 (status read-only — CMP-30) · P6: F22/F23 (CCB download+upload — CMP-31/33)

Testes E2E · estabilização



**Semana 5–6 é o gargalo real:** as 14 componentes das Fichas PJ+PF precisam de 2 semanas inteiras. Se houver atraso no alinhamento dos campos com a área de crédito antes da semana 5, a sequência inteira desloca para a direita.
