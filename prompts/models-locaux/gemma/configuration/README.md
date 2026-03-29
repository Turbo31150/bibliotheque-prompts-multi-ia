# Gemma 3-4B — Configuration

## Presentation

Google Gemma 3-4B est un modele leger et rapide, ideal pour les taches de classification, extraction d'entites et reponses courtes.

## Caracteristiques

| Propriete | Valeur |
|-----------|--------|
| Taille | 4B parametres |
| VRAM | ~3 GB |
| Debit | 80-100 tok/s |
| Score qualite | 78/100 |
| Createur | Google DeepMind |

## Installation

### LM Studio

Rechercher `gemma-3-4b` dans le catalogue LM Studio et telecharger le GGUF.

### Ollama

```bash
ollama pull gemma3:4b
```

## Cas d'Usage Recommandes

- **Classification** : categoriser des textes, tickets, logs
- **Extraction** : extraire des entites nommees, dates, montants
- **Reponses courtes** : FAQ, questions factuelles
- **Pre-filtrage** : trier avant d'envoyer a un modele plus lourd

## Parametres Recommandes

```json
{
  "model": "gemma-3-4b",
  "messages": [
    {"role": "user", "content": "Classe ce texte : positif, negatif ou neutre"}
  ],
  "temperature": 0.1,
  "max_tokens": 256
}
```

Temperature basse (0.1) recommandee pour la classification. Le modele n'a pas besoin de prefixes speciaux.

## Avantages

- Tres faible empreinte VRAM : peut tourner en parallele avec d'autres modeles
- Temps de chargement quasi-instantane
- Ideal comme "modele de garde" toujours charge sur le cluster
