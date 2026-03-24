# BrowserOS — Automation Web

> Prompts pour l'automatisation web avec BrowserOS via Chrome DevTools Protocol (CDP).

---

## Prompt d'automatisation generique

```
Automatise la tache web suivante avec BrowserOS :

## Tache
[DECRIRE LA TACHE : navigation, remplissage formulaire, scraping, etc.]

## Site cible
URL : [URL]
Authentification requise : OUI/NON
Si OUI : methode (cookies, login form, OAuth)

## Etapes
1. [ETAPE 1]
2. [ETAPE 2]
3. [ETAPE N]

## Donnees a extraire
- [CHAMP 1] : [SELECTEUR CSS OU XPATH]
- [CHAMP 2] : [SELECTEUR CSS OU XPATH]

## Format de sortie
JSON / CSV / Texte brut

## Gestion d'erreurs
- Timeout : 30 secondes par page
- Si element non trouve : screenshot + retry 1 fois
- Si captcha : alerter Telegram et attendre intervention
```

### Ce que ca fait
Configure une tache d'automatisation web complete via BrowserOS. Le navigateur headless execute les etapes de maniere autonome.

### Effet sur le modele
- Le format structure couvre tous les cas limites (auth, erreurs, timeout)
- Les selecteurs CSS/XPath explicites evitent l'ambiguite
- La gestion d'erreurs previent les echecs silencieux

### Exemple concret

```
Automatise avec BrowserOS :

## Tache
Extraire les prix des 50 premiers tokens sur CoinGecko

## Site cible
URL : https://www.coingecko.com/
Authentification : NON

## Etapes
1. Naviguer vers la page d'accueil
2. Attendre le chargement du tableau
3. Extraire les 50 premieres lignes

## Donnees a extraire
- Rang : td:nth-child(2)
- Nom : td:nth-child(3) a
- Prix : td:nth-child(4) span
- Variation 24h : td:nth-child(5) span

## Format de sortie
JSON array

## Gestion d'erreurs
- Si bloque par Cloudflare : attendre 10s et retry
- Si tableau incomplet : scroller et attendre
```

---

## Prompt de scraping structure

```
Configure un scraper BrowserOS pour [SITE] :

1. Navigation : [URLs a visiter]
2. Pagination : [Comment passer a la page suivante]
3. Donnees : [Quels elements extraire]
4. Frequence : [Combien de fois par jour]
5. Stockage : [Ou sauvegarder les donnees]

Le scraper doit :
- Respecter un delai de 2-5 secondes entre les requetes
- Utiliser un User-Agent realiste
- Gerer les redirections
- Detecter les pages d'erreur (403, 404, 500)
- Envoyer un rapport par Telegram a la fin
```

---

## Prerequis
- BrowserOS installe (Docker recommande)
- Configuration CDP dans JARVIS (src/browseros_cdp.py)
- MCP server browseros-mcp actif

## Version Courte (Modèles Locaux <4B)

> Pour qwen2.5:1.5b, gemma-3-4b et petits modèles

```text
[Rôle en 1 ligne]. [Tâche en 1 ligne]. Réponds en 3 lignes max. Français.
```
