# Perplexity -- Web & Social

## Description

Prompts pour utiliser Perplexity dans la veille web, l'analyse de tendances et la recherche d'informations sur les reseaux sociaux. Perplexity est ideal pour la recherche d'actualites et de tendances grace a ses sources en temps reel.

## Cas d'usage
- Veille technologique et concurrentielle
- Analyse de tendances sur les reseaux sociaux
- Recherche d'influenceurs et de communautes
- Suivi d'actualites par domaine
- Analyse de sentiment sur un sujet

---

## Prompts prets a copier

### 1 -- Veille technologique

```
Fais une veille technologique sur [SUJET] pour la semaine passee :

1. ACTUALITES MAJEURES
   - Les 5 news les plus importantes
   - Source et date pour chaque news
   - Impact sur le domaine

2. RELEASES ET MISES A JOUR
   - Nouvelles versions de projets majeurs
   - Features notables
   - Breaking changes

3. ARTICLES ET ANALYSES
   - Top 3 articles de blog/medium
   - Discussions Reddit/HN les plus engagees

4. TENDANCES EMERGENTES
   - Ce qui monte (adoption croissante)
   - Ce qui descend (depreciation, abandon)

Format : newsletter resume, 500 mots max.
```

---

### 2 -- Analyser les tendances d'un sujet

```
Analyse les tendances actuelles autour de [SUJET] :

1. VOLUME DE DISCUSSIONS
   - Tendance Google Trends (hausse/baisse)
   - Activite Reddit/Twitter/HN

2. SENTIMENT GENERAL
   - Positif / Negatif / Neutre
   - Arguments principaux de chaque camp
   - Citations representatives

3. ACTEURS CLES
   - Qui en parle (influenceurs, entreprises)
   - Positions prises

4. PREDICTION
   - Ou ca va dans les 6 prochains mois
   - Evenements a venir qui pourraient changer la donne

Sources avec liens.
```

---

### 3 -- Rechercher des communautes

```
Recherche les meilleures communautes en ligne pour [SUJET/TECHNOLOGIE] :

1. REDDIT
   - Subreddits pertinents (taille, activite)
   - Qualite des discussions

2. DISCORD / SLACK
   - Serveurs actifs (lien d'invitation si public)
   - Taille et activite

3. FORUMS
   - Forums specialises encore actifs
   - Qualite du contenu

4. GITHUB
   - Organizations et repos communautaires
   - Discussions GitHub actives

Pour chaque communaute : lien, taille, activite, qualite, ton general.
Top 5 recommandees pour un [DEBUTANT / EXPERT].
```

---

### 4 -- Suivi d'actualites ciblees

```
Resume les actualites des dernieres 48h sur [SUJET SPECIFIQUE] :

## FORMAT
Pour chaque actualite (maximum 10) :
- Titre
- Source et date
- Resume en 2-3 phrases
- Impact potentiel (faible/moyen/fort)
- Lien

## FILTRES
- Pertinence : directement lie a [SUJET]
- Sources fiables uniquement
- Pas de clickbait ou rumeurs non confirmees

Ajouter en conclusion : les questions ouvertes et les prochaines etapes a surveiller.
```

---

### 5 -- Analyser un debat technique

```
Resume le debat actuel autour de [SUJET CONTROVERSE] :

Exemples : "Rust vs Go", "Monolithe vs Microservices", "Cloud vs Self-hosted"

## ANALYSE
1. POSITION A : arguments, defenseurs, exemples concrets
2. POSITION B : arguments, defenseurs, exemples concrets
3. NUANCES : cas ou A est meilleur, cas ou B est meilleur
4. CONSENSUS (s'il y en a un) : vers quoi la communaute converge
5. MON CAS : pour [DECRIRE MON CONTEXTE], quelle position est la plus adaptee

Citer les articles, talks et discussions les plus influents des deux cotes.
```

---

## Exemples d'utilisation

### Exemple : Veille IA
**Prompt** : "Actualites IA open source de la semaine : nouveaux modeles, outils, annonces."

**Resultat attendu** : Newsletter resume avec les releases de modeles, outils et discussions.

### Exemple : Debat technique
**Prompt** : "Resume le debat Docker vs Podman en 2026. Qui gagne pour un homelab ?"

**Resultat attendu** : Analyse equilibree avec recommandation contextuelle et sources.

---

## Effet sur le modele
- Perplexity est le meilleur outil pour la veille grace a la recherche temps reel
- Les sources citees permettent de verifier et approfondir
- L'analyse de tendances s'appuie sur des donnees reelles (pas d'hallucination)
- Le format newsletter est directement consommable
