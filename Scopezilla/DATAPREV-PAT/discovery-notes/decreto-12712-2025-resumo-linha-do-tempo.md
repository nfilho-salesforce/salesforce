<!-- Source: DuckDuckGo (confirmação da data de publicação) + planalto.gov.br + notas anteriores do projeto · Retrieved: 2026-07-30 · Via: Claude (WebFetch) -->

# Decreto 12.712/2025 — resumo para o projeto + linha do tempo dos prazos (nota de pesquisa)

Nota de grounding para o domínio do projeto DATAPREV-PAT. Consolida **o que o decreto determina no que toca ao nosso escopo** e a **linha do tempo dos prazos**. É a nota-índice do bloco "Decreto 12.712/2025"; as demais aprofundam recortes (credenciamento/economia → `reforma-pat-decreto-12712-2025.md`; ciclo mensal/adquirência → `ciclo-mensal-beneficio-e-adquirencia.md`; adesão da beneficiária → `adesao-empresa-beneficiaria-pat.md`).

## Fontes

- **Data de publicação (confirmada nesta rodada):** Decreto 12.712/2025 **assinado em 11/nov/2025**, **publicado em 12/nov/2025** (marco zero da contagem dos prazos). Fonte: texto do decreto (planalto.gov.br) + análises de imprensa jurídica/mercado via busca.
- **Prazos de interoperabilidade:** **360 dias contados da publicação** para a interoperabilidade total (→ ~nov/2026); marco intermediário de **180 dias** (→ ~mai/2026) para sistemas com +500 mil trabalhadores (nota anterior do projeto). Imprensa também sinaliza regras financeiras entrando em vigor já em **fev/2026**.
- **Base alterada:** o Decreto 12.712/2025 **altera o Decreto 10.854/2021**, que regulamenta o PAT instituído pela **Lei 6.321/1976**.
- **Judicialização:** **ADI 7962 no STF** — decreto **sub judice**; AGU e PGR sustentam a validade.

## O que o decreto determina — no que toca ao nosso projeto

Só transações **dentro do PAT**. Fora do PAT (auxílio-alimentação e outras modalidades) permanecem as condições de contrato.

| Determinação | O que muda | Onde bate no escopo |
|---|---|---|
| **Interoperabilidade / portabilidade** | Um mesmo terminal/credenciamento passa a aceitar cartões de várias bandeiras, sem contratos separados; portabilidade gratuita entre operadoras. | **E04** (credenciamento unificado vira racional) · **G0401** (system-of-record) · **G0403** (credenciamento per-facilitadora vira transitório?) |
| **Teto de MDR de 3,6%** | Taxa de aceitação nas vendas PAT limitada a 3,6% (antes alta e variável por operadora). | **E04** (value driver do estabelecimento) · **E03** (variável do financeiro) |
| **Repasse ao estabelecimento em até 15 dias** | Previsibilidade de caixa; substitui prazos negociados caso a caso. | **E03** (regra do split/settlement) · **G0301** (conta custódia/split) · **G0305** (exceções: split parcial, estorno) |
| **Pré-pagamento obrigatório** | Vedado o pós-pagamento; a empresa paga a recarga antes do crédito nos cartões. | **E03** (fluxo 1 — recarga pré-paga é o coração do financeiro do marketplace) |
| **Fim do rebate** | Proibido o desconto/deságio entre facilitadora e empresa contratante que cruzava os dois fluxos financeiros. | **E02** (taxa de administração passa a ser a variável limpa da cotação) · **E03** |
| **Regras de uso mantidas** | Vale-refeição = refeições prontas; vale-alimentação = gêneros; controle por MCC. | E03/E04 (controle transacional) |

Requisitos cruzados adicionais que o decreto pressiona: **E05** (as APIs de banco público, adquirência e facilitadoras precisam existir — G0501, sem Swaggers hoje) e **E08 / ADR 0001** (residência de dados e org única — G0808 — seguem premissas do projeto, não do decreto, mas convivem com a trilha de auditoria TCU/CGU/ANPD que o programa exige).

## Linha do tempo

| Data | Marco | Prazo (da publicação) |
|---|---|---|
| **1976** | Lei 6.321 institui o PAT e a dedução do IRPJ. | — |
| **2021** | Decreto 10.854 consolida a regulamentação do PAT. | — |
| **11/nov/2025** | Decreto 12.712/2025 **assinado**. | — |
| **12/nov/2025** | **Publicação** — marco zero da contagem dos prazos. | dia 0 |
| **~fev/2026** | Entrada em vigor das regras financeiras (teto de MDR, repasse 15 dias, pré-pagamento, fim do rebate) — sinalizada pela imprensa ("começam a valer em fevereiro"). | ~90 dias |
| **~mai/2026** | Interoperabilidade para sistemas com **+500 mil trabalhadores**. | 180 dias |
| **~nov/2026** | **Interoperabilidade total** — todos os sistemas. | 360 dias |
| **em curso** | **ADI 7962/STF** — decreto sub judice; AGU/PGR pela validade. | — |

## Ligação com o projeto (síntese)

- Os prazos de **fev → mai → nov/2026** são a **premissa regulatória do deal**: definem quando o value driver de E04 (credenciamento unificado + interoperabilidade) e o desenho financeiro de E03 (pré-pagamento, split, repasse 15 dias) deixam de ser "futuro" e viram requisito vigente.
- A **ADI 7962** é o **gate de risco**: se o STF suspender os prazos, o value driver de E04 e as regras de E03 ficam em suspenso — mesma tensão já registrada nas abas Decisões (thread ABBT) e Estimativa (gate regulatório).

## Status da ADI 7962/STF (atualização 30/jul/2026)

- **Quem move:** a **ABBT** (associação das empresas de benefícios ao trabalhador) ajuizou a ADI 7962 pedindo a derrubada de dispositivos do Decreto 12.712/2025, com **pedido de liminar** para suspendê-los. Argumento central: os prazos curtos alteram contratos vigentes e geram "risco de colapso operacional do setor".
- **Defesa:** **AGU e PGR** apresentaram manifestações **defendendo a validade** do decreto.
- **Onde está (pela leitura das fontes):** liminar **pedida, mas não há decisão** confirmada do STF; **sem julgamento de mérito**; relator **não identificado** nas fontes consultadas. Item datado mais recente é de **~maio/2026** (ajuizamento). Fontes escassas para jun–jul/2026 — recomenda-se conferir o andamento no acompanhamento processual do STF.
- **Batalha nas instâncias inferiores:** no início de 2026 operadoras obtiveram **liminares** suspendendo partes do decreto (sobretudo a vedação ao rebate/desconto). Em **24/fev/2026 o TRF-3 reverteu** essas liminares — "as novas regras do PAT voltam" —, recolocando as regras financeiras em vigor.
- **Leitura de risco:** as **regras financeiras** (teto de MDR, fim do rebate, pré-pagamento) **já sobreviveram a uma reversão (TRF-3) e estão em vigor**; o alvo do lobby de adiamento é sobretudo o **cronograma de interoperabilidade** (mai → nov/2026). Base atual: **os prazos seguem valendo** (nov/2026 total ainda "previsto"), com **risco vivo e não resolvido** de escorregar se o STF conceder liminar ou julgar parcialmente.

## Caveats

- **Data de publicação (12/nov/2025) e prazo de 360 dias** confirmados nesta rodada; os marcos de **180 dias (+500 mil trabalhadores)** e **~fev/2026 (regras financeiras)** vêm de nota anterior do projeto e de leitura de imprensa — tratar como datas-alvo, a ratificar contra o texto oficial artigo a artigo.
- **Decreto sub judice (ADI 7962/STF)** — toda a linha do tempo de prazos depende da decisão do STF.
- **Não somos consultoria jurídica** — a leitura é para fins de escopo; validar o enquadramento com a área jurídica do cliente.
