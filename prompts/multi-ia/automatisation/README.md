# Multi-IA -- Automatisation

## Description

Prompts pour orchestrer plusieurs IA dans l'automatisation : conception avec Claude, recherche d'outils avec Perplexity, implementation avec Claude Code, et test avec Gemini CLI.

## Cas d'usage
- Conception et implementation d'automatisations multi-IA
- Recherche et selection d'outils d'automatisation
- Validation croisee de scripts d'automatisation
- Pipeline CI/CD concu par plusieurs IA
- Maintenance automatisee avec supervision multi-IA

---

## Prompts prets a copier

### 1 -- Automatisation concue et validee multi-IA

```
Tache a automatiser : [DESCRIPTION]

## Perplexity (recherche)
"Outils existants pour automatiser [TACHE].
Scripts et recettes sur GitHub. Meilleures pratiques."

## Claude (conception)
"Concois le workflow d'automatisation :
- Declencheur, etapes, notifications, monitoring
- Choix de l'approche (script, workflow, cron)
- Diagramme du workflow"

## Claude Code (implementation)
"Implemente l'automatisation :
- Script principal
- Configuration
- Tests
- Documentation"

## Gemini CLI (test)
"Teste l'automatisation :
- Execution en mode dry-run
- Execution reelle
- Verification des resultats
- Rapport de test"
```

---

### 2 -- CI/CD multi-IA

```
## Claude (architecture)
"Concois le pipeline CI/CD pour [PROJET] :
- Stages, jobs, conditions
- Tests, qualite, securite, deploy"

## Perplexity (outils)
"Meilleures pratiques CI/CD en [ANNEE].
Actions/plugins recommandes pour chaque stage."

## Claude Code (implementation)
"Genere le fichier de pipeline (GitHub Actions / GitLab CI).
Ajoute les secrets, caches, conditions."

## ChatGPT (documentation)
"Documente le pipeline :
- Ce que fait chaque stage
- Comment ajouter un nouveau job
- Troubleshooting"
```

---

### 3 -- Backup automatise multi-IA

```
## Perplexity
"Meilleur outil de backup pour [CONTEXTE] en [ANNEE]. Comparaison."

## Claude
"Concois la strategie de backup :
- Frequence, retention, chiffrement, stockage distant
- Plan de restauration (RTO/RPO)"

## Claude Code
"Implemente les scripts de backup et restauration.
Cron entries. Tests de verification."

## Gemini CLI
"Teste le backup complet :
- Execution du backup
- Verification de l'integrite
- Test de restauration partielle"
```

---

### 4 -- Monitoring automatise multi-IA

```
## Claude (regles)
"Definis les regles de monitoring et d'alerte.
Seuils, escalade, actions automatiques."

## Claude Code (scripts)
"Implemente les scripts de monitoring et d'alerte.
Integration avec TTS, desktop notifications, email."

## Gemini CLI (deploiement)
"Deploie et teste le monitoring :
- Installation des scripts
- Configuration cron/systemd
- Test de chaque alerte"

## ChatGPT (runbooks)
"Cree les runbooks pour chaque alerte :
- Quoi faire quand l'alerte se declenche
- Qui contacter
- Procedure de resolution"
```

---

### 5 -- Maintenance automatisee multi-IA

```
## Claude (planning)
"Planifie les taches de maintenance :
- Quotidiennes, hebdomadaires, mensuelles
- Criteres de succes pour chaque tache"

## Claude Code (scripts)
"Implemente chaque tache de maintenance :
- Scripts bash idempotents
- Logging et reporting
- Gestion d'erreurs"

## Perplexity (validation)
"Verifie les commandes de maintenance :
- Sont-elles a jour pour [OS VERSION] ?
- Risques connus ?"

## Gemini CLI (execution)
"Execute un dry-run de chaque tache.
Verifie les resultats.
Configure les crons."
```

---

## Exemples d'utilisation

### Exemple : Backup
**Workflow** : Perplexity (outil) → Claude (strategie) → Claude Code (scripts) → Gemini CLI (test)

**Resultat attendu** : Systeme de backup automatise, teste et documente.

---

## Effet sur le modele
- La recherche prealable identifie les outils existants pour ne pas reinventer
- La conception Claude produit des workflows robustes
- L'implementation Claude Code est testee par Gemini CLI
- La documentation ChatGPT rend le systeme maintenable
