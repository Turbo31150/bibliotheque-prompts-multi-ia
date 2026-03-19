# Modeles Locaux -- DeepSeek R1

## Description

Prompts et guides pour utiliser DeepSeek R1 en local : modele de raisonnement avance pour le code, les mathematiques et l'analyse.

## Contenu
- [benchmark/](benchmark/) -- Benchmarks de performance
- [configuration/](configuration/) -- Configuration et optimisation
- [fine-tuning/](fine-tuning/) -- Fine-tuning et personnalisation
- [inference/](inference/) -- Utilisation et prompts

## Installation via Ollama
```bash
ollama pull deepseek-r1:7b    # Version 7B
ollama pull deepseek-r1:32b   # Version 32B (meilleure qualite)
ollama run deepseek-r1:7b "Resous ce probleme..."
```
