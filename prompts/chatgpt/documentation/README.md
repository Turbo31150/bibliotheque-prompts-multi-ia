# ChatGPT -- Documentation

## Description

Prompts pour utiliser ChatGPT dans la redaction de documentation technique : guides d'installation, API docs, architecture, runbooks, changelogs et wikis internes. ChatGPT excelle dans la structuration et la vulgarisation de contenus techniques.

## Cas d'usage
- Documentation d'API et de bibliotheques
- Guides d'installation et de configuration
- Documentation d'architecture systeme
- Runbooks operationnels
- Changelogs et release notes

---

## Prompts prets a copier

### 1 -- Documenter une API

```
Documente cette API REST en generant une documentation complete :

## ENDPOINTS
[LISTER LES ENDPOINTS OU COLLER LE CODE]

## FORMAT DE DOCUMENTATION
Pour chaque endpoint :
1. Methode HTTP + URL
2. Description (1 phrase)
3. Headers requis
4. Parametres (path, query, body) avec types et contraintes
5. Reponse succes (code + schema JSON)
6. Reponses erreur (codes + messages)
7. Exemple curl complet
8. Exemple de reponse

Ajouter en introduction :
- Base URL
- Authentification
- Rate limiting
- Pagination
- Gestion des erreurs (format standard)
```

---

### 2 -- Rediger un guide d'installation

```
Redige un guide d'installation complet pour [LOGICIEL/PROJET] sur Linux :

## STRUCTURE
1. Prerequis (materiel, OS, dependances)
2. Installation pas a pas (commandes exactes)
3. Configuration initiale
4. Verification de l'installation
5. Configuration avancee (optionnel)
6. Troubleshooting (5 problemes frequents avec solutions)
7. Mise a jour
8. Desinstallation propre

## EXIGENCES
- Chaque commande doit etre dans un bloc de code
- Indiquer le shell attendu (bash, root, user)
- Tester chaque etape avec une commande de verification
- Mentionner les versions compatibles
- Inclure les commandes pour Ubuntu ET Arch Linux
```

---

### 3 -- Documenter l'architecture d'un systeme

```
Documente l'architecture de ce systeme :

## COMPOSANTS
[LISTER LES COMPOSANTS]

## DOCUMENTATION A PRODUIRE
1. VUE D'ENSEMBLE
   - Diagramme ASCII des composants et leurs connexions
   - Role de chaque composant (1 phrase)
   - Technologies utilisees

2. FLUX DE DONNEES
   - Diagramme de sequence pour les 3 flux principaux
   - Formats de donnees echanges (JSON schemas)

3. INFRASTRUCTURE
   - Machines et ressources
   - Reseau (ports, protocoles)
   - Stockage (volumes, partitions)

4. OPERATIONS
   - Deploiement (procedure)
   - Monitoring (metriques cles)
   - Backup (strategie)
   - Disaster recovery (RTO/RPO)

5. DECISIONS TECHNIQUES
   - ADR (Architecture Decision Records) pour les choix importants
```

---

### 4 -- Creer un runbook operationnel

```
Cree un runbook pour l'operation : [OPERATION]

## FORMAT
### Titre
### Quand l'executer
### Pre-requis
### Procedure pas a pas
(Chaque etape : commande + verification + resultat attendu)
### Points de controle
### Rollback
### Contacts / Escalade
### Historique des executions (template)

## EXIGENCES
- Niveau : executable par un junior sans connaissance prealable
- Temps estime pour chaque etape
- Commandes copy-paste (pas de variables a deviner)
- Screenshots ou outputs attendus decrits textuellement
```

---

### 5 -- Generer des release notes

```
Genere les release notes pour la version [VERSION] a partir de ces commits :

[COLLER LES COMMITS OU LE DIFF]

## FORMAT
### [VERSION] - [DATE]

#### Nouvelles fonctionnalites
- [Feature] : description orientee utilisateur

#### Ameliorations
- [Improvement] : ce qui a change et pourquoi

#### Corrections de bugs
- [Fix] : le bug et sa resolution

#### Breaking changes
- [Breaking] : ce qui casse et comment migrer

#### Notes de migration
- Etapes pour mettre a jour depuis la version precedente

## REGLES
- Langage oriente utilisateur (pas technique)
- Chaque entree tient sur 1-2 lignes
- Les breaking changes sont mis en evidence
```

---

## Exemples d'utilisation

### Exemple : Documenter un script
**Prompt** : "Documente ce script bash de 200 lignes [coller]. Genere : description, usage, options, exemples, dependances."

**Resultat attendu** : Documentation man-page style avec toutes les sections, prete a integrer dans le repo.

### Exemple : Architecture JARVIS
**Prompt** : "Documente l'architecture de JARVIS : 9 couches du boot au vocal, avec diagrammes ASCII."

**Resultat attendu** : Document structure avec diagramme en couches, flux de donnees et decisions techniques.

---

## Effet sur le modele
- ChatGPT excelle dans la structuration de documentation technique
- Les templates de format explicites produisent des documents homogenes et complets
- Demander des exemples copy-paste garantit une documentation actionnable
- Le niveau de detail "executable par un junior" force la clarte
