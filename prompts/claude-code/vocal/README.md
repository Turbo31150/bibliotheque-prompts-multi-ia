# Claude Code — Vocal

## Description
Pipeline vocal complet pour JARVIS via Claude Code : mot de reveil (wake word), transcription (STT Whisper), synthese vocale (TTS Piper), commandes vocales et integration dans le flux conversationnel.

## Configuration requise
- Claude Code avec MCP `voice-mcp` actif
- Piper TTS installe pour la synthese vocale
- Whisper (ou whisper.cpp) installe pour la transcription
- Script `/home/turbo/jarvis-linux/scripts/jarvis-tts.sh` fonctionnel
- Microphone et haut-parleurs connectes
- 898 commandes vocales existantes reparties en 5 modules

---

## Prompts par type de tache

### Creation — Nouvelle commande vocale

```
Ajoute une commande vocale JARVIS pour [ACTION].

## Systeme vocal JARVIS
- STT : Whisper (transcription)
- NLU : Classification par le cluster IA
- TTS : Piper (synthese vocale)
- Commandes existantes : 898
- Modules : 5 (systeme, media, domotique, trading, dev)

## Nouvelle commande
- Declencheur vocal : "[PHRASE_DECLENCHEUR]"
- Aliases : [LISTE_ALIASES]
- Module : [systeme/media/domotique/trading/dev]
- Action : [DESCRIPTION DE L'ACTION]
- Reponse vocale : "[TEXTE_A_PRONONCER]"

## Implementation
1. Ajouter dans src/commands.py (pattern matching)
2. Ajouter le handler dans le module concerne
3. Ajouter le test dans tests/test_commands.py
4. Mettre a jour la documentation des commandes
```

---

### Creation — Pipeline vocal complet

```
Cree un pipeline vocal complet pour [FONCTIONNALITE] :

## ARCHITECTURE
1. WAKE WORD — Detection du mot de reveil
   - Modele : Porcupine ou openWakeWord
   - Mot cle : "Hey JARVIS" ou "JARVIS"
   - Sensibilite : 0.7 (balance faux positifs / faux negatifs)

2. STT — Speech to Text
   - Moteur : Whisper (whisper.cpp pour la latence)
   - Modele : base.en ou small.en (compromis vitesse/precision)
   - Langue : francais
   - Timeout : 10 secondes de silence = fin de capture

3. NLU — Natural Language Understanding
   - Classifie l'intention (commande systeme, question, action)
   - Extrait les entites (nom de fichier, temperature, paire trading)
   - Route vers le bon module (systeme/media/domotique/trading/dev)

4. EXECUTION — Traitement de la commande
   - Appel au handler correspondant
   - Timeout : 30 secondes max
   - Fallback : "Je n'ai pas compris, peux-tu reformuler ?"

5. TTS — Text to Speech
   - Moteur : Piper
   - Voix : fr_FR-siwis-medium
   - Debit : 1.0x (normal)
   - Script : /home/turbo/jarvis-linux/scripts/jarvis-tts.sh

## FLUX
Micro → Wake Word → STT → NLU → Execution → TTS → Haut-parleur
```

---

### Amelioration / Refactoring — Optimiser la latence vocale

```
Optimise la latence du pipeline vocal :

## METRIQUES ACTUELLES
- Wake word → debut STT : [X]ms
- STT (transcription) : [X]ms
- NLU (classification) : [X]ms
- Execution (commande) : [X]ms
- TTS (synthese) : [X]ms
- Total : [X]ms

## OBJECTIFS
- Total < 2 secondes pour les commandes simples
- Total < 5 secondes pour les commandes complexes (IA)

## OPTIMISATIONS POSSIBLES
1. STT : utiliser un modele plus petit (tiny vs base)
2. STT : streaming (transcrire pendant que l'utilisateur parle)
3. NLU : cache des intentions frequentes
4. TTS : pre-generation des reponses courantes
5. TTS : streaming (commencer a parler avant la fin de la generation)
6. Pipeline : paralleliser NLU + pre-charge TTS
```

---

### Debug — La voix ne fonctionne pas

```
Le pipeline vocal ne fonctionne pas. Diagnostique :

Symptome : [DECRIRE — ex: JARVIS ne repond pas vocalement]

## CHECKLIST
1. Microphone detecte ? (arecord -l)
2. Haut-parleurs fonctionnent ? (aplay /usr/share/sounds/test.wav)
3. Wake word detecte ? (logs du processus wake word)
4. STT fonctionne ? (whisper --model base test.wav)
5. TTS fonctionne ? (echo "test" | piper --model fr_FR-siwis-medium)
6. Script jarvis-tts.sh executable ? (ls -la, bash -x jarvis-tts.sh "test")
7. MCP voice-mcp repond ? (test d'appel MCP)
8. Permissions audio ? (groups, pulseaudio/pipewire status)

Pour chaque etape en echec :
- Identifie la cause
- Corrige
- Verifie
```

---

### Debug — Mauvaise reconnaissance vocale

```
JARVIS comprend mal les commandes vocales.

Commande dite : "[CE_QUI_EST_DIT]"
Commande reconnue : "[CE_QUI_EST_TRANSCRIT]"

## ANALYSE
1. Le probleme est-il dans le STT (mauvaise transcription) ?
   - Tester avec un fichier audio enregistre
   - Comparer avec un modele plus grand (medium vs small)

2. Le probleme est-il dans le NLU (mauvaise classification) ?
   - La transcription est correcte mais l'intention est mal classee
   - Ajouter des aliases pour la commande

3. Le probleme est-il environnemental ?
   - Bruit de fond
   - Distance du microphone
   - Qualite du microphone

## SOLUTIONS
- STT : augmenter la taille du modele Whisper
- NLU : ajouter des variantes dans le pattern matching
- Environnement : configurer la suppression du bruit
```

---

### Documentation — Catalogue des commandes vocales

```
Genere le catalogue complet des commandes vocales JARVIS :

## FORMAT
Par module (5 modules) :

### Module Systeme
| Commande | Aliases | Action | Reponse vocale |
|----------|---------|--------|----------------|
| "Quel est le status du cluster" | "cluster check", "etat du cluster" | /cluster-check | "Le cluster est operationnel, 4 noeuds actifs" |
| ... | ... | ... | ... |

### Module Media
[...]

### Module Domotique
[...]

### Module Trading
[...]

### Module Dev
[...]

### Statistiques
- Total : 898 commandes
- Module le plus riche : [NOM] (N commandes)
- Commandes les plus utilisees (top 10)
```

---

## Exemples concrets

### Exemple 1 : Ajouter une commande vocale
```bash
claude "Ajoute la commande vocale 'lance les tests' qui execute uv run pytest et annonce le resultat"
```

**Resultat attendu** : Pattern matching ajoute dans commands.py, handler qui lance pytest, reponse vocale "X tests passes, Y echecs", test unitaire.

### Exemple 2 : Tester le TTS
```bash
claude "Fais dire a JARVIS 'Bonjour Turbo, le cluster est operationnel'"
```

**Resultat attendu** : Appel a jarvis-tts.sh, son joue sur les haut-parleurs.

### Exemple 3 : Diagnostiquer la latence
```bash
claude "Mesure la latence de chaque etape du pipeline vocal"
```

**Resultat attendu** : Tableau avec temps par etape (wake word, STT, NLU, execution, TTS) et recommandations.

---

## Effet sur le modele
- Le pipeline en 5 etapes (wake word → STT → NLU → execution → TTS) structure la reflexion
- Les 898 commandes existantes donnent un contexte riche pour l'ajout de nouvelles commandes
- Le pattern matching avec aliases ameliore le taux de reconnaissance
- La specification des modeles (Whisper, Piper) et de leurs parametres evite les ambiguites
- Le modele utilise systematiquement jarvis-tts.sh pour chaque reponse vocale
