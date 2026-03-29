# n8n -- Debug

## Description

Workflows n8n pour automatiser le diagnostic et la resolution de bugs : pipelines de triage, analyse automatique d'erreurs et notifications de regression.

## Cas d'usage
- Triage automatique de bugs
- Analyse d'erreurs avec notification
- Detection de regressions dans la CI
- Escalade automatique de bugs critiques
- Post-mortem automatise

---

## Workflows prets a copier

### 1 -- Triage automatique de bugs

```
Webhook (nouvelle issue GitHub/GitLab)
  -> HTTP Request (Claude : analyser le bug)
  -> Code (extraire priorite, categorie, assignation)
  -> GitHub API (ajouter labels, assignation)
  -> IF (priorite P1 ?)
    -> OUI : Slack alerte urgente
    -> Email aux responsables
  -> NON : Slack canal bugs
```

---

### 2 -- Analyse d'erreur automatique

```
Webhook (erreur production : Sentry, logs)
  -> Code (deduplication : deja vu ?)
  -> IF (nouvelle erreur)
    -> HTTP Request (Claude : analyser + suggerer fix)
    -> GitHub API (creer issue avec analyse)
    -> Slack (notifier avec suggestion de fix)
```

---

### 3 -- Detection de regression CI

```
Webhook (CI pipeline echoue)
  -> GitHub API (git diff depuis dernier succes)
  -> HTTP Request (Claude : quel commit a cause la regression ?)
  -> Slack (notifier l'auteur du commit avec l'analyse)
  -> GitHub API (commenter sur le commit/PR)
```

---

### 4 -- Escalade automatique

```
Schedule (toutes les heures)
  -> GitHub API (issues P1 ouvertes > 4h)
  -> IF (issues non assignees ou sans activite)
    -> Slack (escalade au manager)
    -> Email (alerte escalade)
    -> Code (mettre a jour le statut)
```

---

### 5 -- Rapport de bugs hebdomadaire

```
Schedule (vendredi 17h)
  -> GitHub API (issues de la semaine)
  -> HTTP Request (Claude : analyser les tendances)
  -> Code (generer le rapport)
  -> Send Email (rapport hebdomadaire)
  -> Slack (resume dans #engineering)
```

---

## Exemples d'utilisation

### Exemple : Triage auto
**Workflow** : Issue GitHub → Claude (analyse) → Labels + assignation + notification

**Resultat attendu** : Chaque bug est automatiquement trie, labelle et assigne.

---

## Effet sur le modele
- n8n automatise le pipeline de bug management
- L'integration GitHub/GitLab est native
- Claude analyse les bugs et suggere des fixes
- Les escalades automatiques evitent les bugs oublies
