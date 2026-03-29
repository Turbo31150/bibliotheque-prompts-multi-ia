# Gemini App -- Vocal

## Description

Prompts pour utiliser Gemini App dans la conception de systemes vocaux, le design d'interactions vocales et l'optimisation de l'experience utilisateur audio. Gemini App aide a conceptualiser et planifier les aspects vocaux avant l'implementation.

## Cas d'usage
- Design d'experiences vocales (VUI - Voice User Interface)
- Conception de dialogues pour assistants vocaux
- Redaction de scripts pour la synthese vocale
- Planification d'architectures STT/TTS
- Evaluation et amelioration de la qualite vocale

---

## Prompts prets a copier

### 1 -- Designer une interface vocale (VUI)

```
Designe l'interface vocale pour [APPLICATION/ASSISTANT] :

## PERSONA VOCAL
- Nom de l'assistant : [NOM]
- Personnalite : [TRAITS]
- Registre de langue : [FORMEL / CONVERSATIONNEL / TECHNIQUE]
- Voix : [GENRE, TONALITE, DEBIT]

## FLUX DE CONVERSATION
Pour chaque use case principal :
1. Phrase d'accueil / wake word
2. Ecoute et comprehension
3. Confirmation si ambiguite
4. Execution
5. Reponse vocale
6. Enchainement possible

## GESTION DES ERREURS VOCALES
- Pas compris → "Je n'ai pas compris. Pouvez-vous reformuler ?"
- Ambigu → "Vous voulez dire [A] ou [B] ?"
- Hors scope → "Je ne peux pas faire ca, mais je peux [ALTERNATIVE]."
- Timeout → "Etes-vous toujours la ?"

## PRINCIPES VUI
- Reponses < 3 secondes
- Phrases < 15 mots
- Pas de jargon technique dans les reponses
- Toujours donner un feedback audio (meme un "hmm" pendant le traitement)
```

---

### 2 -- Ecrire des dialogues conversationnels

```
Ecris les dialogues pour un assistant vocal domestique :

## SCENARIOS
1. L'utilisateur arrive a la maison
2. L'utilisateur demande la meteo
3. L'utilisateur programme une alarme
4. L'utilisateur controle la musique
5. L'utilisateur demande un resume de ses notifications

Pour chaque scenario, ecris :
- Le dialogue complet (utilisateur + assistant, 5-10 echanges)
- Les variantes de formulation de l'utilisateur (3 par intention)
- Les reponses adaptatives selon le contexte (heure, humeur detectee)
- Les transitions naturelles entre sujets
- Les moments d'humour ou de personnalite (dosés)

Ton : chaleureux, efficace, jamais condescendant.
```

---

### 3 -- Planifier l'architecture TTS/STT

```
Planifie l'architecture vocale pour [PROJET] :

## COMPOSANTS A EVALUER

### STT (Speech-to-Text)
| Solution | Latence | Qualite FR | Cout | Offline |
|----------|---------|------------|------|---------|
| Whisper local | ? | ? | ? | ? |
| Google STT | ? | ? | ? | ? |
| Azure Speech | ? | ? | ? | ? |
| Vosk | ? | ? | ? | ? |

### TTS (Text-to-Speech)
| Solution | Naturalite | Latence | Cout | Offline |
|----------|-----------|---------|------|---------|
| Piper TTS | ? | ? | ? | ? |
| Google TTS | ? | ? | ? | ? |
| ElevenLabs | ? | ? | ? | ? |
| Coqui TTS | ? | ? | ? | ? |

Remplis le tableau et recommande la meilleure combinaison pour :
- Budget limite (tout local/gratuit)
- Meilleure qualite (cloud acceptable)
- Meilleur compromis (hybride)
```

---

### 4 -- Optimiser les reponses pour la voix

```
Transforme ces reponses textuelles en reponses vocales naturelles :

## REPONSES A ADAPTER
[COLLER LES REPONSES]

## REGLES DE TRANSFORMATION
1. Longueur : max 2 phrases, max 20 mots par phrase
2. Structure : information principale en premier
3. Nombres : en toutes lettres si < 100
4. Abreviations : developper (CPU → processeur)
5. Unites : prononcees ("42 pour cent" pas "42%")
6. Listes : max 3 items, sinon resumer
7. Negativite : reformuler positivement quand possible
8. Prosodie : ajouter des virgules pour les pauses naturelles

Pour chaque reponse : version originale → version vocale → note de prosodie.
```

---

### 5 -- Evaluer la qualite vocale

```
Cree une grille d'evaluation pour la qualite d'un assistant vocal :

## CRITERES (note 1-5)

### COMPREHENSION
- Taux de reconnaissance correct
- Gestion des accents et parler naturel
- Gestion du bruit ambiant
- Reconnaissance des noms propres et termes techniques

### REPONSE
- Pertinence de la reponse
- Naturalite de la synthese vocale
- Debit et intonation
- Temps de reponse

### EXPERIENCE
- Fluidite du dialogue
- Gestion des erreurs
- Personnalite coherente
- Satisfaction utilisateur

### TECHNIQUE
- Fiabilite (pas de crash)
- Consommation ressources
- Fonctionnement offline
- Latence bout en bout

## PROTOCOLE DE TEST
- 20 commandes standard
- 10 commandes avec bruit
- 5 commandes ambigues
- 5 commandes hors scope
```

---

## Exemples d'utilisation

### Exemple : Design VUI
**Prompt** : "Designe l'interface vocale de JARVIS : personnalite, dialogues, gestion des erreurs."

**Resultat attendu** : Document complet de design vocal avec persona, flux et dialogues.

### Exemple : Reponses vocales
**Prompt** : "Transforme ces 10 messages systeme techniques en reponses vocales naturelles."

**Resultat attendu** : Reponses reformulees, courtes, naturelles et prononcables.

---

## Effet sur le modele
- Gemini App est bon pour le design creatif d'experiences vocales
- Les personas et traits de personnalite produisent des dialogues coherents
- Les contraintes de longueur et naturalite forcent des reponses vocales realistes
- La grille d'evaluation structure une demarche qualite reproductible
