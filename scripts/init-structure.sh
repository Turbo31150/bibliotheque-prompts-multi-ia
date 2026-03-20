#!/usr/bin/env bash
set -euo pipefail

# Script d'initialisation de la bibliotheque de prompts Jarvis
# Usage : ./scripts/init-structure.sh [target_dir]
# Cree l'arborescence complete si elle n'existe pas deja

TARGET="${1:-.}"
cd "$TARGET"

TOOLS=(CLAUDE_CODE GEMINI_CLI GEMINI_APP CODEX_CLI CHATGPT PERPLEXITY BROWSER_OS JARVIS_CORE)

echo "=== Initialisation bibliotheque prompts Jarvis ==="

# Creer les dossiers
mkdir -p prompt scripts export
for tool in "${TOOLS[@]}"; do
    mkdir -p "prompt/${tool}"
    # Creer fichiers vides s'ils n'existent pas
    for f in system-prompts.md task-prompts.md; do
        [ -f "prompt/${tool}/${f}" ] || touch "prompt/${tool}/${f}"
    done
    echo "  [OK] prompt/${tool}/"
done

echo ""
echo "=== Structure creee ==="
echo ""
echo "Arborescence :"
find prompt -type f | sort
echo ""
echo "Prochaines etapes :"
echo "  1) Remplir les fichiers system-prompts.md et task-prompts.md"
echo "  2) git init && git add . && git commit -m 'Init prompt library'"
echo "  3) git remote add origin <url> && git push -u origin main"
