# DeepSeek R1 -- Inference

## Description

Prompts optimises pour l'inference avec DeepSeek R1, tirant parti de ses capacites de raisonnement.

## Prompts optimises

### 1 -- Raisonnement complexe

```
Resous ce probleme en montrant ton raisonnement :

[PROBLEME]

Pense etape par etape. Verifie ta reponse.
```

### 2 -- Debug de code

```
Ce code a un bug. Trouve-le et corrige-le :

[CODE]

Explique :
1. Quel est le bug
2. Pourquoi il se produit
3. La correction
4. Un test pour verifier
```

### 3 -- Architecture logicielle

```
Concois l'architecture pour [BESOIN] :
1. Analyse les contraintes
2. Evalue les options
3. Choisis la meilleure approche
4. Justifie le choix
5. Identifie les risques

Format ADR (Architecture Decision Record).
```

### 4 -- Optimisation algorithmique

```
Cet algorithme est en O(n^2). Optimise-le :

[CODE]

Montre :
1. Pourquoi c'est O(n^2)
2. L'approche optimisee
3. La complexite de la nouvelle version
4. Le code optimise avec preuves
```

### 5 -- Analyse de securite

```
Analyse ce code pour les vulnerabilites de securite :

[CODE]

Pour chaque vulnerabilite :
- Type (CWE)
- Severite (CVSS)
- Exploitation possible
- Correction
```

---

## Parametres recommandes
| Cas d'usage | Temperature | Think | Num-ctx |
|-------------|-------------|-------|---------|
| Raisonnement | 0.1 | Oui | 8192 |
| Code | 0.0 | Oui | 4096 |
| Analyse | 0.1 | Oui | 8192 |
| Chat rapide | 0.3 | Non | 2048 |
