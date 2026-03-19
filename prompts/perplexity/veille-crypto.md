# Perplexity — Veille Crypto

> Prompts pour la veille crypto et trading avec Perplexity AI.

---

## Prompt de veille crypto quotidienne

```
Veille crypto du jour. Analyse les dernieres 24h :

## Marche global
- Bitcoin : prix, variation 24h, dominance
- Ethereum : prix, variation 24h
- Market cap total
- Fear & Greed Index
- Volume 24h global

## Top movers
- Top 5 hausses (> $100M market cap)
- Top 5 baisses (> $100M market cap)
- Raison identifiee pour chaque mouvement

## Actualites majeures
- Regulations (SEC, EU, pays majeurs)
- Hacks / exploits
- Listings / delistings sur exchanges majeurs
- Fusions / acquisitions
- Mises a jour de protocoles

## Analyse technique rapide
- Bitcoin : support et resistance cles
- Ethereum : support et resistance cles
- Signaux : RSI, MACD, volume profile

## Source de chaque information
Lien vers la source originale.
```

### Ce que ca fait
Briefing crypto complet en une seule requete. Perplexity cherche les informations en temps reel.

### Effet sur le modele
- Perplexity a acces aux donnees en temps reel — ideal pour la crypto
- Le format structure force une couverture exhaustive
- Les sources permettent de verifier les informations

### Comment l'utiliser
- Executer chaque matin pour le briefing quotidien
- Peut etre automatise via n8n + API Perplexity

---

## Prompt d'analyse d'un token

```
Analyse complete du token [SYMBOL] :

## Fondamentaux
- Projet : description en 3 lignes
- Equipe : qui est derriere
- Technologie : consensus, TPS, smart contracts
- Tokenomics : supply, inflation, distribution
- Utilite : a quoi sert le token concretement

## Metriques
- Prix actuel et ATH
- Market cap et rank
- Volume 24h
- Holders (nombre et concentration)
- TVL si DeFi

## Analyse technique
- Tendance court terme (1-7 jours)
- Tendance moyen terme (1-3 mois)
- Supports et resistances cles
- Patterns identifies

## Risques
- Risques techniques (bugs, hacks passes)
- Risques reglementaires
- Risques de centralisation
- Risques de liquidite

## Verdict
Score global /10 avec justification.
Horizon recommande : court / moyen / long terme.
```

---

## Prompt de detection d'opportunites

```
Identifie les opportunites crypto du moment :

Criteres :
- Market cap entre $10M et $500M (small/mid cap)
- Volume 24h en hausse de > 50%
- Catalyseurs identifies (listing, update, partenariat)
- Pas de red flags (rug pull risk, equipe anonyme)

Pour chaque opportunite (max 5) :
- Token et exchange disponible
- Raison de l'opportunite
- Prix d'entree suggere
- Stop loss suggere
- Take profit suggere
- Risque : LOW / MEDIUM / HIGH

DISCLAIMER : Ce n'est pas un conseil financier.
```

---

## Prerequis
- Compte Perplexity Pro (recommande pour les recherches en temps reel)
- Pour l'automatisation : API Perplexity + n8n
