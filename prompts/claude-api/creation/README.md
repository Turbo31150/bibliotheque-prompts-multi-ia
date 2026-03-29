# Claude API — Creation

## Description
Prompts et patterns pour creer des applications alimentees par l'API Claude : assistants specialises, pipelines de traitement, systemes multi-agents et integrations avec des services externes.

## Configuration requise
- SDK Anthropic (`pip install anthropic`)
- Cle API Anthropic configuree
- Python 3.9+ avec async/await
- FastAPI pour les applications web (optionnel)
- Redis pour le caching (optionnel)

---

## Prompts par type de tache

### Creation — Assistant specialise

```
Cree un assistant specialise pour [DOMAINE] avec l'API Claude :

## SPECIFICATION
1. System prompt expert [DOMAINE] (< 500 tokens)
2. Base de connaissances injectee dans le contexte
3. Outils specifiques au domaine
4. Gestion de la conversation multi-turn
5. Export des resultats (JSON, PDF, Markdown)

## ARCHITECTURE
class SpecializedAssistant:
    def __init__(self, domain: str, knowledge_base: str):
        self.client = anthropic.Anthropic()
        self.system = f"Tu es un expert en {domain}. {knowledge_base}"
        self.tools = self._build_domain_tools(domain)
        self.messages = []

    def ask(self, question: str) -> str:
        # Agent loop avec outils du domaine
        ...

## DOMAINES EXEMPLES
- Trading : outils scan, analyse, execution
- DevOps : outils monitoring, deployment, logs
- Legal : outils recherche jurisprudence, redaction
- Medical : outils symptomes, medicaments, references
```

---

### Creation — Pipeline de traitement de documents

```
Cree un pipeline de traitement de documents avec l'API Claude :

## ETAPES
1. INGESTION
   - Accepter : PDF, Markdown, texte, HTML
   - Extraire le texte brut
   - Decouper en chunks de 4000 tokens

2. ANALYSE
   - Pour chaque chunk : extraction d'entites, resume, classification
   - Modele : Haiku (rapide et economique pour l'extraction)

3. SYNTHESE
   - Agreger les resultats de tous les chunks
   - Generer un resume global
   - Modele : Sonnet (qualite pour la synthese)

4. EXPORT
   - JSON structure avec les entites et le resume
   - Markdown formate pour la lecture
   - Metadonnees (nombre de pages, tokens utilises, cout)

## CODE
async def process_document(file_path: str) -> dict:
    chunks = split_into_chunks(extract_text(file_path))

    # Analyse parallele des chunks (Haiku)
    analyses = await asyncio.gather(*[
        analyze_chunk(chunk, model="claude-haiku-3-5-20241022")
        for chunk in chunks
    ])

    # Synthese (Sonnet)
    summary = await synthesize(analyses, model="claude-sonnet-4-20250514")

    return {"analyses": analyses, "summary": summary}
```

---

### Creation — Systeme multi-agents

```
Cree un systeme multi-agents avec l'API Claude :

## ARCHITECTURE
3 agents specialises qui collaborent :

### Agent 1 — Planificateur (Opus)
- Recoit l'objectif global
- Decompose en sous-taches
- Assigne chaque sous-tache a l'agent le plus adapte
- Supervise l'avancement

### Agent 2 — Executeur (Sonnet)
- Recoit une sous-tache
- Execute avec les outils disponibles
- Rapporte le resultat au Planificateur

### Agent 3 — Verificateur (Sonnet)
- Recoit le resultat de l'Executeur
- Verifie la qualite et la completude
- Approuve ou demande une correction

## FLUX
Objectif → Planificateur → [Executeur → Verificateur] × N → Resultat final

## COMMUNICATION
Les agents communiquent via un message queue (asyncio.Queue ou Redis).
Chaque message contient : agent_source, agent_cible, type (task/result/feedback), contenu.

## IMPLEMENTATION
class MultiAgentSystem:
    def __init__(self):
        self.planner = Agent("planner", model="claude-opus-4-20250514")
        self.executor = Agent("executor", model="claude-sonnet-4-20250514")
        self.verifier = Agent("verifier", model="claude-sonnet-4-20250514")
        self.queue = asyncio.Queue()

    async def run(self, objective: str) -> str:
        plan = await self.planner.plan(objective)
        for task in plan.tasks:
            result = await self.executor.execute(task)
            verified = await self.verifier.verify(task, result)
            if not verified.approved:
                result = await self.executor.execute(task, feedback=verified.feedback)
        return await self.planner.synthesize(results)
```

---

### Creation — API wrapper avec FastAPI

```
Cree un wrapper FastAPI pour l'API Claude :

## ENDPOINTS
- POST /chat — Chat simple
- POST /chat/stream — Chat avec streaming (SSE)
- POST /analyze — Analyse de document
- POST /agent — Tache pour l'agent autonome
- GET /models — Liste des modeles disponibles
- GET /usage — Statistiques d'utilisation

## FEATURES
- Authentification par API key
- Rate limiting (100 req/min)
- Logging des requetes
- Caching des reponses (Redis)
- Monitoring des couts
- CORS configure

## CODE
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import anthropic

app = FastAPI(title="Claude API Wrapper")
client = anthropic.Anthropic()

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.messages.create(
        model=request.model,
        max_tokens=request.max_tokens,
        system=request.system,
        messages=request.messages
    )
    return {"response": response.content[0].text, "usage": response.usage}

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    async def generate():
        with client.messages.stream(...) as stream:
            for text in stream.text_stream:
                yield f"data: {text}\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")
```

---

### Amelioration / Refactoring — Ajouter le prompt caching

```
Ajoute le prompt caching Anthropic pour reduire les couts :

## CONCEPT
Le prompt caching permet de cacher les parties statiques du prompt
(system prompt, base de connaissances) pour ne payer que les tokens
variables a chaque requete.

## IMPLEMENTATION
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    system=[
        {
            "type": "text",
            "text": "Tu es un expert...",  # Cache apres le 1er appel
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[...]
)

## GAINS ATTENDUS
- Reduction de 90% du cout des tokens d'entree caches
- Reduction de la latence (pas de re-traitement du cache)
- Particulierement efficace pour les system prompts longs
```

---

### Debug — L'agent boucle indefiniment

```
L'agent autonome boucle sans terminer sa tache.

## DIAGNOSTIC
1. L'agent atteint-il la limite d'iterations ?
2. L'outil task_complete est-il bien defini et accessible ?
3. Le system prompt demande-t-il explicitement d'appeler task_complete ?
4. L'agent re-execute-t-il les memes actions en boucle ?
5. Les resultats des outils sont-ils informatifs (pas vides) ?

## SOLUTIONS
- Ajouter un compteur d'iterations avec limite (max 20)
- Ajouter un timeout global (5 minutes)
- Injecter un rappel "Tu as fait X iterations, appelle task_complete si termine"
- Logger chaque iteration pour debugger
- Verifier que les tool_results contiennent des donnees exploitables
```

---

### Documentation — Architecture d'une application Claude

```
Documente l'architecture d'une application basee sur l'API Claude :

## FORMAT
### 1. Vue d'ensemble
[Diagramme ASCII des composants]

### 2. Flux de donnees
[Sequence request → API Claude → response → client]

### 3. Gestion des erreurs
[Types d'erreurs et strategies de handling]

### 4. Couts et limites
[Estimation des couts par type de requete]
[Limites de rate et strategies de mitigation]

### 5. Securite
[Gestion de la cle API, validation des entrees, sandboxing]

### 6. Monitoring
[Metriques a suivre : latence, tokens, couts, erreurs]
```

---

## Exemples concrets

### Exemple 1 : Assistant trading
```python
assistant = SpecializedAssistant(
    domain="crypto trading",
    knowledge_base="Specialise MEXC et CoinEx. Indicateurs : RSI, MACD, Bollinger."
)
analysis = assistant.ask("Analyse BTC/USDT sur le timeframe 4h")
```

**Resultat attendu** : Analyse technique complete avec signal, niveaux, et recommandation.

### Exemple 2 : Pipeline de documents
```python
result = await process_document("rapport_annuel.pdf")
print(result["summary"])
```

**Resultat attendu** : Resume structure du document avec entites extraites et classification.

### Exemple 3 : Multi-agents
```python
system = MultiAgentSystem()
result = await system.run("Cree un module de monitoring avec tests et documentation")
```

**Resultat attendu** : Code + tests + docs generes par 3 agents collaborants.

---

## Effet sur le modele
- Les assistants specialises avec system prompt expert produisent des reponses de meilleure qualite
- Le pipeline multi-modeles (Haiku extraction + Sonnet synthese) optimise le rapport qualite/cout
- Le systeme multi-agents avec Planificateur/Executeur/Verificateur reduit les erreurs
- Le prompt caching reduit les couts de 90% pour les parties statiques
- Le wrapper FastAPI centralise la gestion des erreurs et le monitoring
- La boucle d'agent avec limite d'iterations et timeout evite les boucles infinies
