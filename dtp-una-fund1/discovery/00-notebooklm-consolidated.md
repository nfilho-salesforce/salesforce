# Project UNA: Implementation Strategy and MVP Scope Planning
## NotebookLM Project Consolidated Extract

**Project Title:** Project UNA: Implementation Strategy and MVP Scope Planning

**Creation Date:** December 22, 2025

**Total Sources:** 33 documents

**Status:** Shared project

---

## Executive Summary

This NotebookLM project documents the **modernization of Brazilian government digital services**, focusing on the implementation of the **Salesforce platform by Dataprev**. The project aims to unify the citizen experience through a standardized **Design System**, using tools like **MuleSoft** for data integration and **AI (Agentforce)** for service automation.

The sources describe **technical requirements**, user profiles, and operational flows needed to efficiently manage complaints and requests. Additionally, the manuals specify **WebService integration** protocols and contractual responsibilities involved in executing this technological foundation. The central goal is to create a **replicable model** that ensures accessibility, visual consistency, and agility in support offered by various public agencies.

---

## Complete List of Source Documents (33 Total)

### Documents Successfully Imported (31 documents):

1. **Apresentação - Escopo ligue 180 (2).pdf** - PDF document
2. **Apresentação do Sistema Cube (1).docx** - Word document
3. **Arquitetura de Alto Nivel - Gemini.png** - Image
4. **Copy of Estimativa UNA - Sheet1** - Google Spreadsheet
5. **Copy of Ordem de Magnitude - Salesforce - Dataprev - UNA - v1** - Google Slides
6. **Copy of TA - UNA - Dataprev v1** - Google Slides
7. **Copy of UNA Basic - Sheet1** - Google Spreadsheet
8. **Copy of [Dataprev] UNA - 2025/12/17 10:29 GMT-03:00 - Notes by Gemini** - Google Doc
9. **DPN_-_Ligue_180_v3.docx** - Word document
10. **Design System — Governo Digital** - Web link
11. **Documento de Orientação Estratégica do Projeto-1 (1) (1).pdf** - PDF document
12. **Escopo Ligue 180.pdf** - PDF document
13. **ITENS TR SOBRE O SISTEMA (1) (1).docx** - Word document
14. **ITENS TR SOBRE O SISTEMA (1).docx** - Word document
15. **Integração WebService** - Web link
16. **Lista de Requisitos da Solução Tecnológica 1 (1).pdf** - PDF document
17. **Lista de Requisitos da Solução Tecnológica 1.pdf** - PDF document
18. **Mapa mental - ligue180.png** - Image
19. **Projeto Dataprev UNA_ apresentacao SOW DATAPREV - UNA (se puderem mandar representante) - 2026_01_23 09_00 GMT-03_00 - Anotações do Gemini.pdf** - PDF document
20. **REQUISITOS POC- TR71_23 (1).pdf** - PDF document
21. **ROM - DATAPREV - 180 Mulheres - v1** - Google Slides
22. **ROM - DATAPREV - UNA 2.0 - v3** - Google Slides
23. **SFDC and EMPRESA DE TECNOLOGIA E INFORMACOES DA PREVIDENCIA S.A. - DATAPREV - SOW#05481543 - fully executed (February 8, 2026) (697360929a) (version 1) (2).pdf** (appears twice) - PDF document
24. **Strategic Analysis MuleSoft: Epics and Processes** - Google Doc
25. **Strategic Analysis of Experience Cloud** - Google Doc
26. **Strategic Catalog of Epics and Use Cases: Salesforce Service Cloud** - Google Doc
27. **USD - UNIFIED SCOPING DOCUMENT - V2.0 - PT** - Google Doc
28. **Untitled document (3) (1).pdf** - PDF document
29. **anotacoes.pdf** - PDF document
30. **plataforma-automacao.pdf** - PDF document
31. **transcricao - reuniao chico Solução Ligue 180 (1).pdf** - PDF document
32. **transcricao - reuniao chico Solução Ligue 180.pdf** - PDF document

### Documents with Import Errors (2 documents):

33. **CSG ProServ Standard Language Library (for SOWs) (3).docx** - Import error
34. **Implementation Services Master SOW (Global-Spanish LATAM).docx** - Import error
35. **Implementation Services Master SOW- (Global - Portuguese).docx** - Import error

---

## Key Topics and Themes

### 1. **Core Platform Architecture**
- **Zero Persistence Strategy**: Salesforce acts as front-end (N1) while UNA legacy system manages N2/N3 and case storage
- **Service Cloud & Portal**: Experience Cloud portal with Service Console for omnichannel support
- **Integration Layer**: MuleSoft for bidirectional data flow between Salesforce and UNA legacy system
- **AI & Automation**: Agentforce/Einstein Bot for citizen self-service and agent assistance

### 2. **Ligue 180 Service (Women's Support Hotline)**
- Multi-channel support: Voice (CTI integration with Comunix), WhatsApp, Web Chat
- Specialized pause types: ISAP (Psychosocial Support), IMC (Training and Capacity Building)
- TMA (Service Time) tracking for USA (Service Unit) billing
- Satisfaction survey integration
- Unified agent console eliminating platform switching

### 3. **Gov.br Design System**
- Standardized template for "factory of sites"
- Consistent visual identity across government portals
- Accessibility compliance
- Replicable across different government agencies

### 4. **Data Model & Case Management**
- Person Accounts for citizen records
- Multiple Record Types: Denúncia (Complaint), Informações (Information), Orientação (Guidance), Manifestação (Manifestation)
- Dynamic Forms based on service catalog
- Security and anonymization rules for complaint data
- Sharing rules for portal visibility

### 5. **Digital Channels Configuration**
- WhatsApp WABA (WhatsApp Business API)
- MIAW (Messaging for In-App and Web)
- Snippet generation for external site embedding
- Omni-Channel routing
- Einstein Bot for triage and qualification

---

## Implementation Strategy Details

### MVP Foundational Scope (Phase 1)

**Total Effort: 2,596 hours**

#### Delivery Workstreams:

**1. Project Management & Engagement (Cross-functional)**
- Total: 306 hours
- Roles: Project Managers, Engagement Managers
- Focus: Planning, governance rituals, execution, communication with Dataprev

**2. Technical & Solution Architecture (Service Cloud and Portal)**
- Total: 580 hours
- Roles: Technical Architects, Solution Architects
- Focus: Architecture design ensuring portal (Experience Cloud) and case management (Service Cloud) are secure and scalable

**3. Development & Quality Assurance (Service Cloud and Portal)**
- Total: 1,060 hours
- Roles: Technical Consultants, Salesforce Developers, QA Consultants
- Focus: Actual platform configuration, visual and logical component development, testing cycles

**4. Integrations & Interoperability (MuleSoft)**
- Total: 400 hours
- Roles: MuleSoft Architects, MuleSoft Developers
- Focus: API construction on Anypoint platform, data flow orchestration connecting Salesforce to UNA legacy system

**5. Artificial Intelligence (AgentForce)**
- Total: 250 hours
- Roles: AI Architects, Functional Consultants, Developers, QA (AgentForce focus)
- Focus: Creation and configuration of autonomous agents for data unification and self-service/real-time agent support

#### Role Distribution (Case Management UNA - 1,100 hours subset):

- **Senior Technical Architect**: 220 hours
- **Senior Solution Architect**: 160 hours
- **Project Manager**: 90 hours
- **Technical Consultant**: 260 hours
- **Quality Assurance Consultant**: 120 hours
- **MuleSoft - Technical Consultant**: 180 hours
- **MuleSoft - Technical Architect**: 60 hours

---

### Additional Scope (2nd OS) - Case Management in Salesforce

**Additional Effort: 1,016 hours**

**Combined Total: 3,612 hours**

This additional scope brings case management INTO Salesforce rather than just acting as a shell.

#### Consolidated Delivery Breakdown:

**1. Project Management & Engagement**
- Total: 390 hours (306h Base + 84h Additional)
- Roles: Project Managers, Engagement Managers
- Focus: Extended planning and governance for cloud data complexity

**2. Technical & Solution Architecture**
- Total: 934 hours (580h Base + 354h Additional)
- Roles: Senior Technical Architects, Senior Solution Architects
- Focus: Data model design (Person Accounts, new Case Record Types), dynamic service catalog, security/anonymization rules for complaint storage in Salesforce

**3. Development & Quality**
- Total: 1,414 hours (1,060h Base + 354h Additional)
- Roles: Technical Consultants (Devs), QA
- Focus: Complex flow configuration (Salesforce Flows), Dynamic Forms based on catalog, complete testing cycle (SIT/UAT) for new case management engine

**4. Integrations & Interoperability (MuleSoft)**
- Total: 624 hours (400h Base + 224h Additional)
- Roles: MuleSoft Technical Architects, MuleSoft Developers
- Focus: New APIs and bidirectional Upsert processes ensuring cases created in Salesforce cloud are perfectly replicated and synchronized with UNA on-premise legacy database

**5. Artificial Intelligence (AgentForce)**
- Total: 250 hours (250h Base + 0h Additional)
- Roles: AI Architects, Developers
- Focus: Autonomous agent configuration remains faithful to foundational scope, no impact from 2nd OS which is strictly focused on structured case management and storage

#### Setup Distribution for 2nd OS (1,016 hours):

**Service Cloud Setup: ~708 hours (70% of additional budget)**
- Complex data modeling enabling Person Accounts
- New Case Record Types (Denúncia, Informações, Orientação, Manifestação)
- Lightning Pages and Dynamic Forms reflecting Service Catalog obligation rules
- Business logic (up to 5 flows/workflows)
- Sharing adjustments to securely expose cases in citizen portal (Experience Cloud)

**MuleSoft On-Premise Setup: ~224 hours (22% of additional budget)**
- Design and construction of bidirectional APIs
- Listening to Salesforce for case creation/classification
- On-premise orchestration to replicate to UNA legacy database
- Data custody maintenance for Dataprev

**Project Governance: ~84 hours (8% of additional budget)**
- Project Manager role
- Timeline alignment between Service Cloud and MuleSoft teams
- Risk management for cloud data storage

---

## CAU Client Extension Project

**Client:** CAU (new client extending UNA foundational platform)

### Scope Overview:

**Duration:** 6 weeks

**Total Effort:** 600 hours

### Technical Scope:

**1. Experience Cloud & Channels**
- Clone Gov.br foundational template for CAU portal
- Apply CAU-specific UX identity
- Activate WhatsApp and Web Chat (MIAW) channels

**2. Einstein Bot & Knowledge Base**
- Rule-based bot (not Agentforce generative AI)
- Decision tree for triage and data collection
- Knowledge Base (KB) integration for FAQ self-service
- Simple response automation to reduce human handoff
- Transfer to Agent functionality with context

**3. Omni-Channel**
- Simplified routing to single queue
- No advanced skills-based routing
- Support for WhatsApp and Web Chat overflow

**4. Service Cloud (N1 Support)**
- Reuse of UNA backend logic (Apex/Flows)
- LWC components adapted for bot data collection
- Service Console for unified agent experience
- Case creation in UNA legacy system (Zero Persistence maintained)

**5. Backend Logic Reuse**
- Cannot reuse LWC visual components in bot (conversational interface limitations)
- CAN reuse Apex classes and integration structure
- Bot collects data via dialog, passes to Invocable Actions (Flow/Apex)
- Same integration engine as LWC to register in UNA

### Team Allocation (6 weeks):

- **Project Manager (PM)**: 20h/week = 120 hours
- **Solution Architect (SA)**: 20h/week = 120 hours
- **Technical Architect (TA)**: 10h/week = 60 hours
- **Developer**: 40h/week = 240 hours
- **UX Designer**: 10h/week = 60 hours

**Total: 600 hours** (QA/Testing absorbed within Development/TA allocation)

### Critical Assumptions (CAU Project):

1. Traditional Einstein Bot with KB for FAQ (no Generative AI/Agentforce in this phase)
2. Simple queue routing (no advanced skills-based routing in Omni-Channel)
3. WABA and Meta Business Manager must be approved on "Day 1"
4. Initial KB article content must be provided by client
5. No new MuleSoft API development - reuse existing UNA integrations
6. Client technical team responsible for embedding snippet in external sites/applications

---

## Technical Integration Details

### CTI Integration (Comunix + Salesforce)

**The Cross-Feature:** Time, state, and pause management

**Key Value Proposition:**
- Eliminates platform switching (alt-tab) between Comunix and Salesforce
- Unified console for all channels (voice, chat, WhatsApp)
- Precise TMA (Service Time) tracking for USA billing
- Humanized pause controls (ISAP, IMC) within Omni-Channel
- Satisfaction survey directly linked to Case and agent
- Cognitive efficiency: System blocks new chats when agent on critical voice call

**Current Pain:**
- Agents switch between Comunix (telephony/pauses) and case registration system
- Scattered attention, difficult to measure exact worked time

**Solution:**
- Voice infrastructure remains in Comunix
- Agent experience 100% in Salesforce Service Console
- Omni-Channel synchronizes statuses bidirectionally with IVR
- Unified journey for all channels

### Snippet & External Integration

**Primary Focus:** Experience Cloud native implementation

**Extension Capability:**
- Digital Engagement package includes snippet generation for external deployment
- Chat can be embedded in any government web portal
- Proven use case: Moodle platform integration
  - APIs integrating Agents and Moodle
  - "Concierge MDS" Agent creation
  - Secure identity passing via token transferred by WhatsApp snippet in Moodle

**Responsibility Boundaries:**
- Salesforce PS provides snippet/integration code
- Supports agent connection to any external system
- Client technical team responsible for installing/configuring code in external sites/apps
- Salesforce PS has access only to Salesforce Application, not client non-SFDC systems per SOW terms

---

## Knowledge Base & Bot Strategy

### Einstein Bot Configuration:
- **Type:** Rule-based (menu navigation, buttons, basic text intent recognition)
- **NOT Agentforce:** No autonomous generative AI in base scope
- **KB Integration:** Bot consults Knowledge Base to answer simple questions and FAQs
- **Deflection:** Retain simple inquiries without human handoff
- **Triage:** Decision tree to identify citizen, classify demand type (subject/reason), collect basic data
- **Transfer to Agent:** Pass session with captured context to human support

### Knowledge Base Requirements:
- Client must provide initial article content
- Simple FAQ structure
- Integrated with bot conversation flow
- No RAG (Retrieval Augmented Generation) in base configuration

---

## Financial & Pricing Structure

### Deliverable-Based Cost Allocation:

**Foundational Project (2,596 hours):**
1. Project Management & Engagement: 306 hours
2. Architecture: 580 hours
3. Development & QA: 1,060 hours (largest budget allocation)
4. MuleSoft Integration: 400 hours
5. AI/Agentforce: 250 hours

**With 2nd OS (3,612 hours total):**
1. Project Management & Engagement: 390 hours
2. Architecture: 934 hours (significant senior architect addition)
3. Development & QA: 1,414 hours
4. MuleSoft Integration: 624 hours (senior architect addition)
5. AI/Agentforce: 250 hours (unchanged)

### Pricing Strategy Recommendations:
- Use 5 delivery blocks as billing milestones
- Apply role-based hourly rates within each block
- Blocks 2 (Architecture) and 4 (MuleSoft) justify higher blended rate due to senior profile concentration
- Financial distribution aligned to capacity and complexity

---

## Project Governance & Methodology

### Salesforce PS Delivery Framework:
- Standard language library (SLL) for SOWs
- Multiple payment models
- Implementation by product (Retail, MC, Tableau, Agentforce, CRM Analytics, Core, SFI)
- Expert Services available
- Standard PS methodology

### Contract Terms (SOW):
- Salesforce PS access limited to Salesforce Application only
- No access to client non-SFDC systems (internal enterprise platform, third-party applications)
- Client responsible for external system configuration and integration
- Security and compliance standards per Brazilian government requirements

---

## Generated Study Materials & Artifacts

NotebookLM project includes multiple generated artifacts:

1. **Audio Summary** (Resumo em Áudio)
2. **Slide Presentation** (Apresentação de slides)
3. **Video Summary** (Resumo em Vídeo)
4. **Mind Map** (Mapa mental)
5. **Reports** (Relatórios)
6. **Flashcards** (Cartões didáticos)
7. **Quiz** (Teste)
8. **Infographic** (Infográfico)
9. **Data Table** (Tabela de dados)

### Related Projects/Infographics in Studio:

1. **Tecnologia no Atendimento Ligue 180** (31 sources, 128 days ago)
2. **Jornada de Atendimento Ligue 180** (31 sources, 137 days ago)
3. **Jornada Digital Ligue 180** (31 sources, 137 days ago)
4. **Arquitetura Técnica de Ecossistema Integrado** (30 sources, 137 days ago)
5. **Evolução das Jornadas de Atendimento** (30 sources, 137 days ago)
6. **Arquitetura Salesforce para o Governo Digital** (30 sources, 140 days ago)
7. **Arquitetura Estrutural Ecossistema Ligue 180** (30 sources, 140 days ago)
8. **Governo Digital: Padrão e Eficiência** (30 sources, 140 days ago)
9. **Especificações de Requisitos e Serviços de Tecnologia** (30 sources, 140 days ago)
10. **Modernização Tecnológica do Ligue 180: Arquitetura e Integração UNA** (30 sources, 140 days ago)
11. **UNA Governo Digital Rota da Transformação** (5 sources, 200 days ago)

---

## Key Questions & Conversation History

### Conversation Timeline (from NotebookLM chat):

**Tuesday, March 3:**
- Discussion on CTI integration cross-feature value proposition
- Unified console eliminating alt-tab between platforms

**Friday, May 22:**
- CAU client extension project scoping
- Bot component reuse analysis (visual vs. logical layers)
- Simplified routing for single queue architecture
- Einstein Bot vs. Agentforce clarification

**Tuesday, June 23:**
- Agent connection scope: Experience Cloud vs. external sites/applications
- Snippet deployment responsibilities
- Moodle integration use case reference
- SOW responsibility boundaries

**Today (most recent):**
- Financial allocation by deliverable and role
- 2nd OS integration (1,016 hours)
- Service Cloud vs. MuleSoft setup distribution
- Pricing structure by role and capacity

---

## Critical Success Factors

### Technical:
1. **Zero Persistence Architecture** - Maintain data custody in UNA legacy system
2. **Bidirectional Sync** - MuleSoft APIs ensuring perfect replication between Salesforce and UNA
3. **CTI Unified Experience** - Single console eliminating platform switching
4. **Gov.br Design System Compliance** - Consistent accessibility and visual identity
5. **Bot-to-Human Handoff** - Seamless context transfer with triage data

### Operational:
1. **TMA Tracking Precision** - Accurate USA billing units
2. **Humanized Pause Management** - ISAP and IMC within Omni-Channel
3. **Multi-channel Support** - Voice, WhatsApp, Web Chat unified
4. **Knowledge Base Deflection** - Self-service FAQ reducing human load
5. **Security & Anonymization** - Complaint data protection in cloud

### Strategic:
1. **Replicable Model** - Factory of sites approach for multiple agencies
2. **Scalable Foundation** - Support for future service expansion
3. **Citizen-Centric Experience** - Unified, accessible digital services
4. **Government Standardization** - Consistent experience across agencies
5. **AI-Augmented Service** - Foundation for autonomous agent evolution

---

## Next Steps & Open Items

### Pending Clarifications:
- Final confirmation on Knowledge Base content provision responsibility
- WABA/Meta Business Manager approval timeline
- External site integration deployment schedule
- Testing environment readiness (SIT/UAT)

### Documentation Needs:
- Detailed API specifications for MuleSoft integration
- Service catalog structure and dynamic form rules
- Security and anonymization implementation details
- Training materials for agent console

### Governance:
- Weekly alignment meetings between Service Cloud and MuleSoft teams
- Risk management protocols for cloud data storage
- Change management procedures
- Handoff and go-live planning

---

## Document Status

**Consolidated by:** Claude Code AI Assistant

**Source:** NotebookLM Project Snapshot

**Consolidation Date:** July 10, 2026

**Total Source Documents:** 33 (31 successfully imported, 2 with errors)

**Project Creation Date:** December 22, 2025

**Last Activity:** Ongoing conversations through July 2026

---

## Notes

This consolidated document represents the complete extracted content from the NotebookLM project interface snapshot. The project demonstrates a comprehensive government digital transformation initiative using Salesforce platform, with particular focus on the Ligue 180 women's support service as a flagship implementation.

The "Zero Persistence" architectural approach is unique and strategic, allowing Salesforce to provide modern user experience and omnichannel capabilities while maintaining data custody in the existing UNA legacy system, reducing risk and compliance concerns.

The project shows clear evolution from a simple front-end implementation (Phase 1) to a more complete case management solution (2nd OS), with careful consideration of role allocation, effort estimation, and financial structuring to support proposal development and client pricing decisions.
