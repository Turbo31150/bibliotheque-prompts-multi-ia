# BrowserOS — Configuration MCP

> Configuration du MCP server BrowserOS pour l'integration avec Claude Code.

---

## Configuration MCP

### Ajout dans `~/.claude/mcp-servers.json`

```json
{
  "browseros-mcp": {
    "command": "node",
    "args": ["/home/turbo/jarvis-linux/src/browseros_mcp.js"],
    "env": {
      "BROWSEROS_CDP_URL": "http://127.0.0.1:9222",
      "BROWSEROS_TIMEOUT": "30000",
      "BROWSEROS_HEADLESS": "true"
    },
    "description": "BrowserOS CDP — navigation, scraping, automation web"
  }
}
```

### Ce que ca fait
- Connecte Claude Code au navigateur BrowserOS via Chrome DevTools Protocol
- Permet a Claude de naviguer, cliquer, remplir des formulaires, extraire des donnees
- Le navigateur tourne en mode headless (pas de fenetre visible)

### Effet sur le modele
- Claude peut interagir avec le web en temps reel
- Le modele "voit" la page via des captures d'ecran CDP
- Les outils MCP BrowserOS apparaissent dans la liste des outils disponibles

---

## Outils MCP disponibles

| Outil | Description | Usage |
|-------|-------------|-------|
| `navigate` | Naviguer vers une URL | `navigate("https://example.com")` |
| `click` | Cliquer sur un element | `click("#button-id")` |
| `type` | Taper du texte | `type("#input-id", "texte")` |
| `screenshot` | Capture d'ecran | `screenshot()` |
| `extract` | Extraire du contenu | `extract("table.data")` |
| `wait` | Attendre un element | `wait("#element", 5000)` |
| `evaluate` | Executer du JavaScript | `evaluate("document.title")` |
| `tabs` | Gerer les onglets | `tabs()` |
| `scroll` | Scroller la page | `scroll("down", 500)` |
| `select` | Selectionner dans un dropdown | `select("#dropdown", "value")` |

---

## Configuration Docker (recommandee)

```yaml
# docker-compose.yml
services:
  browseros:
    image: browserless/chrome:latest
    ports:
      - "9222:3000"
    environment:
      - CONNECTION_TIMEOUT=600000
      - MAX_CONCURRENT_SESSIONS=5
      - ENABLE_DEBUGGER=true
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 2G
```

### Lancement

```bash
docker-compose up -d browseros
# Verifier que BrowserOS repond
curl http://127.0.0.1:9222/json/version
```

---

## Integration avec JARVIS

```python
# src/browseros_client.py
# Client CDP integre dans JARVIS
# Health probe automatique toutes les 30 secondes
# Reconnexion automatique si deconnecte
# Pool de sessions (max 5 simultanees)
```

### Endpoints JARVIS pour BrowserOS

```
GET  /api/browseros/tabs     — Liste des onglets ouverts
POST /api/browseros/navigate — Naviguer vers une URL
POST /api/browseros/extract  — Extraire des donnees
GET  /api/browseros/health   — Status du service
```

---

## Prerequis
- Docker installe
- Port 9222 disponible
- Minimum 2 GB RAM dediee a BrowserOS
- Claude Code avec MCP servers configures
