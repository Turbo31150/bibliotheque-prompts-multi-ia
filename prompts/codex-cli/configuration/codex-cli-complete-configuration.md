# Codex CLI - Configuration complete de A a Z

## Objectif

Documenter la configuration reelle de Codex CLI sur cette machine pour pouvoir :

- comprendre son comportement
- le reconstruire proprement
- le publier dans la bibliotheque
- le migrer sur une autre machine

## Dossier racine

- [`/home/turbo/.codex`](/home/turbo/.codex)

## Fichiers importants

### Configuration principale

- [`config.toml`](/home/turbo/.codex/config.toml)
  - modele par defaut
  - projets de confiance
  - features
  - MCP

### Regles d'execution

- [`default.rules`](/home/turbo/.codex/rules/default.rules)
  - prefix rules deja approuves
  - decisions de securite
  - commandes frequentes autorisees

### Authentification et metadonnees

- [`auth.json`](/home/turbo/.codex/auth.json)
  - jetons et etat d'auth
  - ne pas publier
- [`version.json`](/home/turbo/.codex/version.json)
  - version locale/outillage
- [`models_cache.json`](/home/turbo/.codex/models_cache.json)
  - cache de modeles visibles

### Historique et etat local

- [`history.jsonl`](/home/turbo/.codex/history.jsonl)
  - historique conversationnel local
- [`state_5.sqlite`](/home/turbo/.codex/state_5.sqlite)
  - etat interne local
- [`logs_1.sqlite`](/home/turbo/.codex/logs_1.sqlite)
  - traces et logs locaux
- [`codex-tui.log`](/home/turbo/.codex/log/codex-tui.log)
  - logs TUI

### Skills et extensions

- [`/home/turbo/.codex/skills`](/home/turbo/.codex/skills)
  - skills installes

### Snapshots shell

- [`/home/turbo/.codex/shell_snapshots`](/home/turbo/.codex/shell_snapshots)
  - captures de commandes shell

## Configuration observee maintenant

### Modele

- `model = "gpt-5.4"`

Effet :
- meilleure qualite generale de code et d'orchestration
- bon choix pour agent principal

### Projet de confiance

- `[projects."/home/turbo"]`
- `trust_level = "trusted"`

Effet :
- le workspace principal est traite comme zone autorisee de travail
- moins de friction sur les operations locales legitimes

### Migration de modele

- `"gpt-5.3-codex" = "gpt-5.4"`

Effet :
- evite de rester sur un ancien alias
- stabilise les usages existants

### Features

- `multi_agent = true`

Effet :
- permet la delegation a des sous-agents quand le workflow l'autorise
- utile pour parallelliser audit, code et verif

### MCP configure

- `openaiDeveloperDocs`
- URL : `https://developers.openai.com/mcp`

Effet :
- acces docs OpenAI officielles depuis Codex
- meilleur support `openai-docs`

## Regles approuvees les plus utiles

### Systeme et supervision

- `systemctl --user`
- `journalctl --user`
- `ps -ef`
- `ps -fp`

### Docker et infra

- `docker ps`
- `docker logs`
- `docker compose`
- `docker inspect`
- `docker run`

### Modeles locaux

- `lms server start`
- `lms server status`
- `curl http://127.0.0.1:1234/v1/models`

### BrowserOS / Playwright / JARVIS

- ouverture BrowserOS
- snapshots Playwright
- health checks locaux

### Git et publication

- `git clone`
- `git ls-remote`
- `git -C /home/turbo/lumen-transcription-multilangue push`

## Ce qu'il faut sauvegarder pour reconstruire Codex CLI

### A conserver

- `~/.codex/config.toml`
- `~/.codex/rules/default.rules`
- `~/.codex/version.json`
- `~/.codex/skills/`

### A garder prudemment

- `~/.codex/history.jsonl`
- `~/.codex/log/`
- `~/.codex/state_5.sqlite`
- `~/.codex/logs_1.sqlite`

### A ne pas publier

- `~/.codex/auth.json`
- contenus secrets ou tokens eventuels

## Ordre de reconstruction sur une nouvelle machine

1. installer Codex CLI
2. recreer `~/.codex/`
3. recopier `config.toml`
4. recopier `rules/default.rules`
5. recopier `skills/`
6. reconnecter l'auth
7. verifier le modele, le trust, le MCP et les skills

## Verification rapide

```bash
sed -n '1,120p' ~/.codex/config.toml
sed -n '1,120p' ~/.codex/rules/default.rules
python3 ~/.codex/skills/.system/skill-installer/scripts/list-skills.py
```

## Prompt pour auditer une installation Codex CLI

```text
Tu es un ingenieur plateforme charge d'auditer Codex CLI.
Lis :
- ~/.codex/config.toml
- ~/.codex/rules/default.rules
- ~/.codex/skills/
- ~/.codex/log/
Donne :
1. la configuration actuelle
2. les implications pratiques
3. les risques de publication
4. la liste de ce qu'il faut sauvegarder ou sanitiser
5. la procedure de reconstruction machine neuve
```
