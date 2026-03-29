# Qwen3 -- Inference

## Description

Prompts optimises pour l'inference avec les modeles Qwen3, exploitant le multilinguisme et le mode thinking.

## Prompts optimises

### 1 -- Code avec raisonnement

```
/think
Cree une classe Python pour gerer un pool de connexions a une base de donnees :
- Nombre max de connexions configurable
- Timeout configurable
- Context manager (with)
- Thread-safe
- Tests unitaires
```

### 2 -- Analyse de donnees

```
Analyse ce fichier CSV et reponds :
1. Statistiques descriptives
2. Tendances identifiees
3. Anomalies detectees
4. Visualisation recommandee
5. Code Python pour generer les graphiques

Donnees :
[COLLER OU DECRIRE]
```

### 3 -- Traduction technique bidirectionnelle

```
Traduis ce texte technique en preservant le sens exact :

Source ([LANGUE]) :
[TEXTE]

Regles :
- Garder les termes techniques standards en anglais
- Adapter les exemples au contexte de la langue cible
- Conserver le formatage (code blocks, listes)
```

### 4 -- Agent avec outils

```
Objectif : [DESCRIPTION DE LA TACHE]

Outils disponibles :
- execute_command(cmd) : execute une commande bash
- read_file(path) : lit un fichier
- write_file(path, content) : ecrit un fichier
- search(query) : recherche dans le code

Utilise les outils necessaires pour accomplir l'objectif.
```

### 5 -- Resume multi-documents

```
Resume ces [N] documents en identifiant :
1. Themes communs
2. Points de divergence
3. Informations uniques a chaque document
4. Synthese globale (3-5 phrases)

Documents :
[COLLER]
```

---

## Parametres recommandes
| Cas d'usage | Temperature | Think | Num-ctx |
|-------------|-------------|-------|---------|
| Code | 0.1 | Oui | 4096 |
| Analyse | 0.2 | Oui | 8192 |
| Traduction | 0.1 | Non | 4096 |
| Creatif | 0.7 | Non | 4096 |
| Agent | 0.1 | Oui | 8192 |
