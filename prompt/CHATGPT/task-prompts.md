# ChatGPT - Prompts de Taches

## Sommaire

1. [Architecture avant de coder](#1-architecture-avant-de-coder)
2. [Refactor propre](#2-refactor-propre)
3. [Generation de tests](#3-generation-de-tests)
4. [Debug cible](#4-debug-cible)
5. [Optimisation performance](#5-optimisation-performance)
6. [Comparatif technos](#6-comparatif-technos)

---

### 1. Architecture avant de coder

**Contexte** : Concevoir avant d'implementer
**Attente** : Questions, architecture, plan MVP
**Quand** : Nouveau feature, nouveau projet

```text
Tu es un architecte logiciel senior.
Prends ce besoin : "<decris ton besoin ou user story>".

1) Pose-moi 3-5 questions ciblees si quelque chose est flou.
2) Propose une architecture technique claire (modules, data flow, techno).
3) Donne un plan de livraison etape par etape (MVP puis ameliorations).

Format : titres Markdown + listes numerotees.
```

---

### 2. Refactor propre

**Contexte** : Ameliorer du code existant
**Attente** : Problemes listes, code refactore, explications
**Quand** : Dette technique, lisibilite, performance

```text
Tu es un developpeur senior dans ce langage.
Analyse le code suivant et :

1) Liste les problemes de lisibilite, performance et securite.
2) Propose un refactor propre en gardant la meme API publique.
3) Explique en quelques phrases les principaux changements.

Format :
- "Problemes"
- "Nouveau code"
- "Explications"
```

---

### 3. Generation de tests

**Contexte** : Ecrire des tests pour du code existant
**Attente** : Cas limites, tests unitaires, commande de lancement
**Quand** : Avant merge, couverture insuffisante

```text
Agis comme un ingenieur QA.
Pour le code suivant :

1) Identifie les cas limites et scenarios importants.
2) Genere des tests unitaires/integ dans le framework de test utilise.
3) Indique comment executer les tests (commande, options).

Format :
- "Cas a couvrir"
- "Code de test"
- "Commande pour lancer les tests"
```

---

### 4. Debug cible

**Contexte** : Bug specifique a corriger
**Attente** : Hypotheses, correctif minimal
**Quand** : Incident, regression

```text
Tu es expert debug.
Voici le code + le bug observe : "<description du bug>".

1) Propose des hypotheses de causes probables.
2) Dis-moi EXACTEMENT quelles lignes / parties inspecter.
3) Propose un correctif avec explication courte.

Ne change pas le style du projet, reste minimal.
```

---

### 5. Optimisation performance

**Contexte** : Code trop lent
**Attente** : Hotspots, version optimisee, gain estime
**Quand** : Bottleneck detecte

```text
Agis comme un expert performance dans ce langage.
Pour ce code :

1) Identifie les hotspots potentiels (complexite, allocations, I/O).
2) Propose une version optimisee, en gardant la meme signature publique.
3) Explique le gain attendu et les compromis eventuels.

Format : Problemes -> Nouveau code -> Commentaire perf.
```

---

### 6. Comparatif technos

**Contexte** : Choisir entre plusieurs options
**Attente** : Tableau comparatif, recommandation
**Quand** : Decision d'architecture

```text
Tu es architecte technique.
Compare ces options : <liste>.

1) Fais un tableau avec criteres (maturite, perf, ecosysteme, complexite, cout, lock-in).
2) Explique dans quels cas choisir chaque option.
3) Termine par une recommandation pour mon contexte : <decris ton contexte>.
```
