# DeepSeek-R1 — Configuration

## Presentation

DeepSeek-R1 est un modele de raisonnement avance qui genere automatiquement des chaines de pensee (chain-of-thought) avant de repondre. Il excelle sur les problemes complexes, mathematiques et logiques.

## Deploiement sur M2

Le modele est heberge sur la machine M2 du cluster :

- **Adresse** : `192.168.1.26`
- **Port** : `1234` (LM Studio) ou `11434` (Ollama)
- **GPU** : GPU dedie sur M2

## Regle Critique : `max_output_tokens >= 2048`

DeepSeek-R1 genere des raisonnements longs avant la reponse finale. Le parametre `max_output_tokens` (ou `max_tokens`) doit etre au minimum 2048 :

```json
{
  "model": "deepseek-r1",
  "messages": [
    {"role": "user", "content": "Prouve que la racine de 2 est irrationnelle"}
  ],
  "max_tokens": 2048,
  "temperature": 0.6
}
```

**Pourquoi ?** Le modele utilise en moyenne 500-1500 tokens pour sa phase de reflexion interne (`<think>...</think>`) avant de produire la reponse. Avec `max_tokens < 2048`, la reponse sera tronquee.

## Mode Thinking

Le raisonnement est automatique. La sortie contient :

1. **Phase reflexion** : entre balises `<think>` (optionnellement masquee)
2. **Reponse finale** : apres la reflexion

```
<think>
Pour prouver l'irrationalite de sqrt(2), je vais utiliser
une preuve par l'absurde...
</think>

La racine carree de 2 est irrationnelle. Voici la preuve...
```

## Parametres Recommandes

| Parametre | Valeur |
|-----------|--------|
| `temperature` | 0.6 |
| `max_tokens` | 2048-4096 |
| `top_p` | 0.95 |

## Integration Cluster

DeepSeek-R1 est automatiquement route par le dispatch engine JARVIS pour les taches de type `reasoning`, `math`, `logic`.
