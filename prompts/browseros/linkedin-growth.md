# BrowserOS — LinkedIn Growth

> Prompts pour l'automatisation LinkedIn via BrowserOS.

---

## Prompt de croissance LinkedIn

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
- Pause si detection de captcha LinkedIn
- Pas d'actions entre 23h et 7h

## Reporting
- Rapport quotidien Telegram : connexions acceptees, vues, interactions
- Rapport hebdomadaire : croissance, meilleurs posts, taux d'acceptation
```

### Ce que ca fait
Automatise la croissance organique LinkedIn tout en respectant les limites de la plateforme.

### Effet sur le modele
- Le format structure avec limites de securite empeche l'over-automation
- Les templates personnalises evitent le spam generique
- Le reporting permet d'ajuster la strategie

### Comment l'utiliser
1. Configurer les templates de messages et commentaires
2. Preparer la file d'attente de posts (1 semaine d'avance)
3. Lancer via cron (toutes les 4h)
4. Surveiller les rapports Telegram

---

## Prompt de message personnalise

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

## Prerequis
- BrowserOS installe avec CDP
- Compte LinkedIn connecte dans le navigateur BrowserOS
- Cron configure pour les executions planifiees
- Bot Telegram pour les rapports
