# Multi-IA — Benchmark Comparatif des Modèles

## Prompt
```text
Act as a model benchmarking specialist for JARVIS cluster.

MODELS TO BENCHMARK:
| Model | Engine | VRAM | Speed |
|-------|--------|------|-------|
| qwen3-8b | LM Studio | 6GB | 65 tok/s |
| deepseek-r1:7b | Ollama | 8GB | 40 tok/s |
| gemma-3-4b | LM Studio | 4GB | 80 tok/s |
| qwen2.5:1.5b | Ollama | 2GB | 120 tok/s |

BENCHMARK TASKS:
1. Code generation (Python, Bash)
2. Text summarization (French)
3. Classification (color routing)
4. Translation (EN→FR)
5. Reasoning (multi-step problems)
6. Creative writing (LinkedIn posts)

METRICS:
- Latency (first token, total)
- Quality score (0-10, human evaluation)
- VRAM consumption during inference
- Tokens per second
- Error rate

OUTPUT: Comparative table with rankings per task.
Respond in French.
```
