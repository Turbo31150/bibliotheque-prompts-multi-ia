# Claude API -- Trading

## Description

Prompts et patterns pour utiliser l'API Claude dans le trading : analyse de marche automatisee, generation de signaux, backtesting assiste et gestion de portfolio via API.

## Cas d'usage
- Bot d'analyse technique via API
- Generation de signaux de trading automatisee
- Pipeline d'analyse fondamentale
- Gestion de portfolio assistee par IA
- Alertes de marche intelligentes

---

## Prompts prets a copier

### 1 -- Bot d'analyse technique

```
Cree un bot d'analyse technique avec l'API Claude :

## OUTILS
tools = [
    {"name": "get_ohlcv", "description": "Recupere les donnees OHLCV d'une paire"},
    {"name": "calculate_rsi", "description": "Calcule le RSI"},
    {"name": "calculate_macd", "description": "Calcule le MACD"},
    {"name": "get_orderbook", "description": "Recupere le carnet d'ordres"},
    {"name": "get_funding_rate", "description": "Recupere le funding rate"}
]

## SYSTEM PROMPT
"Tu es un analyste technique crypto expert. Utilise les outils pour recuperer les donnees, calcule les indicateurs, et produis une analyse complete avec signal (LONG/SHORT/NEUTRE), niveaux d'entree/SL/TP, et confiance (0-100)."

## PIPELINE
1. User demande : "Analyse BTC/USDT 4h"
2. Claude appelle les outils pour collecter les donnees
3. Claude analyse et produit le signal
4. Signal envoye en notification
```

---

### 2 -- Generateur de signaux automatise

```
Cree un generateur de signaux avec l'API Claude :

## CODE
async def generate_signal(pair: str, timeframe: str) -> dict:
    data = await fetch_market_data(pair, timeframe)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Expert trading crypto. Analyse les donnees et genere un signal JSON: {direction, entry, stop_loss, take_profit, confidence, reasoning}",
        messages=[{"role": "user", "content": f"Donnees {pair} {timeframe}:\n{json.dumps(data)}"}]
    )
    return json.loads(response.content[0].text)

## AUTOMATISATION
- Cron toutes les 4h pour les paires surveillees
- Filtrer : ne notifier que si confidence > 70
- Historiser les signaux pour mesurer la performance
- Dashboard avec taux de reussite par paire
```

---

### 3 -- Analyse fondamentale automatisee

```
Pipeline d'analyse fondamentale via API Claude :

## ETAPES
1. COLLECTE (outils)
   - API CoinGecko : prix, market cap, volume
   - API DeFiLlama : TVL, protocols
   - GitHub API : activite du repo

2. ANALYSE (Claude)
   response = client.messages.create(
       model="claude-sonnet-4-20250514",
       system="Analyste fondamental crypto. Evalue le projet sur : technologie, equipe, tokenomics, adoption, risques. Score /100.",
       messages=[{"role": "user", "content": json.dumps(project_data)}]
   )

3. OUTPUT
   - Score fondamental /100
   - Points forts et faiblesses
   - Comparaison avec les concurrents
   - Recommandation
```

---

### 4 -- Gestionnaire de portfolio

```
Cree un gestionnaire de portfolio avec l'API Claude :

## OUTILS
tools = [
    {"name": "get_portfolio", "description": "Retourne le portfolio actuel"},
    {"name": "get_market_data", "description": "Prix et metriques d'une crypto"},
    {"name": "calculate_correlation", "description": "Correlation entre deux actifs"},
    {"name": "suggest_rebalance", "description": "Calcule le rebalancing necessaire"}
]

## CONVERSATIONS
"Mon portfolio est-il bien diversifie ?"
"Quel est mon P&L depuis le debut du mois ?"
"Dois-je rebalancer ?"
"Quelles positions sont les plus risquees ?"

## SYSTEM PROMPT
"Tu es un gestionnaire de portfolio crypto. Tu utilises les outils pour acceder aux donnees du portfolio et du marche. Tu donnes des conseils basés sur les donnees, jamais des promesses de rendement."
```

---

### 5 -- Alertes de marche intelligentes

```
Systeme d'alertes de marche via API Claude :

## CODE
def market_alert(events: list) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Analyste marche crypto. Evalue ces evenements. Reponds JSON: {alert: bool, severity, coins_affected, impact, action_suggested}",
        messages=[{"role": "user", "content": json.dumps(events)}]
    )
    return json.loads(response.content[0].text)

## EVENEMENTS SURVEILLES
- Variation de prix > 5% en 1h
- Volume anormal (> 3x moyenne)
- Liquidations massives
- Funding rate extreme
- Whale transactions (on-chain)

## NOTIFICATION
- Filtre intelligent (pas de spam)
- Notification desktop + TTS si severite haute
```

---

## Exemples d'utilisation

### Exemple : Signal automatique
**Code** : `signal = await generate_signal("BTC/USDT", "4h")`

**Resultat attendu** : `{"direction": "LONG", "entry": 63500, "stop_loss": 62200, "take_profit": 66000, "confidence": 75, "reasoning": "RSI en zone de survente..."}`

---

## Effet sur le modele
- L'API permet l'automatisation complete du pipeline de trading
- Le tool_use donne acces aux donnees de marche en temps reel
- Haiku pour les alertes frequentes (cout reduit), Sonnet pour l'analyse approfondie
- L'historisation des signaux permet de mesurer la performance du modele
