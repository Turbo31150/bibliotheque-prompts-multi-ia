# Codex OpenAI — Linux Performance

> Prompts pour l'optimisation de performance Linux avec Codex CLI.

---

## Prompt d'analyse de performance

```
Analyse les performances de cette machine Linux et propose des optimisations.

## Collecte de donnees
Execute et analyse :
1. top -bn1 (charge CPU et processes gourmands)
2. free -h (utilisation memoire)
3. iostat -x 1 3 (performance disque I/O)
4. nvidia-smi --query-gpu=utilization.gpu,temperature.gpu,memory.used --format=csv (GPU)
5. ss -s (statistiques reseau)
6. vmstat 1 5 (virtual memory stats)
7. sar -u 1 5 (CPU history si sysstat installe)

## Analyse
Pour chaque ressource (CPU, RAM, Disk, GPU, Network) :
- Utilisation actuelle vs capacite
- Bottleneck identifie : OUI/NON
- Processes les plus gourmands
- Tendance : stable / en hausse / en baisse

## Optimisations
Propose des optimisations classees par impact :

### Quick wins (< 5 min, impact immediat)
- [Liste]

### Moyen terme (< 1h, impact significatif)
- [Liste]

### Long terme (> 1h, impact structurel)
- [Liste]

Pour chaque optimisation :
- Commande exacte a executer
- Gain estime (%, ms, MB)
- Risque (SAFE / LOW / MEDIUM / HIGH)
```

### Ce que ca fait
Diagnostic complet de performance avec plan d'action priorise. Codex est efficace pour les commandes systeme et l'analyse de sortie.

### Effet sur le modele
- Le format "collecte + analyse + optimisation" structure la reflexion
- La classification quick wins / moyen / long terme rend le plan actionnable
- L'estimation de gain et de risque permet de decider rapidement

---

## Prompt d'optimisation GPU

```
Optimise l'utilisation GPU pour un cluster IA avec 6 GPUs.

Configuration actuelle :
- 6 GPUs (nvidia-smi pour les details)
- LM Studio sur GPU 0-1
- Ollama sur GPU 2-3
- Docker containers sur GPU 4-5

Objectifs :
1. Temperature < 75C en permanence
2. Utilisation > 60% sur chaque GPU actif
3. VRAM : pas de swap memoire
4. Latence inference < 100ms pour les modeles charges

Analyse et propose :
- Repartition optimale des modeles par GPU
- Configuration CUDA_VISIBLE_DEVICES
- Parametres de ventilation (nvidia-settings)
- Strategies de decharge quand GPU > 75C
- Script de monitoring continu
```

---

## Prompt d'optimisation Python

```
Optimise les performances de ce script Python :

[COLLER LE CODE]

Techniques a considerer :
1. Profilage (cProfile, line_profiler)
2. Asyncio pour les I/O
3. Multiprocessing pour le CPU-bound
4. Caching (functools.lru_cache, redis)
5. Comprehensions vs boucles
6. Generators vs listes
7. numpy/pandas pour les calculs numeriques
8. Connection pooling pour les requetes HTTP/DB

Pour chaque optimisation :
- Montre le code avant/apres
- Mesure le gain (benchmark)
- Note les tradeoffs (memoire vs vitesse, complexite vs performance)
```

---

## Prerequis
- Codex CLI installe
- Acces root/sudo pour les commandes systeme
- nvidia-smi pour les optimisations GPU
- sysstat installe pour sar
