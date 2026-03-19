# Gemini CLI — Demarrage de Session

> Prompts pour demarrer une session productive avec Gemini CLI.

---

## Prompt de demarrage standard

```
@gemini Nouvelle session de travail. Configuration :

## Environnement
- Machine : [NOM] — [CPU] / [GPU] / [RAM]
- OS : Linux [VERSION]
- Projet : [CHEMIN_DU_PROJET]
- Stack : Python 3.13 + uv / Node.js 20 / Docker

## Regles de cette session
- Repondre en francais
- Code en anglais avec commentaires francais
- Type hints obligatoires (Python)
- Tester avant de valider
- Ne pas modifier les fichiers de config sans demander
- Toujours utiliser 127.0.0.1 (jamais localhost)

## Objectif de la session
[DECRIRE L'OBJECTIF]

## Premiere tache
[DECRIRE LA PREMIERE TACHE]

Commence par un audit rapide du projet (git status, structure, tests).
```

### Ce que ca fait
Initialise une session Gemini CLI avec tout le contexte necessaire. Evite les 5-10 premiers messages habituellement perdus en mise en contexte.

### Effet sur le modele
- Les regles de session sont appliquees pendant toute la conversation
- L'audit initial au demarrage donne a Gemini une vision du projet
- L'objectif + premiere tache orientent immediatement l'action

---

## Prompt de demarrage rapide

```
@gemini Session rapide. Projet : ~/jarvis-linux. Python 3.13 + uv.
Francais. Type hints. Tests pytest.
Objectif : [UNE LIGNE]
Go.
```

### Ce que ca fait
Version minimaliste pour les sessions courtes ou les taches simples.

### Quand l'utiliser
- Taches de moins de 30 minutes
- Corrections rapides
- Questions ponctuelles

---

## Prompt de demarrage avec cluster

```
@gemini Session JARVIS. Cluster IA actif :
- M1 (127.0.0.1:1234) : qwen3-8b — 46 tok/s
- M2 (192.168.1.26:1234) : deepseek-r1 — 44 tok/s
- M3 (192.168.1.113:1234) : deepseek-r1 — fallback
- OL1 (127.0.0.1:11434) : gpt-oss:120b-cloud — 51 tok/s

Regles cluster :
- M1 : prefixe /nothink obligatoire pour qwen3
- M2/M3 : max_output_tokens >= 2048
- OL1 cloud : think:false obligatoire
- GPU warning a 75C, critical a 85C

Objectif : [DECRIRE L'OBJECTIF]
```

---

## Prerequis
- Gemini CLI installe et configure
- Cle API Gemini active
- Projet git initialise
