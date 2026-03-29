# Ollama — Configuration

## Installation

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

## Demarrage du Service

```bash
# Demarrer le serveur
ollama serve

# Ou via systemd
sudo systemctl enable --now ollama
```

Le serveur ecoute par defaut sur `http://localhost:11434`.

## Telecharger les Modeles

```bash
ollama pull kimi-k2.5:cloud
ollama pull deepseek-r1:7b
ollama pull qwen2.5:1.5b
```

## Modeles Disponibles

| Modele | Taille | Usage |
|--------|--------|-------|
| `kimi-k2.5:cloud` | Cloud | Haute qualite, modele cloud hybride |
| `deepseek-r1:7b` | 7B | Raisonnement, version compacte |
| `qwen2.5:1.5b` | 1.5B | Ultra-leger, reponses rapides |

## Regles Importantes

### Modeles Cloud : `think:false`

Pour les modeles cloud (comme `kimi-k2.5:cloud`), desactiver le mode reflexion :

```json
{
  "model": "kimi-k2.5:cloud",
  "messages": [{"role": "user", "content": "Hello"}],
  "options": {
    "think": false
  }
}
```

Cela evite les latences inutiles et les tokens de reflexion dans la sortie.

## Configuration Reseau

Pour exposer Ollama sur le reseau du cluster :

```bash
# /etc/systemd/system/ollama.service.d/override.conf
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

## Lister les Modeles Installes

```bash
ollama list
```
