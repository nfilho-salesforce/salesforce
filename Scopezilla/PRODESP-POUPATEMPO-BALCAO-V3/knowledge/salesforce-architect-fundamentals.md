# Salesforce Architecture Basics
Source: https://architect.salesforce.com/docs/architect/fundamentals/guide/architecture-basics.html
Fetched: 2026-09-21
Relevance: General architecture fundamentals for any multi-cloud Salesforce project (this deal spans Slack, Agentforce, MuleSoft, Data 360).

## Overview
The Salesforce Customer 360 Platform runs on a "multitenant, metadata-driven architecture" applied to every org. Architects need to understand three core areas when designing solutions on the platform:

1. Transactions
2. Metadata vs. Data
3. Platform APIs

---

## 1. Transactions

Transactions can be triggered by code execution and/or database operations. Salesforce enforces limits at two levels:

- **Transactional level**: Governor and execution limits prevent any single code/database operation from monopolizing shared resources.
- **Org-wide level**: Limits are based on edition and feature type, including rolling API usage limits across the org.

### Execution Context
Execution context is tied to the platform runtime engine broadly, not just custom code in one org. It encompasses:
- Custom code in the tenant's org
- Code from installed packages
- Code from Salesforce platform services itself

The platform differentiates governor limits based on the type of Apex code running.

### Order of Execution
Database manipulation transactions follow a built-in "order of execution" that governs how configuration and code behave together, ensuring data integrity. Key points:

- Trigger context variables expose the state of database operations for **all** transactions—even in orgs without custom Apex triggers—and are accessible to declarative tools like Salesforce Flow.
- Data is not committed until final *after* trigger logic completes successfully.
- Errors in *before* or *after* contexts cause a full rollback of the transaction; no partial commits occur.
- Apex offers database methods for more granular savepoint/rollback control.

**Anti-pattern warning**: Architects should avoid trying to "short cut or supersede the platform's built-in order of execution behavior."

---

## 2. Metadata vs. Data

Understanding what counts as data versus metadata affects the application lifecycle (sandbox copying, migration, packaging).

### Comparison Table

| Behavior | Data | Metadata |
|---|---|---|
| Copied into sandboxes | No* | Yes |
| Migrated by Metadata API | No | Yes** |
| Migrated by data load | Yes | No |
| Included in packages | No | Yes** |
| Counts against storage limits | Yes | No |

*Full/partial copy sandboxes allow data replication.
**Some metadata types have exceptions (see Metadata Coverage Report).

### Clarifying Examples
- Individual records = data
- sObjects themselves = metadata
- **Custom Settings** = stored as data
- **Custom Metadata Types** = stored as metadata

Despite serving similar design purposes (loosely coupled, flexible configuration), these two features are treated differently by the platform's architecture. The Metadata Coverage Report is the recommended tool for determining classification.

---

## 3. Platform APIs

Key considerations for Salesforce Platform APIs:

- Multiple APIs exist, supporting different data formats, protocols, operation types, and timing needs.
- Some APIs target data, others target metadata; some are built for "large transaction volumes."
- **Versioning**: Salesforce updates version numbers for all Platform APIs with every release.
- **Backwards compatibility**: Existing implementations remain stable even as new versions ship, but adopting new functionality may require refactoring before upgrading API version references.
- Architects must account for built-in API limits (varying by edition/feature) and plan for regular API reference evaluation and maintenance cycles.
