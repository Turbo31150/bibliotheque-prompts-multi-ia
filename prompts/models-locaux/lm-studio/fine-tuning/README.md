# LM Studio -- Fine-tuning

## Description

Guides pour personnaliser les modeles dans LM Studio : system prompts, parametres d'inference et presets de configuration.

## Methodes de personnalisation

### 1 -- System prompt custom

```
Dans LM Studio > Chat > System Prompt :

"Tu es JARVIS, un assistant technique expert en Linux, Docker et GPU NVIDIA.
Tu reponds en francais, de facon concise et technique.
Tu privilegies les commandes et les exemples de code.
Quand on te demande un diagnostic, tu donnes des commandes a executer."
```

### 2 -- Presets de parametres

```yaml
# Preset : Code Generation
temperature: 0.1
top_p: 0.9
top_k: 40
repeat_penalty: 1.1
max_tokens: 2048

# Preset : Conversation
temperature: 0.7
top_p: 0.95
top_k: 50
repeat_penalty: 1.0
max_tokens: 1024

# Preset : Analyse Precise
temperature: 0.0
top_p: 1.0
max_tokens: 4096
```

### 3 -- Chat templates

```
Configurer le chat template dans Model Settings :
- Llama 3 : utiliser le template ChatML
- Mistral : utiliser le template Mistral
- Gemma : utiliser le template Gemma

Le template affecte la qualite des reponses.
```

### 4 -- Context window optimization

```
Pour les longs documents :
- Augmenter n_ctx a 8192 ou 16384
- Activer le sliding window si supporte
- Surveiller la VRAM (n_ctx * taille_modele)

Pour les reponses courtes :
- n_ctx a 2048 suffit
- Reduit l'usage memoire
```

### 5 -- Quantization selection

```
Dans LM Studio, choisir la quantization :
- Q8_0 : meilleure qualite, plus de VRAM
- Q6_K : bon compromis
- Q4_K_M : recommande pour la plupart des cas
- Q4_K_S : si VRAM limitee
- Q3_K_M : qualite reduite, VRAM minimale

Regle : choisir la plus haute quantization qui tient en VRAM.
```

---

## Bonnes pratiques
- Toujours tester un modele avant de le deployer en production
- Sauvegarder les presets de parametres pour chaque cas d'usage
- Utiliser le serveur local LM Studio pour l'integration avec d'autres outils
