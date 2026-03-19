# Multi-IA -- Documentation

## Description

Prompts pour orchestrer plusieurs IA dans la creation de documentation : extraction par Gemini CLI, redaction par Claude, vulgarisation par ChatGPT, et verification par Perplexity.

## Cas d'usage
- Documentation generee et validee par plusieurs IA
- Documentation multi-niveau (technique + utilisateur)
- Verification d'exactitude par recherche
- Documentation vivante avec mise a jour multi-IA
- Traduction et adaptation multi-IA

---

## Prompts prets a copier

### 1 -- Documentation complete multi-IA

```
Projet a documenter : [CHEMIN]

## Gemini CLI (extraction)
"Lis le code source. Extrais :
- Structure, modules, fonctions publiques
- Configuration, dependances, entrypoints"

## Claude (documentation technique)
"A partir de l'extraction, redige :
- Architecture, API reference, configuration
- Diagrammes ASCII"

## ChatGPT (documentation utilisateur)
"Adapte la doc technique en guide utilisateur :
- Getting started (5 minutes)
- Tutoriel pas a pas
- FAQ"

## Perplexity (verification)
"Verifie les versions, commandes et liens dans la documentation.
Sont-ils a jour et corrects ?"
```

---

### 2 -- Documentation multi-niveau

```
Sujet : [FONCTIONNALITE]

## Claude (expert)
"Documentation technique detaillee :
- Architecture interne, algorithmes, performances
- Pour les developpeurs et mainteneurs"

## ChatGPT (intermediaire)
"Guide pratique :
- Comment l'utiliser, exemples, cas d'usage
- Pour les utilisateurs techniques"

## Gemini (debutant)
"Introduction accessible :
- Qu'est-ce que c'est, a quoi ca sert
- Premier pas en 5 minutes
- Pour les debutants"

Les 3 documents se referent mutuellement (liens croisees).
```

---

### 3 -- Mise a jour de documentation

```
Documentation existante : [CHEMIN]
Changements recents : [COMMITS / DIFF]

## Claude Code
"Identifie les parties de la documentation impactees par les changements.
Propose les mises a jour necessaires."

## ChatGPT
"Reformule les sections mises a jour pour la clarte.
Ajoute des exemples si le changement est significatif."

## Perplexity
"Les references externes dans la doc sont-elles encore valides ?
(URLs, versions de dependances, commandes)"
```

---

### 4 -- Documentation d'architecture

```
## Gemini CLI
"Analyse le projet dans [CHEMIN] :
- Technologies, structure, flux de donnees"

## Claude
"Redige le document d'architecture :
- Diagramme C4 (Context, Container, Component)
- ADRs pour les decisions cles
- Flux de donnees principaux"

## ChatGPT
"Ajoute des explications accessibles :
- Analogies pour les concepts complexes
- Scenario de bout en bout commente"

## Perplexity
"Verifie que les patterns architecturaux decrits sont corrects
et conformes aux definitions officielles."
```

---

### 5 -- Changelog et release notes multi-IA

```
## Gemini CLI
"Lis les commits depuis le dernier tag.
Extrais les changements par categorie."

## Claude
"Redige le changelog technique :
- Features, fixes, breaking changes
- Impact par changement"

## ChatGPT
"Adapte en release notes orientees utilisateur :
- Quoi de neuf pour l'utilisateur
- Comment migrer si breaking change
- Ton engageant"
```

---

## Exemples d'utilisation

### Exemple : Doc projet
**Workflow** : Gemini CLI (extraction) → Claude (technique) → ChatGPT (utilisateur) → Perplexity (verification)

**Resultat attendu** : Documentation complete, exacte et accessible.

---

## Effet sur le modele
- L'extraction par Gemini CLI garantit une documentation fidele au code
- Claude produit une documentation technique rigoureuse
- ChatGPT rend la documentation accessible
- Perplexity valide l'exactitude des references
