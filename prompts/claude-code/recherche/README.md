# Claude Code — Recherche

## Description
Prompts de recherche avec Claude Code : recherche web intelligente, analyse crypto, veille IA et technologique, recherche RAG dans la base de connaissances locale.

## Configuration requise
- Claude Code avec MCP `rag-mcp` pour la recherche locale
- Plugin `web-researcher` pour la recherche web
- Cluster IA pour le consensus de recherche
- Base de connaissances SQLite FTS5 indexee
- Bot Telegram pour les digests

---

## Prompts par type de tache

### Creation — Recherche technique approfondie

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

---

### Creation — Veille technologique

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

### Creation — Analyse crypto

```
Analyse approfondie de [CRYPTO/TOKEN] :

## FONDAMENTAUX
1. Projet : description, equipe, roadmap
2. Tokenomics : supply, distribution, inflation, utility
3. Technologie : blockchain, consensus, innovations
4. Ecosysteme : DeFi, NFT, partnerships, integrations
5. Communaute : taille, activite, sentiment

## TECHNIQUE
1. Prix actuel et variation 24h/7j/30j
2. Volume et liquidite par exchange
3. Indicateurs techniques (RSI, MACD, Bollinger)
4. Supports et resistances
5. Correlation avec BTC et ETH

## RISQUES
1. Risques reglementaires
2. Risques techniques (smart contract, bridge)
3. Risques de marche (liquidite, concentration)
4. Concurrents directs

## VERDICT
- Score fondamental : /10
- Score technique : /10
- Score risque : /10 (10 = faible risque)
- Recommandation : BUY / HOLD / SELL / AVOID
- Horizon : court terme / moyen terme / long terme
```

---

### Creation — Recherche RAG locale

```
Recherche dans la base de connaissances locale :

Query : [QUESTION]

## PROCESSUS
1. Recherche semantique dans la base SQLite FTS5
2. Retourne les 10 resultats les plus pertinents
3. Pour chaque resultat :
   - Source (fichier, date)
   - Extrait pertinent (200 mots max)
   - Score de pertinence
4. Synthese : reponse a la question basee sur les resultats
5. Si aucun resultat pertinent : le dire explicitement

## FORMAT
| # | Source | Date | Score | Extrait |
|---|--------|------|-------|---------|
| 1 | ... | ... | ... | ... |

## Synthese
[Reponse basee sur les resultats]
```

---

### Creation — Comparaison d'outils

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

### Amelioration / Refactoring — Enrichir la base RAG

```
Enrichis la base de connaissances RAG :

1. Identifie les sources manquantes :
   - Documentation des projets non indexee
   - Conversations Claude Code non sauvegardees
   - Notes et decisions techniques non capturees

2. Indexe les nouvelles sources :
   - Parcours les fichiers .md du projet
   - Extrait les docstrings du code Python
   - Indexe les README des dependances principales

3. Optimise l'index :
   - Supprime les documents obsoletes
   - Met a jour les documents modifies
   - Verifie la qualite de l'indexation (recherches de test)

4. Mesure la qualite :
   - 10 questions de test avec reponses attendues
   - Taux de bonne reponse avant/apres enrichissement
```

---

### Debug — Resultats de recherche non pertinents

```
La recherche RAG retourne des resultats non pertinents.

Query : [LA_QUESTION]
Resultats obtenus : [RESUME_DES_RESULTATS]
Resultats attendus : [CE_QUI_DEVRAIT_ETRE_TROUVE]

## DIAGNOSTIC
1. Le document pertinent est-il dans la base ? (verification)
2. Le document est-il bien indexe ? (verification FTS5)
3. La tokenisation est-elle correcte ? (mots-cles extraits)
4. Le score de pertinence est-il calcule correctement ?
5. Y a-t-il trop de bruit dans l'index ? (documents non pertinents)

## SOLUTIONS
- Document absent : l'ajouter a l'index
- Mauvaise tokenisation : ajuster le tokenizer
- Trop de bruit : filtrer par date/type/source
- Score incorrect : ajuster les poids de ranking
```

---

### Documentation — Rapport de veille

```
Genere le rapport de veille hebdomadaire :

## FORMAT
### Tendances IA
- [Tendance 1 avec source et impact]
- [Tendance 2]
- [Tendance 3]

### Tendances Crypto
- [Tendance 1 avec source et impact]
- [Tendance 2]
- [Tendance 3]

### Outils et releases
| Outil | Version | Date | Impact | Action |
|-------|---------|------|--------|--------|
| ... | ... | ... | FAIBLE/MOYEN/FORT | RIEN/SURVEILLER/ADOPTER |

### Articles a lire
| Titre | Source | Sujet | Priorite |
|-------|--------|-------|----------|
| ... | ... | ... | HAUTE/MOYENNE/BASSE |

### Actions recommandees
1. [Action 1 avec justification]
2. [Action 2]
3. [Action 3]
```

---

## Exemples concrets

### Exemple 1 : Recherche web
```bash
claude "/web-search 'meilleures pratiques MCP servers 2026'"
```

**Resultat attendu** : Digest structure avec les sources recentes, recommendations classees.

### Exemple 2 : Analyse crypto
```bash
claude "Analyse fondamentale et technique de SOL/USDT pour un potentiel investissement"
```

**Resultat attendu** : Rapport complet fondamental + technique + risques avec verdict et recommandation.

### Exemple 3 : Recherche locale RAG
```bash
claude "Cherche dans la base de connaissances comment configurer le thermal guard GPU"
```

**Resultat attendu** : Resultats pertinents de la base locale avec synthese actionnable.

---

## Effet sur le modele
- Le format "recherche technique approfondie" elimine les reponses generiques
- La veille avec classification d'impact (FAIBLE/MOYEN/FORT) priorise l'attention
- L'analyse crypto en 4 axes (fondamentaux/technique/risques/verdict) force une analyse complete
- La recherche RAG locale enrichit les reponses avec le contexte specifique du projet
- La comparaison d'outils avec scores ponderes rend la decision objective et tracable
- Le modele apprend a distinguer les sources fiables des sources generiques
