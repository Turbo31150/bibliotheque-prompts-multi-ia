# Multi-IA -- Trading

## Description

Prompts pour orchestrer plusieurs IA dans l'analyse de marche et le trading : recherche fondamentale avec Perplexity, analyse technique avec ChatGPT/Gemini, backtesting avec Claude Code, et suivi avec alertes multi-IA.

## Cas d'usage
- Analyse multi-perspectif d'une crypto
- Pipeline de signal : recherche → analyse → decision
- Backtesting avec validation croisee
- Veille marche multi-sources
- Gestion de portfolio assistee par plusieurs IA

---

## Prompts prets a copier

### 1 -- Analyse multi-IA d'une crypto

```
## ETAPE 1 : Perplexity (fondamentale)
Recherche les fondamentaux de [CRYPTO] :
- Actualites recentes, partenariats, roadmap
- Tokenomics et unlock schedule
- Sentiment communautaire
- Comparaison avec les concurrents

## ETAPE 2 : ChatGPT (technique)
Analyse technique de [CRYPTO] sur [TIMEFRAME] :
- RSI, MACD, Bollinger, Volume
- Supports et resistances
- Patterns de chandeliers
- Signal : LONG / SHORT / NEUTRE

## ETAPE 3 : Claude (synthese)
Combine l'analyse fondamentale et technique :
- Convergence ou divergence des signaux
- Score de confiance global (0-100)
- Recommandation finale avec niveaux
- Risques identifies et taille de position recommandee

## ETAPE 4 : Claude Code (backtesting)
Backteste le signal sur les donnees historiques :
- Applique la meme strategie sur les 6 derniers mois
- Win rate, profit factor, max drawdown
- Rapport de validation
```

---

### 2 -- Veille marche multi-sources

```
## Perplexity (actualites)
"Actualites crypto majeures des dernieres 24h : reglementations, hacks, partenariats, releases."

## ChatGPT (analyse sentiment)
"A partir de ces actualites [coller resultat Perplexity], analyse le sentiment marche :
- Impact haussier / baissier par news
- Score de sentiment global
- Cryptos les plus impactees"

## Claude (strategie)
"A partir du sentiment et des actualites, quelles sont les opportunites de trading ?
- Paires a surveiller
- Scenarios probables (24h, 7j)
- Risques a eviter"
```

---

### 3 -- Construction de portfolio multi-IA

```
## Perplexity
"Top 50 cryptos par capitalisation. Pour chacune : capitalisation, variation 30j, TVL si DeFi."

## ChatGPT
"A partir de ces donnees, construis un portfolio diversifie :
- Profil : [RISQUE]
- Capital : [MONTANT]
- Allocation par secteur et par coin"

## Claude
"Revois ce portfolio et :
- Identifie les correlations excessives
- Propose des ajustements de diversification
- Calcule le risque (VaR, max drawdown estime)
- Definis le plan de rebalancing"

## Claude Code
"Cree un script de suivi du portfolio :
- Valeur en temps reel (API CoinGecko)
- Alertes de rebalancing
- Rapport quotidien"
```

---

### 4 -- Validation croisee de signal

```
Signal a valider : [LONG/SHORT] sur [PAIRE] a [PRIX]

## IA 1 : ChatGPT
"Valide ou invalide ce signal technique : [DETAILS]. Analyse RSI, MACD, volume, structure."

## IA 2 : Claude
"Valide ou invalide ce signal. Analyse le risk/reward, les niveaux, le contexte macro."

## IA 3 : Gemini
"Valide ou invalide ce signal. Analyse les metriques on-chain, open interest, funding."

## DECISION
- 3/3 IA valident → execution
- 2/3 IA valident → execution avec taille reduite
- 1/3 ou 0/3 → pas d'execution
```

---

### 5 -- Backtesting multi-strategie

```
## Claude Code (implementation)
Implemente ces 3 strategies en Python :
1. Strategie A : [DESCRIPTION]
2. Strategie B : [DESCRIPTION]
3. Strategie C : [DESCRIPTION]

Backteste sur les memes donnees (BTC/USDT 1h, 6 mois).

## ChatGPT (analyse)
Compare les resultats :
- Metriques par strategie
- Dans quelles conditions chacune performe
- Recommandation de combinaison

## Claude (portfolio de strategies)
Concois un portfolio de strategies :
- Allocation de capital par strategie
- Correlation entre les strategies
- Gestion du drawdown global
```

---

## Exemples d'utilisation

### Exemple : Signal BTC
**Workflow** : Perplexity (news) → ChatGPT (technique) → Claude (synthese) → execution si 2/3 valident

**Resultat attendu** : Signal valide par consensus multi-IA avec confiance et niveaux.

---

## Effet sur le modele
- La validation croisee reduit les faux signaux
- Chaque IA apporte une perspective differente (fondamentale, technique, risque)
- Le consensus multi-IA augmente la confiance dans les decisions
- Le backtesting valide les signaux sur des donnees historiques
