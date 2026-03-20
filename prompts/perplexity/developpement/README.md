# Perplexity -- Developpement

## Description

Prompts pour utiliser Perplexity dans la recherche d'information pour le developpement : documentation officielle, exemples de code, meilleures pratiques et comparaisons de librairies.

## Cas d'usage
- Recherche de documentation officielle
- Trouver des exemples de code fonctionnels
- Comparer des librairies et frameworks
- Meilleures pratiques par langage/framework
- Recherche de patterns et architectures

---

## Prompts prets a copier

### 1 -- Trouver la documentation officielle

```
Recherche la documentation officielle pour [FONCTIONNALITE] dans [TECHNOLOGIE] :

1. Lien direct vers la page de documentation
2. Resume des points cles
3. Exemple de code officiel
4. Parametres et options disponibles
5. Cas limites documentes
6. Changements recents (si l'API a evolue)

Si la doc officielle est insuffisante :
- Meilleur tutoriel tiers
- Exemples GitHub les plus etoiles
- Discussion Stack Overflow la plus utile
```

---

### 2 -- Comparer des librairies

```
Compare les librairies [LANGAGE] pour [BESOIN] en [ANNEE] :

## CANDIDATS
[LISTER OU DEMANDER LES MEILLEURES]

## CRITERES
1. API / ergonomie (exemples de code)
2. Performance (benchmarks recents)
3. Taille et dependances
4. Maintenance (derniere release, frequence commits)
5. Popularite (npm downloads, pip installs, GitHub stars)
6. Documentation (qualite, exemples)
7. TypeScript / type hints (si applicable)
8. Breaking changes (stabilite de l'API)

Tableau comparatif avec sources.
Recommandation : "utilise X si..., utilise Y si..."
```

---

### 3 -- Trouver des patterns et architectures

```
Recherche les patterns recommandes pour [PROBLEME] en [LANGAGE/FRAMEWORK] :

1. Pattern recommande par la communaute
   - Description
   - Exemple de code
   - Source (doc officielle, article, repo)

2. Alternatives
   - Autres patterns applicables
   - Quand preferer chaque alternative

3. Anti-patterns
   - Ce qu'il ne faut PAS faire
   - Pourquoi (problemes rencontres)

4. Exemples en production
   - Projets open source qui implementent ce pattern
   - Liens GitHub

References : articles, livres, talks.
```

---

### 4 -- Rechercher des exemples de code

```
Recherche des exemples de code fonctionnels pour [TACHE] en [LANGAGE] :

## EXIGENCES
- Code a jour (compatible [VERSION])
- Teste et fonctionnel
- Avec gestion d'erreurs
- Bien commente

## SOURCES A PRIVILEGIER
1. Documentation officielle (exemples)
2. Repos GitHub etoiles
3. Stack Overflow (reponses acceptees)
4. Blogs tech reconnus

Pour chaque exemple :
- Code complet (copy-paste ready)
- Source et lien
- Date (est-ce encore d'actualite ?)
- Dependances requises
- Adaptations necessaires pour mon cas
```

---

### 5 -- Meilleures pratiques par technologie

```
Quelles sont les meilleures pratiques [LANGAGE/FRAMEWORK] en [ANNEE] :

1. STRUCTURE DE PROJET
   - Organisation des fichiers recommandee
   - Conventions de nommage

2. CODE
   - Patterns idiomatiques
   - Gestion d'erreurs
   - Tests (frameworks recommandes, couverture cible)

3. PERFORMANCE
   - Optimisations courantes
   - Pieges de performance a eviter

4. SECURITE
   - Pratiques de securite specifiques au langage
   - Dependances : audit et mise a jour

5. OUTILLAGE
   - Linter / formatter recommande
   - IDE / extensions
   - CI/CD template

Sources : guides officiels, livres de reference, styleguides d'entreprises (Google, Airbnb).
```

---

## Exemples d'utilisation

### Exemple : Documentation
**Prompt** : "Comment utiliser asyncio.TaskGroup en Python 3.12, doc officielle et exemples."

**Resultat attendu** : Lien vers la doc, exemples de code et cas d'usage avec sources.

### Exemple : Comparaison
**Prompt** : "FastAPI vs Litestar vs Django Ninja pour une API REST en 2026."

**Resultat attendu** : Comparaison sourcee avec benchmarks, ecosysteme et recommandation.

---

## Effet sur le modele
- Perplexity fournit des liens directs vers la documentation officielle
- Les exemples de code sont verifiables via les sources citees
- Les comparaisons s'appuient sur des benchmarks et metriques reelles
- Les meilleures pratiques sont a jour grace a la recherche temps reel
