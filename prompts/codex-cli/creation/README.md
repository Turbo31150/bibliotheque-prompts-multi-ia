# Codex CLI — Creation

## Description
Prompts de creation avec Codex CLI orientes Linux performance et integration JARVIS. Codex excelle dans la creation de scripts systeme, l'optimisation de performance Linux, l'integration de services et la generation de configurations d'infrastructure.

## Configuration requise
- Codex CLI installe et configure
- Acces root/sudo pour les modifications systeme
- Linux (Debian/Ubuntu recommande)
- JARVIS installe dans ~/jarvis-linux/

---

## Prompts par type de tache

### Creation — Optimisation Linux pour workloads IA

```
You are an expert Linux performance engineer and SRE.
Your job is to help me turn this Linux machine into a highly optimized host for:
- heavy AI workloads (GPU/CPU bound, long-running background jobs)
- a custom AI assistant called "JARVIS" that must be tightly integrated into the OS

GENERAL RULES
- Always start by asking for and analyzing system information:
  - OS and version, kernel, CPU, RAM, disks, GPU(s), filesystem, network
  - My distribution family (Debian/Ubuntu, RHEL/Fedora/Rocky, Arch, etc.)
- NEVER assume sudo is available: always prefix with `sudo` when needed.
- Before changing anything:
  - Show the exact commands or config file diffs you propose.
  - Propose a backup strategy for each file you touch.
  - Ask for my confirmation before any destructive/irreversible action.

GOAL
1. Max out performance:
   - CPU: governor `performance`, IRQ affinity, NUMA awareness
   - Memory: vm.swappiness, dirty ratios, huge pages
   - Disk: I/O scheduler, noatime, NVMe queue settings
   - Network: TCP/IP sysctl tuning, BBR congestion control
   - Services: systemd-analyze, disable unused services, fast boot

2. Integrate JARVIS into the OS:
   - systemd unit files for JARVIS backend and workers
   - Dedicated system user with minimal permissions
   - Log rotation (logrotate or journald)
   - Auto-start, restart policies, health checks
   - cgroups to prioritize JARVIS CPU/RAM/GPU

3. Make changes reproducible:
   - Ansible playbook snippet OR shell script
   - Document each step with comments

WORKFLOW
Step 1: Collect system info
Step 2: Propose prioritized plan (safety/baseline → performance → JARVIS integration)
Step 3: Execute with exact commands and rollback options
Step 4: Validate with benchmarks and verification commands
```

---

### Creation — Service systemd pour JARVIS

```
Cree un service systemd complet pour JARVIS :

## SPECIFICATION
- Service principal : jarvis-core.service
  - Type : notify (avec sd_notify)
  - User : jarvis (compte systeme dedie)
  - WorkingDirectory : /home/turbo/jarvis-linux
  - ExecStart : uv run python -m jarvis.main
  - Restart : on-failure (max 5 en 5 min)
  - Health check : ExecStartPost avec curl /health

- Worker inference : jarvis-worker@.service (template)
  - Instancie : jarvis-worker@gpu0, jarvis-worker@gpu1, etc.
  - Isole par GPU via cgroups
  - Depends on : jarvis-core.service

## FICHIERS A GENERER
1. /etc/systemd/system/jarvis-core.service
2. /etc/systemd/system/jarvis-worker@.service
3. /etc/logrotate.d/jarvis
4. Script d'installation : scripts/install-service.sh
5. Script de verification : scripts/check-service.sh
```

---

### Creation — Script de monitoring GPU

```
Cree un script de monitoring GPU complet :

## SPECIFICATION
- Langage : Python 3 (standalone, pas de dependances externes)
- Collecte : toutes les 10 secondes
- Metriques : temperature, utilisation, VRAM, fan speed, power draw
- Seuils : warning 75C, critical 85C
- Actions :
  - Warning : log + notification Telegram
  - Critical : log + notification + decharge modele le plus lourd
- Stockage : append dans /var/log/jarvis/gpu_metrics.csv
- Format CSV : timestamp, gpu_id, temp, util, vram_used, vram_total, fan, power

## CODE
#!/usr/bin/env python3
# gpu_monitor.py — Monitoring GPU autonome pour JARVIS
# Execution : python3 gpu_monitor.py (ou via cron/systemd)
```

---

### Creation — Audit complet de la machine

```
Tu es Codex CLI en mode audit de reconstruction.
Objectif : lister toute la configuration actuelle utile pour recreer cette machine.
1) Inventorie : config shell, services, Docker, MCP, plugins, skills, memoire, auth, aliases, dependances, ports, repos.
2) Separe ce qui est :
   - requis pour fonctionner
   - ajoute par l'utilisateur
   - secret a migrer separement
   - historique facultatif
3) Produis un rapport de migration clair avec chemins exacts.
4) Termine par : prerequis, ordre de migration, verifications post-install.
Structure : Goal/Plan/Code/Verify.
```

---

### Amelioration / Refactoring — Tuning kernel Linux

```
Optimise le kernel Linux pour les workloads IA :

## SYSCTL RECOMMANDES
# /etc/sysctl.d/99-jarvis-performance.conf

# CPU
kernel.sched_autogroup_enabled = 0     # Desactiver autogroup pour les workloads batch

# Memoire
vm.swappiness = 10                      # Reduire l'utilisation du swap
vm.dirty_ratio = 40                     # Ratio d'ecriture dirty pages
vm.dirty_background_ratio = 10          # Ratio background flush
vm.overcommit_memory = 1                # Permettre l'overcommit (utile pour les LLM)

# Reseau
net.core.rmem_max = 16777216            # Buffer reception max
net.core.wmem_max = 16777216            # Buffer envoi max
net.ipv4.tcp_congestion_control = bbr   # BBR congestion control
net.core.default_qdisc = fq            # Fair queueing

# Fichiers
fs.file-max = 2097152                   # Limite fichiers ouverts
fs.inotify.max_user_watches = 524288    # Watchers inotify

## VERIFICATION
sysctl -a | grep vm.swappiness
sysctl -a | grep tcp_congestion_control

## ROLLBACK
# Garder une copie de /etc/sysctl.conf avant modification
```

---

### Debug — Machine lente apres modification

```
La machine est lente apres les modifications de tuning.

## DIAGNOSTIC
1. Quels sysctl ont ete modifies ? (diff avec la config precedente)
2. Le swap est-il sature ? (free -h, swapon -s)
3. Un service est-il en boucle ? (top, htop)
4. Les GPUs sont-ils satures ? (nvidia-smi)
5. Le disque est-il en I/O wait ? (iostat -x 1)

## ROLLBACK
1. Restaurer le sysctl precedent :
   sudo cp /etc/sysctl.d/99-jarvis-performance.conf.bak /etc/sysctl.d/99-jarvis-performance.conf
   sudo sysctl --system

2. Si un service est en boucle :
   sudo systemctl stop [SERVICE]
   journalctl -u [SERVICE] --since "10 min ago"

3. Mesurer apres rollback pour confirmer l'amelioration
```

---

### Documentation — Rapport d'audit machine

```
Genere un rapport d'audit machine complet :

## FORMAT
### Systeme
| Element | Valeur |
|---------|--------|
| OS | [distro version] |
| Kernel | [version] |
| CPU | [modele, cores] |
| RAM | [total, utilise] |
| Disque | [type, taille, utilise] |
| GPU | [modeles, VRAM] |

### Services actifs
| Service | Port | Status | PID | Memory |
|---------|------|--------|-----|--------|

### Tuning applique
| Parametre | Valeur | Defaut | Impact |
|-----------|--------|--------|--------|

### Recommandations
1. [Recommandation 1]
2. [Recommandation 2]
3. [Recommandation 3]
```

---

## Exemples concrets

### Exemple 1 : Tuning complet
```bash
codex "Analyse cette machine (Ryzen 5700X3D, 6 GPUs, 46GB RAM) et propose un plan de tuning Linux pour les workloads IA"
```

**Resultat attendu** : Plan priorise en 3 phases (baseline, performance, JARVIS), avec commandes exactes et rollback.

### Exemple 2 : Service systemd
```bash
codex "Cree un service systemd pour JARVIS avec auto-restart, health check et log rotation"
```

**Resultat attendu** : Fichier .service complet, logrotate config, script d'installation et verification.

### Exemple 3 : Monitoring GPU
```bash
codex "Cree un script Python de monitoring GPU qui alerte via Telegram si temp > 75C"
```

**Resultat attendu** : Script standalone avec parsing nvidia-smi, seuils, notifications, CSV logging.

---

## Effet sur le modele
- Le prompt SRE expert active un mode de raisonnement structure et prudent
- Les garde-fous (backup avant modif, confirmation avant action irreversible) evitent les catastrophes
- La structure Goal/Plan/Code/Verify force la verification apres chaque modification
- Les commandes de rollback permettent de revenir en arriere rapidement
- Codex est particulierement efficace pour les scripts shell et les configurations systeme
- Le tuning kernel avec commentaires explique chaque parametre, rendant la config maintenable
