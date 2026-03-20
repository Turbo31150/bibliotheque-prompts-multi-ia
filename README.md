# Bibliothèque de Prompts Multi-IA

> **Guide complet** pour configurer, utiliser et maîtriser les outils IA modernes.
> De l'installation zéro à un environnement de production multi-IA avec cluster GPU.

---

### Ce que contient ce dépôt

- **31 skills** Claude Code avec leurs prompts complets et détaillés
- **22 plugins** documentés, configurés et prêts à l'emploi
- **Configuration de A à Z**, reproductible par n'importe qui
- **Prompts pour 12 outils IA** : Claude, Gemini, ChatGPT, Codex, Perplexity, BrowserOS, OpenClaw, n8n, LM Studio, Ollama, DeepSeek, Qwen
- **Architecture cluster JARVIS** : 3 machines, 6 GPUs, 10+ modèles locaux

---

## Table des matières

1. [Démarrage rapide](#1--démarrage-rapide)
2. [Installation de Claude Code depuis zéro](#2--installation-de-claude-code-depuis-zéro)
3. [Configuration des permissions](#3--configuration-des-permissions)
4. [Installation des 22 plugins](#4--installation-des-22-plugins)
5. [Les 37 skills : mode d'emploi](#5--les-37-skills--mode-demploi)
6. [Serveurs MCP : connexions externes](#6--serveurs-mcp--connexions-externes)
7. [Hooks : automatisations au démarrage](#7--hooks--automatisations-au-démarrage)
8. [Memory : mémoire persistante entre sessions](#8--memory--mémoire-persistante-entre-sessions)
9. [CLAUDE.md : instructions par projet](#9--claudemd--instructions-par-projet)
10. [Prompts par outil IA](#10--prompts-par-outil-ia)
11. [Modèles locaux](#11--modèles-locaux)
12. [Cluster JARVIS](#12--cluster-jarvis)
13. [Page interactive](#13--page-interactive)
14. [Structure du dépôt](#14--structure-du-dépôt)
15. [Chiffres clés](#15--chiffres-clés)

---

## 1 — Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/Turbo31150/bibliotheque-prompts-multi-ia.git
cd bibliotheque-prompts-multi-ia

# Option A : Parcourir dans le navigateur
open index.html

# Option B : Reproduire toute la configuration Claude Code
# → Suivre les sections 2 à 9 ci-dessous, dans l'ordre
```

---

## 2 — Installation de Claude Code depuis zéro

### Pré-requis

- **Node.js 18+** — vérifier avec `node --version`
- **Un compte Anthropic** avec abonnement (Pro, Max ou Team)
- **Linux, macOS ou WSL2** (Windows natif non supporté)

### Étape 1 — Installer Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### Étape 2 — Première connexion

```bash
claude
# Suivre les instructions pour se connecter avec son compte Anthropic.
# Un navigateur s'ouvre pour l'authentification OAuth.
```

### Étape 3 — Vérifier l'installation

```bash
claude --version
claude /help
```

> **À ce stade**, Claude Code fonctionne, mais avec la configuration par défaut :
> chaque outil demande une confirmation manuelle, aucun plugin n'est installé,
> aucun skill n'est disponible, pas de connexion externe, pas de mémoire.
>
> **Les sections suivantes transforment cette installation vierge en environnement de production.**

---

## 3 — Configuration des permissions

Par défaut, Claude Code demande une autorisation pour **chaque action**. Pour travailler sans friction, on active les permissions globalement.

### Appliquer la configuration

```bash
cp configs/claude-code-complet/settings.json ~/.claude/settings.json
```

> **Important :** Remplacer `/home/turbo` par votre propre chemin dans le fichier `settings.json`.

### Ce que ça change

| Paramètre | Avant (vierge) | Après (configuré) |
|---|---|---|
| Lire des fichiers | Demande à chaque fois | Automatique |
| Écrire des fichiers | Demande à chaque fois | Automatique |
| Exécuter des commandes | Demande à chaque fois | Automatique |
| Chercher dans le code | Demande à chaque fois | Automatique |
| Lancer des sous-agents | Demande à chaque fois | Automatique |
| Naviguer sur le web | Demande à chaque fois | Automatique |
| Mode vocal | Désactivé | Activé |

### Détail des permissions activées

```
Bash(*)           → Exécuter n'importe quelle commande terminal
Read(*)           → Lire n'importe quel fichier
Write(*)          → Créer des fichiers
Edit(*)           → Modifier des fichiers existants
Glob(*)           → Rechercher des fichiers par motif de nom
Grep(*)           → Rechercher dans le contenu des fichiers
Agent(*)          → Lancer des sous-agents spécialisés
WebFetch(*)       → Récupérer du contenu depuis une URL
WebSearch(*)      → Effectuer des recherches sur internet
NotebookEdit(*)   → Modifier des notebooks Jupyter
Skill(*)          → Invoquer des skills
```

### Répertoires autorisés

```
/home/turbo/**    → Tout le dossier personnel
/tmp/**           → Fichiers temporaires
/var/log/**       → Journaux système
/opt/**           → Logiciels complémentaires
```

---

## 4 — Installation des 22 plugins

Les plugins ajoutent des fonctionnalités à Claude Code : nouveaux outils, skills, hooks, connexions externes.

### Installation complète

```bash
# ── Workflow et développement ──
claude plugins install superpowers
claude plugins install commit-commands
claude plugins install feature-dev
claude plugins install code-review
claude plugins install pr-review-toolkit
claude plugins install code-simplifier

# ── Support langages ──
claude plugins install typescript-lsp
claude plugins install pyright-lsp

# ── Outils externes (MCP) ──
claude plugins install playwright
claude plugins install github
claude plugins install context7
claude plugins install pinecone

# ── Création et méta-outils ──
claude plugins install plugin-dev
claude plugins install agent-sdk-dev
claude plugins install skill-creator
claude plugins install claude-code-setup
claude plugins install claude-md-management

# ── Styles de sortie ──
claude plugins install explanatory-output-style
claude plugins install learning-output-style

# ── Sécurité, design et prototypage ──
claude plugins install security-guidance
claude plugins install frontend-design
claude plugins install playground
```

### Description de chaque plugin

| N° | Plugin | Rôle | Impact sur le travail |
|---|---|---|---|
| 1 | **superpowers** | 14 skills de workflow (TDD, debug, plans, review) | Transforme la façon de travailler |
| 2 | **commit-commands** | Git commit, push, PR en une commande | Gain de temps sur Git |
| 3 | **feature-dev** | Développement guidé de fonctionnalités | Structure le travail |
| 4 | **code-review** | Review de code automatisée | Améliore la qualité |
| 5 | **pr-review-toolkit** | Review complète de Pull Requests | Qualité avant merge |
| 6 | **code-simplifier** | Simplifie le code après écriture | Code plus lisible |
| 7 | **typescript-lsp** | Intelligence TypeScript (types, erreurs) | Meilleur code TS |
| 8 | **pyright-lsp** | Intelligence Python (types, erreurs) | Meilleur code Python |
| 9 | **playwright** | Contrôle un navigateur web | Automatisation web |
| 10 | **github** | Opérations GitHub directes | PRs et issues sans quitter le terminal |
| 11 | **context7** | Documentation à jour des librairies | Moins d'erreurs de version |
| 12 | **pinecone** | Base de données vectorielle | Recherche sémantique |
| 13 | **plugin-dev** | Création de plugins Claude Code | Étendre Claude Code |
| 14 | **agent-sdk-dev** | SDK Agent Anthropic | Créer des agents autonomes |
| 15 | **skill-creator** | Création et test de skills | Automatiser ses workflows |
| 16 | **claude-code-setup** | Recommandations de configuration | Optimiser sa config |
| 17 | **claude-md-management** | Gestion des fichiers CLAUDE.md | Instructions par projet |
| 18 | **explanatory-output-style** | Explications éducatives automatiques | Apprendre en travaillant |
| 19 | **learning-output-style** | Mode d'apprentissage interactif | Participation active |
| 20 | **security-guidance** | Vérification de sécurité à chaque écriture | Protection automatique |
| 21 | **frontend-design** | Interfaces web de qualité professionnelle | Design soigné, pas de templates |
| 22 | **playground** | Outils HTML interactifs en une page | Prototypage rapide |

---

## 5 — Les 37 skills : mode d'emploi

Un **skill** est un workflow pré-construit. On l'invoque avec `/nom-du-skill` dans Claude Code, ou il se déclenche automatiquement selon le contexte.

> **Tous les prompts complets** sont disponibles dans `prompts/claude-code/skills/`.

### Superpowers : 14 skills de workflow

Ce sont les plus importants. Ils structurent chaque étape du développement.

#### Avant de coder

| Commande | Quand l'utiliser | Ce que ça fait |
|---|---|---|
| `/brainstorming` | Avant toute création | Explore les besoins, les contraintes et le design **avant** d'écrire du code. |
| `/writing-plans` | Quand on a un cahier des charges | Crée un plan d'implémentation structuré, étape par étape. |

#### Pendant le développement

| Commande | Quand l'utiliser | Ce que ça fait |
|---|---|---|
| `/test-driven-development` | Avant d'écrire du code | Force le cycle RED-GREEN-REFACTOR : tests d'abord, code après. |
| `/systematic-debugging` | Quand un bug apparaît | Diagnostic méthodique : reproduire → isoler → trouver la cause → corriger. |
| `/subagent-driven-development` | Plan avec tâches indépendantes | Lance un sous-agent par tâche, avec double review (spécification puis qualité). |
| `/dispatching-parallel-agents` | Deux tâches ou plus sans lien | Lance plusieurs agents en parallèle pour gagner du temps. |
| `/executing-plans` | Exécuter un plan existant | Exécute chaque étape avec validation humaine entre les tâches. |

#### Qualité et review

| Commande | Quand l'utiliser | Ce que ça fait |
|---|---|---|
| `/requesting-code-review` | Code terminé, avant merge | Demande une review structurée avec template standard. |
| `/receiving-code-review` | Quand on reçoit du feedback | Traite le feedback avec rigueur technique, vérifie avant d'accepter. |
| `/verification-before-completion` | Avant de dire « c'est terminé » | Oblige à vérifier avec des commandes réelles. Preuve avant affirmation. |

#### Git et finalisation

| Commande | Quand l'utiliser | Ce que ça fait |
|---|---|---|
| `/using-git-worktrees` | Début d'une fonctionnalité | Crée un espace de travail Git isolé, sans polluer la branche principale. |
| `/finishing-a-development-branch` | Tout est testé et prêt | Guide vers la bonne option : merge, PR ou nettoyage. |

#### Méta

| Commande | Quand l'utiliser | Ce que ça fait |
|---|---|---|
| `/writing-skills` | Créer un nouveau skill | Applique le TDD à la documentation : tester d'abord, écrire après. |
| `/using-superpowers` | Automatique au démarrage | Détecte quel skill utiliser selon le contexte de la conversation. |

### Plugin-Dev : 7 skills de création

Pour créer vos propres extensions Claude Code :

| Skill | Ce que ça fait |
|---|---|
| `plugin-structure` | Architecture d'un plugin : manifest, composants, auto-discovery. |
| `agent-development` | Créer des agents autonomes avec system prompt et conditions de déclenchement. |
| `command-development` | Créer des commandes `/slash` avec arguments et interactions. |
| `skill-development` | Créer de nouveaux skills avec progressive disclosure. |
| `hook-development` | Créer des hooks événementiels (8 types d'événements disponibles). |
| `mcp-integration` | Connecter des services externes via le protocole MCP. |
| `plugin-settings` | Gérer la configuration utilisateur d'un plugin. |

### Autres skills

| Skill | Ce que ça fait |
|---|---|
| `frontend-design` | Crée des interfaces web de qualité professionnelle, anti-template IA. |
| `skill-creator` | Workflow complet : créer, tester, benchmarker et publier un skill. |
| `playground` | Crée des outils HTML interactifs en une seule page, avec contrôles et preview. |
| `pinecone` | Sept sous-skills pour la base vectorielle Pinecone (query, cli, assistant, docs, quickstart, help, mcp). |

---

## 6 — Serveurs MCP : connexions externes

Le protocole **MCP** (Model Context Protocol) connecte Claude Code à des services externes.

### Serveurs cloud (automatiques avec un abonnement Max)

| Serveur | Ce que ça permet |
|---|---|
| **Google Calendar** | Lire, créer et modifier des événements de calendrier. |
| **Canva** | Créer et modifier des designs graphiques. |
| **Notion** | Lire et écrire dans des bases Notion. |

### Serveurs installés avec les plugins

| Serveur | Plugin associé | Ce que ça permet |
|---|---|---|
| **Playwright** | `playwright` | Contrôler un navigateur : cliquer, remplir, capturer. |
| **GitHub** | `github` | Gérer les repos, PRs et issues sans quitter le terminal. |
| **Context7** | `context7` | Obtenir la documentation à jour de n'importe quelle librairie. |
| **Pinecone** | `pinecone` | Effectuer des recherches sémantiques dans une base vectorielle. |

### Serveurs personnalisés (projets locaux)

Pour connecter vos propres services, créer un fichier `.mcp.json` à la racine du projet :

```json
{
    "mcpServers": {
        "mon-service": {
            "command": "python3",
            "args": ["chemin/vers/mon_serveur_mcp.py"],
            "env": { "API_KEY": "votre-clé" }
        }
    }
}
```

> Voir `configs/claude-code-complet/mcp-*.json` pour des exemples réels (JARVIS, LM Studio, Filesystem).

---

## 7 — Hooks : automatisations au démarrage

Les **hooks** exécutent des actions automatiquement en réponse à des événements.

### Hooks actifs dans cette configuration

| Hook | Événement | Effet |
|---|---|---|
| **superpowers** | `SessionStart` | Charge le système de skills au lancement de chaque session. |
| **learning-output-style** | `SessionStart` | Active le mode d'apprentissage interactif. |
| **explanatory-output-style** | `SessionStart` | Ajoute des encadrés d'explication éducative. |
| **security-guidance** | `PreToolUse` (Edit/Write) | Vérifie la sécurité avant chaque modification de fichier. |

### Événements disponibles

| Événement | Quand il se déclenche |
|---|---|
| `SessionStart` | Au lancement de `claude`. |
| `PreToolUse` | Avant chaque utilisation d'outil (lecture, écriture, commande). |
| `PostToolUse` | Après chaque utilisation d'outil. |
| `Stop` | Quand Claude termine sa réponse. |
| `UserPromptSubmit` | Quand l'utilisateur envoie un message. |
| `PreCompact` | Avant la compression du contexte. |
| `Notification` | Quand une notification est émise. |

> Les hooks sont gérés par les plugins. Pas de configuration manuelle nécessaire.
> Voir `configs/claude-code-complet/hooks-*.json` pour le détail technique.

---

## 8 — Memory : mémoire persistante entre sessions

Claude Code peut **retenir des informations** d'une conversation à l'autre.

### Types de mémoire

| Type | Exemple | Utilité |
|---|---|---|
| **user** | Langue préférée, niveau technique, profil | Adapter les réponses à l'utilisateur. |
| **project** | Décisions d'architecture, contraintes | Ne pas ré-expliquer le contexte à chaque session. |
| **feedback** | « Ne fais pas X », « Continue à faire Y » | Éviter de répéter les mêmes erreurs. |
| **reference** | « Les bugs sont dans Linear projet X » | Savoir où chercher l'information. |

### Emplacement des fichiers

```
~/.claude/projects/<identifiant-projet>/memory/
├── MEMORY.md              ← Index (toujours chargé automatiquement)
├── user_language.md       ← Préférence de langue
├── user_profile.md        ← Profil utilisateur
├── project_*.md           ← Contexte des projets
└── ...
```

### Comment sauvegarder une mémoire

Dire à Claude :
— *« Retiens que je préfère les réponses concises. »*
— *« Souviens-toi que le projet Y utilise PostgreSQL et non SQLite. »*
— *« Oublie l'information sur le serveur X, ce n'est plus vrai. »*

> Voir `configs/claude-code-complet/memory/` pour 10 exemples de fichiers mémoire réels.

---

## 9 — CLAUDE.md : instructions par projet

Chaque projet peut avoir un fichier `CLAUDE.md` à sa racine. Claude le lit **automatiquement** et suit ses instructions à chaque session.

### Exemple de CLAUDE.md

```markdown
# Instructions pour ce projet

## Contraintes
- Toujours utiliser `127.0.0.1` au lieu de `localhost`.
- Ne jamais committer les fichiers `.env`.
- GPU : alerte à 75 °C, critique à 85 °C.

## Architecture
- Backend : FastAPI (Python 3.12)
- Frontend : React + TypeScript
- Base de données : SQLite avec FTS5

## Commandes utiles
- `make test` — Lancer les tests.
- `make dev` — Lancer le serveur de développement.
- `docker compose up` — Démarrer les services.
```

> Voir `configs/claude-code-complet/claude-md/` pour quatre exemples réels de projets JARVIS.

---

## 10 — Prompts par outil IA

Chaque dossier contient des prompts prêts à l'emploi, classés par outil.

| Dossier | Outil | Contenu |
|---|---|---|
| `prompts/claude-code/` | Claude Code (terminal) | Configuration, développement, automatisation, **37 skills complets** |
| `prompts/claude-api/` | API Anthropic | Intégration directe dans vos applications |
| `prompts/gemini-cli/` | Gemini CLI (terminal) | Génération de code, audit système, sessions |
| `prompts/gemini-app/` | Gemini (navigateur) | Prompts pour l'interface web |
| `prompts/chatgpt/` | ChatGPT | Configuration et prompts optimisés |
| `prompts/codex-cli/` | Codex CLI (OpenAI) | Utilisation en terminal |
| `prompts/codex-openai/` | Codex OpenAI | Refactoring, performance Linux |
| `prompts/perplexity/` | Perplexity | Recherche technique, veille crypto |
| `prompts/browseros/` | BrowserOS | Automatisation web, LinkedIn |
| `prompts/openclaw/` | OpenClaw | Configuration et prompts |
| `prompts/n8n/` | n8n | 65 workflows JARVIS documentés |
| `prompts/multi-ia/` | Multi-IA | Consensus multi-modèle, dispatch cluster |

---

## 11 — Modèles locaux

Configuration et benchmarks de cinq familles de modèles tournant en local sur GPU.

| Modèle | Outil | VRAM requise | Vitesse | Qualité |
|---|---|---|---|---|
| Qwen3-8b | LM Studio | 6 Go | 65 tok/s | 98,4/100 |
| Qwen3-coder-30b | LM Studio | 12 Go | 25 tok/s | Excellent pour le code |
| DeepSeek-R1 (7b) | Ollama | 8 Go | 40 tok/s | Raisonnement avancé |
| Gemma-3-4b | LM Studio | 4 Go | 80 tok/s | Classification rapide |
| GPT-OSS-20b | LM Studio | 12 Go | 15 tok/s | Généraliste |

> Voir `prompts/models-locaux/` pour la configuration détaillée, les commandes d'installation et les benchmarks de chaque modèle.

---

## 12 — Cluster JARVIS

Architecture du cluster IA distribué sur trois machines physiques.

### Machines

| Machine | Rôle | Caractéristiques |
|---|---|---|
| **M1** « La Créatrice » | Orchestration + inférence GPU | AMD Ryzen 7 5700X3D, 6 GPUs NVIDIA, 46 Go RAM |
| **M2** | Inférence lourde | DeepSeek-R1 dédié |
| **M3** / Serveur | Inférence + stockage | 3× Quadro, 45 Go RAM |

### Composants documentés

| Composant | Dossier | Description |
|---|---|---|
| **Dispatch Engine** | `prompts/cluster/dispatch-engine/` | Pipeline intelligent en 9 étapes : cache, health, auto-load, route, enrichissement, dispatch, qualité, feedback, post-traitement. |
| **Consensus** | `prompts/cluster/consensus/` | Vote pondéré entre 5 modèles, avec seuil de confiance. |
| **Routage** | `prompts/cluster/routage/` | Matrice 17 domaines × 6 nœuds, poids multi-niveaux. |
| **Self-Healing** | `prompts/cluster/self-healing/` | Réparation automatique : détection → diagnostic → réparation → vérification. |
| **GPU Management** | `prompts/cluster/gpu-management/` | 6 GPUs, garde thermique (75 °C / 85 °C), allocation VRAM. |
| **Backup** | `prompts/cluster/backup/` | 103 bases SQLite, synchronisation quotidienne, notification Telegram. |

---

## 13 — Page interactive

Ouvrir `index.html` dans un navigateur pour accéder à **tous les prompts** avec :

- **Filtrage par outil IA** : Claude, Gemini, ChatGPT, Perplexity, BrowserOS.
- **Filtrage par contexte** : Setup, Code, Debug, Trading, Automation, Monitoring.
- **Copie en un clic** vers le presse-papiers.
- **245 cartes** de prompts navigables.

---

## 14 — Structure du dépôt

```
bibliotheque-prompts-multi-ia/
│
├── README.md                              ← Ce document
├── index.html                             ← Interface web interactive (245 cartes)
│
├── configs/
│   ├── claude-code-complet/               ← Configuration COMPLÈTE reproductible
│   │   ├── AUDIT-COMPLET.md               ← Comparaison : installation vierge vs configurée
│   │   ├── settings.json                  ← Permissions et plugins actifs
│   │   ├── installed_plugins.json         ← 22 plugins avec versions et dates
│   │   ├── hooks-*.json (×4)             ← Hooks actifs (SessionStart, PreToolUse)
│   │   ├── mcp-*.json (×7)              ← Serveurs MCP (plugins + projets)
│   │   ├── memory/ (10 fichiers)          ← Mémoire persistante complète
│   │   └── claude-md/ (4 fichiers)        ← Instructions CLAUDE.md par projet
│   ├── claude-settings.json               ← Configuration simplifiée
│   └── claude-mcp-servers.json            ← Serveurs MCP (version légère)
│
├── prompts/
│   ├── claude-code/
│   │   ├── skills/                        ← 37 SKILLS COMPLETS (prompts inclus)
│   │   │   ├── README.md                  ← Index détaillé avec triggers et effets
│   │   │   ├── superpowers/ (14 skills)   ← Workflow : TDD, debug, plans, review
│   │   │   ├── plugin-dev/ (7 skills)     ← Création : agents, commandes, hooks
│   │   │   ├── frontend-design/ (1 skill) ← Design UI de qualité professionnelle
│   │   │   └── autres/ (15 skills)        ← Pinecone, playground, skill-creator
│   │   ├── automatisation/                ← Prompts d'automatisation
│   │   ├── configuration/                 ← Prompts de configuration
│   │   ├── developpement/                 ← Prompts de développement
│   │   ├── debug/                         ← Prompts de débogage
│   │   └── ...                            ← Autres catégories
│   │
│   ├── gemini-cli/                        ← Prompts Gemini CLI
│   ├── chatgpt/                           ← Prompts ChatGPT
│   ├── codex-cli/                         ← Prompts Codex CLI
│   ├── perplexity/                        ← Prompts Perplexity
│   ├── browseros/                         ← Prompts BrowserOS
│   ├── openclaw/                          ← Prompts OpenClaw
│   ├── n8n/                               ← 65 workflows n8n
│   ├── multi-ia/                          ← Consensus multi-modèle
│   ├── models-locaux/                     ← 5 modèles locaux documentés
│   └── cluster/                           ← 6 composants du cluster JARVIS
│
└── docs/
    ├── GUIDE-UTILISATION.md               ← Guide général d'utilisation
    ├── PREREQUIS.md                       ← Pré-requis détaillés
    ├── EFFETS-SUR-MODELES.md              ← Impact des plugins sur le comportement
    └── CLAUDE_CODE_MIGRATION_GUIDE.md     ← Migration entre versions de Claude Code
```

---

## 15 — Chiffres clés

| Métrique | Valeur |
|---|---|
| Prompts documentés | 245+ |
| Skills avec prompts complets | 31 |
| Plugins configurés et documentés | 22 |
| Serveurs MCP connectés | 11 |
| Hooks actifs | 4 |
| Fichiers mémoire persistante | 10 |
| Workflows n8n | 65 |
| Modèles locaux documentés | 5 |
| Composants cluster | 6 |
| Lignes de documentation | 38 000+ |

---

## Contribuer

1. Forker le dépôt.
2. Ajouter vos prompts dans le dossier correspondant.
3. Mettre à jour le `README.md` si nécessaire.
4. Créer une Pull Request.

---

## Auteur

**Turbo31150** — Créateur de **[JARVIS](https://github.com/Turbo31150/jarvis-linux)**

> Projet JARVIS : 320 000 lignes de code, 317 modules Python, 674 endpoints REST,
> 10 services Docker, pilotage vocal complet de Linux (1 007 commandes),
> cluster GPU distribué sur 3 machines.

---

*Dernière mise à jour : 20 mars 2026*
