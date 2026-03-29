# Claude Code — Developpement

## Description
Prompts complets pour la generation de code, le refactoring, le TDD, la code review et l'architecture avec Claude Code. Chaque prompt suit la structure Goal/Analysis/Code/Tests pour maximiser la qualite du code produit.

## Configuration requise
- Claude Code avec plugin `jarvis-turbo` actif
- Python 3.13+ avec `uv` pour les tests (`uv run pytest`)
- Fichier `CLAUDE.md` dans le projet (conventions, fichiers critiques)
- Cluster IA operationnel pour la code review consensus

---

## Prompts par type de tache

### Creation — Generation de code (Goal/Analysis/Code/Tests)

```
Tu es un developpeur senior Python/TypeScript. Je vais te donner un objectif.

Suis ce processus en 4 etapes :

## GOAL
Reformule l'objectif en une phrase claire. Identifie les contraintes.

## ANALYSIS
- Liste les fichiers existants a modifier
- Identifie les dependances
- Propose l'architecture (classes, fonctions, modules)
- Estime la complexite (S/M/L/XL)

## CODE
- Ecris le code complet, fonctionnel, type
- Utilise async/await si IO
- Type hints obligatoires (Python)
- Commentaires en francais si pertinent
- snake_case Python, camelCase JavaScript

## TESTS
- Ecris les tests unitaires correspondants
- Minimum 3 cas : nominal, edge case, erreur
- Utilise pytest (Python) ou jest (JS)
- Vise 90%+ de couverture sur le nouveau code

Objectif : [DECRIRE L'OBJECTIF ICI]
```

**Resultat attendu** : Code complet avec tests, structure analysee, complexite estimee. Le modele produit du code de meilleure qualite quand il analyse avant de coder.

---

### Amelioration / Refactoring (Inspect/Problems/Diff)

```
Analyse le fichier [CHEMIN_DU_FICHIER] et effectue un refactoring complet.

## INSPECT
- Lis le fichier entier
- Identifie le role de chaque fonction/classe
- Note les metriques : nombre de lignes, complexite cyclomatique, couplage

## PROBLEMS
Liste tous les problemes trouves, classes par severite :
- CRITICAL : bugs, failles de securite, data loss
- HIGH : code duplique, fonctions > 50 lignes, couplage fort
- MEDIUM : nommage inconsistant, magic numbers, commentaires obsoletes
- LOW : style, formatting, imports inutilises

## DIFF
Pour chaque probleme HIGH+ :
- Montre le code actuel (old)
- Montre le code propose (new)
- Explique pourquoi c'est mieux
- Confirme que les tests existants passent toujours

Ne touche PAS aux fichiers critiques sans confirmation explicite.
Fichiers critiques : src/config.py, src/tools.py, src/mcp_server.py
```

**Resultat attendu** : Liste priorisee de problemes avec diffs precis. Les fichiers critiques sont proteges.

---

### Debug systematique (Reproduce/Isolate/Fix/Verify)

```
Un bug a ete detecte. Suis ce processus de debug systematique :

## BUG REPORT
- Symptome : [DECRIRE LE SYMPTOME]
- Contexte : [QUAND CA SE PRODUIT]
- Logs/erreur : [COLLER L'ERREUR]

## REPRODUCE
1. Trouve la sequence exacte qui reproduit le bug
2. Ecris un test qui echoue (test_reproduce_bug_XXX)
3. Confirme que le test echoue bien

## ISOLATE
1. Trace l'execution depuis le point d'entree
2. Identifie la ligne exacte qui cause le probleme
3. Explique POURQUOI ca bugge (cause racine, pas le symptome)

## FIX
1. Propose le fix minimal (moins de changements = moins de risque)
2. Applique le fix
3. Explique pourquoi ce fix resout la cause racine

## VERIFY
1. Relance le test de reproduction — il doit passer
2. Relance la suite de tests complete — rien ne doit regresser
3. Verifie manuellement si possible

Ne propose JAMAIS un fix sans avoir identifie la cause racine.
```

**Resultat attendu** : Bug reproduit par un test, cause racine identifiee, fix minimal applique, zero regression.

---

### TDD strict (Red/Green/Refactor)

```
On travaille en TDD strict. Voici la fonctionnalite a implementer :

[DECRIRE LA FONCTIONNALITE]

## ETAPE 1 — WRITE TEST FIRST
Ecris les tests AVANT le code :
- Test du cas nominal (happy path)
- Test des cas limites (edge cases)
- Test des erreurs attendues
- Les tests doivent etre clairs et documenter le comportement attendu

## ETAPE 2 — VERIFY FAIL
Lance les tests avec `uv run pytest [fichier_test] -v`
- Confirme qu'ils echouent tous (RED)
- Si un test passe deja, c'est que le test est mal ecrit — corriger

## ETAPE 3 — IMPLEMENT
Ecris le code minimal pour faire passer les tests :
- Pas de fonctionnalites bonus
- Pas d'optimisation prematuree
- Juste assez pour que les tests passent

## ETAPE 4 — VERIFY PASS
Lance les tests :
- Tous les nouveaux tests passent (GREEN)
- Aucun test existant ne regresse
- Couverture > 90% sur le nouveau code

## ETAPE 5 — REFACTOR (optionnel)
Si le code peut etre ameliore :
- Refactorer en gardant les tests au vert
- Relancer apres chaque modification
```

**Resultat attendu** : Cycle Red-Green-Refactor complet. Les tests definissent le contrat avant l'implementation.

---

### Code Review Consensus (3 modeles en parallele)

```
Lance une code review consensus sur [FICHIER_OU_PR].

## PROCESSUS
1. Envoie le code a 3 modeles en parallele :
   - Claude (via Claude Code)
   - Modele local M1 qwen3-8b (via /quick-ask)
   - Modele local M2 deepseek-r1 (via /quick-ask)

2. Chaque modele doit produire :
   - Score qualite /10
   - Liste des problemes trouves (CRITICAL/HIGH/MEDIUM/LOW)
   - Suggestions d'amelioration
   - Verdict : APPROVE / REQUEST_CHANGES / COMMENT

3. Synthese consensus :
   - Si 3/3 APPROVE : merge automatique
   - Si 2/3 APPROVE : merge avec les commentaires du dissent
   - Si majorite REQUEST_CHANGES : lister les changements requis

## FORMAT DE SORTIE
| Modele | Score | Verdict | Issues |
|--------|-------|---------|--------|
| Claude | ?/10 | ? | ? |
| qwen3-8b | ?/10 | ? | ? |
| deepseek-r1 | ?/10 | ? | ? |
| **Consensus** | **?/10** | **?** | **?** |
```

**Resultat attendu** : 3 avis independants synthetises en un verdict consensus. Le mecanisme de vote 2/3 automatise la decision.

---

### Architecture — Conception de module

```
Concois l'architecture pour [FONCTIONNALITE].

## CONTRAINTES
- Stack : Python 3.13 + uv + Claude Agent SDK
- Pattern : async/await, type hints, dataclasses
- Integration : MCP handlers, FastAPI endpoints
- Tests : pytest, couverture 90%+

## DELIVRABLES
1. Diagramme de composants (texte ASCII)
2. Interfaces publiques (signatures de fonctions)
3. Flux de donnees (entree → traitement → sortie)
4. Points d'integration avec l'existant
5. Estimation de complexite et plan d'implementation
```

---

## Exemples concrets

### Exemple 1 : Generation de code avec Goal/Analysis/Code/Tests

```
Objectif : Creer un module health_aggregator.py qui collecte le status
de 8 composants (cluster, GPU, trading, RAG, voice, BrowserOS, Canvas, n8n)
en parallele avec asyncio, et expose un endpoint /health/full qui retourne
un JSON avec le status global et le detail par composant.
```

**Resultat attendu** :
- GOAL : "Module de health check aggrege asynchrone pour 8 composants"
- ANALYSIS : Liste des fichiers, dependances asyncio/httpx, architecture avec dataclass HealthStatus
- CODE : Module complet ~100-150 lignes avec gather() pour parallelisme
- TESTS : 5+ tests (nominal, 1 composant down, timeout, tous down, reponse partielle)

### Exemple 2 : Code review consensus

```bash
/consensus "Review le fichier src/health_aggregator.py"
```

**Resultat attendu** : Tableau avec scores de 3 modeles, verdict consensus APPROVE ou REQUEST_CHANGES.

---

## Effet sur le modele
- La structure en 4 etapes (Goal/Analysis/Code/Tests) active le mode "chain of thought"
- Le modele produit du code de meilleure qualite quand il analyse avant de coder
- Les contraintes explicites (type hints, async) reduisent les allers-retours
- Demander les tests dans le meme prompt evite l'oubli
- Le format Inspect/Problems/Diff force une lecture complete avant modification
- L'exigence de "fix minimal" en debug evite le over-engineering
- Le TDD force Claude a penser au "quoi" avant le "comment"
- La confrontation de 3 modeles en code review revele les angles morts
