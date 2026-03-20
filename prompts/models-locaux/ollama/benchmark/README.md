# Ollama -- Benchmark

## Description

Scripts et methodologies pour benchmarker les modeles Ollama : latence, throughput, qualite et consommation de ressources.

## Benchmarks prets a executer

### 1 -- Benchmark de latence

```bash
# Mesurer le temps de premiere reponse (TTFT) et le debit de tokens
for model in llama3.1:8b mistral:7b qwen2.5:7b; do
    echo "=== $model ==="
    time ollama run $model "Explique le concept de containerisation en 3 phrases." --verbose
done
```

### 2 -- Benchmark multi-GPU

```bash
# Tester la repartition sur plusieurs GPUs
OLLAMA_NUM_GPU=1 ollama run llama3.1:70b "test" --verbose
OLLAMA_NUM_GPU=2 ollama run llama3.1:70b "test" --verbose
OLLAMA_NUM_GPU=4 ollama run llama3.1:70b "test" --verbose
# Comparer les latences
```

### 3 -- Benchmark qualite (francais)

```
Teste ces 10 prompts en francais et note la qualite (1-5) :
1. Resume ce texte technique : [TEXTE]
2. Traduis en anglais : [PHRASE]
3. Genere du code Python pour [TACHE]
4. Explique [CONCEPT] simplement
5. Analyse ce log d'erreur : [LOG]
```

### 4 -- Benchmark consommation memoire

```bash
# Mesurer la VRAM par modele
for model in llama3.1:8b llama3.1:70b; do
    ollama run $model "test" &
    nvidia-smi --query-gpu=memory.used --format=csv
    ollama stop $model
done
```

### 5 -- Benchmark comparatif

```bash
# Script complet de benchmark
#!/bin/bash
MODELS="llama3.1:8b mistral:7b qwen2.5:7b deepseek-r1:7b"
PROMPT="Ecris une fonction Python qui trie une liste par insertion."
for model in $MODELS; do
    echo "Model: $model"
    start=$(date +%s%N)
    ollama run $model "$PROMPT" > /tmp/bench_$model.txt
    end=$(date +%s%N)
    echo "Time: $(( (end - start) / 1000000 ))ms"
    echo "Tokens: $(wc -w /tmp/bench_$model.txt)"
done
```

---

## Metriques cles
| Metrique | Description | Objectif |
|----------|-------------|----------|
| TTFT | Time to First Token | < 1s |
| Tokens/s | Debit de generation | > 30 t/s |
| VRAM | Memoire GPU utilisee | < VRAM dispo |
| Qualite | Note humaine 1-5 | > 3.5 |
