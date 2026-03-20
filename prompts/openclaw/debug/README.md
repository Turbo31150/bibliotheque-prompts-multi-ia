# OpenClaw -- Debug

## Description

Prompts pour utiliser OpenClaw dans le diagnostic et la resolution de bugs avec un agent IA local capable de lire le code, executer des tests et appliquer des corrections.

## Cas d'usage
- Investigation de bugs avec acces au code
- Execution de tests et analyse des echecs
- Application de correctifs automatises
- Analyse de logs locaux
- Debug de configurations

---

## Prompts prets a copier

### 1 -- Investiguer un bug

```
Investigue ce bug dans [CHEMIN] :
Symptome : [DESCRIPTION]
1. Lis le code lie a la fonctionnalite
2. Identifie la cause probable
3. Propose et applique un correctif
4. Execute les tests pour verifier
```

### 2 -- Corriger des tests echoues

```
Les tests echouent dans [CHEMIN] :
1. Execute les tests et lis les erreurs
2. Pour chaque echec : identifie la cause
3. Corrige le code (pas les tests, sauf si le test est faux)
4. Re-execute pour confirmer
```

### 3 -- Analyser des logs d'erreur

```
Analyse les logs dans [FICHIER] :
1. Identifie les erreurs et leur frequence
2. Correle avec le code source
3. Propose des corrections
4. Implementer les corrections les plus urgentes
```

### 4 -- Debug de configuration

```
Le service [NOM] ne demarre pas. Diagnostique :
1. Lis la configuration dans [CHEMIN]
2. Verifie la syntaxe
3. Verifie les valeurs (ports, chemins, credentials)
4. Compare avec la documentation officielle
5. Corrige et teste
```

### 5 -- Regression apres mise a jour

```
Apres la mise a jour de [DEPENDANCE], [FONCTIONNALITE] ne marche plus.
1. Lis le changelog de la mise a jour
2. Identifie les breaking changes
3. Adapte le code
4. Execute les tests
```

---

## Exemples d'utilisation

### Exemple : Fix test
**Prompt** : "3 tests echouent apres mon dernier commit. Diagnostique et corrige."

**Resultat attendu** : Cause identifiee, code corrige, tests qui passent.

---

## Effet sur le modele
- OpenClaw lit le code, diagnostique et corrige en une seule session
- L'execution locale des tests valide les corrections immediatement
- L'agent autonome suit une methodologie de debug structuree
- L'acces au filesystem permet une investigation complete
