# JARVIS OS — Bibliotheque de Prompts

> Index principal de la bibliotheque multi-IA. Derniere mise a jour : 2026-03-29.

## Vue d'ensemble

| Metrique | Valeur |
|----------|--------|
| Skills totaux | 56 (40 Claude Code + 15 plugin jarvis-turbo + 12 Gemini CLI natifs) |
| Agents | 928 total (38 SQL + 140 Claude + 85 Gemini + 15 Core + 579 Cowork + 71 Domino) |
| Commands | 14 (slash commands Claude Code) |
| Outils MCP | 60+ (BrowserOS 40+ / Chrome 15 / Strata 45+) |
| Chaines domino | 16 fichiers YAML + 1798 traces executees |
| Benchmarks | 930+ enregistres |
| Rapports de reparation | 767+ incidents documentes |
| Services systemd | 30 (22 services + 10 timers) |
| Backends inference | 4 (LM Studio :1234, ik-llama :1235, vLLM :1236, speculative :1237) |
| Tests pytest COWORK | 20 tests (5 suites) |
| Plateformes IA | 8 (Claude Code, Gemini CLI, BrowserOS, ChatGPT, Codex CLI, Perplexity, JARVIS Core, YOLO) |

---

## Structure

### SHARED/ — Catalogues communs (toutes IA)

| Fichier | Description |
|---------|-------------|
| [skills-catalog.md](SHARED/skills-catalog.md) | 51 skills detailles avec parametres et auto-triggers |
| [agents-catalog.md](SHARED/agents-catalog.md) | 22 agents detailles avec roles et dependances |
| [mcp-tools-catalog.md](SHARED/mcp-tools-catalog.md) | 60+ outils MCP par categorie |
| [domino-chains.md](SHARED/domino-chains.md) | 15 chaines YAML + 47 traces d'execution |
| [incident-patterns.md](SHARED/incident-patterns.md) | Patterns des 767 incidents documentes |

### SECURITE/ — Protection systeme

| Fichier | Description |
|---------|-------------|
| [skills-systeme.md](SECURITE/skills-systeme.md) | 9 skills securite/stabilite systeme |
| [domino-protection.md](SECURITE/domino-protection.md) | 10 chaines de protection automatique |
| [incident-response.md](SECURITE/incident-response.md) | Protocoles de reponse incident |

### Par Plateforme

| Dossier | Contenu |
|---------|---------|
| [CLAUDE_CODE/](CLAUDE_CODE/) | system-prompts, task-prompts, skills-pack, skills-dashboard |
| [GEMINI_CLI/](GEMINI_CLI/) | system-prompts, task-prompts, skills-pack |
| [BROWSER_OS/](BROWSER_OS/) | system-prompts, task-prompts, skills-pack |
| [CHATGPT/](CHATGPT/) | system-prompts, task-prompts, skills-pack |
| [CODEX_CLI/](CODEX_CLI/) | system-prompts, task-prompts, skills-pack |
| [PERPLEXITY/](PERPLEXITY/) | system-prompts, task-prompts, skills-pack |
| [JARVIS_CORE/](JARVIS_CORE/) | system-prompts, task-prompts |
| [YOLO_MODE/](YOLO_MODE/) | system-prompts |

---

## Matrice Skills x Plateformes

| Skill | Claude Code | Gemini CLI | BrowserOS | ChatGPT | Codex CLI | Perplexity |
|-------|:-----------:|:----------:|:---------:|:-------:|:---------:|:----------:|
| **Securite / Stabilite** | | | | | | |
| flow-controller | X | | | | X | |
| crash-guardian | X | | | | X | |
| system-crash-guardian | X | | | | | |
| ram-pressure-handler | X | | | | | |
| gpu-crash-recovery | X | | | | | |
| network-degradation | X | | | | | |
| system-stabilization-mode | X | | | | | |
| zombie-cleanup | X | | | | X | |
| service-auto-repair | X | | | | | |
| rescue-mode-switcher | X | | | | X | |
| **Orchestration** | | | | | | |
| jarvis-orchestrator | X | X | | | | |
| boot-sequencer | X | X | | | X | |
| task-queue-planner | X | X | | | | |
| task-distributor | X | | | | | |
| smart-routing | | X | | | | |
| weighted-orchestration | | X | | | | |
| pipeline-builder | X | | | | | |
| **Developpement** | | | | | | |
| codeur-operator | X | X | | | | |
| auto-debug | X | X | | | | |
| auto-learn | X | X | | | | |
| project-architect | X | X | | | | |
| autotest-analysis | | X | | | | |
| continuous-improvement | | X | | | | |
| performance-tuning | | X | | | | |
| skill-advisor | X | | | | | |
| container-module-architecture | X | | | | | |
| **Production / Monitoring** | | | | | | |
| production-monitor | X | X | | | | |
| production-improver | X | X | | | | |
| validation-consensus | X | X | | X | | |
| incident-learner | X | | | | | |
| security-audit | | X | | | | |
| security-review | X | | | | | |
| **Donnees / Memoire** | | | | | | |
| sql-memory-reader | X | X | | | | |
| file-log-reader | X | X | | | | |
| prompt-alimentation | X | X | | | | |
| **Web / Social** | | | | | | |
| browseros-operator | X | X | X | | | |
| browser-session-curator | X | X | X | | | |
| github-reader | X | X | | | | X |
| linkedin-operator | X | X | X | | | |
| telegram-ops | X | X | | | | |
| retrieval-web | X | X | | | | X |
| voice-first-operator | X | X | | | | |
| **Infrastructure** | | | | | | |
| cluster-management | | X | | | | |
| failover-recovery | | X | | | | |
| demarrage | | X | | | | |
| mao-workflow | | X | | | | |
| openclaw-router | X | X | | | | |
| codex-cli-builder | X | X | | | | |
| trading-pipeline | | X | | | | |
| timeshift-backup | X | | | | | |
| github-manager | X | | | | | |
| **BrowserOS natifs** | | | | | | |
| navigate | | | X | | | |
| click | | | X | | | |
| fill | | | X | | | |
| screenshot | | | X | | | |
| dom | | | X | | | |
| gmail | | | X | | | |
| slack | | | X | | | |
| github-web | | | X | | | |
| notion | | | X | | | |
| calendar | | | X | | | |
| jira | | | X | | | |
| linear | | | X | | | |
| telegram-web | | | X | | | |

---

## Utilisation

Pour copier les skills vers une IA :

1. **Copier `SHARED/`** — catalogues communs (valides pour toutes les plateformes)
2. **Copier le dossier de la plateforme cible** — ex: `CLAUDE_CODE/` pour Claude Code
3. **Copier `SECURITE/`** si l'IA gere la stabilite systeme (Claude Code, Codex CLI)

### Ordre de chargement recommande

```
1. SHARED/skills-catalog.md        (connaissance des skills)
2. SHARED/agents-catalog.md        (connaissance des agents)
3. SHARED/mcp-tools-catalog.md     (outils disponibles)
4. <PLATEFORME>/system-prompts.md  (personnalite IA)
5. <PLATEFORME>/skills-pack.md     (skills specifiques)
6. SECURITE/*                      (si applicable)
7. SHARED/domino-chains.md         (automatisations)
```

### Cluster JARVIS — Noeuds

| Noeud | Role | Modeles | Endpoint |
|-------|------|---------|----------|
| M1 (La Creatrice) | Principal — qualite | gemma-3-4b, qwen3.5-9b, deepseek-r1 | localhost:1234 |
| OL1 | Rapide — classif/embed | qwen2.5:1.5b, deepseek-r1:7b | localhost:11434 |
| M2 | Code specialise | deepseek-coder | 192.168.1.26:1234 |
| M3 | Raisonnement profond | deepseek-r1-qwen3-8b | 192.168.1.113:1234 |

### Routage par complexite

| Complexite | Noeud | Modele | Latence moy. |
|------------|-------|--------|--------------|
| low | OL1 | qwen2.5:1.5b | ~800ms |
| medium | M1 | gemma-3-4b | ~400ms |
| high | M1 | qwen3.5-9b | ~600ms |
| critical | consensus | tous les noeuds votent | ~2s |
