# Multi-IA -- Developpement

## Description

Prompts pour orchestrer plusieurs IA dans le developpement logiciel : specification avec ChatGPT, architecture avec Claude, implementation avec Claude Code, recherche avec Perplexity, et test avec Gemini CLI.

## Cas d'usage
- Cycle de developpement complet multi-IA
- Revue de code multi-perspectif
- Architecture validee par consensus
- TDD avec generation de tests par une IA et code par une autre
- Refactoring avec validation croisee

---

## Prompts prets a copier

### 1 -- Cycle de dev complet multi-IA

```
Feature a developper : [DESCRIPTION]

## ChatGPT (specification)
"Redige la specification fonctionnelle :
- User stories, criteres d'acceptation
- Cas nominaux et cas d'erreur"

## Claude (architecture)
"Concois l'architecture technique :
- Composants, interfaces, schema de donnees
- Diagrammes et ADR"

## Claude Code (implementation)
"Implemente la feature :
- Code, tests, documentation
- Respect de l'architecture definie"

## Gemini CLI (validation)
"Execute les tests. Build. Smoke test.
Rapport de qualite."
```

---

### 2 -- Revue de code multi-perspectif

```
Code a revoir : [COLLER]

## Claude — focus correction et securite
## ChatGPT — focus lisibilite et patterns
## Gemini — focus performance

## Synthese
Bugs unanimes → corriger immediatement
Suggestions majoritaires → implementer
Divergences → discussion humaine
```

---

### 3 -- TDD multi-IA

```
## ETAPE 1 : Claude (tests d'abord)
"Ecris les tests unitaires pour [FONCTIONNALITE].
Cas nominaux, edge cases, erreurs."

## ETAPE 2 : Claude Code (implementation)
"Implemente le code qui fait passer tous les tests.
Aucune modification des tests."

## ETAPE 3 : ChatGPT (revue)
"Revois le code et les tests.
Les tests couvrent-ils tous les cas ?
Le code est-il la solution la plus simple ?"

## ETAPE 4 : Gemini CLI (execution)
"Execute les tests. Tous passent ?
Mesure la couverture."
```

---

### 4 -- Refactoring valide multi-IA

```
Code a refactorer : [CHEMIN]

## Claude Code (refactoring)
"Refactore ce code : decouplage, nommage, duplication."

## ChatGPT (validation)
"Compare avant/apres. Le comportement est-il preserve ?
Le code est-il reellement meilleur ?"

## Gemini CLI (tests)
"Execute les tests existants sur le code refactore.
Aucune regression ?"

## Claude (final)
"Revue finale du refactoring.
Score qualite avant/apres."
```

---

### 5 -- Choix technologique multi-IA

```
Choix a faire : [OPTION A] vs [OPTION B] pour [BESOIN]

## Perplexity
"Benchmarks, adoption, tendances, retours d'experience."

## Claude
"Analyse technique : architecture, scalabilite, compromis."

## ChatGPT
"Experience developpeur : documentation, ecosysteme, courbe d'apprentissage."

## Synthese
Matrice de decision ponderee. Recommandation argumentee.
```

---

## Exemples d'utilisation

### Exemple : Nouvelle feature
**Workflow** : ChatGPT (spec) → Claude (archi) → Claude Code (code) → Gemini CLI (test)

**Resultat attendu** : Feature specifiee, concue, implementee et testee.

---

## Effet sur le modele
- Le cycle multi-IA couvre chaque phase avec l'IA la plus adaptee
- La revue multi-perspectif attrape plus de bugs
- Le TDD multi-IA separe les biais (testeur != developpeur)
- Les choix technologiques sont mieux informes
