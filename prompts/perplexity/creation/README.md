# Perplexity -- Creation

## Description

Prompts pour utiliser Perplexity dans la creation de projets en s'appuyant sur la recherche d'etat de l'art, de meilleures pratiques et d'exemples existants. Perplexity aide a prendre des decisions de creation informees.

## Cas d'usage
- Recherche d'etat de l'art avant de creer un projet
- Identification des meilleures pratiques actuelles
- Trouver des exemples et templates existants
- Evaluer les technologies avant de choisir
- Veille sur les nouvelles approches

---

## Prompts prets a copier

### 1 -- Rechercher l'etat de l'art

```
Recherche l'etat de l'art pour creer [TYPE DE PROJET] en [ANNEE] :

1. Les 5 meilleurs projets open source similaires
   - Nom, lien GitHub, etoiles, derniere activite
   - Stack technique utilisee
   - Points forts et limites

2. Les technologies recommandees actuellement
   - Framework/langage le plus adapte
   - Base de donnees recommandee
   - Infrastructure (cloud, self-hosted, hybrid)

3. Les patterns architecturaux en vogue
   - Ce qui est recommande en [ANNEE]
   - Ce qui est deprecie / a eviter

4. Les erreurs courantes a eviter
   - Anti-patterns documentes
   - Post-mortems de projets similaires echoues

Sources avec liens pour chaque point.
```

---

### 2 -- Trouver des templates et boilerplates

```
Recherche les meilleurs templates/boilerplates pour demarrer [TYPE DE PROJET] :

## CRITERES
- Langage : [LANGAGE]
- Framework : [FRAMEWORK si defini, sinon recommander]
- Features requises : [LISTER]

## POUR CHAQUE TEMPLATE
1. Nom et lien (GitHub, npm, etc.)
2. Etoiles / popularite
3. Derniere mise a jour
4. Ce qui est inclus (auth, tests, CI, Docker, etc.)
5. Ce qui manque
6. Qualite du code et documentation
7. Licence

Top 3 recommandes avec commande d'installation.
```

---

### 3 -- Evaluer les options technologiques

```
Compare ces options pour [BESOIN] :
- Option A : [TECHNO A]
- Option B : [TECHNO B]
- Option C : [TECHNO C]

Recherche pour chaque option :
1. Benchmarks recents (performance, scalabilite)
2. Avis de la communaute (Reddit, HN, blogs tech)
3. Cas d'utilisation en production (qui l'utilise ?)
4. Problemes connus et limitations
5. Roadmap et avenir du projet
6. Ecosysteme (plugins, integrations, communaute)
7. Courbe d'apprentissage (retours d'experience)

Tableau comparatif avec score /5 par critere.
Recommandation contextuelle pour [MON CAS D'USAGE].
```

---

### 4 -- S'inspirer des meilleures implementations

```
Recherche les meilleures implementations de [FONCTIONNALITE] :

## CONTEXTE
- Stack : [LANGAGE / FRAMEWORK]
- Contraintes : [PERFORMANCE, SECURITE, etc.]

## RECHERCHE
1. Comment les grands projets open source implementent cette fonctionnalite
   (Linux kernel, Kubernetes, PostgreSQL, etc. selon pertinence)
2. Patterns recommandes dans la documentation officielle
3. Articles de blog tech detaillant l'implementation
4. Videos / talks de conferences (si pertinent)

Pour chaque implementation trouvee :
- Approche choisie et pourquoi
- Code ou pseudo-code illustratif
- Compromis explicites
- Lien source
```

---

### 5 -- Valider une idee de projet

```
Valide cette idee de projet : [DESCRIPTION]

Recherche :
1. EXISTANT : des projets similaires existent-ils deja ?
   - Si oui : quels sont leurs points faibles (opportunite)
   - Si non : pourquoi (pas de besoin ? trop complexe ?)

2. DEMANDE : y a-t-il une demande pour ca ?
   - Discussions Reddit/HN/forums
   - GitHub Issues demandant cette fonctionnalite
   - Recherches Google Trends

3. FAISABILITE
   - Technologies necessaires
   - Complexite estimee
   - Ressources requises (serveur, API, donnees)

4. MONETISATION (si applicable)
   - Modeles economiques des projets similaires
   - Disposition a payer de la cible

Verdict : VALIDE / A PIVOTER / A ABANDONNER, avec justification.
```

---

## Exemples d'utilisation

### Exemple : Etat de l'art
**Prompt** : "Quel est le meilleur framework pour creer un dashboard de monitoring en temps reel en 2026 ?"

**Resultat attendu** : Comparaison sourcee de Grafana, Metabase, Apache Superset avec recommandation.

### Exemple : Templates
**Prompt** : "Meilleurs boilerplates FastAPI avec auth, Docker et tests en 2026."

**Resultat attendu** : Top 3 templates GitHub avec liens, features et commandes d'installation.

---

## Effet sur le modele
- Perplexity fournit des donnees a jour grace a la recherche web
- Les comparaisons sont basees sur des sources verifiables
- Les liens GitHub permettent de verifier la popularite et l'activite
- La recherche de retours d'experience (Reddit, HN) donne des avis reels
