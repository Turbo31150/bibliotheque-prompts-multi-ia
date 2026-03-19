# Gemini CLI -- Web & Social

## Description

Prompts pour utiliser Gemini CLI dans le scraping web, l'analyse de reseaux sociaux, la veille technologique et l'automatisation de taches web. Gemini CLI peut executer des scripts et stocker les resultats localement.

## Cas d'usage
- Scraping et extraction de donnees web
- Veille technologique automatisee
- Analyse de tendances et sentiments
- Automatisation de publications
- Monitoring de reputation en ligne

---

## Prompts prets a copier

### 1 -- Veille technologique automatisee

```
Cree un systeme de veille technologique en bash :

## SOURCES
- Hacker News (API : https://hacker-news.firebaseio.com)
- Reddit (API : subreddits r/linux, r/selfhosted, r/homelab)
- GitHub Trending (scraping)
- RSS feeds (liste configurable)

## FONCTIONNALITES
- Collecte toutes les 4 heures
- Filtrage par mots-cles configurables
- Deduplication (pas d'articles deja vus)
- Scoring de pertinence (mots-cles matches x upvotes)
- Resume des top 10 articles du jour
- Sauvegarde en Markdown dans ~/veille/YYYY-MM-DD.md
- Notification desktop des articles scoring > seuil

## DEPENDANCES
- curl, jq, sqlite3 (historique)
- Pas de Python requis
```

---

### 2 -- Scraper et analyser un site

```
Cree un script pour scraper [URL] et extraire :

1. Structure du site (sitemap / liens internes)
2. Contenu textuel principal (pas la navigation)
3. Metadonnees (title, description, og tags)
4. Technologies detectees (headers, scripts, frameworks)
5. Performance (temps de reponse, taille page)

## REGLES
- Respecter robots.txt
- Rate limiting (1 requete / seconde)
- User-Agent identifie
- Stocker les resultats en JSON structure
- Pas de scraping de donnees personnelles

## OUTILS
- curl pour les requetes
- xmllint ou pup pour le parsing HTML
- jq pour le formatage JSON
```

---

### 3 -- Monitorer des pages web pour changements

```
Cree un script qui surveille des pages web pour detecter les changements :

## PAGES A SURVEILLER
[LISTER LES URLs]

## FONCTIONNEMENT
1. Telecharger la page (curl)
2. Extraire le contenu pertinent (pas headers/footers)
3. Comparer avec la version precedente (diff)
4. Si changement detecte :
   - Sauvegarder l'ancienne et la nouvelle version
   - Generer un diff lisible
   - Notifier avec le resume du changement
5. Historique dans SQLite (url, date, hash, diff)

## EXECUTION
- Cron configurable par page (toutes les heures, tous les jours)
- Fichier de config YAML pour les URLs et frequences
- Dashboard : resume des changements de la semaine
```

---

### 4 -- Analyser les tendances GitHub

```
Analyse les tendances GitHub pour [LANGAGE/TECHNOLOGIE] :

1. Recupere les repos trending de la semaine (API GitHub)
2. Pour chaque repo du top 20 :
   - Nom, description, etoiles, forks
   - Croissance recente (etoiles cette semaine)
   - Derniere activite (commit, issue, PR)
   - Licence
3. Identifie les patterns :
   - Nouvelles technologies emergentes
   - Projets morts (plus de commits depuis > 6 mois)
   - Forks actifs qui depassent l'original
4. Rapport Markdown dans ~/veille/github/

Inclure les commandes gh CLI pour chaque requete.
```

---

### 5 -- Generer du contenu pour les reseaux sociaux

```
A partir de ce contenu technique [COLLER OU CHEMIN FICHIER], genere des posts pour :

1. Twitter/X (280 caracteres, thread si necessaire)
   - Hook accrocheur
   - Points cles en bullet points
   - CTA (call to action)
   - Hashtags pertinents (max 5)

2. LinkedIn (post professionnel)
   - Introduction avec question
   - Corps structure
   - Conclusion avec invitation au debat

3. Reddit (post communautaire)
   - Titre descriptif
   - Corps detaille avec formatage Markdown
   - Ton communautaire (pas marketing)

Sauvegarder chaque version dans ~/social/YYYY-MM-DD/
```

---

## Exemples d'utilisation

### Exemple : Veille rapide
**Commande** : `gemini "Quels sont les projets GitHub trending en Rust cette semaine ?"`

**Resultat attendu** : Liste des projets trending avec description et metriques.

### Exemple : Monitoring de page
**Commande** : `gemini "Surveille https://example.com/pricing et previens-moi si les prix changent"`

**Resultat attendu** : Script de monitoring avec cron et notification configure.

---

## Effet sur le modele
- Gemini CLI peut executer curl et les outils CLI pour du scraping reel
- L'acces au filesystem permet de stocker et organiser la veille
- Les scripts generes sont autonomes et executables via cron
- L'integration avec les APIs (GitHub, HN, Reddit) donne des donnees structurees
