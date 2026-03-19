# ChatGPT -- Vocal

## Description

Prompts pour utiliser ChatGPT dans la conception et l'optimisation de systemes vocaux : commandes vocales, TTS, reconnaissance vocale, assistants conversationnels. ChatGPT aide a structurer les grammaires vocales et a designer les flux d'interaction.

## Cas d'usage
- Conception de grammaires de commandes vocales
- Optimisation de prompts pour assistants vocaux
- Design de flux conversationnels voice-first
- Integration TTS / STT dans des applications
- Tests et debug d'interactions vocales

---

## Prompts prets a copier

### 1 -- Concevoir une grammaire de commandes vocales

```
Concois une grammaire de commandes vocales pour piloter un systeme Linux :

## CATEGORIES
1. Navigation fichiers : "ouvre le dossier X", "liste les fichiers de Y"
2. Controle systeme : "eteins l'ecran", "monte le volume", "redemarre le service X"
3. Applications : "lance Firefox", "ferme le terminal", "ouvre VS Code"
4. Monitoring : "quel est l'etat du CPU", "montre les GPUs"
5. Macros : "mode travail", "mode gaming", "mode nuit"

Pour chaque commande :
- Phrase principale + 3 variantes acceptees
- Regex de matching
- Action systeme associee (commande bash)
- Reponse TTS de confirmation

Format : tableau par categorie.
```

---

### 2 -- Designer un flux conversationnel

```
Designe un flux conversationnel complet pour un assistant vocal domotique :

## CONTRAINTES
- Reponses courtes (< 15 mots pour le TTS)
- Desambiguation en 1 question maximum
- Fallback gracieux si commande non comprise
- Confirmation avant actions destructives
- Support du contexte ("et dans la chambre aussi")

## SCENARIOS A COUVRIR
1. Allumer/eteindre des lumieres
2. Regler la temperature
3. Lancer de la musique
4. Programmer une alarme
5. Demander un statut ("tout est ferme ?")

Pour chaque scenario : arbre de decision avec les branches possibles.
```

---

### 3 -- Optimiser des reponses pour TTS

```
Reecris ces reponses techniques pour qu'elles soient naturelles en synthese vocale :

## REGLES
- Maximum 20 mots par phrase
- Pas d'abreviations (CPU → processeur, RAM → memoire vive)
- Pas de caracteres speciaux ou symboles
- Nombres en toutes lettres quand < 100
- Pourcentages lus naturellement ("soixante-quinze pourcent")
- Pauses naturelles avec des virgules
- Ton conversationnel, pas robotique

## REPONSES A RECRIRE
1. "CPU: 45%, RAM: 12.3/46GB, GPU0: 72°C"
2. "Service nginx (PID 1234) is running on port 443"
3. "Error: ENOSPC - /dev/sda1 is 98% full"
4. "3 containers running, 2 stopped, 1 restarting (crash loop)"
5. "Backup completed: 234GB in 1h23m, next run at 03:00"
```

---

### 4 -- Creer un systeme de wake word et intents

```
Concois l'architecture d'un systeme de reconnaissance d'intentions vocales :

## COMPOSANTS
1. Wake word : "Hey JARVIS" → activation
2. STT : Whisper local (modele medium)
3. NLU : Classification d'intention + extraction d'entites
4. Action : Execution de la commande
5. TTS : Reponse vocale

## INTENTS A DEFINIR (minimum 20)
Pour chaque intent :
- Nom technique (snake_case)
- 10 exemples de phrases d'entrainement
- Entites a extraire (slots)
- Action associee
- Reponse type

Exemples d'intents : system_status, open_app, search_files, set_timer, play_music...
```

---

### 5 -- Debugger des problemes de reconnaissance vocale

```
Mon systeme de commandes vocales a un taux d'erreur de [X]% sur ces commandes :

## ERREURS FREQUENTES
[LISTER : commande dite → commande reconnue]

Analyse les erreurs et :
1. Identifie les patterns (sons confondus, mots similaires)
2. Propose des reformulations des commandes problematiques
3. Suggere des mots-cles alternatifs moins ambigus
4. Recommande des ajustements de la grammaire
5. Propose un plan de test pour valider les corrections
```

---

## Exemples d'utilisation

### Exemple : Grammaire pour monitoring vocal
**Prompt** : "Cree les commandes vocales pour demander l'etat des 6 GPUs avec variantes naturelles."

**Resultat attendu** : Liste de commandes ("montre les GPUs", "temperature des cartes graphiques", "etat du cluster GPU") avec les actions nvidia-smi associees et les reponses TTS formatees.

### Exemple : Reponses TTS optimisees
**Prompt** : "Reformule 'GPU0: 72C, GPU1: 68C, GPU2: 75C' pour le TTS."

**Resultat attendu** : "Les temperatures GPU sont normales. La plus chaude est a soixante-quinze degres, la plus froide a soixante-huit."

---

## Effet sur le modele
- ChatGPT comprend bien les contraintes de naturalite du langage parle
- Fournir des exemples concrets de phrases permet de generer des variantes coherentes
- Specifier la longueur maximale des reponses TTS produit des textes reellement prononçables
- Le contexte JARVIS/Linux permet des commandes vocales specifiques et utiles
