# Claude API -- Debug

## Description

Prompts et patterns pour utiliser l'API Claude dans le diagnostic et la resolution de bugs : analyse automatisee de stack traces, debug interactif avec outils, et detection de regressions.

## Cas d'usage
- Analyse automatisee de stack traces et erreurs
- Bot de debug interactif avec acces aux outils
- Detection de regressions via revue de code automatique
- Triage automatique de bugs (priorite, assignation)
- Post-mortem automatise

---

## Prompts prets a copier

### 1 -- Analyseur de stack traces automatise

```
def analyze_error(error: str, context: dict = None) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Expert en debug. Analyse l'erreur et reponds en JSON: {type, root_cause, file, line, fix_suggestion, severity, related_issues}",
        messages=[{"role": "user", "content": f"Erreur:\n{error}\n\nContexte:\n{json.dumps(context or {})}"}]
    )
    return json.loads(response.content[0].text)

## INTEGRATION CI
- Hook sur les erreurs en production → analyse automatique
- Triage par severite
- Suggestion de fix dans le ticket
- Lien vers les issues similaires passees
```

---

### 2 -- Bot de debug interactif

```
tools = [
    {"name": "read_file", "description": "Lit un fichier du projet"},
    {"name": "search_code", "description": "Recherche dans le code (grep)"},
    {"name": "run_test", "description": "Execute un test specifique"},
    {"name": "git_log", "description": "Affiche l'historique git"},
    {"name": "git_diff", "description": "Affiche les changements recents"}
]

## CONVERSATION
User: "Les tests d'integration echouent depuis le dernier merge"
Claude: [git_log] → [git_diff] → [read_file] → [run_test]
Claude: "Le commit abc123 a modifie le schema de la BDD sans mettre a jour les fixtures de test. Voici le fix..."

## SYSTEM PROMPT
"Tu es un debugger expert. Utilise les outils pour investiguer les bugs methodiquement. Commence par les hypotheses les plus probables."
```

---

### 3 -- Trieur automatique de bugs

```
def triage_bug(bug_report: str) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Triage de bugs. JSON: {priority: P1-P4, category, affected_component, reproducibility, estimated_effort, suggested_assignee_skill}",
        messages=[{"role": "user", "content": bug_report}]
    )
    return json.loads(response.content[0].text)

## CRITERES
- P1 : Blocage production, perte de donnees
- P2 : Fonctionnalite majeure cassee
- P3 : Bug mineur, workaround existe
- P4 : Cosmétique, amelioration
```

---

### 4 -- Detecteur de regressions

```
def check_regression(diff: str, test_results: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Analyse ce diff et les resultats de tests. Identifie les regressions potentielles non couvertes par les tests. JSON: [{file, change, risk, missing_test, suggestion}]",
        messages=[{"role": "user", "content": f"Diff:\n{diff}\n\nTests:\n{test_results}"}]
    )
    return json.loads(response.content[0].text)

## INTEGRATION
- Hook pre-merge dans la CI
- Bloque le merge si risque de regression eleve
- Suggere les tests manquants
```

---

### 5 -- Post-mortem automatise

```
def auto_postmortem(incident_data: dict) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Redige un post-mortem blame-free. Sections: resume, timeline, cause racine (5 whys), impact, actions correctives (immediat/court/long terme).",
        messages=[{"role": "user", "content": json.dumps(incident_data)}]
    )
    return response.content[0].text

## INPUT
incident_data = {
    "start": "2026-03-19T14:00:00",
    "end": "2026-03-19T16:30:00",
    "symptoms": "API 500 errors, 30% requests failing",
    "logs": "[extraits de logs]",
    "actions_taken": ["restart service", "rollback deploy"],
    "root_cause": "Database connection pool exhausted"
}
```

---

## Exemples d'utilisation

### Exemple : Analyse d'erreur
**Code** : `result = analyze_error("TypeError: Cannot read property 'id' of undefined", {"file": "api/users.js", "line": 42})`

**Resultat attendu** : `{"type": "null_reference", "root_cause": "User object not found before accessing id", "fix_suggestion": "Add null check: if (!user) return 404"}`

---

## Effet sur le modele
- L'API permet l'integration dans les pipelines CI/CD
- Haiku pour le triage rapide, Sonnet pour l'analyse approfondie
- Le tool_use permet un debug interactif avec acces au code reel
- L'automatisation reduit le temps de diagnostic de bugs courants
