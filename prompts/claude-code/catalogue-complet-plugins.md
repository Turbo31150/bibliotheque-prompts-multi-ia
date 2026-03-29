# Claude Code — Catalogue Complet Plugins, Skills, Agents, Commands

> 31 plugins | 89 skills | 31 agents | 20 commands | 2 hooks | 66 domino chains
> Derniere mise a jour : 2026-03-29

---

## SKILLS (89) — Classes par ponderation utilite

### Tier S — Usage quotidien (ponderation 10)

| Skill | Plugin | Declencheur | Prompt d'utilisation |
|-------|--------|-------------|---------------------|
| brainstorming | superpowers | Avant tout travail creatif | `/brainstorm` ou "Je veux creer [X]" |
| verification-before-completion | superpowers | Avant de dire "c'est fait" | Automatique — bloque les claims sans preuve |
| systematic-debugging | superpowers | Bug, erreur, echec test | "J'ai une erreur [X]" ou automatique sur echec |
| writing-plans | superpowers | Avant implementation multi-etapes | `/write-plan` ou "Planifie [X]" |
| test-driven-development | superpowers | Avant d'ecrire du code | "Implemente [feature]" → TDD auto |
| jarvis-omega-megaprompt | jarvis-turbo | A chaque session | Charge automatique (claude-only) |
| demarrage | jarvis-turbo | Boot JARVIS | `/demarrage` |

### Tier A — Usage frequent (ponderation 8)

| Skill | Plugin | Declencheur | Prompt d'utilisation |
|-------|--------|-------------|---------------------|
| executing-plans | superpowers | Apres un plan ecrit | `/execute-plan` |
| dispatching-parallel-agents | superpowers | 2+ taches independantes | Automatique si taches paralleles |
| subagent-driven-development | superpowers | Plan avec taches independantes | Automatique pendant execution |
| requesting-code-review | superpowers | Apres feature complete | Automatique post-implementation |
| receiving-code-review | superpowers | Feedback de review recu | Quand review feedback arrive |
| using-git-worktrees | superpowers | Feature isolee | "Travaille sur [feature] en isolation" |
| finishing-a-development-branch | superpowers | Implementation terminee | "C'est pret a merger" |
| using-superpowers | superpowers | Debut de session | Automatique |
| chrome-devtools | chrome-devtools-mcp | Debug web | "Debug cette page web" |
| frontend-design | frontend-design | UI/composants web | "Cree un composant [X]" |
| skill-creator | skill-creator | Creer/modifier skill | "Cree un skill pour [X]" |
| claude-md-improver | claude-md-management | Audit CLAUDE.md | `/revise-claude-md` |
| playground | playground | Outil interactif HTML | "Cree un playground pour [X]" |

### Tier B — Usage regulier (ponderation 6)

| Skill | Plugin | Declencheur | Prompt d'utilisation |
|-------|--------|-------------|---------------------|
| build-mcp-server | mcp-server-dev | Creer serveur MCP | "Construis un MCP pour [API]" |
| build-mcp-app | mcp-server-dev | UI dans MCP | "Ajoute un widget a mon MCP" |
| build-mcpb | mcp-server-dev | Packager MCP | "Package mon MCP en .mcpb" |
| skill-development | plugin-dev | Creer skill plugin | "Cree un skill [nom]" |
| agent-development | plugin-dev | Creer agent plugin | "Cree un agent [nom]" |
| command-development | plugin-dev | Creer commande | "Cree une commande /[nom]" |
| hook-development | plugin-dev | Creer hook | "Cree un hook PreToolUse pour [X]" |
| mcp-integration | plugin-dev | Integrer MCP | "Ajoute un serveur MCP [X]" |
| plugin-structure | plugin-dev | Architecture plugin | "Structure un plugin pour [X]" |
| plugin-settings | plugin-dev | Config plugin | "Ajoute des settings au plugin" |
| writing-hookify-rules | hookify | Creer regle hookify | `/hookify` |
| configure (telegram) | telegram | Setup Telegram | "Configure le bot Telegram" |
| access (telegram) | telegram | Gestion acces | "Approuve [user] pour Telegram" |

### Tier C — Usage specialise (ponderation 4)

| Skill | Plugin | Declencheur | Prompt d'utilisation |
|-------|--------|-------------|---------------------|
| a11y-debugging | chrome-devtools-mcp | Accessibilite | "Audite l'accessibilite de cette page" |
| debug-optimize-lcp | chrome-devtools-mcp | Performance web | "Optimise le LCP de cette page" |
| troubleshooting | chrome-devtools-mcp | Erreur CDP | Automatique si CDP echoue |
| claude-automation-recommender | claude-code-setup | Setup Claude Code | `/claude-automation-recommender` |
| pinecone:* (7 skills) | pinecone | Vector DB | "Cree un index Pinecone" |
| qodo-* (3 skills) | qodo-skills | Regles code | "Charge les regles Qodo" |

### Tier J — JARVIS specifique (ponderation 8)

| Skill | Plugin | Declencheur | Prompt d'utilisation |
|-------|--------|-------------|---------------------|
| Cluster Management | jarvis-turbo | Cluster ops | `/cluster-check` |
| Smart Routing | jarvis-turbo | Routing taches | "Route cette tache vers [noeud]" |
| Weighted Orchestration | jarvis-turbo | Consensus pondere | `/consensus "question"` |
| Security Audit | jarvis-turbo | Audit securite | "Audite la securite du cluster" |
| Performance Tuning | jarvis-turbo | Optimisation | "Optimise les performances GPU" |
| Failover Recovery | jarvis-turbo | Noeud offline | Automatique si noeud DOWN |
| Continuous Improvement | jarvis-turbo | Amelioration | "Prochaine amelioration ?" |
| Trading Pipeline | jarvis-turbo | Trading | `/trading-scan` |
| MAO Workflow | jarvis-turbo | Multi-agent | `/consensus` |
| browser-workflow | jarvis-turbo | Web automation | `/browse [url]` |
| browseros-skill-triggers | jarvis-turbo | Auto-declenchement | Automatique par mots-cles |
| Autotest Analysis | jarvis-turbo | Analyse tests | Apres autotests |

---

## AGENTS (31) — Classes par impact

### Agents de Review (impact: 9)

| Agent | Plugin | Auto-trigger | Prompt |
|-------|--------|-------------|--------|
| code-reviewer | feature-dev | Apres ecriture de code | Automatique |
| code-reviewer | pr-review-toolkit | Avant commit | `/review-pr` |
| code-reviewer | superpowers | Apres feature | Automatique |
| silent-failure-hunter | pr-review-toolkit | Error handling ecrit | Automatique |
| comment-analyzer | pr-review-toolkit | Documentation ajoutee | Automatique |
| pr-test-analyzer | pr-review-toolkit | Avant PR | Automatique |
| type-design-analyzer | pr-review-toolkit | Nouveau type cree | Automatique |
| code-simplifier | code-simplifier | Apres code ecrit | Automatique |
| code-simplifier | pr-review-toolkit | Post-implementation | Automatique |

### Agents d'Architecture (impact: 8)

| Agent | Plugin | Auto-trigger | Prompt |
|-------|--------|-------------|--------|
| code-explorer | feature-dev | Analyse codebase profonde | "Explore [module]" |
| code-architect | feature-dev | Design feature | "Designe l'architecture de [X]" |
| agent-creator | plugin-dev | Creer agent | "Cree un agent [nom]" |
| plugin-validator | plugin-dev | Apres modif plugin | Automatique |
| skill-reviewer | plugin-dev | Apres modif skill | Automatique |
| conversation-analyzer | hookify | Analyse conversation | `/hookify` |

### Agents SDK (impact: 5)

| Agent | Plugin | Prompt |
|-------|--------|--------|
| agent-sdk-verifier-py | agent-sdk-dev | "Verifie mon app Agent SDK Python" |
| agent-sdk-verifier-ts | agent-sdk-dev | "Verifie mon app Agent SDK TypeScript" |

### Agents JARVIS (impact: 9)

| Agent | Plugin | Auto-trigger |
|-------|--------|-------------|
| jarvis-devops | jarvis-turbo | Infra changes |
| jarvis-code-reviewer | jarvis-turbo | Post-code |
| jarvis-auto-improver | jarvis-turbo | Post-feature |
| jarvis-auditor | jarvis-turbo | Post-deploy |
| jarvis-gpu-manager | jarvis-turbo | GPU ops |
| jarvis-cluster-health | jarvis-turbo | Health check |
| jarvis-auto-scaler | jarvis-turbo | Load > 80% |
| jarvis-backpressure | jarvis-turbo | Saturation |
| jarvis-browser | jarvis-turbo | Web tasks |
| jarvis-voice-controller | jarvis-turbo | Voice commands |
| jarvis-flow-dispatcher | jarvis-turbo | Task routing |
| jarvis-multi-platform-router | jarvis-turbo | Cross-platform |
| jarvis-quality-gate | jarvis-turbo | Quality check |
| jarvis-task-balancer | jarvis-turbo | Load balancing |

---

## COMMANDS (20) — Slash commands

| Commande | Plugin | Prompt equivalent |
|----------|--------|-------------------|
| `/brainstorm` | superpowers | "Brainstorm sur [sujet]" |
| `/write-plan` | superpowers | "Planifie l'implementation de [X]" |
| `/execute-plan` | superpowers | "Execute le plan" |
| `/feature-dev` | feature-dev | "Developpe la feature [X]" |
| `/commit` | commit-commands | "Commite les changements" |
| `/commit-push-pr` | commit-commands | "Commit, push et cree une PR" |
| `/clean_gone` | commit-commands | "Nettoie les branches supprimees" |
| `/code-review` | code-review | "Review ce code" |
| `/review-pr` | pr-review-toolkit | "Review cette PR en profondeur" |
| `/create-plugin` | plugin-dev | "Cree un nouveau plugin" |
| `/new-sdk-app` | agent-sdk-dev | "Cree une app Agent SDK" |
| `/revise-claude-md` | claude-md-management | "Mets a jour CLAUDE.md" |
| `/hookify` | hookify | "Cree des hooks depuis cette conversation" |
| `/configure` | hookify | "Configure les regles hookify" |
| `/ralph-loop` | ralph-loop | "Lance Ralph Loop" |
| `/cluster-check` | jarvis-turbo | "Health check cluster" |
| `/gpu-status` | jarvis-turbo | "Etat des GPUs" |
| `/diagnostic` | jarvis-turbo | "Diagnostic complet" |
| `/consensus` | jarvis-turbo | "Consensus multi-IA sur [question]" |
| `/browse` | jarvis-turbo | "Navigue vers [url]" |

---

## DOMINO CHAINS (70) — Cascades multi-agents

### Chains CLI nouvelles (5)

| Chain | Steps | Trigger | Impact |
|-------|-------|---------|--------|
| cli-system-health | 6 | cron:boot_check | Health complet via CLIs |
| cli-ai-consensus-dispatch | 5 | user:consensus_request | Consensus pondere M1+OL1+M3 |
| cli-security-hardening | 6 | cron:daily_security | Audit + correction auto |
| cli-freelance-optimizer | 5 | cron:freelance_scan | Scan + proposition + verification |
| cli-gpu-auto-optimize | 4 | gpu:temperature > 75 | Thermal + GPU max reload |

### Chains systeme existantes (65)

Backup, monitoring, trading, content, github, docker, network, GPU, boot, disaster recovery, etc.

---

## CLIs JARVIS (10)

| CLI | Commande | Sous-commandes |
|-----|----------|----------------|
| `jarvis` | Unifie | status, health, gpu, ask, security, clean, load, skills |
| `jai` | Dispatch IA | 23 targets (m1, ol1, claude, gemini, codex, perplexity, chatgpt, aistudio...) |
| `jarvis-security` | Securite | scan, ports, secrets, guard |
| `jarvis-gpu` | GPU | status, load, unload, thermal, vram |
| `jarvis-cluster` | Cluster | health, nodes, route, failover |
| `jarvis-zombie` | Zombies | list, kill, parents |
| `jarvis-monitor` | Monitoring | snapshot, live, services |
| `jarvis-layers` | Boot | check, boot, boot-safe |
| `jarvis-dispatch` | Alias jai | --list |
| `jarvis-boot` | Boot legacy | start, stop |

---

## PONDERATION COMBINAISONS RECOMMANDEES

### Combo S-Tier (impact maximum, usage quotidien)
```
brainstorming → writing-plans → test-driven-development → executing-plans → verification-before-completion → requesting-code-review
```

### Combo Debug (resoudre n'importe quel bug)
```
systematic-debugging → code-explorer → code-reviewer → silent-failure-hunter
```

### Combo Deploy (livrer en production)
```
finishing-a-development-branch → /commit-push-pr → /review-pr → verification-before-completion
```

### Combo JARVIS Ops (maintenance quotidienne)
```
jarvis-layers check → jarvis-zombie kill → jarvis-gpu thermal → jarvis-security scan → jarvis-cluster health
```

### Combo Freelance (trouver et repondre aux missions)
```
codeur-operator → jarvis-ai-dispatch m1 → retrieval-web (Perplexity) → validation-consensus → telegram-ops
```

### Combo Consensus Multi-IA (decision importante)
```
jai m1 "question" + jai ol1 "question" + jai claude "question" → validation-consensus → synthese
```
