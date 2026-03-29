# Claude Code — Configuration Complete

> Tout ce qu'il faut pour configurer Claude Code avec JARVIS : MCP servers, permissions, plugins, settings, memory.

---

## 1. MCP Servers (Model Context Protocol)

Les MCP servers etendent les capacites de Claude Code en lui donnant acces a des outils externes.

### Configuration (`~/.claude/mcp-servers.json`)

```json
{
  "mcpServers": {
    "jarvis-turbo": {
      "command": "uv",
      "args": ["run", "python", "/home/turbo/jarvis-linux/src/mcp_server.py"],
      "env": {
        "JARVIS_VERSION": "15.0",
        "MCP_API_KEY": "${MCP_API_KEY}"
      },
      "description": "JARVIS MCP — 658 handlers, cluster IA, trading, monitoring"
    },
    "voice-mcp": {
      "command": "uv",
      "args": ["run", "python", "/home/turbo/jarvis-linux/src/voice_mcp.py"],
      "env": {
        "VOICE_MCP_TOKEN": "${VOICE_MCP_TOKEN}"
      },
      "description": "Commandes vocales — TTS/STT, commandes JARVIS"
    },
    "browseros-mcp": {
      "command": "node",
      "args": ["/home/turbo/jarvis-linux/src/browseros_mcp.js"],
      "env": {},
      "description": "BrowserOS CDP — navigation, scraping, automation web"
    },
    "rag-mcp": {
      "command": "uv",
      "args": ["run", "python", "/home/turbo/jarvis-linux/src/rag_mcp.py"],
      "description": "RAG local SQLite FTS5 — recherche dans la base de connaissances"
    },
    "notion-mcp": {
      "command": "uv",
      "args": ["run", "python", "/home/turbo/jarvis-linux/src/notion_bridge.py", "--mcp"],
      "description": "Bridge Notion — lecture/ecriture pages et bases"
    },
    "calendar-mcp": {
      "command": "uv",
      "args": ["run", "python", "/home/turbo/jarvis-linux/src/calendar_bridge.py", "--mcp"],
      "description": "Google Calendar — evenements, alertes, planification"
    }
  }
}
```

### Ce que ca fait
- **jarvis-turbo** : Acces a 658 handlers MCP (cluster, trading, monitoring, deployment, RAG, voice)
- **voice-mcp** : Controle vocal de la machine (TTS Piper, STT Whisper)
- **browseros-mcp** : Pilotage du navigateur via Chrome DevTools Protocol
- **rag-mcp** : Recherche semantique dans la base de connaissances locale
- **notion-mcp** : Synchronisation bidirectionnelle avec Notion
- **calendar-mcp** : Gestion du calendrier Google (creation, modification, alertes)

### Effet sur le modele
- Claude peut appeler directement les outils JARVIS sans passer par le terminal
- Reduit la latence : appel MCP direct vs commande bash intermediaire
- Le modele "voit" les outils disponibles et peut choisir le plus pertinent
- Plus le nombre d'outils est eleve, plus le context window est consomme au demarrage

---

## 2. Permissions

### Fichier `.claude/settings.json`

```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(uv run *)",
      "Bash(python *)",
      "Bash(node *)",
      "Bash(npm *)",
      "Bash(make *)",
      "Bash(docker *)",
      "Bash(systemctl status *)",
      "Bash(journalctl *)",
      "Bash(nvidia-smi *)",
      "Bash(curl 127.0.0.1*)",
      "Bash(ls *)",
      "Bash(cat *)",
      "Bash(grep *)",
      "Bash(find *)",
      "mcp__jarvis-turbo__*",
      "mcp__voice-mcp__*",
      "mcp__browseros-mcp__*",
      "mcp__rag-mcp__*",
      "mcp__notion-mcp__*",
      "mcp__calendar-mcp__*"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(dd if=*)",
      "Bash(mkfs*)",
      "Bash(shutdown*)",
      "Bash(reboot*)"
    ]
  }
}
```

### Effet sur le modele
- Les permissions `allow` suppriment les confirmations pour les commandes courantes
- Les permissions `deny` bloquent les commandes dangereuses meme si demandees
- Claude adapte son comportement : il prefere les commandes autorisees pour eviter les interruptions
- Un bon set de permissions accelere les sessions de 40-60%

---

## 3. Plugins (22 plugins documentes)

### Liste complete avec effets sur le modele

| # | Plugin | Description | Effet sur le modele |
|---|--------|-------------|---------------------|
| 1 | `jarvis-turbo` | Plugin principal JARVIS (11 skills, 7 agents, 12 commandes) | Donne acces a tout l'ecosysteme JARVIS |
| 2 | `gpu-monitor` | Surveillance temperatures GPU en temps reel | Claude peut verifier l'etat thermique avant calcul |
| 3 | `cluster-health` | Health check des 4 noeuds du cluster | Permet le routage intelligent des requetes |
| 4 | `trading-scanner` | Scan crypto multi-exchange (MEXC, CoinEx) | Analyse de marche en temps reel |
| 5 | `rag-search` | Recherche dans la base de connaissances | Enrichit les reponses avec le contexte local |
| 6 | `voice-control` | Commandes vocales TTS/STT | Claude peut parler et ecouter |
| 7 | `browseros-pilot` | Pilotage navigateur CDP | Navigation web automatisee |
| 8 | `notion-sync` | Synchronisation Notion bidirectionnelle | Lecture/ecriture dans Notion |
| 9 | `calendar-bridge` | Google Calendar integration | Gestion du calendrier |
| 10 | `discord-webhook` | Notifications Discord | Alertes en temps reel |
| 11 | `telegram-bot` | Bot Telegram JARVIS | Communication mobile |
| 12 | `backup-manager` | Gestion des sauvegardes automatiques | Securite des donnees |
| 13 | `log-analyzer` | Analyse des logs systeme | Diagnostic automatise |
| 14 | `metrics-exporter` | Export Prometheus/Grafana | Monitoring avance |
| 15 | `docker-manager` | Gestion containers Docker | Deployment containerise |
| 16 | `git-workflow` | Automatisation Git (PR, issues, releases) | CI/CD integre |
| 17 | `cron-scheduler` | Gestion des taches planifiees | Automatisation temporelle |
| 18 | `web-researcher` | Recherche web intelligente + digest | Veille technologique |
| 19 | `model-router` | Routage intelligent entre modeles IA | Optimisation cout/performance |
| 20 | `session-manager` | Gestion des sessions Claude Code | Persistance du contexte |
| 21 | `canvas-ui` | Interface Canvas standalone | UI interactive port 18800 |
| 22 | `openclaw-gateway` | Gateway OpenClaw (40 agents + 56 dynamic) | Orchestration multi-agent |

### Effet global sur le modele
- Chaque plugin ajoute des outils au context window (~200-500 tokens par plugin)
- 22 plugins = ~6000-8000 tokens de context consommes au demarrage
- Le modele priorise les outils des plugins actifs dans ses reponses
- Desactiver les plugins inutilises reduit le bruit et ameliore la precision

---

## 4. Plugin jarvis-turbo — Detail complet

### 11 Skills

| Skill | Description | Commande |
|-------|-------------|----------|
| `cluster-check` | Verification sante de tous les noeuds | `/cluster-check` |
| `gpu-status` | Temperatures et utilisation GPU | `/gpu-status` |
| `thermal-guard` | Protection thermique automatique | `/thermal` |
| `heal-cluster` | Reparation automatique des noeuds en panne | `/heal-cluster` |
| `consensus` | Vote multi-modele (3+ IA en parallele) | `/consensus` |
| `trading-scan` | Scan crypto multi-exchange | `/trading-scan` |
| `web-search` | Recherche web intelligente | `/web-search` |
| `audit` | Audit systeme complet | `/audit` |
| `model-swap` | Changement de modele a chaud | `/model-swap` |
| `deploy` | Deployment automatise | `/deploy` |
| `canvas-status` | Status de l'interface Canvas | `/canvas-status` |

### 7 Agents

| Agent | Description | Mode |
|-------|-------------|------|
| `code-reviewer` | Review de code multi-fichier | Parallele |
| `bug-hunter` | Detection de bugs automatisee | Sequentiel |
| `refactor-pilot` | Refactoring guide par metriques | Interactif |
| `test-generator` | Generation de tests automatiques | Parallele |
| `doc-writer` | Generation de documentation | Sequentiel |
| `perf-analyzer` | Analyse de performance | Parallele |
| `security-auditor` | Audit de securite du code | Sequentiel |

### 12 Commandes slash

```
/cluster-check    — Sante du cluster complet
/mao-check        — Status MAO (Monitoring, Alerting, Orchestration)
/gpu-status       — Temperatures et utilisation GPU
/thermal          — Protection thermique
/heal-cluster     — Reparation automatique
/consensus        — Vote multi-modele
/quick-ask        — Question rapide a un modele
/web-search       — Recherche web
/trading-scan     — Scan crypto
/trading-feedback — Retour sur predictions trading
/canvas-status    — Status Canvas UI
/canvas-restart   — Redemarrage Canvas
/audit            — Audit systeme
/model-swap       — Changement de modele
/deploy           — Deployment
```

### 2 Hooks

| Hook | Declencheur | Action |
|------|-------------|--------|
| `gpu-thermal-guard` | Temperature GPU > 75C | Alerte + re-routage cascade vers noeuds froids |
| `session-cluster-check` | Debut de session Claude Code | Verification automatique de la sante du cluster |

---

## 5. Settings.json — Template complet

```json
{
  "model": "claude-sonnet-4-20250514",
  "theme": "dark",
  "verbose": false,
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(uv run *)",
      "Bash(python *)",
      "Bash(node *)",
      "Bash(npm *)",
      "Bash(make *)",
      "Bash(docker *)",
      "Bash(systemctl status *)",
      "Bash(journalctl *)",
      "Bash(nvidia-smi *)",
      "Bash(curl 127.0.0.1*)",
      "mcp__jarvis-turbo__*",
      "mcp__voice-mcp__*",
      "mcp__browseros-mcp__*"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(shutdown*)",
      "Bash(reboot*)"
    ]
  },
  "mcpServers": {},
  "plugins": ["jarvis-turbo"],
  "memory": {
    "enabled": true,
    "path": "~/.claude/memory/"
  }
}
```

---

## 6. Memory Files

Liste des fichiers memoire utilises par Claude Code pour maintenir le contexte entre sessions :

| Fichier | Contenu |
|---------|---------|
| `user_language.md` | Preference de langue francaise |
| `user_profile.md` | Profil utilisateur Turbo, GitHub, preferences |
| `user_machine_m1.md` | M1 La Creatrice : Ryzen 5700X3D, 6 GPUs, 46GB RAM |
| `project_voice_linux_control.md` | Pilotage vocal Linux (898 commandes, 5 modules) |
| `project_jarvis_os.md` | JARVIS OS : integration complete dans Linux (9 couches) |
| `project_jarvis_linux_port.md` | Portage JARVIS Linux : 4 chantiers, 443 dominos, 11 modules |
| `project_portage_linux_progress.md` | Portage Windows vers Linux : supervisor v2, ~250 fichiers portes |

### Effet sur le modele
- Les fichiers memoire sont charges automatiquement a chaque session
- Ils consomment ~2000-4000 tokens du context window
- Le modele connait instantanement le profil, les preferences et l'etat du projet
- Sans memoire, chaque session recommence a zero

---

## Prerequis

- Claude Code CLI installe (`npm install -g @anthropic-ai/claude-code`)
- Cle API Anthropic configuree (`ANTHROPIC_API_KEY`)
- Python 3.13+ avec `uv` pour les MCP servers Python
- Node.js 20+ pour les MCP servers JavaScript
- Acces reseau local pour le cluster (192.168.1.x)

## Comment utiliser

1. Copier `mcp-servers.json` dans `~/.claude/`
2. Copier `settings.json` dans `~/.claude/`
3. Creer les fichiers memoire dans `~/.claude/memory/`
4. Lancer Claude Code : `claude`
5. Verifier la configuration : `/cluster-check`
