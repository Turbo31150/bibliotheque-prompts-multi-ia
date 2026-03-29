# API Anthropic — Guide complet

> Intégrer Claude directement dans vos applications via l'API Anthropic.
> SDK Python et TypeScript, tool use, streaming et bonnes pratiques.

---

## Installation du SDK

```bash
# Python
pip install anthropic

# TypeScript / Node.js
npm install @anthropic-ai/sdk
```

## Authentification

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Premier appel

### Python
```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Bonjour Claude !"}]
)
print(message.content[0].text)
```

### TypeScript
```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();
const message = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Bonjour Claude !" }]
});
console.log(message.content[0].text);
```

## Modèles disponibles

| Modèle | ID | Contexte | Usage |
|---|---|---|---|
| **Opus 4.6** | `claude-opus-4-6` | 1M tokens | Le plus capable. Raisonnement, code complexe. |
| **Sonnet 4.6** | `claude-sonnet-4-6` | 200K tokens | Équilibre vitesse/qualité. |
| **Haiku 4.5** | `claude-haiku-4-5-20251001` | 200K tokens | Ultra-rapide, tâches simples. |

## Fonctionnalités avancées

| Fonctionnalité | Description |
|---|---|
| **Tool Use** | Donner des outils (fonctions) que Claude peut appeler. |
| **Streaming** | Recevoir la réponse token par token. |
| **Vision** | Envoyer des images pour analyse. |
| **Batches** | Envoyer des lots de requêtes à tarif réduit. |
| **Extended Thinking** | Activer le raisonnement étendu pour les tâches complexes. |

## Tool Use (appel de fonctions)

```python
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[{
        "name": "get_weather",
        "description": "Obtenir la météo d'une ville.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Nom de la ville."}
            },
            "required": ["city"]
        }
    }],
    messages=[{"role": "user", "content": "Quel temps fait-il à Toulouse ?"}]
)
```

## Bonnes pratiques

1. **System prompt** : toujours définir un rôle clair.
2. **Temperature** : 0 pour le code, 0.7 pour la créativité.
3. **Max tokens** : toujours définir une limite.
4. **Gestion d'erreurs** : capturer les `RateLimitError` et `APIError`.
5. **Caching** : utiliser le prompt caching pour réduire les coûts.
