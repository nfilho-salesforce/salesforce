# NotebookLM - Instruções de Upload

## Projeto: UNA-FUND1
**Fonte:** Project UNA: Implementation Strategy and MVP Scope Planning

---

## 📥 Como Fazer Upload dos Documentos

### Opção 1: Via Comando (Recomendado)
```bash
# Copiar documentos do NotebookLM para este diretório
cp /path/to/notebooklm/documents/* ~/claude/dtp-una-fund1/discovery/notebooklm/

# Ou se os documentos estiverem em outro projeto
cp ~/Downloads/notebooklm-una/* ~/claude/dtp-una-fund1/discovery/notebooklm/
```

### Opção 2: Informar Localização
Se você já possui os documentos em outro local, informe o caminho completo:
```
/caminho/completo/para/documentos/notebooklm-una/
```

---

## 📄 Tipos de Documento Esperados

Do NotebookLM "Project UNA: Implementation Strategy and MVP Scope Planning":

### Documentos Principais
- [ ] PDFs de estratégia de implementação
- [ ] Documentos de escopo MVP
- [ ] Notas de áudio/transcrições
- [ ] Diagramas de arquitetura
- [ ] Especificações técnicas
- [ ] Business requirements

### Documentos Relacionados (se disponíveis)
- [ ] RFP/Edital Dataprev
- [ ] Atas de reunião
- [ ] Discovery notes anteriores
- [ ] Comparativo UNA-FUND1 vs FUND2
- [ ] Benchmark de projetos similares

---

## 🔍 Após Upload - Análise Automática

Assim que os documentos forem carregados, realizarei:

1. **Leitura e consolidação** de todos os documentos
2. **Extração de requisitos** técnicos e de negócio
3. **Análise de estratégia** de implementação
4. **Definição de escopo MVP** otimizado
5. **Geração de ROM** comparado com UNA-FUND2
6. **Identificação de riscos** e dependências críticas

---

## 📊 Output Esperado

Após análise, gerarei:

### discovery/
- `00-notebooklm-consolidated.md` - Consolidação de todos os docs
- `01-implementation-strategy.md` - Estratégia de implementação
- `02-mvp-scope-definition.md` - Escopo MVP detalhado
- `03-requirements-matrix.md` - Matriz de requisitos

### outputs/
- `ROM-UNA-FUND1-v1.0.md` - ROM inicial
- `comparison-FUND1-vs-FUND2.md` - Análise comparativa
- `risk-assessment.md` - Avaliação de riscos
- `resource-allocation.md` - Plano de alocação

### architecture/
- Diagramas de arquitetura técnica
- Fluxos de integração
- Matriz de dependências

---

## ⚡ Pronto para Começar?

**Opção A:** Cole os documentos nesta pasta e digite:
```
analisar documentos notebooklm
```

**Opção B:** Informe a localização dos documentos:
```
documentos estão em /caminho/completo/
```

**Opção C:** Se precisar de acesso ao NotebookLM original:
```
preciso acessar o notebooklm diretamente
```
