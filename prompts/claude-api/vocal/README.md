# Claude API -- Vocal

## Description

Prompts et patterns pour utiliser l'API Claude dans les pipelines vocaux : NLU (Natural Language Understanding) via API, generation de reponses optimisees TTS, et orchestration de commandes vocales.

## Cas d'usage
- NLU via API (intent classification, entity extraction)
- Generation de reponses optimisees pour le TTS
- Orchestration de commandes vocales
- Conversation multi-turn vocale
- Pipeline STT → Claude API → TTS

---

## Prompts prets a copier

### 1 -- NLU via API Claude

```
def understand_command(transcript: str) -> dict:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        max_tokens=256,
        system="NLU pour assistant vocal Linux. Extrais l'intention et les entites. JSON strict: {intent: str, entities: {}, confidence: float, tts_response: str}",
        messages=[{"role": "user", "content": transcript}]
    )
    return json.loads(response.content[0].text)

## INTENTS SUPPORTES
- open_app, close_app, system_status, file_search
- set_volume, set_brightness, toggle_wifi
- run_command, create_timer, play_music

## EXEMPLE
understand_command("ouvre Firefox et mets le volume a cinquante")
→ {"intent": "multi_action", "entities": {"actions": [{"intent": "open_app", "app": "firefox"}, {"intent": "set_volume", "level": 50}]}, "confidence": 0.95, "tts_response": "J'ouvre Firefox et je mets le volume a cinquante pourcent."}
```

---

### 2 -- Pipeline vocal complet

```
Pipeline : micro → Whisper → Claude API → action → TTS

## CODE
async def vocal_pipeline():
    # 1. Capture audio
    audio = capture_microphone(silence_timeout=2.0)

    # 2. Transcription (Whisper local)
    transcript = whisper_transcribe(audio)

    # 3. Comprehension (Claude API)
    result = understand_command(transcript)

    # 4. Execution
    if result["confidence"] > 0.8:
        execute_action(result["intent"], result["entities"])
        speak(result["tts_response"])
    else:
        speak("Je n'ai pas bien compris. Pouvez-vous reformuler ?")

## OPTIMISATIONS
- Haiku pour la latence minimale
- Prompt caching pour le system prompt (static)
- Reponse TTS incluse dans la reponse NLU (1 seul appel API)
```

---

### 3 -- Conversation multi-turn vocale

```
class VocalConversation:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.messages = []
        self.system = "Tu es JARVIS, assistant vocal. Reponses courtes (< 20 mots). Pas d'abreviations. Nombres en lettres si < 100."

    def turn(self, transcript: str) -> str:
        self.messages.append({"role": "user", "content": transcript})
        response = self.client.messages.create(
            model="claude-haiku-3-5-20241022",
            max_tokens=100,
            system=self.system,
            messages=self.messages
        )
        reply = response.content[0].text
        self.messages.append({"role": "assistant", "content": reply})
        return reply

## UTILISATION
conv = VocalConversation()
conv.turn("Quel temps fait-il ?")  # → "Il fait vingt-deux degres, ciel degage."
conv.turn("Et demain ?")  # → "Demain, vingt-cinq degres avec des nuages le matin."
```

---

### 4 -- Generateur de reponses TTS

```
def tts_format(technical_response: str) -> str:
    response = client.messages.create(
        model="claude-haiku-3-5-20241022",
        max_tokens=100,
        system="Reformule pour la synthese vocale. Max 2 phrases, max 15 mots chacune. Nombres en lettres. Pas d'abreviations. Ton naturel et conversationnel.",
        messages=[{"role": "user", "content": technical_response}]
    )
    return response.content[0].text

## EXEMPLES
tts_format("CPU: 45%, RAM: 12.3/46GB, Disk: 234GB free")
→ "Le processeur tourne a quarante-cinq pourcent. Il reste deux cent trente-quatre giga de stockage."

tts_format("3 Docker containers running, 2 stopped")
→ "Trois conteneurs Docker sont actifs. Deux sont arretes."
```

---

### 5 -- Commande vocale avec confirmation

```
def vocal_command_with_confirmation(transcript: str) -> dict:
    # Premiere passe : comprendre la commande
    result = understand_command(transcript)

    # Si action destructive : demander confirmation
    destructive = ["delete", "restart", "shutdown", "format"]
    if result["intent"] in destructive:
        return {
            "needs_confirmation": True,
            "tts_prompt": f"Vous voulez {result['tts_response']}. Confirmez-vous ?",
            "pending_action": result
        }

    return {"needs_confirmation": False, "action": result}

## FLUX
1. "Supprime les logs de la semaine derniere"
2. → "Vous voulez supprimer les logs de la semaine derniere. Confirmez-vous ?"
3. "Oui, confirme"
4. → Execution + "Les logs ont ete supprimes."
```

---

## Exemples d'utilisation

### Exemple : Pipeline vocal
**Code** : `result = understand_command("montre-moi les temperatures des GPUs")`

**Resultat attendu** : `{"intent": "system_status", "entities": {"target": "gpu", "metric": "temperature"}, "confidence": 0.92, "tts_response": "Voici les temperatures des GPUs."}`

---

## Effet sur le modele
- Haiku est ideal pour le NLU vocal (latence < 500ms, cout minimal)
- Le prompt caching reduit la latence pour le system prompt statique
- La reponse TTS incluse dans le NLU evite un second appel API
- La conversation multi-turn garde le contexte pour les commandes enchainées
