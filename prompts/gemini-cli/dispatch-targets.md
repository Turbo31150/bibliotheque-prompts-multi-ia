# Gemini CLI — Dispatch & Orchestration

> Prompts pour utiliser Gemini CLI comme agent de dispatch JARVIS.

---

## Prompt — Session JARVIS avec Mega Prompt

```bash
gemini -p "$(cat ~/.gemini/JARVIS_OMEGA_MEGAPROMPT.md)" "Ta requete ici"
```

## Prompt — Publication web via BrowserOS

```bash
gemini -p "Tu es JARVIS Web Publisher. Utilise BrowserOS MCP pour :
1. Ouvrir le tab Codeur.com (cherche dans les tabs CDP 9222)
2. Naviguer vers mon profil /edit
3. Coller ce nouveau pitch : [PITCH]
4. Screenshot avant publication
5. ATTENDRE ma confirmation avant de sauvegarder"
```

## Prompt — Dispatch vers cluster local

```bash
gemini -p "Dispatch cette tache vers M1 (127.0.0.1:1234) :
Requete : [PROMPT]
Flag : /nothink obligatoire
Format retour : JSON
Si M1 echoue, failover vers OL1 (127.0.0.1:11434) avec think:false"
```

## Prompt — Consensus avec validation web

```bash
gemini -p "Pipeline consensus en 3 etapes :
1. Envoie a M1 : [QUESTION]
2. Envoie a OL1 : [QUESTION]
3. Ouvre Perplexity via CDP et envoie : [QUESTION]
4. Compare les 3 reponses, poids M1=1.9 OL1=1.4 Perplexity=1.5
5. Retourne la synthese consensus si score >= 0.65"
```

## Prompt — Lecture de prompts depuis la bibliotheque

```bash
gemini -p "Lis le fichier /home/turbo/IA/Research/bibliotheque-prompts-multi-ia/prompts/[CATEGORIE]/[FICHIER].md et execute le prompt qu'il contient. Adapte les variables entre crochets avec le contexte actuel."
```
