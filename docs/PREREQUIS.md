# Prérequis Système

## Matériel minimum
- CPU : 4+ cores (recommandé : AMD Ryzen 7 ou équivalent)
- RAM : 16 Go minimum (recommandé : 32-64 Go)
- GPU : NVIDIA avec CUDA (optionnel mais recommandé pour LM Studio/Whisper)
- Stockage : 100 Go SSD minimum

## Logiciels requis

### Base
```bash
sudo apt update && sudo apt install -y \
    python3 python3-pip python3-venv \
    nodejs npm git curl jq tmux wget
```

### Python (uv)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Docker
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

### Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```

### Ollama (IA locale)
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:1.5b
```

### n8n (workflows)
```bash
npm install -g n8n
```

### NVIDIA (si GPU)
```bash
sudo apt install -y nvidia-driver-590 nvidia-utils-590
```

### LM Studio
Télécharger depuis https://lmstudio.ai/

## Clés API nécessaires
| Service | Variable | Où l'obtenir |
|---------|----------|-------------|
| Anthropic (Claude) | ANTHROPIC_API_KEY | console.anthropic.com |
| Google (Gemini) | GEMINI_API_KEY | aistudio.google.com |
| Telegram | TELEGRAM_TOKEN | @BotFather sur Telegram |
| MEXC (Trading) | MEXC_API_KEY | mexc.com (optionnel) |
| Picovoice (Wake Word) | PV_ACCESS_KEY | picovoice.ai (optionnel) |
| HuggingFace (Whisper) | HF_TOKEN | huggingface.co (optionnel) |
