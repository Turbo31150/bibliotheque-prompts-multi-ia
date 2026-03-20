# Claude Code — Trading

## Description
Pipeline de trading crypto avec Claude Code : scan multi-exchange (MEXC, CoinEx), vote consensus multi-modele, execution de trades, suivi PnL et feedback loop pour amelioration continue.

## Configuration requise
- Claude Code avec plugin `trading-scanner` actif
- Cles API MEXC et CoinEx configurees dans `.env`
- Cluster IA operationnel pour le consensus (minimum 3 noeuds)
- Bot Telegram pour les alertes trading
- Base de donnees SQLite pour l'historique des trades

---

## Prompts par type de tache

### Creation — Scanner de marche

```
Lance un scan complet du marche crypto :

## PARAMETRES
- Exchanges : MEXC, CoinEx
- Paires : toutes les paires USDT avec volume > $100k/24h
- Timeframes : 15m, 1h, 4h, 1d
- Indicateurs : RSI, MACD, Bollinger, Volume Profile

## ANALYSE
Pour chaque paire detectee :
1. Signal technique (BUY/SELL/NEUTRAL) par timeframe
2. Force du signal (1-10)
3. Support et resistance proches
4. Volume relatif (vs moyenne 20 jours)
5. Correlation avec BTC

## SORTIE
Tableau trie par force de signal decroissante :
| Paire | Exchange | Signal | Force | RSI | Volume | Correlation BTC |
|-------|----------|--------|-------|-----|--------|----------------|

Top 5 opportunites avec explication detaillee.
```

---

### Creation — Vote consensus trading

```
Lance un consensus trading sur [PAIRE] :

## PROCESSUS
1. Envoie l'analyse de [PAIRE] a 3 modeles en parallele :
   - Claude (analyse fondamentale + technique)
   - qwen3-8b (analyse technique pure)
   - deepseek-r1 (analyse quantitative)

2. Chaque modele doit produire :
   - Direction : LONG / SHORT / NEUTRAL
   - Confiance : 0-100%
   - Prix d'entree suggere
   - Stop loss
   - Take profit (TP1, TP2, TP3)
   - Ratio risque/reward
   - Horizon temporel

3. Synthese consensus :
   - Si 3/3 meme direction avec confiance > 70% : signal fort
   - Si 2/3 meme direction : signal modere
   - Si pas de consensus : pas de trade

## FORMAT
| Modele | Direction | Confiance | Entree | SL | TP1 | TP2 | R:R |
|--------|-----------|-----------|--------|----|-----|-----|-----|
```

---

### Creation — Execution de trade

```
Execute un trade sur [EXCHANGE] :

## PARAMETRES
- Paire : [PAIRE]
- Direction : [LONG/SHORT]
- Taille : [MONTANT USDT]
- Prix d'entree : [PRIX ou MARKET]
- Stop loss : [PRIX]
- Take profit : [TP1], [TP2], [TP3]
- Repartition TP : 33% / 33% / 34%

## PROCESSUS
1. Verifie le solde disponible sur [EXCHANGE]
2. Calcule la taille de position exacte
3. Place l'ordre d'entree
4. Place le stop loss
5. Place les 3 take profits
6. Envoie une notification Telegram avec le resume
7. Enregistre le trade dans la base de donnees

## SECURITE
- Ne jamais risquer plus de 2% du portefeuille par trade
- Verifier que le spread est < 0.1%
- Verifier que le volume 24h est suffisant (> $100k)
- Confirmer avec l'utilisateur avant execution
```

---

### Amelioration / Refactoring — Analyse PnL

```
Analyse le PnL des trades des [N] derniers jours :

## METRIQUES
1. PnL total (USDT et %)
2. Win rate (%)
3. Ratio gain moyen / perte moyenne
4. Profit factor
5. Max drawdown
6. Sharpe ratio

## ANALYSE PAR CATEGORIE
- Par exchange (MEXC vs CoinEx)
- Par paire
- Par timeframe
- Par force de signal consensus
- Par jour de la semaine
- Par heure du jour

## INSIGHTS
- Quels patterns gagnants se repetent ?
- Quels patterns perdants eviter ?
- Les consensus 3/3 performent-ils mieux que les 2/3 ?
- Recommandations pour ameliorer la strategie

## FORMAT
Tableaux + resume executif en 5 points.
```

---

### Debug — Trade qui a mal tourne

```
Analyse ce trade perdant et identifie ce qui a mal tourne :

Trade : [DETAILS DU TRADE]
Resultat : [PERTE EN USDT ET %]

## ANALYSE POST-MORTEM
1. Le signal etait-il correct au moment de l'entree ?
2. Le stop loss etait-il bien place ?
3. Y a-t-il eu un evenement externe (news, whale, manipulation) ?
4. Le consensus etait-il fort (3/3) ou faible (2/3) ?
5. Le timing etait-il bon (heure, jour) ?

## LECONS
- Qu'est-ce qui aurait du declencher un alerte ?
- Comment eviter ce type de perte a l'avenir ?
- Faut-il ajuster les parametres du scanner ?
```

---

### Documentation — Rapport trading hebdomadaire

```
Genere le rapport trading hebdomadaire :

## FORMAT
### Resume executif
- PnL total de la semaine
- Nombre de trades (wins/losses)
- Meilleur trade / Pire trade

### Detail par jour
| Jour | Trades | Wins | Losses | PnL | Cumul |
|------|--------|------|--------|-----|-------|

### Top 3 trades gagnants
[Detail avec analyse de pourquoi ca a marche]

### Top 3 trades perdants
[Detail avec analyse de pourquoi ca n'a pas marche]

### Metriques de performance
[Win rate, profit factor, Sharpe, drawdown]

### Recommandations pour la semaine prochaine
[Ajustements de strategie]
```

---

## Exemples concrets

### Exemple 1 : Scan quotidien
```bash
claude "/trading-scan"
# ou
claude "Scanne toutes les paires USDT sur MEXC avec volume > $100k"
```

**Resultat attendu** : Tableau de 10-20 paires triees par force de signal, avec les 5 meilleures opportunites detaillees.

### Exemple 2 : Consensus avant trade
```bash
claude "/consensus 'Analyse BTC/USDT pour un potentiel long sur 4h'"
```

**Resultat attendu** : 3 analyses independantes + verdict consensus avec prix d'entree, SL, TP.

### Exemple 3 : Suivi PnL
```bash
claude "/trading-feedback"
```

**Resultat attendu** : PnL des 7 derniers jours, win rate, profit factor, recommandations.

---

## Effet sur le modele
- Le scan multi-exchange donne une vue complete du marche en un seul appel
- Le consensus 3 modeles reduit les faux signaux (chaque modele a ses biais)
- Le format tableau force des donnees comparables et actionnables
- L'analyse PnL cree une boucle de feedback qui ameliore la strategie
- La limite de 2% par trade est un garde-fou critique integre dans le prompt
- Le post-mortem des pertes transforme chaque erreur en apprentissage
