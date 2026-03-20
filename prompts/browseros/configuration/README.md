# BrowserOS - Configuration

## Vue d'ensemble

Installation et configuration de BrowserOS, le navigateur automatise du cluster JARVIS. Base sur Chrome/Chromium avec CDP (Chrome DevTools Protocol) pour le controle programmatique.

## Ports

| Service | Port |
|---------|------|
| CDP (Chrome DevTools Protocol) | `9105` |
| MCP Server | `9001` |

## Installation

```bash
# Lancer Chrome avec remote debugging
google-chrome --remote-debugging-port=9105 \
  --user-data-dir=$HOME/.browseros \
  --no-first-run \
  --disable-default-apps

# Verifier la connexion CDP
curl -s http://localhost:9105/json/version
```

## Configuration MCP

Le serveur MCP BrowserOS ecoute sur le port 9001 et expose les fonctions navigateur aux agents OpenClaw.

### server_config.json

```json
{
  "server": {
    "port": 9001,
    "host": "0.0.0.0"
  },
  "cdp": {
    "host": "localhost",
    "port": 9105
  },
  "auth": {
    "token": "${BROWSEROS_MCP_TOKEN}"
  },
  "capabilities": [
    "navigate",
    "click",
    "type",
    "screenshot",
    "evaluate",
    "wait_for_selector",
    "get_text",
    "tab_management"
  ]
}
```

## Extension Skills

Les skills BrowserOS sont des scripts JavaScript charges dynamiquement :

| Skill | Fichier | Description |
|-------|---------|-------------|
| Health patrol | `health_patrol.js` | Verification sante des onglets |
| Trading monitor | `trading_monitor.js` | Surveillance dashboards trading |
| GitHub watchdog | `github_watchdog.js` | Monitoring repos GitHub |
| LinkedIn engagement | `linkedin_engagement.js` | Automatisation LinkedIn |

## Integration Kimi-Claw

Kimi-Claw (modele vision) peut analyser les screenshots captures par BrowserOS pour comprendre le contenu visuel des pages web :

```
BrowserOS screenshot -> Kimi-Claw vision -> Analyse textuelle -> Agent OpenClaw
```

## Session save/restore

BrowserOS sauvegarde et restaure les sessions automatiquement :

```bash
# Sauvegarde manuelle
curl -X POST http://localhost:9001/session/save \
  -H "Authorization: Bearer $BROWSEROS_MCP_TOKEN"

# Restauration
curl -X POST http://localhost:9001/session/restore \
  -H "Authorization: Bearer $BROWSEROS_MCP_TOKEN"
```

Les sessions incluent : onglets ouverts, cookies, localStorage, positions de scroll.

## Fichiers cles

- `server_config.json` - Configuration du serveur MCP
- `skills/` - Repertoire des skills JavaScript
- `sessions/` - Sauvegardes de sessions
- `.browseros/` - Profil Chrome avec donnees persistantes
