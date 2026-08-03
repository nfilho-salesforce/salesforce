# Regras da Org Alvo — DATAPREV-PAT

> Papel de reference: restrições rígidas sobre o que o agente de construção pode e não pode fazer na org alvo. Leia uma vez; nunca viole sem override explícito do usuário.

## Identidade da org
- **Nome:** `DATAPREV-PAT Greenfield`
- **Tipo:** scratch
- **Construção permitida:** sim
- **Postura:** Greenfield — nenhuma customização pré-existente assumida

## Regras rígidas

- Esta é uma construção **greenfield**. Presuma que não há customizações pré-existentes além do setup padrão do Salesforce que a conexão fornece.
- Não faça deploy em produção sem uma instrução explícita `"deploy to production"` do usuário.
- Apenas permission sets — não modifique perfis padrão (System Administrator, Standard User).
- Idempotente: antes de criar qualquer metadado, verifique se ele já existe. Atualize no lugar se a especificação mudou.
- Use os nomes de API de `03-glossary-and-naming.md`. Se um nome não estiver listado, pergunte antes de inventar.

## Customizações existentes
**Nenhuma assumida.** Se o agente encontrar customizações existentes na primeira conexão, pare e reporte-as; não modifique nem exclua.

## Perfis a não tocar
- System Administrator
- Standard User
- Qualquer outro perfil padrão

## Pacotes gerenciados (managed packages)
_(Nenhum assumido no escopo. Se a instalação de um managed package se tornar necessária no meio da construção, leve-a ao usuário antes de instalar.)_

## Regras operacionais
- **Sandbox primeiro.** Deploys em produção exigem uma instrução explícita `"deploy to production"` do usuário.
- **Construções idempotentes.** Antes de criar qualquer metadado, verifique se ele já existe. Se existir, atualize somente se a especificação mudou.
- **Deltas, não em massa.** Quando o usuário revisar um brief de fase no meio da construção, faça o diff contra a org atual e aplique apenas as mudanças.
- **Permission sets, não perfis.** Conceda acesso via permission sets. Não modifique perfis padrão.
- **Dados de teste só a pedido.** Cargas de dados de amostra/seed só ocorrem quando o usuário aprovar explicitamente.

## Como o escopo é escrito (para a sua interpretação)

O Scopezilla escreve em dois registros e tenta não misturá-los:

- **Intenção de negócio** — "Os reps precisam de um brief de preparação de reunião de uma página acessível a partir da conta" — é *seu* trabalho mapear para o construto Salesforce correto.
- **Termos reais de plataforma** — "CPQ explicitamente fora de escopo", "objeto Quote nativo, não CPQ" — o Scopezilla usa o nome genuíno da plataforma quando sabe que a decisão é de nível de plataforma. Isso é pré-decidido.

Se você encontrar uma linguagem com cara de Salesforce que não corresponde a um tipo de metadado ou recurso real (ex.: algo que *soa* como um nome de recurso com rótulos custom grudados), trate como intenção de negócio escrita com afobação — traduza para o resultado e escolha você mesmo o construto de plataforma. Não procure pelo recurso literal.
