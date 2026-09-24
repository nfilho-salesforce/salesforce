# 0003 — Zero-migração implica ausência de histórico prévio no go-live; nenhuma consulta retroativa ao sistema legado

**Date:** 2026-09-24 · **Status:** accepted · **Source:** scopezilla-recommended (extends client-supplied fact)

## Context

"Zero migração" está confirmado (ata do cliente) como ausência de carga de dados históricos no novo ambiente no go-live — fato do cliente, não premissa nossa. Mas dois épicos assumem, cada um a seu modo, que existe histórico para consultar: E03/RN-05 exige que o Agentforce entregue um "resumo do histórico" ao atendente (G0303); E07 assume a mesma capacidade de resumo (G0704), sem que nenhuma fonte declare se isso implica uma consulta retroativa em tempo real ao ServiceDesk legado para cidadãos com atendimentos pré-existentes — o que seria um segundo caminho de leitura não documentado, além do par protocolo-entrada/histórico-saída já escopado em E03.

Sem uma regra explícita, o time de build poderia interpretar RN-05 como exigindo lookup-back ao legado — ampliando materialmente a superfície de integração de E03 e os requisitos de acesso a dados do Agentforce, na direção contrária à decisão de "sem migração".

## Decision

Zero-migração implica zero-lookback: o Agentforce resume apenas o histórico gerado nativamente no Salesforce após o go-live. Não há consulta em tempo real ao histórico de tickets do sistema legado para citizens com atendimento pré-existente. Nos primeiros meses pós-go-live, "sem histórico disponível" é o comportamento esperado e normal do agente — uma limitação temporária do MVP a comunicar ao cliente, não uma falha a corrigir.

## Consequences

- E03 mantém sua superfície de integração como hoje escopada (protocolo-entrada + transcrição/histórico-saída), sem um terceiro caminho de leitura retroativa.
- E07 precisa comunicar esta limitação temporária como parte do enablement/change management do go-live, não escondê-la.
- Reversão desta premissa (se o cliente exigir lookup-back) reabre G0303/G0704 e adiciona um novo caminho de integração a E03 — mudança de escopo, não apenas de configuração.

## Grounds

`data/gaps.json` G0303, G0704 — citando RN-05 e a confirmação de zero-migração do inventário/ata. "Zero-migração" é fato client-supplied; a implicação de "zero-lookback" é nossa leitura para torná-lo operacionalmente consistente, a confirmar com o cliente se o comportamento "sem histórico" nos primeiros meses é aceitável.
