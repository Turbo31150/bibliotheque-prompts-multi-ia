# Perplexity — Configuration

> Guide de configuration de Perplexity AI pour la recherche et l'analyse.

---

## Description

Perplexity AI est un moteur de recherche conversationnel qui cite systematiquement ses sources. Ideal pour la recherche technique, la veille, le fact-checking et l'analyse de marche. Chaque reponse inclut des citations numerotees avec URLs.

## Configuration

### Compte
- Compte gratuit : 5 requetes Pro par jour
- Perplexity Pro : requetes illimitees, modeles avances, upload de fichiers
- API : acces programmatique pour l'automatisation

### Modeles
| Modele | Acces | Forces |
|--------|-------|--------|
| Default | Gratuit | Recherche rapide, citations |
| Pro Search | Pro | Recherche approfondie, multi-etapes |
| Reasoning | Pro | Raisonnement complexe |

### API
```bash
# Cle API disponible sur https://www.perplexity.ai/settings/api
export PERPLEXITY_API_KEY="pplx-votre-cle"

# Utilisation via curl
curl -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Votre question"}]
  }'
```

### Modeles API
| Modele API | Usage |
|------------|-------|
| `sonar` | Recherche rapide |
| `sonar-pro` | Recherche approfondie |
| `sonar-reasoning` | Raisonnement + recherche |

### Collections
- Organiser les recherches par projet/theme
- Partageables avec des collaborateurs
- Historique complet des requetes

### Parametres Pro Search
- **Focus** : Web / Academic / Writing / Math / Video
- Le focus "Academic" cherche dans les papers scientifiques
- Le focus "Web" est le mode par defaut pour la recherche technique

## Prompts par type

### Test de configuration
```
Recherche les dernieres versions de Python, Node.js et Rust.
Pour chaque langage : version actuelle, date de sortie, lien source.
```

### Configuration API
```
Comment configurer l'API Perplexity avec Python (requests) ?
Donne un exemple fonctionnel avec gestion d'erreurs.
```

## Effet sur le modele

- Perplexity cite toujours ses sources — c'est sa force fondamentale vs ChatGPT/Gemini
- Le Pro Search fait plusieurs recherches en cascade — plus lent mais plus complet
- Le focus "Academic" est unique pour la recherche scientifique
- L'API permet l'integration dans des pipelines d'automatisation (veille, monitoring)
- Perplexity est moins bon en generation de code — utiliser pour la recherche, pas le dev
