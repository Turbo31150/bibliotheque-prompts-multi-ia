# BrowserOS -- Creation

## Description

Prompts pour utiliser BrowserOS MCP dans la creation de contenu web, le prototypage et le scraping de donnees pour alimenter des projets.

## Cas d'usage
- Scraping de donnees pour alimenter un projet
- Prototypage d'interactions web
- Capture et extraction de contenu
- Tests automatises d'interfaces
- Generation de maquettes par screenshot

---

## Prompts prets a copier

### 1 -- Scraper des donnees structurees

```
Utilise BrowserOS pour scraper [URL] :
1. Naviguer vers la page
2. Attendre le chargement complet (attendre le selecteur [CSS])
3. Extraire les donnees dans ce format JSON :
   {titre, description, prix, image, lien}
4. Paginer si necessaire (bouton "suivant")
5. Sauvegarder en JSON dans [CHEMIN]
Respecter un delai de 2 secondes entre les pages.
```

---

### 2 -- Capturer des references visuelles

```
Capture des references visuelles de ces sites :
[LISTER LES URLs]
Pour chaque site :
- Screenshot pleine page (pas juste le viewport)
- Screenshot mobile (375x812)
- Extraire la palette de couleurs (CSS computed styles)
- Extraire les fonts utilisees
Sauvegarder dans ~/references/[nom_site]/
```

---

### 3 -- Tester des interactions utilisateur

```
Teste ce flux utilisateur sur [URL] :
1. Naviguer vers la page d'accueil
2. Cliquer sur [BOUTON/LIEN]
3. Remplir le formulaire avec [DONNEES]
4. Soumettre et verifier la reponse
5. Screenshot a chaque etape
Rapport : flux complet en screenshots avec annotations.
```

---

### 4 -- Extraire du contenu pour un dataset

```
Extrais le contenu de [LISTE URLs] pour creer un dataset :
Pour chaque URL :
- Titre de la page
- Contenu principal (texte sans navigation/footer)
- Date de publication
- Auteur si disponible
- Tags/categories
Sauvegarder en CSV et JSON.
```

---

### 5 -- Verifier le rendu d'une page

```
Verifie le rendu de [URL] sur differentes resolutions :
- Desktop : 1920x1080, 1366x768
- Tablet : 768x1024
- Mobile : 375x812, 414x896
Pour chaque resolution : screenshot + verification des elements visibles.
Rapport de compatibilite responsive.
```

---

## Exemples d'utilisation

### Exemple : Scraping
**Prompt** : "Scrape les 100 premiers repos GitHub trending et sauvegarde en JSON"

**Resultat attendu** : Fichier JSON avec nom, description, etoiles et lien de chaque repo.

---

## Effet sur le modele
- BrowserOS permet le scraping interactif (JavaScript, SPA, pagination)
- Les screenshots multi-resolution testent le responsive design
- L'extraction de contenu structure alimente les projets en donnees
- Les tests d'interaction valident les flux utilisateur
