# Cluster — Routage

## Matrice de Routage

Le routeur JARVIS associe 17 domaines a 6 noeuds du cluster avec un systeme de poids a 5 niveaux.

### Domaines (17)

| # | Domaine | Modele prefere |
|---|---------|----------------|
| 1 | Code (general) | M1 qwen3-coder-30b |
| 2 | Code (review) | M1 qwen3-coder-30b |
| 3 | Debug | M1 qwen3-coder-30b |
| 4 | Raisonnement | M2 DeepSeek-R1 |
| 5 | Mathematiques | M2 DeepSeek-R1 |
| 6 | Logique | M2 DeepSeek-R1 |
| 7 | General | M1 qwen3-8b |
| 8 | Classification | M1 gemma-3-4b |
| 9 | Extraction | M1 gemma-3-4b |
| 10 | Traduction | Gemini |
| 11 | Recherche | Perplexity |
| 12 | Creative | Gemini |
| 13 | Documentation | M1 qwen3.5-9b |
| 14 | Trading | Consensus (multi) |
| 15 | Securite | M1 qwen3-coder-30b |
| 16 | DevOps | M1 qwen3-8b |
| 17 | Embeddings | M1 nomic-embed |

### Noeuds (6)

| Noeud | IP | Specialite |
|-------|----|------------|
| M1 | 192.168.1.20 | GPU principal, multi-modeles |
| M2 | 192.168.1.26 | DeepSeek-R1, raisonnement |
| M3 | Local | Modeles legers |
| OL1 | Local | Ollama, modeles cloud |
| Gemini | Cloud | Google Gemini API |
| Perplexity | Cloud | Recherche web |

## Systeme de Poids a 5 Niveaux

Le score de routage combine 5 facteurs :

1. **Poids du noeud** (0-2.0) : fiabilite et puissance intrinseque
2. **Affinite domaine** (0-1.0) : specialisation du noeud pour le domaine
3. **Latence** (penalite) : -0.1 par 100ms au-dessus de 200ms
4. **Temperature GPU** (penalite) : -0.2 si > 75C, -0.5 si > 85C
5. **Auto-apprentissage** (bonus/malus) : ajustement base sur l'historique de qualite

### Formule

```
score = (poids_noeud * affinite_domaine) - penalite_latence - penalite_temp + bonus_apprentissage
```

Le noeud avec le meilleur score recoit la requete. En cas d'egalite, le noeud avec la temperature GPU la plus basse est prefere.
