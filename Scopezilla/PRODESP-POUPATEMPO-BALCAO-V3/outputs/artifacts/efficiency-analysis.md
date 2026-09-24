# Análise de Eficiência de Entrega com IA — PRODESP · Poupatempo Balcão (V3)

## So What
**~8-18% de eficiência de entrega realizada em prontidão Mid.** Um ganho de ritmo e qualidade dentro do mesmo formato de time — não redução de headcount, não input de preço.

Onde os ganhos aparecem neste projeto:
- **Technical Engineering & QA** (~6-16%): E03 (integração com os dois sistemas legados) e E01 (ponte Apex/Platform Events WhatsApp↔Slack) concentram o esforço — e a maior taxa de IA do projeto.
- **Documentation & Knowledge Management** (~10-20%): E07 (base de conhecimento por especialidade) e E06 (relatório executivo) — o ganho mais confiável do projeto.
- **Analysis & Design** (~8-18%): E04 (regras de seleção) e E07 (contrato Slackbot↔T7) — rascunho acelera, decisão do cliente não.

**Onde a IA não ajuda**: decisão de compliance/LGPD (residência de dados, criptografia, opt-out — ainda "Unknown, com alerta"), alinhamento de stakeholders — mais o change management da mudança de frontend do atendente (Service Console → Slack), a maior barreira específica deste projeto.

**Para chegar a High readiness (~15-22%)**: publicar política de dados de IA e endereçar LGPD, confirmar disciplina de sandbox/DevOps dos dois sistemas legados, confirmar cadência de release da PRODESP.

## Headline
**Realizado: ~8-18%** (prontidão Mid) · **Blend de nível de tarefa: ~25-45%** · **Fator de realização: 0.30-0.40** — entre o perfil "config + custom dev" e o perfil "legado + regulado", pela carga real de integração com dois sistemas legados e a exposição LGPD ainda não endereçada · **Confiança: Assumed**

## Cenários de Prontidão do Cliente
| Cenário | Faixa Realizada | Notas |
|---|---|---|
| Prontidão Baixa | ~6-10% | Ganhos ficam no piso enquanto compliance e cadência de release não são esclarecidas. |
| Prontidão Média (atual: ✓) | ~8-18% | Uso pontual de IA já existe no discovery, mas sem política formal nem cadência confirmada. |
| Prontidão Alta | ~15-22% | Com política de dados de IA e cadência de release mais rápida confirmadas, o teto fica ao alcance. |

**Cenário atual**: Prontidão Média (score 3/8)

### Sinais atrás da pontuação
- **Postura de ferramentas de IA**: 1/2 — a ata de discovery registra o próprio grupo usando o Claude para desenhar a jornada, mas nenhuma política formal de ferramentas de IA para o time de build foi declarada.
- **Velocidade de entrega / viés de ritmo**: 1/2 — Unknown, nenhuma fonte de discovery descreve cadência de release, sprints ou pipeline de deploy da PRODESP.
- **Higiene de dados e ambiente**: 1/2 — Unknown, a estratégia de sandbox/DevOps não foi abordada em nenhuma fonte de discovery; mesma lacuna para a higiene de dados dos dois sistemas legados.
- **Postura legal / segurança / compliance**: 0/2 — o próprio inventário rotula conformidade como "Unknown, com alerta": dado pessoal via WhatsApp, biometria e autenticação gov.br, sem decisão de residência/criptografia tomada.

### O que é preciso para subir
- **Baixa → Média**: aprovar ferramentas de IA para o time de build, publicar política de dados de IA/LGPD, confirmar cadência de release.
- **Média → Alta**: confirmar postura de compliance/segurança, confirmar disciplina de sandbox/DevOps dos legados, padronizar cadência de entrega rápida.

## Por Categoria
### Technical Engineering & QA — realizado ~6-16% (nível de tarefa ~20-40%)
- **Épicos condutores**: E01 (L), E03 (L), E05 (XL)
- **Como aparece aqui**: E03 (MuleSoft contra dois sistemas legados) e E01 (ponte Apex/Platform Events) concentram o maior esforço — e a maior taxa de IA, com os contratos de erro legados e o limite de Platform Events (G0111/R14) fora do caso de tela-limpa que gera os ganhos maiores [4].

### Analysis & Design — realizado ~8-18% (nível de tarefa ~25-45%)
- **Épicos condutores**: E04 (M), E07 (L)
- **Como aparece aqui**: as regras de seleção de E04 e o contrato Slackbot↔Agente do T7 de E07 (G0703) ainda não foram fechadas pelo cliente — a IA acelera o rascunho, a decisão continua totalmente humana [2].

### Documentation & Knowledge Management — realizado ~10-20% (nível de tarefa ~30-50%)
- **Épicos condutores**: E07 (L), E06 (L)
- **Como aparece aqui**: estruturar a base de conhecimento por especialidade de E07 e o relatório executivo de E06 são os ganhos mais confiáveis do projeto, mas a postura de compliance ainda não endereçada limita até onde a documentação avança sem revisão adicional [7].

### Project Management & Operations — realizado ~6-14% (nível de tarefa ~20-35%)
- **Épicos condutores**: E01 (L), E05 (XL)
- **Como aparece aqui**: relato de status e coordenação no caminho crítico E05→E01→E06 ganham algum ritmo, mas o alinhamento sobre os gaps de governança e compliance ainda abertos segue no ritmo humano [7].

## Trabalho Só-Humano
- **Project Pulse Reports** — trabalho de construção de confiança que a IA resume, não facilita.
- **Stakeholder Alignment** — negociação humano-a-humano; a IA rascunha posições, as pessoas decidem.
- **Conflict Resolution** — julgamento humano.
- **Decisão de compliance/LGPD** — residência de dados, criptografia e o opt-out (L-12) exigem decisão jurídica/governança, hoje sem política registrada.
- **Change management da mudança de frontend do atendente (Service Console → Slack)** — adoção de rotina nova por duas populações de atendentes é mudança de comportamento, não tarefa de rascunho.

## Premissas e Ressalvas
- Ganhos de nível de tarefa vêm de estudos publicados 2022-2026; o fator de realização (0.30-0.40) reflete a lei de Amdahl, a sobrecarga de revisão/"taxa de IA" e o trabalho de barreira humana que não se move.
- **Faixa honesta para codificação**: evidência de RCT vai de −19% (METR 2025 [1], OSS madura) a +21% (Paradis/Google 2024 [4], enterprise complexo) a +55% (Peng/GitHub 2022 [3], laboratório greenfield). A linha de legado/enterprise realista é o ponto de partida defensável para integração e build customizado Salesforce.
- Ganhos individuais ≠ ganhos de time: DORA 2024 [5] mediu produtividade individual subindo enquanto estabilidade e throughput de entrega caíam. Faros AI [12] corrobora em escala 10x maior (22 mil devs, 2 anos): throughput local sobe, entrega no nível de sistema não, qualidade degrada.
- A capacidade dos modelos está avançando mais rápido que os ganhos de fluxo de trabalho realizados (Stanford HAI 2026 [9]); esse é o motivo de as bandas de projeto ficarem em ~8-18%, não mais.
- Bandas são qualitativas e específicas deste projeto — nenhuma implicação de horas, FTE ou custo é computada ou sugerida.

## Fontes
1. METR (julho 2025) — RCT de desenvolvedores experientes de OSS; mediu ~19% de lentidão apesar de uma sensação de ~20% de aceleração.
2. BCG × Harvard (2023, pilotos 2025) — 12,2-40% de economia de tempo em tarefas dentro do escopo; a "fronteira irregular" degrada fora do escopo.
3. Peng et al., GitHub (2022) — RCT de laboratório, 95 devs numa tarefa greenfield de servidor HTTP; ~55% mais rápido, IC 95% [21%, 89%].
4. Paradis et al., Google (arXiv 2410.12944, 2024) — RCT com 96 engenheiros do Google numa tarefa enterprise complexa; ~21% de redução de tempo com IC largo. Contrapeso a [1].
5. DORA 2024 State of DevOps — primeira medição rigorosa em nível de time mostrando ganhos individuais de IA coexistindo com queda de estabilidade e throughput de entrega.
6. DORA 2025 — posiciona a IA como "um amplificador" dos sistemas sociotécnicos existentes; qualitativo, suplementar a [5].
7. McKinsey State of AI (2025) — ganhos de 10-30% em nível de função; faixas amplamente inalteradas desde 2024.
8. GitClear AI Code Quality (atualização 2025, 211M LOC, 2020-2024) — clonagem 8,3%→12,3%, refatoração 25% (2021)→<10% (2024).
9. Stanford HAI AI Index (abril 2026) — SWE-bench Verified subiu de 60% para quase 100% do baseline humano em um ano; 88% de adoção organizacional; gap de 50 pontos entre especialistas e público sobre o impacto da IA no trabalho.
10. Salesforce Agentforce pilotos internos (2024-2025, públicos).
11. Observações internas Scopezilla (2025-2026).
12. Faros AI "Acceleration Whiplash" (abril 2026) — telemetria observacional de 22 mil devs/4 mil times/2 anos: throughput local sobe, estabilidade/qualidade degradam de forma acentuada.
13. MSR 2026 (arXiv 2601.15195) — estudo empírico de ~33 mil PRs autorados por agentes; sucesso de merge cai fortemente em correção de bugs/performance — exatamente o trabalho enterprise que domina engajamentos Salesforce.

## Como Usar Isto
- Combinar com o resumo executivo (`narratives`) para a seção de valor — as narrativas devem usar a banda de prontidão Média.
- Combinar com `slides` para um slide único de valor de IA — os três cenários num slide só mostram o upside/downside com clareza.
- Re-rodar quando o roster (`resource-plan.json`, do `estimate`) estiver pronto para subir de fidelidade category-only para category+role-type.
