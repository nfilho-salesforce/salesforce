# 0001 — MVP exclui integração de voz/URA (CTI); unificação de canais vai para fase dedicada do Roadmap, em alto nível de detalhe

**Date:** 2026-09-17 · **Status:** accepted · **Source:** client-supplied (vontade de unificação) + scopezilla-recommended (fasing)

## Context
O DER-SP expressou o desejo de unificar todos os canais de atendimento (WhatsApp, voz/URA, 0800) em uma única plataforma. Hoje a URA é operada pela "Instinct" (vendor terceirizado, migração recente causou instabilidade), com contrato ativo até abril/2027. O MVP já está confirmado como WhatsApp-first (questionário do cliente: "URA, não previsto no MVP"). A pergunta em aberto desde a reabertura deste projeto era se essa integração de voz/CTI deveria entrar no MVP ou ser tratada separadamente.

## Decision
A integração com CTI e um Agente de IA de voz para atendimento **não entram no MVP**. Ficam como uma fase separada e explícita do Roadmap — não uma nota lateral, mas um item detalhado no maior nível de granularidade possível (arquitetura, dependências de contrato/vendor, decisão Open CTI vs. Salesforce Voice), já que o Open CTI legado do Salesforce será retirado em fevereiro/2028 e o contrato da Instinct expira em abril/2027, criando uma janela de decisão real.

## Consequences
- O épico de MVP não carrega escopo de telefonia/CTI — mantém o corte WhatsApp + Field Service + Service Cloud (atendimento geral) limpo.
- O Roadmap (fase futura da metodologia Scopezilla) precisa detalhar esta fase de voz/CTI com o mesmo rigor de uma fase de build, não como um "item futuro" genérico — decisão explícita do usuário.
- A decisão formal Open CTI vs. Salesforce Voice permanece pendente de validação técnica com a Stefanini (itens 1-5 do termo de referência) antes de poder ser detalhada no roadmap.
- Reverter esta premissa (trazer CTI/voz para o MVP) reabriria o dimensionamento de licenciamento e o cronograma de homologação (jan/fev) e produção (abril).

## Grounds
- Questionário do cliente (`DER-SP_Questionario-Cliente-Socorro.xlsx`): "URA, não previsto no mvp."
- Aba `Discovery - Service Cloud CTI` (`scoping-deliverables.xlsx`), Q32-36: retirada do Open CTI em fev/2028, recomendação de Salesforce Voice.
- Granola — Execução PoC (2026-09-17): vendor "Instinct", contrato até abril/2027, validação de itens 1-5 do termo de referência com a Stefanini.
- Instrução direta do usuário nesta sessão (2026-09-17): "quero colocar a integração com CTI e um Agente IA voz para atender como roadmap. Teremos os itens em roadmap separado, é muito importante no maior nível de detalhe possível."
