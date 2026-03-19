# Claude API — Configuration

## Description
Guide complet pour configurer et utiliser l'API Claude d'Anthropic : installation du SDK, gestion des cles API, selection des modeles (Opus, Sonnet, Haiku), parametrage des requetes et bonnes pratiques.

## Configuration requise

### Prerequis
- Python 3.9+ ou Node.js 18+
- Compte Anthropic avec cle API active
- `pip install anthropic` (Python) ou `npm install @anthropic-ai/sdk` (Node.js)

### Installation

```bash
# Python
pip install anthropic

# Node.js
npm install @anthropic-ai/sdk

# Variable d'environnement
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

---

## Prompts par type de tache

### Creation — Configuration initiale Python

```
Configure l'API Claude pour un projet Python :

1. Installe le SDK : pip install anthropic
2. Cree un fichier config.py avec :
   - Client Anthropic initialise
   - Gestion de la cle API via variable d'environnement
   - Configuration des modeles par defaut
   - Gestion des erreurs et retries
3. Cree un fichier .env avec ANTHROPIC_API_KEY placeholder
4. Ajoute .env dans .gitignore
5. Teste avec un appel simple

## Code de base

import anthropic

client = anthropic.Anthropic()  # Utilise ANTHROPIC_API_KEY env var

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": "Bonjour Claude !"}
    ]
)
print(message.content[0].text)
```

---

### Creation — Configuration Node.js

```
Configure l'API Claude pour un projet Node.js :

import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();  // Utilise ANTHROPIC_API_KEY env var

const message = await client.messages.create({
  model: 'claude-sonnet-4-20250514',
  max_tokens: 4096,
  messages: [
    { role: 'user', content: 'Bonjour Claude !' }
  ]
});

console.log(message.content[0].text);
```

---

### Amelioration / Refactoring — Selection du modele optimal

```
Aide-moi a choisir le bon modele Claude pour mon cas d'usage :

## Modeles disponibles
| Modele | Forces | Latence | Cout | Usage recommande |
|--------|--------|---------|------|-----------------|
| claude-opus-4-20250514 | Raisonnement complexe, code, analyse | Haute | $$$$  | Taches critiques, architecture, decisions |
| claude-sonnet-4-20250514 | Equilibre qualite/vitesse | Moyenne | $$ | Dev quotidien, code review, generation |
| claude-haiku-3-5-20241022 | Rapidite, cout faible | Basse | $ | Classification, extraction, taches simples |

## Mon cas d'usage
- Type de tache : [DECRIRE]
- Volume : [NOMBRE DE REQUETES/JOUR]
- Budget : [BUDGET MENSUEL]
- Latence max acceptable : [SECONDES]
- Qualite requise : [CRITIQUE/STANDARD/BASIQUE]

Recommande le modele optimal et la configuration.
```

---

### Debug — Erreurs API courantes

```
L'API Claude retourne une erreur. Diagnostique :

Erreur : [MESSAGE D'ERREUR]
Code HTTP : [CODE]

## ERREURS COURANTES
| Code | Cause | Solution |
|------|-------|----------|
| 401 | Cle API invalide | Verifier ANTHROPIC_API_KEY |
| 403 | Acces refuse | Verifier les permissions du compte |
| 429 | Rate limit atteint | Implementer backoff exponentiel |
| 500 | Erreur serveur Anthropic | Retry apres 30s |
| 529 | API surchargee | Retry avec backoff |

## IMPLEMENTATION RETRY
import time
from anthropic import RateLimitError, APIStatusError

for attempt in range(3):
    try:
        response = client.messages.create(...)
        break
    except RateLimitError:
        time.sleep(2 ** attempt)
    except APIStatusError as e:
        if e.status_code >= 500:
            time.sleep(2 ** attempt)
        else:
            raise
```

---

### Documentation — Reference API rapide

```
Genere une reference rapide de l'API Claude :

## Parametres principaux de messages.create()
| Parametre | Type | Requis | Description |
|-----------|------|--------|-------------|
| model | string | oui | Modele a utiliser |
| max_tokens | int | oui | Tokens max en sortie |
| messages | array | oui | Conversation [{role, content}] |
| system | string | non | System prompt |
| temperature | float | non | 0.0-1.0 (defaut 1.0) |
| top_p | float | non | Nucleus sampling |
| stop_sequences | array | non | Sequences d'arret |
| stream | bool | non | Streaming de la reponse |
| tools | array | non | Outils/fonctions disponibles |
| tool_choice | object | non | Forcer l'utilisation d'un outil |
```

---

## Exemples concrets

### Exemple 1 : Appel simple
```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explique async/await en Python"}]
)
print(message.content[0].text)
```

**Resultat attendu** : Explication claire d'async/await avec exemples de code.

### Exemple 2 : Avec system prompt
```python
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2048,
    system="Tu es un expert Python senior. Reponds en francais avec des exemples de code.",
    messages=[{"role": "user", "content": "Comment implementer un rate limiter ?"}]
)
```

**Resultat attendu** : Implementation complete d'un rate limiter en Python avec explications en francais.

### Exemple 3 : Streaming
```python
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    messages=[{"role": "user", "content": "Ecris un module complet de health check"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

**Resultat attendu** : Reponse affichee en temps reel, mot par mot.

---

## Effet sur le modele
- Le choix du modele (Opus/Sonnet/Haiku) impacte directement la qualite et le cout
- Le system prompt oriente le comportement de maniere persistante pour toute la conversation
- La temperature basse (0.0-0.3) produit des reponses plus deterministes (code, analyse)
- La temperature haute (0.7-1.0) produit des reponses plus creatives (brainstorming)
- Le streaming ameliore l'experience utilisateur en affichant la reponse progressivement
- Le retry avec backoff exponentiel est essentiel pour la fiabilite en production
