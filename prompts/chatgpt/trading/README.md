# ChatGPT — Trading & Crypto

> Prompts optimises pour l'analyse crypto et trading avec ChatGPT.

---

## Description

ChatGPT avec GPT-4o permet l'analyse de charts crypto (vision), l'analyse technique, la lecture de donnees on-chain et le backtesting de strategies. Sa force : la capacite multimodale (coller des screenshots de charts) et le Code Interpreter pour les calculs.

## Configuration

- Modele : GPT-4o (vision pour les charts)
- Code Interpreter actif (calculs, backtesting)
- Web Browsing actif (donnees marche en temps reel)

## Prompts par type

### Analyse technique de chart
```
[JOINDRE SCREENSHOT DU CHART]

Analyse technique de ce chart :

1. Tendance globale (haussiere/baissiere/range)
2. Supports et resistances cles
3. Indicateurs visibles (RSI, MACD, volumes)
4. Patterns chartistes detectes
5. Probabilite de mouvement (avec justification)

Timeframe : [1H/4H/1D/1W]
Asset : [BTC/ETH/SOL...]
```

### Analyse fondamentale
```
Analyse fondamentale de [CRYPTO] :

1. Utilite du projet (use case reel)
2. Equipe et financement
3. Tokenomics (supply, distribution, inflation)
4. Activite on-chain (TVL, transactions, utilisateurs actifs)
5. Concurrents directs et positionnement
6. Catalyseurs a venir (upgrades, partnerships, listings)

Score global /10 avec justification.
```

### Backtesting de strategie
```
Backteste cette strategie sur [ASSET] :

## Strategie
- Entree : [CONDITION D'ENTREE]
- Sortie : [CONDITION DE SORTIE]
- Stop loss : [%]
- Take profit : [%]

## Parametres
- Periode : [DATE_DEBUT] a [DATE_FIN]
- Timeframe : [1H/4H/1D]
- Capital initial : [MONTANT]

## Metriques attendues
- Win rate
- Profit factor
- Max drawdown
- Sharpe ratio
- Equity curve (graphique)
```

### Analyse de sentiment
```
Analyse le sentiment actuel sur [CRYPTO] :

Sources a considerer :
- Twitter/X (CT — Crypto Twitter)
- Reddit (r/cryptocurrency, r/[coin])
- Fear & Greed Index
- Funding rates
- Open interest

Score sentiment : -10 (extreme fear) a +10 (extreme greed)
Recommendation : WAIT / ACCUMULATE / TAKE_PROFIT
```

## Exemples concrets

```
[SCREENSHOT DU CHART BTC/USDT 4H]

Analyse ce chart BTC/USDT 4H.
Je vois un triangle symetrique avec volume decroissant.
Confirme ou infirme mon analyse.
Quels niveaux surveiller pour un breakout ?
```

```
Backteste une strategie DCA Bitcoin :
- Achat de 100€ chaque lundi a 9h
- Periode : janvier 2023 a mars 2026
- Compare avec un lump sum de la meme somme totale
- Genere les graphiques d'equity curve
```

## Effet sur le modele

- GPT-4o peut analyser des screenshots de charts mais n'est pas un analyste professionnel — toujours croiser avec d'autres sources
- Le Code Interpreter permet des backtests basiques mais limites (pas de donnees live)
- ChatGPT a tendance a etre neutre/conservateur dans ses analyses — le forcer a donner un score chiffre aide
- Le web browsing donne acces a des donnees recentes mais attention aux hallucinations sur les prix exacts
- Ne jamais prendre de decision financiere basee uniquement sur l'analyse d'une IA
