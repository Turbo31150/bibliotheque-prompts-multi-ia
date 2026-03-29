# Catalogue Complet des Agents JARVIS (928)

> Derniere mise a jour : 2026-03-29
> Architecture : Core Claude Code (8) + Plugin jarvis-turbo (15)

---

## Core Claude Code (8 agents)

### incident-responder

**Description :** Agent de reponse aux incidents. Effectue un diagnostic automatique complet, selectionne la chaine domino appropriee, execute la reparation et genere un rapport detaille. Premier agent active lors d'un incident critique.

**Outils disponibles :**
- `journalctl`, `dmesg`, `systemctl status`, `docker logs`
- `domino-engine select-chain`, `domino-engine execute`
- `jarvis-report generate`, `sqlite3 incidents.db`

**Auto-trigger :** Oui - declenche automatiquement sur signal d'incident (service failed, crash detecte, alerte monitoring). Seuil : severite >= WARNING.

---

### architect-guardian

**Description :** Gardien de l'architecture JARVIS. Valide toute modification structurelle (ajout/suppression fichier, changement config, migration DB), detecte les derives architecturales et lance des audits periodiques. Bloque les mutations non conformes.

**Outils disponibles :**
- `git diff`, `git log`, `find`, `diff`
- `schema_validate()`, `drift_detect()`, `audit_report()`
- `sqlite3 architecture.db`, `tree`

**Auto-trigger :** Oui - pre-mutation (avant tout commit touchant la structure), audit periodique toutes les 24h, et sur alerte de derive detectee par monitoring.

---

### domino-optimizer

**Description :** Optimise les chaines domino. Analyse les 877+ benchmarks, identifie les chaines depassant 5000ms, propose des optimisations (parallelisation, cache, skip conditionnel). Maintient le score de performance global.

**Outils disponibles :**
- `sqlite3 benchmarks.db`, `jq`, `bc`
- `domino-engine benchmark`, `domino-engine optimize`
- `flame_graph()`, `critical_path_analysis()`

**Auto-trigger :** Oui - apres chaque benchmark (si temps > 5000ms), et analyse batch quotidienne a 03h00. Alerte si degradation > 15% vs baseline.

---

### ia-flow

**Description :** Moniteur des flux IA. Assure la separation I/O-bound vs CPU-bound, gere les politiques de backpressure, optimise l'utilisation asyncio/ProcessPool. Previent la saturation des queues et le starvation des workers.

**Outils disponibles :**
- `asyncio.Queue`, `ProcessPoolExecutor`, `ThreadPoolExecutor`
- `backpressure_policy()`, `queue_depth_monitor()`
- `psutil`, `htop`, `py-spy`

**Auto-trigger :** Oui - monitoring continu. Alerte quand queue depth > 100, CPU worker starvation > 30s, ou backpressure activee.

---

### jarvis-system-agent

**Description :** Agent systeme principal du cluster JARVIS. Health check complet des machines M1 (Creatrice), M2 et Server. Optimisation VRAM (allocation GPU dynamique), ZRAM (compression memoire), PBO (Precision Boost Overdrive Ryzen).

**Outils disponibles :**
- `nvidia-smi`, `rocm-smi`, `sensors`, `lscpu`
- `zramctl`, `swapon/swapoff`, `cpupower`
- `ssh M2/Server`, `cluster_health_report()`

**Auto-trigger :** Oui - healthcheck toutes les 60s, rapport complet toutes les 5min. Alerte immediate si node unreachable ou VRAM > 95%.

---

### security-reviewer

**Description :** Auditeur securite base sur OWASP Top 10. Detection de secrets en clair dans le code, analyse des risques d'injection (SQL, command, XSS), scan des ports exposes, verification des permissions fichiers et conteneurs.

**Outils disponibles :**
- `nmap`, `ss -tlnp`, `ufw status`, `fail2ban-client status`
- `trufflehog`, `gitleaks`, `find -perm`
- `bandit` (Python), `npm audit` (Node), `docker scan`

**Auto-trigger :** Non - declenchement manuel ou planifie (audit hebdomadaire dimanche 02h00). Alerte immediate si secret detecte dans un commit.

---

### system-health-monitor

**Description :** Moniteur de sante systeme complet. Produit un rapport structure couvrant CPU (charge, frequence, temperature), RAM (usage, swap, ZRAM), GPU (VRAM, temperature, utilisation), services (systemd, docker), zombies et reseau.

**Outils disponibles :**
- `top`, `free -h`, `nvidia-smi --query-gpu=*`, `sensors`
- `systemctl list-units --failed`, `docker ps`, `ps aux`
- `ip addr`, `ss -s`, `ping`, `ethtool`

**Auto-trigger :** Oui - rapport toutes les 60s (leger), rapport complet toutes les 5min. Escalade vers incident-responder si seuil critique depasse.

---

### task-decomposer-prime

**Description :** Decomposeur de taches complexes multi-domaines. Prend une requete complexe (ex: "deploie la v2 avec migration DB et notification Slack") et la decompose en etapes orchestrees avec dependances, parallelisme et points de validation.

**Outils disponibles :**
- `decompose()`, `dependency_graph()`, `parallel_plan()`
- `validate_step()`, `rollback_plan()`
- `task_queue_planner`, `skill_advisor`

**Auto-trigger :** Oui - quand une requete est classee "complexe" (> 3 domaines ou > 5 etapes estimees) par le flow-controller.

---

## Plugin jarvis-turbo (14 agents)

### jarvis-auditor

**Description :** Audit complet et continu du systeme JARVIS. Verifie la coherence des configurations, l'integrite des bases de donnees, la conformite des logs, et produit des rapports d'audit detailles avec scoring.

**Outils disponibles :** `sqlite3`, `jq`, `diff`, `sha256sum`, `audit_score()`

**Auto-trigger :** Oui - audit continu toutes les 6h, audit complet hebdomadaire.

---

### jarvis-auto-improver

**Description :** Agent d'amelioration automatique. Analyse les patterns repetitifs, les goulots d'etranglement et les erreurs recurrentes pour proposer et appliquer des ameliorations (config, scripts, workflows).

**Outils disponibles :** `pattern_analyze()`, `bottleneck_detect()`, `apply_improvement()`, `rollback()`

**Auto-trigger :** Oui - apres chaque cycle de production, analyse batch quotidienne.

---

### jarvis-auto-scaler

**Description :** Scaling automatique des ressources JARVIS. Ajuste le nombre de workers, la taille des pools, les limites memoire et les allocations GPU en fonction de la charge temps reel.

**Outils disponibles :** `scale_workers()`, `adjust_pool()`, `gpu_allocate()`, `cgroup_limit()`

**Auto-trigger :** Oui - charge > 80% (scale up) ou < 20% (scale down), evaluation toutes les 30s.

---

### jarvis-backpressure

**Description :** Gestion backpressure avancee. Detecte la saturation des queues, active le throttling, redirige le trafic, et gere les politiques de rejet gracieux pour eviter les cascades de pannes.

**Outils disponibles :** `queue_monitor()`, `throttle()`, `redirect_traffic()`, `graceful_reject()`

**Auto-trigger :** Oui - queue depth > seuil configurable (defaut: 50), latence P99 > 10s.

---

### jarvis-browser

**Description :** Agent navigateur central. Coordonne les operations BrowserOS, gere les sessions, le pool d'onglets, et orchestre les workflows multi-pages avec gestion d'erreurs et retry.

**Outils disponibles :** `take_snapshot`, `navigate_page`, `click`, `fill`, `evaluate_script`, `save_screenshot`

**Auto-trigger :** Oui - tache necessitant interaction navigateur detectee.

---

### jarvis-cluster-health

**Description :** Sante du cluster JARVIS (M1/M2/Server). Heartbeat inter-nodes, synchronisation configs, detection split-brain, failover automatique, rapport de sante consolide.

**Outils disponibles :** `heartbeat()`, `sync_config()`, `detect_split_brain()`, `failover()`, `ssh`

**Auto-trigger :** Oui - heartbeat toutes les 10s, rapport consolide toutes les 5min.

---

### jarvis-code-reviewer

**Description :** Revue de code automatique. Analyse les diffs, detecte les anti-patterns, verifie la conformite aux conventions JARVIS, suggere des ameliorations et bloque les merges non conformes.

**Outils disponibles :** `git diff`, `ast_analyze()`, `pattern_check()`, `convention_verify()`, `review_report()`

**Auto-trigger :** Oui - sur chaque PR ou commit dans les repos surveilles.

---

### jarvis-devops

**Description :** Agent DevOps complet. Gestion CI/CD, deployements, rollbacks, monitoring pipeline, gestion des artefacts et des environnements (dev, staging, prod).

**Outils disponibles :** `gh actions`, `docker build/push`, `deploy()`, `rollback()`, `artifact_manage()`

**Auto-trigger :** Non - declenchement sur push tag ou workflow dispatch.

---

### jarvis-flow-dispatcher

**Description :** Dispatcher de flux. Route les requetes vers le bon agent/skill/plateforme en fonction du contexte, des priorites et des capacites disponibles. Gere le load balancing inter-agents.

**Outils disponibles :** `route()`, `balance_load()`, `priority_sort()`, `capacity_check()`

**Auto-trigger :** Oui - chaque requete entrante passe par le dispatcher.

---

### jarvis-gpu-manager

**Description :** Gestionnaire GPU avance. Allocation VRAM dynamique, scheduling des taches GPU, monitoring temperature/utilisation, reset automatique, gestion multi-GPU (6 GPUs sur M1).

**Outils disponibles :** `nvidia-smi`, `cuda_malloc()`, `gpu_schedule()`, `gpu_reset()`, `vram_allocate()`

**Auto-trigger :** Oui - monitoring continu, alerte VRAM > 90% ou temperature > 85C.

---

### jarvis-multi-platform-router

**Description :** Routeur multi-plateforme. Decide si une tache doit aller sur Claude, Gemini ou BrowserOS en fonction du type de tache, du cout, de la latence et des capacites specifiques.

**Outils disponibles :** `platform_score()`, `cost_estimate()`, `latency_predict()`, `route_to_platform()`

**Auto-trigger :** Oui - tache multi-plateforme ou tache sans plateforme explicite.

---

### jarvis-quality-gate

**Description :** Porte qualite. Valide les sorties avant livraison : tests unitaires, integration, performance, securite. Bloque si qualite insuffisante, genere rapport de conformite.

**Outils disponibles :** `run_tests()`, `performance_check()`, `security_scan()`, `quality_score()`, `gate_decision()`

**Auto-trigger :** Oui - avant chaque deploiement ou livraison de resultat critique.

---

### jarvis-task-balancer

**Description :** Equilibreur de charge des taches. Repartit les taches entre les workers disponibles en tenant compte de l'affinite, des ressources et des deadlines. Previent la surcharge d'un worker unique.

**Outils disponibles :** `balance()`, `affinity_check()`, `deadline_sort()`, `worker_capacity()`

**Auto-trigger :** Oui - quand > 5 taches en parallele ou worker a > 80% capacite.

---

### jarvis-voice-controller

**Description :** Controleur vocal JARVIS. Traduit les commandes vocales en actions systeme, gere le pipeline STT/TTS, les macros vocales (898 commandes), et l'apprentissage de nouvelles commandes.

**Outils disponibles :** `stt_process()`, `tts_generate()`, `macro_execute()`, `learn_command()`, `jarvis-tts.sh`

**Auto-trigger :** Oui - activation vocale permanente ("JARVIS" wake word).

---

### jarvis-github-manager

**Description :** Agent autonome de gestion GitHub Turbo31150. Audite 40 repos, organise descriptions+topics, genere badges et READMEs via IA locale (LM Studio), genere logos via IA web (AI Studio/ChatGPT) en utilisant BrowserOS/Chrome DevTools MCP. Workflow 5 phases : audit → fix → beautify → contenu → rapport.

**Outils disponibles :** `gh api`, `gh repo edit`, `curl LM Studio :1234`, `mcp__claude-in-chrome__*`, `xdotool`, `xclip`

**Auto-trigger :** Oui - tache planifiee quotidienne 7h via systemd timer. Declenchement aussi sur mots : github, repo, organize, beautify, readme, badge.

---

## Nouveaux Services Systemd (Session 2026-03-29)

| Service | Role | Type | Frequence |
|---------|------|------|-----------|
| jarvis-sqlite-turbo | Applique PRAGMA turbo (WAL+mmap+cache) a toutes les bases | timer | toutes les 6h |
| jarvis-zombie-reaper | Nettoie les processus zombies | timer | toutes les 5min |
| jarvis-daily-benchmark | Benchmark quotidien LM Studio+Ollama+SQLite+NVMe | timer | tous les jours 6h |
| jarvis-gpu-oc | Overclock memoire +500MHz RTX 3080+RTX 2060 | oneshot boot | au demarrage |
| jarvis-ik-llama | ik_llama.cpp serveur (layer split, flash-attn, port 1235) | service | on-demand |
| jarvis-speculative | Speculative decoding (draft gemma-3-4b → target deepseek, port 1237) | service | on-demand |
| jarvis-vllm | vLLM 0.18.0 serveur (tensor-parallel=2, port 1236) | service | on-demand |
| jarvis-github-manager | Claude Code planifie : audit+fix GitHub repos | timer | tous les jours 7h |

## Statistiques Globales

| Metrique | Valeur |
|----------|--------|
| Total agents | 928 |
| SQL (etoile.db patterns) | 38 |
| Claude Code (plugins + core) | 140 |
| Gemini CLI (skills + routing) | 85 |
| Core Python | 15 |
| COWORK scripts autonomes | 579 |
| Domino chains | 71 |
| Auto-trigger actifs | 20 |
| Agents critiques (toujours actifs) | 6 |
| Services systemd JARVIS | 32 (22 services + 10 timers) |
| Backends inference | 4 (LM Studio :1234, ik-llama :1235, vLLM :1236, speculative :1237) |
| CLIs OMEGA | 12 operationnels |
| Apprentissage cumule | 426,859 entrees (self_improve_log) |
| COWORK missions traitees | 34,698 |
