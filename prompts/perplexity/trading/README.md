# Perplexity — Trading & Crypto

> Prompts optimises pour la recherche crypto et l'analyse de marche avec Perplexity.

---

## Description

Perplexity est ideal pour la recherche crypto grace a son acces en temps reel aux donnees web : actualites, analyses de marche, donnees on-chain, sentiment. Chaque information est sourcee, ce qui est critique pour les decisions financieres.

## Configuration

- Perplexity Pro recommande (recherches approfondies)
- Focus : Web pour les actualites, Academic pour les papers DeFi
- Collections pour organiser la veille par asset/theme

## Prompts par type

### Analyse de marche en temps reel
```
Analyse du marche crypto aujourd'hui :

1. BTC : prix, variation 24h, volume, sentiment
2. Top 5 gainers/losers (avec %)
3. Evenements majeurs du jour
4. Fear & Greed Index actuel
5. Flux institutionnels (ETF, treasuries)

Sources pour chaque donnee.
```

### Recherche fondamentale sur un projet
```
Recherche approfondie sur [CRYPTO/PROJET] :

1. Description du projet et use case
2. Equipe (fondateurs, background, track record)
3. Tokenomics detaillees (supply, distribution, vesting)
4. Metriques on-chain recentes (TVL, transactions, holders)
5. Derniers developpements (30 derniers jours)
6. Concurrents directs et positionnement
7. Risques identifies
8. Prochains catalyseurs

Sources pour chaque point.
Score conviction /10.
```

### Veille crypto quotidienne
```
Veille crypto des dernieres 24h :

## Actualites majeures
- Regulations (SEC, EU, Asie)
- Hacks / exploits
- Listings / delistings
- Partnerships
- Upgrades de protocoles

## Donnees marche
- BTC dominance
- Total market cap
- DeFi TVL
- Stablecoin flows

Pour chaque news : source, date, impact estime.
```

### Analyse de sentiment
```
Analyse le sentiment actuel sur [CRYPTO] :

Sources a rechercher :
- Twitter/X (comptes influents)
- Reddit (subreddits principaux)
- Articles d'analyse recents
- Donnees on-chain (whale movements)
- Funding rates et open interest

Synthese :
- Sentiment global : BEARISH / NEUTRAL / BULLISH
- Arguments bull (avec sources)
- Arguments bear (avec sources)
- Catalyseurs a court terme
```

### Recherche reglementaire
```
Quel est le cadre reglementaire actuel pour [SUJET_CRYPTO] ?

## Zones geographiques
- USA (SEC, CFTC)
- Europe (MiCA)
- Asie (Japon, Singapour, Hong Kong)

## Format
Pour chaque zone :
- Reglementation en vigueur
- Changements recents
- Changements prevus
- Impact sur [CRYPTO/USAGE]
- Source officielle
```

## Exemples concrets

```
Recherche approfondie sur Solana (SOL) :
Metriques on-chain, developpements recents, concurrence avec Ethereum L2s.
Focus : adoption DeFi, NFT, et gaming.
Sources pour chaque point.
```

```
Veille crypto des 7 derniers jours :
Focus sur les reglementations SEC et les ETF crypto.
Impact sur BTC et ETH.
```

```
Analyse le sentiment sur Bitcoin apres le dernier FOMC :
Sources Twitter, Reddit, analystes, donnees on-chain.
Bull case vs Bear case source.
```

## Effet sur le modele

- Perplexity est le meilleur outil pour la veille crypto grace aux citations en temps reel
- Les donnees de prix sont generalement a jour (quelques minutes de delai)
- Le Pro Search fait des recherches multi-sources — ideal pour croiser les informations
- Attention : Perplexity peut sourcer des articles d'opinion comme des faits — toujours verifier la nature de la source
- Pour les donnees on-chain, Perplexity agrege mais ne remplace pas les outils specialises (Dune, DefiLlama)
- Ne jamais prendre de decision financiere basee uniquement sur une recherche IA
