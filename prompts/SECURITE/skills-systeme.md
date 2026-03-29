# Catalogue des Skills Systeme - Securite & Stabilite

> **JARVIS Linux** — 9 skills de protection systeme
> Derniere mise a jour : 2026-03-28

---

## 1. system-crash-guardian

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P10 — Critique |

**Description detaillee :**
Gardien permanent contre les crash systeme. Surveille en continu les boucles de crash (services qui redemarrent en boucle), l'accumulation de processus zombies au-dela du seuil de 10, et les freezes de l'interface graphique GNOME. Applique une politique de containerisation pour isoler les services instables et empecher la propagation des pannes. Constitue la premiere ligne de defense du systeme JARVIS.

**Conditions d'auto-trigger :**
- Service en crash loop detecte (3+ redemarrages en 60s)
- Nombre de zombies > 10
- GUI freeze detecte (GNOME Shell unresponsive > 15s)
- Charge CPU d'un service > 95% pendant 30s

**Commandes cles :**
```bash
# Detection des zombies
ps aux | awk '$8~/Z/ {print $0}'

# Services en echec
systemctl list-units --failed

# Logs de crash d'un service
journalctl -u SERVICE_NAME --since "5 min ago" --no-pager

# Verification crash loop
systemctl show SERVICE_NAME -p NRestarts

# Freeze GUI detection
dbus-send --session --dest=org.gnome.Shell --type=method_call /org/gnome/Shell org.gnome.Shell.Eval string:'global.get_current_time()'
```

**Chaines domino liees :**
- `service-crash-recovery` (P10) — recuperation apres crash
- `gpu-error-cascade` (P10) — si crash GPU detecte
- `pre-incident-backup` (P9) — snapshot avant intervention

---

## 2. system-stabilization-mode

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P10 — Critique |

**Description detaillee :**
Mode d'urgence en deux phases pour stabiliser le systeme en moins de 60 secondes. Phase 1 (30s) : detection et diagnostic rapide des CPU hogs, crash loops, zombies et pression RAM. Phase 2 (30s) : neutralisation des menaces identifiees par kill, restart ou isolation. Ce skill est le mode "combat" de JARVIS — tout est subordonne a la stabilite immediate du systeme.

**Conditions d'auto-trigger :**
- CPU global > 90% pendant 15s
- RAM > 85% et swap en augmentation
- 3+ services en echec simultane
- Declenchement manuel par commande vocale "JARVIS mode urgence"

**Commandes cles :**
```bash
# Phase 1 — Detection (30s)
# CPU hogs
ps aux --sort=-%cpu | head -20

# Crash loops
systemctl list-units --failed --no-legend | wc -l

# Zombies
ps aux | awk '$8~/Z/' | wc -l

# RAM pressure
free -h && cat /proc/meminfo | grep -E "MemAvailable|SwapFree"

# Phase 2 — Neutralisation (30s)
# Kill CPU hog
kill -9 PID

# Restart service
systemctl restart SERVICE_NAME

# Drop caches urgence
sync && echo 3 > /proc/sys/vm/drop_caches

# Reap zombies
kill -s SIGCHLD PARENT_PID
```

**Chaines domino liees :**
- `ram-pressure-cascade` (P10) — si RAM critique
- `service-crash-recovery` (P10) — si service en echec
- `pre-incident-backup` (P9) — snapshot avant action destructrice

---

## 3. gpu-crash-recovery

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P10 — Critique |

**Description detaillee :**
Recuperation GPU en 4 niveaux progressifs d'intervention. Niveau 1 : soft reset par dechargement du module nvidia_uvm. Niveau 2 : reset au niveau PCIe. Niveau 3 : rechargement complet du module nvidia. Niveau 4 : reboot machine en dernier recours. Chaque niveau est tente avec verification avant escalade. Gere les 6 GPUs du cluster M1 individuellement ou en masse.

**Conditions d'auto-trigger :**
- `nvidia-smi` retourne une erreur ou timeout
- Temperature GPU > 85C
- VRAM leak detecte (utilisation croissante sans processus actif)
- Erreur CUDA dans les logs kernel
- Echec d'un job Ollama/LM Studio lie au GPU

**Commandes cles :**
```bash
# Niveau 1 — Soft reset
sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm

# Niveau 2 — PCIe reset
echo 1 > /sys/bus/pci/devices/0000:XX:00.0/reset

# Niveau 3 — Reload module complet
sudo rmmod nvidia_drm nvidia_modeset nvidia_uvm nvidia
sudo modprobe nvidia nvidia_uvm nvidia_modeset nvidia_drm

# Niveau 4 — Reboot
sudo systemctl reboot

# Diagnostics
nvidia-smi --query-gpu=index,name,temperature.gpu,utilization.gpu,memory.used --format=csv
dmesg | grep -i nvidia | tail -20
```

**Chaines domino liees :**
- `gpu_error` — erreur GPU simple
- `gpu_thermal` — surchauffe GPU
- `vram_leak` — fuite memoire VRAM
- `gpu_mass_failure` — echec multi-GPU
- `gpu-error-cascade` (P10) — chaine complete de recuperation

---

## 4. ram-pressure-handler

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P10 — Critique |

**Description detaillee :**
Gestion de la pression memoire en 4 niveaux. Niveau 1 : liberation des caches noyau. Niveau 2 : identification du plus gros consommateur RAM. Niveau 3 : arret des services non essentiels (Chrome, n8n, services sociaux). Niveau 4 : protection OOM avec cgroups pour sanctuariser les services critiques (Redis, Ollama, moniteur). Sur les 46GB de RAM de M1, le seuil critique est a 4GB disponibles.

**Conditions d'auto-trigger :**
- RAM utilisee > 80% (MemAvailable < ~9GB)
- Swap en remplissage rapide (> 1GB/min)
- OOM kill detecte dans dmesg
- MemAvailable < 4GB

**Commandes cles :**
```bash
# Niveau 1 — Drop caches
sync && echo 3 > /proc/sys/vm/drop_caches

# Niveau 2 — Identifier le consommateur
ps aux --sort=-rss | head -10
smem -t -k -s rss | tail -10

# Niveau 3 — Stop non-essentiels
systemctl stop jarvis-social.service
systemctl stop jarvis-n8n.service
pkill -f chrome

# Niveau 4 — OOM protect
echo -1000 > /proc/$(pgrep redis-server)/oom_score_adj
echo -1000 > /proc/$(pgrep ollama)/oom_score_adj

# Monitoring
free -h
cat /proc/meminfo | grep -E "MemTotal|MemAvailable|SwapTotal|SwapFree"
vmstat 1 5
```

**Chaines domino liees :**
- `ram-pressure-cascade` (P10) — chaine complete de desescalade
- `service-crash-recovery` (P10) — si un service tombe pendant le delestage
- `pre-incident-backup` (P9) — snapshot si intervention lourde

---

## 5. zombie-cleanup

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P8 — Haute |

**Description detaillee :**
Nettoyage des processus zombies qui s'accumulent dans le systeme. Detecte les zombies au-dela du seuil de 10, envoie SIGCHLD au processus parent pour forcer le reap, et gere les orphelins en les rattachant a init. Cible principalement LM Studio et Ollama qui sont les principaux generateurs de zombies sur le cluster JARVIS.

**Conditions d'auto-trigger :**
- Nombre de zombies > 10
- Verification periodique toutes les 5 minutes
- Apres un crash de LM Studio ou Ollama
- Apres un kill -9 de processus IA

**Commandes cles :**
```bash
# Detection des zombies
ps aux | awk '$8~/Z/ {print $2, $3, $11}'

# Comptage
ps aux | awk '$8~/Z/' | wc -l

# Envoyer SIGCHLD au parent
kill -s SIGCHLD $(ps -o ppid= -p ZOMBIE_PID)

# Cleanup en masse
ps aux | awk '$8~/Z/ {print $3}' | sort -u | xargs -I{} kill -s SIGCHLD {}

# Orphelins — si le parent est PID 1
ps aux | awk '$8~/Z/ && $3==1 {print $2}' | xargs kill -9 2>/dev/null

# Verification post-cleanup
ps aux | awk '$8~/Z/' | wc -l
```

**Chaines domino liees :**
- `ram-pressure-cascade` (P10) — les zombies sont nettoyes dans cette chaine
- `system-stabilization-mode` — triage des zombies en Phase 1

---

## 6. timeshift-backup

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P9 — Tres haute |

**Description detaillee :**
Gestion des snapshots Timeshift pour la protection du systeme. Cree des snapshots pre-incident (avant toute reparation), post-update (apres mises a jour apt/pilotes), et gere la rotation automatique pour eviter de saturer le disque. En cas de catastrophe, propose la restauration depuis le dernier snapshot sain. Verification d'integrite hebdomadaire le dimanche a 5h.

**Conditions d'auto-trigger :**
- Avant toute reparation systeme (pre-incident)
- Apres `apt upgrade` ou mise a jour driver NVIDIA
- Rotation quotidienne a 4h du matin
- Verification integrite dimanche 5h
- Sur demande explicite "JARVIS backup"

**Commandes cles :**
```bash
# Creer un snapshot
sudo timeshift --create --comments "JARVIS pre-incident $(date +%Y%m%d-%H%M)" --tags D

# Lister les snapshots
sudo timeshift --list

# Restaurer un snapshot
sudo timeshift --restore --snapshot 'YYYY-MM-DD_HH-MM-SS' --skip-grub

# Supprimer un snapshot ancien
sudo timeshift --delete --snapshot 'YYYY-MM-DD_HH-MM-SS'

# Verification integrite
sudo timeshift --list | grep -c ">"
df -h / | awk 'NR==2 {print "Espace utilise:", $5}'
```

**Chaines domino liees :**
- `pre-incident-backup` (P9)
- `post-update-backup` (P6)
- `backup-rotation-check` (P3)
- `disaster-recovery` (P10)
- `backup-integrity-verify` (P4)

---

## 7. boot-sequencer

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P10 — Critique |

**Description detaillee :**
Orchestrateur de demarrage en 8 vagues avec delais inter-vagues de 5 secondes et delais inter-services de 2 secondes. Chaque vague a un ordre de priorite strict : infrastructure d'abord (Redis), puis IA (Ollama), puis monitoring, puis les services applicatifs. Verifie la sante de chaque service avant de lancer la vague suivante. Un echec de vague critique (1-3) bloque le demarrage.

**Conditions d'auto-trigger :**
- Boot systeme (apres login)
- Apres un reboot force
- Commande vocale "JARVIS demarrage complet"
- Apres une restauration Timeshift

**Commandes cles :**
```bash
# Vague 1 — Redis (infrastructure)
systemctl start redis-server && sleep 5

# Vague 2 — Ollama (moteur IA)
systemctl start ollama && sleep 5

# Vague 3 — Moniteur systeme
systemctl start jarvis-monitor && sleep 5

# Vague 4 — Services IA
systemctl start jarvis-ai lm-studio && sleep 5

# Vague 5 — n8n (workflows)
systemctl start jarvis-n8n && sleep 5

# Vague 6 — Chrome (navigateur)
systemctl start jarvis-chrome && sleep 5

# Vague 7 — Social (LinkedIn, GitHub)
systemctl start jarvis-social && sleep 5

# Vague 8 — Voice (TTS/STT)
systemctl start jarvis-voice && sleep 5

# Health check global
systemctl list-units --type=service --state=running | grep jarvis
```

**Chaines domino liees :**
- `full-boot-sequence` (P10) — chaine complete de boot
- `service-crash-recovery` (P10) — si un service echoue pendant le boot

---

## 8. rescue-mode-switcher

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P10 — Critique |

**Description detaillee :**
Basculement entre mode TTY3 (terminal de debug/Claude) et mode GUI GNOME pour diagnostic et reparation. En mode TTY3, capture l'etat complet du systeme (CPU, RAM, GPU, services, logs) et l'envoie au cluster IA pour analyse. Permet de reprendre le controle meme quand l'interface graphique est completement figee. C'est la "porte de secours" de JARVIS.

**Conditions d'auto-trigger :**
- GUI freeze > 30s
- Commande clavier Ctrl+Alt+F3 (vers TTY3)
- Commande clavier Ctrl+Alt+F1 (retour GUI)
- Perte de connexion avec le session manager

**Commandes cles :**
```bash
# Basculer vers TTY3
sudo chvt 3

# Retour vers GUI (TTY1)
sudo chvt 1

# Capture diagnostic complete
{
  echo "=== CPU ==="
  top -bn1 | head -20
  echo "=== RAM ==="
  free -h
  echo "=== GPU ==="
  nvidia-smi 2>/dev/null || echo "GPU inaccessible"
  echo "=== Services ==="
  systemctl list-units --failed
  echo "=== Logs recents ==="
  journalctl --since "10 min ago" -p err --no-pager | tail -50
} > /tmp/jarvis-diagnostic-$(date +%s).txt

# Envoi au cluster IA
curl -X POST http://localhost:3000/api/diagnostic -d @/tmp/jarvis-diagnostic-*.txt
```

**Chaines domino liees :**
- `system-stabilization-mode` — stabilisation depuis TTY3
- `disaster-recovery` (P10) — si le diagnostic revele une catastrophe

---

## 9. network-degradation

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Claude |
| **Priorite** | P8 — Haute |

**Description detaillee :**
Gestion des degradations reseau : downshift automatique de 1Gbps a 100Mbps, perte de lien (Link Down), et deconnexion de noeuds du cluster. Detecte les anomalies via ethtool et tente une renegociation forcee avant de passer en mode degrade. Surveille la connectivite avec les autres machines du cluster JARVIS et bascule les charges si un noeud devient injoignable.

**Conditions d'auto-trigger :**
- Vitesse lien < 1000Mbps detectee par ethtool
- Interface reseau en etat DOWN
- Ping vers noeud cluster echoue (3 tentatives)
- Augmentation latence > 100ms vers le cluster
- Perte de paquets > 5%

**Commandes cles :**
```bash
# Diagnostic vitesse
ethtool enp6s0 | grep -E "Speed|Link detected"

# Forcer renegociation 1Gbps
sudo ethtool -s enp6s0 speed 1000 duplex full autoneg on

# Verifier etat interface
ip link show enp6s0

# Recharger driver r8169
sudo modprobe -r r8169 && sudo modprobe r8169

# Ping cluster
ping -c 3 -W 2 192.168.1.10  # M2
ping -c 3 -W 2 192.168.1.11  # M3

# Verifier connectivite services
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/health
```

**Chaines domino liees :**
- `network-degradation-cascade` (P8) — chaine complete de recuperation reseau
- `service-crash-recovery` (P10) — si des services tombent a cause du reseau
