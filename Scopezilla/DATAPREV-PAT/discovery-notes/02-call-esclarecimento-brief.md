<!-- Source: Reunião de esclarecimento Salesforce × Dataprev + MTE ("[Externa] Sales Force: dúvidas PAT") · Retrieved: 2026-07-30 · Via: Claude (síntese da transcrição) -->

# Brief — Call de esclarecimento PAT (30/jul/2026)

Síntese estruturada dos sinais que esta call trouxe para o escopo. Fonte bruta: `02-call-esclarecimento-transcript.md`. É material **pós-escopo** (as épicas, gaps, roadmap, estimativa já existem) — portanto entra como **revisão** (revise), não como nova discovery.

## Sinais que mudam o escopo

### 1. Arquitetura de org — instância dedicada vs. compartilhada (DECISÃO tomada na call)
O ponto de maior peso. Hoje a Dataprev opera **uma org onde já rodam vários clientes** (MGI/"serviço na ponta", Saúde, MDS). Para o PAT/MTE havia dois cenários:
- **Cenário A** — colocar o PAT dentro da **instância existente compartilhada** (administração única Dataprev).
- **Cenário B** — **instância dedicada, apartada**, exclusiva do MTE/PAT.

Na call a resposta foi **dada e travada**: por **segurança, sensibilidade do dado** (conta custódia, banco público, split/distribuição financeira), **volumetria**, **auditabilidade** (TCU/CGU/ANPD, eventual PF), e porque **o cliente MTE vai administrar** o ambiente (não pode ver "a cozinha" dos demais clientes Dataprev) → **instância dedicada e apartada (Cenário B)**. Fernanda/Ju: *"a administração não pode ficar compartilhada com nenhum outro ambiente… a resposta já está dada."*
- **Porém**: a diretoria do cliente quer **os dois cenários precificados** na proposta (cenário A = valor X, cenário B = valor Y) para decidir. → afeta `estimate`/`commercials` (dual-scenario), não só a arquitetura.
- **Impacto**: isto é uma **premissa de arquitetura load-bearing** (fork resolvido → org dedicada). Candidata a **ADR** — provavelmente **revisa/soma a ADR 0001** (hybrid-residency/org). E as justificativas de segurança/auditoria precisam **constar na proposta**.

### 2. Timeline agressiva — go-live fixo 15/nov/2026
- O cliente precisa da solução **100% rodando em novembro** — **15/nov/2026 é a data de "plano de uso"** (data externa, fixa, citada pelo Flávio).
- Conta de trás pra frente do cliente: proposta assinada ~**15/ago**, para reservar **15/ago → 5/nov** para construção + testes.
- Isto é um **go-live externo imóvel** → aciona o modo do `roadmap` **"data fixa → escopo é a variável de folga"** (trabalhar de trás pra frente, nomear candidatos a de-escopo como buffer). O skeleton atual (18–38 semanas, 5 fases) **não cabe** em ~12 semanas → tensão real a resolver.
- Salesforce sinalizou apetite (times em paralelo, turnos) mas **condicionado** à prontidão das **APIs da Dataprev** e das facilitadoras.

### 3. Volumetria confirmada
- **~800 mil estabelecimentos** e **~450 mil beneficiárias** (empresas). Confirmado como **dentro da capacidade** da plataforma pelo lado Salesforce — mas é justamente o que **empurra a decisão de instância apartada** (item 1) e pressiona as APIs das facilitadoras no fechamento de mês (pico de recargas).

### 4. Segurança / auditoria como requisito explícito de proposta
- Conta custódia de banco público, split/distribuição financeira, boletagem bancária → **observabilidade, auditoria, trilha ANPD/TCU/CGU** deixam de ser transversais implícitos e viram **requisito que precisa estar escrito na proposta com justificativa**. Reforça E08.
- Salesforce sinalizou que precisa **envolver especialistas** (arquitetura bancária/financeira, split, cálculo de percentuais entre bancos) — vai além do CRM básico.

### 5. Portais — entendimento a rever
- Linha 217: o lado Salesforce sinalizou que **as reflexões sobre "a parte dos portais" alteram bastante o racional** e exigem revisão interna. Sinal a **grillar** (o que exatamente muda em E01/portais?) — pode ser ruído de conversa ou mudança real de escopo dos portais/experiência.

## Próximos passos acordados (contexto, não escopo)
- **Sexta 9h**: Salesforce reapresenta o entendimento + arquitetura macro para o cliente **validar**.
- Material técnico (escopo/arquitetura/justificativas) **antecipado**; **preço na terça** (ou quarta).
- Fernanda (Dataprev) enviaria a parte de arquitetura para adiantar o lado Salesforce.

## Como tratar (roteiro de revisão)
Candidatos a mudança confirmada, a serem grillados um a um antes de propagar:
1. **Org dedicada (Cenário B)** — premissa de arquitetura → ADR (revisa/soma 0001) + justificativas de segurança. **Dual-scenario (A/B) para precificação.**
2. **Go-live fixo 15/nov** — `roadmap` modo data-fixa + de-escopo como buffer; tensão vs. 18–38 sem.
3. **Volumetria 800k/450k** — premissa de sizing (confirma E-financeiro/integração; pressão nas APIs facilitadoras).
4. **Segurança/auditoria explícita na proposta** — E08 + narrativa.
5. **Portais** — grillar antes de tratar (mudança real vs. ruído).

## Caveats
- Transcrição automática (Gemini) — nomes e falas podem conter erros de ASR; validar pontos sensíveis contra a memória da call.
- Números da call (800k/450k, 15/nov, 15/ago) são **falados**, a ratificar por escrito com o cliente.
- Decisão de org dedicada foi **verbal e travada na call**, mas a diretoria ainda decide entre A e B na proposta — tratar org dedicada como **forte recomendação/premissa** e precificar ambos.
