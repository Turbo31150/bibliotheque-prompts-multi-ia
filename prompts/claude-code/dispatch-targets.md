# Claude Code — Dispatch & Orchestration Multi-IA

> Utiliser Claude Code comme orchestrateur central pour dispatcher vers toutes les IA.

---

## Prompt — Dispatch vers M1 (LM Studio GPU)

```
Envoie cette requete a M1 via l'API LM Studio :
curl -s -X POST http://127.0.0.1:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek/deepseek-r1-0528-qwen3-8b","messages":[{"role":"user","content":"/nothink [PROMPT]"}],"max_tokens":2048,"stream":false}'
```

## Prompt — Consensus multi-modele

```
Lance un consensus sur cette question : [QUESTION]

1. Envoie a M1 (127.0.0.1:1234) avec /nothink
2. Envoie a OL1 (127.0.0.1:11434) avec think:false
3. Compare les reponses
4. Poids : M1=1.9, OL1=1.4
5. Seuil consensus : score pondere >= 0.65

Synthetise la reponse consensus.
```

## Prompt — Verification via IA web (pattern async)

```
Utilise le navigateur Chrome (CDP 9222) pour :
1. Ouvrir Perplexity dans un tab existant
2. Coller ce contenu : [CONTENU]
3. Memoriser le tab ID
4. Revenir lire la reponse dans 60 secondes
5. Integrer les ameliorations dans le fichier [FICHIER]
```

## Prompt — Pipeline publication verifiee

```
Pipeline de publication en 4 etapes :
1. PREPARER : Lis le fichier [SOURCE] et adapte pour [PLATEFORME]
2. VERIFIER : Envoie a Perplexity/AI Studio pour validation
3. ATTENDRE : 60s puis lire la reponse
4. PUBLIER : Apres confirmation, poster via BrowserOS/CDP

REGLE : JAMAIS publier sans mon OK explicite.
```

## Prompt — Agents paralleles sur toutes les IA

```
Lance ces 3 agents en parallele :

Agent 1 — RECHERCHE (Perplexity via CDP)
- Recherche : [SUJET]
- Memorise le tab

Agent 2 — ANALYSE (M1 local GPU)
- Analyse : [DONNEES]
- Retourne un resume structure

Agent 3 — VALIDATION (Gemini AI Studio via CDP)
- Verifie : [CONTENU]
- Note /10

Synthetise les 3 quand tous ont termine.
```
