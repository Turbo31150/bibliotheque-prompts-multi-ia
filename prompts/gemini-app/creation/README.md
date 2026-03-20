# Gemini App — Creation Multimodale

> Prompts optimises pour la creation multimodale avec Gemini App : images, documents, audio.

---

## Description

Gemini App excelle en creation multimodale grace a sa comprehension native des images, PDFs, audio et video. Elle permet d'analyser des visuels, de generer du contenu a partir de documents et de creer des architectures a partir de schemas.

## Configuration

- Gemini Advanced (Google One AI Premium) recommande
- AI Studio pour le controle fin des parametres
- Uploads : images, PDFs, audio, video supportes

## Prompts par type

### Analyse d'image technique
```
[UPLOADER L'IMAGE]

Analyse cette image technique :
1. Que montre-t-elle exactement ?
2. Composants identifies
3. Architecture / flux de donnees
4. Problemes potentiels detectes
5. Suggestions d'amelioration
```

### Extraction de donnees depuis un document
```
[UPLOADER LE PDF/DOC]

Extrais les informations cles de ce document :
1. Resume en 5 lignes
2. Points cles (bullet points)
3. Donnees chiffrees (tableau)
4. Actions requises
5. Questions ouvertes
```

### Creation a partir d'un schema
```
[UPLOADER LE SCHEMA/DIAGRAMME]

A partir de ce schema d'architecture :
1. Genere le code d'implementation pour chaque composant
2. Identifie les interfaces entre composants
3. Propose un plan d'implementation (ordre des taches)
4. Signale les risques techniques
```

### Analyse comparative d'images
```
[UPLOADER IMAGE_A ET IMAGE_B]

Compare ces deux [SCREENSHOTS/DESIGNS/ARCHITECTURES] :
1. Differences majeures
2. Avantages de chaque version
3. Recommendation pour [CAS_D_USAGE]
```

### Creation de contenu depuis audio/video
```
[UPLOADER L'AUDIO/VIDEO]

A partir de cet enregistrement :
1. Transcription complete
2. Resume structure
3. Points cles et decisions
4. Actions a suivre (qui, quoi, quand)
```

## Exemples concrets

```
[UPLOADER SCREENSHOT NVIDIA-SMI]

Analyse cette sortie nvidia-smi :
- Etat de sante de chaque GPU
- Temperatures anormales ?
- Processus qui consomment le plus de VRAM
- Recommendations pour optimiser l'utilisation
```

```
[UPLOADER SCHEMA D'ARCHITECTURE JARVIS]

A partir de ce schema :
1. Genere la structure de fichiers Python correspondante
2. Definis les interfaces (ABC/Protocol) entre chaque module
3. Propose un ordre d'implementation
4. Identifie les single points of failure
```

```
[UPLOADER PDF DE DOCUMENTATION TECHNIQUE]

Resume ce document technique :
- Ce que ca fait en 3 lignes
- API principales
- Limitations connues
- Pertinence pour mon projet (monitoring GPU Linux)
```

## Effet sur le modele

- Gemini est nativement multimodal — l'analyse d'images est plus naturelle que chez la concurrence
- L'upload de documents entiers (jusqu'a 1M tokens de contexte) permet une comprehension globale
- Pour les screenshots de code/terminal, Gemini extrait bien le texte et le contexte
- L'analyse video est une capacite unique — utile pour les tutoriels et presentations
- Attention : Gemini peut halluciner des details dans les images complexes — toujours verifier les chiffres extraits
