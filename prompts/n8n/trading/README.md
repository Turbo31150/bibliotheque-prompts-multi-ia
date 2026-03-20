# n8n - Trading

## Vue d'ensemble

Workflows n8n dedies au trading : alertes crypto, scans de marche, suivi de positions et rapports PnL.

## Workflows trading

### Crypto Alert (toutes les 15 min)

**Schedule** : `*/15 * * * *`

```
Cron -> HTTP Request (MEXC API /ticker/price)
  -> Code (comparer avec seuils)
  -> IF (seuil depasse ?)
    -> OUI : Notification + TTS (jarvis-tts.sh)
    -> NON : fin
```

**Nodes** :
- `HTTP Request` : appel MEXC API pour prix BTC, ETH, SOL
- `Code` : comparaison prix actuel vs seuils configures
- `IF` : branchement conditionnel
- `Execute Command` : appel `jarvis-tts.sh` pour alerte vocale

**Seuils configures** :
```json
{
  "BTC_USDT": { "high": 100000, "low": 50000 },
  "ETH_USDT": { "high": 5000, "low": 2000 },
  "SOL_USDT": { "high": 300, "low": 80 }
}
```

### Trading Scan (toutes les heures)

**Schedule** : `0 * * * *`

```
Cron -> HTTP Request (MEXC API /klines)
  -> Code (calcul RSI, MACD, volumes)
  -> IF (signal detecte ?)
    -> OUI : Slack + Screenshot BrowserOS
    -> NON : log
```

**Analyse** :
- RSI sur 14 periodes (signal si < 30 ou > 70)
- MACD crossover detection
- Volume anormal (> 2x moyenne 24h)

### Position Tracker (toutes les 30 min)

**Schedule** : `*/30 * * * *`

```
Cron -> HTTP Request (MEXC API /account)
  -> Code (calculer PnL par position)
  -> Set (formater donnees)
  -> DB (sauvegarder historique)
  -> IF (PnL critique ?)
    -> OUI : Alerte vocale
    -> NON : fin
```

### Daily PnL (tous les jours a 20h)

**Schedule** : `0 20 * * *`

```
Cron -> HTTP Request (MEXC API /trades + /account)
  -> Code (calcul PnL journalier)
  -> Code (generer rapport HTML)
  -> Email (envoi rapport)
  -> Execute Command (jarvis-tts.sh resume vocal)
```

**Rapport inclut** :
- PnL total du jour (realise + non realise)
- Meilleurs/pires trades
- Positions ouvertes avec PnL
- Comparaison avec veille/semaine

## Configuration commune

### Credentials MEXC

Les credentials MEXC sont stockees dans n8n (chiffrees) :

```bash
# Via l'interface n8n : Settings > Credentials > MEXC API
# Ou via API
curl -X POST http://localhost:5678/api/v1/credentials \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -d '{
    "name": "MEXC API",
    "type": "httpHeaderAuth",
    "data": {
      "name": "X-MEXC-APIKEY",
      "value": "'$MEXC_API_KEY'"
    }
  }'
```

### Endpoints MEXC utilises

| Endpoint | Methode | Usage |
|----------|---------|-------|
| `/api/v3/ticker/price` | GET | Prix actuel |
| `/api/v3/klines` | GET | Donnees OHLCV |
| `/api/v3/account` | GET | Solde et positions |
| `/api/v3/myTrades` | GET | Historique trades |
| `/api/v3/openOrders` | GET | Ordres ouverts |
| `/api/v3/order` | POST | Placement d'ordre |
