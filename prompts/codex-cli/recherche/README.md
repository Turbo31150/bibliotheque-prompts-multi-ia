# Codex CLI -- Recherche

## Description

Prompts pour utiliser OpenAI Codex CLI dans la recherche d'information dans le code, les fichiers et la documentation locale.

## Cas d'usage
- Recherche dans de grands codebases
- Exploration de projets inconnus
- Analyse de dependances
- Recherche de patterns dans le code
- Investigation de bugs

---

## Prompts prets a copier

### 1 -- Explorer un projet

```
Explore [CHEMIN] et donne une vue d'ensemble :
Structure, langages, architecture, fichiers cles.
```

### 2 -- Chercher un pattern

```
Cherche toutes les utilisations de [PATTERN] dans [CHEMIN].
Contexte de chaque occurrence. Fichiers les plus concernes.
```

### 3 -- Analyser les dependances

```
Liste les dependances du projet [CHEMIN].
Version actuelle vs derniere. Vulnerabilites connues.
```

### 4 -- Trouver du code duplique

```
Identifie le code duplique dans [CHEMIN].
Fichiers concernes, lignes, suggestion de factorisation.
```

### 5 -- Comprendre un flux

```
Explique le flux d'execution de [FONCTIONNALITE] dans [CHEMIN] :
De l'entree utilisateur a la sortie, fichier par fichier.
```

---

## Effet sur le modele
- Codex CLI parcourt les fichiers reels pour une recherche factuelle
- L'execution de grep/find donne des resultats precis
- L'exploration de projets est basee sur le code existant
