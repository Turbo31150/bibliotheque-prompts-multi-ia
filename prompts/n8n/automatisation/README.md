# n8n — Automatisation JARVIS

> Généré par M1 cluster (gpt-oss-20b)

# Guide complet : Créer et gérer des workflows n8n pour orchestrer **JARVIS**

> Ce document est rédigé en français, au format Markdown, et s’adresse aux développeurs souhaitant automatiser les tâches de JARVIS à l’aide d’**n8n** (workflow automation platform).  
> Vous trouverez ci‑dessus un aperçu des 65 workflows existants, une description rapide de chacun, puis la procédure pas‑à‑pas pour créer un **nouveau workflow via l’API n8n**, avec plusieurs exemples `curl`.

---

## Table des matières

| # | Section |
|---|---------|
| 1 | Aperçu des workflows existants |
| 2 | Pré-requis techniques |
| 3 | Créer un nouveau workflow via l’API |
| 4 | Exemples curl détaillés |
| 5 | Bonnes pratiques & dépannage |
| 6 | Ressources supplémentaires |

---

## 1. Aperçu des workflows existants

> **JARVIS** est un système autonome qui interagit avec plusieurs services externes (GitHub, LinkedIn, Prometheus, etc.).  
> Les workflows ci‑dessous sont déjà déployés sur votre instance n8n et exécutés à l’intervalle défini.

| Workflow | Fréquence | Description |
|----------|-----------|-------------|
| **Health** | 15 min | Vérifie le statut des services JARVIS (CPU, RAM, temps de réponse). Envoie un webhook Slack si problème détecté. |
| **Trading** | Horaire (ex: 09:00‑16:30) | Récupère les données de marché, applique une stratégie de trading algorithmique et place des ordres via l’API Xchange. |
| **GPU Guard** | 10 min | Surveille la température du GPU ; si > 85°C, redémarre le serveur via SSH. |
| **Backup** | Quotidien (02:00) | Exporte les bases de données PostgreSQL et archive sur S3. |
| **LinkedIn** | Hebdomadaire (Lundi 08:00) | Publie un article automatisé avec contenu généré par GPT‑4. |
| **GitHub** | En continu (webhook) | Sur push, exécute CI/CD pipeline via GitHub Actions. |
| **Prometheus** | 1 min | Expose métriques personnalisées pour JARVIS (ex: nombre de requêtes API). |

> *Total : 65 workflows*  
> Vous pouvez les consulter dans l’interface n8n sous **Workflows → All Workflows**.

---

## 2. Pré‑requis techniques

| Item | Détails |
|------|---------|
| **Instance n8n** | Version ≥ 1.0 (Docker ou npm). L’API est accessible via `http://<HOST>:5678/api` par défaut. |
| **Token d’accès** | Créez un utilisateur API dans *Settings → Credentials* et notez le **Bearer Token**. |
| **curl** | Commande disponible sur Linux/MacOS; sous Windows utilisez Git Bash ou PowerShell `Invoke-RestMethod`. |
| **JSON** | Le payload du workflow doit être un JSON valide, conforme à la structure de n8n (`nodes`, `connections`, etc.). |

---

## 3. Créer un nouveau workflow via l’API

### Étape 1 : Préparer le fichier JSON

Vous pouvez exporter un workflow existant depuis l’interface et l’éditer, ou créer un fichier JSON à partir de zéro.

```json
{
  "name": "MonWorkflowExemple",
  "nodes": [
    {
      "parameters": { ... },
      "id": "12345678-90ab-cdef-1234-567890abcdef",
      "type": "n8n-nodes-base.httpRequest",
      "position": [250, 300]
    }
  ],
  "connections": { ... }
}
```

> **Astuce** : Utilisez l’export → *Export as JSON* pour copier la structure d’un workflow existant.

### Étape 2 : Authentifier la requête

Utilisez votre **Bearer Token** dans l’en‑tête `Authorization`.

```bash
curl -X POST "http://<HOST>:5678/api/workflows" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <YOUR_TOKEN>" \
     --data-binary @workflow.json
```

### Étape 3 : Vérifier la création

- La réponse `200 OK` contiendra le **ID** du workflow créé.
- Vous pouvez ensuite activer le workflow via l’interface ou via API :

```bash
curl -X POST "http://<HOST>:5678/api/workflows/<WORKFLOW_ID>/start" \
     -H "Authorization: Bearer <YOUR_TOKEN>"
```

---

## 4. Exemples curl détaillés

### 4.1 Créer un workflow simple (HTTP → Slack)

**workflow_http_slack.json**

```json
{
  "name": "Webhook to Slack",
  "nodes": [
    {
      "parameters": {
        "url": "https://hooks.slack.com/services/TOKEN/CHANNEL"
      },
      "id": "http1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [200,300]
    }
  ],
  "connections": {}
}
```

**curl**

```bash
curl -X POST "http://<HOST>:5678/api/workflows" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <TOKEN>" \
     --data-binary @workflow_http_slack.json
```

### 4.2 Créer un workflow qui lit un fichier CSV depuis S3 puis écrit dans BigQuery

**workflow_s3_to_bq.json**

```json
{
  "name": "S3 to BigQuery",
  "nodes": [
    {
      "parameters": { "bucketName":"my-bucket", "filePath":"data/input.csv" },
      "id":"s31",
      "type":"n8n-nodes-base.s3",
      "position":[200,200]
    },
    {
      "parameters":{
        "table":"dataset.table",
        "projectId":"my-project",
        "credentials":{...}
      },
      "id":"bq1",
      "type":"n8n-nodes-base.bigQuery",
      "position":[400,200]
    }
  ],
  "connections": {
    "s31": { "main":[ [{ "node":"bq1", "type":"main", "index":0 }] ] }
  }
}
```

**curl**

```bash
curl -X POST "http://<HOST>:5678/api/workflows" \
    