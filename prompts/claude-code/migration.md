# Claude Code — Guide de Migration Nouvelle Machine

> Procedure complete pour migrer un environnement Claude Code + JARVIS vers une nouvelle machine.

---

## Prompt de migration

```
Je migre mon environnement de developpement vers une nouvelle machine.

Machine source : [SPECS ACTUELLES]
Machine cible : [SPECS NOUVELLES]

Execute le plan de migration suivant :

## PHASE 1 — INVENTAIRE
1. Liste tous les outils installes (claude, uv, node, python, docker, ollama)
2. Liste les versions exactes
3. Liste les fichiers de configuration a migrer
4. Liste les bases de donnees a copier
5. Estime l'espace disque total necessaire

## PHASE 2 — EXPORT
1. Exporte les configurations Claude Code (~/.claude/)
2. Exporte les fichiers memoire
3. Exporte les MCP servers configs
4. Exporte les .env (sans les secrets — remplacer par des placeholders)
5. Sauvegarde les bases de donnees (63 bases, 160 MB)
6. Exporte la crontab
7. Exporte les workflows n8n

## PHASE 3 — INSTALL (sur la nouvelle machine)
1. Installe les prerequis systeme
2. Installe Claude Code
3. Installe uv + Python 3.13
4. Installe Node.js 20+
5. Installe Docker
6. Installe Ollama
7. Configure le reseau cluster (IPs statiques)

## PHASE 4 — IMPORT
1. Restaure les configurations Claude Code
2. Restaure les fichiers memoire
3. Restaure les MCP servers
4. Restaure les bases de donnees
5. Restaure la crontab
6. Restaure les workflows n8n
7. Configure les .env avec les vrais secrets

## PHASE 5 — VALIDATION
1. Lance /cluster-check
2. Lance /audit
3. Lance les tests (uv run pytest)
4. Verifie chaque MCP server
5. Verifie les crons
6. Verifie n8n
7. Test vocal (TTS + STT)
```

### Ce que ca fait
Procedure exhaustive qui ne laisse rien derriere. Chaque phase a un objectif clair et des etapes verifiables.

### Effet sur le modele
- Le plan structure empeche Claude d'oublier des etapes
- Les 5 phases ordonnees garantissent que les dependances sont respectees
- L'etape VALIDATION finale confirme que tout fonctionne

---

## Checklist de migration

### Fichiers a copier

```bash
# Configurations Claude Code
~/.claude/settings.json
~/.claude/mcp-servers.json
~/.claude/memory/*.md
~/.claude/plugins/

# JARVIS
~/jarvis-linux/.env
~/jarvis-linux/data/*.db          # 63 bases
~/jarvis-linux/system/crontab-jarvis.txt
~/jarvis-linux/configs/

# n8n
~/.n8n/                            # Workflows et credentials

# Ollama
~/.ollama/                         # Modeles telecharges

# SSH et Git
~/.ssh/
~/.gitconfig
```

### Services a configurer

```bash
# Ordre d'installation
1. Systeme de base (apt update, build-essential, git)
2. Python 3.13 + uv
3. Node.js 20+
4. Docker + docker-compose
5. Ollama
6. Claude Code (npm install -g @anthropic-ai/claude-code)
7. JARVIS (git clone + uv sync)
8. n8n (npm install -g n8n)
9. LM Studio (si noeud cluster)
10. BrowserOS (docker)
```

### Verification post-migration

```bash
# Tests rapides
claude --version                   # Claude Code installe
uv run pytest --quick              # Tests passent
curl 127.0.0.1:1234/health        # LM Studio repond
curl 127.0.0.1:11434/api/tags     # Ollama repond
curl 127.0.0.1:5678               # n8n repond
curl 127.0.0.1:18800              # Canvas repond
nvidia-smi                         # GPUs detectes
```

---

## Prerequis

- Acces SSH aux deux machines (source et cible)
- Espace disque suffisant sur la cible (minimum 100 GB)
- Meme reseau local pour le cluster (192.168.1.x)
- Cles API a portee de main (Anthropic, Gemini, MEXC, CoinEx, Telegram, Discord)
