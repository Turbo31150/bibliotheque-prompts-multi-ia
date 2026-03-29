# BrowserOS -- Developpement

## Description

Prompts pour utiliser BrowserOS MCP dans le developpement web : tests end-to-end, debug de rendu, validation d'interfaces et prototypage.

## Cas d'usage
- Tests end-to-end automatises
- Validation de rendu cross-browser
- Debug de problemes CSS/JavaScript
- Scraping pour alimenter des APIs
- Tests d'accessibilite

---

## Prompts prets a copier

### 1 -- Tests end-to-end

```
Execute ces tests end-to-end sur [URL] :
1. Login : naviguer vers /login, remplir credentials, verifier redirection
2. CRUD : creer un element, le lire, le modifier, le supprimer
3. Navigation : verifier que tous les liens du menu fonctionnent
4. Responsive : tester sur 3 resolutions (desktop, tablet, mobile)
5. Performance : chaque page charge en moins de 3 secondes
Rapport : test par test, PASS/FAIL avec screenshot si FAIL.
```

---

### 2 -- Validation d'accessibilite

```
Audit d'accessibilite de [URL] :
1. Verifier les alt texts des images
2. Verifier le contraste des couleurs
3. Verifier la navigation au clavier
4. Verifier les ARIA labels
5. Verifier la structure des headings (H1 > H2 > H3)
Rapport : conformite WCAG 2.1 niveau AA.
```

---

### 3 -- Debug CSS

```
Debug le probleme de layout sur [URL] :
1. Screenshot du rendu actuel
2. Inspecter les elements CSS (computed styles)
3. Identifier les proprietes causant le probleme
4. Proposer la correction CSS
5. Appliquer la correction et screenshot du resultat
```

---

### 4 -- Scraping pour API mock

```
Scrape [URL] pour creer des donnees de mock API :
1. Extraire les donnees structurees
2. Generer un fichier JSON au format API REST
3. Creer un endpoint mock (json-server ou equivalent)
Pour le prototypage front-end sans back-end.
```

---

### 5 -- Test de formulaire complet

```
Teste exhaustivement le formulaire sur [URL] :
1. Validation HTML5 (required, pattern, min, max)
2. Validation JavaScript custom
3. Soumission reussie
4. Gestion des erreurs serveur
5. Comportement hors ligne
Rapport detaille par champ et scenario.
```

---

## Exemples d'utilisation

### Exemple : E2E
**Prompt** : "Teste le flux d'inscription complet sur mon app a http://localhost:3000"

**Resultat attendu** : Test du formulaire d'inscription avec tous les scenarios, screenshots inclus.

---

## Effet sur le modele
- BrowserOS execute de vrais tests dans un vrai navigateur
- Les tests E2E verifient le comportement complet de l'application
- L'audit d'accessibilite couvre les standards WCAG
- Le scraping pour mock API accelere le prototypage
