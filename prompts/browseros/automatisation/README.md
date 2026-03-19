# BrowserOS - Automatisation

## Vue d'ensemble

Scripts d'automatisation navigateur executes via BrowserOS. Chaque script se connecte au CDP (port 9105) via `browser_runner.js` et effectue des actions automatisees dans les onglets.

## Scripts d'automatisation

### health_patrol.js

Verification periodique de la sante des onglets ouverts.

- **Fonction** : parcourt chaque onglet, verifie le chargement, detecte les erreurs
- **Schedule** : toutes les 10 minutes
- **Actions** : reload des onglets plantes, notification si un site est down

### trading_monitor.js

Surveillance des dashboards de trading.

- **Fonction** : capture les prix, detecte les alertes visuelles sur MEXC
- **Schedule** : toutes les 5 minutes
- **Actions** : screenshot si signal detecte, notification vocale si alerte critique

### github_watchdog.js

Monitoring des repositories GitHub.

- **Fonction** : verifie les notifications, nouvelles PRs, issues
- **Schedule** : toutes les 30 minutes
- **Actions** : extraction des donnees, dispatch vers l'agent dev

### linkedin_engagement.js

Automatisation de l'engagement LinkedIn.

- **Fonction** : scroll du feed, likes strategiques, commentaires generes par IA
- **Schedule** : 2 fois par jour (10h et 15h)
- **Actions** : interactions mesurees pour garder un profil naturel

## Execution via browser_runner.js

Le runner central gere la connexion CDP et l'execution des scripts :

```javascript
// browser_runner.js se connecte au CDP
const CDP = require('chrome-remote-interface');

async function runSkill(skillName, params) {
  const client = await CDP({ port: 9105 });
  const skill = require(`./skills/${skillName}`);
  const result = await skill.execute(client, params);
  await client.close();
  return result;
}
```

### Lancement manuel

```bash
# Executer un script directement
node browser_runner.js --skill health_patrol

# Avec parametres
node browser_runner.js --skill trading_monitor --pair BTCUSDT

# Via API MCP
curl -X POST http://localhost:9001/skills/run \
  -H "Authorization: Bearer $BROWSEROS_MCP_TOKEN" \
  -d '{"skill": "github_watchdog", "params": {}}'
```

## Cron scheduling

Les scripts sont planifies via crontab ou via OpenClaw :

```cron
*/10 * * * * node /path/to/browser_runner.js --skill health_patrol
*/5  * * * * node /path/to/browser_runner.js --skill trading_monitor
*/30 * * * * node /path/to/browser_runner.js --skill github_watchdog
0 10,15 * * * node /path/to/browser_runner.js --skill linkedin_engagement
```

## Gestion des erreurs

- Les scripts attendent le chargement complet (`waitForSelector`) avant d'agir
- Timeout de 30 secondes par defaut pour chaque action
- En cas d'echec, le runner log l'erreur et passe au script suivant
- Les screenshots d'erreur sont sauvegardes dans `logs/screenshots/`
