# Patterns de Reponse aux Incidents

> **JARVIS Linux** — Analyse des rapports de reparation, 10 patterns majeurs
> Derniere mise a jour : 2026-03-28

---

## Top 10 des patterns d'incidents

### 1. Crash de service (228 incidents)

**Signal :**
- `systemctl is-failed SERVICE` retourne `failed`
- Logs `journalctl` montrent segfault, OOM, ou exit code non-zero
- Monitoring detecte absence de heartbeat

**Commandes de diagnostic :**
```bash
journalctl -u SERVICE_NAME --since "5 min ago" --no-pager -p err
systemctl status SERVICE_NAME
systemctl show SERVICE_NAME -p NRestarts,ActiveState,SubState
```

**Sequence d'auto-fix :**
1. Analyser les logs pour identifier la cause (OOM, segfault, config, dependance)
2. `systemctl restart SERVICE_NAME`
3. Attendre 5 secondes
4. `systemctl is-active SERVICE_NAME` — verifier le retour
5. Si echec : verifier les dependances, corriger, re-tenter
6. Si 3 echecs : escalader

**Declencheur d'escalade :**
- 3 restarts echoues consecutifs
- Meme cause racine sur 2+ services
- Service critique (Redis, Ollama, moniteur)

**Chaine domino liee :** `service-crash-recovery` (P10)

---

### 2. Echec GPU massif (3 incidents)

**Signal :**
- `nvidia-smi` retourne `Unable to determine the device handle` ou timeout
- `dmesg` contient `NVRM: Xid` ou `nvidia: GPU has fallen off the bus`
- Tous les jobs IA en erreur simultanement

**Commandes de diagnostic :**
```bash
nvidia-smi 2>&1
dmesg | grep -i -E "nvidia|nvrm|xid|pci" | tail -30
lspci | grep -i nvidia
cat /proc/driver/nvidia/version
```

**Sequence d'auto-fix :**
1. Niveau 1 : `sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm` (15s)
2. Niveau 2 : `echo 1 > /sys/bus/pci/devices/0000:XX:00.0/reset` (15s)
3. Niveau 3 : rechargement complet des modules nvidia (30s)
4. Niveau 4 : reboot machine (dernier recours, avec confirmation Turbo)

**Declencheur d'escalade :**
- Niveau 3 echoue
- Erreur hardware PCIe dans dmesg
- Temperature GPU > 95C

**Chaine domino liee :** `gpu-error-cascade` (P10)

---

### 3. Cascade multi-services (15 incidents)

**Signal :**
- 3+ services JARVIS en echec simultane
- Pattern typique : un service infrastructure tombe, emportant ses dependants
- `systemctl list-units --failed` montre un cluster de services lies

**Commandes de diagnostic :**
```bash
systemctl list-units --failed --no-legend
systemctl list-dependencies SERVICE_NAME --reverse
journalctl --since "2 min ago" -p err --no-pager | head -50
```

**Sequence d'auto-fix :**
1. Identifier le service racine de la cascade (celui tombe en premier)
2. Arreter tous les services dependants proprement
3. Reparer et redemarrer le service racine
4. Relancer via boot-sequencer en respectant l'ordre des vagues
5. Health check global apres redemarrage

**Declencheur d'escalade :**
- Service racine ne redemarre pas
- Plus de 5 services en echec
- Redis ou Ollama est le service racine

**Chaine domino liee :** `full-boot-sequence` (P10)

---

### 4. OOM Kill (12 incidents)

**Signal :**
- `dmesg | grep -i "out of memory"` retourne des lignes recentes
- `journalctl -k | grep -i oom` montre un processus tue
- Disparition soudaine d'un processus sans log d'erreur

**Commandes de diagnostic :**
```bash
dmesg | grep -i "out of memory" | tail -5
dmesg | grep -i "killed process" | tail -5
free -h
cat /proc/meminfo | grep -E "MemAvailable|SwapFree|CommitLimit|Committed_AS"
ps aux --sort=-rss | head -15
```

**Sequence d'auto-fix :**
1. `sync && echo 3 > /proc/sys/vm/drop_caches` — liberation immediate
2. Identifier le processus consommateur (`ps aux --sort=-rss`)
3. Si Chrome : `pkill -f chrome` puis redemarrer avec limites
4. Appliquer cgroups : `systemd-run --scope -p MemoryMax=4G COMMAND`
5. Proteger les critiques : `echo -1000 > /proc/PID/oom_score_adj`

**Declencheur d'escalade :**
- OOM kill sur un service critique (Redis, Ollama)
- 3+ OOM kills en 10 minutes
- RAM toujours > 90% apres drop caches

**Chaine domino liee :** `ram-pressure-cascade` (P10)

---

### 5. Accumulation de zombies (20 incidents)

**Signal :**
- `ps aux | awk '$8~/Z/' | wc -l` retourne > 10
- Load average en hausse sans CPU reel eleve
- LM Studio ou Ollama recement crashe/restart

**Commandes de diagnostic :**
```bash
ps aux | awk '$8~/Z/ {print $2, $3, $11}'
ps aux | awk '$8~/Z/' | wc -l
# Identifier les parents
ps aux | awk '$8~/Z/ {print $3}' | sort | uniq -c | sort -rn
```

**Sequence d'auto-fix :**
1. Envoyer SIGCHLD a chaque parent : `kill -s SIGCHLD PPID`
2. Attendre 3s, reverifier le comptage
3. Si orphelins (parent=1) : `kill -9 ZOMBIE_PID`
4. Si LM Studio est le parent : restart LM Studio proprement
5. Verification finale : comptage zombies doit etre < 5

**Declencheur d'escalade :**
- Zombies > 50 malgre cleanup
- Parent ne repond pas a SIGCHLD
- Zombies re-apparaissent en < 5 minutes

**Chaine domino liee :** `ram-pressure-cascade` (P10, etape 3)

---

### 6. Downshift reseau (5 incidents)

**Signal :**
- `ethtool enp6s0 | grep Speed` affiche `100Mb/s` au lieu de `1000Mb/s`
- Latence cluster augmentee (> 10ms au lieu de < 1ms)
- Transferts de modeles IA anormalement lents

**Commandes de diagnostic :**
```bash
ethtool enp6s0 | grep -E "Speed|Duplex|Link detected|Auto-negotiation"
ip link show enp6s0
dmesg | grep -i -E "r8169|eth|link" | tail -10
ping -c 5 192.168.1.1
```

**Sequence d'auto-fix :**
1. Forcer renegociation : `sudo ethtool -s enp6s0 speed 1000 duplex full autoneg on`
2. Attendre 5s, verifier vitesse
3. Si echec : `sudo modprobe -r r8169 && sleep 2 && sudo modprobe r8169`
4. Si echec : accepter 100Mbps, notifier Turbo (probable probleme cable/switch)
5. Ajuster les timeouts des services reseau-dependants

**Declencheur d'escalade :**
- Link Down total (interface DOWN)
- Reload driver echoue
- Probleme persiste > 5 minutes

**Chaine domino liee :** `network-degradation-cascade` (P8)

---

### 7. Erreurs filesystem (3 incidents)

**Signal :**
- `dmesg | grep -i "ext4.*error"` retourne des erreurs
- Fichiers corrompus ou illisibles
- `journalctl` montre des erreurs I/O

**Commandes de diagnostic :**
```bash
dmesg | grep -i -E "ext4|io.error|blk_update" | tail -20
sudo smartctl -a /dev/nvme0n1
df -h
mount | grep -E "errors|ro"
```

**Sequence d'auto-fix :**
1. Verifier si le filesystem est passe en read-only
2. Si oui : **NE PAS tenter de reparer en ligne**
3. Creer un snapshot Timeshift si possible
4. Proposer a Turbo : `sudo fsck -y /dev/PARTITION` (necessite reboot)
5. Si corruption severe : proposer restauration Timeshift

**Declencheur d'escalade :**
- Filesystem en read-only
- SMART rapporte des secteurs defaillants
- Corruption sur /home ou /
- Toujours escalader — ne jamais tenter fsck automatiquement

**Chaine domino liee :** `disaster-recovery` (P10)

---

### 8. CUDA driver mismatch (4 incidents)

**Signal :**
- Erreur `CUDA error: no kernel image is available for execution on the device`
- `nvidia-smi` fonctionne mais les jobs CUDA echouent
- Version CUDA runtime != version driver

**Commandes de diagnostic :**
```bash
nvidia-smi | head -5
nvcc --version 2>/dev/null
cat /usr/local/cuda/version.txt 2>/dev/null
ldconfig -p | grep cuda
echo $CUDA_VISIBLE_DEVICES
python3 -c "import torch; print(torch.cuda.is_available(), torch.version.cuda)"
```

**Sequence d'auto-fix :**
1. Verifier `CUDA_VISIBLE_DEVICES` — corriger si mal configure
2. `sudo ldconfig` — reconstruire le cache des librairies
3. Verifier les symlinks CUDA : `ls -la /usr/local/cuda`
4. Si mismatch version : `sudo apt install cuda-toolkit-XX-X` (version compatible)
5. Restart des services IA apres correction

**Declencheur d'escalade :**
- Mismatch entre kernel module et userspace
- Necessite reinstallation complete du driver
- Apres un `apt upgrade` qui a touche aux paquets nvidia

**Chaine domino liee :** `gpu-error-cascade` (P10)

---

### 9. systemd StartLimitInterval (10 incidents)

**Signal :**
- `systemctl status SERVICE` affiche `start-limit-hit`
- Service refuse de redemarrer malgre `systemctl restart`
- Logs : `Start request repeated too quickly`

**Commandes de diagnostic :**
```bash
systemctl status SERVICE_NAME
systemctl show SERVICE_NAME -p StartLimitInterval,StartLimitBurst,NRestarts
journalctl -u SERVICE_NAME --since "10 min ago" --no-pager | tail -30
```

**Sequence d'auto-fix :**
1. `systemctl reset-failed SERVICE_NAME` — reinitialiser le compteur
2. Corriger le fichier unit : deplacer `StartLimitInterval` et `StartLimitBurst` dans la section `[Unit]` (pas `[Service]`)
3. Ajuster les valeurs : `StartLimitInterval=60` et `StartLimitBurst=5`
4. `systemctl daemon-reload`
5. `systemctl start SERVICE_NAME`

**Declencheur d'escalade :**
- Service retombe immediatement apres reset-failed
- Cause racine non identifiee dans les logs
- Service critique bloque en start-limit

**Chaine domino liee :** `service-crash-recovery` (P10)

---

### 10. Chrome CDP perdu (8 incidents)

**Signal :**
- `curl -s http://localhost:9222/json/version` echoue ou timeout
- BrowserOS/scripts CDP ne peuvent plus piloter Chrome
- Chrome visible a l'ecran mais port debug ferme

**Commandes de diagnostic :**
```bash
curl -s http://localhost:9222/json/version
pgrep -a chrome | grep remote-debugging
ss -tlnp | grep 9222
ps aux | grep chrome | grep -v grep | wc -l
```

**Sequence d'auto-fix :**
1. `pkill -f chrome` — tuer toutes les instances
2. Attendre 3s que les processus se terminent
3. Nettoyer le profil lock : `rm -f ~/.config/google-chrome/SingletonLock`
4. Redemarrer avec debug : `google-chrome --remote-debugging-port=9222 --no-first-run &`
5. Attendre 5s, verifier : `curl -s http://localhost:9222/json/version`

**Declencheur d'escalade :**
- Chrome ne demarre pas (crash au lancement)
- Port 9222 occupe par un autre processus
- Profil Chrome corrompu (erreur au demarrage)

**Chaine domino liee :** `service-crash-recovery` (P10)

---

## Regles d'or de la reponse incident

Ces 5 regles constituent la doctrine JARVIS pour la gestion des incidents. Elles sont non-negociables.

### Regle 1 : Diagnostiquer avant d'agir

> **Jamais de kill -9 en premier reflexe.** Toujours lire les logs, comprendre la cause, puis agir. Un restart aveugle masque le probleme et garantit sa recurrence. La sequence est : observer (`journalctl`, `ps`, `free`) → comprendre → agir → verifier.

### Regle 2 : Snapshot avant intervention destructrice

> **Tout acte de reparation qui modifie l'etat du systeme doit etre precede d'un snapshot Timeshift.** Pas de snapshot = pas de filet de securite = pas d'intervention. La chaine `pre-incident-backup` doit se declencher automatiquement. Cout : 90 secondes. Benefice : restauration complete en cas d'erreur.

### Regle 3 : Escalade progressive, jamais le marteau d'emblee

> **Toujours commencer par l'intervention la moins invasive.** Niveau 1 avant Niveau 2, restart avant reboot, drop caches avant kill. Chaque niveau est tente avec verification avant escalade. Le reboot est le dernier recours, pas le premier reflexe. Les 4 niveaux de la recuperation GPU illustrent parfaitement ce principe.

### Regle 4 : Verifier le resultat, pas seulement l'action

> **Une reparation n'est pas terminee tant qu'elle n'est pas verifiee.** Apres chaque action corrective, attendre le delai de stabilisation (5-30s selon le service) et verifier que le service est reellement operationnel. Un `systemctl restart` qui retourne 0 ne signifie pas que le service fonctionne — il faut tester le health endpoint.

### Regle 5 : Tout incident laisse une trace

> **Logger systematiquement : horodatage, symptome, diagnostic, action, resultat.** Ces traces alimentent les benchmarks du Domino Engine, permettent de detecter les patterns recurrents, et constituent la base de l'apprentissage continu de JARVIS. Un incident non-documente est un incident qui se reproduira sans qu'on puisse l'anticiper.
