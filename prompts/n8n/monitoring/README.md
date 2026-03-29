# n8n - Monitoring

## Vue d'ensemble

Workflows n8n dedies au monitoring du cluster JARVIS : health dashboard, surveillance GPU, metriques Prometheus, espace disque, analyse logs Docker.

## Workflows monitoring

### Health Dashboard (toutes les 15 min)

**Schedule** : `*/15 * * * *`

```
Cron -> HTTP Request (multi-services health)
  -> Code (agreger statuts)
  -> IF (service down ?)
    -> OUI : Slack alerte + tentative restart
    -> NON : log OK
  -> Set (formater dashboard)
  -> HTTP Request (push vers Grafana)
```

**Services verifies** :
| Service | Endpoint | Port |
|---------|----------|------|
| OpenClaw | `/api/health` | 18789 |
| n8n | `/healthz` | 5678 |
| BrowserOS MCP | `/status` | 9001 |
| Ollama | `/api/tags` | 11434 |
| LM Studio | `/v1/models` | 1234 |
| Prometheus | `/-/healthy` | 9090 |
| Grafana | `/api/health` | 3000 |

### GPU Thermal Monitor (toutes les 10 min)

**Schedule** : `*/10 * * * *`

```
Cron -> SSH (nvidia-smi sur chaque machine)
  -> Code (parser output, extraire temperatures)
  -> IF (temp > 75C ?)
    -> WARNING : Slack notification
  -> IF (temp > 85C ?)
    -> CRITIQUE : TTS alerte vocale + action corrective
  -> Set (metriques formatees)
  -> HTTP Request (push Prometheus)
```

**Metriques extraites** :
- Temperature par GPU (6 GPUs sur M1)
- Utilisation GPU (%)
- Memoire VRAM utilisee/totale
- Puissance consommee (W)
- Fan speed (%)

### Prometheus Metrics Collector (toutes les 5 min)

**Schedule** : `*/5 * * * *`

```
Cron -> HTTP Request (endpoints metriques multiples)
  -> Code (transformer en format Prometheus)
  -> HTTP Request (push vers Prometheus Pushgateway)
```

**Metriques collectees** :
- CPU, RAM, disque, reseau (node_exporter)
- GPU (nvidia_smi_exporter)
- Docker containers (cAdvisor)
- Services applicatifs (custom)

### Disk Space Alert (toutes les heures)

**Schedule** : `0 * * * *`

```
Cron -> SSH (df -h sur chaque partition)
  -> Code (parser, calculer % libre)
  -> IF (< 10% libre ?)
    -> OUI : Email alerte + Slack
    -> IF (< 5% libre ?)
      -> CRITIQUE : TTS + nettoyage auto (logs, tmp, docker prune)
  -> NON : log OK
```

**Partitions surveillees** :
| Partition | Seuil warning | Seuil critique |
|-----------|---------------|----------------|
| `/` | < 15% libre | < 5% libre |
| `/home` | < 10% libre | < 3% libre |
| `/var` | < 20% libre | < 10% libre |
| `/tmp` | < 30% libre | < 10% libre |

### Docker Log Analyzer (toutes les 4h)

**Schedule** : `0 */4 * * *`

```
Cron -> SSH (docker logs --since 4h pour chaque container)
  -> Code (parser logs, detecter erreurs/warnings)
  -> IF (erreurs critiques ?)
    -> OUI : Slack avec details + suggestion de fix
  -> Code (agreger statistiques)
  -> Slack (resume des 4 dernieres heures)
```

**Patterns detectes** :
- `ERROR` / `FATAL` : erreurs critiques
- `OOM` / `OutOfMemory` : problemes memoire
- `Connection refused` : services injoignables
- `Timeout` : lenteurs reseau/service
- Restart loops (container qui redemarre en boucle)

## Alertes et notifications

| Severite | Canal | Exemple |
|----------|-------|---------|
| Info | Log n8n | Service OK, metrique normale |
| Warning | Slack #monitoring | Temp GPU 78C, disque 12% libre |
| Critique | Slack + TTS vocal | GPU 87C, service down, disque 3% |
| Urgence | Slack + TTS + Email | Cluster unreachable, data loss risk |
