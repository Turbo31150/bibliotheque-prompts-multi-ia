# Gemma -- Fine-tuning

## Description

Guides pour le fine-tuning des modeles Gemma : Modelfile, LoRA et adaptation a des domaines specifiques.

## Methodes

### 1 -- Modelfile custom

```dockerfile
FROM gemma2:9b
SYSTEM "Tu es un assistant technique Linux specialise en administration systeme. Reponds en francais, de facon concise et technique."
PARAMETER temperature 0.2
PARAMETER num_ctx 8192
```

### 2 -- LoRA avec Unsloth

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained("unsloth/gemma-2-9b-it-bnb-4bit")
model = FastLanguageModel.get_peft_model(model, r=16, lora_alpha=16)
# Entrainer sur vos donnees
# Exporter en GGUF pour Ollama
```

### 3 -- Few-shot dans le Modelfile

```dockerfile
FROM gemma2:9b
SYSTEM "Analyseur de logs Linux. Reponds en JSON."
MESSAGE user "auth.log: Failed password for root from 192.168.1.100 port 22"
MESSAGE assistant '{"severity": "warning", "type": "brute_force", "source_ip": "192.168.1.100", "action": "ban_ip"}'
```

### 4 -- Specialisation domaine

```dockerfile
FROM gemma2:9b
SYSTEM "Expert en trading crypto. Tu analyses les indicateurs techniques (RSI, MACD, Bollinger) et generes des signaux de trading. Format JSON strict."
PARAMETER temperature 0.1
```

### 5 -- Modele multilingue optimise

```dockerfile
FROM gemma2:9b
SYSTEM "Tu es un assistant multilingue. Tu detectes la langue de l'utilisateur et reponds dans la meme langue. Tu excelles en francais et en anglais technique."
PARAMETER temperature 0.3
```
