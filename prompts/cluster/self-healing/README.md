# Cluster — Self-Healing

## Boucle Auto-Reparation

Le cluster JARVIS surveille et repare automatiquement les pannes via une boucle en 4 etapes.

### 1. Detection

Surveillance continue toutes les 5 minutes :
- Ping des noeuds (timeout 5s)
- Verification API endpoint (health check HTTP)
- Monitoring GPU (nvidia-smi)
- Verification des modeles charges

### 2. Diagnostic

Quand une anomalie est detectee :
- Classification du type de panne (reseau, GPU, modele, memoire)
- Evaluation de la severite (warning, critical, fatal)
- Identification de la cause probable

### 3. Reparation

Actions automatiques selon le type de panne :

| Panne | Action |
|-------|--------|
| Noeud injoignable | Retry 3x, puis exclusion du routeur |
| GPU OOM | Decharger le modele le moins utilise |
| Modele non charge | Auto-load sur noeud disponible |
| API timeout | Restart du service (LM Studio / Ollama) |
| Temperature critique | Throttle GPU, redistribution charge |

### 4. Verification

Apres reparation :
- Re-test du noeud repare
- Validation avec une requete de test
- Reintegration dans le routeur si OK
- Notification Telegram si echec persistant

## Circuit Breaker

Protection contre les cascades de pannes :

```
Etats : CLOSED -> OPEN -> HALF-OPEN -> CLOSED

CLOSED   : fonctionnement normal
OPEN     : noeud exclu (apres 3 echecs consecutifs)
HALF-OPEN: 1 requete test toutes les 60s
CLOSED   : retour normal si test OK
```

- **Seuil d'ouverture** : 3 echecs consecutifs
- **Duree OPEN** : 60 secondes minimum
- **Reset** : apres 1 requete HALF-OPEN reussie

## Backoff Exponentiel

En cas d'echecs repetes, l'intervalle entre les tentatives augmente :

```
Tentative 1 : attente 1s
Tentative 2 : attente 2s
Tentative 3 : attente 4s
Tentative 4 : attente 8s
Maximum     : 60s
```

## Scheduler

Le self-healing tourne via un scheduler automatique :

```bash
# Crontab ou timer systemd
*/5 * * * * /home/turbo/jarvis-linux/scripts/cluster-health-check.sh
```

Verification toutes les 5 minutes, 24/7.
