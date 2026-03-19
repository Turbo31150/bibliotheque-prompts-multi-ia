# OpenClaw - Trading

## Vue d'ensemble

Integration trading via OpenClaw : connexion MEXC, routage d'alertes, notifications vocales. Le trading-agent centralise l'analyse marche et la gestion des positions.

## Integration MEXC

### Configuration API

```json
{
  "mexc": {
    "api_key": "${MEXC_API_KEY}",
    "api_secret": "${MEXC_API_SECRET}",
    "base_url": "https://api.mexc.com",
    "websocket_url": "wss://wbs.mexc.com/ws"
  }
}
```

### Fonctions disponibles

| Skill | Description |
|-------|-------------|
| `mexc_price` | Prix temps reel d'une paire |
| `mexc_orderbook` | Carnet d'ordres |
| `mexc_positions` | Positions ouvertes |
| `mexc_place_order` | Placement d'ordre (limit/market) |
| `mexc_cancel_order` | Annulation d'ordre |
| `mexc_balance` | Solde du compte |
| `mexc_history` | Historique des trades |

## Routage des alertes

Le systeme d'alertes fonctionne en pipeline :

1. **Source** : websocket MEXC (prix, volume, liquidations)
2. **Filtrage** : regles definies dans `config/trading_alerts.json`
3. **Dispatch** : routage vers le canal approprie

### Canaux de notification

| Canal | Condition | Exemple |
|-------|-----------|---------|
| Vocal (TTS) | Alerte critique | "BTC chute de 5% en 1h" |
| Desktop notification | Alerte standard | Signal RSI sur ETH |
| Log OpenClaw | Toutes alertes | Historique complet |
| n8n workflow | Alertes avec action | Declenchement auto-trade |

### Exemple de regle d'alerte

```json
{
  "name": "btc_dump_alert",
  "pair": "BTCUSDT",
  "condition": "price_change_pct < -3",
  "timeframe": "1h",
  "channels": ["vocal", "desktop"],
  "message": "Alerte : BTC en baisse de {change}% sur 1h, prix actuel {price}"
}
```

## Notifications vocales

Les alertes critiques sont lues a voix haute via le pipeline :

```
trading-agent -> vocal skill -> jarvis-tts.sh -> haut-parleurs
```

```bash
# La skill vocal appelle directement le TTS
/home/turbo/jarvis-linux/scripts/jarvis-tts.sh "Alerte trading : BTC a 58000 dollars"
```

## Workflows associes

- Scan marche toutes les heures (`trading_scan` cron)
- Alertes prix toutes les 15 min (`crypto_alert` cron)
- Rapport PnL quotidien via n8n
