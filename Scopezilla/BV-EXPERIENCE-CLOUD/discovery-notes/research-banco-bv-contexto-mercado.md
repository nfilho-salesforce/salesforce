<!-- Source: pesquisa web (researcher agent) · Retrieved: 2026-08-04 · Via: Claude/Scopezilla researcher -->

# Banco BV — Contexto de Mercado (pesquisa web consolidada)

> Fontes públicas; fato vs. inferência marcados. Alguns números (nº de funcionários/clientes, ativos consolidados) não foram encontrados em fonte primária confiável.

## 1. Perfil e porte
- **Origem e rebrand** — Fundado em 1988 (família Ermírio de Moraes); banco múltiplo em 1991 como Banco Votorantim S/A; rebranding para "banco BV" em 2019. `Fato` — pt.wikipedia.org/wiki/Banco_BV
- **Estrutura acionária: 50% Votorantim S.A. + 50% Banco do Brasil** (BB desde 2009). `Fato` — pt.wikipedia.org/wiki/Banco_BV | Confiança alta
- **Posicionamento** — Líder histórico em **financiamento de veículos** (usados ≈46,7% da carteira); também crédito, atacado (banco de investimento) e banco digital. `Fato` — Relatório Anual BV 2024 | Confiança média-alta
- **Nº de funcionários / clientes / ativos consolidados** — **não encontrado** em fonte primária.

## 2. Resultados (escala)
- **Lucro líquido 2024: R$ 1,7 bi** (recorde, +49,2%). `Fato` — brazileconomy.com.br (fev/2025)
- **Carteira de crédito total (fim 2024): R$ 93,8 bi**; **carteira ampliada 1T25: R$ 102,1 bi** (+13% a/a). `Fato` — universodoseguro; CNN Brasil
- Fonte IR ideal: ri.bv.com.br → Central de Resultados.

## 3. Estratégia digital / plataforma de APIs (relevante ao projeto)
- **BV Open = plataforma Banking-as-a-Service (BaaS) via API**, aberta a fintechs, marketplaces e parceiros não-financeiros. `Fato` — bv.com.br/bv-inspira/open-finance/bv-open | Confiança alta
- **Portais de desenvolvedores JÁ EXISTENTES rodando em Apigee (Google Cloud):**
  - Sandbox: developers-sandbox.bvopen.com.br
  - Produção/parceiros: developers.bvopen.com.br
  - Portal adicional: developers.bancovotorantim.com.br
  `Fato` — Confiança alta. **Implicação:** gestão de APIs já em Apigee → cenário brownfield.
- **Escala do ecossistema:** 70+ APIs / 85 parceiros na esteira de crédito (jun/2023); "+150 parceiros" (mídia posterior). `Fato/mídia` — confiança média (varia por data)
- **Acordo com Google Cloud** para open banking. **Parcerias fintech:** Klavi (BVx/Open Finance, 2022), Neon, Méliuz. `Fato/mídia`

## 4. Contexto regulatório (APIs bancárias BR)
- **Open Finance Brasil** — iniciativa do BCB, implantação faseada desde 2021, APIs regulatórias padronizadas. `Fato` — bcb.gov.br; openfinancebrasil.org.br | Confiança alta
- **LGPD** (Lei 13.709/2018) aplicável ao compartilhamento de dados via APIs. `Fato`

## 5. Sinais de Salesforce / MuleSoft
- **Nenhuma evidência pública** de uso de Salesforce/MuleSoft pelo BV. `Fato (ausência)`
- **Inferência:** camada de API management atual = Apigee. No assessment, Apigee aparece no edge (integrações de saída) e MuleSoft como camada de XAPIs segregadas → **coexistência**, não substituição. Ponto a validar com o cliente. `Inferência` | Confiança média

## Implicações para o scoping
- Não é greenfield: BV já opera portal de desenvolvedores (Apigee) e programa de parceiros BaaS maduro. Valor do projeto = **camada de experiência/onboarding (Experience Cloud)** + **orquestração/integração (MuleSoft)**, não expor APIs do zero.
- **Validar cedo:** topologia MuleSoft ↔ Apigee (o assessment já os posiciona coexistindo).
- **Regulatório:** conformidade Open Finance + LGPD nos requisitos não-funcionais e de segurança/consentimento (OneTrust já no fluxo).
- **Pendências:** nº de funcionários/clientes, ativos consolidados, stack Salesforce existente.
