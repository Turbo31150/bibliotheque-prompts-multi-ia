# Multi-IA — CLI Dispatch Unifié (jai)

> Interface unique pour dispatcher vers 23 targets IA (local + web + consensus).
> Commande : `jai <target> "<prompt>"`
> Fichier : `/home/turbo/jarvis-linux/scripts/jarvis-ai-dispatch.py`

---

## Installation

```bash
# Deja installe en symlink
sudo ln -sf /home/turbo/jarvis-linux/scripts/jarvis-ai-dispatch.py /usr/local/bin/jai
```

## Targets disponibles

### CLI Locaux
```bash
jai claude "ton prompt"       # Claude Code (Opus 4.6)
jai claude-fast "ton prompt"  # Claude Sonnet (rapide)
jai claude-deep "ton prompt"  # Claude Deep Research
jai gemini "ton prompt"       # Gemini CLI (Google)
jai codex "ton prompt"        # Codex CLI (OpenAI)
jai lms "ton prompt"          # LM Studio Chat
jai ollama "ton prompt"       # Ollama direct
jai gh "ton prompt"           # GitHub Copilot
jai browseros "ton prompt"    # BrowserOS CLI
```

### APIs Locales (GPU)
```bash
jai m1 "ton prompt"           # LM Studio qwen3-8b (6 GPU)
jai ol1 "ton prompt"          # Ollama qwen2.5 (triage)
jai m2 "ton prompt"           # M2 remote deepseek-r1
jai m3 "ton prompt"           # M3 remote fallback
jai openclaw "ton prompt"     # OpenClaw Gateway (40 agents)
```

### IA Web via CDP (Chrome)
```bash
jai perplexity "ton prompt"   # Perplexity (recherche + sources)
jai chatgpt "ton prompt"      # ChatGPT Web
jai aistudio "ton prompt"     # Google AI Studio
jai claude-web "ton prompt"   # Claude.ai Web
jai gemini-web "ton prompt"   # Gemini Web
```

### Consensus (multi-target parallele)
```bash
jai consensus "ton prompt"       # M1 + OL1 + Claude
jai all-web "ton prompt"         # Perplexity + ChatGPT + AI Studio
jai all-local "ton prompt"       # M1 + OL1 + M2 + M3
jai full-consensus "ton prompt"  # Local + Cloud complet
```

## Options
```bash
jai --list                    # Lister toutes les targets
jai m1 "prompt" --json        # Sortie JSON structuree
jai m1 "prompt" --timeout 120 # Timeout custom
```

## Prompts d'usage avance

### Prompt — Verification croisee multi-IA
```
jai consensus "Verifie cette affirmation : [AFFIRMATION]. Reponds par vrai/faux avec justification en 2 lignes."
```

### Prompt — Recherche web + synthese locale
```
# Etape 1 : recherche
jai perplexity "Tarifs freelance IA France 2026"
# Etape 2 : synthese (60s plus tard, lire la reponse CDP)
jai m1 "Synthetise ces donnees marche : [COLLER RESULTATS]"
```

### Prompt — Audit code multi-agent
```
jai claude "Analyse ce fichier pour les bugs" < fichier.py
jai codex "Propose un refactor de ce fichier" < fichier.py
jai m1 "Review de securite de ce code" < fichier.py
```

### Prompt — Publication verifiee
```
# 1. Generer le contenu
jai m1 "Genere un post LinkedIn sur l'orchestration IA"
# 2. Verifier via IA web
jai perplexity "Verifie ce post LinkedIn, ameliore le wording: [CONTENU]"
# 3. Publier (via BrowserOS)
jai browseros "Publie ce post sur LinkedIn: [CONTENU_VERIFIE]"
```

## Architecture technique
- **0 dependance pip** — stdlib Python uniquement
- **Types** : cli, api, cdp, openclaw, multi
- **CDP** : detecte automatiquement les onglets ouverts sur Chrome 9222
- **Multi** : ThreadPoolExecutor pour parallélisme
- **Failover** : M1 → OL1 → M2 → M3 → GEMINI → CLAUDE
