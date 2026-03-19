# n8n -- Automatisation

## Description

Workflows n8n pour automatiser des taches repetitives : pipelines de donnees, maintenance systeme, deploiement et orchestration de services.

## Cas d'usage
- Pipelines de traitement automatises
- Maintenance systeme planifiee
- Deploiement automatique
- Orchestration de services
- Synchronisation de donnees

---

## Workflows prets a copier

### 1 -- Pipeline de backup automatise

```
Schedule (quotidien 3h)
  -> SSH (dump base de donnees)
  -> SSH (tar des configs)
  -> SSH (docker save des images custom)
  -> SSH (rsync vers NAS)
  -> Code (verifier checksums)
  -> IF (tout OK ?)
    -> Slack (backup OK avec taille et duree)
  -> IF (erreur)
    -> Slack alerte + Email
    -> SSH (tentative de retry)
```

---

### 2 -- Nettoyage systeme automatise

```
Schedule (hebdomadaire dimanche 4h)
  -> SSH (docker system prune -f)
  -> SSH (suppression logs > 30 jours)
  -> SSH (nettoyage /tmp et caches)
  -> SSH (apt autoremove)
  -> Code (calculer espace libere)
  -> Slack (rapport de nettoyage)
```

---

### 3 -- Deploiement automatique sur push

```
Webhook (GitHub push sur main)
  -> SSH (git pull)
  -> SSH (docker-compose build)
  -> SSH (docker-compose up -d)
  -> HTTP Request (healthcheck)
  -> IF (healthcheck OK ?)
    -> Slack (deploy reussi)
  -> NON :
    -> SSH (docker-compose rollback)
    -> Slack (deploy echoue, rollback effectue)
```

---

### 4 -- Synchronisation de donnees

```
Schedule (toutes les heures)
  -> HTTP Request (API source : recuperer les donnees)
  -> Code (transformer le format)
  -> HTTP Request (API cible : envoyer les donnees)
  -> IF (erreur ?)
    -> Code (retry avec backoff)
    -> Slack (alerte si echec apres 3 retries)
  -> Database (log de synchronisation)
```

---

### 5 -- Rotation de certificats SSL

```
Schedule (quotidien)
  -> SSH (openssl x509 -enddate sur chaque certificat)
  -> Code (calculer jours restants)
  -> IF (< 30 jours)
    -> SSH (certbot renew)
    -> SSH (nginx reload)
    -> Slack (certificat renouvele)
  -> IF (< 7 jours et renouvellement echoue)
    -> Email alerte urgente
```

---

## Exemples d'utilisation

### Exemple : Backup
**Workflow** : Cron 3h → dump DB → tar configs → rsync → verification → notification

**Resultat attendu** : Backup quotidien automatise avec verification et notification.

---

## Effet sur le modele
- n8n orchestre visuellement les automatisations complexes
- Le mode schedule remplace les crons manuels
- Les workflows sont versionnables et exportables
- L'integration SSH permet d'operer sur les serveurs directement
