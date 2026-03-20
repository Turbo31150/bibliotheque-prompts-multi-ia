# Guide d'Utilisation des Prompts

## Comment utiliser cette bibliothèque

### Méthode 1 : Page HTML interactive
1. Ouvrir `index.html` dans un navigateur
2. Utiliser les 3 niveaux de filtres (Modèle / Application / Contexte)
3. Cliquer sur le prompt souhaité pour le copier
4. Coller dans l'outil IA

### Méthode 2 : Fichiers Markdown
1. Naviguer dans le dossier `prompts/`
2. Choisir le sous-dossier correspondant à l'outil (claude-code, gemini-cli, etc.)
3. Ouvrir le fichier .md correspondant au contexte
4. Copier le prompt et l'adapter à votre besoin

### Méthode 3 : Configs prêtes à l'emploi
1. Copier les fichiers de `configs/` vers votre installation
2. `claude-settings.json` → `~/.claude/settings.json`
3. `claude-mcp-servers.json` → fusionner dans `~/.claude.json`
4. `plugin-jarvis-turbo.json` → `~/.claude/plugins/local/jarvis-turbo/plugin.json`

## Par outil

### Claude Code
- **Configuration** : `prompts/claude-code/configuration.md` — Setup MCP, permissions, plugins
- **Développement** : `prompts/claude-code/developpement.md` — Code, refactor, TDD, debug
- **Automatisation** : `prompts/claude-code/automatisation.md` — Agents, skills, hooks, cron
- **Migration** : `prompts/claude-code/migration.md` — Reproduire la config sur nouvelle machine
- **Linux Perf** : `prompts/claude-code/linux-performance-claude.md` — Tuning OS pour IA

### Gemini CLI
- **Code** : `prompts/gemini-cli/generation-code.md` — Génération Python/shell/infra
- **Audit** : `prompts/gemini-cli/audit-systeme.md` — Diagnostic Linux
- **Session** : `prompts/gemini-cli/demarrage-session.md` — Initialiser une session productive

### Codex / OpenAI
- **Linux Perf** : `prompts/codex-openai/linux-performance-codex.md` — Tuning complet
- **Refactoring** : `prompts/codex-openai/refactoring.md` — Refactoring sans casser l'API

### Multi-IA
- **Consensus** : `prompts/multi-ia/consensus-vote.md` — Vote pondéré multi-modèle
- **Dispatch** : `prompts/multi-ia/cluster-dispatch.md` — Routage intelligent 17 domaines

## Bonnes pratiques
1. **Toujours adapter** le prompt à votre contexte spécifique
2. **Commencer** par les prompts de configuration avant les prompts de dev
3. **Vérifier** les résultats avant d'appliquer des modifications système
4. **Sauvegarder** avant toute modification irréversible
5. **Combiner** les prompts (ex: audit → plan → exécution → vérification)
