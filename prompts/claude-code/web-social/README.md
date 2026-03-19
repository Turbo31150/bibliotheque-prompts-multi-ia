# Claude Code — Web et Social

## Description
Prompts pour l'automatisation web et sociale avec Claude Code : publication LinkedIn, automatisation GitHub, pilotage navigateur BrowserOS via CDP (Chrome DevTools Protocol) et bot Telegram.

## Configuration requise
- Claude Code avec MCP `browseros-mcp` actif
- BrowserOS installe avec CDP (Chrome DevTools Protocol)
- Compte LinkedIn connecte dans le navigateur BrowserOS
- Bot Telegram configure (token dans .env)
- GitHub CLI (`gh`) installe et authentifie
- Cron configure pour les executions planifiees

---

## Prompts par type de tache

### Creation — Strategie de croissance LinkedIn

```
Configure une strategie de croissance LinkedIn automatisee :

## Profil
- Secteur : [SECTEUR]
- Cible : [TYPE_DE_CONTACTS]
- Objectif mensuel : [NOMBRE_CONNEXIONS]

## Actions automatisees (via BrowserOS)

### 1. Engagement quotidien (8h et 12h)
- Liker les 10 derniers posts du feed
- Commenter 3 posts pertinents (commentaires pre-ecrits varies)
- Partager 1 article avec commentaire personnalise

### 2. Connexions (toutes les 4h)
- Chercher des profils correspondant aux criteres
- Envoyer 5 demandes de connexion avec message personnalise
- Template : "Bonjour [PRENOM], [MESSAGE_CONTEXTUEL]. Au plaisir d'echanger !"

### 3. Publication (1x par jour, 8h)
- Publier un post prepare (file d'attente de posts)
- Alterner : texte, image, carrousel, sondage
- Hashtags adaptes au secteur

## Limites de securite
- Maximum 20 connexions/jour (eviter le ban)
- Maximum 50 likes/jour
- Maximum 10 commentaires/jour
- Delai aleatoire 30-120 secondes entre chaque action
- Pause si detection de captcha
- Pas d'actions entre 23h et 7h

## Reporting
- Rapport quotidien Telegram : connexions acceptees, vues, interactions
- Rapport hebdomadaire : croissance, meilleurs posts, taux d'acceptation
```

---

### Creation — Messages LinkedIn personnalises

```
Genere 20 variantes de messages de connexion LinkedIn pour [SECTEUR].

Contraintes :
- Maximum 300 caracteres
- Ton professionnel mais amical
- Mentionner un point commun (secteur, ville, interet)
- Pas de pitch commercial
- Terminer par une question ouverte

Variantes par contexte :
- 5 messages pour des developpeurs
- 5 messages pour des CTO/VP Engineering
- 5 messages pour des entrepreneurs
- 5 messages pour des recruteurs
```

---

### Creation — Automatisation GitHub

```
Configure l'automatisation GitHub pour le projet [REPO] :

## ACTIONS AUTOMATISEES
1. PR Auto-review :
   - A chaque PR, lancer une code review automatique
   - Verifier : tests passent, lint OK, couverture maintenue
   - Commenter avec le rapport de review

2. Issue Triage :
   - Classer automatiquement les nouvelles issues (bug, feature, question)
   - Ajouter les labels correspondants
   - Assigner au bon mainteneur

3. Release Notes :
   - Generer les notes de release depuis les commits
   - Format : Keep a Changelog
   - Inclure les contributeurs

4. Stale Issues :
   - Marquer les issues sans activite depuis 30 jours
   - Fermer apres 60 jours sans activite
   - Notification avant fermeture

## IMPLEMENTATION
- GitHub Actions pour les workflows CI
- Webhook vers n8n pour les actions complexes
- Cron github_watchdog.js toutes les 2 heures
```

---

### Creation — Bot Telegram JARVIS

```
Configure le bot Telegram JARVIS :

## FONCTIONNALITES
1. Commandes :
   - /status — Status du cluster et des services
   - /gpu — Temperatures GPU
   - /trading — Resume positions ouvertes
   - /health — Health check complet
   - /ask [question] — Question au cluster IA
   - /scan [paire] — Scan rapide d'une paire crypto

2. Alertes automatiques :
   - GPU temperature > 75C
   - Service down
   - Trade execute (entree/sortie)
   - Backup termine
   - Erreur critique dans les logs

3. Rapport quotidien (8h) :
   - Resume de la nuit (crons executes, erreurs)
   - Status du cluster
   - Positions trading ouvertes
   - Taches du jour

## SECURITE
- Restreint aux chat_id autorises
- Rate limiting : 10 commandes/minute
- Log de toutes les interactions
```

---

### Amelioration / Refactoring — Optimiser le scraping web

```
Optimise le scraping web via BrowserOS :

1. Identifie les pages scrapees regulierement
2. Pour chaque page :
   - Temps de chargement actuel
   - Elements extraits
   - Frequence de scraping
3. Optimisations :
   - Utiliser les selecteurs CSS au lieu de XPath (plus rapide)
   - Bloquer les images/CSS/JS non necessaires
   - Utiliser le cache pour les pages stables
   - Paralleliser les scraping independants
4. Mesurer avant/apres
```

---

### Debug — BrowserOS ne repond pas

```
BrowserOS ne repond pas aux commandes CDP.

## CHECKLIST
1. Le container Docker tourne ? (docker ps | grep browseros)
2. Le port CDP est ouvert ? (ss -tlnp | grep 9222)
3. Chrome demarre correctement dans le container ?
4. Le MCP browseros-mcp repond ? (test d'appel MCP)
5. Les cookies de session sont valides ? (LinkedIn, GitHub)
6. Le proxy est configure ? (si necessaire)

## ACTIONS
- Container arrete : docker start browseros
- Port non ouvert : verifier la config Docker (port mapping)
- Session expiree : re-login manuellement, sauvegarder les cookies
```

---

### Documentation — Rapport d'activite sociale

```
Genere un rapport d'activite web et sociale :

## FORMAT
### LinkedIn
- Connexions envoyees / acceptees cette semaine
- Posts publies et engagement (likes, commentaires, partages)
- Vues de profil
- Croissance nette

### GitHub
- PRs creees / mergees
- Issues ouvertes / fermees
- Commits
- Contributeurs actifs

### Telegram
- Messages envoyes (alertes, rapports)
- Commandes recues et traitees
- Erreurs de livraison

### BrowserOS
- Sessions CDP actives
- Pages visitees
- Actions automatisees executees
- Erreurs de scraping
```

---

## Exemples concrets

### Exemple 1 : Publier sur LinkedIn
```bash
claude "Publie sur LinkedIn : [CONTENU DU POST] avec les hashtags #IA #DevOps #Linux"
```

**Resultat attendu** : Post publie via BrowserOS CDP, confirmation avec lien vers le post.

### Exemple 2 : Automatiser GitHub
```bash
claude "Configure un GitHub Action qui lance les tests et la code review a chaque PR"
```

**Resultat attendu** : Fichier .github/workflows/ci.yml cree, PR de test pour verifier.

### Exemple 3 : Alerte Telegram
```bash
claude "/notify 'Cluster degrade : noeud M2 offline'"
```

**Resultat attendu** : Message envoye sur Telegram avec le status detaille.

---

## Effet sur le modele
- Les limites de securite LinkedIn (20 connexions/jour) empechent les bans
- Le delai aleatoire entre actions simule un comportement humain
- Le format de reporting structure permet le suivi de la croissance
- L'automatisation GitHub reduit le travail manuel de maintenance
- Le bot Telegram centralise les notifications et commandes a distance
- BrowserOS via CDP permet le pilotage web sans API officielle
