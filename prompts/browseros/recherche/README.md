# BrowserOS - Recherche

## Vue d'ensemble

Automatisation de la recherche web via BrowserOS : recherche Perplexity, extraction de donnees, capture de screenshots pour analyse.

## Recherche Perplexity

Perplexity est l'un des 23 onglets pre-configures. BrowserOS peut y effectuer des recherches automatisees.

### Recherche automatisee

```javascript
async function searchPerplexity(client, query) {
  const { Page, Runtime } = client;

  // Naviguer vers Perplexity
  await Page.navigate({ url: 'https://www.perplexity.ai/' });
  await Page.loadEventFired();

  // Saisir la requete
  await Runtime.evaluate({
    expression: `
      const input = document.querySelector('textarea[placeholder*="Ask"]');
      input.value = "${query}";
      input.dispatchEvent(new Event('input', { bubbles: true }));
    `
  });

  // Soumettre
  await Runtime.evaluate({
    expression: `document.querySelector('button[aria-label="Submit"]').click()`
  });

  // Attendre la reponse (polling du DOM)
  await waitForResponse(client, 30000);

  // Extraire le resultat
  const result = await Runtime.evaluate({
    expression: `document.querySelector('[class*="answer"]').innerText`
  });

  return result.result.value;
}
```

## Extraction de donnees

BrowserOS peut extraire des donnees structurees depuis n'importe quelle page :

```javascript
async function extractData(client, url, selectors) {
  const { Page, Runtime } = client;

  await Page.navigate({ url });
  await Page.loadEventFired();

  const data = {};
  for (const [key, selector] of Object.entries(selectors)) {
    const result = await Runtime.evaluate({
      expression: `document.querySelector('${selector}')?.innerText || null`
    });
    data[key] = result.result.value;
  }

  return data;
}
```

### Exemple : extraction de metriques GitHub

```javascript
const githubMetrics = await extractData(client, 'https://github.com/turbo/jarvis-linux', {
  stars: '[id="repo-stars-counter-star"]',
  forks: '[id="repo-network-counter"]',
  issues: '[id="issues-repo-tab-count"]'
});
```

## Capture de screenshots

### Screenshot complet

```javascript
async function fullScreenshot(client, url, filename) {
  const { Page } = client;

  await Page.navigate({ url });
  await Page.loadEventFired();
  await new Promise(r => setTimeout(r, 2000)); // Attendre rendu JS

  const screenshot = await Page.captureScreenshot({ format: 'png' });
  fs.writeFileSync(filename, Buffer.from(screenshot.data, 'base64'));

  return filename;
}
```

### Screenshot partiel (zone specifique)

```javascript
const screenshot = await Page.captureScreenshot({
  format: 'png',
  clip: { x: 100, y: 200, width: 800, height: 400, scale: 1 }
});
```

## Integration avec le pipeline

```
Requete recherche -> BrowserOS (Perplexity) -> Extraction texte
  -> Retour a l'agent OpenClaw pour synthese
  -> Reponse TTS via jarvis-tts.sh (si requete vocale)
```

## Cas d'usage

| Cas | Source | Extraction |
|-----|--------|------------|
| Veille technologique | Perplexity, HackerNews | Texte + liens |
| Analyse concurrentielle | Sites web cibles | Donnees structurees |
| Documentation technique | MDN, StackOverflow | Code + explications |
| Cours crypto | CoinGecko, CoinMarketCap | Prix, volumes, marketcap |
