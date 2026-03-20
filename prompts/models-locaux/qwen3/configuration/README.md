# Qwen3 — Configuration

## Famille Qwen3

| Modele | Taille | Debit | Score | Specialite |
|--------|--------|-------|-------|------------|
| `qwen3-8b` | 8B | **65 tok/s** | **98.4/100** | Champion local, general purpose |
| `qwen3-coder-30b` | 30B | 18-25 tok/s | 96/100 (code) | Code specialise |
| `qwen3.5-9b` | 9B | 55-65 tok/s | 92/100 | Successeur, general purpose |
| `qwen3.5-35b-a3b` | 35B MoE | 35-45 tok/s | 95/100 | MoE haute qualite |

## Champion Local : qwen3-8b

`qwen3-8b` est le modele le plus performant en rapport qualite/vitesse sur le cluster :

- **65 tokens/seconde** sur GPU unique
- **Score 98.4/100** sur le benchmark interne
- Ideal pour le dispatch rapide

## Regle Obligatoire : prefixe `/nothink`

Tous les modeles Qwen3 et Qwen3.5 necessitent le prefixe `/nothink` pour desactiver le mode de reflexion interne. Sans ce prefixe, le modele genere des tokens `<think>` inutiles qui consomment du contexte.

### Correct

```json
{
  "messages": [
    {"role": "user", "content": "/nothink Ecris un serveur HTTP en Go"}
  ]
}
```

### Incorrect (gaspille des tokens)

```json
{
  "messages": [
    {"role": "user", "content": "Ecris un serveur HTTP en Go"}
  ]
}
```

## Configuration LM Studio

1. Charger le modele dans LM Studio
2. Verifier le GPU split si > 20B
3. Le prefixe `/nothink` est gere cote prompt, pas dans la config LM Studio

## Configuration Ollama

```bash
ollama pull qwen2.5:1.5b   # Version legere Ollama
```

Note : les versions Ollama utilisent la branche Qwen2.5, pas Qwen3. Pour Qwen3, utiliser LM Studio.

## Integration JARVIS

Le dispatch engine route automatiquement vers `qwen3-8b` pour les taches rapides (< 5s attendu) et vers `qwen3-coder-30b` pour les taches de code complexes.
