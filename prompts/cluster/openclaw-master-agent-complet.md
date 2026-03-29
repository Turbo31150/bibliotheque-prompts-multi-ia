# OpenClaw Master Agent — Reference Complete

> 805+ agents | 10 Legions | 8 cascades auto-repair | Dispatch vectoriel
> CLI : `openclaw-master` | Fichier : `scripts/openclaw-master.py`
> Horodatage creation : 2026-03-29 05:00 UTC+1

---

## 1. COMMANDES MASTER

| Commande | Action | Domino associe | Horodatage trigger |
|----------|--------|---------------|-------------------|
| `openclaw-master status` | Dashboard 805+ agents, 6 noeuds, 10 legions | cli-system-health (step 1) | Boot + chaque 5min |
| `openclaw-master master` | 8 cascades detect+fix automatiques | cli-system-health (full) | Boot + chaque 60s patrol |
| `openclaw-master patrol` | Boucle continue 30/60s | cli-system-health (loop) | Daemon permanent |
| `openclaw-master dispatch "texte"` | Route vers Legion optimale par vecteur | cli-ai-consensus-dispatch | Sur chaque requete |
| `openclaw-master legion L3` | Details Legion Sentinelles | Aucun | Manuel |
| `openclaw-master agents` | Liste 38 agents SQL avec status | Aucun | Diagnostic |
| `openclaw-master predict` | Decision Engine vectoriel | Aucun | Avant action complexe |

---

## 2. LES 10 LEGIONS — Detail professionnel

### L1 ARCHITECTES (60 agents) — Design et Mutation

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.95, 0.90, 0.80, 0.70, 0.90, 0.60, 0.95] |
| **Skills** | sequential-thinking, writing-plans, project-architect |
| **Agents SQL** | architect-guardian, task-decomposer-prime, feature-dev:code-architect |
| **Trigger regex** | `design\|architecture\|plan\|mutation\|refactor` |
| **Domino chain** | legion-architectes-design (4 steps) |
| **Combinaison action** | Sequential Thinking → Writing Plans → Validation Consensus → Project Architect |
| **Quand declencher** | Nouvelle feature, refactoring majeur, changement d'architecture |
| **Score pondere** | utilite=0.95 × impact=0.90 × synergie=0.95 = **0.812** |

### L2 FORGEURS (60 agents) — Implementation et Code

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.90, 0.95, 0.75, 0.65, 0.85, 0.80, 0.90] |
| **Skills** | tdd, code-review, executing-plans |
| **Agents SQL** | feature-dev:code-reviewer, jarvis-code-reviewer, jarvis-auto-improver |
| **Trigger regex** | `code\|implement\|feature\|tdd\|test\|commit\|pr` |
| **Domino chain** | legion-forgeurs-implement (4 steps) |
| **Combinaison action** | Brainstorming → TDD → Code Review → GitHub Push |
| **Quand declencher** | Implementation feature, bug fix, PR creation |
| **Score pondere** | utilite=0.90 × impact=0.95 × synergie=0.90 = **0.769** |

### L3 SENTINELLES (60 agents) — Protection et Securite

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.85, 0.95, 0.90, 0.85, 0.95, 0.70, 0.80] |
| **Skills** | security-audit, jarvis-security-audit, zombie-cleanup |
| **Agents SQL** | security-reviewer, system-crash-guardian, jarvis-security-audit |
| **Trigger regex** | `securite\|security\|audit\|crash\|zombie\|port\|firewall` |
| **Domino chain** | legion-sentinelles-protect (4 steps) + cli-security-hardening (6 steps) |
| **Combinaison action** | Security Scan → Zombie Kill → Service Repair → Telegram Alert |
| **Quand declencher** | Incident securite, crash service, zombies > 10, port expose |
| **Score pondere** | utilite=0.85 × impact=0.95 × synergie=0.80 = **0.646** |

### L4 ANALYSTES (60 agents) — Recherche et Consensus

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.90, 0.85, 0.70, 0.50, 0.85, 0.60, 0.95] |
| **Skills** | validation-consensus, deep-research, ai-consensus |
| **Agents SQL** | pr-review-toolkit:pr-test-analyzer, pr-review-toolkit:comment-analyzer |
| **Trigger regex** | `analyse\|recherche\|consensus\|verifie\|compare\|valide` |
| **Domino chain** | cli-ai-consensus-dispatch (5 steps) |
| **Combinaison action** | M1 Query → OL1 Query → M3 Query → Consensus Pondere → SQL Store |
| **Quand declencher** | Decision importante, verification contenu, due diligence |
| **Score pondere** | utilite=0.90 × impact=0.85 × synergie=0.95 = **0.727** |

### L5 AUTOMATES (60 agents) — Workflows et Pipelines

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.85, 0.80, 0.80, 0.90, 0.80, 0.90, 0.85] |
| **Skills** | pipeline-builder, domino-engine, browseros-operator |
| **Agents SQL** | jarvis-flow-dispatcher, jarvis-browser, incident-responder |
| **Trigger regex** | `domino\|pipeline\|workflow\|automate\|n8n\|browseros` |
| **Domino chain** | cli-freelance-optimizer (5 steps) |
| **Combinaison action** | Domino Engine → n8n Workflow → BrowserOS Action → Verification |
| **Quand declencher** | Automatisation repetitive, pipeline web, orchestration multi-etapes |
| **Score pondere** | utilite=0.85 × impact=0.80 × synergie=0.85 = **0.578** |

### L6 TRADERS (60 agents) — Finance et Freelance

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.75, 0.85, 0.65, 0.80, 0.70, 0.50, 0.70] |
| **Skills** | trading-pipeline, codeur-operator, offres-v2 |
| **Agents SQL** | jarvis-multi-platform-router |
| **Trigger regex** | `trading\|trade\|crypto\|mexc\|signal\|marche\|freelance\|codeur` |
| **Domino chain** | freelance-pipeline + cli-freelance-optimizer |
| **Combinaison action** | Codeur Scan → M1 Proposal → Perplexity Verify → Consensus → Telegram |
| **Quand declencher** | Scan marche, proposition client, trading signal |
| **Score pondere** | utilite=0.75 × impact=0.85 × synergie=0.70 = **0.446** |

### L7 COMMUNICATEURS (60 agents) — Diffusion et Alertes

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.70, 0.75, 0.75, 0.60, 0.75, 0.40, 0.65] |
| **Skills** | telegram-ops, linkedin-operator, voice-first-operator |
| **Agents SQL** | jarvis-voice-controller |
| **Trigger regex** | `telegram\|linkedin\|post\|message\|vocal\|voix\|alerte` |
| **Domino chain** | content-pipeline |
| **Combinaison action** | Content Generate → IA Web Verify → LinkedIn Publish → Telegram Digest |
| **Quand declencher** | Publication contenu, alerte systeme, commande vocale |
| **Score pondere** | utilite=0.70 × impact=0.75 × synergie=0.65 = **0.341** |

### L8 OPTIMISEURS (60 agents) — Performance et GPU

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.90, 0.85, 0.85, 0.95, 0.90, 0.80, 0.85] |
| **Skills** | gpu-manager, cluster-management, smart-routing |
| **Agents SQL** | jarvis-gpu-manager, jarvis-auto-scaler, jarvis-cluster-health, jarvis-task-balancer |
| **Trigger regex** | `gpu\|vram\|thermal\|load\|optimize\|scale\|cluster\|performance` |
| **Domino chain** | cli-gpu-auto-optimize (4 steps) |
| **Combinaison action** | GPU Status → Thermal Check → Model Reload --gpu max → Cluster Rebalance |
| **Quand declencher** | GPU > 78C, CPU LM Studio > 40%, load > 25, VRAM pleine |
| **Score pondere** | utilite=0.90 × impact=0.85 × synergie=0.85 = **0.650** |

### L9 ERUDITS (60 agents) — Savoir et Memoire

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.80, 0.70, 0.85, 0.70, 0.85, 0.50, 0.80] |
| **Skills** | prompt-alimentation, sql-memory-reader, auto-learn |
| **Agents SQL** | pr-review-toolkit:type-design-analyzer, domino-optimizer |
| **Trigger regex** | `prompt\|memoire\|sql\|base\|connaissance\|docs\|apprend` |
| **Domino chain** | benchmark-self-improve |
| **Combinaison action** | SQL Read → Knowledge Extract → Prompt Generate → Auto Learn |
| **Quand declencher** | Recherche en base, generation prompts, apprentissage feedback |
| **Score pondere** | utilite=0.80 × impact=0.70 × synergie=0.80 = **0.448** |

### L10 DEBUGGERS (60 agents) — Root Cause et Fix

| Composant | Detail |
|-----------|--------|
| **Vecteur** | [0.90, 0.90, 0.80, 0.75, 0.90, 0.70, 0.85] |
| **Skills** | systematic-debugging, file-log-reader, service-auto-repair |
| **Agents SQL** | system-health-monitor, code-simplifier:code-simplifier, pr-review-toolkit:silent-failure-hunter |
| **Trigger regex** | `debug\|erreur\|bug\|log\|fix\|crash\|repair\|heal` |
| **Domino chain** | legion-debuggers-rootcause (4 steps) + code-error-debug |
| **Combinaison action** | Reproduce Bug → Analyze Logs → Auto Fix → Verify Fix |
| **Quand declencher** | Erreur, bug, crash, log suspect, service failed |
| **Score pondere** | utilite=0.90 × impact=0.90 × synergie=0.85 = **0.689** |

---

## 3. CASCADES AUTO-REPAIR (8 regles)

| # | Nom | Legion | Detection | Seuil | Fix automatique | Domino |
|---|-----|--------|-----------|-------|----------------|--------|
| 1 | Zombie Guard | L3 Sentinelles | `ps -eo stat` | > 8 zombies | `jarvis-zombie kill` | cli-system-health step 2 |
| 2 | GPU Thermal | L8 Optimiseurs | `nvidia-smi temp` | > 78C | `jarvis-gpu thermal` | cli-gpu-auto-optimize step 1 |
| 3 | LM Studio CPU | L8 Optimiseurs | `ps aux` | CPU > 40% | `lms unload --all` | cli-gpu-auto-optimize step 2 |
| 4 | Failed Services | L10 Debuggers | `systemctl --failed` | > 2 failed | `reset-failed` | cli-system-health step 5 |
| 5 | Load Average | L8 Optimiseurs | `/proc/loadavg` | > 25 | `jarvis clean` | cli-system-health step 1 |
| 6 | RAM Pressure | L8 Optimiseurs | `/proc/meminfo` | < 4GB free | `jarvis clean` | cli-system-health step 1 |
| 7 | Cluster Down | L5 Automates | `curl M1` | M1 offline | `lms server start` | cluster-node-failover |
| 8 | Domino Leak | L3 Sentinelles | `pgrep gemini` | > 5 processes | `pkill gemini JARVIS` | cli-security-hardening |

---

## 4. MATRICE DISPATCH — Routing par mots-cles

| Mots-cles utilisateur | Legion | Score vectoriel | Agents dispatches |
|-----------------------|--------|----------------|-------------------|
| debug, erreur, bug, crash, fix | **L10 Debuggers** | 0.689 | system-health-monitor, silent-failure-hunter |
| gpu, vram, thermal, scale, load | **L8 Optimiseurs** | 0.650 | jarvis-gpu-manager, jarvis-auto-scaler |
| securite, audit, zombie, port | **L3 Sentinelles** | 0.646 | security-reviewer, system-crash-guardian |
| architecture, plan, refactor | **L1 Architectes** | 0.812 | architect-guardian, task-decomposer-prime |
| code, implement, tdd, commit | **L2 Forgeurs** | 0.769 | feature-dev:code-reviewer, jarvis-code-reviewer |
| analyse, consensus, verifie | **L4 Analystes** | 0.727 | pr-test-analyzer, comment-analyzer |
| domino, pipeline, n8n, workflow | **L5 Automates** | 0.578 | jarvis-flow-dispatcher, jarvis-browser |
| trading, codeur, freelance | **L6 Traders** | 0.446 | jarvis-multi-platform-router |
| telegram, linkedin, vocal | **L7 Communicateurs** | 0.341 | jarvis-voice-controller |
| prompt, sql, memoire, docs | **L9 Erudits** | 0.448 | type-design-analyzer, domino-optimizer |

---

## 5. CHAINES DOMINO PAR LEGION

### L1 — legion-architectes-design.yaml
```
Step 1: sequential-thinking → Decomposer la tache
Step 2: writing-plans → Ecrire le plan
Step 3: validation-consensus → Valider par consensus M1+OL1
Step 4: project-architect → Definir l'architecture
```

### L2 — legion-forgeurs-implement.yaml
```
Step 1: brainstorming → Explorer les approches
Step 2: tdd → Ecrire les tests d'abord
Step 3: code-review → Review automatique
Step 4: github-reader → Commit et push
```

### L3 — legion-sentinelles-protect.yaml + cli-security-hardening.yaml
```
Step 1: jarvis-security-audit → Scan complet 6 points
Step 2: jarvis-zombie-cleaner → Kill zombies
Step 3: service-auto-repair → Reparer services failed
Step 4: security ports → Audit ports exposes
Step 5: gpu thermal → Verifier temperatures
Step 6: telegram-ops → Alerter Turbo
```

### L8 — cli-gpu-auto-optimize.yaml
```
Step 1: jarvis-gpu status → Identifier GPUs chauds + workers CPU
Step 2: lms unload+reload → Forcer --gpu max
Step 3: jarvis-monitor snapshot → Verifier load < 10
Step 4: jarvis-cluster route → Distribuer vers M3/OL1 si sature
```

### L10 — legion-debuggers-rootcause.yaml
```
Step 1: systematic-debugging → Reproduire le bug
Step 2: file-log-reader → Analyser les logs
Step 3: auto-debug → Fix iteratif
Step 4: verification → Verifier le fix
```

---

## 6. METRIQUES DE VALIDATION

> Si utilise massivement = calculs et logique etaient bons.

### Indicateurs de succes
| Metrique | Seuil bon | Seuil excellent |
|----------|----------|----------------|
| Cascades/jour declenchees | > 10 | > 50 |
| Issues auto-reparees | > 80% | > 95% |
| Dispatch correct (legion match) | > 70% | > 90% |
| Temps moyen cascade | < 30s | < 10s |
| Load moyen post-master | < 5 | < 2 |
| GPU temp max | < 75C | < 60C |
| Zombies residuels | < 5 | 0 |

### Formule de score global
```
Score_Master = (cascades_fixed / cascades_detected) × 0.4
             + (dispatch_correct / dispatch_total) × 0.3
             + (1 - load_avg/30) × 0.15
             + (1 - gpu_max_temp/85) × 0.15

Interpretation:
  > 0.85 = EXCELLENT — logique validee, usage massif justifie
  > 0.65 = BON — ajustements mineurs
  < 0.65 = A REVOIR — recalibrer les seuils
```

---

## 7. HORODATAGE DECLENCHEMENT

| Quand | Quoi | Domino | Frequence |
|-------|------|--------|-----------|
| Boot systeme | `openclaw-master boot` | cli-system-health | 1x au demarrage |
| Chaque 60s | `openclaw-master patrol` | cli-system-health (loop) | Continu |
| Chaque 5min | Zombie + GPU check | cli-gpu-auto-optimize | Planifie |
| Chaque 15min | Task queue refresh | cli-ai-consensus-dispatch | Planifie |
| Chaque 30min | GitHub + browser session | github-automation | Planifie |
| Chaque 60min | Prompt feed + improver | benchmark-self-improve | Planifie |
| Chaque 2h | LinkedIn engagement | content-pipeline | Business hours |
| Chaque 6h | Codeur scan | cli-freelance-optimizer | Business hours |
| Sur incident | Master cascade 8 regles | Toutes les chains | Reactif |
| Sur requete | Dispatch vectoriel → Legion | Chain de la legion | Reactif |

---

## TOTAUX

```
Master Agent CLI:     7 commandes
Legions:              10 (600 agents)
Cascades auto:        8 regles
Domino chains liees:  12
Agents SQL:           38
Skills Gemini:        85
Skills OpenClaw:      11 (46 commands)
Domino chains total:  71
Score vectoriel dims: 7
Trigger regex:        10 patterns
Metriques:            7 indicateurs
```

[HORODATAGE] 2026-03-29T05:00:00+01:00
[STATUT] PRODUCTION ACTIVE
[VALIDATION] Si usage massif → logique confirmee
