# Multi-IA — Consensus Vote

> Prompts pour obtenir un consensus entre plusieurs modeles IA en parallele.

---

## Prompt de consensus standard

```
Lance un consensus multi-modele sur la question suivante :

QUESTION : [POSER LA QUESTION]

## Modeles a interroger
1. Claude (Claude Code) — Modele principal
2. qwen3-8b (M1 local) — Modele local rapide
3. deepseek-r1 (M2 local) — Modele reasoning
4. gpt-oss:120b (OL1 cloud) — Modele cloud

## Instructions pour chaque modele
Reponds a la question avec :
- Ta reponse en 3-5 lignes
- Ton niveau de confiance : 1-10
- Tes reserves ou incertitudes

## Mecanisme de vote
- Unanimite (4/4) : Haute confiance, appliquer directement
- Majorite forte (3/4) : Bonne confiance, verifier le dissent
- Majorite simple (2/4) : Confiance moyenne, investigation supplementaire
- Pas de majorite : Reformuler la question ou decomposer

## Format de sortie
| Modele | Reponse | Confiance | Reserves |
|--------|---------|-----------|----------|
| Claude | ... | ?/10 | ... |
| qwen3-8b | ... | ?/10 | ... |
| deepseek-r1 | ... | ?/10 | ... |
| gpt-oss:120b | ... | ?/10 | ... |
| **CONSENSUS** | **...** | **?/10** | **...** |
```

### Ce que ca fait
Interroge 4 modeles IA en parallele et synthetise un consensus pondere par la confiance de chaque modele.

### Effet sur le modele
- Les modeles repondent independamment (pas d'influence mutuelle)
- La confrontation revele les certitudes et les zones grises
- Le score de confiance pondere le poids de chaque avis
- Le format tableau rend la comparaison instantanee

### Comment l'utiliser

```bash
# Via la commande slash dans Claude Code
/consensus "Quelle base de donnees utiliser pour du time-series a haute frequence ?"

# Via l'API JARVIS
curl -X POST http://127.0.0.1:8000/api/consensus \
  -H "Content-Type: application/json" \
  -d '{"question": "Quelle DB pour du time-series ?", "models": ["claude", "qwen3", "deepseek-r1", "gpt-oss"]}'
```

---

## Prompt de consensus code review

```
Consensus code review sur le fichier [FICHIER].

Chaque modele doit :
1. Lire le code entier
2. Donner un score qualite /10
3. Lister les problemes (CRITICAL/HIGH/MEDIUM/LOW)
4. Proposer des ameliorations
5. Donner son verdict : APPROVE / REQUEST_CHANGES / COMMENT

Synthese :
- Si 3+ APPROVE : code valide
- Si 2+ REQUEST_CHANGES : lister les changements unanimes
- Conflit : montrer les divergences pour decision humaine
```

---

## Prompt de consensus architecture

```
Consensus sur un choix d'architecture :

## Contexte
[DECRIRE LE CONTEXTE]

## Options
A : [OPTION A]
B : [OPTION B]
C : [OPTION C]

## Criteres d'evaluation
| Critere | Poids |
|---------|-------|
| Performance | 30% |
| Maintenabilite | 25% |
| Scalabilite | 20% |
| Complexite | 15% |
| Cout | 10% |

Chaque modele evalue chaque option sur chaque critere (/10).
Score pondere final par modele.
Consensus = option avec le meilleur score moyen pondere.
```

---

## Quand utiliser le consensus

| Situation | Consensus utile ? |
|-----------|-------------------|
| Bug simple et clair | Non — un seul modele suffit |
| Choix d'architecture | Oui — perspectives differentes |
| Code review critique | Oui — reduit les angles morts |
| Question factuelle | Non — verifier la source directement |
| Decision de design | Oui — equilibre creativite et pragmatisme |
| Optimisation performance | Oui — chaque modele a ses heuristiques |

---

## Prerequis
- Cluster IA operationnel (minimum 3 noeuds sur 4)
- Plugin jarvis-turbo actif avec commande `/consensus`
- Les 4 modeles doivent etre charges et accessibles
