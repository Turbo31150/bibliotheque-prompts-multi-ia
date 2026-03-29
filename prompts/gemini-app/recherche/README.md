# Gemini App — Recherche

> Prompts optimises pour la recherche avec Gemini App : grounded search, web research.

---

## Description

Gemini App dispose du "grounding" natif via Google Search : les reponses sont ancrees dans des resultats web recents et cites. C'est un avantage majeur pour la recherche technique, la veille et la verification de faits.

## Configuration

- Gemini App (gemini.google.com) ou AI Studio
- Grounding active (Google Search integration)
- Gemini Advanced pour les recherches complexes

## Prompts par type

### Recherche technique grounded
```
Recherche avec sources web actuelles :

[SUJET DE RECHERCHE]

## Consignes
- Base tes reponses sur des sources web recentes (2025-2026)
- Cite chaque source avec URL
- Indique la date de chaque source
- Distingue faits verifies et opinions

## Format
1. Resume (3-5 lignes)
2. Details par aspect
3. Sources citees avec URLs
4. Fiabilite estimee de chaque source
```

### Veille technologique
```
Veille technologique sur [DOMAINE] :

Quelles sont les nouveautes des 30 derniers jours ?

Pour chaque element :
- Date de publication
- Source (URL)
- Resume en 2 lignes
- Impact : FAIBLE / MOYEN / FORT
- Action : IGNORER / SURVEILLER / ADOPTER

Classe par impact decroissant.
```

### Verification de faits (fact-checking)
```
Verifie cette affirmation :

"[AFFIRMATION A VERIFIER]"

1. Est-ce vrai, faux ou partiellement vrai ?
2. Sources qui confirment
3. Sources qui infirment
4. Contexte manquant
5. Verdict final avec niveau de confiance (%)
```

### Recherche comparative avec sources
```
Compare [OPTION_A] vs [OPTION_B] pour [CAS_D_USAGE] :

## Criteres
- Performance (benchmarks recents)
- Communaute et support
- Documentation
- Cout
- Integration avec [STACK]

## Exigences
- Uniquement des donnees sourcees (pas d'opinions sans source)
- Benchmarks avec liens
- Tableau comparatif final
- Recommendation argumentee
```

### Recherche d'alternatives
```
Je cherche des alternatives a [OUTIL/SERVICE] :

## Criteres
- [CRITERE_1]
- [CRITERE_2]
- [CRITERE_3]

## Format
Pour chaque alternative :
- Nom + URL officielle
- Description en 2 lignes
- Score /10 par critere
- Prix
- Avantage cle / Inconvenient cle
```

## Exemples concrets

```
Recherche les dernieres avancees en inference locale de LLM sur GPU consumer :
- Nouveaux frameworks (vLLM, llama.cpp, Ollama)
- Benchmarks recents sur RTX 3090/4090
- Techniques de quantization (GPTQ, AWQ, GGUF)
- Sources avec URLs et dates
```

```
Verifie : "Python 3.13 a un JIT compiler qui ameliore les performances de 30%"
Sources, contexte, verdict.
```

```
Compare pour un dashboard de monitoring :
- Grafana vs Prometheus UI vs Netdata
Criteres : facilite d'installation, performance, GPU monitoring, cout.
Sources et benchmarks recents uniquement.
```

## Effet sur le modele

- Le grounding Google Search est la force majeure de Gemini App — les reponses sont ancrees dans des donnees recentes
- Les citations sont generalement fiables mais doivent etre verifiees (les URLs peuvent etre approximatives)
- Le format "sources + dates" force la transparence sur l'origine des informations
- Gemini avec grounding est plus fiable que ChatGPT pour les informations recentes (acces direct a Google Search)
- Pour les benchmarks, toujours demander les liens directs — Gemini peut synthetiser des chiffres de memoire
- La veille technologique est un cas d'usage ideal pour Gemini App grace au grounding
