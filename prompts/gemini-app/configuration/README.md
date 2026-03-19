# Gemini App — Configuration

> Guide de configuration de Google Gemini App (AI Studio et application web).

---

## Description

Gemini App est l'interface web de Google pour interagir avec les modeles Gemini. Accessible via gemini.google.com et Google AI Studio, elle offre des capacites multimodales (images, documents, audio) et un acces aux derniers modeles Google.

## Configuration

### Compte et acces
- Compte Google (gratuit pour Gemini basique)
- Gemini Advanced (Google One AI Premium) pour les modeles avances
- Google AI Studio : https://aistudio.google.com pour l'acces developpeur

### Cle API (AI Studio)
```
1. Aller sur https://aistudio.google.com/apikey
2. Creer une cle API
3. Sauvegarder la cle en securite
```

### Modeles disponibles
| Modele | Usage | Forces |
|--------|-------|--------|
| Gemini 2.5 Pro | Raisonnement complexe | Code, analyse, long contexte |
| Gemini 2.5 Flash | Rapide et polyvalent | Bon rapport vitesse/qualite |
| Gemini 2.0 Flash | Ultra-rapide | Taches simples, cout minimal |

### Google AI Studio — Configuration avancee
- **Temperature** : 0.1-0.3 pour le code, 0.7-1.0 pour la creation
- **Top-P** : 0.95 par defaut
- **Max output tokens** : ajuster selon le besoin
- **Safety settings** : configurable par categorie
- **System Instructions** : equivalent des Custom Instructions

### System Instructions recommandees
```
Tu es un assistant technique senior.
Domaines : Linux, Python, GPU computing, IA.
Langue : francais.
Format : markdown structure, code avec type hints.
Reponses : concises, concretes, actionnables.
Pas de disclaimers inutiles.
```

## Prompts par type

### Test de configuration
```
Confirme ta version de modele et tes capacites.
Peux-tu : analyser des images, lire des PDFs, generer du code, rechercher le web ?
```

### Configuration AI Studio
```
Je configure AI Studio pour un projet Python/Linux.
Quels reglages recommandes-tu pour :
1. Generation de code (temperature, tokens)
2. Analyse de documents (temperature, tokens)
3. Recherche (grounding settings)
```

## Effet sur le modele

- Les System Instructions dans AI Studio persistent par session — elles configurent le comportement sans repeter le contexte
- Gemini App a acces a Google Search (grounding) — les reponses peuvent etre ancrees dans des donnees web recentes
- Le contexte 1M tokens permet d'uploader des documents entiers pour analyse
- Gemini est integre a l'ecosysteme Google (Drive, Docs, Gmail) — exploitable pour l'analyse de documents
- La temperature basse (0.1-0.3) est critique pour le code — Gemini devient imprecis a haute temperature
