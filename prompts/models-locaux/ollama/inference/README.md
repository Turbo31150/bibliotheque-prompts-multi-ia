# Ollama — Inference

## Endpoints API

Ollama expose deux endpoints principaux sur `http://localhost:11434`.

### /api/chat (conversationnel)

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1:7b",
  "messages": [
    {"role": "system", "content": "Tu es un assistant technique."},
    {"role": "user", "content": "Explique les goroutines en Go"}
  ],
  "stream": false
}'
```

### /api/generate (completion brute)

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:1.5b",
  "prompt": "Ecris une fonction Python de tri rapide",
  "stream": false
}'
```

## Streaming

Par defaut, Ollama streame les reponses. Chaque ligne JSON contient un fragment :

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1:7b",
  "messages": [{"role": "user", "content": "Hello"}],
  "stream": true
}'
```

Sortie :
```json
{"message":{"role":"assistant","content":"Bon"},"done":false}
{"message":{"role":"assistant","content":"jour"},"done":false}
{"message":{"role":"assistant","content":"!"},"done":true}
```

## Options Avancees

```json
{
  "model": "deepseek-r1:7b",
  "messages": [{"role": "user", "content": "..."}],
  "options": {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "num_predict": 1024,
    "num_ctx": 4096
  }
}
```

| Option | Description | Defaut |
|--------|-------------|--------|
| `temperature` | Creativite (0=deterministe, 1=creatif) | 0.8 |
| `top_p` | Nucleus sampling | 0.9 |
| `top_k` | Limite les tokens candidats | 40 |
| `num_predict` | Nombre max de tokens generes | 128 |
| `num_ctx` | Taille de la fenetre de contexte | 2048 |

## Python

```python
import httpx

resp = httpx.post("http://localhost:11434/api/chat", json={
    "model": "deepseek-r1:7b",
    "messages": [{"role": "user", "content": "Hello"}],
    "stream": False
})
print(resp.json()["message"]["content"])
```
