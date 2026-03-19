# Codex CLI — Configuration

## Description
Guide complet pour configurer et utiliser Codex CLI (OpenAI) : installation, configuration de la cle API, selection des modeles, modes d'operation et integration avec JARVIS.

## Configuration requise

### Prerequis
- Node.js 18+ ou installation standalone
- Cle API OpenAI active
- Terminal Linux/macOS

### Installation

```bash
# Installation via npm
npm install -g @openai/codex

# Variable d'environnement
export OPENAI_API_KEY="sk-..."

# Verification
codex --version
```

---

## Prompts par type de tache

### Creation — Configuration initiale

```
Tu es Codex CLI.
Projet : Jarvis Linux.
1) Comprends d'abord le contexte local avant toute modification.
2) Relie la tache a l'historique si utile.
3) Reste coherent avec l'existant et evite les reecritures inutiles.
4) Pour l'infra/Linux/SRE, structure : Goal/Plan/Code/Verify.
5) Pour un refactor, structure : Goal/Analysis/Changes/Tests.
6) Agis comme l'agent principal du terminal, execute, verifie et resume clairement.
```

**Usage** : Coller ce prompt au debut de chaque session Codex CLI pour etablir le contexte.

---

### Creation — Configuration des modes

```
Configure Codex CLI avec les 3 modes d'operation :

## MODE 1 — suggest (defaut)
- Codex propose des commandes sans les executer
- L'utilisateur valide avant execution
- Usage : exploration, apprentissage

## MODE 2 — auto-edit
- Codex peut modifier des fichiers sans confirmation
- Les commandes shell necessitent toujours validation
- Usage : refactoring, corrections rapides

## MODE 3 — full-auto
- Codex execute tout sans confirmation
- Usage : scripts automatises, CI/CD
- ATTENTION : utiliser avec precaution

## CONFIGURATION
codex --mode suggest          # Mode par defaut (safe)
codex --mode auto-edit        # Modifications fichiers auto
codex --mode full-auto        # Tout automatique (dangereux)

## MODELES
codex --model o4-mini         # Rapide et economique
codex --model o3              # Raisonnement avance
codex --model gpt-4.1         # Equilibre qualite/cout
```

---

### Amelioration / Refactoring — Personnaliser les instructions

```
Personnalise les instructions Codex CLI dans ~/.codex/instructions.md :

## CONTENU RECOMMANDE
# Instructions Codex CLI

## Langue
Reponds en francais. Code en anglais.

## Projet
Jarvis Linux — assistant IA integre dans Linux.
Stack : Python 3.13, uv, Claude Agent SDK, FastAPI, SQLite.

## Conventions
- Type hints obligatoires
- async/await pour I/O
- snake_case Python
- Tests dans tests/test_*.py
- Ne jamais modifier : src/config.py, src/tools.py, src/mcp_server.py

## Structure de reponse
Pour l'infra : Goal/Plan/Code/Verify
Pour le code : Goal/Analysis/Changes/Tests
```

---

### Debug — Codex CLI ne fonctionne pas

```
Codex CLI ne repond pas correctement.

## CHECKLIST
1. Installation OK ? (codex --version)
2. Cle API valide ? (echo $OPENAI_API_KEY)
3. Modele disponible ? (codex --model o4-mini "test")
4. Permissions du terminal ? (sandbox restrictions)
5. Reseau OK ? (curl api.openai.com)

## ERREURS COURANTES
| Erreur | Cause | Solution |
|--------|-------|----------|
| "API key invalid" | Cle expiree ou incorrecte | Regenerer sur platform.openai.com |
| "Model not found" | Modele non disponible | Utiliser o4-mini ou gpt-4.1 |
| "Permission denied" | Sandbox trop restrictif | Ajuster --mode ou les permissions |
| "Network error" | Pas d'acces internet | Verifier la connexion |
```

---

### Documentation — Reference des commandes

```
## Commandes Codex CLI

### Utilisation basique
codex "ta question ou instruction"

### Options principales
| Option | Description | Exemple |
|--------|-------------|---------|
| --model | Modele a utiliser | --model o4-mini |
| --mode | Mode d'operation | --mode auto-edit |
| --quiet | Sortie minimale | --quiet |
| --json | Sortie JSON | --json |

### Exemples
codex "explique ce fichier" src/main.py
codex "corrige le bug dans cette fonction"
codex "ajoute des tests pour ce module"
codex --model o3 "architecture pour un systeme de cache"
```

---

## Exemples concrets

### Exemple 1 : Demarrage de session
```bash
codex "Tu es Codex CLI. Projet : Jarvis Linux. Lis le CLAUDE.md et resume le contexte."
```

**Resultat attendu** : Resume du projet, stack, conventions, fichiers critiques.

### Exemple 2 : Audit systeme
```bash
codex "Inventorie tous les services systemd actifs et les ports ouverts sur cette machine"
```

**Resultat attendu** : Tableau des services avec leur status et des ports avec le processus associe.

### Exemple 3 : Generation de code
```bash
codex "Cree un script Python qui monitore les temperatures GPU et envoie une alerte Telegram si > 75C"
```

**Resultat attendu** : Script complet avec nvidia-smi parsing, seuils, et envoi Telegram.

---

## Effet sur le modele
- Le prompt de demarrage de session ancre le contexte pour toutes les interactions suivantes
- Le mode suggest (defaut) est le plus sur — toujours valider avant execution
- Le mode full-auto est utile pour les scripts automatises mais dangereux en interactif
- Les instructions dans ~/.codex/instructions.md sont chargees automatiquement
- Codex est optimise pour le terminal et les commandes shell — exploiter cette force
- Le modele o4-mini est suffisant pour 80% des taches, o3 pour les taches complexes
