# Perplexity -- Debug

## Description

Prompts pour utiliser Perplexity dans le diagnostic et la resolution de bugs. Perplexity excelle grace a sa capacite de recherche web en temps reel : il peut trouver des solutions sur Stack Overflow, GitHub Issues et la documentation officielle.

## Cas d'usage
- Recherche de solutions a des erreurs specifiques
- Identification de bugs connus dans des librairies
- Trouver des workarounds documentes
- Comparaison de solutions communautaires
- Verification de la pertinence des solutions trouvees

---

## Prompts prets a copier

### 1 -- Rechercher une solution a une erreur

```
J'ai cette erreur dans [LANGAGE/FRAMEWORK] version [VERSION] :

[COLLER LE MESSAGE D'ERREUR COMPLET]

Contexte : [CE QUE JE FAISAIS QUAND L'ERREUR EST APPARUE]

Recherche :
1. Les causes les plus courantes de cette erreur
2. Les solutions verifiees (Stack Overflow, GitHub Issues)
3. Si c'est un bug connu de la version [VERSION]
4. Les workarounds si pas de fix officiel
5. La version qui corrige le probleme (si bug connu)

Cite les sources avec les liens.
```

---

### 2 -- Verifier si un bug est connu

```
Recherche si ce comportement est un bug connu :

## LOGICIEL : [NOM] version [VERSION]
## COMPORTEMENT OBSERVE : [DESCRIPTION]
## COMPORTEMENT ATTENDU : [DESCRIPTION]

Recherche dans :
1. Le bug tracker officiel (GitHub Issues, Jira, Bugzilla)
2. Les forums communautaires
3. Les release notes des versions recentes
4. Les PR en cours qui adressent ce probleme

Pour chaque resultat pertinent :
- Lien vers l'issue/discussion
- Statut (ouvert, ferme, en cours)
- Workaround propose
- Version de fix si disponible
```

---

### 3 -- Comparer les solutions de la communaute

```
Pour ce probleme : [DESCRIPTION DU PROBLEME]

Plusieurs solutions circulent en ligne. Recherche et compare :

1. Solution la plus votee sur Stack Overflow
2. Solution proposee dans la documentation officielle
3. Solution alternative proposee sur GitHub
4. Solution la plus recente (tenant compte des dernières versions)

Pour chaque solution :
- Description
- Avantages / inconvenients
- Nombre de confirmations (upvotes, thumbs up)
- Date (est-elle encore d'actualite ?)
- Effets de bord potentiels

Recommandation : quelle solution privilegier et pourquoi.
```

---

### 4 -- Diagnostiquer une regression

```
Mon application fonctionnait avant la mise a jour de [COMPOSANT] de [V_ANCIENNE] a [V_NOUVELLE].

Recherche :
1. Les breaking changes entre ces deux versions
2. Le changelog / release notes
3. Les issues GitHub mentionnant des regressions similaires
4. Le guide de migration officiel
5. Les deprecations qui sont devenues des erreurs

Si le probleme est documente :
- Lien vers la documentation
- Migration requise
- Si possible, le diff de code minimal pour corriger
```

---

### 5 -- Trouver des outils de debug

```
Recherche les meilleurs outils de debug pour [TECHNOLOGIE] en [ANNEE] :

## CRITERES
- Type : profiler, debugger, tracer, linter, analyzer
- Gratuit / open source prefere
- Compatible avec [OS / ENVIRONNEMENT]

## POUR CHAQUE OUTIL
1. Nom et lien
2. Ce qu'il fait (specialite)
3. Installation (1 commande si possible)
4. Cas d'usage ideal
5. Avantages vs alternatives
6. Derniere mise a jour (est-il maintenu ?)
7. Popularite (GitHub stars, telechargements)

Top 5 recommandes avec justification.
```

---

## Exemples d'utilisation

### Exemple : Erreur specifique
**Prompt** : "Perplexity, j'ai 'CUDA out of memory' avec PyTorch 2.1 et un modele de 7B parametres sur une RTX 3060 12GB. Solutions ?"

**Resultat attendu** : Solutions sourcees (gradient checkpointing, quantization, batch size) avec liens vers la doc PyTorch.

### Exemple : Regression
**Prompt** : "Mon Docker Compose ne monte plus les volumes apres la mise a jour 2.24 → 2.27. Bug connu ?"

**Resultat attendu** : Lien vers l'issue GitHub, explication du changement de comportement, workaround.

---

## Effet sur le modele
- Perplexity fournit des sources verifiables pour chaque solution proposee
- La recherche web en temps reel trouve les solutions les plus recentes
- Les liens vers Stack Overflow et GitHub Issues permettent de verifier les reponses
- Perplexity identifie bien les bugs connus et les regressions documentees
