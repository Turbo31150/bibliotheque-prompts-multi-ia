# Gemini App -- Trading

## Description

Prompts pour utiliser Gemini App dans l'analyse de marches financiers et crypto : analyse technique, analyse fondamentale, gestion de portfolio et strategies de trading.

## Cas d'usage
- Analyse technique de paires crypto
- Evaluation fondamentale de projets
- Construction et rebalancing de portfolio
- Backtesting conceptuel de strategies
- Veille marche et sentiment analysis

---

## Prompts prets a copier

### 1 -- Analyse technique complete

```
Realise une analyse technique complete de [PAIRE] sur le timeframe [TF] :

## INDICATEURS A ANALYSER
1. Tendance : EMA 20/50/200, direction et croisements
2. Momentum : RSI (14), MACD (12,26,9), Stochastic
3. Volatilite : Bandes de Bollinger (20,2), ATR (14)
4. Volume : OBV, Volume Profile, VWAP
5. Supports/Resistances : 3 niveaux chacun avec methode d'identification

## SIGNAL
- Direction : LONG / SHORT / NEUTRE
- Confiance : 0-100%
- Entree recommandee : [prix]
- Stop loss : [prix] (justification technique)
- Take profit : [TP1, TP2, TP3] (justification)
- Ratio risque/reward
- Invalidation du scenario : [condition]

## CONTEXTE MACRO
- Correlation avec BTC
- Sentiment general du marche
- Evenements a venir (tokenomics, partenariats)
```

---

### 2 -- Evaluer un projet crypto

```
Evalue ce projet crypto pour un investissement potentiel :

## PROJET : [NOM]

## ANALYSE FONDAMENTALE
1. TECHNOLOGIE
   - Probleme resolu et solution proposee
   - Innovation vs existant
   - Stack technique et auditabilite

2. EQUIPE
   - Fondateurs (background, track record)
   - Taille de l'equipe et transparence
   - Advisors notables

3. TOKENOMICS
   - Supply (circulating, total, max)
   - Distribution (team, investisseurs, communaute)
   - Unlock schedule et inflation
   - Utilite du token

4. ECOSYSTEME
   - Partenariats et integrations
   - Activite on-chain (TVL, transactions, adresses actives)
   - Communaute (taille, engagement)

5. RISQUES
   - Concurrents directs
   - Risques reglementaires
   - Risques techniques (hacks, bugs)
   - Centralisation

Score global sur 100 avec recommandation : ACHETER / HOLD / EVITER.
```

---

### 3 -- Construire un portfolio diversifie

```
Construis un portfolio crypto diversifie :

## CAPITAL : [MONTANT]
## PROFIL DE RISQUE : [CONSERVATEUR / MODERE / AGRESSIF]
## HORIZON : [COURT / MOYEN / LONG TERME]

## ALLOCATION DEMANDEE
1. Blue chips (BTC, ETH) : [%]
2. Large caps (top 20) : [%]
3. Mid caps (top 100) : [%]
4. Small caps (conviction plays) : [%]
5. Stablecoins (reserve) : [%]

Pour chaque position :
- Coin et allocation (%)
- Justification (pourquoi celui-ci)
- Zone d'achat ideale
- Stop loss de portfolio (-X% → reduire)
- Objectif de prise de profit

## PLAN DE REBALANCING
- Frequence
- Seuils de deviation declenchant un rebalancing
- Regles de prise de profit partielle
```

---

### 4 -- Analyser le sentiment du marche

```
Analyse le sentiment actuel du marche crypto :

## INDICATEURS A EVALUER
1. Fear & Greed Index (valeur et tendance)
2. Funding rates des perpetuals (positif = greedy, negatif = fearful)
3. Open Interest (augmentation = conviction, diminution = incertitude)
4. Dominance BTC (flight to safety ou altseason)
5. Stablecoin market cap (afflux = buy pressure)
6. Liquidations recentes (montant et direction)
7. Social sentiment (mots-cles trending, engagement)

## CONCLUSION
- Phase du marche : accumulation / markup / distribution / markdown
- Biais directionnel a court terme (1-7 jours)
- Biais directionnel a moyen terme (1-3 mois)
- Risques principaux a surveiller
- Opportunites identifiees
```

---

### 5 -- Backtester une strategie conceptuellement

```
Evalue cette strategie de trading avant implementation :

## STRATEGIE
- Entree : [CONDITIONS]
- Sortie : [CONDITIONS]
- Stop loss : [METHODE]
- Take profit : [METHODE]
- Taille de position : [METHODE]
- Marche : [PAIRE / TYPE]
- Timeframe : [TF]

## EVALUATION DEMANDEE
1. Forces de la strategie
2. Faiblesses et scenarios defavorables
3. Conditions de marche ideales vs defavorables
4. Ameliorations possibles (filtres, confirmations)
5. Estimation du win rate et du ratio R:R
6. Risques de sur-optimisation (overfitting)
7. Gestion du drawdown
8. Correlation avec d'autres strategies (diversification)

## BENCHMARKS
Comparer conceptuellement avec : DCA, Buy & Hold, Mean Reversion.
```

---

## Exemples d'utilisation

### Exemple : Analyse rapide
**Prompt** : "BTC/USDT 4h : RSI 28, MACD croisement haussier, prix sur support 62000. Analyse et signal."

**Resultat attendu** : Analyse avec signal LONG, niveaux d'entree/SL/TP et conditions d'invalidation.

### Exemple : Portfolio
**Prompt** : "J'ai 10000 euros, profil modere, horizon 2 ans. Construis mon portfolio crypto."

**Resultat attendu** : Allocation detaillee avec justifications et plan de gestion.

---

## Effet sur le modele
- Gemini App gere bien l'analyse multi-criteres pour le trading
- Les prompts structures avec indicateurs specifiques evitent les reponses vagues
- Demander des niveaux de prix concrets force des recommandations actionables
- Le format risque/reward explicite produit des strategies plus rigoureuses
