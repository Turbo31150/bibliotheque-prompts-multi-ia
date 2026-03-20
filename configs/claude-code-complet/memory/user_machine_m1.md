---
name: M1 La Créatrice - Hardware specs
description: Machine principale JARVIS - Ryzen 7 5700X3D, 6 GPUs NVIDIA, 46GB RAM, Ubuntu 22.04
type: user
---

## M1 "La Créatrice"
- CPU: AMD Ryzen 7 5700X3D (8C/16T, AM4)
- Carte mère: MSI B550, watercooling MSI 3 ventilateurs
- RAM: 46 Go DDR4
- GPUs: 4x GTX 1660 Super, 1x RTX 2060 12Go, 1x RTX 3080 10Go
- OS: Ubuntu 22.04 LTS
- Rôle: machine principale JARVIS Turmont (cluster IA, coding, orchestration)

## Cluster
- M1 (Créatrice) → M2 (LM Studio LMT2) → Server (3x Quadro 45GB RAM)
- Services: vcluster, openclaw, wisperflow, comet, crypto MEXC

## Flask MCP
- Port 8080, auth Bearer 1202
- Tools: root_read, root_write, root_ls, range_bureau, gpu_scale, run_wave, crypto_trade
