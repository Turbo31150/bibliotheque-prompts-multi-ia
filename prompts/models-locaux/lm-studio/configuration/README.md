# LM Studio — Configuration

## Installation

1. Telecharger LM Studio depuis [lmstudio.ai](https://lmstudio.ai)
2. Installer sur la machine GPU (M1 : Ryzen 5700X3D, 5 GPUs)
3. Configurer l'allocation GPU dans Settings > GPU

## Serveur API

Lancer le serveur local compatible OpenAI :

```bash
# LM Studio expose une API OpenAI-compatible
# Adresse : http://0.0.0.0:1234/v1
# Accessible depuis tout le cluster JARVIS
```

- **Hote** : `0.0.0.0` (ecoute sur toutes les interfaces)
- **Port** : `1234`
- **Endpoint** : `/v1/chat/completions`

## Modeles Disponibles

| Modele | Taille | Usage principal |
|--------|--------|-----------------|
| `qwen3.5-9b` | 9B | General purpose, rapide |
| `qwen3-coder-30b` | 30B | Code specialise |
| `qwen3.5-35b-a3b` | 35B (MoE) | Haute qualite, architecture MoE |
| `gpt-oss-20b` | 20B | Alternative open-source |
| `deepseek-r1` | Variable | Raisonnement avance |
| `gemma-3-4b` | 4B | Leger, classification |
| `text-embedding-nomic` | — | Embeddings pour RAG |

## Regles Importantes

### Qwen3 : prefixe `/nothink`

Tous les modeles Qwen3 necessitent le prefixe `/nothink` dans le message systeme ou utilisateur pour desactiver le mode reflexion interne et obtenir des reponses directes :

```json
{
  "messages": [
    {"role": "user", "content": "/nothink Explique le pattern observer"}
  ]
}
```

### DeepSeek-R1 : `max_output_tokens >= 2048`

Le modele DeepSeek-R1 genere des chaines de raisonnement longues. Toujours configurer :

```json
{
  "max_tokens": 2048,
  "temperature": 0.6
}
```

Sans ce parametre, les reponses seront tronquees en plein raisonnement.

## Configuration GPU

LM Studio gere automatiquement le split GPU. Pour les modeles > 20B, verifier que plusieurs GPUs sont alloues dans l'onglet GPU Settings.
