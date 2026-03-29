# BrowserOS -- Monitoring

## Description

Prompts pour utiliser BrowserOS MCP dans le monitoring web : surveillance de pages, verification de disponibilite, capture de screenshots et tests de performance web.

## Cas d'usage
- Surveillance de disponibilite de sites web
- Capture de screenshots programmatique
- Tests de performance web (Core Web Vitals)
- Monitoring de contenu (changements de page)
- Verification de certificats SSL via navigateur

---

## Prompts prets a copier

### 1 -- Surveillance de disponibilite

```
Utilise BrowserOS pour verifier la disponibilite de ces URLs toutes les 5 minutes :
[LISTER LES URLs]

Pour chaque URL :
1. Naviguer vers la page
2. Verifier le code de statut HTTP
3. Verifier que le contenu attendu est present (selecteur CSS)
4. Mesurer le temps de chargement
5. Si indisponible : prendre un screenshot et alerter
```

---

### 2 -- Capture de screenshots periodiques

```
Capture des screenshots de [URLs] a intervalles reguliers :
- Resolution : 1920x1080
- Format : PNG
- Nommage : site_YYYYMMDD_HHmm.png
- Stockage : ~/monitoring/screenshots/
- Comparer avec le screenshot precedent (diff visuel)
```

---

### 3 -- Tests de performance web

```
Execute des tests de performance sur [URL] :
1. Mesurer le First Contentful Paint (FCP)
2. Mesurer le Largest Contentful Paint (LCP)
3. Mesurer le Cumulative Layout Shift (CLS)
4. Mesurer le Time to Interactive (TTI)
5. Taille totale de la page (MB)
6. Nombre de requetes
Sauvegarder les resultats en CSV pour suivi historique.
```

---

### 4 -- Verification de formulaires

```
Teste que le formulaire sur [URL] fonctionne correctement :
1. Naviguer vers la page
2. Remplir les champs avec des donnees de test
3. Soumettre le formulaire
4. Verifier la reponse (message de succes, redirection)
5. Verifier qu'aucune erreur JavaScript n'est apparue
```

---

### 5 -- Monitoring de contenu

```
Surveille le contenu de [URL] pour detecter les changements :
1. Extraire le texte du selecteur [CSS_SELECTOR]
2. Comparer avec la valeur precedente
3. Si changement : notifier avec l'ancien et le nouveau contenu
4. Historique des changements en base SQLite
```

---

## Exemples d'utilisation

### Exemple : Uptime monitoring
**Prompt** : "Verifie que https://mon-api.local:8080/health repond 200 et contient 'ok'"

**Resultat attendu** : Verification automatique avec alerte si le check echoue.

---

## Effet sur le modele
- BrowserOS permet un monitoring web reel via navigateur headless
- Les screenshots apportent une preuve visuelle des problemes
- Les Core Web Vitals mesurent la performance reelle de l'utilisateur
- La comparaison de contenu detecte les changements non annonces
