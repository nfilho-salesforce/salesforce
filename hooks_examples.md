# Exemplos de Hooks Automáticos para Claude Code

## 1. Auto-formatar código após edições

**Hook:** `PostToolUse` para `Write|Edit`

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \"$f\" 2>/dev/null || true; }"
      }]
    }]
  }
}
```

**O que faz:** Formata automaticamente arquivos JS/TS com Prettier após cada edição.

---

## 2. Executar testes após mudanças de código

**Hook:** `PostToolUse` para `Write|Edit`

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // .tool_response.filePath' | grep -E '\\.(ts|js)$' && npm test || true"
      }]
    }]
  }
}
```

**O que faz:** Roda `npm test` automaticamente quando arquivos `.ts` ou `.js` são editados.

---

## 3. Backup automático antes de edições destrutivas

**Hook:** `PreToolUse` para `Write|Edit`

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path' | { read -r f; [ -f \"$f\" ] && cp \"$f\" \"$f.bak-$(date +%s)\" || true; }"
      }]
    }]
  }
}
```

**O que faz:** Cria backup `.bak-timestamp` antes de editar qualquer arquivo.

---

## 4. Notificação ao fim de comandos longos

**Hook:** `PostToolUse` para `Bash`

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Comando concluído\" with title \"Claude Code\"'"
      }]
    }]
  }
}
```

**O que faz:** Mostra notificação macOS quando um comando Bash termina.

---

## 5. Log de todos os comandos Bash executados

**Hook:** `PreToolUse` para `Bash`

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.command' >> ~/.claude/bash-log.txt"
      }]
    }]
  }
}
```

**O que faz:** Registra todos os comandos Bash em `~/.claude/bash-log.txt`.

---

## 6. Validar sintaxe Python antes de executar

**Hook:** `PreToolUse` para `Bash`

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.command' | grep 'python' && echo '{\"continue\": true}' || echo '{\"continue\": true}'"
      }]
    }]
  }
}
```

**O que faz:** Intercepta comandos Python (pode adicionar validação com `python -m py_compile`).

---

## 7. Commit automático após mudanças

**Hook:** `PostToolUse` para `Write|Edit`

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path' | { read -r f; git add \"$f\" && git commit -m \"Auto-commit: $(basename $f)\" 2>/dev/null || true; }"
      }]
    }]
  }
}
```

**O que faz:** Cria commit Git automático para cada arquivo editado pelo Claude.

---

## 8. Limpar arquivos temporários ao parar

**Hook:** `Stop`

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "rm -rf /tmp/claude-temp-* 2>/dev/null || true"
      }]
    }]
  }
}
```

**O que faz:** Remove arquivos temporários quando você para o Claude.

---

## 9. Verificar cobertura de testes após edições

**Hook:** `PostToolUse` para `Write|Edit`

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path' | grep -E '\\.test\\.(ts|js)$' && npm run test:coverage || true"
      }]
    }]
  }
}
```

**O que faz:** Roda cobertura de testes quando arquivos de teste são modificados.

---

## 10. Mensagem personalizada ao iniciar sessão

**Hook:** `SessionStart`

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "echo '{\"systemMessage\": \"🚀 Sessão iniciada por Nelson - LATAM PS\"}'"
      }]
    }]
  }
}
```

**O que faz:** Mostra mensagem personalizada ao iniciar cada sessão.

---

## 🔥 Hook Avançado: Validação de Segurança

**Hook:** `PreToolUse` para `Bash` com bloqueio condicional

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.command' | grep -E 'rm -rf /' && echo '{\"continue\": false, \"stopReason\": \"Comando perigoso bloqueado\"}' || echo '{\"continue\": true}'"
      }]
    }]
  }
}
```

**O que faz:** Bloqueia comandos destrutivos como `rm -rf /` antes da execução.

---

## 📚 Tipos de Hooks Disponíveis

1. **command** — Executa comando shell
2. **prompt** — Avalia com LLM (usa tokens)
3. **agent** — Roda agente completo (usa mais tokens)
4. **http** — Faz POST HTTP
5. **mcp_tool** — Chama ferramenta MCP

---

## 🎯 Eventos de Hook

- `SessionStart` — Início da sessão
- `PreToolUse` — Antes de executar ferramenta
- `PostToolUse` — Depois de executar com sucesso
- `PostToolUseFailure` — Depois de falha
- `Stop` — Quando Claude para
- `SessionEnd` — Fim da sessão
- `UserPromptSubmit` — Quando você envia prompt
- `PreCompact` / `PostCompact` — Antes/depois de compactar contexto

---

## ✅ Como Adicionar um Hook

1. Edite `~/.claude/settings.json`
2. Adicione o hook no evento desejado
3. Teste com `echo '{"tool_name":"Edit","tool_input":{"file_path":"test.txt"}}' | <seu_comando>`
4. Reinicie Claude ou use `/hooks` para recarregar

---

## ⚠️ Cuidados

- Hooks rodam **automaticamente** — teste bem antes de usar
- Hooks com `continue: false` **bloqueiam** a execução
- Use `|| true` para evitar que erros interrompam o Claude
- Redirecione erros com `2>/dev/null` para manter limpo

---

## 📖 Documentação Completa

Veja `/hooks` no Claude Code para gerenciar hooks visualmente, ou leia:
- https://docs.anthropic.com/claude-code/hooks
