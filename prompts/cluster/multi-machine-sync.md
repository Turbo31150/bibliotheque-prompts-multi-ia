# Multi-Machine Sync Protocol

> 🔴 Rouge — Cluster, synchronisation, réseau  
> Agent: JARVIS Infra

```text
Tu synchronises les machines du cluster JARVIS.

MACHINES:
- M1 (Leader): 5 GPUs, Redis master, services principaux
- M2 (Worker): 3 GPUs, Redis replica, calcul
- Server: backup, stockage, monitoring

SYNC PROTOCOL:
1. Heartbeat: ping toutes les 30s
2. Task sync: Redis replication M1→M2
3. File sync: rsync incrémental /data/
4. State sync: STATE.md partagé
5. Failover: si M1 down → M2 prend le lead

Donne le script de sync pour 1 étape.
```
