# OpenClaw — Trading

> Généré par M1 cluster (gpt-oss-20b)

# Guide complet d’utilisation d’**OpenClaw** comme **gateway de trading crypto**

> *OpenClaw* est un framework open‑source qui permet d’orchestrer des agents IA pour la prise de décision en trading.  
> Ce guide vous montre comment le configurer, l’utiliser pour scanner le marché MEXC, mettre en place un consensus multi‑IA et envoyer des alertes via Telegram.

---

## 1. Description générale

| Élément | Détails |
|---------|--------|
| **OpenClaw** | Hub d’orchestration IA (agents, prompts, workflows) |
| **MEXC** | Exchange crypto à scanner |
| **Consensus multi‑IA** | Combinaison de plusieurs modèles/langages pour réduire le biais et augmenter la robustesse |
| **Telegram** | Canal de notification en temps réel |

### Flux de travail typique

1. **Scanner MEXC** → agent `scan_mexc` lit les ticks, récupère données OHLCV.  
2. **Analyse technique** → agents multiples (p.ex., RSI, MACD, Sentiment) évaluent la position.  
3. **Consensus** → un orchestrateur combine les votes des agents pour décider d’acheter/ vendre/ conserver.  
4. **Exécution** → si consensus positif, agent `execute_trade` place l’ordre via l’API MEXC.  
5. **Alertes** → agent `notify_telegram` envoie la décision et le résumé.

---

## 2. Configuration

### 2.1 Prérequis

| Outil | Version recommandée |
|-------|---------------------|
| Python | ≥ 3.10 |
| pip | latest |
| Docker (facultatif) | ≥ 20.10 |
| Node.js (pour certains plugins) | ≥ 16 |

### 2.2 Installation d’OpenClaw

```bash
# Clone le dépôt
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# Crée un environnement virtuel
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate

# Installe les dépendances
pip install -r requirements.txt

# Optionnel : lancer via Docker
docker-compose up --build
```

### 2.3 Variables d’environnement

Créez un fichier `.env` à la racine :

```dotenv
# MEXC API
MEXC_API_KEY=xxxxxxxxxxxxxxxxxxxx
MEXC_SECRET_KEY=yyyyyyyyyyyyyyyyyyyy

# Telegram Bot
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
TELEGRAM_CHAT_ID=-1001234567890

# OpenAI / LLMs
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
LLM_MODEL=gpt-4o-mini

# Réseau de consensus
CONSENSUS_AGENTS=RSI,MACD,SENTIMENT,PRICE_PATTERN
```

### 2.4 Fichiers de configuration OpenClaw

| Fichier | Rôle |
|---------|------|
| `config.yaml` | Paramètres globaux (agents, seuils, fréquence) |
| `agent_definitions.yaml` | Définition des prompts et des fonctions d’agent |

Exemple simplifié :

```yaml
# config.yaml
scan_interval: 30          # secondes
trade_threshold: 0.7       # consensus >= 70%
max_position_size: 0.01    # % de l’équivalent USD

agents:
  - name: scan_mexc
    type: api_scanner
    endpoint: mexc
  - name: rsi_analyzer
    type: technical_indicator
    indicator: RSI
    period: 14
  - name: macd_analyzer
    type: technical_indicator
    indicator: MACD
    fast_period: 12
    slow_period: 26
    signal_period: 9
  - name: sentiment_analyzer
    type: nlp_sentiment
    source: twitter
  - name: consensus_orchestrator
    type: aggregator
  - name: execute_trade
    type: order_executor
  - name: notify_telegram
    type: notifier
```

---

## 3. Prompts par tâche

| Tâche | Prompt type | Exemple de prompt |
|-------|-------------|-------------------|
| **Scanner MEXC** | API request + data extraction | `GET /api/v3/klines?symbol=BTCUSDT&interval=1m` → parse JSON |
| **RSI Analyzer** | Analyse technique | *"Calcule l’indice RSI sur les 14 dernières périodes pour BTCUSDT. Si RSI < 30, indique 'OVERBOUGHT', sinon 'OVERSOLD'."* |
| **MACD Analyzer** | Analyse technique | *"Calcule MACD (12/26/9) pour BTCUSDT. Retourne la valeur actuelle et un signal d’achat/vente selon croisement."* |
| **Sentiment Analyzer** | NLP | *"Scrape les derniers tweets mentionnant BTC. Évalue le sentiment global (+1 positif, -1 négatif). Fournis une note de 0 à 1."* |
| **Consensus Orchestrator** | Aggregation | *"Récolte les votes des agents RSI, MACD et Sentiment. Chaque agent donne +1 pour achat, -1 pour vente, 0 pour neutre. Si la somme > 0.7*max_agents*, déclenche un ordre d’achat."* |
| **Order Executor** | API request | *"Place un marché BUY de taille X% du solde USD sur MEXC."* |
| **Telegram Notifier** | Message format | *"✅ TRADE EXECUTED: BUY BTCUSDT @ {timestamp}\n📈 RSI: {rsi}\n⚡ MACD: {macd}\n💬 Sentiment: {sentiment}"* |

### Exemple complet de prompt orchestré

```yaml
# agent_definitions.yaml
agents:
  - name: rsi_analyzer
    prompt: |
      Calcule l’indice RSI sur les 14 dernières périodes pour BTCUSDT.
      Si RSI < 30, retourne 'OVERBOUGHT', sinon 'OVERSOLD'.
  - name: macd_analyzer
    prompt: |
      Calcule MACD (12/26/9) pour BTCUSDT. Retourne la valeur actuelle et un signal d’achat/vente selon croisement.
  - name: sentiment_analyzer
    prompt: |
      Scrape les derniers tweets mentionnant BTC. Évalue le sentiment global (+1 positif, -1 négatif). Fournis une note de 0 à 1.
  - name: consensus_orchestrator
    prompt: |
      Récolte les votes des agents RSI, MACD et Sentiment.
      Chaque agent donne +1 pour achat, -1 pour