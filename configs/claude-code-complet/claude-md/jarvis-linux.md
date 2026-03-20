# JARVIS Turbo v15.0 — Project Instructions

## Langue
Toujours repondre en francais. Code en anglais, commentaires en francais si pertinent.

## Architecture
- **SDK**: Claude Agent SDK Python v0.1.35 | **Runtime**: uv v0.10.2 + Python 3.13
- **Cluster**: 4 noeuds IA (M1/M1B/M2/M3) + cloud (gpt-oss/devstral/glm/minimax) | 10 GPU, 78 GB VRAM
- **Modules**: 246 dans `src/` (93K lignes) | **Outils MCP**: 658 handlers | **REST**: 670+ endpoints
- **Canvas**: `canvas/` — UI standalone port 18800 avec autolearn engine
- **COWORK**: 574 scripts dans `cowork/dev/` | Pipeline autonome
- **OpenClaw**: 40 agents + 56 dynamic | 11 crons | Gateway port 18789
- **Tests**: 2,241 fonctions (77 fichiers) | Couverture src: 85.5%
- **Electron**: 29 pages | **Launchers**: 35 | **n8n**: 65 workflows at http://127.0.0.1:5678
- **DBs**: 63 bases (160 MB total) | etoile.db (42 tables, 13.5K rows)

## Conventions Code
- Python: type hints, async/await, f-strings, dataclasses
- Imports: `from __future__ import annotations` en premier
- Node.js (canvas): CommonJS require, pas d'ESM
- Nommage: snake_case Python, camelCase JS
- Tests: `uv run pytest` — fichiers `test_*.py`

## Fichiers critiques (ne pas casser)
- `src/config.py` — Noeuds cluster, routage, chemins projets
- `src/tools.py` — Outils MCP (pool httpx partagee)
- `src/mcp_server.py` — 658 handlers (6282 lignes)
- `src/commands.py` — Commandes vocales
- `src/commander.py` — Classification/decomposition taches
- `canvas/direct-proxy.js` — Proxy HTTP cluster + autolearn
- `src/health_aggregator.py` — Endpoint unifie /health/full (8 composants)
- `src/auth.py` — Tokens centralises, rotation automatique
- `src/browseros_client.py` — Client CDP BrowserOS + health probe
- `src/rate_limiter.py` — Rate limiting par IP/token (sliding window)
- `src/metrics_exporter.py` — Export Prometheus-compatible /metrics
- `src/rag_engine.py` — RAG local SQLite FTS5 (zero deps externes)
- `src/browseros_cdp.py` — Moteur CDP BrowserOS (navigation, scraping)
- `src/notion_bridge.py` — Bridge bidirectionnel JARVIS ↔ Notion
- `src/calendar_bridge.py` — Integration Google Calendar (evenements, alertes)
- `src/web_researcher.py` — Recherche web intelligente + digest
- `src/webhooks.py` — Receiver webhooks (n8n, GitHub, services externes)
- `src/discord_bridge.py` — Bridge Discord webhook integration
- `src/voice_multilingual.py` — Voice multilingue (FR/EN/ES) TTS + STT config
- `src/mobile_api.py` — API mobile endpoints

## Cluster — Acces rapide
| Noeud | URL | Modele | Role | Score |
|-------|-----|--------|------|-------|
| M1 | 127.0.0.1:1234 | qwen3-8b | CHAMPION LOCAL (46tok/s) | 98.4/100 |
| M1B | 127.0.0.1:1234 | gpt-oss-20b | Deep local (9s, ctx25k) | — |
| M2 | 192.168.1.26:1234 | deepseek-r1-0528-qwen3-8b | Reasoning (44tok/s) | — |
| M3 | 192.168.1.113:1234 | deepseek-r1-0528-qwen3-8b | Reasoning fallback | — |
| OL1 cloud | 127.0.0.1:11434 | gpt-oss:120b-cloud | CHAMPION CLOUD (51tok/s) | 100/100 |
| OL1 cloud | 127.0.0.1:11434 | devstral-2:123b-cloud | Code cloud #2 | 94/100 |
| OL1 local | 127.0.0.1:11434 | qwen3:1.7b | Ultra-rapide (84tok/s) | — |
| OL1 cloud | 127.0.0.1:11434 | kimi-k2.5:cloud | Moonshot cloud (tool calling) | — |

## Regles
- JAMAIS `localhost` → toujours `127.0.0.1` (IPv6 lag Windows)
- Ollama cloud: `think:false` OBLIGATOIRE
- M1: `/nothink` prefix OBLIGATOIRE pour qwen3/gpt-oss (pas deepseek-r1)
- M2/M3: max_output_tokens=2048 minimum (reasoning needs space)
- LM Studio API: `/api/v1/chat` (Responses API) — output[].content
- GPU: warning 75C, critical 85C → re-routage cascade
- Ne pas committer: `data/*.db`, `.env`, credentials, `node_modules/`

## Scripts utiles
```bash
uv run python scripts/system_audit.py --quick          # Audit rapide
uv run python scripts/trading_v2/gpu_pipeline.py --quick --json  # Trading scan
node canvas/direct-proxy.js                             # Canvas proxy
python cowork/dev/autonomous_cluster_pipeline.py        # Pipeline autonome
make test                                               # Lancer les tests
make health                                             # Health check complet
make cluster                                            # Status cluster
# Endpoints REST v15.0:
# /docs                  — Swagger UI (auto-generated)
# /metrics               — Prometheus metrics export
# /api/rag/search?q=...  — RAG local search (FTS5)
# /api/browseros/tabs    — BrowserOS CDP tabs management
# /api/research/digest   — Web research digest
```

## Documentation
- `CHANGELOG.md` — Historique complet des versions et breaking changes
- `CONTRIBUTING.md` — Guide de contribution, conventions, process de PR

## n8n
- **65 workflows** at http://127.0.0.1:5678
- Couvre: monitoring, trading, notifications, backups, health checks, Discord, GitHub

## Slash commands (plugin jarvis-turbo, 43 commandes)
`/cluster-check` `/mao-check` `/gpu-status` `/thermal` `/heal-cluster`
`/consensus` `/quick-ask` `/web-search` `/trading-scan` `/trading-feedback`
`/canvas-status` `/canvas-restart` `/audit` `/model-swap` `/deploy`

## Troubleshooting rapide
| Symptome | Fix |
|----------|-----|
| M2/M3 TIMEOUT | max_output_tokens trop bas pour deepseek-r1, minimum 2048 |
| OL1 OFFLINE | `ollama serve` restart |
| Canvas crash | `node canvas/direct-proxy.js` restart (port 18800) |
| GPU >75C | `/thermal`, decharger modeles |
| Context exceeded | Reduire prompt ou max_output_tokens |
| OpenClaw cron spam | Verifier jobs.json, max 11 crons actifs |
