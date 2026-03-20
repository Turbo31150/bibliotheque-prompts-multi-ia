---
name: project_jarvis_v15_complete
description: Inventaire complet JARVIS v15.0 — 128 commits, 12 tags, 320K lignes, toute la session documentée
type: project
---

# JARVIS v15.0 — Inventaire Complet (2026-03-16 → 2026-03-20)

## Repos GitHub
- jarvis-linux: https://github.com/Turbo31150/jarvis-linux (128 commits, 12 tags)
- bibliotheque-prompts-multi-ia: https://github.com/Turbo31150/bibliotheque-prompts-multi-ia (20 commits, 217 fichiers, 245 HTML cards)

## Code
- src/: 317 modules Python (109 515 lignes)
- scripts/: 225 scripts
- cowork/: 574 scripts autonomes
- tests/: 331 fichiers test (8845+ fonctions)
- automation/: 25 tasks JavaScript
- n8n_workflows/: 71 exports JSON
- Total: 320 465 lignes Python

## Infrastructure
- Docker: 10 services (docker-compose.modular.yml)
- Systemd: 24 services + 3 timers
- SQLite: 103 bases de données
- MCP: 658 handlers
- REST: 674+ endpoints (Swagger /docs)
- n8n: 65 workflows actifs
- Crontab: 12 entries
- OpenClaw: 12 crons

## Fichiers créés cette session
src/health_aggregator.py, src/auth.py, src/rate_limiter.py, src/metrics_exporter.py
src/rag_engine.py, src/log_aggregator.py, src/smart_memory.py, src/browseros_cdp.py
src/notifications.py, src/webhooks.py, src/discord_bridge.py, src/voice_multilingual.py
src/mobile_api.py, src/canva_bridge.py, src/notion_bridge.py, src/calendar_bridge.py
src/web_researcher.py, src/api_auth.py, src/roles.py, src/you_search.py
src/you_search_cached.py, scripts/gpu_redistribute.py, scripts/backup_pipeline.py
scripts/auto_heal_scheduler.py, scripts/ai_self_improve.py, scripts/openclaw_devops_agent.py

## Documentation
- README.md (787L FR), README.en.md (208L EN), CLAUDE.md (105L)
- CHANGELOG.md (72L), CONTRIBUTING.md (69L)
- .env.example (56L), Makefile (48L), requirements.lock (114L)
- docs/CLAUDE_CODE_MIGRATION_GUIDE.md
- docs/you-research/ (11 fichiers, 165 Ko de recherche You.com)
- .github/workflows/ci.yml + docker-multiarch.yml

## Versions release
v12.5: Health, Auth, CI, Makefile, BrowserOS, OpenClaw, AI self-improve
v12.6: Swagger, RAG, Prometheus, Rate Limit, Dashboard, Log rotation
v12.7: Logs centralisés, Backup pipeline
v12.8: HTTPS/TLS, API key auth, Prometheus live, Docker health
v12.9: RBAC roles, Notifications, Auto-heal, 7438 tests fixés
v12.9.1-3: Automations BrowserOS, LinkedIn post, session save
v13.0: Notion, Calendar, Web Research
v13.1: Canva, Smart Memory
v14.0: 65 n8n workflows, Webhooks, Discord, CHANGELOG, CONTRIBUTING
v15.0: Docker multi-arch, Voice multilingue, Mobile API, roadmap 100%

## Contraintes à respecter
- JAMAIS localhost → 127.0.0.1
- Ollama cloud: think:false
- M1 Qwen3: /nothink prefix
- M2/M3: max_output_tokens >= 2048
- GPU: Warning 75°C, Critical 85°C
- Ne pas committer: .env, *.db, .fernet_key, venv
- BrowserOS CDP: port 9105 (server_config.json à 9105)
- Telegram: un seul polling

## Cluster
- M1: AMD Ryzen 7 5700X3D, 46GB RAM, 5 GPUs (40GB VRAM)
- GPU 0: RTX 2060 12GB | GPU 1-3: 3x GTX 1660S 6GB | GPU 4: RTX 3080 10GB
- LM Studio: 7 modèles (qwen3.5-9b, qwen3-coder-30b, qwen3.5-35b, gpt-oss-20b, deepseek-r1, gemma-3-4b, nomic-embed)
- Ollama: 3 modèles (kimi-k2.5:cloud, deepseek-r1:7b, qwen2.5:1.5b)
- M2: 192.168.1.26:1234 (deepseek-r1)
- M3: 192.168.1.113:1234 (deepseek-r1)

## You.com API
- Clé dans .env (YOU_API_KEY), ~$94.80 restants sur $100
- 11 rapports de recherche stockés dans docs/you-research/
- YouSearchCached: RAG-first, API-fallback
- 10 524 chunks RAG indexés

## Trading
- Module: scripts/trading_v2/ (universal_scalper.py, strategies.py, gpu_pipeline.py, ai_consensus.py)
- Scanner RIVER/USDT avec alertes Telegram
- Clés MEXC API: PAS CONFIGURÉES dans .env

**Why:** Inventaire complet pour restauration ou continuation dans une future session
**How to apply:** Référencer ce fichier pour retrouver n'importe quel composant
