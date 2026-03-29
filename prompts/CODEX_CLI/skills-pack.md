# Codex CLI Skills Pack — Integration JARVIS

> Derniere mise a jour : 2026-03-28
> Role : moteur d'execution shell, scripts JARVIS, mode YOLO

---

## Skills Shell-executables

| # | Skill | Commande | Declencheur |
|---|-------|----------|-------------|
| 1 | `flow-check` | `bash ~/Workspaces/jarvis-linux/scripts/jarvis-flow-check.sh` | Timer 5 min, verification flux complet (CPU, RAM, GPU, services, Redis, LM Studio) |
| 2 | `boot-sequencer` | `bash ~/Workspaces/jarvis-linux/scripts/jarvis-boot-sequencer.sh` | Au demarrage systeme, boot ordonne de tous les services (8 vagues) |
| 3 | `crash-guardian` | `bash ~/Workspaces/jarvis-linux/core/scripts/devops/jarvis-crash-guardian.sh` | Sur crash detecte, detection et reparation des crashs critiques |
| 4 | `benchmark-triggers` | `bash ~/Workspaces/jarvis-linux/scripts/jarvis-benchmark-triggers.sh` | Post-deploiement ou cron 3h, collecte et comparaison benchmarks |
| 5 | `rescue-switcher` | `bash ~/Workspaces/jarvis-linux/scripts/jarvis-rescue-switcher.sh` | Sur instabilite critique, bascule mode rescue |

---

## Flags Codex CLI

| Flag | Effet | Exemple |
|------|-------|---------|
| `--yolo` | Execute tout sans confirmation, aucune limite | `codex --yolo "repare le service redis"` |
| `--auto-approve` | Approuve automatiquement les actions proposees | `codex --auto-approve "deploie la nouvelle version"` |
| `--full-auto` | Combine yolo + auto-approve (mode par defaut JARVIS) | `codex --full-auto "boot sequence complète"` |
| `--model` | Choix du modele (defaut: o4-mini) | `codex --model o3 "analyse ce crash"` |
| `--quiet` | Sortie minimale, pas de decorations | `codex --quiet "status jarvis"` |

Le mode `--yolo` est le mode par defaut dans JARVIS pour Codex CLI.

---

## 5 Prompts de Taches

Extrait de `CODEX_CLI/task-prompts.md` :

### 1. Generation de script infra
Creer des scripts shell ou infra-as-code. Script complet, commente, avec dry-run.

### 2. Debug cible
Erreur de production ou de dev a diagnostiquer. Resume, investigation, patch minimal.

### 3. Mise en route Jarvis
Deployer Jarvis comme service Linux via Codex. systemd, setup, health-check, rollback.

### 4. Creation de code
Generer du code nouveau pour une tache specifique. Code complet, style du projet, exemple d'usage.

### 5. Ancrage indestructible Jarvis
Assurer que les services Jarvis ne tombent jamais. Auto-heal GPU, emergency reset, VRAM load balancing.

> Voir `CODEX_CLI/task-prompts.md` pour les prompts complets.

---

## Pattern Ancrage Indestructible

Le pattern "JARVIS-CORE-ANCHOR" est le coeur de la resilience :

```
1. Surveillance active GPUs (nvidia-smi polling 30s)
2. Auto-heal : GPU down → reset driver + restart service associe
3. VRAM load balancing : repartir les modeles sur GPUs disponibles
4. Emergency reset : si 3+ GPUs down → purge VRAM, restart complet stack
5. Alertes : log journald + TTS notification + webhook optionnel
```

**Contraintes :**
- Ne jamais tuer un job en cours sans save d'etat
- Services proteges : jarvis-master, jarvis-openclaw, jarvis-whisper, jarvis-voice
- GPUs : RTX 2060 12GB, 3x GTX 1660S 6GB, RTX 3080 10GB
- Maximum 3 retries avant escalade humaine

---

## Scripts Disponibles

### Orchestration et Boot

| Script | Fonction |
|--------|----------|
| `jarvis-boot-sequencer.sh` | Sequence de boot ordonnee de tous les services |
| `jarvis-ctl.sh` | Controle central JARVIS (start/stop/status/restart) |
| `jarvis-domino-engine.sh` | Lancement moteur domino en mode shell |
| `jarvis-wire-dominos.sh` | Cablage des chaines domino |

### Monitoring et Diagnostic

| Script | Fonction |
|--------|----------|
| `jarvis-flow-check.sh` | Verification flux systeme complet |
| `check_jarvis.sh` | Health check rapide JARVIS |
| `check_gpu_lmstudio.sh` | Verification GPU et LM Studio |
| `dashboard_resilient.sh` | Dashboard resilient (mode texte) |
| `jarvis-stress-benchmark.sh` | Benchmark stress complet |

### Reparation et Rescue

| Script | Fonction |
|--------|----------|
| `jarvis-rescue-switcher.sh` | Bascule mode rescue |
| `jarvis-benchmark-triggers.sh` | Declencheurs de benchmarks |
| `jarvis-log-reactor.sh` | Reacteur de logs (detecte patterns critiques) |
| `jarvis-hook-bridge.sh` | Pont entre hooks et skills |

### Automatisation

| Script | Fonction |
|--------|----------|
| `jarvis-auto-learn.sh` | Apprentissage automatique depuis logs |
| `linkedin_publish_auto.sh` | Publication LinkedIn automatique (CDP + xdotool) |
| `auto-backup.sh` | Sauvegarde automatique Timeshift |

---

## Integration Domino Engine

Codex CLI est une plateforme de dispatch dans le router domino :

```python
# core/domino/router.py
shell_skills = {
    "flow-controller": "bash scripts/jarvis-flow-check.sh",
    "zombie-cleanup": "ps aux | awk '$8~/Z/{print $2}' | xargs -r kill -9",
    "boot-sequencer": "bash scripts/jarvis-boot-sequencer.sh status",
}
```

---

## Chemins cles

```
~/Workspaces/jarvis-linux/scripts/                          # Tous les scripts shell
~/Workspaces/jarvis-linux/scripts/jarvis-flow-check.sh      # Flow check principal
~/Workspaces/jarvis-linux/scripts/jarvis-boot-sequencer.sh  # Boot sequencer
~/Workspaces/jarvis-linux/scripts/jarvis-rescue-switcher.sh # Rescue switcher
~/Workspaces/jarvis-linux/scripts/jarvis-benchmark-triggers.sh # Benchmarks
~/Workspaces/jarvis-linux/core/scripts/devops/jarvis-crash-guardian.sh # Crash guardian
~/Workspaces/jarvis-linux/core/domino/router.py             # Router (shell dispatch)
```
