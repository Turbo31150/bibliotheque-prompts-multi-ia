# Gemini App -- Documentation

## Description

Prompts pour utiliser Gemini App dans la creation de documentation technique de qualite : guides, references, tutoriels et documentation d'architecture. Gemini App gere bien les documents longs et structures.

## Cas d'usage
- Redaction de documentation utilisateur
- Creation de tutoriels pas a pas
- Documentation d'architecture et de decisions
- Guides de contribution et onboarding
- FAQ et troubleshooting

---

## Prompts prets a copier

### 1 -- Creer un tutoriel complet

```
Ecris un tutoriel complet pour [SUJET] :

## PUBLIC CIBLE : [DEBUTANT / INTERMEDIAIRE / AVANCE]
## PREREQUIS : [CE QUE LE LECTEUR DOIT SAVOIR]

## STRUCTURE
1. INTRODUCTION (pourquoi ce tutoriel, ce qu'on va apprendre)
2. CONCEPTS CLES (theorie minimale necessaire)
3. MISE EN PLACE (installation, configuration)
4. ETAPES PRATIQUES
   Pour chaque etape :
   - Objectif de l'etape
   - Instructions precises
   - Code ou commandes (copy-paste ready)
   - Resultat attendu (screenshot ou output)
   - Erreurs courantes et solutions
5. EXERCICE (le lecteur applique seul)
6. POUR ALLER PLUS LOIN (ressources, variations)

## REGLES
- Chaque concept nouveau est explique a sa premiere apparition
- Pas de saut logique (chaque etape decoule de la precedente)
- Le tutoriel complet est realisable en [DUREE]
```

---

### 2 -- Documenter une API interne

```
Documente cette API interne pour les developpeurs de l'equipe :

## API : [NOM / DESCRIPTION]

## FORMAT PAR ENDPOINT
### [METHODE] [URL]
**Description** : [1 phrase]
**Authentification** : [type]
**Parametres** :
| Nom | Type | Requis | Description | Defaut |
|-----|------|--------|-------------|--------|

**Reponse succes** (code [XXX]) :
```json
{ "exemple": "de reponse" }
```

**Erreurs** :
| Code | Message | Cause |
|------|---------|-------|

**Exemple** :
```bash
curl -X [METHOD] ...
```

**Notes** : [comportements speciaux, limites, deprecations]

Ajouter : guide de demarrage rapide, authentification, rate limits, pagination, webhooks si applicable.
```

---

### 3 -- Rediger un guide d'onboarding

```
Redige le guide d'onboarding pour un nouveau membre de l'equipe :

## PROJET : [NOM]

## JOUR 1 : Mise en place
- Acces a obtenir (liste avec qui contacter)
- Outils a installer (avec liens et versions)
- Repos a cloner
- Premier build / lancement du projet

## JOUR 2-3 : Comprendre le projet
- Architecture (diagramme + explication)
- Flux principaux (3 plus importants)
- Base de code (ou commencer a lire)
- Conventions de l'equipe (code style, git flow, PR process)

## SEMAINE 1 : Premiere contribution
- Bonne premiere issue a traiter
- Process de development (branch, code, test, PR)
- Qui demander pour quoi

## REFERENCES
- Documentation existante (liens)
- Personnes ressources par domaine
- FAQ des questions de nouveaux arrivants
```

---

### 4 -- Creer une documentation d'architecture (ADR)

```
Redige les Architecture Decision Records pour [PROJET] :

## FORMAT PAR ADR
### ADR-[NUMERO] : [TITRE]
**Date** : [DATE]
**Statut** : [propose / accepte / deprecie / remplace par ADR-X]

**Contexte** : Quel est le probleme ou la situation ?

**Decision** : Quelle decision a ete prise ?

**Alternatives considerees** :
| Option | Avantages | Inconvenients |
|--------|-----------|---------------|

**Consequences** :
- Positives : [liste]
- Negatives : [liste]
- Neutres : [liste]

## ADR A REDIGER
1. Choix du langage / framework
2. Architecture (monolithe vs micro-services)
3. Base de donnees
4. Strategie de deployment
5. Gestion des secrets
```

---

### 5 -- Ecrire un troubleshooting guide

```
Cree un guide de troubleshooting pour [SERVICE/APPLICATION] :

## FORMAT PAR PROBLEME
### Probleme : [DESCRIPTION]
**Symptome** : ce que l'utilisateur observe
**Cause probable** : explication technique
**Diagnostic** : commandes pour confirmer
**Solution** :
1. [Etape 1]
2. [Etape 2]
**Verification** : comment confirmer que c'est resolu
**Prevention** : comment eviter la recurrence

## PROBLEMES A COUVRIR
1. Le service ne demarre pas
2. Le service est lent
3. Le service crash / redémarre en boucle
4. Erreurs d'authentification
5. Problemes de connexion reseau
6. Espace disque insuffisant
7. Erreurs de permissions
8. Problemes apres mise a jour
9. Incompatibilite de configuration
10. Perte de donnees / corruption

Organiser par categorie et par frequence (plus courant en premier).
```

---

## Exemples d'utilisation

### Exemple : Tutoriel
**Prompt** : "Ecris un tutoriel pour installer et configurer Prometheus + Grafana sur Linux, niveau debutant."

**Resultat attendu** : Tutoriel complet de 2000+ mots, step by step, avec commandes et screenshots textuels.

### Exemple : ADR
**Prompt** : "Redige l'ADR pour le choix de SQLite vs PostgreSQL pour notre projet homelab."

**Resultat attendu** : ADR formel avec contexte, alternatives, decision et consequences.

---

## Effet sur le modele
- Gemini App gere bien les documents longs et structures
- Le format ADR produit des documents de decision professionnels
- Les guides step-by-step avec verification a chaque etape sont actionables
- La demande de FAQ force le modele a anticiper les questions courantes
