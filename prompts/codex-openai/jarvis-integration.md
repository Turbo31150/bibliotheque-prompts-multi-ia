# Codex OpenAI — Integration JARVIS

> Prompts pour integrer et etendre JARVIS avec Codex CLI.

---

## Prompt d'ajout de module JARVIS

```
Cree un nouveau module JARVIS pour [FONCTIONNALITE].

## Architecture JARVIS
- Runtime : Python 3.13 + uv
- Framework : Claude Agent SDK
- MCP : 658 handlers existants dans src/mcp_server.py
- DB : SQLite (63 bases, 160 MB)
- API : FastAPI (670+ endpoints)

## Conventions obligatoires
- from __future__ import annotations en premier import
- Type hints sur toutes les fonctions
- async/await pour tout I/O
- Logging via logging module (pas print)
- snake_case pour Python
- Docstrings en francais
- Tests dans tests/test_[module].py

## Structure du module
Genere :
1. src/[module].py — Code principal
2. tests/test_[module].py — Tests (min 5 cas)
3. Integration MCP : handlers a ajouter dans mcp_server.py
4. Integration API : endpoints a ajouter
5. Documentation : docstring du module

## Contraintes
- Ne pas modifier les fichiers critiques directement
- Utiliser le pool httpx partage de src/tools.py
- Respecter le rate limiting de src/rate_limiter.py
- Exporter les metriques via src/metrics_exporter.py
```

### Ce que ca fait
Cree un module JARVIS complet et integre, respectant toutes les conventions du projet.

### Effet sur le modele
- Le contexte architectural guide Codex vers une solution compatible
- Les conventions explicites evitent les corrections post-generation
- La structure en 5 points garantit un module complet

---

## Prompt d'ajout de commande vocale

```
Ajoute une commande vocale JARVIS pour [ACTION].

## Systeme vocal JARVIS
- STT : Whisper (transcription)
- NLU : Classification par le cluster IA
- TTS : Piper (synthese vocale)
- Commandes existantes : 898
- Modules : 5 (systeme, media, domotique, trading, dev)

## Nouvelle commande
- Declencheur vocal : "[PHRASE_DECLENCHEUR]"
- Aliases : [LISTE_ALIASES]
- Module : [systeme/media/domotique/trading/dev]
- Action : [DESCRIPTION DE L'ACTION]
- Reponse vocale : "[TEXTE_A_PRONONCER]"

## Implementation
1. Ajouter dans src/commands.py (pattern matching)
2. Ajouter le handler dans le module concerne
3. Ajouter le test dans tests/test_commands.py
4. Mettre a jour la documentation des commandes
```

---

## Prompt de debug cluster

```
Debug un probleme sur le cluster JARVIS :

Symptome : [DECRIRE]
Noeud concerne : [M1/M2/M3/OL1]
URL : [IP:PORT]

Verifie dans l'ordre :
1. Ping reseau (le noeud repond-il ?)
2. Service IA (LM Studio / Ollama demarre ?)
3. Modele charge (quel modele, quelle VRAM ?)
4. API fonctionnelle (requete test)
5. Performance (latence, tokens/s)

Si le noeud est down :
- Propose un fix
- Active le fallback vers le noeud suivant
- Envoie une alerte Telegram
```

---

## Prerequis
- Codex CLI installe
- Acces au projet jarvis-linux
- Connaissance de l'architecture JARVIS (voir CLAUDE.md)
