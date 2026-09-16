# SEFIN-CE — Fluxo de Atendimento v2.0 — Transcrição Completa
### Transbordo Humano via Omni-Channel / Service Console (E09)

Base: fluxo v1.0 validado por Nelson Stebulaitis Filho em 02/07/2026. Atualizado em 14/09/2026 para incorporar E09 — Transbordo Humano via Omni-Channel/Service Console (ADD-ON 3), aprovado como tamanho **M** (Digital Engagement license confirmada disponível — G0901 resolvido; headcount 3 PAs em turno único — G0903 resolvido).

Diagrama: `/Users/nfilho/claude/Scopezilla/DATAPREV-SEFIN-CE/outputs/artifacts/SEFIN_CE_Fluxo_v2_Transbordo.png`
Fonte DOT: `/Users/nfilho/claude/Scopezilla/DATAPREV-SEFIN-CE/outputs/artifacts/sefin_ce_fluxo_v2_transbordo.dot`

Seções **4.1–4.6 e 4.8 sem alteração** em relação à v1.0 (reproduzidas abaixo por completude). Seção **4.7 atualizada** e nova seção **4.7-B** substituem o placeholder `[TRANSBORDO — A DEFINIR]`.

---

## 4.1 Entrada

| Nó | Tipo | Ação |
|---|---|---|
| INÍCIO | Evento | Cidadão envia mensagem ao canal WhatsApp da SEFIN-CE |
| SAUDAÇÃO | Ação Agente | Agente envia boas-vindas ao canal SEFIN-CE |
| Veio de HSM? | Condicional | SIM → apresenta contexto do HSM [Q-A: a confirmar] · NÃO → segue para Menu |
| MENU DE SERVIÇOS | Ação Agente | 1. Boleto IPTU · 2. Boleto Taxa do Lixo (TMRSU) · 3. ISS · 4. Preciso de ajuda / Outros |

## 4.2 Identificação do Cidadão

Disparada para IPTU, Taxa do Lixo e Preciso de Ajuda. ISS não requer identificação.

| Nó | Tipo | Ação |
|---|---|---|
| Já identificado? | Condicional | SIM + mesmo CPF → reutiliza sessão, vai para API · SIM + CPF diferente ou NÃO → solicita CPF/CNPJ |
| Validação CPF/CNPJ | Condicional | Válido → solicita Nome · Inválido → até 2 tentativas → esgotou → Pesquisa → Encerra |
| Solicita NOME | Ação Agente | Coleta nome do cidadão |
| Solicita DATA | Ação Agente | Data de Nascimento (PF) ou Data de Abertura RFB (PJ) |
| Validação Data | Condicional | Válida → chama API · Inválida → até 2 tentativas → esgotou → Pesquisa → Encerra |

## 4.3 Consulta Imóvel — API

| Nó | Tipo | Ação |
|---|---|---|
| API ConsultaImovel | Chamada API | Envia CPF/CNPJ + nome + data |
| Serviço OK? | Condicional | NÃO → 1 retentativa automática · NÃO (2ª vez) → Informa falha + registra + AJUDO COM ALGO MAIS? |
| Possui inscrições? | Condicional | NÃO → AJUDO COM ALGO MAIS? |
| Possui inscrições em aberto? | Condicional | NÃO → AJUDO COM ALGO MAIS? |
| Apresenta inscrições | Ação Agente | Apresenta TODAS as inscrições em aberto (sem limite — P-13) |

## 4.4 Emissão DAM — IPTU / Taxa do Lixo

| Nó | Tipo | Ação |
|---|---|---|
| Cidadão seleciona inscrição | Ação Usuário | Seleciona uma inscrição da lista apresentada |
| DAM só no ano vigente? | Condicional | SIM → Confirma emissão diretamente · NÃO → Escolhe Cota Única ou Parcelamento |
| Cota Única / Parcelamento | Ação Usuário | COTA ÚNICA → confirma emissão · PARCELADO → seleciona parcelas · Escolhe ano → ano vigente ou todos os anos |
| CONFIRMA EMISSÃO? | Condicional | SIM → chama API EmitirDamUnico · NÃO → AJUDO COM ALGO MAIS? |
| API EmitirDamUnico | Chamada API | Envia CPF/CNPJ + tipoDebito + tipoPagamento + ano/parcelas |
| Serviço OK? | Condicional | NÃO → 1 retentativa · NÃO (2ª vez) → informa falha + AJUDO COM ALGO MAIS? (sem pesquisa) |
| Envia PDF | Ação Agente | Envia link PDF do DAM via WhatsApp |
| Outra inscrição pendente? | Condicional | SIM → Quer emitir outra? → SIM = loop para seleção / NÃO = AJUDO COM ALGO MAIS? |

## 4.5 ISS

| Nó | Tipo | Ação |
|---|---|---|
| ISS Info | Ação Agente | Informa link do site SEFIN-CE para resolução de ISS [Q-E: URL a confirmar]. Não requer identificação do cidadão |
| Segue para | Fluxo | AJUDO COM ALGO MAIS? |

## 4.6 Preciso de Ajuda / Outros

| Nó | Tipo | Ação |
|---|---|---|
| Solicita CPF/CNPJ | Ação Agente | Reutiliza fluxo de identificação (2 tentativas) |
| Solicita Nome | Ação Agente | Coleta nome para registro |
| Consulta KB | Chamada API | Agente consulta Knowledge Base [Q-F: KB a definir com cliente] |
| KB respondeu? | Condicional | SIM → entrega resposta → AJUDO COM ALGO MAIS? · NÃO → DHA (horário de atendimento) |

## 4.7 DHA — Dentro do Horário de Atendimento *(atualizado v2.0)*

| Nó | Tipo | Ação |
|---|---|---|
| DHA? | Condicional | FORA → informa que atendimento humano só em horário comercial, das 08h às 17h, segunda a sexta (confirmado) → AJUDO COM ALGO MAIS? · DENTRO → coleta nome (se não coletado) → segue para **4.7-B Transbordo Humano** |

## 4.7-B Transbordo Humano — Omni-Channel / Service Console (E09) *(novo v2.0)*

Substitui o placeholder `[TRANSBORDO — A DEFINIR]` da v1.0. Requer Enhanced Omni-Channel [G0902: **confirmado pelo cliente em 2026-09-14** — Standard atinge EOL Summer '26] + Service Console app + Case/Messaging Session como objeto de trabalho roteado.

| Nó | Tipo | Ação |
|---|---|---|
| Monta contexto da transferência | Ação Agente | Reúne CPF/CNPJ, serviço solicitado e transcript da sessão do bot |
| Cria Case/Messaging Session | Chamada API/Plataforma | Roteia via Omni-Channel Enhanced (confirmado) para a fila "Atendimento Tributário" |
| PA disponível? | Condicional | 3 PAs em turno único (G0903 confirmado). SIM → agente assume · NÃO → fila de espera |
| Fila de espera | Ação Agente | Informa posição na fila ao cidadão; aguarda liberação de uma das 3 PAs |
| Agente Humano assume | Ação Agente Humano | Assume no Service Console mantendo a mesma thread WhatsApp (continuidade de contexto) |
| Atendimento humano resolve | Ação Agente Humano | Resolve a solicitação com o contexto SEFIN disponível (ConsultaImovel / EmitirDamUnico) |
| Agente fecha o Case | Ação Agente Humano | Fecha o Case ao concluir o atendimento — segue para Pesquisa de Satisfação (4.8) |

## 4.8 Encerramento Universal

| Nó | Tipo | Ação |
|---|---|---|
| AJUDO COM ALGO MAIS? | Condicional | SIM → volta ao Menu de Serviços · NÃO → Pesquisa de Satisfação |
| PESQUISA DE SATISFAÇÃO | Ação Agente | ⭐ Muito ruim ⭐⭐ Ruim ⭐⭐⭐ Razoável ⭐⭐⭐⭐ Bom ⭐⭐⭐⭐⭐ Muito bom — dispara também no fechamento humano (E09) |
| Nota ≤ 3? | Condicional | SIM → solicita descrição da insatisfação → API Registro · NÃO → API Registro direto |
| API Registro de Contato | Chamada API | CPF/CNPJ + nome + serviço + resultado + nota + justificativa |
| DESPEDIDA | Encerramento | Agente se despede e encerra a conversa |

**EXCEÇÃO** (inalterada): Falha de API após 2 tentativas → informa falha + registra contato + AJUDO COM ALGO MAIS? → SEM pesquisa de satisfação neste caminho.

---

## Premissas Atualizadas (v2.0)

| # | Premissa v1.0 | Premissa v2.0 |
|---|---|---|
| P-02 | Sem transbordo humano confirmado no escopo. DHA dentro do horário sinaliza [TRANSBORDO — a definir]. | **Transbordo humano confirmado via Omni-Channel Enhanced/Service Console (E09).** DHA dentro do horário coleta nome e cria Case/Messaging Session roteado para 1 das 3 PAs (turno único). |
| P-15 | Preciso de Ajuda → coleta CPF/CNPJ + nome → consulta KB → se KB não responde → DHA → [TRANSBORDO]. | Preciso de Ajuda → coleta CPF/CNPJ + nome → consulta KB → se KB não responde → DHA → **Transbordo Humano (4.7-B)**. |

Demais premissas (P-01, P-03 a P-14) permanecem inalteradas.

## Gaps remanescentes ligados ao E09

| Gap | Status |
|---|---|
| G0901 — Digital Engagement licensing | **Resolvido** — confirmado disponível 2026-09-14, não bloqueadora |
| G0902 — Enhanced vs Standard Omni-Channel | **Resolvido (2026-09-14)** — cliente confirmou Enhanced Omni-Channel |
| G0903 — Headcount de PAs | **Resolvido** — 3 PAs em turno único (era assumido 10 no briefing original) |
| G0904 — Horário exato do DHA (Business Hours) | **Resolvido (2026-09-16)** — 08h às 17h, segunda a sexta |
