# Catalogue Complet des Skills JARVIS (52)

> Derniere mise a jour : 2026-03-28
> Plateformes : claude, gemini, browseros

---

## Systeme (9 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| system-crash-guardian | claude | Detecte et recupere les crashes systeme critiques (kernel panic, freeze, services morts) | Oui - signal SIGKILL/freeze detecte | `systemctl status`, `journalctl -xe`, `dmesg --level=emerg,crit` |
| system-stabilization-mode | claude | Active le mode stabilisation : reduit charge, desactive services non-essentiels, monitor renforce | Oui - quand 3+ incidents en 10min | `nice -n 19`, `systemctl stop`, `cpupower frequency-set` |
| boot-sequencer | claude | Orchestre la sequence de demarrage JARVIS : services, GPU, containers, healthcheck | Oui - au boot systeme | `systemctl start jarvis-*`, `nvidia-smi`, `docker-compose up` |
| rescue-mode-switcher | claude | Bascule en mode rescue : desactive GPU, reduit RAM, services minimaux | Oui - quand crash-guardian echoue | `systemctl isolate rescue.target`, `rmmod nvidia`, `swapoff -a` |
| gpu-crash-recovery | claude | Recuperation GPU : reset PCIe, reload driver, verification VRAM, rebind containers | Oui - nvidia-smi erreur ou GPU lost | `nvidia-smi -r`, `nvidia-smi --gpu-reset`, `echo 1 > /sys/bus/pci/.../reset` |
| ram-pressure-handler | claude | Gestion pression memoire : OOM killer config, ZRAM tuning, swap management, cleanup caches | Oui - RAM > 90% ou OOM imminent | `sysctl vm.oom_kill`, `zramctl`, `sync && echo 3 > /proc/sys/vm/drop_caches` |
| zombie-cleanup | claude | Detection et nettoyage processus zombies, orphelins, et processus bloques | Oui - zombies > 5 detectes | `ps aux \| grep Z`, `kill -9`, `wait`, `reap_children` |
| auto-scaler | claude | Ajuste dynamiquement les ressources selon la charge : CPU governor, GPU clocks, RAM allocation | Oui - charge > 80% ou < 20% | `cpupower frequency-set`, `nvidia-smi -lgc`, `cgroup` |
| timeshift-backup | claude | Snapshots systeme automatiques avant operations risquees, rotation, restauration | Oui - avant mutation critique | `timeshift --create`, `timeshift --list`, `timeshift --restore` |

---

## Infrastructure (5 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| network-degradation | claude | Detecte et compense les degradations reseau : downshift, latence, perte paquets | Oui - latence > 200ms ou perte > 5% | `ping`, `mtr`, `ethtool`, `tc qdisc`, `ip link` |
| container-module-architecture | claude | Gestion architecture conteneurs : build, deploy, scaling, healthcheck, cleanup images | Non | `docker build`, `docker-compose`, `docker system prune`, `docker stats` |
| security-review | claude | Audit securite : ports exposes, secrets en clair, permissions, certificats, firewall | Non - declenchement manuel | `nmap`, `ss -tlnp`, `find / -perm -4000`, `ufw status`, `fail2ban-client` |
| service-auto-repair | claude | Detecte services tombes et les repare : restart, reconfiguration, fallback | Oui - systemctl failed detecte | `systemctl restart`, `systemctl reset-failed`, `journalctl -u` |
| production-monitor | claude | Monitoring production continu : metriques, alertes, dashboards, SLA tracking | Oui - toutes les 60s | `curl health endpoints`, `docker stats`, `nvidia-smi`, `free -h` |

---

## Routage (7 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| jarvis-flow-controller | claude | Controleur principal des flux JARVIS : routing requetes, priorites, load balancing | Oui - chaque requete entrante | `route_request()`, `priority_queue`, `load_balance()` |
| skill-advisor | claude | Recommande le skill optimal pour une tache donnee, scoring multi-criteres | Oui - quand aucun skill explicite | `score_skills()`, `match_intent()`, `suggest_chain()` |
| task-distributor | claude | Distribue les taches entre plateformes claude/gemini/browseros selon capacites | Oui - tache multi-plateforme | `distribute()`, `platform_capacity()`, `affinity_check()` |
| jarvis-orchestrator | claude | Orchestrateur central : coordonne skills, agents, chains, gere lifecycle | Oui - permanent | `orchestrate()`, `chain_execute()`, `lifecycle_manage()` |
| openclaw-router | claude | Routage intelligent vers modeles LLM : selection modele, fallback, cost optimization | Oui - requete LLM | `model_select()`, `fallback_chain()`, `cost_estimate()` |
| task-queue-planner | claude | Planification file d'attente : priorites, deadlines, dependances, parallélisation | Oui - > 3 taches en attente | `queue_plan()`, `dependency_graph()`, `parallel_schedule()` |
| validation-consensus | claude | Validation par consensus multi-agents : vote, quorum, conflict resolution | Non - taches critiques uniquement | `vote()`, `quorum_check()`, `resolve_conflict()` |

---

## Browser (6 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| browseros-operator | browseros | Operateur principal BrowserOS : navigation, DOM, interactions, screenshots | Oui - tache browser | `take_snapshot`, `navigate_page`, `click`, `fill` |
| browser-session-curator | browseros | Gestion sessions navigateur : onglets, groupes, historique, bookmarks, cleanup | Non | `list_pages`, `group_tabs`, `search_history`, `create_bookmark` |
| linkedin-operator | browseros | Automatisation LinkedIn : publication, reactions, commentaires, profils, messages | Non - declenchement explicite | `navigate LinkedIn`, `fill post`, `click publish`, `xdotool` |
| codeur-operator | browseros | Automatisation plateformes dev : GitHub, GitLab, StackOverflow, documentation | Non | `navigate`, `fill`, `click`, `evaluate_script` |
| telegram-ops | browseros | Operations Telegram Web : messages, groupes, bots, fichiers | Non | `navigate Telegram`, `fill message`, `upload_file` |
| voice-first-operator | browseros | Interface voix-vers-browser : commandes vocales traduites en actions navigateur | Oui - commande vocale browser | `speech_to_action()`, `take_snapshot`, `click` |

---

## IA/DevOps (7 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| prompt-alimentation | claude | Alimentation et enrichissement des prompts : contexte, historique, RAG | Oui - chaque prompt | `enrich_prompt()`, `fetch_context()`, `rag_search()` |
| retrieval-web | claude | Recherche web intelligente : multi-sources, deduplication, summarization | Non | `web_search()`, `scrape()`, `summarize()` |
| codex-cli-builder | claude | Generation et execution de commandes CLI complexes, pipelines, scripts | Non | `build_command()`, `validate_syntax()`, `execute_safe()` |
| github-reader | claude | Lecture et analyse repos GitHub : issues, PRs, code, actions, releases | Non | `gh repo view`, `gh pr list`, `gh issue list`, `gh run list` |
| project-architect | claude | Architecture projet : structure, dependances, patterns, scaffolding | Non | `scaffold()`, `dependency_graph()`, `pattern_detect()` |
| pipeline-builder | claude | Construction pipelines CI/CD : GitHub Actions, Docker, tests, deploy | Non | `build_pipeline()`, `test_stage()`, `deploy_stage()` |
| github-manager | claude | Gestion GitHub Turbo31150 : audit 40 repos, organize topics/descriptions, beautify badges, generate README via IA locale, logos via IA web, social cards, tache planifiee 7h | Oui - mots github/repo/organize/beautify | `gh api`, `gh repo edit`, `curl LM Studio`, `mcp__claude-in-chrome__*` |

---

## Amelioration (6 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| production-improver | claude | Amelioration continue production : analyse metriques, suggestions, auto-apply | Oui - apres chaque cycle | `analyze_metrics()`, `suggest_improvement()`, `apply_patch()` |
| incident-learner | claude | Apprentissage depuis incidents : patterns, correlations, prevention proactive | Oui - apres chaque incident | `learn_pattern()`, `correlate()`, `update_knowledge()` |
| auto-debug | claude | Debug automatique : stack trace analysis, root cause, fix suggestion, apply | Oui - erreur detectee dans logs | `parse_stacktrace()`, `find_root_cause()`, `suggest_fix()` |
| auto-learn | claude | Apprentissage continu : nouvelles commandes, patterns utilisateur, optimisations | Oui - pattern repete 3+ fois | `learn_command()`, `pattern_detect()`, `optimize_flow()` |
| sql-memory-reader | claude | Lecture et analyse memoire SQL JARVIS : 73 bases, requetes, consolidation | Non | `sqlite3`, `SELECT`, `ANALYZE`, `VACUUM` |
| file-log-reader | claude | Lecture et analyse logs fichiers : parsing, patterns, alertes, rotation | Non | `tail -f`, `journalctl`, `logrotate`, `parse_log()` |

---

## Gemini Plugin (12 skills)

| Skill | Plateforme | Description | Auto-trigger | Commandes cles |
|-------|-----------|-------------|--------------|----------------|
| autotest-analysis | gemini | Analyse automatique des tests : couverture, regressions, flaky tests, rapports | Oui - apres CI/CD | `run_tests()`, `coverage_report()`, `flaky_detect()` |
| browser-workflow | gemini | Workflows navigateur complexes : multi-etapes, conditionnels, boucles | Non | `workflow_define()`, `step_execute()`, `condition_check()` |
| cluster-management | gemini | Gestion cluster JARVIS : M1/M2/Server, load balancing, failover, sync | Oui - heartbeat cluster | `cluster_status()`, `failover()`, `sync_nodes()` |
| continuous-improvement | gemini | Boucle amelioration continue : metriques, benchmarks, optimisations automatiques | Oui - toutes les 6h | `benchmark()`, `compare_baseline()`, `apply_optimization()` |
| demarrage | gemini | Sequence demarrage Gemini : init plugins, charge modeles, healthcheck | Oui - au boot Gemini | `init_plugins()`, `load_models()`, `healthcheck()` |
| failover-recovery | gemini | Recuperation failover : detection panne, basculement, restauration, verification | Oui - node down detecte | `detect_failure()`, `switch_node()`, `verify_recovery()` |
| mao-workflow | gemini | Workflows MAO (Maintenance Assistee par Ordinateur) : planification, execution, rapports | Non | `plan_maintenance()`, `execute_tasks()`, `generate_report()` |
| performance-tuning | gemini | Tuning performance : profiling, bottleneck detection, optimization, validation | Non | `profile()`, `detect_bottleneck()`, `tune()`, `validate()` |
| security-audit | gemini | Audit securite avance : vulnerabilites, compliance, remediation automatique | Non - planifie hebdomadaire | `scan_vulns()`, `check_compliance()`, `remediate()` |
| smart-routing | gemini | Routage intelligent requetes Gemini : modele optimal, context window, cost | Oui - requete Gemini | `route_request()`, `select_model()`, `estimate_cost()` |
| trading-pipeline | gemini | Pipeline trading : signaux, analyse, execution, risk management, reporting | Oui - signal marche | `analyze_signal()`, `risk_check()`, `execute_trade()`, `report()` |
| weighted-orchestration | gemini | Orchestration ponderee multi-agents : scoring, allocation, load balancing | Oui - multi-agent request | `weight_agents()`, `allocate()`, `balance_load()` |

---

## Statistiques Globales

| Metrique | Valeur |
|----------|--------|
| Total skills | 51 |
| Auto-trigger actifs | 31 |
| Plateforme Claude | 33 |
| Plateforme Gemini | 12 |
| Plateforme BrowserOS | 6 |
| Categories | 7 |
