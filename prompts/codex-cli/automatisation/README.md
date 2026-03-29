# Codex CLI -- Automatisation

## Description

Prompts pour utiliser OpenAI Codex CLI dans la creation de scripts et d'automatisations systeme.

## Cas d'usage
- Scripts bash/Python d'automatisation
- Configuration de crons et timers
- Pipelines de traitement de donnees
- Automatisation de deploiement
- Maintenance automatisee

---

## Prompts prets a copier

### 1 -- Script de backup

```
Cree un script de backup complet :
- Sauvegarde [DOSSIERS] en tar.gz avec date
- Transfert vers [DESTINATION] via rsync
- Rotation : garde 7 quotidiens, 4 hebdomadaires
- Log et notification par email en cas d'erreur
- Cron entry pour execution quotidienne a 3h
```

### 2 -- Deploiement automatise

```
Cree un script de deploiement pour [PROJET] :
- git pull, build, tests, restart service
- Rollback automatique si tests echouent
- Notification Slack du resultat
```

### 3 -- Nettoyage automatique

```
Cree un script de nettoyage systeme :
- Logs > 30 jours
- /tmp > 7 jours
- Docker images/volumes orphelins
- Cache apt/pip
Cron hebdomadaire. Log des actions.
```

### 4 -- Synchronisation de fichiers

```
Cree un script de synchronisation bidirectionnelle
entre [SOURCE] et [DESTINATION].
Detection de conflits. Log des changements. Cron toutes les heures.
```

### 5 -- Provisionnement de serveur

```
Cree un script de provisionnement pour un serveur Ubuntu frais :
Paquets essentiels, configuration systeme, Docker, monitoring, securite.
Idempotent (re-executable sans effet de bord).
```

---

## Effet sur le modele
- Codex CLI cree et teste les scripts directement
- Les crons sont configures et actives immediatement
- Les scripts sont valides dans le contexte reel du serveur
