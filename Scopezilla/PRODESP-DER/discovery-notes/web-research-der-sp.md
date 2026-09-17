---
research_date: 2026-09-17
researcher: scopezilla-dev:researcher (Claude)
project: PRODESP-DER (DER-SP — Field Service + Service Cloud + Agentforce, atendimento emergencial de rodovias)
method: >
  Web research via Bing search results page (fetched through WebFetch) plus direct fetch of
  official/public source pages. No browser automation was available in this environment
  (Playwright launch blocked by system policy: "DevTools remote debugging is disallowed by the
  system admin"), and Google/DuckDuckGo blocked automated fetch (error page / CAPTCHA). Bing's
  static SERP was the only reliable query surface found. Findings below are limited to what
  surfaced through that channel on 2026-09-17; absence of a finding does not mean the fact is
  false, only that it isn't indexed/discoverable via this method today.
sources_consulted:
  - https://pt.wikipedia.org/wiki/Departamento_de_Estradas_de_Rodagem_do_Estado_de_S%C3%A3o_Paulo
  - https://www.sp.gov.br/sp/institucional/estrutura/autarquias/der
  - https://www.der.sp.gov.br/der (403 Forbidden to automated fetch)
  - https://pt.wikipedia.org/wiki/DERSA
  - https://www.al.sp.gov.br/repositorio/legislacao/lei/2019/lei-17148-13.09.2019.html
  - https://g1.globo.com/sp/sao-paulo/noticia/2019/09/10/extincao-da-dersa-e-aprovada-na-assembleia-legislativa-de-sp.ghtml (title/snippet only, full fetch blocked)
  - https://pt.wikipedia.org/wiki/Agência_Reguladora_de_Serviços_Públicos_Delegados_de_Transporte_do_Estado_de_São_Paulo
  - https://ccm.artesp.sp.gov.br/rodovias/ocorrencias
  - https://dadosabertos.artesp.sp.gov.br
  - https://infosiga.detran.sp.gov.br / https://dadosabertos.sp.gov.br/dataset/sinistros-infosiga
  - https://mobilidadesampa.com.br/2025/09/infosiga-3-0-dados-transito/
  - https://g1.globo.com/sp/sao-paulo/noticia/2024/05/16/... (title/snippet only, full fetch blocked)
  - Bing SERPs (www.bing.com/search) for: DER-SP km rede, DER-SP orçamento/LOA, PRODESP+Salesforce, CCR/ARTESP TMA, Instinct URA, Stefanini+PRODESP, SIGOR, DER-MG, PRODESP+edital+WhatsApp
---

# Pesquisa Web — DER-SP / PRODESP (contexto de mercado para scoping)

## Resumo executivo

A pesquisa pública confirma a estrutura organizacional básica do DER-SP (14 unidades regionais, o que valida o número de "14 CGRs" citado no projeto) e localiza dois ativos públicos de dados de trânsito/ocorrências genuinamente úteis como referência de mercado: o **CCM da ARTESP** (portal de ocorrências relevantes em rodovias concedidas, com taxonomia de tipos de ocorrência incluindo "pane mecânica/elétrica/seca") e o **Infosiga 3.0** do Detran-SP (painel estadual de sinistros de trânsito, relançado em setembro/2025, com a **PRODESP como parceira de implementação** confirmada). Este último é o achado mais relevante para o engagement: mostra que a PRODESP já entrega plataformas de dados de segurança viária para o governo do estado, em parceria com Detran-SP e a Bloomberg Initiative for Road Safety — um precedente direto e citável de "PRODESP como braço de TI para modernização de segurança rodoviária em SP".

Não foi possível confirmar publicamente: quilometragem total da malha sob gestão direta do DER-SP (não-concedida), orçamento/LOA específico do DER-SP, qualquer edital ou notícia pública sobre o projeto WhatsApp+Field Service em si (esperado — provavelmente ainda não publicizado nesta fase de discovery), o sistema legado "SIGOR" citado nas notas internas (o termo colide publicamente com um sistema não relacionado da CETESB de resíduos sólidos — não encontrei nenhuma página pública que descreva um "SIGOR" de ocorrências rodoviárias do DER-SP), o fornecedor de URA "Instinct" citado nas notas internas (nome genérico demais para busca pública — nenhum resultado relevante), nem qualquer contrato específico Stefanini–PRODESP de telefonia. A DERSA (empresa de desenvolvimento rodoviário do estado, historicamente citada como benchmark) foi **extinta por lei em 2019** — não é mais um comparador operacional válido.

**Implicação central para o scoping:** os achados dão munição para o business case (custo social/fiscal de sinistros em SP é mensurável e alto) e para o posicionamento da PRODESP (já entrega plataformas estaduais de segurança viária), mas não sustentam nenhuma alegação numérica específica sobre escala física do DER-SP ou orçamento do projeto — essas afirmações devem continuar vindo exclusivamente dos documentos de discovery internos, não de fontes públicas.

---

## Achados

### 1. DER-SP — estrutura organizacional

> **DER-SP é dividido em 14 divisões regionais (DR-01 a DR-14), cada uma subdividida em "residências de conservação".** As sedes regionais incluem Campinas, Itapetininga, Bauru, Araraquara, Cubatão, Taubaté, Assis, Ribeirão Preto, São José do Rio Preto, São Paulo, Araçatuba, Presidente Prudente, Rio Claro e Barretos.
> Significado para o engagement: confirma de forma independente o número de "14 CGRs" usado no projeto como escala de rollout — é consistente com a estrutura regional histórica do órgão (ainda que a nomenclatura "CGR" não apareça no texto, que usa "regionais"/"DR").
> Source: `https://pt.wikipedia.org/wiki/Departamento_de_Estradas_de_Rodagem_do_Estado_de_S%C3%A3o_Paulo` | Confidence: `Medium` (fonte secundária, mas dado estrutural verificável e estável historicamente)

> **DER-SP foi criado pelo Decreto nº 6.529 (2 de julho de 1934) e tornou-se autarquia pelo Decreto nº 16.546 (26 de dezembro de 1946).**
> Significado: útil apenas como contexto institucional/histórico para narrativas de proposta ("quase 90 anos de história").
> Source: `https://pt.wikipedia.org/wiki/Departamento_de_Estradas_de_Rodagem_do_Estado_de_S%C3%A3o_Paulo` | Confidence: `Medium`

> **Sergio Henrique Codello Nascimento é listado como Presidente do DER-SP.**
> Significado: nome de referência institucional para eventuais menções de patrocínio executivo — deve ser verificado contra fonte primária antes de uso em qualquer documento client-facing, pois pode ter mudado.
> Source: `https://www.sp.gov.br/sp/institucional/estrutura/autarquias/der` | Confidence: `Low` / não verificado contra fonte primária de identidade (LinkedIn ou página de liderança dedicada) — tratar como não confirmado.

> **Quilometragem total da malha sob gestão do DER-SP: não encontrada publicamente.** Múltiplas buscas (termos diretos e variações) retornaram apenas páginas institucionais/serviços do DER-SP, sem estatística de extensão de malha.
> Significado: qualquer número de "X mil km" usado no scoping deve vir dos documentos internos de discovery (ou ser explicitamente marcado como pendente de confirmação com o cliente) — não há como validar externamente com os recursos disponíveis nesta pesquisa.
> Source: N/A (busca sem resultado) | Confidence: `Low` / não encontrado, sinalizar para verificação com o cliente.

> **Orçamento público do DER-SP (LOA, editais, atas de registro de preço): não localizado.** Busca por "DER-SP orçamento 2026 LOA" retornou apenas páginas institucionais.
> Significado: para dimensionar teto de investimento do projeto, será necessário consultar diretamente o Portal da Transparência do Governo de SP ou a Lei Orçamentária Anual publicada pela ALESP — não foi possível fazer isso via busca indexada nesta sessão.
> Source: N/A | Confidence: `Low` / não encontrado.

### 2. DERSA — não é mais um comparador operacional válido

> **A Dersa (Desenvolvimento Rodoviário S.A.), companhia de economia mista do governo de SP historicamente responsável por parte da rede viária estadual, foi extinta por lei em 2019** (Lei nº 17.148, de 13/09/2019, que autorizou "a dissolução, liquidação e extinção da Dersa"), aprovada pela Assembleia Legislativa em 10/09/2019.
> Significado: se as notas internas do projeto ou qualquer benchmark competitivo citarem a Dersa como referência de "outro DER estadual" que usa CRM para despacho, isso está desatualizado — a empresa está em liquidação, não é um operador ativo comparável.
> Source: `https://www.al.sp.gov.br/repositorio/legislacao/lei/2019/lei-17148-13.09.2019.html` | Confidence: `High` (fonte primária — texto da lei estadual)

### 3. ARTESP — benchmark de taxonomia de ocorrências em rodovias concedidas de SP

> **O CCM (Centro de Controle Multimodal) da ARTESP mantém um portal público de "ocorrências relevantes" em rodovias concedidas, com taxonomia estruturada:** classes amplas (Acidentes, Eventos Naturais, Obras, Ocorrências Gerais) e subclasses incluindo colisão, tombamento, incêndio em veículo, queda de talude, animais na pista, derramamento de carga, emergência médica, manifestações e operações de tráfego. Critério de "relevância" inclui bloqueio total/parcial de pista, vítimas fatais ou de repercussão, incidentes em faixa de domínio, filas de 2+ km, entre outros. Cada registro tem código único (ex. OC20992), referência MITS, concessionária, rodovia/km, município, status de interdição e contagem de vítimas por severidade (Fatal/Grave/Moderada/Leve/Ileso).
> Significado para o engagement: é um modelo público, real e já em produção de taxonomia de ocorrências de rodovia no estado de SP — diretamente reutilizável como referência para o design de categorias de ocorrência (pane vs. sinistro/acidente) no Field Service do DER-SP, e para justificar campos obrigatórios (severidade, status de bloqueio, localização por km).
> Source: `https://ccm.artesp.sp.gov.br/rodovias/ocorrencias` | Confidence: `High` (portal oficial público, dados observados diretamente)

> **O dataset "Categorias de Ocorrências" do portal de dados abertos da ARTESP inclui explicitamente "panes elétricas, mecânicas e secas"** como subcategoria de ocorrência geral, além de alagamento, erosão e queda de talude.
> Significado: confirma que "pane mecânica" já é uma categoria padronizada no setor rodoviário paulista — reforça que o MVP do DER-SP (foco em pane + sinistro) está alinhado à prática de mercado regional.
> Source: `https://dadosabertos.artesp.sp.gov.br/dataset/categorias-de-ocorrencias` | Confidence: `High`

> **A malha rodoviária concedida regulada pela ARTESP tem aproximadamente 6.900 km, administrada por 20 concessionárias** (dado de contexto histórico 1998–2016 apresentado no artigo da Wikipedia, incluindo R$ 89 bilhões investidos no período em obras/operação/manutenção).
> Significado: é a malha **concedida** (privada), não a malha sob gestão direta do DER-SP (pública, foco deste projeto) — não confundir os dois universos ao citar escala. Útil apenas como contraste ("SP tem dois sistemas paralelos de gestão viária: concessões via ARTESP e rede direta via DER").
> Source: `https://pt.wikipedia.org/wiki/Agência_Reguladora_de_Serviços_Públicos_Delegados_de_Transporte_do_Estado_de_São_Paulo` | Confidence: `Medium` (fonte secundária, dado possivelmente datado — não confirmado para 2026)

> **Tempos médios de atendimento (TMA) para socorro mecânico/guincho em concessões — não localizados publicamente** nas buscas realizadas (CCR/Motiva, ARTESP SASI). Os resultados retornaram apenas páginas institucionais genéricas de concessionárias, sem métricas de TMA divulgadas.
> Significado: não há benchmark numérico público de TMA para citar no discovery — se o cliente ou a PRODESP tiverem esse dado internamente (ex. contratos de concessão com metas de tempo de atendimento), deve vir de lá, não de fonte pública.
> Source: N/A | Confidence: `Low` / não encontrado.

### 4. Infosiga / Detran-SP — precedente direto de entrega PRODESP em segurança viária

> **O Governo de SP relançou o "Infosiga 3.0" em setembro de 2025, painel estadual de estatísticas de sinistros de trânsito do Detran-SP, com parceria explícita entre "Detran-SP, Iniciativa Bloomberg para a Segurança Viária, Prodesp e a consultoria Tech Solutions".**
> Significado: é o achado mais forte para o posicionamento comercial do projeto — mostra a PRODESP já atuando como integradora/parceira de tecnologia em iniciativas estaduais de segurança viária e dados de trânsito, o que reforça a lógica de "PRODESP como braço de TI para modernização de atendimento emergencial em rodovias" nesta proposta.
> Source: `https://mobilidadesampa.com.br/2025/09/infosiga-3-0-dados-transito/` | Confidence: `Medium` (fonte jornalística secundária, mas específica e verificável)

> **Em 2024, São Paulo registrou 135.545 sinistros de trânsito no estado, com custo estimado de mais de R$ 12 bilhões aos cofres públicos** (R$ 7,7 bilhões só em vias urbanas, embora o custo por acidente seja maior em rodovias).
> Significado: é um número estadual agregado (todas as vias — municipal, estadual e federal — não apenas malha DER), mas serve como âncora de business case para justificar investimento em modernização de atendimento emergencial: a escala do problema de segurança viária em SP é mensurável e financeiramente significativa.
> Source: `https://mobilidadesampa.com.br/2025/09/infosiga-3-0-dados-transito/` | Confidence: `Medium`

> **O Infosiga rastreia fatalidades desde 2015 e sinistros não-fatais desde 2019, cobrindo 645 municípios paulistas**, com novo painel municipal, mapa de calor e geração de relatórios com IA lançados na versão 3.0.
> Significado: contexto adicional sobre maturidade de dados de trânsito em SP — mostra que o estado já tem cultura de dados/analytics em segurança viária, o que facilita a narrativa de integração futura entre o novo sistema DER-SP e o ecossistema estadual de dados (Infosiga/Detran).
> Source: `https://mobilidadesampa.com.br/2025/09/infosiga-3-0-dados-transito/` | Confidence: `Medium`

### 5. Itens não confirmados publicamente (marcar como pendente/não verificado)

- **"Instinct" (fornecedor de URA citado nas notas internas):** nome comum demais para isolar em busca pública; nenhum resultado relevante encontrado sobre uma empresa de URA/telefonia chamada Instinct associada à PRODESP ou ao DER-SP. **Não fabricar** nenhuma biografia ou histórico corporativo para esse nome — segue não verificado.
- **Stefanini como parceira de infraestrutura de telefonia da PRODESP/DER-SP:** nenhum resultado público encontrado ligando a Stefanini a um contrato específico de telefonia com a PRODESP ou o DER-SP. A Stefanini é uma consultoria de TI global real (fundada 1989, presente em 104 países, sede administrativa no Brasil) — isso é fato público sobre a empresa em geral, mas **não há evidência pública do contrato específico citado nas notas do projeto.**
- **"SIGOR" como sistema legado de ocorrências do DER-SP:** o termo colide integralmente, nos resultados de busca, com o Sistema Estadual de Gerenciamento Online de Resíduos Sólidos da CETESB (sigor.cetesb.sp.gov.br) — um sistema completamente não relacionado (gestão de resíduos). Não há nenhuma página pública indexada descrevendo um "SIGOR" de ocorrências rodoviárias do DER-SP. Isso pode significar apenas que o sistema é interno/não indexado — **não é evidência de que o sistema não exista**, apenas de que não há confirmação pública.
- **Edital ou notícia pública sobre o projeto WhatsApp + Field Service do DER-SP:** nenhum resultado encontrado — esperado, dado que o projeto está em fase de discovery/scoping e provavelmente não foi publicizado.
- **DER-MG, outros DERs estaduais usando CRM/Salesforce para despacho:** nenhum resultado relevante encontrado nas buscas realizadas.

---

## Implicações para o scoping

- **Business case / narrativa:** usar o dado Infosiga (135.545 sinistros em 2024, R$12bi+ de custo público) para ancorar a urgência de modernização de segurança viária em SP, deixando claro que é um número estadual agregado, não específico da malha DER — e usar o precedente PRODESP–Detran-SP–Bloomberg (Infosiga 3.0) como prova de conceito de que a PRODESP já entrega esse tipo de iniciativa de dados/segurança viária no estado.
- **Design de ocorrências:** a taxonomia pública da ARTESP/CCM (pane elétrica/mecânica/seca, classes de acidente, severidade de vítimas, status de bloqueio) é um ponto de partida legítimo e citável para validar/enriquecer o modelo de dados de ocorrência do Field Service, mesmo que a malha ARTESP seja de concessões (não gestão direta do DER).
- **Risco de referência desatualizada:** remover ou marcar como obsoleta qualquer menção à Dersa como comparador operacional ativo — a empresa está extinta desde 2019.
- **Gaps que precisam de verificação com o cliente/PRODESP (não supridos por pesquisa pública):** quilometragem total da malha DER-SP, orçamento/teto de investimento do projeto, existência e características reais do sistema "SIGOR" citado internamente, identidade e contrato real do fornecedor de URA "Instinct" e da eventual parceria Stefanini de telefonia. Nenhuma dessas afirmações deve ser tratada como fato até confirmação em fonte primária ou documento interno do cliente.
- **Baixa confiança / não usar em documento client-facing sem confirmação:** nome do atual Presidente do DER-SP (não verificado contra fonte de identidade primária); dado de 6.900 km / 20 concessionárias da ARTESP (possivelmente datado, período 1998–2016).
