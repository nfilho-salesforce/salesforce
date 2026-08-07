# Como Configurar NotebookLM MCP no Claude Code

## ✅ Status Atual

- ✅ `notebooklm-mcp 2.0.11` instalado via pipx
- ❌ Não configurado no Claude Code
- 📄 Documento pronto: `DTP-UNA-FUND2/DATAPREV_UNA_FUND2_NotebookLM.md`

---

## 🚀 Configuração Rápida

### Método 1: Comando Claude MCP (RECOMENDADO)

```bash
# Adicionar NotebookLM MCP
claude mcp add notebooklm

# Se pedir autenticação Google:
# 1. Siga o link que aparecer
# 2. Faça login com sua conta Google
# 3. Autorize o acesso ao NotebookLM
```

### Método 2: Configuração Manual

Se o comando acima não funcionar, adicione manualmente:

**1. Encontre o caminho do servidor:**
```bash
which notebooklm-server
# Deve retornar algo como: /Users/nfilho/.local/bin/notebooklm-server
```

**2. Configure no Claude Code:**

Você precisa adicionar o servidor MCP. O local do arquivo de configuração depende:

- **Claude Desktop:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Claude Code (CLI):** Pode precisar criar/editar `~/.claude/mcp_servers.json`

**Conteúdo da configuração:**
```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "/Users/nfilho/.local/bin/notebooklm-server",
      "args": [],
      "env": {}
    }
  }
}
```

**3. Reinicie o Claude Code:**
```bash
# Se estiver usando Claude Desktop, reinicie o app
# Se estiver no CLI, a próxima sessão já carrega
```

---

## 🔐 Autenticação Google

Quando executar pela primeira vez, o NotebookLM MCP vai pedir autorização:

1. **Abrirá um browser** com a página de login do Google
2. **Faça login** com a conta que tem acesso ao NotebookLM
3. **Autorize** o acesso (apenas leitura para projetos/notebooks)
4. **Tokens salvos** em `~/.notebooklm/credentials`

---

## 📋 Teste da Configuração

Depois de configurar, teste:

```bash
# Teste 1: Verificar se o servidor inicia
notebooklm-server

# Teste 2: No Claude Code, perguntar:
# "Liste meus projetos do NotebookLM"
# Se retornar uma lista, está funcionando!
```

---

## 🎯 Uso Após Configuração

### Comandos Disponíveis

1. **Listar projetos:**
   - "Liste meus projetos do NotebookLM"
   - "Quais notebooks tenho no NotebookLM?"

2. **Upload de documentos:**
   - "Faça upload do arquivo X para o projeto NotebookLM Y"
   - "Adicione este markdown ao notebook Z"

3. **Consultar conteúdo:**
   - "O que tem no projeto 'Project UNA' do NotebookLM?"
   - "Liste as fontes do notebook X"

---

## 📄 Documento Pronto Para Upload

**Arquivo criado:**
`/Users/nfilho/claude/Scopezilla/DTP-UNA-FUND2/DATAPREV_UNA_FUND2_NotebookLM.md`

**Conteúdo:**
- ✅ Sumário Executivo (contexto incremental)
- ✅ Objetivo e Escopo (4 validações técnicas)
- ✅ Arquitetura (4 camadas)
- ✅ Timeline (8 semanas, 4 fases)
- ✅ Equipe (6 perfis, 488h)
- ✅ Investimento (Traditional vs Quantum Leap)
- ✅ Riscos (8 identificados)
- ✅ Perguntas (15 totais, 4 bloqueadoras)
- ✅ Premissas
- ✅ Próximos Passos
- ✅ Comparativo ROM v1.0 vs v2.0 (-73%)

**Após configurar o MCP, você poderá:**
```
Faça upload do arquivo /Users/nfilho/claude/Scopezilla/DTP-UNA-FUND2/DATAPREV_UNA_FUND2_NotebookLM.md 
para o projeto NotebookLM "Project UNA: Implementation Strategy and MVP Scope Planning"
```

---

## 🆘 Troubleshooting

### Erro: "notebooklm-server: command not found"

```bash
# Reinstalar
pipx uninstall notebooklm-mcp
pipx install notebooklm-mcp

# Verificar PATH
echo $PATH | grep -o '/Users/nfilho/.local/bin'
```

### Erro: "Authentication failed"

```bash
# Limpar credenciais e refazer
rm -rf ~/.notebooklm/credentials
notebooklm-server
# Refazer autenticação no browser
```

### Erro: "MCP server not responding"

```bash
# Verificar se o servidor está rodando
ps aux | grep notebooklm

# Matar processos antigos
pkill -f notebooklm-server

# Reiniciar Claude Code
```

---

## 📚 Alternativa: Upload Manual

Se a configuração do MCP não funcionar, você pode fazer upload manual:

1. **Abrir NotebookLM:** https://notebooklm.google.com
2. **Selecionar projeto:** "Project UNA: Implementation Strategy and MVP Scope Planning"
3. **Add Source → Upload:**
   - Escolha o arquivo: `DATAPREV_UNA_FUND2_NotebookLM.md`
   - Ou copie/cole o conteúdo do arquivo

**O documento já está otimizado para NotebookLM** (markdown estruturado, headers, tabelas).

---

## ✅ Próximos Passos

1. **Configure o MCP** (Método 1 ou 2)
2. **Teste** com "Liste meus projetos do NotebookLM"
3. **Faça upload** do documento preparado
4. **Verifique** se apareceu no projeto "Project UNA"

**Documento pronto para upload:**
`/Users/nfilho/claude/Scopezilla/DTP-UNA-FUND2/DATAPREV_UNA_FUND2_NotebookLM.md`
