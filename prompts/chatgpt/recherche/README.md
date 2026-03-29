# ChatGPT — Recherche

> Prompts optimises pour la recherche, l'analyse et les syntheses avec ChatGPT.

---

## Description

ChatGPT avec le web browsing permet de faire de la recherche en temps reel, des syntheses de documentation, et des analyses comparatives. Combine avec le Code Interpreter, il peut analyser des datasets et produire des visualisations.

## Configuration

- Modele : GPT-4o
- Web Browsing actif (indispensable pour la recherche)
- Code Interpreter actif (analyse de donnees)

## Prompts par type

### Recherche avec sources
```
Recherche sur : [SUJET]

## Consignes
- Utilise le web browsing pour trouver des informations a jour
- Cite tes sources avec les URLs
- Distingue les faits des opinions
- Date de chaque source

## Format
1. Resume executif (5 lignes max)
2. Analyse detaillee
3. Points cles (bullet points)
4. Sources avec URLs
5. Limites de la recherche
```

### Synthese de documentation
```
Synthetise la documentation officielle de [OUTIL/FRAMEWORK] :

## Focus
- Installation et configuration
- Concepts cles
- API principales
- Patterns recommandes
- Pieges courants (gotchas)

## Format
- Cheatsheet condensee (1 page)
- Exemples de code pour chaque concept
- Liens vers la doc officielle
```

### Analyse comparative
```
Compare [OPTION_A] vs [OPTION_B] vs [OPTION_C] pour [CAS_D_USAGE] :

## Criteres
| Critere | Importance |
|---------|-----------|
| Performance | Haute |
| Facilite | Moyenne |
| Cout | Haute |
| Ecosysteme | Moyenne |
| Maintenance | Haute |

## Format
- Tableau comparatif
- Score /10 par critere
- Recommendation finale
- Sources
```

### Veille technologique
```
Quelles sont les nouveautes majeures de [DOMAINE] ces 3 derniers mois ?

Format :
- Liste chronologique
- Pour chaque element : date, description, impact (FAIBLE/MOYEN/FORT)
- Lien source
- Action recommandee : IGNORER / SURVEILLER / ADOPTER
```

## Exemples concrets

```
Recherche les meilleures pratiques 2026 pour deployer des LLM locaux
sur GPU NVIDIA consumer (RTX 3090/4090).
Frameworks, quantization, benchmarks recents.
Cite tes sources.
```

```
Compare FastAPI vs Litestar vs Django Ninja pour un backend API Python :
- Performance (benchmarks)
- DX (developer experience)
- Ecosysteme et communaute
- Adapte pour un projet avec WebSocket + streaming
```

## Effet sur le modele

- Le web browsing est essentiel — sans lui, les connaissances de ChatGPT sont figees a sa date de cutoff
- "Cite tes sources" force ChatGPT a verifier ses affirmations au lieu d'halluciner
- Le format tableau comparatif produit des analyses plus objectives
- ChatGPT a tendance a etre diplomate dans les comparaisons — "recommendation finale" force un choix
- Pour la veille, specifier "3 derniers mois" evite les informations obsoletes
