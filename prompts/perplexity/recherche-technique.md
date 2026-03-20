# Perplexity — Recherche Technique

> Prompts optimises pour la recherche technique avec Perplexity AI.

---

## Prompt de recherche technique approfondie

```
Recherche technique approfondie sur : [SUJET]

## Contexte
Je travaille sur un projet [TYPE_PROJET] avec [STACK].
J'ai besoin de comprendre [ASPECT_SPECIFIQUE].

## Ce que je veux
1. Explication technique detaillee (pas de vulgarisation grand public)
2. Comparaison des approches existantes (minimum 3)
3. Avantages / Inconvenients de chaque approche
4. Recommendation pour mon cas d'usage
5. Sources fiables (documentation officielle, papers, benchmarks)

## Format attendu
- Resume en 3 lignes
- Tableau comparatif des approches
- Code d'exemple pour l'approche recommandee
- Liens vers les sources
```

### Ce que ca fait
Force Perplexity a produire une recherche structuree et sourcee, pas une reponse generique.

### Effet sur le modele
- Perplexity excelle quand on demande des sources — ce prompt exploite cette force
- Le format tableau comparatif force une analyse objective
- Demander "pas de vulgarisation" eleve le niveau technique de la reponse
- Le contexte projet oriente la recommendation

### Exemple concret

```
Recherche technique approfondie sur : WebSocket vs Server-Sent Events vs gRPC streaming

Contexte : Je travaille sur un systeme de monitoring temps reel (JARVIS)
avec Python/FastAPI backend et un dashboard HTML/JS.
J'ai besoin de pousser des metriques toutes les 5 secondes vers le client.

Ce que je veux :
1. Comparaison technique (latence, overhead, complexite)
2. Support Python (bibliotheques)
3. Support navigateur
4. Recommendation pour mon cas
```

---

## Prompt de veille technologique

```
Veille technologique : [DOMAINE]

Quelles sont les dernieres avancees (3 derniers mois) dans [DOMAINE] ?

Couvre :
1. Nouvelles releases majeures (versions, features)
2. Changements breaking ou deprecations
3. Nouveaux outils/frameworks emergents
4. Benchmarks recents
5. Tendances de la communaute (GitHub stars, npm downloads)

Pour chaque element :
- Date de publication
- Lien source
- Impact estime : FAIBLE / MOYEN / FORT
- Action requise : RIEN / SURVEILLER / MIGRER / ADOPTER
```

---

## Prompt de comparaison d'outils

```
Compare ces outils pour [CAS_D_USAGE] :
- [OUTIL_1]
- [OUTIL_2]
- [OUTIL_3]

Criteres de comparaison :
| Critere | Poids |
|---------|-------|
| Performance | 30% |
| Facilite d'utilisation | 20% |
| Documentation | 15% |
| Communaute / support | 15% |
| Cout | 10% |
| Integration avec [STACK] | 10% |

Donne un score /10 par critere et un score pondere final.
Recommandation finale avec justification.
```

---

## Prerequis
- Compte Perplexity (gratuit ou Pro)
- Pour les recherches techniques avancees, Perplexity Pro est recommande (acces aux modeles avances)
