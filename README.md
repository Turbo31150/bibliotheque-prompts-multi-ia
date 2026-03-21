<div align="center">
  <img src="assets/logo.svg" alt="PROMPT·VAULT" width="520"/>
  <br/><br/>

  [![License: MIT](https://img.shields.io/badge/License-MIT-C084FC?style=flat-square)](LICENSE)
  [![HTML](https://img.shields.io/badge/HTML5-standalone-E34F26?style=flat-square&logo=html5&logoColor=white)](#)
  [![Prompts](https://img.shields.io/badge/300%2B_prompts-curated-C084FC?style=flat-square)](#catalogue)
  [![IAs](https://img.shields.io/badge/5_IAs-Claude·GPT·Gemini·Perplexity·n8n-F472B6?style=flat-square)](#ias-couvertes)
  [![Stars](https://img.shields.io/github/stars/Turbo31150/bibliotheque-prompts-multi-ia?style=flat-square&color=C084FC)](#)

  <br/>
  <p><strong>Bibliothèque de 300+ prompts optimisés · 5 IAs · Claude Code · Gemini CLI · ChatGPT · OpenClaw · n8n</strong></p>
  <p><em>La référence des prompts JARVIS — chaque prompt testé, optimisé, documenté pour une IA spécifique</em></p>

  [**Catalogue →**](#-catalogue-des-prompts) · [**IAs →**](#-ias-couvertes) · [**Installation →**](#-utilisation) · [**Contribuer →**](#-contribuer)
</div>

---

## Présentation

**PROMPT·VAULT** est la bibliothèque de prompts centralisée de l'écosystème JARVIS. Elle regroupe **300+ prompts** soigneusement testés et optimisés pour **5 IAs différentes** — chaque prompt est classifié par IA cible, cas d'usage, niveau de complexité, et intégration JARVIS.

---

## Structure du projet

```
bibliotheque-prompts-multi-ia/
├── index.html              ← Interface web interactive
├── README.md               ← Ce fichier
├── prompts/                ← Prompts par IA
│   ├── claude/             ← Claude Code + Claude API
│   ├── gemini/             ← Gemini CLI + Gemini API
│   ├── chatgpt/            ← GPT-4o + ChatGPT
│   ├── perplexity/         ← Perplexity AI
│   └── n8n/                ← Nodes IA n8n
├── configs/                ← Configs par outil
│   ├── claude_code.json    ← CLAUDE.md templates
│   ├── gemini_cli.yaml     ← Gemini CLI configs
│   └── openclaw.yaml       ← OpenClaw patterns
├── docs/                   ← Documentation technique
├── scripts/                ← Outils de gestion
└── export/                 ← Exports (JSON, CSV, PDF)
```

---

## Catalogue des prompts

| Catégorie | Total | Claude | GPT | Gemini | Perplexity | n8n |
|-----------|-------|--------|-----|--------|------------|-----|
| **Développement** | 72 | 28 | 18 | 14 | 7 | 5 |
| **Trading & Finance** | 58 | 20 | 12 | 16 | 10 | — |
| **Automation** | 52 | 15 | 10 | 12 | 5 | 10 |
| **Analyse & Recherche** | 46 | 14 | 12 | 10 | 10 | — |
| **Contenu & Social** | 42 | 12 | 14 | 8 | 8 | — |
| **Système & Infra** | 35 | 18 | 8 | 5 | 4 | — |
| **Divers** | 28 | 8 | 8 | 6 | 6 | — |
| **Total** | **333** | 115 | 82 | 71 | 50 | 15 |

---

## IAs couvertes

### Claude (115 prompts)
- **Claude Code** — system prompts, CLAUDE.md templates, agent patterns
- **Claude API** — JSON structured outputs, tool use, multi-turn
- **Claude Desktop** — MCP configurations, Cowork sessions

### Gemini (71 prompts)
- **Gemini CLI** — commandes shell, scripts automatisés
- **Gemini Live API** — voice agents, real-time interactions
- **Gemini API** — vision, code generation, analysis

### ChatGPT / GPT-4o (82 prompts)
- **ChatGPT** — conversations, analysis, generation
- **GPT-4o** — vision, structured outputs, function calling
- **Assistants API** — custom assistants with tools

### Perplexity (50 prompts)
- Recherche web enrichie, veille marché, fact-checking
- Intégration JARVIS pour veille automatique

### n8n AI Nodes (15 prompts)
- Prompts pour les nodes IA dans les workflows n8n
- Intégration avec OpenAI, Claude, Gemini

---

## Utilisation

```bash
# Cloner la bibliothèque
git clone https://github.com/Turbo31150/bibliotheque-prompts-multi-ia.git
cd bibliotheque-prompts-multi-ia

# Ouvrir l'interface web
open index.html
# ou
npx serve . -p 3000
```

### Via l'interface web

L'interface `index.html` permet de :
- **Filtrer** par IA, catégorie, complexité
- **Rechercher** par mot-clé dans tous les prompts
- **Copier** un prompt en un clic
- **Exporter** une sélection en JSON/CSV
- **Prévisualiser** le résultat attendu

---

## Format d'un prompt

```json
{
  "id": "claude-code-scaffold-001",
  "title": "Scaffold Python project avec uv",
  "ia": "claude-code",
  "category": "development",
  "complexity": "intermediate",
  "tags": ["python", "uv", "scaffold", "jarvis"],
  "prompt": "...",
  "expected_output": "...",
  "jarvis_integration": true,
  "tested": true,
  "last_updated": "2026-03"
}
```

---

## Contribuer

1. Fork le repo
2. Ajouter ton prompt dans le bon dossier `prompts/<ia>/`
3. Suivre le format JSON ci-dessus
4. Pull Request avec le label `new-prompt`

---

<div align="center">

**Franc Delmas (Turbo31150)** · [github.com/Turbo31150](https://github.com/Turbo31150) · Toulouse

*PROMPT·VAULT — Multi-AI Prompt Library — MIT License*

</div>
