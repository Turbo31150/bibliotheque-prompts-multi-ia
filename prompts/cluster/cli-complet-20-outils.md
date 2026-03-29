# CLIs JARVIS — 20 Outils Complets

> Horodatage : 2026-03-29T07:10+01:00
> Total : 20 CLIs dans /usr/local/bin/

---

## Index par fonction

| # | CLI | Type | Sous-commandes | Domino lie |
|---|-----|------|----------------|-----------|
| 1 | `jarvis` | Unifie | status, health, gpu, ask, security, clean, load, skills | cli-system-health |
| 2 | `jai` | Dispatch IA | 23 targets (m1, ol1, claude, gemini, codex, perplexity...) | cli-ai-consensus-dispatch |
| 3 | `jarvis-gpu` | GPU | status, load, unload, thermal, vram | cli-gpu-auto-optimize |
| 4 | `jarvis-cluster` | Cluster | health, nodes, route, failover | cluster-node-failover |
| 5 | `jarvis-security` | Securite | scan, ports, secrets, guard | cli-security-hardening |
| 6 | `jarvis-zombie` | Zombie | list, kill, parents | zombie-apocalypse-cleaner |
| 7 | `jarvis-monitor` | Monitor | snapshot, live, services | cli-system-health |
| 8 | `jarvis-layers` | Boot 9L | check, boot, boot-safe | full-boot-sequence |
| 9 | `jarvis-decide` | Decision | predict, simulate, matrix, optimize, visualize | benchmark-self-improve |
| 10 | `jarvis-domino-trigger` | Domino | 15 keywords, dry-run, confirm | Tous les dominos |
| 11 | `jarvis-consensus` | Consensus | M1+OL1+M2 vote pondere (quorum 0.65) | multi-ia-quorum-consensus |
| 12 | `openclaw-master` | Master | status, master, patrol, legion, dispatch, agents, predict | cli-system-health |
| 13 | `openclaw-boot` | Boot OC | boot, register, trigger, status | cli-system-health |
| 14 | `jarvis-dispatch` | Alias | --list | cli-ai-consensus-dispatch |
| 15 | `jarvis-boot` | Boot | start, stop | full-boot-sequence |
| 16 | `jarvis-maintenance.sh` | Cron | weekly cleanup | disk-maintenance-janitor |
| 17 | `jarvis-notify` | Notif | send notification | content-pipeline |
| 18 | `jarvis-repair` | Repair | auto-repair services | service-crash-recovery |
| 19 | `jarvis-search` | Search | search codebase | cognitive-task-indexer |
| 20 | `jarvis-wave` | Wave | launch wave | full-boot-sequence |

---

## Detail par CLI

### 1. jarvis (unifie)
```bash
jarvis status          # Load, RAM, GPU, cluster, services, LM Studio
jarvis health --json   # Health check JSON
jarvis gpu             # GPU detaille
jarvis ask "prompt" -t m1  # Envoyer prompt au cluster
jarvis security        # Audit securite
jarvis clean           # Zombies + reset services
jarvis load [model]    # Charger modele --gpu max
jarvis skills          # Lister 85 Gemini + 14 Claude skills
```

### 2. jai (dispatch IA 23 targets)
```bash
jai m1 "prompt"        # LM Studio GPU local
jai ol1 "prompt"       # Ollama local
jai m2 "prompt"        # M2 remote
jai m3 "prompt"        # M3 remote
jai claude "prompt"    # Claude Code CLI
jai gemini "prompt"    # Gemini CLI
jai codex "prompt"     # Codex CLI
jai perplexity "prompt" # Perplexity Web CDP
jai chatgpt "prompt"   # ChatGPT Web CDP
jai aistudio "prompt"  # AI Studio Web CDP
jai consensus "prompt" # M1+OL1+Claude
jai all-web "prompt"   # Toutes IA web
jai --list             # 23 targets
jai m1 "prompt" --json # Sortie JSON
```

### 10. jarvis-domino-trigger (15 chains)
```bash
jarvis-domino-trigger list              # 15 keywords disponibles
jarvis-domino-trigger heal              # Declenche auto_heal_cluster
jarvis-domino-trigger audit             # Declenche security_audit
jarvis-domino-trigger backup            # Declenche timeshift_snapshot
jarvis-domino-trigger publish --dry-run # Simule linkedin_publish (confirm requis)
jarvis-domino-trigger gpu               # Declenche gpu_auto_optimize
jarvis-domino-trigger debug             # Declenche code_error_debug
jarvis-domino-trigger freelance         # Declenche freelance_pipeline
jarvis-domino-trigger consensus         # Declenche multi_ia_quorum
```

### 11. jarvis-consensus (vote pondere)
```bash
jarvis-consensus "Cette architecture est-elle scalable ?"
# Resultat: M1(1.9) + OL1(1.4) + M2(1.5) = score 0.69 >= 0.65 QUORUM_OK
```

### 12. openclaw-master (agent maitre 805+ agents)
```bash
openclaw-master status     # Dashboard 805+ agents, 10 Legions
openclaw-master master     # 8 cascades detect+fix
openclaw-master patrol     # Boucle continue 30/60s
openclaw-master dispatch "texte"  # Route vers Legion
openclaw-master legion L3  # Details Sentinelles
openclaw-master agents     # 38 agents SQL
openclaw-master predict    # Decision Engine
```

---

## Combinaisons recommandees

### Boot complet session
```bash
openclaw-master boot && jarvis-domino-trigger boot --dry-run
```

### Diagnostic + repair
```bash
jarvis status && jarvis-security scan && jarvis-zombie kill && openclaw-master master
```

### Consensus pour decision importante
```bash
jarvis-consensus "Faut-il monter le tarif a 150 euros/h ?"
```

### Dispatch multi-IA + verification
```bash
jai m1 "Genere un post LinkedIn" && jai perplexity "Verifie ce post"
```

### Monitoring continu
```bash
openclaw-master patrol  # Boucle 60s avec auto-repair
```

---

[HORODATAGE] 2026-03-29T07:10:00+01:00
[TOTAL] 20 CLIs, 15 domino triggers, 23 dispatch targets
[STATUT] PRODUCTION ACTIVE
