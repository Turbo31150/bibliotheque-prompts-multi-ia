# Claude Code Skills - Reference Complète

> Extraction complète des 37 skills Claude Code avec prompts, triggers et effets.
> Sauvegarde du 2026-03-20 — JARVIS M1 La Créatrice

---

## Superpowers (14 skills — workflow & processus)

### Workflow de développement
| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **brainstorming** | Avant tout travail créatif, création de features | Explore intentions, requirements et design AVANT d'écrire du code. Empêche de coder sans réfléchir. |
| **writing-plans** | Quand on a un spec/requirements multi-étapes | Crée un plan d'implémentation structuré avant de toucher au code. |
| **executing-plans** | Quand on a un plan écrit à exécuter | Exécute le plan étape par étape avec checkpoints de review humaine. |
| **subagent-driven-development** | Plan avec tâches indépendantes, même session | Dispatche un sous-agent frais par tâche + double review (spec puis qualité). Workflow le plus puissant. |
| **dispatching-parallel-agents** | 2+ tâches indépendantes sans état partagé | Lance plusieurs agents en parallèle. Maximise la vitesse. |

### Qualité & Review
| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **test-driven-development** | Avant d'écrire du code d'implémentation | Force RED-GREEN-REFACTOR. Tests d'abord, code après. Aucune exception. |
| **systematic-debugging** | Bug, test failure, comportement inattendu | Diagnostic méthodique : reproduire → isoler → root cause → fix. Interdit de deviner. |
| **requesting-code-review** | Tâche terminée, avant merge | Demande une review structurée. Template standard. |
| **receiving-code-review** | Feedback de review reçu | Traite le feedback avec rigueur technique. Vérifie avant d'accepter aveuglément. |
| **verification-before-completion** | Avant de dire "c'est terminé" | Force à vérifier avec des commandes réelles. Evidence avant assertions. |

### Git & Branches
| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **using-git-worktrees** | Début de feature nécessitant isolation | Crée un worktree git isolé pour travailler sans polluer le workspace. |
| **finishing-a-development-branch** | Implémentation terminée, tests passent | Guide la finalisation : merge, PR ou cleanup. Options structurées. |

### Méta
| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **writing-skills** | Création/modification de skills | TDD appliqué à la documentation. Test d'abord, skill après. |
| **using-superpowers** | Début de conversation | Établit comment trouver et utiliser les skills. Skill d'amorçage. |

---

## Plugin-Dev (7 skills — création de plugins Claude Code)

| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **plugin-structure** | "create a plugin", "scaffold" | Architecture complète : plugin.json, auto-discovery, composants, `${CLAUDE_PLUGIN_ROOT}` |
| **agent-development** | "create an agent", "add an agent" | Création d'agents autonomes : system prompt, triggering, outils, couleurs |
| **command-development** | "create a slash command" | Commandes /slash : YAML frontmatter, arguments, bash, interactions utilisateur |
| **skill-development** | "create a skill", "add a skill" | Guide complet de création de skills : SKILL.md, progressive disclosure, 6 étapes |
| **hook-development** | "create a hook", événements | Hooks : 8 events (PreToolUse, PostToolUse, Stop, SessionStart...), prompt-based, sécurité |
| **mcp-integration** | "add MCP server", "integrate MCP" | Serveurs MCP : .mcp.json, stdio/SSE/HTTP/WebSocket, debugging |
| **plugin-settings** | "plugin settings", configuration | Config utilisateur : .claude/plugin-name.local.md, YAML frontmatter, lifecycle |

---

## Frontend-Design (1 skill)

| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **frontend-design** | "build web component", "create UI" | Interfaces distinctives : fondation design, anti-patterns IA générique, code = vision artistique |

---

## Autres (3+ skills)

| Skill | Trigger | Effet sur le travail |
|---|---|---|
| **skill-creator** | Créer, modifier, benchmarker des skills | Workflow complet avec evals et variance analysis |
| **playground** | "make a playground", "interactive tool" | Crée des explorateurs HTML single-file avec contrôles et preview live |
| **pinecone** | Opérations sur base vectorielle Pinecone | 7 sous-skills : query, cli, assistant, docs, quickstart, help, mcp |

---

## Configuration Complète

Voir `configs/claude-code-complet/` pour :
- **settings.json** — Permissions globales (Bash, Read, Write, Edit, Agent, MCP...)
- **installed_plugins.json** — 22 plugins avec versions
- **hooks-*.json** — 4 systèmes de hooks actifs
- **mcp-*.json** — 4 serveurs MCP configurés (Playwright, GitHub, Context7, Pinecone)

---

## Comment utiliser un skill

```
# Dans Claude Code, invoquer directement :
/brainstorming
/writing-plans
/test-driven-development
/systematic-debugging

# Ou le skill est auto-détecté selon le contexte
```

## Comment créer un skill personnalisé

1. Lire `superpowers/writing-skills/SKILL.md`
2. Suivre le processus TDD : baseline → write skill → test → refactor
3. Placer dans `~/.claude/skills/` ou dans un plugin
