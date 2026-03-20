# Cluster — GPU Management

## Inventaire GPU

Le cluster JARVIS dispose de 5 GPUs repartis sur les noeuds :

| GPU | Noeud | VRAM | Usage principal |
|-----|-------|------|-----------------|
| GPU 0 | M1 | Variable | qwen3-8b, gemma-3-4b |
| GPU 1 | M1 | Variable | qwen3-coder-30b (split) |
| GPU 2 | M1 | Variable | qwen3-coder-30b (split) |
| GPU 3 | M1 | Variable | qwen3.5-35b-a3b MoE |
| GPU 4 | M2 | Variable | DeepSeek-R1 |

## Garde Thermique

### Seuils

| Niveau | Temperature | Action |
|--------|-------------|--------|
| Normal | < 75C | Aucune action |
| **Warning** | **75C** | Log + alerte Telegram |
| **Critique** | **85C** | Throttle GPU + redistribution charge |
| Urgence | > 90C | Decharger tous les modeles, cooldown |

### Script de Surveillance

```bash
# Verifier les temperatures
nvidia-smi --query-gpu=index,temperature.gpu,utilization.gpu,memory.used,memory.total \
  --format=csv,noheader

# Exemple de sortie :
# 0, 62, 45 %, 6144 MiB, 8192 MiB
# 1, 71, 88 %, 10240 MiB, 12288 MiB
```

## Allocation VRAM

Regles d'allocation :
- Chaque modele a une allocation VRAM reservee
- Un modele ne peut pas depasser son allocation sans approbation
- Le GPU 0 garde toujours 1 GB libre pour gemma-3-4b (modele de garde)

### Redistribution

Quand un GPU depasse 85C :
1. Identifier le modele le moins sollicite sur ce GPU
2. Le decharger ou le migrer vers un GPU plus froid
3. Attendre que la temperature descende sous 70C
4. Recharger si necessaire

## Mode Persistance

```bash
# Activer le mode persistance (evite le temps de re-init GPU)
sudo nvidia-smi -pm 1

# Verifier
nvidia-smi -q -d PERSISTENCE_MODE
```

Le mode persistance maintient le driver GPU charge en memoire, eliminant le delai d'initialisation (~2-3s) au premier appel.

## Script de Redistribution

```bash
#!/bin/bash
# redistribution-gpu.sh
# Redistribue la charge si un GPU est en surcharge thermique

SEUIL_WARNING=75
SEUIL_CRITIQUE=85

for gpu_id in 0 1 2 3 4; do
    temp=$(nvidia-smi -i $gpu_id --query-gpu=temperature.gpu --format=csv,noheader,nounits)
    if [ "$temp" -ge "$SEUIL_CRITIQUE" ]; then
        echo "[CRITIQUE] GPU $gpu_id a ${temp}C — decharge en cours"
        # Logique de decharge du modele
    elif [ "$temp" -ge "$SEUIL_WARNING" ]; then
        echo "[WARNING] GPU $gpu_id a ${temp}C — surveillance renforcee"
    fi
done
```
