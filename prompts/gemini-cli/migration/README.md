# Gemini CLI -- Migration

## Description

Prompts pour utiliser Gemini CLI dans les migrations de systemes, portages de code et transitions d'infrastructure. Gemini CLI peut lire les fichiers sources, executer des transformations et valider les resultats directement.

## Cas d'usage
- Portage de code entre langages ou frameworks
- Migration de configurations entre systemes
- Conversion de formats de donnees
- Migration de services entre machines
- Automatisation de taches de migration repetitives

---

## Prompts prets a copier

### 1 -- Portage de code entre langages

```
Porte ce code de [LANGAGE SOURCE] vers [LANGAGE CIBLE] :

## FICHIER SOURCE
[CHEMIN ou COLLER LE CODE]

## EXIGENCES
1. Conserver la meme logique et les memes fonctionnalites
2. Utiliser les idiomes natifs du langage cible
3. Conserver les commentaires (traduits si necessaire)
4. Gestion d'erreurs adaptee au langage cible
5. Tests unitaires equivalents

## FORMAT DE SORTIE
1. Code porte complet
2. Tableau des correspondances (fonction par fonction)
3. Differences de comportement connues
4. Dependances requises dans le langage cible
5. Instructions de build et execution
```

---

### 2 -- Migrer des configurations entre serveurs

```
Migre la configuration de [SERVEUR A] vers [SERVEUR B] :

1. Inventorier les configurations a migrer :
   - Fichiers dans /etc/ (liste des modifies vs defaut)
   - Crontabs de tous les utilisateurs
   - Services systemd personnalises
   - Variables d'environnement
   - Packages installes manuellement

2. Generer le plan de migration :
   - Ordre des operations (dependances)
   - Adaptations necessaires (chemins, versions, architecture)
   - Points de verification

3. Creer les scripts :
   - export.sh : exporte tout de A
   - import.sh : importe tout sur B
   - verify.sh : verifie la parite
   - rollback.sh : restaure l'etat initial de B
```

---

### 3 -- Convertir des formats de donnees

```
Convertis les donnees de [FORMAT A] vers [FORMAT B] :

## SOURCE
[CHEMIN DU FICHIER ou DESCRIPTION DU FORMAT]

## CIBLE
[FORMAT ATTENDU avec exemple]

## EXIGENCES
- Preservation de toutes les donnees (zero perte)
- Validation du schema de sortie
- Gestion des cas limites (valeurs nulles, caracteres speciaux, encodage)
- Rapport de conversion (lignes traitees, erreurs, warnings)
- Script reutilisable pour les prochaines conversions

## FORMATS COURANTS
CSV ↔ JSON, XML → JSON, YAML ↔ JSON, SQL dump → CSV,
INI → YAML, Docker Compose v2 → v3, Makefile → script bash
```

---

### 4 -- Migrer des conteneurs Docker

```
Migre ces conteneurs Docker de [MACHINE A] vers [MACHINE B] :

## CONTENEURS
[LISTER : nom, image, volumes, ports, reseaux]

## PROCEDURE
1. EXPORT : sauvegarder images, volumes, configs
   - docker save pour les images custom
   - tar pour les volumes
   - docker-compose.yml pour la configuration

2. TRANSFERT : rsync ou scp vers la machine cible

3. IMPORT : restaurer sur la machine cible
   - docker load pour les images
   - Restaurer les volumes
   - Adapter le docker-compose (chemins, ports si conflit)

4. VERIFICATION : comparer les etats
   - Memes images et versions
   - Donnees intactes dans les volumes
   - Services accessibles et fonctionnels

5. CUTOVER : basculer le traffic (DNS, reverse proxy)

Generer les scripts pour chaque etape.
```

---

### 5 -- Migrer un projet vers une nouvelle stack

```
Analyse le projet dans [CHEMIN] et propose une migration vers [NOUVELLE STACK] :

## ANALYSE
1. Technologies actuelles (langages, frameworks, BDD)
2. Points de douleur identifies
3. Dependances bloquantes pour la migration

## PLAN DE MIGRATION
1. Phase 1 : Migration incrementale (coexistence ancien/nouveau)
2. Phase 2 : Portage des fonctionnalites critiques
3. Phase 3 : Migration des donnees
4. Phase 4 : Tests de regression complets
5. Phase 5 : Cutover et decommissionnement

## ESTIMATION
- Effort par phase (jours-homme)
- Risques par phase
- Criteres de go/no-go pour chaque phase
```

---

## Exemples d'utilisation

### Exemple : Portage PowerShell → Bash
**Commande** : `gemini "Porte ~/scripts/backup.ps1 en bash"`

**Resultat attendu** : Script bash equivalent avec correspondances commentees.

### Exemple : Migration Docker
**Commande** : `gemini "Liste mes conteneurs Docker et genere les scripts pour les migrer vers le serveur 192.168.1.100"`

**Resultat attendu** : Scripts d'export, transfert et import pour chaque conteneur.

---

## Effet sur le modele
- Gemini CLI lit les fichiers sources directement pour un portage fidele
- L'execution de commandes permet de valider les migrations en temps reel
- Les scripts generes sont testes dans le contexte reel du serveur
- L'acces SSH permet potentiellement d'operer sur la machine cible
