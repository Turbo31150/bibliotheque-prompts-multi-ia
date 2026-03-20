# Claude API -- Documentation

## Description

Prompts et patterns pour utiliser l'API Claude dans la generation automatique de documentation : docstrings, README, API docs, changelogs et guides utilisateur.

## Cas d'usage
- Generation automatique de docstrings et commentaires
- Creation de README a partir du code source
- Documentation d'API automatisee
- Changelog automatique depuis git
- Guides utilisateur generes par IA

---

## Prompts prets a copier

### 1 -- Generateur de docstrings

```
def add_docstrings(code: str, language: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Ajoute des docstrings/commentaires a ce code {language}. Format : description, parametres, retour, exceptions. Ne modifie PAS le code, ajoute uniquement la documentation.",
        messages=[{"role": "user", "content": code}]
    )
    return response.content[0].text

## INTEGRATION
- Pre-commit hook : documenter les nouvelles fonctions
- CI : verifier que toutes les fonctions publiques sont documentees
- Batch : documenter un codebase legacy
```

---

### 2 -- Generateur de README

```
def generate_readme(project_structure: str, main_files: dict) -> str:
    context = f"Structure:\n{project_structure}\n\nFichiers principaux:\n"
    for path, content in main_files.items():
        context += f"\n--- {path} ---\n{content}\n"

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Genere un README.md professionnel. Sections: description, installation, usage, configuration, API (si applicable), contribution, licence.",
        messages=[{"role": "user", "content": context}]
    )
    return response.content[0].text
```

---

### 3 -- Changelog automatique

```
def generate_changelog(commits: list) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Genere un changelog au format Keep a Changelog. Classe les commits par type (Added, Changed, Fixed, Removed). Fusionne les commits lies. Version semantique suggeree.",
        messages=[{"role": "user", "content": json.dumps(commits)}]
    )
    return response.content[0].text

## AUTOMATISATION
- Hook post-release : generer le changelog
- CI : mettre a jour CHANGELOG.md automatiquement
```

---

### 4 -- Documentation d'API automatique

```
def document_api(routes_code: str, framework: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Genere la documentation API en Markdown pour ce code {framework}. Pour chaque endpoint : methode, URL, description, parametres, reponses (succes + erreur), exemple curl.",
        messages=[{"role": "user", "content": routes_code}]
    )
    return response.content[0].text
```

---

### 5 -- Guide utilisateur automatique

```
def generate_user_guide(app_code: str, target: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Genere un guide utilisateur pour un public {target}. Pas de jargon technique sauf si {target}=='developpeur'. Sections : getting started, fonctionnalites, FAQ, troubleshooting.",
        messages=[{"role": "user", "content": app_code}]
    )
    return response.content[0].text
```

---

## Exemples d'utilisation

### Exemple : README automatique
**Code** : `readme = generate_readme(tree_output, {"main.py": code, "config.yaml": config})`

**Resultat attendu** : README.md professionnel genere a partir du code source.

---

## Effet sur le modele
- Sonnet pour la documentation (comprehension de code + qualite redactionnelle)
- Le batch processing documente un codebase complet en minutes
- L'integration CI/CD maintient la documentation a jour automatiquement
- Le prompt caching pour le code source reduit le cout des iterations
