# Codex CLI -- Vocal

## Description

Prompts pour utiliser OpenAI Codex CLI dans la creation de systemes vocaux : pipelines STT/TTS, commandes vocales et integration audio.

## Cas d'usage
- Pipeline micro → transcription → action
- Integration Whisper local
- Commandes vocales pour le terminal
- Notifications TTS
- Tests de reconnaissance vocale

---

## Prompts prets a copier

### 1 -- Pipeline vocal basique

```
Cree un script bash : capture micro → Whisper → affiche le texte.
Utilise arecord pour la capture, whisper.cpp pour la transcription.
Detection de silence pour stop automatique.
```

### 2 -- Commandes vocales terminal

```
Cree un script qui ecoute des commandes vocales et les execute :
- "ouvre [app]" → lancer l'application
- "etat du systeme" → afficher CPU, RAM, GPU
- "eteins l'ecran" → xset dpms force off
Mapping configurable en YAML.
```

### 3 -- Notification TTS

```
Cree un wrapper qui lit un message a voix haute :
Usage : say.sh "Message a lire"
Utilise piper-tts ou jarvis-tts.sh.
```

### 4 -- Benchmark Whisper

```
Benchmarke Whisper sur 10 phrases de test en francais :
- Modeles : tiny, small, medium
- Mesure : WER, latence, CPU/GPU usage
- Rapport en tableau Markdown
```

### 5 -- Dictee vocale

```
Cree un outil de dictee vocale :
- Ecoute en continu
- Transcrit en temps reel
- Ecrit le texte dans le presse-papier ou un fichier
- Commande "stop dictee" pour arreter
```

---

## Effet sur le modele
- Codex CLI configure et teste Whisper directement sur le serveur
- Les scripts de pipeline vocal sont executables immediatement
- L'acces au materiel audio permet des tests reels
