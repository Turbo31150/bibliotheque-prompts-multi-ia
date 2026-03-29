# Codex OpenAI — Refactoring

> Prompts de refactoring optimises pour Codex CLI (OpenAI).

---

## Prompt principal

```
Analyse et refactore le fichier [CHEMIN_DU_FICHIER].

## Etape 1 — Diagnostic
- Compte les lignes par fonction (flag si > 40 lignes)
- Identifie le code duplique (DRY violations)
- Repere les anti-patterns Python :
  - Mutable default arguments
  - Bare except clauses
  - Global state
  - Nested loops > 2 niveaux
  - String concatenation dans des boucles

## Etape 2 — Plan de refactoring
Pour chaque probleme identifie :
- Severite : CRITICAL / HIGH / MEDIUM / LOW
- Effort : S (< 5 min) / M (5-15 min) / L (15-30 min)
- Impact : Performance / Lisibilite / Maintenabilite / Securite

## Etape 3 — Execution
Applique les changements par ordre de severite decroissante.
Pour chaque changement :
- Montre le before/after
- Explique pourquoi
- Confirme que la signature publique n'a pas change (retro-compatible)

## Etape 4 — Verification
- Lance les tests existants
- Confirme zero regression
- Mesure le gain (lignes supprimees, complexite reduite)
```

### Ce que ca fait
Refactoring structure et priorise. Codex est particulierement bon pour detecter les patterns et anti-patterns Python.

### Effet sur le modele
- Codex est optimise pour le code — ce prompt exploite cette force
- La classification severite/effort/impact force une approche methodique
- L'exigence de retro-compatibilite evite les breaking changes

### Exemple concret

```bash
codex "Refactore src/mcp_server.py (6282 lignes).
Objectif : decouper en sous-modules < 500 lignes chacun.
Garder l'API publique identique. Tests doivent passer."
```

---

## Prompt de refactoring cible

```
Refactore uniquement la fonction [NOM_FONCTION] dans [FICHIER].

Probleme actuel : [DECRIRE LE PROBLEME]
Comportement attendu : [DECRIRE LE COMPORTEMENT]

Contraintes :
- Signature identique (memes parametres, meme retour)
- Pas de nouvelle dependance
- Tests existants doivent passer sans modification
```

---

## Prerequis
- Codex CLI installe
- Cle API OpenAI configuree
- Projet avec tests existants
