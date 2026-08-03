# Intent Statements — Phase 2 (DATAPREV-PAT)

> Reference role: the **load-bearing build target** for Phase 2. Each intent below is one capability — one firing trigger or user action, one outcome, one walkthrough. Build one at a time. The phase brief (`10-phase-2.md`) is orchestration; this file is what to build.
>
> **For architects:** walk these with the customer to assign priority and answer open questions. Edit `data/intents.json` (canonical) or this file directly — the next quantum-leap run re-renders from JSON.

## INT-019 — Publicação da demanda como Opportunity nativa (leilão reverso)

epic `E02` · priority _(unassigned)_ · confidence _Confirmed_ · surface `experience-cloud`

### 1. Outcome

A beneficiária registra sua demanda de leilão reverso como uma Opportunity nativa do Sales Cloud, com todos os parâmetros que as facilitadoras precisam para cotar.

### 2. Build target

- Record type/estágios de Opportunity dedicados ao leilão reverso (demanda aberta → em vigência → fechada → selecionada → contratada)
- Campos da demanda: nº de trabalhadores, valor, janela de vigência (início/fim), distribuição por UF, recursos obrigatórios, tipo PAT vs. não-PAT
- Fluxo de autoria no portal Experience Cloud para a beneficiária publicar a demanda
- Account/Opportunity carregam referência tokenizada, nunca CPF (coexiste com ADR 0001)

### 3. Guardrails

- Must not persist CPF on the Account/Opportunity — carry a tokenized reference resolved at runtime (ADR 0001)
- Must not expose demand authoring to a facilitadora — the facilitadora is API-only, without portal UI or license

### 4. Out of scope

- Must not compute or apply payment split (owned by the E03 financial split engine)
- Must not build any facilitadora-facing UI (facilitadora is API-only)

### 5. Acceptance

A analista de RH da Construtora Alfa (CNPJ 12.345.678/0001-90), autenticada via gov.br, abre "Nova demanda", informa 320 trabalhadores, valor-face R$ 44,00/dia, 22 dias/mês, modalidade PAT e janela de vigência de 7 dias. Ao salvar, o revisor confirma que foi criada uma Opportunity nativa do Sales Cloud vinculada à Account da Alfa, com todos esses parâmetros preenchidos e status "Aberta para propostas". Inspecionando a Opportunity e a Account, o revisor confirma que nenhum CPF foi gravado — apenas o CNPJ e uma referência tokenizada resolvida em runtime (ADR 0001).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — Sales Cloud objetos nativos (Opportunity = demanda) _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] Quais campos são obrigatórios na publicação da demanda e como os 'recursos obrigatórios' são estruturados (picklist controlada, multi-seleção)? (Resolver: Workshop de regras do leilão (MTE/Dataprev))
- [ ] A janela de vigência é prazo fixo, configurável pela beneficiária ou por norma? (Resolver: Workshop de regras do leilão (G0205))

---

## INT-020 — Recepção de Quotes das facilitadoras via API dentro da vigência

epic `E02` · priority _(unassigned)_ · confidence _Confirmed_ · surface `automation`

### 1. Outcome

N facilitadoras submetem propostas como Quotes nativas associadas à Opportunity aberta, exclusivamente via API, sem UI nem licença de portal — a equidade é por construção.

### 2. Build target

- Quote nativo associado 1-Opportunity-para-N-Quotes, criado por ingestão de API (via a integração MuleSoft do E05)
- Validação de janela: só aceita Quote enquanto a vigência da Opportunity está aberta
- Submissão informando o ID da cotação/oportunidade aberta; validação de elegibilidade da facilitadora (credenciada + por UF)
- Idempotência na submissão para evitar Quotes duplicadas

### 3. Guardrails

- Must not reveal competing Quotes to a facilitadora (equity by construction — facilitadora has no UI)
- Must not accept a Quote after the vigência window closes
- Must not require a portal license for the facilitadora — she is an API integration, not a seat
- Must not implement Apex managed sharing to hide Quotes — unnecessary given the API-only facilitadora (ADR 0004)

### 4. Out of scope

- Must not push notifications to facilitadoras — the Fase 1 exposes only a pull consultation endpoint (owned by E05); active push is future roadmap (G0211)
- Must not enrich facilitadora history via Data Cloud (de-scope/buffer candidate)

### 5. Acceptance

Alelo, Ticket e VR submetem, cada uma por chamada de API autenticada, uma proposta para a Opportunity aberta da Alfa (MDR de 2,8%, 3,1% e 3,6% respectivamente). O revisor confirma que cada submissão criou uma Quote nativa associada à Opportunity, sem nenhuma sessão de UI nem licença de portal consumida pela facilitadora. Ao tentar, pela API de uma facilitadora, ler as Quotes das outras, o revisor confirma que a resposta não expõe nenhuma proposta concorrente (equidade por construção).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 + G0210 — Quote via API, facilitadora API-only, equidade por construção _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] Qual o payload/auth/idempotência da submissão da Quote e como se garante a elegibilidade por UF? (Resolver: Workshop de regras do leilão + contrato de API E05 (G0207))

---

## INT-021 — Máquina de estados da janela de vigência + trava de seleção até o fechamento

epic `E02` · priority _(unassigned)_ · confidence _Confirmed_ · surface `automation`

### 1. Outcome

O ciclo da demanda transita por estados regidos pela janela de vigência; a beneficiária vê as Quotes conforme chegam, mas a seleção fica travada até a janela fechar (não é seleção cega).

### 2. Build target

- Máquina de estados: aberta → em vigência → fechada → selecionada → contratada, com caminhos de exceção (concluída sem contrato, cancelada)
- Job agendado / Platform Event que fecha a janela no fim da vigência e libera a ação de seleção
- Trava de seleção: a seleção manual só é habilitada após o fechamento da janela

### 3. Guardrails

- Must not allow selection before the vigência window closes
- Must not accept new or revised Quotes after the window closes

### 4. Out of scope

- Must not auto-rank or score Quotes — selection is manual by the beneficiária (G0202), no scoring engine
- Must not compute payment split (E03 financial engine)

### 5. Acceptance

Durante a janela de 7 dias, o revisor acompanha a demanda receber as Quotes; logado como a beneficiária, vê as 3 Quotes recebidas mas confirma que a ação de seleção está indisponível. No fechamento da janela (D+7) o estado transita para "Em seleção" e só então a seleção é liberada. O revisor confirma que nenhuma seleção foi possível antes do fechamento da janela.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 + G0210/G0202 — seleção manual travada até o fechamento _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] O que ocorre no vencimento da janela — fecha automaticamente, permite prorrogação? Facilitadoras podem revisar/retirar proposta? (Resolver: Workshop de regras do leilão (G0205))
- [ ] Quais gatilhos definem 'concluída sem contrato' (ninguém propôs, beneficiária não selecionou, rejeitou todas) e há relançamento? (Resolver: Workshop de regras do leilão (G0206))

---

## INT-022 — Tela Comparar Propostas (LWC) lado a lado

epic `E02` · priority _(unassigned)_ · confidence _Assumed_ · surface `lwc`

### 1. Outcome

A beneficiária compara as Quotes recebidas lado a lado numa tela custom, com os atributos decisórios normalizados para comparação justa.

### 2. Build target

- LWC 'Comparar Propostas' que popula conforme as Quotes chegam
- Atributos comparados: preço por trabalhador, SLA/prazo, cobertura por UF, atendimento aos recursos obrigatórios, taxa/desconto — distinguindo decisórios de informativos
- Normalização das propostas para comparação justa (split Alimentação/Refeição, preço regional por UF, recursos obrigatórios)

### 3. Guardrails

- Must not enable the selection action before the vigência window closes
- Must not reveal Quotes to any facilitadora (view is beneficiária-only)

### 4. Out of scope

- Must not implement a scoring/ranking engine — the beneficiária selects manually (owned by the selection→contract capability)

### 5. Acceptance

Com a janela fechada e 3 Quotes recebidas, a beneficiária abre a tela Comparar Propostas e vê as três lado a lado — MDR, prazo de repasse e valor normalizado por trabalhador na mesma unidade. O revisor confirma o alinhamento dos atributos decisórios para comparação justa e que a ação de selecionar permanece desabilitada enquanto a janela não tiver fechado.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — camada custom fina (tela Comparar Propostas) _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] Quais atributos são comparados, como são exibidos lado a lado e quais são decisórios vs. informativos? (tela ausente no protótipo Figma) (Resolver: Cliente / design de serviço (G0201, G0104))
- [ ] Como as propostas são normalizadas — a facilitadora cota valor único, por UF ou por combinação? Comparação por custo total, por trabalhador/mês ou por UF? (Resolver: Workshop de regras do leilão (G0208))
- [ ] Há regra de desempate e de conformidade mínima quando propostas ficam equivalentes? (Resolver: Posição jurídica MTE/Dataprev (G0204))

---

## INT-023 — Seleção do vencedor → firmamento do contrato

epic `E02` · priority _(unassigned)_ · confidence _Assumed_ · surface `screen-flow`

### 1. Outcome

Após o fechamento da janela, a beneficiária seleciona uma Quote e a plataforma transita a demanda para contrato firmado, com trilha de justificativa.

### 2. Build target

- Ação de seleção habilitada somente após o fechamento da janela
- Transição da Quote selecionada → contrato firmado (mudança de estado da Opportunity)
- Registro de justificativa/motivação da escolha para auditabilidade

### 3. Guardrails

- Must not allow selection before the window closes
- Must not firm a contract without a recorded rationale (auditability for TCU/CGU)

### 4. Out of scope

- Must not run contract lifecycle management — no CLM (redlining, clause library, e-signature); the PDF-upload capability owns the document
- Must not compute payment split (E03 financial engine)

### 5. Acceptance

A beneficiária seleciona a Quote da Ticket (MDR 3,1%) e informa a justificativa "melhor prazo de repasse". O revisor confirma que a demanda transita para "Contrato firmado", a Quote vencedora fica marcada, as demais como "Não selecionadas" e a justificativa fica registrada na trilha — transição só possível após o fechamento da janela.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — transição seleção→contrato na camada custom fina _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] A seleção entre propostas está sujeita à Lei 14.133/2021 (critério de julgamento, motivação obrigatória, publicidade, direito de recurso)? (Resolver: Posição jurídica MTE/Dataprev (G0203))

---

## INT-024 — Upload e versionamento do PDF de contrato (sem CLM)

epic `E02` · priority _(unassigned)_ · confidence _Assumed_ · surface `data-model`

### 1. Outcome

A facilitadora anexa o PDF imutável do contrato com metadados e versões (aditivo = nova versão), sem gestão de ciclo de vida de contrato.

### 2. Build target

- Armazenamento do PDF via Files/ContentVersion, imutável
- Metadados do contrato + relação com a Opportunity/Quote vencedora
- Versionamento: cada aditivo entra como nova versão, preservando as anteriores

### 3. Guardrails

- Must not build contract lifecycle management — no CLM redlining, clause library, obligations or e-signature (Fase 1)
- Must not mutate a prior version — versions are immutable, aditivo = nova versão

### 4. Out of scope

- Must not compute payment split (E03 financial engine)

### 5. Acceptance

A facilitadora Ticket anexa o PDF do contrato firmado com a Alfa. O revisor confirma que o arquivo fica vinculado ao contrato como versão 1, imutável, com metadados (data, partes, vigência). A facilitadora sobe um aditivo e o revisor confirma que ele entra como versão 2 preservando a versão 1, e que não há redline, biblioteca de cláusulas, obrigações nem assinatura eletrônica (sem CLM na Fase 1).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — contrato sem CLM (upload de PDF imutável + versões) _(decisions/0004-sales-cloud-objetos-nativos.md)_
- **Source artifact:** knowledge: CLM é componente nativo do Revenue Cloud, explicitamente fora de escopo na Fase 1 _(knowledge/salesforce-revenue-cloud-marketplace-arch.md:14)_

### Open questions

- [ ] O upload do PDF pela facilitadora é via API (dado que ela é API-only) e qual o conjunto de metadados obrigatórios? (Resolver: Contrato de API E05 + workshop de regras)

---

## INT-025 — Termo de aceite: classificação por faixa salarial + matriz/filial → Novo PAT

epic `E02` · priority _(unassigned)_ · confidence _Assumed_ · surface `screen-flow`

### 1. Outcome

Após o contrato firmado, a beneficiária classifica o nº de trabalhadores acima/abaixo de 5 salários mínimos por CNPJ e matriz/filial, e o aceite é integrado ao Novo PAT via INIS PJ.

### 2. Build target

- Fluxo de termo de aceite acionado após o contrato firmado
- Classificação do nº de trabalhadores acima/abaixo de 5 salários mínimos por CNPJ
- Regra matriz/filial: ao aderir, todas as filiais entram
- Integração do aceite ao Novo PAT via INIS PJ (entregue pela camada de integração do E05)

### 3. Guardrails

- Must not persist CPF — classification is by CNPJ and salary band, not by worker identity (ADR 0001)
- Must not let a filial adhere independently of its matriz — all filiais enter on adhesion

### 4. Out of scope

- Must not build the INIS PJ / Novo PAT integration endpoint itself (owned by E05)

### 5. Acceptance

Após o contrato firmado, a beneficiária classifica por CNPJ e por matriz/filial os trabalhadores acima e abaixo de 5 salários mínimos (matriz /0001-90 → 210 abaixo / 40 acima; filial /0002-71 → 60 abaixo / 10 acima). Ao confirmar o termo de aceite, o revisor confirma que a classificação é integrada ao Novo PAT via INIS PJ e que ela usa CNPJ + faixa salarial — nenhum CPF de trabalhador é gravado (ADR 0001).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — termo de aceite Fase 1-required, integrado ao Novo PAT _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] Qual a fonte da contagem de trabalhadores por faixa salarial e como matriz/filial são resolvidas (CNPJ raiz vs. CNPJ+filial)? (Resolver: MTE/Dataprev + contrato INIS PJ (E05))

---

## INT-026 — Ramificação de regras de cálculo PAT vs. não-PAT

epic `E02` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

Beneficiárias PAT e não-PAT contratam pela mesma plataforma, mas com regras de cálculo distintas — PAT sob o teto de 3,6%, não-PAT sem benefício fiscal.

### 2. Build target

- Ramificação por tipo de beneficiária (PAT vs. não-PAT) na demanda/contrato
- Regra PAT: cálculo sob o teto de 3,6%
- Regra não-PAT: sem benefício fiscal

### 3. Guardrails

- Must not apply the fiscal benefit to a não-PAT beneficiária
- Must not exceed the 3,6% teto for a PAT beneficiária

### 4. Out of scope

- Must not execute settlement or payment split (owned by the E03 financial split engine — dinheiro não transita pela plataforma)

### 5. Acceptance

A Construtora Alfa (PAT) e a Boutique Beta (não-PAT) contratam pela mesma plataforma. O revisor confirma que, para a Alfa, o cálculo aplica o teto de 3,6% e o benefício fiscal do PAT; para a Beta, o mesmo fluxo roda sem o benefício fiscal. Ele confirma que o benefício fiscal nunca é aplicado à beneficiária não-PAT.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — beneficiárias PAT e não-PAT, regras de cálculo distintas _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] O teto de 3,6% aqui é o mesmo da reforma (taxa a estabelecimentos) ou taxa distinta de operação? Desambiguar com a regra de taxa ao MTE. (Resolver: MTE/Dataprev (G0307))

---

## INT-027 — Carga de contratos legados

epic `E02` · priority _(unassigned)_ · confidence _Assumed_ · surface `data-model`

### 1. Outcome

Contratos legados existentes são carregados na plataforma, mapeados à estrutura nativa Opportunity/Quote/Account com seus PDFs e metadados.

### 2. Build target

- Importação dos contratos legados mapeados para a estrutura nativa (Account/Opportunity/Quote + PDF)
- Metadados e vínculo à beneficiária correta (por CNPJ, com referência tokenizada)
- Reconciliação da carga com a fonte legada

### 3. Guardrails

- Must not persist CPF — carry tokenized references (ADR 0001)
- Must not create orphan references — reconcile the load against the legacy source

### 4. Out of scope

- Must not perform the bulk Novo PAT beneficiary/establishment migration (owned by E07)

### 5. Acceptance

O time de migração carrega um lote de 500 contratos legados. Amostrando 5 registros, o revisor confirma que cada um foi mapeado à estrutura nativa Account/Opportunity/Quote com o PDF anexado e os metadados (vigência, MDR, facilitadora), e que nenhum CPF foi persistido — as referências de PF vêm tokenizadas (ADR 0001).

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** decision: ADR 0004 — contratos legados a carregar sobre objetos nativos _(decisions/0004-sales-cloud-objetos-nativos.md)_

### Open questions

- [ ] Qual o formato/fonte dos contratos legados e a chave de deduplicação/vínculo à beneficiária? (Resolver: MTE/Dataprev + escopo de carga (G0404/G0704))

---

## INT-028 — Autocadastro de estabelecimento via gov.br (PJ)

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `experience-cloud`

### 1. Outcome

Um estabelecimento se cadastra uma única vez no portal, autenticado como PJ via gov.br, e a plataforma cria um registro pendente na base nacional unificada de estabelecimentos — substituindo o credenciamento repetido facilitadora a facilitadora.

### 2. Build target

- Portal Experience Cloud com login gov.br (OIDC) no qual o representante da PJ acessa em nome do CNPJ (procuração/e-CNPJ)
- Ao concluir o pré-cadastro, criar um registro de estabelecimento em status pendente na base unificada, chaveado por CNPJ
- Capturar os dados cadastrais não sensíveis do estabelecimento (razão social, CNPJ, endereço, CNAE) para instruir a análise
- Expor ao estabelecimento a visão do seu próprio cadastro e do status de credenciamento

### 3. Guardrails

- Não persistir dado pessoal do representante (CPF) fora da fronteira de residência definida no ADR 0001 — resolver identidade PF em runtime
- Não presumir que a identidade PJ do gov.br está resolvida: o vínculo CPF→CNPJ e o nível de garantia da conta são pré-condição externa

### 4. Out of scope

- Não deve tratar a autenticação como cadastro de PF avulso — o acesso é sempre em nome de um CNPJ
- Não deve expor ao estabelecimento o acompanhamento de repasses financeiros (fora do escopo desta rodada)

### 5. Acceptance

O restaurante Sabor & Cia (CNPJ 98.765.432/0001-10), autenticado como PJ via gov.br, faz o autocadastro no portal uma única vez. O revisor confirma que a plataforma cria um registro pendente na base nacional unificada de estabelecimentos e que não há recredenciamento facilitadora a facilitadora. Ele confirma que o CPF do representante não é persistido fora da fronteira do ADR 0001 — a identidade PF é resolvida em runtime.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014
- **External:** gov.br (OIDC/identidade PJ) — Credenciar o portal como Relying Party e confirmar o mecanismo de representação PJ (e-CNPJ/procuração eletrônica) e o nível de garantia mínimo _(owner: gov.br / Dataprev)_

### 7. Grounding

- **Source artifact:** requirement: Credenciamento de estabelecimento é via portal (não API); pré-cadastro via gov.br, registro pendente na base nacional unificada _(.discovery-context.md (transcrição da revisão persona-a-persona: estabelecimento/Sr. Antônio))_
- **Source artifact:** gap: G0402 — identidade gov.br do estabelecimento (PJ/CNPJ) não coberta pelo login PF+procuração de E01 _(data/gaps.json)_

### Open questions

- [ ] Quem é o system-of-record do credenciamento: um cadastro-base único com N status por facilitadora, ou um credenciamento único que todas honram (G0401)? (Resolver: MTE/Dataprev (Etapa 0))
- [ ] O estabelecimento se autentica como PJ por qual mecanismo do gov.br — representante PF com procuração eletrônica, e-CNPJ ou certificado digital (G0402)? (Resolver: gov.br / Dataprev (Jair Bogo))

---

## INT-029 — Envio de documentos do estabelecimento com checklist guiado

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `experience-cloud`

### 1. Outcome

O estabelecimento sobe os documentos exigidos para o credenciamento (licença sanitária, comprovações de regularidade) anexados ao seu registro, com orientação de quais documentos são necessários e por que o cadastro está pendente.

### 2. Build target

- Componente de upload de arquivos (Files) vinculado ao registro do estabelecimento, um anexo por tipo de documento exigido
- Checklist do que falta enviar e do estado de cada documento (pendente/enviado/em análise)
- Orientação ao estabelecimento sobre documentos e pendências (canal de apoio informacional — assistente é escopo de E06)

### 3. Guardrails

- Não deve deixar o registro avançar para análise humana sem o conjunto mínimo de documentos exigido
- Não deve considerar um documento reenviado como novo enquanto o parecer anterior sobre ele não estiver registrado na trilha

### 4. Out of scope

- Não deve extrair automaticamente todos os campos de todo documento — apenas o que a extração por IA suportar de forma confiável (ver capacidade de captura da licença sanitária)
- Não deve armazenar documento financeiro/de repasse — o escopo é documental de habilitação

### 5. Acceptance

O Sabor & Cia acessa seu registro pendente e vê um checklist do que falta (licença sanitária, comprovação de regularidade fiscal) e sobe os dois documentos. O revisor confirma que ficam anexados ao registro, o checklist marca os itens recebidos e explica por que o cadastro segue pendente, e que o registro não avança para análise humana enquanto o conjunto mínimo de documentos não estiver completo.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** requirement: Estabelecimento sobe documentos (licença de vigilância sanitária e outros); sistema aplica rotinas para dizer se pode operar _(.discovery-context.md (fala Dataprev sobre o que o estabelecimento faz no portal))_

### Open questions

- [ ] Qual é a lista definitiva de documentos exigidos para o credenciamento (CNPJ ativo, CNAE compatível, regularidade/licença sanitária, outros)? (Resolver: MTE (em elaboração com o Ministério))

---

## INT-030 — Validação documental automatizada com transbordo humano

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

A plataforma aplica regras determinísticas de validação sobre o cadastro e os documentos (CNPJ ativo, CNAE compatível com alimentação, integridade do documento) e resolve automaticamente os casos claros, transbordando para análise humana somente as exceções.

### 2. Build target

- Fluxo de validação automatizado que checa as regras verificáveis por máquina e marca cada documento como apto/inapto à decisão automática
- Caminho de transbordo: exceções e casos não determinísticos entram na fila de análise do Analista MTE
- Registro do resultado de cada checagem automática na trilha, para reuso pelo analista

### 3. Guardrails

- Não deve aprovar automaticamente documento sinalizado para análise humana
- Não deve descredenciar nem indeferir por conta própria — a validação automática só instrui; a decisão legal é humana

### 4. Out of scope

- Não deve substituir o parecer do Analista MTE nos casos de exceção
- Não deve validar a licença sanitária por regra rígida de conteúdo (padrões municipais não unificados — ver captura por IA)

### 5. Acceptance

Completo o checklist, a plataforma roda as regras determinísticas: CNPJ ativo na Receita, CNAE compatível com alimentação e documentos legíveis/íntegros. Para o Sabor & Cia (tudo conforme), o revisor confirma que o caso é resolvido automaticamente; para um segundo estabelecimento com CNAE incompatível, confirma que o caso é transbordado para análise humana. Ele confirma que nenhum documento sinalizado para análise é aprovado automaticamente.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** requirement: Sistema aplica rotinas para dizer se o estabelecimento pode ou não vender via auxílio alimentação/refeição; validações herdadas do que a facilitadora fazia (CNPJ ativo, CNAE, regularidade sanitária) _(.discovery-context.md (falas de Lucas e do MTE))_

### Open questions

- [ ] Quais checagens são automatizáveis de forma determinística e quais exigem julgamento humano — onde exatamente fica a linha do transbordo? (Resolver: MTE/Dataprev (workshop de regras de credenciamento))

---

## INT-031 — Análise documento a documento e parecer do Analista MTE

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `console`

### 1. Outcome

Um Analista MTE analisa cada documento do estabelecimento (Válido/Inválido + motivo), emite um parecer sobre o credenciamento (Deferido / Exigência complementar / Indeferido) e toda a operação fica registrada em trilha de auditoria.

### 2. Build target

- Console de análise em que o Analista MTE percorre os documentos do estabelecimento um a um, marcando Válido/Inválido com motivo
- Emissão de parecer no nível do credenciamento com os três desfechos (Deferido / Exigência complementar / Indeferido)
- Trilha de auditoria imutável de quem analisou o quê, quando e com qual motivo — insumo para TCU/CGU/ANPD (E08)
- Notificação ao estabelecimento do desfecho e, em exigência, do que precisa reenviar

### 3. Guardrails

- Não deve permitir parecer Deferido com documento pendente ou marcado Inválido sem justificativa registrada
- Uma exigência complementar deve reabrir o envio apenas dos documentos apontados, sem apagar o histórico de análise

### 4. Out of scope

- Não deve executar a ação legal de aprovar/descredenciar sem passar pela alçada da facilitadora/MTE (capacidade separada)
- Não deve tratar a folha de pagamento ou o financeiro — o escopo é a habilitação documental

### 5. Acceptance

A Analista MTE Regina abre o registro transbordado no console, marca cada documento como Válido ou Inválido com motivo e emite o parecer "Exigência complementar", pedindo a licença atualizada. O revisor confirma que toda a operação fica na trilha de auditoria e que o sistema não permite parecer "Deferido" com documento pendente ou marcado Inválido sem justificativa registrada.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** requirement: Análise documental (habilitação, licenças, regularidade sanitária) que antes era da facilitadora passa a ser feita na plataforma; MTE quer visão de auditoria de tudo que acontece _(.discovery-context.md (falas de Lucas e do MTE sobre análise e auditoria))_

### Open questions

- [ ] Quem de fato emite o parecer de credenciamento — Analista MTE, a facilitadora ou um banco? A transcrição alterna entre os três; os protótipos apontam Analista MTE. (Resolver: MTE/Dataprev (Etapa 0))

---

## INT-032 — Ação legal de aprovar e descredenciar (facilitadora/MTE) com propagação de status

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `console`

### 1. Outcome

A facilitadora mantém o papel legal de aprovar e descredenciar o estabelecimento na sua relação, e o MTE pode descredenciar do programa; a mudança de status vira o estado consultável pela base de estabelecimentos que o adquirente lê antes de transacionar.

### 2. Build target

- Ação de credenciar/descredenciar operada pela facilitadora (e pelo MTE, por motivo: fraude, inadimplência, encerramento de CNPJ, perda de regularidade sanitária)
- Máquina de estados do credenciamento que reflete o desfecho e o disponibiliza como estado atual do estabelecimento
- Trilha de auditoria de cada transição de status com ator e motivo

### 3. Guardrails

- A plataforma não deve descredenciar por conta própria — a ação legal pertence à facilitadora/MTE; a plataforma registra e propaga
- Não deve deixar uma transição de status sem ator e motivo registrados

### 4. Out of scope

- Não deve implementar a API de consulta do adquirente — esse contrato vive em E05 (dependência)
- Não deve decidir se o descredenciamento afeta só a relação daquela facilitadora ou remove do cadastro central antes de a semântica ser ratificada

### 5. Acceptance

A facilitadora Alelo aprova o Sabor & Cia na sua relação; meses depois, o MTE descredencia o estabelecimento do programa por irregularidade. O revisor confirma que cada mudança de status é registrada e que o estado consultável na base de estabelecimentos passa a "descredenciado" (lido pelo adquirente antes de transacionar). Ele confirma que a plataforma não descredencia por conta própria — a ação legal é da facilitadora/MTE; a plataforma registra e propaga.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014
- **External:** Adquirente (Cielo/Rede/Getnet) — Consumir o estado de credenciamento antes de processar transações — via API de consulta por CNPJ exposta por E05 _(owner: E05 / adquirentes)_

### 7. Grounding

- **Source artifact:** requirement: Facilitadora mantém papel legal de aprovar/descredenciar; MTE quer poder descredenciar; adquirente consulta a base periodicamente para não vender a estabelecimento descredenciado _(.discovery-context.md (falas de Lucas, MTE e sobre o adquirente))_
- **Source artifact:** gap: G0405 — semântica do descredenciamento em cadastro unificado (afeta só a relação da facilitadora ou remove do central?) _(data/gaps.json)_

### Open questions

- [ ] Descredenciar afeta apenas a relação daquela facilitadora ou remove o estabelecimento do cadastro central, e quais eventos por motivo propagam (G0405)? (Resolver: MTE/Dataprev)
- [ ] Com a interoperabilidade/aceitação universal de bandeiras (~360 dias), o credenciamento por facilitadora vira transitório? Modelar como bilateral legado, universal ou ambos (G0403)? (Resolver: MTE (fonte oficial do prazo))

---

## INT-033 — Captura da licença sanitária com extração de campos por IA

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

A plataforma captura a data de validade da licença sanitária — o único campo comum aos 5000+ padrões municipais sem base unificada — usando extração por IA sobre o documento enviado, com o analista confirmando o valor quando a extração não for confiável.

### 2. Build target

- Extração por IA da data de validade (e demais campos quando extraíveis) do documento de licença sanitária enviado
- Persistir a data de validade como campo estruturado no registro do estabelecimento, base do rastreio de vencimento
- Fallback de confirmação/entrada manual pelo analista quando a extração não atingir confiança

### 3. Guardrails

- Não deve tratar um campo extraído por IA de baixa confiança como confirmado sem revisão humana
- Não deve depender de layout único de licença — os padrões municipais não são unificados

### 4. Out of scope

- Não deve tentar validar o conteúdo regulatório da licença contra as 5000+ normas municipais — só extrair e datar
- Não deve extrair dados pessoais sensíveis do documento além do necessário à habilitação

### 5. Acceptance

O Sabor & Cia envia a licença sanitária emitida pela prefeitura de Recife. O revisor confirma que a IA extrai a data de validade (31/12/2026) e a preenche no registro. Para uma licença de layout atípico com baixa confiança de extração, ele confirma que o campo fica sinalizado para confirmação e que o analista precisa validar o valor antes de ele ser tratado como confirmado.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** requirement: Licença sanitária tem prazo de validade; ideal integrar com a sanitária; data de validade é o parâmetro mínimo comum; IA pode extrair alguns campos _(.discovery-context.md (fala do MTE sobre licença sanitária e prazo))_

### Open questions

- [ ] Há integração viável com as vigilâncias sanitárias (5000+ padrões municipais, sem base unificada) ou o único campo confiável é mesmo a data de validade extraída do documento? (Resolver: MTE (em discussão com a sanitária))

---

## INT-034 — Rastreio de vencimento, renovação e alertas de expiração

epic `E04` · priority _(unassigned)_ · confidence _Assumed_ · surface `automation`

### 1. Outcome

A plataforma rastreia a data de validade da licença de cada estabelecimento, dispara alertas com antecedência antes do vencimento e conduz o fluxo de renovação, de modo que uma licença não expire silenciosamente e o estabelecimento continue apto.

### 2. Build target

- Job agendado que varre as datas de validade e dispara alertas de expiração com antecedência ao estabelecimento
- Fluxo de renovação: o estabelecimento reentra, sobe a licença renovada e o documento volta para captura/análise
- Transição de status ao vencer sem renovação, refletida no estado consultável pelo adquirente (via E05)

### 3. Guardrails

- Não deve marcar o estabelecimento como apto após o vencimento da licença sem renovação analisada
- Alerta de expiração é notificação; não deve, por si, descredenciar — o desfecho legal segue a alçada da facilitadora/MTE

### 4. Out of scope

- Não deve assumir jornada de acesso frequente do estabelecimento — o acesso é esporádico (renovação periódica), o que orienta o modelo de licença
- Não deve posicionar Marketing Cloud para os alertas enquanto o canal não for definido (G0209/G0211) — alerta transacional nativo/Flow atende

### 5. Acceptance

Para um estabelecimento com licença válida até 31/12/2026, o revisor confirma que a plataforma dispara alertas com antecedência (60 e 30 dias antes) e conduz o fluxo de renovação. Avançando a data de simulação para depois do vencimento sem renovação analisada, ele confirma que o estabelecimento não é marcado como apto — a aptidão só se mantém com renovação analisada.

### 6. Dependencies

- **Internal (build first):** INT-001, INT-014

### 7. Grounding

- **Source artifact:** requirement: Portal absorve a informação de vigência e avisa 'sua licença vai vencer em X meses'; estabelecimento reentra para renovar; gestão dos documentos gera alertas de vencimento _(.discovery-context.md (falas de Rogério e da revisão de jornada do estabelecimento))_

### Open questions

- [ ] Qual o canal do alerta de expiração (e-mail nativo, notificação in-app, webhook) e o modelo de licença Experience Cloud coerente com acesso esporádico do estabelecimento? (Resolver: MTE/Dataprev (licenciamento) — G0108/G0103)

