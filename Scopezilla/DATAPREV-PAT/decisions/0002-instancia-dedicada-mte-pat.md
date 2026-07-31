# 0002 — Instância Salesforce dedicada e apartada para o MTE/PAT (Cenário B)

**Date:** 2026-07-31 · **Status:** accepted · **Source:** client-supplied

## Context
A Dataprev opera hoje **uma org Salesforce compartilhada** onde já rodam vários clientes (MGI/"serviço na ponta", Saúde, MDS). Para o PAT/MTE havia dois cenários de topologia:
- **Cenário A** — PAT dentro da instância existente compartilhada (administração única Dataprev).
- **Cenário B** — instância dedicada, apartada, exclusiva do MTE/PAT.

Na call de esclarecimento de 30/jul/2026 a resposta foi dada e travada verbalmente: **Cenário B**. Forças que a impuseram: (1) **segurança e sensibilidade do dado** — conta custódia, banco público, split/distribuição financeira; (2) **volumetria** — ~800 mil estabelecimentos e ~450 mil beneficiárias; (3) **auditabilidade** — TCU/CGU/ANPD, eventual investigação; (4) **administração pelo cliente** — o MTE vai administrar o ambiente e não pode enxergar "a cozinha" dos demais clientes Dataprev. Fala registrada: *"a administração não pode ficar compartilhada com nenhum outro ambiente… a resposta já está dada."*

Distingue-se da [[0001-residencia-dados-hibrida]]: aquela premissa governa **onde o dado sensível reside** (Dataprev, nunca persistido no Salesforce); esta governa a **topologia da org** (instância dedicada vs. multi-cliente compartilhada). São eixos independentes e coexistem.

## Decision
O PAT/MTE é entregue em uma **instância Salesforce dedicada e apartada**, isolada das demais orgs de clientes da Dataprev. O isolamento de ambiente é requisito — não opção — pelas razões de segurança, sensibilidade financeira, auditabilidade e administração-pelo-cliente acima. Todos os domínios do PAT (marketplace/credenciamento/financeiro/atendimento) seguem em uma única org dedicada (o eixo "todos os domínios juntos" do gap G0808 se mantém; o que muda é que essa org é apartada, não compartilhada).

**Precificação:** a proposta traz **apenas o Cenário B** (dedicado). A alternativa de dual-scenario A/B foi descartada nesta rodada.

## Consequences
- **Provisionamento** de uma org dedicada entra como pré-requisito de arranque — lead-time que compete com a janela fixa de 15/nov/2026 (ver [[0003-fronteira-crm-nao-transacional]] e o roadmap em modo data-fixa).
- **Licenciamento/comercial** dimensionam sobre uma instância exclusiva (não rateio de ambiente compartilhado).
- **Segurança/auditoria (E08)** deixam de ser transversais implícitos e viram justificativa explícita na proposta.
- Reverter para o Cenário A re-shapearia a arquitetura de ambiente, o modelo de administração pelo cliente e as justificativas regulatórias — alto custo, daí ser premissa.
- Fecha o gap **G0808** na direção "isolamento é forçado por requisito de segurança/auditoria/administração-cliente" (antes assumia-se que nenhum requisito forçava a separação).

## Grounds
`discovery-notes/02-call-esclarecimento-brief.md` §1 (decisão travada na call de 30/jul/2026; diretoria do cliente ratifica na proposta). Volumetria: mesmo doc §3. Ainda **verbal, a ratificar por escrito** com o cliente — premissa forte, não confirmação documental.
