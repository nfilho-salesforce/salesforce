# SEFIN-CE — Fluxo de Atendimento (para validação com o cliente)
### Slide: Autoatendimento + Transbordo Humano (E09 — novo)

---

## Texto para o corpo do slide (bullets)

**Como funciona hoje (bot):**
- Cidadão inicia conversa pelo WhatsApp e recebe o menu: **IPTU · Taxa do Lixo (TMRSU) · ISS · Preciso de ajuda**
- Bot identifica o cidadão (CPF/CNPJ + nome + data) e resolve via integração com as APIs da SEFIN-CE: consulta o imóvel e emite o boleto (DAM) na hora
- Se a solicitação for resolvida, o bot pergunta se pode ajudar em algo mais e retorna ao menu

**Novidade — Transbordo Humano (E09):**
- Quando o bot **não consegue resolver**, verifica o horário de atendimento
- **Fora do horário:** informa o horário comercial e encerra
- **Dentro do horário:** abre automaticamente um atendimento no **Service Console**, roteado por **Omni-Channel** para uma das **3 posições de atendimento**
- O agente humano assume **a mesma conversa de WhatsApp**, sem o cidadão precisar repetir informações
- Ao final — seja pelo bot ou pelo humano — o cidadão responde a uma **pesquisa de satisfação** antes do encerramento

---

## Texto para as notas do apresentador (fala sugerida)

"Hoje o bot já resolve boleto de IPTU, taxa do lixo e ISS de forma automática, direto pelo WhatsApp, usando as APIs de vocês. A novidade que estamos trazendo é o transbordo humano: quando o bot não consegue resolver — e está dentro do horário de atendimento —, ele abre automaticamente um atendimento no Service Console e direciona para uma das três posições de atendimento, via Omni-Channel. O ponto importante aqui é que o agente assume a mesma conversa, no mesmo WhatsApp, sem o cidadão ter que recomeçar do zero. Fora do horário, o bot informa o horário de atendimento e encerra normalmente. E em todo encerramento — bot ou humano — a gente aplica uma pesquisa de satisfação."

**Pontos a confirmar com o cliente neste slide:**
- Horário exato de atendimento humano (dias/início/fim)
- Confirmação de Omni-Channel Enhanced (licença já disponível, recomendado por descontinuação do Standard em 2026)
