# OpenClaw - Configuration

## Vue d'ensemble

Installation et configuration d'OpenClaw (anciennement Open-WebUI + Pipelines), la gateway IA centrale du cluster JARVIS.

## Ports

| Service | Port |
|---------|------|
| Frontend (WebUI) | `18789` |
| Backend (Pipelines/API) | `28789` |

## Installation

```bash
# Docker compose (recommande)
docker compose up -d openclaw

# Verification
curl -s http://localhost:18789/api/health
```

## Authentification

- Token API defini dans `OPENCLAW_AUTH_TOKEN`
- Fichier `.env` a la racine du projet OpenClaw
- Le token est requis pour tous les appels API et les connexions MCP

## Serveurs MCP connectes

| Serveur | Fonction |
|---------|----------|
| `jarvis-mcp` | Commandes systeme JARVIS |
| `browseros-mcp` | Controle navigateur via CDP |
| `n8n-mcp` | Declenchement workflows n8n |
| `filesystem-mcp` | Acces fichiers local |
| `trading-mcp` | Ordres et alertes MEXC |

## Configuration des modeles

```json
{
  "providers": {
    "ollama": {
      "url": "http://localhost:11434",
      "models": ["llama3", "mistral", "codellama"]
    },
    "lmstudio": {
      "url": "http://localhost:1234",
      "models": ["deepseek-coder"]
    },
    "jarvis-proxy": {
      "url": "http://localhost:28789/proxy",
      "models": ["gpt-4o", "claude-sonnet", "gemini-pro"]
    }
  }
}
```

## Configuration des agents

Les agents sont definis dans l'interface OpenClaw ou via l'API :

```bash
curl -X POST http://localhost:28789/api/agents \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "monitor-agent", "model": "llama3", "skills": ["health_check"]}'
```

## Configuration des skills

Les skills sont des fonctions TypeScript chargees dynamiquement par les agents. Elles se trouvent dans le repertoire `skills/` d'OpenClaw et sont enregistrees au demarrage.

## Fichiers cles

- `docker-compose.yml` - Stack OpenClaw
- `.env` - Variables d'environnement (token, ports, providers)
- `config/models.json` - Configuration des modeles IA
- `config/agents.json` - Definition des agents
- `skills/` - Repertoire des skills TypeScript
