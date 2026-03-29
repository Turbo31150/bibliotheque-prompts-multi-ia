# OpenClaw — Guide complet

> Agent IA autonome auto-hébergé. Gateway IA du cluster JARVIS.
> Interface web, pipelines, API et intégration multi-modèle.

---

## Architecture

OpenClaw (anciennement Open-WebUI + Pipelines) sert de gateway IA centrale :

```
Utilisateur → OpenClaw (port 18789)
                 ↓
              Pipelines (port 28789)
                 ↓
        ┌────────┼────────┐
        ↓        ↓        ↓
     Ollama   LM Studio  API Cloud
```

## Ports

| Service | Port | Description |
|---|---|---|
| Frontend (WebUI) | `18789` | Interface web utilisateur. |
| Backend (API) | `28789` | API REST et pipelines. |

## Installation

```bash
# Via Docker Compose (recommandé)
docker compose up -d openclaw

# Vérification
curl http://localhost:18789/health
curl http://localhost:28789/health
```

## Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| **Multi-modèle** | Basculer entre Ollama, LM Studio et APIs cloud. |
| **Pipelines** | Chaîner des traitements (RAG, résumé, traduction). |
| **Crons** | 12 tâches planifiées (backup, monitoring, rapports). |
| **API REST** | Endpoints compatibles OpenAI. |
| **Agents** | Agents autonomes avec outils personnalisés. |
| **RAG** | Recherche dans les documents uploadés. |

## Intégration JARVIS

OpenClaw est connecté au cluster JARVIS :
- Routage intelligent vers M1/M2/M3 selon la charge.
- Fallback automatique si un nœud est indisponible.
- 12 crons pour la maintenance automatique.
