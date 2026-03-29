# Cluster JARVIS

> Architecture IA distribuée sur 3 machines physiques.
> 6 GPUs NVIDIA, 46 Go RAM, 10+ modèles locaux, auto-réparation et consensus multi-modèle.

---

## Machines

| Machine | Rôle | CPU | GPUs | RAM |
|---|---|---|---|---|
| **M1** « La Créatrice » | Orchestration + inférence | AMD Ryzen 7 5700X3D | 4× GTX 1660S, 1× RTX 2060 12 Go, 1× RTX 3080 10 Go | 46 Go |
| **M2** | Inférence lourde | — | — | — |
| **M3** / Serveur | Inférence + stockage | — | 3× Quadro | 45 Go |

## Composants

| Composant | Guide | Description |
|---|---|---|
| **Dispatch Engine** | [`dispatch-engine/`](dispatch-engine/) | Pipeline intelligent en 9 étapes : cache → health check → auto-load → routage → enrichissement → dispatch → contrôle qualité → feedback → post-traitement. |
| **Consensus** | [`consensus/`](consensus/) | Vote pondéré entre 5 modèles. Poids M1 = 1.8 à M3 = 1.0, seuil de confiance 3+ à 0.7. |
| **Routage** | [`routage/`](routage/) | Matrice 17 domaines × 6 nœuds. Poids sur 5 niveaux : nœud, domaine, latence, température GPU, auto-apprentissage. |
| **Self-Healing** | [`self-healing/`](self-healing/) | Boucle automatique : détection → diagnostic → réparation → vérification. Circuit breaker et backoff exponentiel. |
| **GPU Management** | [`gpu-management/`](gpu-management/) | 6 GPUs supervisés. Garde thermique : alerte 75 °C, critique 85 °C. Allocation VRAM dynamique et mode persistance. |
| **Backup** | [`backup/`](backup/) | 103 bases SQLite sauvegardées. Git bundle, synchronisation HDD, notification Telegram. Planifié à 03h00 quotidien. |
