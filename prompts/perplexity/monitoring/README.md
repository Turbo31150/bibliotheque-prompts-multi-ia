# Perplexity -- Monitoring

## Description

Prompts pour utiliser Perplexity dans la recherche de solutions de monitoring, de bonnes pratiques d'observabilite et de configurations optimales. Perplexity trouve les solutions les plus recentes et les retours d'experience.

## Cas d'usage
- Recherche de stacks de monitoring
- Comparaison d'outils d'observabilite
- Trouver des dashboards et configurations pretes
- Meilleures pratiques SRE et observabilite
- Troubleshooting de problemes de monitoring

---

## Prompts prets a copier

### 1 -- Choisir une stack de monitoring

```
Recherche la meilleure stack de monitoring pour un homelab Linux en [ANNEE] :

## MON INFRASTRUCTURE
- [N] serveurs Linux
- [N] GPUs NVIDIA
- Docker avec [N] containers
- Budget : [GRATUIT / $X/mois]

## COMPARAISON
1. Prometheus + Grafana + Alertmanager
2. InfluxDB + Telegraf + Chronograf
3. Victoria Metrics + Grafana
4. Netdata
5. Zabbix

Pour chaque stack :
- Installation (complexite, temps)
- Consommation de ressources
- Scalabilite
- Dashboards disponibles (prets a l'emploi)
- Alerting
- Communaute et support
- Lien vers la doc d'installation

Recommandation pour mon cas.
```

---

### 2 -- Trouver des dashboards Grafana

```
Recherche les meilleurs dashboards Grafana pour monitorer :
- [COMPOSANT 1 : Linux server, Docker, NVIDIA GPU, etc.]
- [COMPOSANT 2]
- [COMPOSANT 3]

## POUR CHAQUE DASHBOARD
1. Lien Grafana.com (ID du dashboard)
2. Screenshot ou description visuelle
3. Data source requise (Prometheus, InfluxDB, etc.)
4. Metriques couvertes
5. Nombre de telechargements / reviews
6. Derniere mise a jour
7. Instructions d'import

Top 3 par composant.
```

---

### 3 -- Resoudre un probleme de monitoring

```
Mon monitoring ne fonctionne pas correctement :

## PROBLEME
[DECRIRE : metriques manquantes, alertes qui ne se declenchent pas, dashboards vides, etc.]

## STACK
[Prometheus / Grafana / etc. avec versions]

Recherche :
1. Ce probleme est-il connu (GitHub Issues, forums) ?
2. Les causes les plus courantes
3. Les solutions verifiees
4. La configuration correcte (avec exemples)
5. Comment tester que ca fonctionne

Sources avec liens pour chaque solution.
```

---

### 4 -- Meilleures pratiques d'observabilite

```
Recherche les meilleures pratiques d'observabilite en [ANNEE] :

1. Les 3 piliers : metriques, logs, traces
   - Outil recommande pour chaque pilier
   - Comment les correler

2. Alerting efficace
   - Regles pour eviter l'alert fatigue
   - SLO-based alerting vs threshold alerting
   - Runbooks automatiques

3. Dashboards utiles
   - RED method (Rate, Errors, Duration)
   - USE method (Utilization, Saturation, Errors)
   - Les 4 Golden Signals

4. Culture SRE
   - Error budgets
   - Blameless post-mortems
   - Toil reduction

Livres, articles et talks de reference avec liens.
```

---

### 5 -- Monitorer des GPUs NVIDIA

```
Recherche la meilleure facon de monitorer des GPUs NVIDIA sous Linux en [ANNEE] :

## CONTEXTE
- [N] GPUs [MODELE]
- OS : Ubuntu/Debian
- Stack monitoring existante : [Prometheus/Grafana si existant]

## RECHERCHE
1. Exporters Prometheus pour NVIDIA
   - nvidia-smi-exporter vs dcgm-exporter vs nvitop
   - Installation et configuration

2. Metriques essentielles
   - Temperature, utilisation, VRAM, puissance
   - Metriques par processus/container
   - Erreurs ECC

3. Dashboards Grafana pour GPU
   - Meilleurs dashboards disponibles (liens)

4. Alertes recommandees
   - Seuils par metrique
   - Exemples de regles Prometheus

5. Optimisation
   - Frequence de scraping recommandee
   - Impact sur la performance GPU du monitoring
```

---

## Exemples d'utilisation

### Exemple : Stack monitoring
**Prompt** : "Meilleure stack de monitoring gratuite pour 3 serveurs Linux avec Docker et 6 GPUs en 2026."

**Resultat attendu** : Recommandation sourcee avec guide d'installation et dashboards.

### Exemple : Dashboards
**Prompt** : "Meilleur dashboard Grafana pour NVIDIA GPUs avec Prometheus, lien direct."

**Resultat attendu** : ID du dashboard Grafana.com avec instructions d'import et screenshot.

---

## Effet sur le modele
- Perplexity trouve les outils et dashboards les plus recents et populaires
- Les liens directs (Grafana.com, GitHub) sont immediatement utilisables
- Les retours d'experience communautaires completent la documentation officielle
- La recherche en temps reel garantit des recommandations a jour
