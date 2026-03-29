# Claude API -- Securite

## Description

Prompts et patterns pour utiliser l'API Claude dans la securite : analyse de code pour vulnerabilites, revue de configurations, detection d'anomalies dans les logs et automatisation d'audits.

## Cas d'usage
- SAST (Static Application Security Testing) via API
- Revue de securite automatisee de configurations
- Analyse de logs de securite
- Generation de politiques de securite
- Audit automatise de dependances

---

## Prompts prets a copier

### 1 -- Scanner de code securite

```
def security_scan(code: str, language: str) -> list:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Expert securite applicative. Analyse le code pour les vulnerabilites. JSON: [{line, vulnerability_type, severity_cvss, description, exploit_scenario, fix, cwe_id}]",
        messages=[{"role": "user", "content": f"Langage: {language}\n\n{code}"}]
    )
    return json.loads(response.content[0].text)

## INTEGRATION CI
- Pre-commit hook : scanner les fichiers modifies
- CI pipeline : scanner tout le codebase
- Bloquer le merge si vulnerabilite CVSS >= 7.0
```

---

### 2 -- Revue de configuration securite

```
def review_config(config: str, service: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Expert securite. Revois cette configuration {service}. JSON: {{score: int, issues: [{{setting, current, recommended, severity, risk}}], hardened_config: str}}",
        messages=[{"role": "user", "content": config}]
    )
    return json.loads(response.content[0].text)

## SERVICES SUPPORTES
- SSH (sshd_config)
- Nginx / Apache
- Docker / docker-compose
- PostgreSQL / MySQL
- Firewall (nftables, ufw)
```

---

### 3 -- Analyseur de logs de securite

```
def analyze_security_logs(logs: str) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Analyste securite. Analyse les logs d'authentification. JSON: {summary, threats: [{ip, attempts, usernames, time_pattern, threat_level, recommendation}], global_risk, immediate_actions}",
        messages=[{"role": "user", "content": logs}]
    )
    return json.loads(response.content[0].text)

## AUTOMATISATION
- Cron toutes les heures sur /var/log/auth.log
- Si threat_level == "high" → ban IP + alerte
- Rapport quotidien des tentatives
```

---

### 4 -- Generateur de politiques de securite

```
def generate_security_policy(context: dict) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Redige une politique de securite complete et professionnelle en Markdown. Couvre : acces, secrets, reseau, donnees, incidents, conformite.",
        messages=[{"role": "user", "content": f"Contexte: {json.dumps(context)}"}]
    )
    return response.content[0].text

## CONTEXTE
context = {
    "type": "homelab",
    "machines": 3,
    "services": ["docker", "ssh", "web", "gpu-compute"],
    "users": 1,
    "exposure": "ssh + reverse proxy"
}
```

---

### 5 -- Audit de dependances

```
def audit_dependencies(lockfile: str, package_manager: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system=f"Audit de securite des dependances ({package_manager}). Identifie les risques. JSON: {{total, risky: [{{name, version, risk, reason, recommendation}}], safe_count, summary}}",
        messages=[{"role": "user", "content": lockfile}]
    )
    return json.loads(response.content[0].text)

## NOTE
Claude identifie les risques structurels (dependances abandonnees, mainteneur unique).
Pour les CVE specifiques, combiner avec un outil dedié (npm audit, pip-audit).
```

---

## Exemples d'utilisation

### Exemple : Scan de code
**Code** : `vulns = security_scan(open("api.py").read(), "python")`

**Resultat attendu** : Liste des vulnerabilites avec severite, description et fix.

---

## Effet sur le modele
- Sonnet pour l'analyse de code (comprehension approfondie requise)
- Haiku pour l'analyse de logs (volume, cout)
- L'integration CI permet une securite continue
- Les schemas JSON structurent les resultats pour l'automatisation
