# Gemini App -- Developpement

## Description

Prompts pour utiliser Gemini App (interface web/mobile) dans le developpement logiciel : generation de code, revue, refactoring, architecture et bonnes pratiques. Gemini excelle dans la comprehension de contexte large et la generation de code structure.

## Cas d'usage
- Generation de code a partir de specifications
- Revue de code et suggestions d'amelioration
- Refactoring et modernisation de code legacy
- Conception d'architecture logicielle
- Resolution de problemes algorithmiques

---

## Prompts prets a copier

### 1 -- Generer du code a partir de specs

```
Genere le code complet pour cette fonctionnalite :

## SPECIFICATION
[DECRIRE LA FONCTIONNALITE]

## CONTRAINTES TECHNIQUES
- Langage : [LANGAGE]
- Framework : [FRAMEWORK si applicable]
- Style : [conventions de nommage, formatage]
- Tests : inclure les tests unitaires

## STRUCTURE ATTENDUE
1. Interface/types (si applicable)
2. Implementation principale
3. Gestion d'erreurs
4. Tests unitaires (minimum 5 cas)
5. Documentation (docstrings/commentaires)
6. Exemple d'utilisation

## QUALITE
- Pas de code duplique
- Fonctions courtes (< 30 lignes)
- Nommage explicite
- Gestion de tous les cas limites
```

---

### 2 -- Revue de code detaillee

```
Fais une revue de code approfondie :

[COLLER LE CODE]

## CRITERES D'EVALUATION
1. CORRECTION : bugs, edge cases, erreurs logiques
2. LISIBILITE : nommage, structure, commentaires
3. PERFORMANCE : complexite algorithmique, appels inutiles
4. SECURITE : injections, validation d'entrees, secrets
5. MAINTENABILITE : couplage, cohesion, testabilite
6. IDIOMES : utilisation des patterns du langage

Pour chaque probleme trouve :
- Ligne concernee
- Probleme (description)
- Severite (critique/majeur/mineur/style)
- Correction proposee (code)

Score global sur 10 avec justification.
```

---

### 3 -- Refactorer du code legacy

```
Refactore ce code legacy en code moderne et maintenable :

[COLLER LE CODE LEGACY]

## OBJECTIFS
1. Moderniser la syntaxe (utiliser les features recentes du langage)
2. Extraire les fonctions trop longues
3. Eliminer la duplication
4. Ajouter le typage (si applicable)
5. Ameliorer la gestion d'erreurs
6. Rendre le code testable

## CONTRAINTES
- Meme comportement externe (backward compatible)
- Chaque changement justifie
- Tests de non-regression fournis

## FORMAT
1. Code refactore complet
2. Liste des changements avec justification
3. Avant/apres pour chaque refactoring majeur
4. Tests de validation
```

---

### 4 -- Concevoir une architecture

```
Concois l'architecture pour [PROJET/FONCTIONNALITE] :

## CONTEXTE
- Objectif : [DESCRIPTION]
- Contraintes : [PERFORMANCE, SCALABILITE, etc.]
- Stack existante : [TECHNOLOGIES EN PLACE]
- Equipe : [TAILLE, COMPETENCES]

## DELIVRABLES
1. Diagramme d'architecture (ASCII ou Mermaid)
2. Liste des composants avec responsabilites
3. Interfaces entre composants (API contracts)
4. Schema de la base de donnees (si applicable)
5. Flux de donnees pour les 3 cas d'usage principaux
6. Decisions techniques (ADR format) avec alternatives considerees
7. Plan d'implementation par phases
8. Risques identifies et mitigations
```

---

### 5 -- Resoudre un probleme algorithmique

```
Resous ce probleme algorithmique :

## PROBLEME
[DESCRIPTION DU PROBLEME]

## ENTREES / SORTIES
- Input : [FORMAT ET EXEMPLES]
- Output : [FORMAT ET EXEMPLES]

## SOLUTION DEMANDEE
1. Approche brute force (pour comprendre le probleme)
2. Solution optimisee avec analyse de complexite
3. Implementation dans [LANGAGE]
4. Tests avec cas normaux, limites et adversariaux
5. Explication pas a pas de l'algorithme
6. Variantes du probleme et comment les adapter

## FORMAT
- Complexite temporelle et spatiale pour chaque solution
- Commentaires inline expliquant la logique
```

---

## Exemples d'utilisation

### Exemple : Generation de code
**Prompt** : "Genere un serveur WebSocket en Python qui broadcast les metriques systeme toutes les 5 secondes."

**Resultat attendu** : Code complet avec serveur, collecte de metriques, broadcast et tests.

### Exemple : Revue de code
**Prompt** : "Revue ce script de backup de 150 lignes [coller]. Note-le et propose les corrections."

**Resultat attendu** : Revue structuree avec bugs trouves, ameliorations et code corrige.

---

## Effet sur le modele
- Gemini App gere bien les contextes larges pour les revues de code
- Les specifications structurees produisent du code plus complet
- La demande explicite de tests force la generation de code testable
- Le format ADR pour l'architecture produit des decisions bien documentees
