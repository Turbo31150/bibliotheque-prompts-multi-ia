# BrowserOS -- Debug

## Description

Prompts pour utiliser BrowserOS MCP dans le debug d'applications web : inspection d'erreurs JavaScript, tests de fonctionnement, verification de rendu et debug d'APIs.

## Cas d'usage
- Detection d'erreurs JavaScript sur une page
- Test de formulaires et interactions
- Verification de reponses API via le navigateur
- Debug de problemes de rendu CSS
- Analyse de performance de chargement

---

## Prompts prets a copier

### 1 -- Detecter les erreurs JavaScript

```
Navigue vers [URL] et reporte toutes les erreurs :
1. Ouvrir la page
2. Capturer les erreurs console (Error, Warning)
3. Executer les interactions principales
4. Lister toutes les erreurs avec stack trace
5. Screenshot de la page au moment de chaque erreur
```

---

### 2 -- Tester un formulaire

```
Teste le formulaire sur [URL] avec ces scenarios :
1. Soumission valide (donnees correctes)
2. Champs vides (validation requise)
3. Donnees invalides (email invalide, nombre negatif)
4. Injection (caracteres speciaux, scripts)
Pour chaque scenario : screenshot + resultat observe.
```

---

### 3 -- Debug d'API via navigateur

```
Teste cet endpoint API depuis le navigateur :
1. Ouvrir DevTools > Network
2. Faire la requete vers [URL]
3. Capturer : status code, headers, body, temps de reponse
4. Verifier le CORS (si applicable)
5. Reporter les erreurs
```

---

### 4 -- Comparer le rendu entre navigateurs

```
Compare le rendu de [URL] entre :
- Chrome (derniere version)
- Firefox (derniere version)
- Differences de layout, couleurs, fonts
Screenshots cote a cote pour comparaison.
```

---

### 5 -- Profiler le chargement

```
Profile le chargement de [URL] :
1. Desactiver le cache
2. Charger la page
3. Mesurer : DNS, connexion, TTFB, download, rendu
4. Identifier les ressources les plus lourdes
5. Recommander des optimisations
```

---

## Exemples d'utilisation

### Exemple : Erreurs JS
**Prompt** : "Verifie que mon dashboard Grafana a http://localhost:3000 n'a pas d'erreurs JavaScript"

**Resultat attendu** : Liste des erreurs console avec details et screenshot.

---

## Effet sur le modele
- BrowserOS execute les pages comme un vrai navigateur
- La capture d'erreurs console detecte les bugs JavaScript
- Les tests de formulaires verifient la validation cote client
- Le profiling de chargement identifie les bottlenecks
