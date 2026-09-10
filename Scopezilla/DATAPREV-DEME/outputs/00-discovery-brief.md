# Discovery Brief — DATAPREV-DEME (Loja DTP / Marketplace Dataprev)

**Status: rodada parcial.** O usuário sinalizou explicitamente que o conteúdo de discovery ainda não está completo — falta principalmente a **volumetria** (produtos, transações, clientes, contratos, usuários) que Hildegard Paulino Barbosa (DEME) se comprometeu a enviar. Este brief documenta fielmente o que já foi ouvido/lido e mantém como **Open Questions** tudo que depende de material ainda não recebido. Nenhuma posição foi antecipada nas 5 decisões abertas (ver seção 5) — por escolha explícita do usuário nesta sessão.

Gerado em 2026-09-09. Fontes processadas nesta rodada: `DV_Marketplace.pdf` (Documento de Visão v1.1, mai/2026, 33p), `Visao_Solucao_Salesforce_Marketplace_Dataprev.html` (hipótese de arquitetura, Rogério Meira, set/2026), `00-loja-dtp-celebracao-contratual-bsa.md` (material interno BSA, duas visões — Estratégia + Técnica, atualizado 02/09/2026), `01-alinhamento-interno-commerce-dtp-2026-09-09.md` (ata interna Salesforce), `brief-loja-dtp-anotacoes-gemini-2026-08-31.md` (transcrição estruturada da reunião com o cliente, 31/08/2026).

---

## 1. O que é este deal

**Loja DTP** — não confundir com "PAT Marketplace" (outro deal, outro sponsor/ministério). Área DEME da Dataprev (Empresa de Tecnologia e Informações da Previdência), não a área de previdência/agentes. Objetivo: celebração contratual de produtos "de prateleira" (ex.: COMPREV — obrigatório para INSS e 2.100+ RPPS, Decreto 10.188/2019) e, possivelmente, também contratos exclusivos por cliente — ver Decisão 2. Incumbente atual: **ServiceNow**, altamente customizado, quebrando a cada ~6 meses em atualizações de plataforma. Quem implementou o ServiceNow atual — Luis Gabriel Fernandes — hoje é SE Salesforce no time do Rogério Meira, e é autor da hipótese de arquitetura usada nesta rodada.

**Dor nº 1 verbalizada pelo cliente** (Hildegard Paulino Barbosa, DEME): excesso de customização compromete sustentabilidade — requisito central é "o mais nativo possível na plataforma"; customização só quando estritamente necessária.

## 2. Recorte de escopo (Confirmado em 31/08, marcado "Alinhada" nas notas)

- **Dentro**: celebração contratual — catálogo/vitrine, cadastro, autorizador, minuta, assinatura, PNCP, handoff ao ERP, e os atos que geram novo termo (distrato, reajuste, mudança de razão social) enquanto viáveis via automação.
- **Fora**: gestão contratual contínua pós-vigência (NF, RAS, fiscais, consumo — FN10.02, já riscado no DV) e reenquadramento anual COMPREV (NE14) — cobertos por outra ferramenta já integrada ao ERP, ainda sem nome/dono identificado.
- B2B exclusivamente — "nunca B2C" (Hildegard, 00:07:03). O DV v1.1 contradiz isso ao marcar NE15 (cadastro PF) como crítico e "futuro" ao mesmo tempo — tratado como estacionado até o DEME desdizer a fala da reunião.

## 3. Duas fábricas, uma tese em aberto

A reunião descreveu **dois modelos de contratação**: (1) produto de prateleira — catálogo, carrinho, simulação, 9 produtos hoje com plano de expansão; (2) contrato exclusivo por cliente — sem catálogo/carrinho, apenas minuta + assinatura + handoff. O Documento de Visão e a arquitetura do Luis Gabriel desenharam **apenas a fábrica 1**. Se a loja precisar cobrir as duas, Revenue Cloud CPQ é o eixo só da fábrica 1 — não do caso inteiro. **Isso ainda não foi perguntado diretamente ao DEME.**

**Três modelos de comercialização** que qualquer catálogo precisa suportar: (1) consumo bilhetado (sem seleção prévia de volume); (2) faixa de volume mensal (ex.: 5k/10k consultas — CPQ clássico); (3) faixa + componentes opcionais de execução única (instalação, configuração, consultoria).

## 4. Extraction Audit (16 áreas)

| Área | Confiança | Evidência / base |
|---|---|---|
| Identidade da empresa/área | **Confirmado** | Dataprev, DEME. Sponsor: Hildegard Paulino Barbosa. |
| Estado atual (incumbente) | **Confirmado** | ServiceNow, altamente customizado, quebra a cada ~6 meses em upgrade de plataforma. |
| Solução alvo (arquitetura) | **Hipótese interna, não confirmada com o cliente** | Revenue Cloud (catálogo/preço/CPQ/Doc Gen) + Experience Cloud (portal) + Identity Gov.BR + MuleSoft. Agentforce fora do go-live nesta hipótese. Autor: Luis Gabriel Fernandes (SE); ver `knowledge/salesforce-revenue-cloud-experience-cloud-fit-deme.md` — item 3 (Experience Cloud embutir componentes nativos de Revenue Cloud sem Digital Commerce) continua 🔴 sem confirmação em doc oficial. |
| Usuários/personas | **Parcial** | Signatários (PF autorizada por PJ), autorizador do órgão dono do dado, 2 signatários Dataprev por tabela de competência, analista DEME (interno, ≤10 simultâneos — RNF do DV, não descreve a carga real da loja externa). Faltam personas nomeadas: secretário RPPS, autorizador típico (ex. INSS/COMPREV), jurídico, dono do ERP. |
| Timeline/go-live | **Unknown** | Nenhuma data discutida em nenhuma fonte. |
| Objetivos de negócio | **Confirmado** | Sair de customização que quebra; escalar contratação tipo e-commerce (analogia Netflix) para 2.100+ RPPS + expansão de portfólio. |
| Processos centrais | **Confirmado, em detalhe** | 16 NEs / FN-codes no DV, 22 estados de processo (happy path real: 8 passos — vitrine → Gov.BR/PJ → carrinho → papéis/docs → autorizador se aplicável → minuta+assinatura → PNCP se público → handoff+acesso). |
| Integrações | **Confirmado** | Gov.BR (auth), CNIS-PJ (dados PJ), PNCP (publicação = validade jurídica, Lei 14.133), ERP (handoff pós-assinatura, FN10.01), órgão controlador (autorização quando Dataprev é custodiante não proprietária do dado). |
| Migração de dados | **Unknown** | Não discutido em nenhuma fonte. |
| Compliance/regulatório | **Confirmado** | LGPD (custodiante vs. controladora), auditoria TCU, Lei 14.133 Art. 94 (PNCP), Decreto 10.188/2019 (COMPREV), Gov.BR Prata/Ouro para assinatura. |
| Orçamento/budget do projeto | **Unknown** | Nenhum sinal de faixa de investimento; discussão de "orçamento" na reunião foi sobre classificação orçamentária do cliente (dotação), não do projeto. |
| Stakeholders | **Confirmado (lado cliente ainda raso)** | Cliente: Hildegard Paulino Barbosa (Gerente-Executivo DEME, sponsor visível) — únicos presentes confirmados por fala na transcrição. DV v1.1 lista também Thiago Cunha (ausente, médico), Fábio Gasparotto, Rodrigo Lobo, Liliane Frez — não confirmados na reunião de 31/08. Lado Salesforce: Rogério Meira (condução), Luis Gabriel Fernandes (arquitetura), Juliane Lopes, Juliana Brites, Rene Soares, Nelson Filho (presença não confirmada por fala). |
| Riscos/restrições | **Confirmado** | Risco alto: recair em LWC/OmniStudio customizado repetindo a dor do ServiceNow; SoR duplo Salesforce×ERP pós-handoff; rescisão automática por ausência de PNCP em ente público (risco jurídico). Risco médio: SKU Revenue Cloud Advanced (cláusulas condicionais, amend); OCR ≥80%/APIs de terceiro ≤5s; guest user + LGPD em vitrine pública. |
| Sinais de handoff | **Discovery/pré-venda** | Ainda "briefing interno", não oferta — nas palavras do próprio material BSA. |
| Sinais de UX | **Parcial** | Identidade visual Dataprev/Gov.BR DS esperada em Experience; self-service do contratante, mas não "sem gente Dataprev" (autorizador externo, 2 signatários, validação PNCP às vezes manual continuam manuais). |
| Governança | **Não abordado** | Nenhum CoE/change management formal mencionado ainda. |

## 5. As 5 decisões que travam proposta, SKU e SOW (todas em aberto — sem posição do BSA nesta rodada, por escolha do usuário)

1. **Sistema de registro depois da assinatura** — Salesforce (CLM) ou ERP é dono do contrato pós-handoff? Determina se CLM Advanced é necessário ou oversell.
2. **A loja cobre só prateleira, contrato exclusivo, ou os dois?** — determina se Revenue Cloud CPQ é o eixo do caso inteiro ou só da fábrica 1.
3. **PF e chatbot entram em que onda?** — DV marca NE15 (PF) e NE16 (chatbot) como críticos; reunião diz "nunca B2C" e que chatbot não foi a dor nº 1.
4. **Assinatura: registrar o ato ou exigir validade ICP-Brasil/A3?** — muda arquitetura no dia zero (Approval+Flow nativo vs. parceiro de assinatura com custo/homologação). DV trata A3 como desejável; reunião liga validade jurídica ao PNCP, não ao token.
5. **Volumetria, usuários Experience e Org** — produtos, transações, clientes, contratos, usuários (pedido explícito de Rogério Meira, ainda não enviado); e se a loja roda no mesmo Org do programa de previdência/agentes ou em Org próprio do DEME.

## 6. Discrepâncias e pontos de atenção (não fatos — sinalizados para não repetir como se fossem tese fechada)

- **FN10.02 riscado no DV** (portal de NF/RAS/fiscais) — confirmado fora, consistente entre DV e reunião.
- **"Só celebração" + reajuste/distrato automatizado no mesmo fôlego** — só fecha se a loja permanecer dona do termo pós-handoff (ver Decisão 1) ou se o ato for cerimônia de PDF cujo cálculo o ERP refaz.
- **2.100+ RPPS usado como prova de escala** — é base instalada do COMPREV; o trabalho que a movimenta (NE14, reenquadramento) está fora deste deal. Métrica de palco, não tamanho do envelope.
- **"~90% nativo"** — leitura interna de Luis Gabriel sobre a fábrica prateleira, não garantia comercial. Gap duro identificado: ICP-Brasil (que ele lembra não ser necessário no rito atual — a confirmar com jurídica, não de memória).
- **22 estados do DV vs. 8 passos do happy path** — os 22 incluem múltiplos terminais de falha/exceção; útil para desenho de Flow, ruim como slide de processo ("nativo e simples").
- **NE9 (feed para CRM)** — o DV foi escrito como se o Salesforce fosse externo ao "CRM em uso"; se Salesforce for a própria loja, isso não é integração, a oportunidade já nasce no objeto nativo.

## 7. Product Overlay Detection (Step 3.5)

Scan automático do catálogo (`products.json`) contra `.discovery-context.md` retornou apenas um match: **Agentforce Operations** (via keywords genéricas "capa"/"clm", usadas neste material com sentido de "capa do documento" e "Contract Lifecycle Management" — nada a ver com o produto de operações de supply chain/procurement). **Tratado como falso positivo e descartado** — não faz sentido de domínio para este deal (celebração contratual de contratos públicos, não operações de cadeia de suprimentos). Nenhum overlay de produto confirmado nesta rodada. Os produtos centrais em discussão (Revenue Cloud, Experience Cloud, MuleSoft, Agentforce customer-facing, Data 360 Document AI) não são "overlays" no sentido do catálogo — são o núcleo da hipótese de arquitetura, já capturados na seção 4.

## 8. Base de conhecimento

`knowledge/` tem 1 arquivo: `salesforce-revenue-cloud-experience-cloud-fit-deme.md` — nota de pesquisa própria (não documento oficial baixado, não artefato do cliente), que já valida em doc oficial pública: catálogo/pricing/CPQ e CLM nativos (Revenue Lifecycle Management). **Não confirmado**: se componentes nativos de Revenue Cloud/CPQ podem ser embutidos num site Experience Cloud sem depender de Digital Commerce/LWR — item 🔴, decisão de arquitetura interna (reunião 09/09) foi seguir por Experience Cloud + construção de LWC sobre templates, não por confirmação documental. KB central Scopezilla (`kb-search.py`) não foi consultada nesta sessão (MCP de busca `search@aisuite` seguia com falha `ENDPOINT_NOT_FOUND` na última tentativa registrada) — grounding de arquitetura geral permanece parcial até isso ser resolvido ou o gap fechado via Salesforce Docs MCP/diligência com especialista.

## 9. Open Questions (pendentes de material do cliente — não perguntas para grill agora)

- Volumetria completa (produtos, transações, clientes, contratos, usuários) — comprometida por Hildegard, ainda não recebida.
- As 5 decisões da seção 5, todas.
- Nome e dono da ferramenta de pós-vigência (vizinha obrigatória do handoff FN10.01).
- Personas nomeadas: secretário RPPS, autorizador típico (INSS no COMPREV), jurídico Dataprev, dono do ERP.
- Make/buy: por que não reconstruir a loja internamente (Dataprev tem fábrica própria)?
- Caminho de contratação pública (TED, ata, inexigibilidade, licitação) e conflito político com o programa de agentes/previdência.
- Hyperforce Brasil, guest user em vitrine pública — mesa, não detalhe.
- Public Sector Solutions entra na conversa, ou segue Revenue Cloud puro com regra de governo (Lei 14.133, dotação, PNCP)?
- Confirmação da mecânica de "consentimento legal" dos signatários (levantada por Rene Soares, não detalhada).
- Se Salesforce/Experience Cloud realmente embute Revenue Cloud/CPQ nativamente sem Digital Commerce/LWR — pendente de confirmação documental ou diligência com especialista (Luis Gabriel Fernandes é candidato natural).

## 10. Próxima conversa com o DEME (roteiro já sugerido no material BSA)

1. A loja é só prateleira, ou também contrato exclusivo?
2. Depois de assinado, quem é dono de preço e termo — Salesforce ou ERP?
3. Cobrar a volumetria e o DV de ~8 telas de regras (nota: DV_Marketplace.pdf v1.1 já foi recebido nesta rodada — confirmar se é a versão completa ou se ainda falta algo).
4. Nome da ferramenta de pós-vigência — quem opera, quem é dono.
5. Jurídica na sala para PNCP (validade) e ICP-Brasil/A3.
6. PF: reunião disse "nunca B2C", DV diz o contrário — qual vale?

---

**Nota de rodada parcial**: este brief não deve ser usado como base para ROM/estimate/proposta — nem a volumetria, nem as 5 decisões de arquitetura estão fechadas. Próxima sessão de discover deve retomar quando a volumetria e/ou respostas às 5 decisões chegarem.
