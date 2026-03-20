# Multi-IA -- Creation

## Description

Prompts pour orchestrer plusieurs IA dans la creation de projets : ideation avec ChatGPT, validation technique avec Claude, recherche d'etat de l'art avec Perplexity, et implementation avec Claude Code ou Gemini CLI.

## Cas d'usage
- Creation de projets avec validation multi-IA
- Brainstorming collaboratif multi-modeles
- Prototypage rapide avec specialisation des IA
- Revue croisee de code genere
- Documentation multi-perspectif

---

## Prompts prets a copier

### 1 -- Pipeline de creation de projet

```
## ETAPE 1 : Perplexity (recherche)
Recherche l'etat de l'art pour [TYPE DE PROJET] :
- Projets similaires existants
- Technologies recommandees en [ANNEE]
- Erreurs courantes a eviter

## ETAPE 2 : ChatGPT (ideation)
A partir de la recherche Perplexity, concois l'architecture :
- Composants et interactions
- Stack technique choisie (avec justification)
- Diagramme d'architecture

## ETAPE 3 : Claude (validation)
Revois l'architecture proposee par ChatGPT :
- Points forts et faiblesses
- Risques techniques
- Suggestions d'amelioration
- Estimation de complexite

## ETAPE 4 : Claude Code (implementation)
Implemente le projet valide :
- Structure de fichiers
- Code des composants principaux
- Tests unitaires
- Documentation

## ETAPE 5 : Gemini CLI (test)
Execute et teste le projet :
- Build et lancement
- Tests automatises
- Rapport de bugs
```

---

### 2 -- Brainstorming multi-IA

```
Sujet de brainstorming : [DESCRIPTION]

Soumets la meme question a 3 IA differentes :

## Claude
"Propose 10 idees innovantes pour [SUJET]. Pour chaque idee : description, faisabilite (1-5), originalite (1-5)."

## ChatGPT
"Propose 10 idees creatives pour [SUJET]. Pour chaque idee : description, impact potentiel, risques."

## Gemini
"Propose 10 idees pratiques pour [SUJET]. Pour chaque idee : description, technologies necessaires, effort."

## SYNTHESE
- Idees communes (haute validite)
- Idees uniques par IA (perspectives differentes)
- Top 5 final avec scores agreges
```

---

### 3 -- Revue croisee de code

```
Code a revoir : [COLLER OU CHEMIN]

## REVUE 1 : Claude
Focus sur la correction, la securite et les edge cases.

## REVUE 2 : ChatGPT
Focus sur la lisibilite, les patterns et la maintenabilite.

## REVUE 3 : Gemini
Focus sur la performance et les optimisations.

## SYNTHESE
- Bugs trouves par toutes les IA (a corriger en priorite)
- Suggestions unanimes (a implementer)
- Suggestions contradictoires (a arbitrer humainement)
- Score de qualite moyen
```

---

### 4 -- Generation et validation de documentation

```
## ETAPE 1 : Claude Code
Genere la documentation technique du projet dans [CHEMIN] :
- README, architecture, API, configuration

## ETAPE 2 : ChatGPT
Reecris la documentation pour qu'elle soit accessible a un debutant.
Ajoute des exemples et des analogies.

## ETAPE 3 : Perplexity
Verifie que les informations techniques sont correctes :
- Versions des outils mentionnees
- Liens fonctionnels
- Commandes a jour

## ETAPE 4 : Claude
Revue finale : coherence, completude, exactitude.
```

---

### 5 -- Prototypage rapide multi-IA

```
Prototype a creer : [DESCRIPTION]
Delai : 2 heures

## MINUTE 0-15 : Perplexity
Trouver le template/boilerplate le plus proche.
Identifier les librairies necessaires.

## MINUTE 15-30 : Claude
Designer l'architecture minimale.
Definir les interfaces (API, types, schemas).

## MINUTE 30-90 : Claude Code
Implementer le prototype :
- Code minimal viable
- Pas de polish, focus sur la fonctionnalite

## MINUTE 90-110 : Gemini CLI
Tester le prototype :
- Lancer et verifier
- Corriger les bugs bloquants

## MINUTE 110-120 : ChatGPT
Documenter le prototype :
- README rapide (installation, usage)
- Limites connues
- Prochaines etapes
```

---

## Exemples d'utilisation

### Exemple : Creer une CLI
**Workflow** : Perplexity (quel framework CLI ?) → Claude (architecture) → Claude Code (implementation) → Gemini CLI (test)

**Resultat attendu** : CLI fonctionnelle avec documentation, testee et validee.

---

## Effet sur le modele
- L'orchestration multi-IA couvre les forces de chaque modele
- La revue croisee reduit les bugs et ameliore la qualite
- La specialisation des taches (recherche, creation, validation) est plus efficace
- Le prototypage multi-IA est plus rapide que l'utilisation d'une seule IA
