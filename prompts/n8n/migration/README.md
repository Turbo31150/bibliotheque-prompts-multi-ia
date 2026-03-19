# n8n -- Migration

## Description

Workflows n8n pour automatiser et orchestrer les migrations : backup pre-migration, execution planifiee, verification post-migration et rollback automatise.

## Cas d'usage
- Orchestration de migrations multi-etapes
- Backup et rollback automatises
- Verification post-migration
- Notification de progression
- Documentation automatique de migration

---

## Workflows prets a copier

### 1 -- Orchestration de migration

```
Manual Trigger (lancement migration)
  -> SSH (backup pre-migration)
  -> IF (backup OK ?)
    -> OUI : SSH (etape 1 : migration schema)
      -> SSH (etape 2 : migration donnees)
      -> SSH (etape 3 : verification)
      -> IF (verification OK ?)
        -> OUI : Slack (migration reussie)
        -> NON : SSH (rollback) -> Slack (echec + rollback)
    -> NON : Slack (backup echoue, migration annulee)
```

---

### 2 -- Backup pre-migration automatise

```
Manual Trigger
  -> SSH (dump base de donnees)
  -> SSH (tar des configurations)
  -> SSH (docker save des images custom)
  -> Code (verifier checksums)
  -> IF (tout OK ?)
    -> Set (flag backup_ready = true)
    -> Slack (backup pret, migration possible)
```

---

### 3 -- Verification post-migration

```
Webhook (signal fin de migration)
  -> SSH (tests de sante : services, ports, donnees)
  -> HTTP Request (healthchecks des APIs)
  -> Code (comparer metriques avant/apres)
  -> IF (tout OK ?)
    -> Slack (migration validee)
    -> Send Email (rapport de migration)
  -> NON :
    -> Slack (problemes detectes + details)
    -> IF (critique ?)
      -> SSH (rollback automatique)
```

---

### 4 -- Notification de progression

```
Webhook (etape de migration terminee)
  -> Code (calculer progression %)
  -> Slack (mise a jour : "Migration 3/7 : schema migre ✓")
  -> IF (erreur dans l'etape ?)
    -> Slack alerte + Email
```

---

### 5 -- Rapport de migration

```
Webhook (migration terminee)
  -> SSH (collecter metriques avant/apres)
  -> HTTP Request (Claude : generer le rapport)
  -> Send Email (rapport complet)
  -> Google Drive (archiver)
```

---

## Exemples d'utilisation

### Exemple : Migration Docker
**Workflow** : Backup → Migration containers → Verification → Notification

**Resultat attendu** : Migration orchestree avec backup, rollback et rapport.

---

## Effet sur le modele
- n8n orchestre visuellement les migrations multi-etapes
- Le rollback automatique protege contre les echecs
- Les notifications en temps reel suivent la progression
- L'integration SSH permet d'operer sur les serveurs directement
