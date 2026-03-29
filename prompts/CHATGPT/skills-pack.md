# ChatGPT Skills Pack — Integration JARVIS

> Derniere mise a jour : 2026-03-28
> Role : noeud de validation, generation et consensus dans le cluster JARVIS

---

## Configuration Cluster

### Noeuds

| Noeud | Machine | Modeles | Endpoint | Poids |
|-------|---------|---------|----------|-------|
| M1 (La Creatrice) | Ryzen 5700X3D, 6 GPUs, 46GB RAM | gemma-3-4b, qwen3.5-9b, deepseek-r1 | localhost:1234 (LM Studio) | 0.40 |
| OL1 | Meme machine (Ollama) | qwen2.5:1.5b, deepseek-r1:7b, kimi-k2.5:cloud | localhost:11434 | 0.15 |
| M2 | Machine secondaire | deepseek-coder | 192.168.1.26:1234 | 0.15 |
| M3 | Machine tertiaire | deepseek-r1-qwen3-8b | 192.168.1.113:1234 | 0.30 |

### Chaine de Fallback

```
M1 (principal) → OL1 (rapide) → M2 (code) → M3 (raisonnement) → GEMINI → CLAUDE
```

Si un noeud est down, le suivant prend le relais automatiquement. Les noeuds cloud (GEMINI, CLAUDE) sont utilises en dernier recours uniquement.

### Ponderation dans le Consensus

| Noeud / IA | Poids |
|-------------|-------|
| CLAUDE | 1.2 |
| CHATGPT | 1.2 (meme classe de poids) |
| GEMINI | 1.0 |
| M1 local | 0.40 |
| M3 | 0.30 |
| OL1 | 0.15 |
| M2 | 0.15 |

---

## Protocole de Consensus

Le consensus est utilise pour les decisions critiques. ChatGPT participe comme votant externe.

### Niveaux de confiance

| Score consensus | Niveau | Action |
|-----------------|--------|--------|
| >= 0.65 | FORT | Reponse validee, execution automatique |
| 0.45 — 0.65 | MOYEN | Reponse acceptee avec avertissement, verification recommandee |
| < 0.45 | FAIBLE | Pas de consensus, escalade vers humain |

### Processus

```
1. Orchestrateur envoie la question a tous les noeuds
2. Chaque noeud repond avec : reponse + score de confiance (0-1)
3. Score final = somme(poids_noeud * confiance_noeud * accord_noeud) / somme(poids)
4. Classification selon les seuils FORT / MOYEN / FAIBLE
5. Si FAIBLE → escalade TTS vers Turbo
```

### Integration ChatGPT

- **Poids** : 1.2 (classe cloud, meme niveau que Claude)
- **Timeout** : 15 secondes (API OpenAI)
- **Mode** : validation + generation (confirme/infirme + propose)
- **Quorum minimum** : 3 votants

---

## 6 Prompts de Taches

Extrait de `CHATGPT/task-prompts.md` :

### 1. Architecture avant de coder
Concevoir avant d'implementer. Questions ciblees, architecture technique, plan MVP.

### 2. Refactor propre
Ameliorer du code existant. Problemes listes, code refactore, explications.

### 3. Generation de tests
Ecrire des tests. Cas limites, tests unitaires, commande de lancement.

### 4. Debug cible
Bug specifique a corriger. Hypotheses, correctif minimal.

### 5. Optimisation performance
Code trop lent. Hotspots, version optimisee, gain estime.

### 6. Comparatif technos
Choisir entre plusieurs options. Tableau comparatif, recommandation.

> Voir `CHATGPT/task-prompts.md` pour les prompts complets.

---

## Points d'Integration

### Via API OpenAI

```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Tu es un validateur dans le cluster JARVIS."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=2000
)
```

### Via Webhook

ChatGPT recoit des taches via webhook configurable dans `core/llm/router.py` :
- Format : JSON avec `task_type`, `complexity`, `prompt`, `context`
- Reponse attendue : JSON avec `response`, `confidence`, `metadata`

### Via copie manuelle

Pour les cas ou l'API n'est pas disponible :
1. Copier le system-prompt depuis `CHATGPT/system-prompts.md`
2. Copier le task-prompt depuis `CHATGPT/task-prompts.md`
3. Coller la reponse dans le canal Redis `jarvis:consensus:response`

---

## Skills ChatGPT dans JARVIS

| Skill | Description | Quand |
|-------|-------------|-------|
| Architecture | Concevoir des systemes, valider des choix techniques | Nouveau projet, nouvelle feature |
| Refactoring | Analyser et proposer des ameliorations de code | Dette technique, code review |
| Brainstorming | Generer des idees, explorer des approches alternatives | Phase exploratoire |
| Documentation | Rediger docs techniques, README, guides | Post-implementation |
| Code review | Relire du code, identifier bugs et mauvaises pratiques | Avant merge, PR review |
| Prompt engineering | Optimiser les prompts pour les IA du cluster | Amelioration continue |

---

## Limites

- ChatGPT **n'execute pas** de code localement (pas d'acces fichiers, pas de shell)
- ChatGPT **ne pilote pas** le navigateur (pas de BrowserOS)
- ChatGPT **ne gere pas** la stabilite systeme (pas de skills securite)
- Son role est **consultatif** : generation, validation, consensus
