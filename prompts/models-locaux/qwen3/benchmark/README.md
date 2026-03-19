# Qwen3 -- Benchmark

## Description

Benchmarks pour evaluer les modeles Qwen3 en local : performance, qualite multilingue et comparaison.

## Benchmarks

### 1 -- Benchmark comparatif

```bash
PROMPT="Cree un script Python async qui collecte les metriques de 5 serveurs en parallele"
for model in qwen3:8b llama3.1:8b gemma2:9b deepseek-r1:7b; do
    echo "=== $model ==="
    time ollama run $model "$PROMPT" > /tmp/bench_${model}.txt
    wc -w /tmp/bench_${model}.txt
done
```

### 2 -- Benchmark multilingue

```
Qwen3 est repute pour le multilinguisme. Tester :
1. Francais : resume technique
2. Anglais : code generation
3. Code : Python, Bash, SQL
4. Mixte : question en francais, code en anglais

Comparer les scores avec Llama et Gemma.
```

### 3 -- Benchmark mode thinking

```
Qwen3 supporte le mode thinking (/think).
Comparer avec et sans :
- Probleme de logique
- Bug a trouver dans du code
- Optimisation d'algorithme
```

### 4 -- Benchmark VRAM

```bash
for model in qwen3:1.7b qwen3:4b qwen3:8b qwen3:32b; do
    echo "=== $model ==="
    ollama run $model "test" &
    sleep 5
    nvidia-smi | grep MiB
    ollama stop $model
done
```

### 5 -- Benchmark outils (tool use)

```
Qwen3 supporte le tool use nativement.
Tester avec l'API Ollama :
- Appel d'outils simples (get_weather, calculate)
- Chaines d'outils (recherche → analyse → action)
- Comparer avec les autres modeles
```

---

## Notes
- Qwen3 offre un bon compromis multilinguisme/performance
- Le mode thinking ameliore le raisonnement complexe
- Le support natif du tool use est un avantage pour les agents
