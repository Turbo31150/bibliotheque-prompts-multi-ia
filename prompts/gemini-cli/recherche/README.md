# Gemini CLI -- Recherche

## Description

Prompts pour utiliser Gemini CLI dans la recherche d'information, l'exploration de code, la documentation technique et l'investigation de problemes. Gemini CLI peut parcourir le filesystem et executer des commandes pour une recherche active.

## Cas d'usage
- Recherche dans de grands codebases
- Investigation de bugs et comportements inattendus
- Exploration de documentation technique
- Comparaison de technologies et solutions
- Analyse de dependances et compatibilites

---

## Prompts prets a copier

### 1 -- Explorer un codebase inconnu

```
Explore le codebase dans [CHEMIN] et produis une cartographie :

1. STRUCTURE
   - Arbre des repertoires avec description de chaque dossier
   - Langages utilises (% par langage)
   - Fichiers cles (entrypoint, config, CI/CD)

2. ARCHITECTURE
   - Pattern architectural (MVC, microservices, monolithe...)
   - Points d'entree de l'application
   - Flux de donnees principal
   - Dependances externes (packages, APIs)

3. QUALITE
   - Presence de tests (% de couverture estime)
   - Documentation (README, commentaires, docstrings)
   - Configuration (env vars, fichiers config)
   - CI/CD (workflows, pipelines)

4. POINTS D'ATTENTION
   - Code duplique
   - Fichiers volumineux (> 500 lignes)
   - Dependances obsoletes
   - Secrets potentiellement committes
```

---

### 2 -- Investiguer un bug

```
Investigue ce bug dans le projet [CHEMIN] :

## SYMPTOME
[DECRIRE LE BUG]

## METHODE D'INVESTIGATION
1. Chercher le code responsable de la fonctionnalite
2. Lire les logs recents lies a cette fonctionnalite
3. Identifier les changements recents (git log, git diff)
4. Tracer le flux d'execution
5. Chercher des issues similaires dans le code (patterns connus)

## RAPPORT
- Fichier(s) et ligne(s) responsable(s)
- Cause racine
- Impact (quelles autres fonctionnalites sont affectees)
- Correction proposee (diff)
- Test pour verifier la correction
```

---

### 3 -- Comparer des technologies

```
Compare [TECHNO A] et [TECHNO B] pour le cas d'usage [DESCRIPTION] :

## CRITERES DE COMPARAISON
1. Performance (benchmarks, latence, throughput)
2. Facilite d'installation et configuration
3. Documentation et communaute
4. Maintenance et mises a jour
5. Integration avec l'ecosysteme existant [DECRIRE]
6. Cout (licence, infrastructure, operations)
7. Courbe d'apprentissage
8. Securite (CVE historiques, pratiques)

## FORMAT
Tableau comparatif avec score /5 par critere.
Recommandation finale argumentee.
Cas ou l'autre option serait meilleure.
```

---

### 4 -- Analyser les dependances d'un projet

```
Analyse les dependances du projet dans [CHEMIN] :

1. INVENTAIRE
   - Liste toutes les dependances (directes et transitives)
   - Version installee vs derniere version disponible
   - Licence de chaque dependance

2. SECURITE
   - Dependances avec CVE connues
   - Dependances abandonnees (pas de commit depuis > 1 an)
   - Dependances avec peu de mainteneurs (bus factor)

3. OPTIMISATION
   - Dependances inutilisees (importees mais jamais appelees)
   - Dependances dupliquees (plusieurs packages pour la meme chose)
   - Taille de chaque dependance

4. MISE A JOUR
   - Plan de mise a jour par priorite (securite d'abord)
   - Breaking changes attendus pour chaque maj majeure
   - Script de mise a jour avec tests
```

---

### 5 -- Rechercher dans la documentation

```
Recherche dans la documentation de [TECHNOLOGIE] comment faire [OBJECTIF] :

## METHODE
1. Chercher dans les fichiers locaux (man pages, --help, docs/)
2. Identifier les exemples pertinents dans le codebase
3. Synthetiser les informations trouvees

## FORMAT DE REPONSE
1. Reponse courte (1-2 lignes, la commande/le code)
2. Explication detaillee
3. Exemples concrets (3 minimum)
4. Pieges courants a eviter
5. Alternatives si la methode principale ne fonctionne pas
6. References (fichiers locaux ou URLs)
```

---

## Exemples d'utilisation

### Exemple : Explorer un projet
**Commande** : `gemini "Explore ~/projects/mon-app et dis-moi comment c'est organise"`

**Resultat attendu** : Cartographie complete du projet avec architecture et points d'attention.

### Exemple : Debug rapide
**Commande** : `gemini "Le service plante au demarrage, regarde les logs et le code dans ~/mon-service/"`

**Resultat attendu** : Investigation avec identification de la cause racine et correction proposee.

---

## Effet sur le modele
- Gemini CLI parcourt les fichiers reels pour une recherche basee sur des faits
- L'execution de commandes (grep, find, git log) permet une investigation active
- Les resultats sont ancres dans le contexte reel du projet
- La combinaison recherche + execution permet de valider les hypotheses
