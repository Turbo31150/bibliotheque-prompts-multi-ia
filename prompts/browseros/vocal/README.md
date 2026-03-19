# BrowserOS -- Vocal

## Description

Prompts pour utiliser BrowserOS MCP dans l'interaction vocale avec des pages web : lecture de contenu web a voix haute, navigation vocale et extraction de texte pour TTS.

## Cas d'usage
- Lecture de contenu web pour TTS
- Navigation web par commandes vocales
- Extraction de texte pour synthese vocale
- Verification vocale de contenu web
- Podcast automatique depuis articles web

---

## Prompts prets a copier

### 1 -- Lire un article web a voix haute

```
Utilise BrowserOS pour lire cet article a voix haute :
1. Naviguer vers [URL]
2. Extraire le contenu principal (sans pub, navigation, footer)
3. Nettoyer pour le TTS (pas de HTML, pas de liens)
4. Decouper en paragraphes
5. Envoyer chaque paragraphe a jarvis-tts.sh
```

---

### 2 -- Navigation web vocale

```
Interprete cette commande vocale pour naviguer sur le web :
"[COMMANDE VOCALE]"

Actions possibles :
- "Ouvre [site]" → naviguer vers l'URL
- "Cherche [terme]" → recherche Google
- "Lis la page" → extraire et lire le contenu
- "Clique sur [texte]" → cliquer sur le lien/bouton
- "Descends" → scroller vers le bas
- "Screenshot" → capturer l'ecran
```

---

### 3 -- Resume vocal d'une page web

```
1. Naviguer vers [URL]
2. Extraire tout le contenu textuel
3. Envoyer a Claude pour un resume en 3 phrases
4. Formater le resume pour le TTS (max 15 mots par phrase)
5. Lire le resume via jarvis-tts.sh
```

---

### 4 -- Podcast automatique depuis articles

```
Genere un podcast depuis ces articles :
[LISTER LES URLs]

1. Scraper le contenu de chaque article
2. Generer un script de podcast (intro, contenu, transitions, conclusion)
3. Formater pour le TTS (ton conversationnel, pauses)
4. Generer l'audio via TTS
5. Sauvegarder en MP3 dans ~/podcasts/
```

---

### 5 -- Verification vocale d'un site

```
Verifie vocalement que [URL] affiche les bonnes informations :
1. Naviguer vers la page
2. Extraire les elements cles (prix, statut, metriques)
3. Annoncer vocalement : "Le site affiche [CONTENU]"
4. Si valeur anormale : alerte vocale
```

---

## Exemples d'utilisation

### Exemple : Lecture d'article
**Prompt** : "Lis-moi cet article sur le dernier GPU NVIDIA [URL]"

**Resultat attendu** : Contenu de l'article lu a voix haute via TTS.

---

## Effet sur le modele
- BrowserOS accede au contenu web reel pour la lecture vocale
- L'extraction de contenu principal elimine le bruit (pubs, navigation)
- Le formatage TTS rend le contenu web ecoutable naturellement
- La navigation vocale rend le web accessible sans ecran
