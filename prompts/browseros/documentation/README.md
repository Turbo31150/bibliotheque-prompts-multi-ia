# BrowserOS -- Documentation

## Description

Prompts pour utiliser BrowserOS MCP dans la creation de documentation : capture d'ecrans pour tutoriels, extraction de contenu web et generation de guides visuels.

## Cas d'usage
- Captures d'ecran pour documentation
- Extraction de contenu web pour wikis
- Generation de guides visuels step-by-step
- Archivage de pages web pour reference
- Documentation de configuration web (Grafana, n8n, etc.)

---

## Prompts prets a copier

### 1 -- Guide visuel step-by-step

```
Cree un guide visuel pour [PROCEDURE WEB] :
1. Naviguer vers [URL]
2. Pour chaque etape :
   - Screenshot de la page
   - Surligner l'element a cliquer (annotation)
   - Decrire l'action
3. Assembler les screenshots en guide Markdown
Sauvegarder dans ~/docs/guides/[NOM].md
```

---

### 2 -- Documenter une interface web

```
Documente l'interface de [URL] :
1. Screenshot de chaque page/vue
2. Pour chaque element interactif : nom, role, emplacement
3. Flux de navigation (page A → page B)
4. Generer un guide utilisateur avec screenshots
```

---

### 3 -- Archiver une page web

```
Archive cette page web pour reference future :
1. Screenshot pleine page
2. Extraire le HTML complet
3. Sauvegarder les images et CSS
4. Generer une version Markdown du contenu
5. Stocker dans ~/archives/[domaine]/[date]/
```

---

### 4 -- Documenter un dashboard Grafana

```
Documente le dashboard Grafana a [URL] :
1. Screenshot du dashboard complet
2. Screenshot de chaque panneau individuellement
3. Pour chaque panneau : titre, metrique, requete si visible
4. Generer la documentation en Markdown
```

---

### 5 -- Extraire la documentation d'un outil web

```
Extrais la documentation de [URL_DOC] :
1. Naviguer vers la table des matieres
2. Pour chaque section : extraire le contenu
3. Sauvegarder en Markdown local (un fichier par section)
4. Generer l'index avec liens
Pour consultation offline.
```

---

## Exemples d'utilisation

### Exemple : Guide Grafana
**Prompt** : "Capture et documente mon dashboard Grafana de monitoring GPU"

**Resultat attendu** : Guide avec screenshots annotes de chaque panneau.

---

## Effet sur le modele
- BrowserOS capture les interfaces reelles pour la documentation
- Les screenshots annotes sont plus clairs que les descriptions textuelles
- L'archivage web preserve le contenu pour reference future
- La documentation d'interfaces web est automatisee
