# OpenClaw -- Documentation

## Description

Prompts pour utiliser OpenClaw dans la generation de documentation a partir du code source reel.

## Cas d'usage
- Documentation automatique de code
- Generation de README
- Documentation d'API
- Guides d'utilisation
- Changelogs automatiques

---

## Prompts prets a copier

### 1 -- Documenter un projet complet

```
Documente le projet dans [CHEMIN] :
1. Lis le code source
2. Genere README.md (description, installation, usage)
3. Documente chaque module/fichier public
4. Cree des exemples d'utilisation
5. Genere la documentation d'API si applicable
```

### 2 -- Ajouter des docstrings

```
Ajoute des docstrings a toutes les fonctions publiques dans [CHEMIN] :
- Description
- Parametres avec types
- Valeur de retour
- Exceptions possibles
- Exemple d'utilisation
Ne modifie pas le code, ajoute uniquement la documentation.
```

### 3 -- Generer un changelog depuis git

```
Genere le changelog du projet dans [CHEMIN] :
1. Lis git log depuis le dernier tag
2. Classe les commits par type (feat, fix, docs, etc.)
3. Genere CHANGELOG.md au format Keep a Changelog
4. Suggere le prochain numero de version (semver)
```

### 4 -- Creer un guide d'onboarding

```
Cree un guide d'onboarding pour le projet [CHEMIN] :
1. Analyse la structure du projet
2. Identifie les concepts cles
3. Cree un guide step-by-step pour un nouveau contributeur
4. Inclus les commandes de setup
```

### 5 -- Documenter les configurations

```
Documente toutes les options de configuration dans [CHEMIN] :
Pour chaque variable/option :
- Nom, type, valeur par defaut
- Description
- Exemple d'utilisation
- Impact si non configure
```

---

## Exemples d'utilisation

### Exemple : Doc auto
**Prompt** : "Documente ~/projects/mon-api avec README, API docs et guide de contribution"

**Resultat attendu** : Documentation complete generee depuis le code source reel.

---

## Effet sur le modele
- OpenClaw lit le code reel pour une documentation fidele
- Les docstrings ajoutees sont coherentes avec l'implementation
- Le changelog est genere depuis l'historique git reel
- La documentation reflete l'etat actuel du code, pas une version obsolete
