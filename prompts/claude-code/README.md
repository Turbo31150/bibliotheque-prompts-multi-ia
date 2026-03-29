# Claude Code

> L'outil principal de développement IA en terminal — version **2.1.80**.
> Modèle : Claude Opus 4.6 (1M de contexte).
> 31 skills, 22 plugins, 11 serveurs MCP, mémoire persistante et mode vocal.

---

## Installation

```bash
npm install -g @anthropic-ai/claude-code
claude --version     # 2.1.80
```

## Démarrage rapide

```bash
# Mode interactif (conversation)
claude

# Mode non-interactif (une seule commande)
claude -p "Explique ce fichier" < mon_fichier.py

# Reprendre la dernière session
claude --resume

# Invoquer un skill
claude -p "/brainstorming"

# Lancer avec un modèle spécifique
claude --model opus
```

## Fonctionnalités principales

| Fonctionnalité | Description |
|---|---|
| **31 skills** | Workflows pré-construits (TDD, debug, plans, review, Git). |
| **22 plugins** | Extensions installables (superpowers, playwright, github, etc.). |
| **11 serveurs MCP** | Connexions externes (Calendar, Canva, Notion, GitHub, Pinecone). |
| **Mémoire persistante** | Retient le contexte entre les sessions (10 fichiers). |
| **Hooks** | 4 automatisations (sécurité, learning, skills, insights). |
| **Sous-agents** | Lancer plusieurs agents en parallèle sur des tâches indépendantes. |
| **Mode vocal** | Interaction vocale activée. |
| **Git worktrees** | Isolation de branches pour le développement. |
| **CLAUDE.md** | Instructions automatiques par projet. |

> **Configuration complète de A à Z :** voir [`configs/claude-code-complet/AUDIT-COMPLET.md`](../../configs/claude-code-complet/AUDIT-COMPLET.md)

---

## Contenu de ce dossier

### Guides principaux

| Fichier | Description |
|---|---|
| [`configuration.md`](configuration.md) | Configuration complète : MCP servers, permissions, plugins, settings, memory. |
| [`developpement.md`](developpement.md) | Prompts de génération de code, refactoring, debug et TDD. |
| [`automatisation.md`](automatisation.md) | Agents parallèles, skills, hooks, cron et workflows automatisés. |
| [`migration.md`](migration.md) | Migrer entre versions de Claude Code et adapter les prompts. |
| [`claude-md-template.md`](claude-md-template.md) | Modèle de fichier CLAUDE.md pour vos projets. |
| [`linux-performance-claude.md`](linux-performance-claude.md) | Optimisations Linux spécifiques à Claude Code. |
| [`prompts-avances-cluster-ia.md`](prompts-avances-cluster-ia.md) | Prompts avancés pour le cluster IA multi-machines. |

### Prompts par catégorie

| Dossier | Contenu |
|---|---|
| [`configuration/`](configuration/) | Paramétrage initial, permissions, plugins. |
| [`developpement/`](developpement/) | Génération de code, architecture, patterns. |
| [`automatisation/`](automatisation/) | Cron, hooks, agents, pipelines. |
| [`debug/`](debug/) | Diagnostic, traces, correction de bugs. |
| [`creation/`](creation/) | Création de projets, scaffolding. |
| [`documentation/`](documentation/) | Génération de docs, README, commentaires. |
| [`migration/`](migration/) | Portage, mise à jour, adaptation. |
| [`monitoring/`](monitoring/) | Surveillance, alertes, métriques. |
| [`recherche/`](recherche/) | Recherche dans le code et sur le web. |
| [`securite/`](securite/) | Audit de sécurité, bonnes pratiques. |
| [`trading/`](trading/) | Prompts spécialisés trading et crypto. |
| [`vocal/`](vocal/) | Commandes vocales et intégration TTS. |
| [`web-social/`](web-social/) | Automatisation web et réseaux sociaux. |

### Skills (31 workflows complets)

| Dossier | Contenu |
|---|---|
| [`skills/`](skills/) | **31 skills** avec prompts complets, triggers et mode d'emploi. |
| [`skills/superpowers/`](skills/superpowers/) | 14 skills de workflow (TDD, debug, plans, review, Git). |
| [`skills/plugin-dev/`](skills/plugin-dev/) | 7 skills de création de plugins. |
| [`skills/frontend-design/`](skills/frontend-design/) | Design d'interfaces web professionnelles. |
| [`skills/autres/`](skills/autres/) | Pinecone, playground, skill-creator. |

> **Voir aussi :** [`configs/claude-code-complet/`](../../configs/claude-code-complet/) pour la configuration reproductible de A à Z.
