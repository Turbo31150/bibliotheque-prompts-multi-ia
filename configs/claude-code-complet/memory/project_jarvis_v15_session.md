---
name: project_jarvis_v15_session
description: Session massive v12.4→v15.0 — 118 commits, 12 tags, 65 n8n, refactoring complet
type: project
---

Session du 2026-03-16 au 2026-03-19 — JARVIS v12.4 → v15.0

## Décisions architecturales prises
- Health endpoint unifié /health/full — 8 composants en parallèle via asyncio.gather
- Auth centralisée dans src/auth.py (remplace Bearer hardcodés)
- Rate limiting 200 req/min via middleware FastAPI
- RAG local avec SQLite FTS5 (pas de dépendance externe)
- Smart Memory avec keyword overlap × importance scoring
- BrowserOS piloté via CDP port 9105 (pas MCP 9001 qui est instable)
- n8n comme couche d'orchestration principale (65 workflows)
- Docker volumes : python_ws/ + scripts/ + canvas/ montés dans jarvis-ws
- Log rotation Docker : max-size 50m × 3 fichiers dans daemon.json + docker-compose
- cowork-engine : restart policy "no" (batch job, pas daemon)

## Contraintes à respecter
- JAMAIS localhost → toujours 127.0.0.1 (IPv6 lag)
- Ollama cloud : think:false OBLIGATOIRE
- M1 Qwen3 : prefix /nothink OBLIGATOIRE
- M2/M3 : max_output_tokens >= 2048
- GPU : Warning 75°C, Critical 85°C → re-routage
- Ne pas committer : .env, *.db, .fernet_key, node_modules, venv
- Docker CDP port : browseros_server attend 9105 (config dans server_config.json)
- Telegram bot : un seul polling à la fois (conflit si 2 instances)

## Fichiers critiques ajoutés cette session
src/health_aggregator.py, src/auth.py, src/rate_limiter.py, src/metrics_exporter.py
src/rag_engine.py, src/log_aggregator.py, src/smart_memory.py, src/browseros_cdp.py
src/notifications.py, src/webhooks.py, src/discord_bridge.py, src/voice_multilingual.py
src/mobile_api.py, src/canva_bridge.py, src/notion_bridge.py, src/calendar_bridge.py
src/web_researcher.py, src/api_auth.py, src/roles.py

## Chiffres réels vérifiés
315 modules src/, 224 scripts, 574 cowork, 329 tests, 320K lignes
674 endpoints REST, 658 MCP handlers, 103 SQLite DBs
65 n8n workflows, 12 crontab, 11 OpenClaw crons
5 GPUs, 40 Go VRAM, 8 modèles LM Studio, 3 modèles Ollama

**Why:** Session de développement la plus massive — documenter pour cohérence future
**How to apply:** Vérifier ces chiffres avant de les citer dans les README
