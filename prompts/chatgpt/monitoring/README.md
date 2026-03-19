# ChatGPT -- Monitoring

## Description

Prompts pour utiliser ChatGPT dans la surveillance et le monitoring de systemes, serveurs, clusters et applications. ChatGPT excelle dans l'analyse de logs, la creation de dashboards et la suggestion de seuils d'alerte.

## Cas d'usage
- Analyse de logs systeme et applicatifs
- Creation de regles d'alerte Prometheus/Grafana
- Diagnostic de pannes a partir de metriques
- Generation de scripts de monitoring
- Interpretation de metriques de performance

---

## Prompts prets a copier

### 1 -- Analyser des logs systeme

```
Analyse ces logs systeme et identifie :
1. Les erreurs critiques et leur frequence
2. Les patterns recurrents (meme erreur, meme heure)
3. Les correlations entre evenements
4. Les causes probables
5. Les actions correctives recommandees

Classe les problemes par severite (critique/warning/info).
Format : tableau avec colonnes [Heure | Severite | Probleme | Cause probable | Action].

Logs :
[COLLER LES LOGS ICI]
```

---

### 2 -- Creer des regles d'alerte Prometheus

```
Cree des regles d'alerte Prometheus (format YAML) pour surveiller un cluster Linux avec :
- 6 GPUs NVIDIA (temperature, utilisation, VRAM)
- CPU Ryzen 5700X3D (8 cores)
- 46 Go de RAM
- Disques NVMe et HDD

Pour chaque metrique :
- Seuil WARNING et CRITIQUE
- Duree avant declenchement (for:)
- Labels et annotations avec description
- Runbook URL placeholder

Genere au minimum 15 regles couvrant : CPU, RAM, disque, GPU, reseau, services systemd.
```

---

### 3 -- Diagnostiquer une panne a partir de metriques

```
Voici les metriques de mon serveur sur les dernieres 24h :

CPU : [VALEURS]
RAM : [VALEURS]
Disque I/O : [VALEURS]
Reseau : [VALEURS]
GPU : [VALEURS]

Le symptome observe : [DECRIRE LE PROBLEME]

Analyse ces metriques et :
1. Identifie la cause racine la plus probable
2. Explique la chaine de causalite
3. Propose 3 actions correctives par ordre de priorite
4. Suggere des metriques supplementaires a surveiller
5. Recommande des seuils d'alerte pour prevenir la recurrence
```

---

### 4 -- Generer un script de healthcheck

```
Genere un script bash de healthcheck complet pour un serveur Linux qui verifie :

1. Services systemd (liste configurable)
2. Ports ouverts (liste configurable)
3. Espace disque par partition
4. Utilisation CPU et RAM
5. Connectivite reseau (DNS, passerelle, internet)
6. Certificats SSL (expiration)
7. Conteneurs Docker (statut, restarts)
8. GPUs NVIDIA (nvidia-smi)

Sortie : JSON structure avec statut global (OK/WARNING/CRITICAL) et detail par check.
Le script doit etre compatible avec un cron toutes les 5 minutes.
Inclure le logging dans /var/log/healthcheck.log.
```

---

### 5 -- Creer un dashboard Grafana

```
Genere le JSON d'un dashboard Grafana complet pour monitorer un cluster de machines Linux avec :
- Panneau CPU (gauge + timeseries)
- Panneau RAM (gauge + timeseries)
- Panneau disque (bar gauge par partition)
- Panneau GPU (6 GPUs : temperature, utilisation, VRAM en timeseries)
- Panneau reseau (bandwidth in/out)
- Panneau services (stat panels vert/rouge par service)
- Panneau alertes actives (table)

Source : Prometheus. Variables template : $instance, $job.
Theme sombre, refresh 30s.
```

---

## Exemples d'utilisation

### Exemple : Analyser un pic de CPU
**Prompt** : "Mon CPU est a 100% depuis 2h, voici le top 10 des processus [coller top]. Diagnostique et propose des solutions."

**Resultat attendu** : Identification du processus fautif, analyse de la cause (fuite memoire, boucle infinie, charge legitime), et actions correctives specifiques.

### Exemple : Configurer des alertes
**Prompt** : "Cree les regles Prometheus pour alerter quand mes GPUs depassent 80C pendant plus de 5 minutes."

**Resultat attendu** : Fichier YAML avec regles d'alerte, annotations et labels prets a deployer.

---

## Effet sur le modele
- ChatGPT est excellent pour analyser des logs en langage naturel et identifier des patterns
- Les prompts structures avec format de sortie explicite produisent des resultats directement exploitables
- Demander des seuils specifiques (WARNING/CRITIQUE) force le modele a donner des valeurs concretes
- L'ajout de contexte materiel (6 GPUs, Ryzen, 46 Go RAM) permet des recommandations adaptees
