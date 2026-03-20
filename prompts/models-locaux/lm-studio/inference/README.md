# LM Studio — Inference

## Endpoint API

LM Studio expose une API compatible OpenAI sur `http://<host>:1234/v1`.

## Exemples de Requetes

### curl

```bash
curl http://192.168.1.20:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5-9b",
    "messages": [
      {"role": "system", "content": "Tu es un assistant technique."},
      {"role": "user", "content": "/nothink Comment optimiser une requete SQL avec index ?"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
  }'
```

### Python (httpx)

```python
import httpx

response = httpx.post(
    "http://192.168.1.20:1234/v1/chat/completions",
    json={
        "model": "qwen3-coder-30b",
        "messages": [
            {"role": "user", "content": "/nothink Refactore cette fonction Python"}
        ],
        "temperature": 0.3,
        "top_p": 0.9,
        "max_tokens": 2048
    },
    timeout=120.0
)

result = response.json()
print(result["choices"][0]["message"]["content"])
```

## Selection du Modele

Le champ `model` doit correspondre au nom exact charge dans LM Studio. Verifier les modeles disponibles :

```bash
curl http://192.168.1.20:1234/v1/models | jq '.data[].id'
```

## Parametres Recommandes

| Parametre | Code | General | Creatif |
|-----------|------|---------|---------|
| `temperature` | 0.1-0.3 | 0.5-0.7 | 0.8-1.0 |
| `top_p` | 0.9 | 0.95 | 1.0 |
| `max_tokens` | 2048 | 1024 | 1024 |

## Streaming

```bash
curl http://192.168.1.20:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5-9b",
    "messages": [{"role": "user", "content": "/nothink Hello"}],
    "stream": true
  }'
```

Les tokens arrivent en temps reel via Server-Sent Events (SSE).
