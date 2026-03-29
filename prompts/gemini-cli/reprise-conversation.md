# Gemini CLI — Reprise de Conversation

> Prompts pour reprendre efficacement une conversation interrompue avec Gemini CLI.

---

## Prompt de reprise

```
@gemini Reprise de session. Voici le contexte :

## Projet
- Nom : [NOM_DU_PROJET]
- Dossier : [CHEMIN]
- Stack : [TECHNOLOGIES]

## Ou j'en etais
- Derniere tache terminee : [DESCRIPTION]
- Tache en cours : [DESCRIPTION]
- Fichiers modifies : [LISTE]
- Problemes en suspens : [LISTE]

## Ce que tu dois faire maintenant
[INSTRUCTION PRECISE]

Commence par verifier l'etat actuel du projet (git status, tests) avant de continuer.
```

### Ce que ca fait
Reinjecte le contexte perdu lors d'une interruption de session. Gemini CLI ne persiste pas le contexte entre sessions.

### Effet sur le modele
- Sans ce prompt, Gemini recommence a zero et peut defaire du travail deja fait
- Le format structure couvre les 4 dimensions essentielles : projet, etat, tache, instruction
- "Commence par verifier" empeche le modele d'agir sur des hypotheses fausses

### Quand l'utiliser
- Apres un crash de terminal
- Apres une pause de plusieurs heures
- Quand on change de machine
- Quand le context window est sature

---

## Prompt de reprise avec diff

```
@gemini Reprise de session. Voici les changements effectues depuis la derniere session :

\```diff
[COLLER LE GIT DIFF ICI]
\```

Ces changements concernent : [DESCRIPTION]
L'objectif final est : [OBJECTIF]
Continue le travail la ou ca s'est arrete.
```

---

## Prompt de reprise avec historique

```
@gemini Voici l'historique des 5 derniers commits :

\```
[GIT LOG --ONELINE -5]
\```

Le dernier commit a fait : [DESCRIPTION]
Le prochain pas est : [INSTRUCTION]
```
