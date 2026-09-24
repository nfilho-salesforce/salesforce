# Research log — PRODESP

## 2026-09-23 — BPMN Poupatempo: cinco decisões, roteamento e identidade visual

- Registro completo em `99-log/2026-09-23-bpmn-poupatempo-registro-da-sessao.md`.
- Quadro FigJam `nnU7s7eXiIfOnoA9xwg9Ww` na **versão 1.9**. Fecha em **30 premissas assumidas de solução**, nenhuma validada com o cliente.
- **F2.7** autenticação gov.br na jornada 1 (elementos 47–51, RN-21, R-08, L-33). **F2.8** Slackbot integrado ao agente do T7, só na jornada 1 (RN-22, L-34). **F2.9** biometria: gateway 52 e integração 53, consulta que não decide nada, vinculada ao serviço de biometria da arquitetura do cliente (RN-23, L-35). **F2.10** o "não sei" do Slackbot é desfecho legítimo e a decisão fica com o atendente (RN-08 na j2, RN-24 na j1). **F2.11** personas Ana, Felipe e Anderson extraídas do deck; ícones Slack, Omni-Channel e Agentforce do SLDS 2.264.1.
- Roteamento dos conectores refeito nas duas jornadas, sem efeito semântico. Eventos de borda dos passos 18, 20 e 25 movidos para a borda superior.
- Não inventar: contra qual base a biometria valida, nível de confiança gov.br, contrato da integração Slackbot ↔ T7, e qual produto Salesforce executa cada passo — essa associação é nossa.
- Pendente: regerar o Lucidchart `73781e03-e981-44c5-bc9e-997617cc3bc8`, onze versões atrás.

## 2026-09-02 — F5.2 Sync E2E (notas Gemini)

- PDF: `[DER SP] Sync E2E - 2026_09_02 13_30 GMT-03_00 - Notes by Gemini.pdf` → `01-fontes/salesforce-oficial/F5.2-…pdf`. Ata Gemini; o PDF pede revisão humana.
- Presentes: Rafael Marques, Renata Vendramini, Juliana Brites. PRODESP não citada.
- Piloto = emergência + vítimas com transferência humana. WhatsApp to-be. URA fora. Salesforce Contact Center não agora (parceiro CCaaS, ex. Genesys).
- 6 casos comerciais = eixos da Carta (fecha #9 em parte). Piloto abre na emergência.
- FS faseado; Community Plus/Partner para terceiros. Emergency Wizard vs território. Massa: Av. do Estado 777.
- AET 48h aparece na ata — **não** copiar como ficha DER (F6.3 não publica).
- Leitura: `03-salesforce/sync-e2e-2026-09-02.md`. Perguntas #2, #3, #4, #7, #9, #10 atualizadas.

## 2026-09-02 — FigJam Co-Create (kit SFD + Carta DER)

- Board: https://www.figma.com/board/L7Ev4ZDSFQKuIbO2PP3bFU (cópia do molde Co-Create Journey Map).
- Tipo do kit abr/2021: Linear Journey · Single Persona. Fases na voz do cidadão (Incidente → Encerramento).
- Preenchido: persona, fases, seções, ações, decisão “resolvido na ligação?”, dores AS-IS (rosa), capacidades POC (verde, intenção), dependências C2C/UBA.
- Mockups de app da faixa Screens ocultos; canais (placa / 0800 / C2C / campo).
- Journey Atlas dos 6 eixos da Carta + Opportunity Overlay na voz do cidadão.
- Method 123 no Services Central ainda não lido (SSO).

## 2026-09-02 — Material oficial DER-SP (briefing único)

- Pedido: pegar todos os insumos oficiais do DER e fazer material completo.
- Briefing git-durável: `04-discovery/material-oficial-der-sp.md` — três planos (Carta F6 / POC F2.1 / infográfico), arquitetura C2C→UBA (57), matriz dos 6 eixos, jornadas AS-IS, overlay emergencial, P-01..P-10, conflitos, o que não afirmar, perguntas #1–#10.
- Canvas ao lado do chat: `DER-SP-material-oficial.canvas.tsx`.
- Jornadas visuais continuam no arquivo SFD `d4B2dN5oS80mUwN7F0WrTx` (6 posters). FigJam AS-IS em `vzMubNF77CNRTvagMe9BYd`.
- Não inventar: 14 DRs nominadas, SLA de chegada, 48h AET, SKU, volume 2026, papel da PRODESP, WhatsApp de socorro no C2C.

## 2026-09-02 — FigJam só AS-IS

- Board reorganizado: https://www.figma.com/board/vzMubNF77CNRTvagMe9BYd
- Removidos TO-BE F2.1 e matriz UC-01..07. Seis eixos da Carta empilhados: Emergencial, Informação, Autorização, Multas, Ouvidoria/SIC, Pátios. Persona = Cidadão. Emergencial = 0800.

## 2026-09-02 — FigJam BPMN dos fluxos da Carta + F2.1

- Board: https://www.figma.com/board/vzMubNF77CNRTvagMe9BYd
- 8 diagramas: Emergencial AS-IS, Emergencial TO-BE (UC-00), Informação, AET/cartão, Multas, Ouvidoria/SIC, matriz UC-01..07, Pátios.
- Tabela no topo: persona, canal, sistema, prazo, natureza da fonte. WhatsApp só no TO-BE.

## 2026-09-02 — Carta de Serviços DER-SP (portais oficiais)

- Pedido: cruzar o recorte visual (6 categorias + rodapé) com **todos** os sites oficiais.
- Catalogado bloco **F6** `[A]` (DER cidadão, separado da F1 PRODESP). Leitura: `04-discovery/carta-servicos-der-sp.md`.
- C2C oficial = Central de Operações e Informações; 0800 055 5510 (24h) + 0800 000 4771 (adm). Fluxo C2C → CCO da UBA → campo. 57 UBAs; guincho leve/pesado + inspeção batem com recursos da F2.1.
- Infográfico **não** é fonte `[A]`. Divergências: ouvidoria 30 d vs ficha 60 d corridos (30/03/2026); AET “48 h” não encontrada; “12+ serviços” vs 30/33 no Portal de Serviços; pátios **3 dias úteis** confirmados.
- Só Emergencial/Informação alimentam o ciclo F2.1. AET, multa, ouvidoria/SIC e pátio ficam fora do catálogo UC-00..07.
- #6 fechada em parte (nome/fluxo C2C). #9 nova (escopo da proposta vs carta completa).

## 2026-08-31 — Fase: proposta + casos de uso (F5.1)

- SA da conta confirma: estamos em **proposta e criação de casos de uso**, não em execução.
- Catalogado F5.1 `[A]` só sobre a fase **nossa**. Não fecha papel da PRODESP, SKU, N, volume.
- Catálogo derivado **somente** da F2.1: UC-00 (ciclo) + UC-01..07 (matriz §15) + P-01..P-10 (aceite).
- Arquivos: `04-discovery/casos-de-uso-der-sp.md`. Canvas ao lado do chat.
- #2 fechada em parte. #8 nova (quem assina P-01..P-10).
- Não inventar baseline/ROI: F2.1 não traz número operacional.

## 2026-08-31 — F2.1 POC DER-SP v01

- Arquivo depositado em `01-fontes/salesforce-oficial/POC versão 01 - 20.08.26.docx.pdf` (181.385 bytes, 9 páginas, mtime 15:02).
- Lido integralmente. Natureza: **intenção** (prova de conceito). O §18 declara caráter exploratório e que **não** é arquitetura definitiva de produção.
- Título nomeia **DER-SP**, não a PRODESP. Não cita SKU, org, autor, AE nem status de execução.
- Catalogado como F2.1. Leitura em `03-salesforce/poc-der-sp-atendimento-rodovia.md`. Extração em `_texto-extraido/`. Sete perguntas em `04-discovery/perguntas-validacao.md`.
- Colateral: PDFs originais F1.1–F1.4 já estavam em `cliente-oficial/negocio/` (28-ago); registro atualizado para apontar o original, não só a extração.

## 2026-08-31 — Bootstrap da pasta + regra de fonte oficial

- Criada a árvore `clients/prodesp/` no padrão Toks/Sem Parar.
- Zona de depósito: `00-inbox/`.
- Quatro extrações já existentes em `01-fontes/cliente-oficial/_texto-extraido/` catalogadas como F1.1–F1.4 `[A]` no registro de fontes, **com ressalva**: originais PDF ainda não depositados.
- Pedido da usuária: dados oficiais e reais; pasta para compartilhar arquivos locais.
- Próximo passo: ela solta arquivos em `00-inbox/` e pede "processa o inbox".
