# JARVIS Prompt Library

Bibliotheque complete de prompts classes par outil, utilisation, theme et contexte.

## Structure

```
jarvis-prompt-library/
  prompt/
    CLAUDE_CODE/       - Prompts pour Claude Code (CLI/IDE)
    GEMINI_CLI/        - Prompts pour Gemini CLI
    GEMINI_APP/        - Prompts pour Gemini App (bureau)
    CODEX_CLI/         - Prompts pour Codex / OpenAI CLI
    CHATGPT/           - Prompts pour ChatGPT
    PERPLEXITY/        - Prompts pour Perplexity
    BROWSER_OS/        - Prompts pour BrowserOS / agent navigateur
    JARVIS_CORE/       - Prompts pour Jarvis (orchestrateur local)
  scripts/             - Scripts d'initialisation et d'automatisation
  export/              - Fichiers d'export (JSON, CSV, HTML)
```

## Sommaire par outil

| Outil | Utilisations | Fichiers |
|-------|-------------|----------|
| **Claude Code** | Session, Refactor, Tests, Debug, Infra Jarvis, Audit | `prompt/CLAUDE_CODE/` |
| **Gemini CLI** | Session, Code, Reprise, Memoire, Audit, Archi | `prompt/GEMINI_CLI/` |
| **Gemini App** | Session, Flows app, Recherche, Design | `prompt/GEMINI_APP/` |
| **Codex CLI** | Session, Scripts infra, Debug, Refactor, Mode autonome | `prompt/CODEX_CLI/` |
| **ChatGPT** | Session, Code, Recherche, Architecture, Comparatifs | `prompt/CHATGPT/` |
| **Perplexity** | Session, Recherche, Comparatifs, Audit, Plan | `prompt/PERPLEXITY/` |
| **BrowserOS** | Session, Extraction, Automation, Monitoring | `prompt/BROWSER_OS/` |
| **Jarvis Core** | Session, Orchestration, Routing, Securite, Multi-LLM | `prompt/JARVIS_CORE/` |

## Utilisation

1. Naviguer vers l'outil souhaite dans `prompt/`
2. Ouvrir `system-prompts.md` pour les prompts de demarrage de session
3. Ouvrir `task-prompts.md` pour les prompts orientes taches
4. Copier-coller le prompt dans l'outil cible

## Enrichir la bibliotheque

- Ajouter un prompt dans le fichier correspondant a l'outil et au type
- Suivre le format : `### Titre` + `Contexte` + `Attente` + bloc code prompt
- Mettre a jour ce README si une nouvelle categorie est ajoutee

## Deploiement site web

```bash
# Ouvrir le site interactif
open export/site-interactif.html

# Deployer sur GitHub Pages
cp export/site-interactif.html index.html
git add . && git commit -m "Prompt library v1.0" && git push
```
