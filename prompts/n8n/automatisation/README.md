# n8n - Automatisation

## Vue d'ensemble

Les 65 workflows n8n du cluster JARVIS, avec schedule, nodes utilises et objectif. Guide de creation de nouveaux workflows via API.

## Workflows complets (65)

### Infrastructure (12)

| # | Workflow | Schedule | Nodes cles | Description |
|---|---------|----------|------------|-------------|
| 1 | Health Dashboard | `*/15 * * * *` | HTTP, IF, Slack | Dashboard sante cluster |
| 2 | GPU Thermal Monitor | `*/10 * * * *` | SSH, IF, Notification | Surveillance temp GPUs |
| 3 | Prometheus Metrics | `*/5 * * * *` | HTTP, Set, Prometheus | Collecte metriques |
| 4 | Disk Space Alert | `0 * * * *` | SSH, IF, Email | Alerte espace disque |
| 5 | Docker Log Analyzer | `0 */4 * * *` | SSH, Code, Slack | Analyse logs Docker |
| 6 | Service Restart | Webhook | SSH, IF, Notification | Redemarrage auto services |
| 7 | Network Monitor | `*/30 * * * *` | HTTP, Ping, IF | Connectivite reseau |
| 8 | Certificate Check | `0 6 * * *` | HTTP, IF, Email | Expiration certificats SSL |
| 9 | DNS Monitor | `0 */12 * * *` | HTTP, Compare, Alert | Changements DNS |
| 10 | Uptime Report | `0 8 * * 1` | HTTP, Aggregate, Email | Rapport hebdo uptime |
| 11 | Backup Verification | `0 5 * * *` | SSH, IF, Slack | Verification backups |
| 12 | Resource Forecast | `0 9 * * 1` | HTTP, Code, Email | Prevision ressources |

### Trading (10)

| # | Workflow | Schedule | Nodes cles | Description |
|---|---------|----------|------------|-------------|
| 13 | Crypto Alert | `*/15 * * * *` | HTTP/MEXC, IF, TTS | Alertes prix crypto |
| 14 | Trading Scan | `0 * * * *` | HTTP/MEXC, Code, Slack | Scan horaire marche |
| 15 | Position Tracker | `*/30 * * * *` | HTTP/MEXC, Set, DB | Suivi positions ouvertes |
| 16 | Daily PnL | `0 20 * * *` | HTTP/MEXC, Code, Email | Rapport PnL quotidien |
| 17 | Volume Spike | `*/5 * * * *` | HTTP/MEXC, IF, Alert | Detection spikes volume |
| 18 | Funding Rate | `0 */8 * * *` | HTTP/MEXC, Code, Slack | Taux de funding futures |
| 19 | Liquidation Feed | `*/2 * * * *` | WebSocket, IF, Alert | Flux liquidations |
| 20 | Weekly Report | `0 10 * * 0` | HTTP, Aggregate, Email | Rapport trading hebdo |
| 21 | Strategy Backtest | Manuel | Code, HTTP, Set | Backtest de strategies |
| 22 | Order Monitor | `*/1 * * * *` | HTTP/MEXC, IF, TTS | Suivi ordres ouverts |

### AI/Dev (9)

| # | Workflow | Schedule | Nodes cles | Description |
|---|---------|----------|------------|-------------|
| 23 | Code Review | Webhook/GitHub | HTTP, OpenAI, GitHub | Review IA des PRs |
| 24 | Test Runner | Webhook/GitHub | SSH, Code, Slack | Lancement tests auto |
| 25 | Deploy Pipeline | Webhook | SSH, Docker, Notification | Deploiement auto |
| 26 | Model Benchmark | `0 3 * * 0` | HTTP/Ollama, Code, DB | Benchmark modeles LLM |
| 27 | Prompt Library Sync | `0 */6 * * *` | Git, Code, Set | Sync bibliotheque prompts |
| 28 | Doc Generator | Webhook | Code, OpenAI, Git | Generation doc auto |
| 29 | Dependency Check | `0 7 * * 1` | SSH, Code, Slack | Verification dependances |
| 30 | Error Aggregator | `0 */2 * * *` | SSH, Code, Slack | Aggregation erreurs logs |
| 31 | Release Notes | Webhook/GitHub | HTTP, OpenAI, GitHub | Generation release notes |

### Social (8)

| # | Workflow | Schedule | Nodes cles | Description |
|---|---------|----------|------------|-------------|
| 32 | LinkedIn Post | `0 9 * * 1-5` | OpenAI, HTTP/BrowserOS | Publication auto LinkedIn |
| 33 | LinkedIn Engage | `0 10,15 * * 1-5` | HTTP/BrowserOS, Code | Engagement feed LinkedIn |
| 34 | LinkedIn Analytics | `0 18 * * 5` | HTTP/BrowserOS, Code | Metriques LinkedIn hebdo |
| 35 | GitHub Activity | `*/30 * * * *` | HTTP/GitHub, IF, Slack | Activite repos GitHub |
| 36 | GitHub Stars Track | `0 9 * * *` | HTTP/GitHub, DB, Email | Suivi stars quotidien |
| 37 | Content Calendar | `0 8 * * 1` | Code, Set, Notion | Planification contenu hebdo |
| 38 | Hashtag Research | `0 7 * * 1` | HTTP/Perplexity, Code | Recherche hashtags tendance |
| 39 | Community Monitor | `0 */4 * * *` | HTTP, Code, Slack | Veille communaute |

### Ops (14)

| # | Workflow | Schedule | Nodes cles | Description |
|---|---------|----------|------------|-------------|
| 40 | Config Backup | `0 2 * * *` | SSH, Compress, S3 | Backup configs quotidien |
| 41 | Log Cleanup | `0 3 * * 0` | SSH, Code, Notification | Nettoyage logs hebdo |
| 42 | Docker Prune | `0 4 * * 0` | SSH, Docker, Slack | Nettoyage Docker hebdo |
| 43 | Security Audit | `0 1 * * *` | SSH, Code, Email | Audit securite quotidien |
| 44 | Log Error Analyzer | `0 */3 * * *` | SSH, Code, Slack | Analyse erreurs logs |
| 45 | Cluster Drift Detector | `0 6 * * *` | SSH, Code, Alert | Detection derives config |
| 46 | SSL Renew | `0 2 1,15 * *` | SSH, Certbot, Email | Renouvellement SSL |
| 47 | DB Maintenance | `0 3 * * 0` | SSH, SQL, Slack | Maintenance BDD hebdo |
| 48 | Update Checker | `0 8 * * 1` | HTTP, Code, Email | Verification mises a jour |
| 49 | Cron Health | `0 */6 * * *` | SSH, Code, Slack | Verification sante crons |
| 50 | Firewall Audit | `0 2 * * 1` | SSH, Code, Email | Audit regles firewall |
| 51 | User Audit | `0 1 * * 1` | SSH, Code, Email | Audit comptes utilisateurs |
| 52 | Permission Check | `0 5 * * *` | SSH, Code, Alert | Verification permissions |
| 53 | Temp File Cleanup | `0 4 * * *` | SSH, Code, Notification | Nettoyage fichiers temp |

### Integrations (12)

| # | Workflow | Schedule | Nodes cles | Description |
|---|---------|----------|------------|-------------|
| 54 | Webhook Router | Webhook | Switch, HTTP, Code | Routage webhooks entrants |
| 55 | API Bridge OpenClaw | Webhook | HTTP, Transform, HTTP | Bridge API OpenClaw |
| 56 | API Bridge BrowserOS | Webhook | HTTP, Transform, HTTP | Bridge API BrowserOS |
| 57 | Email Digest | `0 8 * * *` | IMAP, Code, Slack | Digest email quotidien |
| 58 | Notification Hub | Webhook | Switch, Slack/Email/TTS | Hub notifications central |
| 59 | Calendar Sync | `0 */2 * * *` | HTTP/GCal, Code, Notion | Sync calendrier |
| 60 | RSS Aggregator | `0 */4 * * *` | RSS, Code, Slack | Aggregation flux RSS |
| 61 | Metrics Export | `*/5 * * * *` | HTTP, Transform, Grafana | Export metriques Grafana |
| 62 | Incident Manager | Webhook | Code, Slack, PagerDuty | Gestion incidents |
| 63 | Report Generator | `0 20 * * *` | HTTP, Code, Email | Rapport quotidien global |
| 64 | Data Pipeline | `0 */6 * * *` | HTTP, Transform, DB | Pipeline donnees generique |
| 65 | Health Aggregator | `0 */15 * * *` | HTTP (multi), Code, Slack | Aggregation sante services |

## Creer un workflow via API

```bash
# Structure minimale d'un workflow
curl -X POST http://localhost:5678/api/v1/workflows \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mon Nouveau Workflow",
    "nodes": [
      {
        "name": "Cron Trigger",
        "type": "n8n-nodes-base.cron",
        "position": [250, 300],
        "parameters": {
          "triggerTimes": {
            "item": [{ "mode": "everyHour" }]
          }
        }
      },
      {
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest",
        "position": [450, 300],
        "parameters": {
          "url": "http://localhost:28789/api/health",
          "method": "GET"
        }
      }
    ],
    "connections": {
      "Cron Trigger": {
        "main": [[{ "node": "HTTP Request", "type": "main", "index": 0 }]]
      }
    },
    "active": true
  }'
```

## Gestion des workflows

```bash
# Lister tous les workflows
curl -s http://localhost:5678/api/v1/workflows \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | jq '.data[] | {id, name, active}'

# Activer/desactiver
curl -X PATCH http://localhost:5678/api/v1/workflows/{id} \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -d '{"active": true}'

# Executer manuellement
curl -X POST http://localhost:5678/api/v1/workflows/{id}/execute \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```
