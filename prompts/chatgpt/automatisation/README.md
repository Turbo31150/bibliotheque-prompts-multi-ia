# ChatGPT — Automatisation

> Prompts optimises pour l'automatisation avec ChatGPT, APIs et Custom GPTs.

---

## Description

ChatGPT permet l'automatisation via son API (OpenAI API), les Custom GPTs (assistants pre-configures), et les integrations avec des outils tiers (Zapier, Make, n8n). Ce guide couvre les prompts pour creer des workflows automatises.

## Configuration

- Compte OpenAI avec acces API (cle API)
- Custom GPTs pour les assistants specialises
- Integrations : Zapier / Make / n8n pour les workflows
- Modeles API : `gpt-4o`, `gpt-4o-mini`

## Prompts par type

### Creation de Custom GPT
```
Cree un Custom GPT avec cette configuration :

## Nom : [NOM_DU_GPT]
## Description : [DESCRIPTION]

## Instructions systeme :
Tu es un assistant specialise en [DOMAINE].
Tu reponds en francais, format markdown.
Tu [COMPORTEMENT SPECIFIQUE].

## Actions (API) :
- Endpoint : [URL]
- Methode : [GET/POST]
- Parametres : [PARAMS]

## Knowledge base :
- [FICHIERS A UPLOADER]
```

### Automatisation API
```
Genere un script Python pour automatiser [TACHE] via l'API OpenAI :

## Workflow
1. [ETAPE 1]
2. [ETAPE 2]
3. [ETAPE 3]

## Contraintes
- Gestion des rate limits
- Retry avec backoff exponentiel
- Logging des couts (tokens in/out)
- Resultats en JSON
```

### Creation de workflow n8n/Zapier
```
Concois un workflow d'automatisation pour [OBJECTIF] :

## Trigger : [EVENEMENT DECLENCHEUR]
## Actions :
1. [ACTION 1] → [OUTIL]
2. [ACTION 2] → [OUTIL]
3. [ACTION 3] → [OUTIL]

## Format de sortie
- Schema du workflow (etapes + connexions)
- Configuration de chaque noeud
- Gestion des erreurs
- Estimation du cout API par execution
```

### Amelioration de workflow existant
```
Optimise ce workflow d'automatisation :

[DECRIRE LE WORKFLOW ACTUEL]

Problemes :
- [PROBLEME 1]
- [PROBLEME 2]

Objectifs :
- Reduire le cout API
- Ameliorer la fiabilite
- Ajouter du monitoring
```

## Exemples concrets

```
Genere un script Python qui automatise la veille technologique :
1. Appel API OpenAI pour analyser les 10 derniers articles HackerNews
2. Resume chaque article en 3 lignes
3. Classe par pertinence pour un dev Python/Linux/GPU
4. Envoie un digest quotidien par webhook Discord

Gestion rate limits, retry, logging des couts.
```

```
Cree un Custom GPT "JARVIS Code Reviewer" :
- Analyse les PRs GitHub (code colle dans le chat)
- Verifie : type hints, gestion erreurs, tests, securite
- Donne un score /10 par critere
- Suggest des ameliorations concretes
- Repond en francais
```

## Effet sur le modele

- ChatGPT connait bien les patterns d'automatisation (Zapier, Make, n8n)
- L'API OpenAI est bien documentee dans le training — les scripts generes sont generalement fonctionnels
- Les Custom GPTs sont efficaces pour pre-charger du contexte sans le repeter
- Attention aux couts API — demander systematiquement une estimation tokens/cout
- Le format "workflow etape par etape" produit des resultats plus fiables que "automatise tout"
