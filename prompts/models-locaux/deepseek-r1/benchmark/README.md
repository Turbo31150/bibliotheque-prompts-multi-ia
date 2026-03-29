# DeepSeek R1 -- Benchmark

## Description

Benchmarks pour evaluer DeepSeek R1 sur ses points forts : raisonnement, code et mathematiques.

## Benchmarks

### 1 -- Raisonnement

```
Teste DeepSeek R1 sur ces problemes de raisonnement :
1. Logique : "Si A implique B, et B implique C, et A est vrai..."
2. Debugging : trouver le bug dans 20 lignes de code
3. Optimisation : proposer une meilleure approche algorithmique
4. Architecture : concevoir un systeme pour [BESOIN]
5. Maths : calculer la complexite d'un algorithme

Comparer avec llama3.1:8b et mistral:7b sur les memes problemes.
```

### 2 -- Code generation

```bash
PROMPT="Implemente un trie (arbre prefixe) en Python avec insert, search et delete. Inclus les tests."
for model in deepseek-r1:7b llama3.1:8b; do
    echo "=== $model ==="
    time ollama run $model "$PROMPT" > /tmp/bench_${model}.txt
done
# Comparer : qualite du code, tests, temps
```

### 3 -- Benchmark chaine de pensee

```
DeepSeek R1 montre sa chaine de pensee (<think>...</think>).
Tester si la chaine de pensee ameliore la qualite :

PROMPT_SIMPLE="Combien de mots de 3 lettres peut-on former avec A, B, C ?"
PROMPT_COT="Combien de mots de 3 lettres peut-on former avec A, B, C ? Montre ton raisonnement etape par etape."

Comparer les resultats et la justesse.
```

### 4 -- Benchmark VRAM et performance

```bash
for model in deepseek-r1:1.5b deepseek-r1:7b deepseek-r1:14b deepseek-r1:32b; do
    echo "=== $model ==="
    ollama run $model "test" &
    sleep 5
    nvidia-smi | grep MiB
    time ollama run $model "Ecris un quicksort en Rust" > /dev/null
    ollama stop $model
done
```

### 5 -- Benchmark francais

```
DeepSeek R1 est-il bon en francais ?
1. Comprehension de texte technique en francais
2. Generation de code avec commentaires en francais
3. Analyse de logs en francais
4. Documentation technique en francais
5. Conversation naturelle en francais

Noter chaque tache sur 5.
```

---

## Notes
- DeepSeek R1 excelle en raisonnement et code
- La chaine de pensee (think) utilise des tokens supplementaires
- Les versions distillees (7B) sont un bon compromis performance/qualite
