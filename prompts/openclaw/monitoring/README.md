# OpenClaw - Monitoring

## Vue d'ensemble

Surveillance du cluster JARVIS via OpenClaw : health checks, statut GPU, watchdog des services. Le monitor-agent centralise toutes les metriques et declenche les alertes.

## Health Checks

### Verification toutes les 5 minutes

Le cron `health_check` verifie :

| Composant | Verification | Seuil critique |
|-----------|-------------|----------------|
| CPU | Charge moyenne | > 90% sur 5 min |
| RAM | Utilisation memoire | > 85% |
| Disque | Espace disponible | < 10% libre |
| Reseau | Connectivite | Timeout > 5s |
| Docker | Containers actifs | Container down |
| Services | Ports ouverts | Port injoignable |

### Services surveilles

| Service | Port | Health endpoint |
|---------|------|-----------------|
| OpenClaw | 18789 | `/api/health` |
| n8n | 5678 | `/healthz` |
| BrowserOS | 9001 | `/status` |
| Ollama | 11434 | `/api/tags` |
| LM Studio | 1234 | `/v1/models` |
| Prometheus | 9090 | `/-/healthy` |
| Grafana | 3000 | `/api/health` |

## Statut GPU

### Surveillance toutes les 10 minutes

```bash
# La skill gpu_thermal execute
nvidia-smi --query-gpu=index,name,temperature.gpu,utilization.gpu,memory.used,memory.total \
  --format=csv,noheader
```

| Metrique | Seuil warning | Seuil critique |
|----------|---------------|----------------|
| Temperature | > 75C | > 85C |
| Utilisation | > 95% pendant 30 min | - |
| Memoire VRAM | > 90% | > 98% |

### Actions automatiques

- **Warning** : log + notification desktop
- **Critique** : notification vocale + tentative de liberation memoire
- **Urgence** : arret des workloads non prioritaires

## Watchdog des services

Le watchdog surveille les services critiques et peut :

1. **Detecter** un service down (health check echoue 3 fois)
2. **Redemarrer** automatiquement (`docker restart <service>`)
3. **Notifier** par vocal si le redemarrage echoue
4. **Escalader** via n8n pour intervention manuelle

```json
{
  "watchdog": {
    "max_retries": 3,
    "retry_interval": 30,
    "auto_restart": true,
    "notify_channels": ["vocal", "desktop"]
  }
}
```

## Consultation du statut

```bash
# Via API OpenClaw
curl http://localhost:28789/api/agents/monitor-agent/status \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"

# Rapport complet
curl http://localhost:28789/api/monitoring/report \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN"
```
