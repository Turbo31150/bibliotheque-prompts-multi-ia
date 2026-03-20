# Claude API -- Automatisation

## Description

Prompts et patterns pour utiliser l'API Claude dans l'automatisation : agents autonomes, pipelines de traitement, orchestration de taches et workflows intelligents.

## Cas d'usage
- Agents autonomes avec boucle d'outils
- Pipelines de traitement de donnees
- Orchestration de taches complexes
- Workflows conditionnels intelligents
- Automatisation event-driven

---

## Prompts prets a copier

### 1 -- Agent autonome avec outils

```
tools = [
    {"name": "run_command", "description": "Execute une commande bash"},
    {"name": "read_file", "description": "Lit un fichier"},
    {"name": "write_file", "description": "Ecrit un fichier"},
    {"name": "http_request", "description": "Fait une requete HTTP"},
    {"name": "task_complete", "description": "Signale la fin de la tache"}
]

async def run_agent(objective: str, max_iterations: int = 20):
    messages = [{"role": "user", "content": objective}]

    for i in range(max_iterations):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            system="Tu es un agent autonome. Utilise les outils pour accomplir l'objectif. Appelle task_complete quand termine.",
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Traiter les tool_use
        for content in response.content:
            if content.type == "tool_use":
                result = execute_tool(content.name, content.input)
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": content.id, "content": result}]})
```

---

### 2 -- Pipeline de traitement de donnees

```
async def data_pipeline(input_data: list) -> list:
    # Etape 1 : Nettoyage (Haiku, parallele, econome)
    cleaned = await asyncio.gather(*[
        clean_item(item, model="claude-haiku-3-5-20241022")
        for item in input_data
    ])

    # Etape 2 : Enrichissement (Sonnet, qualite)
    enriched = await asyncio.gather(*[
        enrich_item(item, model="claude-sonnet-4-20250514")
        for item in cleaned
    ])

    # Etape 3 : Validation (Haiku, rapide)
    validated = await asyncio.gather(*[
        validate_item(item, model="claude-haiku-3-5-20241022")
        for item in enriched
    ])

    return [item for item in validated if item["valid"]]

## MODELES
- Haiku : nettoyage et validation (volume, cout)
- Sonnet : enrichissement (qualite requise)
```

---

### 3 -- Orchestrateur de taches

```
def orchestrate(plan: list) -> list:
    results = []
    for task in plan:
        if task.get("depends_on"):
            # Attendre les dependances
            deps = [r for r in results if r["id"] in task["depends_on"]]
            task["context"] = deps

        result = execute_task(task)
        results.append(result)

        if not result["success"] and task.get("critical"):
            rollback(results)
            raise Exception(f"Tache critique echouee : {task['name']}")

    return results

def execute_task(task: dict) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Execute cette tache et retourne le resultat en JSON.",
        tools=task.get("tools", []),
        messages=[{"role": "user", "content": json.dumps(task)}]
    )
    return {"id": task["id"], "success": True, "output": response.content[0].text}
```

---

### 4 -- Workflow event-driven

```
class EventDrivenWorkflow:
    def __init__(self):
        self.handlers = {}
        self.client = anthropic.Anthropic()

    def on(self, event_type: str, handler):
        self.handlers[event_type] = handler

    def trigger(self, event: dict):
        handler = self.handlers.get(event["type"])
        if handler:
            # Claude decide de l'action basee sur l'evenement
            response = self.client.messages.create(
                model="claude-haiku-3-5-20241022",
                system=f"Evenement recu. Decide l'action. JSON: {{action, params, priority}}",
                messages=[{"role": "user", "content": json.dumps(event)}]
            )
            action = json.loads(response.content[0].text)
            handler(action)

## EVENEMENTS
workflow.on("file_created", handle_new_file)
workflow.on("service_down", handle_service_failure)
workflow.on("alert_triggered", handle_alert)
```

---

### 5 -- Cron intelligent

```
def smart_cron(task_description: str, system_state: dict) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Decide si cette tache planifiee doit s'executer maintenant. JSON: {should_run: bool, reason: str, delay_minutes: int}",
        messages=[{"role": "user", "content": f"Tache: {task_description}\nEtat systeme: {json.dumps(system_state)}"}]
    )
    return json.loads(response.content[0].text)

## EXEMPLE
# Tache : "docker system prune"
# Etat : CPU 95%, 3 containers en cours de build
# → {"should_run": false, "reason": "Build en cours, attendre la fin", "delay_minutes": 30}
```

---

## Exemples d'utilisation

### Exemple : Agent autonome
**Code** : `result = await run_agent("Installe et configure Prometheus sur ce serveur")`

**Resultat attendu** : Agent qui execute les commandes, gere les erreurs et installe Prometheus.

---

## Effet sur le modele
- Le tool_use permet des agents vraiment autonomes
- Le multi-model (Haiku/Sonnet) optimise le rapport cout/qualite
- L'orchestration avec dependances gere les workflows complexes
- Le cron intelligent evite d'executer des taches au mauvais moment
