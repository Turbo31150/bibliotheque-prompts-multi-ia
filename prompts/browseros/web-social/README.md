# BrowserOS - Web & Social

## Vue d'ensemble

Gestion des interactions web et sociales via BrowserOS : publication LinkedIn via CDP, monitoring GitHub, gestion multi-onglets du cluster.

## Onglets pre-configures (23)

La session BrowserOS standard contient 23 onglets repartis en categories :

### IA & Chat

| # | Onglet | URL |
|---|--------|-----|
| 1 | ChatGPT | chat.openai.com |
| 2 | Claude | claude.ai |
| 3 | Gemini | gemini.google.com |
| 4 | Perplexity | perplexity.ai |

### Social & Pro

| # | Onglet | URL |
|---|--------|-----|
| 5 | LinkedIn Feed | linkedin.com/feed |
| 6 | LinkedIn Messaging | linkedin.com/messaging |
| 7 | LinkedIn Notifications | linkedin.com/notifications |

### Dev & Ops

| # | Onglet | URL |
|---|--------|-----|
| 8 | GitHub Dashboard | github.com |
| 9 | GitHub Notifications | github.com/notifications |
| 10 | GitHub PRs | github.com/pulls |
| 11 | n8n | localhost:5678 |
| 12 | Grafana | localhost:3000 |

### Trading

| # | Onglet | URL |
|---|--------|-----|
| 13 | MEXC Spot | mexc.com/exchange |
| 14 | MEXC Futures | futures.mexc.com |
| 15-23 | Autres dashboards | ... |

## LinkedIn via CDP

### Publication de posts

```javascript
// Sequence CDP pour publier sur LinkedIn
async function postLinkedIn(client, content) {
  const { Page, Runtime } = client;

  // Naviguer vers le feed
  await Page.navigate({ url: 'https://www.linkedin.com/feed/' });
  await Page.loadEventFired();

  // Cliquer sur "Commencer un post"
  await Runtime.evaluate({
    expression: `document.querySelector('[class*="share-box"]').click()`
  });

  // Attendre le modal
  await new Promise(r => setTimeout(r, 1500));

  // Saisir le contenu
  await Runtime.evaluate({
    expression: `document.querySelector('[role="textbox"]').innerText = \`${content}\``
  });

  // Publier
  await Runtime.evaluate({
    expression: `document.querySelector('[class*="share-actions"] button[class*="primary"]').click()`
  });
}
```

### Engagement automatise

- Scroll du feed avec pauses naturelles (2-5s entre chaque scroll)
- Like des posts pertinents (filtrage par mots-cles)
- Commentaires generes par le social-agent OpenClaw

## GitHub monitoring

- Verification des notifications toutes les 30 min
- Extraction des nouvelles PRs et issues via DOM
- Dispatch des evenements vers OpenClaw pour traitement

## Gestion multi-onglets

```bash
# Lister les onglets ouverts
curl -s http://localhost:9105/json/list | jq '.[].title'

# Activer un onglet specifique
curl -s http://localhost:9105/json/activate/{targetId}

# Ouvrir un nouvel onglet
curl -s http://localhost:9105/json/new?url=https://example.com
```

## Sauvegarde de session

La configuration des 23 onglets est sauvegardee pour restauration rapide apres redemarrage de Chrome.
