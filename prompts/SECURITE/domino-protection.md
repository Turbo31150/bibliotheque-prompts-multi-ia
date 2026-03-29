# Chaines Domino de Protection

> **JARVIS Linux** — 10 chaines domino de securite et stabilite
> Derniere mise a jour : 2026-03-28

---

## 1. pre-incident-backup

| Champ | Valeur |
|-------|--------|
| **Priorite** | P9 — Tres haute |
| **Evenement declencheur** | Reparation systeme imminente |
| **Condition** | Tout skill de reparation active (crash recovery, GPU reset, stabilization) |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | timeshift-backup | Claude | Creer snapshot avec tag "pre-incident-YYYYMMDD-HHMM" | 120s |
| 2 | timeshift-backup | Claude | Verifier que le snapshot apparait dans `timeshift --list` | 10s |
| 3 | system-crash-guardian | Claude | Logger l'etat systeme avant intervention (CPU, RAM, services) | 5s |
| 4 | — | Claude | Notifier le skill appelant que le backup est pret | 2s |

**Metriques benchmark :**
- Temps de creation snapshot : < 90s (cible), < 120s (acceptable)
- Taux de succes creation : > 99%
- Espace disque utilise par snapshot : < 2GB moyen
- Nombre de snapshots pre-incident/semaine : suivi tendance

---

## 2. post-update-backup

| Champ | Valeur |
|-------|--------|
| **Priorite** | P6 — Moyenne-haute |
| **Evenement declencheur** | Mise a jour systeme terminee |
| **Condition** | `apt upgrade` complete OU driver NVIDIA mis a jour OU kernel update |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | — | Claude | Attendre fin complete de l'update (dpkg lock libere) | 300s |
| 2 | system-crash-guardian | Claude | Verifier stabilite post-update (services OK, pas de crash) | 30s |
| 3 | timeshift-backup | Claude | Creer snapshot avec tag "post-update-YYYYMMDD" | 120s |
| 4 | timeshift-backup | Claude | Verifier integrite du snapshot | 10s |
| 5 | — | Claude | Logger les paquets mis a jour dans le rapport | 5s |

**Metriques benchmark :**
- Delai entre fin update et snapshot : < 60s
- Taux de succes : > 98%
- Frequence : ~2-3 fois/semaine (selon rythme updates)
- Correlation avec incidents post-update : suivi

---

## 3. backup-rotation-check

| Champ | Valeur |
|-------|--------|
| **Priorite** | P3 — Basse |
| **Evenement declencheur** | Cron quotidien |
| **Condition** | Tous les jours a 4h00 du matin |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | timeshift-backup | Claude | Lister tous les snapshots existants | 10s |
| 2 | timeshift-backup | Claude | Identifier les snapshots > 7 jours (sauf weekly) | 5s |
| 3 | timeshift-backup | Claude | Supprimer les snapshots expires | 60s |
| 4 | — | Claude | Verifier espace disque libre > 20% | 5s |
| 5 | — | Claude | Logger le rapport de rotation | 2s |

**Metriques benchmark :**
- Nombre de snapshots apres rotation : 5-10 (cible)
- Espace disque libere par rotation : suivi en GB
- Espace disque disponible apres rotation : > 20%
- Temps total de rotation : < 120s

---

## 4. disaster-recovery

| Champ | Valeur |
|-------|--------|
| **Priorite** | P10 — Critique |
| **Evenement declencheur** | Echec de toutes les tentatives de reparation |
| **Condition** | 3+ skills de reparation echoues OU corruption systeme detectee OU filesystem errors |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | rescue-mode-switcher | Claude | Basculer en TTY3 si GUI instable | 10s |
| 2 | — | Claude | Capturer diagnostic complet du systeme | 30s |
| 3 | timeshift-backup | Claude | Lister les snapshots disponibles | 10s |
| 4 | — | Claude | Identifier le dernier snapshot sain (avant l'incident) | 5s |
| 5 | — | Claude | **DEMANDER CONFIRMATION A TURBO** avant restauration | — |
| 6 | timeshift-backup | Claude | Restaurer le snapshot selectionne | 600s |
| 7 | boot-sequencer | Claude | Redemarrer la sequence de boot complete | 120s |
| 8 | system-crash-guardian | Claude | Verifier stabilite post-restauration pendant 5 min | 300s |

**Metriques benchmark :**
- Temps total de restauration : < 10 min (cible)
- Taux de succes restauration : > 95%
- Perte de donnees : 0 (grace aux snapshots frequents)
- Nombre de disaster recovery/mois : suivi (cible < 1)

---

## 5. backup-integrity-verify

| Champ | Valeur |
|-------|--------|
| **Priorite** | P4 — Moyenne-basse |
| **Evenement declencheur** | Cron hebdomadaire |
| **Condition** | Dimanche a 5h00 du matin |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | timeshift-backup | Claude | Lister tous les snapshots | 10s |
| 2 | timeshift-backup | Claude | Verifier la presence des fichiers de chaque snapshot | 60s |
| 3 | — | Claude | Verifier la coherence des metadonnees (dates, tailles) | 30s |
| 4 | — | Claude | Tester un dry-run de restauration du dernier snapshot | 120s |
| 5 | — | Claude | Logger le rapport d'integrite | 5s |
| 6 | — | Claude | Alerter si un snapshot est corrompu | 2s |

**Metriques benchmark :**
- Nombre de snapshots verifies/semaine : tous
- Taux d'integrite : > 99.9%
- Temps de verification : < 5 min
- Snapshots corrompus detectes : suivi (cible = 0)

---

## 6. service-crash-recovery

| Champ | Valeur |
|-------|--------|
| **Priorite** | P10 — Critique |
| **Evenement declencheur** | Service JARVIS en echec |
| **Condition** | `systemctl is-failed SERVICE` = true OU crash loop detecte (3+ restarts/60s) |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | timeshift-backup | Claude | Snapshot pre-incident (via chaine pre-incident-backup) | 120s |
| 2 | system-crash-guardian | Claude | Analyser les logs du service crashe (`journalctl -u`) | 10s |
| 3 | system-crash-guardian | Claude | Identifier la cause racine (OOM, segfault, config, dep) | 15s |
| 4 | system-stabilization-mode | Claude | Reparer : restart, reload config, fix dependances | 30s |
| 5 | — | Claude | Verifier que le service est stable pendant 30s | 30s |
| 6 | — | Claude | Notifier Turbo du diagnostic et de la resolution via TTS | 5s |

**Metriques benchmark :**
- Temps moyen de recuperation (MTTR) : < 45s (cible)
- Taux de succes auto-repair : > 90%
- Nombre de crash/service/semaine : suivi tendance
- Escalades vers Turbo : < 10% des incidents

---

## 7. gpu-error-cascade

| Champ | Valeur |
|-------|--------|
| **Priorite** | P10 — Critique |
| **Evenement declencheur** | Erreur GPU detectee |
| **Condition** | `nvidia-smi` echoue OU temperature > 85C OU VRAM leak OU erreur CUDA kernel |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | timeshift-backup | Claude | Snapshot pre-incident | 120s |
| 2 | gpu-crash-recovery | Claude | Niveau 1 : soft reset (`rmmod nvidia_uvm`) | 15s |
| 3 | gpu-crash-recovery | Claude | Si echec → Niveau 2 : PCIe reset | 15s |
| 4 | gpu-crash-recovery | Claude | Si echec → Niveau 3 : reload module complet | 30s |
| 5 | system-stabilization-mode | Claude | Stabiliser les services dependants du GPU | 30s |
| 6 | — | Claude | Monitoring GPU pendant 60s pour confirmer stabilite | 60s |
| 7 | boot-sequencer | Claude | Si reboot necessaire (Niveau 4) → boot-wave complete | 120s |

**Metriques benchmark :**
- Taux de resolution Niveau 1 : > 70%
- Taux de resolution Niveau 2 : > 85% (cumule)
- Taux de resolution Niveau 3 : > 95% (cumule)
- Reboots necessaires (Niveau 4) : < 5% des incidents
- Temps moyen de recuperation GPU : < 30s

---

## 8. ram-pressure-cascade

| Champ | Valeur |
|-------|--------|
| **Priorite** | P10 — Critique |
| **Evenement declencheur** | Pression memoire elevee |
| **Condition** | RAM > 80% OU MemAvailable < 4GB OU OOM kill detecte |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | ram-pressure-handler | Claude | Verifier etat RAM/swap (`free -h`, `/proc/meminfo`) | 5s |
| 2 | ram-pressure-handler | Claude | Niveau 1 : drop caches (`echo 3 > drop_caches`) | 5s |
| 3 | zombie-cleanup | Claude | Nettoyer les zombies (SIGCHLD, orphan reap) | 15s |
| 4 | ram-pressure-handler | Claude | Niveau 2 : identifier le top consommateur RAM | 5s |
| 5 | ram-pressure-handler | Claude | Niveau 3 : stop services non essentiels si toujours > 80% | 15s |
| 6 | ram-pressure-handler | Claude | Niveau 4 : OOM protect sur services critiques | 5s |
| 7 | — | Claude | Monitoring RAM pendant 60s pour confirmer desescalade | 60s |

**Metriques benchmark :**
- Taux de resolution Niveau 1 (drop caches) : > 40%
- Taux de resolution sans arret service : > 60%
- Temps de retour sous 70% RAM : < 30s (cible)
- OOM kills evites : suivi (cible = tous)
- RAM moyenne apres intervention : < 65%

---

## 9. full-boot-sequence

| Champ | Valeur |
|-------|--------|
| **Priorite** | P10 — Critique |
| **Evenement declencheur** | Demarrage ou redemarrage systeme |
| **Condition** | Login utilisateur OU post-reboot OU post-restauration Timeshift |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | boot-sequencer | Claude | Vague 1 : Redis (infrastructure data) | 7s |
| 2 | boot-sequencer | Claude | Vague 2 : Ollama (moteur IA principal) | 7s |
| 3 | boot-sequencer | Claude | Vague 3 : Moniteur systeme | 7s |
| 4 | boot-sequencer | Claude | Vague 4 : Services IA (LM Studio, agents) | 7s |
| 5 | boot-sequencer | Claude | Vague 5 : n8n (workflows automatisation) | 7s |
| 6 | boot-sequencer | Claude | Vague 6 : Chrome (navigateur + CDP) | 7s |
| 7 | boot-sequencer | Claude | Vague 7 : Social (LinkedIn, GitHub) | 7s |
| 8 | boot-sequencer | Claude | Vague 8 : Voice (TTS Piper + STT Whisper) | 7s |
| 9 | system-crash-guardian | Claude | Health check global de tous les services | 15s |
| 10 | — | Claude | Orchestrateur JARVIS pret — notification vocale | 5s |
| 11 | — | Claude | Annonce TTS : "JARVIS operationnel" | 3s |

**Metriques benchmark :**
- Temps total de boot : < 90s (cible, 8x7s + health)
- Services demarres avec succes : 100% (cible)
- Services en echec au boot : suivi (cible = 0)
- Temps par vague : < 7s chacune
- Delai entre login et "JARVIS operationnel" : < 120s

---

## 10. network-degradation-cascade

| Champ | Valeur |
|-------|--------|
| **Priorite** | P8 — Haute |
| **Evenement declencheur** | Anomalie reseau detectee |
| **Condition** | Vitesse < 1000Mbps OU Link Down OU ping cluster echoue 3x |

**Sequence des etapes :**

| # | Skill | Plateforme | Action | Timeout |
|---|-------|-----------|--------|---------|
| 1 | network-degradation | Claude | Detecter le type de degradation (downshift, link down, timeout) | 10s |
| 2 | network-degradation | Claude | Forcer renegociation 1Gbps (`ethtool -s speed 1000`) | 10s |
| 3 | network-degradation | Claude | Si echec → recharger driver r8169 (`modprobe -r && modprobe`) | 15s |
| 4 | network-degradation | Claude | Si echec → mode fallback (fonctionner en 100Mbps) | 5s |
| 5 | — | Claude | Verifier connectivite cluster (ping noeuds) | 15s |
| 6 | — | Claude | Ajuster les services reseau-dependants si degrade | 10s |
| 7 | — | Claude | Notifier Turbo si degradation persistante | 5s |

**Metriques benchmark :**
- Taux de resolution par renegociation : > 80%
- Taux de resolution par reload driver : > 95% (cumule)
- Temps de retour a 1Gbps : < 30s
- Temps en mode degrade : suivi (cible < 5 min)
- Nombre d'incidents reseau/semaine : suivi tendance
