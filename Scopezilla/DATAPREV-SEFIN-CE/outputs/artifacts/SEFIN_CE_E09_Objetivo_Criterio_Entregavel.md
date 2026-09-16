# E09 — Transbordo Humano (Service Console + Omni-Channel + Fila + Case Management + Perfis)

Escopo coberto: Service Console · Omni-Channel Enhanced · fila única de atendimento do transbordo (1 regra de roteamento, sem critério) · Case Management 100% nativo · perfis Agente e Supervisor.

Máximo 5 bullets por bloco, pronto para colar no slide.

---

## Objetivo

- Escalonar o atendimento do bot para um agente humano **sem o cidadão perder contexto** — mesma thread de WhatsApp, mesmo Case
- Concentrar o atendimento humano em **uma única fila** ("Atendimento Tributário"), com roteamento simples — sem regras de segmentação por skill, prioridade ou tipo de tributo
- Usar o **Case nativo do Salesforce** como único objeto de trabalho do atendimento humano, sem customização de dados/objetos
- Viabilizar a operação das **3 PAs em turno único** via Omni-Channel Enhanced, evitando construir sobre o Standard (fim de suporte em 2026)
- Dar ao **supervisor** visibilidade e gestão mínima da fila, com apenas 2 perfis no total (Agente + Supervisor)

## Critério de Sucesso

- Agente assume o atendimento no Service Console com **CPF/CNPJ, serviço solicitado e transcript do bot** já disponíveis no Case — sem redigitação
- **100% dos transbordos** chegam por uma única fila, roteados automaticamente pelo Omni-Channel Enhanced às 3 PAs (first-available, sem critério de segmentação)
- Nenhuma regra de roteamento por skill/prioridade/tipo de solicitação é necessária para o Case chegar ao agente
- Supervisor visualiza fila, PAs disponíveis/ocupadas e Cases abertos em tempo real, sem relatório customizado
- Fechamento do Case dispara a pesquisa de satisfação automaticamente, sem etapa manual do agente

## Entregável

- Fila **"Atendimento Tributário"** configurada no Omni-Channel Enhanced, com 1 única regra de roteamento (sem critérios de segmentação)
- **Case** configurado como objeto de trabalho nativo do transbordo — sem campos/objetos customizados fora do padrão Salesforce
- **Service Console** configurado para as 3 PAs, com visão do Case + histórico completo da conversa do bot
- 2 perfis de acesso: **Agente Humano SEFIN** (atendimento) e **Supervisor** (gestão de fila e relatórios)
- Ponto de transferência bot → humano implementado nos 4 fluxos do E02 (IPTU, Taxa do Lixo, ISS, Preciso de Ajuda), todos reaproveitando a mesma fila/Case
