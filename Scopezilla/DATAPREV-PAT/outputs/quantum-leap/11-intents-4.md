# Intent Statements — Phase 4 (DATAPREV-PAT)

> Reference role: the **load-bearing build target** for Phase 4. Each intent below is one capability — one firing trigger or user action, one outcome, one walkthrough. Build one at a time. The phase brief (`10-phase-4.md`) is orchestration; this file is what to build.
>
> **For architects:** walk these with the customer to assign priority and answer open questions. Edit `data/intents.json` (canonical) or this file directly — the next quantum-leap run re-renders from JSON.

## INT-046 — Carga inicial idempotente de referências não-sensíveis (Bulk API 2.0 + upsert por external ID)

epic `E07` · priority _(unassigned)_ · confidence _Assumed_ · surface `integration`

### 1. Outcome

O conjunto mínimo de beneficiárias, facilitadoras e estabelecimentos necessário ao go-live de 15/nov entra no Salesforce como referências tokenizadas não-sensíveis, sem CPF nem dado nominal persistido, por uma carga re-executável que não duplica registros ao rodar de novo.

### 2. Build target

- Carregar via Bulk API 2.0 as três entidades como registros de referência não-sensíveis: identificador tokenizado que liga cada registro à origem Dataprev/Novo PAT, mais os poucos campos não-sensíveis necessários ao go-live (o dado nominal resolve-se em runtime via API, ADR 0001)
- Idempotência por upsert em external ID (a chave tokenizada é o external ID): re-rodar a carga atualiza em vez de duplicar
- Carga MÍNIMA de go-live apenas — o subconjunto que E02/E03/módulo financeiro precisam referenciar em produção; a base completa (~450k/~800k) fica para depois do go-live
- Beneficiárias e facilitadoras originam do Novo PAT / bases MTE; estabelecimentos NÃO existem de forma unificada hoje e vêm de arquivos internos das facilitadoras, consolidados em um extrato de carga

### 3. Guardrails

- Não persistir CPF nem dado sensível — apenas referências tokenizadas (ADR 0001); o dado nominal resolve-se em runtime via API quando autorizado
- Não tentar carga massiva no MVP — só o conjunto mínimo do go-live; a base completa é pós-go-live
- Não recriar registros ao re-executar — o upsert por external ID é a garantia de que a carga é segura de repetir

### 4. Out of scope

- Não fazer sincronização delta contínua nesta rodada — se o extrato exigir sync recorrente, o escopo migra de evento pontual para pipeline permanente e sobrepõe E05 (G0703)
- Não persistir o dicionário completo de campos do Novo PAT — apenas os campos não-sensíveis do go-live
- Não incluir a extração do lado do Novo PAT — isso vive em E05 (Novo PAT sem API hoje → mock-first)

### 5. Acceptance

Um líder de migração de dados dispara a carga inicial a partir do extrato consolidado; ao final, beneficiárias, facilitadoras e estabelecimentos aparecem no Salesforce como registros de referência com a chave tokenizada preenchida e nenhum CPF gravado; ele roda a mesma carga uma segunda vez e a contagem de registros não muda (upsert atualiza, não duplica).

### 6. Dependencies

- **Internal (build first):** INT-001
- **External:** Novo PAT / bases MTE + arquivos das facilitadoras — extrato consolidado dos cadastros para carga (Novo PAT sem API hoje → mock-first; estabelecimentos vêm de tabelas internas das facilitadoras) _(owner: MTE/Dataprev)_

### 7. Grounding

- **Source artifact:** decision: ADR 0001 residência híbrida — CPF não persiste, só referência tokenizada _(decisions/0001-residencia-dados-hibrida.md)_
- **Source artifact:** discovery: carga inicial de estabelecimentos a partir de arquivos das facilitadoras ('entrar marcado, sem batimento') _(.discovery-context.md)_

### Open questions

- [ ] Qual a fonte, o formato (CSV/API/dump) e a janela do extrato de carga, e quem o provê? É carga one-time ou exige sync delta recorrente? (Resolver: Dataprev/MTE (arquitetura Novo PAT))
- [ ] O volume-alvo real (~450k beneficiárias / ~800k estabelecimentos falado na call) confirma-se por escrito contra o extrato oficial do Novo PAT? Fontes públicas citam ~300–327k. (Resolver: MTE/Dataprev (extrato oficial))

---

## INT-047 — Deduplicação na carga por chave não-sensível

epic `E07` · priority _(unassigned)_ · confidence _Assumed_ · surface `data-model`

### 1. Outcome

Registros duplicados de estabelecimentos e beneficiárias não entram como referências redundantes: a carga reconhece o mesmo CNPJ (ou CNPJ+UF) vindo de fontes diferentes e colapsa em uma única referência tokenizada.

### 2. Build target

- Aplicar regras de duplicidade / regras de correspondência (duplicate rules / matching rules) sobre a chave de negócio não-sensível — candidata: CNPJ, possivelmente CNPJ+UF para estabelecimentos multi-facilitadora
- Colapsar em uma referência única quando o mesmo estabelecimento chega de arquivos de facilitadoras diferentes (o mesmo restaurante credenciado por várias facilitadoras não vira N registros)
- Registrar a decisão de dedup (o que colapsou com o quê) para trilha de auditoria

### 3. Guardrails

- Não deduplicar por dado sensível — a chave de match é não-sensível (CNPJ), coerente com ADR 0001
- Não descartar silenciosamente um registro colapsado — manter trilha do que foi unificado para auditoria (TCU/CGU/ANPD)

### 4. Out of scope

- Não assumir a limpeza contínua no credenciamento (E04) — há sobreposição de escopo E07↔E04 a resolver; esta capability cobre a dedup da carga inicial, não o data-cleansing recorrente (G0704)
- Não fazer enriquecimento/correção de dados — dedup colapsa duplicatas, não conserta campos ruins

### 5. Acceptance

O líder de migração roda a carga sobre um extrato em que o mesmo CNPJ de estabelecimento aparece em arquivos de duas facilitadoras; ao final existe uma única referência para aquele estabelecimento, e o registro de dedup mostra que os dois registros de origem foram reconhecidos como o mesmo pela regra de correspondência.

### 6. Dependencies

- **Internal (build first):** INT-001

### 7. Grounding

- **Source artifact:** discovery: cliente sinalizou 'entrar marcado, sem batimento' para estabelecimentos vindos das facilitadoras — tensão com a exigência de qualidade _(.discovery-context.md)_

### Open questions

- [ ] Qual é a chave de dedup (CNPJ? CNPJ+UF?) e como tratar estabelecimentos credenciados por múltiplas facilitadoras? (Resolver: workshop de regras (Dataprev/MTE))
- [ ] A limpeza/dedup acontece na carga inicial (E07) ou no credenciamento contínuo (E04), e quem é o dono do data cleansing? O cliente sinalizou 'sem batimento' na carga de estabelecimentos — isso rebate a necessidade de dedup no MVP? (Resolver: Dataprev/MTE + Solution Lead (fronteira E07/E04))

---

## INT-048 — Validação de qualidade e reconciliação pós-carga

epic `E07` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

Ao fim da carga há prova de que ela bateu com a fonte-de-verdade e de que nenhum dado sensível foi persistido, com critério de aceite e reprocessamento idempotente em caso de falha parcial — condição para defender a carga em auditoria.

### 2. Build target

- Reconciliar a carga contra a fonte-de-verdade (contagem, amostragem e/ou checksum) e emitir um relatório de aceite
- Verificar conformidade de residência: spot-check confirmando que só referências tokenizadas foram gravadas e nenhum CPF/dado sensível persistiu (ADR 0001)
- Tratar falha parcial de forma idempotente: reprocessar o lote falho sem duplicar nem deixar referências órfãs que quebrem E02/E03
- Definir o critério de aceite da carga (o que caracteriza carga 'boa' para liberar o go-live)

### 3. Guardrails

- Não declarar a carga aceita sem trilha de reconciliação — carga sem prova de batimento é passivo em auditoria TCU/CGU/ANPD
- Não deixar referências órfãs após falha parcial — o reprocessamento é idempotente (casado com o upsert por external ID)
- Não gravar amostras de verificação com dado sensível — o spot-check opera sobre a referência tokenizada

### 4. Out of scope

- Não implementar rollback transacional completo da base — a estratégia é reprocessamento idempotente + reconciliação, não um desfazer atômico de toda a carga
- Não construir observabilidade fim-a-fim da integração em runtime — isso é operação pós-carga (G0507), não a validação da carga inicial

### 5. Acceptance

Depois da carga, o líder de migração abre o relatório de reconciliação: a contagem de referências carregadas bate com a fonte dentro do critério de aceite, uma amostra confirma que só a chave tokenizada foi gravada e nenhum CPF aparece, e um lote propositalmente falho é reprocessado sem gerar duplicatas nem referências órfãs.

### 6. Dependencies

- **Internal (build first):** INT-001

### 7. Grounding

- **Source artifact:** decision: ADR 0001 residência híbrida — base do spot-check de não-persistência de CPF _(decisions/0001-residencia-dados-hibrida.md)_

### Open questions

- [ ] Qual a estratégia de reconciliação/validação pós-carga (contagem, amostragem, checksum) e o critério de aceite? O que acontece em falha parcial — reprocessamento idempotente basta ou exige rollback? (Resolver: Solution Lead + Dataprev (plano de teste/RNF))
- [ ] Qual o inventário de campos não-sensíveis por entidade e a chave de referência tokenizada que liga cada registro à origem Dataprev? Sem o dicionário de dados de referência não há como definir objetos-alvo nem mapeamento origem→destino. (Resolver: arquitetura Dataprev (fronteira de residência — Jair Bogo))

---

## INT-049 — Painel de adoção do portal da beneficiária

epic `E09` · priority _(unassigned)_ · confidence _Unknown_ · surface `lightning-record-page`

### 1. Outcome

Um patrocinador do programa (MTE/Dataprev) enxerga, num painel, o quanto as beneficiárias estão de fato usando o portal e progredindo no funil de cotação — logins, necessidades publicadas, propostas recebidas, seleções e contratos — para dirigir o esforço de adoção onde ele trava.

### 2. Build target

- Relatórios e dashboards do Salesforce sobre a atividade do portal da beneficiária, alimentados por objetos que a plataforma já autora (o ciclo de Cotação/Contratação de E02) e por Login History dos usuários do Experience Cloud
- Métricas de funil: necessidades publicadas → propostas recebidas → seleção travada na janela → contrato firmado, com contagem de 'Concluída sem contrato' como sinal de fricção
- Métricas de engajamento: logins de beneficiárias no período, usuários ativos, tempo até a primeira cotação concluída
- Recortes por dimensão não-pessoal (UF, porte, período) para localizar onde a adoção emperra

### 3. Guardrails

- Must not persistir ou exibir CPF nem identificador pessoal da beneficiária no painel — agrega sobre usuário tokenizado e registros, respeitando a residência híbrida (ADR 0001)
- Must not fixar meta/baseline de adoção inventada — os alvos de % de adoção dependem de KPIs ainda em aberto (G0905 / Open Question 6); o painel mostra o observado, não uma meta cravada
- Must not tratar atividade de facilitadora como login de portal — as ~600-700 facilitadoras são API-only (ADR 0004); a adoção delas é onboarding/certificação de API (E05), não uso de portal

### 4. Out of scope

- Must not incluir campanha de comunicação, roteiro de treinamento, sessões de capacitação ou autoria de material de apoio — são atividades de serviço da PS/MTE, não build de plataforma
- Must not construir corpo de governança pós go-live / CoE / data stewardship — responsabilidade recorrente, não entrega de projeto (G0904)
- Must not medir ou orquestrar a adoção das facilitadoras via portal — pertence à integração de API (E05)

### 5. Acceptance

Uma analista de adoção do MTE/Dataprev abre a aba do painel no início da Fase 4, filtra por UF e pelo mês corrente e vê: logins de beneficiárias, necessidades publicadas, propostas recebidas, seleções travadas e contratos firmados, além da contagem de cotações 'Concluída sem contrato'. Nenhuma célula do painel exibe CPF ou dado pessoal — os números são agregados sobre usuários tokenizados e registros de cotação. Ela identifica que uma UF tem muitas necessidades publicadas mas poucas seleções e direciona o esforço de adoção para lá.

### Open questions

- [ ] Esta épica é entregue pela PS ou pelo cliente (Dataprev/MTE)? E quais audiências (beneficiárias no portal, facilitadoras via API, estabelecimentos, equipe interna) estão no escopo de entrega da PS? Isso decide se sequer há build de painel a fazer e para quem. (Resolver: MTE/Dataprev (patrocínio do programa) — G0901/G0906)
- [ ] Como se define e mede sucesso de adoção (ex.: % de beneficiárias que concluem cotação, tempo até primeira contratação)? Sem baseline/alvo acordado o painel não tem critério de aceite quantitativo — só mostra o observado. (Resolver: MTE/Dataprev — G0905 / Open Question 6)
- [ ] A adesão das facilitadoras é mandatória por lei (Decreto 12.712/2025) ou voluntária? Se voluntária, há resistência ativa esperada (transparência comprime margem — ADI no STF pela ABBT) e o painel de adoção da facilitadora ganha peso; se mandatória, vira conformidade de onboarding de API (E05), fora deste painel. (Resolver: MTE (posição jurídica) — G0902)

