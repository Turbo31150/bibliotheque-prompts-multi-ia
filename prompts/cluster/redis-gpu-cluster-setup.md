# Cluster GPU Multi-Machine avec Redis

> 🔴 Rouge — Infra, cluster, GPU, Redis  
> Source: Perplexity AI (mars 2026)

```text
5 étapes pour configurer un cluster GPU multi-machine avec Redis:

1. PRÉPARER L'INFRA: Homogénéiser drivers NVIDIA, CUDA, nvidia-container-toolkit sur chaque nœud. Réseau 10Gbps entre machines.

2. INSTALLER REDIS COMME BUS: Redis master sur M1, replica sur M2. Queues prioritaires (critical/high/medium/low). AOF persistence.

3. CRÉER LES WORKERS GPU: Un worker Python par machine qui pop les tâches Redis, charge le modèle sur GPU disponible, exécute l'inférence.

4. LOAD BALANCING: Router les tâches selon VRAM disponible. Gros modèles → GPU avec plus de VRAM. Monitoring nvidia-smi en continu.

5. FAILOVER + MONITORING: Health check toutes les 30s. Si worker down → redistribuer ses tâches. Dead letter queue pour les échecs. Dashboard temps réel.

COMMANDES CLÉS:
- redis-cli LPUSH jarvis:queue:high '{"task":"..."}'
- nvidia-smi --query-gpu=memory.free --format=csv
- docker run --gpus all --runtime=nvidia worker
```
