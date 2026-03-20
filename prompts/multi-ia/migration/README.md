# Multi-IA -- Migration

## Description

Prompts pour orchestrer plusieurs IA dans les migrations : planification avec Claude, recherche avec Perplexity, execution avec Gemini CLI, et validation avec ChatGPT.

## Cas d'usage
- Migration planifiee et validee par consensus multi-IA
- Portage de code avec revue croisee
- Migration de donnees avec verification multi-IA
- Documentation de migration multi-perspectif
- Rollback planifie et teste

---

## Prompts prets a copier

### 1 -- Migration planifiee multi-IA

```
Migration : [SOURCE] → [CIBLE]

## Perplexity (recherche)
"Guide de migration officiel. Breaking changes. Retours d'experience. Outils existants."

## Claude (planification)
"Plan de migration phase par phase :
- Inventaire, preparation, execution, validation, rollback
- Risques par phase et mitigations"

## ChatGPT (documentation)
"Procedure step-by-step executable par un junior :
- Chaque etape avec commandes exactes
- Verification et rollback"

## Gemini CLI (execution)
"Execute la migration phase par phase.
Verifie apres chaque phase.
Rollback si echec."
```

---

### 2 -- Portage de code multi-IA

```
Code a porter : [SOURCE → CIBLE]

## Claude Code (portage)
"Porte le code de [LANGAGE A] vers [LANGAGE B].
Conserve la logique, utilise les idiomes natifs."

## ChatGPT (revue)
"Revois le portage :
- La logique est-elle fidele ?
- Les idiomes du langage cible sont-ils respectes ?
- Edge cases preserves ?"

## Gemini CLI (test)
"Execute les tests sur le code porte.
Compare les resultats avec le code original."
```

---

### 3 -- Migration de donnees validee

```
## Claude (strategie)
"Concois la strategie ETL :
- Mapping source → cible
- Transformations necessaires
- Validation post-migration"

## Claude Code (implementation)
"Implemente le script de migration.
Ajoute checksums et comptages."

## Gemini CLI (execution)
"Execute la migration.
Verifie les checksums et comptages.
Compare des echantillons source vs cible."

## Perplexity (validation)
"Recherche les problemes courants de migration [SOURCE → CIBLE].
Verifications supplementaires recommandees."
```

---

### 4 -- Migration Windows → Linux multi-IA

```
## Perplexity
"Equivalences logicielles Windows → Linux pour [LISTE LOGICIELS].
Meilleurs guides de migration [ANNEE]."

## Claude
"Plan de migration personnalise :
- Ordre des taches
- Scripts PowerShell → Bash
- Configuration equivalente"

## ChatGPT
"Guide utilisateur pour la transition :
- Raccourcis et habitudes a changer
- FAQ du nouvel utilisateur Linux"

## Gemini CLI
"Verifie que tout fonctionne apres migration :
- Services actifs
- Applications installees
- Peripheriques detectes"
```

---

### 5 -- Post-migration multi-IA

```
Migration terminee. Validation :

## Gemini CLI
"Tests de fonctionnement de tous les services migres.
Benchmark de performance avant/apres."

## Claude
"Analyse les resultats. Identifie les regressions.
Score de succes de la migration."

## ChatGPT
"Redige le rapport de migration :
- Ce qui a ete migre
- Problemes rencontres et solutions
- Performances avant/apres
- Lecons apprises"
```

---

## Exemples d'utilisation

### Exemple : Migration Docker
**Workflow** : Perplexity (guide) → Claude (plan) → Gemini CLI (execution) → Claude (validation)

**Resultat attendu** : Migration executee, validee et documentee.

---

## Effet sur le modele
- La recherche prealable par Perplexity evite les pieges connus
- La planification Claude structure la migration de facon robuste
- L'execution Gemini CLI teste dans le contexte reel
- La validation croisee confirme le succes de la migration
