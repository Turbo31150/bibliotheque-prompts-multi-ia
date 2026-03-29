# OpenClaw -- Recherche

## Description

Prompts pour utiliser OpenClaw dans l'exploration de code et la recherche d'information dans des projets locaux.

## Cas d'usage
- Exploration de codebases inconnus
- Recherche de patterns dans le code
- Analyse de dependances
- Cartographie de projets
- Comprehension d'architecture

---

## Prompts prets a copier

### 1 -- Explorer un codebase

```
Explore le projet dans [CHEMIN] et donne-moi une vue d'ensemble :
- Structure et organisation
- Langage(s) et framework(s)
- Points d'entree
- Fichiers les plus importants
- Architecture generale
```

### 2 -- Chercher un pattern

```
Cherche toutes les occurrences de [PATTERN] dans [CHEMIN] :
- Fichiers concernes
- Contexte de chaque occurrence
- Usage correct vs potentiellement problematique
```

### 3 -- Analyser les dependances

```
Analyse les dependances du projet dans [CHEMIN] :
- Dependances directes et transitives
- Versions et mises a jour disponibles
- Dependances inutilisees
- Vulnerabilites connues
```

### 4 -- Comprendre une fonctionnalite

```
Explique comment [FONCTIONNALITE] est implementee dans [CHEMIN] :
- Flux d'execution (de l'entree a la sortie)
- Fichiers impliques
- Dependances internes
- Points d'extension
```

### 5 -- Trouver du code mort

```
Identifie le code mort dans [CHEMIN] :
- Fonctions jamais appelees
- Imports inutilises
- Variables non utilisees
- Branches de code inatteignables
Propose un plan de nettoyage.
```

---

## Exemples d'utilisation

### Exemple : Exploration
**Prompt** : "Explore ~/projects/jarvis-linux et explique l'architecture"

**Resultat attendu** : Cartographie complete du projet avec diagramme et descriptions.

---

## Effet sur le modele
- OpenClaw parcourt le filesystem pour une analyse reelle du code
- L'exploration est basee sur les fichiers existants, pas des suppositions
- La recherche de patterns couvre tout le codebase
- L'analyse de dependances est basee sur les fichiers de lock reels
