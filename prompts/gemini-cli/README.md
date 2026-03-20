# Gemini CLI

> Google Gemini en ligne de commande — version **0.34.0**.
> Génération de code, audit système, skills, MCP, sessions persistantes et automatisation.

---

## Installation

```bash
npm install -g @google/gemini-cli
gemini --version     # 0.34.0
```

## Démarrage rapide

```bash
# Mode interactif (conversation)
gemini

# Mode non-interactif (une seule commande)
gemini -p "Explique ce fichier" < mon_fichier.py

# Reprendre la dernière session
gemini --resume latest

# Mode YOLO (tout accepter sans confirmation)
gemini --yolo
```

---

## Fonctionnalités

| Fonctionnalité | Commande | Description |
|---|---|---|
| **Mode interactif** | `gemini` | Conversation dans le terminal. |
| **Mode headless** | `gemini -p "prompt"` | Exécution non-interactive, idéal pour les scripts. |
| **Reprise de session** | `gemini --resume latest` | Reprendre exactement où on s'est arrêté. |
| **Lister les sessions** | `gemini --list-sessions` | Voir toutes les sessions disponibles. |
| **Skills** | `gemini skills list` | Agents spécialisés (auto-debug, auto-learn, project-architect). |
| **Extensions** | `gemini extensions list` | Plugins supplémentaires. |
| **Hooks** | `gemini hooks list` | Automatisations événementielles. |
| **MCP Servers** | `gemini mcp` | Connecter des services externes. |
| **Choix du modèle** | `gemini -m gemini-2.5-pro` | Sélectionner un modèle spécifique. |
| **Mode sandbox** | `gemini -s` | Exécution isolée et sécurisée. |
| **Mode plan** | `gemini --approval-mode plan` | Lecture seule, pas de modification. |
| **Debug** | `gemini -d` | Console de debug (F12). |
| **Sortie JSON** | `gemini -o json -p "prompt"` | Réponse au format JSON. |

## Skills installés

| Skill | Description |
|---|---|
| **auto-debug** | Reproduit le bug, investigue, corrige et vérifie automatiquement. |
| **auto-learn** | Retient les préférences et instructions pour les sessions futures. |
| **project-architect** | Planifie et conçoit l'architecture d'une fonctionnalité ou d'un projet. |

## Modes d'approbation

| Mode | Commande | Effet |
|---|---|---|
| **default** | `gemini` | Demande confirmation pour chaque action. |
| **auto_edit** | `--approval-mode auto_edit` | Éditions de fichiers automatiques, le reste demande. |
| **yolo** | `--yolo` | Tout est accepté automatiquement. |
| **plan** | `--approval-mode plan` | Lecture seule, aucune modification. |

---

## Contenu de ce dossier

### Guides principaux

| Fichier | Description |
|---|---|
| [`generation-code.md`](generation-code.md) | Prompts de génération de code avec Gemini CLI. |
| [`audit-systeme.md`](audit-systeme.md) | Audit système complet : performances, sécurité, configuration. |
| [`demarrage-session.md`](demarrage-session.md) | Démarrer et configurer une session Gemini CLI. |
| [`reprise-conversation.md`](reprise-conversation.md) | Reprendre une conversation précédente sans perdre le contexte. |

### Prompts par catégorie

| Dossier | Contenu |
|---|---|
| [`configuration/`](configuration/) | Installation, authentification Google, paramétrage. |
| [`developpement/`](developpement/) | Génération de code, refactoring, architecture. |
| [`automatisation/`](automatisation/) | Scripts et pipelines automatisés. |
| [`debug/`](debug/) | Diagnostic et résolution de problèmes. |
| [`creation/`](creation/) | Scaffolding de projets. |
| [`documentation/`](documentation/) | Génération de documentation technique. |
| [`migration/`](migration/) | Portage et mise à jour de projets. |
| [`monitoring/`](monitoring/) | Surveillance et métriques. |
| [`recherche/`](recherche/) | Recherche dans le code et sur le web. |
| [`securite/`](securite/) | Audit de sécurité. |
| [`trading/`](trading/) | Prompts trading et analyse financière. |
| [`vocal/`](vocal/) | Intégration vocale. |
| [`web-social/`](web-social/) | Automatisation web. |
| [`skills/`](skills/) | Skills spécifiques Gemini CLI. |
| [`usage/`](usage/) | Guides d'utilisation avancée. |
