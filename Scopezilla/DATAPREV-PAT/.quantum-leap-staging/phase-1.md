## INTENT FOR
A equipe de implementação inteira (arquitetura + dev + MuleSoft), arrancando junta sobre a org greenfield dedicada — mais a beneficiária/estabelecimento como usuários finais do portal gov.br.

## INTENT OUTCOME
Estabelecer a base compartilhada de que todas as frentes dependem: o modelo de dados Sales Cloud nativo (Account = beneficiária/CNPJ; Opportunity = demanda; Quote = resposta da facilitadora), a camada de integração API-led do MuleSoft on-premise (com mocks contract-first), a residência híbrida com CPF tokenizado resolvido em runtime, e a identidade gov.br no Experience Cloud. Ratificar o modelo de dados fundacional é o marco que libera a paralelização das Fases 2 e 3.

## INTENT MEASURED BY
Modelo de dados fundacional ratificado com o time inteiro (INT-009, INT-010, INT-014); camada MuleSoft on-premise de pé com mocks incluindo o contrato do gateway (INT-001..008); referência tokenizada resolvendo em runtime na org dedicada (INT-002, INT-009, INT-010); login gov.br OIDC operante no portal Partner Community (INT-014, INT-018).

## INTENT MUST NOT
Não persistir CPF nem dado sensível do trabalhador na org (ADR 0001 — só referências tokenizadas). Não construir capacidade de leilão/financeiro nesta fase (Fases 2/3). Não abrir a paralelização antes de o modelo de dados fundacional fechar. Não introduzir Revenue Cloud/CLM (baseline Core-only, ADR 0004).

## PRE-DECIDED
- **Objetos nativos Sales Cloud, sem custom sell-side inventado**: Account = beneficiária (CNPJ), Opportunity = demanda do leilão reverso, Quote = resposta da facilitadora via API (ADR 0004, decision_log).
- **Residência híbrida (ADR 0001)**: CPF e dados sensíveis nunca persistem na org; ficam na Dataprev e são resolvidos em runtime via MuleSoft on-premise. Só referências tokenizadas na org (INT-009, INT-010).
- **Org 100% greenfield e apartada + MuleSoft ON-PREMISE (ADR 0002/0005)**: nova, isolada de qualquer ambiente/admins Dataprev; integração na infra soberana.
- **Facilitadoras (~600–700) são integrações API MuleSoft, não seats de portal**; a beneficiária é o driver de licença do Experience Cloud (decision_log).
- **Baseline Core-only**: sem Revenue Cloud, sem CLM, sem Billing (ADR 0004).
- **Integração contract-first**: mocks primeiro, virada mock→real governada (INT-001).

## PLAN-MODE QUESTIONS
- Fronteira de residência campo-a-campo (G0801): quais campos são tokenizados vs. persistidos? A ratificação re-molda o data model — precisa fechar antes do build.
- Não existe conector gov.br OIDC nativo (G0101): confirmar a abordagem de federação OIDC no Experience Cloud (INT-014).
- Contratos de API dos sistemas externos existem? (G0501 — Novo PAT possivelmente sem API): o inventário existe/não-existe governa a estratégia de mock (INT-001, INT-004).
- Geride expõe a validação CPF↔CNPJ por API? (INT-016) — se não, definir a alternativa.

## BUILD-MODE QUESTIONS
- Nomes de API dos objetos e campos do termo de aceite (faixa salarial, matriz/filial) — a definir no workshop de modelagem.
- Formato e claims do token OIDC gov.br (mapeamento para o usuário do portal).
- Contrato exato do serviço de de-tokenização MuleSoft (payload, latência aceitável em runtime).

## DATA MODEL
Base fundacional nativa Sales Cloud e a espinha de residência. O modelo de referências tokenizadas (INT-009) garante que CPF/dado sensível nunca resida na org, com de-tokenização em runtime via MuleSoft (INT-010). Sobre a base nativa (Account/Opportunity/Quote — ADR 0004) modela-se o termo de aceite e a estrutura matriz/filial e faixa salarial que as fases seguintes consomem. A detalhe carregado vive nos intents INT-009 e INT-010; a ratificação deste modelo é o marco que libera a paralelização.

## AUTOMATION
A validação de vínculo CPF↔CNPJ via Geride (INT-016) é a automação fundacional que habilita a representação de empresa no portal. A resolução de identidade e de-tokenização em runtime é acionada pela camada de integração, não por gravação de dado sensível.

## UI
Portal Experience Cloud (Partner Community) com login gov.br OIDC (INT-014), seleção 'representar empresa' dirigida por procuração (INT-015), controle de navegação por papel (INT-017) e sessão/logout federado gov.br (INT-018). O portal é a superfície onde beneficiária e estabelecimento entram — as jornadas de negócio (leilão, credenciamento, financeiro) chegam nas fases seguintes.

## SECURITY
Espinha de segurança formalizada nos ADRs 0001/0002. Autenticação federada gov.br (INT-014), acesso de menor privilégio na org dedicada (INT-013), trilha de auditoria imutável de acesso a dado sensível (INT-011), mascaramento de CPF em logs/erros (INT-012) e autenticação + rate-limit dos chamadores externos no gateway de API (INT-003). Nenhum CPF persiste; todo acesso sensível é auditável (TCU/CGU/ANPD).

## DATA SOURCES
Camada API-led MuleSoft on-premise, contract-first com mocks (INT-001). Fontes: serviço de de-tokenização/resolução de identidade na Dataprev (INT-002), System APIs de leitura/validação de fontes federais mock-first (INT-004), ingest do termo de aceite INIS/Kinis PJ (INT-005), contrato padrão da facilitadora — hand-off de Quote, retorno 'processado', endpoint de consulta de demandas em aberto (INT-006), API de checagem de credenciamento + monitoramento transacional do adquirente (INT-007), feed agendado de conciliação de movimentação bancária gateway→CRM (INT-008), e o contrato de integração com o gateway (mockado nesta fase).

## ACCEPTANCE USER
Uma beneficiária acessa o portal, autentica-se via gov.br, escolhe representar a empresa cujo vínculo CPF↔CNPJ é validado, e navega apenas às áreas do seu papel — sem que nenhum CPF tenha sido gravado na org. O time confirma que a org greenfield está de pé, o MuleSoft on-premise responde aos mocks contract-first (incluindo o gateway), e o modelo de dados fundacional foi ratificado.

## ACCEPTANCE METADATA
Verifica-se na org: (a) nenhum objeto persiste CPF — apenas referências tokenizadas (INT-009); (b) a chamada de de-tokenização resolve em runtime via MuleSoft on-premise (INT-010); (c) a trilha de auditoria registra cada acesso a dado sensível de forma imutável (INT-011) e logs mascaram CPF (INT-012); (d) o login OIDC gov.br cria/associa o usuário do portal com o papel correto (INT-014, INT-017); (e) o modelo de acesso é de menor privilégio na org dedicada (INT-013); (f) as System APIs MuleSoft respondem contract-first com mocks versionados (INT-001..008).

## REPORTS
Sem relatórios/dashboards de negócio no escopo desta fase — é fundação (dados, identidade, integração, residência). O único artefato de dados relevante é a trilha de auditoria de acesso a dado sensível (INT-011), consumida por conformidade, não por dashboard operacional.
