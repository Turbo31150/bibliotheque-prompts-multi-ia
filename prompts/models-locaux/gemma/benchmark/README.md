# Gemma -- Benchmark

## Description

Benchmarks pour evaluer les modeles Gemma en local : performance, qualite et comparaison avec d'autres modeles.

## Benchmarks

### 1 -- Gemma vs Llama vs Mistral

```bash
PROMPT="Ecris un script bash qui monitore les GPUs NVIDIA et alerte si temp > 80C"
for model in gemma2:9b llama3.1:8b mistral:7b; do
    echo "=== $model ==="
    time ollama run $model "$PROMPT" > /tmp/bench_${model}.txt
    wc -w /tmp/bench_${model}.txt
done
# Comparer : temps, qualite du code, tokens generes
```

### 2 -- Gemma sur des taches en francais

```
Tester Gemma sur 5 taches en francais :
1. Resume de texte technique
2. Generation de code commente en francais
3. Traduction anglais → francais technique
4. Analyse de logs systeme
5. Redaction de documentation

Noter chaque tache sur 5. Comparer avec Llama et Mistral.
```

### 3 -- Benchmark de latence par taille

```bash
# Comparer les tailles de Gemma
for model in gemma2:2b gemma2:9b gemma2:27b; do
    echo "=== $model ==="
    time ollama run $model "Explique Docker en 3 phrases" --verbose
done
```

### 4 -- Benchmark raisonnement

```
Teste le raisonnement de Gemma :
1. Probleme logique simple
2. Debugging de code (trouver le bug)
3. Analyse de configuration (trouver l'erreur)
4. Planification d'une migration (steps)
5. Optimisation d'un algorithme
```

### 5 -- Benchmark memoire et GPU

```bash
# VRAM utilisee par modele Gemma
for model in gemma2:2b gemma2:9b gemma2:27b; do
    ollama run $model "test" &
    sleep 5
    nvidia-smi | grep MiB
    ollama stop $model
done
```

---

## Resultats types
| Modele | VRAM | Tokens/s | Qualite FR |
|--------|------|----------|------------|
| gemma2:2b | ~2GB | ~60 t/s | 3/5 |
| gemma2:9b | ~6GB | ~35 t/s | 4/5 |
| gemma2:27b | ~18GB | ~15 t/s | 4.5/5 |
