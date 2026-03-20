# ChatGPT -- Migration

## Description

Prompts pour utiliser ChatGPT dans la planification et l'execution de migrations : Windows vers Linux, cloud vers on-premise, anciennes versions vers nouvelles, migration de donnees et d'applications.

## Cas d'usage
- Migration Windows vers Linux
- Migration de bases de donnees
- Portage d'applications entre plateformes
- Migration de configurations et services
- Plans de migration avec rollback

---

## Prompts prets a copier

### 1 -- Plan de migration Windows vers Linux

```
Cree un plan de migration complet de Windows vers Linux pour un poste de travail :

## INVENTAIRE WINDOWS
- Applications utilisees : [LISTER]
- Peripheriques : [LISTER]
- Scripts PowerShell : [NOMBRE]
- Fichiers de configuration : [LISTER]

## PLAN A PRODUIRE
1. AUDIT : equivalences logicielles Windows → Linux
2. PREPARATION : backup complet, image de rescue
3. INSTALLATION : distribution recommandee + justification
4. CONFIGURATION : reproduire l'environnement de travail
5. MIGRATION DONNEES : transfert fichiers, profils, configs
6. PORTAGE SCRIPTS : PowerShell → Bash (pour chaque script)
7. TESTS : checklist de validation post-migration
8. ROLLBACK : procedure de retour Windows si echec

Format : tableau de taches avec estimation de temps, priorite, et dependances.
```

---

### 2 -- Convertir des scripts PowerShell en Bash

```
Convertis ce script PowerShell en Bash equivalent :

## SCRIPT POWERSHELL
[COLLER LE SCRIPT]

## EXIGENCES
- Conserver exactement la meme logique
- Utiliser les equivalents Linux natifs (pas de hacks)
- Commenter chaque section avec l'equivalent PS original
- Gestion d'erreurs avec set -euo pipefail
- Compatible bash 5+
- Tester les dependances (commandes requises) au debut du script
- Fournir les instructions d'installation des dependances manquantes

## FORMAT DE SORTIE
1. Script bash complet
2. Tableau des correspondances (cmdlet PS → commande Linux)
3. Points d'attention / differences de comportement
```

---

### 3 -- Migrer une base de donnees

```
Planifie la migration d'une base de donnees [SOURCE] vers [CIBLE] :

## CONTEXTE
- Taille : [X] Go
- Tables : [N]
- Relations : [complexite]
- Downtime acceptable : [duree]

## PLAN DE MIGRATION
1. SCHEMA : adapter les types de donnees, contraintes, index
2. DONNEES : strategie d'export/import (dump, replication, ETL)
3. PROCEDURES : convertir les stored procedures
4. TRIGGERS : adapter ou remplacer
5. VUES : recreaer ou optimiser
6. PERMISSIONS : mapper les roles et grants
7. TESTS : comparer les resultats de requetes types
8. CUTOVER : procedure de bascule avec zero-downtime si possible

Genere les scripts SQL de migration pour chaque etape.
```

---

### 4 -- Migrer des services systemd

```
Migre ces services Windows (Task Scheduler / Services) vers systemd Linux :

## SERVICES WINDOWS
[LISTER : nom, type, trigger, action]

Pour chaque service, genere :
1. Le fichier .service systemd complet
2. Le fichier .timer si c'est une tache planifiee
3. Les commandes d'installation et d'activation
4. Le test de fonctionnement
5. Les logs avec journalctl

Inclure : restart automatique, dependances, utilisateur dedie, limites de ressources.
```

---

### 5 -- Migration cloud vers on-premise

```
Planifie la migration d'une infrastructure cloud (AWS/GCP/Azure) vers on-premise :

## SERVICES CLOUD UTILISES
[LISTER : EC2, S3, RDS, Lambda, etc.]

## EQUIVALENCES ON-PREMISE
Pour chaque service cloud :
1. Solution open-source equivalente
2. Configuration materielle requise
3. Procedure d'installation
4. Migration des donnees
5. Test de parite fonctionnelle

## RISQUES
- Points de non-retour
- Perte de fonctionnalites
- Impact performance
- Cout de maintenance additionnel

Format : matrice de decision avec score risque/benefice par service.
```

---

## Exemples d'utilisation

### Exemple : Portage PowerShell
**Prompt** : "Convertis Get-Process | Where-Object {$_.CPU -gt 50} | Sort-Object CPU -Descending en bash."

**Resultat attendu** : `ps aux --sort=-%cpu | awk '$3 > 50'` avec explications des differences de comportement.

### Exemple : Migration de services
**Prompt** : "Mon service Windows 'MonBackup' tourne tous les jours a 3h du matin et execute backup.bat. Cree l'equivalent systemd."

**Resultat attendu** : Fichiers .service et .timer complets, prets a deployer.

---

## Effet sur le modele
- ChatGPT connait bien les equivalences Windows/Linux et produit des correspondances fiables
- Les prompts avec inventaire detaille generent des plans de migration realistes
- Demander le rollback force le modele a penser aux cas d'echec
- Le format tableau avec estimations de temps aide a la planification projet
