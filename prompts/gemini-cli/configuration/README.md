# Gemini CLI — Configuration

> Guide d'installation et de configuration de Gemini CLI.

---

## Description

Gemini CLI est l'interface en ligne de commande pour interagir avec les modeles Google Gemini directement depuis le terminal. Ideal pour l'integration dans des workflows Linux et des scripts d'automatisation.

## Configuration

### Installation
```bash
# Installation via npm
npm install -g @google/gemini-cli

# Ou via pip (wrapper Python)
pip install google-generativeai
```

### Cle API
```bash
# Obtenir une cle sur https://aistudio.google.com/apikey
export GEMINI_API_KEY="votre-cle-api"

# Ajouter au .bashrc/.zshrc pour persistance
echo 'export GEMINI_API_KEY="votre-cle-api"' >> ~/.bashrc
```

### Modeles disponibles
| Modele | Usage | Contexte |
|--------|-------|----------|
| gemini-2.5-pro | Taches complexes, code, raisonnement | 1M tokens |
| gemini-2.5-flash | Rapide, economique | 1M tokens |
| gemini-2.0-flash | Ultra-rapide | 1M tokens |

### Fichier GEMINI.md
Le fichier `GEMINI.md` a la racine du projet configure le comportement par defaut :

```markdown
# GEMINI.md

Tu es un assistant technique senior Linux/Python.
- Reponds en francais
- Code avec type hints
- Pas de commentaires inutiles
- Format markdown structure
- Exemples concrets systematiques
```

### Settings
```bash
# Configuration du modele par defaut
gemini config set model gemini-2.5-pro

# Configuration du timeout
gemini config set timeout 120

# Verification
gemini config list
```

## Prompts par type

### Test de configuration
```bash
gemini "Confirme que tu fonctionnes. Donne ta version de modele et tes capacites."
```

### Configuration de projet
```bash
# Creer le GEMINI.md pour un projet Python
gemini "Genere un fichier GEMINI.md optimal pour un projet Python 3.13+
de monitoring systeme Linux avec GPUs NVIDIA."
```

## Effet sur le modele

- Le fichier GEMINI.md est lu automatiquement a chaque requete dans le repertoire — il remplace les Custom Instructions de ChatGPT
- Gemini CLI fonctionne en contexte terminal — il comprend les commandes systeme et peut interagir avec le filesystem
- Le contexte 1M tokens permet de charger des projets entiers
- Gemini est naturellement verbeux — le GEMINI.md doit contenir "reponses concises" pour eviter le bruit
