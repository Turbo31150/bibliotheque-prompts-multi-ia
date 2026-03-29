# BrowserOS -- Migration

## Description

Prompts pour utiliser BrowserOS MCP dans la verification de migrations web : comparaison avant/apres, tests de regression visuelle et validation de fonctionnalites.

## Cas d'usage
- Comparaison visuelle avant/apres migration
- Tests de regression sur les pages migrees
- Verification de liens apres migration
- Validation de formulaires post-migration
- Audit de performance avant/apres

---

## Prompts prets a copier

### 1 -- Comparaison visuelle avant/apres

```
Compare visuellement [URL_AVANT] et [URL_APRES] :
1. Screenshot des deux pages (meme resolution)
2. Diff visuel pixel par pixel
3. Identifier les differences significatives
4. Ignorer les changements attendus (date, contenu dynamique)
Rapport : differences avec screenshots annotes.
```

---

### 2 -- Test de regression post-migration

```
Apres migration, verifie que ces pages fonctionnent :
[LISTER LES URLs]
Pour chaque page :
1. Charge correctement (pas d'erreur 404/500)
2. Contenu principal present
3. Navigation fonctionne
4. Formulaires fonctionnent
5. Pas d'erreurs JavaScript
Rapport : page par page, OK/KO avec details.
```

---

### 3 -- Verification de liens

```
Verifie tous les liens sur [URL] apres migration :
1. Extraire tous les liens (internes et externes)
2. Tester chaque lien (code HTTP)
3. Reporter les liens casses (404, 500, timeout)
4. Verifier les redirections (301 → bonne destination ?)
Rapport CSV : URL source, URL cible, status, redirect.
```

---

### 4 -- Validation de formulaires migres

```
Teste tous les formulaires sur [URL] apres migration :
1. Identifier tous les formulaires de la page
2. Remplir avec des donnees de test
3. Soumettre et verifier la reponse
4. Comparer le comportement avec l'ancien site
Rapport : formulaire par formulaire, OK/KO.
```

---

### 5 -- Benchmark performance avant/apres

```
Compare les performances de [URL_AVANT] et [URL_APRES] :
Metriques : FCP, LCP, CLS, TTI, taille page, requetes.
Tableau comparatif avec amelioration/degradation.
Alerte si degradation > 20%.
```

---

## Exemples d'utilisation

### Exemple : Regression visuelle
**Prompt** : "Compare mon ancien site et le nouveau, montre les differences visuelles"

**Resultat attendu** : Screenshots cote a cote avec differences surlignees.

---

## Effet sur le modele
- BrowserOS permet des tests de regression reels via navigateur
- La comparaison visuelle detecte les bugs de rendu
- La verification de liens previent les 404 post-migration
- Le benchmark avant/apres quantifie l'impact de la migration
