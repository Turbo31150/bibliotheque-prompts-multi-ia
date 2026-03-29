# Claude Code — Skills Pack

> 39 skills disponibles dans Claude Code. Derniere mise a jour : 2026-03-28.

---

## Skills (39)

### Securite et Stabilite (9 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 1 | `flow-controller` | Verifie le flux systeme JARVIS complet (CPU/RAM/GPU/services) | Toutes les 5 min via timer | Claude direct + shell |
| 2 | `crash-guardian` | Detecte et repare les crashs de services critiques | Sur event crash systemd | Claude direct |
| 3 | `system-crash-guardian` | Protection systeme complete avec escalade automatique | Sur alerte RAM > 90% ou kernel panic | Claude direct |
| 4 | `ram-pressure-handler` | Gestion pression memoire (kill selectif, swap, compression) | Sur RAM > 85% | Claude direct |
| 5 | `gpu-crash-recovery` | Recuperation apres crash GPU (reset driver, reload CUDA) | Sur erreur GPU detectee dans dmesg | Claude direct |
| 6 | `network-degradation` | Detection et contournement des degradations reseau | Sur latence > 500ms ou perte paquets > 5% | Claude direct |
| 7 | `system-stabilization-mode` | Mode stabilisation : reduit la charge, prioritise les services critiques | Sur instabilite detectee (3+ incidents/10min) | Claude direct |
| 8 | `zombie-cleanup` | Nettoyage des processus zombies et orphelins | Toutes les 15 min | Claude direct + shell |
| 9 | `service-auto-repair` | Reparation automatique des services systemd en echec | Sur service failed detecte | Claude direct |

### Orchestration (7 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 10 | `jarvis-orchestrator` | Orchestrateur principal — distribue les taches entre les IA | Sur nouvelle tache entrante | Claude + route Gemini |
| 11 | `boot-sequencer` | Sequence de demarrage JARVIS complete (services, LLM, MCP) | Au boot systeme | Claude direct + shell |
| 12 | `task-queue-planner` | Planification des taches dans la queue Redis | Sur accumulation > 5 taches | Claude + route Gemini |
| 13 | `task-distributor` | Distribution des taches selon poids et capacite des noeuds | Sur tache complexite > medium | Claude direct |
| 14 | `pipeline-builder` | Construction de pipelines domino dynamiques | Sur demande utilisateur | Claude direct |
| 15 | `rescue-mode-switcher` | Bascule en mode rescue (desactive services non-essentiels) | Sur instabilite critique | Claude direct + shell |
| 16 | `skill-advisor` | Recommande le meilleur skill pour une tache donnee | Sur tache ambigue | Claude direct |

### Developpement (5 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 17 | `codeur-operator` | Agent codeur — ecrit, modifie, refactore du code | Sur demande dev | Claude + route Gemini |
| 18 | `auto-debug` | Debug automatique (analyse logs, stack traces, propose fix) | Sur erreur detectee dans logs | Claude + route Gemini |
| 19 | `auto-learn` | Apprentissage continu depuis les logs et incidents | Toutes les heures | Claude + route Gemini |
| 20 | `project-architect` | Architecture projet (design patterns, structure, dependances) | Sur nouveau projet | Claude + route Gemini |
| 21 | `container-module-architecture` | Gestion architecture Docker/containers des modules | Sur modification docker-compose | Claude direct |

### Production et Monitoring (5 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 22 | `production-monitor` | Monitoring temps reel des services de production | Toutes les 2 min | Claude + route Gemini |
| 23 | `production-improver` | Amelioration continue des performances production | Sur benchmark en baisse | Claude + route Gemini |
| 24 | `validation-consensus` | Validation par consensus multi-noeud (quorum >= 0.65) | Sur tache critique | Claude + route Gemini |
| 25 | `incident-learner` | Apprend des incidents passes pour prevenir les futurs | Post-incident | Claude direct |
| 26 | `security-review` | Audit securite du code et des configurations | Sur commit sensible | Claude direct |

### Donnees et Memoire (3 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 27 | `sql-memory-reader` | Lecture memoire SQL (73 bases consolidees) | Sur requete donnees | Claude + route Gemini |
| 28 | `file-log-reader` | Lecture intelligente de fichiers logs (pattern matching) | Sur investigation | Claude + route Gemini |
| 29 | `prompt-alimentation` | Alimentation des prompts depuis la base de connaissances | Sur nouveau contexte | Claude + route Gemini |

### Web et Social (7 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 30 | `browseros-operator` | Operateur BrowserOS — pilotage navigateur complet | Sur tache web | Route BrowserOS |
| 31 | `browser-session-curator` | Gestion des sessions navigateur (onglets, historique, cookies) | Sur session degradee | Route BrowserOS |
| 32 | `github-reader` | Lecture repos GitHub (issues, PRs, code, actions) | Sur reference GitHub | Claude + route Gemini |
| 33 | `linkedin-operator` | Publication et interaction LinkedIn automatisee | Sur contenu pret | Route BrowserOS |
| 34 | `telegram-ops` | Operations Telegram (messages, channels, monitoring) | Sur event Telegram | Claude + route Gemini |
| 35 | `retrieval-web` | Recherche web intelligente (Perplexity, scraping, RAG) | Sur question necessitant web | Claude + route Gemini |
| 36 | `voice-first-operator` | Interface vocale prioritaire (STT + TTS + commandes) | Sur entree vocale | Claude + route Gemini |

### Infrastructure (3 skills)

| # | Skill | Description | Auto-trigger | Routage |
|---|-------|-------------|--------------|---------|
| 37 | `openclaw-router` | Routeur OpenClaw Gateway (ws://127.0.0.1:18789) | Sur skill OpenClaw | Claude + route Gemini |
| 38 | `codex-cli-builder` | Construction et execution de commandes Codex CLI | Sur tache shell complexe | Claude + route Gemini |
| 39 | `timeshift-backup` | Sauvegarde Timeshift automatique avant operations risquees | Avant operation critique | Claude direct |

---

## Agents Core (8)

| Agent | Fichier | Role |
|-------|---------|------|
| `orchestrator` | `core/agents/orchestrator.py` | Chef d'orchestre — distribue les taches, gere les priorites, coordonne les agents |
| `browseros_operator` | `core/agents/browseros_operator.py` | Pilote BrowserOS — execute les actions navigateur via API HTTP |
| `github_operator` | `core/agents/github_operator.py` | Operations GitHub — PRs, issues, reviews, actions CI/CD |
| `telegram_operator` | `core/agents/telegram_operator.py` | Operations Telegram — messages, monitoring channels, alertes |
| `sql_operator` | `core/agents/sql_operator.py` | Operations SQL — requetes, migrations, consolidation des 73 bases |
| `mail_operator` | `core/agents/mail_operator.py` | Operations email — lecture, envoi, tri automatique |
| `container_operator` | `core/agents/container_operator.py` | Operations Docker — build, deploy, health check containers |
| `network_operator` | `core/agents/network_operator.py` | Operations reseau — diagnostic, VPN, firewall, latence |

### Agents support

| Agent | Fichier | Role |
|-------|---------|------|
| `voice_router` | `core/agents/voice_router.py` | Routage commandes vocales vers le bon skill |
| `confidence` | `core/agents/confidence.py` | Calcul de confiance pour les reponses multi-noeud |
| `personas` | `core/agents/personas.py` | Gestion des personnalites IA (JARVIS, assistant, expert) |
| `memory_store` | `core/agents/memory_store.py` | Stockage et recuperation memoire conversationnelle |
| `retry_patterns` | `core/agents/retry_patterns.py` | Patterns de retry intelligents (backoff, circuit breaker) |

### Agents vocaux (voice module)

| Agent | Role |
|-------|------|
| `dictation_agent` | Dictee vocale avec correction temps reel |
| `navigation_agent` | Navigation systeme par commande vocale |
| `search_agent` | Recherche vocale multi-source |
| `automation_agent` | Macros et automatisations declenchees par la voix |

---

## Outils MCP disponibles

### BrowserOS (40+ outils)

| Categorie | Outils |
|-----------|--------|
| Navigation | `navigate_page`, `new_page`, `close_page`, `show_page`, `list_pages` |
| Interaction | `click`, `click_at`, `fill`, `hover`, `press_key`, `scroll`, `drag` |
| Formulaires | `select_option`, `check`, `uncheck`, `upload_file`, `handle_dialog` |
| Capture | `take_screenshot`, `take_snapshot`, `take_enhanced_snapshot`, `save_screenshot`, `save_pdf` |
| DOM | `get_dom`, `search_dom`, `get_page_content`, `get_page_links`, `evaluate_script` |
| Onglets | `group_tabs`, `ungroup_tabs`, `list_tab_groups`, `close_tab_group`, `update_tab_group` |
| Fenetres | `create_window`, `create_hidden_window`, `list_windows`, `activate_window`, `close_window`, `move_page` |
| Signets | `create_bookmark`, `search_bookmarks`, `get_bookmarks`, `update_bookmark`, `remove_bookmark`, `move_bookmark` |
| Historique | `get_recent_history`, `search_history`, `delete_history_url`, `delete_history_range` |
| Fichiers | `download_file` |
| Strata | `suggest_app_connection`, `suggest_schedule` (portail vers 45+ services) |
| Info | `browseros_info`, `get_active_page` |

### Claude-in-Chrome (15 outils)

| Outil | Fonction |
|-------|----------|
| `navigate` | Navigation URL dans Chrome |
| `read_page` | Lecture contenu page courante |
| `get_page_text` | Extraction texte brut |
| `find` | Recherche texte dans page |
| `form_input` | Remplissage formulaires |
| `computer` | Actions souris/clavier (Computer Use) |
| `javascript_tool` | Execution JavaScript arbitraire |
| `tabs_context_mcp` | Contexte onglets ouverts |
| `tabs_create_mcp` | Creation nouvel onglet |
| `switch_browser` | Basculer entre navigateurs |
| `read_console_messages` | Lecture console DevTools |
| `read_network_requests` | Lecture requetes reseau |
| `resize_window` | Redimensionnement fenetre |
| `gif_creator` | Creation GIF depuis actions |
| `shortcuts_execute` / `shortcuts_list` | Raccourcis clavier Chrome |

### Canva (28 outils)

Design graphique : `generate-design`, `create-design-from-candidate`, `export-design`, `get-design`, `get-assets`, `list-brand-kits`, `search-designs`, `start-editing-transaction`, `perform-editing-operations`, `commit-editing-transaction`, etc.

### Notion (13 outils)

Base de connaissances : `search`, `fetch`, `notion-create-pages`, `notion-create-database`, `notion-update-page`, `notion-create-comment`, `notion-get-comments`, `notion-get-users`, `notion-get-teams`, `notion-create-view`, `notion-move-pages`, etc.

### Google Calendar (9 outils)

Agenda : `gcal_list_events`, `gcal_create_event`, `gcal_update_event`, `gcal_delete_event`, `gcal_find_meeting_times`, `gcal_find_my_free_time`, `gcal_get_event`, `gcal_list_calendars`, `gcal_respond_to_event`.

### Comet / Perplexity (6 outils)

Recherche web : `comet_ask`, `comet_connect`, `comet_mode`, `comet_poll`, `comet_screenshot`, `comet_stop`.

---

## Chaines Domino declenchees par Claude Code (5)

| Chaine | Fichier YAML | Declencheur | Steps |
|--------|-------------|-------------|-------|
| **Service Crash Recovery** | `service-crash-recovery.yaml` | Service systemd en echec | flow-check → crash-guardian → service-auto-repair → validation |
| **RAM Pressure Cascade** | `ram-pressure-cascade.yaml` | RAM > 85% | ram-pressure-handler → zombie-cleanup → system-stabilization → flow-check |
| **GPU Error Cascade** | `gpu-error-cascade.yaml` | Erreur GPU dans dmesg | gpu-crash-recovery → service-auto-repair → benchmark-self-improve |
| **Code Error Debug** | `code-error-debug.yaml` | Erreur dans logs applicatifs | auto-debug → codeur-operator → autotest-analysis → validation |
| **Content Pipeline** | `content-pipeline.yaml` | Contenu pret a publier | prompt-alimentation → linkedin-operator → telegram-ops → production-monitor |

---

## Chemins cles

```
~/.claude/skills/                          # 100+ skills installes
~/Workspaces/jarvis-linux/core/agents/     # 8 agents core
~/Workspaces/jarvis-linux/core/domino/     # Moteur domino + router multi-IA
~/Workspaces/jarvis-linux/core/llm/        # Router modeles (M1/OL1/M2/M3)
~/Workspaces/jarvis-linux/modules/voice/   # Module vocal (skills + agents)
~/Workspaces/jarvis-linux/scripts/         # Scripts shell executables
```
