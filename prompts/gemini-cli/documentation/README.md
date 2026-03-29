# Gemini CLI -- Documentation

## Description

Prompts pour utiliser Gemini CLI dans la generation et la maintenance de documentation technique. Gemini CLI peut lire le code source directement et generer la documentation alignee avec l'implementation reelle.

## Cas d'usage
- Documentation automatique a partir du code source
- Generation de guides d'utilisation
- Creation de diagrammes et schemas
- Maintenance de wikis techniques
- Documentation d'APIs et de configurations

---

## Prompts prets a copier

### 1 -- Documenter un codebase automatiquement

```
Genere la documentation complete du projet dans [CHEMIN] :

## DOCUMENTS A CREER
1. README.md principal
   - Description du projet
   - Installation rapide
   - Usage basique
   - Configuration
   - Contribution

2. docs/architecture.md
   - Diagramme des composants (ASCII)
   - Description de chaque module
   - Flux de donnees

3. docs/api.md (si applicable)
   - Chaque endpoint/fonction publique
   - Parametres, types, retours
   - Exemples

4. docs/configuration.md
   - Variables d'environnement
   - Fichiers de configuration
   - Valeurs par defaut

5. docs/troubleshooting.md
   - Problemes courants et solutions
   - FAQ

Base chaque document sur le code reel lu dans le projet.
```

---

### 2 -- Generer la doc d'un script

```
Documente le script [CHEMIN] en generant :

1. En-tete de documentation (commentaire au debut du script)
   - Description
   - Usage : script.sh [options] [arguments]
   - Options (chaque flag avec description)
   - Exemples (3 cas d'usage)
   - Dependances
   - Auteur et date

2. Man page (format groff/troff)
   - NAME, SYNOPSIS, DESCRIPTION, OPTIONS
   - EXAMPLES, FILES, EXIT STATUS
   - SEE ALSO

3. Completion bash/zsh
   - Auto-completion des flags et arguments

Lis le script pour extraire les options et la logique.
```

---

### 3 -- Documenter une configuration systeme

```
Documente la configuration actuelle de ce serveur Linux :

1. Lis et documente les fichiers de configuration modifies dans /etc/
2. Liste les services systemd actifs avec leur role
3. Documente les crontabs de chaque utilisateur
4. Documente la configuration reseau
5. Documente les montages et le stockage
6. Documente la configuration Docker (containers, volumes, reseaux)

## FORMAT
Pour chaque element :
- Fichier/service concerne
- Ce qu'il fait (description humaine)
- Pourquoi il est configure ainsi (si deductible)
- Comment le modifier
- Risques si modification

Sauvegarder dans ~/docs/server-config-[DATE].md
```

---

### 4 -- Creer un changelog automatique

```
Genere un changelog a partir de l'historique git du projet dans [CHEMIN] :

## METHODE
1. Lis les commits depuis le dernier tag (ou les N derniers commits)
2. Classe par type :
   - feat: nouvelles fonctionnalites
   - fix: corrections de bugs
   - docs: documentation
   - refactor: restructuration
   - perf: performance
   - test: tests
   - chore: maintenance
3. Genere le changelog en format Keep a Changelog
4. Identifie les breaking changes
5. Suggere le numero de version (semver)

Format Markdown, pret a copier dans CHANGELOG.md.
```

---

### 5 -- Documenter les procedures operationnelles

```
Cree un wiki operationnel pour l'equipe a partir de la configuration actuelle :

## PROCEDURES A DOCUMENTER
1. Deploiement d'une mise a jour
2. Rollback en cas de probleme
3. Ajout d'un nouveau service Docker
4. Backup et restauration
5. Ajout d'un utilisateur avec les bons droits
6. Rotation des certificats SSL
7. Nettoyage de l'espace disque
8. Diagnostic en cas de panne

Pour chaque procedure :
- Pre-requis
- Etapes numerotees avec commandes exactes
- Verification apres chaque etape
- Temps estime
- Qui peut l'executer (permissions requises)
```

---

## Exemples d'utilisation

### Exemple : Doc automatique
**Commande** : `gemini "Documente tous les scripts dans ~/scripts/ avec usage et exemples"`

**Resultat attendu** : Documentation generee pour chaque script, basee sur le code reel.

### Exemple : Config serveur
**Commande** : `gemini "Documente la configuration actuelle de ce serveur pour qu'un nouveau admin puisse le reprendre"`

**Resultat attendu** : Document complet couvrant tous les services, configurations et procedures.

---

## Effet sur le modele
- Gemini CLI lit le code source reel pour une documentation fidele
- L'execution de commandes systeme permet de documenter l'etat actuel
- Les git logs sont lus directement pour les changelogs
- La documentation generee est verifiable car basee sur des faits
