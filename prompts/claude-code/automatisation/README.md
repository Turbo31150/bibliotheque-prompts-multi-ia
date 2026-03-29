# Claude Code — Automatisation

## Description
Prompts pour l'automatisation avec Claude Code : agents paralleles (lancer 3-5 en simultane), 44 skills/slash commands disponibles, hooks reactifs, taches cron, integration n8n et OpenClaw.

## Configuration requise
- Claude Code avec plugin `jarvis-turbo` actif
- Cluster IA operationnel (minimum 2 noeuds sur 4)
- n8n en execution sur http://127.0.0.1:5678
- OpenClaw gateway sur port 18789
- Crontab configure (`crontab -e`)

---

## Prompts par type de tache

### Creation — Lancement multi-agent (3 agents)

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

**Resultat attendu** : 3 rapports independants + synthese. Temps = temps du plus long agent.

---

### Creation — Lancement multi-agent (5 agents)

```
Lance 5 agents en parallele :

1. LINT — Analyse statique du code Python (ruff, mypy)
2. TESTS — Suite de tests complete (pytest -v)
3. PERF — Benchmarks des endpoints critiques
4. DEPS — Verification des dependances (vulnerabilites, mises a jour)
5. DOCS — Verification que la doc est a jour par rapport au code

Format de sortie : tableau recapitulatif avec status par agent.
```

**Resultat attendu** :

| Agent | Status | Duree | Issues |
|-------|--------|-------|--------|
| LINT | OK/FAIL | Xs | N issues |
| TESTS | OK/FAIL | Xs | N fails |
| PERF | OK/FAIL | Xs | N regressions |
| DEPS | OK/FAIL | Xs | N vulns |
| DOCS | OK/FAIL | Xs | N outdated |

---

### Creation — Automatisation 3 couches (Cron + n8n + OpenClaw)

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

### Amelioration / Refactoring — Optimiser un workflow existant

```
Optimise le workflow d'automatisation pour [TACHE].

1. Analyse le workflow actuel :
   - Quelles etapes sont sequentielles mais pourraient etre paralleles ?
   - Quelles etapes sont redondantes ?
   - Ou sont les goulots d'etranglement ?

2. Propose des optimisations :
   - Parallelisation des etapes independantes
   - Mise en cache des resultats intermediaires
   - Reduction des appels reseau inutiles
   - Ajout de conditions de sortie rapide (early exit)

3. Mesure avant/apres :
   - Temps total d'execution
   - Consommation de tokens
   - Fiabilite (taux de succes)
```

---

### Debug — Workflow en echec

```
Un workflow automatise ne fonctionne plus.

Nom du workflow : [NOM]
Derniere execution reussie : [DATE]
Erreur : [DESCRIPTION/LOGS]

Verifie dans l'ordre :
1. Le declencheur cron fonctionne ? (crontab -l)
2. Le script existe et est executable ? (ls -la, chmod)
3. Les dependances sont disponibles ? (services, APIs, cluster)
4. Les permissions sont correctes ? (user, group, fichiers)
5. Le workflow n8n est actif ? (curl 127.0.0.1:5678/api/v1/workflows)
6. L'agent OpenClaw est demarre ? (curl 127.0.0.1:18789/health)

Corrige le probleme et relance le workflow.
```

---

### Documentation — Inventaire des automatisations

```
Genere un inventaire complet de toutes les automatisations actives :

1. Crons systeme (crontab -l) :
   - Frequence, script, description, dernier run

2. Workflows n8n :
   - Nom, declencheur, etapes, status

3. Agents OpenClaw :
   - Nom, type (moniteur/executeur/analyste/communicateur), status

4. Hooks Claude Code :
   - Nom, declencheur, actions

Format : tableau par couche avec status actuel.
```

---

## Skills et Slash Commands (44 disponibles)

### Cluster et Infrastructure (8)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/cluster-check` | Sante de tous les noeuds IA | Verification quotidienne |
| `/mao-check` | Status MAO (Monitoring, Alerting, Orchestration) | Diagnostic avance |
| `/gpu-status` | Temperatures et utilisation des 6 GPUs | Avant calcul lourd |
| `/thermal` | Protection thermique automatique | Quand GPU > 75C |
| `/heal-cluster` | Reparation automatique des noeuds en panne | Apres un crash |
| `/audit` | Audit systeme complet (CPU, RAM, disk, network) | Hebdomadaire |
| `/model-swap` | Changement de modele a chaud | Optimisation |
| `/deploy` | Deployment automatise (git pull, restart) | Mise en production |

### IA et Recherche (6)

| Commande | Description | Usage |
|----------|-------------|-------|
| `/consensus` | Vote multi-modele (3+ IA paralleles) | Decisions critiques |
| `/quick-ask` | Question rapide a un modele specifique | Tests rapides |
| `/web-search` | Recherche web intelligente + digest | Veille techno |
| `/trading-scan` | Scan crypto multi-exchange | Analyse de marche |
| `/trading-feedback` | Retour sur predictions trading | Amelioration continue |
| `/canvas-status` | Status de l'interface Canvas | Monitoring UI |

### Code et Dev (10)

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

### Automation et Ops (8)

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

### Session (9) + Canvas (3)

| Commande | Description |
|----------|-------------|
| `/status`, `/save`, `/load`, `/clear` | Gestion de session |
| `/history`, `/memory`, `/config` | Configuration |
| `/help`, `/version` | Information |
| `/canvas-status`, `/canvas-restart`, `/canvas-open` | Interface Canvas |

---

## Hooks

### Hook 1 : gpu-thermal-guard
- **Declencheur** : Temperature GPU > 75C (check toutes les 10s)
- **Actions** : Alerte Telegram/Discord → re-routage vers noeuds froids → decharge modele si > 85C

### Hook 2 : session-cluster-check
- **Declencheur** : Debut de session Claude Code
- **Actions** : Health check cluster → injection status dans le contexte → alerte si > 50% noeuds offline

---

## Crons actifs (12)

```bash
*/5 * * * *   autonomy_pulse.py --telegram        # Pulse autonomie JARVIS
*/10 * * * *  gpu_thermal_guard.js                 # Surveillance thermique
*/15 * * * *  health_patrol.js                     # Patrouille sante
*/30 * * * *  metrics_snapshot.js                  # Snapshot metriques
0 * * * *     trading_monitor.js                   # Monitoring trading
0 */2 * * *   github_watchdog.js                   # Watchdog GitHub
0 */4 * * *   linkedin_growth.js                   # Croissance LinkedIn
0 */6 * * *   log_digest.js                        # Digest logs
0 3 * * *     backup_auto.js                       # Backup 3h du matin
0 4 * * *     rag_reindex.js                       # Re-indexation RAG
0 7 * * *     daily_research.js                    # Recherche quotidienne
0 8 * * *     daily_briefing.js                    # Briefing quotidien
```

---

## Exemples concrets

### Exemple 1 : Pipeline CI complet en 5 agents
```bash
claude "Lance 5 agents paralleles : lint, tests, perf, deps, docs. Synthese en tableau."
```
**Resultat attendu** : Tableau avec 5 lignes, status OK/FAIL, duree, nombre d'issues par agent.

### Exemple 2 : Ajout d'un cron de monitoring
```bash
claude "/cron-add '*/10 * * * * /usr/bin/python3 /home/turbo/jarvis-linux/scripts/disk_check.py'"
```
**Resultat attendu** : Cron ajoute, verification `crontab -l`, premier run de test.

---

## Effet sur le modele
- Le parallelisme multi-agent divise le temps par N sans affecter la qualite
- Les 44 skills pre-configurees evitent de re-decrire les taches courantes
- Les hooks automatiques injectent du contexte sans action manuelle
- Les 3 couches (cron/n8n/OpenClaw) couvrent tous les niveaux de complexite
- Consomme N fois plus de tokens en parallele mais N fois plus rapide
