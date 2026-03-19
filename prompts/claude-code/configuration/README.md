# Claude Code — Configuration

## Description
Guide complet pour configurer Claude Code avec l'ecosysteme JARVIS : 6 MCP servers, 18 regles de permissions, 22 plugins avec leurs effets, settings.json, repertoires autorises et integration vocale.

## Configuration requise

### Prerequis systeme
- Claude Code CLI installe : `npm install -g @anthropic-ai/claude-code`
- Cle API Anthropic configuree : `export ANTHROPIC_API_KEY=sk-ant-...`
- Python 3.13+ avec `uv` pour les MCP servers Python
- Node.js 20+ pour les MCP servers JavaScript
- Acces reseau local pour le cluster (192.168.1.x)

### Installation en 5 etapes
1. Copier `mcp-servers.json` dans `~/.claude/`
2. Copier `settings.json` dans `~/.claude/`
3. Creer les fichiers memoire dans `~/.claude/memory/`
4. Lancer Claude Code : `claude`
5. Verifier la configuration : `/cluster-check`

---

## Prompts par type de tache

### Creation de la configuration initiale

```
Configure Claude Code pour un environnement JARVIS complet.

1. Cree le fichier ~/.claude/mcp-servers.json avec les 6 MCP servers :
   - jarvis-turbo (658 handlers, cluster IA, trading, monitoring)
   - voice-mcp (commandes vocales TTS/STT)
   - browseros-mcp (navigation CDP)
   - rag-mcp (recherche semantique locale)
   - notion-mcp (synchronisation Notion)
   - calendar-mcp (Google Calendar)

2. Cree le fichier ~/.claude/settings.json avec :
   - Modele par defaut : claude-sonnet-4-20250514
   - Permissions allow : git, uv, python, node, npm, make, docker, systemctl, journalctl, nvidia-smi, curl local, ls, cat, grep, find, tous les MCP
   - Permissions deny : rm -rf /, dd, mkfs, shutdown, reboot
   - Plugin jarvis-turbo actif
   - Memory activee dans ~/.claude/memory/

3. Verifie que chaque MCP server repond.
4. Verifie que les permissions fonctionnent (test avec une commande allow et une deny).
```

### Amelioration / Ajout d'un MCP server

```
Ajoute un nouveau MCP server a ma configuration Claude Code.

Nom : [NOM_DU_SERVER]
Commande : [COMMANDE_LANCEMENT]
Description : [CE_QUE_CA_FAIT]

1. Ajoute l'entree dans ~/.claude/mcp-servers.json
2. Ajoute la permission "mcp__[NOM]__*" dans settings.json
3. Teste que le server repond
4. Documente l'ajout dans les fichiers memoire
```

### Debug de configuration

```
Ma configuration Claude Code ne fonctionne pas correctement.

Symptome : [DECRIRE LE PROBLEME]

Verifie dans l'ordre :
1. ~/.claude/settings.json — syntaxe JSON valide ?
2. ~/.claude/mcp-servers.json — tous les chemins existent ?
3. Permissions — les commandes sont bien dans allow/deny ?
4. MCP servers — chaque server repond au health check ?
5. Memory — les fichiers .md existent dans ~/.claude/memory/ ?
6. Variables d'environnement — ANTHROPIC_API_KEY, MCP_API_KEY, VOICE_MCP_TOKEN ?

Pour chaque probleme trouve, corrige et verifie.
```

### Documentation de la configuration

```
Genere une documentation complete de ma configuration Claude Code actuelle.

Inclus :
1. Liste des MCP servers avec leur status
2. Permissions actives (allow et deny)
3. Plugins installes et leur role
4. Fichiers memoire et leur contenu resume
5. Variables d'environnement necessaires
6. Schema d'architecture (Claude Code → MCP → Services)

Format : Markdown avec tableaux.
```

---

## MCP Servers (6)

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

| MCP Server | Technologie | Handlers | Role |
|------------|-------------|----------|------|
| jarvis-turbo | Python/uv | 658 | Acces complet a l'ecosysteme JARVIS |
| voice-mcp | Python/uv | ~30 | Controle vocal (TTS Piper, STT Whisper) |
| browseros-mcp | Node.js | ~20 | Pilotage navigateur via Chrome DevTools Protocol |
| rag-mcp | Python/uv | ~15 | Recherche semantique dans la base locale |
| notion-mcp | Python/uv | ~10 | Synchronisation bidirectionnelle avec Notion |
| calendar-mcp | Python/uv | ~10 | Gestion du calendrier Google |

---

## Permissions (18 regles)

### Fichier `~/.claude/settings.json`

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

| Categorie | Regles allow | Effet |
|-----------|-------------|-------|
| Dev tools | git, uv, python, node, npm, make | Pas de confirmation pour les commandes dev |
| Infra | docker, systemctl status, journalctl | Monitoring sans interruption |
| GPU | nvidia-smi | Verification thermique directe |
| Exploration | ls, cat, grep, find, curl local | Navigation fichiers fluide |
| MCP | 6 wildcards mcp__*__* | Acces direct aux outils MCP |
| Deny | rm -rf /, dd, mkfs, shutdown, reboot | Bloque les commandes destructives |

---

## Plugins (22)

| # | Plugin | Description | Effet sur le modele |
|---|--------|-------------|---------------------|
| 1 | `jarvis-turbo` | Plugin principal (11 skills, 7 agents, 12 commandes) | Acces a tout l'ecosysteme JARVIS |
| 2 | `gpu-monitor` | Surveillance temperatures GPU | Verification thermique avant calcul |
| 3 | `cluster-health` | Health check des 4 noeuds | Routage intelligent des requetes |
| 4 | `trading-scanner` | Scan crypto multi-exchange | Analyse de marche temps reel |
| 5 | `rag-search` | Recherche base de connaissances | Enrichit les reponses avec contexte local |
| 6 | `voice-control` | Commandes vocales TTS/STT | Claude peut parler et ecouter |
| 7 | `browseros-pilot` | Pilotage navigateur CDP | Navigation web automatisee |
| 8 | `notion-sync` | Synchronisation Notion | Lecture/ecriture dans Notion |
| 9 | `calendar-bridge` | Google Calendar | Gestion du calendrier |
| 10 | `discord-webhook` | Notifications Discord | Alertes temps reel |
| 11 | `telegram-bot` | Bot Telegram JARVIS | Communication mobile |
| 12 | `backup-manager` | Sauvegardes automatiques | Securite des donnees |
| 13 | `log-analyzer` | Analyse des logs systeme | Diagnostic automatise |
| 14 | `metrics-exporter` | Export Prometheus/Grafana | Monitoring avance |
| 15 | `docker-manager` | Gestion containers Docker | Deployment containerise |
| 16 | `git-workflow` | Automatisation Git | CI/CD integre |
| 17 | `cron-scheduler` | Taches planifiees | Automatisation temporelle |
| 18 | `web-researcher` | Recherche web + digest | Veille technologique |
| 19 | `model-router` | Routage entre modeles IA | Optimisation cout/performance |
| 20 | `session-manager` | Gestion sessions Claude Code | Persistance du contexte |
| 21 | `canvas-ui` | Interface Canvas standalone | UI interactive port 18800 |
| 22 | `openclaw-gateway` | Gateway OpenClaw (40+56 agents) | Orchestration multi-agent |

**Impact tokens** : 22 plugins = ~6000-8000 tokens consommes au demarrage. Desactiver les plugins inutilises ameliore la precision.

---

## Settings.json complet

```json
{
  "model": "claude-sonnet-4-20250514",
  "theme": "dark",
  "verbose": false,
  "permissions": {
    "allow": ["..."],
    "deny": ["..."]
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

## AllowedDirs et Memory

### Fichiers memoire charges automatiquement

| Fichier | Contenu | Tokens |
|---------|---------|--------|
| `user_language.md` | Preference langue francaise | ~50 |
| `user_profile.md` | Profil Turbo, GitHub, preferences | ~200 |
| `user_machine_m1.md` | Ryzen 5700X3D, 6 GPUs, 46GB RAM | ~300 |
| `project_voice_linux_control.md` | 898 commandes vocales, 5 modules | ~400 |
| `project_jarvis_os.md` | JARVIS OS 9 couches | ~500 |
| `project_jarvis_linux_port.md` | 4 chantiers, 443 dominos, 11 modules | ~500 |
| `project_portage_linux_progress.md` | Supervisor v2, ~250 fichiers portes | ~400 |

**Total** : ~2000-4000 tokens charges a chaque session.

---

## Integration vocale

La configuration vocale passe par le MCP `voice-mcp` et le script `/home/turbo/jarvis-linux/scripts/jarvis-tts.sh`. JARVIS prononce chaque reponse via TTS Piper. Le declencheur vocal active STT Whisper pour la transcription.

---

## Exemples concrets

### Verifier que tout fonctionne
```bash
claude "/cluster-check"
# Resultat attendu : 4/4 noeuds online, temperatures < 75C, modeles charges
```

### Tester un MCP server
```bash
claude "Appelle le MCP jarvis-turbo pour obtenir le status du cluster"
# Resultat attendu : JSON avec status de chaque noeud
```

### Ajouter une permission
```bash
claude "Ajoute la permission Bash(htop) dans mon settings.json"
# Resultat attendu : settings.json mis a jour, confirmation
```

## Effet sur le modele
- Les permissions `allow` suppriment les confirmations → sessions 40-60% plus rapides
- Les permissions `deny` bloquent les commandes dangereuses meme si demandees
- Chaque MCP server ajoute ~200-500 tokens de contexte au demarrage
- Les fichiers memoire donnent au modele une connaissance instantanee du profil et du projet
- Un bon set de permissions + memoire = un Claude Code qui agit comme un assistant personnel entraine
