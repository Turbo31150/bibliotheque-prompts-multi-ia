# Template CLAUDE.md

> Template de fichier CLAUDE.md pour configurer le comportement de Claude Code dans un projet.

---

## Qu'est-ce que CLAUDE.md ?

Le fichier `CLAUDE.md` est lu automatiquement par Claude Code au demarrage d'une session dans un projet. Il sert de "brief" pour que le modele comprenne instantanement le contexte, les conventions et les contraintes du projet.

### Effet sur le modele
- Le contenu de CLAUDE.md est injecte dans le system prompt
- Il consomme du context window (viser < 3000 tokens)
- Les instructions de CLAUDE.md sont prioritaires sur le comportement par defaut
- Un bon CLAUDE.md reduit de 50-70% les corrections et allers-retours

---

## Template complet

```markdown
# [NOM DU PROJET] v[VERSION] — Project Instructions

## Langue
[Langue de reponse et de code. Ex: Toujours repondre en francais. Code en anglais.]

## Architecture
- **Stack**: [Technologies principales]
- **Runtime**: [Version Python/Node/etc]
- **Structure**: [Nombre de modules, lignes de code]
- **Tests**: [Framework, nombre de tests, couverture]
- **DB**: [Bases de donnees utilisees]

## Conventions Code
- [Langage]: [Conventions specifiques]
- Imports: [Ordre et style]
- Nommage: [snake_case, camelCase, etc]
- Tests: [Comment lancer, convention de nommage]

## Fichiers critiques (ne pas casser)
- `chemin/fichier1.py` — [Role]
- `chemin/fichier2.py` — [Role]
- `chemin/fichier3.js` — [Role]

## Regles
- [Regle 1 : ex. JAMAIS localhost, toujours 127.0.0.1]
- [Regle 2 : ex. Ne pas committer .env, data/*.db]
- [Regle 3 : ex. Type hints obligatoires]

## Scripts utiles
\```bash
[commande1]   # [Description]
[commande2]   # [Description]
[commande3]   # [Description]
\```

## Troubleshooting rapide
| Symptome | Fix |
|----------|-----|
| [Symptome 1] | [Fix 1] |
| [Symptome 2] | [Fix 2] |
```

---

## Exemple reel — JARVIS v15.0

```markdown
# JARVIS Turbo v15.0 — Project Instructions

## Langue
Toujours repondre en francais. Code en anglais, commentaires en francais si pertinent.

## Architecture
- **SDK**: Claude Agent SDK Python v0.1.35 | **Runtime**: uv v0.10.2 + Python 3.13
- **Cluster**: 4 noeuds IA (M1/M1B/M2/M3) + cloud | 10 GPU, 78 GB VRAM
- **Modules**: 246 dans src/ (93K lignes) | **Outils MCP**: 658 handlers
- **Tests**: 2,241 fonctions (77 fichiers) | Couverture src: 85.5%

## Conventions Code
- Python: type hints, async/await, f-strings, dataclasses
- Imports: from __future__ import annotations en premier
- Nommage: snake_case Python, camelCase JS
- Tests: uv run pytest — fichiers test_*.py

## Fichiers critiques (ne pas casser)
- src/config.py — Noeuds cluster, routage, chemins projets
- src/tools.py — Outils MCP (pool httpx partagee)
- src/mcp_server.py — 658 handlers (6282 lignes)

## Regles
- JAMAIS localhost → toujours 127.0.0.1 (IPv6 lag)
- Ollama cloud: think:false OBLIGATOIRE
- GPU: warning 75C, critical 85C → re-routage cascade
- Ne pas committer: data/*.db, .env, credentials, node_modules/
```

---

## Bonnes pratiques

1. **Garder le fichier court** : < 3000 tokens. Le modele lit tout a chaque message
2. **Etre specifique** : "JAMAIS localhost" est mieux que "preferez les IPs"
3. **Lister les fichiers critiques** : Ca empeche le modele de les modifier sans reflexion
4. **Inclure le troubleshooting** : Le modele peut diagnostiquer sans chercher
5. **Mettre a jour regulierement** : Un CLAUDE.md obsolete est pire que pas de CLAUDE.md
6. **Utiliser des tableaux** : Plus compacts que des listes pour les donnees structurees
