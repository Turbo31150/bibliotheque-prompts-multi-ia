# BrowserOS - Trading

## Vue d'ensemble

Automatisation des dashboards de trading via BrowserOS : ouverture MEXC, capture de graphiques, detection et alerte sur signaux.

## Dashboard MEXC

### Ouverture automatique

Au demarrage de la session BrowserOS, les onglets MEXC sont ouverts automatiquement :

- **MEXC Spot** : `https://www.mexc.com/exchange/BTC_USDT`
- **MEXC Futures** : `https://futures.mexc.com/exchange/BTC_USDT`

### Navigation entre paires

```javascript
// Changer de paire sur MEXC
async function switchPair(client, pair) {
  const { Page } = client;
  await Page.navigate({
    url: `https://www.mexc.com/exchange/${pair.replace('/', '_')}`
  });
  await Page.loadEventFired();
}
```

## Capture de graphiques

Le script `trading_monitor.js` capture periodiquement les graphiques :

```javascript
async function captureChart(client, pair) {
  const { Page } = client;

  // Attendre le rendu du graphique
  await new Promise(r => setTimeout(r, 3000));

  // Screenshot de la zone graphique
  const screenshot = await Page.captureScreenshot({
    format: 'png',
    clip: { x: 0, y: 100, width: 1200, height: 600, scale: 1 }
  });

  // Sauvegarder
  const filename = `charts/${pair}_${Date.now()}.png`;
  fs.writeFileSync(filename, Buffer.from(screenshot.data, 'base64'));

  return filename;
}
```

Les screenshots peuvent etre analyses par Kimi-Claw (modele vision) pour detecter des patterns visuels.

## Detection de signaux

### Signaux surveilles

| Signal | Detection | Action |
|--------|-----------|--------|
| Alerte prix | Extraction DOM du prix actuel | Notification si seuil depasse |
| Volume spike | Lecture de la barre de volume | Alerte vocale |
| Liquidations | Monitoring du feed liquidations | Log + notification |
| RSI extreme | Lecture indicateur technique | Alerte si < 30 ou > 70 |

### Pipeline d'alerte

```
MEXC (onglet) -> trading_monitor.js -> Extraction donnees DOM
  -> Comparaison avec seuils -> Si signal detecte :
    -> Screenshot du graphique
    -> Notification vocale via jarvis-tts.sh
    -> Envoi a trading-agent OpenClaw pour analyse
    -> Declenchement workflow n8n si action requise
```

## Configuration des seuils

```json
{
  "alerts": {
    "BTC_USDT": {
      "price_high": 100000,
      "price_low": 50000,
      "volume_spike_pct": 300,
      "rsi_high": 75,
      "rsi_low": 25
    }
  }
}
```
