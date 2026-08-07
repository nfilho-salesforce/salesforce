# DATAPREV — DECIPEX: Perguntas de Discovery
**Data:** 2026-06-18 | **Responsável:** Nelson Stebulaitis Filho

---

## 1. CONTEXTO E MOTIVAÇÃO

1. Qual é o problema ou oportunidade específica que motivou o contato com a Salesforce PS? O que está acontecendo hoje que não está funcionando bem?
2. Este projeto partiu de uma demanda da DECIPEX (MGI) para a DATAPREV, ou é uma iniciativa interna da DATAPREV para melhorar seus serviços ao cliente DECIPEX?
3. Existe um projeto ou iniciativa formal de modernização em andamento na DECIPEX/MGI? Há uma portaria, resolução ou contrato guarda-chuva que orienta esse trabalho?
4. O que motivou a escolha da Salesforce como plataforma? Existe já alguma licença ou contrato Salesforce vigente na DATAPREV ou na DECIPEX?
5. Existe pressão de prazo? Há algum marco político, orçamentário ou regulatório que define uma data de entrega?

---

## 2. ESCOPO E PROCESSOS

6. Quais processos específicos serão alvo desta iniciativa? (Ex: concessão de aposentadoria, prova de vida, atendimento a beneficiários, gestão de pensões, anistiados políticos?)
7. Como é o processo de **atendimento ao beneficiário** hoje? Quais canais existem (telefone, presencial, portal web, e-mail)? Qual o volume mensal de solicitações?
8. Como funciona o processo de **prova de vida** hoje? Qual o percentual de beneficiários que não conseguem fazer presencialmente e precisam de visita domiciliar? Qual o custo operacional desse processo?
9. Como é feita hoje a **concessão de aposentadoria**? Qual o tempo médio de análise? Quais são os principais gargalos?
10. Existe um sistema de **CRM ou gestão de relacionamento** com o beneficiário hoje? Qual? O que ele faz bem e o que falta?

---

## 3. DADOS E INTEGRAÇÕES

11. Como é a integração atual entre DATAPREV e DECIPEX? Quais sistemas estão envolvidos (SIAPE, SIGEPE, outros)?
12. Os dados dos 165.500 beneficiários e 20.217 servidores de ex-Territórios estão centralizados? Onde residem? Qual o nível de qualidade e completude?
13. Quais sistemas legados precisarão ser integrados à nova plataforma? Existe documentação de APIs ou será necessário construir integrações do zero?
14. Há dados de órgãos extintos ainda em formatos analógicos ou sistemas descontinuados que precisariam ser migrados?
15. A DATAPREV utiliza MuleSoft ou outro middleware de integração? Se sim, está em uso para a DECIPEX?

---

## 4. USUÁRIOS E ADOÇÃO

16. Quem são os usuários internos do sistema? Quantos servidores da DECIPEX/MGI operam os processos hoje? Qual o nível de familiaridade com tecnologia?
17. Os beneficiários (aposentados, pensionistas) acessam sistemas digitais diretamente? Qual o perfil etário e de acesso digital dessa população?
18. Existe um portal de autoatendimento para o beneficiário hoje? (Ex: gov.br integrado?) O que ele permite fazer? O que falta?
19. Como é tratado hoje o atendimento para beneficiários **impossibilitados** (idosos, acamados, etc.)? Agentes de campo? Call center?
20. Qual a expectativa de adoção de canais digitais pelos beneficiários nos próximos 2-3 anos?

---

## 5. ESTRUTURA DO PROJETO E GOVERNANÇA

21. Quem é o patrocinador executivo deste projeto na DATAPREV? E na DECIPEX/MGI?
22. Existe um comitê de governança ou steering committee definido? Quem toma decisões de escopo?
23. A DATAPREV tem equipe interna de TI dedicada para este projeto? Qual o tamanho e perfil técnico?
24. Haverá um parceiro de implementação além da Salesforce PS, ou a Salesforce PS assumiria o projeto integralmente?
25. Como é o processo de aprovação orçamentária no governo federal para este tipo de contrato? Qual modalidade de licitação está prevista (dispensa, pregão, inexigibilidade)?

---

## 6. SUCESSO E MÉTRICAS

26. Como será medido o sucesso deste projeto? Quais KPIs serão acompanhados?
27. Qual a expectativa de redução de custo operacional com a digitalização? (Ex: redução de visitas domiciliares de prova de vida, redução de atendimentos presenciais)
28. Existe uma meta de **tempo de resposta** para solicitações de beneficiários? Qual é o SLA atual vs. o desejado?
29. Há expectativa de **autoatendimento** — percentual de beneficiários resolvendo suas demandas sem intervenção humana?
30. Quais são os riscos que o cliente considera mais críticos para o sucesso do projeto?

---

## 7. LACUNAS E PONTOS DE ATENÇÃO (para investigar no discovery)

- ⚠️ Não está claro se o contrato é DATAPREV → DECIPEX ou DATAPREV como parceiro técnico do MGI
- ⚠️ Nível de maturidade digital dos beneficiários (população predominantemente idosa)
- ⚠️ Restrições legais de LGPD e segurança para dados de servidores inativos do governo federal
- ⚠️ Modelo de contratação pública — pode exigir licitação, afetando prazo
- ⚠️ Compatibilidade com ecossistema gov.br (portal único do governo federal)
