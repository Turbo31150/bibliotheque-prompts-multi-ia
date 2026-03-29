# Gemini CLI — Catalogue Complet 85 Skills

> Export complet des skills Gemini CLI JARVIS OMEGA v14.1
> 85 skills | 80 avec OpenClaw | Auto-trigger par mots-cles

---

## SYSTEME & MONITORING (15 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| jarvis-flow-controller | Directive premiere JARVIS — controle flux, distribution taches | Auto-trigger a chaque tache |
| jarvis-orchestrator | Orchestre toutes les taches entre BrowserOS, OpenClaw, M1, M2, M3 | "dispatch", "orchestre", "route" |
| production-monitor | Surveille l'etat de production des services et du runtime | "status", "health check", "etat" |
| system-crash-guardian | Detection crash, respawn loop, systeme non-responsive | Auto-trigger sur crash |
| system-stabilization-mode | Stabilisation — keyboard lag, services crash-loop, zombies | "systeme instable", "lag" |
| zombie-cleanup | Nettoyage processus zombies accumules | "zombie", "defunct", ">10 zombies" |
| ram-pressure-handler | RAM > 80%, swap, OOM killer | Auto-trigger RAM haute |
| gpu-crash-recovery | Recuperation anomalies GPU (NVRM, Xid, Thermal) | Auto-trigger erreur GPU |
| boot-sequencer | Demarrage ordonne JARVIS par 8 vagues | "boot", "demarrage" |
| service-auto-repair | Reparation service systemd failed | Auto-trigger service crash |
| container-module-architecture | Deploiement services, containerisation | "deploy", "container" |
| rescue-mode-switcher | Bascule TTY3 / GUI desktop | "rescue", "tty" |
| network-degradation | Detection degradation reseau, downshift | Auto-trigger reseau |
| auto-scaler | Scaling GPU/cluster quand charge augmente | "scale", "load" |
| timeshift-backup | Snapshots systeme avant/apres changements | "backup", "snapshot" |

## CLUSTER & ROUTING (8 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| jarvis-cluster | Gestion complete du cluster M1/M2/M3/OL1 | "cluster", "noeud" |
| jarvis-full-system | Systeme complet JARVIS | "full system", "tout le systeme" |
| task-distributor | Distribution taches entre GPUs, cluster, APIs | "distribue", "repartit" |
| openclaw-router | Routage backend via OpenClaw (40 agents) | "openclaw", "agent", "route" |
| skill-advisor | Conseils de routing entre skills/plateformes | Auto-trigger avec chaque skill |
| jarvis-debugger | Debug systeme JARVIS | "debug", "erreur" |
| distributed-workflow | Workflow distribue multi-IA (ChatGPT, Claude, Gemini, M2/M3) | "distribue", "multi-ia" |
| pipeline-builder | Creation pipelines automation, chaines domino | "pipeline", "domino" |

## SECURITE (5 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| security-review | Audit securite cluster, ports, firewall | "securite", "audit" |
| security-best-practices | Review securite par langage et framework | "best practices securite" |
| security-threat-model | Threat modeling du codebase | "threat model", "menaces" |
| security-ownership-map | Cartographie ownership securite git | "ownership", "bus factor" |
| incident-learner | Extraction lecons post-incident | Auto-trigger post-incident |

## DONNEES & MEMOIRE (6 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| sql-memory-reader | Lecture SQLite JARVIS (etoile.db, jarvis.db) | "sql", "sqlite", "base", "table" |
| file-log-reader | Lecture fichiers et logs systeme | "log", "fichier", "erreur" |
| auto-learn | Apprentissage automatique des preferences | Auto-trigger feedback |
| comet-intelligence | Intelligence Perplexity via Comet MCP | "recherche", "perplexity" |
| prompt-alimentation | Generation et gestion de prompts | "prompt", "genere prompt" |
| task-queue-planner | Gestion file de taches, priorites, backlog | "queue", "taches", "backlog" |

## WEB & BROWSER (12 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| browseros-operator | Gestion workspace BrowserOS, tabs, sessions | "browseros", "workspace", "tab" |
| browser-session-curator | Maintenance sessions web, nettoyage tabs | "session", "onglets", "nettoie" |
| retrieval-web | Extraction contenu web, scraping, URLs | "page", "url", "extrait" |
| deep-research | Recherche multi-sources avec rapport HTML | "recherche", "investigate" |
| extract-data | Extraction donnees structurees (CSV, JSON) | "extrait donnees", "scrape" |
| summarize-page | Resume page web en markdown | "resume page", "digest" |
| save-page | Sauvegarde PDF de pages web | "sauve page", "PDF" |
| monitor-page | Surveillance changements sur page web | "surveille page", "track" |
| fill-form | Remplissage intelligent de formulaires web | "remplis formulaire" |
| manage-bookmarks | Organisation bookmarks, deduplication | "bookmarks", "favoris" |
| organize-tabs | Groupement et nettoyage d'onglets | "organise tabs", "trie onglets" |
| read-later | Bookmark + PDF pour lecture ulterieure | "lis plus tard", "save" |

## BUSINESS & FREELANCE (8 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| codeur-operator | Gestion Codeur.com — projets, propositions | "codeur", "mission", "freelance" |
| codeur-scanner | Scanner projets Codeur.com IA/automatisation | Auto-trigger planifie |
| linkedin-operator | Veille, posts, engagement LinkedIn | "linkedin", "post", "contenu" |
| linkedin-engage | Engagement LinkedIn — commentaires, reponses | "engage linkedin" |
| linkedin-physical-publisher | Publication LinkedIn via xdotool/xclip | "publie linkedin" |
| prospect-clients | Prospection multi-canal (Codeur, LinkedIn, Malt) | "prospection", "clients" |
| validation-consensus | Validation multi-source, arbitrage | "valide", "verifie", "consensus" |
| ai-consensus | Consensus multi-IA (local + web) | "consensus", "compare IA" |

## DEVELOPPEMENT (5 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| codex-cli-builder | Construction CLI/scripts via Codex | "codex", "refactor", "fix" |
| project-architect | Architecture de features/projets | "architecture", "plan projet" |
| auto-debug | Debug iteratif automatique | "debug", "erreur", "fix" |
| compare-prices | Comparaison prix multi-retailers | "compare prix", "best deal" |
| find-alternatives | Recherche alternatives produits | "alternative", "similaire" |

## VOCAL (3 skills)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| voice-first-operator | Commandes vocales, controle sans clavier | "vocal", "voix", "whisper" |
| voice-wake-porcupine | Wake word detection (Porcupine) | Auto-trigger boot |
| screenshot-walkthrough | Capture screenshots pour documentation | "screenshot", "walkthrough" |

## TRIGGER MAP (1 skill)

| Skill | Description | Prompt d'activation |
|-------|-------------|---------------------|
| browseros-skill-triggers | Dictionnaire 18 skills auto-declenchement par mots-cles FR/EN | Auto-trigger sur chaque message |

---

## AGENTS MAITRES OMEGA (6 agents couleur)

| Agent | Couleur | Role | Workflow IA |
|-------|---------|------|-------------|
| omega-dev-agent | VERT | Ingenierie, TDD, Refactoring | ChatGPT → Claude → Gemini |
| omega-analysis-agent | BLEU | Recherche, Due Diligence, Veille | Perplexity → Claude → ChatGPT |
| omega-system-agent | JAUNE | DevOps, SRE, Backups, Monitoring | Claude → Claude Code → n8n |
| omega-security-agent | ROUGE | Audit, CVE, Incidents, Hardening | Gemini CLI → Claude → Perplexity |
| omega-docs-agent | CYAN | Documentation, Vulgarisation, Memory | Gemini CLI → Claude → ChatGPT |
| omega-trading-agent | MAGENTA | Marche, Backtesting, Signaux Algo | Perplexity → ChatGPT → Claude |

---

## OMEGA CLI (j.py) — Orchestrateur unifie

| Commande | Description |
|----------|-------------|
| `j status` | Dashboard cluster + GPU + services |
| `j heal` | Auto-reparation (zombies, ports, services) |
| `j flow` | Check flux cognitif (charge → routing) |
| `j sync` | Synchronisation git + configs + agents |
| `j cog` | Audit intelligence systeme |
| `j agents` | Gestion cluster des 6 maitres |
| `j cowork` | Gestion des 662+ missions |
| `j memory` | Recherche cognitive locale |
| `j code` | Lance Claude Code |
| `j voice test` | Test pipeline vocal |

---

## MCP SERVERS (12)

| Serveur | Type | Role |
|---------|------|------|
| jarvis-mcp | Python | Orchestrateur 87 outils |
| jarvis-lmstudio | Python | Bridge LM Studio |
| linux-admin | Python | Gestion systemd/logs |
| powershell | npx | Scripting objet |
| domino-mcp | SSE | Pont chaines domino |
| filesystem | npx | Lecture/ecriture fichiers |
| memory | npx | Knowledge graph |
| sqlite | npx | Acces direct jarvis.db |
| context7 | npx | Documentation live |
| sequential-thinking | npx | Raisonnement structure |
| docker | npx | Gestion conteneurs |
| puppeteer | npx | Browser automation |

---

## TOTAUX OMEGA v14.1

```
Gemini CLI Skills:    85
Claude Code Skills:   89
Claude Code Agents:   31
Claude Code Commands: 20
OpenClaw Skills:      11 (40 commands)
SQL Agents:           38
SQL Triggers:         65
Domino Chains:        70
MCP Servers:          12 (Gemini) + 8 (Claude)
CLIs /usr/local/bin:  11
Cowork Scripts:       662+
Voice Commands:       850+
Total Automation:     600+ agents orchestres
```
