# n8n - Configuration

## Vue d'ensemble

Installation et configuration de n8n, le moteur de workflows du cluster JARVIS. 65 workflows documentes couvrant l'ensemble des besoins d'automatisation.

## Installation

```bash
# Installation globale
npm install -g n8n

# Ou via Docker
docker run -d --name n8n \
  -p 5678:5678 \
  -v $HOME/.n8n:/home/node/.n8n \
  n8nio/n8n
```

## Acces

| Parametre | Valeur |
|-----------|--------|
| URL | `http://localhost:5678` |
| Port | `5678` |
| API endpoint | `http://localhost:5678/api/v1` |
| API Key | `${N8N_API_KEY}` |

## Configuration API

```bash
# Definir la cle API
export N8N_API_KEY="votre-cle-api"

# Tester la connexion
curl -s http://localhost:5678/api/v1/workflows \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | jq '.data | length'
```

## Import de workflows

```bash
# Importer un workflow depuis un fichier JSON
curl -X POST http://localhost:5678/api/v1/workflows \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @workflow.json

# Activer un workflow
curl -X PATCH http://localhost:5678/api/v1/workflows/{id} \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -d '{"active": true}'
```

## 65 workflows - Categories

| Categorie | Nombre | Description |
|-----------|--------|-------------|
| Infrastructure | 12 | Health checks, monitoring, alertes systeme |
| Trading | 10 | Alertes crypto, scans marche, PnL |
| AI/Dev | 9 | Code review, tests, deploiement |
| Social | 8 | LinkedIn, GitHub, engagement |
| Ops | 14 | Backup, cleanup, maintenance, securite |
| Integrations | 12 | Webhooks, API bridges, notifications |

## Variables d'environnement

```bash
# n8n core
N8N_PORT=5678
N8N_PROTOCOL=http
N8N_HOST=localhost
N8N_API_KEY=xxx

# Credentials
N8N_ENCRYPTION_KEY=xxx
MEXC_API_KEY=xxx
MEXC_API_SECRET=xxx
GITHUB_TOKEN=xxx
LINKEDIN_COOKIE=xxx

# Services internes
OPENCLAW_URL=http://localhost:28789
BROWSEROS_MCP_URL=http://localhost:9001
OLLAMA_URL=http://localhost:11434
```

## Fichiers cles

- `~/.n8n/` - Repertoire de donnees n8n
- `~/.n8n/config` - Configuration n8n
- `workflows/` - Exports JSON des workflows
- `.env` - Variables d'environnement
