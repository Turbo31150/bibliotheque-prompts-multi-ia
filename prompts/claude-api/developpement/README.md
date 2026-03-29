# Claude API — Developpement

## Description
Prompts et patterns pour construire des applications avec l'API Claude : chat conversationnel, utilisation d'outils (function calling), agents autonomes et streaming temps reel.

## Configuration requise
- SDK Anthropic installe (`pip install anthropic`)
- Cle API configuree (`ANTHROPIC_API_KEY`)
- Python 3.9+ ou Node.js 18+
- Connaissance des concepts : messages, tools, streaming

---

## Prompts par type de tache

### Creation — Chatbot conversationnel

```
Cree un chatbot conversationnel avec l'API Claude :

## SPECIFICATION
1. Gestion de l'historique de conversation (multi-turn)
2. System prompt configurable
3. Streaming des reponses
4. Gestion des erreurs et retries
5. Limite de contexte (tronquer si > 100k tokens)

## CODE

import anthropic

class ChatBot:
    def __init__(self, system_prompt: str = "", model: str = "claude-sonnet-4-20250514"):
        self.client = anthropic.Anthropic()
        self.model = model
        self.system = system_prompt
        self.messages: list[dict] = []

    def chat(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=self.system,
            messages=self.messages
        )

        assistant_message = response.content[0].text
        self.messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message

    def chat_stream(self, user_message: str):
        self.messages.append({"role": "user", "content": user_message})

        full_response = ""
        with self.client.messages.stream(
            model=self.model,
            max_tokens=4096,
            system=self.system,
            messages=self.messages
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        self.messages.append({"role": "assistant", "content": full_response})

## TESTS
- Test conversation multi-turn (contexte preserve)
- Test streaming (reponse progressive)
- Test erreur API (retry)
- Test limite de contexte (troncature)
```

---

### Creation — Function calling (Tools)

```
Implemente le function calling avec l'API Claude :

## SPECIFICATION
Donner a Claude l'acces a des outils externes qu'il peut appeler.

## CODE

import anthropic
import json

client = anthropic.Anthropic()

# Definition des outils
tools = [
    {
        "name": "get_weather",
        "description": "Obtenir la meteo actuelle pour une ville",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Nom de la ville"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "default": "celsius"}
            },
            "required": ["city"]
        }
    },
    {
        "name": "search_database",
        "description": "Rechercher dans la base de donnees",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "limit": {"type": "integer", "default": 10}
            },
            "required": ["query"]
        }
    }
]

# Handlers
def handle_tool_call(name: str, input_data: dict) -> str:
    if name == "get_weather":
        return json.dumps({"temp": 22, "condition": "ensoleille", "city": input_data["city"]})
    elif name == "search_database":
        return json.dumps({"results": [{"id": 1, "title": "Result 1"}]})
    return json.dumps({"error": "Unknown tool"})

# Boucle d'agent
def agent_loop(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            tools=tools,
            messages=messages
        )

        # Si pas d'appel d'outil, retourner la reponse
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Traiter les appels d'outils
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = handle_tool_call(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        messages.append({"role": "user", "content": tool_results})
```

---

### Creation — Agent autonome

```
Cree un agent autonome avec l'API Claude :

## SPECIFICATION
Un agent qui peut :
1. Recevoir un objectif complexe
2. Decomposer en sous-taches
3. Executer chaque sous-tache en utilisant des outils
4. S'auto-corriger en cas d'erreur
5. Rapporter le resultat final

## ARCHITECTURE
- Boucle principale : objectif → plan → execution → verification
- Outils : lecture/ecriture fichiers, execution shell, recherche web
- Memoire : historique des actions et resultats
- Garde-fous : limite d'iterations (20 max), timeout (5 min)

## TOOLS
tools = [
    {"name": "read_file", "description": "Lire un fichier", ...},
    {"name": "write_file", "description": "Ecrire un fichier", ...},
    {"name": "run_command", "description": "Executer une commande shell", ...},
    {"name": "search_web", "description": "Rechercher sur le web", ...},
    {"name": "task_complete", "description": "Signaler la fin de la tache", ...}
]

## SYSTEM PROMPT
"Tu es un agent autonome. Tu recois un objectif et tu dois l'accomplir
en utilisant les outils disponibles. Planifie avant d'agir. Verifie tes
resultats. Si une action echoue, analyse pourquoi et essaie une approche
differente. Appelle task_complete quand l'objectif est atteint."
```

---

### Amelioration / Refactoring — Optimiser les couts API

```
Optimise les couts d'utilisation de l'API Claude :

## STRATEGIES
1. Choix du modele :
   - Haiku pour les taches simples (classification, extraction)
   - Sonnet pour les taches standard (code, analyse)
   - Opus uniquement pour les taches critiques (architecture, decisions)

2. Reduction des tokens :
   - System prompt concis (< 500 tokens)
   - Tronquer l'historique (garder les 10 derniers messages)
   - Resumer les conversations longues periodiquement
   - Utiliser max_tokens adapte (pas 4096 si 200 suffisent)

3. Caching :
   - Cacher les reponses pour les requetes identiques
   - TTL adapte au type de requete (1h pour la meteo, 24h pour la doc)
   - Utiliser le prompt caching d'Anthropic

4. Batching :
   - Regrouper les petites requetes
   - Utiliser l'API batch pour les traitements en masse

## MESURE
Avant/apres optimisation :
- Cout moyen par requete
- Tokens moyen par conversation
- Nombre de requetes/jour
```

---

### Debug — Reponses de mauvaise qualite

```
Claude retourne des reponses de mauvaise qualite via l'API.

## DIAGNOSTIC
1. Le system prompt est-il clair et specifique ?
2. Le contexte est-il suffisant dans les messages ?
3. Le modele est-il adapte a la tache ?
4. La temperature est-elle correcte ? (basse pour le code, haute pour le creatif)
5. Les outils sont-ils bien decrits ? (descriptions claires)
6. L'historique n'est-il pas pollue ? (messages contradictoires)

## SOLUTIONS
- System prompt : ajouter des exemples few-shot
- Contexte : fournir plus d'informations pertinentes
- Modele : passer a Sonnet ou Opus si Haiku est insuffisant
- Temperature : 0.0-0.3 pour le code, 0.5-0.8 pour le texte
- Outils : ameliorer les descriptions et les exemples
- Historique : nettoyer et resumer
```

---

### Documentation — Guide d'integration

```
Genere un guide d'integration de l'API Claude dans une application :

## FORMAT
1. Architecture recommandee
   - Separation client/serveur
   - Gestion de la cle API cote serveur uniquement
   - Rate limiting cote application

2. Patterns d'utilisation
   - Chat simple (messages.create)
   - Chat avec streaming (messages.stream)
   - Function calling (tools)
   - Agent autonome (boucle tool_use)

3. Bonnes pratiques
   - Gestion des erreurs exhaustive
   - Retry avec backoff exponentiel
   - Logging des requetes et reponses
   - Monitoring des couts

4. Securite
   - Ne jamais exposer la cle API cote client
   - Valider les entrees utilisateur
   - Limiter les permissions des outils
   - Sandboxer l'execution de code
```

---

## Exemples concrets

### Exemple 1 : Chat simple
```python
bot = ChatBot(system_prompt="Tu es un assistant Python expert.")
response = bot.chat("Comment implementer un singleton en Python ?")
print(response)
```

**Resultat attendu** : Explication du pattern Singleton avec code Python et cas d'usage.

### Exemple 2 : Agent avec outils
```python
result = agent_loop("Trouve la meteo a Paris et ecris un rapport dans weather.txt")
```

**Resultat attendu** : L'agent appelle get_weather("Paris"), puis write_file("weather.txt", rapport), puis task_complete.

### Exemple 3 : Streaming
```python
for chunk in bot.chat_stream("Ecris un module FastAPI de health check"):
    print(chunk, end="", flush=True)
```

**Resultat attendu** : Code affiche progressivement en temps reel.

---

## Effet sur le modele
- Le system prompt definit le comportement de base pour toute la conversation
- Le function calling permet d'etendre les capacites de Claude avec des outils externes
- La boucle d'agent (plan → execute → verify) produit des resultats plus fiables
- Le streaming ameliore la latence percue par l'utilisateur
- La gestion de l'historique impacte directement la qualite des reponses multi-turn
- Le choix du modele est le levier le plus impactant sur le rapport qualite/cout
