# Bibliotheque de Prompts Multi-IA

> Collection complete de prompts, configurations et guides d'utilisation pour Claude Code, Gemini CLI, ChatGPT, Perplexity, BrowserOS, OpenClaw, n8n, modeles locaux et cluster JARVIS.

## Objectif

Cette bibliotheque centralise tous les prompts, configurations et modes d'emploi pour travailler efficacement avec les IA modernes — en terminal, dans le navigateur, via des workflows automatises ou sur un cluster GPU local.

## Structure Complete

### Outils IA Cloud & CLI

| Dossier | Contenu |
|---------|---------|
| `prompts/claude-code/` | Configuration, developpement, automatisation, migration, CLAUDE.md template |
| `prompts/claude-api/` | Integration API Anthropic directe |
| `prompts/gemini-cli/` | Generation code, audit systeme, sessions, reprise conversation |
| `prompts/gemini-app/` | Gemini dans le navigateur |
| `prompts/chatgpt/` | Configuration et prompts ChatGPT |
| `prompts/codex-cli/` | OpenAI Codex CLI |
| `prompts/codex-openai/` | Refactoring, Linux performance, integration JARVIS |
| `prompts/perplexity/` | Recherche technique, veille crypto |
| `prompts/browseros/` | Automation web, LinkedIn, MCP config |
| `prompts/openclaw/` | Configuration et prompts OpenClaw |
| `prompts/n8n/` | Workflows JARVIS, configuration n8n |
| `prompts/multi-ia/` | Consensus multi-modele, cluster dispatch |

### Modeles Locaux

| Dossier | Contenu |
|---------|---------|
| `prompts/models-locaux/lm-studio/configuration/` | Setup LM Studio, GPU config, API server 0.0.0.0:1234, 7 modeles |
| `prompts/models-locaux/lm-studio/inference/` | Requetes curl, Python httpx, streaming, parametres |
| `prompts/models-locaux/lm-studio/benchmark/` | Latence, qualite, tok/s — tableau comparatif |
| `prompts/models-locaux/lm-studio/fine-tuning/` | Fine-tuning de modeles LM Studio |
| `prompts/models-locaux/ollama/configuration/` | Install Ollama, pull models, kimi-k2.5, deepseek-r1:7b, qwen2.5:1.5b |
| `prompts/models-locaux/ollama/inference/` | /api/chat, /api/generate, streaming, options |
| `prompts/models-locaux/ollama/benchmark/` | Benchmark modeles Ollama |
| `prompts/models-locaux/ollama/fine-tuning/` | Fine-tuning Ollama |
| `prompts/models-locaux/deepseek-r1/configuration/` | DeepSeek-R1 sur M2, max_output_tokens >= 2048, chain-of-thought |
| `prompts/models-locaux/deepseek-r1/inference/` | Inference DeepSeek-R1 |
| `prompts/models-locaux/deepseek-r1/benchmark/` | Benchmark raisonnement |
| `prompts/models-locaux/deepseek-r1/fine-tuning/` | Fine-tuning DeepSeek-R1 |
| `prompts/models-locaux/qwen3/configuration/` | Qwen3-8b (champion 65 tok/s, 98.4/100), qwen3-coder-30b, prefixe /nothink |
| `prompts/models-locaux/qwen3/inference/` | Inference Qwen3 |
| `prompts/models-locaux/qwen3/benchmark/` | Benchmark famille Qwen3 |
| `prompts/models-locaux/qwen3/fine-tuning/` | Fine-tuning Qwen3 |
| `prompts/models-locaux/gemma/configuration/` | Google Gemma 3-4B, leger, classification rapide |
| `prompts/models-locaux/gemma/inference/` | Inference Gemma |
| `prompts/models-locaux/gemma/benchmark/` | Benchmark Gemma |
| `prompts/models-locaux/gemma/fine-tuning/` | Fine-tuning Gemma |

### Cluster JARVIS

| Dossier | Contenu |
|---------|---------|
| `prompts/cluster/dispatch-engine/` | Pipeline 9 etapes : cache, health, auto-load, route, enrichment, dispatch, quality, feedback, post-process |
| `prompts/cluster/consensus/` | Vote pondere multi-IA (5 modeles, poids M1=1.8 a M3=1.0, seuil 3+ a 0.7) |
| `prompts/cluster/routage/` | Matrice 17 domaines x 6 noeuds, poids 5 niveaux (noeud, domaine, latence, GPU temp, auto-learn) |
| `prompts/cluster/self-healing/` | Boucle detect-diagnose-repair-verify, circuit breaker, backoff exponentiel, scheduler 5 min |
| `prompts/cluster/gpu-management/` | 5 GPUs, garde thermique (75C warning / 85C critique), VRAM allocation, persistence mode |
| `prompts/cluster/backup/` | 103 SQLite DBs, git bundle, sync HDD, notification Telegram, daily 03:00 |

### Support

| Dossier | Contenu |
|---------|---------|
| `configs/` | Fichiers de configuration prets a l'emploi |
| `docs/` | Guides d'utilisation detailles |

## Page Interactive

Ouvrir `index.html` dans un navigateur pour acceder a tous les prompts avec :
- Filtrage par modele IA (Claude, Gemini, ChatGPT, Perplexity, BrowserOS)
- Filtrage par application (Terminal, BrowserOS, n8n, Docker, Telegram)
- Filtrage par contexte (Setup, Code, Debug, Trading, Automation, Monitoring...)
- Copie en 1 clic

## Utilisation Rapide

1. Cloner le repo
2. Ouvrir `index.html` dans un navigateur
3. Selectionner l'outil et le contexte
4. Copier le prompt
5. Coller dans l'outil IA

## Contenu

- **24+ prompts** classes par outil et contexte
- **9 fichiers de configuration** prets a copier
- **3 guides** d'utilisation detailles
- **22 plugins** Claude Code documentes avec effets sur le modele
- **65 workflows** n8n pour JARVIS
- **44 skills/agents** disponibles
- **14 guides** modeles locaux et cluster
- **5 modeles locaux** documentes (LM Studio, Ollama, DeepSeek-R1, Qwen3, Gemma)
- **6 composants cluster** (dispatch, consensus, routage, self-healing, GPU, backup)

## Auteur

Turbo31150 — Createur de [JARVIS](https://github.com/Turbo31150/jarvis-linux)
