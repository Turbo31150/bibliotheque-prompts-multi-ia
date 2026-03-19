# OpenClaw - Automatisation

## Vue d'ensemble

Planification et execution automatique des agents OpenClaw via cron jobs internes. 11 taches configurees couvrant monitoring, trading, social et maintenance.

## Cron jobs configures (11)

| # | Nom | Schedule | Agent | Description |
|---|-----|----------|-------|-------------|
| 1 | `health_check` | `*/5 * * * *` | monitor-agent | Verification sante cluster toutes les 5 min |
| 2 | `gpu_thermal` | `*/10 * * * *` | monitor-agent | Surveillance temperature GPUs |
| 3 | `trading_scan` | `0 * * * *` | trading-agent | Scan marche crypto toutes les heures |
| 4 | `crypto_alert` | `*/15 * * * *` | trading-agent | Alertes prix crypto toutes les 15 min |
| 5 | `linkedin_post` | `0 9 * * 1-5` | social-agent | Publication LinkedIn quotidienne (lun-ven 9h) |
| 6 | `github_watch` | `*/30 * * * *` | dev-agent | Surveillance repos GitHub toutes les 30 min |
| 7 | `backup_config` | `0 2 * * *` | ops-agent | Backup configurations a 2h du matin |
| 8 | `log_cleanup` | `0 3 * * 0` | ops-agent | Nettoyage logs chaque dimanche 3h |
| 9 | `model_refresh` | `0 4 * * 1` | ops-agent | Mise a jour modeles chaque lundi 4h |
| 10 | `daily_report` | `0 20 * * *` | report-agent | Rapport journalier a 20h |
| 11 | `security_audit` | `0 1 * * *` | security-agent | Audit securite quotidien a 1h |

## Configuration des cron jobs

Les cron jobs sont definis dans la configuration OpenClaw :

```json
{
  "cron_jobs": [
    {
      "name": "health_check",
      "schedule": "*/5 * * * *",
      "agent": "monitor-agent",
      "skill": "cluster_health",
      "params": { "notify_on_failure": true },
      "enabled": true
    }
  ]
}
```

## Gestion via API

```bash
# Lister les cron jobs
curl http://localhost:28789/api/cron \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"

# Activer/desactiver un job
curl -X PATCH http://localhost:28789/api/cron/health_check \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN" \
  -d '{"enabled": false}'

# Executer manuellement
curl -X POST http://localhost:28789/api/cron/health_check/run \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"
```

## Auto-dispatch

Le systeme d'auto-dispatch route automatiquement les evenements entrants vers l'agent le plus adapte :

- **Evenement systeme** (alerte CPU, disque plein) -> `monitor-agent`
- **Signal trading** (prix, volume) -> `trading-agent`
- **Notification GitHub** (PR, issue) -> `dev-agent`
- **Requete vocale** -> `vocal-agent`

Le dispatch se base sur des regles de matching configurables dans `config/dispatch_rules.json`.

## Logs et historique

```bash
# Voir les executions recentes
curl http://localhost:28789/api/cron/history?limit=50 \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"

# Logs d'un job specifique
curl http://localhost:28789/api/cron/health_check/logs \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"
```
