# Claude Code — Automatisation

> Agents paralleles, skills, hooks, cron et workflows automatises pour Claude Code.

---

## 1. Agents Paralleles

### Comment lancer 3-5 agents en parallele

Claude Code permet de lancer plusieurs agents qui travaillent en parallele sur des taches differentes. Chaque agent a son propre contexte et ses propres outils.

### Prompt — Lancement multi-agent

```
Lance 3 agents en parallele sur les taches suivantes :

Agent 1 — CODE REVIEW
- Analyse les fichiers modifies dans le dernier commit
- Produis un rapport qualite avec score /10

Agent 2 — TEST COVERAGE
- Lance la suite de tests complete
- Identifie les fichiers avec couverture < 80%
- Propose des tests supplementaires

Agent 3 — SECURITY AUDIT
- Scanne le code pour les vulnerabilites connues
- Verifie les tokens/secrets ne sont pas exposes
- Verifie les permissions des fichiers sensibles

Synthetise les 3 rapports quand tous les agents ont termine.
```

### Ce que ca fait
- 3 taches independantes executees simultanement
- Temps total = temps du plus long agent (au lieu de la somme)
- Chaque agent a son propre context window

### Effet sur le modele
- Le parallelisme n'affecte pas la qualite de chaque agent
- La synthese finale beneficie des 3 perspectives
- Consomme 3x plus de tokens mais 3x plus rapide

### Exemple avance — 5 agents

```
Lance 5 agents en parallele :

1. LINT — Analyse statique du code Python (ruff, mypy)
2. TESTS — Suite de tests complete (pytest -v)
3. PERF — Benchmarks des endpoints critiques
4. DEPS — Verification des dependances (vulnerabilites, mises a jour)
5. DOCS — Verification que la doc est a jour par rapport au code

Format de sortie : tableau recapitulatif avec status par agent.
```

---

## 2. Skills et Slash Commands (44 disponibles)

### Liste complete des skills

#### Cluster et Infrastructure (8)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/cluster-check` | Sante de tous les noeuds IA | Verification quotidienne |
| `/mao-check` | Status MAO (Monitoring, Alerting, Orchestration) | Diagnostic avance |
| `/gpu-status` | Temperatures et utilisation des 6 GPUs | Avant calcul lourd |
| `/thermal` | Protection thermique automatique | Quand GPU > 75C |
| `/heal-cluster` | Reparation automatique des noeuds en panne | Apres un crash |
| `/audit` | Audit systeme complet (CPU, RAM, disk, network) | Hebdomadaire |
| `/model-swap` | Changement de modele a chaud sur un noeud | Optimisation |
| `/deploy` | Deployment automatise (git pull, restart services) | Mise en production |

#### IA et Recherche (6)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/consensus` | Vote multi-modele (3+ IA en parallele) | Decisions critiques |
| `/quick-ask` | Question rapide a un modele specifique | Tests rapides |
| `/web-search` | Recherche web intelligente + digest | Veille techno |
| `/trading-scan` | Scan crypto multi-exchange | Analyse de marche |
| `/trading-feedback` | Retour sur predictions trading | Amelioration continue |
| `/canvas-status` | Status de l'interface Canvas | Monitoring UI |

#### Canvas et UI (3)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/canvas-status` | Status Canvas UI (port 18800) | Verification |
| `/canvas-restart` | Redemarrage Canvas | Apres crash |
| `/canvas-open` | Ouvrir Canvas dans le navigateur | Acces rapide |

#### Code et Dev (10)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/review` | Code review du dernier commit | Avant merge |
| `/test` | Lance les tests | Validation |
| `/test-coverage` | Couverture de tests detaillee | Qualite |
| `/lint` | Analyse statique (ruff + mypy) | Proprete |
| `/refactor` | Refactoring guide | Amelioration |
| `/debug` | Debug systematique | Correction |
| `/generate` | Generation de code structure | Creation |
| `/doc` | Generation de documentation | Documentation |
| `/bench` | Benchmarks de performance | Optimisation |
| `/security` | Audit de securite | Protection |

#### Automation et Ops (8)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/cron-list` | Liste des taches cron actives | Monitoring |
| `/cron-add` | Ajout d'une tache cron | Planification |
| `/backup` | Sauvegarde manuelle | Securite |
| `/restore` | Restauration depuis backup | Recovery |
| `/logs` | Consultation des logs | Diagnostic |
| `/notify` | Envoi notification (Telegram/Discord) | Alertes |
| `/workflow` | Lance un workflow n8n | Automation |
| `/openclaw` | Gestion agents OpenClaw | Orchestration |

#### Session (9)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/status` | Status de la session courante | Information |
| `/save` | Sauvegarde du contexte | Persistance |
| `/load` | Chargement d'un contexte sauvegarde | Reprise |
| `/clear` | Nettoyage du contexte | Reset |
| `/history` | Historique des commandes | Reference |
| `/memory` | Gestion des fichiers memoire | Personnalisation |
| `/config` | Configuration de la session | Parametrage |
| `/help` | Aide contextuelle | Support |
| `/version` | Version de JARVIS et plugins | Information |

---

## 3. Hooks

### Hook 1 : gpu-thermal-guard

```json
{
  "name": "gpu-thermal-guard",
  "trigger": "temperature_threshold",
  "threshold": 75,
  "unit": "celsius",
  "check_interval": 10,
  "actions": [
    {
      "type": "alert",
      "channels": ["telegram", "discord"],
      "message": "GPU temperature > 75C — re-routage en cours"
    },
    {
      "type": "cascade_reroute",
      "strategy": "coldest_node_first",
      "nodes": ["M1", "M2", "M3", "OL1"]
    },
    {
      "type": "model_unload",
      "condition": "temperature > 85",
      "target": "hottest_gpu"
    }
  ]
}
```

#### Ce que ca fait
- Surveille les temperatures GPU toutes les 10 secondes
- A 75C : alerte Telegram/Discord + re-routage vers les noeuds les plus froids
- A 85C : decharge le modele du GPU le plus chaud

#### Effet sur le modele
- Claude est informe automatiquement des problemes thermiques
- Les requetes sont re-routees sans intervention manuelle
- Le modele adapte ses recommandations (evite les calculs lourds si cluster chaud)

### Hook 2 : session-cluster-check

```json
{
  "name": "session-cluster-check",
  "trigger": "session_start",
  "actions": [
    {
      "type": "health_check",
      "targets": ["M1", "M2", "M3", "OL1"],
      "timeout": 5000
    },
    {
      "type": "context_inject",
      "template": "Cluster status: {healthy}/{total} nodes online. Available models: {models}. GPU temps: {temps}."
    },
    {
      "type": "alert_if_degraded",
      "threshold": 0.5,
      "message": "Cluster degrade — {offline} noeuds offline"
    }
  ]
}
```

#### Ce que ca fait
- A chaque debut de session Claude Code, verifie la sante du cluster
- Injecte le status dans le contexte de la session
- Alerte si plus de 50% des noeuds sont offline

#### Effet sur le modele
- Claude sait immediatement quels modeles sont disponibles
- Adapte ses strategies (consensus impossible si < 3 noeuds)
- Peut proposer des actions de reparation si cluster degrade

---

## 4. Cron + n8n + OpenClaw — Couches d'automatisation

### Couche 1 : Cron (taches systeme)

```bash
# Toutes les 5 minutes — Pulse d'autonomie JARVIS
*/5 * * * * /usr/bin/python3 /home/turbo/jarvis-linux/scripts/autonomy_pulse.py --telegram

# Toutes les 10 minutes — Surveillance thermique GPU
*/10 * * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js gpu_thermal_guard.js

# Toutes les 15 minutes — Patrouille sante systeme
*/15 * * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js health_patrol.js

# Toutes les 30 minutes — Snapshot metriques
*/30 * * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js metrics_snapshot.js

# Toutes les heures — Monitoring trading
0 * * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js trading_monitor.js

# Toutes les 2 heures — Watchdog GitHub
0 */2 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js github_watchdog.js

# Toutes les 4 heures — Croissance LinkedIn
0 */4 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js linkedin_growth.js

# Toutes les 6 heures — Digest des logs
0 */6 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js log_digest.js

# 3h du matin — Sauvegarde automatique
0 3 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js backup_auto.js

# 4h du matin — Re-indexation RAG
0 4 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js rag_reindex.js

# 7h du matin — Recherche quotidienne
0 7 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js daily_research.js

# 8h du matin — Briefing quotidien
0 8 * * * /usr/bin/node /home/turbo/jarvis-linux/automation/browser_runner.js daily_briefing.js
```

### Couche 2 : n8n (workflows complexes)

65 workflows couvrant :
- **Monitoring** : Health checks, GPU monitoring, service status
- **Trading** : Scan multi-exchange, alertes prix, backtesting
- **Notifications** : Telegram, Discord, email, push
- **Backups** : Sauvegarde incrementale, rotation, verification
- **CI/CD** : Tests auto, deployment, rollback
- **Recherche** : Veille techno, aggregation RSS, digest
- **GitHub** : PR auto-review, issue triage, release notes

### Couche 3 : OpenClaw (agents autonomes)

```
40 agents statiques + 56 agents dynamiques
11 crons OpenClaw actifs
Gateway port 18789
```

Types d'agents :
- **Moniteurs** : Surveillance continue (sante, performance, securite)
- **Executeurs** : Taches automatisees (backup, cleanup, indexation)
- **Analystes** : Analyse de donnees (trading, logs, metriques)
- **Communicateurs** : Notifications et rapports (Telegram, Discord)

### Comment les 3 couches interagissent

```
CRON (systeme)
  |
  ├── Taches simples executees directement
  |
  └── Declenchent des workflows n8n pour les taches complexes
        |
        ├── n8n orchestre les etapes
        |
        └── Delegue aux agents OpenClaw pour les taches IA
              |
              └── Les agents utilisent le cluster IA (M1/M2/M3/OL1)
```

### Prompt pour configurer l'automatisation

```
Configure une automatisation complete pour [TACHE] avec les 3 couches :

1. CRON : Quelle frequence ? Quel script declencheur ?
2. N8N : Quel workflow ? Quelles etapes ? Quelles conditions ?
3. OPENCLAW : Quel agent ? Quel modele IA ? Quelle strategie ?

Contraintes :
- Pas de notification entre 23h et 7h (sauf CRITICAL)
- GPU temperature < 75C obligatoire pour les taches IA
- Timeout maximum : 5 minutes par etape
- Retry : 3 tentatives avec backoff exponentiel
```

---

## Prerequis

- Claude Code avec plugin jarvis-turbo actif
- Cluster IA operationnel (au moins 2 noeuds)
- n8n en execution sur http://127.0.0.1:5678
- OpenClaw gateway sur port 18789
- Crontab configure (`crontab -e`)
