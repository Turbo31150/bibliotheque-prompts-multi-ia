# Multi-IA -- Recherche

## Description

Prompts pour orchestrer plusieurs IA dans la recherche d'information : Perplexity pour la recherche web, Claude pour l'analyse, ChatGPT pour la synthese, et Gemini CLI pour la verification dans le code.

## Cas d'usage
- Recherche exhaustive multi-sources
- Analyse et synthese d'information complexe
- Veille technologique multi-perspectif
- Comparaison d'options avec validation croisee
- Due diligence technique sur des projets

---

## Prompts prets a copier

### 1 -- Recherche exhaustive multi-IA

```
Sujet de recherche : [SUJET]

## Perplexity (sources web)
"Recherche les 10 meilleures sources sur [SUJET].
Articles, papers, documentation officielle, tutoriels."

## Claude (analyse)
"A partir de ces sources, synthetise :
- Etat de l'art
- Points de consensus
- Points de debat
- Questions ouvertes"

## ChatGPT (vulgarisation)
"Resume cette synthese en format accessible :
- 3 points cles
- Analogies pour les concepts complexes
- Recommandation actionable"
```

---

### 2 -- Comparaison technologique multi-IA

```
Comparer : [TECHNO A] vs [TECHNO B] pour [CAS D'USAGE]

## Perplexity
"Benchmarks recents, retours d'experience, adoption en production."

## Claude
"Analyse technique approfondie :
- Architecture, design, compromis
- Forces et faiblesses structurelles
- Cas ou A > B et inversement"

## ChatGPT
"Retours utilisateurs et aspects pratiques :
- Courbe d'apprentissage
- Ecosysteme et communaute
- Experience developpeur"

## Synthese
Tableau comparatif consolide. Recommandation argumentee.
```

---

### 3 -- Due diligence technique

```
Projet a evaluer : [NOM / LIEN]

## Perplexity
"Historique, reputation, incidents, equipe, funding."

## Claude Code
"Analyse le code source :
- Qualite, tests, documentation
- Architecture, dependances
- Red flags techniques"

## Claude
"Evaluation globale :
- Score de confiance (0-100)
- Risques identifies
- Recommandation : utiliser / eviter / surveiller"
```

---

### 4 -- Veille technologique multi-IA

```
Domaine de veille : [DOMAINE]

## Perplexity (collecte)
"Actualites et sorties de la semaine dans [DOMAINE]."

## Claude (analyse)
"Trie par importance. Identifie les tendances de fond vs le bruit."

## ChatGPT (newsletter)
"Redige une newsletter de veille de 500 mots :
- Top 3 actualites
- Tendance du mois
- A surveiller"
```

---

### 5 -- Exploration de domaine inconnu

```
Je veux apprendre [DOMAINE]. Je suis [NIVEAU].

## Perplexity
"Meilleures ressources pour apprendre [DOMAINE] en [ANNEE] :
cours, livres, tutoriels, projets pratiques."

## Claude
"Cree un plan d'apprentissage structure :
- Semaine par semaine
- Concepts par ordre logique
- Exercices pratiques"

## ChatGPT
"Pour chaque concept du plan :
- Explication simple avec analogie
- Exemple concret
- Erreur courante a eviter"
```

---

## Exemples d'utilisation

### Exemple : Choisir une BDD
**Workflow** : Perplexity (benchmarks) → Claude (analyse) → ChatGPT (synthese) → decision

**Resultat attendu** : Comparaison complete avec recommandation contextuelle.

---

## Effet sur le modele
- Perplexity apporte des donnees a jour et sourcees
- Claude apporte la profondeur d'analyse
- ChatGPT apporte la clarte de communication
- La combinaison produit une recherche plus complete et fiable
