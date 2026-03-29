# Claude API -- Migration

## Description

Prompts et patterns pour utiliser l'API Claude dans les migrations : portage automatise de code, conversion de formats, migration de schemas et validation de parite.

## Cas d'usage
- Portage de code automatise via API (batch)
- Conversion de formats de configuration
- Migration de schemas de base de donnees
- Validation de parite avant/apres migration
- Documentation automatique de la migration

---

## Prompts prets a copier

### 1 -- Portage de code en batch

```
async def port_code_batch(files: list, source_lang: str, target_lang: str) -> list:
    tasks = [port_single_file(f, source_lang, target_lang) for f in files]
    return await asyncio.gather(*tasks)

async def port_single_file(file_path: str, source: str, target: str) -> dict:
    code = read_file(file_path)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Porte ce code de {source} vers {target}. Conserve la logique, utilise les idiomes natifs du langage cible. Retourne uniquement le code porte.",
        messages=[{"role": "user", "content": code}]
    )
    return {"source": file_path, "ported_code": response.content[0].text}

## UTILISATION
- Portage PowerShell → Bash en batch
- Portage Python 2 → Python 3
- Portage JavaScript → TypeScript
```

---

### 2 -- Convertisseur de configurations

```
def convert_config(config: str, source_format: str, target_format: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Convertis cette configuration de {source_format} vers {target_format}. Preserve toutes les valeurs. Ajoute des commentaires pour les options qui n'ont pas d'equivalent direct.",
        messages=[{"role": "user", "content": config}]
    )
    return response.content[0].text

## CONVERSIONS SUPPORTEES
- Docker Compose v2 → v3
- Nginx → Caddy
- Apache → Nginx
- INI → YAML
- Makefile → script bash
- Systemd → Docker
```

---

### 3 -- Validateur de parite

```
def validate_parity(original: str, migrated: str, context: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Compare le code original et le code migre. Verifie la parite fonctionnelle. JSON: {parity: bool, differences: [{location, original_behavior, migrated_behavior, severity}], score: int}",
        messages=[{"role": "user", "content": f"Original ({context}):\n{original}\n\nMigre:\n{migrated}"}]
    )
    return json.loads(response.content[0].text)

## UTILISATION
- Post-portage : verifier que le code migre fait la meme chose
- Post-conversion : verifier que la config est equivalente
- Integrer dans le pipeline de migration
```

---

### 4 -- Generateur de scripts de migration

```
def generate_migration(source_schema: str, target_schema: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Genere le script de migration SQL pour passer du schema source au schema cible. Inclus : ALTER TABLE, migration de donnees, rollback.",
        messages=[{"role": "user", "content": f"Schema source:\n{source_schema}\n\nSchema cible:\n{target_schema}"}]
    )
    return response.content[0].text
```

---

### 5 -- Rapport de migration automatise

```
def migration_report(source: dict, target: dict, results: dict) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Redige un rapport de migration professionnel. Sections: resume, perimetre, resultats, problemes, metriques (avant/apres), recommandations.",
        messages=[{"role": "user", "content": json.dumps({"source": source, "target": target, "results": results})}]
    )
    return response.content[0].text
```

---

## Exemples d'utilisation

### Exemple : Portage batch
**Code** : `results = await port_code_batch(ps_files, "powershell", "bash")`

**Resultat attendu** : Tous les fichiers .ps1 portes en .sh avec logique preservee.

---

## Effet sur le modele
- Le batch processing avec asyncio.gather accelere les migrations volumineuses
- Sonnet pour le portage (comprehension de code requise)
- La validation de parite catch les erreurs de portage
- Les rapports automatises documentent la migration pour reference future
