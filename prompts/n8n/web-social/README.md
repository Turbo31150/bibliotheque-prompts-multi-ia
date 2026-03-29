# n8n -- Web & Social

## Description

Workflows n8n pour automatiser la publication sur les reseaux sociaux, le scraping web, la veille et la gestion de contenu multi-plateforme.

## Cas d'usage
- Publication automatisee multi-plateforme
- Veille web avec alertes
- Scraping et aggregation de contenu
- Calendrier editorial automatise
- Analyse de metriques sociales

---

## Workflows prets a copier

### 1 -- Publication multi-plateforme

```
Schedule (selon calendrier editorial)
  -> Google Sheets (lire le prochain post a publier)
  -> HTTP Request (Claude : adapter le contenu par plateforme)
  -> Code (parser les versions)
  -> Twitter API (poster le tweet)
  -> LinkedIn API (poster le post)
  -> Reddit API (poster le thread)
  -> Google Sheets (marquer comme publie)
```

---

### 2 -- Veille web automatisee

```
Schedule (toutes les 4h)
  -> HTTP Request (Hacker News API : top stories)
  -> HTTP Request (Reddit API : hot posts r/linux)
  -> Code (filtrer par mots-cles, deduplication)
  -> IF (articles pertinents ?)
    -> OUI : Slack (notification avec resume)
    -> Google Sheets (archiver pour newsletter)
```

---

### 3 -- Monitoring de mentions

```
Schedule (toutes les heures)
  -> HTTP Request (Twitter API : recherche mentions)
  -> HTTP Request (Reddit API : recherche mentions)
  -> Code (deduplication, scoring pertinence)
  -> IF (mention negative ?)
    -> OUI : Slack alerte + Email
  -> Google Sheets (historique des mentions)
```

---

### 4 -- Newsletter automatique

```
Schedule (tous les vendredis 14h)
  -> Google Sheets (articles de la semaine)
  -> HTTP Request (Claude : resume et editorial)
  -> Code (formater en HTML newsletter)
  -> Send Email (liste de diffusion)
  -> Archive (sauvegarder la newsletter)
```

---

### 5 -- Scraping avec alerte changement

```
Schedule (toutes les heures)
  -> HTTP Request (page web a surveiller)
  -> Code (extraire le contenu pertinent, hash)
  -> IF (hash different du precedent ?)
    -> OUI : Slack (notification de changement + diff)
    -> Database (sauvegarder le nouveau hash)
  -> NON : log OK
```

---

## Exemples d'utilisation

### Exemple : Publication auto
**Workflow** : Google Sheets (calendrier) → Claude (adaptation) → APIs sociales (publication)

**Resultat attendu** : Posts publies automatiquement sur toutes les plateformes.

---

## Effet sur le modele
- n8n connecte directement les APIs sociales sans code
- Les workflows sont visuels et faciles a maintenir
- Le scheduling integre remplace les crons manuels
- L'integration avec Claude permet l'adaptation intelligente du contenu
