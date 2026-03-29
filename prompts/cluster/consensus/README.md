# Cluster — Consensus Multi-IA

## Principe

Le systeme de consensus interroge plusieurs modeles IA en parallele et agregue leurs reponses par vote pondere pour obtenir une reponse fiable.

## Poids des Modeles

| Noeud | Modele | Poids | Justification |
|-------|--------|-------|---------------|
| M1 | qwen3-8b / qwen3-coder-30b | **1.8** | GPU puissant, champion local |
| Gemini | Gemini 2.5 Pro | **1.5** | Haute qualite, modele cloud |
| M2 | DeepSeek-R1 | **1.4** | Raisonnement superieur |
| OL1 | Ollama (kimi-k2.5) | **1.3** | Bonne qualite generale |
| M3 | qwen2.5:1.5b | **1.0** | Leger, vote de base |

## Algorithme de Vote

1. La requete est envoyee en parallele aux 5 modeles
2. Chaque reponse recoit un score de confiance (0.0 - 1.0)
3. Le score pondere = confiance x poids du modele
4. Les reponses sont regroupees par similarite semantique
5. Le groupe gagnant doit atteindre le seuil

## Seuil de Consensus

- **Minimum 3 modeles** doivent converger vers la meme reponse
- **Confiance ponderee > 0.7** pour valider le consensus
- Si le seuil n'est pas atteint : escalade vers un modele superieur ou notification utilisateur

## Exemple Reel

**Question** : "Quel est le meilleur framework Python async ?"

| Modele | Reponse | Confiance | Poids | Score |
|--------|---------|-----------|-------|-------|
| M1 (qwen3-8b) | FastAPI + asyncio | 0.92 | 1.8 | 1.656 |
| Gemini | FastAPI | 0.88 | 1.5 | 1.320 |
| M2 (DeepSeek-R1) | FastAPI + uvicorn | 0.95 | 1.4 | 1.330 |
| OL1 (kimi) | FastAPI | 0.85 | 1.3 | 1.105 |
| M3 (qwen2.5) | Flask async | 0.60 | 1.0 | 0.600 |

**Resultat** : 4/5 convergent vers FastAPI. Score pondere total = 5.411. Consensus valide.

## Cas de Non-Consensus

Si les reponses divergent significativement :
1. Log le desaccord dans la base de feedback
2. Retourne la reponse du modele avec le meilleur score individuel
3. Ajoute un disclaimer : "Reponse sans consensus — confiance moderee"
