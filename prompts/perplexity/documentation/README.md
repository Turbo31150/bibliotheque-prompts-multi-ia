# Perplexity — Documentation

> Prompts optimises pour la recherche de documentation technique avec Perplexity.

---

## Description

Perplexity est excellent pour trouver, synthetiser et comparer de la documentation technique. Son acces en temps reel au web garantit des informations a jour, et ses citations permettent de remonter aux sources officielles.

## Configuration

- Perplexity Pro pour les recherches approfondies
- Focus : Web pour la doc technique, Academic pour les papers
- Collections pour organiser la doc par projet/technologie

## Prompts par type

### Recherche de documentation officielle
```
Trouve la documentation officielle de [OUTIL/FRAMEWORK] pour [USAGE] :

1. URL de la documentation officielle
2. Guide de demarrage rapide (resume)
3. API reference principales
4. Exemples de code officiels
5. Changelog recent (derniere version)

Liens directs vers chaque section.
```

### Synthese de documentation
```
Synthetise la documentation de [TECHNOLOGIE] :

## Ce que je dois savoir pour [CAS_D_USAGE]
1. Concepts fondamentaux (5 max)
2. Installation et configuration minimale
3. API/Commandes essentielles (top 10)
4. Patterns recommandes
5. Pieges courants (gotchas)
6. Liens vers la doc pour aller plus loin

Format : cheatsheet condensee, pas un tutoriel.
```

### Comparaison de documentations
```
Compare la documentation de [A] vs [B] :

1. Qualite de la doc (completude, clarte, exemples)
2. Guides de migration disponibles
3. API reference (completude, navigation)
4. Exemples et tutoriels officiels
5. Communaute (forums, Discord, Stack Overflow)

Score documentation /10 pour chaque outil.
```

### Recherche de solutions documentees
```
Je rencontre ce probleme avec [TECHNOLOGIE] :

[DESCRIPTION DU PROBLEME]

Recherche dans la documentation officielle et les issues GitHub :
1. Est-ce un bug connu ? (lien issue)
2. Y a-t-il un workaround documente ?
3. Dans quelle version c'est corrige ?
4. Quelle est la solution recommandee ?

Sources officielles uniquement.
```

### Documentation d'API
```
Recherche la documentation de l'API [NOM_API] :

1. URL de la doc API
2. Authentication (methode, tokens)
3. Endpoints principaux (top 10)
4. Rate limits
5. Exemples de requetes (curl)
6. SDK disponibles (Python, JS, Go)
7. Pricing / quotas

Liens directs vers chaque section.
```

## Exemples concrets

```
Trouve la documentation officielle de FastAPI pour :
- WebSocket support
- Background tasks
- Dependency injection
Liens directs, exemples de code, gotchas.
```

```
Synthetise la doc de systemd timers :
Ce que je dois savoir pour remplacer mes cron jobs.
Cheatsheet : syntaxe, commandes, exemples, pieges.
```

```
Je rencontre "RuntimeError: Event loop is already running" avec asyncio Python 3.13.
Recherche dans la doc Python officielle et les issues CPython.
Est-ce un changement dans 3.13 ? Workaround ?
```

```
Documentation de l'API nvidia-smi :
- Options de query (XML, CSV)
- Metriques disponibles
- Exemples de parsing en Python
Sources officielles NVIDIA.
```

## Effet sur le modele

- Perplexity est le meilleur outil pour trouver de la documentation a jour — les URLs sont generalement valides
- Le focus "Academic" est utile pour les papers et specifications techniques
- Le Pro Search croise plusieurs sources — il peut trouver des workarounds dans des issues GitHub que la doc officielle ne mentionne pas
- Demander "sources officielles uniquement" filtre les blogs approximatifs
- Pour les APIs, Perplexity agrege bien les infos (endpoints, auth, rate limits) mais toujours verifier la version
- La force de Perplexity sur la doc est la synthese avec citations — plus efficace que lire 10 pages de doc soi-meme
