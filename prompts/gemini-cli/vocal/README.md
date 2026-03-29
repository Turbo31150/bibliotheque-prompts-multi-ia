# Gemini CLI -- Vocal

## Description

Prompts pour utiliser Gemini CLI dans la creation et l'optimisation de systemes vocaux : integration TTS/STT, commandes vocales, pipelines audio et assistants conversationnels en mode terminal.

## Cas d'usage
- Integration de Whisper pour la reconnaissance vocale
- Pipelines audio (enregistrement, transcription, action)
- Commandes vocales executees depuis le terminal
- Generation de configurations pour assistants vocaux
- Optimisation de grammaires vocales

---

## Prompts prets a copier

### 1 -- Creer un pipeline vocal complet

```
Cree un pipeline vocal bash : micro → transcription → action → reponse vocale

## COMPOSANTS
1. CAPTURE : arecord ou parec (PulseAudio/PipeWire)
   - Detection de silence pour stop automatique
   - Format : WAV 16kHz mono

2. TRANSCRIPTION : Whisper (local via whisper.cpp ou API)
   - Modele : medium (bon compromis vitesse/qualite)
   - Langue : francais
   - Output : texte brut

3. INTERPRETATION : matching regex ou NLU simple
   - Mapper le texte transcrit a une commande
   - Gerer les variantes ("ouvre", "lance", "demarre")
   - Fallback si commande non reconnue

4. EXECUTION : lancer la commande systeme

5. REPONSE : TTS via jarvis-tts.sh ou piper-tts
   - Confirmation courte de l'action
   - Resultat si pertinent

Script unique, executable, avec gestion des erreurs a chaque etape.
```

---

### 2 -- Configurer Whisper local

```
Configure Whisper pour la reconnaissance vocale locale optimale :

## SETUP
1. Installation de whisper.cpp (compile pour performance)
2. Telecharger le modele medium (ou large-v3 si GPU disponible)
3. Script wrapper bash :
   - Input : fichier WAV ou capture micro en direct
   - Options : langue, modele, format de sortie
   - Output : texte brut, SRT, ou JSON avec timestamps

## OPTIMISATION
- Utilisation du GPU (CUDA) si disponible
- Benchmark des modeles (tiny → large) sur le materiel
- Quantization pour reduire l'usage memoire
- Cache du modele en RAM pour les appels frequents

## TEST
- Jeu de test : 10 phrases en francais avec accents varies
- Mesurer : WER (Word Error Rate), latence, usage CPU/GPU
```

---

### 3 -- Creer un dictionnaire de commandes vocales

```
Genere un dictionnaire de commandes vocales pour piloter Linux :

## FORMAT PAR COMMANDE
nom: "open_application"
phrases:
  - "ouvre [APP]"
  - "lance [APP]"
  - "demarre [APP]"
  - "execute [APP]"
slots:
  APP: ["firefox", "terminal", "vscode", "nautilus", "discord"]
action: "[APP_CMD]"
confirmation: "J'ouvre [APP]"

## CATEGORIES (minimum 5 commandes par categorie)
1. Applications (ouvrir, fermer, basculer)
2. Systeme (volume, luminosite, wifi, bluetooth)
3. Fichiers (ouvrir dossier, chercher fichier, copier)
4. Monitoring (etat CPU, GPUs, RAM, disque)
5. Media (play, pause, suivant, volume)
6. Macros (mode travail, mode nuit, tout fermer)

Exporter en YAML et en JSON.
```

---

### 4 -- Optimiser la latence du pipeline vocal

```
Optimise la latence de mon pipeline vocal (actuel : [X] secondes) :

## PIPELINE ACTUEL
1. Capture audio : [duree]
2. Transcription Whisper : [duree]
3. Traitement commande : [duree]
4. TTS reponse : [duree]
Total : [X] secondes

## OPTIMISATIONS A EXPLORER
- Streaming : commencer la transcription pendant la capture
- Modele plus petit (tiny/base) pour les commandes courtes
- Prechargement du modele en memoire (daemon)
- VAD (Voice Activity Detection) pour couper plus tot
- Cache des reponses TTS frequentes (fichiers pre-generes)
- Paralleliser transcription et preparation de la reponse

Pour chaque optimisation : gain estime, implementation, compromis.
```

---

### 5 -- Tester et debugger la reconnaissance vocale

```
Cree une suite de tests pour le systeme de reconnaissance vocale :

## TESTS
1. PRECISION
   - 50 commandes predefinies lues a voix haute
   - Mesurer le taux de reconnaissance correcte
   - Identifier les commandes problematiques

2. ROBUSTESSE
   - Test avec bruit de fond (musique, ventilateur)
   - Test avec micro a distance (1m, 2m, 3m)
   - Test avec differentes voix (grave, aigue)

3. PERFORMANCE
   - Latence moyenne par commande
   - Usage CPU/GPU/RAM pendant la transcription
   - Temps de chargement du modele

4. REGRESSION
   - Comparer les resultats entre versions du modele
   - Comparer avant/apres changement de config

## OUTPUT
Script bash qui execute tous les tests et genere un rapport HTML.
```

---

## Exemples d'utilisation

### Exemple : Pipeline rapide
**Commande** : `gemini "Cree-moi un script qui ecoute le micro, transcrit avec Whisper, et execute la commande Linux correspondante"`

**Resultat attendu** : Script bash complet avec capture, transcription, matching et execution.

### Exemple : Optimisation
**Commande** : `gemini "Mon Whisper met 3 secondes par commande. Comment reduire a moins d'1 seconde ?"`

**Resultat attendu** : Plan d'optimisation avec benchmarks et implementations concretes.

---

## Effet sur le modele
- Gemini CLI peut tester les configurations audio directement sur le systeme
- L'acces au hardware (micro, GPU) permet des recommandations adaptees
- Les scripts generes sont executables et testables immediatement
- L'integration avec le filesystem local facilite la gestion des modeles et caches
