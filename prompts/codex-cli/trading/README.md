# Codex CLI -- Trading

## Description

Prompts pour utiliser OpenAI Codex CLI dans le trading : scripts d'analyse, bots de surveillance et backtesting depuis le terminal.

## Cas d'usage
- Scripts d'analyse technique
- Bots de surveillance de prix
- Backtesting de strategies
- Alertes de marche
- Rapports de portfolio

---

## Prompts prets a copier

### 1 -- Script d'analyse technique

```
Cree un script Python qui analyse [PAIRE] :
- Recupere les donnees OHLCV via API CoinGecko
- Calcule RSI, MACD, Bollinger
- Affiche le signal (LONG/SHORT/NEUTRE)
```

### 2 -- Bot de surveillance

```
Cree un script bash qui surveille le prix de BTC, ETH, SOL :
- Verifie toutes les 5 minutes via CoinGecko API
- Alerte si variation > 5% en 1h
- Log dans ~/trading/prices.csv
```

### 3 -- Backtesting simple

```
Cree un backtest Python pour la strategie :
- Achat quand RSI < 30, vente quand RSI > 70
- Donnees : BTC/USDT 1h sur 6 mois
- Resultat : win rate, profit factor, equity curve
```

### 4 -- Rapport de portfolio

```
A partir du fichier ~/trading/portfolio.csv, genere un rapport :
- Valeur actuelle (prix live)
- P&L par position
- Allocation par coin
```

### 5 -- Alertes de liquidation

```
Surveille les liquidations crypto via API :
- Alerte si liquidation > 10M$ sur un exchange
- Notification desktop
- Log des evenements
```

---

## Effet sur le modele
- Codex CLI cree et execute les scripts de trading directement
- L'acces aux APIs permet des donnees en temps reel
- Les backtests sont executables immediatement
