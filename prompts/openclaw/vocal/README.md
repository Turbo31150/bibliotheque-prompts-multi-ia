# OpenClaw - Vocal

## Vue d'ensemble

Controle vocal via OpenClaw : detection du wake word, dispatch STT vers l'agent adapte, reponse TTS. Pipeline complet voix-a-voix passant par JARVIS.

## Pipeline vocal

```
Micro -> Wake word -> STT -> OpenClaw dispatch -> Agent -> Reponse -> TTS -> Haut-parleurs
```

### Etapes detaillees

| Etape | Composant | Description |
|-------|-----------|-------------|
| 1. Capture | PulseAudio | Flux micro en continu |
| 2. Wake word | Porcupine/Vosk | Detection "Hey JARVIS" |
| 3. STT | Whisper (local) | Transcription parole -> texte |
| 4. Dispatch | OpenClaw auto-dispatch | Routage vers l'agent adapte |
| 5. Traitement | Agent cible | Execution de la requete |
| 6. TTS | jarvis-tts.sh | Synthese vocale de la reponse |

## Wake word

Configuration du mot declencheur :

```json
{
  "wake_word": {
    "engine": "porcupine",
    "keyword": "jarvis",
    "sensitivity": 0.7,
    "audio_device": "default"
  }
}
```

## STT - Speech to Text

Le module STT utilise Whisper en local :

```json
{
  "stt": {
    "engine": "whisper",
    "model": "base",
    "language": "fr",
    "device": "cuda"
  }
}
```

## Dispatch vocal

Le texte transcrit est envoye au systeme d'auto-dispatch OpenClaw qui determine l'agent cible :

| Mot-cle detecte | Agent | Exemple |
|-----------------|-------|---------|
| "trading", "bitcoin", "crypto" | trading-agent | "Quel est le prix du Bitcoin ?" |
| "serveur", "GPU", "cluster" | monitor-agent | "Statut des GPUs" |
| "LinkedIn", "post", "publier" | social-agent | "Publie un post LinkedIn" |
| "code", "git", "deploy" | dev-agent | "Deploie la derniere version" |
| Autre | general-agent | Questions generales |

## TTS - Text to Speech

Toutes les reponses vocales passent par le script JARVIS :

```bash
/home/turbo/jarvis-linux/scripts/jarvis-tts.sh "La reponse de l'agent"
```

## Commandes vocales speciales

| Commande | Action |
|----------|--------|
| "JARVIS, silence" | Desactive le TTS |
| "JARVIS, mode vocal" | Reactive le TTS |
| "JARVIS, repete" | Relit la derniere reponse |
| "JARVIS, annule" | Annule l'action en cours |
