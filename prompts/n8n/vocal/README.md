# n8n -- Vocal

## Description

Workflows n8n pour integrer des fonctionnalites vocales : TTS, STT, commandes vocales par webhook et notifications vocales automatisees.

## Cas d'usage
- Notifications vocales automatisees (TTS)
- Transcription automatique d'audio
- Commandes vocales via webhook
- Pipeline audio dans les workflows
- Alertes vocales contextuelles

---

## Workflows prets a copier

### 1 -- Notification vocale sur alerte

```
Webhook (alerte monitoring)
  -> Code (formater le message pour TTS)
  -> SSH (executer jarvis-tts.sh sur le serveur)
  -> Slack (log de l'alerte vocale)
```

---

### 2 -- Transcription automatique

```
Webhook (fichier audio recu)
  -> HTTP Request (API Whisper ou Whisper local via SSH)
  -> Code (parser la transcription)
  -> Google Sheets (archiver la transcription)
  -> Slack (partager la transcription)
```

---

### 3 -- Commande vocale → action n8n

```
Webhook (transcription de commande vocale)
  -> HTTP Request (Claude : classifier l'intention)
  -> Switch (intention)
    -> "status" : SSH (diagnostic) -> TTS (resultat)
    -> "backup" : SSH (lancer backup) -> TTS (confirmation)
    -> "deploy" : SSH (deployer) -> TTS (resultat)
    -> default : TTS ("commande non reconnue")
```

---

### 4 -- Resume vocal du matin

```
Schedule (tous les jours 7h)
  -> HTTP Request (metriques systeme)
  -> HTTP Request (calendrier du jour)
  -> HTTP Request (meteo)
  -> HTTP Request (Claude : generer un resume vocal)
  -> SSH (jarvis-tts.sh avec le resume)
```

---

### 5 -- Meeting transcription pipeline

```
Webhook (enregistrement audio uploade)
  -> SSH (Whisper : transcrire)
  -> HTTP Request (Claude : resume, actions, decisions)
  -> Send Email (compte-rendu aux participants)
  -> Google Drive (archiver l'audio + transcription)
```

---

## Exemples d'utilisation

### Exemple : Alerte vocale
**Workflow** : Alerte Prometheus → n8n → jarvis-tts.sh → annonce vocale

**Resultat attendu** : Alerte critique annoncee vocalement sur les haut-parleurs.

---

## Effet sur le modele
- n8n orchestre le pipeline vocal sans code custom
- L'integration SSH permet d'executer TTS/STT sur le serveur local
- Le scheduling permet des routines vocales (resume du matin)
- Les webhooks permettent des commandes vocales event-driven
