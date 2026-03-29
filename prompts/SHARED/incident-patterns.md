# Patterns d'Incidents JARVIS — Extraits de 767+ Repair Reports

> Derniere mise a jour : 2026-03-28
> Source : repair-reports/, domino-chains/, benchmarks/

---

## Top 10 Patterns

### 1. Service Crash (228 incidents)

- **Signal** : `systemctl failed`, SIGKILL, segfault dans journalctl
- **Frequence** : ~8/jour en moyenne
- **Severite** : CRITIQUE

**Commandes diagnostiques :**
```bash
journalctl -u <service> --since "5 min ago" --no-pager
systemctl status <service>
systemctl list-units --state=failed
```

**Sequence auto-fix :**
1. `systemctl restart <service>`
2. Attente T+5s, verification `systemctl is-active`
3. Si echec : isolation cgroups + restart force
4. Si echec x3 : escalade TTS

**Escalation trigger** : 3 echecs consecutifs en moins de 5 min
**Chaine domino liee** : `service-crash-recovery`

---

### 2. GPU Mass Failure (3 incidents)

- **Signal** : `nvidia-smi` retourne erreur, dmesg NVRM/Xid
- **Frequence** : ~1/mois (rare mais critique)
- **Severite** : CRITIQUE

**Commandes diagnostiques :**
```bash
nvidia-smi
dmesg | grep -i "NVRM\|Xid\|gpu\|pcie"
cat /proc/driver/nvidia/gpus/*/information
```

**Sequence auto-fix (4 niveaux) :**
1. Niveau 1 : reset GPU via `nvidia-smi -r`
2. Niveau 2 : restart `nvidia-persistenced`, reload `nvidia_uvm`
3. Niveau 3 : `CUDA_VISIBLE_DEVICES` exclude les GPUs morts, mode degrade
4. Niveau 4 : routage cluster vers M2/M3/OL1

**Escalation trigger** : >3 GPUs down simultanement
**Chaine domino liee** : `gpu-error-cascade`

---

### 3. Multi-Service Cascade (15 incidents)

- **Signal** : >5 services failed dans systemctl, boot partiel
- **Frequence** : ~1/semaine
- **Severite** : CRITIQUE

**Commandes diagnostiques :**
```bash
systemctl list-units --state=failed --no-pager
journalctl -p err --since "10 min ago" --no-pager
```

**Sequence auto-fix :**
1. Arret des services non-essentiels
2. Kill zombies + drop_caches
3. Boot-sequencer wave restart (8 vagues ordonnees)
4. Verification post-boot complete

**Escalation trigger** : boot-sequencer echoue 2 fois
**Chaine domino liee** : `full-boot-sequence`

---

### 4. OOM Kill (12 incidents)

- **Signal** : `oom-killer` dans dmesg, RAM >95%
- **Frequence** : ~1/semaine
- **Severite** : HAUTE

**Commandes diagnostiques :**
```bash
dmesg | grep -i "oom\|out of memory\|killed process"
free -h
ps aux --sort=-%mem | head -20
```

**Sequence auto-fix :**
1. `echo 3 > /proc/sys/vm/drop_caches`
2. Kill processus zombies
3. Arret services non-essentiels (LM Studio workers, Docker non-critique)
4. Reduire parallelisme inference
5. Mise en place cgroups limites memoire

**Escalation trigger** : RAM >95% apres cleanup
**Chaine domino liee** : `ram-pressure-cascade`

---

### 5. Zombie Accumulation (20 incidents)

- **Signal** : Processus en etat Z dans `ps aux`
- **Frequence** : ~2/semaine
- **Severite** : MOYENNE

**Commandes diagnostiques :**
```bash
ps aux | awk '$8~/Z/'
ps -eo pid,ppid,stat,comm | grep Z
```

**Sequence auto-fix :**
1. Identifier les parents des zombies
2. Envoyer SIGCHLD aux parents
3. Kill -9 les zombies orphelins
4. Restart des services parents si necessaire

**Escalation trigger** : >50 zombies ou parent = PID 1
**Chaine domino liee** : `multi_service_fail`

---

### 6. Network Downshift (5 incidents)

- **Signal** : Latence >500ms, perte paquets, vitesse reduite
- **Frequence** : ~2/mois
- **Severite** : HAUTE

**Commandes diagnostiques :**
```bash
ethtool enp6s0
ip link show
ping -c 5 192.168.1.1
ss -tuln
```

**Sequence auto-fix :**
1. Forcer renegociation : `ethtool -s enp6s0 autoneg on`
2. Reload interface : `ip link set enp6s0 down && ip link set enp6s0 up`
3. Si echec : fallback cluster (router vers M2/M3)

**Escalation trigger** : interface down >30s
**Chaine domino liee** : `network-degradation-cascade`

---

### 7. Filesystem Errors (3 incidents)

- **Signal** : Erreurs ext4 dans dmesg, I/O errors
- **Frequence** : Rare (~1/mois)
- **Severite** : CRITIQUE

**Commandes diagnostiques :**
```bash
dmesg | grep -i "ext4\|i/o error\|filesystem"
df -h
smartctl -a /dev/nvme0n1
```

**Sequence auto-fix :**
1. Remount read-only si corruption active
2. `fsck -y` sur la partition (si demontable)
3. Si non reparable : Timeshift restore vers dernier snapshot sain

**Escalation trigger** : Erreurs I/O repetees sur partition systeme
**Chaine domino liee** : `disaster-recovery`

---

### 8. CUDA Driver Mismatch (4 incidents)

- **Signal** : `CUDA error: driver version is insufficient`, module load fail
- **Frequence** : Apres mise a jour kernel/driver (~1/mois)
- **Severite** : HAUTE

**Commandes diagnostiques :**
```bash
nvidia-smi
cat /proc/driver/nvidia/version
nvcc --version 2>/dev/null
cat /etc/environment | grep CUDA
ldconfig -p | grep cuda
```

**Sequence auto-fix :**
1. Verifier coherence kernel module vs userspace lib
2. Ajuster `CUDA_VISIBLE_DEVICES` dans `/etc/environment`
3. `ldconfig` pour recharger les libs
4. Restart services GPU-dependants

**Escalation trigger** : Aucun GPU fonctionnel apres fix
**Chaine domino liee** : `gpu-error-cascade` + `gpu_cuda_poisoned.chain`

---

### 9. systemd StartLimitInterval (10 incidents)

- **Signal** : `start request repeated too quickly` dans journalctl
- **Frequence** : ~1/semaine
- **Severite** : MOYENNE

**Commandes diagnostiques :**
```bash
journalctl -u <service> | grep -i "start.*limit"
systemctl show <service> | grep -i limit
```

**Sequence auto-fix :**
1. `systemctl reset-failed <service>`
2. Deplacer `StartLimitIntervalSec` et `StartLimitBurst` vers la section `[Unit]` (pas `[Service]`)
3. `systemctl daemon-reload`
4. Restart du service

**Escalation trigger** : Service toujours en echec apres reset-failed
**Chaine domino liee** : `service-crash-recovery`

---

### 10. Chrome CDP Lost (8 incidents)

- **Signal** : Connexion CDP port 9222 refusee, Chrome crash
- **Frequence** : ~2/semaine
- **Severite** : MOYENNE

**Commandes diagnostiques :**
```bash
curl -s http://localhost:9222/json/version
pgrep -a chrome
ss -tuln | grep 9222
```

**Sequence auto-fix :**
1. Kill tous les processus Chrome : `pkill -9 chrome`
2. Nettoyage : `rm -rf /tmp/.org.chromium.*`
3. Restart : `google-chrome --remote-debugging-port=9222 --headless &`
4. Verification CDP : `curl http://localhost:9222/json/version`

**Escalation trigger** : CDP toujours down apres 3 tentatives
**Chaine domino liee** : `browser-session-repair` + `chrome_cdp_lost.chain`

---

## Regles d'Or

1. **Snapshot avant repair** — Toujours declencher `pre-incident-backup` avant toute reparation intrusive. On ne repare jamais sans filet de securite.

2. **Jamais de boucle infinie** — Maximum 3 retries par step, maximum 3 escalades par chaine. Au-dela, on passe en mode rescue et on alerte l'humain.

3. **Toujours un rapport** — Chaque incident genere un fichier dans `repair-reports/`. Pas de reparation silencieuse. Tout est trace pour l'apprentissage.

4. **L'humain est le dernier recours** — Si toutes les chaines automatiques echouent, alerte TTS via `jarvis-tts.sh`. Turbo decide. L'IA propose, l'humain dispose.

5. **Le materiel commande** — Hardware first. Si le disque est mort, le GPU crame ou la RAM defaille, aucun logiciel ne peut compenser. Diagnostic hardware avant software, toujours.
