# Bibliothèque de Prompts Multi-IA

> Toute la configuration, les prompts et les skills pour **12 outils IA**,
> un cluster GPU distribué et un assistant vocal complet.
> Reproductible de zéro par n'importe qui.

---

## Vue d'ensemble

Ce dépôt centralise **tout** ce qu'il faut pour travailler avec les IA modernes :
prompts, configurations, skills, plugins, serveurs MCP, mémoire et workflows.

Chaque outil a son propre dossier avec un guide dédié.
Le détail interactif est dans la **[page HTML](#page-interactive)** (245 cartes filtrables, copie en un clic).

---

## Les 12 outils documentés

Ouvrir le guide de chaque outil dans l'ordre qui vous intéresse.

### Outils en terminal

| Outil | Guide à lire | Description |
|---|---|---|
| **Claude Code** | [`prompts/claude-code/`](prompts/claude-code/) | L'outil principal. 31 skills, 22 plugins, configuration complète. |
| **Gemini CLI** | [`prompts/gemini-cli/`](prompts/gemini-cli/) | Google Gemini en terminal. Génération, audit, sessions. |
| **Codex CLI** | [`prompts/codex-cli/`](prompts/codex-cli/) | OpenAI Codex en terminal. Refactoring, performance. |

### Applications navigateur

| Outil | Guide à lire | Description |
|---|---|---|
| **Claude (app)** | [`prompts/claude-api/`](prompts/claude-api/) | API Anthropic et intégration directe. |
| **Gemini (app)** | [`prompts/gemini-app/`](prompts/gemini-app/) | Google Gemini dans le navigateur. |
| **ChatGPT (app)** | [`prompts/chatgpt/`](prompts/chatgpt/) | Configuration et prompts ChatGPT optimisés. |
| **Perplexity** | [`prompts/perplexity/`](prompts/perplexity/) | Recherche technique et veille crypto. |
| **BrowserOS** | [`prompts/browseros/`](prompts/browseros/) | Automatisation web, LinkedIn, MCP. |

### Outils spécialisés

| Outil | Guide à lire | Description |
|---|---|---|
| **OpenClaw** | [`prompts/openclaw/`](prompts/openclaw/) | Agent IA autonome. Configuration et prompts. |
| **n8n** | [`prompts/n8n/`](prompts/n8n/) | 65 workflows d'automatisation JARVIS. |
| **Multi-IA** | [`prompts/multi-ia/`](prompts/multi-ia/) | Consensus multi-modèle, dispatch cluster. |
| **Codex OpenAI** | [`prompts/codex-openai/`](prompts/codex-openai/) | Refactoring avancé, intégration JARVIS. |

---

## Modèles locaux (GPU)

Cinq familles de modèles configurés pour tourner en local.

| Modèle | Guide à lire | Vitesse | Usage |
|---|---|---|---|
| **Qwen3** | [`prompts/models-locaux/qwen3/`](prompts/models-locaux/qwen3/) | 65 tok/s | Champion généraliste |
| **DeepSeek-R1** | [`prompts/models-locaux/deepseek-r1/`](prompts/models-locaux/deepseek-r1/) | 40 tok/s | Raisonnement avancé |
| **Gemma** | [`prompts/models-locaux/gemma/`](prompts/models-locaux/gemma/) | 80 tok/s | Classification rapide |
| **LM Studio** | [`prompts/models-locaux/lm-studio/`](prompts/models-locaux/lm-studio/) | Variable | 7 modèles, API locale |
| **Ollama** | [`prompts/models-locaux/ollama/`](prompts/models-locaux/ollama/) | Variable | 3 modèles, simple à déployer |

---

## Cluster JARVIS

Architecture distribuée sur 3 machines physiques (6 GPUs, 46 Go RAM, 10+ modèles).

| Composant | Guide à lire | Rôle |
|---|---|---|
| **Dispatch Engine** | [`prompts/cluster/dispatch-engine/`](prompts/cluster/dispatch-engine/) | Routage intelligent en 9 étapes |
| **Consensus** | [`prompts/cluster/consensus/`](prompts/cluster/consensus/) | Vote pondéré entre 5 modèles |
| **Routage** | [`prompts/cluster/routage/`](prompts/cluster/routage/) | Matrice 17 domaines × 6 nœuds |
| **Self-Healing** | [`prompts/cluster/self-healing/`](prompts/cluster/self-healing/) | Réparation automatique |
| **GPU Management** | [`prompts/cluster/gpu-management/`](prompts/cluster/gpu-management/) | Garde thermique, allocation VRAM |
| **Backup** | [`prompts/cluster/backup/`](prompts/cluster/backup/) | 103 bases SQLite, sync quotidien |

---

## Configuration Claude Code (de zéro à production)

Pour reproduire l'environnement complet, lire ces fichiers dans l'ordre :

| Étape | Fichier à lire | Ce que ça fait |
|---|---|---|
| 1. Audit complet | [`configs/claude-code-complet/AUDIT-COMPLET.md`](configs/claude-code-complet/AUDIT-COMPLET.md) | Comprendre toutes les différences vs une installation vierge. |
| 2. Permissions | [`configs/claude-code-complet/settings.json`](configs/claude-code-complet/settings.json) | 11 outils auto-autorisés, 22 plugins, voice activé. |
| 3. Plugins installés | [`configs/claude-code-complet/installed_plugins.json`](configs/claude-code-complet/installed_plugins.json) | Liste des 22 plugins avec versions. |
| 4. Hooks | `configs/claude-code-complet/hooks-*.json` | 4 automatisations au démarrage et à l'écriture. |
| 5. Serveurs MCP | `configs/claude-code-complet/mcp-*.json` | 11 connexions externes (GitHub, Calendar, Canva, etc.). |
| 6. Mémoire | [`configs/claude-code-complet/memory/`](configs/claude-code-complet/memory/) | 10 fichiers de mémoire persistante entre sessions. |
| 7. CLAUDE.md | [`configs/claude-code-complet/claude-md/`](configs/claude-code-complet/claude-md/) | 4 fichiers d'instructions par projet. |
| 8. Skills | [`prompts/claude-code/skills/README.md`](prompts/claude-code/skills/README.md) | Index des 31 skills avec triggers et effets. |

---

## Page interactive

Ouvrir **[`index.html`](index.html)** dans un navigateur :

- **245 cartes** de prompts navigables.
- **Filtrage par outil** : Claude, Gemini, ChatGPT, Perplexity, BrowserOS.
- **Filtrage par contexte** : Setup, Code, Debug, Trading, Automation, Monitoring.
- **Copie en un clic** vers le presse-papiers.

C'est le point d'entrée pour explorer le détail de chaque prompt de manière interactive.

---

## Chiffres clés

| Métrique | Valeur |
|---|---|
| Outils IA documentés | 12 |
| Prompts (cartes interactives) | 245+ |
| Skills Claude Code | 31 |
| Plugins configurés | 22 |
| Serveurs MCP | 11 |
| Workflows n8n | 65 |
| Modèles locaux | 5 familles |
| Composants cluster | 6 |
| Fichiers dans le dépôt | 360+ |

---

## Auteur

**[Turbo31150](https://github.com/Turbo31150)** — Créateur de **[JARVIS](https://github.com/Turbo31150/jarvis-linux)**

> 320 000 lignes de code · 317 modules · 674 endpoints · 1 007 commandes vocales · cluster 3 machines

*Dernière mise à jour : 20 mars 2026*
