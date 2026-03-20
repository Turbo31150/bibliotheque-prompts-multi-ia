# OpenClaw -- Creation

## Description

Prompts pour utiliser OpenClaw dans la creation de projets : generation de code, prototypage rapide et creation d'outils avec un agent IA local autonome.

## Cas d'usage
- Generation de projets complets
- Prototypage rapide avec agent autonome
- Creation d'outils en ligne de commande
- Scaffolding de projets
- Creation de scripts d'automatisation

---

## Prompts prets a copier

### 1 -- Creer un projet complet

```
Cree un projet complet pour [DESCRIPTION] :
- Structure de fichiers
- Code source avec tous les modules
- Tests unitaires
- Fichier de configuration
- README avec usage et installation
- Dockerfile si applicable
```

### 2 -- Prototyper un outil CLI

```
Cree un outil CLI en [LANGAGE] qui fait [DESCRIPTION] :
- Parsing des arguments (argparse / clap / cobra)
- Sous-commandes si applicable
- Help et usage
- Gestion d'erreurs
- Tests
```

### 3 -- Scaffolder un microservice

```
Scaffolde un microservice [FRAMEWORK] avec :
- Endpoint healthcheck
- CRUD basique sur [ENTITE]
- Middleware logging et error handling
- Docker + docker-compose
- Tests d'integration
```

### 4 -- Creer un pipeline de donnees

```
Cree un pipeline de traitement de donnees :
- Input : [FORMAT SOURCE]
- Transformations : [DECRIRE]
- Output : [FORMAT CIBLE]
- Gestion d'erreurs et logging
- Mode dry-run
```

### 5 -- Creer une librairie reutilisable

```
Cree une librairie [LANGAGE] pour [FONCTIONNALITE] :
- API publique claire et documentee
- Types et interfaces
- Tests unitaires (couverture > 80%)
- Exemples d'utilisation
- Publication (PyPI / npm / crates.io)
```

---

## Exemples d'utilisation

### Exemple : CLI rapide
**Prompt** : "Cree une CLI Python qui monitore les GPUs NVIDIA et alerte quand la temperature depasse un seuil"

**Resultat attendu** : Projet complet avec CLI, monitoring et alertes.

---

## Effet sur le modele
- OpenClaw agit comme un agent autonome pour creer des projets entiers
- L'execution locale permet de tester immediatement le code genere
- La creation de projets complets (code + tests + docs) est son point fort
- L'acces au filesystem permet de structurer les projets correctement
