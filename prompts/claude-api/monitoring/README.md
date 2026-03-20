# Claude API -- Monitoring

## Description

Prompts et patterns pour utiliser l'API Claude dans le monitoring : analyse intelligente de logs, alertes contextuelles, interpretation de metriques et generation de rapports automatises.

## Cas d'usage
- Analyse de logs par IA (pattern detection, anomalies)
- Alertes contextuelles (pas juste des seuils, mais du contexte)
- Interpretation automatique de metriques
- Generation de rapports de monitoring
- Chatbot de diagnostic systeme

---

## Prompts prets a copier

### 1 -- Analyseur de logs intelligent

```
Cree un analyseur de logs avec l'API Claude :

## ARCHITECTURE
class LogAnalyzer:
    def __init__(self):
        self.client = anthropic.Anthropic()

    def analyze(self, logs: str) -> dict:
        response = self.client.messages.create(
            model="claude-haiku-3-5-20241022",
            max_tokens=2048,
            system="Tu es un expert en analyse de logs Linux. Analyse les logs fournis et identifie les anomalies, erreurs et patterns suspects. Reponds en JSON.",
            messages=[{"role": "user", "content": f"Analyse ces logs :\n{logs}"}]
        )
        return json.loads(response.content[0].text)

## UTILISATION
- Injecter les logs toutes les heures (cron)
- Utiliser Haiku pour le cout reduit (logs volumineux)
- Parser la reponse JSON pour les alertes
- Stocker l'historique pour detecter les tendances
```

---

### 2 -- Alertes contextuelles via API

```
Cree un systeme d'alertes contextuelles avec l'API Claude :

## CONCEPT
Au lieu de "CPU > 90% → alerte", envoyer le contexte a Claude :
"CPU a 92% depuis 10 min, RAM a 85%, 3 containers redemarres, derniere alerte il y a 2h"
→ Claude decide si c'est une vraie alerte ou un comportement normal

## CODE
def should_alert(metrics: dict, history: list) -> dict:
    context = format_context(metrics, history)
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system="Tu es un SRE expert. Evalue si ces metriques necessitent une alerte. Reponds en JSON: {alert: bool, severity: str, reason: str, action: str}",
        messages=[{"role": "user", "content": context}]
    )
    return json.loads(response.content[0].text)

## AVANTAGES
- Moins de faux positifs (contexte > seuil brut)
- Alertes avec explication et action recommandee
- Adapte au comportement normal du systeme
```

---

### 3 -- Rapport de monitoring automatise

```
Genere un rapport de monitoring quotidien avec l'API Claude :

## PIPELINE
1. Collecter les metriques des dernières 24h (Prometheus API)
2. Formater en resume structure
3. Envoyer a Claude pour analyse et rapport

## CODE
def daily_report(metrics_24h: dict) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="Tu es un SRE qui redige un rapport quotidien. Analyse les metriques et produis un rapport clair avec : resume executif, anomalies detectees, tendances, recommandations. Format Markdown.",
        messages=[{"role": "user", "content": json.dumps(metrics_24h)}]
    )
    return response.content[0].text

## ENVOI
- Email du rapport chaque matin a 7h
- Version TTS du resume via jarvis-tts.sh
- Archivage dans ~/rapports/monitoring/
```

---

### 4 -- Chatbot de diagnostic

```
Cree un chatbot de diagnostic systeme avec l'API Claude :

## OUTILS
tools = [
    {"name": "check_cpu", "description": "Verifie l'utilisation CPU"},
    {"name": "check_memory", "description": "Verifie la RAM"},
    {"name": "check_disk", "description": "Verifie l'espace disque"},
    {"name": "check_gpu", "description": "Verifie les GPUs NVIDIA"},
    {"name": "check_services", "description": "Verifie les services systemd"},
    {"name": "read_logs", "description": "Lit les logs d'un service"}
]

## CONVERSATION
User: "Mon serveur est lent depuis ce matin"
Claude: [appelle check_cpu] → [appelle check_memory] → [appelle read_logs]
Claude: "Le CPU est a 95% a cause du processus X. Voici les options..."

## IMPLEMENTATION
Boucle d'agent avec tool_use pour un diagnostic interactif.
```

---

### 5 -- Detecteur d'anomalies

```
Cree un detecteur d'anomalies avec l'API Claude :

## CONCEPT
Envoyer les metriques normales comme contexte (prompt caching)
puis les metriques actuelles pour detection

## CODE
def detect_anomalies(baseline: dict, current: dict) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        system=[{
            "type": "text",
            "text": f"Metriques normales de reference : {json.dumps(baseline)}",
            "cache_control": {"type": "ephemeral"}
        }],
        messages=[{"role": "user", "content": f"Metriques actuelles : {json.dumps(current)}\nIdentifie les anomalies par rapport a la reference. JSON: [{{metric, value, baseline, deviation_pct, severity}}]"}]
    )
    return json.loads(response.content[0].text)

## AVANTAGES
- Baseline cachee (prompt caching → 90% reduction cout)
- Detection relative (pas de seuils absolus)
- Contextuelle (comprend les patterns normaux)
```

---

## Exemples d'utilisation

### Exemple : Alerte intelligente
**Code** : `result = should_alert({"cpu": 92, "ram": 85, "gpu_temp": [72,68,75,70,73,71]}, last_24h_history)`

**Resultat attendu** : `{"alert": false, "severity": "info", "reason": "CPU eleve mais stable, GPU temperatures normales", "action": "surveiller"}`

---

## Effet sur le modele
- Haiku est ideal pour l'analyse de logs (rapide, economique, suffisant)
- Le prompt caching reduit les couts pour les baselines repetitives
- Les outils (tool_use) permettent un diagnostic interactif
- Les alertes contextuelles reduisent significativement les faux positifs
