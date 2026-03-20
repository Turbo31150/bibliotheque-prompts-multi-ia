# Choisir son modèle — Arbre de décision

Quel modèle utiliser pour quelle tâche ? Ce guide répond en moins de 30 secondes.

---

## Arbre de décision rapide

**La tâche nécessite une réponse immédiate (< 2s) ?**
- OUI → qwen3-8b (65 tok/s, local M1)
- NON → continuer

**La tâche est un raisonnement complexe ou multi-étapes ?**
- OUI → deepseek-r1 (chain-of-thought, 40 tok/s)
- NON → continuer

**La tâche nécessite un contexte très long (> 8K tokens) ?**
- OUI → gpt-oss:120b (contexte 120K, 51 tok/s)
- NON → continuer

**La tâche nécessite des sources vérifiées ou des données récentes ?**
- OUI → Perplexity
- NON → continuer

**La tâche est de l'exécution système ou des tests shell ?**
- OUI → Gemini CLI
- NON → Claude (défaut général)

---

## Tableau de référence complet

| Modèle | Forces | Faiblesses | Vitesse | Coût |
|--------|--------|------------|---------|------|
| **Claude** | Analyse, architecture, rédaction technique, raisonnement | Pas de sources en temps réel | — | API payante |
| **qwen3-8b** | Code, tâches simples, rapidité, /nothink disponible | Contexte limité | 65 tok/s | Local gratuit |
| **deepseek-r1** | Raisonnement, mathématiques, logique, chain-of-thought | Plus lent | 40 tok/s | Local gratuit |
| **gpt-oss:120b** | Contexte très long, précision, synthèse | Plus lourd | 51 tok/s | Local OL1 |
| **ChatGPT** | Documentation, lisibilité, explication pédagogique | Hallucinations possibles | — | API payante |
| **Gemini CLI** | Exécution shell, audit système, tests, commandes | Pas de raisonnement profond | — | API gratuite limitée |
| **Perplexity** | Sources vérifiées, actualité, veille technique | Pas de génération de code | — | Gratuit/payant |

---

## Par type de tâche

### Code
| Sous-tâche | Modèle recommandé | Pourquoi |
|------------|------------------|---------|
| Écrire du code simple | qwen3-8b | Rapide, excellent en code |
| Refactoring complexe | Claude | Compréhension architecturale |
| Debug difficile | Claude + Perplexity | Analyse + sources vérifiées |
| Code review | Claude + ChatGPT + Gemini CLI | Couverture complète |
| Optimisation performance | deepseek-r1 | Raisonnement algorithmique |
| Tests automatisés | Claude Code | Intégration native |

### Architecture et décision
| Sous-tâche | Modèle recommandé | Pourquoi |
|------------|------------------|---------|
| Choix technologique | Consensus 3 modèles | Perspectives différentes |
| Design pattern | Claude | Expertise architecture |
| ADR (Architecture Decision Record) | Claude + ChatGPT | Raisonnement + documentation |
| Évaluation de risques | deepseek-r1 + Claude | Double analyse |

### Recherche et veille
| Sous-tâche | Modèle recommandé | Pourquoi |
|------------|------------------|---------|
| Actualité tech | Perplexity | Sources récentes vérifiées |
| Documentation d'une librairie | Context7 MCP + Claude | Docs à jour |
| Comparaison d'outils | Perplexity + Claude | Recherche + synthèse |
| Veille crypto/trading | Perplexity | Données temps réel |

### Opérations système
| Sous-tâche | Modèle recommandé | Pourquoi |
|------------|------------------|---------|
| Commandes shell | Gemini CLI | Exécution directe |
| Audit système Linux | Gemini CLI | Lecture fichiers système |
| Monitoring | Gemini CLI + Claude | Exécution + analyse |
| Backup et scripts | Claude Code | Génération + tests |

---

## Règles d'or

1. **Une question factuelle simple** = un seul modèle suffit. Le consensus est inutile.
2. **Une décision importante** = minimum 3 modèles en consensus.
3. **Sources et dates critiques** = toujours Perplexity en premier.
4. **Tâche critique en production** = consensus + vérification humaine.
5. **Rapidité prioritaire** = qwen3-8b local, jamais d'API cloud.
6. **/nothink** sur qwen3 = réponse directe sans reasoning visible (plus rapide encore).

---

## Quand NE PAS utiliser le consensus

- Question avec une réponse factuelle unique
- Tâche simple et répétitive
- Quand le temps de réponse est critique
- Quand tous les modèles n'ont pas le même contexte disponible

---

*Retour : [README.md](../README.md) — Étape suivante : [tester-le-cluster.md](tester-le-cluster.md)*
