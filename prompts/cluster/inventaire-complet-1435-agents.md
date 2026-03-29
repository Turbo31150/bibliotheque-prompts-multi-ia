# Inventaire Complet JARVIS OMEGA — 1435 Agents

> Horodatage : 2026-03-29T06:50:00+01:00
> Total : 1435 composants actifs across 11 categories

---

## Sommaire par categorie

| # | Categorie | Quantite | Source |
|---|-----------|----------|--------|
| 1 | Agents SQL Registry | 38 | jarvis_orchestrator.db |
| 2 | Agents Core Python | 14 | core/agents/*.py |
| 3 | Agent Modules | 13 | core/agent_modules/*.py |
| 4 | Skills Gemini CLI | 85 | ~/.gemini/skills/ |
| 5 | OpenClaw Skills | 11 (46 cmds) | openclaw/skills/ |
| 6 | Domino Chains | 71 | core/domino/chains.d/ |
| 7 | Cowork Scripts | 579 | modules/cowork/ |
| 8 | Omega Master Agents | 6 | ~/.claude/agents/ |
| 9 | CLIs systeme | 18 | /usr/local/bin/ |
| 10 | Legions | 600 (10x60) | openclaw-master.py |
| **TOTAL** | | **1435** | |

---

## [1] AGENTS SQL REGISTRY (38)

| # | Nom | Type | Node | Capabilities |
|---|-----|------|------|-------------|
| 1 | architect-guardian | architecture | M1 | drift, mutation, consensus, audit |
| 2 | code-simplifier:code-simplifier | quality | M1 | simplify, clarity, maintainability |
| 3 | domino-optimizer | optimization | M1 | pipeline, benchmark, chain |
| 4 | feature-dev:code-architect | design | M1 | architecture, patterns, blueprint |
| 5 | feature-dev:code-explorer | dev | M1 | trace, architecture, dependencies |
| 6 | feature-dev:code-reviewer | review | M1 | bugs, security, conventions |
| 7 | ia-flow | flow | M1 | backpressure, task-separation, health |
| 8 | incident-responder | system | M1 | domino, repair, diagnostic |
| 9 | jarvis-ai-dispatch | tool | M1 | dispatch, inference, consensus, cdp |
| 10 | jarvis-auditor | audit | M1 | code-audit, security, post-deploy |
| 11 | jarvis-auto-improver | improvement | M1 | refactor, optimize, quality |
| 12 | jarvis-auto-scaler | infra | M1 | gpu-scaling, vram, load-balance |
| 13 | jarvis-backpressure | flow | M1 | throttle, queue, overload |
| 14 | jarvis-boot-layers | tool | M1 | boot, layers, startup, check |
| 15 | jarvis-browser | browser | M1 | cdp, scraping, automation, browseros |
| 16 | jarvis-cli-suite | tool | M1 | system, monitoring, security, gpu |
| 17 | jarvis-cluster-health | monitoring | M1 | health-check, gpu-temp, ram, cpu |
| 18 | jarvis-cluster-ops | tool | M1 | cluster, routing, failover, health |
| 19 | jarvis-code-reviewer | review | M1 | code-review, bugs, security, quality |
| 20 | jarvis-devops | devops | M1 | ci-cd, deploy, docker, systemd |
| 21 | jarvis-flow-dispatcher | flow | M1 | routing, dispatch, priority |
| 22 | jarvis-gpu-manager | gpu | M1 | gpu, thermal, vram, load |
| 23 | jarvis-monitor-live | tool | M1 | monitoring, snapshot, services |
| 24 | jarvis-multi-platform-router | routing | M1 | claude, gemini, chatgpt, routing |
| 25 | jarvis-quality-gate | quality | M1 | tests, lint, coverage, gate |
| 26 | jarvis-security-audit | tool | M1 | security, audit, ports, secrets |
| 27 | jarvis-task-balancer | balancing | M1 | load-balance, task-distribute |
| 28 | jarvis-voice-controller | voice | M1 | tts, stt, whisper, easyspeak |
| 29 | jarvis-zombie-cleaner | tool | M1 | system, cleanup, zombie |
| 30 | pr-review-toolkit:code-reviewer | review | M1 | style, guidelines, best-practices |
| 31 | pr-review-toolkit:comment-analyzer | docs | M1 | comments, docstrings, accuracy |
| 32 | pr-review-toolkit:pr-test-analyzer | testing | M1 | test-coverage, edge-cases, gaps |
| 33 | pr-review-toolkit:silent-failure-hunter | review | M1 | error-handling, catch, fallback |
| 34 | pr-review-toolkit:type-design-analyzer | design | M1 | types, encapsulation, invariants |
| 35 | security-reviewer | security | M1 | owasp, secrets, injection, ports |
| 36 | system-crash-guardian | system | M1 | crash, respawn, zombie, containment |
| 37 | system-health-monitor | monitoring | M1 | cpu, ram, gpu, services, network |
| 38 | task-decomposer-prime | orchestration | M1 | decompose, multi-domain, complex |

---

## [2] AGENTS CORE PYTHON (14)

| # | Nom | Description |
|---|-----|-------------|
| 1 | browseros_operator | Controle BrowserOS tabs via CDP |
| 2 | confidence | Score de confiance pour routing |
| 3 | container_operator | Gestion containers Docker |
| 4 | github_operator | Repos, notifications, commits |
| 5 | mail_operator | IMAP, classification emails |
| 6 | master_agent_v3 | Orchestre cluster + Domino Engine |
| 7 | memory_store | Memoire long-terme SQLite |
| 8 | network_operator | Ping, ports, DNS, traceroute |
| 9 | orchestrator | Routing capabilities-based |
| 10 | personas | Systeme de personnalites agents |
| 11 | retry_patterns | Retry et fallback decorators |
| 12 | sql_operator | Requetes SQLite read-only |
| 13 | telegram_operator | Messages et alertes Telegram |
| 14 | voice_router | Voice transcript → actions |

---

## [3] AGENT MODULES (13)

| # | Module | Role |
|---|--------|------|
| 1 | agent_auto_scaler | Scaling automatique |
| 2 | agent_collaboration | Collaboration inter-agents |
| 3 | agent_ensemble | Ensemble multi-agents |
| 4 | agent_episodic_memory | Memoire episodique |
| 5 | agent_factory | Creation dynamique agents |
| 6 | agent_feedback_loop | Boucle feedback |
| 7 | agent_health_guardian | Surveillance sante agents |
| 8 | agent_memory | Memoire persistante |
| 9 | agent_monitor | Monitoring agents |
| 10 | agent_orchestrator_v3 | Orchestration v3 |
| 11 | agent_prompt_optimizer | Optimisation prompts |
| 12 | agent_self_improve | Auto-amelioration |
| 13 | agent_task_planner | Planification taches |

---

## [4] DOMINO CHAINS (71) — Classes par domaine

### Systeme & Boot (12)
full-boot-sequence, cli-system-health, systemd-crash-healer, service-crash-recovery, service-conflict-resolver, repair-missing-commands, zombie-apocalypse-cleaner, universal-skill-loader, automation-loop-monitor, skill-auto-test-integrity, skill-self-evolution, auto-update-safety-net

### Securite (6)
cli-security-hardening, security-breach-lockdown, security-brute-force-shield, security-deep-audit, security-file-integrity-lockdown, network-anomaly-blocker

### GPU & Performance (8)
cli-gpu-auto-optimize, gpu-error-cascade, thermal-gpu-throttle, thermal-cpu-protection, cluster-vram-balancer, high-latency-optimizer, energy-profile-optimizer, predictive-resource-scaling

### Cluster & Reseau (6)
cluster-node-failover, cluster-latency-mitigation, network-degradation-cascade, network-resiliency-guardian, intelligent-task-routing, mcp-bridge-watchdog

### Memoire & Donnees (6)
database-integrity-self-heal, distributed-memory-sync, cognitive-task-indexer, context-window-archiver, memory-oom-preventer, log-pattern-analyzer

### IA & Consensus (5)
cli-ai-consensus-dispatch, multi-ia-quorum-consensus, llm-logic-fallback, benchmark-self-improve, meta-learning-optimizer

### Backup & Recovery (5)
pre-incident-backup, post-update-backup, backup-integrity-verify, backup-rotation-check, disaster-recovery

### Infra & Docker (4)
docker-container-auto-heal, disk-maintenance-janitor, predictive-disk-replacement, power-overload-prevention

### Freelance & Business (4)
cli-freelance-optimizer, freelance-pipeline, freelance-mission-hunter, social-growth-orchestrator

### Contenu & Communication (4)
content-pipeline, automated-vlog-pipeline, documentation-auto-sync, automated-data-shield

### Code & Dev (3)
code-error-debug, git-workspace-guardian, github-automation

### Vocal (3)
voice-command-interceptor, voice-response-pipeline, ghost-pilot-autonomous

### Trading (2)
trading-instant-action, ram-pressure-cascade

### Browser (2)
browser-session-repair, test-integration

---

## [5] LEGIONS (10 x 60 = 600)

| Legion | Nom | Agents | Skills | Trigger | Score |
|--------|-----|--------|--------|---------|-------|
| L1 | Architectes | 3 | 3 | design, architecture, plan | 0.812 |
| L2 | Forgeurs | 3 | 3 | code, implement, tdd | 0.769 |
| L3 | Sentinelles | 3 | 3 | securite, crash, zombie | 0.646 |
| L4 | Analystes | 2 | 3 | analyse, consensus, verifie | 0.727 |
| L5 | Automates | 3 | 3 | domino, pipeline, workflow | 0.578 |
| L6 | Traders | 1 | 3 | trading, codeur, freelance | 0.446 |
| L7 | Communicateurs | 1 | 3 | telegram, linkedin, vocal | 0.341 |
| L8 | Optimiseurs | 4 | 3 | gpu, thermal, scale | 0.650 |
| L9 | Erudits | 2 | 3 | prompt, sql, memoire | 0.448 |
| L10 | Debuggers | 3 | 3 | debug, erreur, crash | 0.689 |

---

## [6] CLIs (18)

| # | CLI | Sous-commandes |
|---|-----|----------------|
| 1 | jarvis | status, health, gpu, ask, security, clean, load, skills |
| 2 | jai | 23 targets IA |
| 3 | jarvis-gpu | status, load, unload, thermal, vram |
| 4 | jarvis-cluster | health, nodes, route, failover |
| 5 | jarvis-security | scan, ports, secrets, guard |
| 6 | jarvis-zombie | list, kill, parents |
| 7 | jarvis-monitor | snapshot, live, services |
| 8 | jarvis-layers | check, boot |
| 9 | jarvis-decide | predict, simulate, matrix, optimize, visualize |
| 10 | jarvis-dispatch | --list |
| 11 | jarvis-boot | start, stop |
| 12 | jarvis-maintenance.sh | weekly cleanup |
| 13 | jarvis-notify | send notification |
| 14 | jarvis-repair | auto-repair |
| 15 | jarvis-search | search codebase |
| 16 | jarvis-wave | launch wave |
| 17 | openclaw-boot | boot, register, trigger, status |
| 18 | openclaw-master | status, master, patrol, legion, dispatch, agents, predict |

---

[HORODATAGE] 2026-03-29T06:50:00+01:00
[TOTAL] 1435 composants
[STATUT] PRODUCTION ACTIVE

