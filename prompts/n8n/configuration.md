# n8n — Configuration

> Configuration complete de n8n pour JARVIS : installation, credentials, integration.

---

## Installation

```bash
# Installation globale
npm install -g n8n

# Ou via Docker (recommande pour la production)
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -e N8N_BASIC_AUTH_USER=admin \
  -e N8N_BASIC_AUTH_PASSWORD=your_password \
  --restart unless-stopped \
  n8nio/n8n
```

---

## Credentials a configurer

### Telegram

```json
{
  "name": "Telegram JARVIS",
  "type": "telegramApi",
  "data": {
    "accessToken": "${TELEGRAM_TOKEN}",
    "chatId": "${TELEGRAM_CHAT}"
  }
}
```

### MEXC (Trading)

```json
{
  "name": "MEXC API",
  "type": "httpHeaderAuth",
  "data": {
    "name": "X-MEXC-APIKEY",
    "value": "${MEXC_API_KEY}"
  }
}
```

### GitHub

```json
{
  "name": "GitHub JARVIS",
  "type": "githubApi",
  "data": {
    "accessToken": "${GITHUB_TOKEN}",
    "server": "https://api.github.com"
  }
}
```

### Discord

```json
{
  "name": "Discord Webhook",
  "type": "webhook",
  "data": {
    "url": "${DISCORD_WEBHOOK_URL}"
  }
}
```

---

## Variables d'environnement n8n

```bash
# Fichier ~/.n8n/.env
N8N_PORT=5678
N8N_PROTOCOL=http
N8N_HOST=127.0.0.1

# Authentification
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your_secure_password

# Execution
N8N_DEFAULT_BINARY_DATA_MODE=filesystem
EXECUTIONS_TIMEOUT=300
EXECUTIONS_TIMEOUT_MAX=600

# Logging
N8N_LOG_LEVEL=info
N8N_LOG_OUTPUT=console,file
N8N_LOG_FILE_LOCATION=/home/turbo/jarvis-linux/logs/n8n.log

# Timezone
GENERIC_TIMEZONE=Europe/Paris
```

---

## Integration avec JARVIS

### Webhook receiver (JARVIS ecoute n8n)

```python
# src/webhooks.py
# Endpoint : POST /api/webhooks/n8n
# Recoit les notifications de workflows termines
# Actions possibles :
# - Relayer vers Telegram/Discord
# - Mettre a jour la base de donnees
# - Declencher un autre workflow
```

### JARVIS appelle n8n

```bash
# Declencher un workflow via webhook
curl -X POST http://127.0.0.1:5678/webhook/jarvis-trigger \
  -H "Content-Type: application/json" \
  -d '{"action": "trading-scan", "params": {"exchange": "mexc"}}'
```

---

## Monitoring de n8n

```bash
# Verifier que n8n tourne
curl -s http://127.0.0.1:5678/healthz

# Lister les workflows actifs
curl -s http://127.0.0.1:5678/api/v1/workflows | python3 -m json.tool

# Voir les executions recentes
curl -s http://127.0.0.1:5678/api/v1/executions | python3 -m json.tool
```

---

## Prerequis
- Node.js 18+ installe
- Port 5678 disponible
- Credentials API pour les services externes
- Docker (optionnel, recommande pour la production)

## Version Courte (Modèles Locaux <4B)

> Pour qwen2.5:1.5b, gemma-3-4b et petits modèles

```text
[Rôle en 1 ligne]. [Tâche en 1 ligne]. Réponds en 3 lignes max. Français.
```
