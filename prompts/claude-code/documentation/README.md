# Claude Code — Documentation

## Description
Prompts pour generer de la documentation avec Claude Code : README, CHANGELOG, CONTRIBUTING, documentation API, Swagger/OpenAPI et documentation technique.

## Configuration requise
- Claude Code avec plugin `doc-writer`
- Acces au code source du projet
- `uv run pytest` pour verifier les exemples de code
- Git pour les changelogs bases sur les commits

---

## Prompts par type de tache

### Creation — README de projet complet

```
Genere un README.md complet pour le projet [NOM_PROJET] :

## STRUCTURE
### 1. Titre et badges
- Nom du projet, version, status CI, couverture de tests, licence

### 2. Description
- Ce que fait le projet (1 paragraphe)
- Pourquoi il existe (probleme resolu)
- Pour qui (audience cible)

### 3. Quick Start
- Installation en 3 commandes max
- Premier usage en 1 commande
- Resultat attendu

### 4. Installation detaillee
- Prerequis (OS, runtime, dependances)
- Installation pas a pas
- Configuration initiale
- Verification que tout fonctionne

### 5. Usage
- Exemples par cas d'usage
- Commandes principales avec explications
- Screenshots ou exemples de sortie

### 6. Architecture
- Diagramme des composants (ASCII ou Mermaid)
- Technologies utilisees
- Structure des fichiers

### 7. Configuration
- Variables d'environnement
- Fichiers de configuration
- Options disponibles

### 8. API (si applicable)
- Endpoints principaux
- Exemples de requetes/reponses

### 9. Contribuer
- Comment contribuer (lien vers CONTRIBUTING.md)
- Comment reporter un bug
- Comment proposer une feature

### 10. Licence
- Type de licence

## REGLES
- Exemples de code fonctionnels et testables
- Pas de placeholder generique — utiliser des valeurs realistes
- Ton technique mais accessible
```

---

### Creation — CHANGELOG

```
Genere le CHANGELOG.md base sur l'historique Git :

## FORMAT
Utilise le format Keep a Changelog (https://keepachangelog.com/) :

# Changelog

## [X.Y.Z] - YYYY-MM-DD

### Added
- Nouvelles fonctionnalites

### Changed
- Modifications de fonctionnalites existantes

### Deprecated
- Fonctionnalites qui seront supprimees

### Removed
- Fonctionnalites supprimees

### Fixed
- Corrections de bugs

### Security
- Corrections de vulnerabilites

## PROCESSUS
1. Lis les commits depuis le dernier tag (git log --oneline vX.Y.Z..HEAD)
2. Classe chaque commit dans la bonne categorie
3. Reecris les messages en langage clair (pas de "fix typo", mais "Corrige l'affichage des temperatures GPU")
4. Ajoute les references aux issues/PR quand disponibles
```

---

### Creation — CONTRIBUTING.md

```
Genere un CONTRIBUTING.md pour le projet :

## CONTENU
### 1. Comment contribuer
- Fork + branch + PR
- Convention de nommage des branches (feature/, bugfix/, hotfix/)
- Convention de commit (Conventional Commits)

### 2. Setup de developpement
- Cloner le repo
- Installer les dependances
- Lancer les tests
- Lancer le linter

### 3. Standards de code
- Style guide (ruff pour Python, eslint pour JS)
- Type hints obligatoires
- Tests obligatoires pour tout nouveau code
- Couverture minimum 90%

### 4. Process de review
- Auto-review avant soumission (checklist)
- Review par 1 mainteneur minimum
- CI doit passer (tests + lint)
- Merge par squash

### 5. Reporter un bug
- Template de bug report
- Informations a fournir

### 6. Proposer une feature
- Template de feature request
- Process de discussion
```

---

### Creation — Documentation API (Swagger/OpenAPI)

```
Genere la documentation OpenAPI/Swagger pour l'API JARVIS :

## SPECIFICATION
- Format : OpenAPI 3.0
- Fichier : docs/openapi.yaml

## CONTENU
Pour chaque endpoint :
1. Methode HTTP et path
2. Description claire
3. Parametres (query, path, body) avec types et exemples
4. Schema de requete (si POST/PUT)
5. Schema de reponse (200, 400, 401, 404, 500)
6. Exemples concrets de requetes/reponses
7. Tags pour le groupement

## GROUPES D'ENDPOINTS
- /health/* — Monitoring et sante
- /auth/* — Authentification
- /cluster/* — Gestion du cluster IA
- /trading/* — Operations trading
- /voice/* — Commandes vocales
- /mcp/* — Operations MCP
- /admin/* — Administration

## BONUS
- Ajouter un serveur Swagger UI accessible sur /docs
- Ajouter les schemas de securite (Bearer token)
- Ajouter les exemples curl pour chaque endpoint
```

---

### Amelioration / Refactoring — Mettre a jour la documentation

```
Verifie que la documentation est a jour par rapport au code :

## PROCESSUS
1. Compare les endpoints documentes vs les endpoints dans le code
2. Compare les parametres documentes vs les signatures de fonctions
3. Identifie les fichiers/modules non documentes
4. Identifie les exemples de code obsoletes (qui ne compilent plus)

## FORMAT DE SORTIE
| Element | Documentation | Code | Status |
|---------|--------------|------|--------|
| GET /health | Documente | Existe | OK |
| POST /trading/scan | Non documente | Existe | MISSING |
| GET /legacy/old | Documente | Supprime | OBSOLETE |

## ACTIONS
- MISSING : generer la documentation manquante
- OBSOLETE : supprimer de la documentation
- OUTDATED : mettre a jour avec les valeurs actuelles
```

---

### Debug — Documentation incorrecte

```
La documentation ne correspond pas au comportement reel.

Endpoint : [URL]
Documentation dit : [CE_QUE_LA_DOC_DIT]
Comportement reel : [CE_QUI_SE_PASSE]

## PROCESSUS
1. Lis le code source de l'endpoint
2. Identifie les differences entre doc et code
3. Determine ce qui est correct : la doc ou le code ?
4. Si la doc est fausse : corriger la doc
5. Si le code est faux : corriger le code (bug)
6. Mettre a jour les tests si necessaire
```

---

## Exemples concrets

### Exemple 1 : Generation de README
```bash
claude "/doc README.md pour le module health_aggregator"
```

**Resultat attendu** : README complet avec description, installation, usage, exemples, architecture.

### Exemple 2 : Changelog automatique
```bash
claude "Genere le CHANGELOG depuis le tag v14.0 jusqu'a HEAD"
```

**Resultat attendu** : CHANGELOG formate avec categories Added/Changed/Fixed, messages clairs, references.

### Exemple 3 : Documentation API
```bash
claude "Genere la spec OpenAPI pour tous les endpoints /trading/*"
```

**Resultat attendu** : Fichier YAML OpenAPI 3.0 avec schemas, exemples, codes d'erreur.

---

## Effet sur le modele
- Le template README en 10 sections produit des documentations completes et homogenes
- Le format Keep a Changelog est un standard que le modele connait bien
- L'audit doc vs code detecte les incoherences avant les utilisateurs
- Les exemples concrets dans la documentation reduisent les questions de support
- Le modele produit une meilleure documentation quand il lit d'abord le code source
- La documentation API generee depuis le code est toujours synchronisee
