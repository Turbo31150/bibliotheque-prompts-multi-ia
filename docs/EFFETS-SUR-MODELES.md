# Effets des Configurations sur les Modèles IA

## Comment les settings changent le comportement de Claude

### Permissions
| Permission | Effet sur le modèle |
|-----------|-------------------|
| `Bash(*)` | Claude peut exécuter des commandes — il devient un SRE actif |
| `Read(*)` | Claude lit le code source — il comprend l'architecture existante |
| `Write(*)` | Claude crée des fichiers — il peut implémenter des solutions |
| `Edit(*)` | Claude modifie le code — il peut refactorer chirurgicalement |
| `Agent(*)` | Claude lance des sous-agents — il parallélise le travail |
| `Skill(*)` | Claude utilise des workflows structurés (TDD, brainstorming, debug) |
| `mcp__*` | Claude accède aux services externes (JARVIS, GitHub, BrowserOS) |

### Plugins et leur impact

| Plugin | Impact sur le comportement |
|--------|--------------------------|
| **superpowers** | Force Goal/Plan/Code/Verify. Claude ne code plus sans plan. |
| **frontend-design** | Active un mode design premium. Les UIs générées sont pro. |
| **code-review** | Active un mode critique. Claude cherche bugs et failles. |
| **security-guidance** | Checks OWASP en arrière-plan. Claude évite les injections. |
| **learning-output-style** | Mode tuteur. Claude pose des questions au lieu de tout faire. |
| **explanatory-output-style** | Mode éducatif. Claude explique chaque décision. |
| **context7** | Vérifie la doc avant de coder. Réduit les hallucinations d'API. |

### MCP Servers et capacités ajoutées

| MCP Server | Capacité ajoutée au modèle |
|-----------|---------------------------|
| `jarvis-ws` | 674 endpoints — santé, trading, logs, backup, mémoire, RAG |
| `jarvis-proxy` | Dispatch vers 6 moteurs IA (M1, M2, Ollama, Gemini, Claude) |
| `browseros` | Navigation web, clics, extraction de données, automation LinkedIn |
| `jarvis-openclaw` | 850+ agents autonomes, crons IA, skills |
| `mon-flask-mcp` | GPU scaling, crypto trading, vagues d'automatisation |

### Plugin jarvis-turbo — Transformation du modèle

Les 11 skills transforment Claude en opérateur JARVIS :
- **cluster-management** : Claude sait gérer M1/M2/M3/OL1
- **trading-pipeline** : Claude comprend le pipeline OMEGA v2.3
- **smart-routing** : Claude route les requêtes vers le bon noeud
- **weighted-orchestration** : Claude fait voter 5 modèles avant d'agir
- **browser-workflow** : Claude pilote BrowserOS via CDP

Les 7 agents spécialisent Claude :
- **jarvis-devops** : Mode SRE — auto-heal, monitoring, déploiement
- **jarvis-gpu-manager** : Mode GPU — thermal, VRAM, persistence, redistribution
- **jarvis-code-reviewer** : Mode review — analyse multi-modèle du code

Les 2 hooks modifient le runtime :
- **gpu-thermal-guard** : Après chaque commande, vérifie la température GPU
- **session-cluster-check** : Au démarrage, health check automatique du cluster

## Impact combiné

Avec TOUTE la configuration activée, Claude Code devient :
1. Un **SRE expert** qui monitore et répare le cluster
2. Un **développeur senior** qui code en TDD avec review
3. Un **trader** qui scanne 200 paires et fait voter 5 modèles
4. Un **architecte** qui planifie avant d'implémenter
5. Un **assistant web** qui pilote BrowserOS et LinkedIn
6. Un **opérateur 24/7** via 65 n8n workflows + 12 crons + 11 OpenClaw crons
