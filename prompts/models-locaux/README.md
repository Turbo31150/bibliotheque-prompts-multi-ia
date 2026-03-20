# Modèles locaux

> Cinq familles de modèles IA tournant en local sur GPU.
> Configuration, benchmarks, inférence et fine-tuning documentés.

---

## Modèles disponibles

| Modèle | Outil | VRAM | Vitesse | Qualité | Usage principal |
|---|---|---|---|---|---|
| **Qwen3-8b** | LM Studio | 6 Go | 65 tok/s | 98,4/100 | Champion généraliste. Préfixe `/nothink` obligatoire sur M1. |
| **Qwen3-coder-30b** | LM Studio | 12 Go | 25 tok/s | Excellent | Code et refactoring avancé. |
| **DeepSeek-R1 (7b)** | Ollama | 8 Go | 40 tok/s | Très bon | Raisonnement avancé. `max_output_tokens >= 2048` obligatoire. |
| **Gemma-3-4b** | Google | 4 Go | 80 tok/s | Bon | Classification et tri rapide. |
| **GPT-OSS-20b** | LM Studio | 12 Go | 15 tok/s | Bon | Généraliste open-source. |

## Guides par modèle

| Modèle | Configuration | Inférence | Benchmark | Fine-tuning |
|---|---|---|---|---|
| **Qwen3** | [`qwen3/configuration/`](qwen3/configuration/) | [`qwen3/inference/`](qwen3/inference/) | [`qwen3/benchmark/`](qwen3/benchmark/) | [`qwen3/fine-tuning/`](qwen3/fine-tuning/) |
| **DeepSeek-R1** | [`deepseek-r1/configuration/`](deepseek-r1/configuration/) | [`deepseek-r1/inference/`](deepseek-r1/inference/) | [`deepseek-r1/benchmark/`](deepseek-r1/benchmark/) | [`deepseek-r1/fine-tuning/`](deepseek-r1/fine-tuning/) |
| **Gemma** | [`gemma/configuration/`](gemma/configuration/) | [`gemma/inference/`](gemma/inference/) | [`gemma/benchmark/`](gemma/benchmark/) | [`gemma/fine-tuning/`](gemma/fine-tuning/) |
| **LM Studio** | [`lm-studio/configuration/`](lm-studio/configuration/) | [`lm-studio/inference/`](lm-studio/inference/) | [`lm-studio/benchmark/`](lm-studio/benchmark/) | [`lm-studio/fine-tuning/`](lm-studio/fine-tuning/) |
| **Ollama** | [`ollama/configuration/`](ollama/configuration/) | [`ollama/inference/`](ollama/inference/) | [`ollama/benchmark/`](ollama/benchmark/) | [`ollama/fine-tuning/`](ollama/fine-tuning/) |

## Contraintes à respecter

- **Ollama cloud** : `think:false` obligatoire.
- **Qwen3 sur M1** : préfixe `/nothink` obligatoire.
- **M2/M3** : `max_output_tokens >= 2048` sinon réponses tronquées.
- **GPU** : alerte à 75 °C, critique à 85 °C → re-routage automatique.
