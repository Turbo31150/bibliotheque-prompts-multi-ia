# Gemini App -- Debug

## Description

Prompts pour utiliser Gemini App dans le diagnostic et la resolution de bugs : analyse d'erreurs, tracing, investigation de problemes de performance et resolution de conflits de dependances.

## Cas d'usage
- Analyse de stack traces et messages d'erreur
- Diagnostic de problemes de performance
- Resolution de conflits de dependances
- Debug de problemes d'integration
- Investigation de comportements inattendus

---

## Prompts prets a copier

### 1 -- Analyser une stack trace

```
Analyse cette erreur et propose des solutions :

## STACK TRACE
[COLLER LA STACK TRACE]

## CONTEXTE
- Langage : [LANGAGE]
- Framework : [FRAMEWORK]
- Quand ca arrive : [CONDITIONS DE REPRODUCTION]
- Frequence : [SYSTEMATIQUE / INTERMITTENT]

## ANALYSE DEMANDEE
1. Type d'erreur et signification exacte
2. Ligne probable de la cause racine (pas juste le symptome)
3. Chaine de causalite (comment on arrive a cette erreur)
4. 3 solutions possibles par ordre de probabilite
5. Comment confirmer la cause (tests a ajouter)
6. Comment prevenir la recurrence
```

---

### 2 -- Diagnostiquer un probleme de performance

```
Mon application est lente. Aide-moi a diagnostiquer :

## SYMPTOME
- Temps de reponse : [ACTUEL] vs [ATTENDU]
- Quand : [TOUJOURS / SOUS CHARGE / MOMENTS SPECIFIQUES]
- Depuis : [DATE / EVENEMENT DECLENCHEUR]

## METRIQUES DISPONIBLES
[COLLER CPU, RAM, I/O, RESEAU, PROFILING]

## ANALYSE DEMANDEE
1. Hypotheses par ordre de probabilite
2. Pour chaque hypothese :
   - Comment la confirmer (commande, outil, test)
   - Cause racine probable
   - Correction specifique
3. Checklist de performance generale :
   - [ ] N+1 queries ?
   - [ ] Absence de cache ?
   - [ ] Algorithme O(n2) ?
   - [ ] Fuites memoire ?
   - [ ] Locks/contention ?
   - [ ] I/O bloquant ?
4. Outils de profiling recommandes pour ce langage/framework
```

---

### 3 -- Resoudre un conflit de dependances

```
J'ai un conflit de dependances :

## ERREUR
[COLLER LE MESSAGE D'ERREUR]

## CONTEXTE
- Gestionnaire de paquets : [pip/npm/cargo/apt...]
- Fichier de dependances : [requirements.txt / package.json / ...]
- OS : [VERSION]

## RESOLUTION DEMANDEE
1. Explication du conflit (qui demande quoi, incompatibilite)
2. Arbre de dependances simplifie montrant le conflit
3. Solutions par ordre de preference :
   a. Mise a jour compatible
   b. Pin de version specifique
   c. Remplacement de la dependance
   d. Fork / patch
4. Commandes exactes pour appliquer la solution
5. Test de verification apres resolution
```

---

### 4 -- Debugger un probleme d'integration

```
Deux composants ne communiquent pas correctement :

## COMPOSANT A
- Role : [DESCRIPTION]
- Output attendu : [FORMAT]

## COMPOSANT B
- Role : [DESCRIPTION]
- Input attendu : [FORMAT]

## SYMPTOME
[CE QUI SE PASSE vs CE QUI DEVRAIT SE PASSER]

## DONNEES
[LOGS, REQUETES, REPONSES si disponibles]

## ANALYSE DEMANDEE
1. Verifier le contrat d'interface (A envoie ce que B attend ?)
2. Verifier la connectivite (reseau, ports, auth)
3. Verifier les formats (encoding, serialisation, headers)
4. Verifier le timing (timeouts, race conditions)
5. Proposer un test d'integration minimal pour reproduire
6. Proposer la correction
```

---

### 5 -- Investiguer un comportement intermittent

```
J'ai un bug intermittent qui se produit environ [FREQUENCE] :

## SYMPTOME
[DESCRIPTION DU COMPORTEMENT INATTENDU]

## CE QUE J'AI DEJA VERIFIE
[LISTER LES PISTES EXPLOREES]

## INVESTIGATION DEMANDEE
1. Liste des causes classiques de bugs intermittents :
   - Race conditions
   - Fuites memoire (accumulees au fil du temps)
   - Timeouts reseau
   - Cache expire
   - Ressource partagee non protegee
   - Dependance externe instable

2. Pour chaque cause possible :
   - Comment la confirmer
   - Comment instrumenter le code pour la detecter
   - Comment la corriger

3. Strategie de debugging :
   - Quels logs ajouter
   - Quel outil de tracing utiliser
   - Comment reproduire de maniere fiable

4. Plan de resolution par etapes
```

---

## Exemples d'utilisation

### Exemple : Stack trace Python
**Prompt** : "J'ai TypeError: 'NoneType' object is not iterable a la ligne 42 de mon script. [coller stack trace]"

**Resultat attendu** : Identification de la variable None, cause probable, et correction avec guard clause.

### Exemple : Performance
**Prompt** : "Mon API Flask repond en 5 secondes au lieu de 200ms. CPU a 10%, RAM 30%. Qu'est-ce qui bloque ?"

**Resultat attendu** : Diagnostic oriente I/O ou base de donnees, avec outils de profiling et corrections.

---

## Effet sur le modele
- Gemini App analyse bien les stack traces longues grace a son contexte large
- Les prompts structures par symptome/contexte/analyse produisent des diagnostics methodiques
- Demander des commandes de verification permet de confirmer les hypotheses
- Le format "par ordre de probabilite" donne une demarche de debug efficace
