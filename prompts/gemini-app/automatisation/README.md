# Gemini App -- Automatisation

## Description

Prompts pour utiliser Gemini App dans la conception de workflows automatises, de scripts et de pipelines. Gemini App aide a planifier l'automatisation et a generer le code necessaire.

## Cas d'usage
- Conception de workflows d'automatisation
- Generation de scripts bash/Python
- Automatisation de taches repetitives
- Pipelines CI/CD
- Orchestration de taches complexes

---

## Prompts prets a copier

### 1 -- Concevoir un workflow d'automatisation

```
Concois un workflow complet pour automatiser [TACHE] :

## DESCRIPTION DE LA TACHE
[CE QUI EST FAIT MANUELLEMENT AUJOURD'HUI]

## WORKFLOW AUTOMATISE
1. DECLENCHEUR : quand le workflow demarre
   - Cron (horaire)
   - Evenement (fichier cree, webhook, etc.)
   - Manuel (commande)

2. ETAPES : chaque action dans l'ordre
   Pour chaque etape :
   - Input requis
   - Action (commande, API call, transformation)
   - Output produit
   - Gestion d'erreur

3. NOTIFICATIONS
   - Succes : [canal et message]
   - Echec : [canal et message avec details]

4. MONITORING
   - Metriques (duree, succes/echec, volume)
   - Historique des executions
   - Alertes si anomalie

Diagramme ASCII du workflow complet.
```

---

### 2 -- Automatiser les backups

```
Cree un systeme de backup automatise complet :

## DONNEES A SAUVEGARDER
[LISTER : dossiers, bases de donnees, configurations]

## STRATEGIE
- Backup incrementiel quotidien
- Backup complet hebdomadaire
- Retention : 7 jours quotidiens, 4 semaines, 3 mois
- Stockage : local + distant (rsync vers NAS ou S3)

## SCRIPT
1. Pre-backup : verifier l'espace, notifier le debut
2. Backup des fichiers (rsync avec checksums)
3. Dump des bases de donnees
4. Export des configurations Docker
5. Compression et chiffrement (gpg)
6. Transfert vers stockage distant
7. Verification de l'integrite (checksum)
8. Nettoyage des anciens backups (rotation)
9. Post-backup : rapport par email, log
10. Test de restauration automatique (mensuel)

## RESTAURATION
- Procedure step-by-step de restauration complete
- Procedure de restauration partielle (un fichier, une BDD)
- Estimation du temps de restauration (RTO)
```

---

### 3 -- Creer un pipeline CI/CD

```
Concois un pipeline CI/CD pour [PROJET] :

## STACK : [LANGAGE, FRAMEWORK, DEPLOYMENT TARGET]
## OUTIL CI : [GitHub Actions / GitLab CI / Jenkins]

## PIPELINE
### Stage 1 : Build
- Checkout
- Install dependencies
- Compile / build
- Cache des dependances

### Stage 2 : Test
- Tests unitaires
- Tests d'integration
- Linting / formatage
- Analyse de securite (SAST)

### Stage 3 : Quality
- Couverture de code (seuil minimum)
- SonarQube / Code Climate
- Scan de dependances vulnerables

### Stage 4 : Deploy
- Staging (automatique sur merge to develop)
- Production (manuel / apres approbation sur merge to main)
- Rollback automatique si healthcheck echoue

### Stage 5 : Post-deploy
- Smoke tests
- Notification (Slack, email)
- Mise a jour du changelog

Generer le fichier de configuration complet (YAML).
```

---

### 4 -- Automatiser la maintenance systeme

```
Cree un ensemble de scripts de maintenance automatisee :

## TACHES
1. QUOTIDIEN
   - Rotation des logs (logrotate)
   - Nettoyage /tmp et caches
   - Verification des mises a jour de securite
   - Healthcheck de tous les services

2. HEBDOMADAIRE
   - Docker system prune
   - Analyse des logs (patterns d'erreurs)
   - Rapport d'utilisation des ressources
   - Verification des certificats SSL

3. MENSUEL
   - Mise a jour systeme complete
   - Test de restauration des backups
   - Revue des acces et permissions
   - Benchmark de performance (comparer au mois precedent)

Pour chaque tache : script bash, cron entry, et verification de succes.
Orchestration : script maitre qui execute les taches selon le planning.
```

---

### 5 -- Automatiser le provisionnement

```
Cree des scripts de provisionnement pour reproduire cet environnement :

## ENVIRONNEMENT A REPRODUIRE
[DECRIRE : OS, paquets, services, configurations]

## SCRIPT DE PROVISIONNEMENT
1. Installation de base (paquets systeme)
2. Configuration systeme (hostname, timezone, locale)
3. Utilisateurs et groupes
4. Configuration reseau
5. Installation des services (Docker, Nginx, etc.)
6. Configuration des services (fichiers de config)
7. Deploiement des applications
8. Configuration du monitoring
9. Configuration des backups
10. Tests de validation

## FORMAT
- Script bash idempotent (re-executable sans effet de bord)
- Variables en haut du script (personnalisation facile)
- Verification de chaque etape
- Log de toutes les actions
- Duree totale estimee
```

---

## Exemples d'utilisation

### Exemple : Backup
**Prompt** : "Automatise le backup de mes 3 serveurs Docker avec retention 30 jours et notification Slack."

**Resultat attendu** : Scripts complets avec cron, rotation, verification et notification.

### Exemple : CI/CD
**Prompt** : "Cree le pipeline GitHub Actions pour un projet Python avec tests, lint et deploy sur mon serveur."

**Resultat attendu** : Fichier .github/workflows/ci.yml complet et teste.

---

## Effet sur le modele
- Gemini App concoit des workflows complets et coherents
- Les scripts generes incluent la gestion d'erreurs et le logging
- La demande de tests de verification produit des automatisations fiables
- Le format idempotent garantit la re-executabilite sans risque
