# Gemini CLI — Skills Pack

> 12 skills natifs Gemini + 23 skills routes depuis le router multi-IA. Derniere mise a jour : 2026-03-28.

---

## Skills natifs Gemini CLI (12)

Ces skills sont declares dans `~/.claude/skills/` et executes nativement par Gemini CLI.

| # | Skill | Description | Auto-trigger |
|---|-------|-------------|--------------|
| 1 | `autotest-analysis` | Analyse des resultats de tests automatises et generation de rapports | Sur echec test CI |
| 2 | `browser-workflow` | Workflows navigateur complexes (multi-etapes, formulaires, scraping) | Sur tache web multi-pages |
| 3 | `cluster-management` | Gestion du cluster JARVIS (M1/OL1/M2/M3, poids, health) | Sur changement etat noeud |
| 4 | `continuous-improvement` | Boucle d'amelioration continue (benchmark → analyse → patch → re-test) | Toutes les 6 heures |
| 5 | `demarrage` | Sequence de demarrage des services Gemini et modules associes | Au boot systeme |
| 6 | `failover-recovery` | Basculement automatique sur noeud de secours en cas de panne | Sur noeud principal down |
| 7 | `mao-workflow` | Workflow MAO (Mise A jour Orchestree) — deploiement coordonne | Sur nouvelle version prete |
| 8 | `performance-tuning` | Optimisation des performances (latence, throughput, memoire) | Sur degradation detectee |
| 9 | `security-audit` | Audit securite complet (ports, services, permissions, CVE) | Hebdomadaire |
| 10 | `smart-routing` | Routage intelligent des requetes entre modeles LLM | Sur requete entrante |
| 11 | `trading-pipeline` | Pipeline de trading automatise (signaux, execution, monitoring) | Sur signal marche |
| 12 | `weighted-orchestration` | Orchestration ponderee des taches selon capacite noeuds | Sur queue > 10 taches |

---

## Skills routes depuis GEMINI_SKILLS (23)

Ces skills sont declares dans `core/domino/router.py` sous `GEMINI_SKILLS` et routes vers Gemini CLI par le moteur domino.

| # | Skill | Description | Source routage |
|---|-------|-------------|---------------|
| 1 | `jarvis-orchestrator` | Orchestration principale — coordination multi-IA | Claude → Gemini |
| 2 | `browseros-operator` | Pilotage BrowserOS depuis Gemini | Claude → Gemini |
| 3 | `retrieval-web` | Recherche web via Perplexity/Comet MCP | Claude → Gemini |
| 4 | `validation-consensus` | Consensus multi-noeud (quorum >= 0.65) | Claude → Gemini |
| 5 | `production-monitor` | Monitoring services production en temps reel | Claude → Gemini |
| 6 | `sql-memory-reader` | Lecture memoire SQL (73 bases consolidees) | Claude → Gemini |
| 7 | `file-log-reader` | Lecture intelligente de logs (pattern matching) | Claude → Gemini |
| 8 | `github-reader` | Lecture repos GitHub (issues, PRs, code) | Claude → Gemini |
| 9 | `linkedin-operator` | Publication LinkedIn automatisee (CDP + xdotool) | Claude → Gemini |
| 10 | `codeur-operator` | Agent codeur — ecriture et refactoring | Claude → Gemini |
| 11 | `telegram-ops` | Operations Telegram (messages, alertes, monitoring) | Claude → Gemini |
| 12 | `voice-first-operator` | Interface vocale prioritaire (Piper TTS + Whisper STT) | Claude → Gemini |
| 13 | `prompt-alimentation` | Alimentation prompts depuis base de connaissances | Claude → Gemini |
| 14 | `codex-cli-builder` | Construction commandes Codex CLI | Claude → Gemini |
| 15 | `openclaw-router` | Routeur OpenClaw Gateway (ws://127.0.0.1:18789) | Claude → Gemini |
| 16 | `task-queue-planner` | Planification taches dans la queue Redis | Claude → Gemini |
| 17 | `production-improver` | Amelioration continue performances production | Claude → Gemini |
| 18 | `browser-session-curator` | Gestion sessions navigateur (onglets, cookies, historique) | Claude → Gemini |
| 19 | `jarvis-flow-controller` | Controleur de flux systeme JARVIS | Claude → Gemini |
| 20 | `boot-sequencer` | Sequence de boot complete | Claude → Gemini |
| 21 | `auto-debug` | Debug automatique depuis logs et stack traces | Claude → Gemini |
| 22 | `auto-learn` | Apprentissage continu depuis incidents et benchmarks | Claude → Gemini |
| 23 | `project-architect` | Architecture projet (patterns, structure, dependances) | Claude → Gemini |

---

## Carte Auto-triggers

| Situation detectee | Skill declenche | Trigger |
|-------------------|-----------------|---------|
| Boot systeme | `demarrage` | systemd timer `jarvis-boot.timer` |
| Noeud cluster down | `failover-recovery` | Heartbeat manquant > 30s |
| Noeud cluster revenu | `cluster-management` | Heartbeat restaure |
| Echec test CI | `autotest-analysis` | Exit code != 0 dans pipeline |
| Degradation perf | `performance-tuning` | Latence > 2x baseline |
| Queue > 10 taches | `weighted-orchestration` | Redis LLEN > 10 |
| Signal marche recu | `trading-pipeline` | Webhook CCXT |
| Nouvelle version prete | `mao-workflow` | Tag git v*.*.* |
| Audit hebdomadaire | `security-audit` | Cron dimanche 03:00 |
| Amelioration planifiee | `continuous-improvement` | Timer toutes les 6h |
| Tache web multi-pages | `browser-workflow` | Requete avec URLs multiples |
| Requete routage | `smart-routing` | Chaque requete LLM entrante |
| Erreur dans logs | `auto-debug` | Pattern ERROR/CRITICAL dans journalctl |
| Post-incident | `auto-learn` | Apres resolution incident |
| Requete GitHub | `github-reader` | Reference a un repo/issue/PR |
| Publication contenu | `linkedin-operator` | Contenu valide en queue |
| Requete web | `retrieval-web` | Question necessitant donnees web |
| Tache critique | `validation-consensus` | Complexite == "critical" |
| Monitoring continu | `production-monitor` | Timer toutes les 2 min |
| Benchmark en baisse | `production-improver` | Score < 90% du precedent |

---

## Execution Gemini CLI

```bash
# Execution directe avec prompt
gemini -p "Analyse les logs de crash dans /var/log/syslog" --yolo

# Execution via le router domino
python -m core.domino.engine --chain full-boot-sequence

# Execution skill specifique
gemini -p "Execute le skill cluster-management: health check tous les noeuds"
```

### Flags utiles

| Flag | Effet |
|------|-------|
| `--yolo` | Mode non-interactif (pas de confirmation) |
| `-p "..."` | Prompt inline |
| `--sandbox` | Execution isolee |

---

## Chemins cles

```
~/.claude/skills/autotest-analysis/       # Skill autotest
~/.claude/skills/cluster-management/       # Gestion cluster
~/.claude/skills/continuous-improvement/   # Amelioration continue
~/.claude/skills/failover-recovery/        # Failover
~/.claude/skills/performance-tuning/       # Perf tuning
~/.claude/skills/security-audit/           # Audit securite
~/.claude/skills/smart-routing/            # Routage intelligent
~/.claude/skills/trading-pipeline/         # Trading
~/.claude/skills/weighted-orchestration/   # Orchestration ponderee
~/Workspaces/jarvis-linux/core/domino/router.py  # Router multi-IA (GEMINI_SKILLS)
```
