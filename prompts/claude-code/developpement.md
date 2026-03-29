# Claude Code — Prompts de Developpement

> Prompts complets pour la generation de code, le refactoring, le debug et le TDD avec Claude Code.

---

## 1. Generation de Code (Goal/Analysis/Code/Tests)

### Prompt

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

### Ce que ca fait
Force Claude a structurer sa reflexion avant de coder. L'etape ANALYSIS evite les erreurs d'architecture. L'etape TESTS garantit du code testable.

### Effet sur le modele
- La structure en 4 etapes active le mode "chain of thought"
- Le modele produit du code de meilleure qualite quand il analyse d'abord
- Les contraintes explicites (type hints, async) reduisent les allers-retours
- Demander les tests dans le meme prompt evite l'oubli

### Exemple concret

```
Objectif : Creer un module health_aggregator.py qui collecte le status
de 8 composants (cluster, GPU, trading, RAG, voice, BrowserOS, Canvas, n8n)
en parallele avec asyncio, et expose un endpoint /health/full qui retourne
un JSON avec le status global et le detail par composant.
```

---

## 2. Refactoring (Inspect/Problems/Diff)

### Prompt

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

### Ce que ca fait
Organise le refactoring de maniere methodique. L'etape INSPECT empeche les modifications aveugles. La classification par severite priorise l'effort.

### Effet sur le modele
- Le mode INSPECT force une lecture complete avant modification
- La classification CRITICAL/HIGH/MEDIUM/LOW ancre le modele sur les priorites
- La protection des fichiers critiques evite les regressions catastrophiques
- Le format diff est plus precis que "reecris le fichier"

### Prerequis
- Le fichier a refactorer doit etre accessible
- Les tests existants doivent passer avant le refactoring
- `uv run pytest` pour verifier

---

## 3. Debug Systematique (Reproduce/Isolate/Fix/Verify)

### Prompt

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

### Ce que ca fait
Empeche le "shotgun debugging" (modifier du code au hasard). Force l'identification de la cause racine avant toute modification.

### Effet sur le modele
- Le format structure empeche Claude de sauter directement au fix
- L'etape REPRODUCE avec un test ecrit est cruciale — elle ancre le diagnostic
- L'etape ISOLATE force une analyse en profondeur
- L'exigence de "fix minimal" evite le over-engineering

### Exemple concret

```
## BUG REPORT
- Symptome : Le endpoint /health/full retourne 500 au lieu de 200
- Contexte : Quand le noeud M2 est offline
- Logs : "ConnectionError: 192.168.1.26:1234 refused"
```

---

## 4. TDD (Test First / Verify Fail / Implement / Verify Pass)

### Prompt

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

### Ce que ca fait
Applique le cycle Red-Green-Refactor du TDD. Les tests definissent le contrat avant l'implementation.

### Effet sur le modele
- Le TDD force Claude a penser au "quoi" avant le "comment"
- Les tests ecrits en premier sont souvent de meilleure qualite
- Le modele produit du code plus simple quand il doit juste faire passer des tests
- L'etape VERIFY FAIL est cruciale — elle valide que les tests testent bien quelque chose

---

## 5. Code Review Consensus (3 modeles en parallele)

### Prompt

```
Lance une code review consensus sur [FICHIER_OU_PR].

## PROCESSUS
1. Envoie le code a 3 modeles en parallele :
   - Claude (via Claude Code)
   - Modele local M1 qwen3-8b (via /quick-ask)
   - Modele local M2 deepseek-r1 (via /quick-ask)

2. Chaque modele doit produire :
   - Score qualite /10
   - Liste des problemes trouves (classement CRITICAL/HIGH/MEDIUM/LOW)
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

### Ce que ca fait
Utilise le cluster IA local pour obtenir 3 avis independants sur le code. Le consensus reduit les faux positifs et faux negatifs d'une review solo.

### Effet sur le modele
- Le format tableau force une sortie structuree et comparable
- La confrontation des 3 avis revele les angles morts de chaque modele
- Le score numerique rend la decision objectivable
- Le mecanisme de vote 2/3 ou 3/3 automatise la decision

### Comment l'utiliser

```bash
# Dans Claude Code
/consensus "Review le fichier src/health_aggregator.py"

# Ou manuellement
claude "Review ce code en mode consensus multi-modele : [coller le code]"
```

### Prerequis
- Cluster IA operationnel (au moins 2 noeuds sur 4)
- Plugin jarvis-turbo actif
- Commande `/consensus` disponible
