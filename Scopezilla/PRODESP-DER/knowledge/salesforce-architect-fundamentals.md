# Salesforce Architecture Basics: Core Principles
Source: https://architect.salesforce.com/docs/architect/fundamentals/guide/architecture-basics.html
Fetched: 2026-09-17
Relevance: General architecture guardrails applicable to any multi-cloud Salesforce build; relevant here given the Field Service + Service Cloud + Agentforce components under discussion for DER-SP.

## Three Essential Areas

Transactions, the metadata/data distinction, and platform APIs.

## 1. Transactions

**Execution Context & Limits**
Salesforce enforces limits at two levels:
- **Transactional level**: governor and execution limits prevent individual code/database operations from monopolizing shared resources
- **Org-wide level**: limits based on edition and feature type, including rolling API usage calculations

Execution context spans custom code, installed packages, and Salesforce platform services collectively — not just custom code in a single org.

**Order of Execution & Data Integrity**
- Trigger context variables describe database transaction states for all database transactions, regardless of whether custom Apex triggers exist — accessible to declarative tools like Flow.
- Data commits only finalize after the final "after trigger" step completes successfully.
- Errors in "before" or "after" contexts trigger a full rollback of all data operations in the transaction — no partial commits or post-commit logic execute.
- Apex provides database methods for finer control over savepoints and rollback behavior.

**Anti-pattern**: Do not try to bypass or override the platform's built-in order of execution.

## 2. Metadata Versus Data

| Behavior | Data | Metadata |
|---|---|---|
| Copied to sandboxes | No* | Yes |
| Migrated via Metadata API | No | Yes** |
| Migrated via data load | Yes | No |
| Included in packages | No | Yes** |
| Counts against storage limits | Yes | No |

*Full/partial copy sandboxes allow data replication from production.
**Some metadata types are excluded from Metadata API/packaging use.

**Decision tool**: Check the Metadata Coverage Report to classify a given type and understand deployment/development behavior.

## 3. Platform APIs

- Multiple APIs support differing data formats/protocols, operation types and timings.
- Some target data interactions, others metadata interactions.
- Some are purpose-built for large transaction volumes, others are not.
- Every release updates version numbers across all platform APIs; APIs remain backwards compatible.
- Applications may require refactoring before upgrading API version references to use new functionality.

**Architectural implication**: Conduct regular evaluations of API references and plan dedicated maintenance cycles.
