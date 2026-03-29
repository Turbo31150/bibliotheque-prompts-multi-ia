# ChatGPT — Developpement

> Prompts optimises pour la generation de code avec ChatGPT (GPT-4o).

---

## Description

ChatGPT excelle en generation de code grace a GPT-4o : comprehension multimodale (screenshots, schemas), Code Interpreter pour executer du Python, et web browsing pour verifier les APIs actuelles.

## Configuration

- Modele : GPT-4o (ou GPT-4o avec Code Interpreter actif)
- Custom Instructions orientees dev (voir `configuration/`)
- Activer le web browsing pour verifier la documentation

## Prompts par type

### Creation de code
```
Genere un module Python 3.13+ pour [FONCTIONNALITE].

Contraintes :
- Type hints complets
- Async/await pour les I/O
- Docstrings en francais
- Gestion d'erreurs avec exceptions custom
- Logging structure (pas de print)
- Compatible Linux

Format :
1. Code principal
2. Tests pytest
3. Exemple d'utilisation
```

### Amelioration de code existant
```
Ameliore ce code en appliquant les bonnes pratiques :

[COLLER LE CODE]

Checklist :
- [ ] Type hints manquants
- [ ] Gestion d'erreurs insuffisante
- [ ] Code duplique a factoriser
- [ ] Performance a optimiser
- [ ] Tests manquants

Explique chaque changement.
```

### Debug
```
Ce code produit l'erreur suivante :

Code :
[COLLER LE CODE]

Erreur :
[COLLER L'ERREUR]

Analyse la cause racine et propose un fix.
```

### Documentation
```
Genere la documentation technique pour ce module :

[COLLER LE CODE]

Format :
- Description du module
- API publique (fonctions, classes, parametres)
- Exemples d'utilisation
- Dependances
```

## Exemples concrets

```
Genere un module Python async qui monitore l'utilisation GPU via nvidia-smi,
expose les metriques en JSON via FastAPI, et alerte via webhook si temperature > 80C.
Type hints, tests pytest, docstrings francais.
```

```
Ameliore ce script bash en Python 3.13+ :

#!/bin/bash
for f in /var/log/*.log; do
  if grep -q "ERROR" "$f"; then
    echo "Errors in $f"
    tail -5 "$f"
  fi
done

Ajoute : rotation, filtrage par date, export JSON.
```

## Effet sur le modele

- GPT-4o genere du code verbeux par defaut — les contraintes explicites (type hints, pas de print) canalisent la sortie
- Le Code Interpreter permet de tester le code genere en temps reel
- Le format "code + tests + exemple" force une sortie complete et utilisable
- ChatGPT a tendance a sur-commenter — "docstrings en francais" sans "commentaires inline" reduit le bruit
- Le web browsing permet de verifier les APIs et versions actuelles
