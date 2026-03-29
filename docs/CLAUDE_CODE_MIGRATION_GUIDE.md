# Claude Code — Guide de Migration Complète

> Ce document liste TOUTE la configuration Claude Code actuelle pour la reproduire sur une nouvelle machine.

## 1. Installation Claude Code

```bash
# Installer Claude Code
npm install -g @anthropic-ai/claude-code

# OU via curl
curl -fsSL https://cli.anthropic.com/install.sh | sh
```

## 2. Configuration Globale (~/.claude.json)

### MCP Servers (6 configurés)

```bash
claude mcp add --transport http jarvis-ws http://127.0.0.1:9742/mcp --scope user
claude mcp add --transport http jarvis-proxy http://127.0.0.1:18800/mcp --scope user
claude mcp add --transport http jarvis-openclaw http://127.0.0.1:18789/mcp --scope user
claude mcp add --transport http browseros http://127.0.0.1:9001/mcp --scope user
claude mcp add --transport http mon-flask-mcp http://127.0.0.1:8080/mcp --scope user
# GitHub MCP (configuré via claude.ai)
```

## 3. Settings (~/.claude/settings.json)

### Permissions (tout autorisé pour dev)

```json
{
  "permissions": {
    "allow": [
      "Bash(*)", "Read(*)", "Write(*)", "Edit(*)", "Glob(*)", "Grep(*)",
      "Agent(*)", "WebFetch(*)", "WebSearch(*)", "NotebookEdit(*)", "Skill(*)",
      "mcp__jarvis__*", "mcp__claude_ai_Google_Calendar__*",
      "mcp__claude_ai_Canva__*", "mcp__claude_ai_Notion__*",
      "mcp__github__*", "mcp__browseros__*",
      "mcp__plugin_playwright_playwright__*"
    ],
    "deny": []
  },
  "allowedDirs": ["/home/turbo/**", "/tmp/**", "/var/log/**", "/opt/**"],
  "voiceEnabled": true
}
```

### Plugins Activés (22)

```json
{
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "context7@claude-plugins-official": true,
    "code-review@claude-plugins-official": true,
    "github@claude-plugins-official": true,
    "feature-dev@claude-plugins-official": true,
    "code-simplifier@claude-plugins-official": true,
    "playwright@claude-plugins-official": true,
    "typescript-lsp@claude-plugins-official": true,
    "commit-commands@claude-plugins-official": true,
    "claude-md-management@claude-plugins-official": true,
    "security-guidance@claude-plugins-official": true,
    "pr-review-toolkit@claude-plugins-official": true,
    "pyright-lsp@claude-plugins-official": true,
    "claude-code-setup@claude-plugins-official": true,
    "agent-sdk-dev@claude-plugins-official": true,
    "plugin-dev@claude-plugins-official": true,
    "explanatory-output-style@claude-plugins-official": true,
    "skill-creator@claude-plugins-official": true,
    "learning-output-style@claude-plugins-official": true,
    "playground@claude-plugins-official": true,
    "pinecone@claude-plugins-official": true
  }
}
```

## 4. Plugin Local : jarvis-turbo (v3.0.0)

**Emplacement** : `~/.claude/plugins/local/jarvis-turbo/`

### plugin.json

```json
{
  "name": "jarvis-turbo",
  "version": "3.0.0",
  "description": "JARVIS Cluster — skills, agents, commands, hooks, BrowserOS",
  "author": "Turbo31150"
}
```

### Skills (11)

| Skill | Rôle |
|-------|------|
| `autotest-analysis` | Analyse des résultats de tests |
| `cluster-management` | Gestion cluster M1/M2/M3/OL1 |
| `continuous-improvement` | Boucle d'auto-amélioration |
| `failover-recovery` | Récupération et failover |
| `mao-workflow` | Workflow Multi-Agent Orchestration |
| `performance-tuning` | Optimisation des performances |
| `security-audit` | Audit de sécurité |
| `smart-routing` | Routage intelligent 17 domaines |
| `trading-pipeline` | Pipeline trading OMEGA v2.3 |
| `weighted-orchestration` | Orchestration pondérée consensus |
| `browser-workflow` | Automation BrowserOS |

### Agents (7)

| Agent | Rôle |
|-------|------|
| `jarvis-auditor` | Audit système complet |
| `jarvis-auto-improver` | Auto-amélioration continue |
| `jarvis-code-reviewer` | Review de code multi-modèle |
| `jarvis-gpu-manager` | Gestion GPU (thermal, VRAM, persistence) |
| `jarvis-voice-controller` | Contrôle vocal pipeline |
| `jarvis-devops` | DevOps et auto-heal |
| `jarvis-browser` | Automation BrowserOS CDP |

### Commands (12 slash commands)

| Commande | Rôle |
|----------|------|
| `/cluster-check` | Vérification santé cluster |
| `/gpu-status` | Status GPU détaillé |
| `/consensus` | Vote multi-IA |
| `/trading-scan` | Scan trading MEXC |
| `/heal-cluster` | Auto-réparation |
| `/ask-ai` | Question au cluster |
| `/browse` | Automation navigateur |
| `/diagnostic` | Diagnostic système |
| `/models` | Liste modèles chargés |
| `/os` | Infos système |
| `/trade` | Commande trading |
| `/content` | Génération contenu |

### Hooks (2)

| Hook | Trigger | Rôle |
|------|---------|------|
| `gpu-thermal-guard` | PostToolUse | Vérifie température GPU après chaque commande |
| `session-cluster-check` | SessionStart | Health check cluster au démarrage |

## 5. Memory Files (9 fichiers)

**Emplacement** : `~/.claude/projects/-home-turbo/memory/`

| Fichier | Contenu |
|---------|---------|
| `MEMORY.md` | Index de toutes les mémoires |
| `user_language.md` | Préférence française |
| `user_profile.md` | Profil Turbo, GitHub, préférences |
| `user_machine_m1.md` | Hardware M1 La Créatrice |
| `project_voice_linux_control.md` | Pilotage vocal Linux |
| `project_jarvis_os.md` | JARVIS OS intégration Linux |
| `project_jarvis_linux_port.md` | Portage Windows→Linux |
| `project_portage_linux_progress.md` | Progression portage |
| `project_jarvis_v15_session.md` | Session v12.4→v15.0 complète |

## 6. CLAUDE.md (Projet)

**Emplacement** : `/home/turbo/jarvis-linux/CLAUDE.md` (105 lignes)

Contient : version, architecture, conventions code, fichiers critiques, cluster access, règles, scripts utiles, slash commands, troubleshooting.

## 7. Services MCP Cloud (claude.ai)

| Service | Status |
|---------|--------|
| Google Calendar | ✅ Connecté |
| Canva | ✅ Connecté |
| Notion | ✅ Connecté |
| Playwright | ✅ Connecté |
| Pinecone | ✅ Connecté |

## 8. Prérequis Système

```bash
# Outils requis
sudo apt install -y python3 python3-pip nodejs npm git curl jq tmux
curl -LsSf https://astral.sh/uv/install.sh | sh
npm install -g n8n

# GPU (si NVIDIA)
sudo apt install -y nvidia-driver-590 nvidia-utils-590

# Docker
curl -fsSL https://get.docker.com | sh

# Ollama
curl -fsSL https://ollama.com/install.sh | sh

# LM Studio (manual)
# https://lmstudio.ai/
```

## 9. Commande de Restauration Complète

```bash
# 1. Cloner le projet
git clone https://github.com/Turbo31150/jarvis-linux.git ~/jarvis-linux
cd ~/jarvis-linux

# 2. Installer JARVIS OS
chmod +x install-jarvis-os.sh && ./install-jarvis-os.sh

# 3. Copier les configs Claude Code
# (copier ~/.claude/ depuis backup)

# 4. Docker
docker compose -f docker-compose.modular.yml up -d

# 5. n8n
n8n start &
# Importer workflows :
for f in n8n_workflows/workflow_*.json; do n8n import:workflow --input="$f"; done

# 6. Crontab
crontab < system/crontab-jarvis.txt  # (à créer depuis crontab -l)

# 7. Vérifier
make health
make test
curl http://127.0.0.1:9742/health/full
```

---

*Généré le 2026-03-19 — JARVIS v15.0 — 118 commits, 12 tags*
