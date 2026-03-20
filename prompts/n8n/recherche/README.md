# n8n -- Recherche

## Description

Workflows n8n pour automatiser la recherche d'information : veille technologique, aggregation de sources, analyse et distribution de contenu.

## Cas d'usage
- Aggregation multi-sources automatisee
- Veille technologique avec filtrage intelligent
- Recherche periodique avec alertes
- Curation de contenu automatisee
- Base de connaissances auto-alimentee

---

## Workflows prets a copier

### 1 -- Veille multi-sources

```
Schedule (toutes les 4h)
  -> HTTP Request (Hacker News API)
  -> HTTP Request (Reddit API)
  -> HTTP Request (GitHub Trending)
  -> HTTP Request (RSS feeds)
  -> Code (deduplication, filtrage mots-cles)
  -> HTTP Request (Claude : scorer la pertinence)
  -> IF (score > seuil)
    -> Slack (notification)
    -> Google Sheets (archiver)
```

---

### 2 -- Alerte sur mots-cles

```
Schedule (toutes les heures)
  -> HTTP Request (recherche sur [SOURCES])
  -> Code (filtrer par mots-cles : [LISTE])
  -> IF (nouveaux resultats)
    -> Slack (notification avec resume)
    -> Database (marquer comme vu)
```

---

### 3 -- Newsletter automatique de veille

```
Schedule (vendredi 10h)
  -> Database (articles de la semaine, top 10 par score)
  -> HTTP Request (Claude : rediger la newsletter)
  -> Send Email (newsletter)
  -> Archive (sauvegarder)
```

---

### 4 -- Recherche GitHub automatisee

```
Schedule (quotidien)
  -> GitHub API (recherche : [QUERY] created:>7d)
  -> Code (filtrer par etoiles, activite, langue)
  -> HTTP Request (Claude : evaluer chaque repo)
  -> IF (repo interessant)
    -> Slack (notification)
    -> Google Sheets (ajouter a la liste de suivi)
```

---

### 5 -- Base de connaissances auto-alimentee

```
Webhook (nouvel article/lien ajoute)
  -> HTTP Request (recuperer le contenu)
  -> HTTP Request (Claude : resumer, tagger, categoriser)
  -> Database (inserer avec tags et resume)
  -> Slack (confirmer l'ajout)
```

---

## Exemples d'utilisation

### Exemple : Veille IA
**Workflow** : HN + Reddit + GitHub → filtrage "LLM" → Claude (resume) → Slack

**Resultat attendu** : Notification Slack avec les meilleures actualites IA de la journee.

---

## Effet sur le modele
- n8n connecte facilement les APIs de sources multiples
- Le filtrage par mots-cles + scoring IA reduit le bruit
- La newsletter automatique synthetise la veille sans effort
- La base de connaissances s'alimente automatiquement
