# Ollama -- Fine-tuning

## Description

Guides pour le fine-tuning de modeles via Ollama : creation de Modelfiles, personnalisation de system prompts et adaptation de modeles a des domaines specifiques.

## Methodes de fine-tuning

### 1 -- Modelfile custom (le plus simple)

```dockerfile
# Fichier : Modelfile.jarvis
FROM llama3.1:8b
SYSTEM "Tu es JARVIS, assistant technique Linux. Tu reponds en francais. Tu es expert en administration systeme, Docker, GPU NVIDIA et automatisation. Tes reponses sont concises et techniques."
PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER num_ctx 4096

# Creer le modele
# ollama create jarvis -f Modelfile.jarvis
# ollama run jarvis
```

### 2 -- Modelfile avec exemples (few-shot)

```dockerfile
FROM mistral:7b
SYSTEM "Assistant de monitoring systeme. Reponds en JSON structure."

MESSAGE user "Etat du CPU ?"
MESSAGE assistant '{"component": "cpu", "usage": "45%", "status": "ok", "recommendation": "aucune action requise"}'

MESSAGE user "Temperature GPU ?"
MESSAGE assistant '{"component": "gpu", "temps": [72, 68, 75], "status": "warning", "recommendation": "verifier la ventilation"}'

PARAMETER temperature 0.1
```

### 3 -- Fine-tuning avec donnees (LoRA)

```bash
# Preparer les donnees au format JSONL
# {"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}

# Utiliser unsloth ou axolotl pour le fine-tuning
pip install unsloth
python -c "
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained('unsloth/llama-3.1-8b-bnb-4bit')
# ... fine-tuning avec les donnees
model.save_pretrained_gguf('jarvis-ft', tokenizer, quantization_method='q4_k_m')
"

# Importer dans Ollama
# ollama create jarvis-ft -f Modelfile.ft
```

### 4 -- Adapter le style de reponse

```dockerfile
FROM qwen2.5:7b
SYSTEM "Tu reponds toujours en 3 parties :
1. DIAGNOSTIC : le probleme identifie
2. SOLUTION : la commande ou le code
3. VERIFICATION : comment verifier que ca marche

Tu es bref et direct. Pas de bavardage."
PARAMETER temperature 0.2
```

### 5 -- Modele specialise trading

```dockerfile
FROM llama3.1:8b
SYSTEM "Analyste technique crypto. Tu reponds en JSON :
{signal: LONG|SHORT|NEUTRE, confidence: 0-100, entry: float, stop_loss: float, take_profit: float, reasoning: string}
Tu analyses : RSI, MACD, Bollinger, Volume, Support/Resistance."
PARAMETER temperature 0.1
PARAMETER num_ctx 8192
```

---

## Bonnes pratiques
- Temperature basse (0.1-0.3) pour les taches techniques
- Temperature haute (0.7-0.9) pour les taches creatives
- num_ctx adapte au cas d'usage (4096 default, 8192+ pour les longs contextes)
- Tester avec un jeu de prompts de reference avant et apres
