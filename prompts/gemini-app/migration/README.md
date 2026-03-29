# Gemini App -- Migration

## Description

Prompts pour utiliser Gemini App dans la planification de migrations : portage de code, migration d'infrastructure, changement de stack technique et transition de donnees.

## Cas d'usage
- Planification de migrations complexes
- Evaluation d'impact avant migration
- Conception de strategies de migration incrementale
- Documentation des procedures de migration
- Gestion des risques de migration

---

## Prompts prets a copier

### 1 -- Planifier une migration de stack

```
Planifie la migration de [STACK ACTUELLE] vers [STACK CIBLE] :

## ETAT ACTUEL
[DECRIRE L'INFRASTRUCTURE / APPLICATION ACTUELLE]

## OBJECTIF
[DECRIRE LA CIBLE ET LES MOTIVATIONS]

## PLAN DE MIGRATION
1. ANALYSE D'IMPACT
   - Composants affectes
   - Risques par composant (probabilite x impact)
   - Dependances bloquantes

2. STRATEGIE
   - Big bang vs incrementale vs strangler fig
   - Justification du choix
   - Coexistence ancien/nouveau pendant la transition

3. PHASES
   Pour chaque phase :
   - Objectif
   - Taches detaillees
   - Criteres de succes
   - Criteres de rollback
   - Duree estimee

4. TESTS
   - Tests de non-regression
   - Tests de performance comparative
   - Tests de charge

5. CUTOVER
   - Procedure de bascule
   - Point de non-retour
   - Plan de rollback complet
```

---

### 2 -- Evaluer la faisabilite d'une migration

```
Evalue la faisabilite de migrer [SOURCE] vers [CIBLE] :

## CRITERES D'EVALUATION
1. EFFORT : jours-homme estimes par composant
2. RISQUE : quels composants sont les plus risques
3. COMPATIBILITE : fonctionnalites supportees vs manquantes
4. PERFORMANCE : impact attendu (mieux, pareil, pire)
5. COUT : licence, infrastructure, formation, maintenance
6. TIMELINE : duree totale realiste

## FORMAT
Matrice de decision :
| Critere | Poids | Score /5 | Score pondere |
|---------|-------|----------|---------------|

Recommandation finale : GO / NO-GO / GO avec reserves.
Alternatives si NO-GO.
```

---

### 3 -- Migrer des donnees entre formats

```
Concois la strategie de migration de donnees de [FORMAT A] vers [FORMAT B] :

## DONNEES
- Volume : [TAILLE]
- Structure : [DESCRIPTION]
- Contraintes : [INTEGRITE, DOWNTIME, etc.]

## STRATEGIE
1. MAPPING : correspondance champ par champ
   | Source | Cible | Transformation | Notes |
   |--------|-------|---------------|-------|

2. VALIDATION
   - Regles de validation des donnees migrees
   - Checksums et comptages
   - Donnees de reference pour comparaison

3. EXECUTION
   - ETL pipeline (extract, transform, load)
   - Parallelisation si possible
   - Reprise sur erreur (idempotence)

4. VERIFICATION
   - Requetes de comparaison source vs cible
   - Tests applicatifs sur les donnees migrees
   - Rapport de migration (lignes traitees, erreurs, warnings)
```

---

### 4 -- Documenter une migration terminee

```
Documente cette migration pour reference future :

## MIGRATION : [SOURCE] → [CIBLE]
## DATE : [DATE]

## DOCUMENT A PRODUIRE
1. CONTEXTE : pourquoi cette migration
2. DECISIONS PRISES : quoi et pourquoi (ADR format)
3. PROCEDURE EXECUTEE : etapes reelles (pas le plan, ce qui s'est passe)
4. PROBLEMES RENCONTRES : et comment ils ont ete resolus
5. RESULTATS : metriques avant/apres
6. LECONS APPRISES : ce qu'on ferait differemment
7. REFERENCES : scripts, configs, documentation utilisee

Ce document servira de base pour les prochaines migrations similaires.
```

---

### 5 -- Gerer les risques de migration

```
Identifie et planifie la gestion des risques pour la migration [DESCRIPTION] :

## RISQUES PAR CATEGORIE
1. TECHNIQUES
   - Incompatibilites non detectees
   - Perte de donnees
   - Degradation de performance
   - Bugs introduits

2. ORGANISATIONNELS
   - Manque de competences sur la cible
   - Resistance au changement
   - Communication insuffisante

3. TEMPORELS
   - Depassement du planning
   - Downtime plus long que prevu
   - Fenetre de maintenance manquee

Pour chaque risque :
- Probabilite et impact
- Mesure preventive
- Plan de contingence si le risque se materialise
- Indicateur d'alerte precoce

Matrice des risques avec code couleur (vert/jaune/rouge).
```

---

## Exemples d'utilisation

### Exemple : Evaluer une migration
**Prompt** : "Est-ce faisable de migrer notre app Django vers FastAPI en 2 mois avec 2 devs ?"

**Resultat attendu** : Evaluation structuree avec effort par composant et recommandation GO/NO-GO.

### Exemple : Plan de migration
**Prompt** : "Planifie la migration de nos VMs vers des containers Docker, 15 services."

**Resultat attendu** : Plan phase par phase avec priorites, risques et procedures de rollback.

---

## Effet sur le modele
- Gemini App est efficace pour la planification strategique de migrations
- Les matrices de decision avec scores ponderes aident a prendre des decisions
- Les ADR (Architecture Decision Records) capturent le raisonnement
- Le format phase/risque/rollback produit des plans de migration robustes
