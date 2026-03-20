# n8n -- Developpement

## Description

Workflows n8n pour assister le developpement : CI/CD, revue de code automatisee, tests et deploiement.

## Cas d'usage
- Pipeline CI/CD orchestre par n8n
- Revue de code automatisee avec IA
- Deploiement automatise avec verification
- Notifications de build et tests
- Gestion de branches et releases

---

## Workflows prets a copier

### 1 -- Revue de code IA automatisee

```
Webhook (nouvelle PR GitHub)
  -> GitHub API (lire le diff)
  -> HTTP Request (Claude : revue de code)
  -> GitHub API (poster le commentaire de revue)
  -> IF (bugs critiques trouves ?)
    -> Request Review (demander une revue humaine)
```

---

### 2 -- Deploy on merge

```
Webhook (PR mergee dans main)
  -> SSH (git pull sur le serveur)
  -> SSH (build et tests)
  -> IF (tests OK ?)
    -> SSH (restart services)
    -> HTTP Request (healthcheck)
    -> Slack (deploy reussi)
  -> NON :
    -> SSH (rollback)
    -> Slack (deploy echoue)
```

---

### 3 -- Notification de build

```
Webhook (CI pipeline termine)
  -> Code (parser le resultat)
  -> IF (succes)
    -> Slack (build OK avec metriques)
  -> IF (echec)
    -> Slack (build KO avec erreurs)
    -> Email (auteur du dernier commit)
```

---

### 4 -- Release automatisee

```
Manual Trigger (version a releaser)
  -> GitHub API (creer tag)
  -> SSH (build production)
  -> SSH (tests de release)
  -> GitHub API (creer release avec changelog)
  -> SSH (deployer en production)
  -> Slack (notifier la release)
```

---

### 5 -- Dependabot workflow

```
Schedule (quotidien)
  -> GitHub API (PRs de dependabot ouvertes)
  -> FOR EACH PR :
    -> GitHub API (lire les changements)
    -> HTTP Request (Claude : evaluer le risque)
    -> IF (risque faible + tests passent)
      -> GitHub API (auto-merge)
    -> IF (risque eleve)
      -> Slack (notifier pour revue manuelle)
```

---

## Exemples d'utilisation

### Exemple : Revue auto
**Workflow** : PR → Claude (revue) → Commentaire GitHub

**Resultat attendu** : Chaque PR recoit une revue IA automatique.

---

## Effet sur le modele
- n8n orchestre les pipelines de developpement visuellement
- L'integration GitHub est native et riche
- Claude fournit des revues de code intelligentes
- Les deploiements sont automatises avec rollback
