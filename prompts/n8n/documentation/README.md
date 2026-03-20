# n8n -- Documentation

## Description

Workflows n8n pour automatiser la generation et la maintenance de documentation : changelogs, rapports, wikis et documentation technique.

## Cas d'usage
- Generation automatique de changelogs
- Rapports periodiques auto-generes
- Mise a jour de wikis et documentation
- Documentation d'incidents automatisee
- Export de documentation multi-format

---

## Workflows prets a copier

### 1 -- Changelog automatique

```
Webhook (nouveau tag Git)
  -> GitHub API (commits depuis dernier tag)
  -> HTTP Request (Claude : generer changelog)
  -> GitHub API (creer release avec changelog)
  -> Slack (notifier la release)
```

---

### 2 -- Rapport hebdomadaire auto

```
Schedule (lundi 8h)
  -> HTTP Request (metriques Prometheus : semaine)
  -> GitHub API (PRs merges, issues fermees)
  -> HTTP Request (Claude : generer rapport)
  -> Send Email (rapport HTML)
  -> Google Drive (archiver)
```

---

### 3 -- Documentation d'incident

```
Webhook (incident declare)
  -> Code (creer timeline)
  -> SSH (collecter logs et metriques)
  -> HTTP Request (Claude : rediger post-mortem)
  -> Google Docs (creer le document)
  -> Slack (partager le lien)
```

---

### 4 -- Mise a jour de wiki

```
Webhook (PR mergee avec label "docs")
  -> GitHub API (lire les fichiers modifies)
  -> HTTP Request (Claude : mettre a jour la doc)
  -> GitHub API (commit les mises a jour doc)
  -> Slack (notifier la mise a jour)
```

---

### 5 -- Export multi-format

```
Manual Trigger (document a exporter)
  -> HTTP Request (recuperer le contenu Markdown)
  -> Code (convertir en HTML)
  -> HTTP Request (API PDF : convertir en PDF)
  -> Google Drive (sauvegarder MD + HTML + PDF)
  -> Send Email (envoyer les 3 formats)
```

---

## Exemples d'utilisation

### Exemple : Changelog auto
**Workflow** : Tag Git → Commits → Claude → Release GitHub

**Resultat attendu** : Release notes generees et publiees automatiquement.

---

## Effet sur le modele
- n8n automatise le cycle de vie de la documentation
- L'integration GitHub permet la generation depuis les commits
- Claude redige les rapports et changelogs
- Les exports multi-format couvrent tous les besoins
