# Prompts Avancés Claude Code — Générés par le Cluster IA M1

> Ces prompts ont été générés par qwen3.5-9b sur le cluster JARVIS M1.



Voici 5 prompts avancés optimisés spécifiquement pour **Claude Code**, structurés en Markdown et prêts à être copiés-collés.

### 1. Audit Sécurité Complet (Security Hardening)

**Titre :** Analyse de Vulnérabilités et Hardening OWASP

**Contexte :**
Vous devez auditer un monorépertoire Python contenant une API REST exposée sur Internet. L'objectif est d'identifier les failles critiques avant le déploiement en production, conformément à l'OWASP Top 10.

**Prompt Complet :**
```markdown
# Rôle : Expert Pentester / Security Engineer Senior

# Tâche : Audit de Sécurité Offensif & Défensif sur une Base de Code Existante

## Instructions Détaillées :
1. **Analyse Statique (SAST) :** Scanne tous les fichiers Python, JSON et YAML à la recherche de failles courantes (ex: injection SQL, gestion d'API keys non sécurisée, dépendances vulnérables via `pip freeze` ou `poetry`).
2. **Revue des Entrées/Sorties :** Vérifie que chaque fonction traitant l'entrée utilisateur sanitize les données pour éviter le XSS et l'injection de commandes shell.
3. **Gestion des Secrets :** Identifie toute occurrence potentielle de secrets (tokens, clés API) dans le code ou les logs, même si masqués par `****`. Propose une stratégie d'utilisation de `.env` ou de gestionnaire de secrets.
4. **Plan de Correction :** Pour chaque vulnérabilité critique trouvée, propose un patch de code spécifique (ex: utiliser `paramiko` pour SSH, sanitiser les entrées avec `bleach`, etc.).

## Contrainte de Format