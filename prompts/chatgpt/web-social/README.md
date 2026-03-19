# ChatGPT — Web & Social Media

> Prompts optimises pour la creation de contenu LinkedIn, reseaux sociaux et emails avec ChatGPT.

---

## Description

ChatGPT est performant pour la redaction de contenu professionnel : posts LinkedIn, tweets, emails, newsletters. GPT-4o comprend le ton, le format et les codes de chaque plateforme.

## Configuration

- Modele : GPT-4o
- Custom Instructions avec ton professionnel et domaine d'expertise
- Web Browsing pour les tendances actuelles

## Prompts par type

### Post LinkedIn
```
Redige un post LinkedIn sur [SUJET] :

## Contexte
- Mon profil : [ROLE / EXPERTISE]
- Audience cible : [DEVS / MANAGERS / TECH LEADS...]
- Objectif : [PARTAGE / THOUGHT LEADERSHIP / ENGAGEMENT]

## Format
- Hook accrocheur (premiere ligne)
- 3-5 paragraphes courts (2-3 lignes max)
- Bullet points pour les insights cles
- Call-to-action final
- 3-5 hashtags pertinents

## Ton
- Professionnel mais accessible
- Concret (pas de buzzwords vides)
- Basé sur l'experience (pas generique)
```

### Email professionnel
```
Redige un email pour [OBJECTIF] :

## Destinataire : [QUI]
## Contexte : [SITUATION]
## Ton : [FORMEL / SEMI-FORMEL / DECONTRACTE]

## Structure
- Objet accrocheur
- Introduction (1-2 phrases)
- Corps du message (clair et actionnable)
- Call-to-action explicite
- Formule de politesse appropriee
```

### Thread Twitter/X
```
Cree un thread Twitter/X sur [SUJET] :

## Format
- Tweet 1 : Hook (max 280 caracteres, accrocheur)
- Tweets 2-8 : Contenu (1 idee par tweet)
- Tweet final : Resume + CTA

## Contraintes
- Max 280 caracteres par tweet
- Emojis : 1-2 par tweet max
- Chaque tweet doit etre comprehensible seul
- Numerotation : 1/N
```

### Newsletter technique
```
Redige une newsletter technique sur [SUJET] :

## Format
- Titre accrocheur
- TL;DR (3 lignes)
- Contenu principal structure en sections
- Liens et ressources
- "Ce que j'en pense" (opinion personnelle)
- Call-to-action
```

## Exemples concrets

```
Redige un post LinkedIn sur mon experience de migration d'un assistant vocal
de Windows a Linux avec 6 GPUs.

Profil : Dev senior / homelab enthusiast
Audience : Devs et tech leads
Angle : les pieges de la migration et ce que j'ai appris
Ton : retour d'experience concret, pas vendeur
```

```
Redige un email a un recruteur tech pour decliner une offre poliment
mais garder la porte ouverte.
Contexte : l'offre est interessante mais le timing ne convient pas.
Ton : semi-formel, professionnel.
```

## Effet sur le modele

- ChatGPT connait tres bien les codes LinkedIn et Twitter — il genere du contenu au bon format
- Le hook est crucial sur LinkedIn — insister dessus dans le prompt
- GPT-4o a tendance a generer du contenu generique — l'ancrage dans l'experience personnelle force l'authenticite
- Le ton "pas de buzzwords" empeche le style corporate creux
- Pour les emails, specifier le niveau de formalite est essentiel — sinon ChatGPT est trop formel par defaut
