# Catalogue des Chaines Domino JARVIS

> Derniere mise a jour : 2026-03-28
> Total : 15 chaines actives + 47 fichiers trace (.chain)

---

## Les 15 Chaines Actives

| Chaine | Priorite | Trigger | Steps |
|--------|----------|---------|-------|
| service-crash-recovery | P10 | crash > systemd-journal | flow-controller > timeshift-backup > crash-guardian > service-auto-repair > production-monitor > telegram-ops |
| gpu-error-cascade | P10 | error > dmesg NVRM/Xid | timeshift-backup > gpu-crash-recovery > system-stabilization > production-monitor > boot-sequencer |
| disaster-recovery | P10 | boot_failed / multi_service >5 | flow-controller > crash-guardian > production-monitor > timeshift-backup (propose restore) > flow-controller (alert TTS) |
| full-boot-sequence | P10 | systemd-boot / manual | boot-sequencer (8 waves) > production-monitor > jarvis-orchestrator > voice-first-operator |
| ram-pressure-cascade | P10 | threshold > RAM >85% | check > drop_caches > kill_zombies > stop_nonessential > reduce_parallelism > stabilize > verify |
| pre-incident-backup | P9 | crash/error critical | flow-controller > timeshift-backup > crash-guardian |
| network-degradation-cascade | P8 | error > network | detect > force_reneg > reload_interface > cluster_fallback |
| post-update-backup | P6 | signal > apt-hook | production-monitor > timeshift-backup > verify > log |
| code-error-debug | P5 | error > code | capture > analyze > fix > validate > learn |
| browser-session-repair | P5 | crash > chrome | detect > restore > verify_cdp |
| backup-integrity-verify | P4 | cron dimanche 5h | list > check_age > verify_files > report > emergency |
| benchmark-self-improve | P4 | cron 3h / rate <70% | sql-memory-reader > validation-consensus > production-improver > auto-learn |
| content-pipeline | P4 | cron daily | generate > format > linkedin-operator > track |
| freelance-pipeline | P4 | cron weekday 10h | scan > codeur-operator > proposal > track |
| backup-rotation-check | P3 | cron 4h / disk >85% | list > check_retention > cleanup > verify > log |

---

## 47 Fichiers Trace (.chain)

Repertoire : `~/Workspaces/jarvis-linux/domino-chains/`

Chaque fichier `.chain` contient la sequence d'execution sous forme `step1:step2:step3:...`

### Crash & Recovery

| Fichier | Sequence |
|---------|----------|
| `health_check_full.chain` | check_cpu:check_ram:check_gpu:check_network:check_watchdog:verify |
| `post_incident_check.chain` | check_cpu:check_ram:check_gpu:kill_zombies:stabilize:verify:notify |
| `oom_recovery.chain` | check_ram:drop_caches:kill_zombies:stop_nonessential:reduce_parallelism:stabilize:verify |
| `cascade_failure.chain` | restart_service:check_logs:kill_zombies:restart_service:stabilize:verify:notify |
| `multi_service_fail.chain` | stop_nonessential:kill_zombies:drop_caches:boot_sequencer:verify:notify |
| `hardware_error_flood.chain` | check_gpu:check_cpu:check_ram:stabilize:verify:notify |
| `progressive_degradation.chain` | check_cpu:check_ram:reduce_parallelism:route_cluster:stabilize:verify |

### Backup & Restore

| Fichier | Sequence |
|---------|----------|
| `pre_incident_backup.chain` | check_disk_space:create_timeshift_snapshot:log_snapshot_result:proceed_repair |
| `post_update_backup.chain` | verify_services:check_gpu:check_dmesg:create_timeshift_snapshot:verify_snapshot:log_report |
| `backup_rotation.chain` | list_snapshots:check_retention_policy:check_disk_space:cleanup_old_snapshots:verify_remaining:log_report |
| `disaster_recovery.chain` | emergency_triage:attempt_graduated_repair:verify_repair:list_timeshift_snapshots:recommend_restore:alert_turbo_tts |
| `backup_integrity.chain` | list_snapshots:check_age_policy:verify_critical_files:check_rsync_logs:generate_report:emergency_snapshot_if_needed |

### GPU

| Fichier | Sequence |
|---------|----------|
| `gpu_mass_failure.chain` | check_gpu:reset_gpu:restart_persistenced:verify_smi:check_gpu:degrade_mode:route_cluster:notify |
| `gpu_thermal.chain` | check_gpu:reduce_parallelism:stop_nonessential:stabilize:verify |
| `gpu_pcie_reset_fail.chain` | check_gpu:restart_persistenced:verify_smi:reduce_parallelism:route_cluster:stabilize:verify:notify |
| `gpu_cuda_poisoned.chain` | check_gpu:count_working_gpus:set_cuda_visible_devices:restart_nvidia_persistenced:reload_nvidia_uvm:verify_cuda:notify |
| `all_gpu_saturated.chain` | check_gpu:reduce_parallelism:route_cluster:stop_nonessential:stabilize:verify |
| `nvidia_lib_mismatch.chain` | reinstall_libs:restart_persistenced:verify_smi:notify |
| `vram_leak.chain` | check_gpu:restart_service:check_gpu:stabilize:verify |

### Reseau & Cluster

| Fichier | Sequence |
|---------|----------|
| `network_flapping.chain` | check_network:fallback_local:check_network:renegotiate:verify:notify |
| `cluster_node_lost.chain` | check_network:fallback_local:reduce_parallelism:route_cluster:notify |
| `m2_unreachable.chain` | check_network:fallback_local:route_cluster:notify |
| `websocket_down.chain` | restart_service:check_network:verify:notify |
| `websocket_overflow.chain` | check_logs:restart_service:verify:notify |
| `telegram_disconnected.chain` | restart_service:check_network:verify:notify |

### Services & Applications

| Fichier | Sequence |
|---------|----------|
| `redis_down.chain` | restart_service:check_logs:stop_nonessential:boot_sequencer:verify |
| `services_no_redis.chain` | stop_nonessential:restart_service:check_logs:boot_sequencer:verify |
| `docker_crash.chain` | check_logs:restart_service:check_logs:diagnose:notify |
| `ollama_hang.chain` | check_logs:restart_service:verify:notify |
| `lmstudio_crash.chain` | restart_service:check_gpu:verify:notify |
| `lmstudio_cpu_fallback.chain` | check_gpu:verify_cuda:kill_lmstudio_workers:set_cuda_visible:restart_lms_daemon:load_model_gpu:verify_vram:stabilize |
| `n8n_stuck.chain` | restart_service:check_logs:verify:notify |
| `chrome_cdp_lost.chain` | restart_service:check_logs:verify:notify |
| `cowork_stuck.chain` | restart_service:check_logs:kill_zombies:verify:notify |
| `audio_crash.chain` | restart_service:check_logs:verify:notify |

### Systeme & Boot

| Fichier | Sequence |
|---------|----------|
| `cold_start_check.chain` | check_cpu:check_ram:check_gpu:check_network:verify:notify |
| `partial_boot.chain` | check_logs:restart_service:repair_deps:stabilize:verify:notify |
| `full_diagnostic.chain` | check_cpu:check_ram:check_gpu:check_network:stabilize:verify:notify |
| `gnome_a11y_loop.chain` | kill_gnome:disable_accessibility:kill_zombies:stop_orphans:repair_deps:boot_sequencer:verify |
| `systemd_user_unstable.chain` | kill_zombies:restart_service:check_logs:stabilize:verify |
| `permission_error.chain` | check_logs:repair_deps:restart_service:verify |
| `venv_corrupted.chain` | check_logs:repair_deps:restart_service:verify:notify |

### Memoire & Disque

| Fichier | Sequence |
|---------|----------|
| `swap_filling.chain` | check_ram:drop_caches:stop_nonessential:reduce_parallelism:stabilize |
| `disk_io_saturated.chain` | check_logs:drop_caches:stop_nonessential:stabilize:notify |
| `journal_disk_full.chain` | drop_caches:check_logs:stabilize:verify |

### Inference & Routage

| Fichier | Sequence |
|---------|----------|
| `inference_overload.chain` | check_gpu:reduce_parallelism:route_cluster:restart_service:verify:notify |
| `linkedin_spam.chain` | stop_nonessential:check_logs:restart_service:verify |

---

## Auto-Triggers (13 actifs)

| Chaine | Condition | Cooldown |
|--------|-----------|----------|
| service-crash-recovery | systemctl failed detecte | 30s |
| gpu-error-cascade | nvidia-smi erreur ou dmesg NVRM/Xid | 60s |
| ram-pressure-cascade | RAM > 85% | 30s |
| full-boot-sequence | boot systeme ou manual | N/A |
| disaster-recovery | boot_failed ou multi_service >5 | 0s (immediat) |
| pre-incident-backup | crash/error critique detecte | 60s |
| network-degradation-cascade | latence > 500ms pendant 10s | 120s |
| post-update-backup | signal apt-hook | 86400s (24h) |
| backup-integrity-verify | cron dimanche 5h | 604800s (7j) |
| benchmark-self-improve | cron 3h ou rate <70% | 10800s (3h) |
| content-pipeline | cron daily | 86400s (24h) |
| freelance-pipeline | cron weekday 10h | 86400s (24h) |
| backup-rotation-check | cron 4h ou disk >85% | 14400s (4h) |

---

## Statistiques Globales

| Metrique | Valeur |
|----------|--------|
| Chaines actives | 15 |
| Fichiers trace (.chain) | 47 |
| Benchmarks cumules | 877+ |
| Taux de succes global | 95.5% |
| Auto-triggers actifs | 13 |
| Chaine la plus rapide | llm-routing (890ms) |
| Chaine la plus lente | backup-restore (45600ms) |
