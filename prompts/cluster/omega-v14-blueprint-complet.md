# OMEGA v14.1 — Blueprint Complete de Reproduction

> Dossier de reproduction instantanee du cerveau numerique JARVIS OMEGA.
> 85 skills Gemini + 89 skills Claude + 70 domino chains + 38 agents SQL + 11 OpenClaw + 11 CLIs

---

## 1. PREREQUIS SYSTEME

```
OS: Ubuntu 24.04+ (derive Debian)
CPU: Multi-core (Ryzen 5700X3D recommande)
RAM: 46GB+ (16GB minimum)
GPU: 6x NVIDIA (RTX 3080 + RTX 2060 + 4x GTX 1660S = 46GB VRAM)
Runtime: Python 3.12+, Node.js v22+, Docker, Redis
CLI: claude, gemini, codex, lms, ollama, gh, browseros-cli
```

## 2. INSTALLATION MCP SERVERS

### Linux Admin (SRE Engine)
```bash
cd ~/Workspaces/jarvis-linux && source .venv/bin/activate
pip install linux-mcp-server
```
```json
"linux-admin": {
  "command": "/home/turbo/Workspaces/jarvis-linux/.venv/bin/python",
  "args": ["-m", "linux_mcp_server"]
}
```

### PowerShell OMEGA (Object Automation)
```bash
wget -q https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb && rm packages-microsoft-prod.deb
sudo apt update && sudo apt install -y powershell
```
```json
"powershell": {"command": "npx", "args": ["-y", "powershell-mcp"]}
```

### Filesystem + Memory + SQLite + Context7 + Sequential Thinking
```json
"filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/turbo", "/tmp"]},
"memory": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"]},
"sqlite": {"command": "npx", "args": ["-y", "mcp-sqlite", "/home/turbo/jarvis-linux/jarvis.db"]},
"context7": {"command": "npx", "args": ["-y", "@upstash/context7-mcp@latest"]},
"sequential-thinking": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]},
"docker": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-docker"]}
```

### Domino Bridge MCP
```json
"domino-mcp": {
  "command": "/home/turbo/Workspaces/jarvis-linux/.venv/bin/python",
  "args": ["/home/turbo/Workspaces/jarvis-linux/core/scripts/tools/domino_mcp_bridge.py"]
}
```

---

## 3. OMEGA CLI (j.py) — Orchestrateur Unifie

| Commande | Description | Action |
|----------|-------------|--------|
| `j status` | Dashboard cluster + GPU + services | Barres VRAM, sante noeuds |
| `j heal` | Auto-reparation zombies + ports + services | `j heal --force` pour purge radicale |
| `j flow` | Check flux cognitif (charge → routing) | GREEN/YELLOW/RED |
| `j sync` | Sync git Core + Prompts GitHub + Agents | `git pull --rebase` tous repos |
| `j cog` | Audit intelligence systeme | VRAM cumulee, agents actifs, uptime |
| `j agents` | Gestion cluster des 6 Maitres | Liste et switch agent |
| `j cowork` | Gestion 662+ missions forge | `j cowork run` / `j cowork clear` |
| `j memory` | Recherche cognitive locale | Cherche dans 397+ prompts + 320K lignes |
| `j code` | Lance Claude Code | Delegation implementation |
| `j voice test` | Test pipeline vocal | Calibration STT/TTS |

---

## 4. JARVIS CLIs (11 installes dans /usr/local/bin/)

| CLI | Commandes | Description |
|-----|-----------|-------------|
| `jarvis` | status, health, gpu, ask, security, clean, load, skills | CLI unifie |
| `jai` | 23 targets (m1, ol1, claude, gemini, codex, perplexity, chatgpt, aistudio, consensus, all-web...) | Dispatch IA |
| `jarvis-security` | scan, ports, secrets, guard | Audit securite |
| `jarvis-gpu` | status, load, unload, thermal, vram | GPU manager |
| `jarvis-cluster` | health, nodes, route, failover | Cluster ops |
| `jarvis-zombie` | list, kill, parents | Zombie cleaner |
| `jarvis-monitor` | snapshot, live, services | Monitoring |
| `jarvis-layers` | check, boot, boot-safe | Boot 9 couches |
| `jarvis-dispatch` | --list | Alias jai |
| `jarvis-decide` | predict, simulate, matrix, optimize, visualize | Decision engine vectoriel |
| `jarvis-boot` | start, stop | Boot legacy |

---

## 5. SLASH COMMANDS GEMINI CLI

### Gestion Agents Maitres
| Commande | Action | Description |
|----------|--------|-------------|
| `/agent-init` | `cat ~/.claude/agents/*.md` | Sync les 6 Agents Maitres |
| `/agent-switch` | `j agents` | Bascule vers un Maitre specifique |
| `/omega-mode` | `export MODE=AUTONOMOUS` | Autonomie totale sans confirmation |

### Controle Cluster & Hardware
| Commande | Action | Description |
|----------|--------|-------------|
| `/cluster-check` | `j status` | Diagnostic global M1/M2/M3/OL1 |
| `/gpu-status` | `nvidia-smi --query-gpu=...` | VRAM, Temp, Util des 6 GPUs |
| `/heal-cluster` | `j heal --force` | Purge ports + zombies |
| `/flow-check` | `j flow` | Charge CPU/RAM pour routage |
| `/diagnostic` | `j cog` | Audit cognitif complet |

### Moteurs IA & Inference
| Commande | Action | Description |
|----------|--------|-------------|
| `/models` | `lms ls && lms status` | Liste modeles charges |
| `/load-fast` | `j models load fast` | Charge Gemma-3 GPU Max |
| `/load-master` | `j models load master` | Charge Qwen-3.5 GPU Max |
| `/load-deep` | `j models load deep` | Charge DeepSeek-R1 GPU Max |
| `/unload-all` | `lms unload --all` | Purge totale VRAM |

### Serveurs MCP & Connecteurs
| Commande | Action | Description |
|----------|--------|-------------|
| `/mcp-list` | `cat .mcp.json` | 12+ serveurs MCP actifs |
| `/linux-admin` | `mcp:linux-admin` | Pilotage systemctl/journalctl |
| `/pwsh` | `mcp:powershell` | Scripting objet PowerShell |
| `/sequential` | `mcp:sequential-thinking` | Raisonnement decompose |
| `/domino` | `j domino list` | 70 chaines d'automatisation |

### Ingenierie & Automatisation
| Commande | Action | Description |
|----------|--------|-------------|
| `/code` | `j code` | Claude Code CLI |
| `/tasks` | `j tasks` | File d'attente Redis |
| `/sync` | `j sync` | Sync Git + Prompts + Agents |
| `/logs` | `j logs all` | Stream tous services jarvis-* |
| `/bench` | `j bench gpu` | Benchmark stress cluster |

### Web, Social & Cowork
| Commande | Action | Description |
|----------|--------|-------------|
| `/browse` | `j web [service]` | Ouvre IA web via BrowserOS |
| `/valise-run` | `j valise run [name]` | Pack automatisation BrowserOS |
| `/linkedin-pub` | `j linkedin publish` | Publication auto daemon |
| `/trading-scan` | `j trade scan` | Analyse technique multi-IA |
| `/cowork-run` | `j cowork run` | Cycle traitement Forge |
| `/memory` | `j memory [query]` | Recherche 397+ prompts |

### Parametres Critiques
```
--yolo           Desactive confirmations
--gpu max        Force chargement 6 GPUs
--checkpointing  Sauvegarde apres chaque succes
--127.0.0.1      Force interface locale
--nothink        Desactive thinking qwen3
--no_think       Desactive thinking ollama
```

---

## 6. AGENTS MAITRES OMEGA (6 couleurs)

| Agent | Couleur | Role | Workflow IA | Fichier |
|-------|---------|------|-------------|---------|
| omega-dev-agent | VERT | Ingenierie, TDD, Refactoring | ChatGPT → Claude → Gemini | `~/.claude/agents/omega-dev-agent.md` |
| omega-analysis-agent | BLEU | Recherche, Due Diligence, Veille | Perplexity → Claude → ChatGPT | `~/.claude/agents/omega-analysis-agent.md` |
| omega-system-agent | JAUNE | DevOps, SRE, Backups, Monitoring | Claude → Claude Code → n8n | `~/.claude/agents/omega-system-agent.md` |
| omega-security-agent | ROUGE | Audit, CVE, Incidents, Hardening | Gemini CLI → Claude → Perplexity | `~/.claude/agents/omega-security-agent.md` |
| omega-docs-agent | CYAN | Documentation, Vulgarisation, Memory | Gemini CLI → Claude → ChatGPT | `~/.claude/agents/omega-docs-agent.md` |
| omega-trading-agent | MAGENTA | Marche, Backtesting, Signaux Algo | Perplexity → ChatGPT → Claude | `~/.claude/agents/omega-trading-agent.md` |

---

## 7. DOMINO CHAINS (70) — Top 10 par impact

| Chain | Steps | Trigger | Impact |
|-------|-------|---------|--------|
| cli-system-health | 6 | cron:boot_check | Health complet via CLIs |
| cli-security-hardening | 6 | cron:daily_security | Audit + correction auto |
| cli-ai-consensus-dispatch | 5 | user:consensus_request | Consensus pondere |
| cli-gpu-auto-optimize | 4 | gpu:temperature > 75 | Thermal + GPU max |
| cli-freelance-optimizer | 5 | cron:freelance_scan | Scan + proposition |
| full-boot-sequence | 8 | system:boot | Demarrage 8 vagues |
| benchmark-self-improve | 6 | cron:benchmark | Auto-amelioration |
| freelance-pipeline | 5 | cron:freelance | Scan Codeur + propositions |
| content-pipeline | 4 | cron:content | Generation contenu LinkedIn |
| disaster-recovery | 6 | signal:disaster | Restauration complete |

---

## 8. DECISION ENGINE (jarvis-decide)

| Commande | Description |
|----------|-------------|
| `jarvis-decide predict` | Prediction actions optimales par contexte systeme |
| `jarvis-decide simulate -n 5000` | Monte Carlo 5000 trajectoires |
| `jarvis-decide matrix` | Matrices transition + eigenvalues |
| `jarvis-decide optimize` | Sequences optimales par 5 profils contexte |
| `jarvis-decide visualize` | PNG 4 panneaux (heatmap, transition, superposition, sequence) |

### Profils d'optimisation
| Contexte | Sequence optimale |
|----------|-------------------|
| Production stable | verification → writing-plans → ai-dispatch → smart-routing |
| Incident critique | verification → writing-plans → weighted-orchestration → brainstorming |
| Developpement | brainstorming → writing-plans → weighted-orchestration → ai-dispatch |
| Freelance actif | verification → weighted-orchestration → writing-plans → smart-routing |
| GPU sature | verification → writing-plans → weighted-orchestration → smart-routing |

---

## 9. POWER TOOLS STACK 2026

| Outil | Description | Installation |
|-------|-------------|-------------|
| Bottom (btm) | Moniteur systeme Rust ultra-rapide | `snap install bottom` |
| Nushell (nu) | Shell structure (JSON/Tableaux natifs) | `cargo install nu` |
| Zoxide (z) | Navigation intelligente dossiers | `cargo install zoxide` |
| Claude Code | CLI codage autonome | `npm install -g @anthropic-ai/claude-code` |
| Gemini CLI | CLI Google AI | `npm install -g @anthropic-ai/gemini` |
| Codex CLI | CLI OpenAI | `npm install -g codex` |
| LM Studio | Inference locale GPU | `lms` CLI |
| BrowserOS | Automatisation web 66 outils | `browseros-cli` |

---

## 10. PROCEDURE RESTAURATION RAPIDE (MODE YOLO)

```bash
# 1. Clone
git clone https://github.com/Turbo31150/jarvis-linux.git
git clone https://github.com/Turbo31150/bibliotheque-prompts-multi-ia.git

# 2. Dependances
cd jarvis-linux && python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install linux-mcp-server

# 3. Config MCP
cp .mcp.json ~/.claude/  # ou appliquer dans le projet

# 4. LM Studio GPU
lms server start
lms load deepseek/deepseek-r1-0528-qwen3-8b --gpu max -c 26000 -y

# 5. CLIs
sudo ln -sf $(pwd)/scripts/jarvis-cli.py /usr/local/bin/jarvis
sudo ln -sf $(pwd)/scripts/jarvis-ai-dispatch.py /usr/local/bin/jai
sudo ln -sf $(pwd)/scripts/jarvis-decision-engine.py /usr/local/bin/jarvis-decide
# ... (tous les CLIs)

# 6. Health check
jarvis status
jarvis-layers check

# 7. GO
j cowork run
```

---

## TOTAUX OMEGA v14.1

```
Gemini CLI Skills:      85
Claude Code Skills:     89
Claude Code Agents:     31
Claude Code Commands:   20
Gemini Slash Commands:  30+
OpenClaw Skills:        11 (40 commands)
SQL Agents Registry:    38
SQL Skill Triggers:     65
Domino Chains:          70
MCP Servers:            12 (Gemini) + 8 (Claude) = 20
CLIs /usr/local/bin:    11
Cowork Scripts:         662+
Voice Commands:         850+
Decision Engine:        27 skills vectorises, 7 dimensions
Bibliotheque Prompts:   346+ fichiers
Total Agents Orchestres: 600+
```

[STATUT] STABLE | [BLUEPRINT EXPORTED] | [REPRODUCTION READY]
