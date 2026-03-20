# Codex CLI

> OpenAI Codex en ligne de commande — version **0.115.0**.
> Développement assisté, review de code, sandbox, multi-agent et modèles locaux.

---

## Installation

```bash
npm install -g @openai/codex
codex --version     # 0.115.0
```

## Démarrage rapide

```bash
# Mode interactif (conversation)
codex

# Mode non-interactif (une seule commande)
codex exec "Refactore ce fichier pour utiliser async/await"

# Review de code automatique
codex review

# Full auto (sandbox + approbation automatique)
codex --full-auto "Ajoute des tests unitaires"

# Avec un modèle spécifique
codex -m gpt-5.4 "Optimise cette fonction"

# Avec modèle local (LM Studio ou Ollama)
codex --oss "Explique ce code"
```

---

## Fonctionnalités

| Fonctionnalité | Commande | Description |
|---|---|---|
| **Mode interactif** | `codex` | Conversation dans le terminal. |
| **Exécution directe** | `codex exec "prompt"` | Mode non-interactif, une commande et sortie. |
| **Review de code** | `codex review` | Analyse automatique du code modifié. |
| **Reprendre une session** | `codex resume` | Reprendre où on s'est arrêté. |
| **Forker une session** | `codex fork` | Repartir d'une session existante. |
| **Appliquer un diff** | `codex apply` | Appliquer le dernier diff produit par Codex. |
| **MCP Servers** | `codex mcp list` | Connecter des services externes. |
| **Codex comme MCP** | `codex mcp-server` | Utiliser Codex comme serveur MCP (stdio). |
| **Sandbox** | `codex --sandbox read-only` | Exécution isolée et sécurisée. |
| **Multi-agent** | config `multi_agent = true` | Plusieurs agents en parallèle. |
| **Modèles locaux** | `codex --oss` | Utiliser LM Studio ou Ollama. |
| **Recherche web** | `codex --search` | Recherche web en temps réel. |
| **Images** | `codex -i image.png "Analyse"` | Analyse d'images jointes au prompt. |
| **Cloud** | `codex cloud` | Tâches distantes Codex Cloud. |

## Modes de sandbox

| Mode | Commande | Effet |
|---|---|---|
| **read-only** | `--sandbox read-only` | Lecture seule, aucune écriture. |
| **workspace-write** | `--sandbox workspace-write` | Écriture limitée au workspace. |
| **danger-full-access** | `--sandbox danger-full-access` | Accès complet (dangereux). |

## Modes d'approbation

| Mode | Commande | Effet |
|---|---|---|
| **untrusted** | `-a untrusted` | Seules les commandes de confiance passent (ls, cat, sed). |
| **on-request** | `-a on-request` | Le modèle décide quand demander. |
| **never** | `-a never` | Jamais d'approbation (pour scripts automatisés). |
| **full-auto** | `--full-auto` | Sandbox + approbation automatique (recommandé). |

## Configuration actuelle

```toml
# ~/.codex/config.toml
model = "gpt-5.4"

[features]
multi_agent = true

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

---

## Contenu de ce dossier

### Prompts par catégorie

| Dossier | Contenu |
|---|---|
| [`configuration/`](configuration/) | Installation, clé API, modèles, sandbox, config.toml. |
| [`developpement/`](developpement/) | Génération de code, refactoring, architecture. |
| [`automatisation/`](automatisation/) | Scripts et pipelines automatisés. |
| [`debug/`](debug/) | Diagnostic et résolution de problèmes. |
| [`creation/`](creation/) | Scaffolding de projets. |
| [`documentation/`](documentation/) | Génération de documentation. |
| [`migration/`](migration/) | Portage et mise à jour. |
| [`monitoring/`](monitoring/) | Surveillance et métriques. |
| [`recherche/`](recherche/) | Recherche dans le code. |
| [`securite/`](securite/) | Audit de sécurité. |
| [`trading/`](trading/) | Prompts trading. |
| [`vocal/`](vocal/) | Intégration vocale. |
| [`web-social/`](web-social/) | Automatisation web. |
