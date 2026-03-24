# Optimisation Prompts pour Modèles Locaux

> 🔵 Bleu — IA, modèles locaux, optimisation  
> Techniques pour maximiser la qualité avec petits modèles (1.5B-9B)

```text
RÈGLES D'OPTIMISATION POUR MODÈLES LOCAUX:

1. CONCISION: Max 200 tokens pour le system prompt
   - Les petits modèles perdent le contexte sur les longs prompts
   - Aller droit au but

2. STRUCTURE: Utiliser des listes et formats clairs
   - Bullet points > paragraphes
   - JSON output > texte libre
   - Templates avec placeholders

3. EXEMPLES: 1-2 few-shot > instructions longues
   - Montrer le format attendu
   - Exemple input → output

4. CONTRAINTES: Être explicite
   - "Max 3 phrases"
   - "Format JSON uniquement"
   - "Français seulement"
   - "Pas de markdown"

5. TEMPÉRATURE:
   - Code/data: 0.1-0.3
   - Créatif: 0.7-0.9
   - Analyse: 0.3-0.5

6. MODÈLE PAR TÂCHE:
   - gemma-3-4b: bon généraliste, rapide
   - deepseek-r1-7b: raisonnement, code
   - qwen2.5-1.5b: tâches simples, très rapide
   - qwen3-coder-30b: code complexe (si GPU)

TEMPLATE OPTIMISÉ:
Tu es [rôle]. [Tâche en 1 phrase]. Format: [format]. Max [N] mots. FR.
```
