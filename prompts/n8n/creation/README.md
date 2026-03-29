# n8n -- Creation

## Description

Workflows n8n pour creer des applications, des integrations et des automatisations visuelles. n8n permet de connecter des services sans code et de prototyper rapidement des pipelines.

## Cas d'usage
- Creation de workflows d'integration entre services
- Prototypage rapide d'automatisations
- Creation de bots (Slack, Discord, Telegram)
- Pipelines de traitement de donnees visuels
- Integrations API sans code

---

## Workflows prets a copier

### 1 -- Bot Slack/Discord avec IA

```
Webhook (message recu)
  -> IF (mention du bot ?)
    -> OUI : HTTP Request (API Claude/OpenAI)
      -> Code (formater la reponse)
      -> HTTP Request (repondre dans le canal)
    -> NON : ignore

## CONFIGURATION
- Webhook : URL du bot
- API IA : cle API, model, system prompt
- Format de reponse adapte a la plateforme
```

---

### 2 -- Pipeline de traitement d'emails

```
Email Trigger (nouveau mail)
  -> Code (extraire sujet, expediteur, corps)
  -> IF (priorite haute ?)
    -> OUI : HTTP Request (Claude : resume + action suggeree)
      -> Slack (notification avec resume)
    -> NON : Google Sheets (archiver)
  -> IF (contient pieces jointes ?)
    -> OUI : Move File (sauvegarder dans dossier)
```

---

### 3 -- Generateur de rapports automatique

```
Schedule (tous les lundis 8h)
  -> HTTP Request (API metriques : Prometheus, GitHub, etc.)
  -> Code (agreger les donnees)
  -> HTTP Request (Claude : generer le rapport)
  -> Send Email (rapport en HTML)
  -> Google Drive (sauvegarder le rapport)
```

---

### 4 -- Webhook → action multi-services

```
Webhook (evenement externe)
  -> Switch (type d'evenement)
    -> "deploy" : SSH (deployer sur serveur)
    -> "alert" : Slack + Email + TTS
    -> "backup" : SSH (lancer le backup)
    -> default : Log (evenement inconnu)
```

---

### 5 -- Formulaire → traitement → notification

```
n8n Form Trigger (soumission formulaire)
  -> Code (valider les donnees)
  -> IF (valide ?)
    -> OUI : Database (inserer) -> Email (confirmation)
    -> NON : Email (erreur de validation)
```

---

## Exemples d'utilisation

### Exemple : Bot IA
**Workflow** : Message Slack → Claude API → Reponse Slack

**Resultat attendu** : Bot qui repond intelligemment aux questions dans Slack.

---

## Effet sur le modele
- n8n rend les integrations visuelles et maintenables
- Les workflows sont versionnes et exportables en JSON
- La connexion directe aux APIs evite le code boilerplate
- Le mode webhook permet des automatisations event-driven
