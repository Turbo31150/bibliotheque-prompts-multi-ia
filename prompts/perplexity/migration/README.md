# Perplexity -- Migration

## Description

Prompts pour utiliser Perplexity dans la recherche d'information pour les migrations : guides officiels, retours d'experience, outils de migration et pieges a eviter.

## Cas d'usage
- Trouver les guides de migration officiels
- Rechercher les breaking changes entre versions
- Trouver des retours d'experience de migration
- Identifier les outils de migration existants
- Anticiper les problemes de migration

---

## Prompts prets a copier

### 1 -- Trouver le guide de migration officiel

```
Recherche le guide de migration de [TECHNO] de la version [A] a la version [B] :

1. Documentation officielle
   - Lien vers le guide de migration
   - Breaking changes documentes
   - Deprecations

2. Changelog
   - Resume des changements majeurs
   - Nouveautes a exploiter

3. Retours de la communaute
   - Problemes rencontres par d'autres lors de la migration
   - Discussions Reddit/HN/GitHub Issues
   - Workarounds pour les problemes non documentes

4. Outils de migration
   - Scripts officiels de migration (codemods, etc.)
   - Outils tiers recommandes

5. ESTIMATION
   - Difficulte de la migration (facile/moyenne/difficile)
   - Temps estime
   - Risques principaux
```

---

### 2 -- Rechercher des retours d'experience

```
Recherche des retours d'experience de migration de [SOURCE] vers [CIBLE] :

1. ARTICLES DE BLOG
   - Post-mortems de migration
   - Guides pas a pas
   - Lecons apprises

2. DISCUSSIONS COMMUNAUTAIRES
   - Reddit, Hacker News, forums specialises
   - Questions/reponses sur Stack Overflow

3. TALKS ET VIDEOS
   - Presentations de conferences
   - Tutoriels YouTube

Pour chaque source :
- Lien
- Contexte (taille du projet, equipe)
- Ce qui a bien marche
- Ce qui a mal tourne
- Conseils donnes

Synthese : les 5 lecons les plus frequentes.
```

---

### 3 -- Identifier les outils de migration

```
Recherche les outils existants pour migrer de [SOURCE] vers [CIBLE] :

## TYPES D'OUTILS
1. Migration automatique (codemods, transpilers)
2. Migration de donnees (ETL, sync)
3. Migration d'infrastructure (IaC, scripts)
4. Tests de compatibilite (validation post-migration)

## POUR CHAQUE OUTIL
- Nom et lien
- Ce qu'il migre automatiquement
- Ce qu'il ne gere pas (manuel requis)
- Qualite (etoiles, maintenance, derniere MaJ)
- Retours d'experience

L'outil le plus recommande avec procedure d'utilisation.
```

---

### 4 -- Anticiper les problemes de migration

```
Quels sont les problemes courants lors de la migration de [SOURCE] vers [CIBLE] :

1. PROBLEMES TECHNIQUES
   - Incompatibilites connues
   - Comportements differents (meme API, resultat different)
   - Performance (regression ou amelioration)

2. PROBLEMES DE DONNEES
   - Formats incompatibles
   - Perte de donnees possibles
   - Encoding et caracteres speciaux

3. PROBLEMES OPERATIONNELS
   - Downtime pendant la migration
   - Rollback (est-ce possible ?)
   - Formation de l'equipe

4. PROBLEMES IGNORES
   - Ce que les gens oublient souvent
   - Les gotchas non documentes
   - Les dependances indirectes affectees

Sources avec liens vers les issues et discussions.
```

---

### 5 -- Migration Windows vers Linux

```
Recherche les meilleurs guides et outils pour migrer de Windows a Linux en [ANNEE] :

1. DISTRIBUTIONS RECOMMANDEES
   - Pour un ancien utilisateur Windows
   - Pour un developpeur
   - Pour un serveur

2. EQUIVALENCES LOGICIELLES
   - Les 20 logiciels Windows les plus courants et leurs equivalents Linux
   - Ceux qui n'ont pas d'equivalent (alternatives ou compatibilite Wine)

3. MIGRATION DES DONNEES
   - Fichiers et documents
   - Emails et calendriers
   - Bookmarks et mots de passe

4. OUTILS DE MIGRATION
   - Scripts de migration automatique
   - Dual boot vs VM vs migration complete
   - WSL comme transition

5. RETOURS D'EXPERIENCE
   - Articles de gens qui ont migre
   - Ce qui manque le plus (et comment compenser)
   - Combien de temps pour etre productif

Sources fiables et recentes.
```

---

## Exemples d'utilisation

### Exemple : Guide de migration
**Prompt** : "Guide de migration Python 3.11 vers 3.13, breaking changes et problemes courants."

**Resultat attendu** : Resume des breaking changes avec liens vers la doc officielle et workarounds.

### Exemple : Retours d'experience
**Prompt** : "Retours d'experience migration Docker Compose v1 vers v2, problemes rencontres."

**Resultat attendu** : Synthese des problemes courants avec solutions sourcees.

---

## Effet sur le modele
- Perplexity trouve les guides de migration officiels les plus a jour
- Les retours d'experience communautaires completent la documentation
- Les outils de migration sont evalues avec des donnees recentes
- Les problemes non documentes sont identifies via les forums et issues
