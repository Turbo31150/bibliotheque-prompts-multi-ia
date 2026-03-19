# OpenClaw - Web & Social

## Vue d'ensemble

Automatisation LinkedIn et GitHub via les agents OpenClaw, avec integration BrowserOS pour les actions navigateur.

## LinkedIn

### Agent social-agent

| Fonction | Description | Schedule |
|----------|-------------|----------|
| Publication | Post automatique LinkedIn | Lun-Ven 9h |
| Engagement | Likes, commentaires sur le feed | 2x/jour |
| Connexions | Acceptation demandes | Quotidien |
| Analytics | Metriques de posts | Hebdomadaire |

### Pipeline de publication

1. **Generation** : le social-agent genere le contenu via LLM
2. **Validation** : verification du ton, longueur, hashtags
3. **Publication** : envoi a BrowserOS via MCP pour poster sur LinkedIn
4. **Suivi** : verification du post publie + metriques initiales

```bash
# Declenchement manuel
curl -X POST http://localhost:28789/api/agents/social-agent/run \
  -H "Authorization: Bearer $OPENCLAW_AUTH_TOKEN" \
  -d '{"skill": "linkedin_post", "params": {"topic": "IA et DevOps"}}'
```

## GitHub

### Agent dev-agent

| Fonction | Description | Schedule |
|----------|-------------|----------|
| Watch repos | Surveillance nouveaux commits/PRs | Toutes les 30 min |
| Issues triage | Classification automatique des issues | Sur evenement |
| PR review | Revue de code assistee par IA | Sur evenement |
| Release notes | Generation notes de version | Sur tag |

### Surveillance des repos

Le `github_watch` cron surveille les repos configures :

```json
{
  "watched_repos": [
    "turbo/jarvis-linux",
    "turbo/bibliotheque-prompts-multi-ia",
    "turbo/trading-bot"
  ],
  "events": ["push", "pull_request", "issues", "release"]
}
```

## Integration BrowserOS

Les actions necessitant un navigateur (publication LinkedIn, navigation GitHub) sont deleguees a BrowserOS via le serveur MCP `browseros-mcp` :

```
social-agent -> skill linkedin_post -> browseros-mcp -> CDP port 9105 -> LinkedIn
```

Cette architecture permet aux agents OpenClaw d'interagir avec des sites web authentifies sans gerer directement les sessions navigateur.
