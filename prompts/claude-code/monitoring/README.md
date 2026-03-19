# Claude Code — Monitoring

## Description
Prompts pour le monitoring systeme avec Claude Code : health checks du cluster, surveillance GPU temps reel, metriques Prometheus, dashboards Grafana et alertes automatiques.

## Configuration requise
- Claude Code avec plugins `gpu-monitor`, `cluster-health`, `metrics-exporter`
- `nvidia-smi` installe pour le monitoring GPU
- Prometheus sur port 9090 (optionnel)
- Grafana sur port 3000 (optionnel)
- Bot Telegram/Discord pour les alertes
- Permissions : `nvidia-smi`, `systemctl status`, `journalctl`, `curl 127.0.0.1*`

---

## Prompts par type de tache

### Creation — Dashboard de monitoring complet

```
Cree un systeme de monitoring complet pour l'infrastructure JARVIS :

## COMPOSANTS A MONITORER
1. Cluster IA : 4 noeuds (M1, M2, M3, OL1) — status, latence, modeles charges
2. GPUs : 6 GPUs — temperature, utilisation, VRAM
3. Services : JARVIS, n8n, Canvas, BrowserOS, Ollama, LM Studio
4. Systeme : CPU, RAM, disque, reseau
5. Trading : positions ouvertes, PnL, alertes prix
6. Crons : 12 taches planifiees — dernier run, status

## ARCHITECTURE
- Collecteur : script Python async qui poll toutes les 30s
- Stockage : Prometheus (metriques) + SQLite (historique)
- Affichage : endpoint /dashboard JSON + Grafana
- Alertes : Telegram si composant down ou metrique critique

## SEUILS D'ALERTE
| Metrique | Warning | Critical |
|----------|---------|----------|
| GPU temp | > 75C | > 85C |
| CPU usage | > 80% | > 95% |
| RAM usage | > 85% | > 95% |
| Disk usage | > 80% | > 90% |
| Latence API | > 2s | > 5s |
| Noeud cluster | 1 down | 2+ down |
```

---

### Creation — Health check endpoint

```
Cree un endpoint /health/full qui aggrege le status de tous les composants :

## SPECIFICATION
- Methode : GET
- Latence max : 2 secondes
- Format reponse :

{
  "status": "healthy|degraded|critical",
  "timestamp": "ISO8601",
  "uptime": "Xh Xm",
  "components": {
    "cluster": {"status": "...", "nodes_online": 4, "nodes_total": 4},
    "gpu": {"status": "...", "max_temp": 65, "avg_temp": 58},
    "services": {"status": "...", "healthy": 6, "total": 6},
    "system": {"cpu": 45, "ram": 62, "disk": 55}
  }
}

## LOGIQUE
- "healthy" : tous les composants OK
- "degraded" : 1 composant WARNING ou 1 noeud down
- "critical" : 1+ composant CRITICAL ou 2+ noeuds down

## IMPLEMENTATION
- asyncio.gather pour paralliser les checks
- Timeout 1.5s par composant (fail fast)
- Cache 10s pour eviter le flood
```

---

### Amelioration / Refactoring — Optimiser les metriques

```
Optimise le systeme de metriques existant :

1. Analyse les metriques actuellement collectees
2. Identifie les metriques inutiles (jamais consultees, redondantes)
3. Identifie les metriques manquantes (angles morts)
4. Propose un schema de metriques optimal :
   - Nommage coherent (namespace_subsystem_metric_unit)
   - Labels pertinents
   - Types corrects (counter, gauge, histogram, summary)
5. Reduis la cardinalite pour eviter l'explosion de series temporelles
```

---

### Debug — Alerte GPU temperature

```
Alerte GPU temperature elevee. Diagnostique et resous :

## INFORMATIONS
- GPU concerne : [NUMERO]
- Temperature : [VALEUR]C
- Seuil : 75C (warning) / 85C (critical)

## PROCESSUS
1. Identifie la cause :
   - Quel processus utilise le GPU ? (nvidia-smi -q)
   - Le ventilateur fonctionne ? (fan speed)
   - La charge est-elle normale pour la tache en cours ?
   - Y a-t-il un memory leak GPU ?

2. Actions immediates :
   - Si > 85C : decharger le modele le plus lourd
   - Re-router les requetes vers les GPUs plus froids
   - Notifier via Telegram

3. Actions preventives :
   - Ajuster les limites de puissance (nvidia-smi -pl)
   - Configurer un profil ventilateur plus agressif
   - Redistribuer les modeles entre GPUs
```

---

### Debug — Service down

```
Un service ne repond plus. Diagnostique :

Service : [NOM]
Port attendu : [PORT]
Derniere reponse : [TIMESTAMP]

## CHECKLIST
1. Le processus tourne ? (ps aux | grep [NOM])
2. Le port est ouvert ? (ss -tlnp | grep [PORT])
3. Le service systemd est actif ? (systemctl status [NOM])
4. Les logs montrent quoi ? (journalctl -u [NOM] --since "10 min ago")
5. Les dependances sont OK ? (DB, API externes, cluster)
6. L'espace disque est suffisant ? (df -h)
7. La RAM est suffisante ? (free -h)

## ACTIONS
- Si crash : restart + analyser les logs
- Si OOM : augmenter les limites ou optimiser
- Si disk full : cleanup + rotation des logs
- Si dependance down : corriger la dependance d'abord
```

---

### Documentation — Rapport de sante

```
Genere un rapport de sante complet du systeme :

## FORMAT
### Status global : [HEALTHY/DEGRADED/CRITICAL]

### Cluster IA
| Noeud | Status | Modele | GPU Temp | Latence | Tokens/s |
|-------|--------|--------|----------|---------|----------|
| M1 | ... | ... | ... | ... | ... |
| M2 | ... | ... | ... | ... | ... |
| M3 | ... | ... | ... | ... | ... |
| OL1 | ... | ... | ... | ... | ... |

### GPUs
| GPU | Temp | Utilisation | VRAM Used/Total | Processus |
|-----|------|-------------|-----------------|-----------|

### Services
| Service | Port | Status | Uptime | Derniere erreur |
|---------|------|--------|--------|-----------------|

### Systeme
- CPU : X% (X cores)
- RAM : X GB / X GB (X%)
- Disk : X GB / X GB (X%)
- Network : X MB/s in, X MB/s out

### Alertes actives
[Liste des alertes non resolues]

### Recommandations
[Actions suggerees]
```

---

## Exemples concrets

### Exemple 1 : Health check rapide
```bash
claude "/cluster-check"
```

**Resultat attendu** : Tableau 4 noeuds avec status, temperature, modeles charges, latence.

### Exemple 2 : Surveillance GPU
```bash
claude "/gpu-status"
```

**Resultat attendu** : 6 GPUs avec temperature, utilisation, VRAM, processus actifs.

### Exemple 3 : Audit systeme complet
```bash
claude "/audit"
```

**Resultat attendu** : Rapport complet CPU/RAM/disk/network + recommandations.

---

## Effet sur le modele
- Les seuils explicites (75C warning, 85C critical) donnent des reperes clairs
- Le format tableau force des donnees comparables entre composants
- Le health check asyncio.gather avec timeout evite les blocages
- Les 3 niveaux (healthy/degraded/critical) simplifient la prise de decision
- Le hook session-cluster-check injecte automatiquement le status au debut de chaque session
- Le modele adapte ses recommandations en fonction de l'etat du cluster (evite les calculs lourds si chaud)
