# LM Studio — Benchmark

## Methodologie

Chaque modele est evalue sur 3 axes :

1. **Latence** : temps avant le premier token (TTFT)
2. **Debit** : tokens par seconde (tok/s)
3. **Qualite** : score sur un jeu de 20 questions techniques (0-100)

## Tableau Comparatif

| Modele | TTFT (ms) | tok/s | Qualite (/100) | VRAM (GB) |
|--------|-----------|-------|-----------------|-----------|
| `qwen3.5-9b` | ~200 | 55-65 | 92 | 6.5 |
| `qwen3-coder-30b` | ~800 | 18-25 | 96 (code) | 20 |
| `qwen3.5-35b-a3b` | ~400 | 35-45 | 95 | 12 (MoE) |
| `gpt-oss-20b` | ~500 | 25-35 | 88 | 14 |
| `deepseek-r1` | ~1200 | 12-18 | 97 (reasoning) | 22 |
| `gemma-3-4b` | ~100 | 80-100 | 78 | 3 |
| `text-embedding-nomic` | ~50 | N/A | N/A | 0.5 |

## Comment Reproduire

```bash
# Mesurer le debit
time curl -s http://192.168.1.20:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5-9b",
    "messages": [{"role": "user", "content": "/nothink Explique les design patterns SOLID en detail"}],
    "max_tokens": 512
  }' | jq '.usage'
```

## Notes

- Les valeurs varient selon la charge GPU et le nombre de modeles charges simultanement
- Le MoE (qwen3.5-35b-a3b) utilise moins de VRAM que sa taille le suggere
- DeepSeek-R1 est plus lent mais produit des raisonnements de qualite superieure
- gemma-3-4b est le meilleur choix pour les taches rapides de classification
