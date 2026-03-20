# Modeles Locaux -- Ollama

## Description

Prompts et guides pour utiliser Ollama comme runtime de modeles locaux : installation, configuration, optimisation et utilisation de LLMs en local.

## Contenu
- [benchmark/](benchmark/) -- Benchmarks de performance des modeles
- [configuration/](configuration/) -- Configuration et optimisation d'Ollama
- [fine-tuning/](fine-tuning/) -- Fine-tuning de modeles via Ollama
- [inference/](inference/) -- Utilisation et prompts pour l'inference

## Installation rapide
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.1:8b
ollama run llama3.1:8b "Bonjour, comment vas-tu ?"
```
