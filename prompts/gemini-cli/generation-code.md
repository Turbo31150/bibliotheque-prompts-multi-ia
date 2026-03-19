# Gemini CLI — Generation de Code

> Prompts optimises pour la generation de code avec Gemini CLI (gemini-cli).

---

## Prompt principal

```
@gemini Tu es un generateur de code expert. Genere du code Python 3.13+ pour :

[DECRIRE LA FONCTIONNALITE]

Contraintes :
- Type hints obligatoires
- Async/await si I/O
- Docstrings en francais
- Tests unitaires inclus
- Gestion d'erreurs exhaustive
- Logging structure (pas de print)

Format de sortie :
1. Code principal dans un seul fichier
2. Tests dans un fichier separe
3. Exemple d'utilisation en commentaire

Utilise les bonnes pratiques Python modernes : dataclasses, pathlib, f-strings.
```

### Ce que ca fait
Gemini CLI genere du code directement dans le terminal. Le prompt structutre force une sortie propre et testable.

### Effet sur le modele
- Gemini est naturellement verbeux — les contraintes explicites canalisent la sortie
- Le format "fichier principal + tests + exemple" evite le code non testable
- Les type hints et async/await doivent etre demandes explicitement avec Gemini

### Exemple concret

```bash
gemini "Genere un module Python async qui monitore les temperatures GPU via nvidia-smi,
alerte si > 75C, et expose les metriques en JSON. Type hints, tests inclus."
```

### Prerequis
- Gemini CLI installe (`npm install -g @anthropic-ai/gemini-cli` ou equivalent)
- Cle API Gemini configuree (`GEMINI_API_KEY`)

---

## Prompt pour generation multi-fichier

```
@gemini Genere une architecture complete pour un module [NOM_MODULE] :

Structure attendue :
- src/[module].py — Code principal
- src/[module]_types.py — Types et dataclasses
- tests/test_[module].py — Tests pytest
- [module].md — Documentation rapide

Specifie chaque fichier avec son chemin et son contenu complet.
```

---

## Prompt pour conversion TypeScript vers Python

```
@gemini Convertis ce code TypeScript en Python 3.13+ :

[COLLER LE CODE TS]

Regles de conversion :
- interface → dataclass
- Promise → async/await
- const/let → typage explicite
- try/catch → try/except avec types d'exception specifiques
- console.log → logging.info
```
