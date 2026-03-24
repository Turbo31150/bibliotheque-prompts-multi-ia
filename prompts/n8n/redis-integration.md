# n8n Redis Integration Workflow

> 🟢 Vert — Automatisation, Redis, workflows  
> Agent: n8n

```text
Crée un workflow n8n qui:
1. Écoute la queue Redis JARVIS (trigger: Redis)
2. Parse le JSON de la tâche
3. Route selon le type (IF node)
4. Exécute l'action (HTTP Request / Code / Command)
5. Retourne le résultat dans Redis (ack/fail)
6. Log dans un Google Sheet ou webhook

Nodes nécessaires: Redis Trigger, IF, HTTP Request, Code, Redis Set
```
