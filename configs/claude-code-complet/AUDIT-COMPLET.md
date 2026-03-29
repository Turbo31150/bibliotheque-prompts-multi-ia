# Audit Complet — Claude Code JARVIS M1 vs Installation Vierge
## Date: 2026-03-20

---

## COMPARAISON : Installation Vierge vs Configuration Turbo

| Paramètre | Vierge (défaut) | Turbo (actuel) |
|---|---|---|
| **Permissions** | Aucune (demande à chaque outil) | 11 outils auto-allow + 7 MCP servers |
| **Plugins** | 0 | 22 plugins actifs |
| **Skills** | 0 | 37 skills (14 superpowers + 7 plugin-dev + 16 autres) |
| **Hooks** | 0 | 4 hooks actifs (SessionStart x3, PreToolUse x1) |
| **MCP Servers** | 0 | 11 serveurs (JARVIS, Calendar, Canva, Notion, GitHub, BrowserOS, Playwright, Context7, Pinecone, LMStudio, Filesystem) |
| **Memory** | 0 fichiers | 10 fichiers persistants |
| **CLAUDE.md** | 0 | 4 fichiers (jarvis-linux, openclaw, cluster, turbo) |
| **Keybindings** | Défaut | Défaut (non modifié) |
| **Dirs autorisés** | Répertoire courant | /home/turbo/**, /tmp/**, /var/log/**, /opt/** |
| **Voice** | Désactivé | Activé |
| **Subscription** | - | Max (claude_max_20x rate limit) |
| **Modèle** | Sonnet | Opus 4.6 (1M context) |

---

## 1. PERMISSIONS (settings.json)

### Outils auto-autorisés (vs 0 en vierge)
```json
"allow": [
    "Bash(*)",
    "Read(*)",
    "Write(*)",
    "Edit(*)",
    "Glob(*)",
    "Grep(*)",
    "Agent(*)",
    "WebFetch(*)",
    "WebSearch(*)",
    "NotebookEdit(*)",
    "Skill(*)"
]
```

### MCP Servers auto-autorisés
```json
"mcp__jarvis__*",
"mcp__claude_ai_Google_Calendar__*",
"mcp__claude_ai_Canva__*",
"mcp__claude_ai_Notion__*",
"mcp__github__*",
"mcp__browseros__*",
"mcp__plugin_playwright_playwright__*"
```

### Répertoires autorisés
```json
"allowedDirs": ["/home/turbo/**", "/tmp/**", "/var/log/**", "/opt/**"]
```

### Voice
```json
"voiceEnabled": true
```

---

## 2. PLUGINS ACTIVÉS (22)

### Workflow & Développement
| Plugin | Rôle |
|---|---|
| superpowers | 14 skills de workflow (brainstorming, TDD, debug, plans, review) |
| feature-dev | Développement guidé de features |
| code-review | Review de code |
| code-simplifier | Simplification de code |
| commit-commands | Git commit, push, PR |
| pr-review-toolkit | Review complète de PR |

### Langages & LSP
| Plugin | Rôle |
|---|---|
| typescript-lsp | LSP TypeScript |
| pyright-lsp | LSP Python |

### Outils externes
| Plugin | Rôle |
|---|---|
| playwright | Automatisation navigateur (MCP) |
| github | Opérations GitHub (MCP) |
| context7 | Documentation librairies à jour (MCP) |
| pinecone | Base vectorielle (MCP) |

### Création & Meta
| Plugin | Rôle |
|---|---|
| plugin-dev | Création de plugins Claude Code |
| agent-sdk-dev | SDK Agent Anthropic |
| skill-creator | Création et test de skills |
| claude-code-setup | Recommandations setup |
| claude-md-management | Gestion CLAUDE.md |

### Styles de sortie
| Plugin | Rôle |
|---|---|
| explanatory-output-style | Mode explicatif avec insights |
| learning-output-style | Mode apprentissage interactif |

### Sécurité & Autres
| Plugin | Rôle |
|---|---|
| security-guidance | Garde-fous sécurité (hook PreToolUse) |
| frontend-design | Interfaces web production-grade |
| playground | Playgrounds HTML interactifs |

---

## 3. HOOKS (4 actifs)

### SessionStart (3 hooks)
1. **superpowers** — Charge le système de skills au démarrage
2. **learning-output-style** — Active le mode apprentissage interactif
3. **explanatory-output-style** — Active les insights éducatifs

### PreToolUse (1 hook)
4. **security-guidance** — Vérifie la sécurité avant chaque Edit/Write/MultiEdit

---

## 4. MCP SERVERS (11)

### Cloud (via claude.ai OAuth)
| Serveur | Scope |
|---|---|
| Google Calendar | Événements, disponibilités |
| Canva | Design, export, édition |
| Notion | Pages, bases de données, commentaires |

### Plugins locaux
| Serveur | Transport | Description |
|---|---|---|
| Playwright | stdio (npx) | Automatisation navigateur |
| GitHub | HTTP (api.githubcopilot.com) | Repos, PRs, issues |
| Context7 | stdio (npx) | Docs librairies |
| Pinecone | stdio (npx) | Vector DB |

### JARVIS (projets locaux)
| Serveur | Config | Description |
|---|---|---|
| jarvis-mcp | Python src.mcp_server | 658 handlers JARVIS |
| jarvis-lmstudio | Python mcp_lmstudio_bridge.py | Bridge vers LM Studio |
| filesystem | npx @modelcontextprotocol/server-filesystem | Accès fichiers |

---

## 5. MEMORY PERSISTANTE (10 fichiers)

### Profil utilisateur
- **user_language.md** — Français obligatoire
- **user_profile.md** — GitHub Turbo31150, automatisation maximale
- **user_machine_m1.md** — Ryzen 5700X3D, 6 GPUs, 46GB RAM, cluster M1/M2/Server

### Projets actifs
- **project_jarvis_os.md** — JARVIS OS: 1007 commandes vocales, 9 couches, 16 services
- **project_jarvis_linux_port.md** — Portage Linux: 494 dominos, 153 skills, 180 commandes
- **project_portage_linux_progress.md** — Progression: ~250 fichiers portés, 454 tests
- **project_jarvis_v15_session.md** — Session v12.4→v15.0: décisions archi
- **project_jarvis_v15_complete.md** — Inventaire: 128 commits, 320K lignes, 317 modules
- **project_voice_linux_control.md** — Vocal: 898 commandes, 5 modules, pipeline v3.1

### Instruction spéciale dans MEMORY.md
```
JARVIS doit systématiquement exécuter /home/turbo/jarvis-linux/scripts/jarvis-tts.sh
pour chaque réponse envoyée à Turbo.
```

---

## 6. CLAUDE.MD (4 fichiers)

| Fichier | Lignes | Projet |
|---|---|---|
| jarvis-linux/docs/CLAUDE.md | 105 | Instructions JARVIS Linux |
| jarvis-linux/modules/openclaw/CLAUDE.md | 296 | OpenClaw instructions |
| JARVIS-CLUSTER/CLAUDE.md | 73 | Cluster instructions |
| turbo/CLAUDE.md | 35 | Projet Turbo general |

---

## 7. OPTIMISATIONS vs DÉFAUT

### Performance
- Tous les outils en auto-allow → zéro friction
- 4 répertoires pré-autorisés → pas de blocage
- Voice activé → interaction vocale
- Subscription Max (20x rate limit) → débit maximum

### Workflow
- Superpowers skills → processus structurés (TDD, plans, review)
- 3 hooks SessionStart → contexte chargé automatiquement
- Security hook → protection passive sur chaque écriture
- Memory persistante → contexte conservé entre sessions

### Intégrations
- JARVIS MCP → accès direct au cluster IA (658 handlers)
- LM Studio bridge → modèles locaux accessibles
- 7 MCP cloud → Calendar, Canva, Notion, GitHub, Playwright, Context7, Pinecone
- TTS automatique → chaque réponse est vocalisée

---

## Restauration rapide

```bash
# 1. Settings
cp settings.json ~/.claude/settings.json
cp settings.local.json ~/.claude/settings.local.json

# 2. Plugins (22)
claude plugins install superpowers frontend-design context7 \
  code-review github feature-dev code-simplifier playwright \
  typescript-lsp commit-commands claude-md-management \
  security-guidance pr-review-toolkit pyright-lsp \
  claude-code-setup agent-sdk-dev plugin-dev \
  explanatory-output-style skill-creator \
  learning-output-style playground pinecone

# 3. Memory
mkdir -p ~/.claude/projects/<project>/memory/
cp memory/*.md ~/.claude/projects/<project>/memory/

# 4. CLAUDE.md
cp CLAUDE.md files to respective project roots
```
