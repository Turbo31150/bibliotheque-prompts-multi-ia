# Multi-IA -- Debug

## Description

Prompts pour orchestrer plusieurs IA dans le diagnostic et la resolution de bugs : analyse par Claude, recherche par Perplexity, execution par Gemini CLI, et validation croisee.

## Cas d'usage
- Diagnostic multi-perspectif d'un bug
- Recherche de solutions avec validation croisee
- Debug interactif avec plusieurs IA
- Post-mortem de bugs complexes
- Tests de non-regression multi-IA

---

## Prompts prets a copier

### 1 -- Diagnostic multi-IA d'un bug

```
Bug : [DESCRIPTION]
Erreur : [MESSAGE D'ERREUR]

## Claude (analyse)
"Analyse cette erreur. Identifie les causes probables (top 3).
Pour chaque cause : explication, verification, correction."

## ChatGPT (diagnostic alternatif)
"Analyse cette meme erreur independamment.
Propose 3 hypotheses differentes avec plan de verification."

## Perplexity (recherche)
"Recherche cette erreur exacte : [MESSAGE].
Solutions verifiees sur Stack Overflow, GitHub Issues, forums."

## Synthese
- Causes identifiees par les 3 IA → haute priorite
- Solutions avec sources verifiees → appliquer en premier
- Hypotheses uniques → tester si les solutions courantes echouent
```

---

### 2 -- Debug interactif multi-IA

```
## ROUND 1 : Identification
Gemini CLI : execute les commandes de diagnostic
Claude : analyse les resultats, propose des hypotheses
Perplexity : recherche les problemes similaires documentes

## ROUND 2 : Investigation
Gemini CLI : execute les tests d'hypotheses (commandes suggerees par Claude)
Claude : analyse les nouveaux resultats, affine le diagnostic
ChatGPT : propose des angles d'investigation alternatifs

## ROUND 3 : Correction
Claude Code : implemente la correction
Gemini CLI : teste la correction
Claude : valide que la correction ne cree pas de regression

Repeter jusqu'a resolution.
```

---

### 3 -- Post-mortem de bug complexe

```
## Gemini CLI
Collecte les artefacts :
- Logs avant/pendant/apres le bug
- Git blame des fichiers concernes
- Diff avec la derniere version stable

## Claude
Redige le post-mortem technique :
- Timeline de l'apparition du bug
- Cause racine (analyse 5 Whys)
- Impact (qui est affecte, depuis quand)

## Perplexity
Recherche :
- Ce bug existe-t-il dans d'autres projets ?
- Est-ce un probleme de la librairie sous-jacente ?
- Meilleures pratiques pour eviter ce type de bug

## ChatGPT
Redige les actions preventives :
- Tests a ajouter
- Monitoring a configurer
- Documentation a mettre a jour
```

---

### 4 -- Validation croisee de correctif

```
Correctif propose : [DIFF / DESCRIPTION]

## Claude
"Ce correctif resout-il le probleme sans effets de bord ?
Analyse : correction, securite, performance, maintenabilite."

## ChatGPT
"Ce correctif est-il la meilleure approche ?
Y a-t-il une solution plus elegante ou plus robuste ?"

## Gemini CLI
"Applique le correctif, execute les tests, verifie le resultat.
Rapport : tests passes, echecs, regressions."

## Decision
- 3/3 valident → merger
- 2/3 → merger avec suivi
- 1/3 ou moins → reprendre le correctif
```

---

### 5 -- Analyse de performance multi-IA

```
Probleme de performance : [DESCRIPTION]

## Gemini CLI (metriques)
Profile l'application :
- CPU, RAM, I/O par processus
- Flame graph si applicable
- Requetes lentes (DB, API)

## Claude (analyse)
Analyse le profil :
- Goulot d'etranglement identifie
- Cause racine (algorithme, I/O, concurrence)
- Optimisations specifiques

## ChatGPT (alternatives)
Propose des approches d'optimisation :
- Caching
- Parallelisation
- Algorithme alternatif
- Architecture differente

## Perplexity (benchmarks)
Recherche des benchmarks et comparaisons :
- Performance attendue pour cette stack
- Optimisations documentees par d'autres
```

---

## Exemples d'utilisation

### Exemple : Bug Python
**Workflow** : Claude (analyse) + ChatGPT (analyse) + Perplexity (recherche) → synthese → Gemini CLI (correction + test)

**Resultat attendu** : Bug diagnostique par consensus, corrige et teste.

---

## Effet sur le modele
- Le diagnostic multi-IA couvre plus d'hypotheses qu'une seule IA
- La recherche Perplexity valide les solutions avec des sources
- L'execution par Gemini CLI teste les corrections dans le contexte reel
- La validation croisee du correctif previent les regressions
