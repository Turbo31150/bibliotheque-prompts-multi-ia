# ChatGPT — Configuration

> Guide de configuration de ChatGPT pour une utilisation optimale.

---

## Description

ChatGPT (OpenAI) est l'IA conversationnelle la plus populaire. Ce guide couvre la configuration initiale, les Custom Instructions, la memoire et les plugins pour maximiser la qualite des reponses.

## Configuration

### Compte et modele
- Compte OpenAI (gratuit ou Plus/Pro)
- Modele recommande : **GPT-4o** (multimodal, rapide, performant)
- GPT-4o mini pour les taches simples (plus rapide, moins cher en API)

### Custom Instructions
Les Custom Instructions definissent le comportement par defaut de ChatGPT :

```
Qui etes-vous :
- Developpeur senior Linux/Python
- Travaille sur un cluster multi-GPU (JARVIS)
- Prefere les reponses techniques et directes
- Langue : francais

Comment ChatGPT doit repondre :
- Code commente en francais
- Reponses structurees avec titres
- Pas de disclaimers inutiles
- Exemples concrets systematiques
- Format markdown
```

### Memoire
- Activer la memoire conversationnelle dans Settings > Personalization
- ChatGPT retient le contexte entre sessions
- Permet d'eviter de repeter son profil technique

### Plugins / GPTs
- Code Interpreter : execution Python en sandbox
- Web Browsing : recherche en temps reel
- DALL-E : generation d'images
- Custom GPTs : assistants specialises configurables

## Prompts par type

### Configuration initiale
```
Configure-toi comme un assistant technique senior.
Stack : Python 3.13+, Linux, Docker, GPU computing.
Reponds en francais, format markdown, avec code commente.
```

### Verification de la config
```
Repete ma configuration actuelle : qui je suis, mon stack technique,
mes preferences de reponse. Corrige si quelque chose manque.
```

## Effet sur le modele

- Les Custom Instructions persistent entre sessions — le modele demarre deja contextualise
- GPT-4o est naturellement verbeux : les instructions "pas de disclaimers" et "reponses directes" reduisent le bruit
- La memoire evite la perte de contexte sur les projets longs
- Les Custom GPTs permettent de pre-configurer des assistants specialises sans repeter les instructions
