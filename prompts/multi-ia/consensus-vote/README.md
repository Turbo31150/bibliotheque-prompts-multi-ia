# Multi-IA -- Consensus & Vote

## Description

Prompts pour orchestrer un systeme de vote et de consensus entre plusieurs IA : chaque IA donne son avis, et la decision finale est prise par consensus ou vote majoritaire.

## Cas d'usage
- Decision technique par vote multi-IA
- Validation croisee de diagnostics
- Choix d'architecture par consensus
- Triage de bugs par vote de severite
- Evaluation de risques par consensus

---

## Prompts prets a copier

### 1 -- Vote sur une decision technique

```
Question : [DECISION A PRENDRE]

## VOTE
Soumettre la meme question a 3+ IA :

### Claude
"[QUESTION]. Reponds par A ou B avec justification en 3 lignes."

### ChatGPT
"[QUESTION]. Reponds par A ou B avec justification en 3 lignes."

### Gemini
"[QUESTION]. Reponds par A ou B avec justification en 3 lignes."

## DEPOUILLEMENT
- Unanimite → decision forte, executer
- Majorite (2/3) → decision avec reserve, documenter le desaccord
- Egalite → demander plus de contexte ou arbitrage humain
```

---

### 2 -- Consensus sur un diagnostic

```
Probleme : [DESCRIPTION]

Chaque IA analyse independamment.
Comparer les diagnostics :

- Causes identifiees par 3/3 IA → haute confiance
- Causes identifiees par 2/3 IA → confiance moyenne
- Causes identifiees par 1/3 IA → faible confiance, investiguer

Le diagnostic final combine les causes a haute confiance.
```

---

### 3 -- Evaluation de risques par consensus

```
Risque a evaluer : [DESCRIPTION]

Chaque IA donne :
- Score de probabilite (1-5)
- Score d'impact (1-5)
- Mitigation recommandee

Score final = moyenne des scores.
Mitigation = union des recommandations unanimes.
```

---

### 4 -- Triage de bug par vote

```
Bug : [DESCRIPTION]

Chaque IA attribue :
- Severite : P1 / P2 / P3 / P4
- Composant concerne
- Effort estime

Severite finale = vote majoritaire.
Si aucune majorite, prendre la severite la plus haute.
```

---

### 5 -- Choix d'architecture par deliberation

```
## ROUND 1 : Propositions
Chaque IA propose une architecture pour [BESOIN].

## ROUND 2 : Critique
Chaque IA critique les propositions des autres.

## ROUND 3 : Synthese
Claude synthetise : meilleure architecture en combinant
les points forts de chaque proposition.

## VOTE FINAL
Chaque IA vote pour la proposition synthetisee : ACCEPTE / REFUSE.
```

---

## Exemples d'utilisation

### Exemple : Choix de base de donnees
**Workflow** : Claude (PostgreSQL), ChatGPT (SQLite), Gemini (MongoDB) → deliberation → consensus sur PostgreSQL

**Resultat attendu** : Decision argumentee avec les forces de chaque option considerees.

---

## Effet sur le modele
- Le vote multi-IA reduit le biais d'un seul modele
- Le consensus augmente la confiance dans les decisions
- La deliberation en rounds affine les propositions
- Le desaccord signale les decisions non triviales qui meritent attention
