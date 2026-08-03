# Glossary & Naming — DATAPREV-PAT

> Reference role: **authoritative naming source**. The build agent consults this file every time it's about to invent an object API name, field API name, picklist value, label, or custom permission name.

If a name appears here, **use it verbatim**. If a name doesn't appear here, **ask the user before inventing one**.

## Object naming conventions
Use the following naming patterns. Anything else, **ask the user**.

- Custom objects: `Pascal_Snake_Case__c` (e.g. `Partner_Referral__c`)
- Custom fields: `Pascal_Snake_Case__c` (e.g. `Lead_Score__c`)
- Boolean fields: prefix with `Is_` or `Has_`
- Picklist fields: singular noun (e.g. `Source_Detail__c`, not `Source_Details__c`)

## Field naming conventions
Match the conventions above. When extending a standard object (e.g., Lead, Account, Opportunity), prefix custom fields with the team or feature name (e.g. `Sales_Lead_Score__c`, not just `Score__c`).

## Picklist values
_(No picklist values captured. The build agent must ask the user for picklist values before creating any picklist field. When confirmed, append the values here so subsequent agents can read them.)_

## Custom permissions and permission sets
_(No custom permissions or permission sets named in scope yet. Default convention: one permission set per persona — e.g. `Northwind_Sales_User`, `Northwind_Sales_Manager`. Confirm with user before creating.)_

## Client-specific terms
- API Manager
- API MuleSoft
- Aguardando Propostas
- Analista MTE
- Anypoint Exchange
- Anypoint Platform
- Atendimento Inteligente
- BATCH INCREMENTAL
- BOLETO REGISTRADO
- CONTRATO SEM CLM
- CTPS Digital
- Carga Inicial
- Como Admin
- Como Administrador
- Como Adquirente
- Como Analista MTE
- Como Arquiteto
- Como Auditor
- Como Auditor MTE
- Como DPO
- Como Data Steward
- Como Equipe MTE
- Como Estabelecimento
- Como Facilitadora
- Como Gestor

---

## What's missing here

This file was generated from the Scopezilla scope. It is **not exhaustive** — it captures the names that appeared explicitly in epics, stories, and discovery. When the build agent needs a name not listed here, it must ask the user to confirm before proceeding.
