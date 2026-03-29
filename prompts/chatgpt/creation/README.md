# ChatGPT — Creation

> Prompts optimises pour la creation de features, applications et designs avec ChatGPT.

---

## Description

ChatGPT avec GPT-4o permet de creer des applications completes, des architectures systeme, des interfaces et des workflows. Sa force : la vision (analyser des maquettes), le Code Interpreter (prototyper en live) et la capacite a generer du code multi-fichier.

## Configuration

- Modele : GPT-4o
- Code Interpreter actif (prototypage rapide)
- DALL-E actif (generation de maquettes visuelles)
- Web Browsing (verifier les frameworks actuels)

## Prompts par type

### Creation d'application complete
```
Cree une application [TYPE] avec cette architecture :

## Objectif
[DECRIRE L'APPLICATION]

## Stack technique
- Backend : Python 3.13+ / FastAPI
- Frontend : [HTML/JS ou React]
- DB : [SQLite/PostgreSQL/Redis]
- Deploy : Docker

## Fonctionnalites
1. [FEATURE 1]
2. [FEATURE 2]
3. [FEATURE 3]

## Livrable
- Structure de fichiers complete
- Code fonctionnel pour chaque fichier
- Dockerfile
- README d'installation
```

### Creation de feature
```
Ajoute cette feature a mon projet existant :

## Projet actuel
[DECRIRE L'ARCHITECTURE EXISTANTE]

## Feature demandee
[DECRIRE LA FEATURE]

## Contraintes
- Ne pas casser l'existant
- Tests pour la nouvelle feature
- Migration de DB si necessaire
- Documentation mise a jour
```

### Creation d'architecture
```
Concois l'architecture pour : [SYSTEME]

Contraintes :
- [CONTRAINTES TECHNIQUES]
- [CONTRAINTES DE PERFORMANCE]
- [CONTRAINTES DE SECURITE]

Livrable :
1. Schema d'architecture (en ASCII ou Mermaid)
2. Liste des composants avec responsabilites
3. Flux de donnees
4. Points de failure et strategies de resilience
5. Estimation de complexite par composant
```

### Documentation de creation
```
Documente ce projet que je viens de creer :

[COLLER LE CODE / STRUCTURE]

Format :
- README.md avec installation et usage
- Architecture decision records (ADR) pour les choix techniques
- Diagramme de composants (Mermaid)
```

## Exemples concrets

```
Cree un dashboard de monitoring GPU en temps reel :

Stack : FastAPI backend, HTML/JS frontend (pas de framework lourd)
Features :
1. Temperatures GPU en temps reel (graphiques)
2. Utilisation VRAM par processus
3. Alertes si temp > 80C (notification browser)
4. Historique 24h en SQLite

Contrainte : doit tourner sur un cluster 6 GPUs (mix NVIDIA).
```

```
Concois l'architecture pour un systeme d'assistant vocal (JARVIS) :
- Wake word detection locale
- STT (Speech-to-Text) local
- LLM routing (local + cloud)
- TTS (Text-to-Speech) local
- Plugin system extensible
- Fonctionne sur Linux avec GPU
```

## Effet sur le modele

- GPT-4o excelle en creation d'architectures completes — il connait les patterns modernes
- Le Code Interpreter permet de prototyper et valider des composants en temps reel
- ChatGPT a tendance a sur-ingenierer — les contraintes de stack et de simplicite canalisent
- Le format "livrable explicite" force une sortie actionnable, pas theorique
- La vision permet d'analyser des maquettes UI et de generer le code correspondant
