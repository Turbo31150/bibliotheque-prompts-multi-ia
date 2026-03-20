# Codex CLI -- Web & Social

## Description

Prompts pour utiliser OpenAI Codex CLI dans le scraping web, la veille et l'automatisation de taches liees au web et aux reseaux sociaux.

## Cas d'usage
- Scraping de donnees web
- Veille technologique automatisee
- Generation de contenu
- Monitoring de pages web
- Automatisation de publications

---

## Prompts prets a copier

### 1 -- Scraper une page

```
Scrape [URL] et extrais les donnees en JSON :
- Titre, description, liens principaux
- Stocke dans ~/scraping/[domaine].json
```

### 2 -- Veille Hacker News

```
Cree un script qui recupere le top 10 Hacker News toutes les 4h.
Filtre par mots-cles [LISTE]. Notification desktop si match.
```

### 3 -- Monitorer une page

```
Surveille [URL] pour detecter les changements.
Compare le hash du contenu toutes les heures.
Alerte si changement detecte. Historique en SQLite.
```

### 4 -- Generer du contenu

```
A partir de [FICHIER/SUJET], genere un thread Twitter (5 tweets)
et un post LinkedIn. Sauve dans ~/social/.
```

### 5 -- Analyser les tendances GitHub

```
Recupere les repos trending GitHub en [LANGAGE] cette semaine.
Pour chaque repo : nom, etoiles, description.
Sauve en Markdown dans ~/veille/.
```

---

## Effet sur le modele
- Codex CLI execute curl/jq pour du scraping reel
- Les scripts de veille sont autonomes via cron
- L'acces au filesystem organise les donnees collectees
