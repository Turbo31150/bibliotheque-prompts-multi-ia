# Gemini CLI -- Trading

## Description

Prompts pour utiliser Gemini CLI dans l'analyse de marches, le backtesting de strategies, la surveillance de positions et l'automatisation de taches de trading crypto. Gemini CLI offre l'avantage de l'execution directe en terminal avec acces aux fichiers locaux et APIs.

## Cas d'usage
- Analyse technique automatisee depuis le terminal
- Backtesting de strategies avec acces fichiers locaux
- Surveillance de positions via scripts
- Generation de signaux de trading
- Analyse de donnees de marche en CSV/JSON

---

## Prompts prets a copier

### 1 -- Analyser des donnees de marche locales

```
Analyse le fichier CSV de donnees OHLCV dans [CHEMIN] :

1. Calcule les indicateurs techniques :
   - RSI (14 periodes)
   - MACD (12, 26, 9)
   - Bandes de Bollinger (20, 2)
   - Volume moyen vs actuel
   - Support et resistance (3 niveaux chacun)

2. Genere un signal : ACHAT / VENTE / NEUTRE avec score de confiance (0-100)

3. Identifie les patterns de chandeliers sur les 10 dernieres bougies

4. Cree un script Python qui reproduit cette analyse en autonome

Format de sortie : rapport texte + script Python executable.
```

---

### 2 -- Creer un bot de surveillance de prix

```
Cree un script bash qui surveille les prix crypto via l'API CoinGecko :

## FONCTIONNALITES
- Surveiller [LISTE DE CRYPTOS] toutes les [N] minutes
- Alerter quand :
  - Variation > 5% en 1h
  - Prix atteint un seuil configure (support/resistance)
  - Volume anormal (> 2x la moyenne 24h)
- Stocker l'historique dans un fichier SQLite local
- Notification via notify-send (desktop) et script TTS

## CODE
- Pas de dependances lourdes (curl + jq + sqlite3)
- Fichier de configuration pour les seuils
- Logging dans /var/log/crypto-monitor.log
- Lancement via systemd timer
```

---

### 3 -- Backtester une strategie

```
Ecris un script Python de backtesting pour cette strategie :

## STRATEGIE
- Entree LONG : RSI < 30 ET MACD croise positif
- Entree SHORT : RSI > 70 ET MACD croise negatif
- Stop loss : 2% du prix d'entree
- Take profit : 4% du prix d'entree (ratio 1:2)
- Taille position : 10% du capital par trade

## DONNEES
- Fichier CSV : [CHEMIN] (colonnes : date, open, high, low, close, volume)
- Periode : [DATE DEBUT] a [DATE FIN]

## RESULTATS ATTENDUS
- Nombre de trades (gagnants / perdants)
- Win rate (%)
- Profit factor
- Max drawdown (%)
- Sharpe ratio
- Equity curve (sauvegardee en PNG avec matplotlib)
- Liste des trades avec details
```

---

### 4 -- Analyser le carnet d'ordres

```
Cree un script qui recupere et analyse le carnet d'ordres de [PAIRE] sur [EXCHANGE] :

1. Recuperer les donnees via API REST (orderbook depth 100)
2. Calculer :
   - Bid/Ask spread
   - Imbalance ratio (volume bid vs ask)
   - Murs d'ordres (ordres > 5x la taille moyenne)
   - Profondeur cumulee a 1%, 2%, 5% du mid price
3. Detecter les patterns :
   - Spoofing potentiel (ordres qui apparaissent/disparaissent)
   - Accumulation (murs d'achat croissants)
   - Distribution (murs de vente croissants)
4. Sauvegarder le snapshot en JSON avec timestamp
```

---

### 5 -- Generer un rapport de portfolio

```
Analyse mon portfolio crypto depuis ce fichier [CHEMIN] et genere un rapport :

## FORMAT DU FICHIER
CSV avec colonnes : coin, quantity, buy_price, buy_date

## RAPPORT
1. Valeur actuelle de chaque position (prix live via API)
2. P&L par position (absolu et %)
3. P&L total du portfolio
4. Allocation actuelle (% par coin) avec pie chart
5. Correlation entre les positions
6. Risque : exposition par secteur (DeFi, L1, L2, Meme...)
7. Recommandations de rebalancing selon le risque
8. Export du rapport en Markdown
```

---

## Exemples d'utilisation

### Exemple : Scan rapide
**Commande** : `gemini "Analyse BTC/USDT 4h : RSI, MACD, Bollinger. Signal ?"`

**Resultat attendu** : Analyse technique avec signal et niveaux cles, directement dans le terminal.

### Exemple : Backtesting
**Commande** : `gemini "Backteste RSI < 30 achat / RSI > 70 vente sur les donnees dans ~/trading/btc_1h.csv"`

**Resultat attendu** : Resultats de backtesting avec metriques et equity curve.

---

## Effet sur le modele
- Gemini CLI peut lire directement les fichiers CSV locaux pour l'analyse
- Les scripts generes sont executables immediatement dans le terminal
- L'acces au systeme de fichiers permet de sauvegarder les resultats et rapports
- La combinaison avec les APIs crypto (CoinGecko, exchanges) donne des donnees live
