---
name: project_portage_linux_progress
description: État du portage JARVIS Windows→Linux au 2026-03-16 — fichiers portés, modules validés, reste à faire
type: project
---

## Portage JARVIS Linux — État au 2026-03-16

### Superviseur v2 (COMPLET)
- `jarvis_supervisor.py` réécrit — intégré à load_balancer, circuit_breaker, event_stream, persistence etoile.db/jarvis.db
- Config OMEGA v3.0 avec optimal_patterns du benchmark (code→M1, reasoning→M2, simple→OL1)
- Backpressure 3 niveaux (NORMAL/WARN/CRITICAL) avec seuils dynamiques
- Testé en prod : OL1 → 273ms, persistence OK

### Fichiers critiques portés
- `src/cluster_self_healer.py` → systemctl, M2/M3 ajoutés, httpx async
- `src/executor.py` → bash/xdotool/playerctl + traducteur PS→bash (couvre 563 commandes vocales)
- `src/audio_controller.py` → pactl/amixer (plus de ctypes.wintypes)
- `src/commands.py` → APP_PATHS Linux (44 apps)
- `src/agents.py` → prompts Linux (ia_system, ia_devops)
- `canvas/direct-proxy.js` → 40+ refs portées (prompts, chemins, commandes)
- `canvas/telegram-bot.js` → xdotool/xdg-open

### Batch portés (~250 fichiers)
- `cowork/dev/` : 112 fichiers, 0 F:/BUREAU restant
- `scripts/` : 42 fichiers portés
- `projects/` : 14 fichiers
- `finetuning/` : 25 fichiers
- `src/` : 12 fichiers
- `tests/` : 23 fichiers (C:\Users gardé = tests Windows intentionnels)
- Dossier fantôme `F:` supprimé

### Couche profonde — portée 2026-03-16 (suite)
- `src/windows.py` — **réécrit 100% Linux** (973→450 lignes, wmctrl/xdotool/pactl/xclip)
- `src/mcp_server.py` — `_ps_sync()` branchée sur traducteur bash
- `src/skills.py` — commandes brightness→brightnessctl, bluetooth→bluetoothctl, power→powerprofilesctl
- `src/executor.py` — traducteur PS→bash avec **50 patterns** couvrant 563 commandes vocales
- `src/agents.py` — prompts ia_system et ia_devops portés Linux
- **0 appel direct PowerShell** dans les modules critiques (mcp_server, tools, cluster_startup)
- 18/18 modules core importent sans erreur

### Session 2026-03-16 (suite) — 11 commits

**Nouveaux modules créés :**
- `src/conversation_tracker.py` — logging conversations dans conversations.db
- `src/decision_logger.py` — audit trail des décisions automatiques dans decisions.db
- `src/performance_monitor.py` — collecte CPU/RAM/GPU dans etoile.db.metrics
- `src/auto_healer_linux.py` — daemon auto-heal cluster
- `scripts/jarvis_portal.py` — FastAPI portal :8089
- `scripts/pipeline_runner.py` — 6 templates exécutables, 3 testés en prod
- `scripts/health_guardian.py` — daemon surveillance cluster avec audit_trail.db
- `scripts/validation_runner.py` — 10 scénarios vocaux, progression 30%→60%
- `scripts/voice_enricher.py` — 105 corrections vocales auto-générées
- `scripts/learning_daemon.py` — apprentissage continu (routing, patterns, qualité)

**Services systemd réparés :**
- jarvis-master (msvcrt→fcntl, taskkill→os.kill, wmic→pgrep, where→which)
- jarvis-portal, jarvis-perf-monitor, jarvis-auto-healer

**Tests : 454 passent** (325 core + 129 patterns/pipelines/phases)

### Reste (cosmétique, non-bloquant)
- ~60 modules src/ secondaires — non importés activement
- 4 scénarios vocaux échouent encore (boot, diagnostic, scan_trading, cleanup)
- Le tool MCP `powershell_run` — fonctionne via traducteur bash

**Why:** Le portage est critique pour l'autonomie de JARVIS sur Linux.
**How to apply:** Quand on travaille sur JARVIS Linux, vérifier d'abord cet état avant de toucher aux modules portés.
