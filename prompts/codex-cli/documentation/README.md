# Codex CLI -- Documentation

## Description

Prompts pour utiliser OpenAI Codex CLI dans la generation de documentation technique a partir du code source.

## Cas d'usage
- Documentation automatique de code
- Generation de README
- Changelogs automatiques
- Documentation d'API
- Guides d'utilisation

---

## Prompts prets a copier

### 1 -- Documenter un projet

```
Genere la documentation complete du projet [CHEMIN] :
README.md, architecture, API, configuration, troubleshooting.
Base sur le code source reel.
```

### 2 -- Ajouter des commentaires

```
Ajoute des commentaires explicatifs au code dans [CHEMIN].
Description de chaque fonction, parametres, retour.
Ne modifie pas le code, ajoute uniquement les commentaires.
```

### 3 -- Changelog depuis git

```
Genere le changelog du projet [CHEMIN] depuis le dernier tag.
Format Keep a Changelog. Classe par type (feat, fix, docs).
```

### 4 -- Documentation d'API

```
Documente l'API dans [CHEMIN] :
Pour chaque endpoint : methode, URL, params, reponse, exemple curl.
```

### 5 -- Guide de deploiement

```
Cree un guide de deploiement pour le projet [CHEMIN] :
Prerequis, installation, configuration, verification, troubleshooting.
```

---

## Effet sur le modele
- Codex CLI lit le code reel pour une documentation fidele
- Les changelogs sont generes depuis git
- La documentation reflete l'etat actuel du code
