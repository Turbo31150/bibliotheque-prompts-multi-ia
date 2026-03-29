# n8n — Workflows JARVIS

> 65 workflows n8n pour automatiser JARVIS : monitoring, trading, notifications, backups, CI/CD.

---

## Vue d'ensemble

n8n tourne sur http://127.0.0.1:5678 et orchestre 65 workflows couvrant tous les aspects de JARVIS.

### Categories de workflows

| Categorie | Nombre | Description |
|-----------|--------|-------------|
| Monitoring | 12 | Health checks, GPU, services, cluster |
| Trading | 10 | Scan multi-exchange, alertes, backtesting |
| Notifications | 8 | Telegram, Discord, email, push |
| Backups | 6 | Sauvegarde incrementale, rotation, verification |
| CI/CD | 8 | Tests auto, deployment, rollback |
| Recherche | 7 | Veille techno, RSS, digest |
| GitHub | 6 | PR review, issue triage, releases |
| Data | 5 | ETL, nettoyage, aggregation |
| Securite | 3 | Audit, alertes, rotation secrets |

---

## Workflows cles

### 1. Health Check Complet (toutes les 15 min)

```json
{
  "name": "JARVIS Health Patrol",
  "trigger": "cron",
  "schedule": "*/15 * * * *",
  "nodes": [
    {
      "type": "HTTP Request",
      "name": "Check Cluster M1",
      "url": "http://127.0.0.1:1234/health"
    },
    {
      "type": "HTTP Request",
      "name": "Check Cluster M2",
      "url": "http://192.168.1.26:1234/health"
    },
    {
      "type": "HTTP Request",
      "name": "Check Ollama",
      "url": "http://127.0.0.1:11434/api/tags"
    },
    {
      "type": "HTTP Request",
      "name": "Check Canvas",
      "url": "http://127.0.0.1:18800/health"
    },
    {
      "type": "IF",
      "name": "Any Down?",
      "condition": "statusCode != 200"
    },
    {
      "type": "Telegram",
      "name": "Alert",
      "message": "JARVIS: {{$node.name}} is DOWN"
    }
  ]
}
```

### 2. Trading Monitor (toutes les heures)

```json
{
  "name": "JARVIS Trading Monitor",
  "trigger": "cron",
  "schedule": "0 * * * *",
  "nodes": [
    {
      "type": "HTTP Request",
      "name": "MEXC Prices",
      "url": "https://api.mexc.com/api/v3/ticker/24hr"
    },
    {
      "type": "Code",
      "name": "Filter Movers",
      "code": "return items.filter(i => Math.abs(i.priceChangePercent) > 5)"
    },
    {
      "type": "IF",
      "name": "Big Movers?",
      "condition": "items.length > 0"
    },
    {
      "type": "Telegram",
      "name": "Alert Movers",
      "message": "Crypto movers > 5%: {{$json.symbols}}"
    }
  ]
}
```

### 3. Daily Briefing (8h du matin)

```json
{
  "name": "JARVIS Daily Briefing",
  "trigger": "cron",
  "schedule": "0 8 * * *",
  "nodes": [
    {
      "type": "HTTP Request",
      "name": "System Metrics",
      "url": "http://127.0.0.1:8000/metrics"
    },
    {
      "type": "HTTP Request",
      "name": "Cluster Status",
      "url": "http://127.0.0.1:8000/health/full"
    },
    {
      "type": "HTTP Request",
      "name": "Trading Summary",
      "url": "http://127.0.0.1:8000/api/trading/summary"
    },
    {
      "type": "Code",
      "name": "Format Briefing",
      "code": "// Formate le briefing en texte lisible"
    },
    {
      "type": "Telegram",
      "name": "Send Briefing"
    }
  ]
}
```

### 4. Backup Automatique (3h du matin)

```json
{
  "name": "JARVIS Auto Backup",
  "trigger": "cron",
  "schedule": "0 3 * * *",
  "nodes": [
    {
      "type": "Execute Command",
      "name": "Backup DBs",
      "command": "tar czf /backup/jarvis-db-$(date +%Y%m%d).tar.gz /home/turbo/jarvis-linux/data/*.db"
    },
    {
      "type": "Execute Command",
      "name": "Backup Configs",
      "command": "tar czf /backup/jarvis-config-$(date +%Y%m%d).tar.gz /home/turbo/.claude/ /home/turbo/jarvis-linux/.env"
    },
    {
      "type": "Execute Command",
      "name": "Rotate Old Backups",
      "command": "find /backup -mtime +7 -delete"
    },
    {
      "type": "Telegram",
      "name": "Confirm Backup"
    }
  ]
}
```

---

## Prompt pour creer un nouveau workflow

```
Cree un workflow n8n pour [TACHE].

## Specifications
- Declencheur : [cron/webhook/manual]
- Frequence : [si cron]
- Entree : [donnees d'entree]
- Traitement : [etapes de traitement]
- Sortie : [ou envoyer le resultat]
- Alertes : [conditions d'alerte]

## Contraintes n8n
- Utiliser les nodes natifs quand possible
- Code nodes en JavaScript (pas TypeScript)
- Timeout max 5 minutes par workflow
- Retry 3 fois avec backoff exponentiel
- Logs dans /home/turbo/jarvis-linux/logs/

## Format de sortie
JSON du workflow importable dans n8n.
```

---

## Comment importer un workflow

```bash
# Via l'API n8n
curl -X POST http://127.0.0.1:5678/api/v1/workflows \
  -H "Content-Type: application/json" \
  -d @workflow.json

# Ou via l'interface web
# 1. Ouvrir http://127.0.0.1:5678
# 2. Menu > Import from file
# 3. Selectionner le fichier JSON
```

---

## Prerequis
- n8n installe et en execution (`npm install -g n8n && n8n start`)
- Port 5678 disponible
- Credentials configurees (Telegram, MEXC, GitHub, etc.)
