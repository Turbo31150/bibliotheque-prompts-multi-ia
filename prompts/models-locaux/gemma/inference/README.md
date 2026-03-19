# Gemma -- Inference

## Description

Prompts optimises pour l'inference avec les modeles Gemma : cas d'usage, parametres et bonnes pratiques.

## Prompts optimises

### 1 -- Code generation

```
<start_of_turn>user
Ecris une fonction Python qui calcule les indicateurs RSI et MACD a partir d'une liste de prix de cloture. Inclus les docstrings et le typage.
<end_of_turn>
<start_of_turn>model
```

### 2 -- Analyse de texte

```
Analyse ce texte et extrais les entites en JSON :
{personnes: [], lieux: [], organisations: [], dates: []}

Texte : [COLLER LE TEXTE]
```

### 3 -- Traduction technique

```
Traduis ce texte technique de l'anglais au francais.
Conserve les termes techniques en anglais quand ils sont standards
(Docker, container, API, endpoint, etc.).

[TEXTE ANGLAIS]
```

### 4 -- Resume structure

```
Resume ce document en format structure :
## Points cles (3-5 bullets)
## Details importants
## Actions requises
## Questions ouvertes

Document : [COLLER]
```

### 5 -- Generation de commandes

```
Genere la commande Linux pour : [DESCRIPTION EN LANGAGE NATUREL]
Format : uniquement la commande, pas d'explication.
Si plusieurs etapes : une commande par ligne avec commentaires.
```

---

## Parametres recommandes
| Cas d'usage | Temperature | Top-p | Num-ctx |
|-------------|-------------|-------|---------|
| Code | 0.1-0.2 | 0.9 | 4096 |
| Analyse | 0.2-0.3 | 0.9 | 8192 |
| Creatif | 0.7-0.9 | 0.95 | 4096 |
| Traduction | 0.1 | 0.9 | 4096 |
