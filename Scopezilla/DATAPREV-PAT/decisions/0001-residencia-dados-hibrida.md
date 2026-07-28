# ADR 0001 — Residência de dados híbrida (dados sensíveis fora da nuvem SF)

- **Status:** Aceito
- **Data:** 2026-07-27
- **Source:** client-supplied (imposição de contexto Dataprev/governo federal)

## Premissa
Dados pessoais sensíveis do trabalhador (CPF, transações vinculadas a CPF) devem
permanecer em infraestrutura sob controle da Dataprev (on-premise / nuvem
governamental), não persistidos na nuvem Salesforce. O Salesforce atua como
camada de orquestração/experiência; a persistência do dado sensível fica na
Dataprev.

## Conclusão (o que isso impõe ao escopo)
- **MuleSoft** orquestra as chamadas às bases Dataprev/Novo PAT sem replicar CPF
  no core Salesforce — padrão de integração *data-at-source* / tokenização de
  referências.
- Objetos Salesforce (Cotação, Proposta, Contrato, Folha) referenciam
  beneficiárias/estabelecimentos por identificador não-sensível; o dado nominal
  é resolvido em runtime via API quando autorizado.
- Impacta DESIGN (diagrama de fluxo de dados / DFD sob LGPD), REQUIREMENTS
  (requisito não-funcional de residência) e o dimensionamento MuleSoft.
- Decisão final de arquitetura de residência (quais campos, qual fronteira) fica
  como **pergunta aberta** a ratificar com a arquitetura Dataprev (Jair Bogo).

## Grounds (fonte)
Reunião de 21/jul/2026 (discovery-notes, PDF Notes by Gemini): discussão explícita
de "residência nacional dos dados (nuvem vs. Oracle on-premise — decisão em
aberto)". Confirmado por Nelson (27/jul/2026) como diretriz híbrida para o ROM.

## Alternativas consideradas
- **Nuvem SF Brasil (Hyperforce BR):** residência nacional, porém persiste CPF
  na nuvem SF — rejeitada nesta rodada por conservadorismo LGPD/ANPD do cliente.
- **Tudo on-premise:** inviabiliza o valor da plataforma SaaS — descartada.
