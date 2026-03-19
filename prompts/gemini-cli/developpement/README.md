# Gemini CLI — Developpement

> Prompts optimises pour la generation de code avec Gemini CLI.

---

## Description

Gemini CLI permet de generer du code directement depuis le terminal, avec acces au filesystem local. Ideal pour la generation de modules, la refactorisation et l'integration dans des workflows de developpement Linux.

## Configuration

- Gemini CLI installe et configure (voir `configuration/`)
- Modele recommande : `gemini-2.5-pro` pour le code complexe
- GEMINI.md avec contraintes de code dans le repertoire du projet

## Prompts par type

### Creation de code
```bash
gemini "Genere un module Python 3.13+ pour [FONCTIONNALITE].

Contraintes :
- Type hints complets
- Async/await pour les I/O
- Docstrings en francais
- Gestion d'erreurs exhaustive
- Logging structure (pas de print)
- Tests unitaires pytest inclus

Format : code principal + fichier de tests + exemple d'utilisation."
```

### Amelioration de code existant
```bash
gemini "Ameliore ce fichier : @src/module.py

Checklist :
- Type hints manquants
- Gestion d'erreurs
- Performance
- Tests
Explique chaque changement."
```

### Generation multi-fichier
```bash
gemini "Genere une architecture complete pour un module [NOM_MODULE] :

Structure :
- src/[module].py — Code principal
- src/[module]_types.py — Types et dataclasses
- tests/test_[module].py — Tests pytest
- [module].md — Documentation rapide

Contenu complet de chaque fichier."
```

### Integration systeme Linux
```bash
gemini "Genere un script Python qui interagit avec le systeme :
- Lecture des metriques CPU/GPU via /proc et nvidia-smi
- Exposition en JSON via un serveur HTTP minimal
- Service systemd pour le demarrage automatique
- Rotation des logs

Inclus : le code Python, le fichier .service, et la commande d'installation."
```

### Debug de code
```bash
gemini "Ce code ne fonctionne pas :

$(cat src/broken_module.py)

Erreur :
$(python src/broken_module.py 2>&1)

Analyse la cause racine et corrige le code."
```

## Exemples concrets

```bash
gemini "Genere un module Python async qui :
1. Monitore les 6 GPUs via nvidia-smi (parse XML)
2. Stocke les metriques en SQLite (async)
3. Expose un endpoint FastAPI /metrics en JSON
4. Alerte via webhook si temp > 80C
Type hints, tests, docstrings francais."
```

```bash
gemini "Convertis ce script bash en Python 3.13+ :

$(cat scripts/backup.sh)

Ajoute : gestion d'erreurs, logging, dry-run mode, type hints."
```

## Effet sur le modele

- Gemini CLI a acces au filesystem — `@fichier` permet de referencer des fichiers locaux directement
- Le contexte 1M tokens permet de charger des projets entiers pour de la refactorisation globale
- Gemini est naturellement verbeux en code — les contraintes explicites (type hints, pas de print) canalisent la sortie
- L'integration terminal permet de piquer la sortie d'erreur directement avec `$(commande 2>&1)`
- Gemini 2.5 Pro est bon en raisonnement code mais peut generer des patterns desuets — specifier la version Python aide
