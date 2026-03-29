# Perplexity — Recherche

> Prompts optimises pour la recherche en temps reel avec Perplexity AI : citations, fact-checking, veille.

---

## Description

Perplexity est le meilleur outil pour la recherche web en temps reel avec citations. Chaque affirmation est sourcee, les URLs sont verifiables, et le Pro Search permet des recherches multi-etapes approfondies.

## Configuration

- Compte Perplexity (gratuit ou Pro)
- Pro Search recommande pour les recherches complexes
- Focus : Web pour la tech, Academic pour les papers

## Prompts par type

### Recherche technique approfondie
```
Recherche technique approfondie sur : [SUJET]

## Contexte
Je travaille sur un projet [TYPE] avec [STACK].
J'ai besoin de comprendre [ASPECT_SPECIFIQUE].

## Ce que je veux
1. Explication technique detaillee (pas de vulgarisation)
2. Comparaison des approches existantes (minimum 3)
3. Avantages / Inconvenients de chaque approche
4. Recommendation pour mon cas d'usage
5. Sources fiables (documentation officielle, papers, benchmarks)

## Format
- Resume en 3 lignes
- Tableau comparatif
- Code d'exemple pour l'approche recommandee
- Liens vers les sources
```

### Recherche en temps reel
```
Quelles sont les dernieres nouvelles (7 derniers jours) sur [SUJET] ?

Pour chaque element :
- Date exacte
- Source avec URL
- Resume en 2-3 lignes
- Impact : FAIBLE / MOYEN / FORT

Classe par date decroissante.
```

### Fact-checking
```
Verifie cette affirmation :
"[AFFIRMATION]"

1. Verdict : VRAI / FAUX / PARTIELLEMENT VRAI / NON VERIFIABLE
2. Sources qui confirment (avec URLs)
3. Sources qui infirment (avec URLs)
4. Contexte important manquant
5. Niveau de confiance (%)
```

### Comparaison sourcee
```
Compare [A] vs [B] vs [C] pour [USAGE] :

Criteres :
| Critere | Poids |
|---------|-------|
| Performance | 30% |
| Facilite | 20% |
| Documentation | 15% |
| Communaute | 15% |
| Cout | 10% |
| Integration [STACK] | 10% |

Score /10 par critere, score pondere final.
Sources pour chaque affirmation.
Recommendation finale.
```

### Veille technologique
```
Veille technologique : [DOMAINE]

Dernieres avancees (3 derniers mois) :
1. Nouvelles releases majeures
2. Changements breaking ou deprecations
3. Nouveaux outils emergents
4. Benchmarks recents
5. Tendances communaute

Pour chaque element :
- Date + lien source
- Impact : FAIBLE / MOYEN / FORT
- Action : RIEN / SURVEILLER / MIGRER / ADOPTER
```

## Exemples concrets

```
Recherche technique approfondie sur : WebSocket vs SSE vs gRPC streaming

Contexte : systeme de monitoring temps reel (Python/FastAPI)
avec dashboard HTML/JS, metriques toutes les 5 secondes.

Comparaison : latence, overhead, complexite, support Python/navigateur.
Recommendation pour mon cas.
```

```
Quelles sont les dernieres nouvelles sur llama.cpp et l'inference locale
de LLM ? (7 derniers jours)
Focus : nouvelles versions, benchmarks, support GPU NVIDIA.
```

```
Verifie : "vLLM est 3x plus rapide que llama.cpp pour l'inference
de Llama 3 70B sur RTX 4090"
Sources et benchmarks.
```

## Effet sur le modele

- Perplexity cite systematiquement — c'est fiable pour verifier des faits
- Le Pro Search fait 5-10 sous-recherches pour une question complexe — resultat plus complet
- Le focus "Academic" est ideal pour les papers et benchmarks scientifiques
- Les URLs sont generalement valides (contrairement a ChatGPT qui peut halluciner des URLs)
- Pour les comparaisons, demander des "sources pour chaque affirmation" force la rigueur
- Perplexity est moins creatif que ChatGPT/Claude — c'est un outil de recherche, pas de creation
